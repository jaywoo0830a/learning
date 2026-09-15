# Session 19A: ODE Modeling — Translating Nature into Equations

**Phase 2 — Classical Techniques | 65 min**

*Prerequisites: 15B (related rates), 10B (exponential growth/decay), 16A (FTC)*

> 💡 **Stuck?** Every problem has a collapsible **Hint** below it — click it only when you need a nudge.

> **Source.** Every example and drill below is drawn from Stewart, *Calculus*, Chapter 9 (Sections 9.1–9.2). Each item cites its section and exercise number.

---

## Part A: What Is a Differential Equation?

---

## Example 1: Definition and Vocabulary (§9.1)

An **ordinary differential equation (ODE)** is an equation whose unknown is a *function*, and which involves that function's derivatives. Instead of "find the number $x$", the question is **"find the function $y(t)$ whose rate of change behaves in a specified way."**

**Why they matter**: Nature rarely hands you a quantity — it hands you a *rate rule*. A population grows proportionally to itself; a hot object cools proportionally to the temperature gap; a tank's salt changes as inflow minus outflow. Each "how fast" statement is a differential equation, and *solving* it converts the rate-rule into the quantity itself.

**Notation**:
- $y' = \frac{dy}{dx}$ — first derivative (rate of change).
- $y'' = \frac{d^2y}{dx^2}$ — second derivative (acceleration / curvature).
- An equation may mix $y$, $y'$, $y''$, ... and the independent variable.

**Order** = the highest derivative that appears:
- $\frac{dy}{dx} = ky$ — **1st order** (only $y'$).
- $y'' + y = 0$ — **2nd order** (contains $y''$).

**What "solving" means**: a **solution** is a *function* that makes the equation true for every input in its domain. Checking a candidate answer is purely mechanical: substitute and verify.

**Worked check** (§9.1 Ex 1–6 style) — is $y = 3e^{2x}$ a solution of $y' = 2y$?

① Differentiate: $y' = 3\cdot2e^{2x} = 6e^{2x}$.
② Right side: $2y = 2\cdot3e^{2x} = 6e^{2x}$.
③ Both sides match for every $x$ → **yes**, $y = 3e^{2x}$ is a solution.

**General vs particular**:
- **General solution** — contains arbitrary constants (one per order): $y = Ce^{kt}$ works for *any* $C$ in $y' = ky$.
- **Particular solution** — the constants are fixed by an **initial condition** such as $y(0) = y_0$: here $C = y_0$, giving $y = y_0e^{kt}$.

**Method — Verify a proposed solution in 3 steps:**

(1) **Differentiate** the candidate to produce every derivative appearing in the ODE.
(2) **Substitute** the candidate and its derivatives into the equation.
(3) **Simplify** and check that both sides are identical for all inputs.


---

## Part B: Seeing Solutions Before Solving

---

## Example 2: Direction (Slope) Fields (§9.2)

For $\frac{dy}{dx} = f(x,y)$, draw a short line segment with slope $f(x,y)$ at each grid point $(x,y)$. **Solution curves follow the field.**

$y' = x+y$: the slope field shows curves that look like $-x-1+Ce^x$.

**Verify**: $y = -x-1+Ce^x$ → $y' = -1+Ce^x$. Right side: $x + y = x + (-x-1+Ce^x) = -1+Ce^x$. ✓

**How to read the field**: at each grid point, draw a short segment with slope $f(x,y)$ — where the segments are steep the solution is changing fast, where they are flat ($f=0$) the solution is momentarily constant, and curves follow the stream of segments like a river follows its current.

**Slope field for $y' = y - 2x$** (§9.2 #11): pass through $(1,0)$. The field shows curves that rise for large $y$, fall for large $x$. The solution through $(1,0)$ follows the flow.

![Slope field with solution curves]({{graph:19a-1-slope-field}})

*Graph 19A-1: Slope field for $y' = x+y$. Short line segments show the slope at each grid point. Solution curves (colored) follow the flow of the field like a river.*

---

## Part C: The Exponential Model — Growth and Decay

---

## Example 3: The Population Growth Model (§9.1)

**Setup**: the rate of change is proportional to the amount itself. A population $P(t)$ grows at a rate proportional to its size:

$$\frac{dP}{dt} = kP \tag{1}$$

where $k$ is the proportionality constant. If $k>0$, the population increases; if $k<0$, it decreases. As $P(t)$ increases, $dP/dt$ becomes larger — the growth rate itself accelerates.

**Solve by separation of variables** (§9.3, 🔗 16A):

① Separate: $\frac{dP}{dt} = kP$ → $\frac{dP}{P} = k\,dt$ (valid for $P \neq 0$).
② Integrate both sides (FTC): $\int\frac{dP}{P} = \int k\,dt$ → $\ln|P| = kt + C$.
③ Exponentiate: $|P| = e^{kt+C} = e^{C}e^{kt}$. Absorb the sign into the constant: $P = Ae^{kt}$.

With $P(0) = P_0$: $A = P_0$, so

$$P(t) = P_0 e^{kt}. \tag{2}$$

**Significance of $A$** (§9.1): $P(0) = Ae^{k\cdot 0} = A$, so $A$ is the initial population. The **relative growth rate** $\frac{dP/dt}{P} = k$ is constant — a population with constant relative growth rate must grow exponentially.

$k>0$: exponential growth (population, compound interest). $k<0$: exponential decay (radiation, cooling).

**Doubling time**: $t_2 = \frac{\ln 2}{k}$. **Half-life**: $t_{1/2} = \frac{\ln 2}{|k|}$.

![Exponential growth and decay]({{graph:19a-2-growth-decay}})

*Graph 19A-2: Families of exponential solutions $P = Ae^{kt}$. Left — growth ($k>0$): curves rise, doubling time $t_2 = \ln 2/k$ is the same horizontal distance for all curves. Right — decay ($k<0$): curves fall toward zero, half-life $t_{1/2} = \ln 2/|k|$.*

Bacteria double every 3 hours. $k = \frac{\ln 2}{3} \approx 0.231$. From 1000: $P(t)=1000e^{0.231t}$.

**Method — Building a model in 3 steps:**

(1) **Name the quantity.** Decide what function $y(t)$ you are tracking (population, temperature, amount, current...).
(2) **Write its rate of change.** Either a proportionality law ($y' = ky$) or a balance law: $\frac{dy}{dt} = \text{rate in} - \text{rate out}$.
(3) **Attach the initial condition** $y(0) = y_0$, then solve and interpret (doubling time, steady state, etc.).

> This 3-step loop is the whole session. Every example below is just a different "rate in / rate out" or "proportional to" story.

---

## Example 4: Continuous Compound Interest (§9.1)

This is Example 3 with a new name: the balance changes proportionally to itself.

$\frac{dA}{dt} = rA$ → $A(t) = Pe^{rt}$. With $P = \$1000$ at 5% continuous for 10 years:

$$A = 1000e^{0.05\cdot10} = 1000e^{0.5} \approx \$1648.72.$$

**Compare with yearly compounding** (🔗 12B1): $1000(1.05)^{10} \approx \$1628.89$. Continuous pays more because interest earns interest *every instant* — the bridge is $r = e^k$ (Example 10).

---

## Part D: Linear "Approach" Models — Steady State

---

## Example 5: Newton's Law of Cooling (§9.1)

**Setup** (§9.1): a hot object cools proportionally to the temperature gap between it and the room.

$$\frac{dT}{dt} = -k(T - T_{\text{env}}).$$

**Solve by substitution** — reduce to Example 3:

① Let $u = T - T_{\text{env}}$ (the "excess temperature"). Since $T_{\text{env}}$ is constant, $u' = T'$.
② The ODE becomes $u' = -ku$, so by Example 3: $u = Ce^{-kt}$.
③ Back-substitute: $T(t) = T_{\text{env}} + (T_0 - T_{\text{env}})e^{-kt}$.

$$T(t) = T_{\text{env}} + (T_0 - T_{\text{env}})e^{-kt}.$$

**Worked example** (§9.1 style) — Coffee at 90°C in a 20°C room; after 5 min it is 60°C. Find $k$:

① Plug in: $60 = 20 + (90-20)e^{-5k} = 20 + 70e^{-5k}$.
② Isolate: $40 = 70e^{-5k}$ → $e^{-5k} = \frac{4}{7}$.
③ Solve: $k = -\frac{1}{5}\ln\frac{4}{7} = \frac{1}{5}\ln\frac{7}{4} \approx 0.112\;\text{min}^{-1}$.

After 15 min: $T(15) = 20 + 70e^{-15k} = 20 + 70\left(\frac{4}{7}\right)^3 \approx 20 + 70(0.187) \approx 33.1°\text{C}$.

**Long-term**: $T \to T_{\text{env}} = 20°\text{C}$ (the room always wins).

---

## Example 6: Mixing — Salt in a Tank (§9.1, §9.3)

**Setup** (§9.3 Ex 13–16 style): A tank holds 200 L of brine with 30 g of salt. Pure water enters at 5 L/min; the well-stirred mixture drains at 5 L/min (constant volume).

Let $A(t)$ = grams of salt at time $t$.

**Build the ODE** (3-step method):
- Rate in = $0$ (pure water).
- Rate out = $\frac{A(t)}{200}\times 5 = \frac{A}{40}$ g/min (concentration × flow rate).

$$\frac{dA}{dt} = 0 - \frac{A}{40} = -\frac{A}{40}, \quad A(0) = 30.$$

This is $y' = -by$ from Example 3! Solution: $A(t) = 30e^{-t/40}$.

After 1 hour ($t = 60$): $A(60) = 30e^{-60/40} = 30e^{-1.5} \approx 6.7$ g.

**If inflow has salt**: suppose 0.5 g/L enters at 5 L/min. Then rate in = $0.5\times5 = 2.5$ g/min:

$$\frac{dA}{dt} = 2.5 - \frac{A}{40}.$$

This is the **approach model** $y' = a - by$. Steady state: $A_{ss} = \frac{2.5}{1/40} = 100$ g. Solution: $A(t) = 100 + (30-100)e^{-t/40} = 100 - 70e^{-t/40}$. As $t\to\infty$, $A\to 100$ g.

---

## Part E: Nonlinear Models — Logistic Growth

---

## Example 7: The Logistic Equation (§9.1, §9.4)

**Setup** (§9.4): Exponential growth can't continue forever — resources are limited. If $P(t)$ is the population and $L$ is the **carrying capacity**, the logistic model is:

$$\frac{dP}{dt} = kP\left(1 - \frac{P}{L}\right).$$

- When $P \ll L$: $\frac{dP}{dt} \approx kP$ (exponential growth).
- When $P = L$: $\frac{dP}{dt} = 0$ (equilibrium — the population stabilizes).
- When $P > L$: $\frac{dP}{dt} < 0$ (population decreases back toward $L$).

**Solution** (separable, full derivation in 19B §9.3):

$$P(t) = \frac{L}{1 + Ae^{-kt}}, \quad A = \frac{L - P_0}{P_0}.$$

This is an **S-shaped (sigmoid) curve**. The **inflection point** (fastest growth) occurs at $P = L/2$.

![Logistic growth curve]({{graph:19a-3-logistic}})

*Graph 19A-3: Logistic growth $P(t) = L/(1+Ae^{-kt})$ with $L=1000$, $P_0=100$. The S-curve starts near exponential (dashed red), then levels off at $L$. The inflection at $P=L/2=500$ (dot) is where growth is fastest.*

**Worked example**: $L = 1000$, $P_0 = 100$, $k = 0.3$. Then $A = \frac{1000-100}{100} = 9$, and $P(t) = \frac{1000}{1+9e^{-0.3t}}$. Inflection when $P=500$: $1+9e^{-0.3t}=2$ → $t = \frac{\ln 9}{0.3} \approx 7.3$.

**Harvesting** (§9.4 Ex 19–20): if a constant rate $H$ is removed, $\frac{dP}{dt} = kP(1-P/L) - H$. This can create new equilibria or drive the population to extinction if $H$ is too large.

---

## Part F: Qualitative Analysis — Phase Lines

---

## Example 8: Autonomous Equations and the Phase Line

For $y' = f(y)$ (no explicit $x$ on the right), the slope depends only on $y$. **Equilibrium solutions** occur where $f(y) = 0$.

**The phase line** (1D stability diagram):
1. Mark equilibria on a $y$-number line.
2. In each interval, test the sign of $f(y)$ → draw arrows ($\uparrow$ if $f>0$, $\downarrow$ if $f<0$).
3. **Stable (sink)**: arrows point *toward* the equilibrium — nearby solutions converge.
4. **Unstable (source)**: arrows point *away* — nearby solutions diverge.

**Example**: $y' = y(1-y)$ (§9.4 logistic without carrying capacity notation). Equilibria at $y=0$ and $y=1$.

- $y < 0$: $f(y) = y(1-y) < 0$ → $\downarrow$.
- $0 < y < 1$: $f(y) > 0$ → $\uparrow$ (toward 1).
- $y > 1$: $f(y) < 0$ → $\downarrow$ (toward 1).

So $y=0$ is **unstable** (source) and $y=1$ is **stable** (sink).

![Phase line for autonomous ODE]({{graph:19a-4-phase-line}})

*Graph 19A-4: Phase line for $y' = y(1-y)$. Left — the slope field: solution curves rise toward $y=1$ from below, fall toward $y=1$ from above. Right — the phase line: $y=0$ is a source (arrows out), $y=1$ is a sink (arrows in).*

**For the logistic equation** $P' = kP(1-P/L)$: $P=0$ (unstable) and $P=L$ (stable). Every positive initial population approaches $L$.

---

## Example 9: Multiple Equilibria — When Stability Gets Interesting (§9.4)

$y' = y(1-y)(y-2)$: equilibria at $y=0, 1, 2$.

Test signs in each interval:
- $y<0$: $(-)(+)(-) = +$ → $\uparrow$
- $0<y<1$: $(+)(+)(-) = -$ → $\downarrow$
- $1<y<2$: $(+)(-)(-) = +$ → $\uparrow$
- $y>2$: $(+)(-)(+) = -$ → $\downarrow$

Stability: $y=0$ **stable** (sink), $y=1$ **unstable** (source), $y=2$ **stable** (sink). Two basins of attraction!

---

## Part G: Bridges — Discrete ↔ Continuous, Circuits, Draining

---

## Example 10: Discrete vs Continuous Growth (🔗 12B1)

| | Discrete (12B1) | Continuous (19A) |
|:---|:---|:---|
| Growth rule | $a_{n+1} = r a_n$ | $y' = ky$ |
| Solution | $a_n = a_0 r^n$ | $y(t) = y_0 e^{kt}$ |
| Doubling | $n_2 = \frac{\ln 2}{\ln r}$ steps | $t_2 = \frac{\ln 2}{k}$ |
| Relation | $r = e^k$, $k = \ln r$ | — |

**Example**: 5% annual interest
- **Discrete** (compounded yearly): $a_n = a_0 (1.05)^n$. After 10 years: $a_0 \times 1.05^{10} \approx 1.629a_0$.
- **Continuous**: $k = \ln(1.05) \approx 0.04879$, $y(t) = a_0 e^{0.04879t}$. After 10 years: $a_0 e^{0.4879} \approx 1.629a_0$.

**Same result** — same mathematics, different formulations.

> **🔗 12B1 Connection**: The infinite geometric series $S_\infty = \frac{a_1}{1-r}$ converges when $|r|<1$. The continuous analogue: $\int_0^\infty y_0 e^{-kt}\,dt = \frac{y_0}{k}$ converges when $k>0$ (decay). The bridge $r = e^k$ makes these equivalent.

---

## Example 11: Torricelli's Law — Draining Tank

A tank with cross-sectional area $A(y)$ at height $y$ drains through a hole of area $a$ at the bottom.

**Torricelli's law**: $\frac{dV}{dt} = -a\sqrt{2gy}$ (velocity of efflux = $\sqrt{2gy}$ from energy conservation).

For a cylindrical tank of radius $R$: $V = \pi R^2 y$, so $\pi R^2 \frac{dy}{dt} = -a\sqrt{2g}\sqrt{y}$.

Separable: $\frac{dy}{\sqrt{y}} = -\frac{a\sqrt{2g}}{\pi R^2}\,dt$. Integrate: $2\sqrt{y} = -\frac{a\sqrt{2g}}{\pi R^2}t + C$.

If $y(0)=H$: $\sqrt{y} = \sqrt{H} - \frac{a\sqrt{2g}}{2\pi R^2}t$.

**Drain time**: set $y=0$ → $T = \frac{2\pi R^2\sqrt{H}}{a\sqrt{2g}}$.

**Numeric example** (A11): $R = 0.5$ m, $H = 2$ m, hole $a = 2\,\text{cm}^2 = 2\times10^{-4}\,\text{m}^2$, $g = 9.8$:

$T = \frac{2\pi(0.5)^2\sqrt{2}}{(2\times10^{-4})\sqrt{2(9.8)}} \approx \frac{2.2213}{8.854\times10^{-4}} \approx 2509$ s $\approx 42$ min.

**Units sanity check**: $\frac{\text{m}^2\cdot\sqrt{\text{m}}}{\text{m}^2\cdot\sqrt{\text{m}/\text{s}^2}} = \frac{\text{m}^{5/2}}{\text{m}^{5/2}/\text{s}} = \text{s}$ ✓ — the formula outputs time when everything is in SI.

---

## Example 12: RL Circuit — The Electrical Cousin (§9.3 Ex 4)

An RL circuit has a resistor $R$ and inductor $L$ in series with a voltage source $E(t)$. Kirchhoff's voltage law:

$$L\frac{dI}{dt} + RI = E(t) \quad\Longleftrightarrow\quad \frac{dI}{dt} = \frac{E(t) - RI}{L}.$$

**Worked example** (§9.3 Ex 4): $R = 12\,\Omega$, $L = 4$ H, $E = 60$ V (constant), $I(0)=0$.

$$4\frac{dI}{dt} + 12I = 60 \quad\Longrightarrow\quad \frac{dI}{dt} = 15 - 3I.$$

This is the approach model $y' = a - by$ with $a=15$, $b=3$. Steady state: $I_{ss} = 15/3 = 5$ A.

Solution: $I(t) = 5(1 - e^{-3t})$.

- **Steady state**: $I \to \frac{E}{R} = 5$ A (the inductor becomes a plain wire).
- **Time constant**: $\tau = \frac{L}{R} = \frac{4}{12} = \frac{1}{3}$ s — the time to reach $1 - e^{-1} \approx 63.2\%$ of steady state.

![RL circuit current approaching steady state]({{graph:19a-5-rl-circuit}})

*Graph 19A-5: Current $I(t) = 5(1-e^{-3t})$ rises to the steady state $5$ A. The dashed line marks the time constant $\tau = L/R = 1/3$ s, where the current reaches $63.2\%$ of its final value.*

> **Geometric insight**: Newton's cooling, the mixing tank, and the RL circuit are all the **same** linear model $y' = a - by$: $y$ starts at some value and runs exponentially toward a steady state $a/b$. One formula, three physical settings — temperature, salt, current.

---

## What We Just Did

```
(1) ODE = equation linking a function to its derivatives. Order = highest derivative.
    General solution has constants; particular solution fits initial conditions.

(2) Slope field = direction field: draw slope f(x,y) at grid points; solution curves follow.

(3) Exponential model y' = ky → y = Ce^{kt}. k>0 growth, k<0 decay.
    Doubling time t₂ = ln2/k. Half-life t½ = ln2/|k|.

(4) Linear "approach" models y' = a − by: Newton cooling (T → Tenv), mixing (A → steady),
    RL circuit (i → E/R). Same shape: Ce^{−bt} + steady state.

(5) Logistic y' = ky(1−y/L) → L/(1+Ae^{−kt}). S-curve, inflection at P = L/2.

(6) Phase line (autonomous y'=f(y)): equilibria f(y)=0; sign of f gives direction;
    stable = sink (arrows in), unstable = source (arrows out).

(7) Discrete ↔ continuous: a_{n+1} = r a_n vs y' = ky, bridged by r = e^k (k = ln r).

(8) Torricelli: drain rate ∝ √(depth) (energy conservation). RL circuit: L dI/dt + RI = E,
    current approaches E/R with time constant L/R.
```

---

## Common Mistakes

### Mistake 1: Mixing — using the initial volume for rate out

When the volume changes over time, rate out $= \frac{A}{V(t)} \times f_{\text{out}}$ with $V(t) = V_0 + (\text{in} - \text{out})t$. Using the constant initial volume is wrong — and don't forget to find when the tank overflows.

### Mistake 2: Logistic — confusing $A$ or thinking the inflection is at $L$

$A = \frac{L - P_0}{P_0}$, and the S-curve's inflection point is at $P = \frac{L}{2}$ (fastest growth), not at $P = L$ (where growth stops).

### Mistake 3: Newton cooling — wrong sign or wrong "room temperature"

The ODE is $T' = -k(T - T_{\text{env}})$ with $k > 0$, so $T$ approaches $T_{\text{env}}$ (not 0, and not runaway). Writing $+k$ gives the wrong direction.

### Mistake 4: Discrete vs continuous — using $r$ as $k$

5% yearly interest means $r = 1.05$; the continuous rate is $k = \ln 1.05 \approx 0.0488$, **not** $0.05$. They give the same answer only when used correctly via $r = e^k$.

### Mistake 5: Unit mismatch in physical models

Torricelli (A11): hole area in $\text{cm}^2$ must become $\text{m}^2$ before plugging into $T = \frac{2\pi R^2\sqrt{H}}{a\sqrt{2g}}$ with $g = 9.8$. Always convert units first.

---

## Basic Drills

> All problems from Stewart, *Calculus*, Ch.9. (section 9.x #n).

**D1.** (9.1 #6) Verify that $y = \sin x - \cos x$ solves $y' + y = 2\sin x$.

**D2.** (9.1 #7) Verify that $y = \frac{2}{3}e^x + e^{-2x}$ solves $y' + 2y = 2e^x$.

**D3.** (9.1 #9) Verify that $y = \sqrt{x}$ solves $xy' - y = 0$.

**D4.** (9.1 #18a) Show that $y = (\ln x + C)/x$ solves $x^2y' + xy = 1$.

**D5.** (9.1 #19b) Verify that all members of $y = 1/(x+C)$ solve $y' = -y^2$.

**D6.** (9.2 #9) Sketch a direction field for $y' = \frac{1}{2}y$. Then sketch three solution curves.

**D7.** (9.2 #10) Sketch a direction field for $y' = x - y + 1$. Then sketch three solution curves.

**D8.** (9.1 #19a) What can you say about a solution of $y' = -y^2$ just by looking at the ODE?

**D9.** (9.1 #19d) Find the solution of $y' = -y^2$, $y(0) = 0.5$.

**D10.** (9.2 #11) Sketch the direction field of $y' = y - 2x$. Sketch the solution curve through $(1,0)$.

**D11.** (9.2 #19a) Use Euler's method with $h=0.2$ to estimate $y(0.4)$ for $y'=y$, $y(0)=1$.

**D12.** (9.2 #21) Use Euler's method with $h=0.5$ to compute $y_1,y_2,y_3,y_4$ for $y'=y-2x$, $y(1)=0$.

> Solutions: [Solutions](solutions/19A-solutions.md#basic-drill)

---

## Advanced Drills

**A1.** (9.1 #13) Show that $y = -t\cos t - t$ solves $t\frac{dy}{dt} = y + t^2\sin t$, $y(\pi)=0$.

**A2.** (9.1 #14) Show that $y = 5e^{2x}+x$ solves $y'-2y = 1-2x$, $y(0)=5$.

**A3.** (9.1 #15) For what $r$ does $y=e^{rx}$ solve $2y''+y'-y=0$? Show the family also works.

**A4.** (9.1 #26) Coffee at 95C in a 20C room. (a) When does it cool fastest? (b) Write ODE and IC.

**A5.** (9.1 #27) Learning curve $dP/dt = k(M-P)$. (a) When fastest? (b) Why reasonable? (c) Sketch.

**A6.** (9.2 #25) Euler for $y'+3x^2y=6x^2$, $y(0)=3$. (a) Euler $h=0.1$. (b) Verify $y=2+e^{-x^3}$. (c) Error.

**A7.** (9.2 #27) RC circuit: $R=5$, $C=0.05$, $E=60$. (a) Direction field. (b) Limiting charge? (c) Equilibrium?

**A8.** (9.2 #28) Coffee 95C, room 20C. Cools 1C/min at $T=70C$. (a) Find $k$. (b) Euler $h=2$ for $T(10)$.

**A9.** (9.1 #28) Von Bertalanffy: $dL/dt = k(L_\infty - L)$. (a) Write ODE. (b) Sketch.

**A10.** (9.2 #17) Direction field for $y'=y^3-4y$. For what $c$ does $\lim_{t\to\infty}y(t)$ exist?

**A11.** (9.2 #19c) Euler for $y'=y$, $y(0)=1$: $h=0.4,0.2,0.1$. Errors? What when $h$ halves?

**A12.** (9.1 #19c) A solution of $y'=-y^2$ NOT in the family $y=1/(x+C)$?

> Solutions: [Solutions](solutions/19A-solutions.md#advanced-drill)

---

## Today's Procedure

```
Step 1: Recognize the model — y'=ky (growth/decay), y'=k(L−y) (approach to a limit),
         y'=ky(1−y/L) (logistic), dA/dt = rate in − rate out (mixing/tanks),
         y'=f(y) (autonomous → phase line).

Step 2: Build the ODE — name the quantity; write rate = in − out (or a proportional law);
         attach the initial condition y(0)=y₀.

Step 3: Solve — exponential: y = Ce^{kt}. Approach: y = steady + Ce^{−kt}.
         Logistic: L/(1+Ae^{−kt}) with A=(L−P₀)/P₀. Mixing: linear 1st order
         (full toolbox in 19B).

Step 4: Interpret — doubling time ln2/k, half-life ln2/|k|, steady state, carrying
         capacity L, time constant L/R or 1/b. Discrete↔continuous: r = e^k.

Step 5: Qualitatively — slope field first; then phase line: equilibria f(y)=0,
         test signs, label stable (sink) vs unstable (source).
```

---

## How to Read These Symbols

| Symbol | Reads as | Meaning |
|:---:|:---:|------|
| $\frac{dy}{dx}$ | "d y d x" / "the derivative of y with respect to x" | instantaneous rate of change, slope |
| $y'$ | "y prime" | shorthand for dy/dx |
| $\frac{dP}{dt}$ | "d P d t" / "the rate of change of P" | time derivative — how P changes per unit time |
| $\int$ | "integral" | integration symbol — finds area, accumulation |
| $e^{kt}$ | "e to the k t" | exponential function — e ≈ 2.718, base of natural growth/decay |
| $\ln$ | "natural log" / "ell-en" | logarithm base e — inverse of e^x |
| $\lim$ | "limit" | limit — value approached, not necessarily reached |
| $t_{1/2}$ | "t-half" / "half-life" | time for quantity to decrease by half |
| $t_2$ | "t-two" / "doubling time" | time for quantity to double |
| $k$ | "k" / "rate constant" | growth (k>0) or decay (k<0) rate |
| $L$ | "L" / "carrying capacity" | upper bound in logistic growth — saturation level |
| $C$ | "C" / "constant of integration" | arbitrary constant — determined by initial condition |
| $T_{\text{env}}$ | "T env" / "environment temperature" | ambient temperature in Newton cooling |
| $f(y)=0$ | "f of y equals zero" | equilibrium condition — no change over time |
| $\uparrow$ / $\downarrow$ | "up arrow / down arrow" | direction of motion on the phase line — increasing / decreasing |
| $a_{n+1}=ra_n$ | "a n plus one equals r a n" | discrete growth — geometric sequence (12B1) |
| $r = e^k$ | "r equals e to the k" | bridge between discrete ratio and continuous rate |

---

## Terminology

| What we call it | Math term | Notation |
|:---:|:---:|:---:|
| equation with derivatives | ordinary differential equation (ODE) | $\frac{dy}{dx}=f(x,y)$ |
| solution + arbitrary constant | general solution | $y = Ce^{kt}$ |
| solution with specific initial value | particular solution | $y(0)=y_0$ plugged in |
| exponential growth/decay model | $y'=ky$ | $y=Ce^{kt}$ |
| S-shaped growth to a limit | logistic equation | $\frac{dP}{dt}=kP(1-P/L)$ |
| temperature approaches environment | Newton's law of cooling | $\frac{dT}{dt}=-k(T-T_{\text{env}})$ |
| inflow minus outflow | mixing problem | $\frac{dA}{dt} = \text{rate in} - \text{rate out}$ |
| 1D stability diagram | phase line | $y$-axis with arrows showing direction of $y'$ |
| stable equilibrium | attractor / sink | nearby solutions converge to it |
| unstable equilibrium | repellor / source | nearby solutions diverge from it |
| discrete growth (12B1) | geometric sequence | $a_{n+1}=ra_n$, $a_n = a_0r^n$ |
| continuous ↔ discrete bridge | $r = e^k$ | $r$ (ratio) = $e^k$ (continuous rate) |
> **Geometric insight**: An ODE is a *rule for slopes*. The equation $y' = f(x,y)$ says: at every point $(x,y)$ in the plane, any solution curve passing through that point must have slope $f(x,y)$. Example 2 draws exactly this — a slope field is a differential equation turned into a picture.