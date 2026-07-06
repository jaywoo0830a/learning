#!/usr/bin/env bash
# md2pdf.sh — Pandoc + XeLaTeX로 Markdown → PDF 변환
# 사용법: ./md2pdf.sh <입력.md> [출력.pdf]
#
# 최초 실행 시 Docker 이미지 빌드 (texlive로 약 3~5분, 이미지 ~1.5GB).
# 이후 실행은 즉시 변환됩니다.

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
IMAGE="md2pdf:latest"
DOCKERFILE="$SCRIPT_DIR/Dockerfile.md2pdf"

# ── Docker 이미지 빌드 (최초 1회) ──
if ! docker image inspect "$IMAGE" &>/dev/null; then
    echo "🐳 Docker 이미지 빌드 중... (최초 1회만, texlive 설치로 약 3~5분)"
    docker build -t "$IMAGE" -f "$DOCKERFILE" "$SCRIPT_DIR"
    echo "✅ 빌드 완료!"
fi

# ── 인자 검증 ──
INPUT="$1"
OUTPUT="${2:-${INPUT%.md}.pdf}"

if [ -z "$INPUT" ]; then
    echo "사용법: ./md2pdf.sh <입력.md> [출력.pdf]"
    exit 1
fi
if [ ! -f "$INPUT" ]; then
    echo "❌ 오류: '$INPUT' 파일이 없습니다."
    exit 1
fi

# ── 변환 ──
ABS_INPUT=$(realpath "$INPUT")
WORKDIR=$(dirname "$ABS_INPUT")

echo "📄 변환 중: $INPUT → $OUTPUT"

docker run --rm \
    -v "$WORKDIR:/work" \
    "$IMAGE" \
    "$(basename "$ABS_INPUT")" \
    --pdf-engine=xelatex \
    -V documentclass=scrartcl \
    -V mainfont="Noto Sans CJK KR" \
    -V monofont="Noto Sans Mono CJK KR" \
    -V fontsize=12pt \
    -V linestretch=1.3 \
    -V geometry:margin=2.5cm \
    -V colorlinks=true \
    --include-in-header=/usr/local/share/header.tex \
    -o "$(basename "$OUTPUT")"

echo "✅ 완료: $WORKDIR/$(basename "$OUTPUT")"
