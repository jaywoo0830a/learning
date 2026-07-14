# Solutions — 12A2: Matrices and Vectors

---

## Practice 1

**A $2 \times 2$ matrix $A$ has determinant 0. Geometric meaning + example.**

$\det(A) = 0$ means the transformation **collapses the plane** onto a line (or a point). The two column vectors are linearly dependent — they lie on the same line through the origin. The unit square (area 1) maps to a degenerate parallelogram of area 0.

**Example**: $A = \begin{pmatrix} 2 & 4 \\ 1 & 2 \end{pmatrix}$. $\det(A) = 2\cdot 2 - 4\cdot 1 = 0$.

Column 2 = $2 \times$ Column 1. The unit square collapses onto the line through $(2,1)$ — a line segment of zero area.

> **Answer**: Collapse onto a line; e.g., $A = \begin{pmatrix} 2 & 4 \\ 1 & 2 \end{pmatrix}$

---

## Practice 2

**Solve $\begin{cases} 3x - 2y = 7 \\ x + 4y = 5 \end{cases}$ by matrix inversion.**

$A = \begin{pmatrix} 3 & -2 \\ 1 & 4 \end{pmatrix}$, $\vec{b} = \begin{pmatrix} 7 \\ 5 \end{pmatrix}$.

$\det(A) = 3\cdot 4 - (-2)\cdot 1 = 12 + 2 = 14$.

$A^{-1} = \frac{1}{14}\begin{pmatrix} 4 & 2 \\ -1 & 3 \end{pmatrix}$.

$\vec{x} = A^{-1}\vec{b} = \frac{1}{14}\begin{pmatrix} 4 & 2 \\ -1 & 3 \end{pmatrix}\begin{pmatrix} 7 \\ 5 \end{pmatrix} = \frac{1}{14}\begin{pmatrix} 28+10 \\ -7+15 \end{pmatrix} = \frac{1}{14}\begin{pmatrix} 38 \\ 8 \end{pmatrix} = \begin{pmatrix} 38/14 \\ 8/14 \end{pmatrix} = \begin{pmatrix} 19/7 \\ 4/7 \end{pmatrix}$.

Check: $3(19/7) - 2(4/7) = 57/7 - 8/7 = 49/7 = 7$ ✓.
$(19/7) + 4(4/7) = 19/7 + 16/7 = 35/7 = 5$ ✓.

> **Answer**: $x = \frac{19}{7}$, $y = \frac{4}{7}$

---

## Practice 3

**$\vec{a} = (2, -1, 3)$, $\vec{b} = (1, 4, -2)$. Dot product, cross product, perpendicular check.**

**Dot product**: $\vec{a}\cdot\vec{b} = 2\cdot 1 + (-1)\cdot 4 + 3\cdot(-2) = 2 - 4 - 6 = -8$.

**Cross product**:
$\vec{a} \times \vec{b} = (a_2b_3-a_3b_2,\; a_3b_1-a_1b_3,\; a_1b_2-a_2b_1)$
$= ((-1)(-2)-3\cdot 4,\; 3\cdot 1-2(-2),\; 2\cdot 4-(-1)\cdot 1)$
$= (2-12,\; 3+4,\; 8+1)$
$= (-10,\; 7,\; 9)$.

**Perpendicular check**: Cross product should be perpendicular to both $\vec{a}$ and $\vec{b}$.
$(-10,7,9)\cdot(2,-1,3) = -20 - 7 + 27 = 0$ ✓.
$(-10,7,9)\cdot(1,4,-2) = -10 + 28 - 18 = 0$ ✓.

> **Answer**: $\vec{a}\cdot\vec{b} = -8$, $\vec{a}\times\vec{b} = (-10, 7, 9)$

---

## Practice 4

**Area of triangle $A(0,0,0)$, $B(3,1,0)$, $C(1,4,0)$.**

$\vec{AB} = (3,1,0)$, $\vec{AC} = (1,4,0)$.

$\vec{AB} \times \vec{AC} = (1\cdot 0 - 0\cdot 4,\; 0\cdot 1 - 3\cdot 0,\; 3\cdot 4 - 1\cdot 1) = (0,\; 0,\; 12-1) = (0, 0, 11)$.

$|\vec{AB} \times \vec{AC}| = \sqrt{0^2+0^2+11^2} = 11$.

Triangle area = $\frac{1}{2} \cdot 11 = \frac{11}{2}$.

> **Answer**: $\frac{11}{2}$

---

## Practice 5: Composition

**Reflection across $x$-axis × $90^\circ$ rotation — both orders.**

Reflection across $x$-axis: $R_x = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$.
$90^\circ$ CCW rotation: $R_{90} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$.

**Order 1 — Reflect then Rotate**: $R_{90} \cdot R_x = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.

This is reflection across $y=x$: swaps $x$ and $y$ coordinates. Geometrically: reflect across $x$-axis (flip vertical), then rotate $90^\circ$ CCW. A point $(x,y) \to (x,-y) \to (y,x)$.

**Order 2 — Rotate then Reflect**: $R_x \cdot R_{90} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$.

This is reflection across $y = -x$: $(x,y) \to (-y,-x)$. Geometrically: rotate $90^\circ$ CCW, then reflect across $x$-axis. $(x,y) \to (-y,x) \to (-y,-x)$.

The products differ — matrix multiplication order matters!

> **Answer**: $R_{90}R_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ (reflect across $y=x$), $R_x R_{90} = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$ (reflect across $y=-x$)

---

## Practice 6

**Scalar and vector projections of $\vec{a} = (5, 12)$ onto $\vec{b} = (3, 4)$.**

$\vec{a}\cdot\vec{b} = 5\cdot 3 + 12\cdot 4 = 15 + 48 = 63$.
$|\vec{b}| = \sqrt{3^2+4^2} = 5$.

**Scalar projection**: $\text{comp}_{\vec{b}}\vec{a} = \frac{\vec{a}\cdot\vec{b}}{|\vec{b}|} = \frac{63}{5} = 12.6$.

**Vector projection**: $\text{proj}_{\vec{b}}\vec{a} = \frac{\vec{a}\cdot\vec{b}}{|\vec{b}|^2}\vec{b} = \frac{63}{25}(3,4) = \left(\frac{189}{25}, \frac{252}{25}\right) = (7.56, 10.08)$.

Check: $|(7.56, 10.08)| = \sqrt{7.56^2+10.08^2} = \sqrt{57.15+101.61} \approx \sqrt{158.76} = 12.6$ ✓.

> **Answer**: Scalar projection = $\frac{63}{5}$, Vector projection = $\left(\frac{189}{25}, \frac{252}{25}\right)$

---

## Practice 7

**$A^{-1}$ for $A = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}$ and verify.**

$\det(A) = 2\cdot 3 - 1\cdot 5 = 6 - 5 = 1$.

$A^{-1} = \frac{1}{1}\begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix} = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}$.

Verify: $A \cdot A^{-1} = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}\begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix} = \begin{pmatrix} 6-5 & -2+2 \\ 15-15 & -5+6 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I$ ✓.

> **Answer**: $A^{-1} = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}$

---

## Practice 8: Real Battle

**$M$ has columns $\vec{v}_1=(2,0,0)$, $\vec{v}_2=(0,3,0)$, $\vec{v}_3=(0,0,5)$. Find $\det(M)$, volume of parallelepiped, and shape of $M$(unit cube).**

$M = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 5 \end{pmatrix}$ — a diagonal matrix.

$\det(M) = 2 \cdot 3 \cdot 5 = 30$.

The three column vectors are mutually perpendicular (along $x$, $y$, $z$ axes), so the parallelepiped they span is a **rectangular box** with dimensions $2 \times 3 \times 5$. Its volume = $2 \cdot 3 \cdot 5 = 30$.

Applying $M$ to the unit cube (vertices from $(0,0,0)$ to $(1,1,1)$): each point $(x,y,z) \to (2x, 3y, 5z)$. The unit cube stretches to a $2 \times 3 \times 5$ rectangular box. Volume = $30 = |\det(M)|$ ✓.

> **Answer**: $\det(M) = 30$, volume = 30, shape = $2\times 3\times 5$ rectangular box

---

## Basic Drill

### D1. Multiply $\begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix} \times \begin{pmatrix} 4 & -1 \\ 2 & 1 \end{pmatrix}$

$\begin{pmatrix} 2\cdot 4+1\cdot 2 & 2(-1)+1\cdot 1 \\ 0\cdot 4+3\cdot 2 & 0(-1)+3\cdot 1 \end{pmatrix} = \begin{pmatrix} 10 & -1 \\ 6 & 3 \end{pmatrix}$.

> **Answer**: $\begin{pmatrix} 10 & -1 \\ 6 & 3 \end{pmatrix}$

---

### D2. Determinant of $\begin{pmatrix} 3 & 5 \\ 2 & 4 \end{pmatrix}$

$\det = 3\cdot 4 - 5\cdot 2 = 12 - 10 = 2$.

> **Answer**: $2$

---

### D3. $|\vec{a}|$ for $\vec{a} = (6, -8)$

$|\vec{a}| = \sqrt{6^2 + (-8)^2} = \sqrt{36+64} = \sqrt{100} = 10$.

> **Answer**: $10$

---

### D4. $\vec{a}\cdot\vec{b}$ for $\vec{a}=(1,-2,3)$, $\vec{b}=(4,0,-1)$

$\vec{a}\cdot\vec{b} = 1\cdot 4 + (-2)\cdot 0 + 3\cdot(-1) = 4 + 0 - 3 = 1$.

> **Answer**: $1$

---

### D5. Add $\begin{pmatrix} 1 & 3 \\ 2 & -1 \end{pmatrix} + \begin{pmatrix} 4 & 0 \\ -2 & 5 \end{pmatrix}$

$\begin{pmatrix} 1+4 & 3+0 \\ 2+(-2) & -1+5 \end{pmatrix} = \begin{pmatrix} 5 & 3 \\ 0 & 4 \end{pmatrix}$.

> **Answer**: $\begin{pmatrix} 5 & 3 \\ 0 & 4 \end{pmatrix}$

---

### D6. $5 \cdot (-2, 3, 1)$

$(5\cdot(-2),\; 5\cdot 3,\; 5\cdot 1) = (-10, 15, 5)$.

> **Answer**: $(-10, 15, 5)$

---

### D7. $(2, 1, 0) \times (0, 3, 1)$

$(1\cdot 1 - 0\cdot 3,\; 0\cdot 0 - 2\cdot 1,\; 2\cdot 3 - 1\cdot 0) = (1-0,\; 0-2,\; 6-0) = (1, -2, 6)$.

> **Answer**: $(1, -2, 6)$

---

### D8. Unit vector in direction of $\vec{v} = (3, -4)$

$|\vec{v}| = \sqrt{9+16} = 5$.
$\hat{v} = \frac{(3,-4)}{5} = \left(\frac{3}{5}, -\frac{4}{5}\right) = (0.6, -0.8)$.

Check: $|(0.6, -0.8)| = \sqrt{0.36+0.64} = 1$ ✓.

> **Answer**: $\left(\frac{3}{5}, -\frac{4}{5}\right)$

---

### D9. $\det\begin{pmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix}$

Diagonal matrix: $\det = 1 \cdot 2 \cdot 3 = 6$.

> **Answer**: $6$

---

### D10. $\vec{u}\cdot\vec{v}$ for $\vec{u}=(2,-1)$, $\vec{v}=(-3,4)$. Perpendicular?

$\vec{u}\cdot\vec{v} = 2\cdot(-3) + (-1)\cdot 4 = -6 - 4 = -10$.
Not perpendicular (dot product $\neq 0$). Since $-10 < 0$, the angle is obtuse $(> 90^\circ)$.

> **Answer**: $-10$; not perpendicular

---

### D11. ◆ Geometry Fusion — Stretch matrix $A = \begin{pmatrix} 2 & 0 \\ 0 & 0.5 \end{pmatrix}$

**What happens**: The $x$-coordinate doubles, the $y$-coordinate halves. The unit square $[0,1]\times[0,1]$ becomes a $2 \times 0.5$ rectangle.

**Area**: $2 \times 0.5 = 1$. **Wait** — but $\det(A) = 2 \cdot 0.5 - 0 \cdot 0 = 1$. So area = $1 = |\det(A)|$ ✓. The stretching in $x$ is exactly compensated by the shrinking in $y$.

**Geometric picture**: The square stretches horizontally and squishes vertically. Like pulling taffy.

> **Answer**: Rectangle $2 \times 0.5$, area = 1, $\det(A) = 1$

---

### D12. ◆ Geometry Fusion — Columns $\vec{c}_1=(4,0)$, $\vec{c}_2=(1,3)$

$A = \begin{pmatrix} 4 & 1 \\ 0 & 3 \end{pmatrix}$.

The column vectors span a parallelogram. $\vec{c}_1$ is along the $x$-axis (length 4). $\vec{c}_2 = (1,3)$ goes up and right. The base is 4, the height is the $y$-component of $\vec{c}_2$, which is 3.

Area = base × height = $4 \times 3 = 12$.

$\det(A) = 4\cdot 3 - 1\cdot 0 = 12$ ✓.

> **Answer**: Parallelogram of area 12, $A = \begin{pmatrix} 4 & 1 \\ 0 & 3 \end{pmatrix}$, $\det(A) = 12$

---

### D13. ◆ Geometry Fusion — $\vec{v}=(2,5)$ transformed by $A=\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$

$A\vec{v} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 2 \\ 5 \end{pmatrix} = \begin{pmatrix} -5 \\ 2 \end{pmatrix}$.

**Angle**: $\vec{v}\cdot A\vec{v} = 2(-5) + 5(2) = -10 + 10 = 0$. Dot product = 0 → $90^\circ$ angle ✓.

$A$ is the $90^\circ$ CCW rotation matrix. It rotates every vector by exactly $90^\circ$ while preserving its length: $|(2,5)| = \sqrt{29}$, $|(-5,2)| = \sqrt{29}$ ✓.

> **Answer**: $A\vec{v} = (-5, 2)$, angle = $90^\circ$, $A$ rotates by $90^\circ$ CCW

---

### D14. ◆ Geometry Fusion — Singular matrix $B = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$

$\det(B) = 1\cdot 4 - 2\cdot 2 = 0$.

**Columns**: $\vec{c}_1 = (1,2)$, $\vec{c}_2 = (2,4) = 2\cdot\vec{c}_1$. They are parallel — both lie on the line $y=2x$.

**Collapse**: Every point $(x,y)$ maps to $B\vec{x} = (x+2y,\; 2x+4y) = (x+2y,\; 2(x+2y))$. The output always lies on the line $y=2x$. The entire plane collapses onto this single line. The image (range) is the line $y=2x$ — a 1D subspace.

> **Answer**: Columns are parallel (line $y=2x$), plane collapses to line $y=2x$

---

### D15. ◆ Geometry Fusion — Shear $S = \begin{pmatrix} 1 & 1.5 \\ 0 & 1 \end{pmatrix}$ on $\vec{v}=(2,1)$

$S\vec{v} = \begin{pmatrix} 1\cdot 2 + 1.5\cdot 1 \\ 0\cdot 2 + 1\cdot 1 \end{pmatrix} = \begin{pmatrix} 3.5 \\ 1 \end{pmatrix}$.

The $y$-coordinate is unchanged (1 → 1). The $x$-coordinate shifted by $1.5 \times y$.

$\det(S) = 1\cdot 1 - 1.5\cdot 0 = 1$. A shear preserves area because it "slides" each horizontal line by an amount proportional to its height — like pushing a deck of cards. The shape changes but the total area stays the same.

> **Answer**: $S\vec{v} = (3.5, 1)$, $y$ unchanged, area preserved ($\det=1$)

---

## Advanced Drill

### A1. $A^{-1}$ for $A = \begin{pmatrix} 4 & 3 \\ 3 & 2 \end{pmatrix}$, verify

$\det(A) = 4\cdot 2 - 3\cdot 3 = 8 - 9 = -1$.

$A^{-1} = \frac{1}{-1}\begin{pmatrix} 2 & -3 \\ -3 & 4 \end{pmatrix} = \begin{pmatrix} -2 & 3 \\ 3 & -4 \end{pmatrix}$.

Verify: $A \cdot A^{-1} = \begin{pmatrix} 4 & 3 \\ 3 & 2 \end{pmatrix}\begin{pmatrix} -2 & 3 \\ 3 & -4 \end{pmatrix} = \begin{pmatrix} -8+9 & 12-12 \\ -6+6 & 9-8 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I$ ✓.

> **Answer**: $A^{-1} = \begin{pmatrix} -2 & 3 \\ 3 & -4 \end{pmatrix}$

---

### A2. Vector perpendicular to $\vec{a}=(1,2,3)$ and $\vec{b}=(4,5,6)$

$\vec{a}\times\vec{b} = (2\cdot 6-3\cdot 5,\; 3\cdot 4-1\cdot 6,\; 1\cdot 5-2\cdot 4) = (12-15,\; 12-6,\; 5-8) = (-3, 6, -3)$.

Check: $(-3,6,-3)\cdot(1,2,3) = -3+12-9 = 0$ ✓, $(-3,6,-3)\cdot(4,5,6) = -12+30-18 = 0$ ✓.

Can simplify by factoring $3$: $(-1, 2, -1)$ is also perpendicular.

> **Answer**: $(-3, 6, -3)$ (or any scalar multiple)

---

### A3. Rotation matrix for $60^\circ$ CCW, apply to $(1,0)$

$R_{60} = \begin{pmatrix} \cos 60^\circ & -\sin 60^\circ \\ \sin 60^\circ & \cos 60^\circ \end{pmatrix} = \begin{pmatrix} 1/2 & -\sqrt{3}/2 \\ \sqrt{3}/2 & 1/2 \end{pmatrix}$.

$R_{60}\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 1/2 \\ \sqrt{3}/2 \end{pmatrix} = (0.5,\; 0.866...)$.

This is exactly the first column of $R_{60}$ — because applying the rotation to $\vec{e}_1$ gives column 1.

> **Answer**: $R_{60} = \begin{pmatrix} 1/2 & -\sqrt{3}/2 \\ \sqrt{3}/2 & 1/2 \end{pmatrix}$, result = $(\frac{1}{2}, \frac{\sqrt{3}}{2})$

---

### A4. Solve $2x+y-z=3$, $x-y+2z=1$, $3x+2y+z=7$

$A = \begin{pmatrix} 2 & 1 & -1 \\ 1 & -1 & 2 \\ 3 & 2 & 1 \end{pmatrix}$.

$\det(A) = 2(-1\cdot 1 - 2\cdot 2) - 1(1\cdot 1 - 2\cdot 3) + (-1)(1\cdot 2 - (-1)\cdot 3)$
$= 2(-1-4) - 1(1-6) - 1(2+3) = 2(-5) - (-5) - 5 = -10 + 5 - 5 = -10$.

Cramer's rule or Gaussian elimination:
From eq (2): $x = 1 + y - 2z$. Substitute into (1): $2(1+y-2z) + y - z = 3 \to 2+2y-4z+y-z = 3 \to 3y-5z = 1$.
Into (3): $3(1+y-2z) + 2y + z = 7 \to 3+3y-6z+2y+z = 7 \to 5y-5z = 4 \to y-z = \frac{4}{5}$.

From $y = z + \frac{4}{5}$: $3(z+\frac{4}{5}) - 5z = 1 \to 3z + \frac{12}{5} - 5z = 1 \to -2z = 1 - \frac{12}{5} = -\frac{7}{5} \to z = \frac{7}{10}$.

$y = \frac{7}{10} + \frac{4}{5} = \frac{7}{10} + \frac{8}{10} = \frac{15}{10} = \frac{3}{2}$.
$x = 1 + \frac{3}{2} - 2\cdot\frac{7}{10} = 1 + \frac{3}{2} - \frac{14}{10} = \frac{10}{10} + \frac{15}{10} - \frac{14}{10} = \frac{11}{10}$.

Check: $2(\frac{11}{10}) + \frac{3}{2} - \frac{7}{10} = \frac{22}{10} + \frac{15}{10} - \frac{7}{10} = \frac{30}{10} = 3$ ✓.

> **Answer**: $x = \frac{11}{10}$, $y = \frac{3}{2}$, $z = \frac{7}{10}$

---

### A5. Angle between $\vec{a}=(1,1,0)$ and $\vec{b}=(0,1,1)$

$\vec{a}\cdot\vec{b} = 1\cdot 0 + 1\cdot 1 + 0\cdot 1 = 1$.
$|\vec{a}| = \sqrt{2}$, $|\vec{b}| = \sqrt{2}$.

$\cos\theta = \frac{1}{\sqrt{2}\cdot\sqrt{2}} = \frac{1}{2}$.
$\theta = \arccos(\frac{1}{2}) = 60^\circ = \frac{\pi}{3}$.

> **Answer**: $60^\circ$ (or $\pi/3$)

---

### A6. Projections of $\vec{a}=(5,12)$ onto $\vec{b}=(3,4)$

$\vec{a}\cdot\vec{b} = 15+48 = 63$, $|\vec{b}| = 5$.

Scalar: $\text{comp}_{\vec{b}}\vec{a} = \frac{63}{5} = 12.6$.
Vector: $\text{proj}_{\vec{b}}\vec{a} = \frac{63}{25}(3,4) = \left(\frac{189}{25}, \frac{252}{25}\right) = (7.56, 10.08)$.

> **Answer**: Scalar = $63/5$, Vector = $(189/25, 252/25)$

---

### A7. $A^2$ for $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$

$A^2 = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = \begin{pmatrix} 1\cdot 1+2\cdot 3 & 1\cdot 2+2\cdot 4 \\ 3\cdot 1+4\cdot 3 & 3\cdot 2+4\cdot 4 \end{pmatrix} = \begin{pmatrix} 7 & 10 \\ 15 & 22 \end{pmatrix}$.

> **Answer**: $\begin{pmatrix} 7 & 10 \\ 15 & 22 \end{pmatrix}$

---

### A8. Triangle area with vertices $(0,0,0)$, $(2,1,0)$, $(0,3,0)$

$\vec{AB} = (2,1,0)$, $\vec{AC} = (0,3,0)$.

$\vec{AB}\times\vec{AC} = (1\cdot 0-0\cdot 3,\; 0\cdot 0-2\cdot 0,\; 2\cdot 3-1\cdot 0) = (0, 0, 6)$.

Area = $\frac{1}{2}|\vec{AB}\times\vec{AC}| = \frac{1}{2} \cdot 6 = 3$.

> **Answer**: $3$

---

### A9. Find $2\times 2$ matrix $A$ with $A^2=I$, $A \neq \pm I$

Any reflection matrix works. For example, reflection across $y=x$:

$A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.

$A^2 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I$ ✓.
And $A \neq I$ and $A \neq -I$ ✓.

Other examples: $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ (reflect across $x$-axis), $\begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$ (reflect across $y$-axis), $\begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$ (reflect across $y=-x$).

> **Answer**: $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ (reflection across $y=x$)

---

### A10. Parallelogram area from columns $(3,1)$ and $(1,3)$

$A = \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}$. $\det(A) = 3\cdot 3 - 1\cdot 1 = 9 - 1 = 8$.

Area = $|\det(A)| = 8$.

Alternatively: the two vectors span a rhombus (equal length: $|(3,1)| = |(1,3)| = \sqrt{10}$). Area = base × height or via cross product magnitude.

> **Answer**: $8$

---

### A11. ◆ Geometry Fusion — Shear then Rotate $90^\circ$

$S = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, $R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$.

Combined: $RS = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 0\cdot 1 + (-1)\cdot 0 & 0\cdot 1 + (-1)\cdot 1 \\ 1\cdot 1 + 0\cdot 0 & 1\cdot 1 + 0\cdot 1 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 1 & 1 \end{pmatrix}$.

Apply to unit square vertices:
$(0,0) \to (0,0)$.
$(1,0) \to (0,1)$.
$(1,1) \to (-1,2)$.
$(0,1) \to (-1,1)$.

$\det(RS) = 0\cdot 1 - (-1)\cdot 1 = 1$. The determinant is the product: $\det(R)\cdot\det(S) = 1 \cdot 1 = 1$. The transformation preserves area — it's a composition of two area-preserving operations (rotation + shear).

**Sketch**: A rotated-and-sheared parallelogram; vertices connect $(0,0)\to(0,1)\to(-1,2)\to(-1,1)\to(0,0)$.

> **Answer**: $RS = \begin{pmatrix} 0 & -1 \\ 1 & 1 \end{pmatrix}$, $\det = 1$ (area preserved)

---

### A12. ◆ Geometry Fusion — $P = \begin{pmatrix} 3/5 & 4/5 \\ 4/5 & -3/5 \end{pmatrix}$

$P\vec{v} = \begin{pmatrix} 3/5 & 4/5 \\ 4/5 & -3/5 \end{pmatrix}\begin{pmatrix} 5 \\ 0 \end{pmatrix} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$.

**Angle**: $\vec{v}\cdot P\vec{v} = (5,0)\cdot(3,4) = 15+0 = 15$.
$|\vec{v}| = 5$, $|P\vec{v}| = \sqrt{9+16} = 5$.
$\cos\theta = \frac{15}{5\cdot 5} = \frac{3}{5}$, so $\theta = \arccos(0.6) \approx 53.13^\circ$.

$\det(P) = (3/5)(-3/5) - (4/5)(4/5) = -9/25 - 16/25 = -25/25 = -1$.

$P$ is a **reflection**. $\det = -1$ confirms it's not a rotation (rotations have $\det = +1$). $P^2=I$ and $P=P^T$ means it's an orthogonal reflection. The reflection line is through the eigenvector with eigenvalue 1: solving $P\vec{x} = \vec{x}$ gives direction $(2,1)$. So $P$ reflects across the line $y = x/2$ (or more precisely, the line through the origin with slope $1/2$, since $(2,1)$ is on $y=x/2$).

> **Answer**: $P\vec{v} = (3,4)$, $\theta \approx 53.13^\circ$, reflection across line through $(2,1)$

---

### A13. ◆ Geometry Fusion — Projection matrix onto line $y=2x$

Direction vector of line $y=2x$: $\vec{d} = (1, 2)$. Normalize: $|\vec{d}| = \sqrt{5}$.

Projection formula: $\text{proj}_{\vec{d}}\vec{v} = \frac{\vec{v}\cdot\vec{d}}{|\vec{d}|^2}\vec{d} = \frac{x+2y}{5}(1,2)$.

So $A = \frac{1}{5}\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix} = \begin{pmatrix} 1/5 & 2/5 \\ 2/5 & 4/5 \end{pmatrix}$.

Apply to $(3,1)$: $A\begin{pmatrix} 3 \\ 1 \end{pmatrix} = \frac{1}{5}\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}\begin{pmatrix} 3 \\ 1 \end{pmatrix} = \frac{1}{5}\begin{pmatrix} 3+2 \\ 6+4 \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$.

Check that $(1,2)$ lies on $y=2x$: $2 = 2\cdot 1$ ✓.

$\det(A) = (1/5)(4/5) - (2/5)(2/5) = 4/25 - 4/25 = 0$.

Geometric meaning: A projection collapses the 2D plane onto a 1D line — all area is lost, so $\det=0$. The matrix is singular.

> **Answer**: $A = \frac{1}{5}\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$, result = $(1,2)$ on $y=2x$, $\det=0$ (collapses to line)

---

### A14. ◆ Geometry Fusion — Parallelogram in 3D, area and perpendicular

$\vec{a} = (4,1,2)$, $\vec{b} = (1,3,-1)$.

$\vec{a}\times\vec{b} = (1\cdot(-1)-2\cdot 3,\; 2\cdot 1-4\cdot(-1),\; 4\cdot 3-1\cdot 1)$
$= (-1-6,\; 2+4,\; 12-1) = (-7, 6, 11)$.

Area = $|\vec{a}\times\vec{b}| = \sqrt{(-7)^2 + 6^2 + 11^2} = \sqrt{49+36+121} = \sqrt{206}$.

Unit normal: $\hat{n} = \frac{(-7,6,11)}{\sqrt{206}}$.

Matrix $M = [\vec{a}\; \vec{b}\; \vec{a}\times\vec{b}] = \begin{pmatrix} 4 & 1 & -7 \\ 1 & 3 & 6 \\ 2 & -1 & 11 \end{pmatrix}$.

$\det(M) = \vec{a} \cdot (\vec{b} \times (\vec{a}\times\vec{b}))$. But geometrically: the third column is perpendicular to the plane of the first two columns. So the three columns form a rectangular box-like shape. The volume = (area of base) × (height). The height = $|\vec{a}\times\vec{b}|$ (since the third column IS $\vec{a}\times\vec{b}$), and the area of the base formed by $\vec{a}$ and $\vec{b}$ is $|\vec{a}\times\vec{b}| = \sqrt{206}$.

So $\det(M) = |\vec{a} \times \vec{b}| \cdot |\vec{a} \times \vec{b}| = (\sqrt{206})^2 = 206$.

Let's verify computationally: $\det(M) = 4(3\cdot 11 - 6\cdot(-1)) - 1(1\cdot 11 - 6\cdot 2) + (-7)(1\cdot(-1) - 3\cdot 2)$
$= 4(33+6) - 1(11-12) - 7(-1-6) = 4(39) - (-1) - 7(-7) = 156 + 1 + 49 = 206$ ✓.

> **Answer**: Area = $\sqrt{206}$, $\hat{n} = \frac{(-7,6,11)}{\sqrt{206}}$, $\det(M) = 206$

---

### A15. ◆ Geometry Fusion — $A = \begin{pmatrix} 0.8 & -0.6 \\ 0.6 & 0.8 \end{pmatrix}$ on triangle

Original triangle vertices: $(0,0)$, $(2,0)$, $(0,1)$. Area = $\frac{1}{2} \cdot 2 \cdot 1 = 1$.

Transformed vertices:
$(0,0) \to (0,0)$.
$(2,0) \to (0.8\cdot 2,\; 0.6\cdot 2) = (1.6, 1.2)$.
$(0,1) \to (-0.6, 0.8)$.

Transformed area = $\frac{1}{2}|1.6\cdot 0.8 - 1.2\cdot(-0.6)| = \frac{1}{2}|1.28 + 0.72| = \frac{1}{2} \cdot 2 = 1$.

The areas are equal (both 1) because $|\det(A)| = |0.8\cdot 0.8 - (-0.6)\cdot 0.6| = |0.64 + 0.36| = |1| = 1$.

**Is $A$ a pure rotation?** Check: Columns have length $\sqrt{0.8^2+0.6^2} = \sqrt{0.64+0.36} = 1$ each, and dot product = $0.8(-0.6) + 0.6(0.8) = -0.48+0.48 = 0$ — columns are orthonormal. $\det = +1$.

This looks like $\cos\theta = 0.8$, $\sin\theta = 0.6$, so $\theta = \arcsin(0.6) = \arccos(0.8) \approx 36.87^\circ$. Yes, $A$ is a pure rotation by $\approx 36.87^\circ$ CCW. A pure rotation: orthonormal columns + determinant $+1$.

> **Answer**: Original area = 1, transformed area = 1 (equal because $|\det|=1$). Yes, pure rotation by $\approx 36.87^\circ$
