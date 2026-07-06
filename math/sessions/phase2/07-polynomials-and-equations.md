# Session 07: Tearing, Bundling, and Solving — Every Algebraic Trick

**Phase 2 — Classical Techniques | 60 min**

---

## Part A: Tearing Expressions into Multiplication Form

---

## Example 1: Find Two Numbers and Tear

Look at this expression: $x^2 + 7x + 12$.

① Think of two numbers that add to 7 and multiply to 12. → 3 and 4.
② Tear the expression using those two numbers. → $(x+3)(x+4)$.

Check by hand: spread out $(x+3)(x+4)$.
$x \cdot x = x^2$. $x \cdot 4 = 4x$. $3 \cdot x = 3x$. $3 \cdot 4 = 12$.
Gather: $x^2 + 7x + 12$. Matches exactly.

Add to 7, multiply to −18 → −2, 9. Tear into $(x-2)(x+9)$.
Add to −5, multiply to 6 → −2, −3. Tear into $(x-2)(x-3)$.

---

## Example 2: When the Leading Coefficient Isn't 1 — the ac Method

$2x^2 + 7x + 3$.

① Multiply the leading coefficient 2 and the constant 3. → $2 \times 3 = 6$.
② Find two numbers that add to 7 and multiply to 6. → 6 and 1.
③ Tear the middle $7x$ into $6x + 1x$. → $2x^2 + 6x + x + 3$.
④ Bundle the first two terms. → $2x(x+3)$.
⑤ Bundle the last two terms. → $1(x+3)$.
⑥ Pull out the common $(x+3)$. → $(2x+1)(x+3)$.

Another one: $6x^2 + 5x - 6$.
① $6 \times (-6) = -36$.
② Add to 5, multiply to −36 → 9, −4.
③ Tear: $6x^2 + 9x - 4x - 6$.
④ Bundle: $3x(2x+3) - 2(2x+3)$.
⑤ Pull out: $(3x-2)(2x+3)$.

---

## Example 3: Perfect Square — Fold into One

$x^2 + 6x + 9$.
First term is $x$ squared. Last term is 3 squared.
The middle $6x$ is $2 \times x \times 3$. → Fold into $(x+3)^2$.

$x^2 - 10x + 25$. $x$ squared, 5 squared, middle $2 \cdot x \cdot (-5) = -10x$.
→ Fold into $(x-5)^2$.

$4x^2 + 12x + 9$. $(2x)^2$, $3^2$, middle $2 \cdot 2x \cdot 3 = 12x$.
→ Fold into $(2x+3)^2$.

$x^2 + 6x + 10$. $x^2$, $(\sqrt{10})^2$, middle $2 \cdot x \cdot \sqrt{10} \neq 6x$.
→ Won't fold. Leave it as is.

---

## Example 4: Square Minus Square — Tear into Sum-and-Difference

$x^2 - 9$. $x$ squared minus 3 squared.
→ $(x-3)(x+3)$.

$4x^2 - 25$. $(2x)^2 - 5^2$.
→ $(2x-5)(2x+5)$.

$x^4 - 16$. $(x^2)^2 - 4^2$ → $(x^2-4)(x^2+4)$.
Tear $x^2-4$ further: $(x-2)(x+2)$.
→ Final: $(x-2)(x+2)(x^2+4)$. $x^2+4$ can't be torn further.

---

## Example 5: Sum and Difference of Cubes — One Shot

$x^3 - 8$. $x$ cubed minus 2 cubed.
→ $(x-2)(x^2 + 2x + 4)$. The second bracket won't tear further.

$x^3 + 27$. $x^3 + 3^3$.
→ $(x+3)(x^2 - 3x + 9)$.

$8x^3 - 1$. $(2x)^3 - 1^3$.
→ $(2x-1)(4x^2 + 2x + 1)$.

---

## Example 6: Common Factor — Always Pull Out First

$3x^3 - 12x$.
① Pull out the $3x$ that lives in every term. → $3x(x^2 - 4)$.
② Tear inside the parentheses. $x^2-4 = (x-2)(x+2)$.
→ $3x(x-2)(x+2)$.

$2x^4 - 32$.
① Pull out 2. → $2(x^4 - 16)$.
② Tear inside using difference of squares: $(x^2-4)(x^2+4)$.
③ Tear $x^2-4$ further: $(x-2)(x+2)$.
→ $2(x-2)(x+2)(x^2+4)$.

---

## Part B: Degree 3 and Beyond — Dividing With Coefficients Only

---

## Example 7: Synthetic Division — Divide Using Only Coefficients

$x^3 - 6x^2 + 11x - 6$.

① List the divisors of the constant −6: $\pm 1, \pm 2, \pm 3, \pm 6$.
② Plug them in one by one, starting small.
Plug in $x=1$: $1 - 6 + 11 - 6 = 0$. **Exactly 0!** → $(x-1)$ is a factor.

③ Draw a table with coefficients [1, −6, 11, −6].

```
   │  1  -6   11  -6
 1 │      1   -5    6
───┼─────────────────
   │  1  -5    6    0  ← remainder 0!
```

Follow with your hand:
- Bring down the first 1 as is.
- Multiply the 1 you brought down by 1 → 1. Write it under −6. −6 + 1 = −5.
- Multiply −5 by 1 → −5. Write it under 11. $11 + (-5) = 6$.
- Multiply 6 by 1 → 6. Write it under −6. $-6 + 6 = 0$.

④ The numbers brought down [1, −5, 6] are the quotient: $x^2 - 5x + 6$.
⑤ Tear this again: $(x-2)(x-3)$.
→ Final: $(x-1)(x-2)(x-3)$.

---

## Example 8: Rational Roots — Fractions Are Candidates Too

$2x^3 - 3x^2 - 3x + 2$.

① Candidates = $\frac{\text{divisors of constant}}{\text{divisors of leading coefficient}}$: $\pm 1, \pm 2, \pm \frac{1}{2}$.
② Plug in $x=1$: $2-3-3+2 = -2$. Nope.
③ Plug in $x=-1$: $-2-3+3+2 = 0$. **Exactly 0!** → $(x+1)$ is a factor.

④ Divide using synthetic division. Quotient: $2x^2 - 5x + 2$.
⑤ Tear again: $(2x-1)(x-2)$.

→ Roots: $x = -1$, $x = \frac{1}{2}$, $x = 2$.

---

## Example 9: Substitute $t$ to Lower the Degree

$x^4 - 5x^2 + 4$.

① Replace $x^2$ with $t$. → $t^2 - 5t + 4$.
② Tear: $(t-1)(t-4)$.
③ Return $t$ to $x^2$: $(x^2-1)(x^2-4)$.
④ Tear each using difference of squares: $(x-1)(x+1)(x-2)(x+2)$.

$x^6 - 9x^3 + 8$.
① Replace $x^3$ with $t$. → $t^2 - 9t + 8$.
② $(t-1)(t-8)$.
③ Return: $(x^3-1)(x^3-8)$.
④ Cube formulas: $(x-1)(x^2+x+1)(x-2)(x^2+2x+4)$.

---

## Example 10: Symmetric Coefficients — Divide by $x^2$

$x^4 + x^3 - 4x^2 + x + 1 = 0$.

① Look at the coefficients: 1, 1, −4, 1, 1. Symmetric around the center.
② $x=0$ is not a root. Divide both sides by $x^2$.

$x^2 + x - 4 + \frac{1}{x} + \frac{1}{x^2} = 0$.

③ Replace $x + \frac{1}{x}$ with $t$.
$x^2 + \frac{1}{x^2} = (x + \frac{1}{x})^2 - 2 = t^2 - 2$.

④ Clean up: $(t^2 - 2) + t - 4 = 0$ → $t^2 + t - 6 = 0$.
⑤ Tear: $(t+3)(t-2) = 0$. → $t = -3$ or $t = 2$.

⑥ $t = -3$: $x + \frac{1}{x} = -3$ → $x^2 + 3x + 1 = 0$ → $x = \frac{-3 \pm \sqrt{5}}{2}$.
⑦ $t = 2$: $x + \frac{1}{x} = 2$ → $(x-1)^2 = 0$ → $x = 1$ (double root, appears twice).

---

## Example 11: Roots and Coefficients — Vieta

Let the two roots of $x^2 + px + q = 0$ be $r_1, r_2$.

Sum: $r_1 + r_2 = -p$. Product: $r_1 r_2 = q$.

Check by hand: $x^2 - 5x + 6 = 0$ → sum 5, product 6 → roots are 2, 3.

If one root is $2 + \sqrt{3}$ and the sum is 4, the other root is $2 - \sqrt{3}$. Because the sum is 4.

For a cubic $x^3 + ax^2 + bx + c = 0$ with roots $r_1, r_2, r_3$:
- $r_1 + r_2 + r_3 = -a$.
- $r_1 r_2 + r_2 r_3 + r_3 r_1 = b$.
- $r_1 r_2 r_3 = -c$.

---

## Part C: Tearing Fractions into Pieces

---

## Example 12: Distinct Linear Factors

$\frac{5x-1}{x^2 - x - 2}$.

① Tear the denominator first: $(x-2)(x+1)$.
② Assume the form $\frac{5x-1}{(x-2)(x+1)} = \frac{A}{x-2} + \frac{B}{x+1}$.
③ Multiply both sides by $(x-2)(x+1)$: $5x-1 = A(x+1) + B(x-2)$.

④ Plug in $x=2$. $B$ vanishes → $9 = 3A$ → $A = 3$.
⑤ Plug in $x=-1$. $A$ vanishes → $-6 = -3B$ → $B = 2$.

→ $\frac{3}{x-2} + \frac{2}{x+1}$.

---

## Example 13: When the Denominator Has a Square

$\frac{2x+1}{(x-1)^2} = \frac{A}{x-1} + \frac{B}{(x-1)^2}$.

① Multiply both sides by $(x-1)^2$: $2x+1 = A(x-1) + B$.
② Plug in $x=1$: $3 = B$.
③ Plug in $x=0$: $1 = -A + 3$ → $A = 2$.

→ $\frac{2}{x-1} + \frac{3}{(x-1)^2}$.

---

## Example 14: When the Numerator Has Higher Degree

$\frac{x^2}{x-1}$.

① Numerator degree (2) is bigger than denominator (1). **Divide first.**
② $x^2 \div (x-1) = x + 1 + \frac{1}{x-1}$.
③ The remainder $\frac{1}{x-1}$ is already fully torn.

→ $x + 1 + \frac{1}{x-1}$.

---

## Common Mistakes

### Mistake 1: Getting the Sign Wrong in Synthetic Division Factors

**Wrong path**: "I plugged in $x=-1$ and got remainder 0. The factor is $(x-1)$."

**Why it's wrong**: If it hits 0 at $x=-1$, the factor is $x - (-1) = x+1$.
You must flip the sign of the value you plugged in to get the constant term of the factor.

**Right path**: If it hits 0 at $x=r$, the factor is $(x-r)$.

---

### Mistake 2: Jumping to Partial Fractions Without Checking the Degree

**Wrong path**: "$\frac{x^2}{x-1}$ can be set up as $\frac{A}{x-1}$."

**Why it's wrong**: If the numerator degree is bigger, it's an improper fraction. Divide first!

**Right path**: Divide, then tear only the remainder into partial fractions.

---

### Mistake 3: Counting a Double Root Only Once

**Wrong path**: "$(x-1)^2 = 0$ → $x=1$."

**Why it's wrong**: $(x-1)^2=0$ means $x=1$ appears twice. It's a double root.

**Right path**: Write "$x=1$ (double root, twice)."

---

### Mistake 4: Trying to Tear Without Pulling Out the Common Factor First

**Wrong path**: "I'll tear $3x^3 - 12x$ using difference of squares right away."

**Why it's wrong**: $3x$ lives in every term. You must pull it out first.

**Right path**: Always pull out the common factor before anything else.

---

## What We Just Did

```
① Pull out the common factor first. (If you skip this, you hit a dead end.)
② Pick the right tearing tool for the degree:
   - Degree 2 → find-two-numbers / ac method / perfect square / difference of squares
   - Degree 3 → sum/difference of cubes / synthetic division (rational root theorem)
   - Degree 4+ → substitute t=x² / if symmetric, divide by x² and substitute t=x+1/x
③ Check every torn piece to see if it can tear further.
④ For partial fractions: tear the denominator, set up A,B,C, and erase them one by one.
```

---

## Exercise 1

Tear $2x^3 + 3x^2 - 8x + 3$ completely. (Constant divisors ±1, ±3; fractions too.)

→ Follow: **Examples 7, 8, 1, 2**

> Solutions: [Solution Set](solutions/07-solutions.md#exercise-1)

---

## Exercise 2

Tear $x^4 - 16$ until nothing left can tear. (How many difference-of-squares steps?)

→ Follow: **Example 4**

> Solutions: [Solution Set](solutions/07-solutions.md#exercise-2)

---

## Exercise 3

Tear $\frac{4x^2 + 3x + 2}{x^3 + 2x^2 + x}$ into partial fractions. (Tear the denominator first!)

→ Follow: **Examples 12, 13**

> Solutions: [Solution Set](solutions/07-solutions.md#exercise-3)

---

## Exercise 4: Constructive

Make 3 quadratic expressions that can be torn using two numbers that add to 7 and multiply to 12.
One with leading coefficient 1, and two with leading coefficient not 1.

→ Follow: **Examples 1, 2**

> Solutions: [Solution Set](solutions/07-solutions.md#exercise-4)

---

## Exercise 5

Find all roots of $x^4 - 2x^3 - 13x^2 - 2x + 1 = 0$. (Symmetric coefficients → divide by $x^2$.)

→ Follow: **Example 10**

> Solutions: [Solution Set](solutions/07-solutions.md#exercise-5)

---

## Exercise 6: Challenge

The three roots of $x^3 - 3x^2 + ax + b = 0$ are 1, $r$, and $r^2$. Find $a$, $b$, and $r$.
Vieta: sum = 3, sum of pairwise products = $a$, triple product = $-b$.

→ Follow: **Example 11**

> Solutions: [Solution Set](solutions/07-solutions.md#exercise-6)

---

## Today's Procedure

```
Step 1: Pull out the common factor. If there is none, go to Step 2.
Step 2: Pick the tool for the degree.
       - Degree 2: find-two-numbers / ac method / perfect square / difference of squares
       - Degree 3: sum/difference of cubes / synthetic division (rational root theorem)
       - Degree 4+: substitute t=x² / symmetric→divide by x², substitute t=x+1/x
       - Fractions: tear denominator, set up A,B,C, erase one by one
Step 3: Check every torn piece — can it tear further?
```

---

## Terminology

Up to now, we've only used simple words: "tear", "pull out", "bundle", "fold", "push in".
**You already know the methods.** Now we give them their math names.

| What we've been calling it | Math Term | Symbol / Explanation |
|:--------------------------:|:---------:|:---:|
| tear | factoring / factorization | factor |
| spread out | expand | expand |
| pull out the common factor | factor out the common factor | factor out |
| fold into a square | perfect square trinomial | $(a \pm b)^2 = a^2 \pm 2ab + b^2$ |
| square minus square | difference of squares | $a^2 - b^2 = (a-b)(a+b)$ |
| sum/difference of cubes | sum/difference of cubes | $a^3 \pm b^3 = (a \pm b)(a^2 \mp ab + b^2)$ |
| divide with coefficients only | synthetic division | divide by $(x-r)$ using coefficients only |
| roots and coefficients | Vieta's formulas | Vieta's formulas |
| symmetric coefficients | reciprocal equation | reciprocal equation |
| tear fractions | partial fraction decomposition | partial fraction |
| stacked root | multiple root | multiple root |
