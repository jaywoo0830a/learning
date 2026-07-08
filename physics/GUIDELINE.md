# Physics Session Authoring Guideline v2

> **v2:** English edition. Assumes fluency in single-variable calculus and basic ODEs (separation of variables, integrating factors, characteristic equations, $n$th-order linear ODEs with constant coefficients). Sessions focus on **physical reasoning and modeling**, not calculus technique.
> **Core premise:** Classical mechanics is the discipline of *deriving models with calculus → justifying them logically → modeling real-world scenarios → computing numerical predictions*. Every session follows this flow.

---

## 1. Core Principle: Derive → Justify → Model → Compute

```text
[Calculus Derivation] → [Logical Justification] → [Real-World Modeling] → [Numerical Computation]
        35%                      20%                        25%                      20%
```

### 1-1. Calculus Derivation (35%)

Every formula is **built from definitions using calculus**. Nothing is memorized — everything is constructed.

```
"Where do we start?" → Definition (position, velocity, acceleration, force, work, momentum...)
"What operation do we apply?" → Differentiation / integration / limit
"Where do we arrive?" → Equation of motion, conservation law, predicted value
```

| Don't | Do |
|:---|------|
| "$\mathbf{F}=m\mathbf{a}$." | "Force is the rate of change of momentum: $\frac{d\mathbf{p}}{dt}=\mathbf{F}$. For constant mass, $\frac{d}{dt}(m\mathbf{v})=m\frac{d\mathbf{v}}{dt}=m\mathbf{a}=\mathbf{F}$." |
| "The kinematic formula: $v=v_0+at$." | "When $\mathbf{a}$ is constant, integrate $\frac{d\mathbf{v}}{dt}=\mathbf{a}$: $\int_{v_0}^v d\mathbf{v} = \int_0^t \mathbf{a}\,dt$, giving $v-v_0=at$." |
| "Kinetic energy is $\frac{1}{2}mv^2$." | "Insert $\mathbf{F}=m\frac{d\mathbf{v}}{dt}$ and $d\mathbf{r}=\mathbf{v}\,dt$ into the work integral: $\int \mathbf{F}\cdot d\mathbf{r} = \int m\frac{d\mathbf{v}}{dt}\cdot\mathbf{v}\,dt = \int m\mathbf{v}\cdot d\mathbf{v} = \frac{1}{2}mv^2\big|_{v_1}^{v_2}$." |

**Rules:**
- State the starting point (definition) first.
- Name the calculus operation explicitly: *differentiate*, *integrate*, *take the limit*, *separate variables*.
- Append a one-liner explaining *why* this operation at each step.

### 1-2. Logical Justification (20%)

After deriving, verify **why the derivation is logically sound**.

```
"What assumptions were made?" → Constant mass? Inertial frame? Conservative force? Point particle?
"What breaks if an assumption is violated?" → Which term is no longer zero?
"How do symmetries connect to conservation laws?" → Translational symmetry → momentum conservation, rotational symmetry → angular momentum conservation...
```

| Check | Example Question |
|:---|------|
| Assumption audit | "If mass varies, we must use $\mathbf{F}=\dot{\mathbf{p}}$, not $\mathbf{F}=m\mathbf{a}$. Why?" |
| Classical limit | "Does the relativistic kinetic energy $\gamma mc^2-mc^2$ reduce to $\frac{1}{2}mv^2$ when $v \ll c$?" |
| Dimensional check | "Do both sides share the same dimensions? $[E]=\mathrm{ML^2T^{-2}}$?" |
| Special-case check | "Does this reduce to uniform rectilinear motion when $\mathbf{F}=0$?" |

### 1-3. Real-World Modeling (25%)

Apply the derived equations to **concrete physical situations**.

```
"What real scenario are we modeling?" → Projectile motion, pendulum, planetary orbit, collision...
"What forces act?" → Gravity, tension, normal force, friction, spring force, centripetal...
"What coordinate system?" → Cartesian, polar, cylindrical...
"What are the initial/boundary conditions?" → Position, velocity at $t=0$...
```

Modeling always follows this sequence:

1. **Draw the diagram** — force arrows, coordinate axes, initial positions on paper.
2. **Decompose forces** — component by component: $\sum F_x = \ldots$, $\sum F_y = \ldots$
3. **Write the equations of motion** — each component of $\sum\mathbf{F}=m\mathbf{a}$.
4. **Solve the differential equation** — integrate, separate variables, characteristic equation, etc.
5. **Apply initial conditions** — determine integration constants.
6. **Compute the desired quantity** — time of flight, max height, impact velocity, etc.

### 1-4. Numerical Computation (20%)

Plug **actual numbers** into the model and compute predictions.

```
"What numbers go where?"
"Are units consistent?" → Convert everything to SI.
"Is the result physically sensible?" → Negative mass? Faster than light? Order-of-magnitude sanity check.
```

---

## 2. Linguistic Clarity Principles

### 2-1. Sentence Structure: Start → Operate → Arrive

Every derivation sentence follows this order:

```text
[Start from what] → [Apply what operation] → [Obtain what result]
```

| Bad | Good |
|------|------|
| "Acceleration is the derivative of velocity." | "Differentiate velocity $\mathbf{v}$ with respect to $t$. The result is acceleration $\mathbf{a}$." |
| "Kinetic energy is the path integral of force." | "Insert $\mathbf{F}=m\dot{\mathbf{v}}$ into the work definition $\int\mathbf{F}\cdot d\mathbf{r}$. Integrate. The result is $\frac{1}{2}mv^2$." |
| "Newton's law of gravitation: $F=GMm/r^2$." | "Measure the distance $r$ between masses $M$ and $m$. Divide by $r^2$, multiply by $GMm$. That gives the gravitational force magnitude." |

### 2-2. Referring to Physical Quantities: "Where on the page, what it means"

Pair abstract symbols with their **spatial location** and **physical meaning**.

| Bad | Good |
|------|------|
| "$\mathbf{r}(t)$" | "The position vector of the particle at time $t$" |
| "$\dot{\mathbf{r}}$" | "Differentiate position with respect to time — that's velocity" |
| "$\ddot{\mathbf{r}}$" | "Differentiate velocity again — that's acceleration" |
| "$m\ddot{x} + b\dot{x} + kx = 0$" | "mass $\times$ acceleration + damping $\times$ velocity + stiffness $\times$ position = 0. Left to right: inertial term, dissipative term, restoring term." |

### 2-3. Lexical Consistency: One Operation = One Word

| Operation | Use this word only | Avoid |
|:---:|:---:|------|
| $\frac{d}{dt}$ | "differentiate" | "take the derivative", "compute the rate of change" |
| $\int dt$ | "integrate" | "find the antiderivative", "take the integral" |
| $\lim_{\Delta t\to0}$ | "take the limit" | "let it go to zero", "infinitesimal" |
| Separate variables | "separate" | — |
| Apply initial conditions | "plug in $t=0$" | "apply the initial conditions" |
| Set up coordinates | "draw axes" | "establish a coordinate system" |
| Decompose forces | "split" the force | "resolve into components" |
| Approximate | "drop" (the negligible term) | "approximate", "neglect" |

### 2-4. Always Visualize the Calculus

```text
"Integrate velocity from t=0 to t. The area under the v-t curve is displacement."
"If acceleration is constant, the v-t graph is a straight line — the area is a trapezoid."
```

---

## 3. Cognitive Science Principles

### 3-1. 3-Unit Chunking

Working memory holds 3–5 items. **Every procedure is 3 steps.**

| Bad (5 steps) | Good (3 steps) |
|:---|------|
| ① Draw forces ② Decompose ③ Write EOM ④ Integrate ⑤ Apply ICs | **[1]** Draw forces & write equation of motion **[2]** Solve the ODE **[3]** Plug in initial conditions & compute |

### 3-2. Prediction Error Encoding — "Common Mistake" Corner

The brain encodes prediction-error most strongly (Friston).

1. **Show the wrong approach first** — "Many people do this: $\int v\,dt = vt$ (treating $v$ as constant)."
2. **One-line reason it's wrong** — "But when $v$ depends on $t$, you can't pull it outside the integral."
3. **Then show the correct approach.**

### 3-3. Motor Language — "Let the Hand Remember"

| Abstract Verb | → Motor Verb |
|:---|------|
| "Set up coordinates" | "**Dot** the origin. **Draw** the axes." |
| "Decompose the force" | "**Tear** the arrow into $x$ and $y$ pieces." |
| "Integrate" | "**Add up** the area under the graph." |
| "Cancel terms" | "**Strike out** matching terms on both sides." |
| "Approximate" | "**Drop** the tiny term." |
| "Apply initial conditions" | "**Shove** $t=0$ into the general solution." |

### 3-4. Generation Effect — Constructed-Response Problems

At least 2 exercises per session must be **constructed-response**, not template-application.

| Template Application | Constructed-Response |
|:---|------|
| "Given $v_0=10\,\text{m/s}$, $a=2\,\text{m/s}^2$, find displacement after $5\,\text{s}$." | "Choose your own $v_0$ and $a$. Draw the v-t graph for a 5-second interval and compute the displacement. Verify that your result matches the kinematic formula." |
| "A spring-mass system has $k$ and $m$. Find the period." | "Derive the equation of motion for a mass on a spring. Compute the angular range where $\sin\theta\approx\theta$ holds to within 1%, and estimate when the small-angle approximation breaks." |

### 3-5. Processing Fluency + Primacy/Recency

- Repeat the same rhythm: "Do ___. The result is ___."
- Keep sentences under 20 words.
- Put the most critical derivation step **first**.
- End every session with a "Derivation Chain" card — imprinting the core twice.

### 3-6. Curse of Knowledge Prevention

- [ ] Ban "obviously", "clearly", "trivially".
- [ ] Never omit the integration constant — always write $+C$, then determine it from initial conditions.
- [ ] Never skip intermediate steps.
- [ ] One operation per sentence.

---

## 4. Session Structure

| Section | Weight | Content |
|:----:|:----:|------|
| **Opening** | — | *"The problem we'll solve today"* — a concrete scenario. *"How do we predict the outcome?"* |
| **Derivation** | 35% | Definition → calculus → equation of motion / conservation law. Every intermediate step exposed. |
| **Logic Check** | 20% | Verify assumptions, limits, dimensions, special cases. |
| **Common Mistake** | incl. | Wrong approach → why → correct approach (§3-2) |
| **Modeling** | 25% | Concrete scenario → force diagram → coordinate axes → equations → solution → numerical result |
| **Exercises** | 20% | 5–6 problems. At least 2 constructed-response (§3-4). Final problem labeled **"Combat"** (hardest). |
| **Derivation Chain** | card | 3–4 steps summarizing the session's core derivation. |

---

## 5. Solution Separation

Solutions live in `solutions/0X-solutions.md`. The session file contains only a link:

```markdown
> Solutions: [Solution set](solutions/01-solutions.md#exercise-1)
```

---

## 6. Exercise Layout

| # | Type |
|:---:|------|
| 1–2 | Direct application — plug numbers into the derived formula |
| 3–4 | Variation + trap — bait a common mistake; at least 1 constructed-response |
| 5 | Synthesis — connect with earlier concepts |
| 6 | **Combat** — novel scenario, model and compute from scratch |

---

## 7. Modeling Checklist (Repeated in Every Session)

Whenever you encounter a new physical situation, execute these 6 steps:

```text
[1] Diagram: Draw the object, force arrows, coordinate axes on paper.
[2] Force Decomposition: Split each force into x- and y-components. ∑F_x, ∑F_y.
[3] Equation of Motion: Plug into ∑F = ma. A differential equation emerges.
[4] Solve: Integrate. Separate variables. Solve the characteristic equation.
[5] Initial Conditions: Determine integration constants.
[6] Compute: Calculate the desired quantity. Verify units. Verify dimensions.
```

---

## 8. Master Derivation Chain — The Full Map of Classical Mechanics

One grand logical chain runs through this entire book. Every session is a link.

```text
Position r(t)  ──[differentiate]──▶  Velocity v = dr/dt  ──[differentiate]──▶  Acceleration a = dv/dt = d²r/dt²
                                                                                        │
                                                         Newton's Laws:  F = dp/dt = ma
                                                                                        │
                                         ┌──[integrate dt]──▶  Impulse-Momentum:  Δp = ∫F dt
                                         │
                                         └──[integrate dr]──▶  Work-Energy:  W = ∫F·dr  →  T = ½mv²
                                                                                        │
                                              Conservative Field → Potential Energy U → Mechanical Energy Conservation: T + U = const
                                                                                        │
                                              Constraints + Coordinate Transformations → Lagrangian & Hamiltonian formalisms
                                                                                        │
                                              Special Relativity: c → ∞ limit recovers classical mechanics
```

This chain reappears across every session. First consciously, eventually unconsciously.

---

## 9. Time Allocation Principles

| Complexity | Criterion | Time |
|:---:|------|:---:|
| Simple | 1–2 derivation steps, 1 modeling scenario | **30–45 min** |
| Moderate | 3–4 derivation steps, 2–3 modeling scenarios | **60–90 min** |
| Complex | Multi-step derivation + multiple models + synthesis with earlier topics | **90–150 min** |

---

## 10. Prerequisites (Assumed, Not Taught)

The reader is assumed to already command:

| Skill | Expected Fluency |
|:---|------|
| Single-variable differentiation | Product rule, quotient rule, chain rule — automatic |
| Single-variable integration | $u$-substitution, integration by parts, partial fractions, trig substitution |
| Limits | $\varepsilon$-$\delta$ intuition, L'Hôpital's rule, standard limits ($\frac{\sin x}{x}\to1$, $(1+\frac{1}{n})^n\to e$) |
| ODEs — first order | Separation of variables, integrating factors, homogeneous, exact equations |
| ODEs — second order linear | Characteristic equation, undetermined coefficients, variation of parameters |
| Taylor series | Maclaurin series of $e^x$, $\sin x$, $\cos x$, $\ln(1+x)$, $(1+x)^\alpha$; order-of-magnitude estimation |
| Vector algebra | Dot product, cross product, unit vectors, component decomposition |
| Basic complex numbers | $e^{i\theta}=\cos\theta+i\sin\theta$, complex exponential form |

**Sessions never re-teach these.** When an integration step is needed, the session says "integrate (by parts)" and moves on. The focus is on *why* this integral appears in the physics and *what* the result means.

---

> **The soul of this guideline:** Physical intuition is not a gift — it's the residue of derivations you've done with your own hands. Every session is designed so you pick up the pen, differentiate, integrate, and follow along. No spectator learning.
