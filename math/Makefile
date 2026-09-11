# math — 그래프 렌더 + 마크다운 태그 치환
#
#   make install   logos 설치 (math/graph)             최초 1회
#   make graph     그래프만 렌더 → math/graphs/
#   make build     그래프 렌더 + md 태그 치환 → math/build/rendered/
#   make strict    build + 미해결 태그 있으면 실패 (CI)
#   make serve     렌더 갤러리 서빙 (http://localhost:18080)
#
# 태그 규약: 세션 md 안의 `![alt]({{graph:<id>}})`.

NODE ?= node

.PHONY: install graph build strict serve clean

install:
	cd graph && npm install

graph:
	cd graph && npm run render

build:
	$(NODE) tools/build.mjs

strict:
	$(NODE) tools/build.mjs --strict

serve:
	cd graph && npx logos serve ../graphs 18080

clean:
	rm -rf graphs build