# Session 14B: Advanced Differentiation — Product, Quotient, Chain, and Implicit

**Phase 2 — Classical Techniques | 80 min**

*Simple functions differentiate with a dictionary lookup. Products, quotients, and nested functions need rules. This session gives you a decision tree: identify the structure, apply the matching procedure. By the end, you can differentiate anything built from elementary functions.*

**Prerequisites**: 14A (basic derivative dictionary), 10A (exponents & logs), 11A (trig)

---

## The Differentiation Decision Tree

> **Before you start**, identify the outermost structure. Match it to a procedure.

```
Look at the function. What is the LAST operation you would perform when evaluating?

1. Is it f ± g?                  → Split and differentiate each piece (14A)
2. Is it f × g (product)?        → PRODUCT RULE (14B-A)
3. Is it f ÷ g (quotient)?       → QUOTIENT RULE (14B-A)
4. Is it f(g(x)) (composition)?  → CHAIN RULE (14B-B)
5. Are x and y mixed together?   → IMPLICIT DIFFERENTIATION (14B-C)
6. Is it f(x)^{g(x)}?            → LOGARITHMIC DIFFERENTIATION (14B-C)
7. Is it parametric (x(t),y(t))? → PARAMETRIC: dy/dx = (dy/dt)/(dx/dt) (14B-D)
```

---

## Part A: Product and Quotient — Multiplication and Division

---

## Example 1: Product Rule — $(fg)' = f'g + fg'$

**Procedure**:

| Step | Action |
|:---:|:---|
| 1 | Identify the **two factors**: $f(x)$ and $g(x)$ |
| 2 | Differentiate the **first**: $f'(x)$. Leave the second alone. |
| 3 | Differentiate the **second**: $g'(x)$. Leave the first alone. |
| 4 | **Add** the two products: $f'(x)g(x) + f(x)g'(x)$ |
| 5 | Simplify — factor common terms if possible |

**Memory**: "First derivative × second + first × second derivative."

$\frac{d}{dx}(x^2\sin x)$:

| Step | Action |
|:---:|:---|
| 1 | $f=x^2$, $g=\sin x$ |
| 2 | $f'=2x$ |
| 3 | $g'=\cos x$ |
| 4 | $2x\cdot\sin x + x^2\cdot\cos x = 2x\sin x + x^2\cos x$ |

**Triple product**: $(fgh)' = f'gh + fg'h + fgh'$. Pattern: differentiate one factor at a time.

$\frac{d}{dx}(x e^x \sin x) = 1\cdot e^x\sin x + x\cdot e^x\sin x + x e^x\cdot\cos x = e^x(\sin x + x\sin x + x\cos x)$.

---

## Example 2: Quotient Rule — $(f/g)' = \frac{f'g - fg'}{g^2}$

**Procedure**:

| Step | Action |
|:---:|:---|
| 1 | Identify **top** $f(x)$ and **bottom** $g(x)$ |
| 2 | Differentiate top: $f'(x)$. Differentiate bottom: $g'(x)$ |
| 3 | Assemble numerator: $f'(x)g(x) - f(x)g'(x)$ (top derivative FIRST) |
| 4 | Denominator: $[g(x)]^2$ |
| 5 | Simplify algebraically — expand, cancel, factor |

**Memory**: "Low d-high minus high d-low, over low squared."

$\frac{d}{dx}\frac{x^2}{x+1}$:

| Step | Action |
|:---:|:---|
| 1 | $f=x^2$ (top), $g=x+1$ (bottom) |
| 2 | $f'=2x$, $g'=1$ |
| 3 | Numerator: $2x(x+1) - x^2(1) = 2x^2+2x - x^2 = x^2+2x$ |
| 4 | Denominator: $(x+1)^2$ |
| 5 | $\frac{x^2+2x}{(x+1)^2} = \frac{x(x+2)}{(x+1)^2}$ |

---

## Example 3: Product vs. Quotient — The Decision

| If... | Use... | Because... |
|:---|:---|:---|
| Two factors multiplied | Product rule | $(fg)' = f'g + fg'$ |
| A fraction | Quotient rule | $(f/g)' = (f'g-fg')/g^2$ |
| A fraction where bottom is simple ($x^n$) | Rewrite as $f \cdot x^{-n}$, use product rule | Often faster — avoids quotient rule algebra |

$\frac{d}{dx}\frac{\sin x}{x}$: Use quotient rule. $f=\sin x$, $g=x$. $\frac{\cos x\cdot x - \sin x\cdot 1}{x^2} = \frac{x\cos x - \sin x}{x^2}$.

$\frac{d}{dx}\frac{3}{x^2}$: Rewrite as $3x^{-2}$. Power rule: $-6x^{-3} = -\frac{6}{x^3}$. Faster than quotient rule.

---

## Part B: The Chain Rule — Differentiating Nested Functions

> **The most important rule in all of calculus.** When one function is inside another, differentiate layer by layer from outside in.

---

## Example 4: The Chain Rule Algorithm — Peel the Onion

**Procedure for $(f \circ g)(x) = f(g(x))$**:

| Step | Action |
|:---:|:---|
| 1 | Identify the **outer function** $f$ (the last thing you'd evaluate) |
| 2 | Identify the **inner function** $g$ (inside the parentheses, root, exponent, etc.) |
| 3 | Differentiate the **outer**: $f'(\text{leave inside untouched})$ |
| 4 | Multiply by the derivative of the **inner**: $g'(x)$ |

**Memory**: "Derivative of outside × derivative of inside."

---

## Example 5: Basic Chain Rule — One Layer

$\frac{d}{dx}(x^2+1)^5$:

| Step | Action |
|:---:|:---|
| 1 | Outer: $(\square)^5 \to$ power rule on the outside |
| 2 | Inner: $\square = x^2+1$ |
| 3 | Outer derivative: $5(x^2+1)^4$ (bring 5 down, leave inside untouched) |
| 4 | Inner derivative: $2x$. Multiply: $5(x^2+1)^4 \cdot 2x = 10x(x^2+1)^4$ |

$\frac{d}{dx}\sin(x^3)$: Outer = $\sin(\square) \to \cos(\square)$. Inner = $x^3 \to 3x^2$. Result: $\cos(x^3)\cdot 3x^2 = 3x^2\cos(x^3)$.

$\frac{d}{dx}e^{\sin x}$: Outer = $e^{\square} \to e^{\square}$. Inner = $\sin x \to \cos x$. Result: $e^{\sin x}\cos x$.

$\frac{d}{dx}\ln(\cos x)$: Outer = $\ln(\square) \to 1/\square$. Inner = $\cos x \to -\sin x$. Result: $\frac{1}{\cos x}\cdot(-\sin x) = -\tan x$.

---

## Example 6: Nested Chain — Two or Three Layers

**Procedure for multiple layers**: Peel from outermost to innermost, writing each derivative in a chain. Multiply them all together.

$\frac{d}{dx}\sin(e^{x^2})$:

| Layer | Function | Derivative |
|:---:|:---|:---|
| Outermost | $\sin(\square)$ | $\cos(e^{x^2})$ |
| Middle | $e^{\square}$ | $e^{x^2}$ |
| Innermost | $x^2$ | $2x$ |

Multiply all three: $\cos(e^{x^2}) \cdot e^{x^2} \cdot 2x = 2x e^{x^2}\cos(e^{x^2})$.

$\frac{d}{dx}\sqrt{\ln(\sin x)}$:

| Layer | Derivative |
|:---|:---|
| $\sqrt{\square} = (\square)^{1/2}$ | $\frac{1}{2}(\ln(\sin x))^{-1/2}$ |
| $\ln(\square)$ | $\frac{1}{\sin x}$ |
| $\sin x$ | $\cos x$ |

Multiply: $\frac{1}{2\sqrt{\ln(\sin x)}} \cdot \frac{1}{\sin x} \cdot \cos x = \frac{\cot x}{2\sqrt{\ln(\sin x)}}$.

---

## Example 7: Chain Rule Quick Reference

| Outer form | Outer derivative | Example |
|:---|:---|:---|
| $(\square)^n$ | $n(\square)^{n-1}$ | $(x^3+1)^4 \to 4(x^3+1)^3\cdot 3x^2$ |
| $\sin(\square)$ | $\cos(\square)$ | $\sin(5x) \to \cos(5x)\cdot 5$ |
| $\cos(\square)$ | $-\sin(\square)$ | $\cos(x^2) \to -\sin(x^2)\cdot 2x$ |
| $e^{\square}$ | $e^{\square}$ | $e^{3x} \to e^{3x}\cdot 3$ |
| $\ln(\square)$ | $1/\square$ | $\ln(x^2+1) \to \frac{1}{x^2+1}\cdot 2x$ |
| $\tan(\square)$ | $\sec^2(\square)$ | $\tan(x^3) \to \sec^2(x^3)\cdot 3x^2$ |

---

## Part C: Implicit and Logarithmic Differentiation

---

## Example 8: Implicit Differentiation — When $y$ Is Hidden

**Trigger**: $x$ and $y$ are mixed together in an equation (not $y=$ something).

**Procedure**:

| Step | Action |
|:---:|:---|
| 1 | Differentiate **both sides** with respect to $x$ |
| 2 | Whenever you differentiate a $y$-term, **multiply by $\frac{dy}{dx}$** (treat $y$ as a function of $x$) |
| 3 | **Collect** all terms with $\frac{dy}{dx}$ on one side, everything else on the other |
| 4 | **Factor out** $\frac{dy}{dx}$, then **solve** for it |

$x^2 + y^2 = 25$. Find $\frac{dy}{dx}$.

| Step | Action |
|:---:|:---|
| 1 | $\frac{d}{dx}(x^2) + \frac{d}{dx}(y^2) = \frac{d}{dx}(25)$ |
| 2 | $2x + 2y\frac{dy}{dx} = 0$ (the $y^2$ needs $\frac{dy}{dx}$!) |
| 3 | $2y\frac{dy}{dx} = -2x$ |
| 4 | $\frac{dy}{dx} = -\frac{x}{y}$ |

**Check**: At $(3,4)$ on the circle, slope = $-3/4$. The tangent is perpendicular to the radius (slope $4/3$). Product of slopes = $-1$ ✓.

---

## Example 9: Implicit with Product — $x$ and $y$ Multiplied

$x^3 + y^3 = 6xy$ at $(3,3)$. Find $\frac{dy}{dx}$.

1. $\frac{d}{dx}(x^3) + \frac{d}{dx}(y^3) = \frac{d}{dx}(6xy)$.
2. $3x^2 + 3y^2\frac{dy}{dx} = 6(y + x\frac{dy}{dx})$. (Right side needs product rule on $xy$!)
3. $3x^2 + 3y^2\frac{dy}{dx} = 6y + 6x\frac{dy}{dx}$.
4. $3y^2\frac{dy}{dx} - 6x\frac{dy}{dx} = 6y - 3x^2$.
5. $\frac{dy}{dx}(3y^2-6x) = 6y-3x^2$ → $\frac{dy}{dx} = \frac{6y-3x^2}{3y^2-6x}$.
6. At $(3,3)$: $\frac{18-27}{27-18} = -1$.

---

## Example 10: Logarithmic Differentiation — $x^x$ and Friends

**Trigger**: Both base AND exponent contain $x$ (e.g., $x^x$, $(\sin x)^{\cos x}$, $(x^2+1)^x$).

**Procedure**:

| Step | Action |
|:---:|:---|
| 1 | Set $y = f(x)$. Take $\ln$ of **both sides**: $\ln y = \ln(f(x))$ |
| 2 | Use log laws to **simplify** the right side: $\ln(a^b) = b\ln a$ |
| 3 | Differentiate **both sides** with respect to $x$. Left side: $\frac{1}{y}\frac{dy}{dx}$. Right side: use product/chain as needed |
| 4 | **Multiply** both sides by $y$ to isolate $\frac{dy}{dx}$ |
| 5 | **Replace** $y$ with the original $f(x)$ |

$y = x^x$:

| Step | Action |
|:---:|:---|
| 1,2 | $\ln y = x\ln x$ |
| 3 | $\frac{1}{y}\frac{dy}{dx} = \ln x + x\cdot\frac{1}{x} = \ln x + 1$ |
| 4,5 | $\frac{dy}{dx} = x^x(\ln x + 1)$ |

$y = (x^2+1)^{\sin x}$:

1,2. $\ln y = \sin x \cdot \ln(x^2+1)$.
3. $\frac{y'}{y} = \cos x\ln(x^2+1) + \sin x \cdot \frac{2x}{x^2+1}$.
4,5. $y' = (x^2+1)^{\sin x}\left[\cos x\ln(x^2+1) + \frac{2x\sin x}{x^2+1}\right]$.

---

## Part D: Parametric and Inverse Function Derivatives

---

## Example 11: Parametric — $\frac{dy}{dx} = \frac{dy/dt}{dx/dt}$

**Trigger**: $x$ and $y$ are given as functions of a third variable $t$.

**Procedure**:
1. Differentiate $y(t)$ with respect to $t$ → $dy/dt$.
2. Differentiate $x(t)$ with respect to $t$ → $dx/dt$.
3. Divide: $\frac{dy}{dx} = \frac{dy/dt}{dx/dt}$.

$x=t^2$, $y=t^3$: $\frac{dy}{dx} = \frac{3t^2}{2t} = \frac{3t}{2}$.

$x=\cos t$, $y=\sin t$ at $t=\pi/4$: $\frac{dy}{dx} = \frac{\cos t}{-\sin t} = -\cot t$. At $t=\pi/4$: $-1$.

---

## Example 12: Inverse Function Derivative

If $y=f(x)$ and $f$ is invertible: $(f^{-1})'(y) = \frac{1}{f'(x)}$ where $y=f(x)$.

**Procedure**: To find $(f^{-1})'(b)$:
1. Solve $f(a)=b$ to find $a$.
2. Compute $f'(a)$.
3. Answer = $1/f'(a)$.

$f(x)=x^3+x$. Find $(f^{-1})'(2)$.

1. $f(1)=1^3+1=2$, so $a=1$.
2. $f'(x)=3x^2+1$, $f'(1)=4$.
3. $(f^{-1})'(2) = 1/4$.

---

## Example 13: Inverse Trig Derivatives — Quick Reference

| $f(x)$ | $f'(x)$ | Domain |
|:---|:---|:---|
| $\arcsin x$ | $\frac{1}{\sqrt{1-x^2}}$ | $\vert x\vert < 1$ |
| $\arccos x$ | $-\frac{1}{\sqrt{1-x^2}}$ | $\vert x\vert < 1$ |
| $\arctan x$ | $\frac{1}{1+x^2}$ | all real $x$ |

Combined with chain rule: $\frac{d}{dx}\arcsin(2x) = \frac{2}{\sqrt{1-4x^2}}$. $\frac{d}{dx}\arctan(x^2) = \frac{2x}{1+x^4}$.

---

## Example 14: Absolute Value and Piecewise — Check the Break Points

$|x|$: $f'(x)=1$ for $x>0$, $f'(x)=-1$ for $x<0$, **undefined** at $x=0$ (corner).

$|x^2-1|$: Breaks where $x^2-1=0 \to x=\pm1$.
- $x<-1$ or $x>1$: $f(x)=x^2-1$, $f'(x)=2x$.
- $-1<x<1$: $f(x)=1-x^2$, $f'(x)=-2x$.
- Non-differentiable at $x=\pm1$ (kinks).

> **Up to here**: Product = f'g+fg'. Quotient = (f'g−fg')/g². Chain = outside' × inside'. Implicit: differentiate both sides, attach dy/dx to y-terms, solve. Log-diff: take ln, simplify, differentiate, multiply by y. Parametric: dy/dx = (dy/dt)/(dx/dt).

---

## Common Mistakes

### Mistake 1: Forgetting the chain rule's inner derivative

**Wrong**: $\frac{d}{dx}\sin(x^2) = \cos(x^2)$. **Right**: $\cos(x^2)\cdot 2x$. The chain rule is NOT optional — every composition needs the inner derivative.

### Mistake 2: Swapping the order in the quotient rule numerator

**Wrong**: $\frac{fg' - f'g}{g^2}$. **Right**: $\frac{f'g - fg'}{g^2}$. "Derivative of the TOP first." Check: $\frac{d}{dx}\frac{1}{x} = \frac{0\cdot x - 1\cdot 1}{x^2} = -\frac{1}{x^2} = -x^{-2}$. Power rule gives the same ✓.

### Mistake 3: Dropping $\frac{dy}{dx}$ in implicit differentiation

**Wrong**: Differentiating $y^2$ as $2y$ with no $\frac{dy}{dx}$. **Right**: $\frac{d}{dx}(y^2) = 2y\frac{dy}{dx}$. $y$ is a function of $x$, not a variable.

### Mistake 4: Using log-diff when a simpler rule works

**Wrong**: Log-diff on $y=x^2\sin x$. **Right**: Product rule — faster and less error-prone. Log-diff is specifically for $f(x)^{g(x)}$ forms.

### Mistake 5: Product rule on a constant times a function

**Wrong**: $\frac{d}{dx}(5\sin x) = 0\cdot\sin x + 5\cdot\cos x$. **Right**: Pull the constant out: $5\cdot\frac{d}{dx}\sin x = 5\cos x$. The product rule works but is overkill.

---

## What We Just Did

```
(1) Product rule: (fg)' = f'g + fg'. Quotient: (f/g)' = (f'g−fg')/g².
    Decision: two factors→product. Fraction→quotient. Simple denominator→rewrite as x⁻ⁿ.

(2) Chain rule: (f(g(x)))' = f'(g(x))·g'(x). Peel from outside in.
    Multiple layers: write the derivative chain, multiply all layers.

(3) Implicit: differentiate both sides w.r.t. x. Attach dy/dx to every y-term.
    Collect dy/dx terms, factor, solve. Product rule applies to xy terms.

(4) Log-diff: y=f(x)^g(x) → ln y = g(x)·ln(f(x)). Differentiate, multiply by y.

(5) Parametric: dy/dx = (dy/dt)/(dx/dt). Inverse: (f⁻¹)'(y) = 1/f'(x).
```

---

## Practice 1

$f(x)=x^3\cos x$. Run the product rule: $f=x^3$, $g=\cos x$. $f'=$?, $g'=$?, assemble.

→ Solutions: [Solutions](solutions/14B-solutions.md#practice-1)

---

## Practice 2

$g(x)=\frac{e^x}{x^2+1}$. Run the quotient rule: top=$e^x$, bottom=$x^2+1$. Assemble numerator carefully.

→ Solutions: [Solutions](solutions/14B-solutions.md#practice-2)

---

## Practice 3

$h(x)=\ln(\sin(x^2))$. Chain rule: how many layers? Peel from outside in. Multiply the chain.

→ Solutions: [Solutions](solutions/14B-solutions.md#practice-3)

---

## Practice 4

$x^2+xy+y^2=7$. Find $\frac{dy}{dx}$ at $(1,2)$. Implicit: remember product rule on $xy$.

→ Solutions: [Solutions](solutions/14B-solutions.md#practice-4)

---

## Practice 5

$y=(\cos x)^{\sin x}$. Log-diff: take $\ln$, simplify, differentiate, solve for $y'$.

→ Solutions: [Solutions](solutions/14B-solutions.md#practice-5)

---

## Practice 6: Real Battle

$x=2t-t^2$, $y=3t^2-t^3$. Find $\frac{dy}{dx}$ at $t=1$ and the equation of the tangent line.

→ Solutions: [Solutions](solutions/14B-solutions.md#practice-6)

---

## Basic Algebra Drill — Advanced Differentiation (10 Problems)

> Identify the structure. Apply the matching procedure.

**D1.** $\frac{d}{dx}(x^2e^x)$. Product rule: $f=x^2$, $g=e^x$.

**D2.** $\frac{d}{dx}\left(\frac{\sin x}{x}\right)$. Quotient rule: top=$\sin x$, bottom=$x$.

**D3.** $\frac{d}{dx}((3x+2)^6)$. Chain rule: outer=$(\square)^6$, inner=$3x+2$.

**D4.** $\frac{d}{dx}\cos(5x)$. Chain rule: outer=$\cos(\square)$, inner=$5x$.

**D5.** $\frac{d}{dx}\ln(x^2+1)$. Chain rule: outer=$\ln(\square)$, inner=$x^2+1$.

**D6.** $\frac{d}{dx}\arcsin(3x)$. Inverse trig + chain: $\frac{1}{\sqrt{1-(3x)^2}}\cdot 3$.

**D7.** $\frac{d}{dx}\arctan(\sqrt{x})$. Inverse trig + chain: inner=$\sqrt{x}$.

**D8.** $\frac{d}{dx}(x^2\sin x\cos x)$. Triple product OR group two factors.

**D9.** Find $\frac{dy}{dx}$ for $y^2+x^2y=4x$. Implicit with product rule on $x^2y$.

**D10.** $x=e^{2t}$, $y=\ln t$. Find $\frac{dy}{dx}$. Parametric: $dy/dt \div dx/dt$.

> Solutions: [Solutions](solutions/14B-solutions.md#basic-drill)

---

## Advanced Algebra Drill — Advanced Differentiation (10 Problems)

> Combine techniques. Prove identities. Handle edge cases.

**A1.** Differentiate $x^x$ two ways: (a) log-diff, (b) $x^x=e^{x\ln x}$ + chain rule. Verify match.

**A2.** Find the 100th derivative of $\sin x$. Cycle length = 4. $100 \div 4 = 25$ remainder 0 → back to $\sin x$.

**A3.** $f(x)=\frac{x^2-1}{x^2+1}$. Find $f'(x)$ and simplify to a single fraction.

**A4.** $\sin(xy)=x+y$. Find $\frac{dy}{dx}$. Implicit: chain rule on $\sin(xy)$, product rule on $xy$.

**A5.** $f(x)=\arctan(\ln x) + \arcsin(e^{-x})$. Chain rule on both terms.

**A6.** Find tangent line to $x^3+y^3=9xy$ at $(2,4)$. Implicit diff, plug point.

**A7.** $f(x)=|x^3-3x|$. Find all $x$ where $f$ is NOT differentiable. (Solve $x^3-3x=0$.)

**A8.** Prove $\frac{d}{dx}\arcsin x = \frac{1}{\sqrt{1-x^2}}$. Implicit: $y=\arcsin x \to \sin y = x$. Differentiate.

**A9.** $f(x)=x^{x^x}$. Take $\ln$ twice: $\ln(\ln y) = x\ln x + \ln(\ln x)$? Actually: $\ln y = x^x\ln x$, then differentiate with product rule + chain.

**A10.** Cycloid: $x=t-\sin t$, $y=1-\cos t$. Find $\frac{dy}{dx}$ in terms of $t$. Simplify using half-angle identities. Find where the tangent is horizontal.

> Solutions: [Solutions](solutions/14B-solutions.md#advanced-drill)

---

## Today's Procedure

| When you see... | Do this... |
|:---|:---|
| $f(x)\cdot g(x)$ | **Product rule**: $f'g + fg'$ |
| $\frac{f(x)}{g(x)}$ | **Quotient rule**: $(f'g-fg')/g^2$ |
| $\frac{c}{g(x)}$ (constant top) | Rewrite as $c\cdot g(x)^{-1}$, use chain rule — faster |
| $f(g(x))$ (nested) | **Chain rule**: $f'(g(x))\cdot g'(x)$. Peel outside→in |
| Multiple layers | Write the derivative chain. Multiply all layers |
| $x$ and $y$ mixed | **Implicit**: diff both sides, $y\to y'$, collect, solve |
| $f(x)^{g(x)}$ | **Log-diff**: $\ln y = g\ln f$, differentiate, $\times y$ |
| $x(t), y(t)$ | **Parametric**: $dy/dx = (dy/dt)/(dx/dt)$ |
| $\arcsin, \arccos, \arctan$ | Dictionary + chain rule |
| Absolute value, piecewise | Break at zeros. Check each piece. Test differentiability at breaks |

---

## How to Read These Symbols

| Symbol | Reads as | Meaning |
|:---:|:---:|------|
| $\frac{d}{dx}f(g(x)) = f'(g(x)) \cdot g'(x)$ | "derivative of f of g of x equals f prime of g of x times g prime of x" | chain rule — differentiate outside, then multiply by inside derivative |
| implicit differentiation | "implicit differentiation" | differentiate both sides w.r.t. x, treat y as y(x), solve for dy/dx |
| $\frac{d}{dx}[\ln f(x)] = \frac{f'(x)}{f(x)}$ | "derivative of ln f of x equals f prime of x over f of x" | logarithmic derivative |
| logarithmic differentiation | "logarithmic differentiation" | take ln of both sides first — useful for products/quotients/powers |
| $\frac{d}{dx}[f^{-1}(x)] = \frac{1}{f'(f^{-1}(x))}$ | "derivative of inverse function" | slope of inverse = reciprocal of slope at corresponding point |
| $\frac{dy}{dx} = \frac{dy/dt}{dx/dt}$ | "d y d x equals d y d t over d x d t" | parametric derivative — chain rule with parameter t |
| $\frac{d}{dx}[a^x] = a^x \ln a$ | "derivative of a to the x equals a to the x ln a" | exponential derivative for arbitrary base |
| $\frac{d}{dx}[\log_a x] = \frac{1}{x\ln a}$ | "derivative of log base a of x" | logarithmic derivative for arbitrary base |
| related rates | "related rates" | two quantities change with time — relate their rates via implicit differentiation w.r.t. t |
| $\frac{dx}{dt}$ | "d x d t" / "rate of change of x with respect to time" | time derivative in related rates problems |

---

## Terminology

| What we call it | Math term | Notation |
|:---:|:---:|:---:|
| differentiate a product | product rule | $(fg)' = f'g + fg'$ |
| differentiate a quotient | quotient rule | $(f/g)' = (f'g-fg')/g^2$ |
| differentiate nested functions | chain rule | $(f\circ g)' = (f'\circ g)\cdot g'$ |
| peel from outside in | chain rule layers | multiply derivative chain |
| treat $y$ as function of $x$ | implicit differentiation | attach $dy/dx$ to $y$-terms |
| take $\ln$ first | logarithmic differentiation | for $f(x)^{g(x)}$ forms |
| $dy/dt$ over $dx/dt$ | parametric derivative | $\frac{dy}{dx} = \frac{dy/dt}{dx/dt}$ |
| derivative of inverse | inverse function theorem | $(f^{-1})'(y) = 1/f'(x)$ |
