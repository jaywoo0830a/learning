# Solutions — Session 9C: 3D Geometry

---

## Practice 1

> Find the distance from $(2, -1, 4)$ to the plane $x + 2y + 2z = 6$. Then find the foot of the perpendicular.

**Step 1: Distance.**
Rewrite plane: $x + 2y + 2z - 6 = 0$. $a=1, b=2, c=2, d=6$.
$$D = \frac{|1(2) + 2(-1) + 2(4) - 6|}{\sqrt{1 + 4 + 4}} = \frac{|2 - 2 + 8 - 6|}{\sqrt{9}} = \frac{|2|}{3} = \frac{2}{3}$$

**Step 2: Foot of perpendicular.**
The normal $\vec{n} = (1, 2, 2)$. Parametric line: $(2, -1, 4) + t(1, 2, 2) = (2+t, -1+2t, 4+2t)$.
Plug into plane: $(2+t) + 2(-1+2t) + 2(4+2t) = 6$.
$2 + t - 2 + 4t + 8 + 4t = 6$ → $9t + 8 = 6$ → $9t = -2$ → $t = -\frac{2}{9}$.

Foot: $(2 - \frac{2}{9}, -1 - \frac{4}{9}, 4 - \frac{4}{9}) = (\frac{16}{9}, -\frac{13}{9}, \frac{32}{9})$.

**Answer: $D = \frac{2}{3}$, foot $(\frac{16}{9}, -\frac{13}{9}, \frac{32}{9})$.**

---

## Practice 2

> Find the center and radius of the sphere $x^2 + y^2 + z^2 - 4x + 2y - 6z + 5 = 0$.

$(x^2 - 4x) + (y^2 + 2y) + (z^2 - 6z) = -5$.
$(x - 2)^2 - 4 + (y + 1)^2 - 1 + (z - 3)^2 - 9 = -5$.
$(x - 2)^2 + (y + 1)^2 + (z - 3)^2 = -5 + 4 + 1 + 9 = 9$.

**Answer: Center $(2, -1, 3)$, radius $3$.**

---

## Practice 3

> Describe and sketch the level curves of $z = x^2 - y^2$ at $c = -2, -1, 0, 1, 2$. What quadric surface is this? What happens at $c=0$?

$f(x,y) = x^2 - y^2 = c$.

| $c$ | Curve | Description |
|:---:|:-----:|:-----------|
| $-2$ | $y^2 - x^2 = 2$ → $\frac{y^2}{2} - \frac{x^2}{2} = 1$ | Hyperbola opening up/down |
| $-1$ | $y^2 - x^2 = 1$ | Hyperbola opening up/down |
| $0$ | $x^2 = y^2$ → $y = \pm x$ | **Two crossing lines through origin** |
| $1$ | $x^2 - y^2 = 1$ | Hyperbola opening left/right |
| $2$ | $x^2 - y^2 = 2$ → $\frac{x^2}{2} - \frac{y^2}{2} = 1$ | Hyperbola opening left/right |

The surface is a **hyperbolic paraboloid** (saddle).

At $c=0$, the level curve degenerates into two **crossing lines** $y=x$ and $y=-x$. This is the saddle point — where the surface transitions from curving one way to the other. For $c>0$, hyperbolas open left-right (surface rises along $x$). For $c<0$, hyperbolas open up-down (surface falls along $y$).

---

## Practice 4

> Classify each quadric surface and sketch its key cross-sections:
> (a) $x^2 + y^2 - z^2 = 1$
> (b) $z = 4 - x^2 - y^2$
> (c) $x^2 + 2y^2 + 3z^2 = 12$

**(a)** $x^2 + y^2 - z^2 = 1$: Two plus, one minus → **Hyperboloid of one sheet**.
Cross-sections: $z=0$: circle $x^2+y^2=1$ (waist). $z=k$: circle $x^2+y^2=1+k^2$ (growing as $|k|$ increases).

**(b)** $z = 4 - x^2 - y^2$: Rewrite: $z - 4 = -(x^2 + y^2)$ → **Elliptic paraboloid** opening **downward**, vertex at $(0,0,4)$.
Cross-sections: $z=k$ ($k<4$): circle $x^2+y^2=4-k$. $x=0$: parabola $z=4-y^2$ (opens down).

**(c)** $x^2 + 2y^2 + 3z^2 = 12$: Divide by 12: $\frac{x^2}{12} + \frac{y^2}{6} + \frac{z^2}{4} = 1$. All plus signs → **Ellipsoid**.
Semi-axes: $a=\sqrt{12}=2\sqrt{3}$, $b=\sqrt{6}$, $c=2$.

---

## Practice 5

> Find the center and radius of the circle formed by intersecting the sphere $x^2+y^2+z^2=20$ with the plane $x+y+z=6$.

**Step 1: Distance from origin (sphere center) to plane.**
$D = \frac{|0+0+0-6|}{\sqrt{1+1+1}} = \frac{6}{\sqrt{3}} = 2\sqrt{3}$.

**Step 2: Radius of intersection circle.**
$r = \sqrt{R^2 - D^2} = \sqrt{20 - 12} = \sqrt{8} = 2\sqrt{2}$.

**Step 3: Center of intersection circle.**
The center lies along the normal direction $(1,1,1)$ from the origin toward the plane.
Normal unit vector: $\hat{n} = (\frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}})$.
Center: $D \cdot \hat{n} = 2\sqrt{3} \cdot (\frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}) = (2, 2, 2)$.

**Answer: Center $(2, 2, 2)$, radius $2\sqrt{2}$.**

---

## Practice 6: Real Battle

> A plane passes through the three points $(1,0,0)$, $(0,2,0)$, $(0,0,3)$. Find its equation in both general and intercept form. Then find the distance from the origin to this plane. What is the volume of the tetrahedron formed by this plane and the three coordinate planes?

**Step 1: Equation of the plane.**
$\vec{AB} = (-1, 2, 0)$, $\vec{AC} = (-1, 0, 3)$.
$\vec{n} = \vec{AB} \times \vec{AC} = (2\cdot3 - 0\cdot0,\; 0(-1) - (-1)3,\; (-1)0 - 2(-1)) = (6, 3, 2)$.

Point-normal form with $A(1,0,0)$: $6(x-1) + 3(y-0) + 2(z-0) = 0$ → $6x + 3y + 2z = 6$.

**General form**: $6x + 3y + 2z - 6 = 0$.
**Intercept form**: Divide by 6: $\frac{x}{1} + \frac{y}{2} + \frac{z}{3} = 1$.

**Step 2: Distance from origin.**
$D = \frac{|6(0) + 3(0) + 2(0) - 6|}{\sqrt{36 + 9 + 4}} = \frac{6}{\sqrt{49}} = \frac{6}{7}$.

**Step 3: Volume of tetrahedron.**
The tetrahedron has vertices $(0,0,0), (1,0,0), (0,2,0), (0,0,3)$.
Volume = $\frac{1}{6} \times \text{(product of intercept lengths)} = \frac{1}{6} \cdot 1 \cdot 2 \cdot 3 = \frac{6}{6} = 1$.

(Formula for tetrahedron with right-angle at origin: $V = \frac{1}{6}abc$ where $a,b,c$ are intercepts.)

**Answer: $6x+3y+2z=6$, $\frac{x}{1}+\frac{y}{2}+\frac{z}{3}=1$, $D=\frac{6}{7}$, $V=1$.**

---

## Basic Algebra Drill — 3D Geometry (15 Problems)

---

### D1
> Find the distance between $(1, -2, 3)$ and $(5, 2, 15)$.

$d = \sqrt{(5-1)^2 + (2-(-2))^2 + (15-3)^2} = \sqrt{16 + 16 + 144} = \sqrt{176} = 4\sqrt{11} \approx 13.27$.

---

### D2
> Write the equation of a plane through $(2, 1, -3)$ with normal vector $(1, 4, -2)$.

$1(x-2) + 4(y-1) - 2(z+3) = 0$ → $x - 2 + 4y - 4 - 2z - 6 = 0$ → $x + 4y - 2z = 12$.

---

### D3
> Find the center and radius of $x^2 + y^2 + z^2 + 8x - 2y + 10z + 8 = 0$.

$(x^2+8x) + (y^2-2y) + (z^2+10z) = -8$.
$(x+4)^2 - 16 + (y-1)^2 - 1 + (z+5)^2 - 25 = -8$.
$(x+4)^2 + (y-1)^2 + (z+5)^2 = -8 + 16 + 1 + 25 = 34$.

**Center $(-4, 1, -5)$, radius $\sqrt{34}$.**

---

### D4
> Find the distance from $(3, 1, -2)$ to the plane $2x - y + 2z = 4$.

$D = \frac{|2(3) - 1 + 2(-2) - 4|}{\sqrt{4+1+4}} = \frac{|6 - 1 - 4 - 4|}{3} = \frac{|-3|}{3} = 1$.

---

### D5
> Compute $\vec{u} \cdot \vec{v}$ and $\vec{u} \times \vec{v}$ for $\vec{u}=(2,1,-1)$ and $\vec{v}=(1,-1,2)$. Are they perpendicular?

$\vec{u} \cdot \vec{v} = 2(1) + 1(-1) + (-1)(2) = 2 - 1 - 2 = -1$.
Since $\vec{u} \cdot \vec{v} \neq 0$, they are **not perpendicular**.

$\vec{u} \times \vec{v} = (1\cdot2 - (-1)(-1),\; (-1)\cdot1 - 2\cdot2,\; 2(-1) - 1\cdot1) = (2-1,\; -1-4,\; -2-1) = (1, -5, -3)$.

---

### D6
> Identify the surface: $x^2 + y^2 = 16$ (in 3D). Sketch two cross-sections.

Only $x$ and $y$ appear — $z$ is free. This is a **circular cylinder** of radius 4, extruded infinitely along the $z$-axis.

Cross-sections:
- Horizontal ($z=k$): circle $x^2+y^2=16$, same at every height.
- Vertical ($x=0$): $y^2=16$ → $y=\pm4$ — two parallel lines in the $yz$-plane.

---

### D7
> Identify the surface: $z = 5 - x^2 - y^2$. Find its vertex and the shape of its level curves.

$z - 5 = -(x^2 + y^2)$. **Elliptic paraboloid** opening **downward**.
Vertex: $(0, 0, 5)$. Level curves: $x^2+y^2 = 5-z$ → circles of radius $\sqrt{5-z}$ (only for $z \leq 5$).

---

### D8
> Identify the surface: $\frac{x^2}{4} + \frac{y^2}{9} + \frac{z^2}{16} = 1$. State the lengths of its semi-axes.

All plus signs, RHS = 1 → **Ellipsoid**.
Semi-axes: $a = 2$ (along $x$), $b = 3$ (along $y$), $c = 4$ (along $z$).

---

### D9
> Identify the surface: $x^2 - y^2 + z^2 = 0$. (Hint: is it a cone? Check the signs carefully.)

Rewrite: $x^2 + z^2 = y^2$. Two plus, one minus, RHS = 0 → **Elliptic cone** (double cone along $y$-axis).
It is NOT a circular cone — the $xz$ cross-section at $y=k$ is the circle $x^2+z^2=k^2$.

---

### D10
> Find the distance from $(7, 0, 0)$ to the sphere $x^2+y^2+z^2=16$.

Center $(0,0,0)$, $R=4$. $|P C| = 7$. Point is outside.
$d = |P C| - R = 7 - 4 = 3$.

---

### ◆ D11
> Without using the formula, explain geometrically why the distance from the origin to the plane $x+y+z=3$ is exactly $\sqrt{3}$.

The point on the plane closest to the origin lies along the normal direction $(1,1,1)$. That point is $(1,1,1)$ (since $1+1+1=3$). The distance from $(0,0,0)$ to $(1,1,1)$ is $\sqrt{1^2+1^2+1^2} = \sqrt{3}$.

(Formula verification: $D = \frac{|3|}{\sqrt{3}} = \sqrt{3}$. ✓)

---

### ◆ D12
> The domain of $z = \sqrt{9 - x^2 - y^2}$ is a disk. But the domain of $z = \frac{1}{\sqrt{9 - x^2 - y^2}}$ is an OPEN disk. Explain geometrically what happens to the surface at the boundary in each case.

For $z = \sqrt{9-x^2-y^2}$: The domain is the closed disk $x^2+y^2 \leq 9$. At the boundary $x^2+y^2=9$, $z=0$ — the surface meets the $xy$-plane. The hemisphere has a well-defined bottom edge.

For $z = \frac{1}{\sqrt{9-x^2-y^2}}$: The domain is the open disk $x^2+y^2 < 9$. As $(x,y)$ approaches the boundary, the denominator $\to 0$ and $z \to \infty$. The surface has a **vertical asymptote** at the boundary circle — it shoots up to infinity. This is a 3D analog of a vertical asymptote.

---

### ◆ D13
> Level curves of $z = x^2 + 4y^2$ at evenly spaced heights get closer together as $z$ increases. What does this tell you about the steepness of the paraboloid as you go up? Contrast with the cone $z = \sqrt{x^2+y^2}$.

For $z = x^2 + 4y^2$ (elliptic paraboloid): Level curves are ellipses $x^2+4y^2=c$. As $c$ grows, the radius grows as $\sqrt{c}$. So the same $\Delta z$ produces smaller horizontal displacement at larger $z$ — the surface **steepens** as you go up. The bowl gets steeper, unlike a cone.

For $z = \sqrt{x^2+y^2}$ (cone): Level curves are circles $x^2+y^2=c^2$, radius = $c$ (NOT $\sqrt{c}$). Since radius grows linearly with height, evenly spaced $z$ values produce evenly spaced level curves. The cone has **constant slope** — it never steepens. This is the crucial geometric difference between a paraboloid (accelerating steepness) and a cone (constant steepness).

---

### ◆ D14
> A plane $z = c$ (horizontal) intersects the cone $z^2 = x^2 + y^2$. For which value of $c$ is the intersection a single point? For $c>0$, what shape is the intersection? How does its size grow with $c$?

For $c = 0$: $0 = x^2 + y^2$ → $(0,0,0)$ only. **Single point** — the cone's vertex.

For $c > 0$: $c^2 = x^2 + y^2$ → **circle** of radius $|c|$.
For $c < 0$: also a circle, since $z$ is negative but $z^2 = c^2$ (same equation).

The radius grows **linearly** with $|c|$: $r = |c|$. This linear relationship is the defining feature of a cone.

---

### ◆ D15
> The equation $x^2 + y^2 - z^2 = 0$ defines a cone. The equation $x^2 + y^2 - z^2 = -1$ defines a hyperboloid of two sheets. What happens to the surface as the RHS goes from 0 to −1? Describe the geometric transition.

As $\varepsilon$ goes from $0$ to negative values in $x^2 + y^2 - z^2 = \varepsilon$:

At $\varepsilon = 0$: The double cone, two nappes meeting at a single point (the origin). The "waist" has shrunk to a point.

For $\varepsilon < 0$: Rewrite $z^2 - (x^2 + y^2) = |\varepsilon|$, or $-\frac{x^2}{|\varepsilon|} - \frac{y^2}{|\varepsilon|} + \frac{z^2}{|\varepsilon|} = 1$. This is a **hyperboloid of two sheets**. The two nappes have **separated** — there is a gap $|z| < \sqrt{|\varepsilon|}$ with no real points. The cone was the "tipping point" between connected (one-sheet, $\varepsilon > 0$) and disconnected (two-sheet, $\varepsilon < 0$) shapes. The topology changes at $\varepsilon = 0$.

---

## Advanced Algebra Drill — 3D Geometry (15 Problems)

---

### A1
> Find the distance between the parallel planes $2x - y + 2z = 5$ and $2x - y + 2z = -7$.

Same normal $(2,-1,2)$. $d_1 = 5$, $d_2 = -7$.
$D = \frac{|5 - (-7)|}{\sqrt{4+1+4}} = \frac{12}{3} = 4$.

---

### A2
> Find the equation of the sphere that has $(2, -1, 3)$ and $(6, 5, -1)$ as endpoints of a diameter.

Center (midpoint): $C = (\frac{2+6}{2}, \frac{-1+5}{2}, \frac{3-1}{2}) = (4, 2, 1)$.
Diameter length: $d = \sqrt{(6-2)^2 + (5+1)^2 + (-1-3)^2} = \sqrt{16+36+16} = \sqrt{68} = 2\sqrt{17}$.
Radius: $R = \sqrt{17}$.

Equation: $(x-4)^2 + (y-2)^2 + (z-1)^2 = 17$.

---

### A3
> Find the angle between the planes $x + y + z = 1$ and $x - y + z = 2$.

$\vec{n}_1 = (1, 1, 1)$, $\vec{n}_2 = (1, -1, 1)$.
$\cos\theta = \frac{|1(1) + 1(-1) + 1(1)|}{\sqrt{3}\sqrt{3}} = \frac{|1 - 1 + 1|}{3} = \frac{1}{3}$.
$\theta = \cos^{-1}(\frac{1}{3}) \approx 70.53°$.

---

### A4
> The surface $z = xy$ is a hyperbolic paraboloid. Describe its level curves at $z = -2, -1, 0, 1, 2$ and explain why the saddle shape emerges from hyperbolas.

$xy = c$:

| $c$ | Curve | Description |
|:---:|:-----:|:-----------|
| $-2$ | $xy = -2$ | Hyperbola in Q2 and Q4 |
| $-1$ | $xy = -1$ | Hyperbola in Q2 and Q4 |
| $0$ | $xy = 0$ | **The $x$ and $y$ axes** — two crossing lines |
| $1$ | $xy = 1$ | Hyperbola in Q1 and Q3 |
| $2$ | $xy = 2$ | Hyperbola in Q1 and Q3 |

At $c=0$, the level set is the union of the $x$-axis and $y$-axis — two perpendicular lines. As $c$ becomes positive, the hyperbolas live in Q1 and Q3. As $c$ becomes negative, they live in Q2 and Q4. The surface rises in Q1/Q3 and falls in Q2/Q4, with the axes forming the "cross" at the saddle point — exactly the Pringle shape.

---

### A5
> Find the intersection of the line through $(1,2,3)$ with direction $(1,-1,1)$ and the plane $2x + y - z = 4$.

Parametric line: $(x,y,z) = (1+t,\; 2-t,\; 3+t)$.
Plug into plane: $2(1+t) + (2-t) - (3+t) = 4$.
$2 + 2t + 2 - t - 3 - t = 4$ → $(2+2-3) + (2t - t - t) = 4$ → $1 + 0 = 4$ → $1 = 4$ → Contradiction!

The line is **parallel** to the plane and does NOT intersect it. (Check: direction $(1,-1,1)$ dot normal $(2,1,-1)$ = $2-1-1=0$ → line direction is perpendicular to normal → parallel to plane. But the point $(1,2,3)$ gives $2+2-3=1\neq4$, so it doesn't lie in the plane.)

---

### A6
> A plane passes through $(1,1,1)$ and is perpendicular to both $x+y+z=1$ and $x-y+2z=0$. Find its equation.

$\vec{n}_1 = (1,1,1)$, $\vec{n}_2 = (1,-1,2)$. The required normal is $\vec{n} = \vec{n}_1 \times \vec{n}_2$.

$\vec{n} = (1\cdot2 - 1(-1),\; 1\cdot1 - 1\cdot2,\; 1(-1) - 1\cdot1) = (2+1,\; 1-2,\; -1-1) = (3, -1, -2)$.

Plane through $(1,1,1)$: $3(x-1) - (y-1) - 2(z-1) = 0$ → $3x - 3 - y + 1 - 2z + 2 = 0$ → $3x - y - 2z = 0$.

---

### A7
> Find the equation of the cylinder whose base is the ellipse $\frac{x^2}{4}+\frac{y^2}{9}=1$ and whose rulings are parallel to the $z$-axis.

Since rulings are parallel to the $z$-axis, $z$ does not appear in the equation (the 2D ellipse is extruded along $z$). The cylinder equation is simply $\frac{x^2}{4} + \frac{y^2}{9} = 1$ interpreted in 3D — $z$ is free.

---

### A8
> Two spheres: $x^2+y^2+z^2=25$ and $(x-8)^2+y^2+z^2=9$. Do they intersect? If so, find the equation of the plane containing their circle of intersection.

$S_1$: center $(0,0,0)$, $R_1=5$. $S_2$: center $(8,0,0)$, $R_2=3$.
Distance between centers: $d = 8$.

Check: $R_1 + R_2 = 8$, $|R_1 - R_2| = 2$. Since $d = R_1 + R_2 = 8$, the spheres are **externally tangent** — they touch at exactly one point, not a circle.

The single intersection point lies along the line from $(0,0,0)$ to $(8,0,0)$, at distance 5 from the origin: $(5, 0, 0)$.

Since they don't intersect in a circle, there is **no plane of intersection** containing a circle. They only touch at $(5,0,0)$.

---

### A9
> Find the point on the plane $x + 2y + 3z = 13$ closest to the origin.

The closest point lies along the normal $(1,2,3)$ from the origin.
Parametric: $(t, 2t, 3t)$. Plug into plane: $t + 2(2t) + 3(3t) = 13$ → $t + 4t + 9t = 13$ → $14t = 13$ → $t = \frac{13}{14}$.

Closest point: $(\frac{13}{14}, \frac{26}{14}, \frac{39}{14}) = (\frac{13}{14}, \frac{13}{7}, \frac{39}{14})$.

---

### A10
> The surface $x^2 + 4y^2 - z^2 = 0$ is an elliptic cone. Describe the cross-section at $z=2$ and at $y=1$.

At $z=2$: $x^2 + 4y^2 = 4$ → $\frac{x^2}{4} + y^2 = 1$ → **ellipse** in the plane $z=2$, semi-axes $a=2, b=1$.

At $y=1$: $x^2 + 4 - z^2 = 0$ → $z^2 - x^2 = 4$ → $\frac{z^2}{4} - \frac{x^2}{4} = 1$ → **hyperbola** in the plane $y=1$, opening along $z$-axis.

---

### ◆ A11
> Find the volume of the tetrahedron formed by the coordinate planes and the plane $\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1$. Then show that the sum of the reciprocals of the squares of the distances from the origin to the four faces is constant.

The intercepts are $(a,0,0), (0,b,0), (0,0,c)$. The vertex at the origin completes the tetrahedron.
Volume = $\frac{1}{6}abc$.

Distances from origin to faces:
- $xy$-plane ($z=0$): $d_1 = 0$ — wait, the origin is ON the $xy$-plane. The four faces are the three coordinate planes and the given plane. Distance from origin to each coordinate plane is 0. So the sum of $1/d^2$ is infinite? Let me reconsider — the problem likely means the distances to the faces, where faces are all planes bounding the tetrahedron. But the origin lies on 3 faces...

Reinterpreting: The tetrahedron's 4 faces are the plane and the 3 coordinate planes, but the origin is a VERTEX, not the centroid. The distances from the CENTROID to the 4 faces sum to a constant. Or perhaps it means sum of $1/d_i^2$ where $d_i$ is the distance from the origin to the $i$-th face — but the origin is on 3 faces, giving infinite reciprocals.

Alternatively: the distance from origin to the given plane is $D = \frac{1}{\sqrt{1/a^2 + 1/b^2 + 1/c^2}}$. For coordinate planes, the distance from origin is 0. So the sum diverges. The problem as stated may have an issue — perhaps it means the distances *between parallel face pairs*? Or from the centroid?

Let me interpret differently: the 4 faces are the given plane and the 3 coordinate planes. The tetrahedron has volume $abc/6$. The sum of squares of areas of the 4 faces relates to the volume. But I think the intended result is the well-known fact:

If a tetrahedron has a right-angle corner at the origin with edges $a,b,c$ along axes, then for the face opposite the origin (the given plane), its distance $h$ from the origin satisfies $\frac{1}{h^2} = \frac{1}{a^2} + \frac{1}{b^2} + \frac{1}{c^2}$. (This is the 3D Pythagorean theorem for a right tetrahedron's altitude.)

So: $1/h^2 = 1/a^2 + 1/b^2 + 1/c^2$, where $h = D = 1/\sqrt{1/a^2+1/b^2+1/c^2}$. ✓

---

### ◆ A12
> Consider the family of planes $x + y + z = k$ intersecting the ellipsoid $\frac{x^2}{4} + \frac{y^2}{4} + \frac{z^2}{9} = 1$. As $k$ increases from $0$ to $\infty$, describe how the intersection changes. For what $k$ does the intersection degenerate to a point?

The ellipsoid has semi-axes: $a=2, b=2$ (circle in $xy$-plane), $c=3$ (tall in $z$).

The plane $x+y+z=k$ has normal $(1,1,1)$. Distance from origin: $D = k/\sqrt{3}$.

The intersection is an ellipse (since plane cuts an ellipsoid). As $k$ increases:
- $k=0$: plane through origin, intersection is a maximal ellipse.
- As $k$ grows, the intersection ellipse shrinks.
- Degenerates to a point when the plane is tangent: $D$ equals the distance from origin to the ellipsoid surface along $(1,1,1)$.

The ellipsoid radius along direction $(1,1,1)$: set $x=y=z=t$. Then $\frac{3t^2}{4} + \frac{t^2}{9} = 1$... wait, $x,y$ use $a=2,2$ ($x^2/4+y^2/4$), $z$ uses $c^2=9$. Actually: $\frac{t^2}{4} + \frac{t^2}{4} + \frac{t^2}{9} = t^2(\frac{1}{2} + \frac{1}{9}) = t^2(\frac{9+2}{18}) = \frac{11t^2}{18} = 1$ → $t = \sqrt{18/11} = 3\sqrt{2/11}$.

So the point is $(t,t,t)$. On the plane $x+y+z=k$, $k = 3t = 9\sqrt{2/11} = 9\sqrt{2/11}$.

The intersection is:
- $k=0$: largest ellipse, through center.
- $0 < k < 9\sqrt{2/11}$: ellipses, shrinking.
- $k = 9\sqrt{2/11}$: **single point** (tangency).
- $k > 9\sqrt{2/11}$: no intersection (plane misses).

---

### ◆ A13
> The surface $\frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{z^2}{c^2} = 0$ is an elliptic cone. Replace $0$ with $\varepsilon$. Show that for $\varepsilon > 0$: hyperboloid of one sheet. For $\varepsilon < 0$: hyperboloid of two sheets. The cone is the "transition" between fundamentally different shapes.

For $\varepsilon > 0$: $\frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{z^2}{c^2} = \varepsilon$. Divide by $\varepsilon$: $\frac{x^2}{\varepsilon a^2} + \frac{y^2}{\varepsilon b^2} - \frac{z^2}{\varepsilon c^2} = 1$. Two plus signs, one minus → **hyperboloid of one sheet** (connected, cooling tower). The "waist" at $z=0$ is an ellipse $\frac{x^2}{\varepsilon a^2} + \frac{y^2}{\varepsilon b^2} = 1$, which grows as $\varepsilon$ increases.

For $\varepsilon < 0$: $-\frac{x^2}{a^2} - \frac{y^2}{b^2} + \frac{z^2}{c^2} = |\varepsilon|$. Divide: $-\frac{x^2}{|\varepsilon|a^2} - \frac{y^2}{|\varepsilon|b^2} + \frac{z^2}{|\varepsilon|c^2} = 1$. Two minus signs, one plus → **hyperboloid of two sheets** (disconnected, two bowls). There is a gap where $|z| < |\varepsilon|c$ has no real points.

**Geometric meaning**: As $\varepsilon$ crosses zero, the surface undergoes a **topological phase transition**. At $\varepsilon=0$, the "waist" of the one-sheet hyperboloid has shrunk to zero (a point), and the two nappes of the double cone pinch together. As $\varepsilon$ becomes negative, that pinch breaks apart into two disconnected sheets. The cone is the **critical boundary** between connected and disconnected.

---

### ◆ A14
> A line through the origin with direction $(a,b,c)$ intersects the unit sphere $x^2+y^2+z^2=1$ at two antipodal points. Show that these points are always $(a,b,c)/\sqrt{a^2+b^2+c^2}$ and its negative. What does this tell you about the sphere's symmetry?

Parametric line: $(ta, tb, tc)$. Substitute into sphere: $t^2(a^2+b^2+c^2) = 1$ → $t = \pm\frac{1}{\sqrt{a^2+b^2+c^2}}$.

Points: $\pm\frac{(a,b,c)}{\sqrt{a^2+b^2+c^2}}$. These are always **antipodal** (opposite points on the sphere), and they are the normalization of ANY direction vector.

**Geometric meaning**: Every direction from the origin pierces the unit sphere at exactly the same distance (1). This is the defining property of a sphere — it has the same "radius" in every direction. This is called **radial symmetry** or **isotropy**. Unlike an ellipsoid (where the intersection distance depends on direction), the sphere treats all directions equally. This is why the sphere has maximum symmetry among all quadric surfaces.

---

### ◆ A15
> Level surfaces of $w = x^2 + y^2 + z^2$ are spheres. Now consider $w = x^2 + y^2 - z^2$. Describe the family of level surfaces as $w$ varies from $-\infty$ to $+\infty$. At what value of $w$ does the topology change?

$x^2 + y^2 - z^2 = w$.

| $w$ range | Surface type | Topology |
|:---------:|:------------:|:--------:|
| $w > 0$ | $\frac{x^2}{w} + \frac{y^2}{w} - \frac{z^2}{w} = 1$ → Hyperboloid of **one sheet** | Connected (cylinder-like) |
| $w = 0$ | $x^2 + y^2 = z^2$ → **Double cone** | Two nappes touching at a point |
| $w < 0$ | $-x^2 - y^2 + z^2 = |w|$ → Hyperboloid of **two sheets** (along $z$) | Disconnected (two bowls) |

The topology changes at **$w = 0$**. This is the bifurcation point:
- $w > 0$: one connected component (genus 0 surface, not simply connected — it has a hole).
- $w = 0$: two components meeting at a single point (singular).
- $w < 0$: two disconnected components.

This is a classic example of a **Morse function** where the critical value $w=0$ corresponds to a saddle-type critical point at the origin, where the topology of the level sets changes. This connects to **Morse theory** — the study of how topology changes as you cross critical values.
