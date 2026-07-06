# Session 16B: Advanced Integration — Parts, Trig Integrals, Trig Sub, Partial Fractions

**Phase 2 — Classical Techniques | 85 min**

*Four technique families. Each has a clear trigger, a step-by-step procedure, and a telltale pattern. The hard part isn't executing any single technique — it's choosing the right one. This session teaches you the decision tree.*

**Prerequisites**: 16A (FTC & $u$-sub), 14B (chain/product rules), 11A (trig)

---

## The Integration Decision Tree

> **Before you start**, run this checklist top to bottom. The first match wins.

```
Look at the integral. Ask:

1. Is it a basic form from the dictionary?           →  Antiderivative dictionary (16A)
2. Is it f(g(x))·g'(x) — a function AND its deriv?   →  u-substitution (16A)
3. Is it a PRODUCT of two different function types?   →  Integration by PARTS (16B-A)
4. Is it sin^m cos^n or tan^m sec^n?                 →  Trigonometric INTEGRALS (16B-B)
5. Is there √(a²±x²) or √(x²-a²)?                    →  Trigonometric SUBSTITUTION (16B-C)
6. Is it a rational function P(x)/Q(x)?              →  PARTIAL FRACTIONS (16B-D)
```

---

## Part A: Integration by Parts — Undoing the Product Rule

> **Trigger**: A **product of two unrelated function families** (polynomial×exponential, log×polynomial, inverse trig×anything).
>
> **Procedure**: $\int u\,dv = uv - \int v\,du$. Choose $u$ using LIATE. Let $dv$ be everything else.

---

## Example 1: The Parts Algorithm — Six Steps

**Algorithm for $\int f(x)g(x)\,dx$**:

| Step | Action |
|:---:|:---|
| 1 | **Choose $u$** using LIATE: **L**og, **I**nverse trig, **A**lgebraic ($x^n$), **T**rig, **E**xponential |
| 2 | **Set $dv$** = everything else (including $dx$) |
| 3 | **Compute $du$** = derivative of $u$, times $dx$ |
| 4 | **Compute $v$** = integrate $dv$ (no $+C$ needed here) |
| 5 | **Assemble**: $uv - \int v\,du$ |
| 6 | **Integrate** $\int v\,du$. It should be simpler than the original |

---

## Example 2: Polynomial × Exponential — LIATE in Action

$\int x e^x\,dx$.

| Step | Action |
|:---:|:---|
| 1 | $u = x$ (Algebraic beats Exponential) |
| 2 | $dv = e^x\,dx$ |
| 3 | $du = 1\cdot dx$ |
| 4 | $v = \int e^x\,dx = e^x$ |
| 5 | $uv - \int v\,du = x e^x - \int e^x\,dx$ |
| 6 | $= x e^x - e^x + C = e^x(x-1) + C$ |

**Check**: $\frac{d}{dx}[e^x(x-1)] = e^x(x-1) + e^x(1) = x e^x$. ✓

---

## Example 3: Log × Anything — Log Always Wins (LIATE Priority 1)

$\int \ln x\,dx$. This is a product of $\ln x$ and $1$ (implicit).

| Step | Action |
|:---:|:---|
| 1 | $u = \ln x$ (Log — highest priority) |
| 2 | $dv = 1\cdot dx$ |
| 3 | $du = \frac{1}{x}\,dx$ |
| 4 | $v = \int 1\,dx = x$ |
| 5, 6 | $x\ln x - \int x\cdot\frac{1}{x}\,dx = x\ln x - \int 1\,dx = x\ln x - x + C$ |

**Memorize**: $\int \ln x\,dx = x\ln x - x + C$. This comes up constantly.

---

## Example 4: Inverse Trig — LIATE Priority 2

$\int \arctan x\,dx$.

| Step | Action |
|:---:|:---|
| 1 | $u = \arctan x$ (Inverse trig beats implicit 1) |
| 2 | $dv = 1\cdot dx$ |
| 3 | $du = \frac{1}{1+x^2}\,dx$ |
| 4 | $v = x$ |
| 5, 6 | $x\arctan x - \int \frac{x}{1+x^2}\,dx$ |

The new integral is now a $u$-sub: $w=1+x^2$, $dw=2x\,dx$.
$= x\arctan x - \frac{1}{2}\ln(1+x^2) + C$.

---

## Example 5: Two Rounds — Trig × Exponential (The Cycling Pattern)

$\int e^x\sin x\,dx$. Neither function simplifies when differentiated. The integral **cycles**.

**Procedure for cycling integrals**:
1. Apply parts twice. Name the original integral $I$.
2. When $I$ reappears, solve for it algebraically.
3. Add $+C$ at the very end.

| Round | $u$ | $dv$ | $du$ | $v$ | Result |
|:---:|:---|:---|:---|:---|:---|
| 1 | $\sin x$ | $e^x dx$ | $\cos x\,dx$ | $e^x$ | $I = e^x\sin x - \int e^x\cos x\,dx$ |
| 2 | $\cos x$ | $e^x dx$ | $-\sin x\,dx$ | $e^x$ | $I = e^x\sin x - (e^x\cos x + I)$ |

Simplify: $I = e^x\sin x - e^x\cos x - I$ → $2I = e^x(\sin x - \cos x)$ → $I = \frac{e^x}{2}(\sin x - \cos x) + C$.

**Add $+C$ only when the integral is fully solved** — at the end.

---

## Example 6: Parts Quick Reference

| If you see... | Choose $u=$ | Why |
|:---|:---|:---|
| $x^n e^{kx}$ | $u = x^n$ | Differentiating polynomial lowers its degree → simpler |
| $x^n \sin x$ or $x^n \cos x$ | $u = x^n$ | Same — polynomial simplifies |
| $(\ln x) \times (\text{anything})$ | $u = \ln x$ | Derivative is $\frac{1}{x}$, which tames the rest |
| $(\arctan x) \times (\text{anything})$ | $u = \text{inverse trig}$ | Derivative is algebraic → simpler |
| $e^{kx}\sin(mx)$ or $e^{kx}\cos(mx)$ | Either | It cycles — apply twice, solve for $I$ |

---

## Part B: Trigonometric Integrals — Exploiting $\sin^2+\cos^2=1$

> **Trigger**: The integrand is built from $\sin^m x$, $\cos^n x$, $\tan^m x$, $\sec^n x$.
>
> **Strategy**: Use identities to reduce to a $u$-sub.

---

## Example 7: $\int \sin^m x\cos^n x\,dx$ — The Parity Decision Tree

```
Check the exponents m and n:

Is m ODD?
  → Peel off ONE sin x.
  → Convert sin^{m-1} x to (1−cos²x)^{(m-1)/2}.
  → u = cos x, du = −sin x dx.
  
Is n ODD?  (if m is even)
  → Peel off ONE cos x.
  → Convert cos^{n-1} x to (1−sin²x)^{(n-1)/2}.
  → u = sin x, du = cos x dx.
  
Are BOTH EVEN?
  → Use half-angle: sin²x = (1−cos2x)/2, cos²x = (1+cos2x)/2.
  → Reduces powers. Repeat if needed.
```

---

## Example 8: Odd Power — Peel, Convert, $u$-Sub

$\int \sin^3 x\,dx$. $m=3$ (odd). Follow the "m odd" branch.

1. **Peel**: $\sin^3 x = \sin x \cdot \sin^2 x$.
2. **Convert**: $\sin^2 x = 1 - \cos^2 x$. Integral: $\int \sin x(1-\cos^2 x)\,dx$.
3. **$u$-sub**: $u = \cos x$, $du = -\sin x\,dx \to \sin x\,dx = -du$.
4. **Integrate**: $\int (1-u^2)(-du) = -u + \frac{u^3}{3} + C$.
5. **Back**: $-\cos x + \frac{\cos^3 x}{3} + C$.

---

## Example 9: Even Power — Half-Angle Formula

$\int \cos^2 x\,dx$. $n=2$ (even, and $m=0$ which is even too).

1. **Half-angle**: $\cos^2 x = \frac{1+\cos 2x}{2}$.
2. **Integrate**: $\int \frac{1+\cos 2x}{2}\,dx = \frac{1}{2}\int (1+\cos 2x)\,dx$.
3. $= \frac{1}{2}(x + \frac{\sin 2x}{2}) + C = \frac{x}{2} + \frac{\sin 2x}{4} + C$.

---

## Example 10: $\int \tan^m x\sec^n x\,dx$ — Save $\sec^2 x$

```
Is n EVEN (n≥2)?
  → Save ONE sec²x. It becomes du.
  → Convert remaining sec^{n-2} to (tan²x+1)^{(n-2)/2}.
  → u = tan x, du = sec²x dx.
  
Is m ODD (n≥1)?
  → Save ONE sec x tan x. It becomes du.
  → Convert remaining tan^{m-1} to (sec²x−1)^{(m-1)/2}.
  → u = sec x, du = sec x tan x dx.
  
Otherwise → convert everything to sin/cos and use the sin^m cos^n strategy.
```

$\int \tan^3 x\sec^2 x\,dx$: $n=2$ (even). Save $\sec^2 x$ for $du$.
$u = \tan x$, $du = \sec^2 x\,dx$. Integral = $\int u^3\,du = \frac{\tan^4 x}{4} + C$.

---

## Part C: Trigonometric Substitution — Killing the Square Root

> **Trigger**: The integrand contains $\sqrt{a^2 \pm x^2}$ or $\sqrt{x^2 - a^2}$.
>
> **Strategy**: Replace $x$ with a trig function. The root disappears via a Pythagorean identity.

---

## Example 11: The Trig Sub Lookup Table

| Form | Substitute | $dx$ becomes | The root simplifies to |
|:---|:---|:---|:---|
| $\sqrt{a^2-x^2}$ | $x = a\sin\theta$ | $a\cos\theta\,d\theta$ | $a\cos\theta$ |
| $\sqrt{a^2+x^2}$ | $x = a\tan\theta$ | $a\sec^2\theta\,d\theta$ | $a\sec\theta$ |
| $\sqrt{x^2-a^2}$ | $x = a\sec\theta$ | $a\sec\theta\tan\theta\,d\theta$ | $a\tan\theta$ |

---

## Example 12: Trig Sub Step by Step

| Step | Action | For $\int\frac{dx}{\sqrt{4-x^2}}$ |
|:---:|:---|:---|
| 1 | **Identify** the root form | $\sqrt{4-x^2} = \sqrt{2^2-x^2}$ → Form 1 |
| 2 | **Substitute** $x$ and $dx$ | $x = 2\sin\theta$, $dx = 2\cos\theta\,d\theta$ |
| 3 | **Simplify** the root | $\sqrt{4-x^2} = \sqrt{4-4\sin^2\theta} = 2\cos\theta$ |
| 4 | **Rewrite** integral in $\theta$ | $\int\frac{2\cos\theta\,d\theta}{2\cos\theta} = \int d\theta$ |
| 5 | **Integrate** | $\theta + C$ |
| 6 | **Back-substitute** via right triangle | $\theta = \arcsin(x/2)$ |

---

## Example 13: $\sqrt{a^2+x^2}$ — The Tangent Case

$\int \frac{dx}{\sqrt{x^2+1}}$. Form: $\sqrt{x^2+1}$ → $x=\tan\theta$, $a=1$.

1. $x = \tan\theta$, $dx = \sec^2\theta\,d\theta$.
2. $\sqrt{x^2+1} = \sqrt{\tan^2\theta+1} = \sec\theta$.
3. Integral: $\int \frac{\sec^2\theta\,d\theta}{\sec\theta} = \int \sec\theta\,d\theta$.
4. $\int \sec\theta\,d\theta = \ln|\sec\theta + \tan\theta| + C$. (Standard — memorize.)
5. **Back-substitute**: Draw a right triangle with angle $\theta$, opposite = $x$, adjacent = $1$. Hypotenuse = $\sqrt{x^2+1}$. So $\sec\theta = \sqrt{x^2+1}$, $\tan\theta = x$.
6. Answer: $\ln|x + \sqrt{x^2+1}| + C$.

---

## Example 14: The Right Triangle Method

**After integrating in $\theta$, draw a right triangle to express trig functions in $x$:**

| Substitution | Triangle label | $\sin\theta$ | $\cos\theta$ | $\tan\theta$ | $\sec\theta$ |
|:---|:---|:---|:---|:---|:---|
| $x=a\sin\theta$ | Opp=$x$, Hyp=$a$ | $x/a$ | $\sqrt{a^2-x^2}/a$ | $x/\sqrt{a^2-x^2}$ | — |
| $x=a\tan\theta$ | Opp=$x$, Adj=$a$ | $x/\sqrt{x^2+a^2}$ | $a/\sqrt{x^2+a^2}$ | $x/a$ | $\sqrt{x^2+a^2}/a$ |
| $x=a\sec\theta$ | Hyp=$x$, Adj=$a$ | $\sqrt{x^2-a^2}/x$ | $a/x$ | $\sqrt{x^2-a^2}/a$ | $x/a$ |

---

## Part D: Partial Fractions — Splitting Rational Functions

> **Trigger**: The integrand is $\frac{P(x)}{Q(x)}$ — a rational function with a factorable denominator.
>
> **Strategy**: Decompose into a sum of simpler fractions, each matching the dictionary.

---

## Example 15: The Partial Fractions Algorithm

| Step | Action |
|:---:|:---|
| 1 | **Check degrees**: If $\deg(P) \geq \deg(Q)$, do polynomial long division FIRST |
| 2 | **Factor** $Q(x)$ into linear factors $(ax+b)^k$ and irreducible quadratics $(ax^2+bx+c)^m$ |
| 3 | **Write decomposition** using the template below |
| 4 | **Solve** for constants $A,B,C,\ldots$ (plug roots or match coefficients) |
| 5 | **Integrate** each term |

---

## Example 16: Decomposition Templates

| Factor type | Template |
|:---|:---|
| $(ax+b)$ — distinct linear | $\dfrac{A}{ax+b}$ |
| $(ax+b)^k$ — repeated linear | $\dfrac{A_1}{ax+b} + \dfrac{A_2}{(ax+b)^2} + \cdots + \dfrac{A_k}{(ax+b)^k}$ |
| $ax^2+bx+c$ — irreducible quadratic | $\dfrac{Ax+B}{ax^2+bx+c}$ |

---

## Example 17: Distinct Linear Factors

$\int \frac{1}{x^2-1}\,dx = \int \frac{1}{(x-1)(x+1)}\,dx$.

1. Degree: 0 < 2. No division.
2. Denominator already factored: $(x-1)(x+1)$.
3. Template: $\frac{1}{(x-1)(x+1)} = \frac{A}{x-1} + \frac{B}{x+1}$.
4. Clear denominators: $1 = A(x+1) + B(x-1)$.

**Solve by plugging roots** (fastest):
- Plug $x=1$: $1 = 2A \to A = 1/2$.
- Plug $x=-1$: $1 = -2B \to B = -1/2$.

5. Integrate: $\int (\frac{1/2}{x-1} - \frac{1/2}{x+1})\,dx = \frac{1}{2}\ln|x-1| - \frac{1}{2}\ln|x+1| + C = \frac{1}{2}\ln\left|\frac{x-1}{x+1}\right| + C$.

---

## Example 18: Repeated Linear Factor

$\int \frac{x}{(x-1)^2}\,dx$.

Template: $\frac{x}{(x-1)^2} = \frac{A}{x-1} + \frac{B}{(x-1)^2}$.
Clear: $x = A(x-1) + B = Ax + (B-A)$.
Match: $A=1$, $B-A=0 \to B=1$.

Integrate: $\int (\frac{1}{x-1} + \frac{1}{(x-1)^2})\,dx = \ln|x-1| - \frac{1}{x-1} + C$.

---

## Example 19: Quadratic Factor

$\int \frac{1}{x(x^2+1)}\,dx$.

Template: $\frac{1}{x(x^2+1)} = \frac{A}{x} + \frac{Bx+C}{x^2+1}$.
Clear: $1 = A(x^2+1) + (Bx+C)x = (A+B)x^2 + Cx + A$.
Match: $A+B=0$, $C=0$, $A=1 \to B=-1$.

Integrate: $\int (\frac{1}{x} - \frac{x}{x^2+1})\,dx = \ln|x| - \frac{1}{2}\ln(x^2+1) + C$.

---

## Example 20: When Long Division Is Required First

$\int \frac{x^3}{x^2+1}\,dx$. Degree: $3 \geq 2$ → divide.

$x^3 \div (x^2+1)$: $x^3 = x(x^2+1) - x$. So $\frac{x^3}{x^2+1} = x - \frac{x}{x^2+1}$.

Integrate: $\int x\,dx - \int \frac{x}{x^2+1}\,dx = \frac{x^2}{2} - \frac{1}{2}\ln(x^2+1) + C$.

> **Up to here**: Parts (LIATE). Trig integrals (odd→peel+sub, even→half-angle, tan/sec→save sec²). Trig sub (√form→sin/tan/sec). Partial fractions (factor→template→solve→integrate). All four techniques integrated into one decision tree.

---

## Common Mistakes

### Mistake 1: Choosing $u$ and $dv$ backwards in parts

**Wrong**: $u=e^x$, $dv=x\,dx$ for $\int xe^x\,dx$. Then $\int v\,du = \int \frac{x^2}{2}e^x\,dx$ — worse! **Right**: $u=x$, $dv=e^x\,dx$. The new integral $\int e^x\,dx$ is simpler.

### Mistake 2: Using trig sub when $u$-sub is faster

**Wrong**: $\int \frac{x}{\sqrt{1-x^2}}\,dx$ → trig sub leads to $\int \sin\theta\,d\theta$. **Right**: $u=1-x^2$, $du=-2x\,dx$. One step: $-\frac{1}{2}\int u^{-1/2}\,du = -\sqrt{1-x^2} + C$. Always check if a simple $u$-sub works first.

### Mistake 3: Wrong trig substitution for the root form

**Wrong**: $x=2\sin\theta$ for $\sqrt{x^2+4}$. Then $\sqrt{4\sin^2\theta+4}$ does NOT simplify. **Right**: $x=2\tan\theta$. Then $\sqrt{4\tan^2\theta+4} = 2\sec\theta$.

### Mistake 4: Forgetting long division before partial fractions

**Wrong**: Decomposing $\frac{x^3}{x^2-1}$ directly. **Right**: Numerator degree (3) ≥ denominator degree (2). Divide first: result = $x + \frac{x}{x^2-1}$. Then decompose the remainder.

### Mistake 5: Half-angle when an odd power is available

**Wrong**: Using $\sin^2 x = \frac{1-\cos 2x}{2}$ for $\int \sin^3 x\,dx$. **Right**: Peel one $\sin x$, convert $\sin^2 x = 1-\cos^2 x$, $u$-sub with $u=\cos x$. Much faster.

---

## What We Just Did

```
(1) Parts: ∫u dv = uv − ∫v du. LIATE for u. Cycle → apply twice, solve for I.

(2) Trig Integrals:
    sin^m cos^n: odd→peel+convert+u-sub. both even→half-angle.
    tan^m sec^n: even n→save sec², u=tan. odd m→save sec tan, u=sec.

(3) Trig Sub: √(a²−x²)→x=a sinθ. √(a²+x²)→x=a tanθ. √(x²−a²)→x=a secθ.
    Right triangle for back-substitution.

(4) Partial Fractions:
    deg(P)≥deg(Q)? → long divide first.
    Factor Q. Write template. Solve constants. Integrate each term.
```

---

## Practice 1

$\int x\sin x\,dx$. Run the parts algorithm. LIATE: $u=x$ (Algebraic), $dv=\sin x\,dx$.

→ Solutions: [Solutions](solutions/16B-solutions.md#practice-1)

---

## Practice 2

$\int \cos^3 x\,dx$. Odd power of cosine → peel one, convert $\cos^2$, $u$-sub with $u=\sin x$.

→ Solutions: [Solutions](solutions/16B-solutions.md#practice-2)

---

## Practice 3

$\int \frac{dx}{x^2+4}$. Arctan formula directly, OR trig sub $x=2\tan\theta$. Show both.

→ Solutions: [Solutions](solutions/16B-solutions.md#practice-3)

---

## Practice 4

$\int \frac{x+1}{x^2-3x+2}\,dx$. Factor denominator: $(x-1)(x-2)$. Template: $\frac{A}{x-1}+\frac{B}{x-2}$. Solve, integrate.

→ Solutions: [Solutions](solutions/16B-solutions.md#practice-4)

---

## Practice 5: Real Battle (Constructive)

A classmate sees $\int \frac{x}{\sqrt{1-x^2}}\,dx$ and says: "Trig sub! $\sqrt{1-x^2}$ means $x=\sin\theta$." (a) Is there a faster way? Solve it with $u$-sub. (b) Now solve $\int \frac{1}{\sqrt{1-x^2}}\,dx$ — was trig sub the right call this time? (c) Write a one-sentence rule: when $\sqrt{a^2-x^2}$ appears, how do you choose between $u$-sub and trig sub?

→ Solutions: [Solutions](solutions/16B-solutions.md#practice-5)

---

## Basic Algebra Drill — Advanced Integration (10 Problems)

> Identify the technique from the decision tree. Execute the procedure.

**D1.** $\int x\cos x\,dx$. Parts: $u=x$, $dv=\cos x\,dx$.

**D2.** $\int \ln(2x)\,dx$. Parts: $u=\ln(2x)$, $dv=dx$.

**D3.** $\int \sin^2 x\,dx$. Trig integral (even → half-angle).

**D4.** $\int \tan x\sec^2 x\,dx$. Tan/sec: $n=2$ (even) → $u=\tan x$.

**D5.** $\int \frac{dx}{\sqrt{9-x^2}}$. Trig sub: $x=3\sin\theta$.

**D6.** $\int \frac{dx}{x^2+9}$. Arctan formula: $\frac{1}{3}\arctan(x/3) + C$.

**D7.** $\int \frac{1}{x^2-x}\,dx$. Partial fractions: factor $x(x-1)$.

**D8.** $\int x^2 e^x\,dx$. Parts twice: first $u=x^2$, then $u=x$.

**D9.** $\int \sin x\cos x\,dx$. Two methods: $u=\sin x$ OR $\sin 2x = 2\sin x\cos x$. Verify answers match.

**D10.** $\int \frac{x}{\sqrt{1-x^2}}\,dx$. Decision: trig sub or $u$-sub? Choose the faster one.

> Solutions: [Solutions](solutions/16B-solutions.md#basic-drill)

---

## Advanced Algebra Drill — Advanced Integration (10 Problems)

> Multi-step. May combine techniques.

**A1.** $\int e^x\cos x\,dx$. Cycling parts — apply twice, solve for $I$.

**A2.** $\int \sin^4 x\,dx$. Repeated half-angle: $(\frac{1-\cos 2x}{2})^2$, expand, half-angle again.

**A3.** $\int \frac{dx}{(x^2+1)^2}$. Trig sub $x=\tan\theta$. Right triangle for back-sub.

**A4.** $\int \frac{x^3}{\sqrt{x^2+1}}\,dx$. $u=x^2+1$ is faster than trig sub — try it.

**A5.** $\int \frac{x^2+2x-1}{(x-1)(x^2+1)}\,dx$. Quadratic factor: template $\frac{A}{x-1} + \frac{Bx+C}{x^2+1}$.

**A6.** $\int \arctan x\,dx$. Parts: $u=\arctan x$, $dv=dx$. Result needs $u$-sub.

**A7.** $\int \sec^3 x\,dx$. Parts: $u=\sec x$, $dv=\sec^2 x\,dx$. Classic — it cycles.

**A8.** $\int \frac{\sqrt{x^2-4}}{x}\,dx$. Trig sub $x=2\sec\theta$. Right triangle needed.

**A9.** $\int x\arcsin x\,dx$. Parts: $u=\arcsin x$, $dv=x\,dx$. Result needs trig sub or clever $u$-sub.

**A10.** Derive the reduction formula: $\int \sin^n x\,dx = -\frac{1}{n}\sin^{n-1}x\cos x + \frac{n-1}{n}\int \sin^{n-2}x\,dx$. (Parts: $u=\sin^{n-1}x$, $dv=\sin x\,dx$.)

> Solutions: [Solutions](solutions/16B-solutions.md#advanced-drill)

---

## Today's Procedure

| When you see... | Do this... |
|:---|:---|
| Product of unrelated functions | **Parts**: LIATE for $u$, $dv$ = rest. Cycle → twice, solve for $I$ |
| $\sin^m x\cos^n x$, $m$ or $n$ odd | **Trig integral**: peel one, convert rest, $u$-sub |
| $\sin^m x\cos^n x$, both even | **Half-angle**: reduce powers, integrate, repeat if needed |
| $\tan^m x\sec^n x$, $n$ even | Save $\sec^2 x$, $u=\tan x$ |
| $\sqrt{a^2-x^2}$ | **Trig sub**: $x = a\sin\theta$ |
| $\sqrt{a^2+x^2}$ | **Trig sub**: $x = a\tan\theta$ |
| $\sqrt{x^2-a^2}$ | **Trig sub**: $x = a\sec\theta$ |
| $\frac{P(x)}{Q(x)}$, $Q$ factorable | **Partial fractions**: factor → template → solve → integrate |
| $\frac{P(x)}{Q(x)}$, $\deg P \geq \deg Q$ | Long divide first, then partial fractions on remainder |

---

## Terminology

| What we call it | Math term | Notation |
|:---:|:---:|:---:|
| reverse product rule | integration by parts | $\int u\,dv = uv - \int v\,du$ |
| priority order for $u$ | LIATE | Log, Inverse trig, Algebraic, Trig, Exponential |
| peel-convert-substitute | odd-power trig strategy | $\sin^3 x = \sin x(1-\cos^2 x)$ |
| halve the angle | half-angle formula | $\sin^2 x = \frac{1-\cos 2x}{2}$ |
| remove root via trig | trigonometric substitution | $x = a\sin\theta$, etc. |
| triangle for back-sub | reference triangle | SOH CAH TOA |
| split rational function | partial fraction decomposition | $\frac{A}{x-a} + \frac{B}{x-b} + \cdots$ |
| numerator too big | improper rational function | do long division first |
| integral appears on both sides | cycling / recursive integral | solve for $I$ algebraically |
