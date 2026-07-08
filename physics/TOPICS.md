# Physics Curriculum v2: Classical Mechanics — Derive Models with Calculus, Predict Reality

> **Textbook:** Daniel Kleppner, Robert Kolenkow — *An Introduction to Mechanics* (2nd Edition)
> **Duration:** 3 months (12 weeks), 4–5 sessions/week × ~90 min = ~44 sessions, ~67 total hours
> **Prerequisites:** Fluency in single-variable calculus and basic ODEs (see [GUIDELINE.md §10](GUIDELINE.md#10-prerequisites-assumed-not-taught)). Calculus technique is never re-taught.
> **Grand Objective:** Derive every classical mechanics model from first principles using calculus, understand the logical structure, and compute real numerical predictions.
> **Principle:** Derivation first, modeling second, computation last. There is no path except pen in hand, following along.
> **v2:** English edition. Calculus/ODE skills assumed. All math in KaTeX-compatible LaTeX.

---

## Overall Structure

| Phase | Topic Cluster | Kleppner Ch. | Sessions | Hours |
|:---:|------|:---:|:---:|:---:|
| 1 | Vectors, Kinematics, Newton's Laws — the foundational arsenal | 1–3 | 8 | ~11h |
| 2 | Momentum & Energy — deriving and applying the two conservation laws | 4–5 | 6 | ~9h |
| 3 | Angular Momentum & Rigid-Body Rotation — conquering the rotational world | 6–8 | 7 | ~11h |
| 4 | Non-Inertial Frames, Central Forces, Harmonic Oscillator — advanced dynamics | 9–11 | 7 | ~11h |
| 5 | Special Relativity — reconstructing spacetime | 12–14 | 6 | ~9h |
| 6 | Synthesis & Extensions — restoring the full derivation chain + advanced topics | — | 10 | ~16h |
| **Total** | | | **44** | **~67h** |

---

## Phase 1: Vectors, Kinematics, Newton's Laws — The Foundational Arsenal (8 sessions, ~11h)

> **Core Question:** *"How do we describe motion mathematically, and how do we predict why objects move the way they do?"*
> **Kleppner Ch.1–3.**
> **Key Derivation:** Position $\xrightarrow{\text{differentiate}}$ Velocity $\xrightarrow{\text{differentiate}}$ Acceleration $\xrightarrow{\text{Newton's Laws}}$ Equation of Motion

| # | Topic | Derivation & Modeling Content | Time |
|:--:|------|-----------|:---:|
| 01 | Vectors — the tool for decomposing and combining physical quantities | ① Scalar vs. vector distinction ② Component decomposition: $\mathbf{A}=A_x\hat{\mathbf{i}}+A_y\hat{\mathbf{j}}+A_z\hat{\mathbf{k}}$ ③ Dot product: $\mathbf{A}\cdot\mathbf{B}=AB\cos\theta$ — basis of work & power ④ Cross product: $\mathbf{A}\times\mathbf{B}$ — basis of torque & angular momentum ⑤ Unit vectors and direction | 60 min |
| 02 | Position, Velocity, Acceleration — describing motion with derivatives | ① Average velocity $\xrightarrow{\text{limit}}$ instantaneous velocity $\mathbf{v}=d\mathbf{r}/dt$ ② Average acceleration $\xrightarrow{\text{limit}}$ instantaneous acceleration $\mathbf{a}=d\mathbf{v}/dt=d^2\mathbf{r}/dt^2$ ③ 1D constant acceleration: $\mathbf{a}=\text{const}$ $\xrightarrow{\text{integrate}}$ $v=v_0+at$ $\xrightarrow{\text{integrate}}$ $x=x_0+v_0t+\frac{1}{2}at^2$ ④ Eliminate $t$: $v^2=v_0^2+2a(x-x_0)$ | 75 min |
| 03 | 2D Motion — complete analysis of projectile motion | ① Projectile in uniform gravity: $\mathbf{F}=(0,-mg)$ $\Rightarrow$ $a_x=0$, $a_y=-g$ ② $x$-direction: uniform motion $x(t)=x_0+v_{0x}t$ ③ $y$-direction: constant acceleration $y(t)=y_0+v_{0y}t-\frac{1}{2}gt^2$ ④ Trajectory equation: eliminate $t$ $\Rightarrow$ $y=x\tan\theta - \frac{gx^2}{2v_0^2\cos^2\theta}$ (a parabola) ⑤ Derive max height, time of flight, range ⑥ Two launch angles giving the same range | 90 min |
| 04 | Polar Coordinates & Circular Motion — a better coordinate system for rotation | ① Unit vectors $\hat{\mathbf{r}}, \hat{\boldsymbol{\theta}}$ and their derivatives: $d\hat{\mathbf{r}}/dt=\dot{\theta}\hat{\boldsymbol{\theta}}$, $d\hat{\boldsymbol{\theta}}/dt=-\dot{\theta}\hat{\mathbf{r}}$ ② $\mathbf{r}=r\hat{\mathbf{r}}$ $\xrightarrow{\text{differentiate}}$ $\mathbf{v}=\dot{r}\hat{\mathbf{r}}+r\dot{\theta}\hat{\boldsymbol{\theta}}$ ③ $\xrightarrow{\text{differentiate}}$ $\mathbf{a}=(\ddot{r}-r\dot{\theta}^2)\hat{\mathbf{r}}+(r\ddot{\theta}+2\dot{r}\dot{\theta})\hat{\boldsymbol{\theta}}$ ④ Uniform circular motion: $\dot{r}=0$, $\ddot{\theta}=0$ $\Rightarrow$ $\mathbf{a}=-r\omega^2\hat{\mathbf{r}}$ (centripetal) ⑤ Confirm magnitude & direction via two methods (polar derivation, geometric) | 90 min |
| 05 | Newton's Three Laws — force as the cause of motion | ① First Law (inertia): $\mathbf{F}=0 \Rightarrow \mathbf{v}=\text{const}$ — Galilean transformations and inertial frames ② Second Law: $\mathbf{F}=d\mathbf{p}/dt$. Constant mass $\Rightarrow$ $\mathbf{F}=m\mathbf{a}$. **This is the prototype equation of motion.** ③ Third Law (action-reaction): $\mathbf{F}_{A\to B}=-\mathbf{F}_{B\to A}$ ④ Superposition: $\sum\mathbf{F}=m\mathbf{a}$ ⑤ Units: SI (m, kg, s, N, J, W), cgs, dimensional analysis | 60 min |
| 06 | Everyday Forces — gravity, tension, normal force, friction | ① Gravity: $\mathbf{F}_g=m\mathbf{g}$, near Earth's surface $\mathbf{g}=9.8\,\text{m/s}^2\downarrow$ ② Tension: transmitted along a massless, inextensible ideal string ③ Normal force: surface pushes perpendicular to contact ④ Static friction: $f_s \leq \mu_s N$ — **inequality, not equality** — "only as much as needed" ⑤ Kinetic friction: $f_k=\mu_k N$, opposite to velocity ⑥ Inclined plane decomposition: $mg\sin\theta$ (downhill), $mg\cos\theta$ (normal) | 75 min |
| 07 | Equations of Motion I — constant forces | ① 1D equation of motion $m\ddot{x}=F$ $\xrightarrow{\text{integrate}}$ solution ② Block sliding on incline: $m\ddot{x}=mg\sin\theta-\mu mg\cos\theta$ $\Rightarrow$ constant acceleration ③ Atwood machine: two masses, one string $\Rightarrow$ coupled equations of motion ④ Solving for string tension: EOM for each mass $\Rightarrow$ eliminate $\Rightarrow$ solve | 90 min |
| 08 | Equations of Motion II — velocity-dependent forces | ① Drag forces: $F_{\text{drag}}=-bv$ (viscous), $-cv^2$ (inertial) ② Viscous-damped fall: $m\ddot{y}=-mg-b\dot{y}$ $\xrightarrow{\text{separate}}$ $v(t)=\frac{mg}{b}(1-e^{-bt/m})$ ③ Terminal velocity: $t\to\infty$, $v_{\text{term}}=mg/b$ ④ Inertial-drag fall: terminal velocity $v_{\text{term}}=\sqrt{mg/c}$ ⑤ Physical interpretation: comparing time constants, Reynolds number intuition | 90 min |

---

## Phase 2: Momentum & Energy — Deriving and Applying the Two Conservation Laws (6 sessions, ~9h)

> **Core Question:** *"What is conserved when we integrate Newton's laws? And how do these conserved quantities let us solve problems elegantly?"*
> **Kleppner Ch.4–5.**
> **Key Derivation:** $\mathbf{F}=d\mathbf{p}/dt$ $\xrightarrow{\text{integrate } dt}$ Impulse-Momentum $\quad$ | $\quad$ $\mathbf{F}=m\mathbf{a}$ $\xrightarrow{\text{integrate } d\mathbf{r}}$ Work-Energy

| # | Topic | Derivation & Modeling Content | Time |
|:--:|------|-----------|:---:|
| 09 | Momentum and Impulse — the fruit of time-integration | ① $\mathbf{F}=d\mathbf{p}/dt$ $\Rightarrow$ $\int_{t_1}^{t_2}\mathbf{F}\,dt = \mathbf{p}_2-\mathbf{p}_1$ ② Impulse $\mathbf{J}=\int\mathbf{F}\,dt$ = change in momentum — area under $F$-$t$ graph ③ Brief collisions: $\mathbf{F}_{\text{avg}}\Delta t = \Delta\mathbf{p}$ ④ Momentum conservation: $\sum\mathbf{F}_{\text{ext}}=0$ $\Rightarrow$ $\mathbf{P}_{\text{total}}=\sum\mathbf{p}_i=\text{const}$ ⑤ Newton's 3rd Law $\Rightarrow$ internal forces cancel pairwise $\Rightarrow$ logical basis of momentum conservation | 75 min |
| 10 | Collisions — momentum & energy conservation in concert | ① Elastic collision: momentum conservation + kinetic energy conservation ② 1D elastic collision formula: $v_{1f}=\frac{m_1-m_2}{m_1+m_2}v_{1i}+\frac{2m_2}{m_1+m_2}v_{2i}$ ③ Special cases: equal mass $\Rightarrow$ velocity exchange; massive wall $\Rightarrow$ rebound ④ Perfectly inelastic: stick together, momentum only ⑤ Coefficient of restitution $e$: $v_{2f}-v_{1f}=-e(v_{2i}-v_{1i})$ ⑥ Viewing collisions in the center-of-mass frame | 90 min |
| 11 | Work and Kinetic Energy — the fruit of space-integration | ① Work definition: $W_{a\to b}=\int_a^b \mathbf{F}\cdot d\mathbf{r}$ — integrate force along the path ② Substitute $\mathbf{F}=m\frac{d\mathbf{v}}{dt}$, $d\mathbf{r}=\mathbf{v}\,dt$ $\Rightarrow$ $W=\int m\mathbf{v}\cdot d\mathbf{v}$ ③ $\Rightarrow$ $W=\frac{1}{2}mv_b^2 - \frac{1}{2}mv_a^2$ ④ Kinetic energy $T=\frac{1}{2}mv^2$ — derivation complete ⑤ Work-Energy Theorem: $W_{\text{net}}=\Delta T$ ⑥ Power: $P=dW/dt=\mathbf{F}\cdot\mathbf{v}$ | 75 min |
| 12 | Potential Energy and Conservative Forces — the power of path-independence | ① Conservative force: $\oint\mathbf{F}\cdot d\mathbf{r}=0$ — closed-path work is zero ② Potential energy: $\mathbf{F}=-\nabla U$, in 1D: $F=-dU/dx$ ③ Gravitational potential: $U_g=mgy$ (uniform field), $U_g=-GMm/r$ (universal) ④ Spring potential: $F=-kx$ $\Rightarrow$ $U_s=\frac{1}{2}kx^2$ ⑤ Recovering force from $U$: $F_x=-\partial U/\partial x$ — negative gradient ⑥ Potential wells and equilibrium: stable ($d^2U/dx^2>0$), unstable ($d^2U/dx^2<0$) | 90 min |
| 13 | Mechanical Energy Conservation — the universe's best computational shortcut | ① Conservative forces only: $T+U=E=\text{const}$ ② $E$ is set by initial conditions: $E=\frac{1}{2}mv_0^2+U(\mathbf{r}_0)$ ③ 1D: $\frac{1}{2}m\dot{x}^2+U(x)=E$ $\Rightarrow$ $\dot{x}=\pm\sqrt{\frac{2}{m}(E-U(x))}$ $\xrightarrow{\text{separate}}$ $t=\int\frac{dx}{\sqrt{2(E-U(x))/m}}$ ④ Potential barriers & turning points: $U(x)=E$ $\Rightarrow$ $\dot{x}=0$, direction reverses ⑤ With non-conservative forces: $W_{\text{nc}}=\Delta E$ | 75 min |
| 14 | Solving Problems with Energy — getting answers without touching forces | ① Pendulum: find lowest-point speed via $T+U$ — cleaner than force decomposition ② Roller coaster: knowing height alone gives speed ③ Spring + gravity: $E=\frac{1}{2}mv^2+\frac{1}{2}kx^2+mgy$ ④ Energy diagrams: plot $U(x)$, draw horizontal $E$ line — visualize allowed regions ⑤ Estimating force magnitude from energy: $F\sim\Delta U/\Delta x$ — potential gradient = force ⑥ Decision criteria: momentum vs. energy — which tool for which problem? | 90 min |

---

## Phase 3: Angular Momentum & Rigid-Body Rotation — Conquering the Rotational World (7 sessions, ~11h)

> **Core Question:** *"When objects rotate, how do all linear-motion concepts translate into their rotational counterparts?"*
> **Kleppner Ch.6–8.**
> **Key Derivation:** $\boldsymbol{\tau}=\mathbf{r}\times\mathbf{F}$ $\xrightarrow{\text{cross-product derivative}}$ $\mathbf{L}=\mathbf{r}\times\mathbf{p}$, $\frac{d\mathbf{L}}{dt}=\boldsymbol{\tau}$ $\rightarrow$ Rigid body: $\mathbf{L}=I\boldsymbol{\omega}$

| # | Topic | Derivation & Modeling Content | Time |
|:--:|------|-----------|:---:|
| 15 | Angular Momentum — the momentum of rotation | ① Torque: $\boldsymbol{\tau}=\mathbf{r}\times\mathbf{F}$ — lever arm $\times$ force; direction via right-hand rule ② Angular momentum: $\mathbf{L}=\mathbf{r}\times\mathbf{p}$ ③ $\frac{d\mathbf{L}}{dt}=\frac{d\mathbf{r}}{dt}\times\mathbf{p}+\mathbf{r}\times\frac{d\mathbf{p}}{dt}=\mathbf{v}\times m\mathbf{v}+\mathbf{r}\times\mathbf{F}=\boldsymbol{\tau}$ — first term $\mathbf{v}\times m\mathbf{v}=0$ ④ Angular momentum conservation: $\sum\boldsymbol{\tau}_{\text{ext}}=0$ $\Rightarrow$ $\mathbf{L}=\text{const}$ ⑤ Central force ($\mathbf{F}\parallel\mathbf{r}$) has zero torque $\Rightarrow$ $\mathbf{L}$ conserved $\Rightarrow$ areal velocity constant (Kepler's 2nd) | 90 min |
| 16 | Fixed-Axis Rotation — the emergence of moment of inertia | ① Particle rotating about $z$-axis: $L_z=mr_\perp^2\omega$ ② System of particles: $L_z=(\sum m_i r_{i\perp}^2)\,\omega = I_z\omega$ ③ Moment of inertia $I=\sum m_i r_{i\perp}^2 = \int r_\perp^2\,dm$ — integrating the mass distribution ④ Rod (center): $I=\frac{1}{12}ML^2$, rod (end): $I=\frac{1}{3}ML^2$ — verify via parallel-axis theorem ⑤ Disk: $I=\frac{1}{2}MR^2$, hoop: $I=MR^2$, sphere: $I=\frac{2}{5}MR^2$ | 90 min |
| 17 | Rotational Equation of Motion — deriving and applying $\tau=I\alpha$ | ① $\sum\tau_z = \frac{dL_z}{dt} = \frac{d}{dt}(I_z\omega) = I_z\alpha$ (fixed $I$) ② Combined rotation + translation: pulley, rolling ball, yo-yo ③ Pulley with hanging mass: $mg-T=ma$, $TR=I\alpha$, $a=R\alpha$ $\Rightarrow$ solve coupled system ④ Rolling down an incline: sliding vs. rolling — determining friction direction ⑤ Rolling condition: $v_{\text{cm}}=R\omega$, no slipping $\Rightarrow$ static friction | 90 min |
| 18 | Parallel-Axis & Perpendicular-Axis Theorems — the moment-of-inertia arsenal | ① Parallel-axis theorem derivation: substitute $\mathbf{r}=\mathbf{r}_{\text{cm}}+\mathbf{d}$ $\Rightarrow$ $I=I_{\text{cm}}+Md^2$ ② Perpendicular-axis theorem (thin plate): $I_z=I_x+I_y$ ③ Proof: $\sum(x^2+y^2)=\sum x^2+\sum y^2$ ④ Composite bodies: decompose and sum $I$ ⑤ Mass volume of $I$-calculation practice using the parallel-axis theorem | 75 min |
| 19 | Rotational Work, Energy & Angular Momentum Conservation Applications | ① Rotational kinetic energy: $T_{\text{rot}}=\frac{1}{2}I\omega^2$ — derivation: $T=\sum\frac{1}{2}m_i v_i^2=\sum\frac{1}{2}m_i(r_i\omega)^2=\frac{1}{2}(\sum m_i r_i^2)\omega^2$ ② Work: $W=\int\tau\,d\theta$ — integrate torque over angle ③ Power: $P=\tau\omega$ ④ Angular momentum conservation applications: figure skating spin, falling cat, gyroscope precession intuition ⑤ Collision + rotation: particle sticks to end of rod $\Rightarrow$ use $\mathbf{L}$ conservation to find $\omega$ just after impact | 90 min |
| 20 | Rigid-Body Static Equilibrium — torque balance | ① Equilibrium conditions: $\sum\mathbf{F}=0$ **and** $\sum\boldsymbol{\tau}=0$ (about any point) ② Freedom to choose the pivot: compute torque where convenient ③ Ladder problem: normal force, friction, center of mass — account for all forces & torques ④ Center of mass: $\mathbf{R}_{\text{cm}}=\frac{\sum m_i\mathbf{r}_i}{M}$, integral for continua ⑤ Static equilibrium + stability: tilt slightly, check torque direction | 75 min |
| 21 | Rigid-Body Dynamics Synthesis — rolling + rotation + collisions consolidated | ① Phase 3 comprehensive problems ② Combined translational + rotational kinetic energy: $T=\frac{1}{2}Mv_{\text{cm}}^2+\frac{1}{2}I_{\text{cm}}\omega^2$ ③ Rolling race: compare accelerations of sphere, cylinder, hoop — only $I$ differs ④ Angular momentum vector conservation & precession via ODE: $d\mathbf{L}/dt=\boldsymbol{\tau}\perp\mathbf{L}$ $\Rightarrow$ $\mathbf{L}$ direction rotates (precession) | 120 min |

---

## Phase 4: Non-Inertial Frames, Central Forces, Harmonic Oscillator — Advanced Dynamics (7 sessions, ~11h)

> **Core Question:** *"How does the world look to a rotating observer? Why do planets trace ellipses? Why is every small oscillation a sine wave?"*
> **Kleppner Ch.9–11.**
> **Key Derivation:** Non-inertial frames $\rightarrow$ fictitious forces appear, Central forces $\rightarrow$ effective potential, Harmonic oscillator $\rightarrow$ solution of $m\ddot{x}+kx=0$

| # | Topic | Derivation & Modeling Content | Time |
|:--:|------|-----------|:---:|
| 22 | Accelerated Frames — translational acceleration and fictitious forces | ① Inertial frame $S$ and accelerating frame $S'$: $\mathbf{r}=\mathbf{r}'+\mathbf{R}$ $\xrightarrow{\text{differentiate twice}}$ $\mathbf{a}=\mathbf{a}'+\mathbf{A}$ ② $\mathbf{F}=m\mathbf{a}$ $\Rightarrow$ $m\mathbf{a}'=\mathbf{F}-m\mathbf{A}$ ③ $-m\mathbf{A}$: fictitious force (inertial force) — elevator, sudden-braking bus ④ Real vs. fictitious: who is observing? Measurable by an accelerometer? ⑤ Freely falling elevator: $\mathbf{F}_g=-mg\hat{\mathbf{k}}$, $\mathbf{A}=-g\hat{\mathbf{k}}$ $\Rightarrow$ $\mathbf{a}'=0$ — weightlessness! | 60 min |
| 23 | Rotating Frames — deriving centrifugal and Coriolis forces | ① Time-derivative of rotating-frame unit vectors: $d\hat{\mathbf{i}}'/dt=\boldsymbol{\omega}\times\hat{\mathbf{i}}'$ ② $\mathbf{v}=\mathbf{v}'+\boldsymbol{\omega}\times\mathbf{r}'$ ③ $\mathbf{a}=\mathbf{a}'+2\boldsymbol{\omega}\times\mathbf{v}'+\boldsymbol{\omega}\times(\boldsymbol{\omega}\times\mathbf{r}')$ (constant $\boldsymbol{\omega}$) ④ $\mathbf{F}=m\mathbf{a}$ $\Rightarrow$ $m\mathbf{a}'=\mathbf{F}-2m\boldsymbol{\omega}\times\mathbf{v}'-m\boldsymbol{\omega}\times(\boldsymbol{\omega}\times\mathbf{r}')$ ⑤ $-m\boldsymbol{\omega}\times(\boldsymbol{\omega}\times\mathbf{r}')$: centrifugal — outward, magnitude $m\omega^2 r_\perp$ ⑥ $-2m\boldsymbol{\omega}\times\mathbf{v}'$: Coriolis — perpendicular to velocity, deflection | 90 min |
| 24 | Inertial Forces on Earth — Foucault pendulum and trade winds | ① Earth's rotation $\omega=7.29\times10^{-5}\,\text{rad/s}$, decompose at latitude $\lambda$ ② Plumb-line deflection: effective gravity $\mathbf{g}_{\text{eff}}=\mathbf{g}-\boldsymbol{\omega}\times(\boldsymbol{\omega}\times\mathbf{r})$ ③ Foucault pendulum: rotation rate of oscillation plane $\Omega=-\omega\sin\lambda$ ④ Coriolis eastward deflection of falling bodies: $\frac{2}{3}\omega h\sqrt{2h/g}\cos\lambda$ ⑤ Trade winds & cyclone rotation — CCW in northern hemisphere, CW in southern | 75 min |
| 25 | Central Forces — universal gravitation and the equation of motion | ① Central force: $\mathbf{F}=f(r)\hat{\mathbf{r}}$ $\Rightarrow$ torque = 0 $\Rightarrow$ $\mathbf{L}$ conserved $\Rightarrow$ planar motion ② Polar EOM: $m(\ddot{r}-r\dot{\theta}^2)=f(r)$, $\frac{d}{dt}(mr^2\dot{\theta})=0$ ③ $mr^2\dot{\theta}=L=\text{const}$ $\Rightarrow$ $\dot{\theta}=L/(mr^2)$ ④ Radial equation: $m\ddot{r}=f(r)+\frac{L^2}{mr^3}$ — centrifugal term emerges ⑤ Effective potential: $U_{\text{eff}}(r)=U(r)+\frac{L^2}{2mr^2}$ — centrifugal barrier ⑥ 1D energy view: $\frac{1}{2}m\dot{r}^2+U_{\text{eff}}(r)=E$ | 90 min |
| 26 | Gravitational Orbits — deriving conic sections | ① $f(r)=-GMm/r^2$ $\Rightarrow$ substitute $u=1/r$ $\Rightarrow$ orbit equation: $\frac{d^2u}{d\theta^2}+u=\frac{GMm^2}{L^2}$ ② Solution: $u=A\cos(\theta-\theta_0)+\frac{GMm^2}{L^2}$ ③ $\Rightarrow$ $r=\frac{r_0}{1+\varepsilon\cos\theta}$, $r_0=L^2/(GMm^2)$, $\varepsilon$ = eccentricity ④ $\varepsilon<1$: ellipse, $\varepsilon=1$: parabola, $\varepsilon>1$: hyperbola ⑤ Prove Kepler's Laws: (1) elliptical orbits (2) areal velocity = $L/2m$ (3) $T^2\propto a^3$ | 90 min |
| 27 | Harmonic Oscillator I — complete analysis of free oscillation | ① Hooke's Law: $F=-kx$ $\Rightarrow$ $m\ddot{x}+kx=0$ $\Rightarrow$ $\ddot{x}+\omega_0^2 x=0$, $\omega_0=\sqrt{k/m}$ ② Trial exponential: $x=e^{\lambda t}$ $\Rightarrow$ $\lambda^2+\omega_0^2=0$ $\Rightarrow$ $\lambda=\pm i\omega_0$ ③ General solution: $x(t)=A\cos\omega_0 t+B\sin\omega_0 t=C\cos(\omega_0 t+\phi)$ ④ Amplitude $C$, phase $\phi$ set by initial conditions ⑤ Energy: $E=\frac{1}{2}kA^2=\frac{1}{2}m\omega_0^2 A^2$ — proportional to amplitude squared ⑥ Complex representation: $z=x+iv/\omega_0$, $z=Ae^{i(\omega_0 t+\phi)}$ — a circle in phase space | 75 min |
| 28 | Harmonic Oscillator II — damping, driving, resonance | ① Viscous damping: $m\ddot{x}+b\dot{x}+kx=0$ $\Rightarrow$ $\ddot{x}+2\beta\dot{x}+\omega_0^2 x=0$ ② $\beta<\omega_0$ (underdamped): $x(t)=Ae^{-\beta t}\cos(\omega_1 t+\phi)$, $\omega_1=\sqrt{\omega_0^2-\beta^2}$ ③ $\beta=\omega_0$ (critically damped), $\beta>\omega_0$ (overdamped) — no oscillation ④ Driven oscillator: $m\ddot{x}+b\dot{x}+kx=F_0\cos\omega t$ ⑤ Steady-state: $x(t)=D\cos(\omega t-\delta)$, amplitude $D=\frac{F_0/m}{\sqrt{(\omega_0^2-\omega^2)^2+(2\beta\omega)^2}}$ ⑥ Resonance: $\omega\approx\omega_0$, $D_{\text{max}}=\frac{F_0}{2m\beta\omega_0}$, $\delta=\pi/2$ — quality factor $Q=\omega_0/(2\beta)$ | 105 min |

---

## Phase 5: Special Relativity — Reconstructing Spacetime (6 sessions, ~9h)

> **Core Question:** *"If the speed of light is the same for everyone, how must time and space be redefined?"*
> **Kleppner Ch.12–14.**
> **Key Derivation:** Light-speed invariance $\rightarrow$ Lorentz transformation $\rightarrow$ time dilation & length contraction $\rightarrow$ relativistic momentum & energy $\rightarrow$ $E=mc^2$

| # | Topic | Derivation & Modeling Content | Time |
|:--:|------|-----------|:---:|
| 29 | The Collapse of Galilean Relativity — the shock of invariant light-speed | ① Galilean transformation: $x'=x-Vt$, $t'=t$, $v'=v-V$ ② Maxwell's equations: $c=1/\sqrt{\mu_0\epsilon_0}=3.00\times10^8\,\text{m/s}$ — velocity addition fails ③ Michelson-Morley experiment: no ether wind $\Rightarrow$ $c$ is the same in all inertial frames ④ Einstein's two postulates: (1) Laws of physics identical in all inertial frames (2) $c$ is invariant ⑤ Relativity of simultaneity: events simultaneous in one frame are not in another — signal propagation delay | 75 min |
| 30 | Lorentz Transformation — the new connection law for spacetime | ① Assume linear transformation: $x'=\gamma(x-Vt)$, $t'=\alpha x+\beta t$ ② Invoke light-speed invariance: $x=ct \Leftrightarrow x'=ct'$ $\Rightarrow$ $\gamma=\frac{1}{\sqrt{1-V^2/c^2}}$ ③ Lorentz transformation complete: $x'=\gamma(x-Vt)$, $t'=\gamma(t-Vx/c^2)$ ④ Meaning of $\gamma$: $V\to0$ $\Rightarrow$ $\gamma\to1$ — recovers Galilean transform ⑤ $V\to c$ $\Rightarrow$ $\gamma\to\infty$ — $c$ is an unreachable speed limit ⑥ Spacetime interval: $\Delta s^2=(c\Delta t)^2-(\Delta x)^2$ — Lorentz invariant | 90 min |
| 31 | Time Dilation & Length Contraction — moving clocks run slow | ① Time dilation: moving clocks tick slower. $\Delta t=\gamma\Delta t_0$ ($\Delta t_0$: proper time) ② Muon decay verification: atmospheric muons reach Earth's surface — impossible without time dilation ③ Length contraction: moving rods shorten. $L=L_0/\gamma$ ($L_0$: proper length) ④ Time dilation & length contraction are the same phenomenon from different frames — relativity is internally consistent ⑤ Twin paradox: resolved by acceleration asymmetry — the non-inertial twin ages less | 75 min |
| 32 | Velocity Addition & Doppler Effect | ① Differentiate Lorentz transform $\Rightarrow$ relativistic velocity addition: $u_x=\frac{u_x'+V}{1+Vu_x'/c^2}$ ② Insert $u_x'=c$ $\Rightarrow$ $u_x=c$ — $c$ always comes out as $c$ ③ $V\ll c$ $\Rightarrow$ $u_x\approx u_x'+V$ — Galilean approximation ④ Aberration & Doppler effect derivation ⑤ Longitudinal Doppler: $f'=f\sqrt{\frac{1-\beta}{1+\beta}}$, transverse: $f'=f/\gamma$ — pure time-dilation effect ⑥ Cosmological redshift, radar speed measurement applications | 75 min |
| 33 | Relativistic Momentum & Energy — deriving $E=mc^2$ | ① Classical momentum conservation is not Lorentz-invariant $\Rightarrow$ must redefine momentum ② Collision analysis $\Rightarrow$ $\mathbf{p}=\gamma m\mathbf{v}$ — the $\gamma$ factor appears ③ Force: $\mathbf{F}=d\mathbf{p}/dt$ — Newtonian form preserved, only $\mathbf{p}$ replaced ④ Work-energy: $W=\int\mathbf{F}\cdot d\mathbf{r}=\int\frac{d}{dt}(\gamma m\mathbf{v})\cdot\mathbf{v}\,dt$ $\Rightarrow$ $W=mc^2(\gamma-1)$ ⑤ Rest energy: $E_0=mc^2$, total energy: $E=\gamma mc^2$, kinetic energy: $T=E-mc^2$ ⑥ $v\ll c$ $\Rightarrow$ $T\approx\frac{1}{2}mv^2$ — classical limit recovered | 90 min |
| 34 | Relativistic Momentum-Energy Conservation — particle physics applications | ① Energy-momentum relation: $E^2=(pc)^2+(mc^2)^2$ — a right triangle ② Massless particles (photons): $E=pc$, $v=c$ ③ Collision problems: 4-momentum conservation $\sum P_\mu^{\text{in}}=\sum P_\mu^{\text{out}}$ ④ Particle creation/annihilation: rest mass converts to kinetic energy — nuclear reactions, particle collisions ⑤ Compton scattering: photon-electron collision $\Rightarrow$ wavelength shift $\Delta\lambda=\frac{h}{m_ec}(1-\cos\theta)$ ⑥ Experimental confirmation of mass-energy equivalence | 75 min |
| 35 | Spacetime Geometry — 4-vectors and Minkowski space | ① 4-vectors: $X^\mu=(ct,x,y,z)$, $P^\mu=(E/c,p_x,p_y,p_z)$ ② Lorentz transformation as a matrix: $X'^\mu=\Lambda^\mu_\nu X^\nu$ ③ Inner product: $A\cdot B=A^0B^0-A^1B^1-A^2B^2-A^3B^3$ — Lorentz invariant ④ Proper time: $d\tau=dt/\gamma$, 4-velocity: $U^\mu=dX^\mu/d\tau$ ⑤ 4-force (Minkowski force): $K^\mu=dP^\mu/d\tau$ ⑥ Causality & light cones: $\Delta s^2>0$ (timelike) — causal connection possible; $\Delta s^2<0$ (spacelike) — not possible | 60 min |

---

## Phase 6: Synthesis & Extensions — Restoring the Full Derivation Chain + Advanced Topics (10 sessions, ~16h)

> **Core Question:** *"Weave everything from Phases 1–5 into a single chain, and taste the modern extensions that Kleppner omits."*
> **Goal:** Reconstruct the entire derivation chain of classical mechanics from a blank sheet of paper.

| # | Topic | Derivation & Modeling Content | Time |
|:--:|------|-----------|:---:|
| 36 | Phase 1–2 Synthesis — from equation of motion to conservation laws | ① Starting from $\mathbf{F}=m\mathbf{a}$, derive $\mathbf{p}$, $\mathbf{L}$, $E$ conservation in one uninterrupted chain ② Clarify preconditions for each conservation law: $\sum\mathbf{F}_{\text{ext}}=0$, $\sum\boldsymbol{\tau}_{\text{ext}}=0$, $\mathbf{F}$ conservative ③ Solve one problem via four approaches: direct EOM, momentum, energy, angular momentum — confirm identical results | 120 min |
| 37 | Phase 3–4 Synthesis — rotation + central forces + oscillation crossover | ① Mixed problems: oscillation in a rotating frame, rigid-body motion in a central-force field ② Earth-Moon system: tidal forces and angular momentum exchange ③ Lagrangian points $L_1$–$L_5$ — physical intuition | 120 min |
| 38 | Galilean Invariance & Conservation Laws — a taste of Noether's theorem | ① Spatial translation symmetry $\rightarrow$ momentum conservation ② Temporal translation symmetry $\rightarrow$ energy conservation ③ Rotational symmetry $\rightarrow$ angular momentum conservation ④ Intuitive examples linking symmetry to conservation — "A symmetry implies something is conserved" ⑤ Non-uniform space/time breaks the corresponding conservation law | 90 min |
| 39 | Multi-Particle Systems & Center of Mass — separating internal from external forces | ① $\mathbf{R}_{\text{cm}}=\frac{\sum m_i\mathbf{r}_i}{M}$ $\Rightarrow$ $\mathbf{F}_{\text{ext}}=M\ddot{\mathbf{R}}_{\text{cm}}$ — CM moves only under external forces ② Reduced mass: $\mu=m_1 m_2/(m_1+m_2)$ $\Rightarrow$ two-body to one-body ③ Rocket equation: $m(t)\dot{v}=-\dot{m}u_{\text{ex}}$ $\xrightarrow{\text{integrate}}$ $v_f=v_i+u_{\text{ex}}\ln(m_i/m_f)$ ④ Multi-particle work-energy: total work = CM kinetic energy change + relative kinetic energy change | 75 min |
| 40 | Introduction to Continuum Mechanics — from particles to fields | ① Center of mass (continuum): $\mathbf{R}_{\text{cm}}=\frac{1}{M}\int\mathbf{r}\,dm$ ② Stress and strain: $\sigma=F/A$, $\varepsilon=\Delta L/L$ ③ Young's modulus: $Y=\sigma/\varepsilon$ — Hooke's law for continua ④ Elastic energy density: $u=\frac{1}{2}Y\varepsilon^2$ — generalization of spring potential ⑤ Wave equation for a string: $\mu\frac{\partial^2 y}{\partial t^2}=T\frac{\partial^2 y}{\partial x^2}$ $\Rightarrow$ wave speed $v=\sqrt{T/\mu}$ | 75 min |
| 41 | Lagrangian Mechanics — beyond Newton | ① Generalized coordinates $q_i$ and constraints ② d'Alembert's principle $\rightarrow$ virtual work $\sum(\mathbf{F}_i-\dot{\mathbf{p}}_i)\cdot\delta\mathbf{r}_i=0$ ③ Lagrangian $L=T-U$ $\rightarrow$ Euler-Lagrange equation: $\frac{d}{dt}\frac{\partial L}{\partial\dot{q}_i}-\frac{\partial L}{\partial q_i}=0$ ④ Examples: simple pendulum, double pendulum, constrained particle — more elegant than Newton ⑤ Noether's theorem: symmetry of $L$ $\rightarrow$ conserved quantity ⑥ Re-solve every Kleppner problem using the Lagrangian approach | 120 min |
| 42 | Hamiltonian Mechanics — the emergence of phase space | ① Generalized momentum: $p_i=\partial L/\partial\dot{q}_i$ ② Hamiltonian: $H=\sum p_i\dot{q}_i-L$ $\rightarrow$ for conservative systems $H=T+U=E$ ③ Hamilton's canonical equations: $\dot{q}_i=\partial H/\partial p_i$, $\dot{p}_i=-\partial H/\partial q_i$ ④ Phase space: $2n$-dimensional space of $(q,p)$ — Liouville's theorem (phase-space volume conserved) ⑤ Poisson bracket: $\{f,g\}=\sum\left(\frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i}-\frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i}\right)$ ⑥ The most elegant formulation of classical mechanics — the bridge to quantum mechanics | 120 min |
| 43 | Limits of Classical Mechanics — the bridge to quantum & relativity | ① $c\to\infty$, $\hbar\to0$ limits recover classical mechanics ② Where classical mechanics fails: atomic scale, near light-speed, strong gravity ③ Correspondence principle: quantum expectation values follow classical trajectories (Ehrenfest) ④ Classical chaos: sensitivity to initial conditions, Lyapunov exponents — determinism $\neq$ predictability ⑤ What you've gained from the Kleppner journey: every physical model is derived with calculus, stands on logical assumptions, and is verified against reality | 90 min |
| 44 | **Final Synthesis** — full derivation chain from memory | ① Blank sheet: reconstruct every key derivation from $\mathbf{r}(t)$ to $E=mc^2$ ② Verbally explain: assumptions behind each derivation, the calculus operation used, the logical justification of the result ③ Decision framework: given an arbitrary mechanics problem, which approach (Newton / energy / momentum / angular momentum / Lagrangian) do you choose and why? ④ Identify connections to future subjects: electromagnetism, quantum mechanics, statistical mechanics, fluid dynamics | 150 min |

---

## Supplement — Kleppner Problem Cross-Reference

Use Kleppner's representative examples & problems as Combat exercises for each session.

| Session | Recommended Kleppner Examples & Problems |
|:---:|------|
| 03 | Examples 1.4–1.7, Probs 1.15–1.20 (projectile motion) |
| 04 | Examples 1.8–1.10, Probs 1.21–1.25 (polar coordinates & circular motion) |
| 07 | Examples 2.1–2.5, Probs 2.1–2.10 (inclined planes & pulleys) |
| 08 | Examples 2.6–2.8, Probs 2.15–2.25 (drag-force falling) |
| 10 | Examples 3.3–3.7, Probs 3.10–3.20 (collisions) |
| 12 | Examples 4.1–4.5, Probs 4.1–4.15 (potential energy) |
| 14 | Examples 4.6–4.10, Probs 4.16–4.30 (energy conservation applications) |
| 16 | Examples 6.1–6.5, Probs 6.1–6.15 (moment of inertia) |
| 17 | Examples 6.6–6.10, Probs 6.16–6.30 (rotational EOM) |
| 21 | Examples 7.1–7.8, Probs 7.1–7.25 (rigid-body synthesis) |
| 25 | Examples 8.1–8.4, Probs 8.1–8.10 (central forces) |
| 26 | Examples 8.5–8.8, Probs 8.11–8.25 (orbits) |
| 28 | Examples 9.1–9.5, Probs 9.1–9.20 (harmonic oscillator) |
| 29–35 | Examples 10–14, Probs Ch.11–14 (relativity — all) |

---

## Philosophy of This Curriculum

```text
Classical mechanics is the first great tool humanity built to predict the world with mathematics.

Everything is born from calculus:
  Differentiate position → velocity. Differentiate velocity → acceleration.
  Integrate force (cause of change) over time → momentum. Integrate force over space → energy.

From this tiny chain, we derive everything:
  the orbits of planets, the rhythm of pendulums, the invariance of light,
  and finally E = mc².

When this 3-month journey ends, you will face any mechanics problem
and decide for yourself: "Where do I start? What do I differentiate? What do I integrate?"
