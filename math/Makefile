# math — 그래프 렌더 + 마크다운 태그 치환
#
#   make install     logos 설치 (math/graph) — 도커 node 컨테이너에서 npm install
#   make graph       그래프 렌더 → math/graphs/               도커 · 패키지 render.sh
#   make graph-host  그래프 렌더 (호스트 node · 빠른 확인)     도커 불필요
#   make build       그래프 렌더 + md 태그 치환 → math/build/rendered/
#   make strict      build + 미해결 태그 있으면 실패 (CI)
#   make serve       렌더 갤러리 서빙 (http://localhost:18080) 도커 · 패키지 serve.sh
#   make serve-host  빌드산출(zip: graphs + build/rendered) 임시 HTTP 서버 → SSH 터널 다운로드
#                    옵션: make serve-host ARGS="--no-build --svg-only --port 18081"
#   make send        빌드 + zip → 윈도우 바탕화면 (WSL)      옵션: make send ARGS="--svg-only"
#   make clean       산출물 삭제
#
# ── 도커 우선: 로컬 npm · node 불필요 ──────────────────────────────
#   기본값은 모든 node/npm 작업을 **도커 컨테이너 안에서** 돌린다.
#     install        → node 이미지에서 npm install
#     build / strict → node 이미지에서 tools/build.mjs 실행
#     graph          → 패키지 render.sh (내부에서 도커로 렌더)
#   로컬에 node/npm 이 이미 있으면 *-host 타깃으로 도커 없이 빠르게 돌릴 수 있다.
#     make install-host / graph-host / build-host / strict-host
#
# ── 이미지 ────────────────────────────────────────────────────────
#   NODE_IMAGE : npm install·build.mjs 를 돌릴 node 이미지 (기본 node:24-bookworm).
#                npm install 은 github 의존성(git)을 받으므로 git 이 포함된 이미지여야 한다.
#                build/strict 만 쓸 거면 더 가벼운 node:24-alpine 도 된다.
#   렌더 이미지(logos:<버전>)는 패키지 render.sh 가 없으면 최초 1회 자동 빌드한다.
#
# 태그 규약: 세션 md 안의 `![alt]({{graph:<id>}})`.

DOCKER     ?= docker
NODE_IMAGE ?= node:24-bookworm
NPM        ?= npm
NODE       ?= node
LOGOS      ?= graph/node_modules/@jaywoo0830a/logos/scripts
RENDER_SH  := $(LOGOS)/render.sh

# 컨테이너를 호스트와 같은 uid/gid 로 실행 → 생성물(node_modules·build)이 root 소유가 되지 않게.
#   HOME·npm 캐시는 컨테이너 안 쓰기 가능한 /tmp 로 돌린다.
DOCKER_USER := $(shell id -u 2>/dev/null || echo 0):$(shell id -g 2>/dev/null || echo 0)
DOCKER_BASE := $(DOCKER) run --rm -v "$(CURDIR):/work" -e HOME=/tmp -e npm_config_cache=/tmp/.npm -u "$(DOCKER_USER)"

.PHONY: install install-host graph graph-host build build-host strict strict-host \
        serve serve-host send clean require-docker

# ── 도커 확인 (도커 기반 타깃의 공통 전제) ─────────────────────────
require-docker:
	@command -v $(DOCKER) >/dev/null 2>&1 || { \
	  echo "✗ docker 가 필요합니다 — 설치 후 다시 실행하거나 *-host 타깃을 쓰세요."; exit 1; }
	@$(DOCKER) info >/dev/null 2>&1 || { \
	  echo "✗ 도커 데몬이 실행 중이 아닙니다(docker info 실패)."; exit 1; }

# ── 패키지 설치 (도커 node 로 npm install) ─────────────────────────
install: require-docker
	@echo "▶ npm install — 도커 $(NODE_IMAGE) → graph/node_modules"
	$(DOCKER_BASE) -w /work/graph $(NODE_IMAGE) $(NPM) install

install-host:
	cd graph && $(NPM) install

# ── 렌더 (패키지 render.sh · 내부에서 도커 실행) ───────────────────
graph:
	@test -f "$(RENDER_SH)" || { \
	  echo "✗ $(RENDER_SH) 이 없습니다 — 먼저 'make install' 을 실행하세요."; exit 1; }
	bash "$(RENDER_SH)" -p . -s graph -o graphs -r --clean

graph-host:
	cd graph && $(NPM) run render:host

# ── 빌드 (렌더 + md 태그 치환, 도커 node) ──────────────────────────
build: graph require-docker
	$(DOCKER_BASE) -w /work $(NODE_IMAGE) $(NODE) tools/build.mjs --no-render

build-host: graph-host
	$(NODE) tools/build.mjs --no-render

strict: graph require-docker
	$(DOCKER_BASE) -w /work $(NODE_IMAGE) $(NODE) tools/build.mjs --no-render --strict

strict-host: graph-host
	$(NODE) tools/build.mjs --no-render --strict

# ── 서빙 · 전송 · 정리 ────────────────────────────────────────────
serve:
	bash "$(LOGOS)/serve.sh" graphs 18080

serve-host:
	bash tools/serve-to-host.sh $(ARGS)

send:
	bash tools/send-to-windows.sh $(ARGS)

clean:
	rm -rf graphs build
