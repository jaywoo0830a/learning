# Solutions: 9A — Graph Drawing Toolkit

---

## Practice 1

> Domain of $f(x) = \frac{\sqrt{9-x^2}}{\ln(x-1)}$.

① $\sqrt{\cdot}$: $9-x^2 \geq 0 \to x^2 \leq 9 \to -3 \leq x \leq 3$.
② $\ln(\cdot)$: $x-1 > 0 \to x > 1$.
③ Denominator: $\ln(x-1) \neq 0 \to x-1 \neq 1 \to x \neq 2$.
Intersect: $(1, 2) \cup (2, 3]$.

→ **Domain: $(1,2) \cup (2,3]$.**

---

## Practice 2

> $f(x) = \frac{x^2-4}{x^2-1}$. Factor: $\frac{(x-2)(x+2)}{(x-1)(x+1)}$.

Domain: $x \neq 1, -1$. No cancellation → no hole.
Vertical asymptotes: $x=1$, $x=-1$.
Horizontal: ratio of leading coefficients → $y=1$.
Intercepts: $x$-int: $x=\pm2$, $(0,\pm2)$. $y$-int: $f(0)=4$.
Sign: intervals $(-\infty,-2),(-2,-1),(-1,1),(1,2),(2,\infty)$. Test points.
Crosses $y=1$: $\frac{x^2-4}{x^2-1}=1 \to x^2-4=x^2-1 \to -4=-1$, never. So no crossing — $y=1$ is strict asymptote.

---

## Practice 3

> $f(x) = \frac{x^2+1}{x-2}$.

Divide: $x^2+1 \div (x-2) = x+2$ with remainder $5$.
$f(x) = x+2 + \frac{5}{x-2}$.
Slant asymptote: $y=x+2$.
Vertical: $x=2$. $y$-int: $(0,-\frac{1}{2})$. No $x$-int (numerator $x^2+1>0$ always).

---

## Practice 4

> $\sqrt{x}$ shifted left 3, down 1.

$f(x) = \sqrt{x+3} - 1$. Domain: $x+3 \geq 0 \to x \geq -3$.
Starting point: $(-3, -1)$.

---

## Practice 5

> $f(x)=|x^2-4|$.

$x^2-4$ is negative on $(-2,2)$ (a U-shape dipping to $-4$ at $x=0$).
Folding upward: the dip between $-2$ and $2$ becomes an upward bump peaking at $(0,4)$.
Outside $[-2,2]$, the graph is unchanged ($x^2-4 \geq 0$).

---

## Practice 6

> Piecewise with boundaries.

$x=-1$: piece 1 gives $-(-1)-2=-1$. Piece 2 gives $(-1)^2=1$. → Jump. Filled at $(-1,-1)$, empty at $(-1,1)$.
$x=2$: piece 2 gives $4$. Piece 3: $4/(2-1)=4$. → **Continuous!** Filled at $(2,4)$.
Draw: line (slope -1) for $x<-1$, parabola for $-1\leq x<2$, hyperbola for $x\geq2$ approaching $y=0$.

---

## Basic Drill

**D1.** $2x+6 \geq 0 \to x \geq -3$. Domain: $[-3,\infty)$.

**D2.** $x^2-9 \neq 0 \to x \neq \pm3$. Domain: $\mathbb{R} \setminus \{-3, 3\}$.

**D3.** $x^3-9x = x(x-3)(x+3)=0$. $x$-int: $-3,0,3$. $y$-int: $f(0)=0$. All at origin and $\pm3$.

**D4.** $f(x)=\frac{3x}{x-2}$. Vertical: $x=2$. Horizontal: $y=3$ (ratio of leading coefficients).

**D5.** $x^2+3x \div (x+1) = x+2$ remainder $-2$. $f(x)=x+2-\frac{2}{x+1}$. Slant: $y=x+2$.

**D6.** $f(x)=|x-4|+2$. V-shape, vertex at $(4,2)$.

**D7.** $y=\sqrt{x}$ reflected across $y$-axis → $y=\sqrt{-x}$, domain $x \leq 0$. Up 3 → $y=\sqrt{-x}+3$.

**D8.** $\lfloor 3.7\rfloor = 3$, $\lfloor -2.3\rfloor = -3$, $\lceil 1.2\rceil = 2$, $\lceil -0.8\rceil = 0$.

**D9.** $\frac{x^2-1}{x^2-4}=0 \to x^2-1=0 \to x=\pm1$. Horiz. asy. $y=1$ is crossed at $x=\pm1$. Check: $f(\pm1)=0$.

**D10.** Example: $f(x)=\frac{1}{(x+1)(x-2)}$. Or $\frac{x}{(x+1)(x-2)}$, etc. Must have denominator $(x+1)(x-2)$ and numerator degree < denominator degree.

---

## Advanced Drill

**A1.** $\frac{x^3-8}{x-2} = \frac{(x-2)(x^2+2x+4)}{x-2} = x^2+2x+4$ for $x\neq2$. Hole at $(2, 12)$. It's a parabola with one point missing.

**A2.** $x>2$: $\frac{x-2}{x-2}=1$. $x<2$: $\frac{-(x-2)}{x-2}=-1$. Range: $\{-1, 1\}$. Two horizontal lines with a hole at $(2,1)$ — the function is undefined at $x=2$.

**A3.** $\lfloor 2x\rfloor$: stair width halved to $0.5$. $[-2,-1.5)$: $-4$, $[-1.5,-1)$: $-3$, …, $[1.5,2)$: $3$. At $x=2$, empty circle at $(2,3)$ then filled at $(2,4)$.

**A4.** $\frac{(x-2)(x-3)}{(x-3)(x+2)}$. Cancel $(x-3)$: $f(x)=\frac{x-2}{x+2}$, $x\neq3$. Hole at $(3, \frac{1}{5})$. Vertical: $x=-2$. Horizontal: $y=1$.

**A5.** $f(x)=\frac{1}{(x-1)^2}$. Domain: $x\neq1$. Vertical: $x=1$ (both sides $+\infty$). Horizontal: $y=0$. Sign: always positive. Range: $(0,\infty)$. Symmetric about $x=1$.

**A6.** $f(x)=x+\frac{1}{x}$. Slant: $y=x$. At $x=0$: vertical asymptote (not slant). $x\to0^+$ → $+\infty$, $x\to0^-$ → $-\infty$. Odd function. Min at $x=1$: $f(1)=2$.

**A7.** $\{x\}-\frac{1}{2}$: the sawtooth shifted down by $\frac{1}{2}$. Now oscillates in $[-\frac{1}{2}, \frac{1}{2})$. Each diagonal still has slope 1.

**A8.** Domain: $x^2-4\geq0 \to |x|\geq2$. As $x\to\infty$, $\sqrt{x^2-4} = x\sqrt{1-4/x^2} \approx x(1-2/x^2) = x - 2/x \to x$. The line $y=x$ is the slant asymptote. For $x\leq-2$, similarly $y=-x$ is the asymptote in the left branch.

**A9.** $||x|-2|$: inner $|x|$ is V at origin. $|x|-2$ shifts down by 2. Outer $|\cdot|$ folds the negative part up. Result: a W-shape. Three V-folds: at $x=-2,0,2$.

**A10.** Example: $f(x)=\begin{cases} x^2, & x<0 \\ \text{undefined}, & x=0 \\ 5, & 0<x\leq 2 \\ 5\cdot 2^{-(x-2)}, & x>2 \end{cases}$. Hole at $x=0$ (no value). Jump at $x=2$ from 5 down to 5 (could make it continuous there if desired, or create a jump).
