# Session 09: Functions — Push In, Spin Around, Flip Over, and Draw

**Phase 2 — Classical Techniques | 90 min**

---

## Part A: Numbers Go In, Numbers Come Out

---

## Example 1: Push a Number In, a Number Comes Out

Picture a box called $f(x) = 2x + 3$.

Push in $x=1$. → 5 comes out.
Push in $x=4$. → 11 comes out.
Push in $x=-2$. → −1 comes out.

The set of all numbers you can push in is called the **domain**.
The set of all numbers that come out is called the **range**.
For this box, you can push any number in. Any number can come out.

---

## Example 2: Finding Numbers You Can't Push In — Four Rules

**Rule 1 — Square Root**: $\sqrt{x-2}$.
The inside of a square root must be 0 or bigger.
Solve $x-2 \geq 0$. → $x \geq 2$.
Numbers smaller than 2 can't go in.

**Rule 2 — Denominator**: $\frac{1}{x^2-4}$.
If the denominator becomes 0, the box explodes.
Solve $x^2-4=0$. → $x=2$, $x=-2$.
You can push in any number except these two.

**Rule 3 — Both Mixed**: $\frac{\sqrt{x+1}}{x-2}$.
Square root condition: $x+1 \geq 0$ → $x \geq -1$.
Denominator condition: $x \neq 2$.
Intersect both conditions. → $[-1, 2)$ and $(2, \infty)$.

**Rule 4 — Logarithm**: $\log_3 (2x-5)$.
The expression to the right of log must be positive.
Solve $2x-5 > 0$. → $x > \frac{5}{2}$.

---

## Example 3: What Numbers Come Out

$f(x) = x^2 + 2$.
$x^2$ is always 0 or bigger. Then we add 2.
→ The numbers that come out are always 2 or bigger.

$g(x) = \frac{1}{x-1}$.
As $x$ gets close to 1, the value shoots up to $\pm\infty$.
As $x$ goes to $\pm\infty$, the value gets infinitely close to 0.
→ Numbers that come out: all real numbers except 0.

$h(x) = \sqrt{4-x^2}$.
$x$ can only go in from −2 to 2.
At $x=0$, the peak is 2. At $x=\pm2$, the floor is 0.
→ Numbers that come out: 0 to 2.

---

## Part B: Connecting Functions and Swapping Input-Output

---

## Example 4: Connecting Two Functions

Connect $f(x)=2x+1$ and $g(x)=x^2$.

**Connect $g$ to $f$** — $(f \circ g)(x) = f(g(x))$.
① Push $x$ into $g$ → $x^2$ comes out.
② Push that result into $f$ → $2x^2+1$ comes out.

**Connect $f$ to $g$** — $(g \circ f)(x) = g(f(x))$.
① Push $x$ into $f$ → $2x+1$ comes out.
② Push that result into $g$ → $(2x+1)^2 = 4x^2+4x+1$.

The result changes when you swap the order.

---

## Example 5: Connecting Can Shrink the Domain

$f(x) = \sqrt{x}$, $g(x) = x-3$.

**$f \circ g$**: Push $x$ into the inner $g$ → $x-3$.
Push $x-3$ into the outer $f$ → $\sqrt{x-3}$.
$f$ only accepts 0 or bigger. $x-3 \geq 0$ → $x \geq 3$.
The domain shrinks to $[3, \infty)$.

**$g \circ f$**: Push $x$ into the inner $f$ → $\sqrt{x}$.
Push $\sqrt{x}$ into the outer $g$ → $\sqrt{x}-3$.
$f$'s domain is $[0,\infty)$. $g$ accepts anything.
The domain stays $[0, \infty)$.

---

## Example 6: Connecting a Piecewise Function

$$
f(x) = \begin{cases}
x+1, & x < 0 \\
x^2, & x \geq 0
\end{cases}
$$

Connect $g(x) = 2x-1$ to it — $(f \circ g)(x)$.

① Push $x$ into $g$ → $2x-1$ comes out.
② Check whether this value is less than 0 or 0 or bigger.
③ If less than 0, use $f$'s top rule $(x+1)$.
   If 0 or bigger, use $f$'s bottom rule $(x^2)$.

$2x-1 < 0$ → $x < \frac{1}{2}$ interval: result is $(2x-1)+1 = 2x$.
$x \geq \frac{1}{2}$ interval: result is $(2x-1)^2$.

---

## Example 7: Swapping Input and Output — Inverse Function

$f(x) = 3x-6$.

① Write $y = 3x-6$.
② Solve for $x$: $y+6 = 3x$ → $x = \frac{y+6}{3}$.
③ Write $x$ in place of $y$: $f^{-1}(x) = \frac{x+6}{3}$.

Verify: push $f^{-1}(x)$ into $f$.
Push $\frac{x+6}{3}$ into $3x-6$ → $3 \cdot \frac{x+6}{3} - 6 = x$.
Exactly $x$ comes out. Correct.

---

## Example 8: Inverse of a Rational Function

$f(x) = \frac{2x+1}{x-3}$.

① $y = \frac{2x+1}{x-3}$.
② Multiply both sides by $(x-3)$: $y(x-3) = 2x+1$.
③ Spread out: $yx - 3y = 2x + 1$.
④ Gather $x$ terms on the left: $yx - 2x = 3y + 1$.
⑤ Bundle with $x$: $x(y-2) = 3y + 1$.
⑥ Divide by $y-2$: $x = \frac{3y+1}{y-2}$.
⑦ Write $x$ in place of $y$: $f^{-1}(x) = \frac{3x+1}{x-2}$.

---

## Example 9: When You Can't Swap — Snip the Domain

$f(x) = x^2$.

Push in $x=2$ → 4. Push in $x=-2$ → also 4.
Different inputs give the same output.
If we swap as-is, one input would produce two outputs. That's not a function.

**Keep only the right half**: snip the domain to $[0, \infty)$.
→ Inverse: $f^{-1}(x) = \sqrt{x}$.

**Keep only the left half**: snip the domain to $(-\infty, 0]$.
→ Inverse: $f^{-1}(x) = -\sqrt{x}$.

---

## Part C: The Ultimate 7-Step Graph-Drawing Sequence

> **Get paper and pencil.** Follow each step below and draw as you go.

```
Step 1 ─ Find the x-values you can't draw (domain)
Step 2 ─ If symmetric, draw only half
Step 3 ─ Mark where it meets the axes (intercepts)
Step 4 ─ Draw lines it approaches but never touches (asymptotes)
Step 5 ─ Judge the sign — above or below the x-axis
Step 6 ─ Connect the dots with a smooth curve
Step 7 ─ Steps, sawteeth, or pieces: draw each interval separately
```

---

## Example 10: Polynomial — Draw Using Symmetry and End Behavior

$f(x) = x^3 - 4x$.

**Step 1 — Domain**: A polynomial can be drawn for all $x$.

**Step 2 — Symmetry**: Compute $f(-x)$.
$(-x)^3 - 4(-x) = -x^3 + 4x = -(x^3-4x) = -f(x)$.
→ Origin symmetry. Draw only the right side, then spin it around and copy.

**Step 3 — Intercepts**: Find where it meets the $x$-axis.
$x^3 - 4x = 0$ → $x(x^2-4) = 0$ → $x(x-2)(x+2) = 0$.
It crosses the $x$-axis at $x=-2, 0, 2$.
Plug in $x=0$ → $f(0)=0$. It passes through the origin.

**Step 5 — Sign**: The roots −2, 0, 2 split the line into four intervals.
$x < -2$: all three factors negative → product negative → below axis.
$-2 < x < 0$: two negative, one positive → product positive → above axis.
$0 < x < 2$: one negative, two positive → product negative → below axis.
$x > 2$: all three positive → product positive → above axis.

**End behavior**: $x \to \infty$ → $x^3$ dominates → $+\infty$.
$x \to -\infty$ → $x^3$ dominates → $-\infty$.

**Step 6 — Connect**: Start from bottom left → cross axis upward at $x=-2$ → come up then down, cross origin → cross axis upward at $x=2$ → head to top right.

![Polynomial y=x³-4x](graphs/01-cubic-poly.png)

---

## Example 11: Rational Function — Tear and Cancel First

$f(x) = \frac{x^2 - x - 2}{x^2 - 4}$.

**Step 0 — Tear**: Numerator $(x-2)(x+1)$, denominator $(x-2)(x+2)$.
$(x-2)$ appears in both numerator and denominator. → It cancels.
$f(x) = \frac{x+1}{x+2}$, **but $x \neq 2$**.

$x=2$ made the original denominator 0. It canceled but still can't go in.
→ Punch an **empty circle (hole)** at $(2, \frac{3}{4})$.

**Step 1 — Domain**: $x \neq -2$ (denominator 0), $x \neq 2$ (hole).

**Step 4 — Asymptotes**:
Vertical: $x=-2$ where denominator is 0.
Horizontal: as $x \to \infty$, $\frac{x+1}{x+2} \to 1$. → $y=1$.

**Step 3 — Intercepts**:
$y$-intercept: plug in $x=0$ → $f(0) = \frac{1}{2}$.
$x$-intercept: numerator=0 → $x = -1$.

**Step 5 — Sign near asymptotes**:
$x \to -2^+$: numerator negative, denominator tiny positive → $-\infty$.
$x \to -2^-$: numerator negative, denominator tiny negative → $+\infty$.

**Step 6 — Connect**:
Left of $x=-2$: starts at $+\infty$, passes $x$-intercept −1, approaches $y=1$ from below.
Right of $x=-2$: starts at $-\infty$, passes $y$-intercept $\frac{1}{2}$, approaches $y=1$ from below.
Empty circle at $x=2$.

![Rational function with a hole](graphs/02-rational-hole.png)

---

## Example 12: Slant Asymptote — Divide First

$f(x) = \frac{x^2 + 2x}{x - 1}$.

**Divide**: $x^2+2x$ divided by $x-1$.
Quotient $x+3$, remainder 3.
→ $f(x) = x + 3 + \frac{3}{x-1}$.

**Vertical asymptote**: denominator 0 → $x = 1$.
**Slant asymptote**: as $x \to \pm\infty$, $\frac{3}{x-1} \to 0$.
→ The graph hugs the line $y = x+3$.

**Intercepts**: $x=0$ → $f(0)=0$ (origin). $f(x)=0$ → $x(x+2)=0$ → $x=0,-2$.

**Near asymptote**: $x \to 1^+$ → $\frac{3}{x-1} \to +\infty$ → $+\infty$.
$x \to 1^-$ → $\frac{3}{x-1} \to -\infty$ → $-\infty$.

**Drawing order**:
① Draw the slant line $y=x+3$ as a dashed line first.
② Draw the vertical dashed line at $x=1$.
③ Mark $(-2,0)$ and $(0,0)$.
④ Draw the curve hugging the asymptotes.

![Slant asymptote](graphs/03-slant-asymptote.png)

---

## Example 13: Hyperbola — The $\frac{ax+b}{cx+d}$ Form

$f(x) = \frac{2x+1}{x-1}$.

**Vertical asymptote**: denominator 0 → $x=1$.
**Horizontal asymptote**: $x \to \infty$, $\frac{2x}{x} \to 2$ → $y=2$.

**Intercepts**:
$y$-intercept: $x=0$ → $y=-1$.
$x$-intercept: $2x+1=0$ → $x=-\frac{1}{2}$.

**Center**: the intersection of the two asymptotes $(1,2)$.
The graph is a hyperbola, symmetric on opposite sides of this point.

**Approach directions**:
$x \to 1^+$: $(+)/(+\text{ small}) \to +\infty$.
$x \to 1^-$: $(+)/(-\text{ small}) \to -\infty$.
$x \to \infty$: $2 + \frac{3}{x-1}$ → approaches $y=2$ from above.
$x \to -\infty$: approaches $y=2$ from below.

---

## Example 14: Radical Function — A Half-Graph

$f(x) = \sqrt{x-1} + 2$.

**Starting point**: only at $x=1$ does the inside of the root become 0.
$f(1) = 0 + 2 = 2$. Mark the point $(1, 2)$.
For $x < 1$, the inside is negative → no graph.

**Growth**: as $x$ gets bigger, the root value grows slowly.
The whole graph spreads to the upper right.

**Shape**: $y = \sqrt{x}$ shifted right by 1 and up by 2.

![Shifted square root](graphs/04-sqrt-shifted.png)

---

## Part D: Steps, Sawteeth, and Signs — Special Functions

---

## Example 15: The Floor Function $[x]$ — Building Stairs

$[x]$ is the greatest integer not exceeding $x$.

Let's pin down some values:
$[0] = 0$, $[0.3] = 0$, $[0.999] = 0$.
$[1] = 1$, $[1.7] = 1$.
$[-0.3] = -1$, $[-1] = -1$, $[-1.2] = -2$.

**Pattern**: the interval $[0, 1)$ is all at height 0.
$[1, 2)$ is all at height 1.
$[-1, 0)$ is all at height −1.

**How to draw**:
On $[0, 1)$, draw a horizontal segment at height 0. Right endpoint $(1, 0)$ is an empty circle.
On $[1, 2)$, draw a horizontal segment at height 1. Left endpoint $(1, 1)$ is a filled circle.
Repeat left and right.

![Floor function stair graph](graphs/05-floor-function.png)

$[2x]$: the stair width is halved. $[0,0.5)$ is 0, $[0.5,1)$ is 1.
$[x]+[-x]$: 0 for integers, −1 otherwise.

---

## Example 16: The Fractional Part $\{x\}$ — Repeating Sawteeth

$\{x\} = x - [x]$. Strip away the integer part, leaving only the decimal.

$\{3.7\} = 0.7$, $\{5.0\} = 0$, $\{-1.2\} = -1.2 - (-2) = 0.8$.

**How to draw**:
$[0,1)$ interval: $\{x\} = x - 0 = x$. A diagonal from the origin to just before $(1,1)$.
$[1,2)$ interval: $\{x\} = x - 1$. A diagonal from $(1,0)$ to just before $(2,1)$.
$[-1,0)$ interval: $\{x\} = x + 1$. A diagonal from $(-1,0)$ to just before $(0,1)$.

The sawtooth repeats infinitely with height in $[0,1)$. 1 is never reached.

![Fractional part sawtooth graph](graphs/06-frac-part.png)

---

## Example 17: Ceiling Function and Sign Function

**$\lceil x \rceil$**: the smallest integer not less than $x$.
$\lceil 3.2 \rceil = 4$, $\lceil -1.2 \rceil = -1$.
On $(0,1]$ it's 1, on $(1,2]$ it's 2. Like the floor function but shifted right.

**$\operatorname{sgn}(x)$**: keeps only the sign.
If $x<0$, −1. If $x=0$, 0. If $x>0$, 1.
The graph is three horizontal segments at heights −1, 0, 1.

![Ceiling and sign functions](graphs/07-ceiling-sign.png)

---

## Part E: Cooking with Graphs — Move, Flip, and Stretch

---

## Example 18: Move the Whole Graph

Base ingredient: $f(x) = |x|$. A V-shape, vertex at the origin.

**Right by 3**: $f(x-3) = |x-3|$.
Push $x-3$ into the $x$ slot. → the vertex moves to $(3,0)$.

**Up by 2**: $f(x)+2 = |x|+2$.
Add 2 to everything. → the vertex moves to $(0,2)$.

**Left 1, down 4**: $f(x+1)-4 = |x+1|-4$.
→ the vertex moves to $(-1,-4)$.

**By hand**: draw the original graph, move the vertex, redraw.

---

## Example 19: Flip and Reflect

Ingredient: $f(x) = \sqrt{x}$. Only exists for $x \geq 0$, spreads to the upper right.

**Flip over the $x$-axis**: $y = -\sqrt{x}$.
$(4, 2)$ drops to $(4, -2)$. The graph points downward.

**Flip over the $y$-axis**: $y = \sqrt{-x}$.
Only exists for $x \leq 0$. Mirror image of the right-side graph.

**Flip over the origin**: $y = -\sqrt{-x}$.
Flipped twice. Only exists in quadrant 3.

---

## Example 20: Fold the Part Below the Axis Upward

**$y = |f(x)|$ — Fold the part below the $x$-axis upward**.

Ingredient: $f(x) = x^2 - 1$.
A parabola dipping down to −1 at $x=0$.

$|f(x)| = |x^2-1|$:
The interval $-1 < x < 1$ was originally below the axis.
Fold this part upward across the $x$-axis.
→ Between $(-1,0)$ and $(1,0)$ becomes an upward bump.

**$y = f(|x|)$ — Copy the right side onto the left**.

Ingredient: $f(x) = x^2 - 2x$.
$f(|x|) = |x|^2 - 2|x| = x^2 - 2|x|$.

For $x \geq 0$, it's the original graph.
For $x < 0$, reflect the right-side graph across the $y$-axis and stick it on.
→ A W-shape.

---

## Example 21: Stretch and Shrink

Ingredient: $f(x) = \sin x$. Period $2\pi$, height 1.

**Vertical stretch**: $2\sin x$ → height doubles.
**Vertical shrink**: $\frac{1}{2}\sin x$ → height halves.
**Horizontal stretch**: $\sin(\frac{x}{2})$ → period doubles to $4\pi$.
**Horizontal shrink**: $\sin(2x)$ → period halves to $\pi$.

**Rule**: in $a \cdot f(bx)$,
$a$ scales the height by $a$. $b$ scales the horizontal speed by $b$.
$b>1$ squeezes it, $b<1$ stretches it.

![Absolute value transformations and scaling](graphs/08-transformations.png)

---

## Example 22: Piecewise Function — Draw Each Piece and Stick Together

$$
f(x) = \begin{cases}
x+2, & x \leq 0 \\
4 - x^2, & 0 < x \leq 2 \\
\frac{1}{x-2}, & x > 2
\end{cases}
$$

**Check the boundaries first**:
$x=0$: first piece gives 2. Second piece gives 4. → **Discontinuity!**
Mark a filled dot at $(0,2)$ and an empty dot at $(0,4)$.

$x=2$: second piece ends at 0. Third piece has denominator 0 at $x=2$.
→ $x=2$ is a vertical asymptote.

**Draw piece by piece**:
Piece 1: $x \leq 0$, line $y=x+2$. Ends at $(0,2)$.
Piece 2: $0 < x \leq 2$, downward opening parabola. Starts from empty dot $(0,4)$, ends at $(2,0)$.
Piece 3: $x > 2$, $y=\frac{1}{x-2}$. Wall at $x=2$, approaches 0 going right.

![Piecewise function](graphs/09-piecewise.png)

---

## Example 23: Mixing $[x]$ and $\{x\}$

**$f(x) = x + [x]$**.

Write $x$ as $n + \delta$ ($0 \leq \delta < 1$, $n$ integer).
$f(x) = n + \delta + n = 2n + \delta$.

$[0,1)$: $f(x) = 0 + \delta = \delta$. Diagonal from $(0,0)$ to just before $(1,1)$.
$[1,2)$: $f(x) = 2 + \delta$. From $(1,2)$ to just before $(2,3)$.
Jumps by 1 at every integer.

**$f(x) = x\{x\} = x(x-[x])$**.
$[0,1)$: $x \cdot x = x^2$. One piece of a parabola.
$[1,2)$: $x(x-1) = x^2-x$. Another piece of a parabola.
Drops to 0 at every integer.

![Mixed floor function graphs](graphs/10-mixed-floor.png)

---

## Example 24: Putting It All Together — Absolute Value + Rational

$f(x) = \frac{|x-1|}{x^2-1}$.

**Domain**: denominator $x^2-1 = (x-1)(x+1)$ → $x \neq 1, -1$.

**Strip the absolute value**:
When $x \geq 1$, $|x-1| = x-1$ → $f(x) = \frac{x-1}{(x-1)(x+1)} = \frac{1}{x+1}$ ($x \neq 1$).
When $x < 1$, $|x-1| = -(x-1)$ → $f(x) = \frac{-1}{x+1}$ ($x \neq -1$).

**Hole**: $x=1$ canceled but was originally excluded.
Plug $x=1$ into the $x \geq 1$ formula → $\frac{1}{2}$.
→ Empty circle at $(1, \frac{1}{2})$.

**Asymptotes**: vertical $x=-1$, horizontal $y=0$ (both sides).

**Drawing**:
$x < -1$: $y = -\frac{1}{x+1}$. $x \to -1^-$ → $+\infty$, $x \to -\infty$ → 0.
$-1 < x < 1$: $y = -\frac{1}{x+1}$. $x \to -1^+$ → $-\infty$, at $x=0$ → −1.
$x \geq 1$: $y = \frac{1}{x+1}$. Hole at $(1,\frac{1}{2})$, $x \to \infty$ → 0.

![Absolute value rational function combined](graphs/11-abs-rational.png)

---

## Common Mistakes

### Mistake 1: Getting the Order Wrong for Inverse of a Composition

**Wrong path**: "$(f \circ g)^{-1} = f^{-1} \circ g^{-1}$" ← wrong.

**Why it's wrong**: The inverse of a composition reverses the order.
$(f \circ g)^{-1} = g^{-1} \circ f^{-1}$.
You put on socks then shoes. To take them off: socks first, shoes second.

**Right path**: Taking the inverse flips the inside-to-outside order.

---

### Mistake 2: Forgetting to Punch a Hole After Canceling

**Wrong path**: "$\frac{(x-1)(x+2)}{x-1} = x+2$, so it's just a line." ← incomplete.

**Why it's wrong**: $x=1$ made the original denominator 0 and can never go in.
You must not mark $(1,3)$ on the canceled formula.

**Right path**: Punch an empty circle at $(1,3)$.

---

### Mistake 3: Filling the Right Endpoint of a Floor Function Step

**Wrong path**: "On $[1, 2]$, the value is 1." ← wrong.

**Why it's wrong**: $[2.0]=2$. The interval where $[x]=1$ is $1 \leq x < 2$.
$x=2$ already belongs to the next step.

**Right path**: The right endpoint of the $[1,2)$ interval is an empty circle.

---

### Mistake 4: Believing a Graph Can Never Cross Its Asymptote

**Wrong path**: "There's a horizontal asymptote at $y=1$, so the graph never touches $y=1$." ← not necessarily.

**Why it's wrong**: An asymptote only describes behavior as $x \to \pm\infty$.
For finite $x$, the graph can cross the asymptote.
Example: $y = \frac{x}{x^2+1}$ has horizontal asymptote $y=0$ but passes right through the origin.

**Right path**: The graph only hugs the asymptote as $x \to \pm\infty$.

---

## What We Just Did

```
① Find every x that can't go in. (square root, denominator, log, arcsin)
② When connecting two functions, compute from the inside out — push into the outer one.
③ For the inverse: solve y=f(x) for x, then swap x↔y.
   If one output comes from multiple inputs, snip the domain.
④ Draw graphs in 7 steps:
   domain → symmetry → intercepts → asymptotes → sign → connect → special handling.
⑤ Transformations: move the base graph (±h,±k),
   flip (−f, f(−x)), fold (|f|, f(|x|)), stretch (a·f(bx)).
⑥ [x] makes stairs, {x} makes sawteeth, piecewise functions are drawn interval by interval.
```

---

## Exercise 1

Find the domain of $f(x) = \frac{\sqrt{9-x^2}}{\ln(x-1)}$.
Write the square root, log, and denominator conditions in order.

→ Follow: **Example 2**

> Solutions: [Solution Set](solutions/09-solutions.md#exercise-1)

---

## Exercise 2

Draw the graph of $f(x) = \frac{x^2-4}{x^2-1}$ using the 7 steps.
Check asymptotes, intercepts, sign, and whether there's a hole.

→ Follow: **Example 11**

> Solutions: [Solution Set](solutions/09-solutions.md#exercise-2)

---

## Exercise 3: Constructive

Make two functions of the form $\frac{ax+b}{cx+d}$ that both have asymptotes $x=2$ and $y=1$.
Find their $x$- and $y$-intercepts, then compare and describe the two graphs.

→ Follow: **Example 13**

> Solutions: [Solution Set](solutions/09-solutions.md#exercise-3)

---

## Exercise 4: Constructive

Draw the graph of $f(x) = [x] + \{x\}^2$ on $[-2, 3]$.
First write the formula for each interval $[n, n+1)$.

→ Follow: **Examples 15, 16**

> Solutions: [Solution Set](solutions/09-solutions.md#exercise-4)

---

## Exercise 5

Draw the graph of $f(x) = \frac{|x|-1}{x-1}$.
Split into $x \geq 0$ and $x < 0$ to strip the absolute value.

→ Follow: **Examples 20, 21, 24**

> Solutions: [Solution Set](solutions/09-solutions.md#exercise-5)

---

## Exercise 6: Challenge

Draw the graph of $f(x) = \frac{[x]}{x}$ on $[-3, 0)$ and $(0, 3]$ separately.
Use the fact that $[x]$ is constant on each interval to simplify the formula.

→ Follow: **Example 15**

> Solutions: [Solution Set](solutions/09-solutions.md#exercise-6)

---

## Today's Procedure

```
Step 1: Check the domain first.
       Inside √ ≥ 0, denominator ≠ 0, inside log > 0, arcsin in [−1,1].
       If something cancels, record the hole location.

Step 2: Composition is inside→outside. Inverse: solve y=f(x), swap x↔y.
       If not one-to-one, snip the domain to make an inverse.

Step 3: Graph in 7 steps —
       domain → symmetry → intercepts → asymptotes → sign → connect → special handling.
       Transformations: move (±h,±k), flip (±f, f(±x)),
       fold (|f|, f(|x|)), stretch (a·f(bx)).
```

---

## Terminology

Up to now, we've only used simple words: "push in", "shove in", "move", "flip", "fold", "snip", "stick together".
**You already know the methods.** Now we give them their math names.

| What we've been calling it | Math Term | Symbol / Explanation |
|:--------------------------:|:---------:|:---:|
| numbers you can push in | domain | domain |
| numbers that come out | range | range |
| connecting functions | composite function | $(f \circ g)(x) = f(g(x))$ |
| swapping input and output | inverse function | $f^{-1}(x)$, symmetric across $y=x$ |
| only one comes out per input | one-to-one (injective) | injective |
| origin symmetry | odd function | $f(-x) = -f(x)$ |
| $y$-axis symmetry | even function | $f(-x) = f(x)$ |
| stair function | floor function | $\lfloor x \rfloor = [x]$ |
| ceiling function | ceiling function | $\lceil x \rceil$ |
| sawtooth function | fractional part | $\{x\} = x - \lfloor x \rfloor$ |
| sign function | signum function | $\operatorname{sgn}(x)$ |
| piece-by-piece function | piecewise function | different formulas on different intervals |
| moving the graph | translation | $f(x-h)+k$ |
| flipping the graph | reflection | $-f(x)$, $f(-x)$ |
| folding upward | absolute value of function | $\lvert f(x) \rvert$ |
| stretching/shrinking | scaling | $a \cdot f(bx)$ |
| hole | removable discontinuity | hole |
| line it hugs | asymptote | vertical, horizontal, slant |
