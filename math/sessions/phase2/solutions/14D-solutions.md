# Solutions — 14D: The Relation Lens

> Back to [14D — The Relation Lens](../14D-relation-lens.md)

---

## Shape Practice

### SP1.

**(a)** $d = 4.9\,t^2$: exponent $n=2>0$ → proportional; coefficient $k=4.9>0$ → forward attribute.

**(b)** "More fall time, more fallen distance — distance keeps its natural meaning."

**(c)** $\frac{dd}{dt} = 9.8t$; at $t=2$: $19.6$ m/s, positive, matching the table (same direction).

> **Answer**: proportional · forward; $19.6$ m/s at $t=2$

**Lens reading**: a square is the purest proportional shape — only the direction knob is turned; the attribute knob adds nothing.

### SP2.

**(a)** $t = 120\,v^{-1}$: $n=-1<0$ → inverse; $k=120>0$ → forward.

**(b)** "Faster driving, shorter trip time — time keeps its natural meaning."

**(c)** $\frac{dt}{dv} = -\frac{120}{v^2} < 0$ — one minus, opposite direction.

> **Answer**: inverse · forward; $\frac{dt}{dv} = -\frac{120}{v^2}$, negative

**Lens reading**: the reciprocal is the purest inverse shape; the minus in the derivative is the inverse *speaking*, not a flipped attribute — time is still "time".

### SP3.

**(a)** $T = 20 + (-6.5)\,h$: the direction knob is the slope $k=-6.5$ ($n=1$, proportional in shape), and it is negative → reversed attribute.

**(b)** "Higher up, colder air — temperature reads *down* as altitude rises."

**(c)** $\frac{dT}{dh} = -6.5$ °C/km — negative, as the table predicts.

**(d)** The attribute flips where the constant sets the boundary: $T=0$ at $h = \frac{20}{6.5} \approx 3.08$ km — above that, water freezes (temperature crosses into "below zero").

> **Answer**: proportional · reversed; $-6.5$ °C/km; freezes at ≈3.08 km

**Lens reading**: a linear formula with a negative slope is "proportional in size, reversed in attribute", and the constant term says where the attribute actually flips — the slope says "colder with height", the constant says "freezing at 3.08 km".

### SP4.

**(a)** $U = -GM\,r^{-1}$: two minus signs — one in the coefficient ($k=-GM$), one in the exponent ($n=-1$).

**(b)** $r$ up → $U$ up (toward 0): the two flips cancel, so the direction is restored; but the attribute stays reversed — $U$ is a negative (bound) energy.

**(c)** $\frac{dU}{dr} = +\frac{GM}{r^2} > 0$ — even count of minuses, same direction.

> **Answer**: inverse · reversed; $\frac{dU}{dr} = +\frac{GM}{r^2}$, positive

**Lens reading**: the double minus is the cleanest demonstration of the counting rule — inverse says "opposite", the reversed attribute flips it back, and the derivative's plus sign is both flips in one number.

### SP5.

**(a)** $P = C\,V^{-1}$: $n=-1$ → inverse; $k=C>0$ → forward.

**(b)** Compress ($V$ down) → $P$ up: "squeeze the gas, pressure pushes back."

**(c)** $\frac{dP}{dV} = -\frac{C}{V^2} < 0$.

**(d)** "Inverse" is about *motion* direction, not sign: both $P$ and $V$ are positive quantities, yet they move oppositely — the minus lives in the derivative, not in the attribute.

> **Answer**: inverse · forward; $\frac{dP}{dV} = -\frac{C}{V^2}$, negative

**Lens reading**: Boyle's law is the canonical inverse–forward relation — only the direction knob turned, the attribute knob untouched; elasticity is exactly $-1$ everywhere because the shape is a pure $V^{-1}$ (see RPA3).

### SP6.

**(a)** $q = 200 + (-5)\,p$: slope $k=-5$ → proportional · reversed.

**(b)** "Pricier product, less demand — demand counts down."

**(c)** $\frac{dq}{dp} = -5$ units/\$.

**(d)** Attribute flips at $q=0$: $p = \frac{200}{5} = 40$ — past \$40, demand would read negative (nobody buys; the linear model's boundary).

> **Answer**: proportional · reversed; $-5$ units/\$; zero demand at $p=40$

**Lens reading**: demand is the textbook reversed attribute — the minus is the *meaning* of the relation, not a failure of the model.

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

**(c)** $0.08 \times 12.5 = 1$ — reciprocals. Two numbers, one relation: the consumption direction (L/km) and the mileage direction (km/L) are the same relationship read in reverse.

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

**(c)** $3 \times \frac13 = 1$ — the two directions of one relation are reciprocals.

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

**(c)** Zero at $p=20$: revenue stops responding to price — momentarily flat, the peak ($R = 2000$). Degree zero is not "no relation" (see 14D1 A9) — it is the relation at rest, for one instant.

> **Answer**: $\frac{dR}{dp} = 200-10p$; $100$ \$/\$ at $p=10$; zero at $p=20$ = peak

#### RPA3.

**(a)** $P(R) = \frac{14400}{R}$; $\frac{dP}{dR} = -\frac{14400}{R^2}$. At $R=60$: $-4$ W/Ω.

**(b)** "At 60 Ω, each extra ohm of resistance costs 4 W of power." Negative: resistance and power move in opposite directions — the relation is inverse.

**(c)** $P(60) = \frac{14400}{60} = 240$ W. $E = \frac{R}{P}\frac{dP}{dR} = \frac{60}{240}(-4) = -1$. Reading: "1% of resistance buys exactly −1% of power." The dimensionless degree is unit elastic at *every* resistance, because $P \propto R^{-1}$ — the percentage form exposes a uniformity that the raw $-4$ W/Ω hides (compare with 14D1 Example 6).

> **Answer**: $-4$ W/Ω at $R=60$; $E = -1$ (unit elastic, everywhere)

#### RPA4.

**(a)** Width $x$ (two sides of length $x$), river side $200 - 2x$: $A(x) = x(200 - 2x) = 200x - 2x^2$ m².

**(b)** $\frac{dA}{dx} = 200 - 4x$; at $x=20$: $120$ m²/m: "at width 20 m, each extra meter of width buys about 120 m² of pen."

**(c)** Zero at $x=50$: the degree vanishes — area stops responding to width. There the pen is 50 m × 100 m, $A = 5000$ m² — the maximum. Degree zero is the relation's turning point (see 14D1 A9).

> **Answer**: $\frac{dA}{dx} = 200-4x$; $120$ m²/m at $x=20$; zero at $x=50$ (max 5000 m²)

#### RPA5.

**(a)** $V(t) = 0.1t$ mL; $\frac{dV}{dt} = 0.1$ mL/s: "each second, 0.1 mL of water leaves."

**(b)** $0.1 \frac{\mathrm{mL}}{\mathrm{s}} \times 3600 \frac{\mathrm{s}}{\mathrm{h}} \times 24 \frac{\mathrm{h}}{\mathrm{day}} \times 365 \frac{\mathrm{day}}{\mathrm{yr}} = 3{,}153{,}600$ mL/yr ≈ 3,154 L/yr.

**(c)** Relations chain by multiplying degrees — and unit conversions are relations too: each conversion factor is a degree of relation between two units, and the units cancel exactly like the chain rule's factors do. A two-drops-per-second drip wastes over three tons of water a year.

> **Answer**: $0.1$ mL/s ≈ 3,154 L/yr

---

## Answer Check

| Problem | Answer |
|:---:|:---|
| SP1 | proportional·forward; $19.6$ m/s at $t=2$ |
| SP2 | inverse·forward; $\frac{dt}{dv}=-\frac{120}{v^2} < 0$ |
| SP3 | proportional·reversed; $-6.5$ °C/km; freezes ≈3.08 km |
| SP4 | inverse·reversed; $\frac{dU}{dr}=+\frac{GM}{r^2} > 0$ |
| SP5 | inverse·forward; $\frac{dP}{dV}=-\frac{C}{V^2} < 0$ |
| SP6 | proportional·reversed; $-5$ units/\$; zero demand at $p=40$ |
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
