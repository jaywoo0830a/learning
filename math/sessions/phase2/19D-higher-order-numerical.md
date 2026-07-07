# Session 19D: Higher Order & Numerical Methods

**Phase 2 — Classical Techniques | 55 min**

*Prerequisites: 19B (first-order), 14C (higher derivatives), 12A1 (complex numbers)*

---

## Example 1: Second-Order Homogeneous — $ay''+by'+cy=0$

Assume $y=e^{rx}$. Characteristic equation: $ar^2+br+c=0$.

**Case 1 — Distinct real roots**: $y = c_1e^{r_1x} + c_2e^{r_2x}$.

$y''-5y'+6y=0$. $r^2-5r+6=0$. Roots $r=2,3$. $y=c_1e^{2x}+c_2e^{3x}$.

**Case 2 — Repeated root**: $y = (c_1+c_2x)e^{rx}$.

$y''-4y'+4y=0$. $r^2-4r+4=(r-2)^2=0$. $r=2$ (double). $y=(c_1+c_2x)e^{2x}$.

**Case 3 — Complex roots** $r=\alpha\pm i\beta$: $y = e^{\alpha x}(c_1\cos\beta x + c_2\sin\beta x)$.

$y''+4y'+13y=0$. $r^2+4r+13=0$. $r=-2\pm3i$. $y=e^{-2x}(c_1\cos3x+c_2\sin3x)$.

---

> **🔗 Bridge to Linear Algebra**: The characteristic equation $ar^2+br+c=0$ is secretly an eigenvalue problem. Rewrite $y''+ay'+by=0$ in state-space form (Session 19E):
>
> $$\dot{\vec{x}} = \begin{pmatrix} 0 & 1 \\ -b & -a \end{pmatrix}\vec{x}, \quad \vec{x} = \begin{pmatrix} y \\ y' \end{pmatrix}.$$
>
> The eigenvalues of $A = \begin{pmatrix} 0 & 1 \\ -b & -a \end{pmatrix}$ satisfy $\det(A - rI) = 0$:
>
> $$\det\begin{pmatrix} -r & 1 \\ -b & -a-r \end{pmatrix} = r(a+r) + b = r^2 + ar + b = 0.$$
>
> **The characteristic equation IS the eigenvalue equation.** The roots $r_1, r_2$ are eigenvalues. The solution $y=e^{rt}$ corresponds to the eigenvector $\begin{pmatrix}1 \\ r\end{pmatrix}$. This is why complex eigenvalues give sines and cosines — they're the same complex exponentials rotating in the phase plane. When you move to Session 19E, you'll see this connection fully exploited: coupled systems → matrix $A$ → eigenvalues → solution.

---

## Example 2: Simple Harmonic Motion

$y'' + \omega^2 y = 0$. $r^2+\omega^2=0$, $r=\pm i\omega$. $y=c_1\cos\omega t + c_2\sin\omega t = A\sin(\omega t+\phi)$.

Period $T=2\pi/\omega$. Frequency $f=\omega/2\pi$.

Mass-spring: $my''+ky=0$. $\omega = \sqrt{k/m}$. Pendulum (small angle): $\theta''+\frac{g}{L}\theta=0$.

---

## Example 3: Damped Harmonic Motion

$my'' + cy' + ky = 0$. Characteristic: $mr^2+cr+k=0$.

$r = \frac{-c\pm\sqrt{c^2-4mk}}{2m}$.

- **Overdamped** ($c^2 > 4mk$): two real roots, no oscillation.
- **Critically damped** ($c^2 = 4mk$): repeated root, fastest return.
- **Underdamped** ($c^2 < 4mk$): complex roots, oscillation with decaying amplitude.

![Damping types — 3D state space, 2D phase portraits, 1D time traces](graphs/19d-damping-types.png)

*Graph 19D-1: 3D — state space trajectories $(y, y', t)$ for all three damping regimes. Red: overdamped (slides to zero), Blue: underdamped (spirals in), Green: critically damped (fastest return without oscillation). 2D — phase portraits $(y, y')$ reveal the geometry: overdamped follows the slow eigen-direction, critically damped touches the origin along one line, underdamped spirals. 1D — time traces show overdamped as sum of two decaying exponentials (slow + fast), critically damped as $(c_1+c_2 t)e^{-t}$, underdamped as $e^{-\alpha t}\cos(\beta t)$ with its exponential envelope.*

---

## Example 4: Euler's Method — Numerical Approximation

For $y'=f(x,y)$, $y(x_0)=y_0$: $y_{n+1} = y_n + h\cdot f(x_n, y_n)$. Step size $h$.

$y' = x+y$, $y(0)=1$. Estimate $y(0.5)$ with $h=0.1$:

$x_0=0,y_0=1$: $y_1=1+0.1(0+1)=1.1$.
$x_1=0.1,y_1=1.1$: $y_2=1.1+0.1(0.1+1.1)=1.22$.
$x_2=0.2,y_2=1.22$: $y_3=1.22+0.1(0.2+1.22)=1.362$.
$x_3=0.3,y_3=1.362$: $y_4=1.362+0.1(0.3+1.362)=1.5282$.
$x_4=0.4,y_4=1.5282$: $y_5=1.5282+0.1(0.4+1.5282)=1.7210$.

$y(0.5)\approx1.721$. Exact: $y=-x-1+2e^x$, $y(0.5)=1.797$. Error $\approx0.076$.

![Euler method — 3D staircase, 2D comparison, 1D error](graphs/19d-euler-method.png)

*Graph 19D-2: 3D — Euler's method as a staircase climbing the unknown solution surface. Each vertical step = $h$, each horizontal jump = $h \cdot f(x_n, y_n)$. 2D — Euler approximation (red dots) vs exact solution (blue curve) for $y' = x+y$, $y(0)=1$ with step $h=0.3$. The red segments show the slope used at each step. 1D — absolute error grows roughly linearly with $x$: global error $\propto h$ (first-order method).*

---

## Example 5: Improved Euler (RK2)

**Predictor step**: $\tilde{y}_{n+1} = y_n + h f(x_n,y_n)$ (Euler).
**Corrector step**: $y_{n+1} = y_n + \frac{h}{2}[f(x_n,y_n) + f(x_{n+1},\tilde{y}_{n+1})]$.

Averages the slope at start and predicted end — much better accuracy ($O(h^2)$ local error vs $O(h)$ for Euler).

---

## Example 6: Phase Plane Preview — Lotka-Volterra

Predator-prey: $\frac{dx}{dt} = ax - bxy$ (prey), $\frac{dy}{dt} = -cy + dxy$ (predator).

Equilibria: $(0,0)$ and $(c/d, a/b)$. Orbits form closed loops — populations oscillate!

![Lotka-Volterra phase plane](graphs/19d2-phase-plane.png)

> **Up to here**: 2nd-order homogeneous: characteristic equation → 3 cases. Euler's method = linear approximation with steps. Improved Euler averages slopes. Phase 4 awaits with full ODE theory.

---

## Practice 1

Solve $y''-y'-2y=0$, $y(0)=1$, $y'(0)=0$.

→ Solutions: [Solutions](solutions/19D-solutions.md#practice-1)

---

## Practice 2

Use Euler with $h=0.2$ to estimate $y(0.4)$ for $y'=y$, $y(0)=1$.

→ Solutions: [Solutions](solutions/19D-solutions.md#practice-2)

---

## Basic Algebra Drill — Higher Order & Numerical (10 Problems)

**D1.** Solve $y''+y'-6y=0$.

**D2.** Solve $y''+6y'+9y=0$.

**D3.** Solve $y''+4y=0$, $y(0)=0$, $y'(0)=2$.

**D4.** Find the characteristic equation for $2y''-3y'+y=0$.

**D5.** Euler: $y'=2x$, $y(0)=0$, $h=0.5$. Find $y(1)$.

**D6.** Euler: $y'=x+y$, $y(0)=1$. One step with $h=0.1$.

**D7.** Classify damping: $y''+5y'+6y=0$ (over/critical/under?).

**D8.** Find period of $y''+9y=0$.

**D9.** Solve $y''-4y=0$, $y(0)=1$, $y'(0)=4$.

**D10.** Improved Euler: $y'=y$, $y(0)=1$, $h=0.2$. One step.

> Solutions: [Solutions](solutions/19D-solutions.md#basic-drill)

---

## Advanced Algebra Drill — Higher Order & Numerical (10 Problems)

**A1.** Solve $y''-2y'+5y=0$, $y(0)=1$, $y'(0)=3$.

**A2.** Find the general solution of $y''+2y'+y=e^{-x}$ by guessing $y_p=Ax^2e^{-x}$.

**A3.** For $y''+4y'+20y=0$, express as damped oscillation. Find pseudo-frequency.

**A4.** Euler vs exact: $y'=-2xy$, $y(0)=1$. Compute Euler $y(1)$ with $h=0.25$. Compare to exact $e^{-1}$.

**A5.** Improved Euler on $y'=x+y$, $y(0)=1$, $h=0.2$. Two steps. Compare to Euler.

**A6.** A spring-mass: $m=1$, $c=2$, $k=5$. Classify. Solve $y''+2y'+5y=0$, $y(0)=1$, $y'(0)=0$.

**A7.** Find the ODE whose characteristic equation has roots $r=-1\pm2i$.

**A8.** Euler error: prove local truncation error is $O(h^2)$ for $y'=f(x,y)$ by Taylor expanding $y(x_{n+1})$.

**A9.** RLC circuit: $LQ''+RQ'+Q/C=0$. Find condition for underdamped oscillation.

**A10.** Lotka-Volterra: show $(c/d, a/b)$ is an equilibrium. Linearize and classify stability.

> Solutions: [Solutions](solutions/19D-solutions.md#advanced-drill)

---

## How to Read These Symbols

| Symbol | Reads as | Meaning |
|:---:|:---:|------|
| $y''$ | "y double prime" / "second derivative" | acceleration — rate of change of slope |
| $ay''+by'+cy=0$ | "a y double prime plus b y prime plus c y equals zero" | second-order linear homogeneous ODE |
| $r$ | "r" / "characteristic root" | root of ar²+br+c=0 — determines solution form |
| $i$ | "i" / "the imaginary unit" | i² = −1 — appears in complex roots for oscillatory solutions |
| $e^{\alpha x}(c_1\cos\beta x + c_2\sin\beta x)$ | "e to the alpha x times c1 cosine beta x plus c2 sine beta x" | solution for complex roots α±iβ — damped/growing oscillation |
| $c_1, c_2$ | "c one, c two" / "arbitrary constants" | determined by initial conditions |
| $\omega$ | "omega" / "angular frequency" | ω = 2πf = 2π/T — radians per unit time |
| $T = 2\pi/\omega$ | "T equals two pi over omega" | period — time for one complete cycle |
| $h$ | "h" / "step size" | Euler method step — smaller h = better accuracy |
| $y_{n+1} = y_n + h f(x_n, y_n)$ | "y n+1 equals y n plus h times f of x n, y n" | Euler method — one step of slope-following |
| $O(h^2)$ | "big-O of h squared" | local truncation error proportional to h² |
| RK2 | "R K two" / "Runge-Kutta second order" | improved Euler — averages slopes for better accuracy |
| overdamped / critically damped / underdamped | "overdamped" / "critically damped" / "underdamped" | three damping regimes: no oscillation / fastest return / decaying oscillation |


---

## Terminology

| What we call it | Math term | Notation |
|:---:|:---:|:---:|
| highest derivative is 2nd | second-order ODE | $ay''+by'+cy=0$ |
| equation for r from y=e^{rx} | characteristic equation | $ar^2+br+c=0$ |
| roots are real numbers | real distinct / repeated roots | $r_1,r_2 \in \mathbb{R}$ |
| roots are α±iβ | complex conjugate roots | $r = \alpha \pm i\beta$ |
| mass-spring oscillation | simple harmonic motion | $y''+\omega^2y=0$ |
| step-by-step slope approximation | Euler's method | $y_{n+1}=y_n+h f(x_n,y_n)$ |
| predict-correct average slope | improved Euler / RK2 | $y_{n+1}=y_n+\frac{h}{2}[f_n+f_{n+1}]$ |
