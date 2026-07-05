# 17 풀이집 — 적분 응용

---

## 연습 1

> $y=x^2$과 $y=2x+3$ 사이 넓이.

① 교점: $x^2=2x+3$ → $x^2-2x-3=0$ → $x=-1,3$.
② $[-1,3]$에서 $2x+3 \geq x^2$.
③ $\int_{-1}^3[(2x+3)-x^2]dx = [x^2+3x-\frac{x^3}{3}]_{-1}^3$.
④ $x=3$: $9+9-9=9$. $x=-1$: $1-3+\frac{1}{3}=-\frac{5}{3}$.
⑤ $9-(-\frac{5}{3}) = \frac{32}{3}$.
→ **$\frac{32}{3}$.**

---

## 연습 2

> $y=\cos x$ ($0\leq x\leq\frac{\pi}{2}$) $x$축 회전.

① $V=\pi\int_0^{\pi/2}\cos^2 x\,dx = \pi\int_0^{\pi/2}\frac{1+\cos2x}{2}dx$.
② $=\frac{\pi}{2}[x+\frac{\sin2x}{2}]_0^{\pi/2} = \frac{\pi}{2}\cdot\frac{\pi}{2} = \frac{\pi^2}{4}$.
→ **$\frac{\pi^2}{4}$.**

---

## 연습 3

> $y=\ln x$, $x=1$에서 $x=e$까지 길이.

① $y'=\frac{1}{x}$. $1+(y')^2=1+\frac{1}{x^2}=\frac{x^2+1}{x^2}$.
② $\sqrt{1+(y')^2}=\frac{\sqrt{x^2+1}}{x}$.
③ $L=\int_1^e\frac{\sqrt{x^2+1}}{x}dx$.
④ $x=\tan\theta$, $dx=\sec^2\theta\,d\theta$. $x=1\to\theta=\frac{\pi}{4}$, $x=e\to\theta=\arctan e$.
⑤ $\int\frac{\sec\theta}{\tan\theta}\sec^2\theta\,d\theta = \int\frac{\sec^3\theta}{\tan\theta}d\theta = \int\frac{1}{\sin\theta\cos^2\theta}d\theta$.
⑥ 복잡 — 수치적분으로 $\approx 2.00$.
→ **수치값 약 2.00.**

---

## 연습 4

> $\int_0^\infty\frac{1}{x^2+4}dx$.

① $\frac{1}{x^2+4}=\frac{1}{4}\cdot\frac{1}{(x/2)^2+1}$.
② $\frac{1}{2}\int_0^\infty\frac{1/2}{(x/2)^2+1}dx$. $u=x/2$, $dx=2du$.
③ $=\frac{1}{2}\int_0^\infty\frac{2}{u^2+1}du = \int_0^\infty\frac{1}{u^2+1}du$.
④ $=[\arctan u]_0^\infty = \frac{\pi}{2}-0 = \frac{\pi}{2}$.
→ **$\frac{\pi}{2}$.**

---

## 연습 5: 구성형

> $\int_1^\infty\frac{1}{x^p}dx$.

$p\neq1$: $\lim_{b\to\infty}[\frac{x^{1-p}}{1-p}]_1^b = \lim_{b\to\infty}\frac{b^{1-p}-1}{1-p}$.
$p>1$: $1-p<0$, $b^{1-p}\to0$ → $\frac{1}{p-1}$. **수렴**.
$p<1$: $1-p>0$, $b^{1-p}\to\infty$ → **발산**.
$p=1$: $\lim\ln b = \infty$ → **발산**.

$p=2$: $\frac{1}{2-1}=1$. $p=1.0001$: $\frac{1}{0.0001}=10000$.
$p\to1^+$일 때 값이 폭발적으로 커짐 ($\frac{1}{p-1}\to\infty$).

---

## 연습 6

> $y=e^{-x}$ ($0\leq x<\infty$) $x$축 회전.

① $V=\pi\int_0^\infty e^{-2x}dx = \pi\lim_{b\to\infty}[-\frac{e^{-2x}}{2}]_0^b$.
② $=\pi(0-(-\frac{1}{2})) = \frac{\pi}{2}$.
→ **$\frac{\pi}{2}$.** (유한 부피!)

---

## 연습 7

> 사이클로이드 $x=t-\sin t$, $y=1-\cos t$, $0\leq t\leq2\pi$ 길이.

① $x'=1-\cos t$, $y'=\sin t$.
② $(x')^2+(y')^2=(1-\cos t)^2+\sin^2 t = 1-2\cos t+\cos^2 t+\sin^2 t = 2-2\cos t$.
③ $=4\sin^2\frac{t}{2}$. $\sqrt{}=2|\sin\frac{t}{2}|$.
④ $L=\int_0^{2\pi}2\sin\frac{t}{2}dt = 2[-2\cos\frac{t}{2}]_0^{2\pi} = 4(\cos0-\cos\pi) = 4(1-(-1)) = 8$.
→ **8.**

---

## 연습 8: 실전

> 가브리엘의 뿔: $y=\frac{1}{x}$, $x\geq1$ 회전.

부피: $V=\pi\int_1^\infty\frac{1}{x^2}dx = \pi[-\frac{1}{x}]_1^\infty = \pi(0-(-1))=\pi$. **수렴!**

넓이: $\int_1^\infty\frac{1}{x}dx = \infty$. **발산!**

역설: 유한한 부피의 페인트로 채울 수 있지만, 표면을 칠하려면 무한한 페인트가 필요.
이유: 부피는 $\int 1/x^2$ ($p=2>1$) 수렴, 넓이는 $\int 1/x$ ($p=1$) 발산.
$1/x$이 $1/x^2$보다 훨씬 느리게 감소하기 때문.

---

## 연습 9

> $y=x^2$과 $y=2-x^2$ 사이 넓이.

① 교점: $x^2=2-x^2$ → $2x^2=2$ → $x=\pm1$.
② $[-1,1]$에서 $2-x^2 \geq x^2$.
③ $\int_{-1}^1[(2-x^2)-x^2]dx = 2\int_0^1(2-2x^2)dx = 4[x-\frac{x^3}{3}]_0^1 = 4(1-\frac{1}{3}) = \frac{8}{3}$.
→ **$\frac{8}{3}$.**

---

## 연습 10

> $y=x^2$ ($0\leq x\leq1$) $x$축 회전.

① $V=\pi\int_0^1 (x^2)^2 dx = \pi\int_0^1 x^4 dx = \pi[\frac{x^5}{5}]_0^1 = \frac{\pi}{5}$.
→ **$\frac{\pi}{5}$.**

---

## 연습 11

> $\int_0^\infty xe^{-x}\,dx$.

① 부분적분: $u=x$, $dv=e^{-x}dx$. $du=dx$, $v=-e^{-x}$.
② $\int xe^{-x}dx = -xe^{-x} + \int e^{-x}dx = -xe^{-x} - e^{-x} = -e^{-x}(x+1)$.
③ $\int_0^\infty = \lim_{b\to\infty}[-e^{-x}(x+1)]_0^b = 0 - (-1) = 1$.
→ **1.**

---

## 연습 12: 실전2

> $y=\sin x$, $0\leq x\leq\pi$, $y$축 회전. 껍질.

① $V=2\pi\int_0^\pi x\sin x\,dx$.
② 부분적분: $u=x$, $dv=\sin x\,dx$. $du=dx$, $v=-\cos x$.
③ $=2\pi([-x\cos x]_0^\pi + \int_0^\pi\cos x\,dx) = 2\pi(\pi + 0) = 2\pi^2$.
→ **$2\pi^2$.**

---

[목차](../17-integration-applications.md)
