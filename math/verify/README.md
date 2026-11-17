# verify — 세션 검증 도구

세션 Markdown의 **숫자**와 **KaTeX 구문**을 검사한다. 두 검사는 서로 독립이고,
모든 세션에 쓸 수 있다.

```
verify/
├── verify.py              # CLI 진입점 (katex / answers / all)
├── Dockerfile             # python:3.12-slim + sympy
├── checks/
│   ├── drills.py          # 답안 검증 러너 (세션 무관)
│   ├── katex.py           # 마크다운 + KaTeX 구문 검사
│   └── katex_commands.py  # KaTeX 지원 명령/환경 목록
└── answers/
    └── 14D.py             # 14D가 주장하는 모든 수치 (112개)
```

## 실행

도커(권장 — 로컬 파이썬 의존성 없음):

```bash
make verify VERIFY=14D      # 14D 답안 검증
make verify-katex           # 모든 세션 KaTeX 구문
make verify-all             # 둘 다 (CI 게이트)
```

`make` 없이 직접:

```bash
docker build -t math-verify verify
docker run --rm -v "$PWD:/work" math-verify answers 14D
docker run --rm -v "$PWD:/work" math-verify katex 14D
docker run --rm -v "$PWD:/work" math-verify all
```

세션 파일은 바인드 마운트되므로 세션·답안을 고쳐도 이미지 재빌드는 필요 없다.

호스트 파이썬으로:

```bash
make verify-host VERIFY=14D      # python3 + sympy 필요
python3 verify/verify.py katex 14D
make verify-selftest             # 검사기 회귀 테스트 (도커·sympy 불필요)
```

종료 코드는 검사 실패 시 1 — `make verify-all && make strict` 처럼 게이트로 쓸 수 있다.

## 왜 sympy 인가

답안 검증은 모든 수치를 **기호적으로** 비교한다(`simplify(got - want) == 0`).
부동소수 허용오차로 비교하지 않으므로 `1/30` 과 `0.0333…` 이 다르다고 잘못
판정하지 않고, `361/25` 같은 유리수도 정확히 일치한다. 단, 무리수 근사값
(`2·6^(1/4) ≈ 3.130`)은 문제 파일에서 정확식으로 선언한다.

## 새 세션에 답안 검증 추가하기

`answers/<SESSION>.py` 하나만 추가하면 된다. 러너는 세션을 모른다.

```python
"""Verified numbers for 15A — <session title>."""
import sympy as sp

x = sp.symbols('x', real=True)

SECTIONS = []


def add(title):
    checks = []
    SECTIONS.append((title, checks))
    return checks


_c = add("Q1: f(x) = x^3 - 12x + 16")
_c.append(("f'(x)=3x^2-12", sp.diff(x**3 - 12*x + 16, x), 3*x**2 - 12))
_c.append(("zeros at -4 and 2", sorted(sp.solve(x**3 - 12*x + 16, x)), [-4, 2]))

_c = add("Q2: local minimum value")
_c.append(("f(-2)=32", (x**3 - 12*x + 16).subs(x, -2), sp.Integer(32)))


def run(ctx):
    for title, checks in SECTIONS:
        ctx.begin_section(title)
        for label, got, want in checks:
            ctx.check(label, got, want)
```

각 체크는 `(label, got, want)` 이고 `want` 는 스칼라 또는 리스트다.
`got - want` 가 0으로 단순화되면 통과한다. 무리수 근사는 정확식으로 적는다
(예: `2 * sp.Pow(6, sp.Rational(1, 4))`).

## KaTeX 검사가 잡는 것

| 검사 | 예 |
|:---|:---|
| 미지원 명령 | `\foo` → `unknown KaTeX command \foo` |
| 미지원/짝 안 맞는 환경 | `\begin{aligned}` vs `\end{cases}` |
| 중괄호 불균형 | `\frac{1}{2` |
| `\left`/`\right` 불일치 | `\left(` … `)` |
| 스크립트 피연산자 누락 | `x^}` |
| 짝 안 맞는 `$` | 인라인 수식 하나가 닫히지 않음 |
| 수식 안의 맨 `$` | `$...$` 로 잘못 잘린 흔적 |

검사기는 **코드 펜스**와 **이미지 alt 텍스트**를 건너뛴다(둘 다 수식으로
렌더되지 않음). `\$` 는 이스케이프된 리터럴 달러로 취급하며, 행렬의 `\\`
행 구분자는 명령으로 오인하지 않는다.

### KaTeX 명령 목록 관리

`checks/katex_commands.py` 의 목록은 [katex.org/docs/supported](https://katex.org/docs/supported)
기준으로 벤더링한 것이다. KaTeX가 새 명령을 추가하면 그 목록에 넣는다.
목록에 없는 명령은 **파일:줄:명령** 으로 보고되므로, 누락은 조용히 넘어가지
않고 바로 드러난다.
