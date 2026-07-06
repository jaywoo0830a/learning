# Solutions: Session 12C2 — Parametric Curves and Surfaces

---

## Practice 1

$\vec{r}(t) = (3, -1, 4) + t((7, 2, 10) - (3, -1, 4)) = (3, -1, 4) + t(4, 3, 6)$ for $t \in [0, 1]$.

So $\vec{r}(t) = (3 + 4t,\; -1 + 3t,\; 4 + 6t)$, $t \in [0, 1]$.

---

## Practice 2

$\vec{r}(t) = (5\cos t,\; 3\sin t)$, $t \in [0, 2\pi]$.

Check: $\frac{x^2}{25} + \frac{y^2}{9} = \frac{25\cos^2 t}{25} + \frac{9\sin^2 t}{9} = \cos^2 t + \sin^2 t = 1$. ✅

---

## Practice 3

$\vec{r}{\,}'(t) = (-2\sin t,\; 2\cos t,\; 3)$.
Speed = $\sqrt{(-2\sin t)^2 + (2\cos t)^2 + 3^2} = \sqrt{4\sin^2 t + 4\cos^2 t + 9} = \sqrt{4 + 9} = \sqrt{13}$.

Arc length = $\int_0^{4\pi} \sqrt{13} \, dt = 4\pi\sqrt{13}$.

---

## Practice 4

Cubic Bézier: $\vec{r}(t) = (1-t)^3\vec{P}_0 + 3(1-t)^2 t\vec{P}_1 + 3(1-t)t^2\vec{P}_2 + t^3\vec{P}_3$.

At $t = 0.5$: $(1-t)^3 = 0.125$, $3(1-t)^2 t = 0.375$, $3(1-t)t^2 = 0.375$, $t^3 = 0.125$.

$\vec{r}(0.5) = 0.125(0,0) + 0.375(1,3) + 0.375(4,3) + 0.125(5,0)$.
$= (0.375 \times 1 + 0.375 \times 4 + 0.125 \times 5,\; 0.375 \times 3 + 0.375 \times 3 + 0.125 \times 0)$.
$= (0.375 + 1.5 + 0.625,\; 1.125 + 1.125 + 0)$.
$= (2.5,\; 2.25)$.

---

## Practice 5

$\vec{r}_\theta = \frac{\partial}{\partial\theta}(R\sin\phi\cos\theta,\; R\sin\phi\sin\theta,\; R\cos\phi) = (-R\sin\phi\sin\theta,\; R\sin\phi\cos\theta,\; 0)$.

$\vec{r}_\phi = \frac{\partial}{\partial\phi}(R\sin\phi\cos\theta,\; R\sin\phi\sin\theta,\; R\cos\phi) = (R\cos\phi\cos\theta,\; R\cos\phi\sin\theta,\; -R\sin\phi)$.

Normal $\vec{n} = \vec{r}_\theta \times \vec{r}_\phi$.

Compute cross product:
$\vec{r}_\theta \times \vec{r}_\phi = \det\begin{pmatrix}\hat{i}&\hat{j}&\hat{k}\\-R\sin\phi\sin\theta&R\sin\phi\cos\theta&0\\R\cos\phi\cos\theta&R\cos\phi\sin\theta&-R\sin\phi\end{pmatrix}$.

$= \hat{i}(R\sin\phi\cos\theta \cdot (-R\sin\phi) - 0) - \hat{j}(-R\sin\phi\sin\theta \cdot (-R\sin\phi) - 0) + \hat{k}(-R\sin\phi\sin\theta \cdot R\cos\phi\sin\theta - R\sin\phi\cos\theta \cdot R\cos\phi\cos\theta)$.

Simplify: $= \hat{i}(-R^2\sin^2\phi\cos\theta) - \hat{j}(-R^2\sin^2\phi\sin\theta) + \hat{k}(-R^2\sin\phi\cos\phi(\sin^2\theta + \cos^2\theta))$.

$= (-R^2\sin^2\phi\cos\theta,\; R^2\sin^2\phi\sin\theta,\; -R^2\sin\phi\cos\phi)$.

At $\theta = \pi/4$, $\phi = \pi/3$: $\sin\phi = \frac{\sqrt{3}}{2}$, $\cos\phi = \frac{1}{2}$.
$\sin^2\phi = \frac{3}{4}$, $\cos\theta = \sin\theta = \frac{\sqrt{2}}{2}$.

$\vec{n} = (-R^2 \cdot \frac{3}{4} \cdot \frac{\sqrt{2}}{2},\; R^2 \cdot \frac{3}{4} \cdot \frac{\sqrt{2}}{2},\; -R^2 \cdot \frac{\sqrt{3}}{2} \cdot \frac{1}{2})$
$= (-\frac{3R^2\sqrt{2}}{8},\; \frac{3R^2\sqrt{2}}{8},\; -\frac{R^2\sqrt{3}}{4})$.

The position vector at this point: $\vec{r} = (R\sin\phi\cos\theta,\; R\sin\phi\sin\theta,\; R\cos\phi) = (R\cdot\frac{\sqrt{3}}{2}\cdot\frac{\sqrt{2}}{2},\; R\cdot\frac{\sqrt{3}}{2}\cdot\frac{\sqrt{2}}{2},\; R\cdot\frac{1}{2}) = (\frac{R\sqrt{6}}{4},\; \frac{R\sqrt{6}}{4},\; \frac{R}{2})$.

$\vec{n}$ is a scalar multiple of $\vec{r}$ (both are outward radial), confirming the normal points radially outward.

---

## Practice 6

Conical spiral: $\vec{r}(t) = (t\cos t,\; t\sin t,\; t)$.

$\vec{r}{\,}'(t) = (\cos t - t\sin t,\; \sin t + t\cos t,\; 1)$.

Speed squared: $|\vec{r}{\,}'|^2 = (\cos t - t\sin t)^2 + (\sin t + t\cos t)^2 + 1$.
$= (\cos^2 t - 2t\cos t\sin t + t^2\sin^2 t) + (\sin^2 t + 2t\sin t\cos t + t^2\cos^2 t) + 1$.
$= \cos^2 t + \sin^2 t + t^2(\sin^2 t + \cos^2 t) + 1$.
$= 1 + t^2 + 1 = t^2 + 2$.

Speed = $\sqrt{t^2 + 2}$.

Arc length = $\int_0^{4\pi} \sqrt{t^2 + 2} \, dt$.

Use substitution $t = \sqrt{2}\sinh u$, $dt = \sqrt{2}\cosh u\,du$, $\sqrt{t^2+2} = \sqrt{2}\cosh u$:
$L = \int_0^{\sinh^{-1}(4\pi/\sqrt{2})} 2\cosh^2 u \, du = \int (1 + \cosh 2u) \, du = u + \frac{1}{2}\sinh 2u \Big|$.

Alternative closed form: $L = \frac{1}{2}\left[t\sqrt{t^2+2} + 2\ln|t + \sqrt{t^2+2}|\right]_0^{4\pi}$.
$= \frac{1}{2}\left[4\pi\sqrt{16\pi^2+2} + 2\ln(4\pi + \sqrt{16\pi^2+2}) - 0 - 2\ln(\sqrt{2})\right]$.
$= 2\pi\sqrt{16\pi^2+2} + \ln\left(\frac{4\pi + \sqrt{16\pi^2+2}}{\sqrt{2}}\right)$.

---

## Basic Drill

**D1.** $\vec{r}(t) = (1, 2) + t(3, 4) = (1 + 3t,\; 2 + 4t)$, $t \in [0, 1]$.

**D2.** $\vec{r}(t) = (2 + 4\cos t,\; -3 + 4\sin t)$, $t \in [0, 2\pi]$.

**D3.** $\vec{r}{\,}'(t) = (3, 4)$. Speed = $\sqrt{9 + 16} = 5$.
Arc length = $\int_0^5 5\,dt = 25$.

**D4.** $\vec{r}(t) = (1-t)^2(0,0) + 2(1-t)t(2,4) + t^2(6,0) = (4t(1-t) + 6t^2,\; 8t(1-t))$ $= (4t - 4t^2 + 6t^2,\; 8t - 8t^2) = (4t + 2t^2,\; 8t - 8t^2)$.

**D5.** $\vec{r}_\theta = \frac{\partial}{\partial\theta}(3\cos\theta,\; 3\sin\theta,\; z) = (-3\sin\theta,\; 3\cos\theta,\; 0)$.
$\vec{r}_z = \frac{\partial}{\partial z}(3\cos\theta,\; 3\sin\theta,\; z) = (0, 0, 1)$.

**D6.** $\vec{r}{\,}'(t) = (e^t\cos t - e^t\sin t,\; e^t\sin t + e^t\cos t) = e^t(\cos t - \sin t,\; \sin t + \cos t)$.
At $t = 0$: $\vec{r}{\,}'(0) = (1, 1)$. Speed = $\sqrt{1 + 1} = \sqrt{2}$.

**D7.** $\vec{r}(t) = (1 + 6\cos t,\; -2 + 4\sin t)$, $t \in [0, 2\pi]$.

**D8.** $\vec{r}{\,}'(t) = (2t,\; 3t^2)$. At $t = 2$: $\vec{r}{\,}'(2) = (4, 12)$. Speed = $\sqrt{16 + 144} = \sqrt{160} = 4\sqrt{10}$.

**D9.** $\vec{r}(t) = (3, 1, 8) + t((7, 5, 2) - (3, 1, 8)) = (3, 1, 8) + t(4, 4, -6) = (3+4t,\; 1+4t,\; 8-6t)$, $t \in [0, 1]$.

**D10.** $\vec{r}(t) = (5\cos t,\; 5\sin t,\; 0)$. This is a circle in the $xy$-plane with radius 5, centered at origin. Speed = $\sqrt{(-5\sin t)^2 + (5\cos t)^2 + 0} = 5$.

---

## Advanced Drill

**A1.** $\vec{r}{\,}'(t) = (1, 2t)$. Speed = $\sqrt{1 + 4t^2}$.
$L = \int_0^1 \sqrt{1 + 4t^2} \, dt$.

Substitute $2t = \tan u$, $2\,dt = \sec^2 u\,du$, $1 + 4t^2 = 1 + \tan^2 u = \sec^2 u$.
$L = \int_0^{\tan^{-1}(2)} \sec u \cdot \frac{1}{2}\sec^2 u \, du = \frac{1}{2}\int_0^{\tan^{-1}(2)} \sec^3 u \, du$.

(Leave in this closed-form — the integral of $\sec^3 u$ is known: $\frac{1}{2}(\sec u\tan u + \ln|\sec u + \tan u|)$.)

**A2.** $x = r\cos\theta = (1+\cos\theta)\cos\theta$, $y = r\sin\theta = (1+\cos\theta)\sin\theta$.

Arc length in polar: $L = \int_0^{2\pi} \sqrt{r^2 + (r')^2} \, d\theta$.
$r = 1 + \cos\theta$, $r' = -\sin\theta$.
$r^2 + (r')^2 = (1 + \cos\theta)^2 + \sin^2\theta = 1 + 2\cos\theta + \cos^2\theta + \sin^2\theta = 2 + 2\cos\theta = 4\cos^2(\theta/2)$.

$\sqrt{r^2 + (r')^2} = 2|\cos(\theta/2)|$. For $\theta \in [0, 2\pi]$, $\theta/2 \in [0, \pi]$, so $\cos(\theta/2) \ge 0$ for $\theta \in [0, \pi]$ and negative for $\theta \in [\pi, 2\pi]$.

$L = \int_0^{2\pi} 2|\cos(\theta/2)| \, d\theta = 4\int_0^{\pi} \cos(\theta/2)\, d\theta = 4[2\sin(\theta/2)]_0^{\pi} = 4(2 - 0) = 8$.

**A3.** Torus: $\vec{r}(\theta, \phi) = ((R + r\cos\phi)\cos\theta,\; (R + r\cos\phi)\sin\theta,\; r\sin\phi)$.

$\vec{r}_\theta = (-(R+r\cos\phi)\sin\theta,\; (R+r\cos\phi)\cos\theta,\; 0)$.
$\vec{r}_\phi = (-r\sin\phi\cos\theta,\; -r\sin\phi\sin\theta,\; r\cos\phi)$.

$|\vec{r}_\theta \times \vec{r}_\phi| = r(R + r\cos\phi)$ (standard result — verified in calculus texts).

Area = $\int_0^{2\pi}\int_0^{2\pi} r(R + r\cos\phi)\,d\theta\,d\phi = 2\pi r\int_0^{2\pi}(R + r\cos\phi)\,d\phi = 2\pi r[2\pi R + 0] = 4\pi^2 r R$.

For $R = 4$, $r = 1$: Area = $4\pi^2 \cdot 4 = 16\pi^2$.

**A4.** From Practice 4: $\vec{r}(t) = ((1-t)^3\cdot0 + 3(1-t)^2 t\cdot1 + 3(1-t)t^2\cdot4 + t^3\cdot5,\; (1-t)^3\cdot0 + 3(1-t)^2 t\cdot3 + 3(1-t)t^2\cdot3 + t^3\cdot0)$.

Simplify $x(t)$: $x = 3(1-t)^2 t + 12(1-t)t^2 + 5t^3 = 3t(1-2t+t^2) + 12(t^2 - t^3) + 5t^3 = 3t - 6t^2 + 3t^3 + 12t^2 - 12t^3 + 5t^3 = 3t + 6t^2 - 4t^3$.

$y(t) = 9(1-t)^2 t + 9(1-t)t^2 = 9t(1-2t+t^2) + 9(t^2 - t^3) = 9t - 18t^2 + 9t^3 + 9t^2 - 9t^3 = 9t - 9t^2$.

Horizontal tangent: $y'(t) = 0$. $y'(t) = 9 - 18t = 0 \implies t = 0.5$.

At $t = 0.5$: point from Practice 4 is $(2.5, 2.25)$.

**A5.** The great circle is the intersection of sphere $x^2+y^2+z^2=1$ and plane $x+y+z=0$. The plane passes through the origin, so the intersection is a circle of radius 1 centered at the origin, lying in the plane.

Find two orthogonal unit vectors in the plane. Normal to plane: $\vec{n} = (1, 1, 1)/\sqrt{3}$.
One vector in the plane: $\vec{u} = (1, -1, 0)/\sqrt{2}$ (perpendicular to $\vec{n}$).
Another: $\vec{v} = \vec{n} \times \vec{u} = \frac{(1,1,1)}{\sqrt{3}} \times \frac{(1,-1,0)}{\sqrt{2}} = \frac{(1\cdot0 - 1\cdot(-1),\; 1\cdot1 - 1\cdot0,\; 1\cdot(-1) - 1\cdot1)}{\sqrt{6}} = \frac{(1, 1, -2)}{\sqrt{6}}$.

Check: $\vec{v} \cdot \vec{n} = \frac{1+1-2}{\sqrt{18}} = 0$, $\vec{v} \cdot \vec{u} = \frac{1-1+0}{\sqrt{12}} = 0$. ✅

Parametrization: $\vec{r}(t) = \cos t\,\vec{u} + \sin t\,\vec{v}$, $t \in [0, 2\pi]$.
$= \cos t\left(\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}, 0\right) + \sin t\left(\frac{1}{\sqrt{6}}, \frac{1}{\sqrt{6}}, -\frac{2}{\sqrt{6}}\right)$.

**A6.** Spherical parametrization: $\vec{r}(\theta, \phi) = (R\sin\phi\cos\theta,\; R\sin\phi\sin\theta,\; R\cos\phi)$.

$\vec{r}_\theta = (-R\sin\phi\sin\theta,\; R\sin\phi\cos\theta,\; 0)$.
$\vec{r}_\phi = (R\cos\phi\cos\theta,\; R\cos\phi\sin\theta,\; -R\sin\phi)$.

$|\vec{r}_\theta \times \vec{r}_\phi| = R^2\sin\phi$ (standard computation, see Practice 5 for the cross product pattern; the magnitude simplifies nicely).

Surface area = $\int_0^{2\pi}\int_0^{\pi} R^2\sin\phi \, d\phi \, d\theta = R^2 \cdot 2\pi \cdot \int_0^{\pi}\sin\phi\,d\phi = R^2 \cdot 2\pi \cdot [-\cos\phi]_0^{\pi} = R^2 \cdot 2\pi \cdot (1 - (-1)) = 4\pi R^2$.

**A7.** Cycloid: $\vec{r}(t) = (t - \sin t,\; 1 - \cos t)$.
$\vec{r}{\,}'(t) = (1 - \cos t,\; \sin t)$.
$|\vec{r}{\,}'|^2 = (1 - \cos t)^2 + \sin^2 t = 1 - 2\cos t + \cos^2 t + \sin^2 t = 2 - 2\cos t = 4\sin^2(t/2)$.
Speed = $2|\sin(t/2)|$. For $t \in [0, 2\pi]$, $\sin(t/2) \ge 0$, so speed = $2\sin(t/2)$.
$L = \int_0^{2\pi} 2\sin(t/2)\,dt = 2[-2\cos(t/2)]_0^{2\pi} = 2(-2\cos\pi + 2\cos 0) = 2(2 + 2) = 8$.

**A8.** $\vec{r}(u, v) = (u\cos v,\; u\sin v,\; u^2)$.
$\vec{r}_u = (\cos v,\; \sin v,\; 2u)$.
$\vec{r}_v = (-u\sin v,\; u\cos v,\; 0)$.
$\vec{r}_u \times \vec{r}_v = \det\begin{pmatrix}\hat{i}&\hat{j}&\hat{k}\\\cos v&\sin v&2u\\-u\sin v&u\cos v&0\end{pmatrix} = \hat{i}(-2u^2\cos v) - \hat{j}(2u^2\sin v) + \hat{k}(u\cos^2 v + u\sin^2 v)$.
$= (-2u^2\cos v,\; -2u^2\sin v,\; u)$.
$|\vec{r}_u \times \vec{r}_v| = \sqrt{4u^4\cos^2 v + 4u^4\sin^2 v + u^2} = \sqrt{4u^4 + u^2} = u\sqrt{4u^2 + 1}$.

**A9.** $\vec{r}(t) = (R\cos t,\; R\sin t,\; ct)$.
$\vec{r}{\,}' = (-R\sin t,\; R\cos t,\; c)$.
$\vec{r}{\,}'' = (-R\cos t,\; -R\sin t,\; 0)$.
$\vec{r}{\,}' \times \vec{r}{\,}'' = \det\begin{pmatrix}\hat{i}&\hat{j}&\hat{k}\\-R\sin t&R\cos t&c\\-R\cos t&-R\sin t&0\end{pmatrix} = \hat{i}(Rc\sin t) - \hat{j}(-Rc\cos t) + \hat{k}(R^2\sin^2 t + R^2\cos^2 t) = (Rc\sin t,\; Rc\cos t,\; R^2)$.
$|\vec{r}{\,}' \times \vec{r}{\,}''| = \sqrt{R^2c^2\sin^2 t + R^2c^2\cos^2 t + R^4} = \sqrt{R^2c^2 + R^4} = R\sqrt{c^2 + R^2}$.
$|\vec{r}{\,}'| = \sqrt{R^2 + c^2}$.
$\kappa = \frac{R\sqrt{c^2+R^2}}{(R^2+c^2)^{3/2}} = \frac{R}{R^2 + c^2}$ (constant for a helix).

**A10.** $\vec{r}_1(t) = (1+t,\; 2,\; 3-t)$. $\vec{r}_2(s) = (4+2s,\; 1+s,\; 2+s)$.
Set equal: $1+t = 4+2s$, $2 = 1+s$, $3-t = 2+s$.
From the second: $s = 1$.
First: $1+t = 4+2 \implies t = 5$.
Third: $3-5 = 2+1 \implies -2 = 3$, contradiction.
The lines do not intersect — they are skew.


