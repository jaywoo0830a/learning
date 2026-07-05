# 세션 17: 적분 응용 — 넓이·부피·길이를 쌓아 올린다

**Phase 2 — 고전 테크닉 | 90분**

---

## Part A: 곡선 사이 넓이

---

## 예시 1: $x$축과 곡선 사이 — 기본

$\int_a^b f(x)dx$ = $x$축 위쪽이면 양수, 아래쪽이면 음수 넓이.

$y=x^2$과 $x$축 사이, $x=0$에서 $x=2$까지 넓이.
$\int_0^2 x^2\,dx = [\frac{x^3}{3}]_0^2 = \frac{8}{3}$.

$y=\sin x$와 $x$축 사이, $0$에서 $\pi$까지.
$\int_0^\pi \sin x\,dx = [-\cos x]_0^\pi = 2$.

---

## 예시 2: 두 곡선 사이 — 위에서 아래를 뺀다

$y=x^2$과 $y=x$ 사이 ($0\leq x\leq1$).

① 위 곡선: $y=x$ (더 큰 값). 아래: $y=x^2$.
② $\int_0^1(x-x^2)dx = [\frac{x^2}{2}-\frac{x^3}{3}]_0^1 = \frac{1}{2}-\frac{1}{3} = \frac{1}{6}$.
![곡선 사이 넓이](graphs/17a-between-curves.png)
---

## 예시 3: 삼각함수 곡선 사이

$y=\sin x$와 $y=\cos x$ 사이, $x=0$에서 $x=\frac{\pi}{4}$까지.

① $[0,\frac{\pi}{4}]$에서 $\cos x \geq \sin x$. 위=$\cos x$, 아래=$\sin x$.
② $\int_0^{\pi/4}(\cos x-\sin x)dx = [\sin x+\cos x]_0^{\pi/4}$.
③ $=(\frac{\sqrt{2}}{2}+\frac{\sqrt{2}}{2})-(0+1)=\sqrt{2}-1$.

---

## 예시 4: 지수·로그 곡선 사이

$y=e^x$와 $y=\ln x+2$ 사이? (복잡) 대신:

$y=e^x$와 $y=e^{-x}$ 사이, $x=0$에서 $x=1$까지.
① $[0,1]$에서 $e^x \geq e^{-x}$.
② $\int_0^1(e^x-e^{-x})dx = [e^x+e^{-x}]_0^1 = (e+e^{-1})-(1+1) = e+\frac{1}{e}-2$.

$y=\ln x$와 $x$축 사이, $x=1$에서 $x=e$까지.
① $\int_1^e \ln x\,dx = [x\ln x - x]_1^e = (e\cdot1-e)-(1\cdot0-1) = 0-(-1)=1$.

---

## 예시 5: $y$축 기준 — $x$에 대해 적분

$y=x^2$과 $y=4$ 사이 넓이 ($y$축 기준).

① $x=\sqrt{y}$ (오른쪽). $x=0$에서 $y=4$까지.
② $\int_0^4 \sqrt{y}\,dy = [\frac{2}{3}y^{3/2}]_0^4 = \frac{2}{3}\cdot8 = \frac{16}{3}$.

$x$축 기준으로도: $\int_{-2}^2(4-x^2)dx = [4x-\frac{x^3}{3}]_{-2}^2 = (8-\frac{8}{3})-(-8+\frac{8}{3}) = \frac{32}{3}$? 틀림.
다시: $2\int_0^2(4-x^2)dx = 2[4x-\frac{x^3}{3}]_0^2 = 2(8-\frac{8}{3}) = \frac{32}{3}$.
$y$축이 $\frac{16}{3}$, $x$축이 $\frac{32}{3}$ — 서로 다른 영역!

---

## Part B: 회전체 부피

---

## 예시 6: 디스크 방법 — $\pi\int R^2\,dx$

곡선을 축 주위로 빙글 돌리면 입체가 생긴다. 이 입체의 부피를 구하는 핵심 아이디어는 **얇은 원판(디스크)으로 썰어서 쌓는 것**이다. 각 $x$ 위치에서 원판의 반지름은 그 점에서의 $y$값, 넓이는 $\pi R^2$, 두께는 $dx$. 이 원판들을 모조리 쌓으면 전체 부피가 된다. 그래서 $\int \pi R^2\,dx$가 나온다.

$y=x^2$을 $x$축 기준으로 $x=0$에서 $x=1$까지 회전.

① 단면 반지름 $R=x^2$.
② $V = \pi\int_0^1 (x^2)^2\,dx = \pi\int_0^1 x^4\,dx = \pi[\frac{x^5}{5}]_0^1 = \frac{\pi}{5}$.

![회전체](graphs/17b-solid-revolution.png)

$y=\sqrt{x}$을 $x$축 기준 $x=0$에서 $x=4$까지 회전.
① $R=\sqrt{x}$. $V=\pi\int_0^4 x\,dx = \pi[\frac{x^2}{2}]_0^4 = 8\pi$.

---

## 예시 7: 와셔 방법 — $\pi\int(R^2-r^2)dx$

$y=x^2+1$과 $y=x+1$ 사이 영역을 $x$축 기준 회전 ($0\leq x\leq1$).

① 바깥 반지름 $R=x+1$, 안쪽 $r=x^2+1$.
② $V=\pi\int_0^1[(x+1)^2-(x^2+1)^2]dx$.
③ $(x+1)^2=x^2+2x+1$. $(x^2+1)^2=x^4+2x^2+1$.
④ 차이: $-x^4-x^2+2x$.
⑤ $V=\pi[- \frac{x^5}{5}-\frac{x^3}{3}+x^2]_0^1 = \pi(-\frac{1}{5}-\frac{1}{3}+1) = \pi\cdot\frac{7}{15} = \frac{7\pi}{15}$.

---

## 예시 8: 삼각·지수 회전체

$y=\sin x$ ($0\leq x\leq\pi$)를 $x$축 기준 회전.
① $V=\pi\int_0^\pi \sin^2 x\,dx = \pi\int_0^\pi\frac{1-\cos2x}{2}dx$.
② $=\frac{\pi}{2}[x-\frac{\sin2x}{2}]_0^\pi = \frac{\pi}{2}\cdot\pi = \frac{\pi^2}{2}$.

$y=e^x$ ($0\leq x\leq1$)를 $x$축 기준 회전.
① $V=\pi\int_0^1 e^{2x}\,dx = \pi[\frac{e^{2x}}{2}]_0^1 = \frac{\pi}{2}(e^2-1)$.

---

## 예시 9: 껍질 방법 — $2\pi\int r h\,dx$ ($y$축 회전)

$y=x^2$ ($0\leq x\leq2$)를 $y$축 기준 회전.

① 반지름 $r=x$, 높이 $h=x^2$.
② $V=2\pi\int_0^2 x\cdot x^2\,dx = 2\pi\int_0^2 x^3\,dx = 2\pi[\frac{x^4}{4}]_0^2 = 2\pi\cdot4 = 8\pi$.

같은 것을 디스크로: $x=\sqrt{y}$, $V=\pi\int_0^4(\sqrt{y})^2 dy = \pi\int_0^4 y\,dy = \pi[\frac{y^2}{2}]_0^4 = 8\pi$. 일치!

---

## Part C: 곡선 길이와 표면적

---

## 예시 10: 곡선 길이 — $L=\int\sqrt{1+(y')^2}dx$

곡선의 길이를 어떻게 잴까? 직선이라면 피타고라스 정리로 한 번에 된다. 하지만 곡선은 휘어 있다. 아이디어는 **곡선을 아주 잘게 쪼개서 각 조각을 직선으로 근사**하는 것이다. 한 조각의 길이는 피타고라스 정리에 의해 $\sqrt{(dx)^2+(dy)^2} = \sqrt{1+(dy/dx)^2}\,dx$가 된다. 이걸 모두 더하면 — 즉 적분하면 — 전체 곡선 길이다.

$y=x^{3/2}$의 $x=0$에서 $x=4$까지 길이.
① $y'=\frac{3}{2}x^{1/2}$. $(y')^2=\frac{9}{4}x$.
② $L=\int_0^4\sqrt{1+\frac{9}{4}x}\,dx$.
③ $u=1+\frac{9}{4}x$, $du=\frac{9}{4}dx$.
④ $L=\frac{4}{9}\int_1^{10}\sqrt{u}\,du = \frac{4}{9}[\frac{2}{3}u^{3/2}]_1^{10} = \frac{8}{27}(10\sqrt{10}-1)$.

---

## 예시 11: 지수·로그·삼각 곡선 길이

$y=\ln\cos x$의 $x=0$에서 $x=\frac{\pi}{3}$까지.
① $y'=-\tan x$. $\sqrt{1+\tan^2 x}=\sec x$.
② $L=\int_0^{\pi/3}\sec x\,dx = [\ln|\sec x+\tan x|]_0^{\pi/3}$.
③ $=\ln(2+\sqrt{3})-\ln(1+0)=\ln(2+\sqrt{3})$.

$y=\frac{e^x+e^{-x}}{2}$의 $x=0$에서 $x=1$까지. (현수선)
① $y'=\frac{e^x-e^{-x}}{2}$. $(y')^2=\frac{e^{2x}-2+e^{-2x}}{4}$.
② $1+(y')^2=\frac{e^{2x}+2+e^{-2x}}{4}=(\frac{e^x+e^{-x}}{2})^2$.
③ $L=\int_0^1\frac{e^x+e^{-x}}{2}dx = [\frac{e^x-e^{-x}}{2}]_0^1 = \frac{e-e^{-1}}{2}$.

---

## 예시 12: 매개변수 곡선 길이

$x=\cos^3 t$, $y=\sin^3 t$ ($0\leq t\leq\frac{\pi}{2}$). (아스트로이드)
① $\frac{dx}{dt}=-3\cos^2 t\sin t$, $\frac{dy}{dt}=3\sin^2 t\cos t$.
② $(x')^2+(y')^2=9\cos^4 t\sin^2 t+9\sin^4 t\cos^2 t = 9\cos^2 t\sin^2 t(\cos^2 t+\sin^2 t)=9\cos^2 t\sin^2 t$.
③ $\sqrt{(x')^2+(y')^2}=3|\cos t\sin t|=\frac{3}{2}|\sin2t|$.
④ $L=\int_0^{\pi/2}\frac{3}{2}\sin2t\,dt = \frac{3}{2}[-\frac{\cos2t}{2}]_0^{\pi/2} = \frac{3}{2}\cdot\frac{1-(-1)}{2} = \frac{3}{2}$.

---

## Part D: 이상적분 — 무한대까지

---

## 예시 13: 무한구간 이상적분

적분 구간이 무한대까지 뻗어 있다. 직접 무한대를 대입할 수는 없으니, **유한한 $b$까지 적분한 다음 $b\to\infty$ 극한을 보낸다**. 극한이 유한한 값으로 수렴하면 "적분이 수렴한다", 무한대로 발산하면 "적분이 발산한다"고 말한다. 직관적으로, $\frac{1}{x^3}$처럼 함수가 충분히 빨리 0으로 줄어들면 면적이 유한하고, $\frac{1}{x}$처럼 천천히 줄어들면 무한대가 된다.

$\int_1^\infty \frac{1}{x^3}\,dx = \lim_{b\to\infty}\int_1^b x^{-3}dx = \lim_{b\to\infty}[-\frac{1}{2x^2}]_1^b = \lim_{b\to\infty}(\frac{1}{2}-\frac{1}{2b^2}) = \frac{1}{2}$. **수렴**.

$\int_1^\infty \frac{1}{x}\,dx = \lim_{b\to\infty}[\ln x]_1^b = \lim_{b\to\infty}\ln b = \infty$. **발산**.

$\int_0^\infty e^{-x}\,dx = \lim_{b\to\infty}[-e^{-x}]_0^b = \lim_{b\to\infty}(-e^{-b}+1) = 1$. **수렴**.

---

## 예시 14: 불연속점 이상적분

$\int_0^1 \frac{1}{\sqrt{x}}\,dx = \lim_{a\to0^+}\int_a^1 x^{-1/2}dx = \lim_{a\to0^+}[2\sqrt{x}]_a^1 = 2-0 = 2$. **수렴**.

$\int_0^1 \frac{1}{x}\,dx = \lim_{a\to0^+}[\ln x]_a^1 = \lim_{a\to0^+}(0-\ln a) = \infty$. **발산**.

$\int_0^2 \frac{1}{(x-1)^2}\,dx$.
① $x=1$에서 불연속. $\int_0^1 + \int_1^2$로 나눔.
② $\int_0^1$: $\lim_{b\to1^-}[-\frac{1}{x-1}]_0^b = \lim_{b\to1^-}(\frac{1}{1-b}-1) = \infty$. **발산**.

---

## 예시 15: 수렴 판정 — $\int_1^\infty \frac{1}{x^p}dx$

$p>1$: 수렴 ($\frac{1}{p-1}$). $p\leq1$: 발산.

$\int_1^\infty \frac{1}{x^2}dx = 1$ (수렴). $\int_1^\infty \frac{1}{\sqrt{x}}dx$ 발산 ($p=\frac{1}{2}$).

**비교판정**: $\int_1^\infty \frac{1}{x^2+1}dx \leq \int_1^\infty \frac{1}{x^2}dx = 1$. 수렴.

$\int_2^\infty \frac{1}{\ln x}dx$. $\frac{1}{\ln x} > \frac{1}{x}$ ($x>e$). $\int\frac{1}{x}dx$ 발산 → 이것도 발산.

---

## 예시 16: 지수·삼각 이상적분

$\int_0^\infty e^{-x}\sin x\,dx$.
① 부정적분 (예시12): $\frac{e^{-x}}{2}(-\sin x-\cos x)$.
② $\int_0^\infty = \lim_{b\to\infty}[\frac{e^{-x}}{2}(-\sin x-\cos x)]_0^b$.
③ $b\to\infty$: $e^{-b}\to0$ → $0$.
④ $x=0$: $\frac{1}{2}(0-1)=-\frac{1}{2}$.
⑤ $=0-(-\frac{1}{2}) = \frac{1}{2}$. **수렴**.

$\int_0^\infty e^{-x^2}dx = \frac{\sqrt{\pi}}{2}$. (가우스 적분 — 유명)

> **여기까지**: 넓이(위-아래), 회전체(디스크·와셔·껍질), 곡선길이, 이상적분($\lim$+판정).
> $p$-판정: $\int_1^\infty 1/x^p$는 $p>1$ 수렴, $p\leq1$ 발산.

---

## 자주 하는 실수

### 실수 1: 두 곡선 사이 넓이에서 위/아래 구분 안 함

**틀린 길**: $\int(x^2-x)dx$로 계산. (음수 넓이 나옴)

**왜 틀렸나**: 넓이는 양수. $x^2<x$인 구간에서 $x-x^2$로 적분해야.

**옳은 길**: 그래프 그려서 위 곡선 확인. $\int(\text{위}-\text{아래})dx$.

---

### 실수 2: 회전체에서 반지름 제곱 안 함

**틀린 길**: $V=\pi\int R\,dx$.

**왜 틀렸나**: 디스크 넓이 = $\pi R^2$. $R$이 아니라 $R^2$을 적분.

**옳은 길**: $V=\pi\int R^2\,dx$.

---

### 실수 3: 이상적분 극한 처리 누락

**틀린 길**: $\int_1^\infty\frac{1}{x^2}dx = [-\frac{1}{x}]_1^\infty = 0-(-1)=1$. (우연히 맞음)

**왜 틀렸나**: $\infty$를 직접 대입하면 안 됨. $\lim_{b\to\infty}$로 처리.

**옳은 길**: $\lim_{b\to\infty}\int_1^b$로 쓰고 극한.

---

## 방금 우리가 한 일

```
① 곡선 사이 넓이: ∫(위-아래)dx. y축 기준이면 ∫(오른쪽-왼쪽)dy.
② 회전체: 디스크 π∫R²dx, 와셔 π∫(R²-r²)dx, 껍질 2π∫r·h dx.
   다항·삼각(sin²→반각)·지수(e²ˣ)·로그 모두.
③ 곡선길이: L=∫√(1+(y')²)dx. 현수선·lncosx·매개변수.
④ 이상적분: lim_{b→∞}. p-판정: ∫1/xᵖ (p>1 수렴).
   지수감쇠(e⁻ˣ)는 항상 수렴.
```

---

## 연습 1

$y=x^2$과 $y=2x+3$ 사이 넓이. 교점 먼저.

→ 따라하기: **예시 2**

> 풀이: [풀이집](solutions/17-solutions.md#연습-1)

---

## 연습 2

$y=\cos x$ ($0\leq x\leq\frac{\pi}{2}$)를 $x$축 기준 회전 부피.

→ 따라하기: **예시 6, 8**

> 풀이: [풀이집](solutions/17-solutions.md#연습-2)

---

## 연습 3

$y=\ln x$의 $x=1$에서 $x=e$까지 곡선 길이.

→ 따라하기: **예시 10, 11**

> 풀이: [풀이집](solutions/17-solutions.md#연습-3)

---

## 연습 4

$\int_0^\infty \frac{1}{x^2+4}dx$. $\arctan$ 이용.

→ 따라하기: **예시 13**

> 풀이: [풀이집](solutions/17-solutions.md#연습-4)

---

## 연습 5: 구성형

$\int_1^\infty \frac{1}{x^p}dx$가 수렴하는 $p$의 범위를 구하고,
$p=2$일 때 값과 $p=1.0001$일 때의 값을 비교해보라. $p$가 1에 가까워질수록 어떤 일이?

→ 따라하기: **예시 15**

> 풀이: [풀이집](solutions/17-solutions.md#연습-5)

---

## 연습 6

$y=e^{-x}$ ($0\leq x<\infty$)를 $x$축 기준 회전. 부피는?

→ 따라하기: **예시 8, 13**

> 풀이: [풀이집](solutions/17-solutions.md#연습-6)

---

## 연습 7

$x=t-\sin t$, $y=1-\cos t$ (사이클로이드 한 주기, $0\leq t\leq2\pi$)의 길이.

→ 따라하기: **예시 12**

> 풀이: [풀이집](solutions/17-solutions.md#연습-7)

---

## 연습 8: 실전

$y=\frac{1}{x}$의 $x=1$에서 $x\to\infty$까지 $x$축 회전체 부피는 수렴하지만,
곡선 아래 넓이($\int_1^\infty\frac{1}{x}dx$)는 발산한다.
이 "무한히 긴 뿔"의 부피를 구하고 왜 이런 역설이 생기는지 설명하라.

→ 따라하기: **예시 13, 15**

> 풀이: [풀이집](solutions/17-solutions.md#연습-8)

---

## 연습 9

$y=x^2$과 $y=2-x^2$ 사이 넓이. 교점 먼저.

→ 따라하기: **예시 2**

> 풀이: [풀이집](solutions/17-solutions.md#연습-9)

---

## 연습 10

$y=x^2$ ($0\leq x\leq1$)을 $x$축 회전 부피. 디스크.

→ 따라하기: **예시 6**

> 풀이: [풀이집](solutions/17-solutions.md#연습-10)

---

## 연습 11

$\int_0^\infty xe^{-x}\,dx$. 이상적분+부분적분.

→ 따라하기: **예시 13, 16**

> 풀이: [풀이집](solutions/17-solutions.md#연습-11)

---

## 연습 12: 실전2

$y=\sin x$ ($0\leq x\leq\pi$)와 $x$축 영역을 $y$축 회전 부피. 껍질.

→ 따라하기: **예시 9**

> 풀이: [풀이집](solutions/17-solutions.md#연습-12)

---

## 오늘 배운 절차

```
1단계: 넓이 — 그래프 그리고 위-아래 확인. 교점이 경계.
       y축 기준이면 x=f(y)로.
2단계: 회전체 — 축에 수직인 단면 반지름 찾기.
       디스크/와셔(x축) vs 껍질(y축).
3단계: 곡선길이 — y' 구하고 √(1+(y')²) 적분.
4단계: 이상적분 — lim 처리. p>1 수렴, p≤1 발산.
```

---

## 용어 정리

| 우리가 써온 말 | 수학 용어 | 기호/설명 |
|:------------:|:--------:|:---:|
| 넓이 쌓기 | 정적분 | $\int_a^b f(x)dx$ |
| 디스크 | disk method | $\pi\int R^2 dx$ |
| 와셔 | washer method | $\pi\int(R^2-r^2)dx$ |
| 껍질 | shell method | $2\pi\int r h\,dx$ |
| 곡선 길이 | arc length | $\int\sqrt{1+(y')^2}dx$ |
| 이상적분 | improper integral | $\lim_{b\to\infty}\int_a^b$ |
| 수렴/발산 | converge/diverge | 유한값/무한대 |
| $p$-판정 | $p$-test | $\int_1^\infty 1/x^p$ |
