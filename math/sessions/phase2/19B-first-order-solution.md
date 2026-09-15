# Session 19B: First-Order Solution Methods

**Phase 2 — Classical Techniques | 65 min**

*Prerequisites: 19A (ODE modeling), 16A/B (integration techniques)*

> 💡 **Stuck?** Every problem has a collapsible **Hint** below it — click it only when you need a nudge.

> **Source.** Every example and drill below is drawn from Stewart, *Calculus*, Chapter 9 (Sections 9.3–9.5). Each item cites its section and exercise number.

---

## Part A: Separable Equations

---

## Example 1: The Separation Method (§9.3)

If $\frac{dy}{dx} = g(x)h(y)$: separate → $\int \frac{dy}{h(y)} = \int g(x)\,dx$.

**Always isolate $dy/dx$ first, then separate.**

**§9.3 Ex 1**: $\frac{dy}{dx} = \frac{x^2}{y^2}$. Separate: $\int y^2\,dy = \int x^2\,dx$. $\frac{y^3}{3} = \frac{x^3}{3} + C$. $y^3 = x^3 + C'$.

With $y(0) = 2$: $8 = 0 + C'$ → $C' = 8$. $y = \sqrt[3]{x^3 + 8}$.

**§9.3 Ex 5**: $\frac{dy}{dx} = xy$. Separate: $\int \frac{dy}{y} = \int x\,dx$. $\ln|y| = \frac{x^2}{2} + C$. $y = Ae^{x^2/2}$.

**§9.3 Ex 3**: $\frac{dy}{dx} = \frac{6x^2}{2y + \cos y}$. Separate: $\int (2y + \cos y)\,dy = \int 6x^2\,dx$. $y^2 + \sin y = 2x^3 + C$.

This gives an **implicit solution** — we can't solve for $y$ explicitly, but the relation defines $y$ as a function of $x$.

---

## Example 2: Separable with Initial Value (§9.3 Ex 7, Ex 9)

**§9.3 Ex 7**: $\frac{dy}{dx} = \frac{x}{y}$, $y(0) = -3$. Separate: $y\,dy = x\,dx$. $\frac{y^2}{2} = \frac{x^2}{2} + C$.

$y(0)=-3$: $\frac{9}{2} = 0 + C$ → $C = \frac{9}{2}$. $y^2 = x^2 + 9$. Since $y(0) = -3 < 0$, take the negative root: $y = -\sqrt{x^2 + 9}$.

**§9.3 Ex 9**: $\frac{dy}{dx} = \frac{2x}{1+2y}$, $y(2) = 0$. Separate: $\int(1+2y)\,dy = \int 2x\,dx$. $y + y^2 = x^2 + C$.

$y(2)=0$: $0 + 0 = 4 + C$ → $C = -4$. $y + y^2 = x^2 - 4$.

**Domain restriction**: the solution exists only where $1+2y \neq 0$, i.e., $y \neq -1/2$. The initial condition $y(2)=0$ is safe.

---

## Example 3: Mixing Problems with Separable ODE (§9.3 Ex 13–16)

**§9.3 Ex 13**: A tank contains 200 L of fluid with 30 g of salt. Brine with 1 g/L enters at 4 L/min; the solution leaves at 4 L/min. Find $A(t)$.

Rate in = $1 \times 4 = 4$ g/min. Rate out = $\frac{A}{200} \times 4 = \frac{A}{50}$.

$$\frac{dA}{dt} = 4 - \frac{A}{50} = \frac{200 - A}{50}.$$

Separable: $\int \frac{dA}{200-A} = \int \frac{dt}{50}$. $-\ln|200-A| = \frac{t}{50} + C$.

$A(0)=30$: $-\ln 170 = C$. $200 - A = 170e^{-t/50}$. $A(t) = 200 - 170e^{-t/50}$.

As $t \to \infty$: $A \to 200$ g (the concentration approaches 1 g/L).

**§9.3 Ex 16** — variable volume: A tank initially has 100 L. Brine (1 g/L) enters at 3 L/min; mixture leaves at 2 L/min. Volume grows: $V(t) = 100 + t$.

Rate out = $\frac{A}{100+t} \times 2$. The ODE: $\frac{dA}{dt} = 3 - \frac{2A}{100+t}$.

This is a **linear** ODE (not separable) — solved with the integrating factor in Part B.

---

## Part B: Linear First-Order — The Integrating Factor

---

## Example 4: Standard Form and the Factor (§9.5)

**Standard form**: $y' + P(x)y = Q(x)$. **Integrating factor**: $\mu(x) = e^{\int P(x)\,dx}$.

Multiply ODE by $\mu$: $\frac{d}{dx}(\mu y) = \mu Q$. Integrate: $y = \frac{1}{\mu}\int \mu Q\,dx + \frac{C}{\mu}$.

**Why it works** (§9.5): $\mu' = \mu P$, so $(\mu y)' = \mu y' + \mu' y = \mu(y'+Py) = \mu Q$. The left side becomes an exact derivative.

**Method — Solve a linear first-order ODE in 5 steps:**

(1) **Standard form**: rewrite as $y' + P(x)y = Q(x)$.
(2) **Integrating factor**: $\mu = e^{\int P\,dx}$.
(3) **Multiply** both sides by $\mu$.
(4) **Recognize** the left side as $(\mu y)'$.
(5) **Integrate** and solve for $y$.

---

## Example 5: Integrating Factor in Action (§9.5 Ex 1, Ex 3, Ex 5)

**§9.5 Ex 1**: $y' + 2xy = x$. $P(x)=2x$, $\mu = e^{\int 2x\,dx} = e^{x^2}$.

$e^{x^2}y' + 2xe^{x^2}y = xe^{x^2}$. Left side = $(e^{x^2}y)'$.

$e^{x^2}y = \int xe^{x^2}dx = \frac{1}{2}e^{x^2} + C$. $y = \frac{1}{2} + Ce^{-x^2}$.

**§9.5 Ex 3**: $xy' + y = x^2$. Divide by $x$: $y' + \frac{1}{x}y = x$. $P = 1/x$, $\mu = e^{\ln x} = x$.

$(xy)' = x^2$. $xy = \frac{x^3}{3} + C$. $y = \frac{x^2}{3} + \frac{C}{x}$.

**§9.5 Ex 5**: $y' + 3y = e^{-x}$. $P=3$, $\mu = e^{3x}$. $(e^{3x}y)' = e^{2x}$.

$e^{3x}y = \frac{1}{2}e^{2x} + C$. $y = \frac{1}{2}e^{-x} + Ce^{-3x}$.

As $x\to\infty$: $y \to 0$ (both terms decay). The particular solution $y_p = \frac{1}{2}e^{-x}$ is the "steady" behavior; $Ce^{-3x}$ is the transient.

---

## Example 6: The Logistic Equation — Full Derivation (§9.3, §9.4)

$\frac{dP}{dt} = kP(1-P/L)$. This is separable!

$$\int \frac{dP}{P(1-P/L)} = \int k\,dt.$$

**Partial fractions** (§9.3, 🔗 16B): $\frac{1}{P(1-P/L)} = \frac{1}{P} + \frac{1/L}{1-P/L}$.

$$\int\left(\frac{1}{P} + \frac{1/L}{1-P/L}\right)dP = \ln|P| - \ln|1-P/L| = kt + C.$$

$$\ln\left|\frac{P}{1-P/L}\right| = kt + C \quad\Longrightarrow\quad \frac{P}{1-P/L} = Ae^{kt}.$$

Solve for $P$: $P = \frac{L}{1+Be^{-kt}}$ where $B = \frac{L-P_0}{P_0}$.

**Verify**: $P(0) = \frac{L}{1+B} = \frac{L}{1+(L-P_0)/P_0} = \frac{L}{L/P_0} = P_0$. ✓

**Inflection**: $P = L/2$ (fastest growth). **Carrying capacity**: $P \to L$ as $t \to \infty$.

---

## Part C: Equilibrium, Stability, and Interval of Validity

---

## Example 7: Equilibrium Solutions and Stability (§9.4)

For $\frac{dy}{dt} = f(y)$, equilibrium where $f(y)=0$.

$y' = y(1-y)$: equilibria at $y=0,1$. $y=0$ unstable (small positive pushes away). $y=1$ stable (nearby solutions converge to 1).

**General method**: at each equilibrium $y^*$, check the sign of $f'(y^*)$:
- $f'(y^*) < 0$: stable (restoring force).
- $f'(y^*) > 0$: unstable (amplifying force).

For $f(y) = y(1-y)$: $f'(y) = 1-2y$. $f'(0) = 1 > 0$ → unstable. $f'(1) = -1 < 0$ → stable.

---

## Example 8: Interval of Validity — Where Does the Solution Work? (§9.3)

When you solve an ODE, the solution may only be valid on a **specific interval**. The general solution formula might suggest a wider domain, but the actual solution with initial conditions might blow up at finite $x$.

$y' = y^2$, $y(0)=1$. Separate: $\int y^{-2}dy = \int dx$ → $-\frac{1}{y} = x + C$. With $y(0)=1$: $C = -1$.

$-\frac{1}{y} = x - 1$ → $y = \frac{1}{1-x}$.

**This solution is only valid for $x < 1$.** At $x=1$, $y\to\infty$ (vertical asymptote). The solution doesn't "stop" at $x=1$ — it blows up.

**General rule**: the **interval of validity** is the largest interval containing $x_0$ where the solution exists and is differentiable. It stops at the nearest singularity of the ODE or the solution.

---

## Example 9: Mixing with Variable Volume (§9.3 Ex 16, §9.5)

From Example 3: $V(t) = 100 + t$, $\frac{dA}{dt} = 3 - \frac{2A}{100+t}$. Rewrite:

$$A' + \frac{2}{100+t}A = 3.$$

$P(t) = \frac{2}{100+t}$, $\mu = e^{\int\frac{2}{100+t}dt} = e^{2\ln(100+t)} = (100+t)^2$.

$((100+t)^2 A)' = 3(100+t)^2$. Integrate: $(100+t)^2 A = (100+t)^3 + C$.

$A(t) = (100+t) + \frac{C}{(100+t)^2}$. $A(0)=30$: $30 = 100 + C/10000$ → $C = -700000$.

$A(t) = (100+t) - \frac{700000}{(100+t)^2}$.

As $t\to\infty$: $A \approx 100+t$ (the amount grows because the tank is filling up), but the **concentration** $A/V = A/(100+t) \to 1$ g/L (approaches the inflow concentration).

---

## What We Just Did

```
(1) Separable: dy/dx = g(x)h(y) → ∫dy/h(y) = ∫g(x)dx. Always check for lost solutions.

(2) Linear first-order: y'+P(x)y=Q(x). Integrating factor μ=e^{∫Pdx}.
    Multiply by μ → (μy)' = μQ → integrate → solve for y.

(3) Logistic dP/dt = kP(1−P/L) is separable: partial fractions → P = L/(1+Be^{−kt}).

(4) Equilibrium: f(y)=0. Stability: f'(y*)<0 → stable, f'(y*)>0 → unstable.

(5) Interval of validity: solution exists until it hits a singularity (blow-up).

(6) Variable-volume mixing: if V(t) changes, rate out = (A/V)×flow → linear ODE.
```

---

## Common Mistakes

### Mistake 1: Forgetting the lost solution in separation

When separating $\frac{dy}{dx} = g(x)h(y)$, dividing by $h(y)$ loses any constant solution where $h(y)=0$. Always check: is $y = c$ (constant) a solution? For $y' = y(1-y)$, $y=0$ and $y=1$ are constant solutions lost by dividing.

### Mistake 2: Integrating factor — not in standard form first

$xy' + y = x^2$ is NOT in standard form. Divide by $x$ first: $y' + \frac{1}{x}y = x$. Then $P = 1/x$.

### Mistake 3: Absolute values in logarithms

$\int \frac{dy}{y} = \ln|y| + C$, not $\ln y + C$. The absolute value matters when $y$ can be negative. But when solving $y' = ky$ with $y(0) > 0$, you know $y > 0$ always, so $|y| = y$.

### Mistake 4: Logistic — wrong $B$ or wrong inflection

$B = \frac{L-P_0}{P_0}$, not $\frac{P_0}{L-P_0}$. The inflection is at $P = L/2$, not at $P = L$.

---

## Basic Drills

> All problems from Stewart, *Calculus*, Ch.9. (section 9.x #n).

**D1.** (9.3 #1) Solve $\frac{dy}{dx} = 3x^2y^2$.

**D2.** (9.3 #5) Solve $xyy' = x^2 + 1$.

**D3.** (9.3 #8) Solve $\frac{dy}{dx} = 2x(y^2+1)$.

**D4.** (9.3 #13) Solve $y' = xe^y$, $y(0) = 0$.

**D5.** (9.3 #17) Solve $\frac{du}{dt} = \frac{2t + \sec^2 t}{2u}$, $u(0) = -5$.

**D6.** (9.3 #20) Solve $\frac{dy}{dx} = \frac{x\sin x}{y}$, $y(0) = -1$.

**D7.** (9.5 #5) Solve $y' + y = 1$.

**D8.** (9.5 #7) Solve $y' = x - y$.

**D9.** (9.5 #9) Solve $xy' + y = \sqrt{x}$.

**D10.** (9.5 #12) Solve $y' - 3x^2y = x^2$.

**D11.** (9.4 #1) $\frac{dP}{dt} = 0.04P(1-P/1200)$, $P(0)=60$. Find carrying capacity, $k$, and $P(t)$.

**D12.** (9.4 #6) $\frac{dP}{dt} = 0.4P - 0.001P^2$, $P(0)=50$. Find carrying capacity and $P'(0)$.

> Solutions: [Solutions](solutions/19B-solutions.md#basic-drill)

---

## Advanced Drills

**A1.** (9.3 #23) Solve $y' = x + y$ by substitution $u = x + y$.

**A2.** (9.3 #24) Solve $xy' = y + xe^{y/x}$ by substitution $v = y/x$.

**A3.** (9.3 #25) (a) Solve $y' = 2x\sqrt{1-y^2}$. (b) Solve IVP $y(0)=0$. (c) Does $y(0)=2$ have a solution?

**A4.** (9.5 #17) Solve $xy' + y = 3x^2$, $y(1) = 4$.

**A5.** (9.5 #23) Solve $xy' = y + x^2\sin x$, $y(\pi) = 0$.

**A6.** (9.5 #24) Solve $(x^2+1)\frac{dy}{dx} + 3x(y-1) = 0$, $y(0) = 2$.

**A7.** (9.5 #28) Solve $xy' + y = -xy^2$ (Bernoulli, $n=2$).

**A8.** (9.4 #5) Pacific halibut: $\frac{dy}{dt} = ky(1-y/M)$, $M=8\times10^7$, $k=0.71$. (a) Biomass after 1 year if $y(0)=2\times10^7$. (b) Time to reach $4\times10^7$.

**A9.** (9.4 #7) Logistic: initial 1000, carrying 10000, grows to 2500 after 1 year. Population after 4 years?

**A10.** (9.5 #31) RL circuit: $E=40$ V, $L=2$ H, $R=10\,\Omega$, $I(0)=0$. (a) Find $I(t)$. (b) Current after 0.1 s.

**A11.** (9.5 #33) RC circuit: $R=5$, $C=0.05$, $E=60$, $Q(0)=0$. Find charge and current at time $t$.

**A12.** (9.3 Torricelli #1) Cylindrical tank: height 2 m, radius 1 m, hole radius 1 inch. (a) Show $dh/dt = -0.0004\sqrt{20h}$. (b) Find $h(t)$. (c) Drain time?

> Solutions: [Solutions](solutions/19B-solutions.md#advanced-drill)

---

## Today's Procedure

```
Step 1: Classify — is it separable? Linear? Neither?
         Separable: dy/dx = g(x)h(y). Linear: y'+P(x)y = Q(x).

Step 2: Separable — divide by h(y) (check lost solutions!), integrate both sides.
         Don't forget +C and absolute values in ln.

Step 3: Linear — rewrite in standard form y'+Py=Q. Compute μ=e^{∫Pdx}.
         Multiply, recognize (μy)', integrate, solve for y.

Step 4: Logistic — it's separable! Partial fractions → P = L/(1+Be^{−kt}).
         Inflection at P = L/2. Carrying capacity = L.

Step 5: Check — initial conditions, interval of validity (look for blow-up),
         long-term behavior (what happens as t→∞?).
```

---

## How to Read These Symbols

| Symbol | Reads as | Meaning |
|:---:|:---:|------|
| $\frac{dy}{dx} = g(x)h(y)$ | "d y d x equals g of x times h of y" | separable ODE — split y and x to opposite sides |
| $\int \frac{dy}{h(y)}$ | "integral of d y over h of y" | integration with respect to y after separation |
| $y' + P(x)y = Q(x)$ | "y prime plus P of x y equals Q of x" | standard form of a first-order linear ODE |
| $\mu(x)$ | "mu of x" / "integrating factor" | $\mu = e^{\int P dx}$ — multiplies ODE to make left side an exact derivative |
| $\frac{d}{dx}(\mu y)$ | "d d x of mu y" | derivative of product — left side becomes this after multiplying by $\mu$ |
| $\ln\|y\|$ | "natural log of absolute y" | absolute value is essential — domain of ln is positive numbers only |
| $y \equiv 0$ | "y is identically zero" | zero everywhere — the trivial equilibrium solution |
| $\lim_{t\to\infty}$ | "limit as t goes to infinity" | long-term behavior of the solution |
| equilibrium | "equilibrium" / "steady state" | constant solution where $y'=0$ — no change over time |
| interval of validity | "interval of validity" | largest interval containing $x_0$ where solution exists |
| blow-up / singularity | "blow-up" / "finite-time singularity" | solution $\to \pm\infty$ at finite $x$ (e.g., $y=1/(1-x)$) |
| separable / linear | "separable" / "linear" | ODE classification — determines solution method |

---

## Terminology

| What we call it | Math term | Notation |
|:---:|:---:|:---:|
| separate y and x | separable equation | $\frac{dy}{dx}=g(x)h(y)$ |
| multiply by $\mu$ to make left side exact | integrating factor | $\mu(x) = e^{\int P(x)dx}$ |
| standard form for first-order linear | linear first-order ODE | $y' + P(x)y = Q(x)$ |
| constant solution where $y'=0$ | equilibrium / steady state | $f(y)=0$ |
| nearby solutions converge to it | stable equilibrium | (attractor) |
| nearby solutions move away | unstable equilibrium | (repellor) |
| largest interval where solution exists | interval of validity | contains $x_0$, excludes singularities |
| logistic with constant removal | harvesting model | $P' = kP(1-P/L) - H$ |