#!/usr/bin/env bash
# math/tools/send-to-windows.sh — 빌드 산출물을 zip 으로 묶어 **WSL → Windows 바탕화면**으로 보낸다.
#
#   (리포 루트)  make -C math send
#   (math/)      make send                 # 또는  make send ARGS="--svg-only"
#   직접         bash math/tools/send-to-windows.sh [옵션]
#
# ── zip 안에 무엇이 들어가나 ─────────────────────────────────────────
#   graphs/**          렌더된 그림(SVG·PNG) + 갤러리 index.html + manifest.json
#   build/rendered/**  {{graph:…}} 태그가 `../../../../graphs/<id>.svg` 로 치환된 세션 md
#   README.txt         압축을 푼 사람을 위한 안내(폴더 구조를 그대로 두라고 알려 준다)
#
#   두 폴더는 **같은 루트에 있어야** md 의 상대경로(`../../../../graphs/…`)가 살아난다.
#   그래서 zip 안에도 둘을 나란히 넣는다 → 압축을 `math-figures/` 같은 새 폴더에 풀면
#   그 안에서 md 를 열었을 때 이미지가 그대로 보인다.
#
# ── 옵션 ─────────────────────────────────────────────────────────────
#   --no-build      빌드 생략(이미 만든 산출물만 압축)
#   --host          렌더를 호스트 CLI 로(도커 없이 · 빠른 확인)   *기본은 도커 render.sh
#   --no-md         build/rendered 제외(그림만)
#   --svg-only      PNG 제외(용량 축소 · 도커 렌더로 만든 PNG 를 zip 에서만 뺀다)
#   --no-readme     README.txt 제외
#   --name NAME     zip 파일명(기본 math-figures-YYYYmmdd-HHMM.zip)
#   --out DIR       zip 을 만들 로컬 폴더(기본 <math>/build/exports)
#   --dest DIR      보낼 윈도우 폴더(WSL 경로). 기본: 자동 감지(바탕화면)
#   --zip-tool T    auto|zip|python (기본 auto — zip 없으면 python3 로)
#   --open          복사 후 탐색기에서 그 파일을 선택 표시
#   -q, --quiet     진행 로그 최소
#   -h, --help      이 도움말
#
#   환경변수 WSL_DESKTOP 으로 목적지를 고정할 수도 있다(예: /mnt/c/Users/me/OneDrive/Desktop).
set -euo pipefail

MATH="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"   # math/
GRAPHS="$MATH/graphs"
RENDERED="$MATH/build/rendered"

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

usage() { sed -n '2,/^set -euo pipefail$/p' "${BASH_SOURCE[0]}" | sed '$d' | sed 's/^# \{0,1\}//'; }

# ── 인자 ─────────────────────────────────────────────────────────
BUILD=1; HOST=0; MD=1; PNG=1; README=1
NAME=''; OUTDIR="$MATH/build/exports"; DEST=''; ZIP_TOOL=auto; OPEN=0; QUIET=0
while (( $# )); do
  case "$1" in
    --no-build)  BUILD=0; shift ;;
    --host)      HOST=1; shift ;;
    --no-md)     MD=0; shift ;;
    --svg-only)  PNG=0; shift ;;
    --no-readme) README=0; shift ;;
    --name)      NAME="$2"; shift 2 ;;
    --out)       OUTDIR="$2"; shift 2 ;;
    --dest)      DEST="$2"; shift 2 ;;
    --zip-tool)  ZIP_TOOL="$2"; shift 2 ;;
    --open)      OPEN=1; shift ;;
    -q|--quiet)  QUIET=1; shift ;;
    -h|--help)   usage; exit 0 ;;
    *)           die "알 수 없는 옵션: $1  (--help)" ;;
  esac
done

# ── WSL · 윈도우 바탕화면 찾기 ────────────────────────────────────
is_wsl() { [[ -n "${WSL_DISTRO_NAME:-}" ]] || grep -qi microsoft /proc/version 2>/dev/null; }

# 윈도우 쪽 '진짜' 바탕화면 — OneDrive 리디렉션까지 반영된다.
#   ① WSL_DESKTOP 환경변수 ② 폴더 API(powershell) ③ %USERPROFILE% ④ /mnt/c/Users 스캔
detect_windows_desktop() {
  local win u base name d
  if [[ -n "${WSL_DESKTOP:-}" ]]; then printf '%s\n' "$WSL_DESKTOP"; return 0; fi
  if command -v powershell.exe >/dev/null 2>&1; then
    win="$(powershell.exe -NoProfile -NonInteractive -Command \
            "[Environment]::GetFolderPath('Desktop')" 2>/dev/null | tr -d '\r' | tail -n1)" || win=''
    if [[ -n "$win" ]] && u="$(wslpath -u "$win" 2>/dev/null)" && [[ -d "$u" ]]; then
      printf '%s\n' "$u"; return 0
    fi
  fi
  if command -v cmd.exe >/dev/null 2>&1; then
    win="$(cmd.exe /c 'echo %USERPROFILE%' 2>/dev/null | tr -d '\r' | tail -n1)" || win=''
    if [[ -n "$win" && "$win" != *'%USERPROFILE%'* ]] \
       && u="$(wslpath -u "$win" 2>/dev/null)" && [[ -d "$u/Desktop" ]]; then
      printf '%s\n' "$u/Desktop"; return 0
    fi
  fi
  for base in /mnt/c/Users/*; do
    [[ -d "$base" ]] || continue
    name="$(basename -- "$base")"
    case "$name" in Default|'Default User'|Public|'All Users'|TEMP) continue ;; esac
    for d in "$base/Desktop" "$base"/OneDrive/Desktop "$base"/OneDrive\ -\ */Desktop; do
      [[ -d "$d" ]] && { printf '%s\n' "$d"; return 0; }
    done
  done
  return 1
}

if [[ -z "$DEST" ]]; then
  is_wsl || die "WSL 이 아닙니다 — 보낼 폴더를 --dest DIR 로 지정하세요."
  DEST="$(detect_windows_desktop)" \
    || die "윈도우 바탕화면을 찾지 못했습니다. --dest DIR 로 지정하세요(예: --dest /mnt/c/Users/me/Desktop)."
fi
# --dest 에 윈도우 표기(C:\Users\me\Desktop)를 줘도 되도록 WSL 경로로 바꿔 준다.
if [[ "$DEST" =~ ^[A-Za-z]:[\\/] ]]; then DEST="$(wslpath -u "$DEST")"; fi
[[ -d "$DEST" ]] || die "보낼 폴더가 없습니다: $DEST"

# ── 조용히(--quiet) 모드용 로그/정리 ─────────────────────────────
RUN_LOG="$(mktemp)"; STAGE=''
cleanup() { [[ -n "${STAGE:-}" ]] && rm -rf "$STAGE"; rm -f "$RUN_LOG"; }
trap cleanup EXIT

run() {   # 조용히 모드면 파일로, 실패하면 마지막 30줄만 보여 준다
  if (( QUIET )); then
    "$@" >>"$RUN_LOG" 2>&1 || { tail -n 30 "$RUN_LOG" >&2; return 1; }
  else
    "$@"
  fi
}
MAKE_BIN="${MAKE:-make}"

# ── ① 빌드 (렌더 + md 태그 치환) ─────────────────────────────────
if (( BUILD )); then
  step "[1/4] 빌드"
  if (( HOST )); then
    dim "  호스트 CLI 렌더(make graph-host) + 태그 치환"
    run "$MAKE_BIN" -C "$MATH" graph-host || die "렌더 실패"
    run node "$MATH/tools/build.mjs" --no-render || die "태그 치환 실패"
  else
    dim "  도커 렌더(패키지 render.sh) + 태그 치환"
    run "$MAKE_BIN" -C "$MATH" build || die "빌드 실패"
  fi
else
  step "[1/4] 빌드 생략 (--no-build)"
fi

# ── ② zip 준비 — 그림과 치환된 md 를 '같은 루트'에 모은다 ─────────
#   md 의 이미지 경로가 ../../../../graphs/<id>.svg 이므로 둘이 나란히 있어야 살아난다.
step "[2/4] zip 준비"
[[ -f "$GRAPHS/manifest.json" ]] \
  || die "렌더 산출물이 없습니다: $GRAPHS/manifest.json — 먼저 'make -C math graph' 를 실행하세요."
STAGE="$(mktemp -d)"
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

if command -v unzip >/dev/null 2>&1; then
  unzip -qq -t "$ZIP" >/dev/null || die "zip 무결성 검사 실패: $ZIP"
  ENTRIES="$(unzip -l "$ZIP" | awk '$2 ~ /-/ { n++ } END { print n + 0 }')"
else
  ENTRIES="$(python3 -c 'import sys, zipfile; print(len(zipfile.ZipFile(sys.argv[1]).namelist()))' "$ZIP")"
fi
SIZE="$(du -h "$ZIP" | cut -f1)"

# ── ③ 윈도우 바탕화면으로 복사 ───────────────────────────────────
step "[3/4] 윈도우로 복사"
cp -f "$ZIP" "$DEST/" || die "복사 실패: $DEST (경로·권한 확인)"
WIN_PATH="$(wslpath -w "$DEST/$NAME" 2>/dev/null || printf '%s/%s' "$DEST" "$NAME")"

# ── ④ 결과 ──────────────────────────────────────────────────────
step "[4/4] 결과"
log "  로컬 zip : $ZIP"
log "  내용     : 항목 ${ENTRIES}개 · SVG ${SVG_N} · PNG ${PNG_N} · md ${MD_N} · ${SIZE}"
ok "바탕화면 : $WIN_PATH"
dim "  (같은 zip 을 로컬에도 남겨 둡니다 — 재전송·CI 용)"

if (( OPEN )); then
  command -v explorer.exe >/dev/null 2>&1 && { explorer.exe /select,"$WIN_PATH" >/dev/null 2>&1 || true; }
fi
