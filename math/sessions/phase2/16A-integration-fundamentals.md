# Session 16A: Integration Fundamentals — FTC and $u$-Substitution

**Phase 2 — Classical Techniques | 80 min**

*Prerequisites: 14A (basic derivatives), 13A (limits)*

---

## Part A: Antiderivatives and the FTC

---

## Example 1: Antiderivatives — "What Differentiates to This?"

$\int f(x)\,dx = F(x) + C$ where $F'(x)=f(x)$. The **$+C$ is mandatory** — infinitely many antiderivatives differ by a constant.

$\int x^3\,dx = \frac{x^4}{4} + C$. Check: $\frac{d}{dx}(\frac{x^4}{4})=x^3$. ✓
$\int e^x\,dx = e^x + C$.
$\int \frac{1}{x}\,dx = \ln|x| + C$ (absolute value!).
$\int \sin x\,dx = -\cos x + C$.
$\int \cos x\,dx = \sin x + C$.

---

## Example 2: The Fundamental Theorem of Calculus (FTC)

$\displaystyle \int_a^b f(x)\,dx = F(b) - F(a)$ where $F'=f$.

The definite integral = **net area** between the curve and the $x$-axis (areas below count negative).

$\displaystyle \int_0^3 x^2\,dx = \left[\frac{x^3}{3}\right]_0^3 = 9-0 = 9$.

$\displaystyle \int_0^\pi \sin x\,dx = [-\cos x]_0^\pi = (-\cos\pi)-(-\cos0) = 1+1 = 2$.

![FTC area under sin x](graphs/16b-sin-area.png)

---

## Example 3: Sum, Difference, Constant Multiple Rules

$\int [f(x)\pm g(x)]dx = \int f(x)dx \pm \int g(x)dx$.
$\int cf(x)dx = c\int f(x)dx$.

$\int (3x^2+2e^x-\frac{1}{x})dx = x^3+2e^x-\ln|x|+C$.

---

## Part B: $u$-Substitution — The Chain Rule Backward

---

## Example 4: Basic $u$-Substitution

$\int 2x(x^2+1)^5\,dx$. Let $u=x^2+1$, $du=2x\,dx$.

$\int u^5\,du = \frac{u^6}{6}+C = \frac{(x^2+1)^6}{6}+C$.

**The trick**: spot $u$ and its derivative $du$ inside the integrand.

---

## Example 5: Trigonometric $u$-Substitution

$\int \sin^3 x\cos x\,dx$. $u=\sin x$, $du=\cos x\,dx$.
$\int u^3\,du = \frac{u^4}{4}+C = \frac{\sin^4 x}{4}+C$.

$\int \tan x\,dx = \int\frac{\sin x}{\cos x}dx$. $u=\cos x$, $du=-\sin x\,dx$.
$= -\int\frac{1}{u}du = -\ln|u|+C = -\ln|\cos x|+C = \ln|\sec x|+C$.

---

## Example 6: Exponential and Log $u$-Substitution

$\int xe^{x^2}\,dx$. $u=x^2$, $du=2x\,dx \to x\,dx=\frac{du}{2}$.
$\int e^u\frac{du}{2} = \frac{e^u}{2}+C = \frac{e^{x^2}}{2}+C$.

$\int \frac{\ln x}{x}\,dx$. $u=\ln x$, $du=\frac{1}{x}dx$.
$\int u\,du = \frac{u^2}{2}+C = \frac{(\ln x)^2}{2}+C$.

---

## Example 7: Definite Integrals with $u$-Substitution

**Change the bounds when you change the variable!**

$\displaystyle \int_0^1 2x(x^2+1)^4\,dx$. $u=x^2+1$, $du=2x\,dx$.
$x=0 \to u=1$, $x=1 \to u=2$.
$\displaystyle \int_1^2 u^4\,du = \left[\frac{u^5}{5}\right]_1^2 = \frac{32}{5}-\frac{1}{5} = \frac{31}{5}$.

> **Up to here**: FTC connects derivative and integral. $u$-sub = reverse chain rule. Always change bounds for definite integrals.

---

## Common Mistakes

### Mistake 1: Forgetting $+C$ on indefinite integrals
### Mistake 2: Not changing bounds in definite $u$-substitution
### Mistake 3: $\int\frac{1}{x}dx = \ln x + C$ (missing absolute value)

---

## What We Just Did

```
(1) Antiderivative = reverse derivative. ∫f = F+C where F'=f.
(2) FTC: ∫_a^b f = F(b)-F(a). Definite integral = net signed area.
(3) u-substitution: let u = inner function, du = its derivative dx.
    Replace everything in terms of u, integrate, substitute back.
(4) Definite: change bounds to u-values. Don't go back to x.
```

---

## Practice 1

$\displaystyle \int (4x^3-2x+5)\,dx$. Basic antiderivative.

→ Solutions: [Solutions](solutions/16A-solutions.md#practice-1)

---

## Practice 2

$\displaystyle \int_0^2 (3x^2+1)\,dx$. FTC.

→ Solutions: [Solutions](solutions/16A-solutions.md#practice-2)

---

## Practice 3

$\displaystyle \int x\sqrt{x^2+4}\,dx$. $u$-substitution.

→ Solutions: [Solutions](solutions/16A-solutions.md#practice-3)

---

## Practice 4

$\displaystyle \int_0^{\pi/2} \sin x\cos^2 x\,dx$. $u$-sub with bounds.

→ Solutions: [Solutions](solutions/16A-solutions.md#practice-4)

---

## Basic Algebra Drill — Integration Fundamentals (10 Problems)

**D1.** $\int x^5\,dx$.

**D2.** $\int (2e^x + \frac{3}{x})\,dx$.

**D3.** $\int_1^4 \sqrt{x}\,dx$.

**D4.** $\int_0^{\pi} \cos x\,dx$.

**D5.** $\int 3x^2(x^3+1)^4\,dx$. $u$-sub.

**D6.** $\int e^{3x}\,dx$. $u$-sub.

**D7.** $\int \frac{x}{x^2+1}\,dx$. $u$-sub.

**D8.** $\int_0^1 xe^{x^2}\,dx$. $u$-sub with bounds.

**D9.** $\int \frac{\cos x}{\sin x}\,dx$. $u$-sub.

**D10.** $\int_{-1}^2 (x^2-2x)\,dx$. FTC.

> Solutions: [Solutions](solutions/16A-solutions.md#basic-drill)

---

## Advanced Algebra Drill — Integration Fundamentals (10 Problems)

**A1.** $\int x^2\sqrt{x^3+1}\,dx$. $u$-sub.

**A2.** $\int \frac{e^x}{1+e^{2x}}\,dx$. $u=e^x$, then arctan.

**A3.** $\int_0^4 \frac{x}{\sqrt{1+2x}}\,dx$. $u=1+2x$.

**A4.** $\int \sin^5 x\cos x\,dx$. $u$-sub.

**A5.** $\int_1^e \frac{(\ln x)^2}{x}\,dx$. $u$-sub with bounds.

**A6.** Find $F(x)=\int_0^x \sin(t^2)\,dt$ and compute $F'(x)$. (FTC Part 1.)

**A7.** $\int \frac{1}{x\ln x}\,dx$. $u=\ln x$.

**A8.** $\int_0^{\pi/4} \tan x\,dx$. $u=\cos x$, change bounds.

**A9.** $\int_0^1 \frac{x}{1+x^4}\,dx$. $u=x^2$, then arctan.

**A10.** Prove $\int_{-a}^a \sin x\,dx = 0$ for any $a$. Use the odd function property.

> Solutions: [Solutions](solutions/16A-solutions.md#advanced-drill)

---

## Today's Procedure

```
Step 1: For indefinite integrals, find F such that F'=f. Always add +C.
Step 2: For definite integrals, apply FTC: F(b)-F(a).
Step 3: For u-sub: u=g(x), du=g'(x)dx. Replace all x's with u's.
    For definite: change the bounds to u-values.
```
