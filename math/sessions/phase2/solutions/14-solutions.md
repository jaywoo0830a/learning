# 14 풀이집 — 미분법

---

## 연습 1

> $\frac{d}{dx}(3x^4-2x^3+x-5)$.

① 항마다 미분: $3\cdot4x^3-2\cdot3x^2+1-0$.
→ **$12x^3-6x^2+1$.**

---

## 연습 2

> $\frac{d}{dx}(x^2\cos x)$.

① 곱의 미분: $f=x^2$, $g=\cos x$.
$f'=2x$, $g'=-\sin x$.
② $f'g+fg' = 2x\cos x + x^2(-\sin x)$.
→ **$2x\cos x - x^2\sin x$.**

---

## 연습 3

> $\frac{d}{dx}\frac{x^2+1}{x-1}$.

① 몫의 미분: $f=x^2+1$, $g=x-1$. $f'=2x$, $g'=1$.
② $\frac{f'g-fg'}{g^2} = \frac{2x(x-1) - (x^2+1)\cdot1}{(x-1)^2}$.
③ $= \frac{2x^2-2x-x^2-1}{(x-1)^2} = \frac{x^2-2x-1}{(x-1)^2}$.
→ **$\frac{x^2-2x-1}{(x-1)^2}$.**

---

## 연습 4

> $\frac{d}{dx}\sqrt{\sin(x^2)}$.

① $\sqrt{u} = u^{1/2}$. 겉미분: $\frac{1}{2\sqrt{\sin(x^2)}}$.
② 중간 $\sin(x^2)$ 미분: $\cos(x^2)$.
③ 속 $x^2$ 미분: $2x$.
④ → $\frac{1}{2\sqrt{\sin(x^2)}}\cdot\cos(x^2)\cdot2x = \frac{x\cos(x^2)}{\sqrt{\sin(x^2)}}$.
→ **$\frac{x\cos(x^2)}{\sqrt{\sin(x^2)}}$.**

---

## 연습 5

> $x^3+y^3=6xy$에서 $\frac{dy}{dx}$, 점 $(3,3)$에서 값.

① $3x^2+3y^2\frac{dy}{dx}=6y+6x\frac{dy}{dx}$.
② $\frac{dy}{dx}$항: $3y^2\frac{dy}{dx}-6x\frac{dy}{dx}=6y-3x^2$.
③ $(3y^2-6x)\frac{dy}{dx}=6y-3x^2$.
④ $\frac{dy}{dx}=\frac{6y-3x^2}{3y^2-6x}$.
⑤ $(3,3)$: $\frac{18-27}{27-18}=\frac{-9}{9}=-1$.
→ **$\frac{6y-3x^2}{3y^2-6x}$, 점 $(3,3)$에서 $-1$.**

---

## 연습 6: 구성형

> $f'(x)=f(x)$를 만족하는 함수.

$f(x)=Ce^x$ ($C$는 임의 상수).
예: $e^x$, $2e^x$, $-e^x$, $\frac{1}{2}e^x$.
모두 $Ce^x$ 꼴. $f(0)=C$가 된다.

이유: $\frac{d}{dx}Ce^x = Ce^x = f(x)$.

---

## 연습 7

> $y=(\sin x)^x$를 로그미분.

① $\ln y = x\ln(\sin x)$.
② $\frac{1}{y}\frac{dy}{dx} = 1\cdot\ln(\sin x) + x\cdot\frac{\cos x}{\sin x} = \ln(\sin x) + x\cot x$.
③ $\frac{dy}{dx} = (\sin x)^x[\ln(\sin x) + x\cot x]$.
→ **$(\sin x)^x(\ln\sin x + x\cot x)$.**

---

## 연습 8: 실전

> $x=t-\sin t$, $y=1-\cos t$. $\frac{dy}{dx}$, $\frac{d^2y}{dx^2}$.

① $\frac{dx}{dt}=1-\cos t$, $\frac{dy}{dt}=\sin t$.
② $\frac{dy}{dx}=\frac{\sin t}{1-\cos t}$.
③ $\frac{\sin t}{1-\cos t} = \frac{2\sin\frac{t}{2}\cos\frac{t}{2}}{2\sin^2\frac{t}{2}} = \frac{\cos\frac{t}{2}}{\sin\frac{t}{2}} = \cot\frac{t}{2}$.

④ $\frac{d^2y}{dx^2} = \frac{d}{dx}\left(\frac{dy}{dx}\right) = \frac{d/dt(\cot\frac{t}{2})}{dx/dt}$.
⑤ $\frac{d}{dt}\cot\frac{t}{2} = -\frac{1}{2}\csc^2\frac{t}{2}$.
⑥ $\frac{d^2y}{dx^2} = \frac{-\frac{1}{2}\csc^2\frac{t}{2}}{1-\cos t} = \frac{-\frac{1}{2}\csc^2\frac{t}{2}}{2\sin^2\frac{t}{2}}$.
⑦ $\csc^2\frac{t}{2} = \frac{1}{\sin^2\frac{t}{2}}$. → $-\frac{1}{4\sin^4\frac{t}{2}}$.

→ **$\frac{dy}{dx}=\cot\frac{t}{2}$, $\frac{d^2y}{dx^2}=-\frac{1}{4}\csc^4\frac{t}{2}$.**

---

## 연습 9

> $\frac{d}{dx}(x^2 e^x)$.

① 곱의 미분: $f=x^2$, $g=e^x$. $f'=2x$, $g'=e^x$.
② $=2xe^x + x^2e^x = e^x(x^2+2x)$.
→ **$e^x(x^2+2x)$.**

---

## 연습 10

> $\frac{d}{dx}\frac{\ln x}{x}$.

① 몫의 미분: $\frac{(1/x)\cdot x - \ln x\cdot1}{x^2} = \frac{1-\ln x}{x^2}$.
→ **$\frac{1-\ln x}{x^2}$.**

---

## 연습 11

> $\frac{d}{dx}\cos(x^3)$.

① 연쇄: 겉 $\cos u$ → $-\sin u$. 속 $x^3$ → $3x^2$.
② $=-3x^2\sin(x^3)$.
→ **$-3x^2\sin(x^3)$.**

---

## 연습 12: 실전2

> $\frac{d}{dx}\frac{x}{\sqrt{x^2+1}}$, $f''(0)$.

① $f'=\frac{1\cdot\sqrt{x^2+1} - x\cdot\frac{x}{\sqrt{x^2+1}}}{x^2+1} = \frac{x^2+1-x^2}{(x^2+1)\sqrt{x^2+1}} = (x^2+1)^{-3/2}$.
② $f''=-\frac{3}{2}(x^2+1)^{-5/2}\cdot2x = -3x(x^2+1)^{-5/2}$.
③ $f''(0)=0$.
→ **$f'(x)=(x^2+1)^{-3/2}$, $f''(0)=0$.**

---

[목차](../14-derivatives.md)
