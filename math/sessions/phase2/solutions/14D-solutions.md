# Solutions — 14D: Derivative Interpretation

> Back to [14D — Derivative Interpretation](../14D-derivative-interpretation.md)

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

**(b)** $m(t)$ changing: $F = m\frac{dv}{dt} + v\frac{dm}{dt}$. First term: accelerating the current mass. Second term: the momentum carried off by the ejected mass — for a rocket $\frac{dm}{dt} < 0$, so $-v\frac{dm}{dt}$ is positive thrust. Throw mass backward, get pushed forward.

> **Answer**: $F=ma$ for fixed mass; rockets get thrust from the $v\,dm/dt$ term

### A9.

The exact direction is: $f'(x) > 0$ on an interval ⟹ $f$ increasing there. The converse is false. For $f(x)=x^3$, $f'(0)=0$ but the function is increasing *everywhere*: between any two points $a<b$ there is a $c$ with $\frac{f(b)-f(a)}{b-a} = f'(c) = 3c^2 \ge 0$, and the quotient is positive whenever $a<b$. A zero derivative at a single point cannot force a flat spot — flatness needs the derivative zero on a whole interval. So "$f'=0$" is only a *candidate flag* for an extremum, and "$f'>0$" is a sufficient, not necessary, test.

> **Answer**: $f'>0$ ⟹ increasing is exact; the converse fails at single points like $x=0$ of $x^3$

### A10.

$\frac{dV}{dr} = 2\pi r h = 2\pi(3)(10) = 60\pi \approx 188.5$ cm³ per cm — the **lateral surface** (the wrapped band around the cylinder).

$\frac{dV}{dh} = \pi r^2 = 9\pi \approx 28.3$ cm³ per cm — the **base disk**.

> **Answer**: $60\pi$ = lateral area (band), $9\pi$ = base area (disk)

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
| A1 | $2\pi r$; corner $(dr)^2$ vanishes |
| A2 | $4\pi r^2 dr$; half-side gives $6s^2$ |
| A3 | $\frac{dK}{dt}=Fv$; power |
| A4 | err $\le 0.00133$; local only |
| A5 | $q=5$, $MC=AC=15$ |
| A6 | $R'=q(1+E)$; $p=25$ |
| A7 | $-0.65$ °C/100m; ≈3.08 km |
| A8 | $F=ma$; thrust $=v\,dm/dt$ |
| A9 | converse fails; $f'=0$ is only a flag |
| A10 | $60\pi$ lateral · $9\pi$ base |
