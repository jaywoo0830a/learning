# 12A2 Solutions — Matrices and Vectors

---

## Practice 1: Composition

> $A$ has $\det = 0$. Geometric meaning. Example.

A matrix with $\det(A) = 0$ collapses the plane onto a line or a point. Area after transformation = $|\det(A)| \times$ original area = 0. The matrix is singular (no inverse).

Example: $A = \begin{pmatrix} 2 & 4 \\ 1 & 2 \end{pmatrix}$. $\det(A) = 0$. This maps every point to the line $y = \frac{1}{2}x$. The unit square collapses to a line segment — area becomes 0. The transformation is not reversible.

---

## Practice 2

> Solve $\begin{cases} 3x - 2y = 7 \\ x + 4y = 5 \end{cases}$ via matrix inversion.

(1) $A = \begin{pmatrix} 3 & -2 \\ 1 & 4 \end{pmatrix}$, $\det(A) = 14$.

(2) $A^{-1} = \frac{1}{14}\begin{pmatrix} 4 & 2 \\ -1 & 3 \end{pmatrix}$.

(3) $\vec{x} = A^{-1}\vec{b} = \frac{1}{14}\begin{pmatrix} 38 \\ 8 \end{pmatrix} = \begin{pmatrix} 19/7 \\ 4/7 \end{pmatrix}$.
→ **$x = \frac{19}{7},\; y = \frac{4}{7}$.**

---

## Practice 3

> $\vec{a} = (2,-1,3)$, $\vec{b} = (1,4,-2)$. Dot, cross, perpendicular check.

Dot: $\vec{a}\cdot\vec{b} = 2-4-6 = -8$.

Cross: $\vec{a}\times\vec{b} = (2-12,\; 3+4,\; 8+1) = (-10, 7, 9)$.

Check: $(-10)(2) + 7(-1) + 9(3) = -20-7+27 = 0$ ✓. $(-10)(1) + 7(4) + 9(-2) = -10+28-18 = 0$ ✓.
→ **Dot = $-8$, Cross = $(-10, 7, 9)$.**

---

## Practice 4

> Triangle area with $A(0,0,0)$, $B(3,1,0)$, $C(1,4,0)$.

(1) $\vec{AB} = (3,1,0)$, $\vec{AC} = (1,4,0)$.
(2) $\vec{AB} \times \vec{AC} = (0, 0, 12-1) = (0,0,11)$.
(3) Area = $\frac{1}{2}|\vec{AB} \times \vec{AC}| = \frac{11}{2}$.
→ **Area = $\frac{11}{2}$.**

---

## Practice 5: Composition

> Reflection across $x$-axis: $R_x = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$.
> Rotation $90^\circ$ CCW: $R_{90} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$.

$R_x R_{90} = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$ — reflection across $y = -x$.
$R_{90} R_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ — reflection across $y = x$.
The order matters: two different reflections result.

---

## Practice 6

> Scalar and vector projection of $\vec{a} = (5,12)$ onto $\vec{b} = (3,4)$.

(1) $|\vec{b}| = 5$.
(2) Scalar: $\frac{15+48}{5} = \frac{63}{5}$.
(3) Vector: $\frac{63}{25}(3,4) = (\frac{189}{25}, \frac{252}{25})$.
→ **Scalar = $\frac{63}{5}$, Vector = $(\frac{189}{25}, \frac{252}{25})$.**

---

## Practice 7

> $A = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}$. Find $A^{-1}$.

(1) $\det(A) = 6-5 = 1$.
(2) $A^{-1} = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}$.
(3) $A A^{-1} = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}\begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ ✓.
→ **$A^{-1} = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}$.**

---

## Practice 8: Real Battle

> $M$ has columns $(2,0,0)$, $(0,3,0)$, $(0,0,5)$. Find $\det(M)$, volume.

(1) $\det(M) = 2 \cdot 3 \cdot 5 = 30$ (diagonal matrix).
(2) Volume of parallelepiped = $|\det(M)| = 30$.
(3) The unit cube (volume 1) is stretched to a rectangular box of dimensions $2 \times 3 \times 5$, volume 30.
→ **$\det(M) = 30$, Volume = 30. A $2 \times 3 \times 5$ rectangular box.**

---

## Basic Drill

### D1. $\begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} 4 & -1 \\ 2 & 1 \end{pmatrix}$
$\begin{pmatrix} 8+2 & -2+1 \\ 0+6 & 0+3 \end{pmatrix} = \begin{pmatrix} 10 & -1 \\ 6 & 3 \end{pmatrix}$.
→ **$\begin{pmatrix} 10 & -1 \\ 6 & 3 \end{pmatrix}$.**

### D2. $\det\begin{pmatrix} 3 & 5 \\ 2 & 4 \end{pmatrix}$
$3\cdot4 - 5\cdot2 = 12 - 10 = 2$. → **2.**

### D3. $|\vec{a}|$ for $\vec{a} = (6,-8)$
$\sqrt{36+64} = \sqrt{100} = 10$. → **10.**

### D4. $\vec{a}\cdot\vec{b}$ for $\vec{a} = (1,-2,3)$, $\vec{b} = (4,0,-1)$
$4 + 0 - 3 = 1$. → **1.**

### D5. $\begin{pmatrix} 1 & 3 \\ 2 & -1 \end{pmatrix} + \begin{pmatrix} 4 & 0 \\ -2 & 5 \end{pmatrix}$
$\begin{pmatrix} 1+4 & 3+0 \\ 2-2 & -1+5 \end{pmatrix} = \begin{pmatrix} 5 & 3 \\ 0 & 4 \end{pmatrix}$. → **$\begin{pmatrix} 5 & 3 \\ 0 & 4 \end{pmatrix}$.**

### D6. $5 \cdot (-2, 3, 1)$
$(5\cdot(-2),\; 5\cdot3,\; 5\cdot1) = (-10, 15, 5)$. → **$(-10, 15, 5)$.**

### D7. $(2, 1, 0) \times (0, 3, 1)$
$\begin{pmatrix} 1\cdot1 - 0\cdot3 \\ 0\cdot0 - 2\cdot1 \\ 2\cdot3 - 1\cdot0 \end{pmatrix} = (1, -2, 6)$. → **$(1, -2, 6)$.**

### D8. Unit vector in direction of $\vec{v} = (3, -4)$
$|\vec{v}| = \sqrt{9+16} = 5$. $\hat{v} = (\frac{3}{5}, -\frac{4}{5})$. → **$(\frac{3}{5}, -\frac{4}{5})$.**

### D9. $\det\begin{pmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix}$
Diagonal matrix: $\det = 1 \cdot 2 \cdot 3 = 6$. → **6.**

### D10. $\vec{u}\cdot\vec{v}$ for $\vec{u}=(2,-1)$, $\vec{v}=(-3,4)$. Perpendicular?
Dot = $2(-3) + (-1)(4) = -6-4 = -10 \neq 0$. → **$-10$, not perpendicular.**

---

## Advanced Drill

### A1. $A^{-1}$ for $A = \begin{pmatrix} 4 & 3 \\ 3 & 2 \end{pmatrix}$
(1) $\det(A) = 8-9 = -1$.
(2) $A^{-1} = \begin{pmatrix} -2 & 3 \\ 3 & -4 \end{pmatrix}$.
(3) $A A^{-1} = \begin{pmatrix} -8+9 & 12-12 \\ -6+6 & 9-8 \end{pmatrix} = I$ ✓.
→ **$A^{-1} = \begin{pmatrix} -2 & 3 \\ 3 & -4 \end{pmatrix}$.**

### A2. Cross product of $\vec{a} = (1,2,3)$, $\vec{b} = (4,5,6)$
$\vec{a}\times\vec{b} = (12-15,\; 12-6,\; 5-8) = (-3, 6, -3)$.
→ **$(-3, 6, -3)$.**

### A3. Rotation $60^\circ$ applied to $(1,0)$
$R = \begin{pmatrix} \frac{1}{2} & -\frac{\sqrt{3}}{2} \\ \frac{\sqrt{3}}{2} & \frac{1}{2} \end{pmatrix}$. $R(1,0) = (\frac{1}{2}, \frac{\sqrt{3}}{2})$.
→ **$(\frac{1}{2}, \frac{\sqrt{3}}{2})$.**

### A4. Solve $\begin{cases} 2x+y-z=3 \\ x-y+2z=1 \\ 3x+2y+z=7 \end{cases}$
From eq1: $z = 2x+y-3$. Substitute: $5x+y=7$, $5x+3y=10$. Solve: $y=\frac{3}{2}$, $x=\frac{11}{10}$, $z=\frac{7}{10}$.
→ **$x=\frac{11}{10},\; y=\frac{3}{2},\; z=\frac{7}{10}$.**

### A5. Angle between $\vec{a} = (1,1,0)$ and $\vec{b} = (0,1,1)$
$\vec{a}\cdot\vec{b} = 1$. $|\vec{a}| = \sqrt{2}$, $|\vec{b}| = \sqrt{2}$.
$\cos\theta = \frac{1}{2}$ → $\theta = 60^\circ$. → **$60^\circ$.**

### A6. Projection of $\vec{a} = (5,12)$ onto $\vec{b} = (3,4)$
$|\vec{b}| = 5$. Scalar: $\frac{15+48}{5} = \frac{63}{5}$. Vector: $\frac{63}{25}(3,4)$.
→ **Scalar = $\frac{63}{5}$, Vector = $(\frac{189}{25}, \frac{252}{25})$.**

### A7. $A^2$ for $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$
$A^2 = \begin{pmatrix} 1\cdot1+2\cdot3 & 1\cdot2+2\cdot4 \\ 3\cdot1+4\cdot3 & 3\cdot2+4\cdot4 \end{pmatrix} = \begin{pmatrix} 7 & 10 \\ 15 & 22 \end{pmatrix}$.
→ **$\begin{pmatrix} 7 & 10 \\ 15 & 22 \end{pmatrix}$.**

### A8. Triangle area: $(0,0,0)$, $(2,1,0)$, $(0,3,0)$
$\vec{v}_1 = (2,1,0)$, $\vec{v}_2 = (0,3,0)$. $\vec{v}_1\times\vec{v}_2 = (0,0,6)$. Area = $\frac{1}{2}\cdot6 = 3$.
→ **3.**

### A9. Find $2\times2$ matrix with $A^2=I$, $A \neq \pm I$.
$A = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ (reflection across $x$-axis). $A^2 = I$.
Any reflection matrix works: $A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ also satisfies $A^2 = I$.
→ **$\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ (or any reflection).**

### A10. Area from columns $(3,1)$ and $(1,3)$
Area = $|\det\begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}| = |9-1| = 8$.
→ **8.**

---

[Back to Table of Contents](../12A2-matrices-vectors.md)
