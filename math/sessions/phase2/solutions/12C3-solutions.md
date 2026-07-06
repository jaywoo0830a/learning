# Solutions: Session 12C3 — Coordinate Systems and Geometric Optimization

---

## Practice 1

$x = r\cos\theta$, $y = r\sin\theta$. Then $x^2 - y^2 = r^2\cos^2\theta - r^2\sin^2\theta = r^2(\cos^2\theta - \sin^2\theta) = r^2\cos 2\theta = 1$.

So $r^2\cos 2\theta = 1$, or $r^2 = \sec 2\theta$ (valid for $\cos 2\theta > 0$, i.e., $-\pi/4 < \theta < \pi/4$ and $3\pi/4 < \theta < 5\pi/4$).

---

## Practice 2

Line: $\vec{r}(t) = (2 + t,\; 1 - t,\; 0 + t)$.
Plane: $3x + y + 2z = 10$.

Plug: $3(2+t) + (1-t) + 2(t) = 10$.
$6 + 3t + 1 - t + 2t = 10$.
$7 + 4t = 10 \implies 4t = 3 \implies t = 3/4$.

Intersection point: $(2 + 3/4,\; 1 - 3/4,\; 3/4) = (11/4,\; 1/4,\; 3/4)$.

---

## Practice 3

Line through origin with direction $\vec{d} = (1, 1, 1)$. Point $\vec{p} = (1, 2, 3)$.

$|\vec{d}| = \sqrt{3}$. $\vec{v} = \vec{p} - \vec{0} = (1, 2, 3)$.

Cross product method: distance = $\frac{|\vec{v} \times \vec{d}|}{|\vec{d}|}$.

$\vec{v} \times \vec{d} = \det\begin{pmatrix}\hat{i}&\hat{j}&\hat{k}\\1&2&3\\1&1&1\end{pmatrix} = \hat{i}(2\cdot1 - 3\cdot1) - \hat{j}(1\cdot1 - 3\cdot1) + \hat{k}(1\cdot1 - 2\cdot1)$
$= \hat{i}(-1) - \hat{j}(-2) + \hat{k}(-1) = (-1, 2, -1)$.

$|\vec{v} \times \vec{d}| = \sqrt{1 + 4 + 1} = \sqrt{6}$.

Distance = $\frac{\sqrt{6}}{\sqrt{3}} = \sqrt{2}$.

---

## Practice 4

We want the closest point on the sphere $x^2+y^2+z^2=25$ to $(10, 0, 0)$. Geometrically, the closest point is along the line from the origin to $(10, 0, 0)$, which is the positive $x$-axis. On the sphere of radius 5, the closest point is $(5, 0, 0)$.

Using Lagrange multipliers: minimize $(x-10)^2 + y^2 + z^2$ subject to $x^2+y^2+z^2=25$.

$\nabla f = (2(x-10), 2y, 2z)$, $\nabla g = (2x, 2y, 2z)$.
$\nabla f = \lambda \nabla g \implies (x-10, y, z) = \lambda(x, y, z)$.

From $y$ and $z$: $y = \lambda y$, $z = \lambda z$. If $y \neq 0$ or $z \neq 0$, then $\lambda = 1$.
If $\lambda = 1$, then $x-10 = x \implies -10 = 0$, impossible.
So $y = 0$, $z = 0$. Then $x^2 = 25 \implies x = \pm 5$.
The closer to $(10,0,0)$ is $x = 5$. Closest point: $(5, 0, 0)$.

Distance = $|10 - 5| = 5$.

---

## Practice 5

Point = $0.5\vec{A} + 0.3\vec{B} + 0.2\vec{C} = 0.5(0,0) + 0.3(4,0) + 0.2(0,3) = (1.2,\; 0.6)$.

Check: $0.5 + 0.3 + 0.2 = 1$ ✅.

---

## Practice 6

Points: $P_1(0,0)$, $P_2(3,0)$, $P_3(3,2)$, $P_4(1,1)$.

Visual inspection: plot the points. $P_1, P_2, P_3$ form a right triangle. $P_4(1,1)$ is inside that triangle.
The convex hull vertices are $P_1, P_2, P_3$.

To verify $P_4$ is inside: check barycentric coordinates relative to $\triangle P_1P_2P_3$.

Solve $(1,1) = \alpha(0,0) + \beta(3,0) + \gamma(3,2)$ with $\alpha+\beta+\gamma=1$.
$x$: $1 = 0\alpha + 3\beta + 3\gamma = 3(\beta+\gamma)$.
$y$: $1 = 0\alpha + 0\beta + 2\gamma = 2\gamma \implies \gamma = 0.5$.

Then $\beta+\gamma = 1/3 \implies \beta = 1/3 - 0.5 = -1/6$.
$\alpha = 1 - \beta - \gamma = 1 - (-1/6) - 0.5 = 2/3$.

$\beta = -1/6 < 0$, so $(1,1)$ is **outside** the triangle $P_1P_2P_3$. But wait — $P_4$ has $\beta < 0$, meaning it's outside.

Check: $P_2(3,0)$, $P_3(3,2)$ form a vertical edge. $P_4(1,1)$ has $x=1 < 3$, so it's inside the half-plane determined by that edge. But $\beta < 0$ means it's "on the wrong side" of edge $P_1P_3$ or $P_1P_2$.

Actually, let's double-check. The triangle $P_1P_2P_3$ has edges: $P_1\to P_2$ along $x$-axis, $P_2\to P_3$ vertical, $P_3\to P_1$ diagonal $y = \frac{2}{3}x$.

$P_4(1,1)$: $y = 1$, $\frac{2}{3}x = \frac{2}{3}$ at $x=1$. $1 > 2/3$, so $P_4$ is **above** the hypotenuse — outside the triangle.

Convex hull of all 4 points: all four are vertices? Let's check. $P_1(0,0)$, $P_2(3,0)$, $P_3(3,2)$, $P_4(1,1)$.
The convex hull must contain all 4 points. $P_4(1,1)$ is above the line $P_1P_3$? Actually $P_3(3,2)$ and $P_1(0,0)$: line is $y = \frac{2}{3}x$. At $x=1$, $y=2/3$. $P_4$ has $y=1 > 2/3$. So $P_4$ is **above** $P_1P_3$. Together with $P_3(3,2)$ which is on the line $P_2P_3$, the convex hull is actually $P_1 \to P_2 \to P_3 \to P_4$.
Wait, $P_4(1,1)$ relative to $P_2(3,0)$ and $P_3(3,2)$: line $P_2P_3$ is $x=3$. $P_4$ has $x=1$, which is to the left.
Line $P_2P_4$: $(3,0)\to(1,1)$, slope = $(1-0)/(1-3) = -1/2$. Equation: $y - 0 = -\frac{1}{2}(x-3) \implies y = -\frac{1}{2}x + \frac{3}{2}$.
$P_3(3,2)$: plugin $x=3 \implies y = 0$, but $P_3$ has $y=2$, so $P_3$ is above $P_2P_4$.

So convex hull vertices = $(0,0), (3,0), (3,2), (1,1)$ — all 4 points are on the hull.

For $(2, 0.5)$: check if inside the quadrilateral using area method or by checking it's a convex combination.

Line $P_4P_3$: $(1,1)\to(3,2)$, slope = $(2-1)/(3-1) = 1/2$. Eq: $y-1 = \frac{1}{2}(x-1) \implies y = \frac{1}{2}x + \frac{1}{2}$.
At $x=2$, $y=1.5$. So $(2, 0.5)$ is below this line.

Line $P_1P_2$: $y=0$. $(2, 0.5)$ is above.
Line $P_1P_4$: $(0,0)\to(1,1)$, $y=x$. At $x=2$, $y=2$. $(2, 0.5)$ is below (to the right of this line? Actually $0.5 < 2$, so it's below/right).
Line $P_2P_3$: $x=3$. $(2, 0.5)$ has $x < 3$, so inside.

Since $(2, 0.5)$ is between $y=0$ and the line $P_1P_4$ ($y=x$: $0.5 < 2$, so it's to the right/below $y=x$), and also below $P_4P_3$ but above $P_1P_2$, it's inside the quadrilateral. Actually let's verify by barycentric with triangle $P_1P_2P_3$: it's below $y = \frac{2}{3}x$? At $x=2$, $\frac{2}{3}x = 4/3 > 0.5$, so yes below hypotenuse. That means inside triangle $P_1P_2P_3$. Since it's inside the triangle and the triangle is inside the hull, it's inside the hull.

Inside. ✅

---

## Basic Drill

**D1.** $x = 4\cos 60^\circ = 4 \cdot \frac{1}{2} = 2$. $y = 4\sin 60^\circ = 4 \cdot \frac{\sqrt{3}}{2} = 2\sqrt{3}$.
Cartesian: $(2,\; 2\sqrt{3})$.

**D2.** $r = \sqrt{(-3)^2 + (-3)^2} = \sqrt{18} = 3\sqrt{2}$.
Both $x$ and $y$ negative (Q3): $\theta = \pi + \tan^{-1}(1) = \pi + \frac{\pi}{4} = \frac{5\pi}{4}$ (or $225^\circ$).
Polar: $(3\sqrt{2},\; 5\pi/4)$.

**D3.** $r = \sqrt{1^2 + 1^2} = \sqrt{2}$. $\theta = \tan^{-1}(1/1) = \pi/4$.
Cylindrical: $(\sqrt{2},\; \pi/4,\; 5)$.

**D4.** $\rho = 7$. Since $x=y=0$, the point is on the positive $z$-axis. $\phi = 0$ (north pole). $\theta$ is undefined (can be any value, typically 0).
Spherical: $(7,\; 0,\; 0)$.

**D5.** $\vec{d} = (3, 4, 12)$. Distance = $\sqrt{3^2 + 4^2 + 12^2} = \sqrt{9 + 16 + 144} = \sqrt{169} = 13$.

**D6.** Line: $3x + 4y - 10 = 0$. $a=3$, $b=4$, $c=-10$.
Distance = $\frac{|3\cdot3 + 4\cdot4 - 10|}{\sqrt{9+16}} = \frac{|9 + 16 - 10|}{5} = \frac{15}{5} = 3$.

**D7.** $r = \sqrt{2^2 + (-2)^2} = \sqrt{8} = 2\sqrt{2}$. $\theta = \tan^{-1}(-2/2) = \tan^{-1}(-1) = -\pi/4$ (or $7\pi/4$), $x>0$, $y<0$ → Q4. $z=1$. Cylindrical: $(2\sqrt{2},\; -\pi/4,\; 1)$.

**D8.** $x = 3\cos(\pi/3) = 3 \cdot 1/2 = 1.5$. $y = 3\sin(\pi/3) = 3\sqrt{3}/2$. $z = 4$. Cartesian: $(1.5,\; 3\sqrt{3}/2,\; 4)$.

**D9.** Distance = $\frac{|1\cdot1 + 2\cdot(-1) + 2\cdot2 - 6|}{\sqrt{1+4+4}} = \frac{|1 - 2 + 4 - 6|}{3} = \frac{|-3|}{3} = 1$.

**D10.** $\rho = 5 \implies x^2 + y^2 + z^2 = 25$. A sphere of radius 5 centered at the origin.

---

## Advanced Drill

**A1.** From the torus parametrization in 12C2:
$x = (R + r\cos\phi)\cos\theta$, $y = (R + r\cos\phi)\sin\theta$, $z = r\sin\phi$.

Notice $x^2 + y^2 = (R + r\cos\phi)^2$. So $\sqrt{x^2 + y^2} - R = r\cos\phi$.
Then $(\sqrt{x^2 + y^2} - R)^2 + z^2 = r^2\cos^2\phi + r^2\sin^2\phi = r^2$.

The Cartesian equation: $(\sqrt{x^2 + y^2} - R)^2 + z^2 = r^2$.
Or expanded: $x^2 + y^2 + z^2 + R^2 - r^2 = 2R\sqrt{x^2 + y^2}$.
Squaring gives a 4th-degree equation.

**A2.** Two skew lines: $L_1: \vec{r}_1(t) = (t, 0, 0)$, $L_2: \vec{r}_2(s) = (0, 1, 1+s)$.

Vector between any two points: $\vec{v}(t,s) = (t-0,\; 0-1,\; 0-(1+s)) = (t,\; -1,\; -1-s)$.

Distance = minimum of $|\vec{v}(t,s)|$ over $t, s$.

Direction vectors: $\vec{d}_1 = (1, 0, 0)$, $\vec{d}_2 = (0, 0, 1)$.

Shortest distance formula for skew lines: $d = \frac{|(\vec{p}_2 - \vec{p}_1) \cdot (\vec{d}_1 \times \vec{d}_2)|}{|\vec{d}_1 \times \vec{d}_2|}$.

$\vec{p}_1 = (0,0,0)$, $\vec{p}_2 = (0,1,1)$. $\vec{p}_2 - \vec{p}_1 = (0,1,1)$.

$\vec{d}_1 \times \vec{d}_2 = \det\begin{pmatrix}\hat{i}&\hat{j}&\hat{k}\\1&0&0\\0&0&1\end{pmatrix} = (0\cdot1 - 0\cdot0,\; 0\cdot0 - 1\cdot1,\; 1\cdot0 - 0\cdot0) = (0, -1, 0)$.
$|\vec{d}_1 \times \vec{d}_2| = 1$.

$(\vec{p}_2 - \vec{p}_1) \cdot (\vec{d}_1 \times \vec{d}_2) = (0,1,1) \cdot (0,-1,0) = -1$.

Distance = $|-1|/1 = 1$.

**A3.** Sphere: center $(0,0,0)$, radius $5$. Plane: $x+y+z=3$.

Distance from origin to plane: $d_{\text{center}} = \frac{|3|}{\sqrt{1+1+1}} = \frac{3}{\sqrt{3}} = \sqrt{3}$.

The intersection is a circle. Its center is the foot of the perpendicular from the origin to the plane: along $\vec{n}=(1,1,1)/\sqrt{3}$, distance $\sqrt{3}$ from origin.
Center: $\vec{c} = \frac{3}{3}(1,1,1) = (1,1,1)$.

Radius of intersection circle: $r = \sqrt{R^2 - d_{\text{center}}^2} = \sqrt{25 - 3} = \sqrt{22}$.

Answer: center $(1,1,1)$, radius $\sqrt{22}$.

**A4.** Lagrange: $f(x,y,z) = x^2+y^2+z^2$, $g(x,y,z) = 2x+3y+z-6=0$.
$\nabla f = \lambda \nabla g \implies (2x, 2y, 2z) = \lambda(2, 3, 1)$.
$x = \lambda$, $y = \frac{3}{2}\lambda$, $z = \frac{1}{2}\lambda$.

Plug into plane: $2\lambda + 3\cdot\frac{3}{2}\lambda + \frac{1}{2}\lambda = 6$.
$2\lambda + \frac{9}{2}\lambda + \frac{1}{2}\lambda = 6$.
$(2 + 4.5 + 0.5)\lambda = 6 \implies 7\lambda = 6 \implies \lambda = 6/7$.

Closest point: $(6/7,\; 9/7,\; 3/7)$.

Geometric formula: closest point = $\frac{d}{\sqrt{a^2+b^2+c^2}}(a,b,c) = \frac{6}{4+9+1}(2,3,1) = \frac{6}{14}(2,3,1) = (12/14, 18/14, 6/14) = (6/7, 9/7, 3/7)$. ✅

**A5.** Centroid: average of vertices = $\left(\frac{0+6+0}{3},\; \frac{0+0+4}{3}\right) = (2,\; 4/3)$.

Barycentric: all equal = $(1/3,\; 1/3,\; 1/3)$.

Check: $\frac{1}{3}(0,0) + \frac{1}{3}(6,0) + \frac{1}{3}(0,4) = (2, 4/3)$ ✅.

**A6.** $r = 2\cos\theta$. Multiply by $r$: $r^2 = 2r\cos\theta$. So $x^2 + y^2 = 2x$.
Rearrange: $x^2 - 2x + y^2 = 0 \implies (x-1)^2 + y^2 = 1$.
Circle with center $(1, 0)$, radius $1$.

Arc length: when $\theta = -\pi/2$, $r = 0$. When $\theta = \pi/2$, $r = 0$. The full circle is traced once for $\theta \in [-\pi/2, \pi/2]$.

Arc length in polar: $L = \int_{-\pi/2}^{\pi/2} \sqrt{r^2 + (r')^2}\,d\theta$.
$r = 2\cos\theta$, $r' = -2\sin\theta$.
$r^2 + (r')^2 = 4\cos^2\theta + 4\sin^2\theta = 4$.

$L = \int_{-\pi/2}^{\pi/2} 2\,d\theta = 2(\pi/2 - (-\pi/2)) = 2\pi$.

This matches $2\pi R = 2\pi \cdot 1$ for a circle of radius 1.

**A7.** First, find the line of intersection of the two planes.
Plane 1: $x + y + z = 1$. Plane 2: $x - y + z = 0$.
Subtract: $(x+y+z) - (x-y+z) = 1-0 \implies 2y = 1 \implies y = 1/2$.
Add: $(x+y+z) + (x-y+z) = 1+0 \implies 2x + 2z = 1 \implies x + z = 1/2$.

Line direction: normal cross product. $\vec{n}_1 = (1,1,1)$, $\vec{n}_2 = (1,-1,1)$.
$\vec{d} = \vec{n}_1 \times \vec{n}_2 = \det\begin{pmatrix}\hat{i}&\hat{j}&\hat{k}\\1&1&1\\1&-1&1\end{pmatrix} = (1\cdot1 - 1\cdot(-1),\; 1\cdot1 - 1\cdot1,\; 1\cdot(-1) - 1\cdot1) = (2, 0, -2) = 2(1,0,-1)$.
Direction: $(1, 0, -1)$.

Point on line: set $x=0$, then $z=1/2$, $y=1/2$. Point: $(0, 1/2, 1/2)$.
Line: $\vec{r}(t) = (0, 1/2, 1/2) + t(1, 0, -1)$.

Distance from $P(3,0,0)$ to this line: $\vec{v} = (3, -1/2, -1/2)$, $\vec{d} = (1, 0, -1)$.
$\vec{v} \times \vec{d} = \det\begin{pmatrix}\hat{i}&\hat{j}&\hat{k}\\3&-1/2&-1/2\\1&0&-1\end{pmatrix} = (1/2\cdot(-1) - (-1/2)\cdot0,\; (-1/2)\cdot1 - 3\cdot(-1),\; 3\cdot0 - (-1/2)\cdot1)$.
$= (-1/2,\; -1/2 + 3,\; 0 + 1/2) = (-1/2,\; 5/2,\; 1/2)$.
$|\vec{v} \times \vec{d}| = \sqrt{1/4 + 25/4 + 1/4} = \sqrt{27/4} = \frac{3\sqrt{3}}{2}$.
$|\vec{d}| = \sqrt{2}$.
Distance = $\frac{3\sqrt{3}/2}{\sqrt{2}} = \frac{3\sqrt{6}}{4}$.

**A8.** Tetrahedron vertices: $V_0(0,0,0)$, $V_1(4,0,0)$, $V_2(0,4,0)$, $V_3(0,0,4)$.
Check if $(2,2,2)$ is inside. Try to express as convex combination:
$(2,2,2) = \alpha_0(0,0,0) + \alpha_1(4,0,0) + \alpha_2(0,4,0) + \alpha_3(0,0,4)$ with $\alpha_i \ge 0$, $\sum\alpha_i = 1$.
$x$: $2 = 4\alpha_1 \implies \alpha_1 = 0.5$.
$y$: $2 = 4\alpha_2 \implies \alpha_2 = 0.5$.
$z$: $2 = 4\alpha_3 \implies \alpha_3 = 0.5$.
$\sum\alpha_i = 0 + 0.5 + 0.5 + 0.5 = 1.5 > 1$.
So $(2,2,2)$ is **outside** the tetrahedron.

**A9.** Minimize/maximize $f(x,y) = x^2 + y^2$ subject to $g(x,y) = x^2 + 4y^2 - 4 = 0$.
$\nabla f = (2x, 2y)$, $\nabla g = (2x, 8y)$.
$(2x, 2y) = \lambda(2x, 8y)$.
Case 1: $x \neq 0$, then $2x = 2\lambda x \implies \lambda = 1$. Then $2y = 8y \implies y(2-8) = 0 \implies y = 0$.
If $y = 0$: $x^2 = 4 \implies x = \pm 2$. Points: $(\pm 2, 0)$. Distance = 2.
Case 2: $x = 0$, then $4y^2 = 4 \implies y = \pm 1$. Points: $(0, \pm 1)$. Distance = 1.
Max distance = 2 (at $(\pm 2, 0)$). Min distance = 1 (at $(0, \pm 1)$).

**A10.** The point that minimizes the sum of squared distances to the three vertices is the centroid (the average). This can be proven by calculus minimizing $f(P) = |P-A|^2 + |P-B|^2 + |P-C|^2$.
Centroid = $\left(\frac{0+5+2}{3},\; \frac{0+0+4}{3}\right) = \left(\frac{7}{3},\; \frac{4}{3}\right)$.
Check: it's inside the triangle (all barycentric coordinates are $1/3$).
