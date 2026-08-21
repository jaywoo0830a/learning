# Solutions — 16C1: Integral Interpretation

> Back to [16C1 — Integral Interpretation](../16C1-integral-interpretation.md)

---

## Practice 1

**(a)** $\int_0^{15}(30-2t)dt = \left[30t - t^2\right]_0^{15} = 450 - 225 = 225$ L.

**(b)** Rate table: $30, 20, 10, 0$ L/min at $t = 0, 5, 10, 15$. Trapezoids:

$\frac{30+20}{2}\cdot 5 + \frac{20+10}{2}\cdot 5 + \frac{10+0}{2}\cdot 5 = 125 + 75 + 25 = 225$ L.

Both methods agree because the rate is linear — trapezoids on a line are exact.

> **Answer**: 225 L by both methods

---

## Practice 2

**(a)** $\bar{T} = \frac{1}{24}\int_0^{24}\left(20 + 10\sin\frac{\pi t}{12}\right)dt = \frac{1}{24}\left[20t\right]_0^{24} = 20$ °C (the sine integrates to zero over a full period).

**(b)** Total degree-hours $= \bar{T}\cdot 24 = 480$ °C·h.

**(c)** The rectangle $[0,24]\times 20$ has the same area as the day's temperature curve: the warm afternoon lobe (above 20) exactly balances the cool night lobe (below 20). The average is the flat temperature that would deliver the same total heat.

> **Answer**: (a) 20 °C (b) 480 °C·h

---

## Practice 3

**(a)** $W = \int_0^{0.3}20x\,dx = \left[10x^2\right]_0^{0.3} = 0.9$ J.

**(b)** $W = \int_{0.3}^{0.4}20x\,dx = 10(0.16-0.09) = 0.7$ J.

**(c)** The second stretch is only one third as long yet costs 0.7 J — because the spring is already pulling with 6 N when the second stretch begins. Work is the *area* under the force curve, and the area is higher up where the force is bigger.

> **Answer**: (a) 0.9 J (b) 0.7 J (c) force already 6 N at the start

---

## Practice 4

Equilibrium: $120-3q = 20+2q$ → $q^* = 20$, $p^* = 60$.

$CS = \int_0^{20}(120-3q-60)dq = \left[60q - \frac32 q^2\right]_0^{20} = 1200 - 600 = 600$.

$PS = \int_0^{20}(60-20-2q)dq = \left[40q - q^2\right]_0^{20} = 800 - 400 = 400$.

> **Answer**: equilibrium $(20,\,60)$; CS = 600, PS = 400 (total welfare 1000)

---

## Practice 5: Real Battle — A Growing Income Stream

$PV = \int_0^{20} 50{,}000\,e^{0.02t}e^{-0.06t}dt = 50{,}000\int_0^{20}e^{-0.04t}dt = 50{,}000\cdot\frac{1-e^{-0.8}}{0.04} \approx 688{,}339$ \$.

The income grows at 2% but money loses value at 6% per year — the *net* discount rate is 4%, and the integrand still decays. A dollar 20 years out is worth $e^{-0.8} \approx 45\%$ of a dollar today, growth or no growth. That is why the \$1.1M of raw payments is worth only ≈\$688K now.

> **Answer**: PV ≈ \$688,339

---

## Practice 6: Real Battle — Battery Lifetime

**(a)** $\int_0^{10}\frac{3x^2}{1000}dx = \frac{1000}{1000} = 1$ ✓.

**(b)** $P(X>5) = \int_5^{10}\frac{3x^2}{1000}dx = \frac{1000-125}{1000} = 0.875$.

**(c)** $E[X] = \int_0^{10}x\cdot\frac{3x^2}{1000}dx = \frac{3\cdot 10^4}{4000} = 7.5$ years.

**(d)** $P(X=5) = \int_5^5 p(x)dx = 0$: a single point has zero width, so its area is zero. The density *at* 5 is a rate (probability per year), not a probability. Only intervals accumulate positive probability.

> **Answer**: (a) 1 ✓ (b) 0.875 (c) 7.5 yr (d) $P(X=5)=0$

---

## Basic Drills

### D1.

> **Answer**: (a) m (b) L (c) J = N·m (d) \$ (dollars, since \$/unit × units)

### D2.

$\int_0^{20}5e^{-t/10}dt = 50(1-e^{-2}) \approx 43.23$ L.

> **Answer**: ≈ 43.2 L

### D3.

$\bar{f} = \frac{1}{4}\int_0^4 x^2 dx = \frac{1}{4}\cdot\frac{64}{3} = \frac{16}{3}$.

> **Answer**: $\frac{16}{3}$

### D4.

$W = \frac12 kx^2 = \frac12\cdot 100\cdot(0.2)^2 = 2$ J.

> **Answer**: 2 J

### D5.

$\int_0^2(3t^2+1)dt = [t^3+t]_0^2 = 10$ m.

> **Answer**: 10 m

### D6.

Density $\frac18$ on $[0,8]$. $P(2<X<6) = 4\cdot\frac18 = \frac12$. $E[X] = 4$ (midpoint).

> **Answer**: $P = \frac12$, $E[X]=4$

### D7.

$\int_{-2}^2(4-x^2)dx = \left[4x-\frac{x^3}{3}\right]_{-2}^2 = \left(8-\frac83\right)-\left(-8+\frac83\right) = \frac{32}{3}$.

> **Answer**: $\frac{32}{3}$; with cm axes it is $\frac{32}{3}$ cm² — the true area under the parabola

### D8.

$q^* = 20$ at price 20 ($60-2q=20$). $CS = \int_0^{20}(60-2q-20)dq = \left[40q-q^2\right]_0^{20} = 400$.

> **Answer**: CS = \$400

### D9.

$PV = 1000\cdot\frac{1-e^{-1}}{0.1} \approx 6321.21$ \$.

> **Answer**: ≈ \$6,321

### D10.

$E[X] = \int_0^1 x\cdot 2x\,dx = \left[\frac{2x^3}{3}\right]_0^1 = \frac23$.

> **Answer**: $\frac23$

---

## Advanced Drills

### A1.

- Population: "the total births between $a$ and $b$ equal the population at $b$ minus the population at $a$."
- Tank: "the total inflow between $a$ and $b$ equals the volume at $b$ minus the volume at $a$."
- Account: "the total interest earned between $a$ and $b$ equals the balance at $b$ minus the balance at $a$."

> **Answer**: three instances of "total change = final − initial"

### A2.

$W = \int_1^3 6x^2 dx = [2x^3]_1^3 = 54 - 2 = 52$ J. Check: $\frac{d}{dx}(2x^3) = 6x^2 = F(x)$ ✓ — differentiating the work function recovers the force. Units: N·m = J.

> **Answer**: 52 J; $dW/dx = F$ ✓

### A3.

At height $h$ from the bottom the radius is $r = \frac{h}{2}$ (similar triangles). Layer volume $= \pi r^2 dh = \pi\frac{h^2}{4}dh$; weight $= 9800\,\pi\frac{h^2}{4}dh$; travel distance $= 6-h$.

$W = \int_0^6 9800\,\pi\,\frac{h^2}{4}(6-h)\,dh = \frac{9800\pi}{4}\int_0^6(6h^2-h^3)dh = \frac{9800\pi}{4}\left(2\cdot 216 - \frac{1296}{4}\right) = 9800\pi\cdot 27 \approx 831{,}265$ J ≈ 831 kJ.

The lower layers dominate: the deepest layer is widest ($r$ largest), heaviest, *and* travels the full 6 m. All three factors grow with depth.

> **Answer**: $W = 27\pi\rho g \approx 831$ kJ

### A4.

Average of $x^2$ on $[0,4]$ is $\frac{16}{3}$. The theorem guarantees a $c$ with $f(c) = \frac{16}{3}$: $c^2 = \frac{16}{3}$ → $c = \frac{4}{\sqrt3} \approx 2.31 \in [0,4]$ ✓.

Meaning: no continuous function can stay entirely above (or below) its average — some instant achieves exactly the average height, just as the mean value theorem guarantees some instant with exactly the average slope.

> **Answer**: $c = \frac{4}{\sqrt3} \approx 2.31$

### A5.

Free equilibrium: $200-2q = q$ → $q^* = \frac{200}{3} \approx 66.67$. The quota bans production between 50 and $q^*$, killing trades worth $D(q)-S(q) = 200-3q$ each.

$DWL = \int_{50}^{200/3}(200-3q)dq = \left[200q-\frac32 q^2\right]_{50}^{200/3} = \frac{20000}{3} - 6250 = \frac{1250}{3} \approx 416.67$.

It measures the trades that would have benefited both sides (buyers willing to pay more than sellers demand) but are now illegal — pure lost value, received by no one.

> **Answer**: DWL $= \frac{1250}{3} \approx \$416.67$

### A6.

$PV(T) = \int_0^T Re^{-rt}dt = \frac{R}{r}(1-e^{-rT})$.

As $T\to\infty$: $PV = \frac{R}{r}$. At 5%, a perpetual stream of \$1/yr is worth \$20 today — twenty years of income in one lump, because dollars far in the future are worth almost nothing. The perpetuity price is the natural cap that all finite streams approach.

> **Answer**: $PV(T) = \frac{R}{r}(1-e^{-rT})$; perpetuity $\frac{R}{r}$

### A7.

Median: $\int_0^m 2x\,dx = m^2 = \frac12$ → $m = \frac{1}{\sqrt2} \approx 0.707$.

Mean: $\frac23 \approx 0.667$. The median is larger because the density $2x$ rises with $x$ — more probability mass sits on the right. The mean balances the *mass* (so it chases the heavy right tail), while the median only asks where the *area* halves; with mass piled at the top end, half the area is reached only past the mean.

> **Answer**: median $\frac{1}{\sqrt2} \approx 0.707 > \frac23$ — the density leans right

### A8.

**(a)** $\int_0^\infty 2e^{-2x}dx = [-e^{-2x}]_0^\infty = 1$ ✓.

**(b)** $P(X>1) = \int_1^\infty 2e^{-2x}dx = e^{-2} \approx 0.1353$.

**(c)** $E[X] = \int_0^\infty x\cdot 2e^{-2x}dx = \frac12$ (by parts: $\left[-x e^{-2x}\right]_0^\infty + \int_0^\infty e^{-2x}dx = 0 + \frac12$).

**(d)** The survival probability decays as $e^{-2x}$: the chance of lasting past 1 is $e^{-2}$ because the density itself is exponential — every unit of time kills a constant fraction (2 per unit) of the survivors. It is the same memoryless pattern as radioactive decay and continuously compounded discounting.

> **Answer**: (a) 1 ✓ (b) $e^{-2}\approx0.135$ (c) $\frac12$

### A9.

**(a) Area**: $\frac13$ is the area between $y=x^2$ and the $x$-axis on $[0,1]$.

**(b) Average × length**: the average of $x^2$ on $[0,1]$ is $\frac13$, and $1 \cdot \frac13 = \frac13$ — the area of the equal-height rectangle.

**(c) Total change**: $F(x)=\frac{x^3}{3}$ has $F'=x^2$; the integral is $F(1)-F(0)$ — the accumulation between 0 and 1 of a quantity whose rate is $x^2$.

"Which picture?" matters because each gives different units and a different sentence: geometric area, summary statistic, or accumulated total. The math is one number; the meaning is chosen by the picture.

> **Answer**: one number, three meanings — area / average×length / total change

### A10.

**(a)** Chain rule: $\frac{dV}{dt} = \frac{dV}{dr}\cdot\frac{dr}{dt} = 4\pi r^2\cdot c$ — the surface area times the radial speed. The snowball adds a shell of thickness $c\,dt$ each instant.

**(b)** $\int_0^R 4\pi r^2 dr = \frac{4}{3}\pi R^3 = V(R)$ — integrating the shell areas rebuilds the volume. Integration and differentiation are the same sphere seen from opposite directions.

**(c)** $r = ct$, so $V(t) = \frac{4}{3}\pi(ct)^3$ — volume grows **cubically** in time even though the radius grows only linearly. A constant radial growth rate is an exploding volume growth rate.

> **Answer**: (a) $4\pi r^2 c$ (b) $\frac43\pi R^3$ ✓ (c) $V(t)=\frac43\pi(ct)^3$ — cubic

---

## Deep Insight

### DI1.

**(a)** Displacement $= \int_0^\pi\cos t\,dt = \sin\pi-\sin0 = 0$ m — the boat ends where it started.

**(b)** Distance $= \int_0^\pi|\cos t|\,dt = \int_0^{\pi/2}\cos t\,dt - \int_{\pi/2}^{\pi}\cos t\,dt = 1+1 = 2$ m.

**(c)** Average velocity $= \frac{0}{\pi} = 0$ m/h.

**(d)** Average speed $= \frac{2}{\pi} \approx 0.637$ m/h.

The FTC pair: (a) and (c) — displacement is the integral of the *signed* rate, and the average velocity is that integral divided by time. The failing pair: (b) and (d). $|\cos t|$ is not the derivative of any smooth position function — it has a corner where the sign flips, so $\int|v|$ cannot be written $F(\pi)-F(0)$ of one natural $F$. **The FTC is a theorem about signed rates.** Unsigned totals (distance, total outflow regardless of direction) need the absolute value — and the absolute value is precisely where the theorem refuses to work: split the domain at every sign change. Deciding which total is asked (signed vs unsigned) is the first interpretation move of every rate integral.

> **Answer**: displacement 0 m · distance 2 m · avg velocity 0 m/h · avg speed $\frac{2}{\pi}\approx0.637$ m/h; the FTC needs a signed rate

---

## Answer Check

| Problem | Answer |
|:---:|:---|
| P1 | 225 L both ways |
| P2 | 20 °C · 480 °C·h |
| P3 | 0.9 J · 0.7 J |
| P4 | (20, 60) · CS 600 · PS 400 |
| P5 | ≈ \$688,339 |
| P6 | 1 ✓ · 0.875 · 7.5 yr · $P(X=5)=0$ |
| D1 | m · L · J · \$ |
| D2 | ≈ 43.2 L |
| D3 | $\frac{16}{3}$ |
| D4 | 2 J |
| D5 | 10 m |
| D6 | $\frac12$ · 4 |
| D7 | $\frac{32}{3}$ (cm²) |
| D8 | \$400 |
| D9 | ≈ \$6,321 |
| D10 | $\frac23$ |
| A1 | three translations |
| A2 | 52 J |
| A3 | ≈ 831 kJ |
| A4 | $c=\frac{4}{\sqrt3}\approx2.31$ |
| A5 | $\frac{1250}{3}\approx416.67$ |
| A6 | $\frac{R}{r}(1-e^{-rT})$; $\frac{R}{r}$ |
| A7 | $0.707 > \frac23$ |
| A8 | 1 ✓ · $e^{-2}$ · $\frac12$ |
| A9 | area / avg×len / total change |
| A10 | $4\pi r^2c$ · $\frac43\pi R^3$ · cubic |
| DI1 | disp 0 · dist 2 · avg vel 0 · avg speed $2/\pi$ |
