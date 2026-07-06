# 07 Solutions — Tearing, Bundling, and Solving

---

## Exercise 1

> Tear $2x^3 + 3x^2 - 8x + 3$ completely.

① Divisors of the constant 3: $\pm 1, \pm 3$. Rational root candidates (leading coeff 2): $\pm 1, \pm 3, \pm \frac{1}{2}, \pm \frac{3}{2}$.

② Plug in starting from the smallest.
$x=1$: $2+3-8+3=0$. **Exactly 0!** → $(x-1)$ is a factor.

③ Synthetic division. Coefficients [2, 3, −8, 3], divide by 1.

```
   │  2   3   -8   3
 1 │      2    5  -3
───┼────────────────
   │  2   5   -3   0
```

Quotient: $2x^2 + 5x - 3$.

④ Tear the quotient. $ac = 2 \times (-3) = -6$. Add to 5, multiply to −6 → 6, −1.
$2x^2 + 6x - x - 3 = 2x(x+3) - 1(x+3) = (2x-1)(x+3)$.

→ **$(x-1)(2x-1)(x+3)$.**

---

## Exercise 2

> Tear $x^4 - 16$ until nothing more can tear.

① Difference of squares: $(x^2)^2 - 4^2 = (x^2-4)(x^2+4)$.
② Tear $x^2-4$ again with difference of squares: $x^2 - 2^2 = (x-2)(x+2)$.
③ $x^2+4$ can't tear further over the reals. $D = -16 < 0$.

→ **$(x-2)(x+2)(x^2+4)$.** Used difference of squares twice.

---

## Exercise 3

> Tear $\frac{4x^2 + 3x + 2}{x^3 + 2x^2 + x}$ into partial fractions.

① Tear the denominator: $x^3 + 2x^2 + x = x(x^2 + 2x + 1) = x(x+1)^2$.

② Partial fraction setup: $\frac{4x^2+3x+2}{x(x+1)^2} = \frac{A}{x} + \frac{B}{x+1} + \frac{C}{(x+1)^2}$.

③ Multiply both sides by $x(x+1)^2$:
$4x^2+3x+2 = A(x+1)^2 + Bx(x+1) + Cx$.

④ Plug in values to find them one by one.
$x=0$: $2 = A \cdot 1 + 0 + 0$ → $A = 2$.
$x=-1$: $4-3+2 = 0 + 0 + C(-1)$ → $3 = -C$ → $C = -3$.

⑤ Plug $A$ and $C$ in, then substitute $x=1$: $4+3+2 = 9$.
Right side: $2(4) + B(1)(2) + (-3)(1) = 8 + 2B - 3 = 5 + 2B$.
$9 = 5 + 2B$ → $B = 2$.

→ **$\frac{2}{x} + \frac{2}{x+1} - \frac{3}{(x+1)^2}$.**

---

## Exercise 4: Constructive

> Make 3 quadratic expressions that can be torn using two numbers that add to 7 and multiply to 12.

Add to 7, multiply to 12 → the two numbers are 3 and 4.

**Leading coefficient 1**: $x^2 + 7x + 12 = (x+3)(x+4)$.

**Leading coefficient 2**: Form $2x^2 + 7x + \square$.
$ac$ method: $2 \times \square = 2\square$. Two numbers adding to 7 and multiplying to $2\square$ are 3 and 4.
3 and 4 multiply to 12. $2\square = 12$ → $\square = 6$.
→ $2x^2 + 7x + 6$. Check: $2x^2+3x+4x+6 = x(2x+3)+2(2x+3) = (x+2)(2x+3)$.

**Leading coefficient 3**: $3x^2 + 7x + \square$. $3\square = 12$ → $\square = 4$.
→ $3x^2 + 7x + 4$. Check: $3x^2+3x+4x+4 = 3x(x+1)+4(x+1) = (3x+4)(x+1)$.

→ Answer: **$x^2+7x+12$, $2x^2+7x+6$, $3x^2+7x+4$** (infinitely many possible).

---

## Exercise 5

> Find all roots of $x^4 - 2x^3 - 13x^2 - 2x + 1 = 0$.

① Coefficients: 1, −2, −13, −2, 1. Symmetric. Verify $x=0$ is not a root.

② Divide by $x^2$: $x^2 - 2x - 13 - \frac{2}{x} + \frac{1}{x^2} = 0$.

③ Substitute $t = x + \frac{1}{x}$.
$x^2 + \frac{1}{x^2} = t^2 - 2$.

④ Clean up: $(t^2 - 2) - 2t - 13 = 0$ → $t^2 - 2t - 15 = 0$.
$(t-5)(t+3) = 0$. → $t = 5$ or $t = -3$.

⑤ $t = 5$: $x + \frac{1}{x} = 5$ → $x^2 - 5x + 1 = 0$ → $x = \frac{5 \pm \sqrt{21}}{2}$.

⑥ $t = -3$: $x + \frac{1}{x} = -3$ → $x^2 + 3x + 1 = 0$ → $x = \frac{-3 \pm \sqrt{5}}{2}$.

→ **Four roots: $\frac{5 \pm \sqrt{21}}{2}$, $\frac{-3 \pm \sqrt{5}}{2}$.**

---

## Exercise 6: Challenge

> The three roots of $x^3 - 3x^2 + ax + b = 0$ are $1, r, r^2$. Find $a$, $b$, and $r$.

① Apply Vieta's formulas ($a_3=1, a_2=-3, a_1=a, a_0=b$):
- Sum: $1 + r + r^2 = -(-3) = 3$ → $r^2 + r + 1 = 3$ → $r^2 + r - 2 = 0$.
- Sum of pairwise products: $1 \cdot r + r \cdot r^2 + r^2 \cdot 1 = a$ → $r + r^3 + r^2 = a$.
- Triple product: $1 \cdot r \cdot r^2 = -b$ → $r^3 = -b$.

② $r^2 + r - 2 = 0$ → $(r+2)(r-1) = 0$ → $r = -2$ or $r = 1$.

③ If $r = 1$, the three roots are 1, 1, 1. The polynomial is $(x-1)^3 = x^3 - 3x^2 + 3x - 1$.
→ $a = 3$, $b = -1$.

④ If $r = -2$, the three roots are 1, −2, 4.
Sum: $1 + (-2) + 4 = 3$ ✓.
Sum of pairwise products: $1(-2) + (-2)(4) + 4(1) = -2 - 8 + 4 = -6$ → $a = -6$.
Triple product: $1 \cdot (-2) \cdot 4 = -8$ → $-b = -8$ → $b = 8$.

→ **$(a, b, r) = (3, -1, 1)$ or $(-6, 8, -2)$.**

---

[Back to Index](../07-polynomials-and-equations.md)
