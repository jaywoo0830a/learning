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

## Basic Algebra Drill — Advanced Integration

### D1. $\int x\cos x\,dx$

Parts: LIATE → $u=x$ (Algebraic), $dv=\cos x\,dx$.

| Step | Action |
|:---:|:---|
| 1-2 | $u = x$, $dv = \cos x\,dx$ |
| 3 | $du = dx$ |
| 4 | $v = \sin x$ |
| 5-6 | $uv - \int v\,du = x\sin x - \int \sin x\,dx = x\sin x + \cos x + C$ |

**Check**: $\frac{d}{dx}(x\sin x + \cos x) = \sin x + x\cos x - \sin x = x\cos x$. ✓

---

### D2. $\int \ln(2x)\,dx$

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

### D3. $\int \sin^2 x\,dx$

Even power → half-angle formula: $\sin^2 x = \frac{1-\cos 2x}{2}$.

$\int \sin^2 x\,dx = \int \frac{1-\cos 2x}{2}\,dx = \frac{1}{2}\int (1-\cos 2x)\,dx$

$= \frac{1}{2}\left(x - \frac{\sin 2x}{2}\right) + C = \frac{x}{2} - \frac{\sin 2x}{4} + C$.

---

### D4. $\int \tan x\sec^2 x\,dx$

Tan/sec: $n=2$ (even) → save $\sec^2 x$, $u = \tan x$.

$u = \tan x$, $du = \sec^2 x\,dx$ — **exact match**.

$\int \tan x\sec^2 x\,dx = \int u\,du = \frac{u^2}{2} + C = \frac{\tan^2 x}{2} + C$.

(Equivalently, $\frac{\sec^2 x}{2} + C$ since $\tan^2 x = \sec^2 x - 1$ — the constants differ by $-\frac{1}{2}$, which is absorbed into $+C$.)

---

### D5. $\int \frac{dx}{\sqrt{9-x^2}}$

Form: $\sqrt{9-x^2} = \sqrt{3^2-x^2}$ → $x = 3\sin\theta$.

1. $x = 3\sin\theta$, $dx = 3\cos\theta\,d\theta$.
2. $\sqrt{9-x^2} = \sqrt{9-9\sin^2\theta} = 3\cos\theta$.
3. Integral: $\int \frac{3\cos\theta\,d\theta}{3\cos\theta} = \int d\theta = \theta + C$.
4. Back-substitute: $\theta = \arcsin(x/3)$.

$\int \frac{dx}{\sqrt{9-x^2}} = \arcsin\left(\frac{x}{3}\right) + C$.

---

### D6. $\int \frac{dx}{x^2+9}$

Arctan formula: $\int \frac{dx}{x^2+a^2} = \frac{1}{a}\arctan\left(\frac{x}{a}\right) + C$.

$a = 3$: $\int \frac{dx}{x^2+9} = \frac{1}{3}\arctan\left(\frac{x}{3}\right) + C$.

---

### D7. $\int \frac{1}{x^2-x}\,dx$

Factor denominator: $x^2-x = x(x-1)$.

Template (distinct linear): $\frac{1}{x(x-1)} = \frac{A}{x} + \frac{B}{x-1}$.

Clear: $1 = A(x-1) + Bx$.

Plug roots:
- $x=0$: $1 = -A$ → $A = -1$.
- $x=1$: $1 = B$ → $B = 1$.

Integrate:

$\int \frac{1}{x^2-x}\,dx = \int \left(\frac{-1}{x} + \frac{1}{x-1}\right)dx = -\ln|x| + \ln|x-1| + C = \ln\left|\frac{x-1}{x}\right| + C$.

---

### D8. $\int x^2 e^x\,dx$

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

### D9. $\int \sin x\cos x\,dx$

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

### D10. $\int \frac{x}{\sqrt{1-x^2}}\,dx$

Decision: $u$-sub is faster (see Practice 5a).

$u = 1-x^2$, $du = -2x\,dx$ → $x\,dx = -\frac{du}{2}$.

$\int \frac{x}{\sqrt{1-x^2}}\,dx = \int u^{-1/2} \cdot \left(-\frac{du}{2}\right) = -\frac{1}{2}\int u^{-1/2}\,du$

$= -\frac{1}{2} \cdot \frac{u^{1/2}}{1/2} + C = -u^{1/2} + C = -\sqrt{1-x^2} + C$.

---

## Advanced Algebra Drill — Advanced Integration

### A1. $\int e^x\cos x\,dx$

This is a cycling integral. Let $I = \int e^x\cos x\,dx$.

**Round 1**: $u = \cos x$, $dv = e^x\,dx$ (either choice works — LIATE gives Trig before Exp, so $u=\cos x$).

$du = -\sin x\,dx$, $v = e^x$.

$I = e^x\cos x - \int e^x(-\sin x)\,dx = e^x\cos x + \int e^x\sin x\,dx$.

**Round 2**: For $\int e^x\sin x\,dx$, $u = \sin x$, $dv = e^x\,dx$.

$du = \cos x\,dx$, $v = e^x$.

$\int e^x\sin x\,dx = e^x\sin x - \int e^x\cos x\,dx = e^x\sin x - I$.

**Combine**:

$I = e^x\cos x + (e^x\sin x - I) = e^x(\cos x + \sin x) - I$

$2I = e^x(\cos x + \sin x)$ → $I = \frac{e^x}{2}(\cos x + \sin x) + C$.

**Check**: $\frac{d}{dx}\left[\frac{e^x}{2}(\cos x+\sin x)\right] = \frac{e^x}{2}(\cos x+\sin x) + \frac{e^x}{2}(-\sin x+\cos x) = \frac{e^x}{2}(2\cos x) = e^x\cos x$. ✓

---

### A2. $\int \sin^4 x\,dx$

Repeated half-angle: $\sin^4 x = (\sin^2 x)^2 = \left(\frac{1-\cos 2x}{2}\right)^2$.

$= \frac{1}{4}(1 - 2\cos 2x + \cos^2 2x)$

Now $\cos^2 2x = \frac{1+\cos 4x}{2}$ (half-angle again).

$= \frac{1}{4}\left(1 - 2\cos 2x + \frac{1+\cos 4x}{2}\right)$

$= \frac{1}{4}\left(1 - 2\cos 2x + \frac{1}{2} + \frac{\cos 4x}{2}\right)$

$= \frac{1}{4}\left(\frac{3}{2} - 2\cos 2x + \frac{\cos 4x}{2}\right)$

$= \frac{3}{8} - \frac{1}{2}\cos 2x + \frac{1}{8}\cos 4x$

Integrate:

$\int \sin^4 x\,dx = \int \left(\frac{3}{8} - \frac{1}{2}\cos 2x + \frac{1}{8}\cos 4x\right)dx$

$= \frac{3x}{8} - \frac{\sin 2x}{4} + \frac{\sin 4x}{32} + C$.

---

### A3. $\int \frac{dx}{(x^2+1)^2}$

Trig sub $x = \tan\theta$, $a=1$.

1. $x = \tan\theta$, $dx = \sec^2\theta\,d\theta$.
2. $x^2+1 = \tan^2\theta+1 = \sec^2\theta$. So $(x^2+1)^2 = \sec^4\theta$.
3. Integral: $\int \frac{\sec^2\theta\,d\theta}{\sec^4\theta} = \int \cos^2\theta\,d\theta$.
4. $\int \cos^2\theta\,d\theta = \int \frac{1+\cos 2\theta}{2}\,d\theta = \frac{\theta}{2} + \frac{\sin 2\theta}{4} + C$.
5. Back-substitute using right triangle ($x = \tan\theta$):
   - $\theta = \arctan x$
   - $\sin 2\theta = 2\sin\theta\cos\theta$

   From triangle: opposite = $x$, adjacent = $1$, hypotenuse = $\sqrt{x^2+1}$.
   - $\sin\theta = \frac{x}{\sqrt{x^2+1}}$, $\cos\theta = \frac{1}{\sqrt{x^2+1}}$.
   - $\sin 2\theta = 2 \cdot \frac{x}{\sqrt{x^2+1}} \cdot \frac{1}{\sqrt{x^2+1}} = \frac{2x}{x^2+1}$.

6. Final answer:

$\int \frac{dx}{(x^2+1)^2} = \frac{1}{2}\arctan x + \frac{x}{2(x^2+1)} + C$.

---

### A4. $\int \frac{x^3}{\sqrt{x^2+1}}\,dx$

$u$-sub: $u = x^2+1$, $du = 2x\,dx$ → $x\,dx = \frac{du}{2}$.

Rewrite $x^3 = x^2 \cdot x$. Solve for $x^2$: $x^2 = u-1$.

$\int \frac{x^3}{\sqrt{x^2+1}}\,dx = \int \frac{x^2 \cdot x}{\sqrt{x^2+1}}\,dx = \int \frac{(u-1) \cdot x\,dx}{\sqrt{u}} = \int \frac{u-1}{u^{1/2}} \cdot \frac{du}{2}$

$= \frac{1}{2}\int (u^{1/2} - u^{-1/2})\,du = \frac{1}{2}\left(\frac{u^{3/2}}{3/2} - \frac{u^{1/2}}{1/2}\right) + C$

$= \frac{1}{2}\left(\frac{2}{3}u^{3/2} - 2u^{1/2}\right) + C = \frac{1}{3}u^{3/2} - u^{1/2} + C$

$= \frac{1}{3}(x^2+1)^{3/2} - (x^2+1)^{1/2} + C = \frac{1}{3}(x^2+1)^{3/2} - \sqrt{x^2+1} + C$.

Factor: $= \frac{\sqrt{x^2+1}}{3}(x^2+1 - 3) + C = \frac{\sqrt{x^2+1}}{3}(x^2-2) + C$.

---

### A5. $\int \frac{x^2+2x-1}{(x-1)(x^2+1)}\,dx$

Template for linear + irreducible quadratic:

$\frac{x^2+2x-1}{(x-1)(x^2+1)} = \frac{A}{x-1} + \frac{Bx+C}{x^2+1}$

Clear denominators: $x^2+2x-1 = A(x^2+1) + (Bx+C)(x-1)$.

$= A(x^2+1) + Bx(x-1) + C(x-1)$
$= Ax^2 + A + Bx^2 - Bx + Cx - C$
$= (A+B)x^2 + (C-B)x + (A-C)$.

Match coefficients:
- $x^2$: $A+B = 1$
- $x$: $C-B = 2$
- constant: $A-C = -1$

Solve:
From (3): $A = C-1$.
From (2): $C = B+2$.
Sub into (1): $(C-1)+B = 1$ → $(B+2-1)+B = 1$ → $2B+1 = 1$ → $B = 0$.

Then $C = 2$, $A = 1$.

So: $\frac{x^2+2x-1}{(x-1)(x^2+1)} = \frac{1}{x-1} + \frac{2}{x^2+1}$.

Integrate:

$\int \frac{x^2+2x-1}{(x-1)(x^2+1)}\,dx = \int \frac{1}{x-1}\,dx + \int \frac{2}{x^2+1}\,dx$

$= \ln|x-1| + 2\arctan x + C$.

---

### A6. $\int \arctan x\,dx$

Parts: $u = \arctan x$ (Inverse trig), $dv = dx$.

| Step | Value |
|:---:|:---|
| $u$ | $\arctan x$ |
| $dv$ | $dx$ |
| $du$ | $\frac{1}{1+x^2}\,dx$ |
| $v$ | $x$ |

$uv - \int v\,du = x\arctan x - \int \frac{x}{1+x^2}\,dx$

The new integral is a $u$-sub: $w = 1+x^2$, $dw = 2x\,dx$ → $x\,dx = \frac{dw}{2}$.

$\int \frac{x}{1+x^2}\,dx = \int \frac{1}{w} \cdot \frac{dw}{2} = \frac{1}{2}\ln|w| + C = \frac{1}{2}\ln(1+x^2) + C$.

$\int \arctan x\,dx = x\arctan x - \frac{1}{2}\ln(1+x^2) + C$.

---

### A7. $\int \sec^3 x\,dx$

Parts: $u = \sec x$, $dv = \sec^2 x\,dx$.

| Step | Value |
|:---:|:---|
| $u$ | $\sec x$ |
| $dv$ | $\sec^2 x\,dx$ |
| $du$ | $\sec x\tan x\,dx$ |
| $v$ | $\tan x$ |

$I = \sec x\tan x - \int \tan x \cdot \sec x\tan x\,dx = \sec x\tan x - \int \sec x\tan^2 x\,dx$

Use $\tan^2 x = \sec^2 x - 1$:

$I = \sec x\tan x - \int \sec x(\sec^2 x - 1)\,dx$

$= \sec x\tan x - \int \sec^3 x\,dx + \int \sec x\,dx$

$= \sec x\tan x - I + \int \sec x\,dx$

Now $\int \sec x\,dx = \ln|\sec x + \tan x| + C$ (standard formula).

$I = \sec x\tan x - I + \ln|\sec x + \tan x|$

$2I = \sec x\tan x + \ln|\sec x + \tan x|$

$I = \frac{1}{2}\sec x\tan x + \frac{1}{2}\ln|\sec x + \tan x| + C$.

---

### A8. $\int \frac{\sqrt{x^2-4}}{x}\,dx$

Form: $\sqrt{x^2-4} = \sqrt{x^2-2^2}$ → $x = 2\sec\theta$.

1. $x = 2\sec\theta$, $dx = 2\sec\theta\tan\theta\,d\theta$.
2. $\sqrt{x^2-4} = \sqrt{4\sec^2\theta-4} = 2\sqrt{\sec^2\theta-1} = 2\tan\theta$ (assuming $\theta$ where $\tan\theta \geq 0$).
3. Integral: $\int \frac{2\tan\theta}{2\sec\theta} \cdot 2\sec\theta\tan\theta\,d\theta = \int 2\tan^2\theta\,d\theta$.

$= 2\int (\sec^2\theta - 1)\,d\theta = 2(\tan\theta - \theta) + C$.

4. Back-substitute via right triangle: $\sec\theta = x/2$.

   Adjacent = $2$, hypotenuse = $x$, opposite = $\sqrt{x^2-4}$.
   - $\tan\theta = \frac{\sqrt{x^2-4}}{2}$
   - $\theta = \operatorname{arcsec}(x/2)$ or $\theta = \arccos(2/x)$.

$\int \frac{\sqrt{x^2-4}}{x}\,dx = 2\left(\frac{\sqrt{x^2-4}}{2} - \operatorname{arcsec}(x/2)\right) + C$

$= \sqrt{x^2-4} - 2\operatorname{arcsec}(x/2) + C$.

(Alternative: $\sqrt{x^2-4} - 2\arccos(2/x) + C$.)

---

### A9. $\int x\arcsin x\,dx$

Parts: $u = \arcsin x$ (Inverse trig), $dv = x\,dx$.

| Step | Value |
|:---:|:---|
| $u$ | $\arcsin x$ |
| $dv$ | $x\,dx$ |
| $du$ | $\frac{1}{\sqrt{1-x^2}}\,dx$ |
| $v$ | $\frac{x^2}{2}$ |

$uv - \int v\,du = \frac{x^2}{2}\arcsin x - \int \frac{x^2}{2} \cdot \frac{1}{\sqrt{1-x^2}}\,dx$

$= \frac{x^2}{2}\arcsin x - \frac{1}{2}\int \frac{x^2}{\sqrt{1-x^2}}\,dx$

For $\int \frac{x^2}{\sqrt{1-x^2}}\,dx$, use trig sub $x = \sin\theta$, $dx = \cos\theta\,d\theta$:

$\int \frac{\sin^2\theta}{\sqrt{1-\sin^2\theta}} \cdot \cos\theta\,d\theta = \int \frac{\sin^2\theta}{\cos\theta} \cdot \cos\theta\,d\theta = \int \sin^2\theta\,d\theta$

$= \int \frac{1-\cos 2\theta}{2}\,d\theta = \frac{\theta}{2} - \frac{\sin 2\theta}{4} + C$.

Back-substitute: $\theta = \arcsin x$, $\sin 2\theta = 2\sin\theta\cos\theta = 2x\sqrt{1-x^2}$.

$= \frac{1}{2}\arcsin x - \frac{x\sqrt{1-x^2}}{2} + C$.

Now combine:

$\int x\arcsin x\,dx = \frac{x^2}{2}\arcsin x - \frac{1}{2}\left(\frac{1}{2}\arcsin x - \frac{x\sqrt{1-x^2}}{2}\right) + C$

$= \frac{x^2}{2}\arcsin x - \frac{1}{4}\arcsin x + \frac{x\sqrt{1-x^2}}{4} + C$

$= \frac{2x^2-1}{4}\arcsin x + \frac{x\sqrt{1-x^2}}{4} + C$.

---

### A10. Derive $\int \sin^n x\,dx = -\frac{1}{n}\sin^{n-1}x\cos x + \frac{n-1}{n}\int \sin^{n-2}x\,dx$

Parts: $u = \sin^{n-1}x$, $dv = \sin x\,dx$.

| Step | Value |
|:---:|:---|
| $u$ | $\sin^{n-1}x$ |
| $dv$ | $\sin x\,dx$ |
| $du$ | $(n-1)\sin^{n-2}x \cdot \cos x\,dx$ |
| $v$ | $-\cos x$ |

Let $I_n = \int \sin^n x\,dx$.

$I_n = \sin^{n-1}x \cdot (-\cos x) - \int (-\cos x) \cdot (n-1)\sin^{n-2}x\cos x\,dx$

$= -\sin^{n-1}x\cos x + (n-1)\int \sin^{n-2}x\cos^2 x\,dx$

Use $\cos^2 x = 1 - \sin^2 x$:

$I_n = -\sin^{n-1}x\cos x + (n-1)\int \sin^{n-2}x(1-\sin^2 x)\,dx$

$= -\sin^{n-1}x\cos x + (n-1)\int \sin^{n-2}x\,dx - (n-1)\int \sin^n x\,dx$

$= -\sin^{n-1}x\cos x + (n-1)I_{n-2} - (n-1)I_n$.

Bring $(n-1)I_n$ to the left side:

$I_n + (n-1)I_n = -\sin^{n-1}x\cos x + (n-1)I_{n-2}$

$nI_n = -\sin^{n-1}x\cos x + (n-1)I_{n-2}$

$I_n = -\frac{1}{n}\sin^{n-1}x\cos x + \frac{n-1}{n}\int \sin^{n-2}x\,dx$. ∎

---

