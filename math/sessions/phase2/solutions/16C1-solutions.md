# Solutions — 16C1: Integral Interpretation

> Back to [16C1 — Integral Interpretation](../16C1-integral-interpretation.md)

---

## Practice 1

**(a)** $\int_0^{15}(30-2t)dt = \left[30t - t^2\right]_0^{15} = 450 - 225 = 225$ L.

**(b)** Rate table: $30, 20, 10, 0$ L/min at $t = 0, 5, 10, 15$. Trapezoids:

$\frac{30+20}{2}\cdot 5 + \frac{20+10}{2}\cdot 5 + \frac{10+0}{2}\cdot 5 = 125 + 75 + 25 = 225$ L.

Both methods agree because the rate is linear — trapezoids on a line are exact.

> **Answer**: 225 L by both methods

**Lens reading**: the total is the collected relation of flow to time — every strip is the rate's degree at that instant times one instant of the driver.

---

## Practice 2

**(a)** $\bar{T} = \frac{1}{24}\int_0^{24}\left(20 + 10\sin\frac{\pi t}{12}\right)dt = \frac{1}{24}\left[20t\right]_0^{24} = 20$ °C (the sine integrates to zero over a full period).

**(b)** Total degree-hours $= \bar{T}\cdot 24 = 480$ °C·h.

**(c)** The rectangle $[0,24]\times 20$ has the same area as the day's temperature curve: the warm afternoon lobe (above 20) exactly balances the cool night lobe (below 20). The average is the flat temperature that would deliver the same total heat.

> **Answer**: (a) 20 °C (b) 480 °C·h

**Lens reading**: 480 °C·h is the collected temperature-time relation; dividing by the span gives the uniform degree 20 °C that delivers the same total.

---

## Practice 3

**(a)** $W = \int_0^{0.3}20x\,dx = \left[10x^2\right]_0^{0.3} = 0.9$ J.

**(b)** $W = \int_{0.3}^{0.4}20x\,dx = 10(0.16-0.09) = 0.7$ J.

**(c)** The second stretch is only one third as long yet costs 0.7 J — because the spring is already pulling with 6 N when the second stretch begins. Work is the *area* under the force curve, and the area is higher up where the force is bigger.

> **Answer**: (a) 0.9 J (b) 0.7 J (c) force already 6 N at the start

**Lens reading**: work is the collected force-stretch relation — 0.9 J for the first stretch but 0.7 J for the next 0.1 m, because the relation's degree had already grown.

---

## Practice 4

Equilibrium: $120-3q = 20+2q$ → $q^* = 20$, $p^* = 60$.

$CS = \int_0^{20}(120-3q-60)dq = \left[60q - \frac32 q^2\right]_0^{20} = 1200 - 600 = 600$.

$PS = \int_0^{20}(60-20-2q)dq = \left[40q - q^2\right]_0^{20} = 800 - 400 = 400$.

> **Answer**: equilibrium $(20,\,60)$; CS = 600, PS = 400 (total welfare 1000)

**Lens reading**: surplus collects the relation between willingness and price — buyers keep the gap, sellers keep the margin: two money triangles.

---

## Practice 5: Real Battle — A Growing Income Stream

$PV = \int_0^{20} 50{,}000\,e^{0.02t}e^{-0.06t}dt = 50{,}000\int_0^{20}e^{-0.04t}dt = 50{,}000\cdot\frac{1-e^{-0.8}}{0.04} \approx 688{,}339$ \$.

The income grows at 2% but money loses value at 6% per year — the *net* discount rate is 4%, and the integrand still decays. A dollar 20 years out is worth $e^{-0.8} \approx 45\%$ of a dollar today, growth or no growth. That is why the \$1.1M of raw payments is worth only ≈\$688K now.

> **Answer**: PV ≈ \$688,339

**Lens reading**: discounting is money's relation to time — each instant's dollar is worth $e^{-rt}$; collecting that decaying relation gives today's value.

---

## Practice 6: Real Battle — Battery Lifetime

**(a)** $\int_0^{10}\frac{3x^2}{1000}dx = \frac{1000}{1000} = 1$ ✓.

**(b)** $P(X>5) = \int_5^{10}\frac{3x^2}{1000}dx = \frac{1000-125}{1000} = 0.875$.

**(c)** $E[X] = \int_0^{10}x\cdot\frac{3x^2}{1000}dx = \frac{3\cdot 10^4}{4000} = 7.5$ years.

**(d)** $P(X=5) = \int_5^5 p(x)dx = 0$: a single point has zero width, so its area is zero. The density *at* 5 is a rate (probability per year), not a probability. Only intervals accumulate positive probability.

> **Answer**: (a) 1 ✓ (b) 0.875 (c) 7.5 yr (d) $P(X=5)=0$

**Lens reading**: the density is probability's relation to time — intervals collect positive area, single points collect none; expectation balances the collected area.

---

## Integral Practice

### RPB1.

**(a)** $V = \int_0^{15}(60-4t)\,dt$.

**(b)** $[60t-2t^2]_0^{15} = 900 - 450 = 450$ L.

**(c)** "Over 15 minutes the pump delivers 450 liters" — (L/min) × min = L.

**(d)** The rate falls linearly from 60 to 0, so the area is the trapezoid $\frac{60+0}{2}\cdot 15 = 450$ L. Each thin strip is (L/min) × (a small number of minutes) = a small volume; the integral stacks the strips.

**Lens reading**: the total is the collected relation of flow to time — the rate's degree weakens from 60 to 0 L/min, and the total is the average degree (30) × the driver span (15 min).

> **Answer**: 450 L

### RPB2.

**(a)** $\int_0^4 3t^2\,dt = [t^3]_0^4 = 64$ m.

**(b)** "In 4 seconds the particle travels 64 m" — (m/s) × s = m.

**(c)** $\frac{d}{dt}t^3 = 3t^2 = v(t)$ — differentiating the total reads the rate back: distance's degree of relation to time is velocity.

> **Answer**: 64 m; undo reads $v$ back

**Lens reading**: distance's degree of relation to time is the velocity — collecting it gives 64 m, and the undo reads the relation back.

### RPB3.

**(a)** $\int_0^{10}(2q+1)\,dq = [q^2+q]_0^{10} = 110$.

**(b)** Each thin strip is (cost of one more item) × (one item) = dollars added by that one item; stacking the strips totals the added cost.

**(c)** "Producing the first 10 items adds \$110 of cost."

**Lens reading**: marginal cost is cost's degree of relation to quantity; the integral collects that relation back into total cost.

> **Answer**: \$110

### RPB4.

**(a)** $\bar f = \frac13\int_0^3 x^2\,dx = \frac13\cdot 9 = 3$.

**(b)** The rectangle $[0,3]\times 3$ has the same area as the parabola — the average is the *uniform* relation that delivers the same total.

> **Answer**: 3

**Lens reading**: the average 3 is the uniform relation delivering the parabola's total — the equal-area rectangle's height.

### RPB5.

**(a)** $W = \int_0^8 5\,dx = 40$ J.

**(b)** The force's relation to distance is uniform — 5 N everywhere — so the total is the rectangle 5 × 8. No triangle, because the relation never grows: each meter buys the same 5 J.

> **Answer**: 40 J

**Lens reading**: a uniform relation collects into a rectangle — 5 N every meter, 40 J.

### RPA1.

**(a)** $F(x) = kx$: force's degree of relation to stretch is $k$, and the relation grows linearly from zero.

**(b)** $W = \int_0^x kx\,dx = \frac12 kx^2$.

**(c)** $\frac{dW}{dx} = kx = F(x)$ ✓ — work's degree of relation to stretch is the force.

**(d)** The last centimeter is pulled against the fully built tension. Each step costs the *current* force, so the total is the triangle: half of final × final.

> **Answer**: $W = \frac12 kx^2$; undo ✓

**Lens reading**: the growing force relation collects into a triangle — half of final × final; the undo reads the force back off the work.

### RPA2.

**(a)** Slice at depth $y$ below the top: the segment $dy$ has weight $\rho g\,dy$ and must climb $y$ meters. $W = \int_0^{30}\rho g\,y\,dy$.

**(b)** $20\cdot 9.8\left[\frac{y^2}{2}\right]_0^{30} = 196\cdot 450 = 88{,}200$ J ≈ 88.2 kJ.

**(c)** The bottom segment climbs the full 30 m — distance, not weight, decides the fare, so the deepest slice pays the most.

> **Answer**: 88,200 J ≈ 88.2 kJ

**Lens reading**: each rope segment's fare is its own height relation — the bottom segment climbs the full 30 m and pays the most.

### RPA3.

**(a)** $PV = \int_0^\infty R_0 e^{gt}e^{-rt}dt = R_0\int_0^\infty e^{(g-r)t}dt$.

**(b)** $= \left[\frac{R_0}{g-r}e^{(g-r)t}\right]_0^\infty = \frac{R_0}{r-g}$ for $r>g$. The denominator is a **difference of two percentage relations** — growth minus discount — a ratio hearing the difference of rates (14D1B's lesson, in integral form).

**(c)** $\frac{1000}{0.08-0.03} = 20{,}000$.

> **Answer**: $\frac{R_0}{r-g}$; \$20,000

**Lens reading**: the perpetuity's value is the difference of two percentage relations — growth minus discount, sitting in the denominator.

### RPA4.

**(a)** $\int_0^\infty \lambda e^{-\lambda t}dt = [-e^{-\lambda t}]_0^\infty = 1$ ✓.

**(b)** $P(X>1) = \int_1^\infty \lambda e^{-\lambda t}dt = e^{-\lambda}$: "the chance of surviving past 1 unit is the discount factor itself — the density's remaining relation."

**(c)** $E[X] = \int_0^\infty t\,\lambda e^{-\lambda t}dt$; parts with $u=t$, $dv = \lambda e^{-\lambda t}dt$: $[-te^{-\lambda t}]_0^\infty + \int_0^\infty e^{-\lambda t}dt = 0 + \frac1\lambda$.

**(d)** $\lambda=2$: $P(X>1) = e^{-2} \approx 0.135$; $E[X] = 0.5$.

> **Answer**: 1 ✓; $e^{-\lambda}$; $\frac1\lambda$

**Lens reading**: the survival probability is the density's remaining relation; expectation is its balance point — $\frac1\lambda$.

### RPA5.

**(a)** Displacement $= \int_0^4(t^2-4t+3)\,dt = \left[\frac{t^3}{3}-2t^2+3t\right]_0^4 = \frac{64}{3}-32+12 = \frac43$ m.

**(b)** $v = (t-1)(t-3)$: positive on $[0,1]$ and $[3,4]$, negative on $[1,3]$. Distance $= \frac43 + \frac43 + \frac43 = 4$ m.

**(c)** The FTC owns **displacement** — the signed rate's integral is the total change of position. Distance needs the unsigned rate $|v|$, which has corners where the sign flips: split the domain there (the same break as DI1).

> **Answer**: displacement $\frac43$ m; distance 4 m; FTC = signed rates only

**Lens reading**: displacement is the signed relation's total; distance needs the unsigned relation, split where the sign flips.

---

## Basic Drills

### D1.

> **Answer**: (a) m (b) L (c) J = N·m (d) \$ (dollars, since \$/unit × units)

**Lens reading**: four integrals, four collected relations — m, L, J, \$: the units are the relation's signature.

### D2.

$\int_0^{20}5e^{-t/10}dt = 50(1-e^{-2}) \approx 43.23$ L.

> **Answer**: ≈ 43.2 L

**Lens reading**: the leak's relation to time decays with degree $-1/10$; collecting it over 20 minutes gives ≈43.2 L.

### D3.

$\bar{f} = \frac{1}{4}\int_0^4 x^2 dx = \frac{1}{4}\cdot\frac{64}{3} = \frac{16}{3}$.

> **Answer**: $\frac{16}{3}$

**Lens reading**: the average of $x^2$ over $[0,4]$ is the uniform relation delivering the same total — $\frac{16}{3}$.

### D4.

$W = \frac12 kx^2 = \frac12\cdot 100\cdot(0.2)^2 = 2$ J.

> **Answer**: 2 J

**Lens reading**: a constant force is a uniform relation; collecting 1 N over 2 m gives 2 J.

### D5.

$\int_0^2(3t^2+1)dt = [t^3+t]_0^2 = 10$ m.

> **Answer**: 10 m

**Lens reading**: displacement collects the signed velocity relation; splitting at the sign flips converts it to distance — 10 m.

### D6.

Density $\frac18$ on $[0,8]$. $P(2<X<6) = 4\cdot\frac18 = \frac12$. $E[X] = 4$ (midpoint).

> **Answer**: $P = \frac12$, $E[X]=4$

**Lens reading**: the density's total relation is 1 (all outcomes); the expectation balances the collected area at 4.

### D7.

$\int_{-2}^2(4-x^2)dx = \left[4x-\frac{x^3}{3}\right]_{-2}^2 = \left(8-\frac83\right)-\left(-8+\frac83\right) = \frac{32}{3}$.

> **Answer**: $\frac{32}{3}$; with cm axes it is $\frac{32}{3}$ cm² — the true area under the parabola

**Lens reading**: $\int x^2 dx$ is the parabola's collected relation; with cm axes the units name the same relation in cm².

### D8.

$q^* = 20$ at price 20 ($60-2q=20$). $CS = \int_0^{20}(60-2q-20)dq = \left[40q-q^2\right]_0^{20} = 400$.

> **Answer**: CS = \$400

**Lens reading**: consumer surplus collects the willingness gap — the buyers' saved relation, stacked.

### D9.

$PV = 1000\cdot\frac{1-e^{-1}}{0.1} \approx 6321.21$ \$.

> **Answer**: ≈ \$6,321

**Lens reading**: present value collects the discounted stream — money's relation to time, run backwards.

### D10.

$E[X] = \int_0^1 x\cdot 2x\,dx = \left[\frac{2x^3}{3}\right]_0^1 = \frac23$.

> **Answer**: $\frac23$

**Lens reading**: the balance point of the density's collected area — where the relation has delivered half.

---

## Advanced Drills

### A1.

- Population: "the total births between $a$ and $b$ equal the population at $b$ minus the population at $a$."
- Tank: "the total inflow between $a$ and $b$ equals the volume at $b$ minus the volume at $a$."
- Account: "the total interest earned between $a$ and $b$ equals the balance at $b$ minus the balance at $a$."

> **Answer**: three instances of "total change = final − initial"

**Lens reading**: the FTC in three costumes — population, tank, bank: every total is a collected relation, and every answer is final minus initial.

### A2.

$W = \int_1^3 6x^2 dx = [2x^3]_1^3 = 54 - 2 = 52$ J. Check: $\frac{d}{dx}(2x^3) = 6x^2 = F(x)$ ✓ — differentiating the work function recovers the force. Units: N·m = J.

> **Answer**: 52 J; $dW/dx = F$ ✓

**Lens reading**: work is the collected force relation; the undo button reads it back — $\frac{dW}{dx} = F$ ✓.

### A3.

At height $h$ from the bottom the radius is $r = \frac{h}{2}$ (similar triangles). Layer volume $= \pi r^2 dh = \pi\frac{h^2}{4}dh$; weight $= 9800\,\pi\frac{h^2}{4}dh$; travel distance $= 6-h$.

$W = \int_0^6 9800\,\pi\,\frac{h^2}{4}(6-h)\,dh = \frac{9800\pi}{4}\int_0^6(6h^2-h^3)dh = \frac{9800\pi}{4}\left(2\cdot 216 - \frac{1296}{4}\right) = 9800\pi\cdot 27 \approx 831{,}265$ J ≈ 831 kJ.

The lower layers dominate: the deepest layer is widest ($r$ largest), heaviest, *and* travels the full 6 m. All three factors grow with depth.

> **Answer**: $W = 27\pi\rho g \approx 831$ kJ

**Lens reading**: the cone's radius relation ($r = h/2$) weights each layer's area; the deepest layers collect the most because their fare — distance to the rim — is largest.

### A4.

Average of $x^2$ on $[0,4]$ is $\frac{16}{3}$. The theorem guarantees a $c$ with $f(c) = \frac{16}{3}$: $c^2 = \frac{16}{3}$ → $c = \frac{4}{\sqrt3} \approx 2.31 \in [0,4]$ ✓.

Meaning: no continuous function can stay entirely above (or below) its average — some instant achieves exactly the average height, just as the mean value theorem guarantees some instant with exactly the average slope.

> **Answer**: $c = \frac{4}{\sqrt3} \approx 2.31$

**Lens reading**: the MVT for integrals says some single instant carries the average degree — the relation's average is attained at one point.

### A5.

Free equilibrium: $200-2q = q$ → $q^* = \frac{200}{3} \approx 66.67$. The quota bans production between 50 and $q^*$, killing trades worth $D(q)-S(q) = 200-3q$ each.

$DWL = \int_{50}^{200/3}(200-3q)dq = \left[200q-\frac32 q^2\right]_{50}^{200/3} = \frac{20000}{3} - 6250 = \frac{1250}{3} \approx 416.67$.

It measures the trades that would have benefited both sides (buyers willing to pay more than sellers demand) but are now illegal — pure lost value, received by no one.

> **Answer**: DWL $= \frac{1250}{3} \approx \$416.67$

**Lens reading**: deadweight loss collects the banned trades — the relation between willingness and supply that the quota cuts.

### A6.

$PV(T) = \int_0^T Re^{-rt}dt = \frac{R}{r}(1-e^{-rT})$.

As $T\to\infty$: $PV = \frac{R}{r}$. At 5%, a perpetual stream of \$1/yr is worth \$20 today — twenty years of income in one lump, because dollars far in the future are worth almost nothing. The perpetuity price is the natural cap that all finite streams approach.

> **Answer**: $PV(T) = \frac{R}{r}(1-e^{-rT})$; perpetuity $\frac{R}{r}$

**Lens reading**: the perpetuity is the limit where the discount relation collects forever — $\frac{R}{r}$, twenty years of income at 5%.

### A7.

Median: $\int_0^m 2x\,dx = m^2 = \frac12$ → $m = \frac{1}{\sqrt2} \approx 0.707$.

Mean: $\frac23 \approx 0.667$. The median is larger because the density $2x$ rises with $x$ — more probability mass sits on the right. The mean balances the *mass* (so it chases the heavy right tail), while the median only asks where the *area* halves; with mass piled at the top end, half the area is reached only past the mean.

> **Answer**: median $\frac{1}{\sqrt2} \approx 0.707 > \frac23$ — the density leans right

**Lens reading**: the median is where the density's collected area halves; the mean chases the heavy tail — two balance points of one relation.

### A8.

**(a)** $\int_0^\infty 2e^{-2x}dx = [-e^{-2x}]_0^\infty = 1$ ✓.

**(b)** $P(X>1) = \int_1^\infty 2e^{-2x}dx = e^{-2} \approx 0.1353$.

**(c)** $E[X] = \int_0^\infty x\cdot 2e^{-2x}dx = \frac12$ (by parts: $\left[-x e^{-2x}\right]_0^\infty + \int_0^\infty e^{-2x}dx = 0 + \frac12$).

**(d)** The survival probability decays as $e^{-2x}$: the chance of lasting past 1 is $e^{-2}$ because the density itself is exponential — every unit of time kills a constant fraction (2 per unit) of the survivors. It is the same memoryless pattern as radioactive decay and continuously compounded discounting.

> **Answer**: (a) 1 ✓ (b) $e^{-2}\approx0.135$ (c) $\frac12$

**Lens reading**: the survival chance $e^{-2}$ is the density's remaining collected relation past 1; parts balances its expectation at $\frac12$.

### A9.

**(a) Area**: $\frac13$ is the area between $y=x^2$ and the $x$-axis on $[0,1]$.

**(b) Average × length**: the average of $x^2$ on $[0,1]$ is $\frac13$, and $1 \cdot \frac13 = \frac13$ — the area of the equal-height rectangle.

**(c) Total change**: $F(x)=\frac{x^3}{3}$ has $F'=x^2$; the integral is $F(1)-F(0)$ — the accumulation between 0 and 1 of a quantity whose rate is $x^2$.

"Which picture?" matters because each gives different units and a different sentence: geometric area, summary statistic, or accumulated total. The math is one number; the meaning is chosen by the picture.

> **Answer**: one number, three meanings — area / average×length / total change

**Lens reading**: one integral, three relations — area, average × length, total change: which picture depends on which relation you read.

### A10.

**(a)** Chain rule: $\frac{dV}{dt} = \frac{dV}{dr}\cdot\frac{dr}{dt} = 4\pi r^2\cdot c$ — the surface area times the radial speed. The snowball adds a shell of thickness $c\,dt$ each instant.

**(b)** $\int_0^R 4\pi r^2 dr = \frac{4}{3}\pi R^3 = V(R)$ — integrating the shell areas rebuilds the volume. Integration and differentiation are the same sphere seen from opposite directions.

**(c)** $r = ct$, so $V(t) = \frac{4}{3}\pi(ct)^3$ — volume grows **cubically** in time even though the radius grows only linearly. A constant radial growth rate is an exploding volume growth rate.

> **Answer**: (a) $4\pi r^2 c$ (b) $\frac43\pi R^3$ ✓ (c) $V(t)=\frac43\pi(ct)^3$ — cubic

**Lens reading**: volume's relation to radius is the surface — collected, it rebuilds the sphere; with $r=ct$ the relation to time is cubic.

---

## Deep Insight

### DI1.

**(a)** Displacement $= \int_0^\pi\cos t\,dt = \sin\pi-\sin0 = 0$ m — the boat ends where it started.

**(b)** Distance $= \int_0^\pi|\cos t|\,dt = \int_0^{\pi/2}\cos t\,dt - \int_{\pi/2}^{\pi}\cos t\,dt = 1+1 = 2$ m.

**(c)** Average velocity $= \frac{0}{\pi} = 0$ m/h.

**(d)** Average speed $= \frac{2}{\pi} \approx 0.637$ m/h.

The FTC pair: (a) and (c) — displacement is the integral of the *signed* rate, and the average velocity is that integral divided by time. The failing pair: (b) and (d). $|\cos t|$ is not the derivative of any smooth position function — it has a corner where the sign flips, so $\int|v|$ cannot be written $F(\pi)-F(0)$ of one natural $F$. **The FTC is a theorem about signed rates.** Unsigned totals (distance, total outflow regardless of direction) need the absolute value — and the absolute value is precisely where the theorem refuses to work: split the domain at every sign change. Deciding which total is asked (signed vs unsigned) is the first interpretation move of every rate integral.

> **Answer**: displacement 0 m · distance 2 m · avg velocity 0 m/h · avg speed $\frac{2}{\pi}\approx0.637$ m/h; the FTC needs a signed rate

**Lens reading**: the FTC owns signed relations only — $|v|$ breaks the undo button; deciding which total (signed vs unsigned) the question asks is the first relation-reading move.

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
| RPB1 | 450 L |
| RPB2 | 64 m |
| RPB3 | \$110 |
| RPB4 | 3 |
| RPB5 | 40 J |
| RPA1 | $\frac12 kx^2$ |
| RPA2 | 88,200 J |
| RPA3 | $\frac{R_0}{r-g}$; \$20,000 |
| RPA4 | 1 ✓ · $e^{-\lambda}$ · $\frac1\lambda$ |
| RPA5 | $\frac43$ m · 4 m · FTC=signed |
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
