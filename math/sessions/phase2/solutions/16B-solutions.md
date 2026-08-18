# Solutions — 16B: Advanced Integration

> Back to [16B — Advanced Integration](../16B-advanced-integration.md)

---

## Practice 1

$\int x\sin x\,dx$

Run the parts algorithm. LIATE: **A**lgebraic ($x$) beats **T**rig ($\sin x$).

| Step | Action |
|:---:|:---|
| 1 | $u = x$ (Algebraic) |
| 2 | $dv = \sin x\,dx$ |
| 3 | $du = dx$ |
| 4 | $v = \int \sin x\,dx = -\cos x$ |
| 5 | $uv - \int v\,du = -x\cos x - \int (-\cos x)\,dx$ |
| 6 | $= -x\cos x + \int \cos x\,dx = -x\cos x + \sin x + C$ |

**Check**: $\frac{d}{dx}(-x\cos x + \sin x) = -\cos x + x\sin x + \cos x = x\sin x$. ✓

---

## Practice 2

$\int \cos^3 x\,dx$

$n=3$ (odd power of cosine). Follow the "n odd" branch:

1. **Peel**: $\cos^3 x = \cos x \cdot \cos^2 x$.
2. **Convert**: $\cos^2 x = 1 - \sin^2 x$. So $\cos^3 x = \cos x(1-\sin^2 x)$.
3. **$u$-sub**: $u = \sin x$, $du = \cos x\,dx$ — **exact match**.

$\int \cos^3 x\,dx = \int \cos x(1-\sin^2 x)\,dx = \int (1-u^2)\,du$

4. **Integrate**: $u - \frac{u^3}{3} + C$.
5. **Back**: $\sin x - \frac{\sin^3 x}{3} + C$.

**Check**: $\frac{d}{dx}(\sin x - \frac{\sin^3 x}{3}) = \cos x - \sin^2 x\cos x = \cos x(1-\sin^2 x) = \cos x\cos^2 x = \cos^3 x$. ✓

---

## Practice 3

$\int \frac{dx}{x^2+4}$

### Method 1: Arctan formula directly

$\int \frac{dx}{x^2+a^2} = \frac{1}{a}\arctan\left(\frac{x}{a}\right) + C$.

Here $a=2$: $\int \frac{dx}{x^2+4} = \frac{1}{2}\arctan\left(\frac{x}{2}\right) + C$.

### Method 2: Trig sub $x = 2\tan\theta$

Form: $x^2+4 = x^2+2^2$ → $x=2\tan\theta$.

1. $x = 2\tan\theta$, $dx = 2\sec^2\theta\,d\theta$.
2. $x^2+4 = 4\tan^2\theta+4 = 4(\tan^2\theta+1) = 4\sec^2\theta$.
3. Integral: $\int \frac{2\sec^2\theta\,d\theta}{4\sec^2\theta} = \int \frac{1}{2}\,d\theta = \frac{\theta}{2} + C$.
4. Back-substitute: $\theta = \arctan(x/2)$ → $\frac{1}{2}\arctan\left(\frac{x}{2}\right) + C$.

Both methods give the same answer. The arctan formula is faster.

---

## Practice 4

$\int \frac{x+1}{x^2-3x+2}\,dx$

**Step 1**: Factor denominator: $x^2-3x+2 = (x-1)(x-2)$.

Degree check: numerator degree (1) < denominator degree (2). No division needed.

**Step 2**: Template for distinct linear factors:

$\frac{x+1}{(x-1)(x-2)} = \frac{A}{x-1} + \frac{B}{x-2}$

**Step 3**: Clear denominators: $x+1 = A(x-2) + B(x-1)$.

**Step 4**: Solve by plugging roots:
- Plug $x=1$: $1+1 = A(1-2) + B(0)$ → $2 = -A$ → $A = -2$.
- Plug $x=2$: $2+1 = A(0) + B(2-1)$ → $3 = B$ → $B = 3$.

(Alternative — match coefficients: $x+1 = (A+B)x + (-2A-B)$. So $A+B=1$, $-2A-B=1$. From first: $B=1-A$. Plug into second: $-2A-(1-A)=1$ → $-A-1=1$ → $A=-2$, $B=3$. Both methods agree.)

**Step 5**: Integrate:

$\int \frac{x+1}{x^2-3x+2}\,dx = \int \left(\frac{-2}{x-1} + \frac{3}{x-2}\right)dx$

$= -2\ln|x-1| + 3\ln|x-2| + C = \ln\left|\frac{(x-2)^3}{(x-1)^2}\right| + C$.

---

## Practice 5: Real Battle (Constructive)

**(a) $\int \frac{x}{\sqrt{1-x^2}}\,dx$ — is there a faster way?**

Yes! $u$-sub is much faster. Let $u = 1-x^2$, $du = -2x\,dx$ → $x\,dx = -\frac{du}{2}$.

$\int \frac{x}{\sqrt{1-x^2}}\,dx = \int \frac{1}{\sqrt{u}} \cdot \left(-\frac{du}{2}\right) = -\frac{1}{2}\int u^{-1/2}\,du$

$= -\frac{1}{2} \cdot \frac{u^{1/2}}{1/2} + C = -\sqrt{u} + C = -\sqrt{1-x^2} + C$.

Trig sub would also work but takes much longer.

**(b) $\int \frac{1}{\sqrt{1-x^2}}\,dx$ — was trig sub the right call?**

Trig sub is perfect here — there's no $x$ in the numerator to absorb into $du$:

$x = \sin\theta$, $dx = \cos\theta\,d\theta$. $\sqrt{1-x^2} = \cos\theta$.

$\int \frac{1}{\sqrt{1-x^2}}\,dx = \int \frac{\cos\theta\,d\theta}{\cos\theta} = \int d\theta = \theta + C = \arcsin x + C$.

A $u$-sub would fail because there's no $x\,dx$ to match $du$ for $u=1-x^2$. Trig sub is indeed the right call.

**(c) One-sentence rule**:

> When $\sqrt{a^2-x^2}$ appears, try $u$-sub ($u=a^2-x^2$) first if there's an $x$ in the numerator to make $du$; if the numerator has no $x$ (or the $x$ doesn't help), use trig sub $x=a\sin\theta$.

---

## Basic Drills

### B1. $\int x\cos x\,dx$

Parts: LIATE → $u=x$ (Algebraic), $dv=\cos x\,dx$.

| Step | Action |
|:---:|:---|
| 1-2 | $u = x$, $dv = \cos x\,dx$ |
| 3 | $du = dx$ |
| 4 | $v = \sin x$ |
| 5-6 | $uv - \int v\,du = x\sin x - \int \sin x\,dx = x\sin x + \cos x + C$ |

**Check**: $\frac{d}{dx}(x\sin x + \cos x) = \sin x + x\cos x - \sin x = x\cos x$. ✓

---

### B2. $\int \ln(2x)\,dx$

Parts: LIATE → $u=\ln(2x)$ (Log — highest priority), $dv=dx$.

First, simplify: $\ln(2x) = \ln 2 + \ln x$. But we can also do parts directly.

| Step | Action |
|:---:|:---|
| 1-2 | $u = \ln(2x)$, $dv = dx$ |
| 3 | $du = \frac{1}{x}\,dx$ |
| 4 | $v = x$ |
| 5-6 | $x\ln(2x) - \int x \cdot \frac{1}{x}\,dx = x\ln(2x) - \int 1\,dx = x\ln(2x) - x + C$ |

Alternative using $\ln(2x) = \ln 2 + \ln x$:

$\int \ln(2x)\,dx = \int (\ln 2 + \ln x)\,dx = x\ln 2 + (x\ln x - x) + C = x(\ln 2 + \ln x) - x + C = x\ln(2x) - x + C$. Same answer.

---

### B3. $\int \sin^2 x\,dx$

Even power → half-angle formula: $\sin^2 x = \frac{1-\cos 2x}{2}$.

$\int \sin^2 x\,dx = \int \frac{1-\cos 2x}{2}\,dx = \frac{1}{2}\int (1-\cos 2x)\,dx$

$= \frac{1}{2}\left(x - \frac{\sin 2x}{2}\right) + C = \frac{x}{2} - \frac{\sin 2x}{4} + C$.

---

### B4. $\int \tan x\sec^2 x\,dx$

Tan/sec: $n=2$ (even) → save $\sec^2 x$, $u = \tan x$.

$u = \tan x$, $du = \sec^2 x\,dx$ — **exact match**.

$\int \tan x\sec^2 x\,dx = \int u\,du = \frac{u^2}{2} + C = \frac{\tan^2 x}{2} + C$.

(Equivalently, $\frac{\sec^2 x}{2} + C$ since $\tan^2 x = \sec^2 x - 1$ — the constants differ by $-\frac{1}{2}$, which is absorbed into $+C$.)

---

### B5. $\int \frac{dx}{\sqrt{9-x^2}}$

Form: $\sqrt{9-x^2} = \sqrt{3^2-x^2}$ → $x = 3\sin\theta$.

1. $x = 3\sin\theta$, $dx = 3\cos\theta\,d\theta$.
2. $\sqrt{9-x^2} = \sqrt{9-9\sin^2\theta} = 3\cos\theta$.
3. Integral: $\int \frac{3\cos\theta\,d\theta}{3\cos\theta} = \int d\theta = \theta + C$.
4. Back-substitute: $\theta = \arcsin(x/3)$.

$\int \frac{dx}{\sqrt{9-x^2}} = \arcsin\left(\frac{x}{3}\right) + C$.

---

### B6. $\int \frac{dx}{x^2+9}$

Arctan formula: $\int \frac{dx}{x^2+a^2} = \frac{1}{a}\arctan\left(\frac{x}{a}\right) + C$.

$a = 3$: $\int \frac{dx}{x^2+9} = \frac{1}{3}\arctan\left(\frac{x}{3}\right) + C$.

---

### B7. $\int \frac{1}{x^2-x}\,dx$

Factor denominator: $x^2-x = x(x-1)$.

Template (distinct linear): $\frac{1}{x(x-1)} = \frac{A}{x} + \frac{B}{x-1}$.

Clear: $1 = A(x-1) + Bx$.

Plug roots:
- $x=0$: $1 = -A$ → $A = -1$.
- $x=1$: $1 = B$ → $B = 1$.

Integrate:

$\int \frac{1}{x^2-x}\,dx = \int \left(\frac{-1}{x} + \frac{1}{x-1}\right)dx = -\ln|x| + \ln|x-1| + C = \ln\left|\frac{x-1}{x}\right| + C$.

---

### B8. $\int x^2 e^x\,dx$

Parts twice. LIATE: $u = x^2$ (Algebraic), $dv = e^x\,dx$.

**Round 1**:

| Step | Value |
|:---:|:---|
| $u$ | $x^2$ |
| $dv$ | $e^x\,dx$ |
| $du$ | $2x\,dx$ |
| $v$ | $e^x$ |
| Result | $x^2 e^x - \int 2x e^x\,dx = x^2 e^x - 2\int x e^x\,dx$ |

**Round 2** for $\int x e^x\,dx$ (LIATE: $u=x$, $dv=e^x\,dx$):

$= x e^x - \int e^x\,dx = x e^x - e^x + C_1$.

**Combine**:

$\int x^2 e^x\,dx = x^2 e^x - 2(x e^x - e^x) + C = e^x(x^2 - 2x + 2) + C$.

**Check**: $\frac{d}{dx}[e^x(x^2-2x+2)] = e^x(x^2-2x+2) + e^x(2x-2) = e^x(x^2) = x^2 e^x$. ✓

---

### B9. $\int \sin x\cos x\,dx$

### Method 1: $u = \sin x$

$u = \sin x$, $du = \cos x\,dx$ — **exact match**.

$\int \sin x\cos x\,dx = \int u\,du = \frac{u^2}{2} + C = \frac{\sin^2 x}{2} + C$.

### Method 2: Double-angle identity

$\sin 2x = 2\sin x\cos x$ → $\sin x\cos x = \frac{\sin 2x}{2}$.

$\int \sin x\cos x\,dx = \int \frac{\sin 2x}{2}\,dx = \frac{1}{2}\int \sin 2x\,dx$

$u = 2x$, $du = 2\,dx$ → $\frac{1}{2} \cdot \left(-\frac{\cos 2x}{2}\right) + C = -\frac{\cos 2x}{4} + C$.

### Verify answers match

Use $\cos 2x = 1 - 2\sin^2 x$:

$-\frac{\cos 2x}{4} = -\frac{1-2\sin^2 x}{4} = -\frac{1}{4} + \frac{\sin^2 x}{2}$.

$-\frac{1}{4} + \frac{\sin^2 x}{2} + C = \frac{\sin^2 x}{2} + \left(C - \frac{1}{4}\right)$.

The constants differ by $-\frac{1}{4}$, which is absorbed into $+C$. Both answers are equivalent. ✓

---

### B10. $\int \frac{x}{\sqrt{1-x^2}}\,dx$

Decision: $u$-sub is faster (see Practice 5a).

$u = 1-x^2$, $du = -2x\,dx$ → $x\,dx = -\frac{du}{2}$.

$\int \frac{x}{\sqrt{1-x^2}}\,dx = \int u^{-1/2} \cdot \left(-\frac{du}{2}\right) = -\frac{1}{2}\int u^{-1/2}\,du$

$= -\frac{1}{2} \cdot \frac{u^{1/2}}{1/2} + C = -u^{1/2} + C = -\sqrt{1-x^2} + C$.

---

### B11. $\int \frac{dx}{x^2+6x+13}$.

Complete the square: $x^2+6x+13 = (x+3)^2+4$.

Let $u=x+3$: $\int\frac{du}{u^2+4} = \frac{1}{2}\arctan\frac{u}{2}+C = \frac{1}{2}\arctan\frac{x+3}{2}+C$.

> **Answer**: $\frac{1}{2}\arctan\frac{x+3}{2}+C$

---

### B12. $\int \sec x\,dx$.

Multiply by $\frac{\sec x+\tan x}{\sec x+\tan x}$:

$\int\sec x\,dx = \int\frac{\sec^2 x+\sec x\tan x}{\sec x+\tan x}\,dx$. With $u=\sec x+\tan x$ (the numerator is $du$):

$= \ln|\sec x+\tan x| + C$.

> **Answer**: $\ln|\sec x+\tan x|+C$

---

## Calculation Drills

### C1. $\int \frac{5x+7}{x^2+x-2}\,dx$

Factor: $x^2+x-2 = (x+2)(x-1)$. Cover-up:
- at $x=1$: $\frac{5+7}{1+2} = 4$ → $\frac{4}{x-1}$.
- at $x=-2$: $\frac{-10+7}{-2-1} = 1$ → $\frac{1}{x+2}$.

$\int\left(\frac4{x-1}+\frac1{x+2}\right)dx = 4\ln|x-1| + \ln|x+2| + C$.

> **Answer**: $4\ln|x-1| + \ln|x+2| + C$

---

### C2. $\int x^2\ln x\,dx$

Parts: $u = \ln x$, $dv = x^2\,dx$ ($du = \frac{dx}{x}$, $v = \frac{x^3}{3}$):

$\frac{x^3}{3}\ln x - \int\frac{x^3}{3}\cdot\frac1x\,dx = \frac{x^3\ln x}{3} - \frac13\int x^2\,dx = \frac{x^3\ln x}{3} - \frac{x^3}{9} + C = \frac{x^3}{9}(3\ln x - 1) + C$.

> **Answer**: $\frac{x^3}{9}(3\ln x - 1) + C$

---

### C3. $\int_0^{\pi/2} x\cos x\,dx$

Parts: $u = x$, $dv = \cos x\,dx$ ($v = \sin x$):

$\left[x\sin x\right]_0^{\pi/2} - \int_0^{\pi/2}\sin x\,dx = \frac{\pi}{2} - \left[-\cos x\right]_0^{\pi/2} = \frac{\pi}{2} - 1$.

> **Answer**: $\frac{\pi}{2} - 1$

---

### C4. $\int \tan^3 x\sec^4 x\,dx$

Save one $\sec^2 x$ for $du$; $u = \tan x$, $du = \sec^2 x\,dx$, $\sec^2 x = 1+\tan^2 x$:

$\int\tan^3 x\sec^2 x\cdot\sec^2 x\,dx = \int u^3(1+u^2)\,du = \frac{u^4}{4} + \frac{u^6}{6} = \frac{\tan^4 x}{4} + \frac{\tan^6 x}{6} + C$.

> **Answer**: $\frac{\tan^4 x}{4} + \frac{\tan^6 x}{6} + C$

---

### C5. $\int_0^{\pi/2}\sin^4 x\cos^3 x\,dx$

$\cos$ power is odd → peel one: $\sin^4 x(1-\sin^2 x)\cos x$. $u = \sin x$, bounds $0\to1$:

$\int_0^1 u^4(1-u^2)\,du = \frac15 - \frac17 = \frac{2}{35}$.

> **Answer**: $\frac{2}{35}$

---

### C6. $\int \frac{dx}{(x^2+1)^{3/2}}$

Trig sub (form $\sqrt{x^2+1}$): $x = \tan\theta$, $dx = \sec^2\theta\,d\theta$, $x^2+1 = \sec^2\theta$:

$\int\frac{\sec^2\theta}{\sec^3\theta}\,d\theta = \int\cos\theta\,d\theta = \sin\theta$.

Triangle ($\tan\theta = x/1$): $\sin\theta = \frac{x}{\sqrt{x^2+1}}$.

> **Answer**: $\frac{x}{\sqrt{x^2+1}} + C$

---

### C7. $\int \frac{x^2}{\sqrt{4-x^2}}\,dx$

Trig sub (form $\sqrt{4-x^2}$): $x = 2\sin\theta$, $dx = 2\cos\theta\,d\theta$, $\sqrt{4-x^2} = 2\cos\theta$:

$\int\frac{4\sin^2\theta}{2\cos\theta}\cdot 2\cos\theta\,d\theta = \int 4\sin^2\theta\,d\theta = 2\theta - \sin 2\theta = 2\theta - 2\sin\theta\cos\theta$.

Back-sub ($\sin\theta = x/2$, $\cos\theta = \frac{\sqrt{4-x^2}}{2}$, $\theta = \arcsin\frac{x}{2}$):

$= 2\arcsin\frac{x}{2} - \frac{x\sqrt{4-x^2}}{2} + C$.

> **Answer**: $2\arcsin\frac{x}{2} - \frac{x\sqrt{4-x^2}}{2} + C$

---

### C8. $\int e^{2x}\sin 3x\,dx$

Cycling parts, or the formula $\int e^{ax}\sin(bx)\,dx = \frac{e^{ax}}{a^2+b^2}(a\sin bx - b\cos bx)$ with $a=2, b=3$:

$\int e^{2x}\sin 3x\,dx = \frac{e^{2x}}{13}(2\sin 3x - 3\cos 3x) + C$.

**Check**: derivative $= \frac{e^{2x}}{13}\left[2(2\sin3x-3\cos3x) + 3(2\cos3x+3\sin3x)\right] = e^{2x}\sin 3x$ ✓

> **Answer**: $\frac{e^{2x}}{13}(2\sin 3x - 3\cos 3x) + C$

---

### C9. $\int \frac{3x^2+4x+3}{(x+1)(x^2+1)}\,dx$

Template: $\frac{A}{x+1}+\frac{Bx+C}{x^2+1}$:

$3x^2+4x+3 = A(x^2+1) + (Bx+C)(x+1)$
$= (A+B)x^2 + (B+C)x + (A+C)$.

Match: $A+B=3$, $B+C=4$, $A+C=3$ → $A=1$, $B=2$, $C=2$.

$\int\left(\frac1{x+1} + \frac{2x}{x^2+1} + \frac{2}{x^2+1}\right)dx = \ln|x+1| + \ln(x^2+1) + 2\arctan x + C$.

> **Answer**: $\ln|x+1| + \ln(x^2+1) + 2\arctan x + C$

---

### C10. $\int_0^1 x\arctan x\,dx$

Parts: $u = \arctan x$, $dv = x\,dx$ ($du = \frac{dx}{1+x^2}$, $v = \frac{x^2}{2}$):

$\left[\frac12(x^2+1)\arctan x - \frac{x}{2}\right]_0^1 = \frac12(2)\cdot\frac{\pi}{4} - \frac12 - 0 = \frac{\pi}{4} - \frac12$.

> **Answer**: $\frac{\pi}{4} - \frac12$

---

## Advanced Drills

### A1. $\int e^x\cos x\,dx$ — which side do you cycle?

Cycling integral. $I = \int e^x\cos x\,dx$.

**Round 1**: $u = \cos x$, $dv = e^x\,dx$ (LIATE: Trig before Exp, so $u = \cos x$). $du = -\sin x\,dx$, $v = e^x$.

$I = e^x\cos x - \int e^x(-\sin x)\,dx = e^x\cos x + \int e^x\sin x\,dx$.

**Round 2**: for $\int e^x\sin x\,dx$, $u = \sin x$, $dv = e^x\,dx$: $= e^x\sin x - \int e^x\cos x\,dx = e^x\sin x - I$.

**Combine**: $I = e^x\cos x + e^x\sin x - I$ → $2I = e^x(\cos x + \sin x)$ → $I = \frac{e^x}{2}(\cos x + \sin x) + C$.

**Check**: $\frac{d}{dx}\left[\frac{e^x}{2}(\cos x+\sin x)\right] = \frac{e^x}{2}(\cos x+\sin x) + \frac{e^x}{2}(-\sin x+\cos x) = e^x\cos x$. ✓

**Why it works / why either choice is fine**: $e^x$ recycles under integration ($\int e^x = e^x$) and $\cos x$ recycles under repeated parts — so after two rounds you're back to $I$ with the pieces flipped, and $I$ appears on both sides. Choosing $u = e^x$ instead just flips the order; the same $2I$ equation results. **LIATE only decides which piece sits in $u$; it cannot break the cycle — it just tells you the answer won't get uglier.**

---

### A2. $\int \sin^4 x\,dx$, and $\int \cos^4 x\,dx$ — the $n=4$ pattern.

Half-angle twice: $\sin^4 x = \left(\frac{1-\cos 2x}{2}\right)^2 = \frac14(1 - 2\cos 2x + \cos^2 2x) = \frac14\left(1 - 2\cos 2x + \frac{1+\cos 4x}{2}\right)$

$= \frac38 - \frac12\cos 2x + \frac18\cos 4x$.

$\int \sin^4 x\,dx = \frac{3x}{8} - \frac{\sin 2x}{4} + \frac{\sin 4x}{32} + C$.

**Same pattern for $\cos^4 x$**: $\cos^4 x = \frac38 + \frac12\cos 2x + \frac18\cos 4x$, so $\int \cos^4 x\,dx = \frac{3x}{8} + \frac{\sin 2x}{4} + \frac{\sin 4x}{32} + C$ — only the middle sign flips.

**General pattern for even $n$**: $\int_0^{\pi/2}\sin^n x\,dx = \frac{n-1}{n}\cdot\frac{n-3}{n-2}\cdots\frac12\cdot\frac{\pi}{2}$.
- $n=2$: $\frac12\cdot\frac{\pi}{2} = \frac{\pi}{4}$
- $n=4$: $\frac34\cdot\frac12\cdot\frac{\pi}{2} = \frac{3\pi}{16}$

On $[0,\pi/2]$, $\sin$ and $\cos$ give identical values (they are mirrors), so $\int_0^{\pi/2}\cos^4 x\,dx = \frac{3\pi}{16}$ too. **Spot the pattern once, and you never grind through half-angle again.**

---

### A3. $\int \frac{dx}{(x^2+1)^2}$ — and find $C$ with $\int_0^1 = \frac{\pi}{8} + C$.

Trig sub $x = \tan\theta$ (form $\sqrt{x^2+1}$, $a=1$):

1. $dx = \sec^2\theta\,d\theta$; $x^2+1 = \sec^2\theta$ → $(x^2+1)^2 = \sec^4\theta$.
2. $\int \frac{\sec^2\theta\,d\theta}{\sec^4\theta} = \int \cos^2\theta\,d\theta = \frac{\theta}{2} + \frac{\sin 2\theta}{4} + C_1$.
3. Back-substitute with the right triangle ($x = \tan\theta$: opposite $x$, adjacent $1$, hypotenuse $\sqrt{x^2+1}$): $\theta = \arctan x$, $\sin 2\theta = 2\cdot\frac{x}{\sqrt{x^2+1}}\cdot\frac{1}{\sqrt{x^2+1}} = \frac{2x}{x^2+1}$.

$\int \frac{dx}{(x^2+1)^2} = \frac12\arctan x + \frac{x}{2(x^2+1)} + C$.

**Find $C$**: $\int_0^1 = \left[\frac12\arctan x + \frac{x}{2(x^2+1)}\right]_0^1 = \frac12\cdot\frac{\pi}{4} + \frac{1}{2\cdot2} = \frac{\pi}{8} + \frac14$.

So $C = \frac14$: $\int_0^1\frac{dx}{(x^2+1)^2} = \frac{\pi}{8} + \frac14$.

**How you knew**: read off the two "clean" pieces — $\arctan 1 = \frac{\pi}{4}$ (halved by the leading $\frac12$) and the algebraic part $\frac{x}{2(x^2+1)}$ at $x=1$ is exactly $\frac14$. **The bound $1$ was chosen so both pieces land on values you can compute in your head.**

---

### A4. $\int \frac{x^3}{\sqrt{x^2+1}}\,dx$, then $\int \frac{x^5}{\sqrt{x^2+1}}\,dx$ — the odd-power pattern.

**$x^3$**: $u = x^2+1$, $du = 2x\,dx$; solve $x^2 = u-1$:

$\int\frac{x^2\cdot x\,dx}{\sqrt{u}} = \frac12\int\frac{u-1}{u^{1/2}}\,du = \frac12\left(\frac{2}{3}u^{3/2} - 2u^{1/2}\right) = \frac13 u^{3/2} - u^{1/2} + C$

$= \frac13(x^2+1)^{3/2} - \sqrt{x^2+1} + C = \frac{\sqrt{x^2+1}}{3}(x^2-2) + C$.

**$x^5$**: same trick, but $x^5 = x\cdot x^4 = x(u-1)^2$:

$\frac12\int\frac{(u-1)^2}{u^{1/2}}\,du = \frac12\int(u^{3/2} - 2u^{1/2} + u^{-1/2})\,du = \frac15 u^{5/2} - \frac23 u^{3/2} + u^{1/2} + C$

$= \frac15(x^2+1)^{5/2} - \frac23(x^2+1)^{3/2} + \sqrt{x^2+1} + C$.

**Pattern**: $x^3$ → power $\frac32$; $x^5$ → powers $\frac52, \frac32, \frac12$. Each extra $x^2$ in the numerator costs one more term in the answer, generated by expanding $(u-1)^k$. **Peel one $x$ for $du$, expand the rest as powers of $u-1$ — you never need trig sub for odd powers.**

---

### A5. $\int \frac{x^2+2x-1}{(x-1)(x^2+1)}\,dx$ — the $B=0$ surprise.

Template: $\frac{x^2+2x-1}{(x-1)(x^2+1)} = \frac{A}{x-1} + \frac{Bx+C}{x^2+1}$.

Clear: $x^2+2x-1 = A(x^2+1) + (Bx+C)(x-1)$.

Match coefficients:
- $x^2$: $A+B = 1$
- $x$: $C-B = 2$
- const: $A-C = -1$

From the last two, $A = C-1$, $C = B+2$ → $(B+1)+B = 1$ → $B=0$, then $C=2$, $A=1$.

$\int = \int\frac{dx}{x-1} + \int\frac{2\,dx}{x^2+1} = \ln|x-1| + 2\arctan x + C$.

**Check by cover-up at $x=0$**: LHS $= \frac{-1}{(-1)(1)} = 1$; RHS $= \frac{1}{-1} + \frac{2}{1} = 1$ ✓.

**Why $B=0$ surprises you (and why it shouldn't)**: the numerator is *linear-free* in the quadratic part — after division, no genuine $Bx$ survives. **Whenever $B=0$ appears, plug in one convenient $x$ (like $x=0$) to confirm before trusting the algebra.**

---

### A6. $\int \arctan x\,dx$, and $\int x\arctan x\,dx$ — why the $\frac12\ln$?

Parts on $\arctan x$ (Inverse trig first):

| $u$ | $dv$ | $du$ | $v$ |
|:---:|:---:|:---:|:---:|
| $\arctan x$ | $dx$ | $\frac{dx}{1+x^2}$ | $x$ |

$\int \arctan x\,dx = x\arctan x - \int\frac{x}{1+x^2}\,dx = x\arctan x - \frac12\ln(1+x^2) + C$.

**Why the $\frac12$**: the leftover integral is a $\frac{P'}{P}$ form — $d(1+x^2) = 2x\,dx$, so the numerator $x$ is only *half* a derivative. The factor $\frac12$ is the $2$ from $2x$ being divided out, exactly like A6 in 16A.

**$x\arctan x$**: parts again, $u = \arctan x$, $dv = x\,dx$:

$\frac{x^2}{2}\arctan x - \frac12\int\frac{x^2}{1+x^2}\,dx = \frac{x^2}{2}\arctan x - \frac12\int\left(1 - \frac{1}{1+x^2}\right)dx$

$= \frac{x^2}{2}\arctan x - \frac{x}{2} + \frac12\arctan x + C = \frac12(x^2+1)\arctan x - \frac{x}{2} + C$.

**Check**: derivative $= x\arctan x + \frac12\cdot\frac{x^2+1}{x^2+1}\cdot$ (chain) $= x\arctan x + \frac12 - \frac12 = x\arctan x$ ✓. **Both problems are the same move — dump $\arctan$ into $u$ because its derivative is rational — and both times the leftover integral is a $u$-sub or a $\frac{P'}{P}$.**

---

### A7. $\int \sec^3 x\,dx$, then $\int \sec^5 x\,dx$ — the recursion.

Parts: $u = \sec x$, $dv = \sec^2 x\,dx$ ($du = \sec x\tan x\,dx$, $v = \tan x$):

$I_3 = \sec x\tan x - \int \sec x\tan^2 x\,dx = \sec x\tan x - \int\sec x(\sec^2 x-1)\,dx$

$= \sec x\tan x - I_3 + \int\sec x\,dx$ → $2I_3 = \sec x\tan x + \ln|\sec x + \tan x|$

$I_3 = \frac12\sec x\tan x + \frac12\ln|\sec x+\tan x| + C$.

**$\sec^5$ by recursion (not from scratch)**: $u = \sec^3 x$, $dv = \sec^2 x\,dx$ ($du = 3\sec^3 x\tan x\,dx$, $v = \tan x$):

$I_5 = \sec^3 x\tan x - 3\int\sec^3 x\tan^2 x\,dx = \sec^3 x\tan x - 3\int\sec^3 x(\sec^2 x - 1)\,dx$

$= \sec^3 x\tan x - 3I_5 + 3I_3$ → $4I_5 = \sec^3 x\tan x + 3I_3$

$I_5 = \frac14\sec^3 x\tan x + \frac34I_3 = \frac14\sec^3 x\tan x + \frac38\sec x\tan x + \frac38\ln|\sec x+\tan x| + C$.

**The thinking**: you *never* integrate $\sec^5$ from scratch. Raising the power by 2 in $u$ lowers it by 2 in the leftover ($\tan^2$ → $\sec^2 - 1$), so $I_5$ reduces to $I_3$ — a recursion $I_{n} = \frac{\sec^{n-2}x\tan x}{n-1} + \frac{n-2}{n-1}I_{n-2}$. **Solve the recurrence once; each higher odd power is one substitution away from the previous.**

---

### A8. $\int \frac{\sqrt{x^2-4}}{x}\,dx$ — the choice table and the sign.

Form $\sqrt{x^2 - 2^2}$ → $x = 2\sec\theta$, $dx = 2\sec\theta\tan\theta\,d\theta$.

$\sqrt{x^2-4} = 2\sqrt{\sec^2\theta-1} = 2|\tan\theta| = 2\tan\theta$ (taking $\theta \in [0,\pi/2)$, where $\tan\theta \geq 0$).

$\int \frac{2\tan\theta}{2\sec\theta}\cdot 2\sec\theta\tan\theta\,d\theta = \int 2\tan^2\theta\,d\theta = 2\int(\sec^2\theta-1)\,d\theta = 2(\tan\theta - \theta)$.

Right triangle ($\sec\theta = x/2$: adjacent $2$, hypotenuse $x$, opposite $\sqrt{x^2-4}$): $\tan\theta = \frac{\sqrt{x^2-4}}{2}$.

$\int \frac{\sqrt{x^2-4}}{x}\,dx = \sqrt{x^2-4} - 2\operatorname{arcsec}(x/2) + C = \sqrt{x^2-4} - 2\arccos(2/x) + C$.

**The choice table** — one line that removes all guessing:
| radical | substitution |
|:---:|:---:|
| $\sqrt{a^2 - x^2}$ | $x = a\sin\theta$ |
| $\sqrt{a^2 + x^2}$ | $x = a\tan\theta$ |
| $\sqrt{x^2 - a^2}$ | $x = a\sec\theta$ |

**Why sec here**: we need $\sqrt{x^2-4}$ to become a single trig function, and $\sec^2\theta - 1 = \tan^2\theta$. **The sign question**: $\sqrt{\cdot}$ is always nonnegative but $2\tan\theta$ isn't — you must declare the quadrant where $\tan\theta \geq 0$. This is the one place a sloppy trig sub silently flips signs.**

---

### A9. $\int x\arcsin x\,dx$ — recycle A6's answer.

Parts: $u = \arcsin x$, $dv = x\,dx$ ($du = \frac{dx}{\sqrt{1-x^2}}$, $v = \frac{x^2}{2}$):

$\frac{x^2}{2}\arcsin x - \frac12\int\frac{x^2}{\sqrt{1-x^2}}\,dx$.

Trig sub $x = \sin\theta$: $\int\frac{x^2}{\sqrt{1-x^2}}\,dx = \int\sin^2\theta\,d\theta = \frac{\theta}{2} - \frac{\sin 2\theta}{4} = \frac12\arcsin x - \frac{x\sqrt{1-x^2}}{2}$.

$\int x\arcsin x\,dx = \frac{x^2}{2}\arcsin x - \frac12\left(\frac12\arcsin x - \frac{x\sqrt{1-x^2}}{2}\right) = \frac{2x^2-1}{4}\arcsin x + \frac{x\sqrt{1-x^2}}{4} + C$.

**Compare with A6's structure**: both times $\arcsin$/$\arctan$ goes into $u$ (Inverse trig first in LIATE) and the leftover is a rational/radical integral you already know. **The $\frac12$ factors come from $dv = x\,dx$ (an $x$ too many) and from $\sin 2\theta$'s half-angle — same "halves" you've now seen three times today.**

---

### A10. $\int_0^{\pi/2}\sin^3 x\cos^2 x\,dx$, and $\int_0^{\pi/2}\sin^2 x\cos^2 x\,dx$ — odd vs even.

**Odd exponent ($m=3$)** → peel: $\sin^3 x\cos^2 x = \sin x(1-\cos^2 x)\cos^2 x$. $u = \cos x$, $du = -\sin x\,dx$; bounds $x=0\to u=1$, $x=\pi/2\to u=0$:

$\int_0^{\pi/2}\sin^3 x\cos^2 x\,dx = \int_1^0 (1-u^2)u^2(-du) = \int_0^1(u^2-u^4)\,du = \frac13 - \frac15 = \frac{2}{15}$.

**Even-even ($m=2,n=2$)** → half-angle: $\sin^2 x\cos^2 x = \frac{\sin^2 2x}{4} = \frac{1-\cos 4x}{8}$:

$\int_0^{\pi/2}\sin^2 x\cos^2 x\,dx = \frac18\left[x - \frac{\sin 4x}{4}\right]_0^{\pi/2} = \frac18\cdot\frac{\pi}{2} = \frac{\pi}{16}$.

**Why $2/15$ but $\pi/16$?** The odd case reduces to a pure polynomial in $u$ — rational answer. The even case needs half-angle, which leaves a linear $x$ term — so $\pi$ appears. **Odd power → rational; all-even → $\pi$. That fingerprint tells you which technique to reach for before you start.**

(Also: $\int_0^{\pi/2}\sin^4 x\,dx = \frac{3\pi}{16}$ and $\int_0^{\pi/2}\cos^4 x\,dx = \frac{3\pi}{16}$ by A2's pattern — the even-case answers always carry $\pi$.)

---

