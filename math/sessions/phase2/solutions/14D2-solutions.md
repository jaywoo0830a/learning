# Solutions — 14D2: Advanced Derivative Interpretation

> Back to [14D2 — Advanced Derivative Interpretation](../14D2-advanced-derivative-interpretation.md)

---

## Practice 1

| Quantity | Dimension vector |
|:---:|:---:|
| speed | $\mathrm{L} - \mathrm{T}$ |
| force | $\mathrm{M} + \mathrm{L} - 2\mathrm{T}$ |
| energy | $\mathrm{M} + 2\mathrm{L} - 2\mathrm{T}$ |
| power | $\mathrm{M} + 2\mathrm{L} - 3\mathrm{T}$ |

**(a)** $[\frac12 mv^2] = \mathrm{M} + (2\mathrm{L}-2\mathrm{T}) = \mathrm{M}+2\mathrm{L}-2\mathrm{T}$ = energy ✓

**(b)** $[Fv] = (\mathrm{M}+\mathrm{L}-2\mathrm{T}) + (\mathrm{L}-\mathrm{T}) = \mathrm{M}+2\mathrm{L}-3\mathrm{T}$ = power ✓

**(c)** $[\frac12 gt^2] = (\mathrm{L}-2\mathrm{T}) + 2\mathrm{T} = \mathrm{L}$ = length ✓

> **Answer**: all three formulas pass; each check was one vector addition

**Lens reading**: each check verifies the relation between a formula and the base dimensions — multiply quantities and their dimension-relations add. Units are the ledger of relations.

---

## Practice 2

**(a)** $\frac{\partial T}{\partial x} = -2x \to -6$ °C/m at $x=3$. $\frac{\partial T}{\partial y} = -4y \to -4$ °C/m at $y=1$.

**(b)** $\nabla T(3,1) = (-6,-4)$; magnitude $\sqrt{36+16} = \sqrt{52} \approx 7.2$ °C/m.

**(c)** Sentence: "walk toward the arrow's direction (roughly back toward the plate's center) and the temperature rises fastest — about 7.2 °C per meter."

> **Answer**: (a) $-6$, $-4$ °C/m (b) $(-6,-4)$, $\sqrt{52}\approx7.2$ °C/m

**Lens reading**: two partial degrees of relation to position ($-6$ and $-4$ °C/m) stack into the full relation — a vector whose magnitude (7.2 °C/m) is the strongest local response.

---

## Practice 3

$z = e^{i3t}$; $v = \frac{dz}{dt} = 3i\,e^{i3t} = 3i z$; $a = 3i\cdot 3i\,z = -9z$.

Speed $= 3$ m/s. The velocity is the position rotated **90° ahead** (multiply by $i$). The acceleration is the position rotated **180°** — it points **inward** (centripetal), magnitude $9$ m/s².

> **Answer**: $v = 3i z$ (speed 3, a quarter-turn ahead); $a = -9z$ (inward, magnitude 9)

**Lens reading**: velocity relates to position at degree $3i$ (quarter-turn ahead), acceleration at degree $-9$ (half-turn, inward) — circular motion is a relation whose degree keeps rotating.

---

## Practice 4

$f'(z) = 2z$, so $f'(1+i) = 2+2i$. Modulus $2\sqrt2 \approx 2.83$, argument $45°$.

A tiny square at $1+i$ is stretched $2.83\times$ and rotated $45°$ — no shear. Every shape keeps its angles (the lens is a rotation+scale).

> **Answer**: stretch $2\sqrt2\approx2.83$, rotate $45°$

**Lens reading**: near $1+i$, $z^2$'s degree of relation to its input is the lens $2+2i$ — stretch 2.83, rotate 45°. Locally, the map and its degree are the same thing.

---

## Practice 5: Real Battle — Reading the Spinning Plate

**(a)** At $(3,3)$: $v = (-6, 6)$ m/s, speed $\sqrt{36+36} = \sqrt{72} \approx 8.49$ m/s.

**(b)** $\omega = 2$ rad/s (the field is $(-\omega y, \omega x)$).

**(c)** No. If a potential $\phi$ existed, work around any closed loop would be zero — but this field pushes **along** every circle, so a lap earns positive work. Gradient fields cross their own contours perpendicularly; this field is tangent to circles. The loop test fails.

> **Answer**: (a) $(-6,6)$, ≈8.49 m/s (b) $\omega=2$ (c) no potential — nonzero circulation around circles

**Lens reading**: the spinning field relates velocity to position tangentially at every point — a relation with circulation. A potential would need the relation to be flat around every loop; this one never is.

---

## Practice 6: Real Battle — Fingerprints of a Linear Field

Trace $= 2+3 = 5$: the sum of stretch rates — total edge-growth (divergence). Determinant $= 6$: area scaling per unit time.

Pure-stretch lanes: $A(1,0) = (2,0)$ — the $x$-axis stretches $2\times$. $A(1,1) = (3,3) = 3(1,1)$ — the line along $(1,1)$ stretches $3\times$. The shear (the off-diagonal 1) tilts everything else but leaves trace and determinant alone.

> **Answer**: trace 5 (spreading), determinant 6 (area ×6); lanes $(1,0)$ stretch 2, $(1,1)$ stretch 3

**Lens reading**: trace and determinant are the field's fingerprints — the relation's total spreading and its area-scaling. Shear changes neither: it redirects without strengthening the relation.

---

## Basic Drills

### D1.

> **Answer**: $\mathrm{L}-\mathrm{T}$; $\mathrm{L}-2\mathrm{T}$; $\mathrm{M}+\mathrm{L}-2\mathrm{T}$; $\mathrm{M}+2\mathrm{L}-2\mathrm{T}$

**Lens reading**: four dimension-vectors, four relations to the base dimensions — velocity $\mathrm{L}-\mathrm{T}$, acceleration $\mathrm{L}-2\mathrm{T}$, force and energy adding mass. Each vector names the relation.

### D2.

$[mv^2] = \mathrm{M}+2\mathrm{L}-2\mathrm{T}$. $[mgh] = \mathrm{M} + (\mathrm{L}-2\mathrm{T}) + \mathrm{L} = \mathrm{M}+2\mathrm{L}-2\mathrm{T}$.

> **Answer**: both are $\mathrm{M}+2\mathrm{L}-2\mathrm{T}$ — energies ✓

**Lens reading**: both formulas relate to mass, length, and time identically ($\mathrm{M}+2\mathrm{L}-2\mathrm{T}$) — the same relation, two costumes.

### D3.

$e^{3t}$ meaningful (3 carries $s^{-1}$). $e^{x}$ with $x$ in m: meaningless. $\sin(2t)$ meaningful. $\sin(2x)$ with $x$ in m: meaningless.

> **Answer**: meaningless: $e^x$, $\sin(2x)$ (dimensional arguments)

**Lens reading**: transcendental functions require a zero-strength relation to every dimension — $e^x$ with $x$ in meters relates to length, and that is meaningless.

### D4.

Holding $y$ fixed: $\frac{\partial T}{\partial x} = 2x$. Holding $x$ fixed: $\frac{\partial T}{\partial y} = 2y$.

> **Answer**: $2x$, $2y$

**Lens reading**: $T$'s degree of relation to $x$ (with $y$ held) is $2x$; to $y$ (with $x$ held) is $2y$ — two partial relations, one field.

### D5.

$\nabla T = (3,-4)$, constant everywhere. Magnitude $5$ °C/m. Direction: the vector $(3,-4)$ — down-right, steepest descent along its opposite.

> **Answer**: $(3,-4)$, magnitude 5 °C/m

**Lens reading**: a linear field has a constant relation to position: degree $(3,-4)$, strength 5 °C/m — uniform everywhere.

### D6.

$v = 2i\,e^{i2t}$. Speed $=2$. The velocity is $90°$ ahead of the position — tangent to the unit circle.

> **Answer**: speed 2; $90°$ ahead (tangent)

**Lens reading**: velocity's relation to position is $2i$ — speed 2, a quarter-turn ahead: circular motion as a constant rotational relation.

### D7.

$F(2,0) = (0,6)$, length 6. It is tangent to the circle of radius 2 — a spinning-plate field with $\omega = 3$.

> **Answer**: $(0,6)$, length 6, tangent to the circle

**Lens reading**: at $(2,0)$ the field relates velocity to position as $(0,6)$ — pure tangent: the relation of a spinning plate with $\omega=3$.

### D8.

Trace $=5$: total stretch rate (divergence). Determinant $=6$: areas grow $6\times$ per unit time. Pure-stretch lanes: the two axes.

> **Answer**: trace 5, det 6; $x$ stretches 3, $y$ stretches 2

**Lens reading**: the field relates each axis to itself at degrees 3 and 2 — the trace sums the two relations, the determinant multiplies their effect on area.

### D9.

$\nabla T = (-2x,-4y) = 0$ only at $(0,0)$ — the warmest point (peak). Arrows point inward toward it (heat flows outward along $-\nabla T$).

> **Answer**: gradient vanishes at $(0,0)$, a maximum

**Lens reading**: the gradient vanishes where the field's relation to position pauses — the peak. The relation's zero is the warmest point, where temperature stops responding to movement.

### D10.

Pa/m — pressure per meter. The gradient always has field-units per length.

> **Answer**: Pa/m

**Lens reading**: pressure's relation to position has units Pa/m — field-units per meter, the gradient's universal costume.

---

## Advanced Drills

### A1.

$\tau \propto L^a g^b$: $[\tau] = \mathrm{T}$, $[L] = \mathrm{L}$, $[g] = \mathrm{L}-2\mathrm{T}$.

$\mathrm{T} = a\mathrm{L} + b(\mathrm{L}-2\mathrm{T})$: L-coefficients $a+b = 0$; T-coefficients $-2b = 1$ → $b = -\frac12$, $a = \frac12$.

So $\tau \propto \sqrt{L/g}$ — units alone give the full form. The true $\tau = 2\pi\sqrt{L/g}$: the $2\pi$ is dimensionless, so dimensional analysis can never find it. Units bound the answer; dimensionless constants are the only freedom units leave.

> **Answer**: $\tau \propto \sqrt{L/g}$; $2\pi$ is invisible to units

**Lens reading**: the pendulum's period relates to length at degree $\frac12$ and to gravity at degree $-\frac12$ — units alone read the relation's shape; only the dimensionless $2\pi$ escapes them.

### A2.

Move along a level curve with $r'(t)$. The chain rule:

$\frac{d}{dt}T(r(t)) = \frac{\partial T}{\partial x}x' + \frac{\partial T}{\partial y}y' = \nabla T\cdot r'(t)$.

On the level curve $T$ is constant, so $\frac{d}{dt}T = 0$. Hence $\nabla T \cdot r'(t) = 0$ for every tangent direction — the gradient is perpendicular to the level curve (12A2's perpendicular test).

> **Answer**: $\nabla T \cdot r' = 0$ on every level curve → gradient ⊥ contour

**Lens reading**: along a contour the field's relation to position is flat — the dot product with every tangent direction is zero, so the strongest relation must point across the contours.

### A3.

**(a)** $\nabla T = (2x, 2y, 2z) = 2(x,y,z)$.

**(b)** At radius $r$, arrows point radially **outward** (along the position vector) with length $2r$.

**(c)** Level surfaces are spheres $x^2+y^2+z^2=c$ (9C); the arrows cross each sphere at right angles, like porcupine quills. The gradient vanishes only at the origin — the coldest point.

> **Answer**: radial field $2(x,y,z)$, length $2r$; level surfaces spheres, crossed perpendicularly

**Lens reading**: temperature's relation to position is radial with strength $2r$ — the relation grows with distance and dies exactly at the source.

### A4.

$f'(z) = 3z^2$; at $z_0 = 1+i$: $f'(z_0) = 3(1+i)^2 = 3(2i) = 6i$.

Modulus $6$: stretch $6\times$. Argument $90°$: rotate a quarter-turn. A tiny shape at $1+i$ is enlarged sixfold and turned $90°$.

> **Answer**: stretch 6, rotate $90°$

**Lens reading**: $z^3$'s local relation near $1+i$ is the lens $6i$ — stretch 6, rotate 90°. Each point carries its own degree of relation.

### A5.

$f(z) = \bar z$. Real direction: $h$ real → $\frac{\overline{z_0+h}-\overline{z_0}}{h} = \frac{\bar h}{h} = 1$.

Imaginary direction: $h = it$ → $\frac{\overline{it}}{it} = \frac{-it}{it} = -1$.

The two directions give different lenses ($1$ vs $-1$). A reflection cannot be one rotation+scale — no complex derivative exists.

> **Answer**: real direction → 1, imaginary direction → −1: no single lens, $\bar z$ is not complex-differentiable

**Lens reading**: conjugation's relation to its input depends on the direction of approach — 1 along the real axis, −1 along the imaginary. No single degree of relation can serve; the map has no lens.

### A6.

$F = (-\omega y, \omega x)$: $\frac{\partial F_2}{\partial x} - \frac{\partial F_1}{\partial y} = \omega - (-\omega) = 2\omega$ — the **spin density**; every point rotates at $2\omega$.

$F = (x,y)$: $0 - 0 = 0$ — no spin, pure spreading.

> **Answer**: vortex: $2\omega$ (rotation); source: $0$ (spreading). This is the curl

**Lens reading**: the vortex relates velocity to position with spin $2\omega$ at every point; the source field with zero — one relation that turns, one that spreads.

### A7.

Trace $= 2+3 = 5$; determinant $= 2\cdot3 - 1\cdot0 = 6$. Lanes: $A(1,0) = (2,0)$ — stretch 2; $A(1,1) = (3,3)$ — stretch 3.

The shear (off-diagonal 1) tilts vectors but adds nothing to the trace (diagonal entries unchanged) or the determinant (shear preserves area — a parallelogram and its base rectangle share base, height, and area). Shear redirects; only stretch and spin change the fingerprints.

> **Answer**: trace 5, det 6; lanes $(1,0)$→2, $(1,1)$→3; shear redirects without changing either

**Lens reading**: shear redirects the field's action but leaves its relation's fingerprints intact — trace 5, determinant 6, and two pure-stretch lanes.

### A8.

$[t/\tau] = 0$ forces $[\tau] = \mathrm{T}$ — the time constant has units of time.

After one $\tau$: $T(\tau) = T_0 e^{-1} \approx 0.368\,T_0$ — about **63% of the gap has closed** (37% remains). Every additional $\tau$ shaves off the same fraction.

The exponent must be dimensionless because $e^x = 1 + x + x^2/2 + \cdots$ adds different powers — meaningful only when all terms are pure numbers.

> **Answer**: $[\tau]=\mathrm{T}$; $e^{-1}\approx37\%$ remains after one $\tau$; dimensionless exponent required

**Lens reading**: the time constant is the relation's unit — after one $\tau$, the gap's relation to time has delivered 63% of the return. The exponent must carry zero relation to every dimension.

### A9.

**(a)** $\nabla z = (2x, -2y)$.

**(b)** Along the $x$-axis ($y=0$): arrows $(2x, 0)$ point **outward** along $x$. Along the $y$-axis ($x=0$): arrows $(0,-2y)$ point **inward** along $y$. Up two ridges, down two valleys — the saddle field of 9C.

**(c)** At the origin $\nabla z = 0$, but it is neither peak nor pit: approaching along $x$ the surface rises, along $y$ it falls — a saddle point. The gradient vanishing is a *flag*, never a verdict (14D1's lesson, at field level).

> **Answer**: $(2x,-2y)$; outward along $x$, inward along $y$; origin is a saddle

**Lens reading**: the saddle's relation to position is outward along $x$, inward along $y$ — two opposite relations meeting at a point where the net relation vanishes, yet neither peak nor pit.

### A10.

$v = \frac{d}{dt}e^{i\omega t} = i\omega\,e^{i\omega t} = i\omega z$. $a = i\omega\cdot i\omega z = -\omega^2 z$.

Each differentiation multiplies by $i\omega$: one quarter-turn (with scale $\omega$). Two quarter-turns $= 180°$: the acceleration points opposite the position — **centripetal**, magnitude $\omega^2 r$. The "plus 90° per derivative" is the whole story of circular motion, compressed into one multiplication.

> **Answer**: $v = i\omega z$ (90° ahead), $a = -\omega^2 z$ (inward)

**Lens reading**: each differentiation rotates the relation a quarter-turn more — velocity's relation to position is $i\omega$, acceleration's is $-\omega^2$: the relation keeps turning inward.

---

## Deep Insight

### DI1.

**(a)** $\Delta(x^2+y^2) = 2+2 = 4$; $\Delta(x^2-y^2) = 2-2 = 0$; $\Delta(x^3-3xy^2)$: $\nabla = (3x^2-3y^2,\ -6xy)$, divergence $6x-6x = 0$; $\Delta(x^2) = 2$.

**(b)** Along the $x$-direction the arrows lengthen as $x$ grows ($+2$ of spreading); along the $y$-direction they shorten ($-2$). The two cancel: the flow is **area-preserving** — what it stretches horizontally it squeezes vertically. A tiny square carried by the arrow field deforms into a parallelogram of the same area. No sources, no sinks.

**(c)** $\Delta T = 0$ is the **mean-value property**: $T$ at the point equals the average of $T$ over any tiny circle around it. The surface neither bulges up (bowl, $\Delta>0$) nor caps down (hill, $\Delta<0$) — it is perfectly flat *in the average sense*, which is exactly what a saddle is. $\Delta T$ is the "bulge detector": positive at bowl points, negative at peak points, zero at saddles. The ladder scalar → gradient → divergence lands on the one scalar that reports the surface's shape.

> **Answer**: $\Delta = 4,\ 0,\ 0,\ 2$; the saddle's gradient flow is area-preserving (harmonic = mean-value property)

**Lens reading**: the Laplacian reads the field's relation to its own gradient — the net spreading. The saddle's two partial relations cancel exactly: what the $x$-relation adds, the $y$-relation takes, leaving an area-preserving flow and the mean-value property.

---

## Answer Check

| Problem | Answer |
|:---:|:---|
| P1 | speed $\mathrm{L}-\mathrm{T}$ · force $\mathrm{M}+\mathrm{L}-2\mathrm{T}$ · energy $\mathrm{M}+2\mathrm{L}-2\mathrm{T}$ · power $\mathrm{M}+2\mathrm{L}-3\mathrm{T}$ |
| P2 | $(-6,-4)$, $\sqrt{52}\approx7.2$ °C/m |
| P3 | $v=3iz$ (speed 3, 90° ahead); $a=-9z$ inward |
| P4 | stretch $2\sqrt2$, rotate 45° |
| P5 | $(-6,6)$, ≈8.49; $\omega=2$; no potential |
| P6 | trace 5, det 6; lanes 2× and 3× |
| D1 | $\mathrm{L}-\mathrm{T}$ · $\mathrm{L}-2\mathrm{T}$ · $\mathrm{M}+\mathrm{L}-2\mathrm{T}$ · $\mathrm{M}+2\mathrm{L}-2\mathrm{T}$ |
| D2 | both energies ✓ |
| D3 | $e^{x}$, $\sin(2x)$ meaningless |
| D4 | $2x$, $2y$ |
| D5 | $(3,-4)$, 5 °C/m |
| D6 | speed 2, 90° ahead |
| D7 | $(0,6)$, length 6 |
| D8 | trace 5, det 6 |
| D9 | $(0,0)$ = maximum |
| D10 | Pa/m |
| A1 | $\tau\propto\sqrt{L/g}$ |
| A2 | $\nabla T\cdot r'=0$ |
| A3 | $2(x,y,z)$, length $2r$, ⊥ spheres |
| A4 | stretch 6, rotate 90° |
| A5 | 1 vs −1 → not differentiable |
| A6 | $2\omega$ vs 0 |
| A7 | 5, 6; lanes 2×, 3× |
| A8 | $[\tau]=\mathrm{T}$, 37% remains |
| A9 | outward along $x$, inward along $y$; saddle |
| A10 | $v=i\omega z$; $a=-\omega^2 z$ |
| DI1 | $\Delta=4,0,0,2$ — saddle flow area-preserving |
