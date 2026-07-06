# Session 16B: Advanced Integration — Parts, Trig Integrals, Trig Sub, Partial Fractions

**Phase 2 — Classical Techniques | 85 min**

*Prerequisites: 16A (FTC & u-sub), 14B (chain/product rules), 11A (trig)*

---

## Part A: Integration by Parts — The Product Rule Backward

---

## Example 1: Basic Integration by Parts

$\int u\,dv = uv - \int v\,du$. **Choose $u$ using LIATE**: Log, Inverse trig, Algebraic, Trig, Exponential (priority order for $u$).

$\int x e^x\,dx$. $u=x$ (Algebraic), $dv=e^x dx$. $du=dx$, $v=e^x$.
$= x e^x - \int e^x\,dx = x e^x - e^x + C = e^x(x-1)+C$.

---

## Example 2: Log — $u=\ln x$

$\int \ln x\,dx$. $u=\ln x$, $dv=dx$. $du=\frac{1}{x}dx$, $v=x$.
$= x\ln x - \int x\cdot\frac{1}{x}dx = x\ln x - x + C$.

---

## Example 3: Inverse Trig — $u=\arctan x$

$\int \arctan x\,dx$. $u=\arctan x$, $dv=dx$. $du=\frac{1}{1+x^2}dx$, $v=x$.
$= x\arctan x - \int \frac{x}{1+x^2}dx$. Second integral: $w=1+x^2$, $dw=2x\,dx$ → $\frac{1}{2}\ln(1+x^2)$.
$= x\arctan x - \frac{1}{2}\ln(1+x^2) + C$.

---

## Example 4: Trig×Exponential — Two Rounds of Parts

$\int e^x\sin x\,dx$. $u=\sin x$, $dv=e^x dx$. $du=\cos x\,dx$, $v=e^x$.
$I = e^x\sin x - \int e^x\cos x\,dx$.

Second parts: $u=\cos x$, $dv=e^x dx$. $\int e^x\cos x\,dx = e^x\cos x + \int e^x\sin x\,dx = e^x\cos x + I$.

$I = e^x\sin x - (e^x\cos x + I) = e^x\sin x - e^x\cos x - I$.
$2I = e^x(\sin x - \cos x) \to I = \frac{e^x}{2}(\sin x - \cos x) + C$.

---

## Example 5: Reduction Formula Pattern

$\int x^n e^x\,dx$: parts with $u=x^n$ repeats $n$ times, each time reducing the power.

---

## Part B: Trigonometric Integrals

---

## Example 6: $\int \sin^n x\,dx$, $\int \cos^n x\,dx$

**Odd power**: peel off one factor, convert the rest using $\sin^2+\cos^2=1$, $u$-sub.

$\int \sin^3 x\,dx = \int \sin x(1-\cos^2 x)dx$. $u=\cos x$, $du=-\sin x\,dx$.
$= -\int(1-u^2)du = -u+\frac{u^3}{3}+C = -\cos x+\frac{\cos^3 x}{3}+C$.

**Even power**: use half-angle formulas: $\sin^2 x=\frac{1-\cos2x}{2}$, $\cos^2 x=\frac{1+\cos2x}{2}$.

$\int \cos^2 x\,dx = \int\frac{1+\cos2x}{2}dx = \frac{x}{2}+\frac{\sin2x}{4}+C$.

---

## Example 7: $\int \tan^n x\sec^m x\,dx$

Strategy depends on parity of $n$ and $m$. Key identity: $\sec^2 x = \tan^2 x+1$.

$\int \tan^3 x\sec^2 x\,dx$. $u=\tan x$, $du=\sec^2 x\,dx$. $= \frac{\tan^4 x}{4}+C$.

---

## Part C: Trigonometric Substitution — Eliminating Roots

---

## Example 8: $\sqrt{a^2-x^2}$ → $x=a\sin\theta$

$\displaystyle \int \frac{dx}{\sqrt{4-x^2}}$. $x=2\sin\theta$, $dx=2\cos\theta\,d\theta$, $\sqrt{4-x^2}=2\cos\theta$.
$= \int\frac{2\cos\theta}{2\cos\theta}d\theta = \int d\theta = \theta+C = \arcsin\frac{x}{2}+C$.

$\displaystyle \int \sqrt{9-x^2}\,dx$. $x=3\sin\theta$. After substitution: $\int 9\cos^2\theta\,d\theta = \frac{9}{2}(\theta+\sin\theta\cos\theta)+C$. Back-substitute.

---

## Example 9: $\sqrt{x^2\pm a^2}$ → $x=a\tan\theta$ or $x=a\sec\theta$

$\sqrt{a^2+x^2}$: $x=a\tan\theta$, $dx=a\sec^2\theta\,d\theta$, $\sqrt{a^2+x^2}=a\sec\theta$.

$\displaystyle \int\frac{dx}{\sqrt{x^2+1}}$. $x=\tan\theta$. $=\int\sec\theta\,d\theta = \ln|\sec\theta+\tan\theta|+C = \ln|x+\sqrt{x^2+1}|+C$.

$\sqrt{x^2-a^2}$: $x=a\sec\theta$.

---

## Part D: Partial Fractions — Rational Function Integration

---

## Example 10: Distinct Linear Factors

$\displaystyle \int\frac{1}{x^2-1}\,dx = \int\frac{1}{(x-1)(x+1)}dx$.

Decompose: $\frac{1}{x^2-1} = \frac{A}{x-1}+\frac{B}{x+1}$. Solve: $1=A(x+1)+B(x-1)$. $A=\frac{1}{2}, B=-\frac{1}{2}$.
$= \frac{1}{2}\ln|x-1| - \frac{1}{2}\ln|x+1| + C = \frac{1}{2}\ln\left|\frac{x-1}{x+1}\right|+C$.

---

## Example 11: Repeated and Quadratic Factors

$\int\frac{x}{(x-1)^2}dx$. Decompose: $\frac{x}{(x-1)^2} = \frac{A}{x-1}+\frac{B}{(x-1)^2}$. $A=1,B=1$.
$= \ln|x-1| - \frac{1}{x-1} + C$.

---

## What We Just Did

```
(1) Integration by parts: ∫u dv = uv - ∫v du. LIATE rule for choosing u.
(2) Trig integrals: odd power → peel+u-sub. Even power → half-angle.
    tan^m sec^n: save sec² for du, or tan sec for pattern.
(3) Trig substitution: √(a²-x²)→x=a sinθ, √(a²+x²)→x=a tanθ, √(x²-a²)→x=a secθ.
(4) Partial fractions: decompose rational function into sum of simpler ones.
```

---

## Practice 1

$\int x\sin x\,dx$. Integration by parts.

→ Solutions: [Solutions](solutions/16B-solutions.md#practice-1)

---

## Practice 2

$\int \cos^3 x\,dx$. Trig integral (odd power).

→ Solutions: [Solutions](solutions/16B-solutions.md#practice-2)

---

## Practice 3

$\displaystyle \int \frac{dx}{x^2+4}$. Trig substitution or arctan formula.

→ Solutions: [Solutions](solutions/16B-solutions.md#practice-3)

---

## Practice 4

$\displaystyle \int \frac{x+1}{x^2-3x+2}\,dx$. Partial fractions.

→ Solutions: [Solutions](solutions/16B-solutions.md#practice-4)

---

## Basic Algebra Drill — Advanced Integration (10 Problems)

**D1.** $\int x\cos x\,dx$. Parts.

**D2.** $\int \ln(2x)\,dx$. Parts.

**D3.** $\int \sin^2 x\,dx$. Half-angle.

**D4.** $\int \tan x\sec^2 x\,dx$. $u$-sub.

**D5.** $\displaystyle \int \frac{dx}{\sqrt{9-x^2}}$. Trig sub.

**D6.** $\displaystyle \int \frac{dx}{x^2+9}$. Arctan formula.

**D7.** $\displaystyle \int \frac{1}{x^2-x}\,dx$. Partial fractions.

**D8.** $\int x^2 e^x\,dx$. Parts twice.

**D9.** $\int \sin x\cos x\,dx$. $u$-sub or double-angle.

**D10.** $\displaystyle \int \frac{x}{\sqrt{1-x^2}}\,dx$. $u$-sub.

> Solutions: [Solutions](solutions/16B-solutions.md#basic-drill)

---

## Advanced Algebra Drill — Advanced Integration (10 Problems)

**A1.** $\int e^x\cos x\,dx$. Parts twice, solve for the integral.

**A2.** $\int \sin^4 x\,dx$. Repeated half-angle.

**A3.** $\displaystyle \int \frac{dx}{(x^2+1)^2}$. Trig sub $x=\tan\theta$.

**A4.** $\displaystyle \int \frac{x^3}{\sqrt{x^2+1}}\,dx$. $u=x^2+1$.

**A5.** $\displaystyle \int \frac{x^2+2x-1}{(x-1)(x^2+1)}\,dx$. Partial fractions with quadratic factor.

**A6.** $\int \arctan x\,dx$. Parts.

**A7.** $\int \sec^3 x\,dx$. Parts with $u=\sec x$, $dv=\sec^2 x\,dx$.

**A8.** $\displaystyle \int \frac{\sqrt{x^2-4}}{x}\,dx$. Trig sub $x=2\sec\theta$.

**A9.** $\int x\arcsin x\,dx$. Parts.

**A10.** Derive the reduction formula: $\int \sin^n x\,dx = -\frac{1}{n}\sin^{n-1}x\cos x + \frac{n-1}{n}\int\sin^{n-2}x\,dx$.

> Solutions: [Solutions](solutions/16B-solutions.md#advanced-drill)

---

## Today's Procedure

```
Step 1: Parts → LIATE for u. Let dv be everything else.
Step 2: Trig integrals: odd power → peel+sub. Even → half-angle.
Step 3: Trig sub: √(a²-x²)→sin, √(a²+x²)→tan, √(x²-a²)→sec.
Step 4: Partial fractions: factor denominator, decompose, solve for constants.
```
