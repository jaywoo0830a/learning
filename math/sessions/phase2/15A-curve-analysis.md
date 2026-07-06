# Session 15A: Curve Analysis — Tangent Lines, Extrema, and Graph Sketching

**Phase 2 — Classical Techniques | 80 min**

*Prerequisites: 14A/B (derivatives), 09A (7-step graph drawing), 13A (limits)*

---

## Part A: Tangent and Normal Lines

---

## Example 1: Tangent Line Equation

Tangent to $f$ at $x=a$: $y - f(a) = f'(a)(x-a)$.

$f(x)=x^2$ at $x=3$: $f(3)=9$, $f'(3)=6$. Tangent: $y-9=6(x-3) \to y=6x-9$.

---

## Example 2: Normal Line — Perpendicular to Tangent

Slope of normal = $-\frac{1}{f'(a)}$ (negative reciprocal).

For $f(x)=x^2$ at $x=3$: normal slope $=-1/6$, line: $y-9=-\frac{1}{6}(x-3)$.

---

## Example 3: Tangent from an External Point

Find tangent lines to $y=x^2$ that pass through $(0,-1)$.

Let the tangent point be $(a, a^2)$. Slope $=2a$. Line: $y-a^2=2a(x-a)$.
Through $(0,-1)$: $-1-a^2=2a(0-a)=-2a^2 \to a^2=1$. $a=\pm1$.
Tangents: $y=2x-1$ and $y=-2x-1$.

---

## Part B: Mean Value Theorem (MVT)

---

## Example 4: MVT — There's a Point with Average Slope

If $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$, there exists $c\in(a,b)$ with $f'(c)=\frac{f(b)-f(a)}{b-a}$.

$f(x)=x^2$ on $[1,4]$: average slope $=\frac{16-1}{3}=5$. $f'(x)=2x=5 \to x=2.5$. ✓

---

## Part C: Increasing, Decreasing, and Extrema

---

## Example 5: First Derivative Sign Test

$f'>0$ → increasing. $f'<0$ → decreasing.

$f(x)=x^3-3x$: $f'(x)=3x^2-3=3(x-1)(x+1)$.
Sign chart: $(-\infty,-1)$: $f'>0$ (up). $(-1,1)$: $f'<0$ (down). $(1,\infty)$: $f'>0$ (up).

---

## Example 6: Critical Points and Local Extrema

Critical points: $f'=0$ or $f'$ undefined. Test sign change of $f'$ to classify.

$f(x)=x^3-3x$: critical at $x=\pm1$.
$x=-1$: $f'$ goes + → − → **local max** at $(-1,2)$.
$x=1$: $f'$ goes − → + → **local min** at $(1,-2)$.

---

## Example 7: $f'=0$ but No Extremum — Inflection Points

$f(x)=x^3$: $f'(0)=0$, but $f'$ does NOT change sign — always positive. No extremum at $x=0$. Instead, this is an **inflection point** where curvature changes.

---

## Example 8: Second Derivative Test

$f'(a)=0$: if $f''(a)>0$ → local min; $f''(a)<0$ → local max; $f''(a)=0$ → inconclusive.

$f(x)=x^3-3x$: $f''(x)=6x$. $f''(-1)=-6<0$ → max. $f''(1)=6>0$ → min. ✓

---

## Part D: Concavity and Inflection Points

---

## Example 9: Second Derivative Sign

$f''>0$: concave up (cup shape). $f''<0$: concave down (cap shape). $f''=0$ or undefined: possible inflection.

$f(x)=x^3-3x$: $f''(x)=6x$. $x<0$: concave down. $x>0$: concave up. Inflection at $(0,0)$.

![Critical points and optimization](graphs/15a-critical-points.png)

---

## Part E: The 7-Step Curve Sketch

---

## Example 10: Complete Graph Analysis

$f(x)=\frac{x^2}{x-1}$.

① **Domain**: $x\neq1$.
② **Intercepts**: $(0,0)$.
③ **Asymptotes**: vertical $x=1$. Slant: divide → $y=x+1+\frac{1}{x-1}$, asymptote $y=x+1$.
④ **$f'$**: $f'(x)=\frac{x(x-2)}{(x-1)^2}$. Critical at $x=0,2$. $x=0$: max $(0,0)$. $x=2$: min $(2,4)$.
⑤ **$f''$**: $f''(x)=\frac{2}{(x-1)^3}$. Never 0. $x<1$: concave down. $x>1$: concave up.
⑥ **Sketch**: left branch (below slant, concave down, peak at origin), right branch (min at $(2,4)$, concave up, hugging slant).

---

## What We Just Did

```
(1) Tangent line: y-f(a)=f'(a)(x-a). Normal: slope = -1/f'(a).
(2) MVT: average slope matches instantaneous slope somewhere.
(3) f' sign → increasing/decreasing. f'=0 + sign change → extremum.
(4) f'' sign → concavity. f''=0 + sign change → inflection.
(5) 7-step curve sketch using f, f', f''.
```

---

## Practice 1

Find the tangent and normal lines to $f(x)=x^3$ at $x=1$.

→ Solutions: [Solutions](solutions/15A-solutions.md#practice-1)

---

## Practice 2

Find all local extrema of $f(x)=x^4-4x^3$. Use the second derivative test.

→ Solutions: [Solutions](solutions/15A-solutions.md#practice-2)

---

## Practice 3

Sketch $f(x)=x^3-3x^2$ using domain, intercepts, $f'$, $f''$.

→ Solutions: [Solutions](solutions/15A-solutions.md#practice-3)

---

## Practice 4: Real Battle

$f(x)=\frac{x^2-1}{x^2+1}$. Find all asymptotes, extrema, inflection points. Sketch.

→ Solutions: [Solutions](solutions/15A-solutions.md#practice-4)

---

## Basic Algebra Drill — Curve Analysis (10 Problems)

**D1.** Find the tangent line to $f(x)=x^2+2x$ at $x=1$.

**D2.** Find all critical points of $f(x)=x^3-6x^2+9x$.

**D3.** Classify the critical points from D2 as max/min/neither.

**D4.** Find intervals where $f(x)=x^3-3x$ is increasing.

**D5.** Find all inflection points of $f(x)=x^4-6x^2$.

**D6.** Determine concavity of $f(x)=\ln x$ on $(0,\infty)$.

**D7.** Apply MVT to $f(x)=\sqrt{x}$ on $[1,9]$. Find $c$.

**D8.** Find the normal line to $f(x)=e^x$ at $x=0$.

**D9.** Find horizontal asymptotes of $f(x)=\frac{x^2}{x^2+4}$.

**D10.** Find all vertical asymptotes of $f(x)=\frac{x}{x^2-9}$.

> Solutions: [Solutions](solutions/15A-solutions.md#basic-drill)

---

## Advanced Algebra Drill — Curve Analysis (10 Problems)

**A1.** Prove that $f(x)=x^3+ax+b$ has exactly one inflection point and find it.

**A2.** Find $a,b,c$ so $f(x)=ax^3+bx^2+cx$ has a local max at $(-1,2)$ and a local min at $(1,-2)$.

**A3.** $f(x)=\frac{x}{x^2+1}$. Find all extrema, asymptotes, inflection points, and sketch.

**A4.** Prove that $\frac{x}{1+x} < \ln(1+x) < x$ for $x>0$ by analyzing $f(x)=\ln(1+x)-\frac{x}{1+x}$ and $g(x)=x-\ln(1+x)$.

**A5.** Find the point on $y=\sqrt{x}$ closest to $(2,0)$.

**A6.** A line with slope $m$ through $(0,1)$ is tangent to $y=x^2$. Find all possible $m$.

**A7.** $f(x)=x^4-8x^2+3$. Find all intervals of increase, decrease, concavity, and all extrema.

**A8.** Sketch $f(x)=xe^{-x}$ using $f$, $f'$, $f''$.

**A9.** Show that $f(x)=x^3-3x+1$ has exactly three real roots. Use extrema and IVT.

**A10.** Find the equation of the tangent line to $f(x)=\ln x$ that passes through the origin.

> Solutions: [Solutions](solutions/15A-solutions.md#advanced-drill)

---

## Today's Procedure

```
Step 1: Tangent: find point, find slope f'(a), write y-f(a)=f'(a)(x-a).
Step 2: f' tells increasing/decreasing and extrema. f'' tells concavity.
Step 3: Curve sketch = domain + asymptotes + intercepts + f' + f''.
Step 4: MVT guarantees c where f'(c) equals average slope.
```
