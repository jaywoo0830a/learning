# 세션 11: 삼각함수 — 각과 파도를 자유자재로

**Phase 2 — 고전 테크닉 | 105분**

---

## Part A: 각도 — 도에서 호도로

---

## 예시 1: $\pi = 180^\circ$만 기억한다

호도법(라디안): 원의 반지름과 같은 길이의 호가 만드는 각 = 1라디안.
반원 = $\pi r$ 호 → $180^\circ = \pi$ rad.

변환은 비례:
$90^\circ = \frac{\pi}{2}$. $60^\circ = \frac{\pi}{3}$. $45^\circ = \frac{\pi}{4}$. $30^\circ = \frac{\pi}{6}$.
$120^\circ = \frac{2\pi}{3}$. $270^\circ = \frac{3\pi}{2}$. $360^\circ = 2\pi$.

거꾸로: $\frac{5\pi}{6} \times \frac{180^\circ}{\pi} = 150^\circ$.

---

## Part B: 단위원 — 삼각함수의 씨앗

---

## 예시 2: 단위원에서 $(\cos\theta, \sin\theta)$를 읽는다

반지름 1인 원 위를 각 $\theta$만큼 돈 점의 좌표 = $(\cos\theta, \sin\theta)$.

$\theta=0$: $(1,0)$. $\theta=\frac{\pi}{2}$: $(0,1)$. $\theta=\pi$: $(-1,0)$.

$\theta=\frac{\pi}{4}$: $x^2+y^2=1$, $x=y$ → $x=y=\frac{\sqrt{2}}{2}$. → $\cos\frac{\pi}{4}=\sin\frac{\pi}{4}=\frac{\sqrt{2}}{2}$.

$\theta=\frac{\pi}{3}$: 30-60-90 삼각형. 짧은 변 $\frac{1}{2}$, 긴 변 $\frac{\sqrt{3}}{2}$.
→ $\cos\frac{\pi}{3}=\frac{1}{2}$, $\sin\frac{\pi}{3}=\frac{\sqrt{3}}{2}$.

![단위원 특수각](graphs/11a-unit-circle.png)

---

## 예시 3: 특수각 표를 손에 새긴다

| $\theta$ | $0$ | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $\sin$ | $0$ | $\frac{1}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{3}}{2}$ | $1$ |
| $\cos$ | $1$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{1}{2}$ | $0$ |
| $\tan$ | $0$ | $\frac{\sqrt{3}}{3}$ | $1$ | $\sqrt{3}$ | 없음 |

$\sin$: $0, \frac{1}{2}, \frac{\sqrt{2}}{2}, \frac{\sqrt{3}}{2}, 1$ 순서.
$\cos$: 역순. $\tan = \frac{\sin}{\cos}$.

---

## 예시 4: 사분면 부호 — "올 사 탄 코"

$\tan\theta = \frac{\sin\theta}{\cos\theta}$.

| 사분면 | $\sin$ | $\cos$ | $\tan$ | $\csc$ | $\sec$ | $\cot$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | + | + | + | + | + | + |
| 2 | + | − | − | + | − | − |
| 3 | − | − | + | − | − | + |
| 4 | − | + | − | − | + | − |

$\sin 150^\circ$: 2사분면 → +. $150^\circ = 180^\circ-30^\circ$ → $\sin 30^\circ = \frac{1}{2}$.
$\cos 210^\circ$: 3사분면 → −. $210^\circ = 180^\circ+30^\circ$ → $-\cos 30^\circ = -\frac{\sqrt{3}}{2}$.
$\tan 300^\circ$: 4사분면 → −. $300^\circ = 360^\circ-60^\circ$ → $-\tan 60^\circ = -\sqrt{3}$.

**기준각(reference angle) 방법**: $\theta$를 가장 가까운 $x$축과의 각으로.

---

## 예시 5: $\csc, \sec, \cot$ — 여섯 형제 완성

$\csc\theta = \frac{1}{\sin\theta}$ ($\sin\theta \neq 0$). $\sec\theta = \frac{1}{\cos\theta}$ ($\cos\theta \neq 0$).
$\cot\theta = \frac{1}{\tan\theta} = \frac{\cos\theta}{\sin\theta}$ ($\sin\theta \neq 0$).

값 구하기:
$\csc\frac{\pi}{6} = \frac{1}{1/2} = 2$. $\sec\frac{\pi}{4} = \frac{1}{\sqrt{2}/2} = \sqrt{2}$.
$\cot\frac{\pi}{3} = \frac{1}{\sqrt{3}} = \frac{\sqrt{3}}{3}$.

**피타고라스 항등식 확장**:
$\sin^2\theta + \cos^2\theta = 1$.
$1 + \tan^2\theta = \sec^2\theta$ (위 식을 $\cos^2\theta$로 나눔).
$1 + \cot^2\theta = \csc^2\theta$ (위 식을 $\sin^2\theta$로 나눔).

---

## Part C: 그래프 — 파도를 그리고 조절한다

---

## 예시 6: $\sin$, $\cos$, $\tan$ 기본 그래프

**$y = \sin x$**: $(0,0)$ 시작, 주기 $2\pi$, 진폭 1, 치역 $[-1,1]$.
$\frac{\pi}{2}$에서 1, $\pi$에서 0, $\frac{3\pi}{2}$에서 −1, $2\pi$에서 0. 원점대칭(기함수).

**$y = \cos x$**: $(0,1)$ 시작. $\sin$을 왼쪽으로 $\frac{\pi}{2}$ 옮긴 것. $y$축대칭(우함수).

**$y = \tan x$**: $\cos=0$인 점($\frac{\pi}{2}, \frac{3\pi}{2}, \dots$)에 수직 점근선. 주기 $\pi$. 원점대칭.

![sin cos tan](graphs/11b-sin-cos-tan.png)

---

## 예시 7: $\csc$, $\sec$, $\cot$ 그래프

$\csc x = \frac{1}{\sin x}$: $\sin=0$인 $0, \pi, 2\pi, \dots$에 점근선.
$\sin$이 양수인 곳에서 U자(최소 1), 음수인 곳에서 ∩자(최대 −1).

$\sec x = \frac{1}{\cos x}$: $\cos=0$인 $\frac{\pi}{2}, \frac{3\pi}{2}, \dots$에 점근선.

$\cot x = \frac{1}{\tan x} = \frac{\cos}{\sin}$: $\sin=0$인 $0, \pi, 2\pi, \dots$에 점근선. 주기 $\pi$, 항상 감소.

![csc sec cot](graphs/11c-csc-sec-cot.png)

---

## 예시 8: $y = a\sin(bx + c) + d$ — 파도를 요리한다

$y = 3\sin(2x - \frac{\pi}{3}) + 1$.

① **진폭**: $|a| = 3$. 파도 높이 ±3.
② **주기**: $\frac{2\pi}{|b|} = \frac{2\pi}{2} = \pi$.
③ **위상 이동**: $bx + c = 0$ → $x = -\frac{c}{b} = \frac{\pi}{6}$. 오른쪽으로 $\frac{\pi}{6}$.
④ **수직 이동**: $+1$. 치역 $[-2, 4]$.

$y = -2\cos(\frac{x}{2})$: 진폭 2(뒤집힘), 주기 $4\pi$.

![사인 변형](graphs/11d-sin-transform.png)

---

## Part D: 항등식 — 공식으로 무장한다

---

## 예시 9: 기본 항등식

$\sin^2\theta + \cos^2\theta = 1$ (피타고라스).

$\sin\theta = \frac{3}{5}$ → $\cos\theta = \pm\frac{4}{5}$ (사분면 따라 부호 결정).

$\tan\theta = \frac{\sin\theta}{\cos\theta}$.
$\sec^2\theta - \tan^2\theta = 1$.

---

## 예시 10: 덧셈정리 — 두 각의 합·차

$\sin(A+B) = \sin A\cos B + \cos A\sin B$.
$\sin(A-B) = \sin A\cos B - \cos A\sin B$.
$\cos(A+B) = \cos A\cos B - \sin A\sin B$.
$\cos(A-B) = \cos A\cos B + \sin A\sin B$.

$\sin 75^\circ = \sin(45^\circ+30^\circ) = \frac{\sqrt{2}}{2}\cdot\frac{\sqrt{3}}{2} + \frac{\sqrt{2}}{2}\cdot\frac{1}{2} = \frac{\sqrt{6}+\sqrt{2}}{4}$.

$\cos 15^\circ = \cos(45^\circ-30^\circ) = \frac{\sqrt{2}}{2}\cdot\frac{\sqrt{3}}{2} + \frac{\sqrt{2}}{2}\cdot\frac{1}{2} = \frac{\sqrt{6}+\sqrt{2}}{4}$.

---

## 예시 11: 2배각·반각 공식

$\sin 2\theta = 2\sin\theta\cos\theta$.
$\cos 2\theta = \cos^2\theta - \sin^2\theta = 2\cos^2\theta - 1 = 1 - 2\sin^2\theta$.
$\tan 2\theta = \frac{2\tan\theta}{1-\tan^2\theta}$.

반각: $\sin^2\frac{\theta}{2} = \frac{1-\cos\theta}{2}$, $\cos^2\frac{\theta}{2} = \frac{1+\cos\theta}{2}$.

---

## 예시 12: 조화합성 — $a\sin x + b\cos x$를 하나로

$3\sin x + 4\cos x$.

① $R = \sqrt{a^2+b^2} = \sqrt{9+16} = 5$.
② $\cos\phi = \frac{a}{R} = \frac{3}{5}$, $\sin\phi = \frac{b}{R} = \frac{4}{5}$.
③ $3\sin x + 4\cos x = 5\sin(x + \phi)$. $\phi = \arcsin\frac{4}{5} \approx 53.13^\circ$.

$\sqrt{3}\sin x - \cos x = 2\sin(x - \frac{\pi}{6})$. ($R=2$, $\cos\phi=\frac{\sqrt{3}}{2}$, $\sin\phi=\frac{1}{2}$ → $\phi=\frac{\pi}{6}$)

---

## 예시 13: 곱↔합 변환

$\sin A\cos B = \frac{1}{2}[\sin(A+B) + \sin(A-B)]$.
$\sin A + \sin B = 2\sin\frac{A+B}{2}\cos\frac{A-B}{2}$.
$\cos A - \cos B = -2\sin\frac{A+B}{2}\sin\frac{A-B}{2}$.

> **여기까지**: 6개 삼각함수, 그래프 조절($a,b,c,d$), 5종류 항등식. 조화합성.

---

## Part E: 방정식과 삼각형

---

## 예시 14: 삼각방정식 — 기본해 + $n$×주기

$\sin x = \frac{1}{2}$ → $x = \frac{\pi}{6} + 2n\pi$ 또는 $\frac{5\pi}{6} + 2n\pi$.

$2\cos^2 x - \cos x - 1 = 0$.
① $t = \cos x$: $2t^2 - t - 1 = 0$ → $(2t+1)(t-1)=0$.
② $\cos x = 1$ → $x = 2n\pi$.
③ $\cos x = -\frac{1}{2}$ → $x = \frac{2\pi}{3} + 2n\pi$ 또는 $\frac{4\pi}{3} + 2n\pi$.

$\sin 2x = \cos x$.
① $2\sin x\cos x - \cos x = 0$ → $\cos x(2\sin x - 1) = 0$.
② $\cos x = 0$ → $x = \frac{\pi}{2} + n\pi$.
③ $\sin x = \frac{1}{2}$ → $x = \frac{\pi}{6} + 2n\pi$ 또는 $\frac{5\pi}{6} + 2n\pi$.

---

## 예시 15: 사인법칙

$\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R$.

두 각과 한 변 알 때($AAS$/$ASA$) 나머지 구하기.
$a=10$, $A=30^\circ$, $B=45^\circ$ → $b = a\frac{\sin B}{\sin A} = 10\frac{\sin45^\circ}{\sin30^\circ} = 10\frac{\sqrt{2}/2}{1/2} = 10\sqrt{2}$.

**주의**: 두 변과 끼인각 아닌 각($SSA$)은 2해 가능성(ambiguous case).
$a=5$, $b=8$, $A=30^\circ$ → $\sin B = \frac{8\sin30^\circ}{5} = 0.8$ → $B \approx 53.1^\circ$ 또는 $126.9^\circ$.

---

## 예시 16: 코사인법칙

$a^2 = b^2 + c^2 - 2bc\cos A$.

두 변+끼인각($SAS$) → 나머지 변. 세 변($SSS$) → 각.

$b=5$, $c=7$, $A=60^\circ$ → $a^2 = 25+49-2\cdot5\cdot7\cdot\frac{1}{2} = 39$ → $a=\sqrt{39}$.

세 변 3,4,5 → $\cos A = \frac{4^2+5^2-3^2}{2\cdot4\cdot5} = \frac{32}{40} = \frac{4}{5}$. $A \approx 36.87^\circ$.

---

## 예시 17: 삼각형 넓이

**기본**: $\frac{1}{2} \times$ 밑변 $\times$ 높이.

**두 변+끼인각**: $\text{넓이} = \frac{1}{2}ab\sin C = \frac{1}{2}bc\sin A = \frac{1}{2}ca\sin B$.

$a=5$, $b=8$, $C=30^\circ$ → $\frac{1}{2}\cdot5\cdot8\cdot\sin30^\circ = 20\cdot\frac{1}{2} = 10$.

**헤론 공식** (세 변): $s = \frac{a+b+c}{2}$, 넓이 = $\sqrt{s(s-a)(s-b)(s-c)}$.
3,4,5 → $s=6$. $\sqrt{6\cdot3\cdot2\cdot1} = \sqrt{36} = 6$. 맞다.

---

## 예시 18: 역삼각함수

$\arcsin x$: $\sin\theta = x$인 $\theta \in [-\frac{\pi}{2}, \frac{\pi}{2}]$.
$\arcsin\frac{1}{2} = \frac{\pi}{6}$. $\arcsin(-1) = -\frac{\pi}{2}$.

$\arccos x$: $\theta \in [0, \pi]$. $\arccos\frac{1}{2} = \frac{\pi}{3}$.

$\arctan x$: $\theta \in (-\frac{\pi}{2}, \frac{\pi}{2})$. $\arctan 1 = \frac{\pi}{4}$.

$\arcsin(\sin\frac{5\pi}{6})$: $\sin\frac{5\pi}{6} = \frac{1}{2}$. $\arcsin\frac{1}{2} = \frac{\pi}{6}$. $\frac{5\pi}{6}$는 $\arcsin$ 치역 밖.

![삼각형 법칙](graphs/11e-triangle-laws.png)

> **여기까지**: 방정식→기본해+$n$×주기. 사인법칙(각+대변), 코사인법칙(두 변+끼인각 or 세 변).
> 삼각형 넓이 3가지. 역삼각함수는 치역 제한에 주의.

---

## Part F: 궁극의 삼각방정식·부등식 풀이법

> 어떤 삼각 문제든 아래 결정 트리로 무기를 고른다.

---

## 🔑 삼각방정식 — 무엇부터 할까?

```
삼각방정식을 만나면
├── ① 한 종류의 삼각함수만 있는가? (예: sin만, cos만)
│   ├── YES → t = sin x (또는 cos x) 치환. 이차방정식.
│   │        t∈[-1,1] 확인 필수!
│   └── NO  →
├── ② 다른 각인가? (2x vs x, 3x vs x)
│   ├── YES → 배각공식으로 각 통일.
│   │        sin2x = 2sinx·cosx, cos2x = 1-2sin²x = 2cos²x-1.
│   └── NO  →
├── ③ sin과 cos이 섞였는가?
│   ├── sin = cos 꼴 → 양변 cos으로 나누기 (cos≠0 확인).
│   │                  또는 sin²+cos²=1 이용.
│   ├── a sin + b cos = c → 조화합성 R sin(x+φ)=c.
│   └── sin², cos² 섞임 → sin²+cos²=1로 한 종류로.
├── ④ 곱=0 꼴인가?
│   └── YES → 각 인수=0. 해 합집합.
├── ⑤ 해 범위가 제한됐는가? [0,2π] 등
│   └── 일반해 구하고 → 범위 내 n만 선택.
└── ⑥ 삼각부등식인가?
    └── 그래프 그리고 축 위/아래 구간 + 주기.
```

---

## 예시 19: 결정 트리 실전 — 방정식 분류

**유형 1 — 한 종류+치환**: $2\cos^2 x - \cos x - 1 = 0$.
$t=\cos x$, $t\in[-1,1]$. $2t^2-t-1=0$ → $t=1$, $t=-\frac{1}{2}$.
$\cos x=1$ → $x=2n\pi$. $\cos x=-\frac{1}{2}$ → $x=\frac{2\pi}{3}+2n\pi$ 또는 $\frac{4\pi}{3}+2n\pi$.

**유형 2 — 각 통일**: $\cos 2x = \sin x$.
$1-2\sin^2 x = \sin x$ → $2\sin^2 x + \sin x - 1 = 0$.
$t=\sin x$: $(2t-1)(t+1)=0$ → $t=\frac{1}{2}, -1$.
$\sin x=\frac{1}{2}$ → $x=\frac{\pi}{6}+2n\pi$ 또는 $\frac{5\pi}{6}+2n\pi$. $\sin x=-1$ → $x=\frac{3\pi}{2}+2n\pi$.

**유형 3 — sin·cos 섞임+곱=0**: $\sin 2x = \cos x$.
$2\sin x\cos x - \cos x = 0$ → $\cos x(2\sin x - 1) = 0$.
$\cos x=0$ → $x=\frac{\pi}{2}+n\pi$. $\sin x=\frac{1}{2}$ → $x=\frac{\pi}{6}+2n\pi$ 또는 $\frac{5\pi}{6}+2n\pi$.

**유형 4 — 조화합성**: $\sin x + \sqrt{3}\cos x = 1$.
$R=\sqrt{1+3}=2$, $\phi=\frac{\pi}{3}$. $2\sin(x+\frac{\pi}{3})=1$.
$\sin(x+\frac{\pi}{3})=\frac{1}{2}$ → $x+\frac{\pi}{3}=\frac{\pi}{6}+2n\pi$ 또는 $\frac{5\pi}{6}+2n\pi$.
$x = -\frac{\pi}{6}+2n\pi$ 또는 $\frac{\pi}{2}+2n\pi$.

**유형 5 — 범위 제한**: $2\sin^2 x - 1 = 0$, $x\in[0, 2\pi]$.
$\sin^2 x = \frac{1}{2}$ → $\sin x = \pm\frac{\sqrt{2}}{2}$.
$x = \frac{\pi}{4}, \frac{3\pi}{4}, \frac{5\pi}{4}, \frac{7\pi}{4}$.

---

## 🔑 삼각부등식 — 그래프로 판단

```
삼각부등식을 만나면
├── ① sin x > k or cos x > k 꼴인가?
│   └── 단위원 그리고, 해당 높이보다 위/아래인 구간.
│       주기만큼 반복.
├── ② 이차부등식 꼴인가? (예: 2sin²x-sinx-1<0)
│   └── t치환 → t범위 → sin x 범위 → x 구간.
└── ③ 곱>0 or 곱<0 꼴인가?
    └── 부호표. 각 인수 0 되는 점 → 구간 나누기.
```

---

## 예시 20: 삼각부등식 실전

$\sin x > \frac{1}{2}$, $x\in[0, 2\pi]$.
단위원: 높이 $\frac{1}{2}$보다 위인 구간.
$x\in(\frac{\pi}{6}, \frac{5\pi}{6})$.
일반해: $\frac{\pi}{6}+2n\pi < x < \frac{5\pi}{6}+2n\pi$.

$2\sin^2 x - \sin x - 1 < 0$, $x\in[0, 2\pi]$.
$t=\sin x$: $2t^2-t-1<0$ → $(2t+1)(t-1)<0$ → $-\frac{1}{2}<t<1$.
$-\frac{1}{2}<\sin x<1$ ($\sin x=1$은 $<$라 제외).
$\sin x=1$ → $x=\frac{\pi}{2}$만 제외.
$\sin x=-\frac{1}{2}$ → $x=\frac{7\pi}{6}, \frac{11\pi}{6}$.
구간: $[0,\frac{7\pi}{6})\cup(\frac{11\pi}{6},2\pi]$ 에서 $\sin x > -\frac{1}{2}$.
$\frac{\pi}{2}$ 제외 → 최종: $[0,\frac{\pi}{2})\cup(\frac{\pi}{2},\frac{7\pi}{6})\cup(\frac{11\pi}{6},2\pi]$.

---

## 자주 하는 실수

### 실수 1: $\sin 2x = 2\sin x$

**틀린 길**: "$\sin 2x = 2\sin x$."

**왜 틀렸나**: $\sin 2x = 2\sin x\cos x$. $\cos x$가 빠졌다.

**옳은 길**: 2배각 공식 정확히: $\sin 2\theta = 2\sin\theta\cos\theta$.

---

### 실수 2: $\arcsin$ 치역 망각

**틀린 길**: "$\sin x = \frac{1}{2}$ → $x = \arcsin\frac{1}{2} = \frac{\pi}{6}$ 또는 $\frac{5\pi}{6}$."

**왜 틀렸나**: $\arcsin$은 $[-\frac{\pi}{2}, \frac{\pi}{2}]$만 낸다.

**옳은 길**: $\arcsin\frac{1}{2} = \frac{\pi}{6}$만. 다른 해는 $\pi - \frac{\pi}{6}$으로 구한다.

---

### 실수 3: 사인법칙 각-대변 짝 틀림

**틀린 길**: $\frac{a}{\sin B}$로 쓴다.

**왜 틀렸나**: 변 $a$의 맞은편 각은 $A$다.

**옳은 길**: $\frac{a}{\sin A} = \frac{b}{\sin B}$.

---

## 방금 우리가 한 일

```
① 단위원+특수각표. 6함수+사분면 부호. 그래프(a,b,c,d).
② 항등식: 피타고라스, 덧셈, 2배각, 조화합성, 합↔곱.
③ 방정식 결정 트리:
   한종류→t치환. 각다름→통일. sin·cos섞임→곱=0 or 조화합성.
④ 부등식 결정 트리:
   sin>k → 단위원+주기. 이차형→t치환. 곱→부호표.
⑤ 삼각형: 사인법칙(AAS/ASA/SSA주의), 코사인법칙(SAS/SSS), 넓이3종.
```

---

## 연습 1

$\sin\theta = -\frac{\sqrt{3}}{2}$, $\theta$ 4사분면. $\cos,\tan,\sec,\csc,\cot$ 전부 구하라.

→ 따라하기: **예시 3, 4, 5**

> 풀이: [풀이집](solutions/11-solutions.md#연습-1)

---

## 연습 2

$y = 2\sin(3x+\pi)-1$의 진폭·주기·위상·수직이동을 말하고, 최대·최소값을 구하라.

→ 따라하기: **예시 8**

> 풀이: [풀이집](solutions/11-solutions.md#연습-2)

---

## 연습 3

$\cos 2x = \sin x$를 $[0, 2\pi]$에서 풀어라. $\cos 2x = 1-2\sin^2 x$.

→ 따라하기: **예시 14, 11**

> 풀이: [풀이집](solutions/11-solutions.md#연습-3)

---

## 연습 4: 구성형

$5\sin x + 12\cos x$를 $R\sin(x+\phi)$ 꼴로 바꾸고, 최댓값과 그때의 $x$를 구하라.
이 방법이 유용한 예시를 하나 더 들어보라.

→ 따라하기: **예시 12**

> 풀이: [풀이집](solutions/11-solutions.md#연습-4)

---

## 연습 5

$a=7$, $b=10$, $c=13$인 삼각형의 세 각과 넓이를 구하라.

→ 따라하기: **예시 16, 17**

> 풀이: [풀이집](solutions/11-solutions.md#연습-5)

---

## 연습 6: 실전

$\sec x + \tan x = 2$일 때 $\sec x - \tan x$와 $\sin x$를 구하라.
$(\sec x + \tan x)(\sec x - \tan x) = 1$ 이용.

→ 따라하기: **예시 5, 9**

> 풀이: [풀이집](solutions/11-solutions.md#연습-6)

---

## 오늘 배운 절차

```
1단계: 단위원+특수각표+6함수+사분면 부호. 그래프 a·sin(bx+c)+d.
2단계: 방정식 결정 트리 — t치환→각통일→sin·cos분리→곱=0→조화합성.
       부등식 결정 트리 — 그래프+주기. 범위제한 확인.
3단계: 삼각형 — SAS/SSS→코사인, AAS/ASA→사인, SSA는 2해 경고.
       넓이=½ab sinC, 헤론. 역삼각함수 치역 주의.
```

---

## 용어 정리

지금까지 우리는 "파도", "한 바퀴", "뒤집는다", "맞은편 각", "끼인각" 같은 쉬운 말만 썼다.
**방법은 이미 다 배웠다.** 이제 수학에서 쓰는 이름을 소개한다.

| 우리가 써온 말 | 수학 용어 | 기호/설명 |
|:------------:|:--------:|:---:|
| 호도(라디안) | radian | $\pi = 180^\circ$ |
| 단위원 | unit circle | 반지름 1 |
| 한 바퀴(주기) | period | $\sin$/$\cos$: $2\pi$, $\tan$: $\pi$ |
| 파도 높이(진폭) | amplitude | $\lvert a\rvert$ |
| 위상 옮기기 | phase shift | $-c/b$ |
| 역수 삼각함수 | reciprocal trig | $\csc,\sec,\cot$ |
| 덧셈정리 | sum formulas | $\sin(A\pm B),\cos(A\pm B)$ |
| 2배각·반각 | double/half-angle | $\sin2\theta,\cos2\theta$ |
| 조화합성 | harmonic addition | $a\sin x+b\cos x = R\sin(x+\phi)$ |
| 사인법칙 | law of sines | $\frac{a}{\sin A} = 2R$ |
| 코사인법칙 | law of cosines | $a^2=b^2+c^2-2bc\cos A$ |
| 헤론 공식 | Heron's formula | $\sqrt{s(s-a)(s-b)(s-c)}$ |
| 역삼각함수 | inverse trig | $\arcsin,\arccos,\arctan$ |
