# Session 14B: Advanced Differentiation — Product, Quotient, Chain, and Implicit

**Phase 2 — Classical Techniques | 80 min**

*Prerequisites: 14A (basic derivatives), 10A (exponents & logs), 11A (trig)*

---

## Part A: The Three Pillars — Product, Quotient, Chain

---

## Example 1: Product Rule — $(fg)' = f'g + fg'$

Two functions multiplied: differentiate one at a time, leave the other alone, then add.

**Memory**: "First derivative × second + first × second derivative."

$f(x)=x^2\sin x$.

① $f'=2x$, $g'=\cos x$.
② $(fg)' = 2x\cdot\sin x + x^2\cdot\cos x = 2x\sin x + x^2\cos x$.

$(x^3+1)e^x$: $= 3x^2e^x + (x^3+1)e^x = e^x(x^3+3x^2+1)$.

**Product of three**: $(fgh)' = f'gh + fg'h + fgh'$.

---

## Example 2: Quotient Rule — $(f/g)' = \frac{f'g - fg'}{g^2}$

**Memory**: "Low d-high minus high d-low, over low squared."

$f(x)=\frac{x^2}{x+1}$.

① $f'=2x$, $g'=1$.
② $\frac{2x(x+1) - x^2(1)}{(x+1)^2} = \frac{2x^2+2x-x^2}{(x+1)^2} = \frac{x^2+2x}{(x+1)^2}$.

**Proof of $\frac{d}{dx}\tan x$**:
$\tan x = \frac{\sin x}{\cos x}$. Quotient rule:
$\frac{\cos x\cdot\cos x - \sin x\cdot(-\sin x)}{\cos^2 x} = \frac{\cos^2 x + \sin^2 x}{\cos^2 x} = \frac{1}{\cos^2 x} = \sec^2 x$. ✓

---

## Example 3: Chain Rule — $(f(g(x)))' = f'(g(x))\cdot g'(x)$

**The most powerful differentiation tool.** When a function is nested inside another, differentiate the outside (evaluated at the inside), then multiply by the derivative of the inside.

**Memory**: "Derivative of outside × derivative of inside."

$\frac{d}{dx}(x^2+1)^5$:
① Outside: $5(x^2+1)^4$. ② Inside: $2x$.
→ $5(x^2+1)^4\cdot 2x = 10x(x^2+1)^4$.

$\frac{d}{dx}\sin(x^3) = \cos(x^3)\cdot 3x^2$.

$\frac{d}{dx}e^{\sin x} = e^{\sin x}\cdot\cos x$.

$\frac{d}{dx}\ln(\cos x) = \frac{1}{\cos x}\cdot(-\sin x) = -\tan x$.

---

## Example 4: Nested Chain — Three or More Layers

Peel the onion one layer at a time, from outside in.

$\frac{d}{dx}\sin(e^{x^2})$:
① Outside: $\cos(e^{x^2})$.
② Middle: $e^{x^2}$.
③ Inside: $2x$.
→ $\cos(e^{x^2})\cdot e^{x^2}\cdot 2x = 2x e^{x^2}\cos(e^{x^2})$.

$\frac{d}{dx}\sqrt{\ln(\sin x)} = \frac{1}{2\sqrt{\ln(\sin x)}}\cdot\frac{1}{\sin x}\cdot\cos x = \frac{\cot x}{2\sqrt{\ln(\sin x)}}$.

---

## Part B: Implicit, Logarithmic, and Parametric Differentiation

---

## Example 5: Implicit Differentiation — $y$ Is Hiding

When $x$ and $y$ are mixed together (like $x^2+y^2=25$), treat $y$ as a function of $x$. Differentiate both sides with respect to $x$, and **multiply by $\frac{dy}{dx}$ whenever you differentiate $y$**.

$x^2 + y^2 = 25$. Find $\frac{dy}{dx}$.

① $2x + 2y\cdot\frac{dy}{dx} = 0$.
② $2y\frac{dy}{dx} = -2x$ → $\frac{dy}{dx} = -\frac{x}{y}$.

$x^3 + y^3 = 6xy$ at $(3,3)$:
① $3x^2 + 3y^2\frac{dy}{dx} = 6y + 6x\frac{dy}{dx}$.
② Group $\frac{dy}{dx}$ terms: $3y^2\frac{dy}{dx}-6x\frac{dy}{dx} = 6y-3x^2$.
③ $\frac{dy}{dx} = \frac{6y-3x^2}{3y^2-6x}$.
④ At $(3,3)$: $\frac{18-27}{27-18} = -1$.

---

## Example 6: Logarithmic Differentiation — $x^x$ and Friends

When both base and exponent are functions of $x$, take $\ln$ of both sides first.

$y = x^x$.

① $\ln y = x\ln x$.
② Differentiate: $\frac{1}{y}\frac{dy}{dx} = \ln x + x\cdot\frac{1}{x} = \ln x + 1$.
③ $\frac{dy}{dx} = x^x(\ln x + 1)$.

$y = (x^2+1)^{\sin x}$:
① $\ln y = \sin x\cdot\ln(x^2+1)$.
② $\frac{y'}{y} = \cos x\ln(x^2+1) + \sin x\cdot\frac{2x}{x^2+1}$.
③ $y' = (x^2+1)^{\sin x}\left[\cos x\ln(x^2+1) + \frac{2x\sin x}{x^2+1}\right]$.

---

## Example 7: Inverse Function Derivative

If $y=f(x)$, then $(f^{-1})'(y) = \frac{1}{f'(x)}$.

$f(x)=x^3+x$. $f(1)=2$. Find $(f^{-1})'(2)$.
$f'(x)=3x^2+1$, $f'(1)=4$. $(f^{-1})'(2) = \frac{1}{4}$.

---

## Example 8: Parametric Differentiation

$x=x(t)$, $y=y(t)$: $\displaystyle \frac{dy}{dx} = \frac{dy/dt}{dx/dt}$.

$x=t^2$, $y=t^3$: $\frac{dy}{dx} = \frac{3t^2}{2t} = \frac{3t}{2}$.

$x=\cos t$, $y=\sin t$ at $t=\pi/4$: $\frac{dy}{dx} = \frac{\cos t}{-\sin t} = -\cot t \to -1$.

---

## Part C: Special Function Derivatives

---

## Example 9: Inverse Trig Functions

$\frac{d}{dx}\arcsin x = \frac{1}{\sqrt{1-x^2}}$ ($|x|<1$).
$\frac{d}{dx}\arccos x = -\frac{1}{\sqrt{1-x^2}}$ ($|x|<1$).
$\frac{d}{dx}\arctan x = \frac{1}{1+x^2}$.

$\frac{d}{dx}\arcsin(2x) = \frac{2}{\sqrt{1-4x^2}}$.
$\frac{d}{dx}\arctan(x^2) = \frac{2x}{1+x^4}$.

---

## Example 10: Absolute Value and Piecewise Functions

$|x|$: $f'(x)=1$ for $x>0$, $f'(x)=-1$ for $x<0$, undefined at $x=0$.

$|x^2-1|$: $x<-1$ or $x>1$: $f'=2x$. $-1<x<1$: $f'=-2x$. Non-differentiable at $x=\pm1$.

> **Up to here**: Product = $f'g+fg'$. Quotient = $(f'g-fg')/g^2$. Chain = outside'×inside'.
> Implicit: differentiate both sides, multiply $\frac{dy}{dx}$ for every $y$.
> Log-diff: take $\ln$ first. Parametric: $(dy/dt)/(dx/dt)$.

---

## Common Mistakes

### Mistake 1: Forgetting the chain rule's inside derivative

**Wrong**: $\frac{d}{dx}\sin(x^2) = \cos(x^2)$. **Right**: $2x\cos(x^2)$.

### Mistake 2: Swapping order in the quotient rule

**Wrong**: $fg' - f'g$ in numerator. **Right**: $f'g - fg'$. "Derivative of top first."

### Mistake 3: Dropping $\frac{dy}{dx}$ in implicit differentiation

**Wrong**: Differentiating $y^2$ as $2y$ with no $\frac{dy}{dx}$. **Right**: $2y\frac{dy}{dx}$.

---

## What We Just Did

```
(1) Product rule: (fg)' = f'g + fg'. Quotient rule: (f/g)' = (f'g-fg')/g².
(2) Chain rule: (f(g(x)))' = f'(g(x))·g'(x). Peel from outside in.
(3) Implicit diff: differentiate both sides, multiply dy/dx for y terms.
(4) Log-diff: take ln, then differentiate. Solves x^x and f(x)^g(x).
(5) Parametric: dy/dx = (dy/dt)/(dx/dt). Inverse: (f⁻¹)'(y) = 1/f'(x).
```

---

## Practice 1

Differentiate: $f(x)=x^3\cos x$. Product rule.

→ Reference: **Example 1**

> Solutions: [Solutions](solutions/14B-solutions.md#practice-1)

---

## Practice 2

Differentiate: $g(x)=\frac{e^x}{x^2+1}$. Quotient rule.

→ Reference: **Example 2**

> Solutions: [Solutions](solutions/14B-solutions.md#practice-2)

---

## Practice 3

Differentiate: $h(x)=\ln(\sin(x^2))$. Chain rule (3 layers).

→ Reference: **Example 4**

> Solutions: [Solutions](solutions/14B-solutions.md#practice-3)

---

## Practice 4

$x^2+xy+y^2=7$. Find $\frac{dy}{dx}$ at $(1,2)$. Implicit differentiation.

→ Reference: **Example 5**

> Solutions: [Solutions](solutions/14B-solutions.md#practice-4)

---

## Practice 5

Differentiate: $y=(\cos x)^{\sin x}$. Logarithmic differentiation.

→ Reference: **Example 6**

> Solutions: [Solutions](solutions/14B-solutions.md#practice-5)

---

## Practice 6: Real Battle

$x=2t-t^2$, $y=3t^2-t^3$. Find $\frac{dy}{dx}$ at $t=1$ and the tangent line equation.

→ Reference: **Example 8**

> Solutions: [Solutions](solutions/14B-solutions.md#practice-6)

---

## Basic Algebra Drill — Advanced Differentiation (10 Problems)

**D1.** $\frac{d}{dx}(x^2e^x)$. Product rule.

**D2.** $\frac{d}{dx}\left(\frac{\sin x}{x}\right)$. Quotient rule.

**D3.** $\frac{d}{dx}((3x+2)^6)$. Chain rule.

**D4.** $\frac{d}{dx}\cos(5x)$. Chain rule.

**D5.** $\frac{d}{dx}\ln(x^2+1)$. Chain rule.

**D6.** $\frac{d}{dx}\arcsin(3x)$. Inverse trig.

**D7.** $\frac{d}{dx}\arctan(\sqrt{x})$. Inverse trig + chain.

**D8.** $\frac{d}{dx}(x^2\sin x\cos x)$. Triple product.

**D9.** Find $\frac{dy}{dx}$ for $y^2+x^2y=4x$ using implicit differentiation.

**D10.** $x=e^{2t}$, $y=\ln t$. Find $\frac{dy}{dx}$. Parametric.

> Solutions: [Solutions](solutions/14B-solutions.md#basic-drill)

---

## Advanced Algebra Drill — Advanced Differentiation (10 Problems)

**A1.** Differentiate $f(x)=x^x$ two ways: (a) logarithmic differentiation, (b) write $x^x=e^{x\ln x}$ and use chain rule. Verify they match.

**A2.** Find the 100th derivative of $\sin x$. (Hint: the cycle length is 4.)

**A3.** $f(x)=\frac{x^2-1}{x^2+1}$. Find $f'(x)$ and simplify fully.

**A4.** $\sin(xy)=x+y$. Find $\frac{dy}{dx}$ using implicit differentiation.

**A5.** Differentiate $f(x)=\arctan(\ln x) + \arcsin(e^{-x})$.

**A6.** Find the equation of the tangent line to $x^3+y^3=9xy$ at $(2,4)$. (This is the Folium of Descartes.)

**A7.** $f(x)=|x^3-3x|$. Find all $x$ where $f$ is NOT differentiable.

**A8.** Prove that $\frac{d}{dx}\arcsin x = \frac{1}{\sqrt{1-x^2}}$ using implicit differentiation on $\sin y = x$.

**A9.** Differentiate $f(x)=x^{x^x}$. (Hint: take $\ln$ twice.)

**A10.** $x=t-\sin t$, $y=1-\cos t$ (cycloid). Find $\frac{dy}{dx}$ in terms of $t$ and simplify. Find where the tangent is horizontal.

> Solutions: [Solutions](solutions/14B-solutions.md#advanced-drill)

---

## Today's Procedure

```
Step 1: Identify the structure. Multiplication → product rule.
    Division → quotient rule. Nested function → chain rule.
    Mixed x and y → implicit. f(x)^g(x) → log-diff.

Step 2: Chain rule = outside' × inside'. For multiple layers,
    peel from outermost to innermost.

Step 3: Implicit: differentiate everything, attach dy/dx to y-terms,
    then solve for dy/dx.
```

---

## Terminology

| What we call it | Math term | Notation |
|:---------------:|:---------:|:--------:|
| product rule | product rule | $(fg)' = f'g + fg'$ |
| quotient rule | quotient rule | $(f/g)' = (f'g-fg')/g^2$ |
| chain rule | chain rule | $(f\circ g)' = (f'\circ g)\cdot g'$ |
| implicit | implicit differentiation | differentiate both sides, solve for $dy/dx$ |
| log-diff | logarithmic differentiation | take $\ln$, then differentiate |
| parametric | parametric derivative | $dy/dx = (dy/dt)/(dx/dt)$ |
| inverse trig | inverse trigonometric derivative | $\arcsin$, $\arccos$, $\arctan$ rules |
