# Solutions — 16C1A: Implicit Regions

> Back to [16C1A — Implicit Regions](../16C1A-integral-interpretation.md)

---

## Basic Drills

### D1.

kPa·m³ = 1000 Pa·m³ = 1000 J = 1 kJ.

> **Answer**: kJ

**Lens reading**: kPa × m³ = kJ — the units name the collected relation.

### D2.

$4\int_0^4\sqrt{16-x^2}dx = 16\pi \approx 50.3$.

> **Answer**: $16\pi$

**Lens reading**: the constraint's manufactured area, collected by symmetry.

### D3.

$500\ln 3 \approx 549.3$ kJ.

> **Answer**: $549.3$ kJ

**Lens reading**: the hyperbola's collected relation — positive because expansion lets the gas push out.

### D4.

$500\ln\frac13 = -549.3$ kJ — negative: the world compresses the gas, doing work on it.

> **Answer**: $-549.3$ kJ (compression)

**Lens reading**: the same relation collected backwards — the sign flips, and the payer changes.

### D5.

$\pi\cdot 2\cdot 3 = 6\pi \approx 18.85$.

> **Answer**: $6\pi$

**Lens reading**: the stretched circle's collected area.

### D6.

$\frac{800\ln 2}{2} = 400\ln 2 \approx 277.3$ kPa.

> **Answer**: $277.3$ kPa

**Lens reading**: the uniform relation delivering the hyperbola's total.

### D7.

$277.3 \times 2 = 554.5 = 800\ln 2$ ✓.

> **Answer**: $554.5$ ✓

**Lens reading**: the log-mean rectangle's total — equal to the hyperbola's own collection.

### D8.

$W = \int CV^{-\gamma}dV = \frac{CV^{1-\gamma}}{1-\gamma}$; since $pV = CV^{1-\gamma}$ at each endpoint, $W = \frac{p_2V_2-p_1V_1}{1-\gamma}$.

> **Answer**: $\frac{p_2V_2-p_1V_1}{1-\gamma}$

**Lens reading**: the adiabat's fingerprint formula — work read from the endpoints of the relation.

### D9.

$3\pi \approx 9.42$ — half the full ellipse.

> **Answer**: $3\pi$

**Lens reading**: one nested relation's layer.

### D10.

$p = \frac{C}{V}$ integrates to $\ln$ (10A's one special power); $p = CV^{-\gamma}$ integrates to a power. The law's exponent decides the integral's fingerprint.

> **Answer**: $1/V$ → log; $V^{-\gamma}$ → power

**Lens reading**: $1/V$ collects into a logarithm, $V^{-\gamma}$ into a power — two relations, two collections.

---

## Advanced Drills

### A1.

$W = \int_{V_1}^{V_2}\frac{C}{V}dV = C\ln\frac{V_2}{V_1}$. Check: $\frac{d}{dV}\left(C\ln\frac{V}{V_1}\right) = \frac{C}{V} = p$.

The check is free because work *is* the accumulation of $p\,dV$ — by construction (16C1's undo button), differentiating the total returns the rate.

> **Answer**: $C\ln\frac{V_2}{V_1}$; $dW/dV = p$ ✓

**Lens reading**: the collected reciprocal relation; the undo reads the pressure back.

### A2.

The log-mean is the average of $p$ with respect to equal volume steps, but $p = C/V$ falls *faster* than a straight line: equal volume steps near the right end come at lower pressure. The curve's long flat tail occupies more length, dragging the area-average below the arithmetic mean (known: log-mean < arithmetic mean for distinct positive values).

> **Answer**: the hyperbola's tail weights low pressure more

**Lens reading**: the curve's shape is the weighting — the relation's tail sits at low pressure, so the log-mean undershoots the midpoint.

### A3.

$u = x/a$, $v = y/b$: the map shrinks $x$ by $a$ and $y$ by $b$ — diagonal matrix with determinant $\frac{1}{ab}$ (12A2). Its inverse stretches areas by $ab$. The unit circle's area $\pi$ becomes $\pi ab$ on the ellipse.

> **Answer**: area scales by the stretch determinant $ab$ → $\pi ab$

**Lens reading**: the stretch factors are the relation's degrees on each axis; areas respond through the determinant.

### A4.

$p_2 = 300\cdot2^{-5/3} \approx 94.5$ kPa. Endpoint formula: $W = \frac{94.5\cdot2-300}{1-\frac53} \approx 166.5$ kJ. Direct: $C = 300$, $W = \frac{300}{1-\frac53}\left(2^{-2/3}-1\right) \approx 166.5$ kJ — agree.

The adiabat is $\gamma$ times steeper (14D1A), dives below the isotherm, and sweeps less area: keeping the heat inside costs the gas work output.

> **Answer**: $p_2\approx94.5$; $W\approx166.5$ kJ both ways; steeper curve → less area

**Lens reading**: two paths, one work — the relation's collection is the area; steeper means less.

### A5.

With $T$ fixed, $pV=C$ pins the curve and the area. With $T$ free, the same endpoints can be joined by different curves (an isotherm, a straight line in the $p$-$V$ plane, …), each with different heights — different areas, different work. Path-dependence is the signature of an unpinned constraint; it is exactly what 16C2's line integrals make precise.

> **Answer**: unpinned temperature ⟹ the path picks the area

**Lens reading**: unpinned temperature frees the path — the relation itself picks the area.

### A6.

Area $= 9\pi - 4\pi = 5\pi \approx 15.7$.

$I = \int_0^{2\pi}\int_2^3 r^2\cdot r\,dr\,d\theta = 2\pi\cdot\frac{81-16}{4} = \frac{65\pi}{2} \approx 102.1$ kg·m². The outer rim dominates: it is farther from the axis and $I$ weights distance squared.

> **Answer**: area $5\pi$; $I = \frac{65\pi}{2}\approx102.1$

**Lens reading**: the ring's inertia collects $r^2$ against the area relation.

### A7.

$I = \int_0^{2\pi}\int_0^R r^3\,dr\,d\theta = 2\pi\cdot\frac{R^4}{4} = \frac{\pi R^4}{2}$.

Fourth power: mass grows like $R^2$, mass sits at distances $\sim R$, and $I$ weights distance *squared* — $R^2\cdot R^2 = R^4$. The constraint's own nesting ($r^2\,dA$) is the fourth power.

> **Answer**: $\frac{\pi R^4}{2}$; mass $R^2$ × distance² $R^2$

**Lens reading**: mass × distance² — the inertia relation, collected.

### A8.

Compression: $dV < 0$ while $p > 0$, so every slice contributes $p\,dV < 0$ — negative work. The sign records who pays: positive = the gas pays energy out (expansion), negative = the outside pays energy in (compression). The energy budget balances either way.

> **Answer**: $dV<0$ with $p>0$ → negative; the sign names the payer

**Lens reading**: the sign names the payer — the relation's direction says who does the work.

### A9.

$V = \iint_{x^2+y^2\le1}\sqrt{1-x^2-y^2}\,dA = \int_0^{2\pi}\int_0^1\sqrt{1-r^2}\,r\,dr\,d\theta$. With $u = 1-r^2$: $\int_0^1\sqrt{1-r^2}\,r\,dr = \frac12\cdot\frac23 = \frac13$, so $V = 2\pi\cdot\frac13 = \frac{2\pi}{3}$ — half of $\frac{4\pi}{3}$, the unit ball (9C's sphere, sliced into cylinders).

> **Answer**: $\frac{2\pi}{3}$ — the hemisphere's volume

**Lens reading**: the hemisphere's volume — the implicit relation sliced into disks and collected.

### A10.

$x' = -3\cos^2 t\sin t$, $y' = 3\sin^2 t\cos t$, so $ds = 3|\sin t\cos t|dt$. One quarter: $3\int_0^{\pi/2}\sin t\cos t\,dt = \frac32$. Four quarters: length $= 6$.

Parametrizing is the fastest path because it *solves the constraint by geometry* — one parameter, one integral. The same step algebra performs for $y = \sqrt{\cdot}$, the parameter performs by construction.

> **Answer**: length 6; the parameter solves the constraint for you

**Lens reading**: the parameter solves the constraint — the relation is handed to you, ready to collect.

---

## Deep Insight

### DI1.

With $pV^{\gamma} = C$, both endpoints satisfy $p_iV_i = C V_i^{1-\gamma} = C V_i^{s}$ with $s = 1-\gamma$, so

$W = \dfrac{C(V_2^{s}-V_1^{s})}{s}$.

As $s\to0$ this is the derivative of $V^{s}$ with respect to $s$, evaluated at the two endpoints:

$\lim_{s\to0}\dfrac{V_2^{s}-V_1^{s}}{s} = \ln V_2 - \ln V_1 = \ln\dfrac{V_2}{V_1}$, so $W \to C\ln\dfrac{V_2}{V_1}$ — the isotherm formula ✓.

Numbers: $\gamma=1.001$: $W = 300\cdot\dfrac{2^{-0.001}-1}{-0.001} \approx 207.87$ kJ; the isotherm: $300\ln 2 \approx 207.94$ kJ — equal to three decimals. The apparent singularity at $\gamma=1$ is only a limit, never a cliff.

Physically: as $\gamma\to1$ the gas exchanges heat so freely that each bit of compression work leaks out — the adiabat softens continuously into the isotherm, and the stiffness factor melts into the logarithm. The power-law family $pV^{\gamma}=C$ and the log law are **one family**; $\ln$ is the $\gamma=1$ member, the boundary case of every power.

> **Answer**: $\lim_{\gamma\to1}W = C\ln\frac{V_2}{V_1}$; 207.87 vs 207.94 kJ — one family, the log as its boundary case

**Lens reading**: the adiabat's collection approaches the isotherm's logarithm as $\gamma\to1$ — one family of relations, the log as its boundary.

---

## Answer Check

| Problem | Answer |
|:---:|:---|
| D1 | kJ |
| D2 | $16\pi$ |
| D3 | $549.3$ kJ |
| D4 | $-549.3$ kJ |
| D5 | $6\pi$ |
| D6 | $277.3$ kPa |
| D7 | $554.5$ ✓ |
| D8 | endpoint formula |
| D9 | $3\pi$ |
| D10 | log vs power |
| A1 | $C\ln(V_2/V_1)$; check ✓ |
| A2 | log-mean below arithmetic |
| A3 | $\pi ab$ via determinant |
| A4 | $166.5$ kJ; less area |
| A5 | path picks the area |
| A6 | $5\pi$ · $\frac{65\pi}{2}$ |
| A7 | $\frac{\pi R^4}{2}$; $R^2\cdot R^2$ |
| A8 | negative = outside pays |
| A9 | $\frac{2\pi}{3}$ |
| A10 | 6 |
| DI1 | limit $= C\ln(V_2/V_1)$; 207.87 ≈ 207.94 kJ |
