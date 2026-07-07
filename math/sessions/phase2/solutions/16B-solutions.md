# Solutions — 16B: Advanced Integration

---

## Practice 1

$\int x\sin x\,dx$

**Integration by parts**. LIATE: Algebraic ($x$) beats Trig ($\sin x$).

| Step | Action |
|:---:|:---|
| 1 | $u = x$ (Algebraic) |
| 2 | $dv = \sin x\,dx$ |
| 3 | $du = dx$ |
| 4 | $v = \int \sin x\,dx = -\cos x$ |
| 5 | Assemble: $\int u\,dv = uv - \int v\,du$ |

$= x(-\cos x) - \int (-\cos x)\,dx$

$= -x\cos x + \int \cos x\,dx$

$= -x\cos x + \sin x + C$

$\boxed{\sin x - x\cos x + C}$

**Check**: $\frac{d}{dx}(\sin x - x\cos x + C) = \cos x - (\cos x - x\sin x) = \cos x - \cos x + x\sin x = x\sin x$. ✓

---

## Practice 2

$\int \cos^3 x\,dx$

**Trig integral**: $n = 3$ is odd. Follow the "odd power" branch.

**Step 1 — Peel**: $\cos^3 x = \cos x \cdot \cos^2 x$.

**Step 2 — Convert**: $\cos^2 x = 1 - \sin^2 x$.

$\int \cos x (1 - \sin^2 x)\,dx$

**Step 3 — $u$-sub**: $u = \sin x$, $du = \cos x\,dx$. Exact match!

$\int (1 - u^2)\,du$

**Step 4 — Integrate**: $u - \frac{u^3}{3} + C$.

**Step 5 — Back**: $\boxed{\sin x - \frac{\sin^3 x}{3} + C}$

**Check**: $\frac{d}{dx}\left(\sin x - \frac{\sin^3 x}{3}\right) = \cos x - \sin^2 x \cos x = \cos x(1 - \sin^2 x) = \cos x \cos^2 x = \cos^3 x$. ✓

---

## Practice 3

$\int \frac{dx}{x^2+4}$

**Method 1 — Arctan formula directly**:

Recall $\int \frac{1}{x^2 + a^2}\,dx = \frac{1}{a}\arctan\left(\frac{x}{a}\right) + C$.

Here $a^2 = 4$, so $a = 2$.

$\int \frac{dx}{x^2+4} = \boxed{\frac{1}{2}\arctan\left(\frac{x}{2}\right) + C}$

**Method 2 — Trig substitution**:

Form $\sqrt{x^2+4}$ doesn't appear, but the integrand suggests $x = 2\tan\theta$.

1. $x = 2\tan\theta$, $dx = 2\sec^2\theta\,d\theta$.
2. $x^2 + 4 = 4\tan^2\theta + 4 = 4(\tan^2\theta + 1) = 4\sec^2\theta$.
3. $\int \frac{2\sec^2\theta\,d\theta}{4\sec^2\theta} = \int \frac{1}{2}\,d\theta = \frac{\theta}{2} + C$.
4. Back-substitute: $\theta = \arctan(x/2)$.
5. Answer: $\frac{1}{2}\arctan(x/2) + C$.

Both methods give the same answer. The arctan formula is faster.

---

## Practice 4

$\int \frac{x+1}{x^2-3x+2}\,dx$

**Step 1 — Factor denominator**: $x^2 - 3x + 2 = (x-1)(x-2)$.

**Step 2 — Check degrees**: Numerator degree 1 < denominator degree 2. No long division needed.

**Step 3 — Write decomposition template** (distinct linear factors):

$\frac{x+1}{(x-1)(x-2)} = \frac{A}{x-1} + \frac{B}{x-2}$

**Step 4 — Clear denominators**:

$x+1 = A(x-2) + B(x-1)$

**Step 5 — Solve for $A$ and $B$** (plug roots):

- Plug $x = 1$: $1+1 = A(1-2) + B(0) \to 2 = -A \to A = -2$
- Plug $x = 2$: $2+1 = A(0) + B(2-1) \to 3 = B \to B = 3$

**Step 6 — Integrate each term**:

$\int \left(\frac{-2}{x-1} + \frac{3}{x-2}\right)\,dx = -2\ln|x-1| + 3\ln|x-2| + C$

$\boxed{3\ln|x-2| - 2\ln|x-1| + C}$

**Alternative compact form**: $\ln\left|\frac{(x-2)^3}{(x-1)^2}\right| + C$.

---

## Practice 5: Real Battle

**(a) Is there a faster way? Solve $\int \frac{x}{\sqrt{1-x^2}}\,dx$ with $u$-sub.**

Yes — $u$-sub is MUCH faster.

$u = 1 - x^2$
$du = -2x\,dx \to x\,dx = -\frac{du}{2}$

$\int \frac{x}{\sqrt{1-x^2}}\,dx = \int \frac{1}{\sqrt{u}} \cdot \left(-\frac{du}{2}\right) = -\frac{1}{2}\int u^{-1/2}\,du$

$= -\frac{1}{2} \cdot \frac{u^{1/2}}{1/2} + C = -\sqrt{u} + C = \boxed{-\sqrt{1-x^2} + C}$

Trig sub would work but takes 5 steps instead of 3. The numerator $x$ exactly matches (up to a constant) the derivative of the inside $1-x^2$ — that's the signal to use $u$-sub.

**(b) Now solve $\int \frac{1}{\sqrt{1-x^2}}\,dx$ — was trig sub the right call this time?**

Here there's **no $x$ in the numerator** — $u$-sub fails because $u=1-x^2$ gives $du = -2x\,dx$, but we have no $x$ to pair with it.

Trig sub is the right call:

$x = \sin\theta$, $dx = \cos\theta\,d\theta$.
$\sqrt{1-x^2} = \sqrt{1-\sin^2\theta} = \cos\theta$.

$\int \frac{\cos\theta\,d\theta}{\cos\theta} = \int d\theta = \theta + C = \boxed{\arcsin x + C}$

This is actually one of the dictionary entries: $\int \frac{1}{\sqrt{1-x^2}}\,dx = \arcsin x + C$.

**(c) One-sentence rule:**

> **If there's an $x$ (or constant multiple of $x$) in the numerator, try $u$-sub first; if the numerator is just a constant (no $x$), trig sub is the right tool.**

More precisely: when you see $\sqrt{a^2-x^2}$, check if the derivative of $a^2-x^2$ (which is $-2x$) appears in the integrand. If yes → $u$-sub. If no → trig sub.

---

## Basic Algebra Drill — Solutions

### D1. $\int x\cos x\,dx$

**Parts**: LIATE → $u = x$ (Algebraic), $dv = \cos x\,dx$.

$du = dx$, $v = \sin x$.

$\int x\cos x\,dx = x\sin x - \int \sin x\,dx = \boxed{x\sin x + \cos x + C}$

---

### D2. $\int \ln(2x)\,dx$

**Parts**: $u = \ln(2x)$ (Log, highest priority), $dv = dx$.

$du = \frac{1}{2x} \cdot 2\,dx = \frac{1}{x}\,dx$, $v = x$.

$\int \ln(2x)\,dx = x\ln(2x) - \int x \cdot \frac{1}{x}\,dx = x\ln(2x) - \int 1\,dx$

$= \boxed{x\ln(2x) - x + C}$

**Alternative using log property**: $\ln(2x) = \ln 2 + \ln x$, so $\int \ln(2x)\,dx = x\ln 2 + \int \ln x\,dx = x\ln 2 + x\ln x - x + C = x\ln(2x) - x + C$. Same result.

---

### D3. $\int \sin^2 x\,dx$

**Trig integral — both exponents even** ($m=2$, $n=0$). Use half-angle formula.

$\sin^2 x = \frac{1 - \cos 2x}{2}$

$\int \sin^2 x\,dx = \int \frac{1 - \cos 2x}{2}\,dx = \frac{1}{2}\int (1 - \cos 2x)\,dx$

$= \frac{1}{2}\left(x - \frac{\sin 2x}{2}\right) + C = \boxed{\frac{x}{2} - \frac{\sin 2x}{4} + C}$

---

### D4. $\int \tan x \sec^2 x\,dx$

**Tan/sec integral**: $n = 2$ (even). Save $\sec^2 x$ for $du$.

$u = \tan x$, $du = \sec^2 x\,dx$. Exact match!

$\int \tan x \sec^2 x\,dx = \int u\,du = \frac{u^2}{2} + C = \boxed{\frac{\tan^2 x}{2} + C}$

---

### D5. $\int \frac{dx}{\sqrt{9-x^2}}$

**Trig sub**: Form $\sqrt{9-x^2} = \sqrt{3^2 - x^2}$ → $x = 3\sin\theta$.

$dx = 3\cos\theta\,d\theta$, $\sqrt{9-x^2} = \sqrt{9-9\sin^2\theta} = 3\cos\theta$.

$\int \frac{3\cos\theta\,d\theta}{3\cos\theta} = \int d\theta = \theta + C = \boxed{\arcsin\left(\frac{x}{3}\right) + C}$

**Dictionary shortcut**: $\int \frac{1}{\sqrt{a^2-x^2}}\,dx = \arcsin(x/a) + C$.

---

### D6. $\int \frac{dx}{x^2+9}$

**Arctan formula**: $\int \frac{1}{x^2 + a^2}\,dx = \frac{1}{a}\arctan(x/a) + C$.

Here $a^2 = 9$, so $a = 3$.

$\boxed{\frac{1}{3}\arctan\left(\frac{x}{3}\right) + C}$

---

### D7. $\int \frac{1}{x^2-x}\,dx$

**Partial fractions**: Factor denominator: $x^2 - x = x(x-1)$.

Template: $\frac{1}{x(x-1)} = \frac{A}{x} + \frac{B}{x-1}$.

Clear: $1 = A(x-1) + Bx$.

- Plug $x = 0$: $1 = A(-1) \to A = -1$.
- Plug $x = 1$: $1 = B(1) \to B = 1$.

$\int \left(-\frac{1}{x} + \frac{1}{x-1}\right)\,dx = -\ln|x| + \ln|x-1| + C$

$= \boxed{\ln\left|\frac{x-1}{x}\right| + C}$

---

### D8. $\int x^2 e^x\,dx$

**Parts — two rounds needed** (polynomial degree 2).

**Round 1**: $u = x^2$, $dv = e^x\,dx$. $du = 2x\,dx$, $v = e^x$.

$\int x^2 e^x\,dx = x^2 e^x - \int 2x e^x\,dx = x^2 e^x - 2\int x e^x\,dx$

**Round 2**: On $\int x e^x\,dx$: $u = x$, $dv = e^x\,dx$. $du = dx$, $v = e^x$.

$\int x e^x\,dx = x e^x - \int e^x\,dx = x e^x - e^x + C$

**Combine**:

$\int x^2 e^x\,dx = x^2 e^x - 2(x e^x - e^x) + C$

$= x^2 e^x - 2x e^x + 2e^x + C$

$= \boxed{e^x(x^2 - 2x + 2) + C}$

**Pattern**: Each round of parts reduces the polynomial degree by 1. For $\int x^n e^x\,dx$, you need $n$ rounds.

---

### D9. $\int \sin x \cos x\,dx$

**Method 1 — $u$-sub** ($u = \sin x$):

$u = \sin x$, $du = \cos x\,dx$. Exact match!

$\int \sin x \cos x\,dx = \int u\,du = \frac{u^2}{2} + C = \frac{\sin^2 x}{2} + C$

**Method 2 — Double-angle identity**:

$\sin 2x = 2\sin x \cos x \to \sin x \cos x = \frac{1}{2}\sin 2x$

$\int \sin x \cos x\,dx = \frac{1}{2}\int \sin 2x\,dx = \frac{1}{2}\left(-\frac{\cos 2x}{2}\right) + C = -\frac{\cos 2x}{4} + C$

**Are these the same?** Yes! Use $\cos 2x = 1 - 2\sin^2 x$:

$-\frac{\cos 2x}{4} = -\frac{1-2\sin^2 x}{4} = -\frac{1}{4} + \frac{\sin^2 x}{2}$

The $-\frac{1}{4}$ gets absorbed into $C$. Both are valid antiderivatives.

$\boxed{\frac{\sin^2 x}{2} + C \quad\text{or}\quad -\frac{\cos 2x}{4} + C}$

---

### D10. $\int \frac{x}{\sqrt{1-x^2}}\,dx$

**Decision**: The numerator has $x$, which (up to a constant) is the derivative of $1-x^2$. → **Use $u$-sub, not trig sub!**

$u = 1 - x^2$, $du = -2x\,dx \to x\,dx = -\frac{du}{2}$.

$\int \frac{x}{\sqrt{1-x^2}}\,dx = \int u^{-1/2} \cdot \left(-\frac{du}{2}\right) = -\frac{1}{2}\int u^{-1/2}\,du$

$= -\frac{1}{2} \cdot \frac{u^{1/2}}{1/2} + C = -\sqrt{u} + C = \boxed{-\sqrt{1-x^2} + C}$

**Why not trig sub?** Trig sub would also work: $x = \sin\theta \to \int \frac{\sin\theta \cos\theta}{\cos\theta}\,d\theta = \int \sin\theta\,d\theta = -\cos\theta + C = -\sqrt{1-x^2} + C$. But $u$-sub is one step faster. Rule: check $u$-sub first.

---

## Advanced Algebra Drill — Solutions

### A1. $\int e^x \cos x\,dx$

**Cycling parts** — apply twice and solve for $I$.

Let $I = \int e^x \cos x\,dx$.

**Round 1**: $u = \cos x$, $dv = e^x\,dx$. $du = -\sin x\,dx$, $v = e^x$.

$I = e^x \cos x - \int e^x(-\sin x)\,dx = e^x \cos x + \int e^x \sin x\,dx$

**Round 2**: On $\int e^x \sin x\,dx$: $u = \sin x$, $dv = e^x\,dx$. $du = \cos x\,dx$, $v = e^x$.

$\int e^x \sin x\,dx = e^x \sin x - \int e^x \cos x\,dx = e^x \sin x - I$

**Substitute back**:

$I = e^x \cos x + (e^x \sin x - I)$
$I = e^x \cos x + e^x \sin x - I$
$2I = e^x(\cos x + \sin x)$
$I = \boxed{\frac{e^x}{2}(\sin x + \cos x) + C}$

---

### A2. $\int \sin^4 x\,dx$

**Repeated half-angle** — both exponents are even.

$\sin^4 x = (\sin^2 x)^2 = \left(\frac{1 - \cos 2x}{2}\right)^2$

$= \frac{1}{4}(1 - 2\cos 2x + \cos^2 2x)$

Now use half-angle on $\cos^2 2x$: $\cos^2 2x = \frac{1 + \cos 4x}{2}$.

$= \frac{1}{4}\left(1 - 2\cos 2x + \frac{1 + \cos 4x}{2}\right)$

$= \frac{1}{4}\left(\frac{3}{2} - 2\cos 2x + \frac{\cos 4x}{2}\right)$

$= \frac{3}{8} - \frac{1}{2}\cos 2x + \frac{1}{8}\cos 4x$

**Integrate term by term**:

$\int \sin^4 x\,dx = \frac{3}{8}x - \frac{1}{2} \cdot \frac{\sin 2x}{2} + \frac{1}{8} \cdot \frac{\sin 4x}{4} + C$

$= \boxed{\frac{3x}{8} - \frac{\sin 2x}{4} + \frac{\sin 4x}{32} + C}$

---

### A3. $\int \frac{dx}{(x^2+1)^2}$

**Trig sub**: Form $\sqrt{x^2+1}$ is suggested → $x = \tan\theta$, $dx = \sec^2\theta\,d\theta$.

$x^2 + 1 = \tan^2\theta + 1 = \sec^2\theta$, so $(x^2+1)^2 = \sec^4\theta$.

$\int \frac{\sec^2\theta\,d\theta}{\sec^4\theta} = \int \cos^2\theta\,d\theta$

Use half-angle: $\cos^2\theta = \frac{1 + \cos 2\theta}{2}$.

$= \int \frac{1 + \cos 2\theta}{2}\,d\theta = \frac{\theta}{2} + \frac{\sin 2\theta}{4} + C$

**Back-substitute via right triangle** ($x = \tan\theta$):
- Opposite = $x$, adjacent = $1$, hypotenuse = $\sqrt{x^2+1}$.
- $\theta = \arctan x$
- $\sin 2\theta = 2\sin\theta\cos\theta = 2 \cdot \frac{x}{\sqrt{x^2+1}} \cdot \frac{1}{\sqrt{x^2+1}} = \frac{2x}{x^2+1}$

$\int \frac{dx}{(x^2+1)^2} = \frac{\arctan x}{2} + \frac{1}{4} \cdot \frac{2x}{x^2+1} + C$

$= \boxed{\frac{1}{2}\arctan x + \frac{x}{2(x^2+1)} + C}$

---

### A4. $\int \frac{x^3}{\sqrt{x^2+1}}\,dx$

**Decision**: $u$-sub is faster than trig sub.

$u = x^2 + 1$, $du = 2x\,dx$.

Rewrite $x^3 = x^2 \cdot x = (u-1) \cdot x$.

$x^3\,dx = (u-1) \cdot x\,dx = (u-1) \cdot \frac{du}{2}$

$\int \frac{x^3}{\sqrt{x^2+1}}\,dx = \int \frac{u-1}{\sqrt{u}} \cdot \frac{du}{2} = \frac{1}{2}\int \frac{u-1}{u^{1/2}}\,du$

$= \frac{1}{2}\int \left(u^{1/2} - u^{-1/2}\right)\,du$

$= \frac{1}{2}\left(\frac{u^{3/2}}{3/2} - \frac{u^{1/2}}{1/2}\right) + C$

$= \frac{1}{2}\left(\frac{2}{3}u^{3/2} - 2u^{1/2}\right) + C$

$= \frac{1}{3}u^{3/2} - u^{1/2} + C$

Substitute back $u = x^2 + 1$:

$= \frac{1}{3}(x^2+1)^{3/2} - (x^2+1)^{1/2} + C$

$= \boxed{\frac{(x^2+1)^{3/2}}{3} - \sqrt{x^2+1} + C}$

**Alternative form**: Factor $\sqrt{x^2+1}$: $\sqrt{x^2+1}\left(\frac{x^2+1}{3} - 1\right) + C = \sqrt{x^2+1} \cdot \frac{x^2-2}{3} + C$.

---

### A5. $\int \frac{x^2+2x-1}{(x-1)(x^2+1)}\,dx$

**Partial fractions with a quadratic factor**.

Template: $\frac{x^2+2x-1}{(x-1)(x^2+1)} = \frac{A}{x-1} + \frac{Bx+C}{x^2+1}$.

Clear denominators:

$x^2 + 2x - 1 = A(x^2+1) + (Bx+C)(x-1)$

Expand: $= Ax^2 + A + Bx^2 - Bx + Cx - C$

$= (A+B)x^2 + (C-B)x + (A-C)$

Match coefficients:
- $x^2$: $A + B = 1$
- $x$: $C - B = 2$
- Constant: $A - C = -1$

Solve the system:
From $A+B=1$: $B = 1-A$.
From $A-C=-1$: $C = A+1$.
From $C-B=2$: $(A+1) - (1-A) = 2 \to A+1-1+A = 2 \to 2A = 2 \to A = 1$.

Then $B = 1-A = 0$, $C = A+1 = 2$.

**Integrate**:

$\int \left(\frac{1}{x-1} + \frac{2}{x^2+1}\right)\,dx$

$= \ln|x-1| + 2\arctan x + C$

$\boxed{\ln|x-1| + 2\arctan x + C}$

---

### A6. $\int \arctan x\,dx$

**Parts**: $u = \arctan x$ (Inverse trig, LIATE priority 2), $dv = dx$.

$du = \frac{1}{1+x^2}\,dx$, $v = x$.

$\int \arctan x\,dx = x\arctan x - \int \frac{x}{1+x^2}\,dx$

The remaining integral is a $u$-sub: $w = 1+x^2$, $dw = 2x\,dx \to x\,dx = \frac{dw}{2}$.

$\int \frac{x}{1+x^2}\,dx = \frac{1}{2}\int \frac{dw}{w} = \frac{1}{2}\ln|w| + C = \frac{1}{2}\ln(1+x^2) + C$

**Final answer**: $\boxed{x\arctan x - \frac{1}{2}\ln(1+x^2) + C}$

---

### A7. $\int \sec^3 x\,dx$

**Classic cycling parts integral**.

Let $I = \int \sec^3 x\,dx = \int \sec x \cdot \sec^2 x\,dx$.

Parts: $u = \sec x$, $dv = \sec^2 x\,dx$.
$du = \sec x \tan x\,dx$, $v = \tan x$.

$I = \sec x \tan x - \int \tan x \cdot \sec x \tan x\,dx$

$= \sec x \tan x - \int \sec x \tan^2 x\,dx$

Use $\tan^2 x = \sec^2 x - 1$:

$= \sec x \tan x - \int \sec x (\sec^2 x - 1)\,dx$

$= \sec x \tan x - \int \sec^3 x\,dx + \int \sec x\,dx$

$= \sec x \tan x - I + \int \sec x\,dx$

$2I = \sec x \tan x + \int \sec x\,dx$

Recall $\int \sec x\,dx = \ln|\sec x + \tan x| + C$.

$2I = \sec x \tan x + \ln|\sec x + \tan x| + C$

$I = \boxed{\frac{1}{2}\sec x \tan x + \frac{1}{2}\ln|\sec x + \tan x| + C}$

---

### A8. $\int \frac{\sqrt{x^2-4}}{x}\,dx$

**Trig sub**: Form $\sqrt{x^2 - 2^2}$ → $x = 2\sec\theta$, $dx = 2\sec\theta\tan\theta\,d\theta$.

$\sqrt{x^2-4} = \sqrt{4\sec^2\theta - 4} = 2\sqrt{\sec^2\theta-1} = 2\tan\theta$.

$\int \frac{2\tan\theta}{2\sec\theta} \cdot 2\sec\theta\tan\theta\,d\theta = \int 2\tan^2\theta\,d\theta$

$= 2\int (\sec^2\theta - 1)\,d\theta = 2(\tan\theta - \theta) + C$

**Back-substitute via right triangle** ($\sec\theta = x/2$, so adjacent = $2$, hypotenuse = $x$):
- Opposite = $\sqrt{x^2-4}$.
- $\tan\theta = \frac{\sqrt{x^2-4}}{2}$.
- $\theta = \operatorname{arcsec}(x/2) = \arctan\left(\frac{\sqrt{x^2-4}}{2}\right)$.

$= 2\left(\frac{\sqrt{x^2-4}}{2} - \arctan\left(\frac{\sqrt{x^2-4}}{2}\right)\right) + C$

$= \boxed{\sqrt{x^2-4} - 2\arctan\left(\frac{\sqrt{x^2-4}}{2}\right) + C}$

---

### A9. $\int x\arcsin x\,dx$

**Parts**: $u = \arcsin x$ (Inverse trig), $dv = x\,dx$.

$du = \frac{1}{\sqrt{1-x^2}}\,dx$, $v = \frac{x^2}{2}$.

$\int x\arcsin x\,dx = \frac{x^2}{2}\arcsin x - \int \frac{x^2}{2} \cdot \frac{1}{\sqrt{1-x^2}}\,dx$

$= \frac{x^2}{2}\arcsin x - \frac{1}{2}\int \frac{x^2}{\sqrt{1-x^2}}\,dx$

For the remaining integral, use trig sub: $x = \sin\theta$, $dx = \cos\theta\,d\theta$.

$\int \frac{x^2}{\sqrt{1-x^2}}\,dx = \int \frac{\sin^2\theta}{\cos\theta} \cdot \cos\theta\,d\theta = \int \sin^2\theta\,d\theta$

$= \int \frac{1-\cos 2\theta}{2}\,d\theta = \frac{\theta}{2} - \frac{\sin 2\theta}{4} + C$

Back-substitute: $\theta = \arcsin x$, $\sin 2\theta = 2\sin\theta\cos\theta = 2x\sqrt{1-x^2}$.

$= \frac{\arcsin x}{2} - \frac{2x\sqrt{1-x^2}}{4} + C = \frac{\arcsin x}{2} - \frac{x}{2}\sqrt{1-x^2} + C$

**Final answer**:

$\int x\arcsin x\,dx = \frac{x^2}{2}\arcsin x - \frac{1}{2}\left(\frac{\arcsin x}{2} - \frac{x}{2}\sqrt{1-x^2}\right) + C$

$= \frac{x^2}{2}\arcsin x - \frac{\arcsin x}{4} + \frac{x}{4}\sqrt{1-x^2} + C$

$= \boxed{\frac{2x^2-1}{4}\arcsin x + \frac{x}{4}\sqrt{1-x^2} + C}$

---

### A10. Derive the reduction formula: $\int \sin^n x\,dx = -\frac{1}{n}\sin^{n-1}x\cos x + \frac{n-1}{n}\int \sin^{n-2}x\,dx$

**Proof via integration by parts**:

Write $\int \sin^n x\,dx = \int \sin^{n-1}x \cdot \sin x\,dx$.

Let $u = \sin^{n-1}x$, $dv = \sin x\,dx$.

Then:
- $du = (n-1)\sin^{n-2}x \cos x\,dx$
- $v = -\cos x$

Apply parts formula $\int u\,dv = uv - \int v\,du$:

$\int \sin^n x\,dx = -\sin^{n-1}x \cos x - \int (-\cos x)(n-1)\sin^{n-2}x \cos x\,dx$

$= -\sin^{n-1}x \cos x + (n-1)\int \sin^{n-2}x \cos^2 x\,dx$

Use $\cos^2 x = 1 - \sin^2 x$:

$= -\sin^{n-1}x \cos x + (n-1)\int \sin^{n-2}x (1 - \sin^2 x)\,dx$

$= -\sin^{n-1}x \cos x + (n-1)\int \sin^{n-2}x\,dx - (n-1)\int \sin^n x\,dx$

Let $I_n = \int \sin^n x\,dx$. Then:

$I_n = -\sin^{n-1}x \cos x + (n-1)I_{n-2} - (n-1)I_n$

Bring $(n-1)I_n$ to the left:

$I_n + (n-1)I_n = -\sin^{n-1}x \cos x + (n-1)I_{n-2}$

$n I_n = -\sin^{n-1}x \cos x + (n-1)I_{n-2}$

$I_n = \boxed{-\frac{1}{n}\sin^{n-1}x \cos x + \frac{n-1}{n}I_{n-2}}$

This is the reduction formula for $\int \sin^n x\,dx$. It reduces the power by 2 each time. Repeated application eventually reaches either $I_0 = \int dx = x + C$ (if $n$ is even) or $I_1 = \int \sin x\,dx = -\cos x + C$ (if $n$ is odd).
