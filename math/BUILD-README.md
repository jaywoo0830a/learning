# Math visual rendering pipeline

그래프를 **커밋하지 않고**, 빌드 시 생성한 뒤 마크다운에 주입하는 구조.
커밋되는 마크다운은 **순수 텍스트 + KaTeX**만 유지한다.

## 구조

```
math/
├── viz/                  # 공통 렌더링 코어 (theme/canvas/primitives/export)
├── verify/               # 수치·기호·Z3 검증 계층
├── graphs/               # [git-ignored] 빌드 산출물 — 만지는 순간 재생성
├── build/rendered/       # [git-ignored] placeholder가 치환된 렌더링 md
├── tools/
│   ├── build.py          # 그래프 재생성 + md 렌더 (원본 md는 변경 안 함)
│   └── build_markdown.py # {{graph:<id>}} -> 상대경로 치환 레지스트리
├── scripts/graphs/       # 세션별 그래프 spec 빌더
├── sessions/phase*/...md # [커밋됨] 순수 텍스트 + KaTeX + {{graph:<id>}} placeholder
└── tests/                # 서술형 테스트만 (수치·기호 사실, 렌더 요소, 치환)
```

## 사용법 (Docker 컨테이너로 실행)

```bash
cd math

# 전체 테스트 (검증·프리미티브·빌드 치환)
make test

# 그래프 재생성 + md 렌더링 (원본 md는 건드리지 않음)
make build-md
# → graphs/ 에 PNG 생성, build/rendered/ 에 치환된 md 기록
```

## 마크다운 규칙

- **커밋되는 `.md`**: 이미지 참조는 반드시 `{{graph:<id>}}` placeholder 사용.
  예: `![Units of the derivative](./img/units.png)` ❌
      `![Units of the derivative]({{graph:14d-01-derivative-units}})` ✅
- **빌드 후**: `build/rendered/` 에서 placeholder가 `../../graphs/...png` 로 치환된다.
- 그래프 id는 `tools/build_markdown.py` 의 `_KNOWN`(레지스트리)에 등록한다.