# 16 풀이집 — 적분법

---

## 연습 1

> $\int(3x^2+2e^x-\frac{1}{x})dx$.

① 각 항 적분: $3\cdot\frac{x^3}{3}+2e^x-\ln|x|+C$.
→ **$x^3+2e^x-\ln|x|+C$.**

---

## 연습 2

> $\int x\sqrt{x^2+4}\,dx$.

① $u=x^2+4$, $du=2x\,dx$ → $x\,dx=\frac{1}{2}du$.
② $\int\sqrt{u}\cdot\frac{1}{2}du = \frac{1}{2}\cdot\frac{2}{3}u^{3/2}+C = \frac{1}{3}(x^2+4)^{3/2}+C$.
→ **$\frac{1}{3}(x^2+4)^{3/2}+C$.**

---

## 연습 3

> $\int x\cos x\,dx$.

① $u=x$, $dv=\cos x\,dx$. $du=dx$, $v=\sin x$.
② $=x\sin x - \int\sin x\,dx = x\sin x + \cos x + C$.
→ **$x\sin x+\cos x+C$.**

---

## 연습 4

> $\int \ln(x^2)\,dx$.

① $\ln(x^2)=2\ln|x|$.
② $=2\int\ln|x|dx = 2(x\ln|x|-x)+C = 2x\ln|x|-2x+C$.
→ **$2x\ln|x|-2x+C$.**

---

## 연습 5

> $\int_0^{\pi/2}\sin^3 x\,dx$.

① $\sin^3 x = \sin x(1-\cos^2 x) = \sin x - \sin x\cos^2 x$.
② $u=\cos x$, $du=-\sin x\,dx$. $x=0\to u=1$, $x=\frac{\pi}{2}\to u=0$.
③ $\int_0^{\pi/2}\sin x\,dx = [-\cos x]_0^{\pi/2}=1$.
④ $\int_0^{\pi/2}\sin x\cos^2 x\,dx = \int_1^0 -u^2\,du = [\frac{u^3}{3}]_0^1 = \frac{1}{3}$.
⑤ $1-\frac{1}{3}=\frac{2}{3}$.
→ **$\frac{2}{3}$.**

---

## 연습 6

> $\int\frac{1}{x^2\sqrt{x^2-4}}dx$ ($x>2$).

① $x=2\sec\theta$, $dx=2\sec\theta\tan\theta\,d\theta$.
② $\sqrt{x^2-4}=2\tan\theta$.
③ $\int\frac{2\sec\theta\tan\theta}{4\sec^2\theta\cdot2\tan\theta}d\theta = \int\frac{1}{4\sec\theta}d\theta = \frac{1}{4}\int\cos\theta\,d\theta$.
④ $=\frac{1}{4}\sin\theta+C$.
⑤ $\sin\theta = \frac{\sqrt{x^2-4}}{x}$.
→ **$\frac{\sqrt{x^2-4}}{4x}+C$.**

---

## 연습 7: 구성형

> $\int\frac{1}{x^2-1}dx$를 부분분수와 $x=\sec\theta$로.

**방법1 — 부분분수**:
$\frac{1}{(x-1)(x+1)} = \frac{1}{2}(\frac{1}{x-1}-\frac{1}{x+1})$.
적분: $\frac{1}{2}(\ln|x-1|-\ln|x+1|)+C = \frac{1}{2}\ln|\frac{x-1}{x+1}|+C$.

**방법2 — $x=\sec\theta$** (복잡):
$\int\frac{\sec\theta\tan\theta}{\sec^2\theta-1}d\theta = \int\frac{\sec\theta\tan\theta}{\tan^2\theta}d\theta = \int\frac{\sec\theta}{\tan\theta}d\theta = \int\csc\theta\,d\theta$.
$=\ln|\csc\theta-\cot\theta|+C$.
$\csc\theta=\frac{x}{\sqrt{x^2-1}}$, $\cot\theta=\frac{1}{\sqrt{x^2-1}}$.
$=\ln|\frac{x-1}{\sqrt{x^2-1}}|+C = \frac{1}{2}\ln|\frac{x-1}{x+1}|+C$ (동치 확인 가능).

---

## 연습 8: 실전

> $\int e^{2x}\sin 3x\,dx$.

① $u=\sin3x$, $dv=e^{2x}dx$. $du=3\cos3x\,dx$, $v=\frac{e^{2x}}{2}$.
② $I = \frac{e^{2x}}{2}\sin3x - \frac{3}{2}\int e^{2x}\cos3x\,dx$.

③ 두 번째: $u=\cos3x$, $dv=e^{2x}dx$. $du=-3\sin3x\,dx$, $v=\frac{e^{2x}}{2}$.
④ $\int e^{2x}\cos3x\,dx = \frac{e^{2x}}{2}\cos3x + \frac{3}{2}\int e^{2x}\sin3x\,dx = \frac{e^{2x}}{2}\cos3x + \frac{3}{2}I$.

⑤ $I = \frac{e^{2x}}{2}\sin3x - \frac{3}{2}(\frac{e^{2x}}{2}\cos3x + \frac{3}{2}I)$.
⑥ $I = \frac{e^{2x}}{2}\sin3x - \frac{3e^{2x}}{4}\cos3x - \frac{9}{4}I$.
⑦ $\frac{13}{4}I = \frac{e^{2x}}{4}(2\sin3x-3\cos3x)$.
⑧ $I = \frac{e^{2x}}{13}(2\sin3x-3\cos3x)+C$.
→ **$\frac{e^{2x}}{13}(2\sin3x-3\cos3x)+C$.**

---

## 연습 9

> $\int x\sqrt{x^2+4}\,dx$.

① $u=x^2+4$, $du=2x\,dx$ → $x\,dx=\frac{1}{2}du$.
② $\int\sqrt{u}\cdot\frac{1}{2}du = \frac{1}{2}\cdot\frac{2}{3}u^{3/2}+C$.
③ $=\frac{1}{3}(x^2+4)^{3/2}+C$.
→ **$\frac{1}{3}(x^2+4)^{3/2}+C$.**

---

## 연습 10

> $\int x\ln x\,dx$.

① $u=\ln x$, $dv=x\,dx$. $du=\frac{1}{x}dx$, $v=\frac{x^2}{2}$.
② $=\frac{x^2}{2}\ln x - \int\frac{x^2}{2}\cdot\frac{1}{x}dx = \frac{x^2}{2}\ln x - \frac{x^2}{4}+C$.
→ **$\frac{x^2}{2}\ln x - \frac{x^2}{4}+C$.**

---

## 연습 11

> $\int_0^{\pi/2}\sin^2 x\cos x\,dx$.

① $u=\sin x$, $du=\cos x\,dx$. $x=0\to u=0$, $x=\pi/2\to u=1$.
② $\int_0^1 u^2\,du = [\frac{u^3}{3}]_0^1 = \frac{1}{3}$.
→ **$\frac{1}{3}$.**

---

## 연습 12: 실전2

> $\int\frac{1}{x^2-4}\,dx$.

① $\frac{1}{(x-2)(x+2)} = \frac{1}{4}(\frac{1}{x-2}-\frac{1}{x+2})$.
② $\frac{1}{4}(\ln|x-2|-\ln|x+2|)+C$.
→ **$\frac{1}{4}\ln\left|\frac{x-2}{x+2}\right|+C$.**

---

[목차](../16-integration.md)
