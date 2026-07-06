# Session 14C: Higher Derivatives & Mixed Techniques

**Phase 2 — Classical Techniques | 60 min**

*Prerequisites: 14A (basic derivatives), 14B (product/quotient/chain/implicit)*

---

## Example 1: Second and Third Derivatives

$f''(x) = \frac{d}{dx}f'(x)$. The derivative of the derivative — **acceleration**.

$f(x)=x^4-3x^3+2x$: $f'(x)=4x^3-9x^2+2$, $f''(x)=12x^2-18x$, $f'''(x)=24x-18$.

---

## Example 2: Meaning of Higher Derivatives

- $f'$ = slope (velocity). $f''$ = concavity (acceleration). $f'''$ = jerk.

$f(x)=\sin x$: $f'=\cos x$, $f''=-\sin x$, $f'''=-\cos x$, $f^{(4)}=\sin x$. Cycle of 4.

---

## Example 3: Mixed Technique Problems

**$f(x)=e^x\sin x + \ln(\cos x)$**:
$f'(x)=e^x\sin x + e^x\cos x - \tan x = e^x(\sin x+\cos x) - \tan x$.

**$f(x)=x^3e^{2x}\tan x$ (triple product)**:
$f'=3x^2e^{2x}\tan x + x^3\cdot2e^{2x}\tan x + x^3e^{2x}\sec^2 x = x^2e^{2x}[3\tan x + 2x\tan x + x\sec^2 x]$.

**$f(x)=\arctan(\ln x)$**: $f'=\frac{1}{1+(\ln x)^2}\cdot\frac{1}{x}$.

---

## Example 4: Finding the $n$-th Derivative Pattern

$f(x)=e^{3x}$: $f^{(n)}(x)=3^n e^{3x}$.
$f(x)=\frac{1}{x}$: $f^{(n)}(x)=(-1)^n n!\,x^{-(n+1)}$.
$f(x)=\sin x$: $f^{(n)}(x)=\sin(x+\frac{n\pi}{2})$.

---

## What We Just Did

```
(1) Higher derivatives: differentiate repeatedly. f'' = (f')'.
(2) Physical meaning: f'=velocity, f''=acceleration, f'''=jerk.
(3) Mixed problems use product + chain + trig + log simultaneously.
(4) nth derivative patterns: exponentials scale by a^n, trig cycles with period 4.
```

---

## Practice 1

Find $f''(x)$ for $f(x)=x^5-2x^3+x$.

→ Solutions: [Solutions](solutions/14C-solutions.md#practice-1)

---

## Practice 2

Find $f^{(4)}(x)$ (4th derivative) of $f(x)=e^{2x}$.

→ Solutions: [Solutions](solutions/14C-solutions.md#practice-2)

---

## Practice 3

Differentiate: $f(x)=\frac{e^x\sin x}{x^2+1}$. Use quotient + product + chain.

→ Solutions: [Solutions](solutions/14C-solutions.md#practice-3)

---

## Basic Algebra Drill — Higher Derivatives (10 Problems)

**D1.** Find $f''(x)$ for $f(x)=3x^4-5x^2+2x-7$.

**D2.** Find $f'''(x)$ for $f(x)=x^5$.

**D3.** Find $f''(x)$ for $f(x)=e^{-x}$.

**D4.** Find $f''(x)$ for $f(x)=\ln x$.

**D5.** Find $f''(x)$ for $f(x)=\sin 2x$.

**D6.** Find $f^{(n)}(x)$ for $f(x)=e^{5x}$.

**D7.** Find $f''(x)$ for $f(x)=x\ln x$.

**D8.** Find $f''(x)$ for $f(x)=\tan x$ at $x=0$.

**D9.** Differentiate: $f(x)=\arcsin(x^2)+\arctan(e^x)$.

**D10.** $f(x)=|x^3|$. Where is $f'(x)$ undefined?

> Solutions: [Solutions](solutions/14C-solutions.md#basic-drill)

---

## Advanced Algebra Drill — Higher Derivatives (10 Problems)

**A1.** Prove Leibniz rule: $(fg)'' = f''g + 2f'g' + fg''$.

**A2.** Find $f^{(100)}(x)$ for $f(x)=x e^x$.

**A3.** $f(x)=\frac{1}{1-x}$. Find a formula for $f^{(n)}(x)$.

**A4.** Find $f''(\pi/4)$ for $f(x)=\sin^2 x$.

**A5.** Differentiate $f(x)=\ln(\sin x + \cos x)$ and find $f''(0)$.

**A6.** Prove that $y=e^x\sin x$ satisfies $y''-2y'+2y=0$.

**A7.** Find all $x$ where $f''(x)=0$ for $f(x)=x^4-6x^2+8x$.

**A8.** Differentiate $f(x)=x^{x^x}$ using log-diff twice.

**A9.** Find $\frac{d^2y}{dx^2}$ for $x^2+y^2=1$ using implicit differentiation twice.

**A10.** $f(x)=\frac{ax+b}{cx+d}$. Show that $f'''(x)=0$ for all $x \neq -d/c$.

> Solutions: [Solutions](solutions/14C-solutions.md#advanced-drill)

---

## Today's Procedure

```
Step 1: Higher derivatives = differentiate repeatedly. Keep going until
    the requested order is reached.

Step 2: Mixed problems: identify the outermost structure first
    (product? quotient? chain?), then work inward.

Step 3: nth derivative: look for the pattern. Exponential scales by a^n.
    Trig cycles. Rational follows factorial pattern.
```
