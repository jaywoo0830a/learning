# Solutions — 15A: Curve Analysis — Tangent Lines, Extrema, and Shape Through Geometry

> Back to [15A — Curve Analysis](../15A-curve-analysis.md)
## Basic Drills

### D1. Tangent line to $f(x) = x^2 + 2x$ at $x=1$.

$f(1) = 3$, $f'(x) = 2x+2$, $f'(1) = 4$.
$y - 3 = 4(x-1)$ → $y = 4x - 1$.

> **Answer**: $y = 4x - 1$

### D2. Critical points of $f(x) = x^3 - 6x^2 + 9x$.

$f'(x) = 3x^2 - 12x + 9 = 3(x-1)(x-3) = 0$ → $x = 1$ and $x = 3$.

> **Answer**: $x = 1, 3$

### D3. Classify the critical points from D2.

$f''(x) = 6x - 12$. $f''(1) = -6 < 0$ → **local max** at $(1, 4)$. $f''(3) = 6 > 0$ → **local min** at $(3, 0)$.

> **Answer**: max at $(1,4)$; min at $(3,0)$

### D4. Intervals where $f(x) = x^3 - 3x$ is increasing.

$f'(x) = 3x^2 - 3 = 3(x-1)(x+1) > 0$ when $x < -1$ or $x > 1$.

> **Answer**: increasing on $(-\infty, -1)$ and $(1, \infty)$

### D5. Inflection points of $f(x) = x^4 - 6x^2$.

$f''(x) = 12x^2 - 12 = 12(x-1)(x+1) = 0$ → $x = \pm 1$, and the sign of $f''$ changes at both → inflection points $(\pm 1,\, -5)$.

> **Answer**: $(\pm 1, -5)$

### D6. Concavity of $f(x) = \ln x$ on $(0,\infty)$.

$f''(x) = -\frac{1}{x^2} < 0$ everywhere on $(0,\infty)$ → **concave down** (∩).

> **Answer**: concave down on $(0,\infty)$

### D7. Apply MVT to $f(x) = \sqrt{x}$ on $[1,9]$. Find $c$.

Average slope $= \frac{3-1}{9-1} = \frac{1}{4}$. $f'(x) = \frac{1}{2\sqrt{x}} = \frac{1}{4}$ → $2\sqrt{x} = 4$ → $x = 4$.

> **Answer**: $c = 4$

### D8. Normal line to $f(x) = e^x$ at $x=0$.

$f(0) = 1$, $f'(0) = 1$. Tangent slope $1$, so normal slope $= -1$. $y - 1 = -1(x-0)$.

> **Answer**: $y = 1 - x$

### D9. Horizontal asymptotes of $f(x) = \frac{x^2}{x^2+4}$.

As $x \to \pm\infty$, $\frac{x^2}{x^2+4} \to 1$.

> **Answer**: $y = 1$

### D10. Vertical asymptotes of $f(x) = \frac{x}{x^2-9}$.

$x^2 - 9 = 0$ → $x = \pm 3$, and the numerator $x = \pm 3 \neq 0$ at those points.

> **Answer**: $x = 3$ and $x = -3$

### D11. For $f(x) = |x^2-4|$, find all points where $f$ is not differentiable.

The inside $x^2-4$ is zero at $x = \pm 2$, where the graph has sharp corners (cusps).

> **Answer**: $x = \pm 2$ — sharp corners, so no tangent line exists there

### D12. Tangent line to $f(x) = \sin x$ at $x = \pi/4$.

$f(\pi/4) = \frac{\sqrt2}{2}$, $f'(x) = \cos x$, $f'(\pi/4) = \frac{\sqrt2}{2}$.
Line: $y - \frac{\sqrt2}{2} = \frac{\sqrt2}{2}\left(x - \frac{\pi}{4}\right)$ (point-slope form).

**Unit-circle check**: the slope $\cos(\pi/4) = \frac{\sqrt2}{2}$ is exactly the $x$-coordinate of the unit-circle point at angle $\pi/4$ — the derivative of $\sin$ is $\cos$, which reads off the adjacent coordinate.

> **Answer**: $y - \tfrac{\sqrt2}{2} = \tfrac{\sqrt2}{2}\left(x - \tfrac{\pi}{4}\right)$

### D13. For $\vec{r}(t) = (t, t^2)$, find $\vec{v}(t)$, $|\vec{v}(t)|$, and curvature at $t=1$.

$\vec{v}(t) = (1, 2t)$; $|\vec{v}(t)| = \sqrt{1 + 4t^2}$.
At $t=1$: $x'=1, x''=0, y'=2, y''=2$.
$\kappa = \frac{|1\cdot 2 - 2\cdot 0|}{(1+4)^{3/2}} = \frac{2}{5\sqrt5}$.

> **Answer**: $\vec{v}(t) = (1,2t)$; $|\vec{v}(t)| = \sqrt{1+4t^2}$; $\kappa(1) = \frac{2}{5\sqrt5}$

### D14. Linear approximation (1st-order Taylor) of $\sqrt{x}$ at $a=4$; approximate $\sqrt{4.1}$.

$f(4) = 2$, $f'(x) = \frac{1}{2\sqrt{x}}$, $f'(4) = \frac{1}{4}$.
$L(x) = 2 + \frac{1}{4}(x-4)$.
$\sqrt{4.1} \approx L(4.1) = 2 + \frac{1}{4}(0.1) = 2.025$.
True value: $\sqrt{4.1} \approx 2.02485$ — error $\approx 1.5\times 10^{-4}$, tiny because $x$ is close to $a$.

> **Answer**: $L(x) = 2 + \tfrac14(x-4)$; $\sqrt{4.1} \approx 2.025$

### D15. Find $a,b$ so $f(x) = x^3 + ax + b$ has a local max at $(-1,2)$ and a local min at $(1,-2)$.

$f'(x) = 3x^2 + a$. Extrema need $f'(\pm 1) = 0$: $3 + a = 0$ → $a = -3$.
Local min at $(1,-2)$: $f(1) = 1 + a + b = 1 - 3 + b = -2 + b = -2$ → $b = 0$.
**Check** max: $f(-1) = -1 + 3 + 0 = 2$ ✓. So $f(x) = x^3 - 3x$.

> **Answer**: $a = -3$, $b = 0$ (i.e. $f(x) = x^3 - 3x$)

### D16. Curvature of $f(x) = \ln x$ at $x=1$ using $\kappa = \frac{|f''|}{(1+(f')^2)^{3/2}}$.

$f'(x) = \frac{1}{x}$, $f''(x) = -\frac{1}{x^2}$. At $x=1$: $f' = 1$, $f'' = -1$.
$\kappa = \frac{|-1|}{(1+1^2)^{3/2}} = \frac{1}{2\sqrt2} = \frac{\sqrt2}{4}$.

> **Answer**: $\kappa = \frac{\sqrt2}{4}$

### D17. Use Rolle's Theorem to show $f(x) = x^3 + x - 1$ has at most one real root.

**Contradiction argument**: suppose $f$ has two roots $a < b$. $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$ with $f(a) = f(b) = 0$, so Rolle gives $\exists c \in (a,b)$ with $f'(c) = 0$.
But $f'(x) = 3x^2 + 1 \geq 1 > 0$ for all $x$ — it can never be zero. Contradiction.

(Combined with the IVT — $f(0) = -1 < 0$, $f(1) = 1 > 0$ — there is exactly one real root, in $(0,1)$.)

> **Answer**: $f' = 3x^2+1 > 0$ makes two roots impossible; there is exactly one real root

---

## Advanced Drills

### A1. Prove that $f(x) = x^3 + ax + b$ has exactly one inflection point; find it and show it's always on the $y$-axis.

$f''(x) = 6x$. Zero at $x=0$, and $f''$ changes sign ($- \to +$) there → **one inflection point** at $(0, b)$.

Because this family has no $x^2$ term, the inflection sits at $x=0$ — on the $y$-axis — regardless of $a$ and $b$. (For a general cubic $Ax^3+Bx^2+Cx+D$, $f'' = 6Ax+2B$ puts the inflection at $x = -B/(3A)$; shifting by $+B/(3A)$ moves it to the origin.)

> **Answer**: inflection at $(0,b)$, always on the $y$-axis

### A2. $f(x) = \frac{x}{x^2+1}$: all extrema, asymptotes, inflection points. Sketch.

- **Domain**: all real $x$. **Odd** function (symmetric about origin).
- **Asymptote**: $y = 0$ (horizontal), since $\frac{x}{x^2+1} \to 0$ as $x \to \pm\infty$.
- **$f'$**: $f'(x) = \frac{(x^2+1) - x(2x)}{(x^2+1)^2} = \frac{1-x^2}{(x^2+1)^2}$. Critical $x = \pm 1$.
  - $x<-1$: $f'<0$ ↘; $(-1,1)$: $f'>0$ ↗; $x>1$: $f'<0$ ↘.
  - **min** at $(-1, -\tfrac12)$; **max** at $(1, \tfrac12)$.
- **$f''$**: $f''(x) = \frac{2x(x^2-3)}{(x^2+1)^3}$. Zero at $x = 0, \pm\sqrt3$, sign changes at each → inflection points $(0,0)$, $\left(\sqrt3, \tfrac{\sqrt3}{4}\right)$, $\left(-\sqrt3, -\tfrac{\sqrt3}{4}\right)$.

**Sketch**: a single "bump" above the axis on the right, mirror below on the left, decaying to $0$ at both ends — the classic damped-oscillation look.

> **Answer**: max $(1,\tfrac12)$; min $(-1,-\tfrac12)$; inflections $(0,0)$ and $\left(\pm\sqrt3, \pm\tfrac{\sqrt3}{4}\right)$; asymptote $y=0$

### A3. Prove $\frac{x}{1+x} < \ln(1+x) < x$ for $x>0$.

**Left inequality** — $F(x) = \ln(1+x) - \frac{x}{1+x}$:
$F'(x) = \frac{1}{1+x} - \frac{1}{(1+x)^2} = \frac{x}{(1+x)^2} > 0$ for $x>0$, and $F(0) = 0$. So $F(x) > 0$ → $\frac{x}{1+x} < \ln(1+x)$. ✓

**Right inequality** — $G(x) = x - \ln(1+x)$:
$G'(x) = 1 - \frac{1}{1+x} = \frac{x}{1+x} > 0$ for $x>0$, and $G(0)=0$. So $G(x)>0$ → $\ln(1+x) < x$. ✓

> **Answer**: both functions start at 0 and are strictly increasing, giving the double inequality

### A4. Find the point on $y = \sqrt{x}$ closest to $(2, 0)$.

Minimize $D^2 = (x-2)^2 + (\sqrt{x})^2 = x^2 - 3x + 4$.
$D' = 2x - 3 = 0$ → $x = \tfrac32$. $D'' = 2 > 0$ → minimum.
Point $\left(\tfrac32, \sqrt{\tfrac32}\right)$; minimum distance $\sqrt{D(\tfrac32)} = \sqrt{\tfrac94 - \tfrac92 + 4} = \sqrt{\tfrac74} = \tfrac{\sqrt7}{2}$.

> **Answer**: point $\left(\tfrac32, \sqrt{\tfrac32}\right)$; distance $\tfrac{\sqrt7}{2}$

### A5. For the cycloid $\vec{r}(t) = (t - \sin t,\; 1 - \cos t)$: find all $t$ where the tangent is horizontal.

$y'(t) = \sin t = 0$ → $t = n\pi$.
- $n$ odd: points $(n\pi, 2)$ — the **tops of the arches** (the geometric interpretation).
- $n$ even: points $(n\pi, 0)$ — the **cusps** where the curve touches the ground (also horizontal tangents).

> **Answer**: $t = n\pi$; odd multiples of $\pi$ are the arch tops $(n\pi, 2)$

### A6. A line through $(0,1)$ is tangent to $y = x^3$. Find the tangent line and its slope $m$.

Tangent at $(a, a^3)$: $y = 3a^2 x - 2a^3$. Require $(0,1)$ to lie on it:
$1 = -2a^3$ → $a^3 = -\tfrac12$ → $a = -\frac{1}{\sqrt[3]{2}}$.

Slope $m = 3a^2 = \frac{3}{\sqrt[3]{4}}$. Tangent: $y = \frac{3}{\sqrt[3]{4}}x + 1$.
**Check**: at $x=0$, $y=1$ ✓. Tangency point $\left(-\frac{1}{\sqrt[3]{2}}, -\frac12\right)$.

> **Answer**: $y = \frac{3}{\sqrt[3]{4}}x + 1$, slope $m = \frac{3}{\sqrt[3]{4}}$

### A7. $f(x) = x^4 - 8x^2 + 3$: all intervals of increase/decrease, concavity, extrema. Sketch.

$f'(x) = 4x^3 - 16x = 4x(x-2)(x+2)$. Critical $x = 0, \pm 2$.
- $(-\infty,-2)$: $f'<0$ ↘; $(-2,0)$: $f'>0$ ↗; $(0,2)$: $f'<0$ ↘; $(2,\infty)$: $f'>0$ ↗.
- **mins** at $(\pm 2, -13)$; **max** at $(0, 3)$.

$f''(x) = 12x^2 - 16 = 4(3x^2-4)$; zero at $x = \pm \frac{2}{\sqrt3}$, sign changes → inflections $\left(\pm \tfrac{2}{\sqrt3},\, -\tfrac{53}{9}\right)$.
Concave up outside $\left(-\tfrac{2}{\sqrt3}, \tfrac{2}{\sqrt3}\right)$, down inside.

**Sketch**: a symmetric "W" — two minima at $\pm 2$, a middle maximum at the origin.

> **Answer**: decreasing on $(-\infty,-2)\cup(0,2)$, increasing on $(-2,0)\cup(2,\infty)$; max $(0,3)$, mins $(\pm2,-13)$; inflections $\left(\pm\tfrac{2}{\sqrt3}, -\tfrac{53}{9}\right)$

### A8. Sketch $f(x) = x e^{-x}$ using $f, f', f''$. Find the global maximum.

- **$f'$**: $e^{-x}(1-x)$ → critical $x=1$; increasing on $(-\infty,1)$, decreasing on $(1,\infty)$.
- **$f''$**: $e^{-x}(x-2)$; $f''(1) = -e^{-1} < 0$ → **global max** at $(1, \tfrac1e)$. Inflection at $x=2$ ($f''$ changes sign), point $\left(2, \tfrac{2}{e^2}\right)$.
- **Limits**: as $x \to -\infty$, $f \to -\infty$ (the linear term wins); as $x \to +\infty$, $f \to 0^+$.

> **Answer**: global max $\tfrac1e$ at $x=1$; inflection $\left(2, \tfrac{2}{e^2}\right)$; $y\to 0^+$ as $x\to\infty$

### A9. Show $f(x) = x^3 - 3x + 1$ has exactly three real roots.

$f'(x) = 3x^2 - 3 = 0$ → $x = \pm 1$. $f(-1) = 3$ (local max), $f(1) = -1$ (local min). As $x\to -\infty$, $f\to -\infty$; as $x\to\infty$, $f\to\infty$.

By the IVT, the graph crosses the axis once on each interval:
- $(-\infty, -1)$: from $-\infty$ up to $3$ → one root;
- $(-1, 1)$: from $3$ down to $-1$ → one root;
- $(1, \infty)$: from $-1$ up to $\infty$ → one root.

A cubic has at most three roots, so exactly three.

> **Answer**: one root in each of $(-\infty,-1)$, $(-1,1)$, $(1,\infty)$ — three real roots total

### A10. Find the tangent to $f(x) = \ln x$ that passes through the origin.

Tangent at $(a, \ln a)$: $y - \ln a = \frac{1}{a}(x - a)$. Through $(0,0)$:
$-\ln a = -1$ → $\ln a = 1$ → $a = e$.
Tangent: $y - 1 = \frac{1}{e}(x - e)$ → $y = \frac{x}{e}$.

> **Answer**: $y = \frac{x}{e}$

### A11. For the logarithmic spiral $\vec{r}(t) = (e^t\cos t,\; e^t\sin t)$: find the angle between the position and velocity vectors. Show it's constant.

$\vec{r} = (e^t\cos t,\, e^t\sin t)$; $\vec{r}{\,}' = (e^t(\cos t - \sin t),\, e^t(\sin t + \cos t))$.

$\vec{r}\cdot\vec{r}{\,}' = e^{2t}\left[\cos t(\cos t-\sin t) + \sin t(\sin t+\cos t)\right] = e^{2t}(\cos^2 t + \sin^2 t) = e^{2t}$.

$|\vec{r}| = e^t$; $|\vec{r}{\,}'| = e^t\sqrt{(\cos t-\sin t)^2 + (\sin t+\cos t)^2} = e^t\sqrt{2}$.

$\cos\theta = \frac{\vec{r}\cdot\vec{r}{\,}'}{|\vec{r}|\,|\vec{r}{\,}'|} = \frac{e^{2t}}{\sqrt2\, e^{2t}} = \frac{1}{\sqrt2}$ → $\theta = 45^\circ$ for all $t$. ✓

> **Answer**: $\theta = 45^\circ$, constant — the defining property of the logarithmic spiral

### A12. A cubic $f(x) = ax^3 + bx^2 + cx + d$ has an inflection point at $x=0$. Show $b=0$, then find $a,c,d$ so it has a local max at $(-1,2)$ and a local min at $(1,0)$.

**Show $b=0$**: $f''(x) = 6ax + 2b$. An inflection at $x=0$ requires $f''(0) = 0$ → $2b = 0$ → $b = 0$. ✓

Now $f(x) = ax^3 + cx + d$, $f'(x) = 3ax^2 + c$.
- Extrema at $\pm 1$: $f'(-1) = 3a + c = 0$ and $f'(1) = 3a + c = 0$ → $c = -3a$.
- Max at $(-1,2)$: $f(-1) = -a - c + d = -a + 3a + d = 2a + d = 2$.
- Min at $(1,0)$: $f(1) = a + c + d = a - 3a + d = -2a + d = 0$ → $d = 2a$.

Substitute: $2a + d = 2a + 2a = 4a = 2$ → $a = \tfrac12$, $d = 1$, $c = -\tfrac32$.

**Verify**: $f(x) = \tfrac12 x^3 - \tfrac32 x + 1$; $f''(x) = 3x$; $f''(-1) = -3 < 0$ (max ✓), $f''(1) = 3 > 0$ (min ✓); $f(-1) = -\tfrac12 + \tfrac32 + 1 = 2$ ✓; $f(1) = \tfrac12 - \tfrac32 + 1 = 0$ ✓.

> **Answer**: $b=0$; $a = \tfrac12$, $c = -\tfrac32$, $d = 1$; $f(x) = \tfrac12 x^3 - \tfrac32 x + 1$
