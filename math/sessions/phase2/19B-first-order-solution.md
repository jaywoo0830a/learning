# Session 19B: First-Order Solution Methods

**Phase 2 — Classical Techniques | 60 min**

*Prerequisites: 19A (ODE modeling), 16A/B (integration techniques)*

---

## Example 1: Separable Equations

If $\frac{dy}{dx} = g(x)h(y)$: separate → $\int \frac{dy}{h(y)} = \int g(x)dx$.

$\frac{dy}{dx} = xy$. Separate: $\int \frac{dy}{y} = \int x\,dx$. $\ln|y| = \frac{x^2}{2}+C$. $y = Ce^{x^2/2}$.

$\frac{dy}{dx} = \frac{x}{y}$: $y\,dy = x\,dx$. $\frac{y^2}{2} = \frac{x^2}{2}+C$. $y^2 = x^2 + C$.

**Always isolate $dy/dx$ first, then separate.**

---

## Example 2: Separable with Trig and Exponential

$\frac{dy}{dx} = y^2\cos x$. Separate: $\int y^{-2}dy = \int \cos x\,dx$. $-\frac{1}{y} = \sin x + C$. $y = \frac{-1}{\sin x + C}$.

$\frac{dy}{dx} = e^{x+y} = e^x e^y$. $\int e^{-y}dy = \int e^x dx$. $-e^{-y} = e^x + C$. $y = -\ln(C - e^x)$.

---

## Example 3: Linear First-Order — Integrating Factor

**Standard form**: $y' + P(x)y = Q(x)$. **Integrating factor**: $\mu(x) = e^{\int P(x)dx}$.

Multiply ODE by $\mu$: $\frac{d}{dx}(\mu y) = \mu Q$. Integrate: $y = \frac{1}{\mu}\int \mu Q\,dx + \frac{C}{\mu}$.

**Why it works**: $\mu' = \mu P$, so $(\mu y)' = \mu y' + \mu' y = \mu(y'+Py) = \mu Q$.

---

## Example 4: Integrating Factor in Action

$y' + 2xy = x$. $P(x)=2x$, $\mu = e^{\int 2x\,dx} = e^{x^2}$.

$e^{x^2}y' + 2xe^{x^2}y = xe^{x^2}$. Left side = $(e^{x^2}y)'$.

$e^{x^2}y = \int xe^{x^2}dx = \frac{1}{2}e^{x^2} + C$. $y = \frac{1}{2} + Ce^{-x^2}$.

---

## Example 5: $y' + \frac{1}{x}y = x^2$

$P=1/x$, $\mu = e^{\ln x} = x$. $(xy)' = x^3$. $xy = \frac{x^4}{4} + C$. $y = \frac{x^3}{4} + \frac{C}{x}$.

---

## Example 6: Logistic Equation in Full

$\frac{dP}{dt} = kP(1-P/L)$. This is separable!

$\int \frac{dP}{P(1-P/L)} = \int k\,dt$. Use partial fractions: $\frac{1}{P(1-P/L)} = \frac{1}{P} + \frac{1/L}{1-P/L}$.

$\ln|P| - \ln|1-P/L| = kt + C$. $\frac{P}{1-P/L} = Ae^{kt}$. Solve: $P = \frac{L}{1+Be^{-kt}}$ where $B = \frac{L-P_0}{P_0}$.

---

## Example 7: Equilibrium Solutions and Stability

For $\frac{dy}{dt} = f(y)$, equilibrium where $f(y)=0$.

$y' = y(1-y)$: equilibria at $y=0,1$. $y=0$ unstable (small positive pushes away). $y=1$ stable (nearby solutions converge to 1).

---

## Common Mistakes

### Mistake 1: Forgetting the absolute value in $\int \frac{dy}{y} = \ln|y|$
### Mistake 2: Not putting ODE in standard form before identifying $P(x)$
### Mistake 3: Losing the $+C$ — it's always there for indefinite integration

---

## Practice 1

Solve: $\frac{dy}{dx} = \frac{x^2}{y}$, $y(0)=3$.

→ Solutions: [Solutions](solutions/19B-solutions.md#practice-1)

---

## Practice 2

Solve: $y' + 3y = 6$, $y(0)=2$. Find equilibrium.

→ Solutions: [Solutions](solutions/19B-solutions.md#practice-2)

---

## Practice 3

Solve: $y' - \frac{2}{x}y = x^3$, $x>0$.

→ Solutions: [Solutions](solutions/19B-solutions.md#practice-3)

---

## Basic Algebra Drill — First-Order Methods (10 Problems)

**D1.** Solve $dy/dx = 2xy$. Separable.

**D2.** Solve $dy/dx = y\sin x$, $y(0)=1$.

**D3.** Solve $y' + y = e^x$. Integrating factor.

**D4.** Solve $y' - y = 2$, $y(0)=3$.

**D5.** Solve $dy/dx = \frac{\cos x}{2y}$, $y(0)=1$.

**D6.** Solve $xy' + y = x^2$. Write in standard form first.

**D7.** Solve $y' + 2y = 4$, equilibrium?

**D8.** Find $\mu(x)$ for $y' + (\tan x)y = \sec x$.

**D9.** Solve $dy/dx = y^2$, $y(0)=1$. Watch domain.

**D10.** Solve $y' = \frac{y}{x}$, $x>0$.

> Solutions: [Solutions](solutions/19B-solutions.md#basic-drill)

---

## Advanced Algebra Drill — First-Order Methods (10 Problems)

**A1.** Solve $dy/dx = (x+y)^2$ using substitution $u=x+y$.

**A2.** Solve $y' + y = y^2$ (Bernoulli with $n=2$).

**A3.** Solve $y' + \frac{2}{x}y = \frac{\sin x}{x^2}$.

**A4.** Tank: $A' + \frac{2}{100}A = 1$, $A(0)=0$. Solve and find $\lim_{t\to\infty}A(t)$.

**A5.** Solve $dy/dx = \frac{y}{x} + x\sin x$ (linear, not separable).

**A6.** An ODE has integrating factor $\mu = \sec x$. Write the general solution form.

**A7.** Solve $(1+x^2)y' + 2xy = 1$, $y(0)=0$. The left side is already a perfect derivative.

**A8.** Solve $\frac{dy}{dx} = \frac{x+y}{x-y}$ (homogeneous). Use $v=y/x$.

**A9.** Solve $y' + P(x)y = Q(x)$ where $P$ and $Q$ are constants. Derive the general formula.

**A10.** Show that every solution of $y' = y(1-y)$ approaches 1 as $t\to\infty$ (except $y\equiv0$).

> Solutions: [Solutions](solutions/19B-solutions.md#advanced-drill)
