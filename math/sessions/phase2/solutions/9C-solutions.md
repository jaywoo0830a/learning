# Solutions: 9C — 3D Surfaces & Geometry

---

## Practice 1

> Distance from $(2,-1,4)$ to $x+2y+2z=6$.

Rewrite as $x+2y+2z-6=0$. $d = \frac{|2+2(-1)+2(4)-6|}{\sqrt{1+4+4}} = \frac{|2-2+8-6|}{3} = \frac{2}{3}$.

→ **$2/3$.**

---

## Practice 2

> $x^2+y^2+z^2-4x+2y-6z+5=0$.

$(x^2-4x) + (y^2+2y) + (z^2-6z) = -5$.
$(x-2)^2 + (y+1)^2 + (z-3)^2 = -5 + 4 + 1 + 9 = 9$.
Center $(2,-1,3)$, radius $3$.

---

## Practice 3

> $z = x^2 - y^2$. Level curves: $x^2-y^2=c$.

$c=-2$: hyperbola $y^2-x^2=2$, opens vertically.
$c=-1$: $y^2-x^2=1$, opens vertically.
$c=0$: $x^2=y^2 \to y=\pm x$, two crossing lines.
$c=1$: $x^2-y^2=1$, opens horizontally.
$c=2$: $x^2-y^2=2$, opens horizontally.
Surface: **hyperbolic paraboloid** (saddle).

---

## Practice 4

**(a)** $x^2+y^2-z^2=1$: **hyperboloid of one sheet** (exactly one minus).

**(b)** $z=4-x^2-y^2$: **elliptic paraboloid** (bowl opening downward, vertex at $z=4$).

**(c)** $\frac{x^2}{12} + \frac{y^2}{6} + \frac{z^2}{4} = 1$: **ellipsoid** (all plus signs).

---

## Practice 5

> Sphere $x^2+y^2+z^2=20$ (center origin, $R=\sqrt{20}=2\sqrt{5}$), plane $x+y+z=6$.

Distance from origin to plane: $d = \frac{|6|}{\sqrt{3}} = 2\sqrt{3}$.
Radius of intersection: $r = \sqrt{R^2-d^2} = \sqrt{20-12} = \sqrt{8} = 2\sqrt{2}$.
Center: foot of perpendicular from origin to plane = $\frac{6}{3}(1,1,1) = (2,2,2)$.

→ **Center $(2,2,2)$, radius $2\sqrt{2}$.**

---

## Practice 6

> Plane through $(1,0,0), (0,2,0), (0,0,3)$.

Find normal: $\vec{v} = (0,2,0)-(1,0,0) = (-1,2,0)$, $\vec{w} = (0,0,3)-(1,0,0) = (-1,0,3)$.
$\vec{n} = \vec{v}\times\vec{w} = (2\cdot3-0, 0(-1)-(-1)3, (-1)0-2(-1)) = (6, 3, 2)$.
Plane: $6(x-1)+3(y-0)+2(z-0)=0 \to 6x+3y+2z=6$. Or $\frac{x}{1}+\frac{y}{2}+\frac{z}{3}=1$ (intercept form).

Distance from origin: $d = \frac{|6|}{\sqrt{36+9+4}} = \frac{6}{7}$.

---

## Basic Drill

**D1.** $\sqrt{(5-1)^2+(2-(-2))^2+(15-3)^2} = \sqrt{16+16+144} = \sqrt{176} = 4\sqrt{11}$.

**D2.** $1(x-2)+4(y-1)-2(z+3)=0 \to x+4y-2z = 2+4+6 = 12$. → $x+4y-2z=12$.

**D3.** $(x^2+8x)+(y^2-2y)+(z^2+10z)=-8$. $(x+4)^2+(y-1)^2+(z+5)^2 = -8+16+1+25 = 34$. Center $(-4,1,-5)$, radius $\sqrt{34}$.

**D4.** **Circular cylinder** of radius 4 along the $z$-axis.

**D5.** **Elliptic paraboloid** (bowl), vertex at $(0,0,5)$, opening downward.

**D6.** **Ellipsoid** with semi-axes $2,3,4$.

**D7.** $x^2+z^2=y^2$. This is a **cone** along the $y$-axis.

**D8.** $|PC| = 3$, $R=2$. Point is outside. Distance = $3-2=1$.

**D9.** $x^2+4y^2=4$, or $\frac{x^2}{4}+y^2=1$. An ellipse in the $xy$-plane.

**D10.** $z = \sqrt{9-x^2-y^2}$ (upper hemisphere). $z$ is always $\geq 0$, so no $xy$-plane symmetry (replacing $z\to-z$ changes the equation). $xz$-plane: $y\to-y$ unchanged → Yes. $yz$-plane: $x\to-x$ unchanged → Yes.

---

## Advanced Drill

**A1.** Distance between parallel planes: $\frac{|5-(-7)|}{\sqrt{4+1+4}} = \frac{12}{3} = 4$.

**A2.** Center = midpoint = $(4, 2, 1)$. Radius = half the distance between endpoints.
$d = \sqrt{(4)^2+(6)^2+(-4)^2} = \sqrt{16+36+16} = \sqrt{68} = 2\sqrt{17}$. Radius = $\sqrt{17}$.
Equation: $(x-4)^2+(y-2)^2+(z-1)^2 = 17$.

**A3.** $z=xy$. Level curves: $xy=c$. $c=0$: $x=0$ or $y=0$ (axes). $c>0$: hyperbolas in Q1/Q3. $c<0$: hyperbolas in Q2/Q4. The surface goes up in Q1/Q3, down in Q2/Q4 — saddle shape.

**A4.** Line: $(x,y,z) = (1+t, 2-t, 3+t)$. Plug into $2x+y-z=4$:
$2(1+t)+(2-t)-(3+t)=4 \to 2+2t+2-t-3-t=4 \to (2+2-3)+(2t-t-t)=4 \to 1+0=4$. Never. → **No intersection** (line is parallel to the plane).

**A5.** $\vec{n}_1 = (1,1,1)$, $\vec{n}_2 = (1,-1,2)$. Cross: $\vec{n} = (1\cdot2-1(-1), 1\cdot1-1\cdot2, 1(-1)-1\cdot1) = (3, -1, -2)$.
Simpler: $(1+2, 2-1, -1-1) = (3, 1, -2)$. Let's recompute: $\vec{n}_1 \times \vec{n}_2 = \det\begin{pmatrix}\hat{i}&\hat{j}&\hat{k}\\1&1&1\\1&-1&2\end{pmatrix} = \hat{i}(1\cdot2-1(-1)) - \hat{j}(1\cdot2-1\cdot1) + \hat{k}(1(-1)-1\cdot1) = (3, -1, -2)$.
Plane: $3(x-1)-(y-1)-2(z-1)=0 \to 3x-y-2z = 3-1-2 = 0$. → $3x-y-2z=0$.

**A6.** The cylinder is all points $(x,y,z)$ where $(x,y)$ satisfies $\frac{x^2}{4}+\frac{y^2}{9}=1$, $z$ arbitrary. Equation: $\frac{x^2}{4}+\frac{y^2}{9}=1$ (in 3D, this IS the cylinder — $z$ is free).

**A7.** Sphere 1: center $(0,0,0)$, $R_1=5$. Sphere 2: center $(8,0,0)$, $R_2=3$.
Distance between centers: $8$. Sum of radii: $8$. → They touch at exactly one point!
Intersection is a single point. The plane of contact: subtract sphere equations:
$(x^2+y^2+z^2-25) - ((x-8)^2+y^2+z^2-9) = 0 \to x^2+y^2+z^2-25 - (x^2-16x+64+y^2+z^2-9) = 0 \to 16x-80=0 \to x=5$.
The point of intersection: $(5,0,0)$. Check: $5^2+0+0=25$ ✅, $(5-8)^2+0+0=9$ ✅.

**A8.** Closest point along normal $(1,2,3)$. Point: $(t, 2t, 3t)$. On plane: $t+4t+9t=13 \to 14t=13 \to t=\frac{13}{14}$.
Point: $(\frac{13}{14}, \frac{26}{14}, \frac{39}{14}) = (\frac{13}{14}, \frac{13}{7}, \frac{39}{14})$.

**A9.** $x^2+4y^2-z^2=0$. At $z=2$: $x^2+4y^2=4 \to \frac{x^2}{4}+y^2=1$, ellipse. At $y=1$: $x^2+4-z^2=0 \to z^2-x^2=4$, hyperbola (vertical opening).

**A10.** Intercepts: $(2,0,0)$, $(0,3,0)$, $(0,0,4)$. Tetrahedron volume = $\frac{1}{6}|\det(\text{edge vectors})|$.
Edge vectors from $(0,0,0)$: $(2,0,0), (0,3,0), (0,0,4)$. Volume = $\frac{1}{6} \cdot 2 \cdot 3 \cdot 4 = \frac{24}{6} = 4$.
