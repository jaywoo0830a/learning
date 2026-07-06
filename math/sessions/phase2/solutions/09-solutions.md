# 09 Solutions — Push In, Spin Around, Flip Over, and Draw

---

## Exercise 1

> Find the domain of $f(x) = \frac{\sqrt{9-x^2}}{\ln(x-1)}$.

Write each condition one at a time.

① **Inside square root** ≥ 0: $9 - x^2 \geq 0$ → $-3 \leq x \leq 3$.

② **Log argument** > 0: $x - 1 > 0$ → $x > 1$.

③ **Denominator** ≠ 0: $\ln(x-1) \neq 0$ → $x-1 \neq 1$ → $x \neq 2$.

④ Intersect all three conditions:
$-3 \leq x \leq 3$ ∩ $x > 1$ ∩ $x \neq 2$.
→ $(1, 2) \cup (2, 3]$.

→ **Domain: $(1, 2) \cup (2, 3]$.**

---

## Exercise 2

> Draw the graph of $f(x) = \frac{x^2-4}{x^2-1}$ using the 7 steps.

**Step 1 — Domain**: denominator $x^2-1 = (x-1)(x+1) = 0$ → $x \neq \pm 1$.

**Step 2 — Symmetry**: $f(-x) = \frac{x^2-4}{x^2-1} = f(x)$. → $y$-axis symmetry (even function).

**Step 3 — Intercepts**:
$x$-intercepts: numerator=0 → $x^2-4=0$ → $x = \pm 2$.
$y$-intercept: $x=0$ → $f(0) = \frac{-4}{-1} = 4$.

**Step 4 — Asymptotes**:
Vertical: denominator 0 at $x = -1$, $x = 1$.
Horizontal: as $x \to \pm\infty$, $\frac{x^2-4}{x^2-1} \to 1$. → $y=1$.

**Step 5 — Sign**: roots at −2, −1, 1, 2 create five intervals.
- $x < -2$: $(+)/(+) = +$. Above axis.
- $-2 < x < -1$: $(−)/(+) = −$. Below axis.
- $-1 < x < 1$: $(−)/(−) = +$. Above axis. At $x=0$, value is 4.
- $1 < x < 2$: $(−)/(+) = −$. Below axis.
- $x > 2$: $(+)/(+) = +$. Above axis.

**Step 6 — Near asymptotes**:
$x \to -1^-$: numerator $(+)$, denominator small $(+)$ → $+\infty$.
$x \to -1^+$: numerator $(+)$, denominator small $(−)$ → $-\infty$.
$x \to 1^-$: numerator $(−)$, denominator small $(−)$ → $+\infty$.
$x \to 1^+$: numerator $(−)$, denominator small $(+)$ → $-\infty$.

**Step 7 — Draw**:
$y$-axis symmetric, so draw only the right side and copy.
Wall at $x=1$. Crosses axis at $x=2$. $y$-intercept at 4. Approaches $y=1$ from above as $x \to \infty$.
Left side is the mirror image of the right.

---

## Exercise 3: Constructive

> Make two functions of the form $\frac{ax+b}{cx+d}$ that both have asymptotes $x=2$ and $y=1$.

For $\frac{ax+b}{cx+d}$:
- Vertical asymptote: $cx+d=0$ → $x = -d/c = 2$ → $d = -2c$.
- Horizontal asymptote: $a/c = 1$ → $a = c$.

Set $c=1$, then $a=1$, $d=-2$. → $\frac{x+b}{x-2}$.

**Function 1**: $b=0$ → $f(x) = \frac{x}{x-2}$.
$x$-intercept: $x=0$. $y$-intercept: $f(0)=0$. Passes through the origin.
$x \to 2^+$: $+\infty$. $x \to 2^-$: $-\infty$.

**Function 2**: $b=2$ → $f(x) = \frac{x+2}{x-2}$.
$x$-intercept: $x=-2$. $y$-intercept: $f(0)=-1$.
$x \to 2^+$: $+\infty$. $x \to 2^-$: $-\infty$.

Comparison: both functions share the same asymptotes, but their intercepts differ.
Function 1 passes through the origin; Function 2 passes through $(−2,0)$ and $(0,−1)$.

---

## Exercise 4: Constructive

> Draw the graph of $f(x) = [x] + \{x\}^2$ on $[-2, 3]$.

$\{x\} = x - [x]$. On each interval $[n, n+1)$, $[x] = n$ and $\{x\} = x - n$.

Formula for each interval:
- $[-2, -1)$: $f(x) = -2 + (x+2)^2$.
  $x=-2$: $f(-2) = -2 + 0 = -2$. $x \to -1^-$: $-2 + 1 = -1$ (empty dot).
- $[-1, 0)$: $f(x) = -1 + (x+1)^2$.
  $x=-1$: $f(-1) = -1$. $x \to 0^-$: $-1+1 = 0$ (empty dot).
- $[0, 1)$: $f(x) = 0 + x^2 = x^2$.
  $x=0$: $0$. $x \to 1^-$: $1$ (empty dot).
- $[1, 2)$: $f(x) = 1 + (x-1)^2$.
  $x=1$: $1$. $x \to 2^-$: $1+1 = 2$ (empty dot).
- $[2, 3)$: $f(x) = 2 + (x-2)^2$.
  $x=2$: $2$. $x \to 3^-$: $2+1 = 3$ (empty dot).
- $x=3$: $f(3) = 3 + 0^2 = 3$.

Each interval is a piece of a parabola. At integers, left endpoints are filled dots, right endpoints are empty.
There are small jumps at integers.
($x \to 1^-$ gives 1, $x=1$ gives 1 — it actually connects at $x=1$.)

---

## Exercise 5

> Draw the graph of $f(x) = \frac{|x|-1}{x-1}$.

① Split into $x \geq 0$ and $x < 0$ to strip the absolute value.

**Case 1: $x \geq 0$**: $|x| = x$.
$f(x) = \frac{x-1}{x-1}$.
For $x \neq 1$, $f(x) = 1$. $x=1$ is a hole.
→ Horizontal line at height 1 for $x \geq 0$, $x \neq 1$. Empty circle at $(1, 1)$.

**Case 2: $x < 0$**: $|x| = -x$.
$f(x) = \frac{-x-1}{x-1} = \frac{-(x+1)}{x-1}$.
As $x \to -\infty$: $\frac{-x-1}{x-1} = \frac{-(x+1)}{x-1} \to -1$.
→ Horizontal asymptote $y=-1$.

② Drawing:
$x \geq 0, x \neq 1$: horizontal line $y=1$. Hole at $(1,1)$.
$x < 0$: $y = \frac{-x-1}{x-1}$. At $x=0$, $f(0) = \frac{-1}{-1} = 1$. Point $(0,1)$.
At $x=-1$, $f(-1) = \frac{1-1}{-2} = 0$. Crosses axis at $(-1,0)$.
As $x \to -\infty$, approaches $y=-1$.

---

## Exercise 6: Challenge

> Draw the graph of $f(x) = \frac{[x]}{x}$ on $[-3, 0) \cup (0, 3]$.

① $[x]$ is constant $n$ on each interval $[n, n+1)$.

**$x > 0$ region**:
- $0 < x < 1$: $[x]=0$ → $f(x)=0$.
- $1 \leq x < 2$: $[x]=1$ → $f(x)=\frac{1}{x}$. From $(1,1)$ to just before $(2, 0.5)$.
- $2 \leq x \leq 3$: $[x]=2$ → $f(x)=\frac{2}{x}$. From $(2,1)$ to $(3, \frac{2}{3})$.

**$x < 0$ region**:
- $-1 \leq x < 0$: $[x]=-1$ → $f(x)=\frac{-1}{x}$. From $(-1,1)$, shoots to $+\infty$ as $x \to 0^-$.
- $-2 \leq x < -1$: $[x]=-2$ → $f(x)=\frac{-2}{x}$. From $(-2,1)$ to just before $(-1, 2)$.
- $-3 \leq x < -2$: $[x]=-3$ → $f(x)=\frac{-3}{x}$. From $(-3,1)$ to just before $(-2, \frac{3}{2})$.

② Behavior as $x \to 0$:
$x \to 0^+$: $[x]=0$, $f(x)=0$. → Converges to 0.
$x \to 0^-$: $[x]=-1$, $f(x)=-\frac{1}{x}$ → $+\infty$. Shoots up like a vertical asymptote.

③ At interval boundaries: at $x=1$, left $f \to 1$, right $f=1$ — connected.
At $x=2$, left $f \to 0.5$, right $f=1$ — jump.
At $x=-1$, left $f \to 2$, right $f=1$ — jump.
At $x=-2$, left $f \to 1.5$, right $f=1$ — jump.

---

[Back to Index](../09-functions.md)
