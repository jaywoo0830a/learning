# Solutions — 15B: Optimization and Related Rates — Geometry in Motion

> Back to [15B — Optimization and Related Rates](../15B-optimization-related-rates.md)

---

## Practice 1

**Find two positive numbers whose product is 100 and sum is minimized.**

① **Objective**: minimize $S = x + y$ with constraint $xy = 100$.

② **Reduce to one variable**: $y = \frac{100}{x}$, so $S(x) = x + \frac{100}{x}$, $x > 0$.

③ **Differentiate**: $S'(x) = 1 - \frac{100}{x^2} = 0$ → $x^2 = 100$ → $x = 10$ (reject $-10$).

④ **Verify**: $S''(x) = \frac{200}{x^3} > 0$ → minimum. $y = \frac{100}{10} = 10$.

> **Answer**: $10$ and $10$; minimum sum $= 20$

---

## Practice 2

**A cylindrical can (with top) must hold 1 liter (1000 cm³). Minimize the surface area. Find the optimal radius, height, and the ratio $h/r$.**

① **Constraint**: $V = \pi r^2 h = 1000$ → $h = \frac{1000}{\pi r^2}$.

② **Objective**: $S = 2\pi r^2 + 2\pi r h = 2\pi r^2 + \frac{2000}{r}$.

③ **Differentiate**: $S'(r) = 4\pi r - \frac{2000}{r^2} = 0$ → $4\pi r^3 = 2000$ → $r^3 = \frac{500}{\pi}$ → $r = \left(\frac{500}{\pi}\right)^{1/3} \approx 5.42$ cm.

④ **Verify**: $S''(r) = 4\pi + \frac{4000}{r^3} > 0$ → minimum. $h = \frac{1000}{\pi r^2} = 2r \approx 10.84$ cm.

Ratio $\frac{h}{r} = 2$. Minimum area $S = 2\pi r^2 + 2\pi r(2r) = 6\pi r^2 = 6\pi\left(\frac{500}{\pi}\right)^{2/3} \approx 553.7$ cm².

> **Answer**: $r \approx 5.42$ cm, $h \approx 10.84$ cm, $h/r = 2$, $S_{\min} \approx 553.7$ cm²

---

## Practice 3

**A spherical balloon inflates at 100 cm³/s. How fast does the radius grow when $r = 5$ cm?**

$V = \frac43\pi r^3$ → $\frac{dV}{dt} = 4\pi r^2 \frac{dr}{dt}$.

At $r=5$: $100 = 4\pi (25) \frac{dr}{dt}$ → $\frac{dr}{dt} = \frac{100}{100\pi} = \frac{1}{\pi} \approx 0.318$ cm/s.

> **Answer**: $\frac{dr}{dt} = \frac{1}{\pi}$ cm/s $\approx 0.318$ cm/s

---

## Practice 4: Real Battle

**Car A goes north through an intersection at 60 km/h. Car B goes east through the same intersection at 80 km/h, but leaves 1 hour later. How fast is the distance between them increasing 2 hours after car A passes the intersection?**

① **Positions at $t = 2$** (hours after A passes): A has traveled $y = 60\cdot 2 = 120$ km north; B has traveled $x = 80(2-1) = 80$ km east.

② **Constraint**: $s^2 = x^2 + y^2$, so $s = \sqrt{80^2 + 120^2} = \sqrt{6400 + 14400} = \sqrt{20800} = 40\sqrt{13} \approx 144.2$ km.

③ **Differentiate**: $2s\frac{ds}{dt} = 2x\frac{dx}{dt} + 2y\frac{dy}{dt}$ → $\frac{ds}{dt} = \frac{x\frac{dx}{dt} + y\frac{dy}{dt}}{s}$.

④ **Plug in**: $\frac{ds}{dt} = \frac{80\cdot 80 + 120\cdot 60}{40\sqrt{13}} = \frac{6400 + 7200}{40\sqrt{13}} = \frac{13600}{40\sqrt{13}} = \frac{340}{\sqrt{13}} \approx 94.3$ km/h.

**Why not $100$ km/h?** Because B started an hour late, the position vector is NOT $(80t, 60t)$ — at the measuring moment the relative velocity argument from Example 11 no longer applies. The separation speed is not constant.

> **Answer**: $\frac{ds}{dt} = \frac{340}{\sqrt{13}} \approx 94.3$ km/h

---

## Practice 5: Distance Minimization

**Find the point on the line $y = 2x + 1$ closest to the origin. Solve two different ways and verify they agree.**

**(a) Squared distance**: $D^2 = x^2 + (2x+1)^2 = 5x^2 + 4x + 1$.
$D' = 10x + 4 = 0$ → $x = -\frac25$. Then $y = 2\left(-\frac25\right) + 1 = \frac15$. $D'' = 10 > 0$ → minimum.
Point $\left(-\frac25, \frac15\right)$, distance $\sqrt{D^2} = \sqrt{5\cdot\frac{4}{25} + 4\left(-\frac25\right) + 1} = \sqrt{\frac15} = \frac{\sqrt5}{5}$.

**(b) Perpendicular line**: the line's slope is $2$, so the perpendicular through the origin is $y = -\frac12 x$. Intersect: $2x + 1 = -\frac12 x$ → $\frac52 x = -1$ → $x = -\frac25$, $y = \frac15$. Same point ✓.

> **Answer**: point $\left(-\frac25, \frac15\right)$, distance $\frac{\sqrt5}{5}$ — both methods agree

---

## Practice 6: Related Rates — Volume

**A spherical snowball melts at $\frac{dV}{dt} = -kS$, $S = 4\pi r^2$. Show $\frac{dr}{dt}$ is constant. If the radius drops from 10 cm to 9 cm in 30 minutes, when is it completely melted?**

① $\frac{dV}{dt} = 4\pi r^2 \frac{dr}{dt} = -k(4\pi r^2)$ → cancel $4\pi r^2$: $\frac{dr}{dt} = -k$ — **constant** (independent of $r$). ✓

② From $10 \to 9$ cm in 30 min: $k = \frac{1}{30}$ cm/min.

③ Melted when $r = 0$: starting at 10 cm, time $= \frac{10}{1/30} = 300$ minutes $= 5$ hours.

> **Answer**: $\frac{dr}{dt} = -k$ (constant); completely melted after $5$ hours

---

## Practice 7: Exponential Optimization

**Population $P(t) = 1000e^{0.03t}$ (3%/yr growth). Per-capita consumption $C(t) = 50e^{-0.05t}$ (5%/yr improvement). Total consumption $R(t) = P(t)C(t)$.**

**(a)** $R(t) = 1000e^{0.03t} \cdot 50e^{-0.05t} = 50000\, e^{-0.02t}$.
$R'(t) = 50000(-0.02)e^{-0.02t} = -1000\,e^{-0.02t} < 0$ for all $t$ → **strictly decreasing**.
Maximum occurs at $t=0$: $R(0) = 50000$. As $t \to \infty$, $R \to 0$.

**(b)** With $C(t) = 50e^{-rt}$: $R(t) = 50000\, e^{(0.03 - r)t}$. The net rate is $0.03 - r$:
- (i) grows forever when $r < 0.03$ (growth outpaces efficiency);
- (ii) stays constant when $r = 0.03$ (exactly balanced);
- (iii) declines when $r > 0.03$ (efficiency outpaces growth).

**Interpretation**: to ever reduce total resource use, the per-capita efficiency improvement rate must exceed the population growth rate.

> **Answer**: (a) $R(t) = 50000e^{-0.02t}$, max $50000$ at $t=0$; (b) $r<0.03$ grows, $r=0.03$ constant, $r>0.03$ declines

---

## Practice 8: Real Battle

**Find the point on the plane $x + 2y + 3z = 6$ closest to the origin, and the shortest distance. Solve two different ways and verify they agree.**

**(a) Normal-vector shortcut**: $\vec{n} = (1,2,3)$, $|\vec{n}| = \sqrt{1+4+9} = \sqrt{14}$. The closest point lies on the line through the origin parallel to $\vec{n}$: $\vec{r}(t) = t(1,2,3) = (t, 2t, 3t)$.
Plug into the plane: $t + 2(2t) + 3(3t) = 6$ → $t + 4t + 9t = 6$ → $14t = 6$ → $t = \frac37$.
Closest point $\left(\frac37, \frac67, \frac97\right)$. Distance $= |\vec{n}| \cdot t = \sqrt{14}\cdot\frac37 = \frac{3\sqrt{14}}{7}$.

**(b) Distance formula**: plane $x + 2y + 3z - 6 = 0$, point $(0,0,0)$:
$d = \frac{|1\cdot 0 + 2\cdot 0 + 3\cdot 0 - 6|}{\sqrt{1^2+2^2+3^2}} = \frac{6}{\sqrt{14}} = \frac{6\sqrt{14}}{14} = \frac{3\sqrt{14}}{7}$ ✓ — same distance.

> **Answer**: point $\left(\frac37, \frac67, \frac97\right)$; distance $\frac{3\sqrt{14}}{7}$ — both methods agree

---

## Basic Drills

### D1. Maximum of $f(x) = -x^2 + 6x - 5$.

$f'(x) = -2x + 6 = 0$ → $x = 3$. $f'' = -2 < 0$ → max. $f(3) = -9 + 18 - 5 = 4$.

> **Answer**: max $4$ at $x = 3$

### D2. Minimize $f(x) = x^2 + \frac{16}{x}$ for $x > 0$.

$f'(x) = 2x - \frac{16}{x^2} = 0$ → $2x^3 = 16$ → $x = 2$. $f'' = 2 + \frac{32}{x^3} > 0$ → min. $f(2) = 4 + 8 = 12$.

> **Answer**: min $12$ at $x = 2$

### D3. A rectangle has perimeter 40. Maximize its area. What shape gives the maximum?

$x + y = 20$ → $A = xy = x(20-x) = 20x - x^2$. $A' = 20 - 2x = 0$ → $x = 10$, $y = 10$.

> **Answer**: a $10 \times 10$ square; max area $100$

### D4. $V = \frac43\pi r^3$, $\frac{dr}{dt} = 2$. Find $\frac{dV}{dt}$ when $r=3$.

$\frac{dV}{dt} = 4\pi r^2 \frac{dr}{dt} = 4\pi(9)(2) = 72\pi$.

> **Answer**: $\frac{dV}{dt} = 72\pi$

### D5. $x^2 + y^2 = 100$, $\frac{dx}{dt} = 3$. Find $\frac{dy}{dt}$ when $x=6, y=8$.

$2x\frac{dx}{dt} + 2y\frac{dy}{dt} = 0$ → $2(6)(3) + 2(8)\frac{dy}{dt} = 0$ → $36 + 16\frac{dy}{dt} = 0$ → $\frac{dy}{dt} = -\frac94$.

> **Answer**: $\frac{dy}{dt} = -\frac{9}{4}$

### D6. Find the point on $y = x^2$ closest to $(0, 1)$.

$D^2 = x^2 + (x^2 - 1)^2 = x^4 - x^2 + 1$. $D' = 4x^3 - 2x = 2x(2x^2 - 1) = 0$ → $x = 0$ or $x = \pm\frac{1}{\sqrt2}$.
- $x=0$: $D^2 = 1$ — this is a local **max** of $D^2$ (check: $D''(0) = -2 < 0$).
- $x = \pm\frac{1}{\sqrt2}$: $x^2 = \frac12$ and $(x^2-1)^2 = \frac14$, so $D^2 = \frac12 + \frac14 = \frac34$ → minimum.

Points $\left(\pm\frac{1}{\sqrt2}, \frac12\right)$, distance $\frac{\sqrt3}{2}$.

> **Answer**: points $\left(\pm\frac{1}{\sqrt2}, \frac12\right)$; distance $\frac{\sqrt3}{2}$

### D7. A 10 m ladder: bottom slides at 2 m/s. Find $\frac{dy}{dt}$ when the bottom is 6 m from the wall.

$x^2 + y^2 = 100$ → at $x=6$: $y = 8$. $2x\frac{dx}{dt} + 2y\frac{dy}{dt} = 0$ → $\frac{dy}{dt} = -\frac{x}{y}\frac{dx}{dt} = -\frac{6}{8}(2) = -\frac32$ m/s.

> **Answer**: $\frac{dy}{dt} = -\frac32$ m/s (falling)

### D8. Maximize $f(x) = x(10-x)$ on $[0, 10]$.

$f' = 10 - 2x = 0$ → $x = 5$, $f(5) = 25$. Endpoints: $f(0) = f(10) = 0$.

> **Answer**: max $25$ at $x=5$

### D9. Water fills a cylindrical tank (radius 3 m) at 5 m³/min. Find $\frac{dh}{dt}$.

$V = \pi r^2 h = 9\pi h$ → $\frac{dV}{dt} = 9\pi \frac{dh}{dt} = 5$ → $\frac{dh}{dt} = \frac{5}{9\pi}$ m/min.

> **Answer**: $\frac{dh}{dt} = \frac{5}{9\pi} \approx 0.177$ m/min

### D10. $y = \sqrt{x}$, $\frac{dx}{dt} = 4$. Find $\frac{dy}{dt}$ when $x = 9$.

$\frac{dy}{dt} = \frac{1}{2\sqrt{x}}\frac{dx}{dt} = \frac{1}{2\cdot 3}(4) = \frac23$.

> **Answer**: $\frac{dy}{dt} = \frac{2}{3}$

### D11. Maximize $f(x) = x e^{-x}$ on $[0, \infty)$.

$f' = e^{-x}(1-x) = 0$ → $x = 1$. $f''(1) = e^{-1}(-1) < 0$ → max. $f(1) = \frac1e$.

> **Answer**: max $\frac1e$ at $x = 1$

### D12. A rectangle is inscribed in a circle of radius 5. Maximize its area.

Diagonal = diameter = 10. If sides are $a, b$: $a^2 + b^2 = 100$. $A = ab \leq \frac{a^2+b^2}{2} = 50$, equality when $a = b = 5\sqrt2$.

> **Answer**: square of side $5\sqrt2$; max area $50$

### D13. Find the point on $y = \cosh x$ closest to the origin.

Minimize $D^2 = x^2 + \cosh^2 x$. $D' = 2x + 2\cosh x\sinh x = 2x + \sinh(2x)$.
For $x<0$: both $2x<0$ and $\sinh(2x)<0$ → $D'<0$. For $x>0$: $D'>0$. So the minimum is at $x=0$.

> **Answer**: point $(0, 1)$; distance $1$

### D14. A box with a square base and open top must have volume 32 m³. Minimize surface area.

Base $x \times x$, height $h$: $x^2 h = 32$ → $h = \frac{32}{x^2}$.
$S = x^2 + 4xh = x^2 + \frac{128}{x}$. $S' = 2x - \frac{128}{x^2} = 0$ → $2x^3 = 128$ → $x = 4$, $h = 2$.
$S_{\min} = 16 + 4\cdot 4\cdot 2 = 48$.

> **Answer**: base $4 \times 4$, height $2$; min area $48$ m²

### D15. Position $(x(t), y(t)) = (t^2, t^3)$. Rate of change of distance from origin at $t=2$.

At $t=2$: $x=4$, $y=8$, $\frac{dx}{dt}=4$, $\frac{dy}{dt}=12$, $s = \sqrt{16+64} = 4\sqrt5$.
Differentiate $s^2 = x^2 + y^2$: $s\frac{ds}{dt} = x\frac{dx}{dt} + y\frac{dy}{dt} = 16 + 96 = 112$.
$\frac{ds}{dt} = \frac{112}{4\sqrt5} = \frac{28}{\sqrt5} \approx 12.52$.

> **Answer**: $\frac{ds}{dt} = \frac{28}{\sqrt5} \approx 12.52$

### D16. A searchlight 50 m from a wall rotates at 3 rad/min. How fast does the spot move when the beam makes a $30^\circ$ angle with the perpendicular?

$x = 50\tan\theta$ → $\frac{dx}{dt} = 50\sec^2\theta \frac{d\theta}{dt}$.
At $\theta = 30^\circ$: $\sec^2 30^\circ = \frac{4}{3}$, $\frac{d\theta}{dt} = 3$.
$\frac{dx}{dt} = 50 \cdot \frac43 \cdot 3 = 200$ m/min.

> **Answer**: $\frac{dx}{dt} = 200$ m/min

### D17. Absolute maximum AND minimum of $f(x) = -x^2 + 4x$ on $[0, 5]$.

$f'(x) = -2x + 4 = 0$ → $x = 2$ (critical point). Compare all candidates:
$f(2) = -4 + 8 = 4$; $f(0) = 0$; $f(5) = -25 + 20 = -5$.

> **Answer**: absolute max $4$ at $x=2$; absolute min $-5$ at the endpoint $x=5$

---

## Advanced Drills

### A1. A wire of length $L$ is cut into two pieces: one forms a circle, the other a square. How should you cut to (a) minimize total area, (b) maximize total area?

Let the circle use length $x$, the square $L - x$. Circle radius $\frac{x}{2\pi}$; square side $\frac{L-x}{4}$.
$A(x) = \frac{x^2}{4\pi} + \frac{(L-x)^2}{16}$.

**(a) Minimize**: $A'(x) = \frac{x}{2\pi} - \frac{L-x}{8} = 0$ → $4x = \pi(L-x)$ → $x = \frac{\pi L}{4+\pi}$.
Circle radius $= \frac{L}{2(4+\pi)}$; square side $= \frac{L}{4+\pi}$. This is the minimum ($A'' = \frac{1}{2\pi} + \frac18 > 0$).

**(b) Maximize**: the only critical point is a minimum, so the maximum is at an endpoint of $[0, L]$:
- all square: $A(0) = \frac{L^2}{16}$;
- all circle: $A(L) = \frac{L^2}{4\pi}$.
Since $\frac{1}{4\pi} \approx 0.0796 > \frac{1}{16} = 0.0625$, the **all-circle** cut wins.

> **Answer**: (a) cut at $x = \frac{\pi L}{4+\pi}$; (b) don't cut — make the whole wire a circle, area $\frac{L^2}{4\pi}$

### A2. A Norman window (rectangle topped by a semicircle) has fixed perimeter $P$. Find the width and height that maximize the area.

Rectangle $2x$ wide, $y$ tall; semicircle radius $x$ on top. Perimeter:
$P = 2y + 2x + \pi x$ → $y = \frac{P - (2+\pi)x}{2}$.

Area: $A = 2xy + \frac12 \pi x^2 = x(P - (2+\pi)x) + \frac{\pi}{2}x^2 = Px - \left(2 + \frac{\pi}{2}\right)x^2$.

$A'(x) = P - (4+\pi)x = 0$ → $x = \frac{P}{4+\pi}$. $A'' = -(4+\pi) < 0$ → maximum.

$y = \frac{P - (2+\pi)\frac{P}{4+\pi}}{2} = \frac{P}{4+\pi}$.

So width $= 2x = \frac{2P}{4+\pi}$ and height $= y = \frac{P}{4+\pi}$. At the optimum $y = x$: the rectangle is exactly as tall as the semicircle's radius.

> **Answer**: width $\frac{2P}{4+\pi}$, height $\frac{P}{4+\pi}$ (rectangle height = semicircle radius)

### A3. A trough is 10 m long with isosceles triangular ends (1 m wide at top, 0.5 m deep). Water pours in at 0.2 m³/min. How fast does water rise when depth is 0.3 m?

By similar triangles, at depth $h$ the surface width is $w = 2h$ (since $w/h = 1/0.5$).
$V = \frac12 \cdot w \cdot h \cdot L = \frac12 (2h)(h)(10) = 10h^2$.
$\frac{dV}{dt} = 20h \frac{dh}{dt} = 0.2$ → at $h=0.3$: $20(0.3)\frac{dh}{dt} = 0.2$ → $\frac{dh}{dt} = \frac{0.2}{6} = \frac{1}{30} \approx 0.0333$ m/min.

> **Answer**: $\frac{dh}{dt} = \frac{1}{30}$ m/min $\approx 0.0333$ m/min

### A4. Cylindrical tank: base costs \$3/m², sides \$2/m². Volume $= 100\pi$ m³. Minimize cost. What is the optimal $h/r$?

$V = \pi r^2 h = 100\pi$ → $h = \frac{100}{r^2}$.
Cost $C = 3\pi r^2 + 2(2\pi r h) = 3\pi r^2 + 4\pi r h = 3\pi r^2 + \frac{400\pi}{r}$.
$C'(r) = 6\pi r - \frac{400\pi}{r^2} = 0$ → $6r^3 = 400$ → $r^3 = \frac{200}{3}$ → $r = \left(\frac{200}{3}\right)^{1/3} \approx 4.05$ m.
$\frac{h}{r} = \frac{100/r^2}{r} = \frac{100}{r^3} = \frac{100}{200/3} = \frac32$.
$h = \frac32 r \approx 6.07$ m.

> **Answer**: $r \approx 4.05$ m, $h \approx 6.07$ m, optimal $h/r = \frac32$

### A5. Ship A sails east at 20 km/h from a port. Ship B sails north at 15 km/h toward the port from a point 100 km south. When are they closest? Minimum distance?

A at $(20t, 0)$; B at $(0, 100 - 15t)$.
$d^2 = (20t)^2 + (100 - 15t)^2$.
$\frac{d}{dt}(d^2) = 800t - 30(100 - 15t) = 800t - 3000 + 450t = 1250t - 3000 = 0$ → $t = 2.4$ hours.
$d^2 = 400(5.76) + (100-36)^2 = 2304 + 4096 = 6400$ → $d = 80$ km.

> **Answer**: closest at $t = 2.4$ h; minimum distance $80$ km

### A6. Find the maximum of $f(x) = x^{1/x}$ for $x > 0$.

$\ln f = \frac{\ln x}{x}$ → $\frac{f'}{f} = \frac{1 - \ln x}{x^2}$. Set $=0$: $\ln x = 1$ → $x = e$.
Since $\frac{1-\ln x}{x^2}$ goes $+ \to -$, this is a maximum. $f(e) = e^{1/e} \approx 1.4447$.

> **Answer**: max $e^{1/e} \approx 1.4447$ at $x = e$

### A7. A 2 m tall man walks away from a 6 m lamppost at 1.5 m/s. How fast does (a) the tip of his shadow move, (b) his shadow lengthen?

Let $x$ = man's distance from post, $s$ = distance of shadow tip from post. Similar triangles:
$\frac{s}{6} = \frac{s-x}{2}$ → $2s = 6(s-x)$ → $4s = 6x$ → $s = 1.5x$.

(a) $\frac{ds}{dt} = 1.5 \frac{dx}{dt} = 1.5(1.5) = 2.25$ m/s.
(b) shadow length $= s - x = 0.5x$ → $\frac{d}{dt}(s-x) = 0.5(1.5) = 0.75$ m/s.

> **Answer**: (a) tip moves at $2.25$ m/s; (b) shadow lengthens at $0.75$ m/s

### A8. Find the point on the ellipse $x^2/4 + y^2/9 = 1$ farthest from $(1, 0)$.

Parametrize $x = 2\cos t$, $y = 3\sin t$. Squared distance:
$D(t) = (2\cos t - 1)^2 + (3\sin t)^2 = -5\cos^2 t - 4\cos t + 10$.
With $u = \cos t \in [-1,1]$: $D(u) = -5u^2 - 4u + 10$ (a downward parabola → interior maximum).
$D'(u) = -10u - 4 = 0$ → $u = -0.4$. $D(-0.4) = -5(0.16) + 1.6 + 10 = 10.8$.

Point: $\cos t = -0.4$ → $x = -0.8 = -\frac45$; $\sin t = \pm\sqrt{0.84} = \pm\frac{\sqrt{21}}{5}$ → $y = \pm\frac{3\sqrt{21}}{5}$.
Distance $\sqrt{10.8} = \sqrt{\frac{54}{5}} \approx 3.286$.

> **Answer**: points $\left(-\frac45, \pm\frac{3\sqrt{21}}{5}\right)$; distance $\sqrt{\frac{54}{5}}$

### A9. Oil spills in a circle. Radius grows at 0.5 km/h. When $r = 10$ km, how fast is the area growing? Also: with constant thickness 1 mm, how fast is the volume growing?

$A = \pi r^2$ → $\frac{dA}{dt} = 2\pi r \frac{dr}{dt} = 2\pi(10)(0.5) = 10\pi$ km²/h $\approx 31.4$ km²/h.

Volume with thickness $h = 1$ mm $= 10^{-6}$ km: $V = \pi r^2 h$.
$\frac{dV}{dt} = 2\pi r h \frac{dr}{dt} = 2\pi(10)(10^{-6})(0.5) = 10\pi \times 10^{-6} = \pi \times 10^{-5}$ km³/h $\approx 31{,}416$ m³/h.

> **Answer**: $\frac{dA}{dt} = 10\pi$ km²/h; $\frac{dV}{dt} = \pi\times 10^{-5}$ km³/h $\approx 31{,}416$ m³/h

### A10. A cone is inscribed in a sphere of radius $R$. Maximize the cone's volume.

Let cone height be $H$ (apex on the sphere). The base circle is at distance $R - H$ from the center, so $r^2 + (R-H)^2 = R^2$ → $r^2 = 2RH - H^2 = H(2R-H)$.
$V = \frac13 \pi r^2 H = \frac{\pi}{3} H^2 (2R - H)$.
$\frac{dV}{dH} = \frac{\pi}{3}(4RH - 3H^2) = \frac{\pi H}{3}(4R - 3H) = 0$ → $H = \frac{4R}{3}$.
$r^2 = \frac{4R}{3}\left(2R - \frac{4R}{3}\right) = \frac{4R}{3}\cdot\frac{2R}{3} = \frac{8R^2}{9}$.
$V_{\max} = \frac{\pi}{3}\cdot\frac{8R^2}{9}\cdot\frac{4R}{3} = \frac{32\pi R^3}{81}$.

> **Answer**: $V_{\max} = \frac{32}{81}\pi R^3$ at $H = \frac{4R}{3}$

### A11. A hemispherical tank (radius 2 m): water pours in at 1 m³/min. Find $\frac{dh}{dt}$ when $h = 1$ m.

$V = \pi h^2\left(R - \frac{h}{3}\right)$ → $\frac{dV}{dh} = 2\pi h\left(R - \frac{h}{3}\right) + \pi h^2\left(-\frac13\right) = 2\pi h R - \frac{2\pi h^2}{3} - \frac{\pi h^2}{3} = \pi h(2R - h)$.

At $R=2$, $h=1$: $\frac{dV}{dh} = \pi(1)(4-1) = 3\pi$.
$\frac{dh}{dt} = \frac{dV/dt}{dV/dh} = \frac{1}{3\pi} \approx 0.106$ m/min.

> **Answer**: $\frac{dh}{dt} = \frac{1}{3\pi} \approx 0.106$ m/min

### A12. Profit $P(x) = 1000\ln(x+1) - 5x$. Find the optimal production level $x$. Why does profit eventually decrease despite $\ln(x+1)$ growing forever?

$P'(x) = \frac{1000}{x+1} - 5 = 0$ → $\frac{1000}{x+1} = 5$ → $x+1 = 200$ → $x = 199$.
$P''(x) = -\frac{1000}{(x+1)^2} < 0$ → maximum. $P(199) = 1000\ln 200 - 995 \approx 1000(5.298) - 995 \approx 4303$.

**Interpretation**: marginal benefit $\frac{1000}{x+1}$ shrinks toward 0 as $x$ grows (logarithms grow ever more slowly), while marginal cost stays constant at $5$. Once $x > 199$, each extra unit of production costs more than it returns — profit falls even though $\ln(x+1)$ keeps growing.

> **Answer**: optimal $x = 199$, max profit $\approx 4303$; marginal benefit decays to 0 while marginal cost is constant
