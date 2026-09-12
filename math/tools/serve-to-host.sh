#!/usr/bin/env bash
# math/tools/serve-to-host.sh — 빌드 산출물을 zip 으로 묶어 **임시 HTTP 서버**로 띄워
# 호스트(로컬)가 curl/브라우저로 받아가도록 한다. (서버 → 호스트 전송 · 자격증명 불필요)
#
#   (math/)      bash tools/serve-to-host.sh [옵션]
#   직접         bash math/tools/serve-to-host.sh [옵션]
#
#  ── 대략 동작 ─────────────────────────────────────────────────────
#   ① 빌드   렌더(로고스 도커) + md 태그 치환(node 도커)  → math/graphs, math/build/rendered
#            (이미 있으면 --no-build 로 생략, 렌더만 --no-md ...)
#   ② zip    graphs/** + build/rendered/** 를 '같은 루트'에 모아 압축
#            (md 의 상대경로 ../../../../graphs/<id>.svg 가 살아나도록 두 폴더를 나란히 넣는다)
#   ③ 서빙   math/build/exports 에 임시 HTTP 서버를 띄워 zip 다운로드 URL 을 출력
#
#  ── 호스트가 받는 두 가지 방법 ─────────────────────────────────────
#   A. SSH 터널 (기본 bind=127.0.0.1 · 안전 · 방화벽 무관)
#      호스트 터미널에서 아래 터널을 연 뒤
#        ssh -N -L <port>:127.0.0.1:<port> <user>@<server>
#      같은 터널(또는 다른 터미널)에서 받는다
#        curl -fO http://127.0.0.1:<port>/<zip>
#   B. 직접 접근 (--bind 0.0.0.0 · 서버 방화벽/보안그룹에서 해당 포트 허용 필요)
#        curl -fO http://<server-ip>:<port>/<zip>
#
# ── 옵션 ─────────────────────────────────────────────────────────
#   --no-build      빌드 생략(이미 만든 산출물만 압축·서빙)
#   --host          렌더·태그치환을 호스트 CLI 로(도커 없이 · node 필요)   *기본은 도커
#   --no-md         build/rendered 제외(그림만)
#   --svg-only      PNG 제외(용량 축소)
#   --no-readme     README.txt 제외
#   --name NAME     zip 파일명(기본 math-figures-YYYYmmdd-HHMM.zip)
#   --out DIR       zip 을 만들·서빙할 폴더(기본 <math>/build/exports)
#   --zip-tool T    auto|zip|python (기본 auto — zip 없으면 python3 로)
#   --port N        HTTP 서버 포트 (기본 18081)
#   --bind ADDR     바인딩 주소 (기본 127.0.0.1 · 전역 노출은 0.0.0.0)
#   --public-ip IP  안내용 서버 공개 IP를 직접 지정(자동 감지 실패 시)
#   -q, --quiet     진행 로그 최소(서버 요청 로그는 /tmp 로 격리)
#   -h, --help      이 도움말
set -euo pipefail

MATH="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"   # math/
GRAPHS="$MATH/graphs"
RENDERED="$MATH/build/rendered"
MAKE_BIN="$(command -v make || echo make)"

# ── 로그 ─────────────────────────────────────────────────────────
if [[ -t 1 && -z "${NO_COLOR:-}" ]]; then
  C_DIM=$'\033[2m'; C_RED=$'\033[31m'; C_GREEN=$'\033[32m'; C_BOLD=$'\033[1m'; C_OFF=$'\033[0m'
else
  C_DIM=''; C_RED=''; C_GREEN=''; C_BOLD=''; C_OFF=''
fi
log()  { printf '%s\n' "$*"; }
dim()  { printf '%s%s%s\n' "$C_DIM" "$*" "$C_OFF"; }
ok()   { printf '%s %s\n' "${C_GREEN}✓${C_OFF}" "$*"; }
step() { printf '\n%s\n' "${C_BOLD}$*${C_OFF}"; }
die()  { printf '%s %s\n' "${C_RED}✗${C_OFF}" "$*" >&2; exit 1; }
run()  { dim "  \$ $*"; "$@"; }

usage() { sed -n '2,/^set -euo pipefail$/p' "${BASH_SOURCE[0]}" | sed '$d' | sed 's/^# \{0,1\}//'; }

require_docker() {
  if ! docker info >/dev/null 2>&1; then
    die "도커가 실행 중이지 않습니다(docker info 실패). 렌더는 도커로 돌아갑니다."
  fi
}

# ── 인자 ─────────────────────────────────────────────────────────
BUILD=1; HOST=0; MD=1; PNG=1; README=1
NAME=''; OUTDIR="$MATH/build/exports"; ZIP_TOOL=auto; QUIET=0
PORT=18081; BIND=127.0.0.1; PUBLIC_IP=''
while (( $# )); do
  case "$1" in
    --no-build)  BUILD=0; shift ;;
    --host)      HOST=1; shift ;;
    --no-md)     MD=0; shift ;;
    --svg-only)  PNG=0; shift ;;
    --no-readme) README=0; shift ;;
    --name)      NAME="$2"; shift 2 ;;
    --out)       OUTDIR="$2"; shift 2 ;;
    --zip-tool)  ZIP_TOOL="$2"; shift 2 ;;
    --port)      PORT="$2"; shift 2 ;;
    --bind)      BIND="$2"; shift 2 ;;
    --public-ip) PUBLIC_IP="$2"; shift 2 ;;
    -q|--quiet)  QUIET=1; shift ;;
    -h|--help)   usage; exit 0 ;;
    *)           die "알 수 없는 옵션: $1  (--help)" ;;
  esac
done
# ── ① 빌드 (렌더 + md 태그 치환) ─────────────────────────────────
step "[1/4] 빌드"
if (( BUILD )); then
  if (( HOST )); then
    dim "  호스트 CLI 렌더(make graph-host) + 태그 치환 (node 필요)"
    command -v node >/dev/null 2>&1 || die "호스트에 node 가 없습니다: 'sudo apt install nodejs npm' 후 다시, 또는 옵션 생략(도커)."
    run "$MAKE_BIN" -C "$MATH" graph-host || die "렌더 실패"
    run node "$MATH/tools/build.mjs" --no-render || die "태그 치환 실패"
  else
    require_docker
    dim "  도커 렌더(logos:0.4.1) + 태그 치환(node:24-alpine)"
    docker run --rm -u "$(id -u):$(id -g)" -e HOME=/tmp -e npm_config_cache=/tmp/npm-cache \
      -v "$MATH":/work -w /work --entrypoint sh logos:0.4.1 -c '
        set -e
        mkdir -p node_modules/@jaywoo0830a
        ln -sfn /opt/logos node_modules/@jaywoo0830a/logos
        node /opt/logos/bin/logos.mjs "$@"
        rc=$?
        set +e
        rm -f node_modules/@jaywoo0830a/logos
        rmdir node_modules/@jaywoo0830a 2>/dev/null; rmdir node_modules 2>/dev/null
        exit $rc
      ' sh render graph --out /work/graphs --recursive --clean || die "도커 렌더 실패"
    docker run --rm -u "$(id -u):$(id -g)" -e HOME=/tmp -v "$MATH":/work -w /work \
      --entrypoint node node:24-alpine tools/build.mjs --no-render || die "태그 치환 실패"
  fi
else
  dim "  빌드 생략 (--no-build)"
fi

# ── ② zip 준비 — 그림과 치환된 md 를 '같은 루트'에 모은다 ─────────
#   md 의 이미지 경로가 ../../../../graphs/<id>.svg 이므로 둘이 나란히 있어야 살아난다.
step "[2/4] zip 준비"
[[ -f "$GRAPHS/manifest.json" ]] \
  || die "렌더 산출물이 없습니다: $GRAPHS/manifest.json — 먼저 빌드하거나 'make -C math graph' 를 실행하세요."
STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT
cp -a "$GRAPHS/." "$STAGE/graphs/"
if (( ! PNG )); then find "$STAGE/graphs" -type f -name '*.png' -delete; fi
if (( MD )); then
  [[ -d "$RENDERED" ]] \
    || die "치환된 md 가 없습니다: $RENDERED — 'make -C math build' 로 만드세요(또는 --no-md)."
  mkdir -p "$STAGE/build"
  cp -a "$RENDERED" "$STAGE/build/rendered"
fi

SVG_N="$(find "$STAGE" -type f -name '*.svg' | wc -l)"
PNG_N="$(find "$STAGE" -type f -name '*.png' | wc -l)"
MD_N="$(find "$STAGE" -type f -name '*.md' | wc -l)"
if (( README )); then
  {
    echo "math-figures — @jaywoo0830a/logos 로 렌더한 수학 그림 모음"
    echo
    echo "graphs/           SVG·PNG 그림 + 갤러리(index.html). index.html 을 브라우저로 열면 한 번에 훑어봅니다."
    echo "build/rendered/   {{graph:…}} 태그를 그림 경로로 바꾼 세션 마크다운."
    echo "                  각 md 의 이미지 경로(../../../../graphs/<id>.svg)가 살아 있으려면 두 폴더가"
    echo "                  나란히 있어야 합니다 — 구조를 그대로 두고 압축을 푸세요."
    echo "                  (아직 그림이 없는 세션은 그 줄이 {{graph:…}} 그대로 남습니다 — 'make strict' 로 확인)"
    echo
    echo "생성 $(date '+%Y-%m-%d %H:%M') · SVG ${SVG_N}장 · PNG ${PNG_N}장 · md ${MD_N}개"
  } >"$STAGE/README.txt"
fi

OUTDIR="$(mkdir -p "$OUTDIR" && cd "$OUTDIR" && pwd)"
[[ -n "$NAME" ]] || NAME="math-figures-$(date +%Y%m%d-%H%M).zip"
ZIP="$OUTDIR/$NAME"
rm -f "$ZIP"

if [[ "$ZIP_TOOL" = auto ]]; then
  if command -v zip >/dev/null 2>&1; then ZIP_TOOL=zip; else ZIP_TOOL=python; fi
fi
case "$ZIP_TOOL" in
  zip)    (cd "$STAGE" && zip -qr "$ZIP" .) || die "zip 실패: $ZIP" ;;
  python) command -v python3 >/dev/null 2>&1 \
            || die "zip 도 python3 도 없습니다 — 'sudo apt install zip' 후 다시 실행하세요."
          (cd "$STAGE" && python3 -c 'import shutil,sys; shutil.make_archive(sys.argv[1], "zip", ".")' "${ZIP%.zip}") \
            || die "python zip 실패: $ZIP" ;;
  *)      die "알 수 없는 --zip-tool: $ZIP_TOOL (auto|zip|python)" ;;
esac

ENTRIES="$(python3 -c 'import sys, zipfile; print(len(zipfile.ZipFile(sys.argv[1]).namelist()))' "$ZIP")"
SIZE="$(du -h "$ZIP" | cut -f1)"
ok "zip 완료: $ZIP  (항목 ${ENTRIES}개 · SVG ${SVG_N} · PNG ${PNG_N} · md ${MD_N} · ${SIZE})"
# ── ③ 목적지 URL 계산 ────────────────────────────────────────────
#   bind 가 로컬이면 SSH 터널로, 전역이면 서버 공개 IP 로 안내한다.
server_ip() {
  if [[ -n "$PUBLIC_IP" ]]; then printf '%s\n' "$PUBLIC_IP"; return 0; fi
  local t
  t="$(awk '{print $3}' <<<"${SSH_CONNECTION:-}" 2>/dev/null)"          # 서버 IP (클라이언트가 본 주소)
  [[ -n "$t" ]] && { printf '%s\n' "$t"; return 0; }
  t="$(hostname -I 2>/dev/null | tr ' ' '\n' | \
        grep -vE '^(127\.|10\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.|fd[0-9a-f]{2}:|fe80:)' | head -1)"
  [[ -n "$t" ]] && printf '%s\n' "$t" || printf '%s\n' SERVER_IP
}
SERVER_IP="$(server_ip)"
HOST_USER="${SUDO_USER:-${USER:-user}}"
is_loopback_bind() { [[ "$BIND" = 127.0.0.1 || "$BIND" = ::1 || "$BIND" = localhost ]]; }

step "[3/4] HTTP 서버"
command -v python3 >/dev/null 2>&1 || die "python3 가 필요합니다 — 'sudo apt install python3' 후 다시 실행하세요."
if is_loopback_bind; then
  ACCESS_URL="http://127.0.0.1:$PORT/$NAME"
  dim "  바인딩: $BIND (로컬 전용) — 호스트는 SSH 터널로 받으세요."
else
  ACCESS_URL="http://$SERVER_IP:$PORT/$NAME"
  dim "  바인딩: $BIND — 서버 공개 IP 로 직접 받으세요. (방화벽에서 포트 $PORT 허용 필요)"
fi

echo
log "  ── 호스트에서 받기 ─────────────────────────────────────────"
if is_loopback_bind; then
  log "  [1/2] 터널 열기 (호스트 터미널)"
  log "        ssh -N -L $PORT:127.0.0.1:$PORT $HOST_USER@$SERVER_IP"
  log "  [2/2] 받기"
else
  log "   받기 (방화벽에서 $PORT 허용 필요)"
fi
log "        curl -fO $ACCESS_URL"
log "  또는 브라우저로 ${C_DIM}${ACCESS_URL}${C_OFF} 열기"
log "  ───────────────────────────────────────────────────────────"
echo
log "  서버 zip : $ZIP"
log "  정지     : Ctrl-C (서버 종료 · zip 은 그대로 남습니다)"
echo

# ── ④ 서빙 (앞으로 대기 · Ctrl-C 로 종료) ─────────────────────────
#   python http.server → 호스트 다운로드를 받는 동안 계속 돈다.
cd "$OUTDIR"
if (( QUIET )); then
  exec python3 -m http.server "$PORT" --bind "$BIND" 2>>"$MATH/build/.serve-to-host.$$.log"
else
  exec python3 -m http.server "$PORT" --bind "$BIND"
fi
[[ "$PORT" =~ ^[0-9]+$ ]] || die "--port 는 숫자여야 합니다: $PORT"