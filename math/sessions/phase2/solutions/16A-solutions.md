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

### D1. $\int x^5\,dx$

Power rule: $\int x^n\,dx = \frac{x^{n+1}}{n+1} + C$.

$\int x^5\,dx = \frac{x^6}{6} + C$.

---

### D2. $\int (2e^x + \frac{3}{x})\,dx$

Split and pull constants:

$= 2\int e^x\,dx + 3\int \frac{1}{x}\,dx$

$= 2e^x + 3\ln|x| + C$

---

### D3. $\int_1^4 \sqrt{x}\,dx$

Rewrite: $\sqrt{x} = x^{1/2}$.

Antiderivative: $\int x^{1/2}\,dx = \frac{x^{3/2}}{3/2} + C = \frac{2}{3}x^{3/2} + C$.

FTC: $\left[\frac{2}{3}x^{3/2}\right]_1^4 = \frac{2}{3}(4^{3/2}) - \frac{2}{3}(1^{3/2})$

$4^{3/2} = (4^{1/2})^3 = 2^3 = 8$, $1^{3/2} = 1$.

$= \frac{2}{3} \cdot 8 - \frac{2}{3} \cdot 1 = \frac{16}{3} - \frac{2}{3} = \frac{14}{3}$

---

### D4. $\int_0^{\pi} \cos x\,dx$

Antiderivative: $\int \cos x\,dx = \sin x + C$.

FTC: $\left[\sin x\right]_0^{\pi} = \sin\pi - \sin 0 = 0 - 0 = 0$.

Net signed area is zero — the positive lobe on $[0, \pi/2]$ cancels the negative lobe on $[\pi/2, \pi]$.

---

### D5. $\int 3x^2(x^3+1)^4\,dx$

$u$-sub:

1. $u = x^3+1$ (priority 1 — inside parentheses raised to a power)
2. $du = 3x^2\,dx$ — **exact match** with $3x^2\,dx$ in the integrand!
3. Replace: $(x^3+1)^4 = u^4$, $3x^2\,dx = du$. Integral: $\int u^4\,du$.
4. Integrate: $\frac{u^5}{5} + C$.
5. Back: $\frac{(x^3+1)^5}{5} + C$.

**Check**: $\frac{d}{dx}\left[\frac{(x^3+1)^5}{5}\right] = \frac{5(x^3+1)^4}{5} \cdot 3x^2 = 3x^2(x^3+1)^4$. ✓

---

### D6. $\int e^{3x}\,dx$

$u = 3x$, $du = 3\,dx$ → $dx = \frac{du}{3}$.

$\int e^{3x}\,dx = \int e^u \cdot \frac{du}{3} = \frac{1}{3}\int e^u\,du = \frac{1}{3}e^u + C = \frac{1}{3}e^{3x} + C$.

---

### D7. $\int \frac{x}{x^2+1}\,dx$

$u = x^2+1$ (priority 3 — denominator), $du = 2x\,dx$ → $x\,dx = \frac{du}{2}$.

$\int \frac{x}{x^2+1}\,dx = \int \frac{1}{u} \cdot \frac{du}{2} = \frac{1}{2}\int \frac{1}{u}\,du = \frac{1}{2}\ln|u| + C = \frac{1}{2}\ln(x^2+1) + C$.

(No absolute value needed in the final answer since $x^2+1 > 0$ always, but it's harmless to include.)

---

### D8. $\int_0^1 xe^{x^2}\,dx$

$u = x^2$ (priority 4 — exponent of $e$), $du = 2x\,dx$ → $x\,dx = \frac{du}{2}$.

Change bounds: $x=0 \to u=0$, $x=1 \to u=1$.

$\int_0^1 xe^{x^2}\,dx = \int_0^1 e^u \cdot \frac{du}{2} = \frac{1}{2}\int_0^1 e^u\,du = \frac{1}{2}\left[e^u\right]_0^1 = \frac{1}{2}(e - 1)$.

---

### D9. $\int \frac{\cos x}{\sin x}\,dx$

$u = \sin x$, $du = \cos x\,dx$ — **exact match**.

$\int \frac{\cos x}{\sin x}\,dx = \int \frac{1}{u}\,du = \ln|u| + C = \ln|\sin x| + C$.

---

### D10. $\int_{-1}^2 (x^2-2x)\,dx$

Antiderivative: $F(x) = \frac{x^3}{3} - x^2$.

FTC:

$F(2) = \frac{8}{3} - 4 = \frac{8}{3} - \frac{12}{3} = -\frac{4}{3}$

$F(-1) = \frac{(-1)^3}{3} - (-1)^2 = -\frac{1}{3} - 1 = -\frac{4}{3}$

$\int_{-1}^2 (x^2-2x)\,dx = F(2) - F(-1) = -\frac{4}{3} - \left(-\frac{4}{3}\right) = 0$.

(Net signed area is zero — check: $x^2-2x = x(x-2)$ has roots at $0$ and $2$, so on $[-1,0]$ the parabola is above the axis (positive area) and on $[0,2]$ it's below (negative area). The areas happen to cancel over $[-1,2]$.)

---

### D11. Average value of $f(x)=\sin x$ on $[0,\pi]$.

$\bar f = \frac{1}{\pi}\int_0^\pi\sin x\,dx = \frac{1}{\pi}[-\cos x]_0^\pi = \frac{1}{\pi}(1+1) = \frac{2}{\pi}$.

> **Answer**: $\frac{2}{\pi}$

---

### D12. $\int \sec x\tan x\,dx$.

Dictionary: $\sec x\tan x \to \sec x$.

> **Answer**: $\sec x + C$

---

## Advanced Drills

### A1. $\int x^2\sqrt{x^3+1}\,dx$

$u = x^3+1$ (priority 2 — inside a root), $du = 3x^2\,dx$ → $x^2\,dx = \frac{du}{3}$.

$\int x^2\sqrt{x^3+1}\,dx = \int \sqrt{u} \cdot \frac{du}{3} = \frac{1}{3}\int u^{1/2}\,du$

$= \frac{1}{3} \cdot \frac{u^{3/2}}{3/2} + C = \frac{1}{3} \cdot \frac{2}{3}u^{3/2} + C = \frac{2}{9}(x^3+1)^{3/2} + C$.

---

### A2. $\int \frac{e^x}{1+e^{2x}}\,dx$

$u = e^x$, $du = e^x\,dx$ — **exact match**.

$\int \frac{e^x}{1+e^{2x}}\,dx = \int \frac{e^x}{1+(e^x)^2}\,dx = \int \frac{1}{1+u^2}\,du$

$= \arctan u + C = \arctan(e^x) + C$.

---

### A3. $\int_0^4 \frac{x}{\sqrt{1+2x}}\,dx$

$u = 1+2x$, then $du = 2\,dx$ → $dx = \frac{du}{2}$. Also solve for $x$: $x = \frac{u-1}{2}$.

Change bounds:
- $x=0 \to u = 1+0 = 1$
- $x=4 \to u = 1+8 = 9$

$\int_0^4 \frac{x}{\sqrt{1+2x}}\,dx = \int_1^9 \frac{(u-1)/2}{\sqrt{u}} \cdot \frac{du}{2} = \frac{1}{4}\int_1^9 \frac{u-1}{u^{1/2}}\,du$

$= \frac{1}{4}\int_1^9 (u^{1/2} - u^{-1/2})\,du = \frac{1}{4}\left[\frac{u^{3/2}}{3/2} - \frac{u^{1/2}}{1/2}\right]_1^9$

$= \frac{1}{4}\left[\frac{2}{3}u^{3/2} - 2u^{1/2}\right]_1^9$

Compute at $u=9$: $\frac{2}{3} \cdot 27 - 2 \cdot 3 = 18 - 6 = 12$.

At $u=1$: $\frac{2}{3} \cdot 1 - 2 \cdot 1 = \frac{2}{3} - 2 = -\frac{4}{3}$.

$= \frac{1}{4}\left(12 - \left(-\frac{4}{3}\right)\right) = \frac{1}{4}\left(12 + \frac{4}{3}\right) = \frac{1}{4}\left(\frac{36}{3} + \frac{4}{3}\right) = \frac{1}{4} \cdot \frac{40}{3} = \frac{10}{3}$.

---

### A4. $\int \sin^5 x\cos x\,dx$

$u = \sin x$, $du = \cos x\,dx$ — **exact match**.

$\int \sin^5 x\cos x\,dx = \int u^5\,du = \frac{u^6}{6} + C = \frac{\sin^6 x}{6} + C$.

**Check**: $\frac{d}{dx}\left[\frac{\sin^6 x}{6}\right] = \frac{6\sin^5 x}{6} \cdot \cos x = \sin^5 x\cos x$. ✓

---

### A5. $\int_1^e \frac{(\ln x)^2}{x}\,dx$

$u = \ln x$, $du = \frac{1}{x}\,dx$ — **exact match**.

Change bounds:
- $x = 1$ → $u = \ln 1 = 0$
- $x = e$ → $u = \ln e = 1$

$\int_1^e \frac{(\ln x)^2}{x}\,dx = \int_0^1 u^2\,du = \left[\frac{u^3}{3}\right]_0^1 = \frac{1}{3} - 0 = \frac{1}{3}$.

---

### A6. $F(x)=\int_0^x \sin(t^2)\,dt$. Find $F'(x)$.

FTC Part 1: $\frac{d}{dx}\int_a^x f(t)\,dt = f(x)$.

$F'(x) = \sin(x^2)$. No integration needed.

---

### A7. $\int \frac{1}{x\ln x}\,dx$

$u = \ln x$ (priority 5 — inside log), $du = \frac{1}{x}\,dx$ — **exact match**.

$\int \frac{1}{x\ln x}\,dx = \int \frac{1}{\ln x} \cdot \frac{1}{x}\,dx = \int \frac{1}{u}\,du = \ln|u| + C = \ln|\ln x| + C$.

(Valid for $x > 0$, $x \neq 1$.)

---

### A8. $\int_0^{\pi/4} \tan x\,dx$

Rewrite: $\tan x = \frac{\sin x}{\cos x}$.

$u = \cos x$ (priority 3 — denominator), $du = -\sin x\,dx$ → $\sin x\,dx = -du$.

Change bounds:
- $x = 0$ → $u = \cos 0 = 1$
- $x = \pi/4$ → $u = \cos(\pi/4) = \frac{\sqrt{2}}{2}$

$\int_0^{\pi/4} \tan x\,dx = \int_0^{\pi/4} \frac{\sin x}{\cos x}\,dx = \int_{u=1}^{u=\sqrt{2}/2} \frac{1}{u}(-du)$

$= -\int_1^{\sqrt{2}/2} \frac{1}{u}\,du = \int_{\sqrt{2}/2}^1 \frac{1}{u}\,du$ (flip bounds, sign flips)

$= \left[\ln|u|\right]_{\sqrt{2}/2}^1 = \ln 1 - \ln\left(\frac{\sqrt{2}}{2}\right) = 0 - \ln\left(\frac{\sqrt{2}}{2}\right)$

$= -\ln\left(\frac{\sqrt{2}}{2}\right) = \ln\left(\frac{2}{\sqrt{2}}\right) = \ln\sqrt{2} = \frac{1}{2}\ln 2$.

---

### A9. $\int_0^1 \frac{x}{1+x^4}\,dx$

$u = x^2$, $du = 2x\,dx$ → $x\,dx = \frac{du}{2}$.

Change bounds:
- $x = 0$ → $u = 0$
- $x = 1$ → $u = 1$

$\int_0^1 \frac{x}{1+x^4}\,dx = \int_0^1 \frac{x}{1+(x^2)^2}\,dx = \int_0^1 \frac{1}{1+u^2} \cdot \frac{du}{2} = \frac{1}{2}\int_0^1 \frac{1}{1+u^2}\,du$

$= \frac{1}{2}\left[\arctan u\right]_0^1 = \frac{1}{2}(\arctan 1 - \arctan 0) = \frac{1}{2}\left(\frac{\pi}{4} - 0\right) = \frac{\pi}{8}$.

---

### A10. Prove $\int_{-a}^a \sin x\,dx = 0$ for any $a$

**Direct computation**:

$\int_{-a}^a \sin x\,dx = [-\cos x]_{-a}^a = (-\cos a) - (-\cos(-a))$

Since $\cos$ is even: $\cos(-a) = \cos a$.

$= -\cos a + \cos a = 0$.

**By odd function property**: $\sin(-x) = -\sin x$, so $\sin x$ is odd.

For any odd function $f$: $\int_{-a}^a f(x)\,dx = 0$.

Geometrically, the area on $[-a, 0]$ is the mirror image (below the axis) of the area on $[0, a]$ (above the axis), so they cancel exactly. The **net signed area** is zero — but the **total area** (absolute value) is $2\int_0^a \sin x\,dx = 2(1-\cos a)$, which is nonzero for $a \neq 2\pi k$.

---

