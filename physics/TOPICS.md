# Physics Curriculum v4: Values You Can Never Reach Without Limits

> **Ultimate Goal:** Enter Kleppner & Kolenkow already "knowing what it means."
> **Method:** **In every session, experience "algebraic approximation → failure → exact value through limits (infinite splitting and gathering)."**
> **Core Question:** "What scene does this equation describe, and why can algebra alone never give the exact value?"
> **Scale:** 21 sessions, 4 weeks, approximately 28 hours. Each session includes 5~10 Examples + 5 Basic Drills + 5 Advanced Drills.
> **Duration:** 60~120 minutes (varies by difficulty).
> **Prerequisite:** You already know how to compute change-in-a-blink, split-and-gather, and rate-relationship equations (Math Phase 2 completed).
> **v4 change:** Deprecate "differentiation" and "integration" terminology; instead use physical actions like "change in a blink" and "split and gather."

---

## Alignment with Kleppner

```
Phase 0                                →  Kleppner & Kolenkow
───────────────────────────────────────────────────────────────
Week 1: Describing Motion (Vectors + Kinematics)  →  Ch 1  Vectors and Kinematics
Week 2: Causes of Motion (Newton + FBD)           →  Ch 2  Newton's Laws
                                                     Ch 3  Forces and Equations of Motion
Week 3: Conservation from Gathering (Momentum + Energy) →  Ch 4  Momentum
                                                           Ch 5  Energy
Week 4: Rotation + Synthesis (Angular Momentum + Oscillation) →  Ch 6  Angular Momentum
                                                                  Ch 7  Fixed Axis Rotation
                                                                  Ch 11 Harmonic Oscillator (preview)
```

---

## Week 1: Describing Motion — Vectors and Kinematics (5 sessions, ~5.5h)

> Corresponds to Kleppner Ch 1. **Core Question:** "How do we transcribe motion into space?"

| # | Title | Physical Meaning | 🔥 With Algebra Alone? (Trying Without Limits) | Kleppner | Time |
|:--:|------|-----------|------|:---:|:---:|
| 01 | **What Is a Vector** | $\vec{r} = (x, y, z)$ is "an arrow pointing from the origin to that point." The dot product measures shadow length; the cross product gives the perpendicular direction of the parallelogram. Vectors are necessary because **space has direction.** | Vector operations themselves are algebraic. But **the change-in-a-blink of a vector** ($d\vec{r}/dt$) begins in the next session. The goal here is to build the habit of "seeing position as an arrow, not just a pair of numbers." | Ch 1.1~1.4 | 60 min |
| 02 | **Position, Velocity, Acceleration as Vectors** | $\vec{v} = d\vec{r}/dt$: the arrow tangent to the trajectory. **Each axis is independent.** Horizontal throw: horizontal constant-velocity + vertical free-fall = unrelated to each other. | To find the **instantaneous velocity** of an object with $\vec{r}(t)=(t^2, t^3)$? At $t=2$, compute $\Delta \vec{r}/\Delta t$ with $\Delta t=1/10, 1/100, 1/1000$ → approaches $(4, 12)$ but **never exactly reaches it.** Only $\lim_{\Delta t\to 0}$ gives $(4,12)$. | Ch 1.5~1.7 | 70 min |
| 03 | **Free Fall and Projectile Motion** | $a_y=-g, a_x=0$. "Gravity only pulls downward, so horizontal velocity never changes." A parabola = the sum of two independent stories. | To get $x(t)$ starting from $a=-g$, you need **two rounds of split-and-gather.** Without it, "$v=gt$ so $x=\frac{1}{2}gt^2$" is just memorization — you cannot explain **why the $\frac{1}{2}$ appears.** All three constant-acceleration formulas are results of $\int a\,dt$. | Ch 1.7 | 60 min |
| 04 | **Curvilinear Motion — Tangential and Normal Acceleration** | $\vec{a} = \frac{dv}{dt}\hat{t} + \frac{v^2}{\rho}\hat{n}$. **Acceleration exists even without change in speed!** The cause is change in direction. | To derive $a_c=v^2/r$ for uniform circular motion **without limits?** Use similar triangles: $\Delta v/v \approx \Delta s/r$ → $a \approx v^2/r$. But this is an approximation! $v^2/r$ is exact only in the $\Delta t\to 0$ limit. | Ch 1.8~1.10 | 75 min |
| 05 | **Relativity of Motion** | $\vec{r} = \vec{r}\,' + \vec{V}t$. When the reference frame changes, velocities add and acceleration is invariant. Galilean transformation. | Position transformation is algebraic. But velocity transformation requires $\vec{v}=d\vec{r}/dt$, and acceleration $\vec{a}=d\vec{v}/dt$ introduces **change-in-a-blink.** Proving acceleration invariance requires $\frac{d}{dt}(\vec{v}\,'+\vec{V}) = \vec{a}\,' + 0$ — the linearity of the change-in-a-blink operation is essential. | Ch 1.11 | 50 min |

---

## Week 2: Causes of Motion — Newton's Laws and Free Body Diagrams (6 sessions, ~7h)

> Corresponds to Kleppner Ch 2~3. **Core Question:** "Why does motion happen? — And how do we predict it?"

| # | Title | Physical Meaning | 🔥 With Algebra Alone? | Kleppner | Time |
|:--:|------|-----------|------|:---:|:---:|
| 06 | **Newton's Three Laws** | 1st: defines inertial frames. 2nd: $\vec{F}=m\vec{a}$ — force determines acceleration. 3rd: interactions are always mutual. | In $\vec{F}=m\vec{a}$, $\vec{a}=d^2\vec{r}/dt^2$, so **this law itself is a rate-relationship equation.** Algebra alone stops at "knowing force gives acceleration." To reach position, split-and-gather is essential. | Ch 2.1~2.3 | 60 min |
| 07 | **Free Body Diagrams (FBD) 🔥** | FBD = "listening to the story the object hears." ① Isolate ② Contact forces ③ Action-at-a-distance forces ④ Coordinate axes ⑤ $\sum F_x=ma_x$, $\sum F_y=ma_y$. | The FBD itself is an algebraic tool. But the equations set up via FBD are **rate-relationship equations** ($\sum F_x = m\ddot{x}$). The FBD is the "blueprint" for setting up the rate-relationship equation; the moment you start solving it, splitting and gathering begins. Practice with inclined planes, pulleys, and connected objects. | Ch 2.4, 3.1~3.3 | 90 min |
| 08 | **Tension, Normal Force, Friction** | The physical origin of contact forces (intermolecular electromagnetic forces). Tension: along the string. Normal: perpendicular to surface. Friction: parallel to surface, opposing relative motion. Static friction $f_s \leq \mu_s N$ acts "only as much as needed." | The rules determining the magnitude of contact forces are algebraic empirical laws. Split-and-gather enters when predicting **how these forces change motion.** Example: even if $f_k=\mu_k N$ is constant, how this force changes velocity is $v(t)=v_0-\mu_k g t$ — the result of splitting and gathering. | Ch 3.4~3.5 | 70 min |
| 09 | **$F=ma$ Is a Rate-Relationship Equation** | $m\ddot{x}=F(t,x,v)$. "The force at this instant determines the motion at the very next instant." The universe is a rate-relationship equation progressing step by step. | **This entire session IS the necessity of limits itself.** Constant force → constant acceleration (two rounds of split-and-gather). $F=-kx$ → oscillation (rate-relationship equation). $F=-bv$ → decay (separation of variables). **The moment the force varies, algebra can do nothing.** | Ch 2.5, 3.6 | 60 min |
| 10 | **Position-Dependent Force — Springs** | $F=-kx$ → $m\ddot{x}=-kx$. The solution is $\sin,\cos$ because: take the change-in-a-blink twice and you get the negative of the original function. $x=A\cos(\omega t+\phi)$, $\omega=\sqrt{k/m}$. The most common motion in nature. | **Predicting spring motion without limits?** Approximations like "average force × time" cannot follow the actual sine-wave trajectory at all. **Without solving the rate-relationship equation, you will never know where the spring is at any moment.** | Ch 3.6, 11.1 | 75 min |
| 11 | **Velocity-Dependent Force — Drag** | $F=-bv$ → $m\dot{v}=-bv$. Solution: $v(t)=v_0 e^{-bt/m}$. Gravity + drag: $v(t)=v_t(1-e^{-bt/m})$, $v_t=mg/b$. | **Without limits:** "As $v$ decreases, the force decreases, so the deceleration decreases too..." — makes sense in words, but **you can never get the exact $v(t)$.** Even $v_t$ is just a guess without knowing $b$. Only separation of variables + split-and-gather gives $v(t)$ and $v_t$ exactly. | Ch 3.6 | 60 min |

---

## Week 3: Conservation Born from Split-and-Gather — Momentum and Energy (5 sessions, ~6h)

> Corresponds to Kleppner Ch 4~5. **Core Question:** "When you split-and-gather $F=ma$ through time or space, what 'remains unchanged'?"

| # | Title | Physical Meaning | 🔥 With Algebra Alone? | Kleppner | Time |
|:--:|------|-----------|------|:---:|:---:|
| 12 | **Impulse and Momentum** | $\int F\,dt = mv_2-mv_1$. "Impulse = change in momentum." The result of splitting and gathering $F=ma$ through time. | During the 0.001s a baseball bat contacts the ball, $F(t)$ surges to thousands of N then drops to zero. **Without knowing this $F(t)$, you know neither $a(t)$ nor $v(t)$.** But $\int F\,dt = \Delta p$ lets you know the velocity change from **just one gathered value.** How could you possibly get this with algebra alone? | Ch 4.1~4.3 | 60 min |
| 13 | **Conservation of Momentum** | $\vec{F}_{AB}=-\vec{F}_{BA}$ → $d\vec{p}_A/dt=-d\vec{p}_B/dt$ → $\vec{p}_A+\vec{p}_B=$ constant. The 3rd law, split and gathered through time. | Two objects collide: if you try to track each one with $F=ma$ at every instant? **You'd need the exact $F(t)$ during contact, which is practically impossible.** But momentum conservation uses the fact that the $\int F\,dt$ terms cancel each other — you get the result **without knowing the details of $F(t)$.** The power of split-and-gather. | Ch 4.4~4.6 | 70 min |
| 14 | **Work and Kinetic Energy** | $F\,dx=mv\,dv$ → $\int F\,dx=\frac{1}{2}mv_2^2-\frac{1}{2}mv_1^2$. $F=ma$ split and gathered through space. | Compressing a spring ($F=kx$) by 0.1m: use $W=Fd$? Which $F$ do you use? 0N at the start, $k\times 0.1$N at the end. Using the average gives $W \approx \frac{1}{2}k(0.1)^2$... **sheer luck!** If the spring followed $F=kx^2$, the average would never give the exact value. Only $\int F\,dx$ is correct. | Ch 5.1~5.3 | 65 min |
| 15 | **Potential Energy and Conservative Forces** | $F=-dU/dx$. "Force is the slope of the potential energy hill." With only conservative forces, $K+U=$ constant. | **Without limits:** Defining $U$ requires knowing that $\int F\,dx$ is path-independent. Gravity: $W=mgh$ (deceptively simple). For a general force, determining whether $U$ can be defined requires **splitting and gathering along the path.** $F=-dU/dx$ is change-in-a-blink itself. | Ch 5.4~5.6 | 75 min |
| 16 | **Energy Diagrams — Reading $U(x)$** | $E=K+U$. Motion is only possible where $U(x)\leq E$. Minima = stable equilibrium, maxima = unstable. **Grasp all qualitative features of motion without solving the rate-relationship equation.** | How was $U(x)$ obtained? From $F(x)$ via $U(x)=-\int F\,dx$. **Without split-and-gather, you cannot even draw $U(x)$.** But once you have $U(x)$, the rest is algebraic graph interpretation. — Limits are needed only at the accumulation step; beyond that lies the domain of intuition. | Ch 5.7 | 70 min |

---

## Week 4: Rotation and Synthesis — Angular Momentum, Rigid Bodies, Introduction to Oscillation (5 sessions, ~5.5h)

> Corresponds to Kleppner Ch 6~7 + Ch 11 preview. **Core Question:** "How closely does the world of rotation resemble the world of translation?"

| # | Title | Physical Meaning | 🔥 With Algebra Alone? | Kleppner | Time |
|:--:|------|-----------|------|:---:|:---:|
| 17 | **Angular Momentum and Torque** | $\vec{L}=\vec{r}\times\vec{p}$, $\vec{\tau}=d\vec{L}/dt$. "Torque is the rate of change of angular momentum." Central force $\Rightarrow \vec{L}$ conserved $\Rightarrow$ Kepler's 2nd Law. | Deriving $\vec{\tau}=d\vec{L}/dt$ requires the **change-in-a-blink of a cross product:** $d(\vec{r}\times\vec{p})/dt = \vec{v}\times\vec{p} + \vec{r}\times\vec{F} = 0 + \vec{r}\times\vec{F}$. Algebra alone cannot make this connection. Also, proving $\vec{L}$ conservation requires $\int\vec{\tau}\,dt=0$ — **the logic of split-and-gather.** | Ch 6.1~6.4 | 75 min |
| 18 | **Moment of Inertia and Rotational Motion** | $\tau=I\alpha$, $I=\int r^2 dm$. "Moment of inertia = mass of rotation." Parallel axis theorem. Center of mass $\vec{R}=\int\vec{r}dm/M$. | $I=\sum m_i r_i^2$ only works for point particles. **To find $I$ exactly for a continuous body (rod, disk, sphere), split-and-gather is essential.** Can you find a rod's moment of inertia $ML^2/12$ without $I=\int r^2 dm$? 10-segment approximation: $0.0825ML^2$, 100-segment: $0.08325ML^2$... **never reaching** $1/12=0.08333...$ | Ch 7.1~7.4 | 70 min |
| 19 | **The Physical Meaning of Simple Harmonic Motion** | $m\ddot{x}+kx=0$ → $x=A\cos(\omega t+\phi)$. Every stable equilibrium point is approximated by SHM — because **$U$ is approximated by its quadratic term.** | Understanding why SHM is "the most common motion in nature" requires both **Taylor expansion** ($U(x)\approx U(x_0)+\frac{1}{2}U''(x_0)(x-x_0)^2$) and the **rate-relationship equation.** Algebra alone can never explain "why $\sin,\cos$?" | Ch 11.1~11.3 | 65 min |
| 20 | **Damped Oscillation and Resonance** | $m\ddot{x}+b\dot{x}+kx=0$ → under/over/critical damping. External driving + matching natural frequency → explosive resonance. | Can you obtain the complete solution to $m\ddot{x}+b\dot{x}+kx=F_0\cos(\omega t)$ with algebra? **Impossible.** Separation of variables, characteristic equations, and the method of undetermined coefficients are all built on splitting and gathering. Without this, **you cannot explain mathematically why bridges collapse.** | Ch 11.4~11.6 | 70 min |
| 21 | **Synthesis — One Motion, Three Languages** | Translate the same situation through ① $F=ma$ ② Energy ③ Momentum/Angular Momentum — three perspectives. Training to choose the language depending on what the problem asks. | **The core of this session:** Review all the "algebra-alone failure scenes" learned so far. Meta-summary of **which split-and-gather gave birth to each language** (time-splitting $F=ma$ → momentum, space-splitting → energy). **"All conservation laws are the offspring of split-and-gather."** | — | 90 min |

---

## The Identity of This Curriculum

```
What someone who already knows computation uniquely lacks:
→ Physical intuition for "Why does this problem need limits (splitting and gathering)?"

Every session of Phase 0 repeats one pattern:
1. Nature changes ceaselessly (velocity, force, pressure, density...).
2. Handling changing quantities with algebra yields only approximations.
3. To reach the exact value, infinite subdivision (limits) is mandatory.
4. That limit is precisely split-and-gather, and split-and-gather gives birth to conservation laws.

Repeat this pattern 21 times, and
splitting-and-gathering is no longer a "calculation tool" — it becomes "the language nature speaks."
Open Kleppner in that state, and every equation reads as obvious.
```

