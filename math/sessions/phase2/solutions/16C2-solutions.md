# Solutions — 16C2: Advanced Integral Interpretation

> Back to [16C2 — Advanced Integral Interpretation](../16C2-advanced-integral-interpretation.md)

---

## Practice 1

**(a)** $M = \int_0^{10}(2x+1)dx = [x^2+x]_0^{10} = 110$ g.

**(b)** Right half: $\int_5^{10}(2x+1)dx = [x^2+x]_5^{10} = 110 - 30 = 80$ g.

**(c)** The right half holds $\frac{80}{110} \approx 73\%$ of the mass because density doubles across the wire: the measure (length) is equal, but the field (density) is not. Mass = field × measure, and the field is bigger on the right.

> **Answer**: (a) 110 g (b) 80 g (c) density is higher on the right

**Lens reading**: mass is density's relation to length, collected along the wire — 110 g.

---

## Practice 2

On the circle of radius 2: $r = (2\cos t, 2\sin t)$, $dr = (-2\sin t, 2\cos t)dt$, $F = (-2\sin t, 2\cos t)$.

$F\cdot dr = (4\sin^2 t + 4\cos^2 t)dt = 4\,dt$ — the field does 4 J per meter walked.

Circulation $= \int_0^{2\pi}4\,dt = 8\pi$.

Reading: one factor $R=2$ comes from the field's strength at radius 2, the other from the path's length $2\pi R$ — together $R^2 \cdot 2\pi = 8\pi$.

> **Answer**: $8\pi$ — field strength ($\propto R$) × path length ($\propto R$)

**Lens reading**: circulation is the field's along-path relation, collected around the loop — $8\pi$.

---

## Practice 3

**(a)** Straight path $r(t) = (t,t)$, $t\in[0,2]$: $F = (t,t)$, $dr = (1,1)dt$, so $F\cdot dr = 2t\,dt$. $W = \int_0^2 2t\,dt = 4$.

**(b)** $\phi = \frac12(x^2+y^2)$: $\nabla\phi = (x,y) = F$ ✓. $\phi(2,2)-\phi(0,0) = 4-0 = 4$ ✓.

**(c)** Gradient field → circulation around any closed loop is $\phi(\text{start})-\phi(\text{start}) = 0$.

> **Answer**: (a) 4 (b) 4 ✓ (c) 0 — path-independent

**Lens reading**: the gradient field's work is the potential relation's difference — path-independent.

---

## Practice 4

Flux through circle radius 3: on the circle $F = n \cdot 3$, so $F\cdot n = 3$ everywhere; arc length $= 2\pi\cdot 3$. Flux $= 3 \cdot 6\pi = 18\pi$.

Gauss check: $\operatorname{div}F = 1+1 = 2$; area $= \pi\cdot 9 = 9\pi$; product $= 18\pi$ ✓.

> **Answer**: $18\pi$; div × area $= 2\cdot 9\pi = 18\pi$ ✓

**Lens reading**: flux is the across-boundary relation; Gauss balances it against the sources inside.

---

## Practice 5: Real Battle — Gauss's Law

Radius $R$: flux $= \frac{kQ}{R^2}\cdot 4\pi R^2 = 4\pi kQ$.

Radius $2R$: flux $= \frac{kQ}{4R^2}\cdot 16\pi R^2 = 4\pi kQ$.

Equal, because the inverse-square decay and the surface-area growth are exact inverses: strength drops $4\times$, area grows $4\times$. Any closed surface around the charge catches the same total flow — the charge is the single source.

> **Answer**: $4\pi kQ$ through both spheres — inverse-square × surface-area = constant

**Lens reading**: the inverse-square relation cancels the area relation — the charge counts, not the distance.

---

## Practice 6: Real Battle — The Winding Integral

$\oint z\,dz = \int_0^{2\pi} e^{it}\cdot ie^{it}dt = i\int_0^{2\pi}e^{2it}dt = 0$ — the point rotates twice around; its average is zero.

$\oint \frac{dz}{z} = \int_0^{2\pi} e^{-it}\cdot ie^{it}dt = i\int_0^{2\pi}1\,dt = 2\pi i$ — the rotation cancels and the total angle survives.

Reading: $z$ winds and averages out; $1/z$ measures the winding itself. The pole at 0 is invisible to $z\,dz$ but is exactly what $dz/z$ counts.

> **Answer**: $\oint z\,dz = 0$; $\oint dz/z = 2\pi i$

**Lens reading**: the winding integral collects the path's angular relation — $2\pi i$; only $z^{-1}$ survives.

---

## Basic Drills

### D1.

> **Answer**: kg; kg; J (N·m); field-units × m (e.g. N, or m²/s for velocity fields)

**Lens reading**: the units name which relation each measure collects.

### D2.

$M = 3 \cdot 20 = 60$ g.

> **Answer**: 60 g

**Lens reading**: the density relation, collected along the wire.

### D3.

On the axis: $F=(x,0)$, $dr=(dx,0)$: $W = \int_0^2 x\,dx = 2$.

> **Answer**: 2 J

**Lens reading**: the field's along-path relation, collected.

### D4.

$F\cdot dr = dt$: circulation $= 2\pi$.

> **Answer**: $2\pi$

**Lens reading**: one lap of the vortex relation.

### D5.

$F = n$ on the circle: flux $= 2\pi$.

> **Answer**: $2\pi$

**Lens reading**: the source relation's flux through the circle.

### D6.

$\operatorname{div}(2x,3y) = 5$ (a strong source). $\operatorname{div}(-y,x) = 0$ (pure spin).

> **Answer**: 5; 0

**Lens reading**: div 5, curl 0 — spreading without spinning: one relation, two readings.

### D7.

$\frac{kQ}{R^2}\cdot 4\pi R^2 = 4\pi kQ$.

> **Answer**: $4\pi kQ$ — independent of $R$

**Lens reading**: the two relations cancel — the charge counts, the radius doesn't.

### D8.

$\int_0^{2\pi}e^{it}dt = \left[\frac{e^{it}}{i}\right]_0^{2\pi} = 0$ — the average position of a full circle is its center.

> **Answer**: 0 — a full circle balances

**Lens reading**: the circle's position relation balances to its center.

### D9.

$M = \int_0^2\int_0^2 1\,dx\,dy = 4$. By symmetry $\bar x = \bar y = 1$.

> **Answer**: $M=4$, centroid $(1,1)$

**Lens reading**: the measure's balance point — the collected average.

### D10.

$\oint z^2 dz = i\int_0^{2\pi}e^{3it}dt = 0$.

> **Answer**: 0 — only $z^{-1}$ survives a loop integral

**Lens reading**: only the $-1$ power sees the hole — every other relation winds to zero.

---

## Advanced Drills

### A1.

On the circle of radius $R$: $F = (-y,x) = R(-\sin t, \cos t)$, $dr = R(-\sin t, \cos t)dt$ → $F\cdot dr = R^2 dt$ → circulation $2\pi R^2$.

For $F = (x,y)$: $F = R(\cos t,\sin t)$ is perpendicular to $dr$ → circulation 0.

The loop test: if $F = \nabla\phi$, then $\oint F\cdot dr = \phi(\text{end})-\phi(\text{start}) = 0$ on every loop. The vortex's $2\pi R^2 \neq 0$ proves no potential exists — going around a loop the field "keeps score" and never returns to zero.

> **Answer**: $2\pi R^2$ vs 0; nonzero circulation ⟹ not a gradient

**Lens reading**: nonzero circulation means no potential — the relation loops without returning.

### A2.

Unit square boundary, counterclockwise, $F = (-y,x)$:
- Bottom ($y=0$): $F=(0,x)$, $dr=(dx,0)$ → 0.
- Right ($x=1$): $F=(-y,1)$, $dr=(0,dy)$ → $\int_0^1 1\,dy = 1$.
- Top ($y=1$, right→left): $F=(-1,x)$, $dr=(-dx,0)$ → $\int_1^0(-1)(-dx) = 1$.
- Left ($x=0$, down): $F=(-y,0)$, $dr=(0,-dy)$ → 0.

Total circulation $= 2$.

Green: $\iint\left(\frac{\partial F_2}{\partial x}-\frac{\partial F_1}{\partial y}\right)dA = \iint(1-(-1))dA = 2\cdot(\text{area }1) = 2$ ✓.

> **Answer**: circulation 2 = ∬2 dA = 2·area ✓

**Lens reading**: Green's theorem — the boundary relation's collection equals the sources inside.

### A3.

Unit square, $F=(x,y)$:
- Right face: $F=(1,y)$, $n=(1,0)$ → $F\cdot n = 1$, contributes 1.
- Top face: $F=(x,1)$, $n=(0,1)$ → contributes 1.
- Left ($x=0$) and bottom ($y=0$): contributions 0.

Flux $= 2$. Gauss: div $= 2$, area $= 1$ → $2 = 2\cdot1$ ✓.

> **Answer**: flux 2 = div × area ✓

**Lens reading**: Gauss at field level — outflow equals collected sources.

### A4.

Away from the origin, flux through any two nested spheres is the same ($4\pi kQ$), so no flux is created in the shell between them — div $E = 0$ there. The field neither emits nor absorbs outside the charge.

All the outflow originates at the origin, the one point where the field is undefined — the charge is a **point source**. Gauss's law reads: flux through any closed surface $= 4\pi kQ_{\text{inside}}$ — the integral detects the charge no matter the surface's size or shape.

> **Answer**: div = 0 away from origin; all flux comes from the charge — a point source

**Lens reading**: all flux originates at the charge — the only point whose relation sources.

### A5.

$\phi = x^2y$, $F = \nabla\phi = (2xy, x^2)$.

Straight path $r(t) = (t, 2t)$: $F = (4t^2, t^2)$, $dr = (1,2)dt$ → $F\cdot dr = 6t^2 dt$ → $W = \int_0^1 6t^2 dt = 2$.

L-path: horizontal leg ($y=0$): $F = (0,x^2)$, $dr=(dx,0)$ → 0. Vertical leg ($x=1$): $F = (2y,1)$, $dr=(0,dy)$ → $\int_0^2 1\,dy = 2$. Total 2.

Both equal $\phi(1,2) - \phi(0,0) = 2 - 0 = 2$ ✓ — the path never matters for a gradient field.

> **Answer**: 2 by both paths = $\phi(1,2)-\phi(0,0)$ ✓

**Lens reading**: the potential difference is the collected relation — 2 by both paths.

### A6.

$I = \int_{-L/2}^{L/2}x^2\,dx = \left[\frac{x^3}{3}\right]_{-L/2}^{L/2} = \frac{2L^3}{24} = \frac{L^3}{12}$.

Cubic growth: total mass grows like $L$, and the mass sits at distances that also grow like $L$; the $r^2$ in the integrand turns that into one more factor of $L$ — three powers total. A rod twice as long is eight times harder to spin.

> **Answer**: $I = L^3/12$ — mass × distance², both grow with $L$

**Lens reading**: moment of inertia collects $r^2$ against the measure — $L^3/12$.

### A7.

For integer $n \neq 0$: $\int_0^{2\pi}e^{int}dt = \frac{1}{in}e^{int}\big|_0^{2\pi} = 0$ (the circle closes — start equals end). For $n=0$: $\int_0^{2\pi}1\,dt = 2\pi$.

Different rotation speeds are **orthogonal**: the average of the product of two different speeds is zero. This lets rotations act as independent measuring units for periodic signals — the foundation of Fourier analysis (25E).

> **Answer**: 0 for $n\neq0$, $2\pi$ for $n=0$ — rotations are orthogonal

**Lens reading**: rotations are orthogonal — the average relation cancels except at $n=0$.

### A8.

$\oint z\,dz = i\int_0^{2\pi}e^{2it}dt = 0$.

$\oint \bar z\,dz = \int_0^{2\pi}e^{-it}\cdot ie^{it}dt = i\int_0^{2\pi}1\,dt = 2\pi i$.

$z$ winds once forward and the path element averages it out; $\bar z$ winds once **backward**, and the quarter-turn element $dz$ cannot cancel a reverse rotation — the leftover $2\pi i$ detects the reflection. Note the contrast: $\bar z$ is not complex-differentiable (14D2 A5), and its loop integral is nonzero — the same failure seen from inside the integral.

> **Answer**: $\oint z\,dz = 0$; $\oint\bar z\,dz = 2\pi i$ — the integral detects the reversed rotation

**Lens reading**: $\bar z$ reverses the relation — the integral detects the reversed rotation.

### A9.

$\bar x = 0$ by left-right symmetry.

$\bar y = \frac{\iint y\,dA}{\iint dA} = \frac{\int_0^{\pi}\int_0^1 r\sin\theta\cdot r\,dr\,d\theta}{\pi/2} = \frac{[\frac{r^3}{3}]_0^1\cdot[-\cos\theta]_0^{\pi}}{\pi/2} = \frac{\frac23\cdot 2}{\pi/2} = \frac{4}{3\pi} \approx 0.42$.

The centroid sits at 42% of the radius, not halfway: the measure thins toward the top (horizontal slices shrink), so the mass piles up lower. The centroid is where the *measure* balances, not the shape's midpoint.

> **Answer**: $\bar x = 0$, $\bar y = \frac{4}{3\pi}\approx0.42$ — measure thins toward the top

**Lens reading**: the measure thins toward the top — the balance point sits at $\frac{4}{3\pi}$.

### A10.

$M = \int_0^L kx\,dx = \frac{kL^2}{2}$. $\bar x = \frac{\int_0^L x\cdot kx\,dx}{\int_0^L kx\,dx} = \frac{kL^3/3}{kL^2/2} = \frac{2L}{3}$.

Compare 16C1's triangular density $p(x) = \frac{2x}{L^2}$: its expectation is $\frac23 L$ — the same $\frac23$! The math is identical because both are "the average of $x$ against the ramp weighting." Only the units and meanings differ: kg·m vs probability. That is the measure concept in one sentence — *the weighting scheme is the mathematics; the units are the interpretation.*

> **Answer**: $M = kL^2/2$, $\bar x = 2L/3$ — same math as the triangular density, different units

**Lens reading**: the rod's centroid — the same collected average, different units.

---

## Deep Insight

### DI1.

**(a)** Right side $x=1$, outward normal $n=(1,0)$: $E\cdot n = kQ\cdot\frac{1}{1+y^2}$, so the contribution is $\int_{-1}^{1}\frac{kQ}{1+y^2}dy = kQ\cdot 2\arctan(1) = kQ\cdot\frac{\pi}{2}$. By symmetry the four sides total $4\cdot kQ\frac{\pi}{2} = 2\pi kQ$.

**(b)** Circle radius 1: $|E| = kQ$ on the circle, normal outward: flux $= kQ\cdot 2\pi = 2\pi kQ$ ✓ — identical.

**(c)** Away from the origin, $\operatorname{div} E = 0$ (the inverse-square field neither creates nor destroys flow between nested curves — Example 6). By Gauss, flux through any closed curve $=$ the total source inside $= 2\pi kQ$, no matter the shape. **Flux does not measure the boundary — it counts the sources enclosed.** The square and the circle agree because they enclose the same charge; a curve that misses the charge gives 0. That is the whole power of the divergence theorem: a hard boundary integral is secretly a trivial source count. Shape-independence is not a coincidence to check — it is the theorem's meaning.

> **Answer**: $2\pi kQ$ through both; any closed curve enclosing the charge gives $2\pi kQ$ — flux counts sources

**Lens reading**: flux counts sources, not boundaries — any closed curve around the charge gives $2\pi kQ$.

---

## Answer Check

| Problem | Answer |
|:---:|:---|
| P1 | 110 g · 80 g · density × measure |
| P2 | $8\pi$ |
| P3 | 4 · 4 ✓ · 0 |
| P4 | $18\pi$ = div×area ✓ |
| P5 | $4\pi kQ$ both spheres |
| P6 | 0 vs $2\pi i$ |
| D1 | kg · kg · J · field×m |
| D2 | 60 g |
| D3 | 2 J |
| D4 | $2\pi$ |
| D5 | $2\pi$ |
| D6 | 5 · 0 |
| D7 | $4\pi kQ$ |
| D8 | 0 |
| D9 | 4, (1,1) |
| D10 | 0 |
| A1 | $2\pi R^2$ vs 0; loop test |
| A2 | 2 = ∬2 ✓ |
| A3 | 2 = 2·1 ✓ |
| A4 | div=0 away; charge is the source |
| A5 | 2 both paths |
| A6 | $L^3/12$ |
| A7 | 0 ($n\neq0$), $2\pi$ ($n=0$) |
| A8 | 0 vs $2\pi i$ |
| A9 | $(0, \frac{4}{3\pi})$ |
| A10 | $kL^2/2$; $2L/3$ |
| DI1 | $2\pi kQ$ both — flux counts sources |
