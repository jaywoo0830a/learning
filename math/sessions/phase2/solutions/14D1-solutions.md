# Solutions — 14D1: Derivative Interpretation

> Back to [14D1 — Derivative Interpretation](../14D1-derivative-interpretation.md)

---

## Practice 1

| Derivative | Units | One-sentence meaning |
|:---:|:---:|:---|
| $V'(t)$ | L/min | "each minute adds about $V'$ liters of volume." |
| $P'(t)$ | people/yr | "each year the population grows by about $P'$ people." |
| $T'(x)$ | °C/m | "each meter deeper, the water is about $T'$ degrees colder." |
| $W'(q)$ | kg/item | "each extra item weighs about $W'$ kilograms." |

> **Answer**: units = y-units ÷ x-units, and the sentence always starts with "each extra …".

---

## Practice 2

$v(t) = (t-2)(t-4)$, $a(t) = 2t-6$. Turning points: $v=0$ at $t=2, 4$. Acceleration switch: $a=0$ at $t=3$.

| Interval | $v$ | $a$ | Story |
|:---:|:---:|:---:|:---|
| $0<t<2$ | $+$ | $-$ | forward, slowing |
| $2<t<3$ | $-$ | $-$ | backward, speeding up |
| $3<t<4$ | $-$ | $+$ | backward, slowing |
| $4<t<6$ | $+$ | $+$ | forward, speeding up |

> **Answer**: turns at $t=2$ (forward→backward) and $t=4$ (backward→forward); the speed story flips at $t=3$.

---

## Practice 3

$f(9)=3$, $f'(x)=\frac{1}{2\sqrt{x}}$, so $f'(9)=\frac16$.

$L(x) = 3 + \frac{1}{6}(x-9)$, so $L(9.3) = 3 + \frac{0.3}{6} = 3.05$.

True value $\sqrt{9.3} = 3.04959\ldots$, error $= 0.00041$.

Bound: $f''(x) = -\frac{1}{4x^{3/2}}$, largest magnitude on $[9,\,9.3]$ at $x=9$: $M = \frac{1}{4\cdot 27} = \frac{1}{108}$.

$|error| \le \frac{M}{2}(0.3)^2 = \frac{1}{216}\cdot 0.09 = 0.000417$ ✓ (true error 0.00041 sits inside).

> **Answer**: $\sqrt{9.3} \approx 3.05$, error $\le 0.000417$ (true ≈ 0.00041)

---

## Practice 4

**(a)** $C'(q) = 2q+4$, so $C'(20) = 44$ \$/unit. Sentence: "at 20 units, the 21st unit costs about \$44."

**(b)** $C(20) = 624$. Estimate: $C(21) \approx 624 + 44 = 668$. Exact: $C(21) = 21^2+84+144 = 669$. The \$1 gap is the second-order curvature term $\frac12 C'' = \frac12\cdot 2 = 1$.

**(c)** $MC = AC$: $2q+4 = q+4+\frac{144}{q}$ → $q^2 = 144$ → $q = 12$. Check: $MC(12)=28$, $AC(12)=12+4+12=28$ ✓.

> **Answer**: (a) \$44/unit (b) ≈\$668 vs exact \$669 (c) $q=12$, where $MC=AC=28$

---

## Practice 5: Real Battle — The Inflating Balloon

**(a)** $\frac{dV}{dr} = 4\pi r^2$. At $r=5$: $4\pi\cdot 25 = 100\pi \approx 314$ cm³ per cm. Geometrically it is the **surface area** — a 1-cm-thick shell holds about 314 cm³.

**(b)** Chain rule: $\frac{dV}{dt} = \frac{dV}{dr}\cdot\frac{dr}{dt}$, so $\frac{dr}{dt} = \frac{8}{100\pi} \approx 0.0255$ cm/s.

**(c)** $\frac{dV}{dr}$ measures growth *per unit of radius* — how much volume comes with being bigger. $\frac{dV}{dt}$ measures growth *per unit of time* — how fast air is arriving. Both answer "how fast is the balloon growing," for two different "with respect to"s.

> **Answer**: (a) $100\pi \approx 314$ cm³/cm = surface area (b) $\frac{8}{100\pi} \approx 0.0255$ cm/s

---

## Practice 6: Real Battle — Pricing with Elasticity

**(a)** $\frac{dq}{dp} = -8$.
- $p=30$: $q=160$, $E = \frac{30}{160}(-8) = -\frac32 = -1.5$.
- $p=10$: $q=320$, $E = \frac{10}{320}(-8) = -0.25$.

**(b)** At $p=30$: $|E|=1.5>1$ (elastic) — 1% price rise costs 1.5% of demand: revenue **falls**. At $p=10$: $|E|=0.25<1$ (inelastic) — revenue **rises**.

**(c)** $R = 400p - 8p^2$, $R' = 400-16p = 0$ → $p=25$, $q=200$, $R=\$5000$. At that price $E = \frac{25}{200}(-8) = -1$ ✓.

> **Answer**: (a) $E=-1.5$ at $p=30$, $E=-0.25$ at $p=10$ (b) revenue falls at 30, rises at 10 (c) max revenue \$5000 at $p=25$ ($E=-1$)

---

## Relationship Practice

### RP1.

**(a)** $F(d) = 4 + 2d$ (\$). $\frac{dF}{dd} = 2$ \$/km.

**(b)** "Each kilometer of the ride buys \$2 of fare."

**(c)** A constant degree means the relation is *uniform* — the \$2/km never changes, so the relation has the same strength everywhere. (Most real relations are not uniform; that is exactly why the derivative is usually not constant.)

> **Answer**: $F = 4 + 2d$; $2$ \$/km; uniform relation

### RP2.

**(a)** $A(s) = s^2$. $\frac{dA}{ds} = 2s$; at $s=5$: $10$ cm²/cm.

**(b)** "At side 5 cm, each extra cm of side buys about 10 cm² of area."

**(c)** At $s=20$: $40$ cm²/cm — four times stronger. The degree of relation is *local*: a bigger plate has a longer boundary, so each cm of side adds a wider strip of area. The relation's strength depends on where you are.

> **Answer**: $10$ cm²/cm at $s=5$; $40$ cm²/cm at $s=20$ — the relation strengthens with size

### RP3.

**(a)** $f(d) = 0.08d$ L. $\frac{df}{dd} = 0.08$ L/km: "each km of driving burns 0.08 L."

**(b)** Invert: $d(f) = 12.5f$ km. $\frac{dd}{df} = 12.5$ km/L: "each liter of fuel buys 12.5 km."

**(c)** $0.08 \times 12.5 = 1$ ✓ — reciprocals. Two numbers, one relation: the consumption direction (L/km) and the mileage direction (km/L) are the same relationship read in reverse.

> **Answer**: $0.08$ L/km ↔ $12.5$ km/L, reciprocals

### RP4.

**(a)** Relation 1: $P(T) = 0.4T$, degree $\frac{dP}{dT} = 0.4$ kPa/K. Relation 2: $T(t) = 300 + 2t$, degree $\frac{dT}{dt} = 2$ K/s.

**(b)** Chain: $\frac{dP}{dt} = \frac{dP}{dT}\cdot\frac{dT}{dt} = 0.4 \times 2 = 0.8$ kPa/s. Units multiply through: $\frac{\mathrm{kPa}}{\mathrm{K}}\cdot\frac{\mathrm{K}}{\mathrm{s}} = \frac{\mathrm{kPa}}{\mathrm{s}}$ — the K cancels, exactly as it should.

**(c)** "Each second of heating raises the pressure by 0.8 kPa." The pressure–time relation is the *product* of the two chained degrees — relations chain by multiplication.

> **Answer**: $0.4$ kPa/K and $2$ K/s; chained degree $0.8$ kPa/s

### Basic RP Drills

#### RPB1.

**(a)** $V(t) = 50 + 12t$ L.

**(b)** $\frac{dV}{dt} = 12$ L/min: "each minute of pumping adds 12 L."

**(c)** The degree is constant because the relation is linear — a uniform relation: 12 L/min everywhere, regardless of how much water is already in the tank.

> **Answer**: $V = 50 + 12t$; $12$ L/min, uniform

#### RPB2.

**(a)** $A(s) = \frac{\sqrt3}{4}s^2$ cm².

**(b)** $\frac{dA}{ds} = \frac{\sqrt3}{2}s$. At $s=4$: $2\sqrt3 \approx 3.46$ cm²/cm: "at side 4 cm, each extra cm of side buys about 3.46 cm² of area."

**(c)** At $s=10$: $5\sqrt3 \approx 8.66$ cm²/cm — over twice as strong. The relation is local: a bigger triangle has a longer boundary, so each cm of side adds a wider strip of area.

> **Answer**: $2\sqrt3 \approx 3.46$ cm²/cm at $s=4$; $5\sqrt3 \approx 8.66$ at $s=10$

#### RPB3.

**(a)** $t(v) = \frac{120}{v}$ hours.

**(b)** $\frac{dt}{dv} = -\frac{120}{v^2}$. At $v=60$: $-\frac{120}{3600} = -\frac{1}{30}$ h per km/h = 2 minutes per km/h: "at 60 km/h, each extra km/h shaves 2 minutes off the trip."

**(c)** The minus sign says the two quantities move in opposite directions — more speed, less time. At $v=90$: $-\frac{120}{8100} \approx -0.0148$ h per km/h ≈ 0.89 min — weaker, because once the trip is already short, each km/h matters less. Same relation, different strength (local).

> **Answer**: $-\frac{1}{30}$ h/(km/h) = −2 min/(km/h) at $v=60$; weaker at $v=90$

#### RPB4.

**(a)** $C(w) = 3w$; $\frac{dC}{dw} = 3$ \$/kg: "each extra kg costs \$3."

**(b)** $w(C) = \frac{C}{3}$; $\frac{dw}{dC} = \frac13$ kg/\$: "each extra dollar buys one third of a kg."

**(c)** $3 \times \frac13 = 1$ ✓ — the two directions of one relation are reciprocals.

> **Answer**: $3$ \$/kg ↔ $\frac13$ kg/\$

#### RPB5.

**(a)** $\frac{dd}{dt} = 9.8t$. At $t=2$: $19.6$ m/s — **velocity**: the degree of relation between distance and time has its own name.

**(b)** At $t=5$: $49$ m/s.

**(c)** The relation strengthens as the rock falls: each additional second buys more distance than the previous one. The degree of relation is not a property of "distance vs time" in general — it is a property of the relation *at that instant*.

> **Answer**: $19.6$ m/s at $t=2$; $49$ m/s at $t=5$ — velocity, local

### Advanced RP Drills

#### RPA1.

**(a)** $S(x) = 2x^2 + 4(10x) = 2x^2 + 40x$ cm².

**(b)** $\frac{dS}{dx} = 4x + 40$; at $x=5$: $60$ cm²/cm.

**(c)** $C(x) = 0.02\,S(x) = 0.04x^2 + 0.8x$; $\frac{dC}{dx} = 0.02(4x+40) = 0.08x + 0.8$; at $x=5$: $1.2$ \$/cm. The units chain: $\left(\frac{\$}{\mathrm{cm^2}}\right)\!\left(\frac{\mathrm{cm^2}}{\mathrm{cm}}\right) = \frac{\$}{\mathrm{cm}}$ — the two relations (surface ↔ side, cost ↔ surface) chain by multiplying their degrees.

**(d)** "At side 5 cm, each extra cm of side costs about \$1.20 of material."

> **Answer**: $S = 2x^2+40x$; $\frac{dS}{dx} = 60$ cm²/cm; $\frac{dC}{dx} = 1.2$ \$/cm

#### RPA2.

**(a)** $R(p) = p(200 - 5p) = 200p - 5p^2$. $\frac{dR}{dp} = 200 - 10p$; at $p=10$: $100$ \$/\$ — each dollar of price buys 100 dollars of revenue.

**(b)** "At \$10, raising the price by one dollar raises revenue by about \$100." (The degree of relation here is unitless: dollars per dollar.)

**(c)** Zero at $p=20$: revenue stops responding to price — momentarily flat, the peak ($R = 2000$). Degree zero is not "no relation" (🔗 A9) — it is the relation at rest, for one instant.

> **Answer**: $\frac{dR}{dp} = 200-10p$; $100$ \$/\$ at $p=10$; zero at $p=20$ = peak

#### RPA3.

**(a)** $P(R) = \frac{14400}{R}$; $\frac{dP}{dR} = -\frac{14400}{R^2}$. At $R=60$: $-4$ W/Ω.

**(b)** "At 60 Ω, each extra ohm of resistance costs 4 W of power." Negative: resistance and power move in opposite directions — the relation is inverse.

**(c)** $P(60) = \frac{14400}{60} = 240$ W. $E = \frac{R}{P}\frac{dP}{dR} = \frac{60}{240}(-4) = -1$. Reading: "1% of resistance buys exactly −1% of power." The dimensionless degree is unit elastic at *every* resistance, because $P \propto R^{-1}$ — the percentage form exposes a uniformity that the raw $-4$ W/Ω hides.

> **Answer**: $-4$ W/Ω at $R=60$; $E = -1$ (unit elastic, everywhere)

#### RPA4.

**(a)** Width $x$ (two sides of length $x$), river side $200 - 2x$: $A(x) = x(200 - 2x) = 200x - 2x^2$ m².

**(b)** $\frac{dA}{dx} = 200 - 4x$; at $x=20$: $120$ m²/m: "at width 20 m, each extra meter of width buys about 120 m² of pen."

**(c)** Zero at $x=50$: the degree vanishes — area stops responding to width. There the pen is 50 m × 100 m, $A = 5000$ m² — the maximum. Degree zero is the relation's turning point (🔗 A9).

> **Answer**: $\frac{dA}{dx} = 200-4x$; $120$ m²/m at $x=20$; zero at $x=50$ (max 5000 m²)

#### RPA5.

**(a)** $V(t) = 0.1t$ mL; $\frac{dV}{dt} = 0.1$ mL/s: "each second, 0.1 mL of water leaves."

**(b)** $0.1 \frac{\mathrm{mL}}{\mathrm{s}} \times 3600 \frac{\mathrm{s}}{\mathrm{h}} \times 24 \frac{\mathrm{h}}{\mathrm{day}} \times 365 \frac{\mathrm{day}}{\mathrm{yr}} = 3{,}153{,}600$ mL/yr ≈ 3,154 L/yr.

**(c)** Relations chain by multiplying degrees — and unit conversions are relations too: each conversion factor is a degree of relation between two units, and the units cancel exactly like the chain rule's factors do. A two-drops-per-second drip wastes over three tons of water a year.

> **Answer**: $0.1$ mL/s ≈ 3,154 L/yr

---

## Basic Drills

### D1.

> **Answer**: (a) mi/hr (b) \$/item (c) bacteria/min (d) N/m

### D2.

$v = 3(t-1)(t-3)$. The sign is negative between the roots.

> **Answer**: backward on $1 < t < 3$

### D3.

$L(x) = 1 + x$ at $a=0$: $e^{0.05} \approx 1.05$ (true $1.051271\ldots$). On $[0,0.05]$, $f''=e^x$ is largest at the right end: $M = e^{0.05} \approx 1.0513$. Bound: $\frac{1.0513}{2}(0.05)^2 \approx 0.00131$; true error $0.00127$ ✓.

> **Answer**: $e^{0.05} \approx 1.05$, error $\le 0.00131$

### D4.

$f'(x) = 2x-4 < 0$ on $(-\infty,2)$ and $>0$ on $(2,\infty)$.

> **Answer**: $f$ decreases on $(-\infty,2)$, increases on $(2,\infty)$, minimum at $x=2$

### D5.

$\frac{dA}{dr} = 2\pi r = 6\pi \approx 18.85$ at $r=3$.

> **Answer**: $6\pi$ cm² per cm — the circumference; each extra cm of radius adds ≈ 18.85 cm² of area

### D6.

$C'(q) = 0.2q+1$, so $C'(10) = 3$ \$/unit. $C(10) = 70$; estimate $C(11) \approx 73$. Exact $C(11) = 73.1$; actual jump $= 3.1$. The $0.1$ gap is $\frac12 C''(10)\cdot 1^2 = \frac12(0.2) = 0.1$ ✓.

> **Answer**: $C'(10) = \$3$/unit; estimate \$73 vs exact \$73.10

### D7.

$\frac{dK}{dv} = mv = 2\cdot 4 = 8$; units $\mathrm{J}/(\mathrm{m/s}) = \mathrm{kg\,m/s}$.

> **Answer**: 8 kg·m/s — momentum

### D8.

$\frac{dV}{dr} = 4\pi r^2 = 16\pi \approx 50.3$ at $r=2$.

> **Answer**: $16\pi$ cm³ per cm — the sphere's surface area

### D9.

$AC'(q) = 1 - \frac{25}{q^2} = 0$ → $q=5$. $AC(5) = 20$. Total cost $C = q\cdot AC = 10q+q^2+25$, so $MC = C' = 10+2q = 20$ at $q=5$ ✓.

> **Answer**: minimum of $AC$ at $q=5$, value 20; $MC(5)=20=AC(5)$

### D10.

$q=60$, $E = \frac{20}{60}(-2) = -\frac23$. $|E| < 1$ → inelastic.

> **Answer**: $E = -\frac23$ (inelastic) — a price rise increases revenue

### D11.

**(a)** $\frac{dd}{df}$ — **km/L**: "each liter of fuel buys $\frac{dd}{df}$ kilometers of driving" (its reciprocal, L/km, is the same relation read from the other direction — consumption).

**(b)** $\frac{dm}{dV}$ — **kg/m³**: "each cubic meter of the substance carries $\frac{dm}{dV}$ kilograms" — density is a degree of relation between mass and volume.

**(c)** $\frac{dC}{dq}$ — **\$/item**: "each extra item costs about $\frac{dC}{dq}$ dollars" — marginal cost is a degree of relation between cost and quantity.

> **Answer**: km/L (mileage) · kg/m³ (density) · \$/item (marginal cost) — three relations, three named degrees

---

## Advanced Drills

### A1.

$\Delta A = \pi(r+dr)^2 - \pi r^2 = \pi\big(r^2 + 2r\,dr + (dr)^2\big) - \pi r^2 = 2\pi r\,dr + \pi(dr)^2$.

Divide by $dr$ and let $dr\to 0$: $\frac{dA}{dr} = 2\pi r$. The ring picture: the added area is a band of length $2\pi r$ (the circumference) and width $dr$ — area $2\pi r\,dr$. The leftover $\pi(dr)^2$ is a tiny corner square, negligible because it is *quadratic* in $dr$: shrinking $dr$ by 10 shrinks the band by 10 but the corner by 100.

> **Answer**: $\frac{dA}{dr}=2\pi r$; ring area = circumference × width, corner term vanishes

### A2.

**(a)** $\Delta V = \frac{4}{3}\pi\big[(r+dr)^3 - r^3\big] = \frac{4}{3}\pi\big[3r^2 dr + 3r(dr)^2 + (dr)^3\big]$. The leading term is $4\pi r^2\,dr$ — a shell of area $4\pi r^2$ and thickness $dr$.

**(b)** With half-side $u = \frac{s}{2}$: $V = 8u^3$, so $\frac{dV}{du} = 24u^2 = 6(2u)^2 = 6s^2$ — the full surface area. The difference: growing $s$ by $ds$ moves only **3 faces** outward (the cube thickens on three sides), adding $3s^2 ds$; growing the half-side moves **all 6 faces** outward by $du$ each, adding $6s^2\,du$. The derivative measures whichever growth direction you feed it.

> **Answer**: shell volume $4\pi r^2 dr$; half-side derivative = $6s^2$ = full surface area

### A3.

**(a)** $\frac{dK}{dt} = \frac{dK}{dv}\cdot\frac{dv}{dt} = mv\cdot a$. With $F=ma$: $\frac{dK}{dt} = Fv$.

**(b)** $\big[\frac{dK}{dv}\big] = \frac{\mathrm{J}}{\mathrm{m/s}} = \mathrm{kg\,m/s}$ — momentum. $\big[\frac{dK}{dt}\big] = \frac{\mathrm{J}}{\mathrm{s}} = \mathrm{W}$ — power.

**(c)** Power is force × velocity because both factors scale the delivery rate: twice the force delivers twice the energy per second, and twice the speed covers twice the distance per second, so twice the work per second.

> **Answer**: $\frac{dK}{dt} = Fv$; units momentum vs power; power = force × velocity

### A4.

**(a)** Tangent at 0: $f'(0)=\cos 0=1$, so $L(x) = x$. $\sin(0.2) \approx 0.2$ (true $0.198669$).

**(b)** $\sin x = x - \frac{x^3}{3!}\cos c$ for some $c$ between 0 and $x$, so $|R| \le \frac{|x|^3}{6}$ since $|\cos c|\le 1$. The error is **cubic** because the $x^2$ term of the Taylor expansion is zero — sine is odd. At $x=0.2$: bound $\frac{0.008}{6} \approx 0.00133$; true error $0.00133$ ✓.

**(c)** The bound blows up like $|x|^3/6$, and for $x=2$ it is $\frac83 \approx 1.33$ — the tangent model is useless far from 0 (and indeed $\sin 2 \approx 0.91$).

> **Answer**: $\sin 0.2 \approx 0.2$ with error $\le \frac{0.2^3}{6} \approx 0.00133$; the model is local

### A5.

$MC = 3q^2-18q+30$, $AC = q^2-9q+30+\frac{25}{q}$.

$MC = AC$ → $2q^2 - 9q - \frac{25}{q} = 0$ → $2q^3 - 9q^2 - 25 = 0$. Factor: $(q-5)(2q^2+q+5) = 0$. The quadratic has discriminant $1-40<0$ — only $q=5$ is real.

Verify minimum: $AC'(q) = 2q-9-\frac{25}{q^2}$; at $q=5$: $10-9-1=0$ ✓. $AC'' = 2+\frac{50}{q^3} > 0$ → minimum.

Interpretation: at $q=5$, $MC = AC = 15$ — the next unit costs exactly what units cost on average. Below 5 each new unit is cheaper than the average and drags it down; above 5 each new unit is dearer and pushes the average up.

> **Answer**: $q=5$, $MC=AC=15$ = minimum average cost

### A6.

**(a)** Product rule: $R'(p) = q + p\,q' = q\left(1 + \frac{p\,q'}{q}\right) = q\,(1+E)$.

**(b)** $q=500-10p$: $R' = 500-20p = 0$ → $p=25$, $q=250$, $R=\$6250$.

**(c)** With $q>0$, $R'=0 \iff E=-1$. Left of the peak ($E>-1$, inelastic) a price rise gains more per unit than it loses in volume; right of the peak ($E<-1$, elastic) it loses more volume than it gains.

> **Answer**: $R'=q(1+E)$; max revenue at $p=25$, where $E=-1$

### A7.

**(a)** $\frac{dT}{dh} = -6.5$ °C/km. Per 100 m: $-0.65$ °C.

**(b)** "Each kilometer higher, the air is 6.5 °C colder."

**(c)** $20 - 6.5h = 0$ → $h = \frac{20}{6.5} \approx 3.08$ km.

> **Answer**: $-6.5$ °C/km ($-0.65$ °C per 100 m); freezing at ≈ 3.08 km

### A8.

**(a)** $m$ constant: $F = \frac{dp}{dt} = \frac{d}{dt}(mv) = m\frac{dv}{dt} = ma$.

**(b)** $m(t)$ changing: $F = m\frac{dv}{dt} + v\frac{dm}{dt}$. First term: accelerating the mass that is already here. Second term: the momentum carried by the mass flow — mass leaving at speed $v$ subtracts momentum like money leaving an account. (The precise rocket story — the exhaust leaves at $v-u$, so the true thrust is $-u\frac{dm}{dt}$ — is worked out in [14D1B A1](../14D1B-product-quotient-interpretation.md#advanced-drill).)

> **Answer**: $F=ma$; two channels: accelerate-current-mass + momentum-of-mass-flow (frame question → 14D1B A1)

### A9.

The exact direction is: $f'(x) > 0$ on an interval ⟹ $f$ increasing there. The converse is false. For $f(x)=x^3$, $f'(0)=0$ but the function is increasing *everywhere*: between any two points $a<b$ there is a $c$ with $\frac{f(b)-f(a)}{b-a} = f'(c) = 3c^2 \ge 0$, and the quotient is positive whenever $a<b$. A zero derivative at a single point cannot force a flat spot — flatness needs the derivative zero on a whole interval. So "$f'=0$" is only a *candidate flag* for an extremum, and "$f'>0$" is a sufficient, not necessary, test.

> **Answer**: $f'>0$ ⟹ increasing is exact; the converse fails at single points like $x=0$ of $x^3$

### A10.

$\frac{dV}{dr} = 2\pi r h = 2\pi(3)(10) = 60\pi \approx 188.5$ cm³ per cm — the **lateral surface** (the wrapped band around the cylinder).

$\frac{dV}{dh} = \pi r^2 = 9\pi \approx 28.3$ cm³ per cm — the **base disk**.

> **Answer**: $60\pi$ = lateral area (band), $9\pi$ = base area (disk)

### A11.

**(a)** $\frac{dq}{dp} = -2$ units/\$ everywhere. $\frac{dp}{dq} = -\frac12$ \$/unit. Product: $(-2)\cdot(-\frac12) = 1$ ✓ — reciprocals, as the two directions of a relation locally always are.

**(b)** "Each dollar of price costs 2 units of demand." "Each unit of demand the market is asked to absorb requires lowering the price by half a dollar." Same relation, two directions, two different numbers.

**(c)** At $p=20$: $q=60$, $E = \frac{20}{60}(-2) = -\frac23$. Reading: "1% of price buys $-\frac23$% of demand" — a scale-free degree of relation. The raw $-2$ units/\$ is glued to dollars and units, so it cannot be laid next to $-6.5$ °C/km; the percentage form strips the domains and leaves only the strength of the relation.

> **Answer**: $-2$ units/\$ ↔ $-\frac12$ \$/unit (reciprocals); $E = -\frac23$

---

## Deep Insight

### DI1.

For all $a,x$: $f(x)-f(a) = f'(a)(x-a)$, i.e. $\frac{f(x)-f(a)}{x-a} = f'(a)$ — the secant slope between any two points equals the slope at $a$. Holding $a$ fixed, the right side is constant in $x$, so $f$ is a straight line: $f(x) = mx+b$ (with $m = f'(a)$) — affine, so $f'' = 0$ everywhere. Conversely, if $f(x) = mx+b$, then $L_a(x) = f(a)+m(x-a) = ma+b+mx-ma = mx+b = f(x)$ ✓.

The error bound in Example 3: $|f-L| \le \frac{M}{2}(x-a)^2$ with $M = \max|f''|$ — it vanishes for every $a,x$ exactly when $f''=0$ everywhere. The tangent model is perfect precisely for curvature-free functions: **all linearization error lives in $f''$.** That is why the bound is quadratic — it is the second derivative's fingerprint.

> **Answer**: exactly the affine functions $f(x)=mx+b$ ($f''=0$); the error lives entirely in $f''$

---

## Answer Check

| Problem | Answer |
|:---:|:---|
| P1 | L/min · people/yr · °C/m · kg/item |
| P2 | turn $t=2,4$; speed flip $t=3$ |
| P3 | $\sqrt{9.3}\approx3.05$, err $\le 0.000417$ |
| P4 | \$44/unit · ≈\$668 vs 669 · $q=12$ |
| P5 | $100\pi$ · $8/(100\pi)\approx0.0255$ cm/s |
| P6 | $E=-1.5$, $-0.25$ · max rev \$5000 at $p=25$ |
| RP1 | $F=4+2d$; $2$ \$/km |
| RP2 | $10$ → $40$ cm²/cm |
| RP3 | $0.08$ L/km ↔ $12.5$ km/L |
| RP4 | $0.8$ kPa/s |
| RPB1 | $12$ L/min |
| RPB2 | $2\sqrt3 \approx 3.46$ cm²/cm |
| RPB3 | $-\frac1{30}$ h/(km/h) = −2 min/(km/h) |
| RPB4 | $3$ \$/kg ↔ $\frac13$ kg/\$ |
| RPB5 | $19.6$ m/s |
| RPA1 | $1.2$ \$/cm |
| RPA2 | $100$ \$/\$ at $p=10$; zero at $p=20$ (peak) |
| RPA3 | $-4$ W/Ω; $E=-1$ |
| RPA4 | $120$ m²/m at $x=20$; zero at $x=50$ |
| RPA5 | $0.1$ mL/s ≈ $3{,}154$ L/yr |
| D1 | mi/hr · \$/item · bacteria/min · N/m |
| D2 | $(1,3)$ |
| D3 | $1.05$, err $\le 0.00131$ |
| D4 | dec $(-\infty,2)$, inc $(2,\infty)$, min at 2 |
| D5 | $6\pi$ = circumference |
| D6 | \$3/unit · ≈\$73 vs \$73.10 |
| D7 | 8 kg·m/s = momentum |
| D8 | $16\pi$ = surface area |
| D9 | $q=5$, value 20, $MC=AC$ |
| D10 | $E=-\frac23$ inelastic |
| D11 | km/L · kg/m³ · \$/item |
| A1 | $2\pi r$; corner $(dr)^2$ vanishes |
| A2 | $4\pi r^2 dr$; half-side gives $6s^2$ |
| A3 | $\frac{dK}{dt}=Fv$; power |
| A4 | err $\le 0.00133$; local only |
| A5 | $q=5$, $MC=AC=15$ |
| A6 | $R'=q(1+E)$; $p=25$ |
| A7 | $-0.65$ °C/100m; ≈3.08 km |
| A8 | $F=ma$; channels $m\dot v + v\dot m$ (frame question → 14D1B A1) |
| A9 | converse fails; $f'=0$ is only a flag |
| A10 | $60\pi$ lateral · $9\pi$ base |
| A11 | $-2$ units/\$ ↔ $-\frac12$ \$/unit; $E=-\frac23$ |
| DI1 | affine functions $f=mx+b$ — $f''=0$ everywhere |
