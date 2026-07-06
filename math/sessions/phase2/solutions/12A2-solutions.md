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

---

[Back to Table of Contents](../12A2-matrices-vectors.md)
