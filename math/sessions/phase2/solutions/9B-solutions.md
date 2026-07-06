# Solutions: 9B — 2D Functions & Geometry

---

## Practice 1

> $f(x)=\frac{1}{x}$, $g(x)=x^2+1$.

$(f\circ g)(x) = f(x^2+1) = \frac{1}{x^2+1}$. Domain: $x^2+1 \neq 0$, always true → all reals.
$(g\circ f)(x) = g(\frac{1}{x}) = \frac{1}{x^2}+1$. Domain: $x \neq 0$.

---

## Practice 2

> $f(x) = \frac{3x-1}{x+4}$.

$y(x+4) = 3x-1 \to yx+4y = 3x-1 \to yx-3x = -4y-1 \to x(y-3) = -(4y+1)$.
$x = \frac{-(4y+1)}{y-3} = \frac{4y+1}{3-y}$. Swap: $f^{-1}(x) = \frac{4x+1}{3-x}$.

---

## Practice 3

**(a)** $x^2-4x + y^2+6y = 3$. Complete: $(x-2)^2 + (y+3)^2 = 3+4+9 = 16$. Circle, center $(2,-3)$, radius $4$.

**(b)** $\frac{x^2}{9} + \frac{y^2}{4} = 1$. Ellipse, center $(0,0)$. Semi-major $3$ (horizontal), semi-minor $2$. Foci: $c=\sqrt{9-4}=\sqrt{5}$, at $(\pm\sqrt{5},0)$.

**(c)** $\frac{y^2}{4} - \frac{x^2}{4} = 1$. Hyperbola, vertical opening. Asymptotes: $y=\pm x$. Vertices: $(0,\pm2)$.

---

## Practice 4

> $(3,1)$ to $4x+3y-10=0$ (rewrite as $4x+3y=10 \to 4x+3y-10=0$).

$d = \frac{|12+3-10|}{\sqrt{16+9}} = \frac{5}{5} = 1$.

---

## Practice 5

> $(3\cos t, 2\sin t)$, $t \in [0, 2\pi]$.

Ellipse: $\frac{x^2}{9} + \frac{y^2}{4} = 1$.
At $t=\pi/3$: $x=3\cos(\pi/3)=1.5$, $y=2\sin(\pi/3)=\sqrt{3}\approx1.732$. Point: $(1.5, \sqrt{3})$.

---

## Practice 6

> Closest point on $(x-3)^2+(y-4)^2=1$ to $(0,0)$.

Line from origin to center: direction $(3,4)$. Distance from origin to center: $5$.
Point on circle closest to origin: center minus radius along this direction.
$(3,4) - \frac{1}{5}(3,4) = (\frac{12}{5}, \frac{16}{5}) = (2.4, 3.2)$.
Tangent line at this point: perpendicular to radius. Slope of radius $4/3$, so tangent slope $-3/4$.
Line: $y-3.2 = -\frac{3}{4}(x-2.4) \to 3x+4y=20$.
Distance from origin to this line: $\frac{20}{5}=4$. Or directly: $5-1=4$.

→ **Distance = 4.**

---

## Basic Drill

**D1.** $(f\circ g)(4) = f(g(4)) = f(2) = 3(2)-2 = 4$.

**D2.** $f(x)=5x+2$. $y=5x+2 \to x=\frac{y-2}{5}$. $f^{-1}(x)=\frac{x-2}{5}$.
$f(f^{-1}(x)) = 5(\frac{x-2}{5})+2 = x-2+2 = x$. ✅

**D3.** $f(-x) = (-x)^4 - 3(-x)^2 = x^4 - 3x^2 = f(x)$. → **Even.**

**D4.** $(x^2+6x) + (y^2-10y) = -18$. $(x+3)^2 + (y-5)^2 = -18+9+25 = 16$. Center $(-3,5)$, radius $4$.

**D5.** $a=5$, $b=4$. Vertices: $(\pm5,0)$ and $(0,\pm4)$. $c=\sqrt{25-16}=3$. Foci: $(\pm3,0)$.

**D6.** $4p=8 \to p=2$. Vertex $(0,0)$, focus $(0,2)$, directrix $y=-2$.

**D7.** $a=3$, $b=2$. Asymptotes: $y = \pm\frac{2}{3}x$.

**D8.** $(x(t), y(t)) = (2+5\cos t,\; -3+5\sin t)$, $t \in [0, 2\pi]$.

**D9.** $d = \frac{|2(-1) - 5 + 3|}{\sqrt{4+1}} = \frac{|-4|}{\sqrt{5}} = \frac{4}{\sqrt{5}} = \frac{4\sqrt{5}}{5}$.

**D10.** $2\sin t = \sqrt{2} \to \sin t = \frac{\sqrt{2}}{2}$. $t = \frac{\pi}{4}, \frac{3\pi}{4}$.

---

## Advanced Drill

**A1.** $f^{-1}(x)=\frac{x-1}{2}$, $g^{-1}(x)=\sqrt[3]{x}$.
$(g^{-1}\circ f^{-1})(x) = \sqrt[3]{\frac{x-1}{2}}$.
$(f\circ g)(x)=2x^3+1$. Inverse: $y=2x^3+1 \to x=\sqrt[3]{\frac{y-1}{2}}$. → Same result. ✅

**A2.** Even: $\frac{(e^x+e^{-x})+(e^{-x}+e^x)}{2}=e^x+e^{-x}=f(x)$. Odd: $\frac{(e^x+e^{-x})-(e^{-x}+e^x)}{2}=0$.
$f$ is purely even.

**A3.** Focus $(2,3)$, directrix $y=-1$. Vertex halfway: $(2,1)$. $p=2$ (distance from vertex to focus).
Equation: $(x-2)^2 = 4\cdot2\cdot(y-1) \to (x-2)^2 = 8(y-1)$.

**A4.** Hyperbola centered at origin: $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$. Asymptotes: $\frac{b}{a}=\frac{2}{3}$.
Through $(3,0)$: $\frac{9}{a^2}=1 \to a^2=9$. Then $b=2a/3=2$. → $\frac{x^2}{9} - \frac{y^2}{4} = 1$.

**A5.** Parallel lines: $3x+4y=5$ and $3x+4y=-15$. Distance = $\frac{|5-(-15)|}{\sqrt{9+16}} = \frac{20}{5}=4$.

**A6.** Point on circle closest to $(7,1)$ lies along radius direction. Vector from origin: normalize $(7,1)$ → $\frac{(7,1)}{\sqrt{50}} = \frac{(7,1)}{5\sqrt{2}}$. Closest point: $5 \cdot \frac{(7,1)}{5\sqrt{2}} = \frac{(7,1)}{\sqrt{2}} = (\frac{7}{\sqrt{2}}, \frac{1}{\sqrt{2}}) \approx (4.95, 0.707)$.

**A7.** Through $(4,8)$: $t^2=4 \to t=\pm2$, $t^3=8 \to t=2$. So $t=2$.
Eliminate $t$: $t = \sqrt[3]{y}$ (or $t = y^{1/3}$), $x = y^{2/3}$. → $x^3 = y^2$.

**A8.** Line: $y-2=m(x-1)$. Substitute into $x^2+y^2=5$:
$x^2+(m(x-1)+2)^2=5$. For tangency, discriminant = 0.
$(1+m^2)x^2 + 2m(2-m)x + (m^2-4m-1) = 0$. Discriminant: $4m^2(2-m)^2 - 4(1+m^2)(m^2-4m-1)=0$.
Simplify: $12m^2 - 16m - 4 = 0 \to 3m^2-4m-1=0 \to m = \frac{4\pm\sqrt{16+12}}{6} = \frac{4\pm 2\sqrt{7}}{6} = \frac{2\pm\sqrt{7}}{3}$.

**A9.** Sum of distances to foci = constant. At $(0,4)$: $\sqrt{3^2+4^2}+\sqrt{(-3)^2+4^2}=5+5=10$. So $2a=10 \to a=5$.
$c=3$, $b^2=a^2-c^2=25-9=16$. Equation: $\frac{x^2}{25} + \frac{y^2}{16} = 1$.

**A10.** Quadrilateral vertices: $(0,0)\to(6,0)\to(4,4)\to(0,3)$. Compute area using shoelace formula and test $(2,2)$.
Shoelace: $0\cdot0+6\cdot4+4\cdot3+0\cdot0 - (0\cdot6+0\cdot4+4\cdot0+3\cdot0) = 0+24+12+0 = 36$. Area = $18$.
Now test if $(2,2)$ is inside by checking barycentric or by splitting. With point $(2,2)$, compute areas of 4 triangles formed with edges. If sum = 18, inside.
Tri-1 $(0,0),(6,0),(2,2)$: area $6$. Tri-2 $(6,0),(4,4),(2,2)$: area $4$. Tri-3 $(4,4),(0,3),(2,2)$: area $4$. Tri-4 $(0,3),(0,0),(2,2)$: area $3$. Sum = $17 \neq 18$. → $(2,2)$ is **outside** (slightly).
