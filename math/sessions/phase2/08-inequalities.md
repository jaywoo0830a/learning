# Session 08: Slicing the Number Line — Mastering Inequalities

**Phase 2 — Classical Techniques | 45 min**

---

## Part A: Marking Ranges on the Number Line

---

## Example 1: Linear Inequalities — Only Careful When Dividing by Negatives

$3x + 5 > 2x - 1$.

① Gather $x$ terms on the left. Move $2x$ to the left → $3x - 2x + 5 > -1$.
② Gather numbers on the right. Move 5 to the right → $x > -6$.

$-2x < 6$.
① Divide both sides by −2.
② **Dividing by a negative flips the inequality sign.** → $x > -3$.

$-3 < 2x + 1 \leq 5$.
① Subtract 1 → $-4 < 2x \leq 4$.
② Divide by 2 → $-2 < x \leq 2$.

Draw on the number line: empty circle at −2, filled circle at 2, shade between them.

---

## Example 2: Quadratic Inequalities — Tear, Split into Intervals, Check Signs

$x^2 - 5x + 6 > 0$.

① Tear first: $(x-2)(x-3) > 0$.
② Find the points where it hits 0: $x=2$, $x=3$.
③ These two points split the number line into three pieces.

④ Pick one number from each interval and check the sign.
- $x < 2$: plug in $x=0$ → $(−2)(−3) = 6 > 0$. ✅
- $2 < x < 3$: plug in $x=2.5$ → $(0.5)(−0.5) = -0.25 < 0$. ❌
- $x > 3$: plug in $x=4$ → $(2)(1) = 2 > 0$. ✅

→ **$x < 2$ or $x > 3$.**

---

## Example 3: Negative Leading Coefficient — Flip to Positive First

$-x^2 + 4x - 3 \geq 0$.

① Multiply by −1 and flip the inequality → $x^2 - 4x + 3 \leq 0$.
② Tear: $(x-1)(x-3) \leq 0$.

③ Zero points: $x=1$, $x=3$. Three intervals.
- $x < 1$: $(−)(−) = +$. ❌
- $1 < x < 3$: $(+)(−) = −$. ✅
- $x > 3$: $(+)(+) = +$. ❌

④ The boundaries $x=1$, $x=3$ give 0, so include them. → **$1 \leq x \leq 3$.**

---

## Example 4: Just Looking at the Discriminant

$x^2 + x + 1 > 0$.

① Try tearing: no two integers add to 1 and multiply to 1.
② Discriminant: $1^2 - 4 \times 1 \times 1 = -3 < 0$.
③ $x^2$ coefficient positive, discriminant negative → the parabola sits entirely above the $x$-axis.
→ **True for all $x$. Always true.**

$x^2 + 2x + 1 \leq 0$.
① $(x+1)^2 \leq 0$.
② A square can't be less than 0. Only the point where it equals 0 works.
→ **True only at $x = -1$. Exactly one point.**

---

## Part B: Rational, Higher-Degree, and Absolute Value Inequalities

---

## Example 5: Rational Inequalities — Never Recklessly Multiply by the Denominator

$\frac{x-1}{x+2} > 0$.

① Find the points where the sign can flip.
Numerator = 0 → $x = 1$. Denominator = 0 → $x = -2$.
These two points split the number line into three. $x=-2$ is excluded (denominator 0).

② Pick one number from each interval and check the sign.
- $x < -2$: $x=-3$ → $(−4)/(−1) = 4 > 0$. ✅
- $-2 < x < 1$: $x=0$ → $(−1)/(2) = -0.5 < 0$. ❌
- $x > 1$: $x=2$ → $(1)/(4) = 0.25 > 0$. ✅

→ **$x < -2$ or $x > 1$.**

---

## Example 6: When the Right Side Isn't 0 — Move Everything and Combine

$\frac{2}{x-1} \geq 1$.

① Move the 1 on the right to the left → $\frac{2}{x-1} - 1 \geq 0$.
② Combine into one fraction: $\frac{2 - (x-1)}{x-1} = \frac{3-x}{x-1} \geq 0$.

③ Numerator 0: $x=3$. Denominator 0: $x=1$ (excluded).
- $x < 1$: $(+)/(−) = −$. ❌
- $1 < x \leq 3$: $(+)/(+) = +$. ✅ ($x=3$ included)
- $x > 3$: $(−)/(+) = −$. ❌

→ **$1 < x \leq 3$.**

---

## Example 7: Higher-Degree Inequalities — Tear and Mark Every Root

$x^3 - 3x^2 - 4x + 12 \geq 0$.

① Try plugging in $x=2$: $8 - 12 - 8 + 12 = 0$. Exactly 0.
② Pull out $(x-2)$ using synthetic division.
Quotient $x^2 - x - 6 = (x-3)(x+2)$.
→ $(x-2)(x-3)(x+2) \geq 0$.

③ Zero points: $x = -2, 2, 3$. Four intervals.
- $x < -2$: $(−)(−)(−) = −$. ❌
- $-2 < x < 2$: $(−)(−)(+) = +$. ✅
- $2 < x < 3$: $(+)(−)(+) = −$. ❌
- $x > 3$: $(+)(+)(+) = +$. ✅

→ **$-2 \leq x \leq 2$ or $x \geq 3$.**

---

## Example 8: $(x-a)^n$ — Even Powers Don't Flip the Sign

$(x-1)^2 (x+2) < 0$.

① Zero points: $x=1$ (twice — even), $x=-2$ (once — odd).
② Even powers don't change sign when crossing. Only odd powers do.

③ Intervals:
- $x < -2$: $(+)^2(−) = −$. ✅
- $-2 < x < 1$: $(+)^2(+) = +$. ❌
- $x > 1$: $(+)^2(+) = +$. ❌

→ **$x < -2$.**

---

## Example 9: Single Absolute Value — Distance from the Zero Point

$|x-3| < 5$.

① An absolute value inequality is "distance left and right from the zero point."
$-5 < x-3 < 5$.
② Add 3 → **$-2 < x < 8$.**

$|2x+1| \geq 3$.
① Outside the zero point in both directions:
$2x+1 \leq -3$ or $2x+1 \geq 3$.
② $2x \leq -4$ → $x \leq -2$. Or $2x \geq 2$ → $x \geq 1$.

→ **$x \leq -2$ or $x \geq 1$.**

---

## Example 10: Two Absolute Values — Split into Intervals and Handle One by One

$|x-1| + |x+2| \leq 5$.

① Find where each absolute value's inside hits 0: $x=1$, $x=-2$.
② Split the whole line into three using these points.

**Interval 1: $x < -2$**
Both insides are negative → flip signs to strip the absolute bars.
$-(x-1) - (x+2) = -2x - 1 \leq 5$.
$-2x \leq 6$ → $x \geq -3$.
Intersect with the interval → $-3 \leq x < -2$.

**Interval 2: $-2 \leq x < 1$**
$(x-1)$ negative, $(x+2)$ positive.
$-(x-1) + (x+2) = 3 \leq 5$. Always true.
→ The whole interval is an answer: $-2 \leq x < 1$.

**Interval 3: $x \geq 1$**
Both positive → just strip the bars.
$(x-1) + (x+2) = 2x+1 \leq 5$.
$2x \leq 4$ → $x \leq 2$.
Intersect with the interval → $1 \leq x \leq 2$.

③ Combine all three → **$-3 \leq x \leq 2$.**

---

## Part C: Exponential and Logarithmic Inequalities

---

## Example 11: Exponential Inequalities — The Inequality Direction Depends on the Base

$2^{x+1} > 8$.

① Write 8 as a power of base 2: $8 = 2^3$.
② $2^{x+1} > 2^3$. Base 2 > 1 → keep the inequality as is: $x+1 > 3$ → $x > 2$.

$\left(\frac{1}{2}\right)^{x+1} \geq \frac{1}{4}$.

① $\frac{1}{4} = \left(\frac{1}{2}\right)^2$.
② Base $\frac{1}{2} < 1$ → **flip the inequality:** $x+1 \leq 2$ → $x \leq 1$.

---

## Example 12: Logarithmic Inequalities — Check the Argument First

$\log_2 (x-1) < 3$.

① Write 3 as a base-2 log: $3 = \log_2 8$.
② $\log_2 (x-1) < \log_2 8$. Base 2 > 1 → $x-1 < 8$ → $x < 9$.
③ **Argument condition**: $x-1 > 0$ → $x > 1$.

→ **$1 < x < 9$.**

$\log_{\frac{1}{2}} (x+2) \geq 1$.

① $1 = \log_{\frac{1}{2}} \frac{1}{2}$.
② Base $\frac{1}{2} < 1$ → flip: $x+2 \leq \frac{1}{2}$ → $x \leq -\frac{3}{2}$.
③ Argument condition: $x+2 > 0$ → $x > -2$.

→ **$-2 < x \leq -\frac{3}{2}$.**

---

## Part D: Inequalities Crossing Integer Boundaries

---

## Example 13: First, Get the Meaning of $[x]$ Down

$[x]$ is the greatest integer that does not exceed $x$.

Let's pin down some values:
$[3.7] = 3$, $[3.0] = 3$, $[0.5] = 0$.
$[-1.2] = -2$, $[-1.0] = -1$, $[5] = 5$.

Now trace the pattern we just saw. $[3.7]=3$ means $3 \leq 3.7 < 4$.
$[0.5]=0$ means $0 \leq 0.5 < 1$. $[-1.2]=-2$ means $-2 \leq -1.2 < -1$.
So $[x]=3$ means → $3 \leq x < 4$.
$[2x] = 5$ → $5 \leq 2x < 6$ → $2.5 \leq x < 3$.

---

## Example 14: Inequalities Containing $[x]$ — Replace with $t$

$[x]^2 - [x] - 6 < 0$.

① Replace $[x]$ with $t$: $t^2 - t - 6 < 0$.
② Tear: $(t-3)(t+2) < 0$ → $-2 < t < 3$.
③ $t = [x]$ is an integer. → $t = -1, 0, 1, 2$.

④ Convert each $t$ value to an $x$ interval:
$[x] = -1$ → $-1 \leq x < 0$.
$[x] = 0$ → $0 \leq x < 1$.
$[x] = 1$ → $1 \leq x < 2$.
$[x] = 2$ → $2 \leq x < 3$.

→ **$-1 \leq x < 3$.**

---

## Example 15: $[x+1] > [x]$ — Always True?

$[x+1] > [x]$.

When $x$ is an integer $n$: $[n+1] = n+1$, $[n] = n$ → $n+1 > n$. True.
When $x$ is not an integer, $x = n + \delta$: $[x+1] = n+1$, $[x] = n$ → $n+1 > n$. True.

→ **True for all $x$.** Reason: $[x+1] = [x] + 1$ always holds.

---

## Example 16: Ceiling Function and Fractional Part

$\lceil x \rceil$: the smallest integer that is not less than $x$.
$\lceil 3.2 \rceil = 4$, $\lceil -1.2 \rceil = -1$.

$\{x\} = x - [x]$: the fractional part of $x$. Always $0 \leq \{x\} < 1$.
$\{3.7\} = 0.7$, $\{-1.2\} = 0.8$.

**Usage**:
$\lceil x \rceil = [x]$ → when $x$ is an integer.
$\lceil x \rceil = [x] + 1$ → when $x$ is not an integer.

$\{x\} > 0.5$ → for every integer $n$, the interval $n + 0.5 < x < n+1$.

---

## Common Mistakes

### Mistake 1: Recklessly Multiplying Both Sides of a Rational Inequality by the Denominator

**Wrong path**: "$\frac{x-1}{x+2} > 0$ so multiply by $x+2$ and get $x-1 > 0$."

**Why it's wrong**: You don't know whether $x+2$ is positive or negative. The inequality direction is unknown.

**Right path**: Split into intervals using the points where numerator and denominator each equal 0. Never multiply by the denominator.

---

### Mistake 2: Forgetting the Argument Condition in Logarithmic Inequalities

**Wrong path**: "$\log_2(x-1) < 3$ → $x < 9$."

**Why it's wrong**: A logarithm's argument must be strictly positive. $x-1 > 0$ → $x > 1$.

**Right path**: Solve the inequality, then **always intersect with argument > 0.**

---

### Mistake 3: Writing $[x] \geq 2$ as $x \geq 2$ — Coincidentally Right, but Dangerous

**Wrong path**: "$[x] \geq 2$ so $x \geq 2$." — in this case it happens to be right, but...

**Why it's dangerous**: $[x] > 2$ actually means $x \geq 3$. Because $[x] = 2$ covers $2 \leq x < 3$.
You must check the equals sign at integer boundaries every time.

**Right path**: Always start from $[x] = n \leftrightarrow n \leq x < n+1$.

---

### Mistake 4: Thinking the Sign Flips When Crossing an Even-Power Factor

**Wrong path**: "In $(x-1)^2(x+2)$, the sign flips at $x=1$ too."

**Why it's wrong**: $(x-1)^2$ is 0 at $x=1$, but because it's squared, its sign is always positive.
On both sides of $x=1$, $(x-1)^2 > 0$. No sign change.

**Right path**: $(x-a)^{\text{even}}$ → sign unchanged. Only $(x-a)^{\text{odd}}$ flips the sign.

---

## What We Just Did

```
① Make the right side 0. Tear the left side completely.
② Mark every zero point on the number line. Always exclude denominator=0.
③ Pick one number in each interval and judge the sign of the torn expression.
④ Remember: even-power factors don't flip the sign.
⑤ Exponentials/logs: base>1 → keep inequality, 0<base<1 → flip.
   For logs, always intersect with argument>0.
⑥ Absolute values: split into intervals at the zero points, strip bars one by one.
⑦ [x]: substitute t=[x] first. Remember t is an integer.
```

---

## Exercise 1

$\frac{x^2 - 4}{x+3} \leq 0$. Tear the numerator, mark denominator ≠ 0, split into intervals, judge signs.

→ Follow: **Example 5**

> Solutions: [Solution Set](solutions/08-solutions.md#exercise-1)

---

## Exercise 2

$2^x + 2^{x+1} > 48$. Start by pulling out $2^x$.

→ Follow: **Example 11**

> Solutions: [Solution Set](solutions/08-solutions.md#exercise-2)

---

## Exercise 3

$\log_2 (x^2 - 3x) \leq 2$. Make sure to intersect with the argument > 0 condition.

→ Follow: **Example 12**

> Solutions: [Solution Set](solutions/08-solutions.md#exercise-3)

---

## Exercise 4: Constructive

Find the range of $x$ that satisfies $[x]^2 - 5[x] + 6 = 0$.
Then make your own quadratic equation in $[x]$ of the same form and solve it.

→ Follow: **Example 14**

> Solutions: [Solution Set](solutions/08-solutions.md#exercise-4)

---

## Exercise 5

$|x-2| + |x+3| \leq 7$. Split into three intervals at the zero points.

→ Follow: **Example 10**

> Solutions: [Solution Set](solutions/08-solutions.md#exercise-5)

---

## Exercise 6: Challenge

Solve $\{x\} + [x]^2 \leq x$ for $0 \leq x < 3$.
Substituting $\{x\}=x-[x]$ gives a simple form.

→ Follow: **Examples 14, 16**

> Solutions: [Solution Set](solutions/08-solutions.md#exercise-6)

---

## Today's Procedure

```
Step 1: Make the right side 0. Tear the left side completely.
Step 2: Mark every zero point on the number line. Exclude denominator=0.
       (Watch for even-power factors — sign doesn't flip there.)
Step 3: Pick one number per interval and check the sign.
       - Rational: check numerator and denominator signs separately
       - Exponential/log: base>1 keep, 0<base<1 flip. Logs: intersect with argument>0
       - n absolute values: split at zero points, handle one interval at a time
       - [x]: substitute t=[x]; t is an integer
```

---

## Terminology

Up to now, we've only used simple words: "tear", "move", "mark on the number line", "check the sign", "split".
**You already know the methods.** Now we give them their math names.

| What we've been calling it | Math Term | Symbol / Explanation |
|:--------------------------:|:---------:|:---:|
| the inequality sign flips | inequality direction reversal | when multiplying by a negative or base<1 |
| point where it hits 0 | critical point | critical point |
| splitting into intervals | interval method | interval method |
| checking only the sign of the torn expression | sign chart | sign chart |
| discriminant | discriminant | $D = b^2 - 4ac$ |
| argument | argument | the expression inside a logarithm |
| base | base | base |
| floor function | floor function (Gauss notation) | $\lfloor x \rfloor = [x]$ |
| ceiling function | ceiling function | $\lceil x \rceil$ |
| fractional part | fractional part | $\{x\} = x - [x]$ |
| absolute value | absolute value | $\lvert x \rvert$ |
