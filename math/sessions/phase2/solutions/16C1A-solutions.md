# Solutions — 16C1A: Implicit Regions

> Back to [16C1A — Implicit Regions](../16C1A-integral-interpretation.md)

---

## Practice 1

Solve: $y = \pm\sqrt{16-x^2}$. The full circle is four quarters:

$A = 4\int_0^4\sqrt{16-x^2}\,dx = 4\cdot\frac{16\pi}{4} = 16\pi \approx 50.3$ (units² — m² if axes are meters).

The symmetry factor 4 matters: $2\int_0^4$ would give only the top half.

> **Answer**: $16\pi \approx 50.3$, with symmetry factor 4

---

## Practice 2

$p = \frac{500}{V}$, so $W = \int_1^3\frac{500}{V}dV = 500\ln 3 \approx 549.3$ kJ.

Positive: the gas expands, pushing outward — it does work *on* the world. Units: kPa·m³ = kJ.

> **Answer**: $500\ln 3 \approx 549.3$ kJ (positive — expansion)

---

## Practice 3

**(a)** $\bar p = \frac{1}{4-2}\int_2^4\frac{800}{V}dV = \frac{800\ln 2}{2} = 400\ln 2 \approx 277.3$ kPa.

**(b)** $W = \bar p\,\Delta V = 277.3 \times 2 = 554.5$ kJ, and directly $W = 800\ln 2 \approx 554.5$ kJ ✓ — the equal-area rectangle.

**(c)** Midpoint: $\frac{400+200}{2} = 300$ kPa — too high. The hyperbola flattens toward the axis: it spends more of its length at large $V$ (low pressure), so the area-average sits below the midpoint. The curve's shape is the weighting.

> **Answer**: (a) $400\ln 2\approx277.3$ kPa (b) $554.5$ kJ ✓ (c) log-mean < midpoint

---

## Practice 4

Integration: $y = 3\sqrt{1-\frac{x^2}{4}}$; $A = 4\int_0^2 3\sqrt{1-\frac{x^2}{4}}\,dx = 12\int_0^2\sqrt{1-\frac{x^2}{4}}dx = 6\pi \approx 18.85$.

Stretch: $u=\frac{x}{2}$, $v=\frac{y}{3}$ maps the ellipse to the unit circle; area scales by the stretch factors $2\times3$, so $A = \pi\cdot 2\cdot 3 = 6\pi$ — same.

> **Answer**: $6\pi \approx 18.85$ by both methods

---

## Practice 5: Real Battle — Adiabatic Expansion

$p_2 = p_1\left(\frac{V_1}{V_2}\right)^{\gamma} = 300\cdot 2^{-5/3} \approx 94.5$ kPa.

$W = \frac{p_2V_2 - p_1V_1}{1-\gamma} = \frac{94.5\cdot 2 - 300\cdot 1}{1-\frac53} = \frac{-111}{-0.667} \approx 166.5$ kJ.

The isotherm through the same start ($pV = 300$) would give $W = 300\ln 2 \approx 207.9$ kJ — more. The adiabat is steeper, dives lower, sweeps less area: keeping the heat costs work.

> **Answer**: $p_2\approx94.5$ kPa, $W\approx166.5$ kJ (less than the isotherm's 207.9)

---

## Practice 6: Real Battle — The Ring

Area: $9\pi - 4\pi = 5\pi \approx 15.7$.

Mass with $\rho = r$: $M = \int_0^{2\pi}\int_2^3 r\cdot r\,dr\,d\theta = 2\pi\cdot\frac{27-8}{3} = \frac{38\pi}{3} \approx 39.8$ kg — the outer rim dominates both the area and the mass.

> **Answer**: area $5\pi$; mass $\frac{38\pi}{3}\approx39.8$ kg

---

## Basic Drills

### D1.

kPa·m³ = 1000 Pa·m³ = 1000 J = 1 kJ.

> **Answer**: kJ

### D2.

$4\int_0^4\sqrt{16-x^2}dx = 16\pi \approx 50.3$.

> **Answer**: $16\pi$

### D3.

$500\ln 3 \approx 549.3$ kJ.

> **Answer**: $549.3$ kJ

### D4.

$500\ln\frac13 = -549.3$ kJ — negative: the world compresses the gas, doing work on it.

> **Answer**: $-549.3$ kJ (compression)

### D5.

$\pi\cdot 2\cdot 3 = 6\pi \approx 18.85$.

> **Answer**: $6\pi$

### D6.

$\frac{800\ln 2}{2} = 400\ln 2 \approx 277.3$ kPa.

> **Answer**: $277.3$ kPa

### D7.

$277.3 \times 2 = 554.5 = 800\ln 2$ ✓.

> **Answer**: $554.5$ ✓

### D8.

$W = \int CV^{-\gamma}dV = \frac{CV^{1-\gamma}}{1-\gamma}$; since $pV = CV^{1-\gamma}$ at each endpoint, $W = \frac{p_2V_2-p_1V_1}{1-\gamma}$.

> **Answer**: $\frac{p_2V_2-p_1V_1}{1-\gamma}$

### D9.

$3\pi \approx 9.42$ — half the full ellipse.

> **Answer**: $3\pi$

### D10.

$p = \frac{C}{V}$ integrates to $\ln$ (10A's one special power); $p = CV^{-\gamma}$ integrates to a power. The law's exponent decides the integral's fingerprint.

> **Answer**: $1/V$ → log; $V^{-\gamma}$ → power

---

## Advanced Drills

### A1.

$W = \int_{V_1}^{V_2}\frac{C}{V}dV = C\ln\frac{V_2}{V_1}$. Check: $\frac{d}{dV}\left(C\ln\frac{V}{V_1}\right) = \frac{C}{V} = p$.

The check is free because work *is* the accumulation of $p\,dV$ — by construction (16C1's undo button), differentiating the total returns the rate.

> **Answer**: $C\ln\frac{V_2}{V_1}$; $dW/dV = p$ ✓

### A2.

The log-mean is the average of $p$ with respect to equal volume steps, but $p = C/V$ falls *faster* than a straight line: equal volume steps near the right end come at lower pressure. The curve's long flat tail occupies more length, dragging the area-average below the arithmetic mean (known: log-mean < arithmetic mean for distinct positive values).

> **Answer**: the hyperbola's tail weights low pressure more

### A3.

$u = x/a$, $v = y/b$: the map shrinks $x$ by $a$ and $y$ by $b$ — diagonal matrix with determinant $\frac{1}{ab}$ (12A2). Its inverse stretches areas by $ab$. The unit circle's area $\pi$ becomes $\pi ab$ on the ellipse.

> **Answer**: area scales by the stretch determinant $ab$ → $\pi ab$

### A4.

$p_2 = 300\cdot2^{-5/3} \approx 94.5$ kPa. Endpoint formula: $W = \frac{94.5\cdot2-300}{1-\frac53} \approx 166.5$ kJ. Direct: $C = 300$, $W = \frac{300}{1-\frac53}\left(2^{-2/3}-1\right) \approx 166.5$ kJ — agree.

The adiabat is $\gamma$ times steeper (14D1A), dives below the isotherm, and sweeps less area: keeping the heat inside costs the gas work output.

> **Answer**: $p_2\approx94.5$; $W\approx166.5$ kJ both ways; steeper curve → less area

### A5.

With $T$ fixed, $pV=C$ pins the curve and the area. With $T$ free, the same endpoints can be joined by different curves (an isotherm, a straight line in the $p$-$V$ plane, …), each with different heights — different areas, different work. Path-dependence is the signature of an unpinned constraint; it is exactly what 16C2's line integrals make precise.

> **Answer**: unpinned temperature ⟹ the path picks the area

### A6.

Area $= 9\pi - 4\pi = 5\pi \approx 15.7$.

$I = \int_0^{2\pi}\int_2^3 r^2\cdot r\,dr\,d\theta = 2\pi\cdot\frac{81-16}{4} = \frac{65\pi}{2} \approx 102.1$ kg·m². The outer rim dominates: it is farther from the axis and $I$ weights distance squared.

> **Answer**: area $5\pi$; $I = \frac{65\pi}{2}\approx102.1$

### A7.

$I = \int_0^{2\pi}\int_0^R r^3\,dr\,d\theta = 2\pi\cdot\frac{R^4}{4} = \frac{\pi R^4}{2}$.

Fourth power: mass grows like $R^2$, mass sits at distances $\sim R$, and $I$ weights distance *squared* — $R^2\cdot R^2 = R^4$. The constraint's own nesting ($r^2\,dA$) is the fourth power.

> **Answer**: $\frac{\pi R^4}{2}$; mass $R^2$ × distance² $R^2$

### A8.

Compression: $dV < 0$ while $p > 0$, so every slice contributes $p\,dV < 0$ — negative work. The sign records who pays: positive = the gas pays energy out (expansion), negative = the outside pays energy in (compression). The energy budget balances either way.

> **Answer**: $dV<0$ with $p>0$ → negative; the sign names the payer

### A9.

$V = \iint_{x^2+y^2\le1}\sqrt{1-x^2-y^2}\,dA = \int_0^{2\pi}\int_0^1\sqrt{1-r^2}\,r\,dr\,d\theta$. With $u = 1-r^2$: $\int_0^1\sqrt{1-r^2}\,r\,dr = \frac12\cdot\frac23 = \frac13$, so $V = 2\pi\cdot\frac13 = \frac{2\pi}{3}$ — half of $\frac{4\pi}{3}$, the unit ball (9C's sphere, sliced into cylinders).

> **Answer**: $\frac{2\pi}{3}$ — the hemisphere's volume

### A10.

$x' = -3\cos^2 t\sin t$, $y' = 3\sin^2 t\cos t$, so $ds = 3|\sin t\cos t|dt$. One quarter: $3\int_0^{\pi/2}\sin t\cos t\,dt = \frac32$. Four quarters: length $= 6$.

Parametrizing is the fastest path because it *solves the constraint by geometry* — one parameter, one integral. The same step algebra performs for $y = \sqrt{\cdot}$, the parameter performs by construction.

> **Answer**: length 6; the parameter solves the constraint for you

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

---

## Answer Check

| Problem | Answer |
|:---:|:---|
| P1 | $16\pi$ (factor 4) |
| P2 | $500\ln3\approx549.3$ kJ |
| P3 | $400\ln2\approx277.3$ kPa · $554.5$ ✓ · below midpoint |
| P4 | $6\pi$ both ways |
| P5 | $p_2\approx94.5$ · $166.5$ kJ < isotherm $207.9$ |
| P6 | $5\pi$ · $\frac{38\pi}{3}\approx39.8$ kg |
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
