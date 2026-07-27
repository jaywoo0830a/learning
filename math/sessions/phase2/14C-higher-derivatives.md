# Session 14C: Higher Derivatives — Patterns, Concavity, and the $n$-th Derivative

**Phase 2 — Classical Techniques | 60 min**

*Differentiate once — you get slope. Differentiate again — you get curvature. Differentiate $n$ times — you find a pattern. This session turns repeated differentiation from tedious computation into pattern recognition.*

**Prerequisites**: 14A (basic derivative dictionary), 14B (product/quotient/chain/implicit)

---

## Part A: Higher Derivatives — Just Keep Differentiating

> **The procedure**: Take the derivative. Then take the derivative of that. Repeat until you reach the requested order. There is no new rule — only persistence.

---

## Example 1: Computing $f''$ and $f'''$ — No New Rules

**Notation**: $f'(x) = \frac{dy}{dx}$ (first). $f''(x) = \frac{d^2y}{dx^2}$ (second). $f'''(x) = \frac{d^3y}{dx^3}$ (third). $f^{(n)}(x) = \frac{d^ny}{dx^n}$ ($n$-th, for $n \geq 4$).

**Procedure**:

| Step | Action |
|:---:|:---|
| 1 | Compute $f'(x)$ using the dictionary + rules from 14A/14B |
| 2 | Compute $f''(x)$ by differentiating $f'(x)$ — apply all rules again |
| 3 | Compute $f'''(x)$ by differentiating $f''(x)$ |
| ... | Repeat until the requested order |

$f(x) = x^4 - 3x^3 + 2x$:

| Order | Derivative | How |
|:---:|:---|:---|
| $f'(x)$ | $4x^3 - 9x^2 + 2$ | Power rule on each term |
| $f''(x)$ | $12x^2 - 18x$ | Differentiate $4x^3 \to 12x^2$, $-9x^2 \to -18x$, $2 \to 0$ |
| $f'''(x)$ | $24x - 18$ | Differentiate $12x^2 \to 24x$, $-18x \to -18$ |
| $f^{(4)}(x)$ | $24$ | Constant |
| $f^{(5)}(x)$ | $0$ | Derivative of constant |

**Polynomials eventually vanish**: A degree-$n$ polynomial becomes zero after $n+1$ derivatives.

---

## Example 2: Physical Meaning — Position, Velocity, Acceleration, Jerk

| Order | Math name | Physics name | What it measures |
|:---:|:---|:---|:---|
| $f(t)$ | position | position | Where you are |
| $f'(t)$ | first derivative | **velocity** | How fast position changes |
| $f''(t)$ | second derivative | **acceleration** | How fast velocity changes |
| $f'''(t)$ | third derivative | **jerk** | How fast acceleration changes |

A car moving with $s(t) = t^3 - 6t^2 + 9t$ (meters, seconds):
- $v(t) = s'(t) = 3t^2 - 12t + 9$ (velocity).
- $a(t) = s''(t) = 6t - 12$ (acceleration).
- At $t=1$: $v=0$ (stopped), $a=-6$ (decelerating — slowing down from positive direction).
- At $t=3$: $v=0$ (stopped again), $a=6$ (accelerating — speeding up in positive direction).

---

## Part B: Pattern Recognition — The $n$-th Derivative

> **The procedure**: Compute the first 3–4 derivatives. Spot the repeating pattern. Write a formula for the $n$-th one.

---

## Example 3: The Four Pattern Families

| Family | $f(x)$ | $f'(x)$ | $f''(x)$ | $f'''(x)$ | $f^{(n)}(x)$ formula |
|:---|:---|:---|:---|:---|:---|
| **Exponential** | $e^{kx}$ | $ke^{kx}$ | $k^2e^{kx}$ | $k^3e^{kx}$ | $k^n e^{kx}$ |
| **Sine** | $\sin x$ | $\cos x$ | $-\sin x$ | $-\cos x$ | $\sin(x + \frac{n\pi}{2})$ |
| **Cosine** | $\cos x$ | $-\sin x$ | $-\cos x$ | $\sin x$ | $\cos(x + \frac{n\pi}{2})$ |
| **Power (negative)** | $1/x = x^{-1}$ | $-x^{-2}$ | $2x^{-3}$ | $-6x^{-4}$ | $(-1)^n n!\,x^{-(n+1)}$ |

---

## Example 4: The Exponential Pattern — Multiply by $k$ Each Time

$f(x)=e^{3x}$.

| $n$ | $f^{(n)}(x)$ | Pattern |
|:---:|:---|:---|
| 1 | $3e^{3x}$ | $3^1$ |
| 2 | $9e^{3x}$ | $3^2$ |
| 3 | $27e^{3x}$ | $3^3$ |
| $n$ | $3^n e^{3x}$ | $3^n$ |

**Check**: $n=5 \to 3^5 e^{3x} = 243e^{3x}$. Differentiate 5 times manually — it matches.

$f(x)=e^{-2x}$: $f^{(n)}(x) = (-2)^n e^{-2x}$. The sign alternates because the base is negative.

---

## Example 5: The Trig Pattern — Cycle of 4

$f(x)=\sin x$:

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|:---:|:---|:---|:---|:---|:---|:---|:---|
| $f^{(n)}(x)$ | $\sin x$ | $\cos x$ | $-\sin x$ | $-\cos x$ | $\sin x$ | $\cos x$ | $-\sin x$ |

**Procedure to find $f^{(n)}(x)$ for trig**:
1. Divide $n$ by 4. Keep the **remainder** $r$ (0, 1, 2, or 3).
2. Read the answer from the cycle: $r=0\to\sin x$, $r=1\to\cos x$, $r=2\to-\sin x$, $r=3\to-\cos x$.

$f^{(100)}(\sin x)$: $100 \div 4 = 25$ remainder $0$. → $\sin x$. (Hundredth derivative returns to the start!)
$f^{(57)}(\sin x)$: $57 \div 4 = 14$ remainder $1$. → $\cos x$.

**For $\cos x$**: Same cycle offset: $r=0\to\cos x$, $r=1\to-\sin x$, $r=2\to-\cos x$, $r=3\to\sin x$.

---

## Example 6: The Rational Pattern — Factorials Appear

$f(x)=\frac{1}{x} = x^{-1}$:

| $n$ | $f^{(n)}(x)$ | Sign | Coefficient | Exponent |
|:---:|:---|:---:|:---:|:---:|
| 1 | $-1\cdot x^{-2}$ | $-$ | 1 | $-2$ |
| 2 | $2\cdot x^{-3}$ | $+$ | $2=2!$ | $-3$ |
| 3 | $-6\cdot x^{-4}$ | $-$ | $6=3!$ | $-4$ |
| 4 | $24\cdot x^{-5}$ | $+$ | $24=4!$ | $-5$ |
| $n$ | $(-1)^n n!\,x^{-(n+1)}$ | alternating | $n!$ | $-(n+1)$ |

**General rational pattern for $\frac{1}{ax+b}$**:
$f^{(n)}(x) = (-1)^n \frac{a^n \cdot n!}{(ax+b)^{n+1}}$.

$f(x)=\frac{1}{2x+1}$: $f^{(3)}(x) = (-1)^3 \frac{2^3 \cdot 3!}{(2x+1)^4} = -\frac{48}{(2x+1)^4}$.

---

## Example 7: Polynomials — They Eventually Vanish

$f(x)=x^5 - 2x^3 + x$.

| $n$ | $f^{(n)}(x)$ | Degree |
|:---:|:---|:---:|
| 1 | $5x^4 - 6x^2 + 1$ | 4 |
| 2 | $20x^3 - 12x$ | 3 |
| 3 | $60x^2 - 12$ | 2 |
| 4 | $120x$ | 1 |
| 5 | $120$ | 0 (constant) |
| 6 | $0$ | — (vanished) |

**Rule**: A degree-$d$ polynomial becomes zero after $d+1$ derivatives. The $d$-th derivative is constant: $f^{(d)}(x) = a_d \cdot d!$ (leading coefficient × factorial of degree).

---

## Part C: The Leibniz Rule — $n$-th Derivative of a Product

---

## Example 8: Leibniz Rule — The Product Rule Repeated

**The pattern** (looks like the binomial theorem):

$(fg)'' = f''g + 2f'g' + fg''$.
$(fg)''' = f'''g + 3f''g' + 3f'g'' + fg'''$.

**General Leibniz rule**:
$(fg)^{(n)} = \sum_{k=0}^{n} \binom{n}{k} f^{(n-k)} g^{(k)}$.

Coefficients are binomial coefficients: $\binom{n}{k} = \frac{n!}{k!(n-k)!}$.

**When to use**: One of the functions becomes zero after a few derivatives (e.g., polynomials — only a few non-zero terms).

$f(x)=x^2 e^x$. $n=3$:
- $f=x^2$: $f'=2x$, $f''=2$, $f'''=0$ (vanishes after 3 derivatives).
- $g=e^x$: $g'=g''=g'''=e^x$ (never vanishes).

$(x^2 e^x)''' = \binom{3}{0}f'''g + \binom{3}{1}f''g' + \binom{3}{2}f'g'' + \binom{3}{3}fg'''$
$= 1\cdot 0\cdot e^x + 3\cdot 2\cdot e^x + 3\cdot 2x\cdot e^x + 1\cdot x^2\cdot e^x$
$= e^x(6 + 6x + x^2)$.

---

## Part D: Implicit Second Derivatives

---

## Example 9: Finding $\frac{d^2y}{dx^2}$ from an Implicit Equation

**Procedure**:

| Step | Action |
|:---:|:---|
| 1 | Differentiate the equation implicitly to find $\frac{dy}{dx}$ (as in 14B) |
| 2 | Differentiate $\frac{dy}{dx}$ with respect to $x$ — this gives $\frac{d^2y}{dx^2}$ |
| 3 | Substitute the expression for $\frac{dy}{dx}$ from step 1 into the result |
| 4 | The answer will involve $x$ and $y$ — that's expected for implicit curves |

$x^2 + y^2 = 25$. Find $\frac{d^2y}{dx^2}$.

**Step 1**: $2x + 2y\frac{dy}{dx} = 0$ → $\frac{dy}{dx} = -\frac{x}{y}$.

**Step 2**: Differentiate $\frac{dy}{dx} = -\frac{x}{y}$ with respect to $x$. Use quotient rule:
$\frac{d^2y}{dx^2} = \frac{d}{dx}\left(-\frac{x}{y}\right) = -\frac{1\cdot y - x\cdot\frac{dy}{dx}}{y^2} = -\frac{y - x\frac{dy}{dx}}{y^2}$.

**Step 3**: Substitute $\frac{dy}{dx} = -\frac{x}{y}$:
$\frac{d^2y}{dx^2} = -\frac{y - x(-\frac{x}{y})}{y^2} = -\frac{y + \frac{x^2}{y}}{y^2} = -\frac{\frac{y^2+x^2}{y}}{y^2} = -\frac{y^2+x^2}{y^3}$.

**Step 4**: Since $x^2+y^2=25$, the numerator simplifies: $-\frac{25}{y^3}$.

**Geometric meaning**: On the circle $x^2+y^2=25$, the second derivative is always negative when $y>0$ (concave down — the top half of the circle curves downward) and positive when $y<0$ (concave up).

---

## Part E: Concavity and Inflection Points

---

## Example 10: Reading Concavity from $f''$

| Sign of $f''(x)$ | Shape | Meaning |
|:---:|:---:|:---|
| $f''(x) > 0$ | **Concave up** $\smile$ | Slope is increasing — graph bends upward |
| $f''(x) < 0$ | **Concave down** $\frown$ | Slope is decreasing — graph bends downward |
| $f''(x) = 0$ | **Possible inflection** | Curvature may switch — test sign change |

**Procedure to find inflection points**:
1. Compute $f''(x)$.
2. Set $f''(x)=0$ and solve for $x$.
3. Check if $f''$ **changes sign** at those $x$-values. If yes → inflection point. If no → not an inflection.

$f(x)=x^3-3x$: $f'(x)=3x^2-3$, $f''(x)=6x$.
$f''(x)=0$ at $x=0$.
- $x<0$: $f''(x)<0$ (concave down).
- $x>0$: $f''(x)>0$ (concave up).
Sign changes → $(0,0)$ is an **inflection point**.

$f(x)=x^4$: $f''(x)=12x^2$. $f''(0)=0$, but $f''(x) \geq 0$ everywhere (never changes sign). No inflection — it's always concave up.

---

## Example 11: Mixed Technique Problems

**Procedure for mixed problems**: Identify the outer structure first (product? quotient? chain?), apply the matching rule from 14B. Then differentiate again if needed.

**$f(x)=e^x\sin x + \ln(\cos x)$**:
1. Split at the $+$: two terms.
2. Term 1 — product rule: $(e^x)'\sin x + e^x(\sin x)' = e^x\sin x + e^x\cos x = e^x(\sin x+\cos x)$.
3. Term 2 — chain rule: outer $\ln(\square) \to 1/\square$, inner $\cos x \to -\sin x$. $= \frac{-\sin x}{\cos x} = -\tan x$.
4. $f'(x) = e^x(\sin x+\cos x) - \tan x$.

**$f(x)=\arctan(\ln x)$**:
1. Chain rule: outer $\arctan(\square) \to \frac{1}{1+\square^2}$, inner $\ln x \to 1/x$.
2. $f'(x) = \frac{1}{1+(\ln x)^2} \cdot \frac{1}{x}$.

**$f(x)=x^3e^{2x}\tan x$ (triple product)**:
$(fgh)' = f'gh + fg'h + fgh'$.
1. $f'gh = 3x^2 e^{2x}\tan x$.
2. $fg'h = x^3 \cdot 2e^{2x} \cdot \tan x$.
3. $fgh' = x^3 e^{2x} \cdot \sec^2 x$.
4. Factor $x^2 e^{2x}$: $x^2 e^{2x}[3\tan x + 2x\tan x + x\sec^2 x]$.

> **Up to here**: Higher derivatives = differentiate repeatedly. Exponential: multiply by $k$ each time. Trig: cycle of 4. Rational: $(-1)^n n!\,x^{-(n+1)}$. Polynomial: vanishes after $d+1$ derivatives. Leibniz rule: $(fg)^{(n)} = \sum \binom{n}{k} f^{(n-k)}g^{(k)}$. Implicit 2nd derivative: differentiate $dy/dx$ again, substitute. Concavity: $f''>0 \to$ up, $f''<0 \to$ down. Inflection: $f''=0$ + sign change.

---

## Common Mistakes

### Mistake 1: Stopping the trig cycle at the wrong remainder

**Wrong**: "$f^{(7)}(\sin x)$: $7 \div 4$ remainder 3 → $\sin x$." **Right**: Remainder 0 = $\sin x$, 1 = $\cos x$, 2 = $-\sin x$, 3 = $-\cos x$. Count carefully from 0.

### Mistake 2: Forgetting the factorial in rational $n$-th derivatives

**Wrong**: $f^{(n)}(1/x) = (-1)^n x^{-(n+1)}$. **Right**: $(-1)^n n!\,x^{-(n+1)}$. The coefficient grows factorially — test with $n=2$: $f''(1/x)=2x^{-3}$, not $x^{-3}$.

### Mistake 3: Claiming $f''(x)=0$ always means inflection

**Wrong**: "$f(x)=x^4$, $f''(0)=0$, so $(0,0)$ is an inflection point." **Right**: $f''$ must CHANGE SIGN. $f''(x)=12x^2 \geq 0$ always — no sign change, no inflection.

### Mistake 4: Forgetting to substitute $dy/dx$ in implicit second derivatives

**Wrong**: Leaving $\frac{dy}{dx}$ in the final answer for $\frac{d^2y}{dx^2}$. **Right**: Substitute the first derivative expression back in. The final answer should only contain $x$ and $y$.

---

## What We Just Did

```
(1) Higher derivatives: differentiate repeatedly. f'' = (f')', f''' = (f'')', etc.
    Physical: f'=velocity, f''=acceleration, f'''=jerk.

(2) nth-derivative patterns:
    Exponential: f^{(n)}(e^{kx}) = k^n e^{kx}.
    Trig: cycle of 4 — use remainder of n÷4.
    Rational: f^{(n)}(1/x) = (−1)^n n! x^{−(n+1)}.
    Polynomial of degree d: vanishes after d+1 derivatives.

(3) Leibniz rule: (fg)^{(n)} = Σ binom(n,k) f^{(n−k)} g^{(k)}. Best when one function vanishes.

(4) Implicit 2nd derivative: find dy/dx, differentiate again, substitute dy/dx.

(5) Concavity: f''>0→up, f''<0→down. Inflection: f''=0 AND sign change.
```

---

## Practice 1

Find $f''(x)$ for $f(x)=x^5-2x^3+x$. Show each step clearly.

→ Reference: **Example 1**

> Solutions: [Solutions](solutions/14C-solutions.md#practice-1)

---

## Practice 2

Find $f^{(4)}(x)$ for $f(x)=e^{2x}$. Use the exponential pattern: $k^n e^{kx}$.

→ Reference: **Example 4**

> Solutions: [Solutions](solutions/14C-solutions.md#practice-2)

---

## Practice 3

Find $f^{(57)}(\cos x)$. Use the trig cycle: divide by 4, take the remainder.

→ Reference: **Example 5**

> Solutions: [Solutions](solutions/14C-solutions.md#practice-3)

---

## Practice 4

Find $f^{(n)}(x)$ for $f(x)=\frac{1}{2x+1}$. Use the rational pattern formula.

→ Reference: **Example 6**

> Solutions: [Solutions](solutions/14C-solutions.md#practice-4)

---

## Practice 5

Find $\frac{d^2y}{dx^2}$ for $x^3+y^3=6xy$. (Implicit second derivative — find $dy/dx$ first, then differentiate again.)

→ Reference: **Example 9**

> Solutions: [Solutions](solutions/14C-solutions.md#practice-5)

---

## Practice 6: Real Battle (Constructive)

$f(x)=x^3-3x^2-9x+5$. (a) Find all $x$ where $f'(x)=0$ (critical points). (b) Find all $x$ where $f''(x)=0$ (possible inflection). (c) Determine intervals where $f$ is concave up and concave down. (d) Sketch the concavity behavior — where does the graph bend upward vs. downward?

→ Reference: **Example 10**

> Solutions: [Solutions](solutions/14C-solutions.md#practice-6)

---

## Basic Drills

> Differentiate repeatedly. Spot the pattern for $n$-th derivatives.

**D1.** Find $f''(x)$ for $f(x)=3x^4-5x^2+2x-7$. Differentiate twice.

**D2.** Find $f'''(x)$ for $f(x)=x^5$. Three derivatives of a monomial.

**D3.** Find $f''(x)$ for $f(x)=e^{-x}$. Chain rule in first derivative, then again.

**D4.** Find $f''(x)$ for $f(x)=\ln x$. First = $1/x$, second = differentiate $1/x$.

**D5.** Find $f''(x)$ for $f(x)=\sin 2x$. Chain rule: $\cos 2x \cdot 2$, then differentiate again.

**D6.** Find $f^{(n)}(x)$ for $f(x)=e^{5x}$. Pattern: $k^n e^{kx}$.

**D7.** Find $f''(x)$ for $f(x)=x\ln x$. Product rule, then differentiate again.

**D8.** Find $f''(0)$ for $f(x)=\tan x$. $f'(x)=\sec^2 x$, $f''(x)=2\sec^2 x\tan x$.

**D9.** $f(x)=|x^3|$. Where is $f'(x)$ undefined? Where is $f''(x)$ undefined?

**D10.** Find the inflection point(s) of $f(x)=x^3-6x^2+9x$. Compute $f''$, set to zero, check sign change.

> Solutions: [Solutions](solutions/14C-solutions.md#basic-drill)

---

## Advanced Drills

> Patterns, proofs, implicit, and Leibniz.

**A1.** Prove Leibniz rule for $n=2$: $(fg)'' = f''g + 2f'g' + fg''$. Start from $(fg)' = f'g+fg'$, differentiate again.

**A2.** Find $f^{(100)}(x)$ for $f(x)=x e^x$. Use Leibniz rule — $x$ vanishes after 2 derivatives, so only 2 terms survive.

**A3.** $f(x)=\frac{1}{1-x}$. Find a formula for $f^{(n)}(x)$. Compute $f', f'', f'''$, spot the pattern.

**A4.** Find $f''(\pi/4)$ for $f(x)=\sin^2 x$. Use $\sin^2 x = \frac{1-\cos 2x}{2}$ first, OR use chain rule twice.

**A5.** $f(x)=\ln(\sin x + \cos x)$. Find $f'(x)$, then $f''(0)$. Quotient rule in the second derivative.

**A6.** Prove $y=e^x\sin x$ satisfies $y''-2y'+2y=0$. Compute $y'$, $y''$, plug in, simplify.

**A7.** Find all $x$ where $f''(x)=0$ for $f(x)=x^4-6x^2+8x$. Compute $f''$, solve quadratic, verify sign change.

**A8.** Find $\frac{d^2y}{dx^2}$ for $x^2+xy+y^2=7$ using implicit differentiation twice. (Product rule on $xy$!)

**A9.** $f(x)=x^{x^x}$. Find $f'(x)$ using log-diff twice. Then find $f''(1)$. (Challenging — take $\ln$ twice.)

**A10.** $f(x)=\frac{ax+b}{cx+d}$. Prove $f'''(x)=0$ for all $x \neq -d/c$. (Rewrite as $A + \frac{B}{cx+d}$ using division — then only one term to differentiate.)

> Solutions: [Solutions](solutions/14C-solutions.md#advanced-drill)

---

## Today's Procedure

| When you see... | Do this... |
|:---|:---|
| Find $f''$, $f'''$, etc. | Differentiate repeatedly. No new rules — just persistence |
| Find $f^{(n)}(e^{kx})$ | Formula: $k^n e^{kx}$. Multiply by $k$ each time |
| Find $f^{(n)}(\sin x)$ or $f^{(n)}(\cos x)$ | Divide $n$ by 4. Remainder tells you where in the cycle |
| Find $f^{(n)}(1/(ax+b))$ | Formula: $(-1)^n a^n n!/(ax+b)^{n+1}$ |
| Find $n$-th derivative of a product | Leibniz rule: $\sum \binom{n}{k} f^{(n-k)}g^{(k)}$. Best when one factor vanishes |
| Find $\frac{d^2y}{dx^2}$ from implicit equation | Find $dy/dx$ first, differentiate it again, substitute $dy/dx$ back |
| Determine concavity | Compute $f''$. Positive → up. Negative → down |
| Find inflection points | Set $f''=0$, solve. Check that $f''$ CHANGES SIGN |
| Mixed techniques (product+chain+trig) | Identify outer structure → apply matching 14B rule → differentiate again if needed |

---

## How to Read These Symbols

| Symbol | Reads as | Meaning |
|:---:|:---:|------|
| $f''(x)$ | "f double prime of x" / "second derivative" | derivative of derivative — rate of change of slope |
| $f'''(x)$ | "f triple prime" / "third derivative" | derivative of second derivative — jerk in physics |
| $f^{(n)}(x)$ | "f superscript n of x" / "n-th derivative" | higher-order derivative notation (for n > 3) |
| $\frac{d^2y}{dx^2}$ | "d two y d x squared" / "second derivative" | Leibniz notation for f''(x) |
| $\frac{d^ny}{dx^n}$ | "d n y d x to the n" / "n-th derivative" | Leibniz notation for n-th derivative |
| concavity | "concavity" | f''>0 = concave up (∪), f''<0 = concave down (∩) |
| inflection point | "inflection point" | f'' changes sign — concavity flips |
| Taylor polynomial | "Taylor polynomial" | $P_n(x) = \sum_{k=0}^n \frac{f^{(k)}(a)}{k!}(x-a)^k$ — polynomial that matches f and its first n derivatives at a |
| jerk | "jerk" | third derivative of position — rate of change of acceleration |
| $C^n$ | "C n" / "n-times continuously differentiable" | first n derivatives exist and are continuous |

---

## Terminology

| What we call it | Math term | Notation |
|:---:|:---:|:---:|
| derivative of the derivative | second derivative | $f''(x)$, $\frac{d^2y}{dx^2}$ |
| rate of change of rate of change | third derivative / jerk | $f'''(x)$ |
| $n$-times differentiated | $n$-th derivative | $f^{(n)}(x)$, $\frac{d^ny}{dx^n}$ |
| bends upward | concave up | $f''(x) > 0$ |
| bends downward | concave down | $f''(x) < 0$ |
| curvature switches | inflection point | $f''(x)=0$ + sign change |
| $n$-th derivative of product | Leibniz rule | $(fg)^{(n)} = \sum \binom{n}{k} f^{(n-k)}g^{(k)}$ |
| trig cycle length 4 | periodic derivative pattern | $\sin \to \cos \to -\sin \to -\cos$ |
| polynomial eventually zero | finite differences | degree-$d$ vanishes at $d+1$ |
