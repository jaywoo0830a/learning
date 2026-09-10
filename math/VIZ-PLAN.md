# 시각화 리팩터링 계획 — 공통 라이브러리 · 검증 계층 · 네이밍 재정의

> 상태: 계획 단계. 코드 수정 없음.
> 목적: `math/sessions` 아래 난립한 그래프 생성 코드를 **공통 렌더링 라이브러리 + 선언적 spec + 검증 계층 + 일관된 네이밍**으로 재편한다.

---

## 1. 문제 진단 (현황 근거)

| 문제 | 관찰 | 근거 |
|---|---|---|
| 스크립트 난립·독립 | 그래프 생성 `.py` 61개가 각자 복사·중복 작성됨 | `find sessions -name '*.py'` = 61 |
| 렌더링 가림/깨짐 | z-order·레이아웃·tight_layout·equal-aspect가 스크립트마다 제각각 | 각 스크립트에 하드코딩, 공통 규약 없음 |
| 공통 코드 중복 | `plt.rcParams` 블록 47곳, 색상 팔레트 16곳 중복 | `grep -rl 'figure.dpi'` = 47, `grep -rl "BLUE = '#1a73e8'"` = 16 |
| 수치 검증 부재 | 테스트 코드 0개, sympy/Z3 미설치 | `grep -rli 'z3\|sympy\|pytest'` 결과 없음, `import sympy` 실패 |
| 폴더 관례 난립 | `graphs/`, `graphs/0715`, `0720`, `0721`, `0728`, `0808`, `0812`, `0821`, `solutions/graphs/` 등 3+ 관례 혼재 | 디렉터리 목록 |
| 파일명 관례 난립 | `01a-connectives.png`, `14d1a-1-circle-trade.png`, `9a-fold-absolute-value.png`, `sol09-ex2-rational.png`, `a11-z3-minus1.png` | 파일 목록 |
| 라이브러리 한정 | numpy + matplotlib만 사용 | import 집계 |

**근본 원인**: 세션을 새로 쓸 때마다 생성 스크립트를 "복사해서 새로 씀" → 렌더링 규약·색상·레이아웃·네이밍이 분산되어 요소 가림/깨짐과 수치 오류가 반복.

---

## 2. 목표 아키텍처

**핵심 아이디어: 렌더링(공통 라이브러리) ↔ 데이터(세션별 spec) ↔ 검증(테스트) 3계층 분리.**

스크립트가 그래프를 직접 그리지 않고 **선언적 spec**(데이터+의도)을 만들면, 공통 렌더러가 일관성·레이아웃·z-order·수치 검증을 단일 지점에서 책임진다.

```
math/
├── viz/                          ← 공통 렌더링 라이브러리 (신설, 전 세션 공유)
│   ├── __init__.py
│   ├── theme.py                  ← 색상·rcParams·폰트·DPI 단일 정의
│   ├── canvas.py                 ← Figure/axes 생성, 레이아웃·가림방지(z-order, tight_layout, equal-aspect)
│   ├── primitives/
│   │   ├── diagram.py            ← 화살표·박스·벤·진리표 개략도
│   │   ├── curves.py             ← 2D 곡선·접선·채움·주석
│   │   ├── surfaces.py           ← 3D 표면·레벨셋·벡터장
│   │   ├── vectorfield.py        ← 위상평면·slope field
│   │   └── annotate.py           ← 일관된 콜아웃/레이블/범례
│   └── export.py                 ← 저장 경로·DPI·포맷(png/svg/pdf) 일원화
│
├── verify/                       ← 수치·기호 검증 계층 (신설)
│   ├── __init__.py
│   ├── symbolic.py               ← sympy 기호 검증 헬퍼
│   ├── numeric.py                ← numpy 수치 오차 검증
│   └── z3logics.py               ← Z3 로직/불대수/기하 제약 검증
│
├── sessions/
│   ├── phase1/
│   │   ├── 01-....md
│   │   └── specs/                ← 세션별 선언적 그래프 정의 (신설)
│   └── phase2/
│       └── ...
│
└── tests/                        ← pytest 테스트 (신설)
    ├── conftest.py
    └── test_*.py                 ← 각 그래프 = "검증 가능한 수학적 사실"
```

---

## 3. 핵심 설계 결정

### 3-1. 선언적 Spec → 렌더러 분리

각 세션은 그래프를 직접 그리지 않고 데이터+의도만 기술한다.

```python
# sessions/phase2/14D1A/specs.py  (예시, 구현 아님)
from viz import FigureSpec, Curve, Tangent, Point, Callout

spec = FigureSpec(
    id="14D1A-01",                 # 새 네이밍 규칙의 안정 키
    title="circle trade",
    curves=[
        Curve(param_x=lambda t: 5*cos(t), param_y=lambda t: 5*sin(t), role="relation"),
        Tangent(at=Point(3,4), slope=-3/4, role="local"),
    ],
    callouts=[Callout(target=Point(3,4), text=r"dy/dx=-x/y=-3/4")],
    checks={                       # 렌더링과 동시에 검증되는 사실
        "tangent_slope_at_3_4": lambda: abs((-3/4) - (-3/4)) < 1e-9,
    },
)
```

- 가림/깨짐은 렌더러가 **단일 지점**에서 해결(z-order 정책, tight_layout, equal-aspect, 콜아웃 자동 회피).
- 세션별 반복 로직이 사라져 유지보수·확장이 쉬워진다.

### 3-2. 검증 계층 (신뢰성)

| 도구 | 검증 대상 | 예시 |
|---|---|---|
| sympy | 기호적 사실 | 접선 기울기 `-x/y`가 `(3,4)`에서 `-3/4`임을 `diff`로 증명 |
| Z3 | 로직·불대수·제약 | 진리표 동치(Phase 1), SMT 부등식 영역, 기하 충돌 |
| pytest | 통합 수집 | 각 spec의 `checks`를 테스트로 수집, `pytest tests/`로 일괄 검증 |

**원칙: 그림이 곧 테스트.** spec의 `checks`를 pytest가 수집해 CI 가능하게 한다.

### 3-3. 네이밍 규칙 (단일 스킴)

```
<sessionscope>/<session_id>/<graph_id>-<slug>.png
예) sessions/phase2/14D1A/14d1a-01-circle-trade.png
```

| 요소 | 규칙 | 예시 |
|---|---|---|
| `session_id` | TOPICS.md 공식 번호+구분자의 소문자 슬러그 | `14D1A` → `14d1a` |
| `graph_id` | 세션 내 **0부터 정렬 가능한 두 자리 서수** | `01`, `02` |
| `slug` | 하이픈 연결된 짧은 설명 | `circle-trade` |
| 폴더 | 날짜 폴더 폐기 → 세션 ID 폴더로 | `graphs/0821/14D1A` → `sessions/phase2/14D1A/` |
| 해설 그림 | `solutions/<session_id>/` 하위로 구분 | `solutions/12A1/` |

- **정렬 가능**: 서수 2자리로 파일 목록이 읽기 순서를 보장.
- **추적 가능**: 세션 ID가 곧 소스·결과의 매핑 키.
- **확장 가능**: 새 세션은 폴더 하나만 추가.

### 3-4. 확장·유연성 원칙

- **렌더러 교체 가능**: spec은 matplotlib에 결합하지 않고 `viz/canvas.py`의 백엔드 추상화 위에 얹음 → Plotly/Manim 전환 여지.
- **프리미티브 조합**: 새 세션은 기존 `primitives/*`를 임포트해 조합하거나 새 프리미티브 하나만 추가. 스크립트 복사가 아닌 **임포트**로 확장.
- **점진 이관**: 61개 기존 스크립트를 한 번에 재작성하지 않고, 코어 구축 → Phase 1 파일럿 → 순차 이관.

---

## 4. 실행 로드맵

| 단계 | 작업 | 산출물 | 리스크 |
|---|---|---|---|
| 0 | `sympy`, `z3-solver`, `pytest` 설치 | 환경 준비 | 낮음 |
| 1 | `viz/theme.py` + `canvas.py` + `export.py` 작성, 색상·레이아웃·z-order 단일화 | 공통 렌더 코어 | 낮음 |
| 2 | `viz/primitives/` 초기 4-5개(곡선·접선·콜아웃·개략도·3D) 추출 | 재사용 객체 | 중간 |
| 3 | `verify/` (sympy/numeric/z3logics) 작성 | 검증 헬퍼 | 중간 |
| 4 | 네이밍 규칙 확정 + 기존 PNG 폴더 정리 스크립트 | 일관 폴더 구조 | 중간 |
| 5 | Phase 1(6세션, 진리표/벤/개략도 중심)을 spec 방식으로 이관 + pytest | 파일럿 검증 | 중간 |
| 6 | Phase 2 대표 세션(13A·14D1A 등) 이관해 가림/깨짐 수정 검증 | 확장 검증 | 중간 |
| 7 | 전 세션 순차 이관, 구 스크립트 제거 | 최종 통일 | 높음(볼륨) |

---

## 5. 핵심 트레이드오프 & 권고

1. **전면 재작성 vs 점진 이관**: 전면 재작성은 위험·고비용. **공통 코어(viz/verify) 먼저 → Phase 1 파일럿으로 검증 → 점진 확산**이 가장 실현 가능.

2. **spec의 검증 결합**: "그림을 그리면서 그 그림이 주장하는 수학적 사실을 동시에 검증"하는 것이 신뢰성의 핵심. `checks`를 spec에 내장하고 pytest가 수집 → **그림이 곧 테스트**.

3. **네이밍은 "정렬가능 + 추적가능 + 세션결합"**: 날짜 폴더를 버리고 세션 ID 폴더로 가는 것이 확장성·검색성에 유리.

---

## 6. 결정 필요 사항 (다음 단계)

- [ ] `viz/` 공통코어 + `verify/` 계층을 최우선 구축할지, 네이밍·폴더 정리를 먼저 할지.
- [ ] 선언적 spec 방식 채택 여부 (vs 기존 스크립트를 공통 헬퍼로만 리팩터링).
- [ ] 각 `viz/*.py`와 `verify/*.py`의 정확한 인터페이스·책임을 상세 설계 문서로 확장할지.
- [ ] 그래프 출력 포맷(png 단일 vs svg/pdf 병행)과 DPI 표준값.
