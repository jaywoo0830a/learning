# Solutions — 14D1A: Implicit Relations

> Back to [14D1A — Implicit Relations](../14D1A-derivative-interpretation.md)

---

## Practice 1

**(a)** $\frac{dy}{dx} = -\frac{x}{y} = -\frac34$ at $(3,4)$. Negative: on the upper-right arc, moving right trades away height — $x$ and $y$ fight.

**(b)** Vertical: $y = 0$ → $x = \pm5$. Horizontal: $x = 0$ → $y = \pm5$.

**(c)** One $x$ allows two $y$'s, so the circle is not a function of $x$. But near every point except the two tips $(\pm5, 0)$, the curve is locally a graph, so the derivative exists there; at the tips the trade ratio explodes (vertical tangent).

> **Answer**: (a) $-\frac34$ (b) vertical at $(\pm5,0)$, horizontal at $(0,\pm5)$ (c) locally a graph everywhere except the tips

---

## Practice 2

**(a)** $V = \frac{600}{150} = 4$ m³; $\frac{dV}{dp} = -\frac{V}{p} = -\frac{4}{150} = -0.0267$ m³/kPa.

**(b)** "Each extra kPa of pressure squeezes out about 0.0267 m³ of volume."

**(c)** $\frac{dV}{dt} = \frac{dV}{dp}\frac{dp}{dt} = -0.0267 \times 3 = -0.08$ m³/s.

> **Answer**: (a) $-0.0267$ m³/kPa (b) trade rate (c) $-0.08$ m³/s

---

## Practice 3

**(a)** Log-differentiation: $\frac{P'}{P} + \frac{V'}{V} = \frac{T'}{T}$.

**(b)** $\frac{T'}{T} = \frac{5}{200} + \frac{-0.2}{3} = 0.025 - 0.0667 = -0.0417$ — temperature falls about 4.2% per second. The volume shrinkage (−6.7%/s) outweighs the pressure growth (+2.5%/s), and the equation forces the difference onto temperature.

> **Answer**: $\frac{T'}{T} = -0.0417$ (−4.2%/s — the budget forces it)

---

## Practice 4

**(a)** $2x\,x' + 2y\,y' + 2z\,z' = 0$: $2(1)(1) + 2(2)(1) + 2(2)z' = 0$ → $2 + 4 + 4z' = 0$ → $z' = -\frac32$.

**(b)** The velocity is perpendicular to the position vector — motion on a sphere is tangent to it. The implicit equation, differentiated, is the geometric fact "radius ⊥ tangent."

> **Answer**: (a) $z' = -\frac32$ (b) velocity ⊥ radius

---

## Practice 5: Real Battle — The Folium's Leaf

**(a)** $y' = \frac{2y - x^2}{y^2 - 2x}$. At $(3,3)$: $\frac{6-9}{9-6} = -1$ — a diagonal tangent on the leaf's outer tip.

**(b)** Horizontal: numerator $= 0$ → $2y = x^2$. Substitute into the curve: $x^3 + \frac{x^6}{8} = 3x^3$ → $x^6 = 16x^3$ → $x^3 = 16$ → $x = 2^{4/3} \approx 2.52$, $y = 2^{5/3} \approx 3.17$. Check: $x^3 + y^3 = 16 + 32 = 48 = 6\cdot 8 = 6xy$ ✓.

> **Answer**: (a) slope $-1$ at $(3,3)$ (b) horizontal at $(2^{4/3},\,2^{5/3}) \approx (2.52,\,3.17)$

---

## Practice 6: Real Battle — Stiffness of a Process

Isotherm: $\frac{dp}{dV} = -\frac{p}{V}$. Adiabat ($\gamma = 1.4$): $\frac{dp}{dV} = -1.4\frac{p}{V}$ — 1.4 times steeper at the same point.

Why: compression does work on the gas; in the adiabat no heat leaks away, so the work becomes internal energy, the temperature rises, and the pressure climbs *further*. The isotherm dumps the heat and stays flatter. The extra steepness is the price of keeping the heat.

> **Answer**: $-1.4\frac{p}{V}$ vs $-\frac{p}{V}$; heating stiffens the curve by the factor $\gamma$

---

## Basic Drills

### D1.

$\frac{dy}{dx} = -\frac{4x}{9y} = 0$ at $(0,2)$ — a horizontal tangent at the ellipse's top.

> **Answer**: 0 — horizontal tangent at the top

### D2.

$V = 4$ m³ at $p = 150$: $\frac{dV}{dp} = -\frac{4}{150} = -0.0267$ m³/kPa.

> **Answer**: $-0.0267$ m³/kPa

### D3.

$y + x y' = 0$ → $y' = -\frac{y}{x} = -\frac43$: each unit of $x$ trades away $\frac43$ units of $y$.

> **Answer**: $-\frac43$ — a 4-to-3 trade

### D4.

Vertical where $y = 0$: $(\pm5, 0)$. Horizontal where $x = 0$: $(0, \pm5)$.

> **Answer**: vertical at $(\pm5,0)$; horizontal at $(0,\pm5)$

### D5.

$\frac{dV}{dp} = -\frac{V}{p}$ → $E = \frac{p}{V}\left(-\frac{V}{p}\right) = -1$.

> **Answer**: $E = -1$ — unit elastic

### D6.

$2(1)(1) + 2(2)(1) + 2(2)z' = 0$ → $z' = -\frac32$.

> **Answer**: $z' = -\frac32$

### D7.

$-\gamma\frac{p}{V}$ vs $-\frac{p}{V}$: ratio $\gamma$ (1.4 for air).

> **Answer**: ratio $\gamma$ — the adiabat is $\gamma$ times steeper

### D8.

$x' + y' + z' = 0$ → $z' = -(x'+y') = -(2-1) = -1$ m/s.

> **Answer**: $-1$ m/s

### D9.

$-\frac{x}{y} \to -\infty$ as $(x,y)\to(5,0)$: the trade ratio blows up — a vertical tangent where $x$ can no longer buy $y$.

> **Answer**: blows up — vertical tangent at the tip

### D10.

$V' = -\frac{V}{P}P' = -\frac{4}{100}\cdot 3 = -0.12$ m³/s.

> **Answer**: $-0.12$ m³/s

---

## Advanced Drills

### A1.

$p\frac{dV}{dp} + V = 0$ → $\frac{dV}{dp} = -\frac{V}{p}$; hence $E = -1$.

Uniqueness: solve $\frac{dV}{dp} = -\frac{V}{p}$ → $\frac{dV}{V} = -\frac{dp}{p}$ → $\ln V = -\ln p + c$ → $pV = C$. The elasticity condition *is* the hyperbola — constant unit elasticity characterizes Boyle's law.

> **Answer**: $\frac{dV}{dp}=-\frac{V}{p}$, $E=-1$; constant elasticity ⟺ hyperbola

### A2.

Log-differentiate $PV=nRT$: $\frac{P'}{P}+\frac{V'}{V}=\frac{T'}{T}$.

Numbers: $0.025 - 0.0667 = -0.0417$. The volume term dominates — the gas is cooling at 4.2%/s even though pressure rises, because the container is expanding faster (percentage-wise) than pressure grows.

> **Answer**: $-0.0417$; the shrinkage outruns the pressure rise

### A3.

$2y = x^2$; with the curve: $x^3 + \frac{x^6}{8} = 3x^3$ → $x^6 = 16x^3$ → $x^3 = 16$ → $x = 2^{4/3}$, $y = 2^{5/3}$. Verify: $16+32 = 48 = 6\cdot8$ ✓.

> **Answer**: $(2^{4/3}, 2^{5/3})$ on the curve ✓

### A4.

$\frac{d}{dV}(pV^{\gamma}) = \frac{dp}{dV}V^{\gamma} + \gamma pV^{\gamma-1} = 0$ → $\frac{dp}{dV} = -\gamma\frac{p}{V}$.

Compression work raises internal energy; without heat exchange the temperature rises, pushing pressure up further — the extra factor $\gamma$ is that heating, priced into the slope.

> **Answer**: $-\gamma\frac{p}{V}$; the heating shows up as extra steepness

### A5.

Differentiating $\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}=1$ along a path: $\frac{2x}{a^2}x' + \frac{2y}{b^2}y' + \frac{2z}{c^2}z' = 0$, i.e. $\left(\frac{x}{a^2},\frac{y}{b^2},\frac{z}{c^2}\right)\cdot(x',y',z')=0$.

The weighted vector is the ellipsoid's normal direction: motion on the surface is perpendicular to it. On the sphere ($a=b=c$) this reduces to radius ⊥ velocity. The weights $1/a^2$ etc. stretch the perpendicularity the same way the surface is stretched.

> **Answer**: weighted dot product $=0$ — a stretched perpendicularity

### A6.

Static: $\frac{dV}{dp} = -0.04$ m³/kPa — the exchange rate, "each kPa buys 0.04 m³," valid whenever the gas sits at this state.

Dynamic: $\frac{dV}{dt} = -0.08$ m³/s — the cash flow, "right now, volume drains at 0.08 m³ per second," tied to *this* pressure's speed. Exchange rate vs cash flow: both answer "volume responds to pressure," at different time scales.

> **Answer**: $-0.04$ m³/kPa (trade) vs $-0.08$ m³/s (flow)

### A7.

Where $y'$ is finite, a small change in $x$ produces a well-defined change in $y$ — locally the equation *can* be solved for $y = f(x)$ (the implicit function theorem's conclusion). Where the denominator vanishes, the trade ratio explodes and no such local graph exists (vertical tangent). "Denominator ≠ 0" is exactly "locally a graph."

> **Answer**: finite derivative ⟺ locally solvable for $y$; denominator 0 kills it

### A8.

$\frac{dq}{q} = -k\frac{dp}{p}$ → $\ln q = -k\ln p + c$ → $q\,p^{k} = C$. Boyle ($k=1$) and power-law demand curves are one family — the elasticity constant is the exponent of the family.

> **Answer**: $qp^k = C$ — elasticity is the exponent

### A9.

Parametric: $\frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{5\cos\theta}{-5\sin\theta} = -\frac{x}{y}$ ✓ — identical.

The parametric lens keeps time visible ($x'$, $y'$ are actual speeds); the implicit lens shows the pure geometric trade. Same curve, two questions: "how fast?" (parametric) vs "how steep?" (implicit).

> **Answer**: both give $-\frac{x}{y}$; parametric reads time, implicit reads geometry

### A10.

**(a)** $P$ fixed: $V = \frac{nRT}{P}$ → $\frac{dV}{dT} = \frac{nR}{P}$ — m³/K: thermal expansion at constant pressure.

**(b)** $V$ fixed: $P = \frac{nRT}{V}$ → $\frac{dP}{dT} = \frac{nR}{V}$ — kPa/K: pressure rise on heating in a sealed container.

**(c)** The same law, two different "holds" — the held variable decides the meaning (14D1's "with respect to what"). One equation manufactures as many derivative-meanings as it has variables.

> **Answer**: $\frac{nR}{P}$ m³/K (expansion), $\frac{nR}{V}$ kPa/K (sealed heating)

---

## Deep Insight

### DI1.

**(a)** $y' = \frac{2y-x^2}{y^2-2x} = \frac{0}{0}$ at $(0,0)$; its reciprocal $x' = \frac{y^2-2x}{2y-x^2} = \frac{0}{0}$ too. Neither variable can be traded for the other.

**(b)** $t\to0$: $x\approx6t$, $y\approx6t^2$ → $y \approx \frac{x^2}{6}$ — a branch tangent to the $x$-axis. $t\to\infty$: $x\approx\frac{6}{t^2}$, $y\approx\frac{6}{t}$ → $y^2 \approx 6x$ — a branch tangent to the $y$-axis. Two branches, two tangent directions, both through the origin.

**(c)** "Locally a graph" needs the trade ratio finite — i.e. at least one partial of $F = x^3+y^3-6xy$ nonzero: $F_x = 3x^2-6y$, $F_y = 3y^2-6x$; at the origin **both** vanish. The gradient dying is the machine's fuse: the tangent direction becomes ambiguous and no variable can serve as the local coordinate. Everywhere else on the folium, one partial survives and A7's reading works. The derivative sees everything except the points where the gradient vanishes.

> **Answer**: (0,0) is the lone singular point; branches $y\approx x^2/6$ and $y^2\approx6x$; gradient $(F_x,F_y)=(0,0)$ is the breakdown condition

---

## Answer Check

| Problem | Answer |
|:---:|:---|
| P1 | $-\frac34$ · vertical $(\pm5,0)$ · horizontal $(0,\pm5)$ |
| P2 | $-0.0267$ m³/kPa · $-0.08$ m³/s |
| P3 | $-0.0417$ (−4.2%/s) |
| P4 | $z'=-\frac32$; velocity ⊥ radius |
| P5 | slope $-1$ · $(2^{4/3},2^{5/3})$ |
| P6 | $-1.4\frac{p}{V}$ vs $-\frac{p}{V}$ |
| D1 | 0 — horizontal at top |
| D2 | $-0.0267$ m³/kPa |
| D3 | $-\frac43$ |
| D4 | $(\pm5,0)$; $(0,\pm5)$ |
| D5 | $E=-1$ |
| D6 | $-\frac32$ |
| D7 | $\gamma$ |
| D8 | $-1$ m/s |
| D9 | blows up at the tip |
| D10 | $-0.12$ m³/s |
| A1 | hyperbola ⟺ $E=-1$ |
| A2 | $-0.0417$ |
| A3 | $(2^{4/3},2^{5/3})$ ✓ |
| A4 | $-\gamma\frac{p}{V}$ |
| A5 | weighted dot $=0$ |
| A6 | trade vs flow |
| A7 | denominator 0 kills local graph |
| A8 | $qp^k=C$ |
| A9 | both $-\frac{x}{y}$ |
| A10 | $\frac{nR}{P}$, $\frac{nR}{V}$ |
| DI1 | singular point; branches $y\approx x^2/6$, $y^2\approx6x$ |
