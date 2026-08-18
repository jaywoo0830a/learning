# Solutions — 16A: Integration Fundamentals

> Back to [16A — Integration Fundamentals](../16A-integration-fundamentals.md)

---

## Practice 1

$\int (4x^3 - 2x + 5)\,dx$

Split at each $+/-$ sign and pull constants:

$\int 4x^3\,dx - \int 2x\,dx + \int 5\,dx = 4\int x^3\,dx - 2\int x\,dx + 5\int 1\,dx$

Apply the power rule $\int x^n\,dx = \frac{x^{n+1}}{n+1}$:

$= 4 \cdot \frac{x^4}{4} - 2 \cdot \frac{x^2}{2} + 5x + C$

$= x^4 - x^2 + 5x + C$

**Check**: $\frac{d}{dx}(x^4 - x^2 + 5x + C) = 4x^3 - 2x + 5$. ✓

---

## Practice 2

$\int_0^2 (3x^2+1)\,dx$

**Step 1**: Find antiderivative $F(x)$.

$F(x) = 3 \cdot \frac{x^3}{3} + x = x^3 + x$ (omit $+C$ — it cancels in FTC)

**Step 2**: FTC — $F(2) - F(0)$.

$F(2) = 2^3 + 2 = 8 + 2 = 10$

$F(0) = 0^3 + 0 = 0$

$\int_0^2 (3x^2+1)\,dx = 10 - 0 = 10$

---

## Practice 3

$\int x\sqrt{x^2+4}\,dx$

Run the $u$-sub algorithm:

| Step | Action |
|:---:|:---|
| 1 | $u = x^2+4$ (inner function inside the root) |
| 2 | $du = 2x\,dx$ → $x\,dx = \frac{1}{2}du$ |
| 3 | Replace: $\sqrt{x^2+4} = \sqrt{u} = u^{1/2}$, $x\,dx = \frac{1}{2}du$. Integral: $\int u^{1/2} \cdot \frac{1}{2}\,du = \frac{1}{2}\int u^{1/2}\,du$ |
| 4 | Integrate: $\frac{1}{2} \cdot \frac{u^{3/2}}{3/2} + C = \frac{1}{2} \cdot \frac{2}{3}u^{3/2} + C = \frac{1}{3}u^{3/2} + C$ |
| 5 | Back-substitute: $\frac{1}{3}(x^2+4)^{3/2} + C$ |

**Check**: $\frac{d}{dx}\left[\frac{1}{3}(x^2+4)^{3/2}\right] = \frac{1}{3} \cdot \frac{3}{2}(x^2+4)^{1/2} \cdot 2x = x\sqrt{x^2+4}$. ✓

---

## Practice 4

$\int_0^{\pi/2} \sin x\cos^2 x\,dx$

Definite $u$-sub with bounds change:

**Step 1**: $u = \cos x$ (priority 5 — inside the power). Then $du = -\sin x\,dx$ → $\sin x\,dx = -du$.

**Step 2**: Change bounds:
- $x = 0$ → $u = \cos 0 = 1$
- $x = \pi/2$ → $u = \cos(\pi/2) = 0$

**Step 3**: Replace: $\cos^2 x = u^2$, $\sin x\,dx = -du$.

$\int_{x=0}^{x=\pi/2} \sin x\cos^2 x\,dx = \int_{u=1}^{u=0} u^2(-du) = -\int_1^0 u^2\,du$

**Step 4**: Flip bounds and integrate:

$-\int_1^0 u^2\,du = \int_0^1 u^2\,du = \left[\frac{u^3}{3}\right]_0^1 = \frac{1}{3} - 0 = \frac{1}{3}$

---

## Practice 5: Real Battle (Constructive)

**(a) Is the computation correct?**

$\int_{-2}^2 x^3\,dx = \left[\frac{x^4}{4}\right]_{-2}^2 = \frac{16}{4} - \frac{16}{4} = 4 - 4 = 0$

Yes, the computation is correct.

**(b) Is the conclusion correct?**

No. The *definite integral* equals zero, but the *total area* is not zero. The definite integral measures **net signed area**: area above the $x$-axis counts as positive, area below counts as negative. For an odd function like $x^3$, the negative area on $[-2,0]$ cancels the positive area on $[0,2]$, yielding net zero — but the actual enclosed region has nonzero area.

**(c) Total area (all regions positive)**

Total area = $\int_{-2}^0 |x^3|\,dx + \int_0^2 |x^3|\,dx$

On $[-2,0]$, $x^3 \leq 0$ so $|x^3| = -x^3$. On $[0,2]$, $x^3 \geq 0$ so $|x^3| = x^3$.

$\int_{-2}^0 (-x^3)\,dx + \int_0^2 x^3\,dx = -\left[\frac{x^4}{4}\right]_{-2}^0 + \left[\frac{x^4}{4}\right]_0^2$

$= -\left(0 - \frac{16}{4}\right) + \left(\frac{16}{4} - 0\right) = -(-4) + 4 = 4 + 4 = 8$

Total area = $8$.

**Odd function property**: For any odd function $f(-x) = -f(x)$ integrated over a symmetric interval $[-a, a]$, the signed area cancels: $\int_{-a}^a f(x)\,dx = 0$. This is because the graph is symmetric about the origin — what's below the axis on one side is exactly mirrored above on the other side, giving net zero.

---

## Basic Drills

### B1. $\int x^5\,dx$

Power rule: $\int x^n\,dx = \frac{x^{n+1}}{n+1} + C$.

$\int x^5\,dx = \frac{x^6}{6} + C$.

---

### B2. $\int (2e^x + \frac{3}{x})\,dx$

Split and pull constants:

$= 2\int e^x\,dx + 3\int \frac{1}{x}\,dx$

$= 2e^x + 3\ln|x| + C$

---

### B3. $\int_1^4 \sqrt{x}\,dx$

Rewrite: $\sqrt{x} = x^{1/2}$.

Antiderivative: $\int x^{1/2}\,dx = \frac{x^{3/2}}{3/2} + C = \frac{2}{3}x^{3/2} + C$.

FTC: $\left[\frac{2}{3}x^{3/2}\right]_1^4 = \frac{2}{3}(4^{3/2}) - \frac{2}{3}(1^{3/2})$

$4^{3/2} = (4^{1/2})^3 = 2^3 = 8$, $1^{3/2} = 1$.

$= \frac{2}{3} \cdot 8 - \frac{2}{3} \cdot 1 = \frac{16}{3} - \frac{2}{3} = \frac{14}{3}$

---

### B4. $\int_0^{\pi} \cos x\,dx$

Antiderivative: $\int \cos x\,dx = \sin x + C$.

FTC: $\left[\sin x\right]_0^{\pi} = \sin\pi - \sin 0 = 0 - 0 = 0$.

Net signed area is zero — the positive lobe on $[0, \pi/2]$ cancels the negative lobe on $[\pi/2, \pi]$.

---

### B5. $\int 3x^2(x^3+1)^4\,dx$

$u$-sub:

1. $u = x^3+1$ (priority 1 — inside parentheses raised to a power)
2. $du = 3x^2\,dx$ — **exact match** with $3x^2\,dx$ in the integrand!
3. Replace: $(x^3+1)^4 = u^4$, $3x^2\,dx = du$. Integral: $\int u^4\,du$.
4. Integrate: $\frac{u^5}{5} + C$.
5. Back: $\frac{(x^3+1)^5}{5} + C$.

**Check**: $\frac{d}{dx}\left[\frac{(x^3+1)^5}{5}\right] = \frac{5(x^3+1)^4}{5} \cdot 3x^2 = 3x^2(x^3+1)^4$. ✓

---

### B6. $\int e^{3x}\,dx$

$u = 3x$, $du = 3\,dx$ → $dx = \frac{du}{3}$.

$\int e^{3x}\,dx = \int e^u \cdot \frac{du}{3} = \frac{1}{3}\int e^u\,du = \frac{1}{3}e^u + C = \frac{1}{3}e^{3x} + C$.

---

### B7. $\int \frac{x}{x^2+1}\,dx$

$u = x^2+1$ (priority 3 — denominator), $du = 2x\,dx$ → $x\,dx = \frac{du}{2}$.

$\int \frac{x}{x^2+1}\,dx = \int \frac{1}{u} \cdot \frac{du}{2} = \frac{1}{2}\int \frac{1}{u}\,du = \frac{1}{2}\ln|u| + C = \frac{1}{2}\ln(x^2+1) + C$.

(No absolute value needed in the final answer since $x^2+1 > 0$ always, but it's harmless to include.)

---

### B8. $\int_0^1 xe^{x^2}\,dx$

$u = x^2$ (priority 4 — exponent of $e$), $du = 2x\,dx$ → $x\,dx = \frac{du}{2}$.

Change bounds: $x=0 \to u=0$, $x=1 \to u=1$.

$\int_0^1 xe^{x^2}\,dx = \int_0^1 e^u \cdot \frac{du}{2} = \frac{1}{2}\int_0^1 e^u\,du = \frac{1}{2}\left[e^u\right]_0^1 = \frac{1}{2}(e - 1)$.

---

### B9. $\int \frac{\cos x}{\sin x}\,dx$

$u = \sin x$, $du = \cos x\,dx$ — **exact match**.

$\int \frac{\cos x}{\sin x}\,dx = \int \frac{1}{u}\,du = \ln|u| + C = \ln|\sin x| + C$.

---

### B10. $\int_{-1}^2 (x^2-2x)\,dx$

Antiderivative: $F(x) = \frac{x^3}{3} - x^2$.

FTC:

$F(2) = \frac{8}{3} - 4 = \frac{8}{3} - \frac{12}{3} = -\frac{4}{3}$

$F(-1) = \frac{(-1)^3}{3} - (-1)^2 = -\frac{1}{3} - 1 = -\frac{4}{3}$

$\int_{-1}^2 (x^2-2x)\,dx = F(2) - F(-1) = -\frac{4}{3} - \left(-\frac{4}{3}\right) = 0$.

(Net signed area is zero — check: $x^2-2x = x(x-2)$ has roots at $0$ and $2$, so on $[-1,0]$ the parabola is above the axis (positive area) and on $[0,2]$ it's below (negative area). The areas happen to cancel over $[-1,2]$.)

---

### B11. Average value of $f(x)=\sin x$ on $[0,\pi]$.

$\bar f = \frac{1}{\pi}\int_0^\pi\sin x\,dx = \frac{1}{\pi}[-\cos x]_0^\pi = \frac{1}{\pi}(1+1) = \frac{2}{\pi}$.

> **Answer**: $\frac{2}{\pi}$

---

### B12. $\int \sec x\tan x\,dx$.

Dictionary: $\sec x\tan x \to \sec x$.

> **Answer**: $\sec x + C$

---

## Calculation Drills

### C1. $\int \frac{(x^2+1)^3}{x^4}\,dx$

Expand the numerator, split the fraction, apply the power rule:

$\frac{(x^2+1)^3}{x^4} = \frac{x^6+3x^4+3x^2+1}{x^4} = x^2 + 3 + 3x^{-2} + x^{-4}$.

$\int = \frac{x^3}{3} + 3x + 3\cdot\frac{x^{-1}}{-1} + \frac{x^{-3}}{-3} + C = \frac{x^3}{3} + 3x - \frac{3}{x} - \frac{1}{3x^3} + C$.

> **Answer**: $\frac{x^3}{3} + 3x - \frac{3}{x} - \frac{1}{3x^3} + C$

---

### C2. $\int (e^x+e^{-x})^2\,dx$

Expand the square, then integrate term by term:

$(e^x+e^{-x})^2 = e^{2x} + 2 + e^{-2x}$.

$\int = \frac{e^{2x}}{2} + 2x - \frac{e^{-2x}}{2} + C$.

> **Answer**: $\frac{e^{2x}}{2} + 2x - \frac{e^{-2x}}{2} + C$

---

### C3. $\int \frac{\ln(x\sqrt{x})}{x}\,dx$

Combine the logs first: $\ln(x\sqrt{x}) = \ln(x\cdot x^{1/2}) = \ln(x^{3/2}) = \frac32\ln x$.

$u = \ln x$, $du = \frac{dx}{x}$: $\frac32\int u\,du = \frac32\cdot\frac{u^2}{2} = \frac{3(\ln x)^2}{4} + C$.

> **Answer**: $\frac{3(\ln x)^2}{4} + C$

---

### C4. $\int_1^2 \frac{x^2+1}{x^3+3x}\,dx$

$P'/P$ form: $\frac{d}{dx}(x^3+3x) = 3x^2+3 = 3(x^2+1)$, so the numerator is $\frac13 P'$:

$\int_1^2\frac{x^2+1}{x^3+3x}dx = \frac13\left[\ln|x^3+3x|\right]_1^2 = \frac13(\ln 14 - \ln 4) = \frac13\ln\frac72$.

> **Answer**: $\frac13\ln\frac72$

---

### C5. $\int \sin^3 x\cos^3 x\,dx$

Use $\sin x\cos x = \frac{\sin 2x}{2}$, cube, then peel:

$\sin^3x\cos^3x = \left(\frac{\sin 2x}{2}\right)^3 = \frac18\sin^3 2x = \frac18\sin 2x(1-\cos^2 2x)$.

$u = \cos 2x$, $du = -2\sin 2x\,dx$: $\frac18\int\sin 2x(1-u^2)\cdot\frac{du}{-2} = -\frac1{16}\int(1-u^2)\,du$

$= -\frac1{16}\left(u - \frac{u^3}{3}\right) = -\frac{\cos 2x}{16} + \frac{\cos^3 2x}{48} + C$.

> **Answer**: $-\frac{\cos 2x}{16} + \frac{\cos^3 2x}{48} + C$

---

### C6. $\int \frac{\tan x}{\ln(\sec x)}\,dx$

$P'/P$ with trig: $\frac{d}{dx}\ln(\sec x) = \frac{\sec x\tan x}{\sec x} = \tan x$ — the numerator is exactly $P'$.

$u = \ln(\sec x)$, $du = \tan x\,dx$: $\int\frac{du}{u} = \ln|u| = \ln|\ln(\sec x)| + C$.

> **Answer**: $\ln|\ln(\sec x)| + C$

---

### C7. $\int_0^{\pi}\sin^2 x\cos^2 x\,dx$

$\sin^2x\cos^2x = \frac{\sin^2 2x}{4} = \frac{1-\cos 4x}{8}$.

$\frac18\int_0^\pi(1-\cos 4x)\,dx = \frac18\left[x - \frac{\sin 4x}{4}\right]_0^\pi = \frac18(\pi - 0) = \frac{\pi}{8}$.

> **Answer**: $\frac{\pi}{8}$

---

### C8. $\int_0^{\pi/2}\left(e^{\sin x}\cos x + \sin 2x\right)\,dx$

First term: $u = \sin x$, bounds $0\to1$: $\int_0^1 e^u\,du = e-1$.

Second term: $\int_0^{\pi/2}\sin 2x\,dx = \left[-\frac{\cos 2x}{2}\right]_0^{\pi/2} = \frac12 + \frac12 = 1$.

Total: $e - 1 + 1 = e$.

> **Answer**: $e$

---

### C9. $\int_0^1 x^3\sqrt{1-x^2}\,dx$

$u = 1-x^2$, $du = -2x\,dx$, $x^2 = 1-u$:

$x^3\sqrt{1-x^2}\,dx = x^2\sqrt{u}\cdot x\,dx = (1-u)u^{1/2}\cdot\frac{du}{-2}$.

Bounds: $x=0\to u=1$, $x=1\to u=0$. $\int_1^0 (1-u)u^{1/2}\frac{du}{-2} = \frac12\int_0^1(u^{1/2}-u^{3/2})\,du = \frac12\left(\frac23-\frac25\right) = \frac{2}{15}$.

> **Answer**: $\frac{2}{15}$

---

### C10. $\int_0^1\left(\frac{x}{1+x^2} + \frac{e^x}{e^x+1}\right)\,dx$

Two $P'/P$ terms:

$\int_0^1\frac{x}{1+x^2}dx = \frac12\ln(1+x^2)\big|_0^1 = \frac12\ln 2$.

$\int_0^1\frac{e^x}{e^x+1}dx = \ln(e^x+1)\big|_0^1 = \ln(e+1)-\ln 2$.

Sum: $\frac12\ln 2 + \ln(e+1) - \ln 2 = \ln(e+1) - \frac12\ln 2 = \ln\frac{e+1}{\sqrt2}$.

> **Answer**: $\ln(e+1) - \frac12\ln 2 = \ln\frac{e+1}{\sqrt2}$

---

## Advanced Drills

### A1. $\int x^2\sqrt{x^3+1}\,dx$ — verify and explain the $\frac13$.

$u = x^3+1$ (inside the root), $du = 3x^2\,dx$ → $x^2\,dx = \frac{du}{3}$.

$\int x^2\sqrt{x^3+1}\,dx = \frac{1}{3}\int u^{1/2}\,du = \frac{1}{3}\cdot\frac{u^{3/2}}{3/2} + C = \frac{2}{9}(x^3+1)^{3/2} + C$.

**Verify**: $\frac{d}{dx}\left[\frac{2}{9}(x^3+1)^{3/2}\right] = \frac{2}{9}\cdot\frac{3}{2}(x^3+1)^{1/2}\cdot 3x^2 = x^2\sqrt{x^3+1}$. ✓

**The $\frac13$**: by the chain rule, $\frac{d}{dx}(x^3+1)^{3/2}$ carries an inner factor $3x^2$. Reading the chain rule backward (u-sub), that inner $3$ must be divided out — so $x^2\,dx = \frac{du}{3}$. The $\frac13$ is the chain rule's inner derivative undone.

---

### A2. $\int \frac{e^x}{1+e^{2x}}\,dx$ — arctan, not log.

$u = e^x$, $du = e^x\,dx$: $\int\frac{e^x}{1+(e^x)^2}dx = \int\frac{du}{1+u^2} = \arctan u + C = \arctan(e^x) + C$.

**Why arctan, not log**: the denominator $1+u^2$ is a sum of squares — the arctan form $\int\frac{du}{1+u^2}$. Compare $\int\frac{e^x}{1+e^x}dx$: after $u=e^x$ it's $\int\frac{du}{1+u} = \ln|1+u|$ — the denominator is linear, not a sum of squares. **Sum of squares → arctan; linear → log.**

---

### A3. $\int_0^4 \frac{x}{\sqrt{1+2x}}\,dx$ — why solve for $x$.

$u = 1+2x$, $du = 2\,dx$ → $dx = \frac{du}{2}$; and $x = \frac{u-1}{2}$. Bounds: $x=0\to u=1$, $x=4\to u=9$.

$\int_1^9 \frac{(u-1)/2}{u^{1/2}}\cdot\frac{du}{2} = \frac{1}{4}\int_1^9(u^{1/2}-u^{-1/2})du = \frac{1}{4}\left[\frac{2}{3}u^{3/2} - 2u^{1/2}\right]_1^9$

$= \frac{1}{4}\left[\left(18-6\right) - \left(\frac23 - 2\right)\right] = \frac{1}{4}\left(12 + \frac43\right) = \frac{1}{4}\cdot\frac{40}{3} = \frac{10}{3}$.

**Why solve for $x$**: in A1 the numerator $x^2$ was (up to a constant) exactly $du$ — nothing left over. Here $du = 2\,dx$ is a pure $dx$, while the numerator $x$ is NOT a multiple of $du$: the leftover $x$ must be expressed in terms of $u$ ($x = \frac{u-1}{2}$) before integrating. **If the numerator is a constant times $du$, you never solve for $x$; if it isn't, you must.**

---

### A4. $\int \sin^3 x\,dx$ — why "peel one".

$\sin^3 x = \sin x(1-\cos^2 x)$. $u=\cos x$, $du = -\sin x\,dx$:

$\int(1-u^2)(-du) = -u + \frac{u^3}{3} + C = -\cos x + \frac{\cos^3 x}{3} + C$.

**Why it works**: the peeled $\sin x$ becomes exactly $du$ for $u = \cos x$; the rest is pure $\cos^2$. **Why it fails for $\sin^2 x$**: $\sin^2 x = 1-\cos^2 x$ has no leftover $\sin x$ to serve as $du$ — you'd be left with $u$ but no $du$. Even powers need half-angle (16B), not peeling.

---

### A5. $\int_1^e \frac{(\ln x)^n}{x}\,dx$ — general formula.

$u = \ln x$, $du = \frac{dx}{x}$, bounds $0 \to 1$: $\int_0^1 u^n\,du = \frac{1}{n+1}$.

- $n=0$: $\int_1^e \frac{dx}{x} = \ln e = 1 = \frac{1}{0+1}$ ✓
- $n=1$: $\int_1^e \frac{\ln x}{x}dx = \left[\frac{(\ln x)^2}{2}\right]_1^e = \frac12 = \frac{1}{1+1}$ ✓
- $n=2$: answer $\frac13$ ✓

> **Answer**: $\int_1^e \frac{(\ln x)^n}{x}\,dx = \frac{1}{n+1}$ for every natural $n$.

---

### A6. $\int \frac{x^2+1}{x^3+3x+1}\,dx$ — the $\frac{P'}{P}$ rule.

$\frac{d}{dx}(x^3+3x+1) = 3(x^2+1)$ — the numerator is $\frac13 P'$. So $u = x^3+3x+1$:

$\frac13\int\frac{du}{u} = \frac13\ln|u| + C = \frac13\ln|x^3+3x+1| + C$.

**General rule**: $\int\frac{P'(x)}{P(x)}dx = \ln|P(x)| + C$. If the numerator is a constant multiple $c\,P'(x)$, the answer is $c\ln|P(x)|$. The whole trick is recognizing the numerator as (part of) the denominator's derivative — the same signal as B7's $x/(x^2+1)$.

---

### A7. Find $b$ with $\int_0^b x\cos(x^2)\,dx = \frac12$.

$u = x^2$, $du = 2x\,dx$, bounds $0 \to b^2$: $\int = \frac12\int_0^{b^2}\cos u\,du = \frac12\sin(b^2)$.

Set $\frac12\sin(b^2) = \frac12$ → $\sin(b^2) = 1$ → $b^2 = \frac{\pi}{2}$ → $b = \sqrt{\pi/2}$.

**How you knew**: the integral's value is $\frac12\sin(\text{upper bound}^2)$. You wanted $\frac12$, so you needed $\sin(b^2) = 1$ — the "clean" angle $\frac{\pi}{2}$. Choose the bound so the substitution lands on a known sine value; that's the thinking that makes the answer tidy.

---

### A8. $\int \frac{dx}{1+e^x}$ — two correct answers.

Multiply by $e^{-x}$: $\frac{1}{1+e^x} = \frac{e^{-x}}{1+e^{-x}}$. $u = 1+e^{-x}$, $du = -e^{-x}dx$:

$-\int\frac{du}{u} = -\ln(1+e^{-x}) + C$.

**But also**: $-\ln(1+e^{-x}) = -\ln\frac{1+e^x}{e^x} = -[\ln(1+e^x) - \ln e^x] = x - \ln(1+e^x)$.

So $-\ln(1+e^{-x}) + C$ and $x - \ln(1+e^x) + C$ are the same function up to the constant. **Why two forms?** The "$1$" in $1+e^x$ can be written as $\frac{e^x}{e^x}$; different algebraic disguises of the same integrand lead to different-looking (but equal) antiderivatives. Always check by differentiating.

---

### A9. $\int_0^1 \frac{x}{1+x^4}\,dx$ — tracing the $\pi$.

$u = x^2$, $du = 2x\,dx$, bounds $0 \to 1$:

$\frac12\int_0^1\frac{du}{1+u^2} = \frac12[\arctan u]_0^1 = \frac12\left(\frac{\pi}{4}\right) = \frac{\pi}{8}$.

**Where $\pi$ comes from**: $\arctan 1 = \frac{\pi}{4}$ — the arctan dictionary entry $\int\frac{du}{1+u^2} = \arctan u$ injects the $\pi$. **Why $\frac{\pi}{8}$ not $\frac{\pi}{4}$**: the substitution's leftover $x\,dx = \frac{du}{2}$ contributes the factor $\frac12$ on top of $\arctan 1 = \frac{\pi}{4}$.

---

### A10. $\int_{-2}^{2}(x^5+x^3-3x)\,dx$ and friends.

**Net integral**: each term is odd, so on the symmetric interval $[-2,2]$ the areas cancel: $\int_{-2}^{2}(x^5+x^3-3x)\,dx = 0$.

**$\int_{-2}^{2}(x^2+x)\,dx$?** Not zero — $x^2$ is EVEN. Even parts double, odd parts vanish:

$\int_{-2}^{2}(x^2+x)\,dx = 2\int_0^2 x^2\,dx + 0 = 2\cdot\frac{8}{3} = \frac{16}{3} \neq 0$.

**Total area of $y = x^5$ on $[-2,2]$**: $x^5 < 0$ on $[-2,0]$ and $> 0$ on $[0,2]$, so total area $= 2\int_0^2 x^5\,dx = 2\cdot\frac{64}{6} = \frac{64}{3}$.

> **Rule of thumb**: odd → net zero on $[-a,a]$; even → double the half; "total area" always means absolute value — flip signs below the axis.

---

