# math — 그래프 렌더 + 마크다운 태그 치환
#
#   make install     logos 설치 (math/graph)                  최초 1회
#   make graph       그래프 렌더 → math/graphs/               도커 · 패키지 render.sh
#   make graph-host  그래프 렌더 (호스트 node · 빠른 확인)     도커 불필요
#   make build       그래프 렌더 + md 태그 치환 → math/build/rendered/
#   make strict      build + 미해결 태그 있으면 실패 (CI)
#   make serve       렌더 갤러리 서빙 (http://localhost:18080) 도커 · 패키지 serve.sh
#   make clean       산출물 삭제
#
# 렌더는 가이드(WORKFLOW.md ③)대로 **패키지에 함께 설치되는 scripts/render.sh** 를 쓴다:
#   bash graph/node_modules/@jaywoo0830a/logos/scripts/render.sh -p . -s graph -o graphs -r
# 항상 도커 컨테이너에서 돌기 때문에 Node·폰트·래스터라이저(resvg)가 이미지 안에서 해결되고
# 결과가 일정하다. 이미지 태그는 패키지 버전을 따른다(logos:0.4.1) — 없으면 최초 1회 자동 빌드.
# `make build`/`make strict`(md 태그 치환)는 호스트 node 를 쓴다.
#
# 태그 규약: 세션 md 안의 `![alt]({{graph:<id>}})`.

NODE  ?= node
LOGOS ?= graph/node_modules/@jaywoo0830a/logos/scripts

.PHONY: install graph graph-host build strict serve clean

install:
	cd graph && npm install

graph:
	cd graph && npm run render

graph-host:
	cd graph && npm run render:host

build: graph
	$(NODE) tools/build.mjs --no-render

strict: graph
	$(NODE) tools/build.mjs --no-render --strict

serve:
	bash $(LOGOS)/serve.sh graphs 18080

clean:
	rm -rf graphs build
