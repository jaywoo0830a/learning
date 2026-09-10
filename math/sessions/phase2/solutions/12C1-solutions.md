# Solutions — 12C1: Geometric Transformations — Moving and Shaping Space
## Basic Drills

### D1. Multiply: $\begin{pmatrix} \cos 30^\circ & -\sin 30^\circ \\ \sin 30^\circ & \cos 30^\circ \end{pmatrix}\begin{pmatrix} 2 \\ 0 \end{pmatrix}$. Give exact coordinates.

$\cos30^\circ = \frac{\sqrt3}{2}$, $\sin30^\circ = \frac12$.
$\begin{pmatrix} \sqrt3/2 & -1/2 \\ 1/2 & \sqrt3/2 \end{pmatrix}\begin{pmatrix}2\\0\end{pmatrix} = \begin{pmatrix} \sqrt3 \\ 1 \end{pmatrix}$.

> **Answer**: $(\sqrt3, 1)$

---

### D2. Write the $2 \times 2$ matrix that scales $x$ by 4 and $y$ by $\frac{1}{2}$.

$S = \begin{pmatrix} 4 & 0 \\ 0 & 1/2 \end{pmatrix}$.

> **Answer**: $\begin{pmatrix}4&0\\0&1/2\end{pmatrix}$

---

### D3. Write the $3 \times 3$ homogeneous matrix that translates by $(5, -3)$.

$T = \begin{pmatrix} 1 & 0 & 5 \\ 0 & 1 & -3 \\ 0 & 0 & 1 \end{pmatrix}$.

> **Answer**: $\begin{pmatrix}1&0&5\\0&1&-3\\0&0&1\end{pmatrix}$

---

### D4. Compute $R_{60^\circ} \cdot R_{30^\circ}$ (rotation matrices). What single rotation does this equal?

$R_{60}R_{30} = R_{90^\circ}$ (composing rotations adds the angles).
$R_{90^\circ} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$.

> **Answer**: $R_{90^\circ} = \begin{pmatrix}0&-1\\1&0\end{pmatrix}$

---

### D5. Find the determinant of the shear matrix $\begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}$. Why does the answer make geometric sense?

$\det = 1\cdot1 - 3\cdot0 = 1$. Shear preserves area — it slides rows of a grid without changing the overall area. The unit square becomes a parallelogram of the same area.

> **Answer**: $\det = 1$, shear preserves area

---

### D6. Apply the reflection $F_{45^\circ}$ (across line at $45^\circ$) to the vector $(1, 0)$.

$F_{45^\circ} = \begin{pmatrix} \cos90^\circ & \sin90^\circ \\ \sin90^\circ & -\cos90^\circ \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.
$F_{45^\circ}\begin{pmatrix}1\\0\end{pmatrix} = \begin{pmatrix}0\\1\end{pmatrix}$.
Reflection across $y=x$ swaps the coordinates.

> **Answer**: $(0, 1)$

---

### D7. Write the $2 \times 2$ matrix that first reflects across the $x$-axis, then rotates by $90^\circ$ CCW. What geometric transformation is the result?

Reflect across $x$-axis: $F_0 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$.
Rotate $90^\circ$ CCW: $R_{90} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$.

$M = R_{90} \cdot F_0 = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.
This is reflection across $y=x$.

> **Answer**: $M = \begin{pmatrix}0&1\\1&0\end{pmatrix}$, reflection across $y=x$

---

### D8. Write the $3 \times 3$ homogeneous matrix for scaling by factor 2 in both $x$ and $y$ about the point $(1, 1)$.

(1) Translate $(-1,-1)$: $T_- = \begin{pmatrix}1&0&-1\\0&1&-1\\0&0&1\end{pmatrix}$.
(2) Scale: $S = \begin{pmatrix}2&0&0\\0&2&0\\0&0&1\end{pmatrix}$.
(3) Translate back: $T_+ = \begin{pmatrix}1&0&1\\0&1&1\\0&0&1\end{pmatrix}$.

$M = T_+ S T_- = \begin{pmatrix}1&0&1\\0&1&1\\0&0&1\end{pmatrix}\begin{pmatrix}2&0&0\\0&2&0\\0&0&1\end{pmatrix}\begin{pmatrix}1&0&-1\\0&1&-1\\0&0&1\end{pmatrix}$
$= \begin{pmatrix}2&0&1\\0&2&1\\0&0&1\end{pmatrix}\begin{pmatrix}1&0&-1\\0&1&-1\\0&0&1\end{pmatrix} = \begin{pmatrix}2&0&-1\\0&2&-1\\0&0&1\end{pmatrix}$.

Test on $(1,1)$: $M(1,1,1)^T = (2-1, 2-1, 1) = (1,1,1)$ — fixed point ✓.
Test on $(2,2)$: $M(2,2,1)^T = (4-1, 4-1, 1) = (3,3,1)$ — distance from $(1,1)$ doubles ✓.

> **Answer**: $M = \begin{pmatrix}2&0&-1\\0&2&-1\\0&0&1\end{pmatrix}$

---

### D9. Compute $F_0 \cdot F_{45^\circ}$ (reflect across $x$-axis, then across $y=x$). Identify the result as a rotation.

$F_0 = \begin{pmatrix}1&0\\0&-1\end{pmatrix}$, $F_{45^\circ} = \begin{pmatrix}0&1\\1&0\end{pmatrix}$.

$M = F_0 \cdot F_{45^\circ} = \begin{pmatrix}1&0\\0&-1\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix} = \begin{pmatrix}0&1\\-1&0\end{pmatrix}$.

This is $R_{-90^\circ}$ — rotation by $90^\circ$ clockwise (or $270^\circ$ CCW).
Indeed, two reflections compose to a rotation by twice the angle between the mirrors: $2 \times (45^\circ - 0^\circ) = 90^\circ$.

> **Answer**: $M = \begin{pmatrix}0&1\\-1&0\end{pmatrix} = R_{-90^\circ}$

---

### D10. A square has vertices $(\pm 1, \pm 1)$. Apply the matrix $\begin{pmatrix} 0 & 2 \\ -3 & 0 \end{pmatrix}$. What is the area of the resulting shape?

$\det = 0\cdot 0 - 2\cdot(-3) = 6$.
Original area of square (side 2) = $4$.
Area after transformation = $|\det| \times$ original area = $6 \times 4 = 24$.

> **Answer**: $24$

---

## Advanced Drills

### A1. Find the eigenvalues of the reflection matrix $F_\alpha = \begin{pmatrix} \cos 2\alpha & \sin 2\alpha \\ \sin 2\alpha & -\cos 2\alpha \end{pmatrix}$. Interpret them geometrically.

$\det(F_\alpha - \lambda I) = (\cos2\alpha - \lambda)(-\cos2\alpha - \lambda) - \sin^2 2\alpha = 0$.
$= -\cos^2 2\alpha + \lambda^2 - \sin^2 2\alpha = \lambda^2 - (\cos^2 2\alpha + \sin^2 2\alpha) = \lambda^2 - 1 = 0$.
$\lambda = \pm 1$.

Geometric interpretation: $\lambda = 1$ corresponds to vectors along the mirror line (unchanged). $\lambda = -1$ corresponds to vectors perpendicular to the mirror (flipped direction). These are the only two possibilities for a reflection.

> **Answer**: $\lambda = 1$ (along mirror), $\lambda = -1$ (perpendicular to mirror)

---

### A2. Write the $4 \times 4$ homogeneous matrix for a $90^\circ$ rotation around the $z$-axis in 3D, followed by translation by $(1, 2, 3)$.

$R_z = \begin{pmatrix} 0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$, $T = \begin{pmatrix} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 2 \\ 0 & 0 & 1 & 3 \\ 0 & 0 & 0 & 1 \end{pmatrix}$.

$M = T \cdot R_z = \begin{pmatrix} 0 & -1 & 0 & 1 \\ 1 & 0 & 0 & 2 \\ 0 & 0 & 1 & 3 \\ 0 & 0 & 0 & 1 \end{pmatrix}$.

> **Answer**: $M = \begin{pmatrix}0&-1&0&1\\1&0&0&2\\0&0&1&3\\0&0&0&1\end{pmatrix}$

---

### A3. A matrix $A$ has columns $(3, 1)$ and $(1, 3)$. Find its singular values by computing the eigenvalues of $A^T A$.

$A = \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}$.
$A^T A = \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}\begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix} = \begin{pmatrix} 9+1 & 3+3 \\ 3+3 & 1+9 \end{pmatrix} = \begin{pmatrix} 10 & 6 \\ 6 & 10 \end{pmatrix}$.

Eigenvalues of $A^T A$: $\det(A^T A - \lambda I) = (10-\lambda)^2 - 36 = 0$.
$\lambda^2 - 20\lambda + 100 - 36 = 0 \implies \lambda^2 - 20\lambda + 64 = 0 \implies (\lambda-4)(\lambda-16) = 0$.
$\lambda_1 = 16$, $\lambda_2 = 4$.

Singular values: $\sigma_1 = \sqrt{16} = 4$, $\sigma_2 = \sqrt{4} = 2$.

> **Answer**: $\sigma_1 = 4$, $\sigma_2 = 2$

---

### A4. Prove that the composition of two reflections is a rotation. (Multiply $F_\alpha \cdot F_\beta$ and identify the result.)

$F_\alpha F_\beta = \begin{pmatrix} \cos2\alpha & \sin2\alpha \\ \sin2\alpha & -\cos2\alpha \end{pmatrix}\begin{pmatrix} \cos2\beta & \sin2\beta \\ \sin2\beta & -\cos2\beta \end{pmatrix}$.

First row, first column: $\cos2\alpha\cos2\beta + \sin2\alpha\sin2\beta = \cos(2\alpha-2\beta)$.
First row, second column: $\cos2\alpha\sin2\beta - \sin2\alpha\cos2\beta = \sin(2\beta-2\alpha) = -\sin(2\alpha-2\beta)$.
Second row, first column: $\sin2\alpha\cos2\beta - \cos2\alpha\sin2\beta = \sin(2\alpha-2\beta)$.
Second row, second column: $\sin2\alpha\sin2\beta + \cos2\alpha\cos2\beta = \cos(2\alpha-2\beta)$.

So $F_\alpha F_\beta = \begin{pmatrix} \cos(2\alpha-2\beta) & -\sin(2\alpha-2\beta) \\ \sin(2\alpha-2\beta) & \cos(2\alpha-2\beta) \end{pmatrix} = R_{2(\alpha-\beta)}$.

The composition of two reflections is a rotation by twice the angle between the mirror lines.

> **Answer**: $F_\alpha F_\beta = R_{2(\alpha-\beta)}$ — a rotation

---

### A5. Find a $3 \times 3$ homogeneous matrix that shears the plane so that the $x$-axis stays fixed, but the $y$-axis tilts to point at $30^\circ$ from vertical.

We want a shear that maps $(1,0) \to (1,0)$ (x-axis fixed) and $(0,1) \to (k, 1)$ where the new direction makes $30^\circ$ from vertical.

If the $y$-axis tilts by $30^\circ$ from vertical, then the angle from the horizontal is $60^\circ$.
The direction vector is $(\cos60^\circ, \sin60^\circ) = (1/2, \sqrt3/2)$.

But we need $(0,1) \to (k, 1)$ to have direction $(k, 1)$ making $30^\circ$ from vertical.
$\tan(30^\circ) = \frac{k}{1} = \frac{1}{\sqrt3}$, so $k = \frac{1}{\sqrt3}$.

Shear matrix: $H = \begin{pmatrix} 1 & 1/\sqrt3 \\ 0 & 1 \end{pmatrix}$.
In homogeneous: $M = \begin{pmatrix} 1 & 1/\sqrt3 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$.

> **Answer**: $M = \begin{pmatrix} 1 & 1/\sqrt3 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$

---

### A6. A square with vertices $(\pm1, \pm1)$ is transformed by $A = \begin{pmatrix} 2 & 1 \\ 0.5 & 1.5 \end{pmatrix}$. Find the area of the resulting parallelogram.

$\det(A) = 2 \cdot 1.5 - 1 \cdot 0.5 = 3 - 0.5 = 2.5$.
Original area of square (side 2) = $4$.
Area of transformed shape = $|\det(A)| \times 4 = 2.5 \times 4 = 10$.

> **Answer**: $10$

---

### A7. Find the eigenvalues and eigenvectors of the rotation matrix $R_\theta$. Show that real eigenvectors exist only for $\theta = 0^\circ$ or $180^\circ$.

$R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$.

Characteristic equation: $(\cos\theta-\lambda)^2 + \sin^2\theta = 0 \implies \lambda^2 - 2\lambda\cos\theta + 1 = 0$.
$\lambda = \cos\theta \pm i\sin\theta = e^{\pm i\theta}$.

For $\theta \neq 0^\circ, 180^\circ$, $\lambda$ is complex → no real eigenvectors.

For $\theta = 0^\circ$: $R_0 = I$, $\lambda = 1$, every vector is an eigenvector.
For $\theta = 180^\circ$: $R_{180} = -I$, $\lambda = -1$, every vector is an eigenvector.

> **Answer**: $\lambda = e^{\pm i\theta}$, real only when $\theta = 0^\circ, 180^\circ$

---

### A8. A matrix $A$ has SVD $A = U\Sigma V^T$ with $\Sigma = \begin{pmatrix} 3 & 0 \\ 0 & 0 \end{pmatrix}$. What is the rank of $A$? Describe geometrically what $A$ does to the plane.

Rank = number of non-zero singular values = 1.

Geometrically: $A$ collapses the 2D plane onto a 1D line. $V^T$ rotates the input, $\Sigma$ scales by 3 in one direction and sends the perpendicular direction to zero, then $U$ rotates the result. Every point in the plane maps to a point on a line through the origin.

> **Answer**: Rank = 1, collapses the plane onto a line

---

### A9. Derive the $3 \times 3$ homogeneous matrix for reflection across an arbitrary line $y = mx + b$ in 2D.

(1) Translate by $(0, -b)$ to move the intercept to the origin: $T_1 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & -b \\ 0 & 0 & 1 \end{pmatrix}$.
(2) Reflect across $y = mx$ (line through origin). The angle $\alpha = \arctan(m)$.
$F_\alpha = \begin{pmatrix} \cos2\alpha & \sin2\alpha & 0 \\ \sin2\alpha & -\cos2\alpha & 0 \\ 0 & 0 & 1 \end{pmatrix}$.
(3) Translate back: $T_2 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & b \\ 0 & 0 & 1 \end{pmatrix}$.

$M = T_2 \cdot F_\alpha \cdot T_1$.

> **Answer**: $M = T_2 F_\alpha T_1$ with $T_1, T_2, F_\alpha$ as above

---

### A10. A shear matrix $H_x(k)$ has determinant 1. What geometric property must any matrix with determinant 1 have? Verify that $H_x(k)$ preserves area by transforming a unit square.

Any matrix with $\det = 1$ preserves area (and orientation if $\det > 0$).

For $H_x(k) = \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$, apply to the unit square vertices:
$(0,0) \to (0,0)$, $(1,0) \to (1,0)$, $(1,1) \to (1+k, 1)$, $(0,1) \to (k, 1)$.

The resulting shape is a parallelogram with base 1 (from $(0,0)$ to $(1,0)$) and height 1 (vertical separation). The area = base $\times$ height = $1 \cdot 1 = 1$, same as the original unit square. ✓

> **Answer**: $\det = 1$ preserves area; verified with unit square

---

### A11. (🔗 9C) A point on a sphere of radius 5 at spherical coordinates $(\rho=5, \phi=\pi/3, \theta=\pi/4)$ is rotated by $30^\circ$ around the $z$-axis. Use $R_z$ to find its new Cartesian coordinates.

First convert to Cartesian:
$x = 5\sin(\pi/3)\cos(\pi/4) = 5 \cdot \frac{\sqrt3}{2} \cdot \frac{\sqrt2}{2} = \frac{5\sqrt6}{4}$.
$y = 5\sin(\pi/3)\sin(\pi/4) = 5 \cdot \frac{\sqrt3}{2} \cdot \frac{\sqrt2}{2} = \frac{5\sqrt6}{4}$.
$z = 5\cos(\pi/3) = 5 \cdot \frac12 = \frac52$.

Rotation by $30^\circ$ around $z$-axis:
$R_z = \begin{pmatrix} \cos30^\circ & -\sin30^\circ & 0 \\ \sin30^\circ & \cos30^\circ & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} \sqrt3/2 & -1/2 & 0 \\ 1/2 & \sqrt3/2 & 0 \\ 0 & 0 & 1 \end{pmatrix}$.

$R_z\begin{pmatrix}5\sqrt6/4\\5\sqrt6/4\\5/2\end{pmatrix} = \begin{pmatrix} \frac{\sqrt3}{2}\cdot\frac{5\sqrt6}{4} - \frac12\cdot\frac{5\sqrt6}{4} \\ \frac12\cdot\frac{5\sqrt6}{4} + \frac{\sqrt3}{2}\cdot\frac{5\sqrt6}{4} \\ 5/2 \end{pmatrix}$
$= \begin{pmatrix} \frac{5\sqrt6}{8}(\sqrt3 - 1) \\ \frac{5\sqrt6}{8}(1 + \sqrt3) \\ 5/2 \end{pmatrix}$.

The $z$-coordinate is unchanged (rotation around $z$-axis).

> **Answer**: $\left(\frac{5\sqrt6}{8}(\sqrt3-1),\; \frac{5\sqrt6}{8}(1+\sqrt3),\; \frac52\right)$

---

### A12. (🔗 9B) The parabola $y = x^2$ is sheared by $H_x(2)$ (shear factor 2). Find the equation of the resulting curve. Is it still a parabola?

$H_x(2) = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$. This maps $(x,y) \to (x+2y, y)$.

A point on the original parabola: $(t, t^2)$.
After shear: $(t + 2t^2, t^2)$.

So $x = t + 2t^2$, $y = t^2$.
Eliminate $t$: $t = \pm\sqrt{y}$.
$x = \pm\sqrt{y} + 2y$.

Taking the positive branch: $x - 2y = \sqrt{y} \implies (x-2y)^2 = y \implies x^2 - 4xy + 4y^2 - y = 0$.

The discriminant $B^2 - 4AC = (-4)^2 - 4(1)(4) = 16 - 16 = 0$.
Since $B^2 - 4AC = 0$, it is still a parabola. Shear preserves the conic type (it's an affine transformation).

> **Answer**: $x^2 - 4xy + 4y^2 - y = 0$; yes, still a parabola ($B^2-4AC = 0$)
