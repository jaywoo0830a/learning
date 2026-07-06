# Session 14A: Derivative Fundamentals — The Basic Toolbox

**Phase 2 — Classical Techniques | 70 min**

*Prerequisites: 13A (algebraic limits), 10A (exponents & logs), 11A (trig foundations)*

---

## Part A: What Is a Derivative?

---

## Example 1: The Limit Definition

A derivative is **instantaneous slope** — the slope of the tangent line at a single point. You find it by shrinking the interval between two points to zero:

$f'(x) = \displaystyle \lim_{h\to 0}\frac{f(x+h)-f(x)}{h}$.

For $f(x)=x^2$ at $x=3$:

① Average rate: $\frac{f(3+h)-f(3)}{h} = \frac{(9+6h+h^2)-9}{h} = \frac{6h+h^2}{h} = 6+h$.
② Send $h\to0$: $6+h \to 6$.
③ $f'(3)=6$ — the slope of the tangent line at $x=3$.

![Tangent line derivative](graphs/14a-tangent.png)

---

## Part B: The Power Rule and Basic Derivatives

---

## Example 2: The Power Rule — $\frac{d}{dx}x^n = nx^{n-1}$

Bring the exponent down as a coefficient, then subtract 1 from the exponent.

$\frac{d}{dx}x^5 = 5x^4$.
$\frac{d}{dx}x^{100} = 100x^{99}$.
$\frac{d}{dx}\sqrt{x} = \frac{d}{dx}x^{1/2} = \frac{1}{2}x^{-1/2} = \frac{1}{2\sqrt{x}}$.
$\frac{d}{dx}\frac{1}{x^3} = \frac{d}{dx}x^{-3} = -3x^{-4} = -\frac{3}{x^4}$.

**Constant rule**: $\frac{d}{dx}7 = 0$. A flat line has zero slope.
**Constant multiple**: $\frac{d}{dx}(5x^3) = 5\cdot 3x^2 = 15x^2$. The constant rides along.

---

## Example 3: Exponential and Logarithmic Derivatives

$\frac{d}{dx}e^x = e^x$. **The only function that is its own derivative.**
$\frac{d}{dx}e^{2x} = e^{2x}\cdot 2 = 2e^{2x}$ (chain rule — preview of 14B).

$\frac{d}{dx}\ln x = \frac{1}{x}$ ($x>0$).
$\frac{d}{dx}\ln(5x) = \frac{1}{5x}\cdot 5 = \frac{1}{x}$.

$\frac{d}{dx}a^x = a^x\ln a$ ($a>0$). $\frac{d}{dx}2^x = 2^x\ln 2$.
$\frac{d}{dx}\log_a x = \frac{1}{x\ln a}$.

---

## Example 4: Trigonometric Derivatives — A Cyclic Dance

$\frac{d}{dx}\sin x = \cos x$.
$\frac{d}{dx}\cos x = -\sin x$. (Sign flips!)
$\frac{d}{dx}\tan x = \sec^2 x$.

The full set:
$\frac{d}{dx}\csc x = -\csc x\cot x$.
$\frac{d}{dx}\sec x = \sec x\tan x$.
$\frac{d}{dx}\cot x = -\csc^2 x$.

**Memory aid**: $\sin\to\cos$, $\cos\to-\sin$. Differentiate four times and you return to $\sin x$.

![Derivative of sin is cos](graphs/14b-sin-derivative.png)

---

## Example 5: Sum, Difference, and Constant Multiple Rules

Derivatives split across sums: $(f\pm g)' = f' \pm g'$.

$\frac{d}{dx}(3x^4 - 2x^2 + 5x - 7) = 12x^3 - 4x + 5$.

$\frac{d}{dx}(2\sin x + e^x - \ln x) = 2\cos x + e^x - \frac{1}{x}$.

> **Up to here**: Power rule (bring down exponent, subtract 1). $e^x$ stays $e^x$. $\ln x \to 1/x$.
> $\sin \to \cos$, $\cos \to -\sin$, $\tan \to \sec^2$. Sums split apart.

---

## Common Mistakes

### Mistake 1: Forgetting the negative sign for $\cos x$

**Wrong**: $\frac{d}{dx}\cos x = \sin x$. **Right**: $\frac{d}{dx}\cos x = -\sin x$.

### Mistake 2: $\frac{d}{dx}e^x = xe^{x-1}$

**Wrong**: Using the power rule on an exponential. **Right**: $\frac{d}{dx}e^x = e^x$.

### Mistake 3: $\frac{d}{dx}\ln x = x\ln x$

**Wrong**. **Right**: $\frac{d}{dx}\ln x = \frac{1}{x}$.

---

## What We Just Did

```
(1) Derivative definition: f'(x) = lim_{h→0} [f(x+h)-f(x)]/h.
(2) Power rule: d/dx(x^n) = n x^{n-1}. Works for any real n.
(3) Exponential: d/dx(e^x)=e^x, d/dx(a^x)=a^x ln a.
(4) Logarithmic: d/dx(ln x)=1/x.
(5) Trig: d/dx(sin x)=cos x, d/dx(cos x)=-sin x, d/dx(tan x)=sec² x.
```

---

## Practice 1

Use the limit definition: find $f'(2)$ for $f(x)=x^2+3x$.

→ Reference: **Example 1**

> Solutions: [Solutions](solutions/14A-solutions.md#practice-1)

---

## Practice 2

Differentiate: $f(x)=4x^5 - 3x^3 + 2x - 1 + \frac{1}{x}$.

→ Reference: **Example 2, 5**

> Solutions: [Solutions](solutions/14A-solutions.md#practice-2)

---

## Practice 3

Differentiate: $g(x)=3e^x - 2\ln x + 5\sin x - \cos x$.

→ Reference: **Example 3, 4, 5**

> Solutions: [Solutions](solutions/14A-solutions.md#practice-3)

---

## Practice 4

Differentiate: $h(x)=2^x + \log_3 x + \tan x$.

→ Reference: **Example 3, 4**

> Solutions: [Solutions](solutions/14A-solutions.md#practice-4)

---

## Practice 5

Find all $x$ where $f'(x)=0$ for $f(x)=x^3-3x^2-9x+5$.

→ Reference: **Example 2, 5**

> Solutions: [Solutions](solutions/14A-solutions.md#practice-5)

---

## Practice 6: Real Battle

Find the equation of the tangent line to $f(x)=x^2+\ln x$ at $x=1$.

→ Reference: **Example 1, 3**

> Solutions: [Solutions](solutions/14A-solutions.md#practice-6)

---

## Basic Algebra Drill — Derivative Fundamentals (10 Problems)

**D1.** $\frac{d}{dx}(7x^4)$. Use the power rule.

**D2.** $\frac{d}{dx}(-3x^{10})$. Power rule with negative coefficient.

**D3.** $\frac{d}{dx}(\sqrt[3]{x})$. Write as $x^{1/3}$.

**D4.** $\frac{d}{dx}(5e^x)$. Constant multiple + exponential.

**D5.** $\frac{d}{dx}(4\ln x)$. Constant multiple + log.

**D6.** $\frac{d}{dx}(3\sin x - 2\cos x)$. Trig derivatives.

**D7.** $\frac{d}{dx}(\tan x + \sec x)$. Trig derivatives.

**D8.** $\frac{d}{dx}(2^x + \log_5 x)$. General exponential/log.

**D9.** $\frac{d}{dx}\left(\frac{1}{x^4}\right)$. Write as $x^{-4}$.

**D10.** Find $f'(0)$ for $f(x)=x^3-2x^2+5x-1$.

> Solutions: [Solutions](solutions/14A-solutions.md#basic-drill)

---

## Advanced Algebra Drill — Derivative Fundamentals (10 Problems)

**A1.** Use the limit definition to prove $\frac{d}{dx}x^2 = 2x$.

**A2.** Find $a$ and $b$ so that $f(x)=ax^2+bx$ has $f'(1)=5$ and $f'(2)=9$.

**A3.** Differentiate $f(x)=\frac{x^3}{\sqrt{x}}$. Simplify first using exponent laws.

**A4.** Find the point on $y=x^2$ where the tangent line has slope 6.

**A5.** Differentiate $f(x)=e^{x}\sin x$ (product rule preview — use the definition pattern or wait for 14B).

**A6.** Find the $x$-values where $f(x)=x^3-6x^2+9x$ has horizontal tangent lines.

**A7.** Prove $\frac{d}{dx}\tan x = \sec^2 x$ using $\tan x = \frac{\sin x}{\cos x}$ and the quotient rule from 14B.

**A8.** Differentiate $f(x)=\ln(x^2)$ in two ways: (a) using $\ln(x^2)=2\ln x$, (b) using the chain rule. Verify they agree.

**A9.** A function satisfies $f'(x)=f(x)$ for all $x$ and $f(0)=3$. What must $f(x)$ be? (Hint: which function is its own derivative?)

**A10.** Find the equation of the line tangent to $y=e^x$ that passes through the origin. (Hint: the line has slope $e^a$ at $x=a$ and passes through $(0,0)$.)

> Solutions: [Solutions](solutions/14A-solutions.md#advanced-drill)

---

## Today's Procedure

```
Step 1: Memorize the five basic derivative families —
    Power: x^n → n x^{n-1}
    Exponential: e^x → e^x, a^x → a^x ln a
    Log: ln x → 1/x
    Trig: sin→cos, cos→-sin, tan→sec²
    Constants and sums split apart.

Step 2: The limit definition f'(x)=lim(f(x+h)-f(x))/h is the foundation.
    Every derivative rule can be proven from it.
```

---

## Terminology

| What we call it | Math term | Notation |
|:---------------:|:---------:|:--------:|
| instantaneous slope | derivative | $f'(x)$, $\frac{dy}{dx}$ |
| limit definition | difference quotient limit | $\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$ |
| power rule | power rule | $\frac{d}{dx}x^n = nx^{n-1}$ |
| its own derivative | exponential invariance | $\frac{d}{dx}e^x=e^x$ |
| tangent line | tangent line | $y-f(a)=f'(a)(x-a)$ |
