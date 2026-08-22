# Solutions — 14D: The Relation Lens

> Back to [14D — The Relation Lens](../14D-relation-lens.md)

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

## Sign Practice

### SN1.

**(a)** $B(10) = -800 + 500 = -300$ — the number sits below zero: in debt.

**(b)** $B'(t) = 50 > 0$ — the arrow points up.

**(c)** "In debt, but climbing."

**(d)** $B = 0$ at $t = \frac{800}{50} = 16$ days; there $B' = 50$ still — crossing zero is an event in the position, not in the direction. The degree never noticed.

> **Answer**: $B(10) = -300$, $B' = 50$; crosses at $t=16$ with the degree unchanged

**Lens reading**: a negative position with a positive arrow — the two axes are independent.

### SN2.

**(a)** $T(10) = 85 - 30 = 55$ °C — still hot: positive.

**(b)** $T'(t) = -3 < 0$ — the arrow points down.

**(c)** "Still hot, sinking."

**(d)** $T = 25$ at $t = \frac{60}{3} = 20$ min; there $T' = -3$ still — arriving at room temperature does not change the direction of cooling.

> **Answer**: $T(10) = 55$, $T' = -3$; hits 25 °C at $t=20$ with the degree still $-3$

**Lens reading**: a positive position with a negative arrow — falling from above.

### SN3.

**(a)** $f(0) = 0$ and $f'(0) = 3(0)^2 = 0$ — here value and flatness coincide.

**(b)** $f(0.1) = 0.001$, $f(-0.1) = -0.001$ — the function passes through and keeps rising; nothing stopped.

**(c)** "Flat for an instant — the coincidence is an accident, not an implication." $f'=0$ never announces the value.

> **Answer**: both zero at $x=0$ by coincidence; the function rises straight through

**Lens reading**: the one case where position and arrow are both zero — and the trap is to think the arrow caused it.

### SN4.

**(a)** $v(t) = 20 - 9.8t = 0$ at $t = \frac{20}{9.8} \approx 2.04$ s.

**(b)** $s \approx 5 + 40.8 - 20.4 \approx 25.4$ m.

**(c)** "Paused at 25 m up — the process has not stopped and the height has not vanished; only the relation to time is flat."

**(d)** Just after the peak $v < 0$ — it falls.

> **Answer**: $v=0$ at $t\approx2.04$ with $s\approx25.4$ m; falls right after

**Lens reading**: $v=0$ is "momentarily flat", and the number it leaves untouched is 25.4 m.

### SN5.

**(a)** $f'(x) = g'(x) = 1 > 0$ — identical arrows.

**(b)** $f(0) = 2 > 0$, $g(0) = -5 < 0$ — opposite positions.

**(c)** "Two functions move in lockstep and sit on opposite sides of zero — direction is shared, position is not."

> **Answer**: both $+1$; positions $+2$ vs $-5$

**Lens reading**: identical degrees of relation, opposite values — the axes are cleanly separable.

### SN6.

**(a)** $s(3) = 9 - 25 = -16$ m — the number sits behind the start line.

**(b)** $v(t) = 2t$; $v(3) = 6 > 0$ — the arrow points forward.

**(c)** "Behind the start line, moving forward."

**(d)** $s = 0$ at $t = 5$; there $v = 10$ — the crossing does not pause the arrow; the degree just keeps climbing.

> **Answer**: $s(3) = -16$, $v(3) = 6$; crosses at $t=5$ with $v=10$

**Lens reading**: a negative position with a positive arrow, in motion — the car crosses the line without the derivative ever noticing.

### SN7.

**(a)** $B(5) = -200 - 150 = -350$ — deeper below zero.

**(b)** $B'(t) = -30 < 0$ — the arrow points down.

**(c)** "Below zero, sinking deeper."

**(d)** Never: the degree is $-30$ whether the debt is $-200$ or $-2{,}000{,}000$ — the arrow is blind to the number's size.

> **Answer**: $B(5) = -350$, $B' = -30$; the degree never notices

**Lens reading**: the fourth combination — negative position, negative arrow — and the degree stays uniform while the position worsens.

### SN8.

**(a)** $f'(x) = 3(x-1)^2 = 0$ at $x = 1$.

**(b)** $f(1) = 2$.

**(c)** $f(0.9) = 1.999$, $f(1.1) = 2.001$ — the curve passes straight through: neither a peak nor a valley.

**(d)** "Flat at height 2 for one instant — flatness is the entire promise."

> **Answer**: $f'=0$ at $x=1$ with $f=2$; neither peak nor valley

**Lens reading**: $f'=0$ guarantees flatness and nothing else — not a zero, not a stop, not an extremum.

### SN9.

**(a)** $T(10) = -10 + 5 = -5$ °C — below freezing.

**(b)** $T'(t) = 0.5 > 0$ — the arrow points up.

**(c)** "Below freezing, warming."

**(d)** $T = 0$ at $t = \frac{10}{0.5} = 20$ min; there $T' = 0.5$ still — the value's zero changes nothing in the arrow.

> **Answer**: $T(10) = -5$, $T' = 0.5$; crosses 0 °C at $t=20$ with the degree unchanged

**Lens reading**: crossing zero is a position event; the arrow sails through untouched.

### SN10.

**(a)** $f(0) = 0$ but $f'(0) = 1000$ — a giant arrow at zero.

**(b)** $g(0) = 100$ but $g'(0) = 0$ — a giant number with no arrow.

**(c)** "The arrow's size is its own axis: slope 1000 at value 0, and value 100 with slope 0 — size in one axis proves nothing in the other."

> **Answer**: $0$ with $f' = 1000$ vs $100$ with $g' = 0$

**Lens reading**: both directions of the size trap — steep at zero, flat at a hundred.

---

## Variable-Jail Practice

### JA1.

**(a)** Lock $V=120$: $P(R) = \frac{14400}{R}$; $\frac{dP}{dR} = -\frac{14400}{R^2} = -4$ W/Ω at $R=60$ — "bigger resistance, less power."

**(b)** Lock $R=60$: $P(V) = \frac{V^2}{60}$; $\frac{dP}{dV} = \frac{2V}{60} = 4$ W/V at $V=120$ — "higher voltage, more power."

**(c)** The formula never changed — the lock picked a different relation out of it. (a) is inverse ($P \propto R^{-1}$), (b) is proportional ($P \propto V^2$).

> **Answer**: (a) $-4$ W/Ω (b) $+4$ W/V (c) same formula, different relation

**Lens reading**: the jail, not the letter, is the interpretation.

### JA2.

**(a)** $T(v) = \frac{240}{v}$; $\frac{dT}{dv} = -\frac{240}{v^2} = -0.0375$ h/(km/h) = −2.25 min per km/h at $v=80$ — the duration is a response bought by speed.

**(b)** $s(t) = 80t$; $s'(t) = 80$ km/h — the flowing clock is a driver that buys meters.

**(c)** Duration is read from outside the trip (one number, the whole trip); flowing time is read from inside (the running instant). Same letter $t$ on the page, two jails in the problem — and two opposite roles.

> **Answer**: $-2.25$ min/(km/h) vs $80$ km/h — response vs driver

**Lens reading**: the $t$-trap, diffused — name the jail before reading the letter.

### JA3.

**(a)** Driver $t$ (flowing clock), response $V$; locked: the start 100 L and the rate 2 L/min. $V'(t) = -2$ L/min — "each minute drains 2 L."

**(b)** $T = \frac{100}{2} = 50$ min is a *value* in the duration jail — the clock reading when $V$ hits zero. The $-2$ is a *degree* — how fast $V$ moves. A number and an arrow.

**(c)** $V(30) = 40$ L is the position; $V'(30) = -2$ L/min is the direction — different axes (the Sign Lens). 40 L of water and 2 L/min of draining describe the same instant without touching each other.

> **Answer**: $V'=-2$ L/min; 50 min is a value, $-2$ L/min is a degree; 40 L vs $-2$ L/min are different axes

**Lens reading**: value, degree, and duration — three different kinds of number, three jails.

### JA4.

**(a)** Lock $T=300$: $PV = 8.3 \cdot 300 = 2490$, so $P(V) = \frac{2490}{V}$; $\frac{dP}{dV} = -\frac{2490}{V^2} = -24.9$ kPa/m³ at $V=10$ — "squeezing one m³ buys 24.9 kPa."

**(b)** Lock $P=100$: $V(T) = \frac{8.3}{100}T = 0.083\,T$; $\frac{dV}{dT} = 0.083$ m³/K — "each kelvin of heating buys 0.083 m³."

**(c)** Locking $T$ turns the law into a reciprocal ($V^{-1}$, inverse); locking $P$ turns it into a line ($V^{+1}$, proportional) — the lock chooses the power, and the exponent's sign decides the direction directly.

> **Answer**: $-24.9$ kPa/m³ (inverse) vs $0.083$ m³/K (proportional) — the lock picks the power

**Lens reading**: one law, two locks, two powers — the jail picks the exponent, and the exponent's sign picks the direction.

### JA5.

**(a)** Chain $P \to R \to t$: $\frac{dP}{dt} = \frac{dP}{dR}\cdot\frac{dR}{dt} = \left(-\frac{14400}{R^2}\right)(0.2)$; at $t=0$, $R=60$: $-4 \cdot 0.2 = -0.8$ W/s — "each second of heating drops the power by 0.8 W."

**(b)** Link 1 ($P$ responds to $R$): $V=120$ locked. Link 2 ($R$ responds to $t$): the start $60$ Ω and the rate $0.2$ Ω/s locked. Every link has its own jail.

**(c)** $-4$ W/Ω is the degree per ohm; $-0.8$ W/s is the degree per second, chained by the $0.2$ Ω/s: $-4 \cdot 0.2 = -0.8$. Both are true at once because they answer different "with respect to what" questions — the jail of each link.

> **Answer**: $-0.8$ W/s; two links, two jails; $-4$ W/Ω · $0.2$ Ω/s $= -0.8$ W/s

**Lens reading**: chains are jails in series — each link locks its own parameters.

### JA6.

**(a)** $t(60) = 2$ h; $\frac{dt}{dv} = -\frac{120}{v^2} = -\frac{120}{3600} = -\frac{1}{30}$ h/(km/h) = −2 min per km/h: "at 60 km/h, each extra km/h shaves 2 minutes off the trip."

**(b)** $t$ is a **duration** — the trip's total, a response the speed buys. A duration is not a clock: it does not flow, it is *counted*. "Time running backwards" is a reading of a flowing clock, and this jail contains no flowing clock.

**(c)** $t = 2$ h sits positive; the arrow points down. The value shrinks toward zero as $v$ rises and **never crosses** — an inverse relation's number approaches 0 from above, forever. (Sign lens: positive position, negative arrow.)

**(d)** $v \to \infty$: $t \to 0^{+}$ — the trip shrinks toward zero duration, never below it. "Backwards time" lives nowhere in the picture: the minus is the relation's direction, not time's nature.

> **Answer**: $-\frac{1}{30}$ h/(km/h) = −2 min/(km/h); $t$ is a duration; $t \to 0^{+}$, never negative

**Lens reading**: a reversed relation is a shrinking duration, not a reversed clock — the minus names the relation's direction, and the quantity's nature stays whatever the jail says it is.

### JA7.

**(a)** $T(80) = 3$ h; $\frac{dT}{dv} = -\frac{240}{v^2} = -0.0375$ h/(km/h) = −2.25 min per km/h — the duration shrinks as speed grows.

**(b)** $s(t) = 80t$: $s' = 80$ km/h — each hour of flowing time buys 80 km.

**(c)** The minus lives in the duration jail only. "Reversed" describes the *relation's direction* (faster → less duration), never the nature of time — in the clock jail the driver is time itself, and the degree is positive.

**(d)** $T' = -0.0375$ h/(km/h): speed is the driver, duration the response — opposite directions. $s' = 80$ km/h: time is the driver, position the response — same directions. Both are ordinary arrows; neither reverses time. In the duration jail time is the quantity being counted; in the clock jail it is the counter — different roles, different signs.

> **Answer**: −2.25 min/(km/h) vs $+80$ km/h — the minus is the relation's direction, not time's nature

**Lens reading**: one formula, two jails, two signs — the sign belongs to the relation, the nature to the jail.

---

## Duration-Clock Drills

### DC1.

**(a)** $T(20) = 20$ min; $\frac{dT}{dr} = -\frac{400}{r^2} = -1$ min per (L/min) — "each extra L/min of drain shaves 1 minute off the emptying time."

**(b)** $T$ is the emptying **duration** — a response the rate buys, not a clock.

**(c)** $+20$ min with a down arrow — positive position, negative direction.

**(d)** $r \to 0^{+}$: $T \to +\infty$; $r \to \infty$: $T \to 0^{+}$ — never below zero.

> **Answer**: $-1$ min/(L/min); $T$ is a duration; $T \to 0^{+}$, never negative

**Lens reading**: a faster drain shrinks the lifetime; the clock is untouched.

### DC2.

**(a)** $T(6) = 10$ h; $\frac{dT}{dP} = -\frac{60}{P^2} = -\frac{5}{3} \approx -1.67$ h/kW.

**(b)** $T$ is the battery's lifetime — a duration, not a clock.

**(c)** $+10$ h, arrow down.

**(d)** $P \to 0^{+}$: $T \to +\infty$ (an idle battery lasts forever); $P \to \infty$: $T \to 0^{+}$.

> **Answer**: $-1.67$ h/kW; lifetime shrinks, never reverses

**Lens reading**: power eats the battery's total; the total only shrinks.

### DC3.

**(a)** $T(30) = 10$ days; $\frac{dT}{dp} = -\frac{300}{p^2} = -\frac{1}{3}$ day per (page/day) = −8 h per (page/day).

**(b)** $T$ is reading duration.

**(c)** $+10$ days, arrow down.

**(d)** $p \to 0^{+}$: $T \to +\infty$; $p \to \infty$: $T \to 0^{+}$.

> **Answer**: $-\frac13$ day per (page/day) = −8 h; duration, never negative

**Lens reading**: reading faster shortens the total — the pages are the total, the rate eats it.

### DC4.

**(a)** $T(50) = 100$ s; $\frac{dT}{db} = -\frac{5000}{b^2} = -2$ s per (MB/s) — "each extra MB/s shaves 2 seconds off the download."

**(b)** $T$ is download duration, not a reversed clock.

**(c)** $+100$ s, arrow down.

**(d)** $b \to 0^{+}$: $T \to +\infty$; $b \to \infty$: $T \to 0^{+}$.

> **Answer**: $-2$ s per (MB/s); duration, never negative

**Lens reading**: bandwidth eats the file's waiting time.

### DC5.

**(a)** $T(40) = 30$ weeks; $\frac{dT}{dd} = -\frac{1200}{d^2} = -0.75$ week per (dollar/week) ≈ −5 days per (dollar/week).

**(b)** $T$ is the saving duration.

**(c)** $+30$ weeks, arrow down.

**(d)** $d \to 0^{+}$: $T \to +\infty$; $d \to \infty$: $T \to 0^{+}$.

> **Answer**: $-0.75$ week per (dollar/week) ≈ −5 days; duration, never negative

**Lens reading**: the savings rate eats the saving time.

### DC6.

**(a)** $T(2.5) = 20$ h; $\frac{dT}{dq} = -\frac{50}{q^2} = -8$ h per (m³/h) — "each extra m³/h shaves 8 hours off the fill."

**(b)** $T$ is the fill duration.

**(c)** $+20$ h, arrow down.

**(d)** $q \to 0^{+}$: $T \to +\infty$; $q \to \infty$: $T \to 0^{+}$.

> **Answer**: $-8$ h per (m³/h); duration, never negative

**Lens reading**: the pump rate eats the fill time.

### DC7.

**(a)** $T(14) = 3$ h; $\frac{dT}{dv} = -\frac{42}{v^2} = -\frac{3}{14}$ h per (km/h) ≈ −13 min per (km/h) — "each extra km/h shaves about 13 minutes off the marathon."

**(b)** $T$ is the finishing duration.

**(c)** $+3$ h, arrow down.

**(d)** $v \to 0^{+}$: $T \to +\infty$; $v \to \infty$: $T \to 0^{+}$.

> **Answer**: $-\frac{3}{14}$ h/(km/h) ≈ −13 min; duration, never negative

**Lens reading**: pace eats the finishing time — the race clock on the wall never runs backwards.

### DC8.

**(a)** $T(20) = 50$ min; $\frac{dT}{dn} = -\frac{1000}{n^2} = -2.5$ min per (page/min).

**(b)** $T$ is the print duration.

**(c)** $+50$ min, arrow down.

**(d)** $n \to 0^{+}$: $T \to +\infty$; $n \to \infty$: $T \to 0^{+}$.

> **Answer**: $-2.5$ min per (page/min); duration, never negative

**Lens reading**: the printer rate eats the print time.

### DC9.

**(a)** $V'(t) = -20$ L/min — "each flowing minute drains 20 L." Here $t$ is the **clock** (driver), and $V$ is the response.

**(b)** No — DC1's minus shrank a duration (a response); DC9's minus drains a volume (also a response, but to the clock). Both minuses are arrows on their own axes.

**(c)** In DC1 the driver is a rate and time is counted; in DC9 the driver is time and a volume is counted. Time flows forward in both — the minus belongs to the relation, never to the clock.

> **Answer**: $V' = -20$ L/min (clock jail); both minuses are relation-arrows, not reversed clocks

**Lens reading**: the same tank, two jails — duration jail for the lifetime, clock jail for the level.

### DC10.

**(a)** $\lim_{r\to0^{+}} T(r) = +\infty$ — a stopped drain never empties.

**(b)** $\lim_{r\to\infty} T(r) = 0^{+}$ — an instant drain empties instantly.

**(c)** None: for every $r > 0$, $T(r) > 0$. "Negative time" lives nowhere — the duration jail contains no negative numbers, so the down arrow is bounded below by zero forever.

> **Answer**: $T \to +\infty$ as $r\to0^{+}$; $T \to 0^{+}$ as $r\to\infty$; never negative

**Lens reading**: the duration's arrow can only approach zero from above — "down forever, never below zero."

---

## Jail Trap Gallery

### JT1.

**(a)** $t(60) = 2$ h — the 2 is a **value**: the duration, in hours.

**(b)** $t'(60) = -2$ min per (km/h) — the 2 is a **degree**: duration per speed.

**(c)** The units decide: "2 h" is a position on the number line; "2 min/(km/h)" is an arrow. Same digit, two jails — the units are the jail's ID card.

> **Answer**: 2 h = value; −2 min/(km/h) = degree

**Lens reading**: a number's jail is written in its units.

### JT2.

**(a)** $T'(t) = -3$ °C/min — $T$ is temperature, $t$ is the flowing clock (clock jail).

**(b)** $T'(v) = -\frac{240}{v^2} = -0.0375$ h/(km/h) at $v=80$ — $T$ is duration, $v$ is speed (duration jail).

**(c)** "Coffee cools 3 °C per flowing minute; the trip shortens 2.25 minutes per extra km/h." Same letter $T$, two jails — the letter carries nothing; the jail carries everything.

> **Answer**: $-3$ °C/min (clock jail) vs $-0.0375$ h/(km/h) (duration jail)

**Lens reading**: never trust the letter; always read the jail.

### JT3.

**(a)** $V(t) = 0.1t$; $V'(t) = 0.1$ mL/s — the degree of the built function $V$.

**(b)** "2 drops/s" is a rate, but not a derivative: it is a **locked parameter** — a rate going *into* the model, fixed by the faucet, not a degree coming *out* of a function.

**(c)** Locked parameters: 2 drops/s, 0.05 mL/drop. Degree: $V'(t) = 0.1$ mL/s. A rate is not automatically a derivative.

> **Answer**: 2 drops/s and 0.05 mL/drop are locked parameters; 0.1 mL/s is the degree

**Lens reading**: parameters are rates the world hands you; degrees are rates your function produces.

### JT4.

**(a)** m³/s — clock jail: a volume per flowing second.

**(b)** s/(m³/s) — duration jail: a lifetime per pump rate.

**(c)** L/min is the clock jail (a level falling per minute); min/(L/min) is the duration jail (emptying time per drain rate). Fingerprint: duration-jail units have **time on top of a rate**.

> **Answer**: quantity/time = clock jail; time/quantity = duration jail

**Lens reading**: the units name the jail before you read a single number.

### JT5.

**(a)** $T(-60) = \frac{120}{-60} = -2$ h — the formula prints $-2$.

**(b)** It is not reversed time: $v = -60$ km/h is not a physical speed. The model's jail has bars — speed is nonnegative — and $-60$ is outside them.

**(c)** The model lives on $v > 0$. Outside the domain, the formula still answers, but the model is silent — $-2$ h is an invalid input, not a reversed clock.

> **Answer**: $-2$ h is an out-of-domain input, not reversed time; domain $v > 0$

**Lens reading**: the jail has bars — domain errors masquerade as reversed quantities.

### JT6.

**(a)** $f = 6\cdot T(v) = \frac{1800}{v}$; $\frac{df}{dv} = -\frac{1800}{v^2} = -0.18$ L per (km/h) at $v = 100$.

**(b)** The 6 L/h locks a **clock-jail** rate (fuel per flowing hour — a parameter). $T'(v) = -\frac{300}{v^2}$ measures the **duration jail** (trip time per speed).

**(c)** "Each extra km/h saves 0.18 L of fuel for the whole trip." The chain multiplies the clock-jail parameter into the duration-jail degree: $6 \cdot \left(-\frac{300}{v^2}\right)$.

> **Answer**: $-0.18$ L per (km/h); the chain multiplies one jail's parameter into the other's degree

**Lens reading**: chains are jails in series — each link contributes its own lock, and the units multiply through.

### JT7.

**(a)** $V'(t) = -30$ m³/s — a **degree** (flow), in the clock jail (driver $t$, response $V$).

**(b)** $5{,}000{,}000$ m³ is a **value** (a level — how much water sits there).

**(c)** Both wear cubic meters, but the "/s" is the jail's ID card: a level is a position, a flow is an arrow. "The reservoir has $5\cdot10^6$ m³ and is losing 30 m³/s" — value and degree, side by side, no contradiction.

> **Answer**: level $5\cdot10^6$ m³ (value) vs flow $30$ m³/s (degree)

**Lens reading**: same unit family, two jails — the rate's per-time is the lock.

### JT8.

**(a)** $e_1(10) = -20$ m, $e_1' = +3$ m/min — "below sea level, climbing."

**(b)** $e_2(10) = -40$ m, $e_2' = -2$ m/min — "below sea level, sinking deeper."

**(c)** The minus in the value is a real position — depth is a legitimate negative coordinate, not "anti-height." The minus in the degree is a direction. Same symbol, two jobs: depth is a place; sinking is a motion.

> **Answer**: −20 m climbing +3 vs −40 m sinking −2; depth is a coordinate, not reversed height

**Lens reading**: the negative quantity is real; only the arrow's sign is direction.

### JT9.

**(a)** $q(45) = 200 - 225 = -25$ — the formula prints −25.

**(b)** It is not "negative demand": the model lives on $0 \le p \le 40$. At $p = 45$ the formula still answers, but the model is silent — an out-of-domain input.

**(c)** $q' = -5$ units/\$ says price and demand move in opposite directions — a direction, never negative customers.

> **Answer**: $q(45) = -25$ outside the model's domain ($p \le 40$); $q'=-5$ is a direction

**Lens reading**: out-of-domain prints masquerade as reversed quantities.

### JT10.

**(a)** $\frac{df}{dd} = 0.08$ L/km — driver = km, response = L: consumption (small is good).

**(b)** $\frac{dd}{df} = \frac{1}{0.08} = 12.5$ km/L — driver = L, response = km: mileage (big is good).

**(c)** Reciprocals: $0.08 \times 12.5 = 1$ — one relation, two readings. The "reversed" feeling is the reader swapping drivers, not the car changing.

> **Answer**: 0.08 L/km ↔ 12.5 km/L — reciprocals of one relation

**Lens reading**: the frame question picks which reciprocal you hold.

### JT11.

**(a)** $B'(1000) = 0.05 \cdot 1000 = 50$ \$/yr — a **degree** (balance per year).

**(b)** The 5%/yr is **not** a derivative — it is a locked parameter (a rate per dollar per year, feeding the function).

**(c)** The same 0.05 does two jobs: as a parameter it is input; inside $B'(t) = 0.05\cdot B(t)$ it multiplies the current value to produce the degree. Input rate vs output rate.

> **Answer**: 50 \$/yr = degree; 5%/yr = locked parameter

**Lens reading**: a rate is not automatically a derivative — parameters are rates the world hands you; degrees are rates your function produces.

### JT12.

**(a)** $P(V) = \frac{2490}{V}$ (pressure): $\frac{dP}{dV} = -\frac{2490}{V^2} = -24.9$ kPa/m³ at $V=10$ — "squeezing one m³ buys 24.9 kPa."

**(b)** $P(R) = \frac{14400}{R}$ (power): $\frac{dP}{dR} = -\frac{14400}{R^2} = -4$ W/Ω at $R=60$ — "each extra ohm costs 4 W."

**(c)** Same letter $P$, same minus — the units separate the jails: kPa/m³ is pressure per volume; W/Ω is power per resistance. The letter is ink; the units are the ID card.

> **Answer**: $-24.9$ kPa/m³ (pressure) vs $-4$ W/Ω (power)

**Lens reading**: read the units, then read the number — never the other way.

### JT13.

**(a)** $R'(p) = 200 - 10p$; $R'(20) = 0$ with $R(20) = 2000$ — flat at the top: a pause at the peak, not a zero.

**(b)** At $p = 30$: $R = 1500 > 0$ but $R' = -100 < 0$ — "positive, sinking."

**(c)** $R = 0$ at $p = 40$ with $R' = -200$: the value dies at the boundary while the arrow was already pointing down.

> **Answer**: $R'=0$ at $R=2000$ (peak); $R=0$ at $p=40$ with $R'=-200$

**Lens reading**: flat means paused at the top; zero value comes only at the model's edge.

### JT14.

**(a)** Lock $h=10$: $\frac{dV}{dr} = 2\pi rh = 40\pi \approx 125.7$ m³/m — the side boundary area; the shell wrapped around the cylinder.

**(b)** Lock $r=2$: $\frac{dV}{dh} = \pi r^2 = 4\pi \approx 12.6$ m³/m — the cross-section; the disk stacked on top.

**(c)** Same $V$, same letters, two degrees — the frame question picks the driver, and each driver carries its own degree (14D1A's frame question).

> **Answer**: $40\pi$ m³/m (shell) vs $4\pi$ m³/m (disk)

**Lens reading**: two locks, two boundaries — the radius wraps, the height stacks.

### JT15.

**(a)** "8 L per 100 km" — a **degree**: a relation between two units (L per km).

**(b)** "50 L" — a **value**: a bare position.

**(c)** "Per" marks the degree — the "/km" is the jail. A number with a bare unit is a position; a number with "per" is an arrow.

> **Answer**: "per" marks a degree; a bare unit marks a value

**Lens reading**: the word "per" is the jail's spoken ID card.

### JT16.

**(a)** "We drove 120 km" — a **value**: the trip's total (the odometer).

**(b)** "We drove at 80 km/h" — a **degree**: the trip's speed (the speedometer).

**(c)** Same trip, same word "drove" — the odometer reads values, the speedometer reads degrees. The total is the story; the rate is how fast the story ran.

> **Answer**: 120 km = value (total); 80 km/h = degree (speed)

**Lens reading**: totals and rates wear the same units' family — the per-time decides.

### JT17.

**(a)** $\frac{dP}{dh} = -12$ kPa/km at $h=2$ (and everywhere) — "each km higher costs 12 kPa of pressure."

**(b)** The driver is altitude — a place, not a clock. The minus is the relation's direction, never negative pressure: $P(2) = 77$ kPa > 0.

**(c)** $P = 0$ at $h = \frac{101}{12} \approx 8.42$ km — the model's edge. The minus flips the *motion* of the number with altitude; it never makes pressure an "anti-quantity."

> **Answer**: $-12$ kPa/km; driver = altitude; $P=0$ at $h \approx 8.42$ km

**Lens reading**: per kilometer, not per second — the driver's jail writes the sentence's tense.

### JT18.

**(a)** $\frac{dq}{dp} = -5$ units/\$ — "each extra dollar of price costs 5 units of demand."

**(b)** The driver is price (a money-jail), not a clock — the market isn't "running in time," it is trading money for demand.

**(c)** The same ink with $t$ instead of $p$ would be a flow (units per second); with $p$ it is a trade (units per dollar). The driver's jail IS the sentence's tense.

> **Answer**: $-5$ units/\$; driver = price, not a clock

**Lens reading**: the denominator names the world the relation lives in.

### JT19.

**(a)** $\frac{dA}{dr} = 2\pi r = 6\pi \approx 18.8$ m² per meter of radius at $r=3$.

**(b)** The formula answers m² per *meter*, never m² per second — it knows nothing about clocks.

**(c)** Time enters only through the chain rule: if $r(t)$ flows, then $\frac{dA}{dt} = 2\pi r \cdot r'$. A length-driver vs a time-driver are two different jails, joined by the chain.

> **Answer**: $6\pi$ m²/m; no seconds anywhere — time needs the chain rule

**Lens reading**: m²/m vs m²/s — the denominator is the jail.

### JT20.

**(a)** $\frac{dV}{dT} = 0.083$ m³/K — "each kelvin buys 0.083 m³ of volume."

**(b)** No speed exists here: the driver is temperature, and the degree is a static trade.

**(c)** $T$ is in the temperature jail (kelvins). $V'(t)$ would be a flow — volume per second — and would require $T(t)$ chained in. $V'(T)$ and $V'(t)$ are different questions wearing nearly the same ink.

> **Answer**: $0.083$ m³/K; driver = temperature; $V'(t)$ would need the chain

**Lens reading**: per kelvin is a trade; per second is a flow — two jails, one letter.

### JT21.

**(a)** $\frac{df}{dd} = 0.08$ L/km — "each kilometer of driving burns 0.08 L."

**(b)** No — per kilometer, not per second: the fuel is not draining in time, it is being spent over distance.

**(c)** 0.08 L/km and 0.08 L/s are the same digit in two jails: the denominator (km vs s) changes the entire sentence. The jail is the denominator.

> **Answer**: $0.08$ L/km vs L/s — the denominator is the jail

**Lens reading**: never read a degree without naming its denominator's world.

### JT22.

**(a)** $\frac{dR}{dx} = 2 - 0.1x$; at $x=10$: $1$ per mg — "each extra mg of dose buys 1 unit of response."

**(b)** The driver is dose (milligrams), not time — the body is not "speeding up," the response is trading per milligram.

**(c)** $\frac{dR}{dx} = 0$ at $x = 20$: the response peaks at 20 mg — a dose-location, not a moment in time. Flat means the dose-station is at the top.

> **Answer**: $1$/mg at $x=10$; peak at $x=20$ mg, not at a time

**Lens reading**: a peak can live on the dose axis, not the time axis.

### JT23.

**(a)** $\frac{dP}{dd} = 9.8$ kPa/m — "each meter deeper adds 9.8 kPa of pressure."

**(b)** The driver is depth — a place, not a clock. Pressure doesn't "flow deeper"; it answers to depth.

**(c)** At $d = 0$: $P = 101$ kPa (positive position) and $P' = 9.8$ (positive arrow) — both axes positive, nothing moving in time.

> **Answer**: $9.8$ kPa/m; surface: positive position, positive arrow

**Lens reading**: the driver is a coordinate — the sentence is a map, not a movie.

### JT24.

**(a)** $\frac{dC}{dq} = 2$ \$/unit — "each extra unit costs \$2."

**(b)** The 400 is a locked **value** (the fixed cost); the 2 is a **degree** (the marginal cost).

**(c)** Per unit, not per hour: the driver is quantity. One formula, one value and one degree, side by side — the units (\$ vs \$/unit) separate the jails.

> **Answer**: 400 = locked value; 2 \$/unit = degree

**Lens reading**: a formula can carry a value and a degree at once — the units sort them.

---

## Answer Check

| Problem | Answer |
|:---:|:---|
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
| SN1 | $B(10)=-300$, $B'=50$; crosses $t=16$ |
| SN2 | $T(10)=55$, $T'=-3$; 25 °C at $t=20$ |
| SN3 | $0$ and $0$ by coincidence; rises through |
| SN4 | $v=0$, $s\approx25.4$ m; falls after |
| SN5 | both $+1$; positions $+2$ vs $-5$ |
| SN6 | $s(3)=-16$, $v=6$; crosses $t=5$ with $v=10$ |
| SN7 | $-350$, $B'=-30$; never notices |
| SN8 | $f'=0$ at $x=1$, $f=2$; neither peak nor valley |
| SN9 | $T(10)=-5$, $T'=0.5$; crosses $t=20$ |
| SN10 | $0$ & $1000$ vs $100$ & $0$ |
| JA1 | $-4$ W/Ω vs $+4$ W/V |
| JA2 | $-2.25$ min/(km/h) vs $80$ km/h |
| JA3 | $V'=-2$ L/min; 50 is a value, $-2$ is a degree |
| JA4 | $-24.9$ kPa/m³ vs $0.083$ m³/K |
| JA5 | $-0.8$ W/s = $-4$ W/Ω · $0.2$ Ω/s |
| JA6 | $-2$ min/(km/h); $t$ is a duration; $t\to0^{+}$ |
| JA7 | $-2.25$ min/(km/h) vs $+80$ km/h |
| DC1 | $-1$ min/(L/min); duration; $T\to0^{+}$ |
| DC2 | $-1.67$ h/kW; lifetime shrinks |
| DC3 | $-\frac13$ day per (page/day) = −8 h |
| DC4 | $-2$ s per (MB/s) |
| DC5 | $-0.75$ week per (dollar/week) ≈ −5 days |
| DC6 | $-8$ h per (m³/h) |
| DC7 | $-\frac{3}{14}$ h/(km/h) ≈ −13 min |
| DC8 | $-2.5$ min per (page/min) |
| DC9 | $V'=-20$ L/min — clock jail; both flow forward |
| DC10 | $T\to+\infty$ then $T\to0^{+}$; never negative |
| JT1 | 2 h = value; −2 min/(km/h) = degree |
| JT2 | $-3$ °C/min vs $-0.0375$ h/(km/h) |
| JT3 | 2 drops/s & 0.05 mL/drop locked; 0.1 mL/s is the degree |
| JT4 | quantity/time = clock; time/quantity = duration |
| JT5 | $-2$ h = invalid input, not reversed time |
| JT6 | $-0.18$ L per (km/h) |
| JT7 | level $5\cdot10^6$ m³ vs flow $30$ m³/s |
| JT8 | $-20$ m climbing $+3$ vs $-40$ m sinking $-2$ — depth is a coordinate |
| JT9 | $q(45)=-25$ outside the model ($p\le40$); $q'=-5$ is a direction |
| JT10 | $0.08$ L/km ↔ $12.5$ km/L — reciprocals |
| JT11 | $50$ \$/yr = degree; 5%/yr = locked parameter |
| JT12 | $-24.9$ kPa/m³ (pressure) vs $-4$ W/Ω (power) |
| JT13 | $R'=0$ at $R=2000$ (peak); $R=0$ at $p=40$ |
| JT14 | $40\pi$ m³/m (shell) vs $4\pi$ m³/m (disk) |
| JT15 | "per" marks a degree |
| JT16 | 120 km = value vs 80 km/h = degree |
| JT17 | $P'=-12$ kPa/km; driver = altitude; $P=0$ at $h\approx8.42$ km |
| JT18 | $-5$ units/\$; driver = price, not a clock |
| JT19 | $6\pi$ m²/m; no seconds anywhere |
| JT20 | $0.083$ m³/K; driver = temperature |
| JT21 | $0.08$ L/km vs L/s — the denominator is the jail |
| JT22 | $1$/mg at $x=10$; peak at $x=20$ mg, not at a time |
| JT23 | $9.8$ kPa/m; surface: positive position, positive arrow |
| JT24 | 400 = locked value; 2 \$/unit = degree |
