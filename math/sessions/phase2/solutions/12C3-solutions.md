# Solutions — 12C3: Coordinate Systems and Geometric Optimization
## Basic Drills

### D1. Convert the polar point $(r=4, \theta=60^\circ)$ to Cartesian coordinates.

$x = 4\cos60^\circ = 4 \cdot \frac12 = 2$.
$y = 4\sin60^\circ = 4 \cdot \frac{\sqrt3}{2} = 2\sqrt3$.

> **Answer**: $(2, 2\sqrt3)$

---

### D2. Convert the Cartesian point $(-3, -3)$ to polar coordinates.

$r = \sqrt{(-3)^2 + (-3)^2} = \sqrt{18} = 3\sqrt2$.
$\theta = \arctan(-3/-3) = \arctan(1)$. Both negative → Q3 → $\theta = \pi + \pi/4 = 5\pi/4$ (or $-3\pi/4$).

> **Answer**: $(r, \theta) = (3\sqrt2, 5\pi/4)$

---

### D3. Write the cylindrical coordinates $(r, \theta, z)$ of the point $(x, y, z) = (1, 1, 5)$.

$r = \sqrt{1^2 + 1^2} = \sqrt2$.
$\theta = \arctan(1/1) = \pi/4$ (Q1).
$z = 5$.

> **Answer**: $(\sqrt2, \pi/4, 5)$

---

### D4. Write the spherical coordinates $(\rho, \phi, \theta)$ of the point $(x, y, z) = (0, 0, 7)$.

$\rho = \sqrt{0^2 + 0^2 + 7^2} = 7$.
$\phi = \arccos(7/7) = \arccos(1) = 0$ (north pole).
$\theta$ is undefined/arbitrary (any value works at the pole).

> **Answer**: $(7, 0, \text{any})$

---

### D5. Compute the distance between $(1, 2, 3)$ and $(4, 6, 15)$ in 3D.

$d = \sqrt{(4-1)^2 + (6-2)^2 + (15-3)^2} = \sqrt{9 + 16 + 144} = \sqrt{169} = 13$.

> **Answer**: $13$

---

### D6. Find the distance from the point $(3, 4)$ to the line $3x + 4y = 10$ in 2D.

$d = \frac{|3\cdot3 + 4\cdot4 - 10|}{\sqrt{3^2+4^2}} = \frac{|9+16-10|}{5} = \frac{15}{5} = 3$.

> **Answer**: $3$

---

### D7. Convert the Cartesian point $(2, -2, 1)$ to cylindrical coordinates.

$r = \sqrt{2^2 + (-2)^2} = \sqrt{8} = 2\sqrt2$.
$\theta = \arctan(-2/2) = \arctan(-1)$. $x > 0$, $y < 0$ → Q4 → $\theta = -\pi/4$.
$z = 1$.

> **Answer**: $(2\sqrt2, -\pi/4, 1)$

---

### D8. Convert the cylindrical point $(r=3, \theta=\pi/3, z=4)$ to Cartesian.

$x = 3\cos(\pi/3) = 3 \cdot \frac12 = \frac32$.
$y = 3\sin(\pi/3) = 3 \cdot \frac{\sqrt3}{2} = \frac{3\sqrt3}{2}$.
$z = 4$.

> **Answer**: $(3/2, 3\sqrt3/2, 4)$

---

### D9. Find the distance from the point $(1, -1, 2)$ to the plane $x + 2y + 2z = 6$.

$d = \frac{|1 + 2(-1) + 2(2) - 6|}{\sqrt{1^2 + 2^2 + 2^2}} = \frac{|1 - 2 + 4 - 6|}{3} = \frac{|-3|}{3} = 1$.

> **Answer**: $1$

---

### D10. Write the Cartesian equation of the sphere $\rho = 5$ in spherical coordinates.

$\rho = 5 \implies \sqrt{x^2 + y^2 + z^2} = 5 \implies x^2 + y^2 + z^2 = 25$.

> **Answer**: $x^2 + y^2 + z^2 = 25$

---

### D11. (🔗 9C) Find the cylindrical coordinates of the point $(x, y, z) = (3, 4, -2)$.

$r = \sqrt{3^2 + 4^2} = 5$.
$\theta = \arctan(4/3)$ (Q1).
$z = -2$.

> **Answer**: $(5, \arctan(4/3), -2)$

---

### D12. (🔗 9B) Convert the polar equation $r = 4\cos\theta$ to Cartesian and identify the curve.

$r = 4\cos\theta \implies r^2 = 4r\cos\theta \implies x^2 + y^2 = 4x$.
$x^2 - 4x + y^2 = 0 \implies (x-2)^2 + y^2 = 4$.
A circle of radius $2$ centered at $(2, 0)$.

> **Answer**: Circle $(x-2)^2 + y^2 = 4$, center $(2, 0)$, radius $2$

---

## Advanced Drills

### A1. Find the equation of a torus in Cartesian coordinates by eliminating the parameters from $\vec{r}(\theta, \phi)$.

$\vec{r}(\theta, \phi) = ((R + r\cos\phi)\cos\theta,\; (R + r\cos\phi)\sin\theta,\; r\sin\phi)$.

$x = (R + r\cos\phi)\cos\theta$, $y = (R + r\cos\phi)\sin\theta$, $z = r\sin\phi$.

$x^2 + y^2 = (R + r\cos\phi)^2$.
So $\sqrt{x^2 + y^2} = R + r\cos\phi \implies \cos\phi = \frac{\sqrt{x^2+y^2} - R}{r}$.
Also $z = r\sin\phi \implies \sin\phi = \frac{z}{r}$.

Since $\cos^2\phi + \sin^2\phi = 1$:
$\left(\frac{\sqrt{x^2+y^2} - R}{r}\right)^2 + \left(\frac{z}{r}\right)^2 = 1$.

$(\sqrt{x^2+y^2} - R)^2 + z^2 = r^2$.

> **Answer**: $(\sqrt{x^2+y^2} - R)^2 + z^2 = r^2$

---

### A2. Find the distance between two skew lines: $\vec{r}_1(t) = (0, 0, 0) + t(1, 0, 0)$ and $\vec{r}_2(s) = (0, 1, 1) + s(0, 0, 1)$.

$\vec{p}_1 = (0,0,0)$, $\vec{d}_1 = (1,0,0)$.
$\vec{p}_2 = (0,1,1)$, $\vec{d}_2 = (0,0,1)$.

$\vec{v} = (0,1,1) - (0,0,0) = (0,1,1)$.
$\vec{n} = \vec{d}_1 \times \vec{d}_2 = (1,0,0) \times (0,0,1) = (0,-1,0)$.
$|\vec{n}| = 1$.
$|\vec{v} \cdot \vec{n}| = |0\cdot0 + 1(-1) + 1\cdot0| = 1$.

$d = \frac{1}{1} = 1$.

> **Answer**: $d = 1$

---

### A3. Find the center and radius of the circle that is the intersection of the sphere $x^2 + y^2 + z^2 = 25$ and the plane $x + y + z = 3$.

The plane's normal vector is $(1,1,1)$. The distance from origin to the plane is $\frac{|3|}{\sqrt{1+1+1}} = \frac{3}{\sqrt3} = \sqrt3$.

The sphere radius is $5$. By the Pythagorean theorem, the intersection circle has radius $\sqrt{5^2 - (\sqrt3)^2} = \sqrt{25-3} = \sqrt{22}$.

The center of the circle is at the foot of the perpendicular from origin to the plane:
$\vec{c} = \frac{3}{1+1+1}(1,1,1) = (1,1,1)$.

> **Answer**: Center $(1,1,1)$, radius $\sqrt{22}$

---

### A4. Use Lagrange multipliers to find the point on the plane $2x + 3y + z = 6$ closest to the origin. Verify using the geometric formula.

Minimize $f = x^2 + y^2 + z^2$ subject to $g = 2x + 3y + z - 6 = 0$.

$\nabla f = \lambda \nabla g \implies (2x, 2y, 2z) = \lambda(2, 3, 1)$.
$x = \lambda$, $y = \frac{3}{2}\lambda$, $z = \frac12\lambda$.

Substitute into constraint: $2\lambda + 3(\frac{3}{2}\lambda) + \frac12\lambda = 6$.
$2\lambda + \frac{9}{2}\lambda + \frac12\lambda = 6 \implies \frac{4+9+1}{2}\lambda = 6 \implies \frac{14}{2}\lambda = 6 \implies 7\lambda = 6 \implies \lambda = \frac{6}{7}$.

$x = \frac{6}{7}$, $y = \frac{9}{7}$, $z = \frac{3}{7}$.

Geometric formula: $d = \frac{|6|}{\sqrt{4+9+1}} = \frac{6}{\sqrt{14}}$.
Closest point: $\frac{6}{14}(2,3,1) = \frac{3}{7}(2,3,1) = (\frac{6}{7}, \frac{9}{7}, \frac{3}{7})$. ✓

> **Answer**: $(\frac{6}{7}, \frac{9}{7}, \frac{3}{7})$

---

### A5. A triangle has vertices $A(0,0)$, $B(6,0)$, $C(0,4)$. Find the barycentric coordinates of its centroid.

The centroid is the average of the three vertices: $\frac{A+B+C}{3} = \frac{(0,0)+(6,0)+(0,4)}{3} = (2, \frac43)$.

Barycentric coordinates of the centroid are always $(\frac13, \frac13, \frac13)$ since it's the arithmetic mean.

Verification: $\frac13(0,0) + \frac13(6,0) + \frac13(0,4) = (2, \frac43)$ ✓.

> **Answer**: $(\frac13, \frac13, \frac13)$

---

### A6. The polar curve $r = 2\cos\theta$ is a circle. Find its center and radius by converting to Cartesian. Also find the arc length.

$x^2 + y^2 = 2x \implies (x-1)^2 + y^2 = 1$.
Center $(1,0)$, radius $1$.

Arc length for $\theta \in [-\pi/2, \pi/2]$:
$L = \int_{-\pi/2}^{\pi/2} \sqrt{(-2\sin\theta)^2 + (2\cos\theta)^2} \, d\theta = \int_{-\pi/2}^{\pi/2} 2 \, d\theta = 2\pi$.

> **Answer**: Center $(1,0)$, radius $1$, arc length $= 2\pi$

---

### A7. Find the shortest distance from the point $(3, 0, 0)$ to the line of intersection of the planes $x + y + z = 1$ and $x - y + z = 0$.

The line direction is the cross product of the normals:
$\vec{d} = (1,1,1) \times (1,-1,1) = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 1 & 1 \\ 1 & -1 & 1 \end{vmatrix} = (1\cdot1-1(-1),\; 1\cdot1-1\cdot1,\; 1(-1)-1\cdot1) = (2, 0, -2)$.

So $\vec{d} = (2, 0, -2) \parallel (1, 0, -1)$.

Find a point on the line: set $y = 0$, then $x+z=1$ and $x+z=0$ — inconsistency. Set $z = 0$:
$x + y = 1$ and $x - y = 0 \implies x = y = \frac12$.
So $\vec{q} = (\frac12, \frac12, 0)$ is on the line.

$\vec{v} = (3,0,0) - (\frac12, \frac12, 0) = (\frac52, -\frac12, 0)$.

$d = \frac{|\vec{v} \times \vec{d}|}{|\vec{d}|}$.
$\vec{v} \times \vec{d} = (\frac52, -\frac12, 0) \times (1, 0, -1)$
$= ((-\frac12)(-1) - 0\cdot0,\; 0\cdot1 - \frac52(-1),\; \frac52\cdot0 - (-\frac12)\cdot1)$
$= (\frac12,\; \frac52,\; \frac12)$.

$|\vec{v} \times \vec{d}| = \sqrt{(\frac12)^2 + (\frac52)^2 + (\frac12)^2} = \sqrt{\frac14 + \frac{25}{4} + \frac14} = \sqrt{\frac{27}{4}} = \frac{3\sqrt3}{2}$.
$|\vec{d}| = \sqrt{1+0+1} = \sqrt2$.

$d = \frac{3\sqrt3/2}{\sqrt2} = \frac{3\sqrt6}{4}$.

> **Answer**: $d = \frac{3\sqrt6}{4}$

---

### A8. Determine if the point $(2, 2, 2)$ lies inside or outside the tetrahedron with vertices $(0,0,0)$, $(4,0,0)$, $(0,4,0)$, $(0,0,4)$ using barycentric coordinates in 3D.

We need to express $(2,2,2)$ as $\alpha A + \beta B + \gamma C + \delta D$ with $\alpha+\beta+\gamma+\delta=1$ and $\alpha,\beta,\gamma,\delta \ge 0$.

$(2,2,2) = \alpha(0,0,0) + \beta(4,0,0) + \gamma(0,4,0) + \delta(0,0,4)$.
This gives: $4\beta = 2$, $4\gamma = 2$, $4\delta = 2 \implies \beta = \gamma = \delta = \frac12$.
Then $\alpha = 1 - (\frac12 + \frac12 + \frac12) = 1 - \frac32 = -\frac12$.

Since $\alpha < 0$, the point is **outside** the tetrahedron.

> **Answer**: Outside ($\alpha = -\frac12 < 0$)

---

### A9. Find the maximum and minimum distances from the origin to the curve $x^2 + 4y^2 = 4$ (an ellipse) using Lagrange multipliers.

Maximize/minimize $f = x^2 + y^2$ subject to $g = x^2 + 4y^2 - 4 = 0$.

$\nabla f = \lambda \nabla g \implies (2x, 2y) = \lambda(2x, 8y)$.

Case 1: $x = 0$. Then $4y^2 = 4 \implies y = \pm 1$. Distance $= 1$.
Case 2: $y = 0$. Then $x^2 = 4 \implies x = \pm 2$. Distance $= 2$.
Case 3: $x \neq 0$, $y \neq 0$. Then $2x = 2\lambda x \implies \lambda = 1$. And $2y = 8\lambda y = 8y \implies 2y = 8y \implies y = 0$. Contradiction. No solutions here.

Minimum distance: $1$ (at $(0, \pm 1)$).
Maximum distance: $2$ (at $(\pm 2, 0)$).

> **Answer**: Min $= 1$ at $(0,\pm1)$, Max $= 2$ at $(\pm2,0)$

---

### A10. Three points in the plane: $(0, 0)$, $(5, 0)$, $(2, 4)$. Find the point inside the triangle that minimizes the sum of squared distances to the three vertices.

Minimize $f(x,y) = (x-0)^2 + (y-0)^2 + (x-5)^2 + (y-0)^2 + (x-2)^2 + (y-4)^2$.
$= x^2 + y^2 + (x^2 - 10x + 25) + y^2 + (x^2 - 4x + 4) + (y^2 - 8y + 16)$.
$= 3x^2 + 3y^2 - 14x - 8y + 45$.

Set partial derivatives to zero:
$\frac{\partial f}{\partial x} = 6x - 14 = 0 \implies x = \frac{7}{3}$.
$\frac{\partial f}{\partial y} = 6y - 8 = 0 \implies y = \frac{4}{3}$.

This is the centroid: $\frac{(0,0)+(5,0)+(2,4)}{3} = \left(\frac{7}{3}, \frac{4}{3}\right)$. ✓

> **Answer**: $(\frac73, \frac43)$ — the centroid

---

### A11. (🔗 9C, 12C2) Find the distance between two skew lines: the $x$-axis and the line through $(0, 1, 1)$ parallel to $(1, 1, 0)$.

$x$-axis: $\vec{r}_1(t) = (t, 0, 0)$, direction $\vec{d}_1 = (1, 0, 0)$.
Line 2: $\vec{r}_2(s) = (0, 1, 1) + s(1, 1, 0)$, direction $\vec{d}_2 = (1, 1, 0)$.

$\vec{v} = (0, 1, 1) - (0, 0, 0) = (0, 1, 1)$.
$\vec{n} = \vec{d}_1 \times \vec{d}_2 = (1,0,0) \times (1,1,0) = (0\cdot0 - 0\cdot1,\; 0\cdot1 - 1\cdot0,\; 1\cdot1 - 0\cdot1) = (0, 0, 1)$.
$|\vec{n}| = 1$.
$|\vec{v} \cdot \vec{n}| = |0\cdot0 + 1\cdot0 + 1\cdot1| = 1$.

$d = \frac{1}{1} = 1$.

> **Answer**: $d = 1$

---

### A12. (🔗 12C1) A point $(x, y)$ is rotated by $90^\circ$, then the result is converted to polar coordinates. If the original point is $(3, 1)$, what are $(r, \theta)$ after the rotation? Solve two ways.

**Method 1: Rotate then convert.**
Rotation by $90^\circ$ CCW: $R_{90} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$.
$R_{90}(3, 1) = (-1, 3)$.
$r = \sqrt{(-1)^2 + 3^2} = \sqrt{10}$.
$\theta = \arctan(3/(-1))$ — Q2 → $\theta = \pi - \arctan(3) \approx \pi - 1.249 = 1.893$ rad.

**Method 2: Use the relationship between rotation and angle addition.**
Original point $(3, 1)$ has $r = \sqrt{10}$, $\theta_0 = \arctan(1/3) \approx 0.322$ rad.
Rotation by $90^\circ$ adds $\pi/2$ to the angle.
New $\theta = \theta_0 + \pi/2 \approx 0.322 + 1.571 = 1.893$ rad.
$r$ stays the same: $r = \sqrt{10}$.

Both methods give the same result ✓.

> **Answer**: $(r, \theta) = (\sqrt{10},\; \arctan(1/3) + \pi/2)$
