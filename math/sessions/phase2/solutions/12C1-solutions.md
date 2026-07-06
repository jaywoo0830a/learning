# Solutions: Session 12C1 — Geometric Transformations

---

## Practice 1

Scale then rotate. Scale: $S = \begin{pmatrix}2&0\\0&3\end{pmatrix}$. Rotate: $R_{45} = \begin{pmatrix}\frac{\sqrt{2}}{2}&-\frac{\sqrt{2}}{2}\\\frac{\sqrt{2}}{2}&\frac{\sqrt{2}}{2}\end{pmatrix}$.

Apply rotate first (rightmost) then scale: $S \cdot R_{45}$? No — the question says "first scales, then rotates." Apply scale first (rightmost), then rotate: $R_{45} \cdot S$.

$R_{45} \cdot S = \begin{pmatrix}\frac{\sqrt{2}}{2}&-\frac{\sqrt{2}}{2}\\\frac{\sqrt{2}}{2}&\frac{\sqrt{2}}{2}\end{pmatrix}\begin{pmatrix}2&0\\0&3\end{pmatrix} = \begin{pmatrix}\frac{\sqrt{2}}{2}\cdot 2 & -\frac{\sqrt{2}}{2}\cdot 3 \\ \frac{\sqrt{2}}{2}\cdot 2 & \frac{\sqrt{2}}{2}\cdot 3\end{pmatrix} = \begin{pmatrix}\sqrt{2} & -\frac{3\sqrt{2}}{2} \\ \sqrt{2} & \frac{3\sqrt{2}}{2}\end{pmatrix}$.

---

## Practice 2

(1) Translate $(-1, -2)$ to move $(1,2)$ to origin: $T_1 = \begin{pmatrix}1&0&-1\\0&1&-2\\0&0&1\end{pmatrix}$.

(2) Rotate by $90^\circ$ CCW: $R_{90} = \begin{pmatrix}0&-1&0\\1&0&0\\0&0&1\end{pmatrix}$.

(3) Translate back by $(1, 2)$: $T_2 = \begin{pmatrix}1&0&1\\0&1&2\\0&0&1\end{pmatrix}$.

Combined: $T_2 \cdot R_{90} \cdot T_1 = \begin{pmatrix}1&0&1\\0&1&2\\0&0&1\end{pmatrix}\begin{pmatrix}0&-1&0\\1&0&0\\0&0&1\end{pmatrix}\begin{pmatrix}1&0&-1\\0&1&-2\\0&0&1\end{pmatrix}$.

Multiply $R_{90} \cdot T_1$ first: $\begin{pmatrix}0&-1&0\\1&0&0\\0&0&1\end{pmatrix}\begin{pmatrix}1&0&-1\\0&1&-2\\0&0&1\end{pmatrix} = \begin{pmatrix}0&-1&2\\1&0&-1\\0&0&1\end{pmatrix}$.

Then $T_2$ times that: $\begin{pmatrix}1&0&1\\0&1&2\\0&0&1\end{pmatrix}\begin{pmatrix}0&-1&2\\1&0&-1\\0&0&1\end{pmatrix} = \begin{pmatrix}0&-1&3\\1&0&1\\0&0&1\end{pmatrix}$.

Final matrix: $\begin{pmatrix}0&-1&3\\1&0&1\\0&0&1\end{pmatrix}$.

---

## Practice 3

$A = \begin{pmatrix}4&1\\2&3\end{pmatrix}$.

Characteristic polynomial: $\det(A - \lambda I) = \det\begin{pmatrix}4-\lambda&1\\2&3-\lambda\end{pmatrix} = (4-\lambda)(3-\lambda) - 2 = \lambda^2 - 7\lambda + 10 = 0$.

Roots: $\lambda = \frac{7 \pm \sqrt{49-40}}{2} = \frac{7 \pm 3}{2}$. So $\lambda_1 = 5$, $\lambda_2 = 2$.

For $\lambda_1 = 5$: $(A - 5I)\vec{v} = \begin{pmatrix}-1&1\\2&-2\end{pmatrix}\vec{v} = 0$. So $v_1 = v_2$. Eigenvector: $(1, 1)$ (normalized or not).

For $\lambda_2 = 2$: $(A - 2I)\vec{v} = \begin{pmatrix}2&1\\2&1\end{pmatrix}\vec{v} = 0$. So $2v_1 + v_2 = 0 \implies v_2 = -2v_1$. Eigenvector: $(1, -2)$.

---

## Practice 4

A pure 2D rotation $R_\theta = \begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}$ has characteristic polynomial $\lambda^2 - 2\cos\theta\lambda + 1 = 0$. Roots: $\lambda = \cos\theta \pm i\sin\theta = e^{\pm i\theta}$.

Real eigenvectors exist only when the eigenvalues are real, i.e., $\sin\theta = 0$. So $\theta = 0^\circ$ (identity, every vector is an eigenvector with $\lambda=1$) or $\theta = 180^\circ$ ($\lambda = -1$). For $180^\circ$, the rotation matrix is $\begin{pmatrix}-1&0\\0&-1\end{pmatrix}$ — every vector is an eigenvector with $\lambda = -1$ (every direction flips).

Geometric meaning: a nontrivial rotation changes every direction, so no real invariant direction exists.

---

## Practice 5

$|\det(A)| = \sigma_1 \sigma_2 = 5 \times 2 = 10$. Or more precisely, the absolute value of the determinant equals the product of singular values.

The unit circle maps to an ellipse with semi-axes $\sigma_1 = 5$ and $\sigma_2 = 2$. Area of ellipse = $\pi \sigma_1 \sigma_2 = 10\pi = |\det(A)| \cdot \pi$, consistent with the determinant being the area scaling factor.

---

## Practice 6

**Step 1**: Reflection across line $y = 2x$. The line has angle $\alpha = \tan^{-1}(2)$. Using $\cos 2\alpha$ and $\sin 2\alpha$ formulas:
$\tan\alpha = 2$, so $\sin\alpha = \frac{2}{\sqrt{5}}$, $\cos\alpha = \frac{1}{\sqrt{5}}$.
$\cos 2\alpha = \cos^2\alpha - \sin^2\alpha = \frac{1}{5} - \frac{4}{5} = -\frac{3}{5}$.
$\sin 2\alpha = 2\sin\alpha\cos\alpha = 2 \cdot \frac{2}{\sqrt{5}} \cdot \frac{1}{\sqrt{5}} = \frac{4}{5}$.

Reflection matrix $F$ in homogeneous $3\times3$: $\begin{pmatrix}-3/5&4/5&0\\4/5&3/5&0\\0&0&1\end{pmatrix}$.

**Step 2**: Translation by $(3, -1)$: $T = \begin{pmatrix}1&0&3\\0&1&-1\\0&0&1\end{pmatrix}$.

**Step 3**: Combined: $T \cdot F = \begin{pmatrix}1&0&3\\0&1&-1\\0&0&1\end{pmatrix}\begin{pmatrix}-3/5&4/5&0\\4/5&3/5&0\\0&0&1\end{pmatrix} = \begin{pmatrix}-3/5&4/5&3\\4/5&3/5&-1\\0&0&1\end{pmatrix}$.

**Step 4**: Apply to $(1, 1, 1)$: $\begin{pmatrix}-3/5&4/5&3\\4/5&3/5&-1\\0&0&1\end{pmatrix}\begin{pmatrix}1\\1\\1\end{pmatrix} = \begin{pmatrix}-3/5+4/5+3\\4/5+3/5-1\\1\end{pmatrix} = \begin{pmatrix}1/5+3\\7/5-1\\1\end{pmatrix} = \begin{pmatrix}16/5\\2/5\\1\end{pmatrix}$.

The point maps to $(16/5,\; 2/5)$.

---

## Basic Drill

**D1.** $R_{30}\begin{pmatrix}2\\0\end{pmatrix} = \begin{pmatrix}\frac{\sqrt{3}}{2}&-\frac{1}{2}\\\frac{1}{2}&\frac{\sqrt{3}}{2}\end{pmatrix}\begin{pmatrix}2\\0\end{pmatrix} = \begin{pmatrix}\sqrt{3}\\1\end{pmatrix} = (\sqrt{3},\; 1)$.

**D2.** $S = \begin{pmatrix}4&0\\0&\frac{1}{2}\end{pmatrix}$.

**D3.** $T = \begin{pmatrix}1&0&5\\0&1&-3\\0&0&1\end{pmatrix}$.

**D4.** $R_{60} \cdot R_{30} = R_{90}$ (rotations are additive: $60^\circ + 30^\circ = 90^\circ$). The product is $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$.

**D5.** $\det\begin{pmatrix}1&3\\0&1\end{pmatrix} = 1$. A shear preserves area — it tilts shapes but doesn't change their area. The determinant being 1 confirms this.

**D6.** $F_{45^\circ}$: $\alpha=45^\circ$, so $2\alpha=90^\circ$. $\cos 90^\circ = 0$, $\sin 90^\circ = 1$.
$F_{45} = \begin{pmatrix}0&1\\1&0\end{pmatrix}$.
Apply to $(1, 0)$: $\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}1\\0\end{pmatrix} = \begin{pmatrix}0\\1\end{pmatrix}$.
Geometrically: reflecting $(1,0)$ across the line $y = x$ gives $(0, 1)$.

**D7.** Reflect across $x$-axis: $F_0 = \begin{pmatrix}1&0\\0&-1\end{pmatrix}$. Rotate $90^\circ$ CCW: $R_{90} = \begin{pmatrix}0&-1\\1&0\end{pmatrix}$.
Apply rotate first (rightmost), then reflect: $F_0 \cdot R_{90} = \begin{pmatrix}1&0\\0&-1\end{pmatrix}\begin{pmatrix}0&-1\\1&0\end{pmatrix} = \begin{pmatrix}0&-1\\-1&0\end{pmatrix}$.
This is reflection across the line $y = -x$. (Check: $(x,y) \to (-y, -x)$, which is reflection across $y=-x$.)

**D8.** Translate $(-1,-1)$ to origin, scale by 2, translate back:
$T_2 \cdot S_2 \cdot T_1 = \begin{pmatrix}1&0&1\\0&1&1\\0&0&1\end{pmatrix}\begin{pmatrix}2&0&0\\0&2&0\\0&0&1\end{pmatrix}\begin{pmatrix}1&0&-1\\0&1&-1\\0&0&1\end{pmatrix} = \begin{pmatrix}2&0&-1\\0&2&-1\\0&0&1\end{pmatrix}$.

**D9.** $F_0 = \begin{pmatrix}1&0\\0&-1\end{pmatrix}$, $F_{45} = \begin{pmatrix}0&1\\1&0\end{pmatrix}$.
$F_0 \cdot F_{45} = \begin{pmatrix}1&0\\0&-1\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix} = \begin{pmatrix}0&1\\-1&0\end{pmatrix}$.
This is $R_{-90^\circ}$ (clockwise rotation by $90^\circ$), since $\begin{pmatrix}0&1\\-1&0\end{pmatrix} = \begin{pmatrix}\cos(-90^\circ)&-\sin(-90^\circ)\\\sin(-90^\circ)&\cos(-90^\circ)\end{pmatrix}$.

**D10.** The original square has area $2 \times 2 = 4$.
$A = \begin{pmatrix}0&2\\-3&0\end{pmatrix}$, $\det(A) = 0 \cdot 0 - 2 \cdot (-3) = 6$.
Area of resulting shape = $4 \times |6| = 24$.

---

## Advanced Drill

**A1.** $\det(F_\alpha - \lambda I) = \det\begin{pmatrix}\cos 2\alpha - \lambda&\sin 2\alpha\\\sin 2\alpha&-\cos 2\alpha - \lambda\end{pmatrix} = (\cos 2\alpha - \lambda)(-\cos 2\alpha - \lambda) - \sin^2 2\alpha$.

$= \lambda^2 - \cos^2 2\alpha - \sin^2 2\alpha = \lambda^2 - 1 = 0$.

Eigenvalues: $\lambda = \pm 1$. Eigenvalue +1 = vectors along the mirror line (fixed). Eigenvalue -1 = vectors perpendicular to the mirror line (flipped). This is exactly what a reflection does geometrically.

**A2.** $R_z(90^\circ)$ in $4 \times 4$ homogeneous: $\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}$.
Translation: $\begin{pmatrix}1&0&0&1\\0&1&0&2\\0&0&1&3\\0&0&0&1\end{pmatrix}$.
Combined: $\begin{pmatrix}1&0&0&1\\0&1&0&2\\0&0&1&3\\0&0&0&1\end{pmatrix}\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix} = \begin{pmatrix}0&-1&0&1\\1&0&0&2\\0&0&1&3\\0&0&0&1\end{pmatrix}$.

**A3.** $A = \begin{pmatrix}3&1\\1&3\end{pmatrix}$. $A^T A = A^2 = \begin{pmatrix}10&6\\6&10\end{pmatrix}$.
Characteristic polynomial: $\lambda^2 - 20\lambda + 64 = 0$. Roots: $\lambda = 16, 4$.
Singular values: $\sigma_1 = 4$, $\sigma_2 = 2$.

**A4.** $F_\alpha = \begin{pmatrix}\cos 2\alpha&\sin 2\alpha\\\sin 2\alpha&-\cos 2\alpha\end{pmatrix}$, $F_\beta = \begin{pmatrix}\cos 2\beta&\sin 2\beta\\\sin 2\beta&-\cos 2\beta\end{pmatrix}$.
$F_\alpha F_\beta = \begin{pmatrix}\cos 2\alpha\cos 2\beta + \sin 2\alpha\sin 2\beta & \cos 2\alpha\sin 2\beta - \sin 2\alpha\cos 2\beta \\ \sin 2\alpha\cos 2\beta - \cos 2\alpha\sin 2\beta & \sin 2\alpha\sin 2\beta + \cos 2\alpha\cos 2\beta\end{pmatrix}$.

Using trig identities: $\cos 2\alpha\cos 2\beta + \sin 2\alpha\sin 2\beta = \cos(2\alpha - 2\beta)$.
$\cos 2\alpha\sin 2\beta - \sin 2\alpha\cos 2\beta = -\sin(2\alpha - 2\beta)$.
$\sin 2\alpha\cos 2\beta - \cos 2\alpha\sin 2\beta = \sin(2\alpha - 2\beta)$.
$\sin 2\alpha\sin 2\beta + \cos 2\alpha\cos 2\beta = \cos(2\alpha - 2\beta)$.

So $F_\alpha F_\beta = \begin{pmatrix}\cos(2\alpha-2\beta)&-\sin(2\alpha-2\beta)\\\sin(2\alpha-2\beta)&\cos(2\alpha-2\beta)\end{pmatrix}$, which is $R_{2(\alpha - \beta)}$, a rotation by $2(\alpha - \beta)$. QED.

**A5.** We want the $y$-axis $(0, 1)$ to map to a vector at $30^\circ$ from the $y$-axis. The $x$-axis stays fixed.

The $x$-axis $(1,0)$ maps to itself. The $y$-axis $(0,1)$ maps to a direction tilted $30^\circ$ from vertical, meaning it makes an angle of $60^\circ$ from the horizontal $x$-axis. So $(0, 1) \to (\cos 60^\circ, \sin 60^\circ) = (1/2, \sqrt{3}/2)$.

In matrix form: $A = \begin{pmatrix}1 & k \\ 0 & 1\end{pmatrix}$ is a horizontal shear, but we need the $y$-axis to tilt. Use a shear parallel to $x$: $A = \begin{pmatrix}1 & \cot 60^\circ \\ 0 & 1\end{pmatrix} = \begin{pmatrix}1 & 1/\sqrt{3} \\ 0 & 1\end{pmatrix}$.

Check: $A\begin{pmatrix}1\\0\end{pmatrix} = \begin{pmatrix}1\\0\end{pmatrix}$. ✅
$A\begin{pmatrix}0\\1\end{pmatrix} = \begin{pmatrix}1/\sqrt{3}\\1\end{pmatrix}$. The angle this makes with the $y$-axis: $\tan(\text{angle from y}) = \frac{1/\sqrt{3}}{1} = \frac{1}{\sqrt{3}}$, so angle $= 30^\circ$. ✅

Homogeneous $3\times3$: $\begin{pmatrix}1 & 1/\sqrt{3} & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{pmatrix}$.

**A6.** The square has area 4 (side length 2). After transformation by $A$, the area scales by $|\det(A)|$.
$\det(A) = 2 \times 1.5 - 1 \times 0.5 = 3 - 0.5 = 2.5$.
Area of parallelogram = $4 \times 2.5 = 10$.

**A7.** $R_\theta = \begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}$.
Characteristic polynomial: $\lambda^2 - 2\cos\theta\lambda + 1 = 0$.
Roots: $\lambda = \cos\theta \pm i\sin\theta = e^{\pm i\theta}$.
Real eigenvalues only when $\sin\theta = 0$, i.e., $\theta = 0^\circ$ (all vectors eigenvectors, $\lambda=1$) or $\theta = 180^\circ$ (all vectors eigenvectors, $\lambda=-1$). For any other angle, eigenvalues are complex, so no real eigenvectors exist.

**A8.** With singular values $\sigma_1 = 3$, $\sigma_2 = 0$, the rank is 1 (one nonzero singular value). Geometrically, $A$ collapses the plane onto a 1D line: it first rotates, then squashes one dimension to zero (projection onto a line), then rotates. The image of the unit circle is a line segment of length $2\sigma_1 = 6$.

**A9.** Step 1: Translate by $(0, -b)$ to move the $y$-intercept to the origin.
Step 2: Reflect across line $y = mx$. The line has angle $\alpha = \tan^{-1}(m)$.
The 2D reflection matrix $F_\alpha = \begin{pmatrix}\cos 2\alpha&\sin 2\alpha\\\sin 2\alpha&-\cos 2\alpha\end{pmatrix}$.
In homogeneous: $\begin{pmatrix}\cos 2\alpha&\sin 2\alpha&0\\\sin 2\alpha&-\cos 2\alpha&0\\0&0&1\end{pmatrix}$.
Step 3: Translate back by $(0, b)$.
Combined: $T_{(0,b)} \cdot F_\alpha \cdot T_{(0,-b)} = \begin{pmatrix}\cos 2\alpha&\sin 2\alpha&b\sin 2\alpha\\\sin 2\alpha&-\cos 2\alpha&b(1+\cos 2\alpha)\\0&0&1\end{pmatrix}$.
Simplify $\cos 2\alpha = \frac{1-m^2}{1+m^2}$, $\sin 2\alpha = \frac{2m}{1+m^2}$.

**A10.** A matrix with determinant 1 preserves area (and orientation). The unit square maps to a parallelogram of area 1. Verify for $H_x(k) = \begin{pmatrix}1&k\\0&1\end{pmatrix}$: the unit square vertices $(0,0),(1,0),(1,1),(0,1)$ map to $(0,0),(1,0),(1+k,1),(k,1)$. The parallelogram has base 1 and height 1, area = 1. Indeed, shear is area-preserving.
