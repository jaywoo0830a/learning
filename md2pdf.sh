#!/usr/bin/env bash
# md2pdf.sh — Docker + 최신 Node.js로 Markdown → PDF 변환
# 사용법: ./md2pdf.sh <입력.md> [출력.pdf]
#
# 최초 실행 시 Docker 이미지를 빌드합니다 (약 1~2분 소요).
# 이후 실행은 즉시 변환됩니다.

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
IMAGE="md2pdf:latest"
DOCKERFILE="$SCRIPT_DIR/Dockerfile.md2pdf"

# ── Docker 이미지 빌드 (최초 1회) ──
if ! docker image inspect "$IMAGE" &>/dev/null; then
    echo "🐳 Docker 이미지 빌드 중... (최초 1회만, 약 1~2분)"
    docker build -t "$IMAGE" -f "$DOCKERFILE" "$SCRIPT_DIR"
    echo "✅ 빌드 완료!"
fi

# ── 인자 검증 ──
INPUT="$1"
OUTPUT="${2:-${INPUT%.md}.pdf}"

if [ -z "$INPUT" ]; then
    echo "사용법: ./md2pdf.sh <입력.md> [출력.pdf]"
    echo "예시:  ./md2pdf.sh math/sessions/phase2/07-polynomials-and-equations.md"
    exit 1
fi

if [ ! -f "$INPUT" ]; then
    echo "❌ 오류: '$INPUT' 파일이 없습니다."
    exit 1
fi

# ── 절대경로로 변환 ──
ABS_INPUT=$(realpath "$INPUT")
WORKDIR=$(dirname "$ABS_INPUT")
REL_INPUT=$(basename "$ABS_INPUT")
REL_OUTPUT=$(basename "$OUTPUT")

echo "📄 변환 중: $INPUT → $OUTPUT"

docker run --rm \
    --shm-size=256m \
    -v "$WORKDIR:/work" \
    "$IMAGE" \
    "$REL_INPUT" \
    "$REL_OUTPUT"

echo "✅ 완료: $WORKDIR/$REL_OUTPUT"
