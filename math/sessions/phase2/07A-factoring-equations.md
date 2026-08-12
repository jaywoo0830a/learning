# Session 07A: Factoring and Polynomial Equations

**Phase 2 — Classical Techniques | 60 min**

---

## Part A: Factoring — Tearing into Multiplication Form

---

## Example 1: Find Two Numbers ($x^2+bx+c$)

Find two numbers that **add to $b$** and **multiply to $c$**.

$x^2+7x+12$. Sum 7, product 12 → $3,4$ → $(x+3)(x+4)$.

$x^2-5x+6$. Sum −5, product 6 → $-2,-3$ → $(x-2)(x-3)$.

$x^2+x-6$. Sum 1, product −6 → $-2,3$ → $(x-2)(x+3)$.

---

## Example 2: The $ac$ Method ($ax^2+bx+c$, $a\neq1$)

$2x^2+7x+3$. $ac = 6$. Need two numbers: sum 7, product 6 → $1,6$.
$2x^2+x+6x+3 = x(2x+1)+3(2x+1) = (x+3)(2x+1)$.

$6x^2-x-2$. $ac=-12$. Sum −1, product −12 → $3,-4$.
$6x^2+3x-4x-2 = 3x(2x+1)-2(2x+1) = (3x-2)(2x+1)$.

---

## Example 3: Perfect Square — $(a\pm b)^2$

$x^2+6x+9 = (x+3)^2$. Check: $2\cdot x\cdot 3 = 6x$ ✓.
$4x^2-12x+9 = (2x-3)^2$.
$x^2-10x+25 = (x-5)^2$.

---

## Example 4: Difference of Squares — $a^2-b^2=(a-b)(a+b)$

$x^2-16 = (x-4)(x+4)$.
$9x^2-25 = (3x-5)(3x+5)$.
$x^4-1 = (x^2-1)(x^2+1) = (x-1)(x+1)(x^2+1)$.

![a²−b² = (a−b)(a+b) — the area model](graphs/0812/07A/07a-diff-squares.png)

---

## Example 5: Sum/Difference of Cubes

$a^3+b^3 = (a+b)(a^2-ab+b^2)$.
$a^3-b^3 = (a-b)(a^2+ab+b^2)$.

$x^3-8 = (x-2)(x^2+2x+4)$.
$8x^3+27 = (2x+3)(4x^2-6x+9)$.

---

## Example 6: Common Factor — Always Pull Out First!

$3x^3-12x = 3x(x^2-4) = 3x(x-2)(x+2)$. Pull out GCF, then factor what remains.

---

## Example 6A: The Quadratic Formula — When Factoring Fails

$ax^2+bx+c=0$ → $x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$.

The **discriminant** $D = b^2-4ac$ decides everything:
- $D > 0$: two distinct real roots
- $D = 0$: one real root (double)
- $D < 0$: two complex conjugate roots

**$x^2+2x+5=0$**: $D = 4-20 = -16 < 0$ → $x = -1 \pm 2i$ (no real roots — the parabola misses the $x$-axis).

**$2x^2-3x-2=0$**: $D = 9+16 = 25 > 0$ → $x = \frac{3\pm5}{4}$ → $2,\ -\frac12$. Same as factoring $(2x+1)(x-2)$ — the formula and factoring always agree.

> **Rule**: try factoring first (faster); fall back on the formula when it doesn't work cleanly. The formula always works, including over the complex numbers.

![Discriminant: D>0, D=0, D<0](graphs/0812/07A/07a-discriminant.png)

---

## Part B: Higher-Degree Equations

---

## Example 7: Synthetic Division

For $x^3-6x^2+11x-6=0$, test $x=1$: $1-6+11-6=0$. ✓
Synthetic divide by $(x-1)$: quotient $x^2-5x+6 = (x-2)(x-3)$.
Roots: $1,2,3$.

---

## Example 8: Rational Root Theorem

For $2x^3-3x^2-3x+2=0$, possible rational roots: $\pm1,\pm2,\pm\frac{1}{2}$.
Test $x=2$: $16-12-6+2=0$. ✓ Synthetic divide → $2x^2+x-1=(2x-1)(x+1)$.
Roots: $2, \frac{1}{2}, -1$.

![Roots of a cubic are the x-intercepts](graphs/0812/07A/07a-factor-graph.png)

---

## Example 8A: The Full Pipeline — Root by Root

**$x^4-2x^3-13x^2+14x+24=0$.** One run of the complete strategy:

1. **Rational root candidates**: divisors of 24: $\pm1,\pm2,\pm3,\pm4,\pm6,\pm8,\pm12,\pm24$.
2. **Test $x=2$**: $16-16-52+28+24=0$ ✓. Synthetic divide by $(x-2)$: quotient $x^3-13x-12$.
3. **Test $x=-1$** on the cubic: $-1+13-12=0$ ✓. Synthetic divide by $(x+1)$: quotient $x^2-x-12=(x-4)(x+3)$.
4. **All roots**: $2,\ -1,\ 4,\ -3$.

$x^4-2x^3-13x^2+14x+24 = (x-2)(x+1)(x-4)(x+3)$.

> **Pattern**: each successful test lowers the degree by one. Four roots (counting multiplicity) = degree 4 — a built-in check.

![Synthetic division layout for dividing by (x-1)](graphs/0812/07A/07a-synthetic-division.png)

---

## Example 9: Substitution $t=x^k$

$x^4-5x^2+4=0$. Let $t=x^2$: $t^2-5t+4=0$ → $t=1,4$. $x=\pm1,\pm2$.

---

## Example 10: Symmetric Coefficients — Divide by $x^2$

$2x^4+3x^3-4x^2+3x+2=0$. Divide by $x^2$: $2(x^2+x^{-2})+3(x+x^{-1})-4=0$.
Let $u=x+x^{-1}$, $x^2+x^{-2}=u^2-2$. Solve for $u$, then $x$.

---

## Example 11: Vieta's Formulas

For $x^3+px^2+qx+r=0$ with roots $a,b,c$:
$a+b+c = -p$, $ab+bc+ca = q$, $abc = -r$.

$x^3-6x^2+11x-6=0$. Sum of roots = 6, pairwise sum = 11, product = 6.

**Quartic extension**: for $x^4+px^3+qx^2+rx+s=0$ with roots $a,b,c,d$:
- sum $a+b+c+d = -p$
- pairwise $ab+ac+ad+bc+bd+cd = q$
- triple $abc+abd+acd+bcd = -r$
- product $abcd = s$

**Check with $(x-1)(x-2)(x-3)(x-4) = x^4-10x^3+35x^2-50x+24$**:
sum $=10$, pairwise $=35$, triple $=50$, product $=24$ ✓

![Polynomial roots and factorization](graphs/0812/07A/07a-cubic-roots.png)

---

## Example 12: Applications — Where Factoring Shows Up

**Geometry**: A rectangle has area 24 and perimeter 20. Let sides be $L,W$: $LW=24$, $L+W=10$. So $L,W$ are the roots of $t^2-10t+24=0=(t-4)(t-6)$ → the rectangle is $4\times6$.

**Physics**: A ball's height is $h(t)=-5t^2+20t+25$ (meters, seconds). When does it hit the ground? $h=0$: $-5t^2+20t+25=0$ → divide by $-5$: $t^2-4t-5=0=(t-5)(t+1)$ → $t=5$ (discard $t=-1$). Lands at $5$ s.

**Numbers**: The sum of a number and its reciprocal is $\frac52$. $x+\frac1x=\frac52$ → $2x^2-5x+2=0=(2x-1)(x-2)$ → $x=2$ or $\frac12$. Both work — a nice symmetry.

> **Key insight**: in every case the equation reduces to $(\text{factor})(\text{factor})=0$, and the answer comes from setting each factor to zero.

> **Up to here**: Factor: GCF first → two-numbers/ac/perfect-square/diff-of-squares/sum-diff-cubes.
> Higher-degree: rational root test → synthetic divide → reduce degree → substitution $t=x^k$ → Vieta.

---

## What We Just Did

```
(1) Factoring: GCF always first. Then ac-method for a≠1, difference of squares,
    sum/difference of cubes, perfect square recognition.

(2) Fallback: quadratic formula + discriminant D=b²−4ac. D>0 two real, D=0 one,
    D<0 complex. Factoring and the formula always agree.

(3) Higher-degree equations: rational root candidates → synthetic division.
    Each success reduces the degree by 1. Repeat until quadratic.

(4) Substitution t=x² or t=x³ for patterns. Vieta connects roots to coefficients
    (cubic AND quartic). Symmetric equations: divide by x², substitute u=x+1/x.
    Applications: geometry (area/perimeter), physics (projectile), numbers.
```

---

## Common Mistakes

### Mistake 1: Wrong sign in synthetic division
The factor is $(x-r)$, so divide by $+r$ (not $-r$).

### Mistake 2: Forgetting to pull out GCF first
$3x^2-12$ → pull 3: $3(x^2-4)=3(x-2)(x+2)$, don't factor $3x^2-12$ directly.

### Mistake 3: Counting a double root only once
$(x-2)^2(x+1)=0$ has roots $2,2,-1$ — three roots (counting multiplicity).

---

## Practice 1

Factor completely: $x^3-4x^2+x+6$. Use rational root test + synthetic division.

→ Solutions: [Solutions](solutions/07A-solutions.md#practice-1)

---

## Practice 2

Solve $x^4-13x^2+36=0$. Substitution $t=x^2$.

→ Solutions: [Solutions](solutions/07A-solutions.md#practice-2)

---

## Practice 3

If $x=2$ is a root of $x^3-3x^2+kx+4=0$, find $k$ and all three roots. Then verify the answer with Vieta's formulas (sum, pairwise sum, product).

→ Solutions: [Solutions](solutions/07A-solutions.md#practice-3)

---

## Practice 4: Real Battle

Solve $2x^4-5x^3+5x-2=0$. Hint: check $x=1$, synthetic divide, then look for a pattern in the cubic.

→ Solutions: [Solutions](solutions/07A-solutions.md#practice-4)

---

## Practice 5: Composition

Create a cubic equation whose roots are 2, −3, and 5. Write it in expanded form $x^3+px^2+qx+r=0$ and verify with Vieta.

→ Solutions: [Solutions](solutions/07A-solutions.md#practice-5)

---

## Basic Drills

**D1.** Factor $x^2+8x+15$.

**D2.** Factor $2x^2+5x-3$ (ac method).

**D3.** Factor $x^2-36$ (difference of squares).

**D4.** Factor $x^3-27$ (difference of cubes).

**D5.** Factor completely: $4x^3-16x$.

**D6.** Solve $x^2-7x+10=0$ by factoring.

**D7.** Solve $x^3-3x^2-4x+12=0$. Use $x=3$ as a first root.

**D8.** Factor $x^4-16$ as far as possible.

**D9.** Solve $2x^3-x^2-7x+6=0$. Test $x=1$.

**D10.** If $x=2$ and $x=-3$ are roots of $x^3+ax^2+bx-6=0$, find $a$ and $b$.

> Solutions: [Solutions](solutions/07A-solutions.md#basic-drill)

---

## Advanced Drills

**A1.** Factor $x^4+x^2+1$ as $(x^2+x+1)(x^2-x+1)$ by adding/subtracting $x^2$.

**A2.** Solve $x^4-4x^3+2x^2+4x+1=0$. Symmetric — divide by $x^2$.

**A3.** Find all roots of $x^3-3x^2-6x+8=0$ using rational root theorem.

**A4.** Prove $x^n-y^n$ is divisible by $x-y$ for all $n$.

**A5.** Solve $x^3-3x+1=0$ has a root in $(0,1)$. Use IVT, then approximate.

**A6.** Factor $x^4+4$ as $(x^2+2x+2)(x^2-2x+2)$. (Sophie Germain identity.)

**A7.** Find $a$ such that $x^3-3x^2+a=0$ has a double root. (A double root satisfies $f(x)=f'(x)=0$.)

**A8.** Solve $(x^2-x)^2-8(x^2-x)+12=0$. Substitute $t=x^2-x$.

**A9.** If $x+\frac{1}{x}=3$, find $x^3+\frac{1}{x^3}$ without solving for $x$.

**A10.** Find all complex roots of $x^4+x^3+x^2+x+1=0$. Multiply by $(x-1)$.

> Solutions: [Solutions](solutions/07A-solutions.md#advanced-drill)

---

## Today's Procedure

```
Step 1: Factor — GCF always first. Then ac-method or two-numbers.
         Recognize special patterns: a²−b², a²±2ab+b², a³±b³.
Step 2: If factoring stalls — quadratic formula + discriminant D.
         D>0 two real, D=0 one, D<0 complex. Both routes agree.
Step 3: For cubic+ equations — rational root candidates.
         Synthetic divide each root. Reduce degree until quadratic.
Step 4: Substitution t=x^k for hidden quadratics.
         Vieta (cubic and quartic) checks your answers.
```

---

## How to Read These Symbols

| Symbol | Reads as | Meaning |
|:---:|:---:|------|
| $x^n$ | "x to the n" / "x raised to the n-th power" | power / exponent form |
| $a x^2 + b x + c = 0$ | "a x squared plus b x plus c equals zero" | quadratic equation (standard form) |
| $x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$ | "x equals negative b plus or minus the square root of b squared minus 4 a c, all over 2 a" | quadratic formula |
| $b^2-4ac$ | "b squared minus 4 a c" / "discriminant" | determines nature of roots (>0: two real, =0: one real, <0: complex) |
| $(x-r)(x-s)=0$ | "x minus r times x minus s equals zero" | factored form — roots are r and s |
| $a^2-b^2$ | "a squared minus b squared" | difference of squares — factors as (a-b)(a+b) |
| $a^3 \pm b^3$ | "a cubed plus or minus b cubed" | sum/difference of cubes |
| $(x+a)^n$ | "x plus a, all to the n" | binomial expansion — use Pascal's triangle |
| $\pm$ | "plus or minus" | two possibilities: plus AND minus |
| synthetic division | "synthetic division" | fast polynomial division by (x-r) |
| $\sum r_i$ | "sum of r sub i" / "sum of roots" | Vieta: sum = -b/a |
| $\prod r_i$ | "product of r sub i" / "product of roots" | Vieta: product = (-1)^n a_0/a_n |

---

## Terminology

| What we called it | Math term | Notation |
|:---------------:|:---------:|:--------:|
| tear apart | factor | $ax^2+bx+c=(px+q)(rx+s)$ |
| pull out first | greatest common factor (GCF) | $3x(x-2)$ |
| two-numbers method | sum-and-product factoring | $(x+p)(x+q)$ |
| ac method | ac method for $a\neq1$ | split middle term |
| difference of squares | difference of squares | $a^2-b^2=(a-b)(a+b)$ |
| perfect square | perfect square trinomial | $a^2\pm2ab+b^2=(a\pm b)^2$ |
| sum/difference of cubes | sum/difference of cubes | $a^3\pm b^3$ |
| synthetic division | synthetic division | divide polynomial by $(x-r)$ |
| rational root candidates | Rational Root Theorem | $\pm p/q$ where $p\mid a_0$, $q\mid a_n$ |
| substitution | substitution | $t=x^k$ to lower degree |
| symmetric equation | palindromic/self-reciprocal | divide by $x^2$, use $u=x+1/x$ |
| root-coefficient link | Vieta's formulas | $\sum r_i=-a_{n-1}/a_n$, $\prod r_i=(-1)^n a_0/a_n$ |
