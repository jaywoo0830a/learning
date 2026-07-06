# 08 Solutions — Slicing the Number Line

---

## Exercise 1

> $\frac{x^2 - 4}{x+3} \leq 0$. Tear the numerator, mark denominator ≠ 0, split into intervals, judge signs.

① Tear the numerator: $x^2-4 = (x-2)(x+2)$.
$\frac{(x-2)(x+2)}{x+3} \leq 0$.

② Zero points: numerator → $x=2$, $x=-2$. Denominator → $x=-3$ (excluded).

③ Four intervals: $(-\infty, -3)$, $(-3, -2]$, $[-2, 2]$, $[2, \infty)$.

④ Sign in each interval:
- $x < -3$: $x=-4$ → $(−6)(−2)/(−1) = (+)/(−) = −$ ≤ 0. ✅
- $-3 < x \leq -2$: $x=-2.5$ → $(−4.5)(−0.5)/(0.5) = (+)/(+) = +$ ≤ 0. ❌
- $-2 \leq x \leq 2$: $x=0$ → $(−2)(2)/(3) = (−)/(+) = −$ ≤ 0. ✅
- $x \geq 2$: $x=3$ → $(1)(5)/(6) = (+)/(+) = +$ ≤ 0. ❌

⑤ Boundaries: $x=-2$, $x=2$ make numerator 0 → included. $x=-3$ is excluded.

→ **$x < -3$ or $-2 \leq x \leq 2$.**

---

## Exercise 2

> $2^x + 2^{x+1} > 48$. Start by pulling out $2^x$.

① $2^{x+1} = 2 \cdot 2^x$. → $2^x + 2 \cdot 2^x = 3 \cdot 2^x > 48$.

② $2^x > 16$. $16 = 2^4$.

③ Base 2 > 1 → keep inequality direction: $x > 4$.

→ **$x > 4$.**

---

## Exercise 3

> $\log_2 (x^2 - 3x) \leq 2$. Don't forget the argument > 0 condition.

① $2 = \log_2 4$. → $\log_2(x^2-3x) \leq \log_2 4$.
Base 2 > 1 → $x^2 - 3x \leq 4$ → $x^2 - 3x - 4 \leq 0$.

② Tear: $(x-4)(x+1) \leq 0$.
→ $-1 \leq x \leq 4$.

③ Argument condition: $x^2 - 3x > 0$ → $x(x-3) > 0$.
→ $x < 0$ or $x > 3$.

④ Intersect the two conditions:
$-1 \leq x \leq 4$ ∩ ($x < 0$ or $x > 3$).
→ $[-1, 0)$ ∪ $(3, 4]$.

→ **$-1 \leq x < 0$ or $3 < x \leq 4$.**

---

## Exercise 4: Constructive

> Find the range of $x$ satisfying $[x]^2 - 5[x] + 6 = 0$, then make your own problem of the same form.

① Substitute $t = [x]$: $t^2 - 5t + 6 = 0$ → $(t-2)(t-3) = 0$.

② $t = 2$: $[x] = 2$ → $2 \leq x < 3$.
$t = 3$: $[x] = 3$ → $3 \leq x < 4$.

→ **$2 \leq x < 3$ or $3 \leq x < 4$, i.e. $2 \leq x < 4$.**

③ My own problem: $[x]^2 + [x] - 6 = 0$.
$(t+3)(t-2) = 0$ → $t = -3$ or $t = 2$.
$[x] = -3$ → $-3 \leq x < -2$.
$[x] = 2$ → $2 \leq x < 3$.
→ Answer: $-3 \leq x < -2$ or $2 \leq x < 3$.

---

## Exercise 5

> $|x-2| + |x+3| \leq 7$. Split into three intervals at the zero points.

① Zero points of the absolute value insides: $x=2$, $x=-3$. Three intervals.

**Interval 1: $x < -3$**
Both insides negative. $-(x-2) - (x+3) = -x+2 -x-3 = -2x-1 \leq 7$.
$-2x \leq 8$ → $x \geq -4$.
Intersect → $-4 \leq x < -3$.

**Interval 2: $-3 \leq x < 2$**
$x-2$ negative, $x+3$ positive.
$-(x-2) + (x+3) = -x+2 + x+3 = 5 \leq 7$. Always true.
→ Whole interval: $-3 \leq x < 2$.

**Interval 3: $x \geq 2$**
Both positive. $(x-2) + (x+3) = 2x+1 \leq 7$.
$2x \leq 6$ → $x \leq 3$.
Intersect → $2 \leq x \leq 3$.

② Union → **$-4 \leq x \leq 3$.**

---

## Exercise 6: Challenge

> Solve $\{x\} + [x]^2 \leq x$ for $0 \leq x < 3$.

① Substitute $\{x\} = x - [x]$: $(x - [x]) + [x]^2 \leq x$.
Cancel $x$ → $-[x] + [x]^2 \leq 0$ → $[x]([x] - 1) \leq 0$.

② $t = [x]$, $t$ is an integer. $t(t-1) \leq 0$ → $0 \leq t \leq 1$.
$t = 0$ or $t = 1$.

③ In the interval $0 \leq x < 3$:
$t = 0$: $[x] = 0$ → $0 \leq x < 1$.
$t = 1$: $[x] = 1$ → $1 \leq x < 2$.

④ When $t = 2$, $2 \cdot 1 = 2 > 0$ → inequality fails.
The interval $2 \leq x < 3$ is excluded.

→ **$0 \leq x < 1$ or $1 \leq x < 2$, i.e. $0 \leq x < 2$.**

---

[Back to Index](../08-inequalities.md)
