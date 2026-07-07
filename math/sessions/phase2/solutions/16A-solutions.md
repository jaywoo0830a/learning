# Solutions — 16A: Integration Fundamentals

---

## Practice 1

$\int (4x^3 - 2x + 5)\,dx$

**Step 1**: Split at $+$ and $-$ signs.

$\int 4x^3\,dx - \int 2x\,dx + \int 5\,dx$

**Step 2**: Pull constants outside.

$4\int x^3\,dx - 2\int x\,dx + 5\int 1\,dx$

**Step 3**: Apply the power rule: $\int x^n\,dx = \frac{x^{n+1}}{n+1} + C$.

- $\int x^3\,dx = \frac{x^4}{4}$
- $\int x\,dx = \int x^1\,dx = \frac{x^2}{2}$
- $\int 1\,dx = \int x^0\,dx = x$

**Step 4**: Assemble and combine $+C$ (only one needed).

$4\cdot\frac{x^4}{4} - 2\cdot\frac{x^2}{2} + 5x + C = x^4 - x^2 + 5x + C$

**Check**: $\frac{d}{dx}(x^4 - x^2 + 5x + C) = 4x^3 - 2x + 5$. ✓

---

## Practice 2

$\int_0^2 (3x^2+1)\,dx$

**Step 1**: Find an antiderivative $F(x)$.

$F(x) = \int (3x^2+1)\,dx = 3\cdot\frac{x^3}{3} + x = x^3 + x$  (use $C=0$ — it cancels)

**Step 2**: Write with the vertical bar notation.

$\left[x^3 + x\right]_0^2$

**Step 3**: Plug upper bound $x=2$: $F(2) = 2^3 + 2 = 8 + 2 = 10$.

**Step 4**: Plug lower bound $x=0$: $F(0) = 0^3 + 0 = 0$.

**Step 5**: Subtract.

$F(2) - F(0) = 10 - 0 = \boxed{10}$

**Geometric interpretation**: The area under $y = 3x^2 + 1$ from $x=0$ to $x=2$ is 10 square units.

---

## Practice 3

$\int x\sqrt{x^2+4}\,dx$

**Step 1 — Choose $u$**: Priority 2: expression inside a root → $u = x^2 + 4$.

**Step 2 — Compute $du$**: $du = 2x\,dx$.

**Step 3 — Adjust for the constant**: We have $x\,dx$, but $du = 2x\,dx$.
Solve: $x\,dx = \frac{1}{2}du$.

**Step 4 — Replace all $x$'s**:
- $\sqrt{x^2+4} = \sqrt{u} = u^{1/2}$
- $x\,dx = \frac{1}{2}du$

The integral becomes: $\int u^{1/2} \cdot \frac{1}{2}\,du = \frac{1}{2}\int u^{1/2}\,du$.

**Step 5 — Integrate in $u$**:

$\frac{1}{2} \cdot \frac{u^{3/2}}{3/2} + C = \frac{1}{2} \cdot \frac{2}{3}u^{3/2} + C = \frac{1}{3}u^{3/2} + C$

**Step 6 — Substitute back** $u = x^2 + 4$:

$\boxed{\frac{1}{3}(x^2+4)^{3/2} + C}$

**Check**: $\frac{d}{dx}\left[\frac{1}{3}(x^2+4)^{3/2}\right] = \frac{1}{3} \cdot \frac{3}{2}(x^2+4)^{1/2} \cdot 2x = x\sqrt{x^2+4}$. ✓

---

## Practice 4

$\int_0^{\pi/2} \sin x \cos^2 x\,dx$

**Step 1 — Choose $u$**: Priority 5 (inside cosine) → $u = \cos x$.

**Step 2 — Compute $du$**: $du = -\sin x\,dx$, so $\sin x\,dx = -du$.

**Step 3 — Change the bounds** (definite integral):
- $x = 0 \to u = \cos 0 = 1$
- $x = \frac{\pi}{2} \to u = \cos\frac{\pi}{2} = 0$

**Step 4 — Replace and integrate**:

$\int_{u=1}^{u=0} u^2 \cdot (-du) = -\int_1^0 u^2\,du = \int_0^1 u^2\,du$

(The negative sign flipped the bounds: $-\int_1^0 = \int_0^1$)

**Step 5 — Evaluate**:

$\left[\frac{u^3}{3}\right]_0^1 = \frac{1}{3} - 0 = \boxed{\frac{1}{3}}$

**Alternative**: Keep $u = \sin x$ instead. Then $du = \cos x\,dx$. But we have $\cos^2 x = 1-\sin^2 x = 1-u^2$, so the integral is $\int u(1-u^2)\,du$, which is also valid but slightly more work. The $u = \cos x$ choice is cleaner here.

---

## Practice 5: Real Battle

$\int_{-2}^2 x^3\,dx$

**(a) Is the computation correct?**

Yes. $\int_{-2}^2 x^3\,dx = \left[\frac{x^4}{4}\right]_{-2}^2 = \frac{16}{4} - \frac{16}{4} = 4 - 4 = 0$. The FTC computation is correct.

**(b) Is the conclusion correct?**

**No.** The definite integral equals 0, but that does NOT mean "the area under $x^3$ from $-2$ to $2$ is zero." The definite integral computes **net signed area** — regions below the $x$-axis contribute negative values. There IS area there; the positive and negative parts simply cancel.

**(c) Compute the TOTAL area (treating all regions as positive) from $-2$ to $2$.**

$y = x^3$ is negative on $[-2,0]$ and positive on $[0,2]$. Total area:

$\text{Total area} = \int_{-2}^0 |x^3|\,dx + \int_0^2 |x^3|\,dx$

On $[-2,0]$, $x^3 \leq 0$, so $|x^3| = -x^3$.
On $[0,2]$, $x^3 \geq 0$, so $|x^3| = x^3$.

$= \int_{-2}^0 (-x^3)\,dx + \int_0^2 x^3\,dx$

$= -\left[\frac{x^4}{4}\right]_{-2}^0 + \left[\frac{x^4}{4}\right]_0^2$

$= -\left(0 - \frac{16}{4}\right) + \left(\frac{16}{4} - 0\right)$

$= -(-4) + 4 = 4 + 4 = \boxed{8}$

**Odd function insight**: $f(x) = x^3$ is an **odd function**: $f(-x) = -f(x)$. For any odd function integrated over a symmetric interval $[-a, a]$, the integral is always zero: $\int_{-a}^a f(x)\,dx = 0$. The negative half exactly cancels the positive half. This is why the signed area is zero even though there is clearly area on both sides. For total (unsigned) area, split at 0 and use absolute value.

---

## Basic Algebra Drill — Solutions

### D1. $\int x^5\,dx$

Power rule: bump exponent $5 \to 6$, divide by new exponent.

$\int x^5\,dx = \frac{x^6}{6} + C$

**Check**: $\frac{d}{dx}\left[\frac{x^6}{6}\right] = \frac{6x^5}{6} = x^5$. ✓

---

### D2. $\int \left(2e^x + \frac{3}{x}\right)\,dx$

Split and pull constants:

$= 2\int e^x\,dx + 3\int \frac{1}{x}\,dx$

Dictionary: $\int e^x\,dx = e^x + C$, $\int \frac{1}{x}\,dx = \ln|x| + C$.

$= 2e^x + 3\ln|x| + C$

---

### D3. $\int_1^4 \sqrt{x}\,dx$

Rewrite $\sqrt{x} = x^{1/2}$.

$\int_1^4 x^{1/2}\,dx = \left[\frac{x^{3/2}}{3/2}\right]_1^4 = \left[\frac{2}{3}x^{3/2}\right]_1^4$

$= \frac{2}{3}(4^{3/2}) - \frac{2}{3}(1^{3/2})$

$4^{3/2} = (\sqrt{4})^3 = 2^3 = 8$, $1^{3/2} = 1$.

$= \frac{2}{3} \cdot 8 - \frac{2}{3} \cdot 1 = \frac{16}{3} - \frac{2}{3} = \frac{14}{3}$

$\boxed{\frac{14}{3}}$

---

### D4. $\int_0^{\pi} \cos x\,dx$

Dictionary: $\int \cos x\,dx = \sin x + C$.

$\int_0^{\pi} \cos x\,dx = \Big[\sin x\Big]_0^{\pi} = \sin\pi - \sin 0 = 0 - 0 = \boxed{0}$

**Why zero?** $\cos x$ is positive on $[0, \pi/2]$ and negative on $[\pi/2, \pi]$. The signed areas cancel. This is not the same as "no area" — the total unsigned area is $\int_0^{\pi/2} \cos x\,dx + \int_{\pi/2}^{\pi} (-\cos x)\,dx = 1 + 1 = 2$.

---

### D5. $\int 3x^2(x^3+1)^4\,dx$

**Step 1**: $u = x^3 + 1$ (inside parentheses, raised to power).

**Step 2**: $du = 3x^2\,dx$.

$du$ matches $3x^2\,dx$ **exactly** — no constant adjustment needed!

**Step 3**: Replace: $(x^3+1)^4 \to u^4$, $3x^2\,dx \to du$.

$\int u^4\,du$

**Step 4**: Integrate: $\frac{u^5}{5} + C$.

**Step 5**: Back: $\boxed{\frac{(x^3+1)^5}{5} + C}$

**Check**: $\frac{d}{dx}\left[\frac{(x^3+1)^5}{5}\right] = \frac{5(x^3+1)^4 \cdot 3x^2}{5} = 3x^2(x^3+1)^4$. ✓

---

### D6. $\int e^{3x}\,dx$

**Step 1**: $u = 3x$ (priority 4: exponent of $e$).

**Step 2**: $du = 3\,dx$, so $dx = \frac{du}{3}$.

**Step 3**: Replace: $e^{3x} \to e^u$, $dx \to \frac{du}{3}$.

$\int e^u \cdot \frac{du}{3} = \frac{1}{3}\int e^u\,du$

**Step 4**: Integrate: $\frac{1}{3}e^u + C$.

**Step 5**: Back: $\boxed{\frac{1}{3}e^{3x} + C}$

**Shortcut (memorize)**: $\int e^{kx}\,dx = \frac{1}{k}e^{kx} + C$. The $1/k$ comes from dividing by the derivative of the exponent.

---

### D7. $\int \frac{x}{x^2+1}\,dx$

**Step 1**: $u = x^2 + 1$ (priority 3: denominator).

**Step 2**: $du = 2x\,dx$, so $x\,dx = \frac{du}{2}$.

**Step 3**: Replace: $\frac{1}{x^2+1} \to \frac{1}{u}$, $x\,dx \to \frac{du}{2}$.

$\int \frac{1}{u} \cdot \frac{du}{2} = \frac{1}{2}\int \frac{1}{u}\,du$

**Step 4**: Integrate: $\frac{1}{2}\ln|u| + C$.

**Step 5**: Back: $\boxed{\frac{1}{2}\ln(x^2+1) + C}$

(No absolute value needed on $x^2+1$ since it's always positive.)

---

### D8. $\int_0^1 xe^{x^2}\,dx$

**Step 1**: $u = x^2$ (priority 4: exponent of $e$).

**Step 2**: $du = 2x\,dx$, so $x\,dx = \frac{du}{2}$.

**Step 3 — Change bounds**:
- $x = 0 \to u = 0^2 = 0$
- $x = 1 \to u = 1^2 = 1$

**Step 4 — Replace**: $\int_{u=0}^{u=1} e^u \cdot \frac{du}{2} = \frac{1}{2}\int_0^1 e^u\,du$.

**Step 5 — Evaluate**:

$\frac{1}{2}\Big[e^u\Big]_0^1 = \frac{1}{2}(e^1 - e^0) = \boxed{\frac{e-1}{2}}$

---

### D9. $\int \frac{\cos x}{\sin x}\,dx$

**Step 1**: $u = \sin x$ (priority 3: denominator, $\frac{1}{\sin x}$).

**Step 2**: $du = \cos x\,dx$. Exact match!

**Step 3**: Replace: $\frac{1}{\sin x} \to \frac{1}{u}$, $\cos x\,dx \to du$.

$\int \frac{1}{u}\,du$

**Step 4**: Integrate: $\ln|u| + C$.

**Step 5**: Back: $\boxed{\ln|\sin x| + C}$

**Note**: This is also $-\ln|\csc x| + C$. Both are equivalent forms of the antiderivative of $\cot x$.

---

### D10. $\int_{-1}^2 (x^2 - 2x)\,dx$

**Step 1**: Find antiderivative.

$F(x) = \frac{x^3}{3} - 2\cdot\frac{x^2}{2} = \frac{x^3}{3} - x^2$

**Step 2**: Apply FTC.

$\left[\frac{x^3}{3} - x^2\right]_{-1}^2$

$F(2) = \frac{8}{3} - 4 = \frac{8}{3} - \frac{12}{3} = -\frac{4}{3}$

$F(-1) = \frac{-1}{3} - 1 = -\frac{1}{3} - \frac{3}{3} = -\frac{4}{3}$

$F(2) - F(-1) = -\frac{4}{3} - \left(-\frac{4}{3}\right) = \boxed{0}$

**Check**: $\int_{-1}^2 x(x-2)\,dx = 0$. The parabola $y = x^2-2x = x(x-2)$ has roots at $x=0$ and $x=2$. On $[-1, 0]$ it's positive, on $[0, 2]$ it's negative. The net signed area happens to be zero (but this is coincidental, not because of odd/even symmetry).

---

## Advanced Algebra Drill — Solutions

### A1. $\int x^2\sqrt{x^3+1}\,dx$

**Step 1**: $u = x^3 + 1$ (inside root).

**Step 2**: $du = 3x^2\,dx$, so $x^2\,dx = \frac{du}{3}$.

**Step 3**: Replace: $\sqrt{x^3+1} = \sqrt{u} = u^{1/2}$, $x^2\,dx \to \frac{du}{3}$.

$\int u^{1/2} \cdot \frac{du}{3} = \frac{1}{3}\int u^{1/2}\,du$

**Step 4**: Integrate:

$\frac{1}{3} \cdot \frac{u^{3/2}}{3/2} + C = \frac{1}{3} \cdot \frac{2}{3}u^{3/2} + C = \frac{2}{9}u^{3/2} + C$

**Step 5**: Back: $\boxed{\frac{2}{9}(x^3+1)^{3/2} + C}$

---

### A2. $\int \frac{e^x}{1+e^{2x}}\,dx$

**Step 1**: $u = e^x$ (then $e^{2x} = (e^x)^2 = u^2$).

**Step 2**: $du = e^x\,dx$. Exact match!

**Step 3**: Replace: $\frac{e^x}{1+e^{2x}} \to \frac{1}{1+u^2}$, $e^x\,dx \to du$.

$\int \frac{1}{1+u^2}\,du$

**Step 4**: Dictionary: $\int \frac{1}{1+u^2}\,du = \arctan u + C$.

**Step 5**: Back: $\boxed{\arctan(e^x) + C}$

---

### A3. $\int_0^4 \frac{x}{\sqrt{1+2x}}\,dx$

**Step 1**: $u = 1 + 2x$ (inside root).

**Step 2**: $du = 2\,dx$, so $dx = \frac{du}{2}$.
Also solve for $x$ in terms of $u$: $x = \frac{u-1}{2}$.

**Step 3 — Change bounds**:
- $x = 0 \to u = 1 + 0 = 1$
- $x = 4 \to u = 1 + 8 = 9$

**Step 4 — Replace**:

$\int_1^9 \frac{\frac{u-1}{2}}{\sqrt{u}} \cdot \frac{du}{2} = \int_1^9 \frac{u-1}{4\sqrt{u}}\,du = \frac{1}{4}\int_1^9 \frac{u-1}{u^{1/2}}\,du$

$= \frac{1}{4}\int_1^9 \left(u^{1/2} - u^{-1/2}\right)\,du$

**Step 5 — Integrate**:

$\frac{1}{4}\left[\frac{u^{3/2}}{3/2} - \frac{u^{1/2}}{1/2}\right]_1^9 = \frac{1}{4}\left[\frac{2}{3}u^{3/2} - 2u^{1/2}\right]_1^9$

**Step 6 — Evaluate at bounds**:

At $u=9$: $\frac{2}{3} \cdot 27 - 2 \cdot 3 = 18 - 6 = 12$
At $u=1$: $\frac{2}{3} \cdot 1 - 2 \cdot 1 = \frac{2}{3} - 2 = -\frac{4}{3}$

$\frac{1}{4}\left(12 - \left(-\frac{4}{3}\right)\right) = \frac{1}{4}\left(12 + \frac{4}{3}\right) = \frac{1}{4}\left(\frac{36}{3} + \frac{4}{3}\right) = \frac{1}{4} \cdot \frac{40}{3} = \boxed{\frac{10}{3}}$

---

### A4. $\int \sin^5 x \cos x\,dx$

**Step 1**: $u = \sin x$ (priority 5: inside a trig function raised to a power).

**Step 2**: $du = \cos x\,dx$. Exact match!

**Step 3**: Replace: $\sin^5 x \to u^5$, $\cos x\,dx \to du$.

$\int u^5\,du$

**Step 4**: Integrate: $\frac{u^6}{6} + C$.

**Step 5**: Back: $\boxed{\frac{\sin^6 x}{6} + C}$

---

### A5. $\int_1^e \frac{(\ln x)^2}{x}\,dx$

**Step 1**: $u = \ln x$ (priority 5: inside a function).

**Step 2**: $du = \frac{1}{x}\,dx$. Exact match!

**Step 3 — Change bounds**:
- $x = 1 \to u = \ln 1 = 0$
- $x = e \to u = \ln e = 1$

**Step 4 — Replace**: $\int_0^1 u^2\,du$.

**Step 5 — Evaluate**: $\left[\frac{u^3}{3}\right]_0^1 = \frac{1}{3} - 0 = \boxed{\frac{1}{3}}$

---

### A6. $F(x) = \int_0^x \sin(t^2)\,dt$. Find $F'(x)$.

**FTC Part 1**: $\frac{d}{dx}\int_a^x f(t)\,dt = f(x)$.

Here $f(t) = \sin(t^2)$, and the upper limit is just $x$ (not a function of $x$ with chain rule).

$F'(x) = \sin(x^2)$

$\boxed{F'(x) = \sin(x^2)}$

No integration needed — FTC Part 1 gives the answer directly.

---

### A7. $\int \frac{1}{x\ln x}\,dx$

**Rewrite**: $\int \frac{1}{x} \cdot \frac{1}{\ln x}\,dx$

**Step 1**: $u = \ln x$ (priority 5: inside $\ln$ — here it's the denominator).

**Step 2**: $du = \frac{1}{x}\,dx$. Exact match!

**Step 3**: Replace: $\frac{1}{x\ln x}\,dx = \frac{1}{\ln x} \cdot \frac{1}{x}\,dx \to \frac{1}{u}\,du$.

$\int \frac{1}{u}\,du$

**Step 4**: Integrate: $\ln|u| + C$.

**Step 5**: Back: $\boxed{\ln|\ln x| + C}$

**Domain note**: This is defined for $x > 0$, $x \neq 1$. When $x > 1$, $\ln x > 0$, so it's $\ln(\ln x) + C$. When $0 < x < 1$, $\ln x < 0$, so it's $\ln(-\ln x) + C$. The absolute value handles both cases.

---

### A8. $\int_0^{\pi/4} \tan x\,dx$

**Step 1 — Rewrite**: $\tan x = \frac{\sin x}{\cos x}$.

**Step 2 — $u$-sub**: $u = \cos x$ (denominator).

$du = -\sin x\,dx$, so $\sin x\,dx = -du$.

**Step 3 — Change bounds**:
- $x = 0 \to u = \cos 0 = 1$
- $x = \frac{\pi}{4} \to u = \cos\frac{\pi}{4} = \frac{\sqrt{2}}{2}$

**Step 4 — Replace**:

$\int_{u=1}^{u=\sqrt{2}/2} \frac{1}{u} \cdot (-du) = -\int_1^{\sqrt{2}/2} \frac{du}{u} = \int_{\sqrt{2}/2}^1 \frac{du}{u}$

**Step 5 — Evaluate**:

$\Big[\ln u\Big]_{\sqrt{2}/2}^1 = \ln 1 - \ln\left(\frac{\sqrt{2}}{2}\right) = 0 - \left(\ln\sqrt{2} - \ln 2\right)$

$= \ln 2 - \ln\sqrt{2} = \ln 2 - \frac{1}{2}\ln 2 = \frac{1}{2}\ln 2 = \boxed{\ln\sqrt{2}}$

**Alternative form**: $\frac{1}{2}\ln 2$ or $\ln\sqrt{2}$.

---

### A9. $\int_0^1 \frac{x}{1+x^4}\,dx$

**Step 1 — $u$-sub**: Notice $x^4 = (x^2)^2$. Let $u = x^2$.

**Step 2**: $du = 2x\,dx$, so $x\,dx = \frac{du}{2}$.

**Step 3 — Change bounds**:
- $x = 0 \to u = 0$
- $x = 1 \to u = 1$

**Step 4 — Replace**:

$\int_0^1 \frac{1}{1+u^2} \cdot \frac{du}{2} = \frac{1}{2}\int_0^1 \frac{du}{1+u^2}$

**Step 5 — Integrate**: $\frac{1}{2}\Big[\arctan u\Big]_0^1$

**Step 6 — Evaluate**: $\frac{1}{2}(\arctan 1 - \arctan 0) = \frac{1}{2}\left(\frac{\pi}{4} - 0\right) = \boxed{\frac{\pi}{8}}$

---

### A10. Prove $\int_{-a}^a \sin x\,dx = 0$ for any $a$ without computing.

**Proof using odd function property**:

$\sin x$ is an **odd function**: $\sin(-x) = -\sin x$ for all $x$.

For any odd function $f$ integrated over a symmetric interval $[-a, a]$:

$\int_{-a}^a f(x)\,dx = \int_{-a}^0 f(x)\,dx + \int_0^a f(x)\,dx$

In the first integral, substitute $u = -x$:
- $x = -a \to u = a$
- $x = 0 \to u = 0$
- $dx = -du$

$\int_{-a}^0 f(x)\,dx = \int_a^0 f(-u)(-du) = \int_a^0 (-f(u))(-du) = \int_a^0 f(u)\,du$

Since $f$ is odd: $f(-u) = -f(u)$. And $(-f(u))(-du) = f(u)\,du$.

$\int_a^0 f(u)\,du = -\int_0^a f(u)\,du$

Therefore:

$\int_{-a}^a f(x)\,dx = -\int_0^a f(x)\,dx + \int_0^a f(x)\,dx = \boxed{0}$

**Geometric meaning**: The area under $\sin x$ from $-a$ to $0$ (below the $x$-axis, signed negative) exactly cancels the area from $0$ to $a$ (above the $x$-axis, signed positive). Net signed area = 0. This holds for **any** odd function on **any** symmetric interval.
