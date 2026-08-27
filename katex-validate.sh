#!/usr/bin/env bash
# katex-validate.sh — Validate KaTeX math in markdown using real KaTeX inside a Docker container
# Usage: ./katex-validate.sh [input.md]   (reads stdin if no argument is given)
# Output: JSON with per-expression validation results (exit 1 if any error)
#
# On first run it builds the Docker image (node alpine + katex, tens of MB).
# Subsequent runs validate immediately.

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
IMAGE="katex-validate:latest"
DOCKERFILE="$SCRIPT_DIR/Dockerfile.katex"

# ── Build Docker image (first run only) ──
if ! docker image inspect "$IMAGE" &>/dev/null; then
    echo "🐳 Building Docker image... (node alpine + katex, tens of MB)" >&2
    docker build -t "$IMAGE" -f "$DOCKERFILE" "$SCRIPT_DIR"
    echo "✅ Build complete!" >&2
fi

# ── Validate: pipe the file (if given) or stdin into the container ──
if [ -n "$1" ] && [ -f "$1" ]; then
    cat "$1"
else
    cat
fi | docker run --rm -i "$IMAGE"
