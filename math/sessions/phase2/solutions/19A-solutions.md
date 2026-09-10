# Solutions — 19A: ODE Modeling — Translating Nature into Equations

> Back to [19A — ODE Modeling](../19A-ode-modeling.md)
## Basic Drills

### D1. Solve $e^{-0.1t} = 0.4$ for $t$.

$\ln$ both sides: $-0.1t = \ln 0.4$ → $t = -10\ln 0.4 = 10\ln 2.5 \approx 10(0.9163) \approx 9.16$.

> **Answer**: $t = 10\ln 2.5 \approx 9.16$

### D2. Radium-226 half-life 1600 years: write $N(t)$ with $k$ filled in, fraction remaining after 3200 years.

$k = \frac{\ln 2}{1600}$, so $N(t) = N_0e^{-(\ln2/1600)t}$. After 3200 yr = 2 half-lives: $N = N_0e^{-2\ln2} = \frac{N_0}{4}$.

> **Answer**: $N(t) = N_0e^{-(\ln2/1600)t}$; $\frac14$ of $N_0$ remains

### D3. Solve $y' = -0.05y$, $y(0)=200$. Find $y(20)$.

$y(t) = 200e^{-0.05t}$; $y(20) = 200e^{-1} \approx 73.6$.

> **Answer**: $y(20) \approx 73.6$

### D4. 100L tank, 200 kg salt, pure water flush at 5 L/min. Write ODE as $A' = -bA$.

$A' = 0 - \frac{A}{100}\times5 = -\frac{A}{20}$, so $b = \frac{1}{20}$.

> **Answer**: $A' = -\frac{A}{20}$ ($b = \frac{1}{20}$), $A(0) = 200$

### D5. Logistic $P'=0.4P(1-P/800)$, $P(0)=200$: find $L$ and $A$.

$L = 800$; $A = \frac{L-P_0}{P_0} = \frac{600}{200} = 3$.

> **Answer**: $L = 800$, $A = 3$

### D6. Set $P(t) = \frac{800}{1+3e^{-0.4t}} = 400$ and solve for $t$.

$1+3e^{-0.4t} = 2$ → $e^{-0.4t} = \frac13$ → $t = \frac{\ln 3}{0.4} = 2.5\ln 3 \approx 2.75$.

> **Answer**: $t = 2.5\ln 3 \approx 2.75$

### D7. $y' = 3 - 0.5y$, $y(0)=0$: steady state and $y(t)$.

$y_{ss} = \frac{3}{0.5} = 6$; $y(t) = 6(1-e^{-0.5t})$.

> **Answer**: $y_{ss} = 6$; $y(t) = 6(1-e^{-0.5t})$

### D8. Newton cooling $T(t) = 30 + 50e^{-kt}$, $T(5)=60$: find $k$.

$60 = 30 + 50e^{-5k}$ → $e^{-5k} = \frac35$ → $k = \frac15\ln\frac53 \approx 0.102$.

> **Answer**: $k = \frac15\ln\frac53 \approx 0.102$

### D9. Solve (a) $100e^{0.2t} = 900$ (b) $\frac{1000}{1+9e^{-0.2t}} = 900$.

(a) $e^{0.2t} = 9$ → $t = 5\ln 9 \approx 10.99$.
(b) $1+9e^{-0.2t} = \frac{10}{9}$ → $e^{-0.2t} = \frac1{81}$ → $t = 5\ln 81 \approx 21.97$.

> **Answer**: (a) $t = 5\ln 9 \approx 11.0$ (b) $t = 5\ln 81 \approx 22.0$

### D10. Lake $P' = 10 - \frac{P}{10^4}$, $P(0)=0$: $P_{ss}$ and $P(t)$.

$P_{ss} = 10\times10^4 = 10^5$; $b = 10^{-4}$, so $P(t) = 10^5\left(1-e^{-t/10^4}\right)$.

> **Answer**: $P(t) = 10^5(1-e^{-t/10^4})$

### D11. Convert $2\,\text{cm}^2$ and compute the Torricelli drain time.

$a = 2\times10^{-4}\,\text{m}^2$; $T = \frac{2\pi(0.25)\sqrt2}{(2\times10^{-4})\sqrt{19.6}} \approx 2509$ s $\approx 42$ min.

> **Answer**: $\approx 2500$ s $\approx 42$ min

### D12. Equilibria of (a) $y' = y(y-3)(y+1)$ (b) $y' = y\sin y$ on $(0,2\pi)$.

(a) $y(y-3)(y+1)=0$ → $y = -1, 0, 3$. (b) $y>0$, so $\sin y = 0$: $y = \pi$ inside $(0,2\pi)$.

> **Answer**: (a) $y=-1,0,3$ (b) $y=\pi$

---

## Advanced Drills

### A1. Carbon-14 half-life 5730 years. A fossil has 15% original C-14. How old?

$N(t)=N_0e^{-kt}$, $k=\frac{\ln2}{5730}$. Set $0.15 = e^{-kt}$:
$t = \frac{\ln(1/0.15)}{k} = 5730\cdot\frac{\ln(20/3)}{\ln 2} \approx 5730\cdot2.737 \approx 1.57\times10^4$ years.

> **Answer**: $\approx 15{,}700$ years old

### A2. A tank initially has 100L of 2 kg/L salt. Pure water enters at 5 L/min, drains at 5 L/min. Find salt after 20 min.

Volume constant 100 L; initial salt $= 2\times100 = 200$ kg.
$A' = 0 - \frac{A}{100}\cdot5 = -\frac{A}{20}$ → $A(t) = 200e^{-t/20}$.
$A(20) = 200e^{-1} \approx 73.6$ kg.

> **Answer**: $\approx 73.6$ kg

### A3. Logistic: $P'=0.4P(1-P/800)$, $P(0)=200$. Find inflection time (when $P=L/2$).

$L=800$, $A=\frac{800-200}{200}=3$ → $P(t)=\frac{800}{1+3e^{-0.4t}}$.
Set $P=\frac L2=400$: $1+3e^{-0.4t}=2$ → $e^{-0.4t}=\frac13$ → $t=\frac{\ln3}{0.4}=2.5\ln3 \approx 2.75$.

> **Answer**: $t = \frac{\ln3}{0.4} \approx 2.75$

### A4. Two tanks in series: tank 1 drains into tank 2. Write the system of ODEs.

Let $A_1, A_2$ be the salt amounts, $V_1, V_2$ the volumes, $f_1$ the flow from 1 into 2, and $c_{\text{in}}$ the inflow concentration to tank 1:

$$\frac{dA_1}{dt} = c_{\text{in}}f_1 - \frac{A_1}{V_1}f_1, \qquad \frac{dA_2}{dt} = \frac{A_1}{V_1}f_1 - \frac{A_2}{V_2}f_2.$$

(Tank 1's outflow is tank 2's inflow.) If volumes are constant, this is a linear system.

> **Answer**: $A_1' = c_{\text{in}}f_1 - \frac{A_1}{V_1}f_1$; $A_2' = \frac{A_1}{V_1}f_1 - \frac{A_2}{V_2}f_2$

### A5. Newton cooling: object at 80° in 30° room. At $t=5$, $T=60$. Find $k$, then find $T(15)$.

$T(t) = 30 + 50e^{-kt}$. $T(5)=60$: $e^{-5k}=\frac{30}{50}=\frac35$ → $k=\frac15\ln\frac53 \approx 0.1022$.
$T(15) = 30 + 50e^{-15k} = 30 + 50e^{-3\ln(5/3)} = 30 + 50\left(\frac35\right)^3 = 30 + 50(0.216) \approx 40.8$.

> **Answer**: $k = \frac15\ln\frac53 \approx 0.102$; $T(15) \approx 40.8$°C

### A6. A rumor spreads logistically. 10 people know at $t=0$, 100 know at $t=2$, $L=5000$. Find $k$.

$P(t)=\frac{5000}{1+Ae^{-kt}}$, $A=\frac{5000-10}{10}=499$. $P(2)=100$:
$1+499e^{-2k}=50$ → $499e^{-2k}=49$ → $k=\frac12\ln\frac{499}{49}\approx\frac12(2.321)\approx1.16$.

> **Answer**: $k \approx 1.16$

### A7. Drug concentration: $\frac{dC}{dt} = -kC + D$ (constant infusion $D$). Find equilibrium $C_{ss}$.

Set $\frac{dC}{dt}=0$: $-kC_{ss}+D=0$ → $C_{ss}=\frac{D}{k}$.

> **Answer**: $C_{ss} = D/k$

### A8. Terminal velocity: $m\frac{dv}{dt}=mg-kv$. Find $v(t)$ and terminal speed.

$\frac{dv}{dt} = \frac{mg-kv}{m}$, $v(0)=0$. This is an approach model with steady state $mg/k$:
$v(t) = \frac{mg}{k}\left(1-e^{-(k/m)t}\right)$. As $t\to\infty$, $v\to\frac{mg}{k}$ (terminal speed).

> **Answer**: $v(t) = \frac{mg}{k}\left(1-e^{-(k/m)t}\right)$; terminal speed $= mg/k$

### A9. Compare exponential vs logistic: both start at 100, $k=0.2$, but logistic has $L=1000$. Find $t$ when logistic reaches 900 vs exponential reaches 900.

**Logistic**: $P(t)=\frac{1000}{1+9e^{-0.2t}}$. Set $=900$: $1+9e^{-0.2t}=\frac{10}{9}$ → $9e^{-0.2t}=\frac19$ → $e^{-0.2t}=\frac1{81}$ → $t=5\ln81\approx21.97$.

**Exponential**: $100e^{0.2t}=900$ → $e^{0.2t}=9$ → $t=5\ln9\approx10.99$.

> **Answer**: exponential hits 900 at $t\approx11.0$; logistic (slowed by the carrying capacity) at $t\approx22.0$ — twice as long

### A10. A lake (10⁶ m³) receives polluted water (0.1 kg/m³) at 100 m³/day, drains at same rate. Initially clean. Write ODE, find pollution after 1 year.

$\frac{dP}{dt} = 0.1\times100 - \frac{P}{10^6}\times100 = 10 - \frac{P}{10^4}$, $P(0)=0$.

Approach model with steady state $10\times10^4 = 10^5$ kg: $P(t) = 10^5\left(1-e^{-t/10^4}\right)$.

After 1 year ($t=365$): $P = 10^5(1-e^{-0.0365}) = 10^5(0.03584) \approx 3.58\times10^3$ kg.

> **Answer**: $P' = 10 - P/10^4$; after 1 year $\approx 3580$ kg

### A11. Torricelli: A cylindrical tank (radius 0.5 m, height 2 m) drains through a 2 cm² hole. Find drain time. Use $g=9.8$.

$T = \frac{2\pi R^2\sqrt{H}}{a\sqrt{2g}}$ with $R=0.5$, $H=2$, $a=2\times10^{-4}\,\text{m}^2$, $g=9.8$:

$T = \frac{2\pi(0.25)(1.4142)}{(2\times10^{-4})(4.4272)} = \frac{2.2213}{8.854\times10^{-4}} \approx 2509$ s $\approx 41.8$ min.

> **Answer**: $\approx 2500$ s $\approx 42$ minutes

### A12. For $y' = y\sin y$ on $0<y<2\pi$, find all equilibria and classify stability.

$f(y)=y\sin y=0$: since $y>0$ on the interval, $\sin y=0$ → $y=\pi$ (the endpoints $0, 2\pi$ are boundaries).
- Just left of $\pi$: $\sin y > 0$ → $f>0$ → rising toward $\pi$.
- Just right of $\pi$: $\sin y < 0$ → $f<0$ → falling back to $\pi$.

Both sides move toward $\pi$ → **stable**.

> **Answer**: equilibrium $y=\pi$ (stable); $0$ and $2\pi$ are boundary equilibria

---

## Answer Check

| Problem | Answer |
|:--------|:-------|
| A1–A12, D1–D12 | see above |
