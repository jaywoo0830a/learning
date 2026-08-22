# Session 16C1B: Integral Techniques — Substitution & Parts As Relations, Read Backwards

**Phase 2 — Classical Techniques | Supplement to 16C1 | 40 min**

*16C1 taught you what integrals mean. This supplement teaches you how to *compute* them with the same mindset: the FTC is the relationship lens's undo button — if a quantity's degree of relation to $x$ is $f(x)$, then $\int f\,dx$ collects the relation back. The two techniques of 16A/16B are the two rules of 14D1B run in reverse: **substitution collects a chained relation** (chain rule backwards), **parts collects a product relation** (product rule backwards). Then we use them to *derive real formulas* — the rocket equation, capacitor energy, annuity value — reading every step as a sentence.*

**Prerequisites**: 16C1 (accumulation), 16A (FTC & u-sub), 16B (techniques), 14D1B (product/quotient relations)

> 💡 **Stuck?** Every problem has a collapsible **Hint** below it — click it only when you need a nudge.

---

## Example 1: Substitution — Renaming the Driver of a Relation

**Forward — the chain rule is a chained relation.** For $y = F(g(x))$:

$$\frac{dy}{dx} = F'(g(x))\,\cdot\,g'(x)$$

Read it: *$y$'s degree of relation to $x$ = ($y$'s degree to the inner driver $g$) × ($g$'s degree to $x$).* Two relations, multiplied — exactly 14D1B's chain.

**Backward — collecting a chained relation.** The FTC, applied to the chain rule:

$$\int F'(g(x))\,g'(x)\,dx = F(g(x)) + C$$

Given the product of two degrees, the integral reassembles the chain. Substitution is just this, organized:

**Step 1 — Rename the driver.** $u = g(x)$: "call the inner driver $u$."

**Step 2 — Read $u$'s degree of relation to $x$.** $\frac{du}{dx} = g'(x)$.

**Step 3 — The infinitesimal step.** $du = g'(x)\,dx$ — "a small step of $x$ buys $g'(x)$ units of $u$." Units: $[\text{u}] = \frac{\text{u}}{\text{x}}\cdot\text{x}$ ✓. This is the relationship lens at the infinitesimal level: $g'(x)$ is the **exchange rate between the two drivers**.

**Step 4 — Collect with respect to the new driver.** $\int f(g(x))\,g'(x)\,dx = \int f(u)\,du$ — the messy relation to $x$ becomes a clean relation to $u$.

**Worked, slowly — $\int_0^1 2x\,e^{x^2}\,dx$:**

1. **Spot the chain**: $e^{x^2}$ is $e^u$ with $u = x^2$ — and the leftover factor $2x$ is exactly $\frac{du}{dx}$. The relation of $u$ to $x$ is $2x$: local, growing with $x$.
2. **Write the exchange rate**: $du = 2x\,dx$ — "each small step of $x$ buys $2x$ units of $u$."
3. **Trade drivers**: $\int_0^1 e^{x^2}\cdot 2x\,dx = \int_{u(0)}^{u(1)} e^u\,du = \int_0^1 e^u\,du = e^1 - e^0 = e - 1$.
4. **Why it works**: we renamed the driver from $x$ to $u$, and the factor $2x\,dx$ is the exchange rate that makes the trade exact. The relation "$e^{x^2}$ to $x$" is tangled; the relation "$e^u$ to $u$" is clean. Substitution trades one driver for a cleaner one — nothing is lost, only relabeled.

**The unit check on substitution.** If $x$ is in meters and $u = x^2$ in m², then $\frac{du}{dx} = 2x$ has units m (m² per m) — the exchange rate is dimensional, and the $dx$ factor converts $x$-steps into $u$-steps. Substitution is a **local unit conversion of the driver**.

**Lens reading**: the chain rule says degrees of relation multiply along a chain; substitution is the same sentence read backwards — *given the multiplied degrees, recover the chain by renaming the driver.*

---

## Example 2: Integration by Parts — The Product Budget, Collected Backwards

**Forward — the product rule is a two-channel budget** (14D1B Ex1): $(uv)' = u'v + uv'$ — channel 1: $u$ changes with $v$ frozen; channel 2: $v$ changes with $u$ frozen.

**Backward — collect both channels.** Integrate the product rule:

$$uv = \int u'\,v\,dx + \int u\,v'\,dx \qquad\Longrightarrow\qquad \int u\,dv = uv - \int v\,du$$

Read the boxed formula as a sentence: *collecting one channel gives the total product, minus the other channel's collection.* "What the $u$-channel contributes = the whole product − what the $v$-channel contributes." The boundary term $uv$ is the product's accumulated two-channel budget at the endpoints.

**Worked, slowly — $\int_0^1 x\,e^x\,dx$:**

1. **Choose the roles.** $u = x$ (its degree of relation to $x$ is 1 — differentiating simplifies), $dv = e^x\,dx$ (collecting $e^x$ doesn't get worse): $du = dx$, $v = e^x$.
2. **Assemble**: $\int x\,e^x\,dx = x\,e^x - \int e^x\,dx = x e^x - e^x + C$.
3. **Press the undo button**: differentiate $x e^x - e^x$ by the product rule — you get $x e^x$ back ✓.
4. **Evaluate**: $[x e^x - e^x]_0^1 = (e - e) - (0 - 1) = 1$.

**The choice of $u$ is a relation-choice**: pick as $u$ the factor whose degree of relation to $x$ *simplifies* (polynomials, logarithms — degrees drop or tame), and as $dv$ the factor whose collection stays manageable (exponentials, trig). LIATE is the ranking of "which factor's relation improves most."

**Worked — $\int_1^e \ln x\,dx$:** $u = \ln x$ (degree $\frac1x$ — tamer), $dv = dx$ → $v = x$. Then $\int \ln x\,dx = x\ln x - \int x\cdot\frac1x\,dx = x\ln x - x + C$. Evaluate: $(e\cdot1 - e) - (1\cdot0 - 1) = 1$.

**Which tool when — a relation dictionary:**

| Integrand shape | Relation reading | Tool |
|:---|:---|:---|
| $f(g(x))\,g'(x)$ — a composition with its inner degree | a **chained** relation, degrees multiplied | substitution |
| $u\,v'$ — two unrelated factors | a **product** relation, two channels | parts |

**Lens reading**: substitution trades drivers; parts trades channels. Both are the relationship lens running backwards through 14D1B's two rules — and both end with the same undo-button check: differentiate your answer and read the relation forward again.

---

## Example 3: The Rocket Equation — Physics, Derived by Renaming the Driver (🔗 14D1B A1)

**The law.** In deep space with exhaust speed $u$ (relative to the rocket), 14D1B gave $m\,\frac{dv}{dt} = -u\,\frac{dm}{dt}$ — *velocity's relation to time, weighted by mass, equals the exhaust speed times mass's relation to time (backwards).*

**Step 1 — Separate the drivers.** Multiply by $dt$ and divide by $m$:

$$dv = -u\,\frac{dm}{m}$$

Each side now owns one driver: speed changes on the left, mass on the right.

**Step 2 — Collect each side.** The left side is trivial. The right side is $\int \frac{dm}{m}$: the reciprocal relation — "each unit of mass buys $\frac1m$ units of…" — and its collection is the logarithm (10A: $\ln m$'s degree of relation to $m$ is $\frac1m$). From mass $m_0$ down to $m$:

$$v = -u\int_{m_0}^{m}\frac{dm}{m} = -u\left[\ln m\right]_{m_0}^{m} = u\ln\frac{m_0}{m}$$

**Step 3 — Read the formula as a sentence.** The final speed is the exhaust speed $u$ (the strength of the thrust relation) times the logarithm of the mass ratio. The $\ln$ is the price of the $1/m$ relation: each kilogram of fuel matters *more* when the rocket is already light — that is why $\frac{m_0}{m}$, not $m_0-m$, appears.

**Numbers.** $m_0 = 1000$ kg, $u = 2500$ m/s, fuel burned down to $m = 600$ kg: $v = 2500\ln\frac{1000}{600} = 2500\ln\frac53 \approx 1277$ m/s.

**Lens reading**: the chain of relations (thrust ↔ mass flow ↔ velocity) was collected by renaming the driver to $m$ — and the collection turned a ratio of masses into a speed. The log is the accumulated reciprocal relation.

---

## Example 4: Capacitor Energy — Accumulating a Growing Voltage Relation

**The physics.** Charging a capacitor: each new parcel of charge $dq$ must be pushed against the voltage *already* on the plates. The voltage's degree of relation to the charge is uniform:

$$V(q) = \frac{q}{C} \qquad \text{"each coulomb already on the plates raises the voltage by } \tfrac1C \text{ volts."}$$

**The derivation.** Work = voltage × charge moved, collected over all the parcels:

$$E = \int_0^Q V\,dq = \int_0^Q \frac{q}{C}\,dq = \frac{Q^2}{2C}$$

**The reading.** This is the same triangle as the spring (16C1 Ex4): the relation starts at zero and grows linearly, so the total is *half* of final × final — $\frac12 QV$, i.e. $\frac12 CV^2$. The last coulomb costs the most, because it must climb the voltage all the previous coulombs built.

**Press the undo button**: $\frac{dE}{dQ} = \frac{Q}{C} = V$ ✓ — energy's degree of relation to charge is the voltage, read back off the answer.

**Numbers.** $C = 2$ F charged to $Q = 6$ C: $V = 3$ V, $E = \frac{36}{4} = 9$ J — and $\frac12 CV^2 = \frac12\cdot2\cdot9 = 9$ ✓.

**Lens reading**: the same "growing relation" pattern pays out $\frac12 \times$ (final degree) $\times$ (final driver) — spring, capacitor, inductor (RPA2). One grammar, three costumes.

---

## Example 5: An Annuity's Present Value — Economics, Derived by a Unit Swap

**The setup.** A stream of $R$ dollars/year arriving for $T$ years, discounted at rate $r$: each dollar arriving at time $t$ is worth $e^{-rt}$ of today's dollars. So

$$PV = \int_0^T R\,e^{-rt}\,dt$$

**The derivation — substitution as a unit swap.** The exponent $-rt$ must be dimensionless (16C1's lesson): $[r] = 1/\mathrm{yr}$. Rename the driver:

- $u = -rt$: "call the dimensionless discount driver $u$."
- **Exchange rate**: $\frac{du}{dt} = -r$ — uniform, and it carries the time unit.
- $du = -r\,dt$, so $dt = -\frac{du}{r}$: "each small step of time buys $-r$ units of $u$."

$$PV = R\int_{0}^{-rT} e^u\left(-\frac{du}{r}\right) = \frac{R}{r}\left(1 - e^{-rT}\right)$$

**Read the formula**: money = (flow ÷ discount rate) × (the fraction the discounting has collected). $\frac{R}{r}$ is what an *infinite* stream is worth today (16C1 A6's perpetuity); $e^{-rT}$ is the fraction still missing because the stream ends at $T$.

**Numbers.** $R = \$10{,}000$/yr, $r = 5\%$, $T = 20$ yr: $PV = \frac{10000}{0.05}(1-e^{-1}) \approx 200000 \times 0.632 = \$126{,}424$.

**Lens reading**: substitution swapped the driver from time (years) to a dimensionless discount coordinate — the exchange rate $-r$ is the relation between the two drivers, and it carried the units out of the exponent and into the money factor $\frac{R}{r}$.

> **Up to here**: substitution = chain rule backwards — rename the driver, $du=g'(x)dx$ is the exchange rate; parts = product rule backwards — $\int u\,dv = uv - \int v\,du$, the product minus the other channel; and both derive real laws: the rocket equation $v = u\ln\frac{m_0}{m}$ (collecting the $1/m$ relation), capacitor energy $\frac12 CV^2$ (the growing-relation triangle), annuity $PV = \frac{R}{r}(1-e^{-rT})$ (swapping time for a dimensionless driver).

---

## The Technique-As-Relation Checklist

> When an integral looks hard, run this. It is the whole supplement in one box.

```
1. SHAPE     → composition f(g)g' (chained relation) or product u·v' (two channels)?
2. DRIVER    → substitution: name u, write the exchange rate du = g'(x)dx, swap limits.
3. ROLES     → parts: pick u whose degree simplifies; collect dv; assemble uv − ∫v du.
4. UNITS     → the exchange rate is dimensional — it converts x-steps into u-steps.
5. UNDO      → differentiate the answer; the relation must read forward again.
```

---

#### Basic RP — Straight Setups (RPB1–RPB5)

> One relation, one collection. Set up the driver, read the exchange rate or the channel, collect, undo.

**RPB1.** Compute $\int_0^1 6x(x^2+1)^2\,dx$ by substitution, reading each step as a relation: name $u$, write the exchange rate, convert the limits, collect, and press the undo button.

<details>
<summary>💡 Hint</summary>

$u = x^2+1$, $\frac{du}{dx} = 2x$ — the leftover $6x = 3\cdot 2x$. Limits: $u(0)=1$, $u(1)=2$. $\int_1^2 3u^2\,du = [u^3]_1^2 = 7$.

</details>

**RPB2.** Compute $\int_0^{\pi/2}\sin t\cos t\,dt$ by substitution: which factor is the exchange rate, and what do the new limits become?

<details>
<summary>💡 Hint</summary>

$u = \sin t$, $du = \cos t\,dt$ — the cosine is the exchange rate. Limits: $\sin 0 = 0$, $\sin\frac\pi2 = 1$. $\int_0^1 u\,du = \frac12$.

</details>

**RPB3.** Compute $\int x\cos x\,dx$ by parts: name $u$, $dv$, $du$, $v$, assemble, and undo.

<details>
<summary>💡 Hint</summary>

$u = x$ (degree 1 — simpler), $dv = \cos x\,dx$ → $v = \sin x$. $x\sin x - \int\sin x\,dx = x\sin x + \cos x + C$.

</details>

**RPB4.** Compute $\int_0^1 t\,e^{-t}\,dt$ by parts: name the roles, assemble, evaluate, undo.

<details>
<summary>💡 Hint</summary>

$u = t$, $dv = e^{-t}dt$ → $v = -e^{-t}$. $[-te^{-t}]_0^1 + \int_0^1 e^{-t}dt = -e^{-1} - [e^{-t}]_0^1 = 1 - \frac2e \approx 0.264$.

</details>

**RPB5.** Compute $\int \frac{2x}{x^2+1}\,dx$ by substitution. The result is a logarithm — read why: what relation did the collection recover?

<details>
<summary>💡 Hint</summary>

$u = x^2+1$, $du = 2x\,dx$: $\int\frac{du}{u} = \ln|u| + C = \ln(x^2+1) + C$. The collection recovered the relation "$\ln u$ has degree $\frac1u$."

</details>

#### Advanced RP — Real Formulas, Derived End to End (RPA1–RPA5)

> Each problem derives a real physical or economic law. Every step is a sentence — no black boxes.

**RPA1.** Derive the capacitor's stored energy $E = \frac12 CV^2$ from scratch: (a) state the voltage-charge relation and its degree; (b) set up the work integral and evaluate; (c) press the undo button; (d) one sentence — why is the last coulomb the most expensive?

<details>
<summary>💡 Hint</summary>

$V(q) = \frac{q}{C}$, degree $\frac1C$ (uniform). $E = \int_0^Q \frac{q}{C}dq = \frac{Q^2}{2C} = \frac12 CV^2$. Undo: $\frac{dE}{dQ} = \frac{Q}{C} = V$.

</details>

**RPA2.** Derive the inductor's stored energy $E = \frac12 LI^2$: (a) write the voltage-current relation and the power relation; (b) use substitution ($u = i$) to collect energy over time; (c) compare with the spring and the capacitor — what is the shared grammar?

<details>
<summary>💡 Hint</summary>

$V = L\frac{di}{dt}$; $P = Vi$; $E = \int P\,dt = \int L\,i\,\frac{di}{dt}dt = \int_0^I L\,i\,di = \frac12 LI^2$. All three: growing relation → half of final × final.

</details>

**RPA3.** A drug decays at a rate proportional to the amount present: $\frac{dN}{dt} = -kN$. (a) Separate and integrate (the reciprocal relation's collection is the log). (b) Solve for $N(t)$. (c) Derive the half-life $t_{1/2} = \frac{\ln 2}{k}$ and compute it for $k = 0.1$/hr. (d) One sentence: what is $k$ in relation-lens language?

<details>
<summary>💡 Hint</summary>

$\int\frac{dN}{N} = -\int k\,dt$ → $\ln N = -kt + C$ → $N = N_0e^{-kt}$. Half-life: $e^{-kt_{1/2}} = \frac12$ → $t_{1/2} = \frac{\ln2}{0.1} \approx 6.93$ hr.

</details>

**RPA4.** A skydiver (mass $m$) falls with drag $-kv$: $m\frac{dv}{dt} = mg - kv$. (a) Separate, and use the substitution $u = mg - kv$ to integrate. (b) Solve for $v(t)$ with $v(0)=0$. (c) Read the terminal speed $\frac{mg}{k}$ as a balance of two relations. (d) Compute it for $m=70$ kg, $k=14$ kg/s, $g=9.8$.

<details>
<summary>💡 Hint</summary>

$\frac{dv}{mg-kv} = \frac{dt}{m}$; with $u = mg-kv$, $du = -k\,dv$: $-\frac1k\ln(mg-kv) = \frac{t}{m}+C$ → $v = \frac{mg}{k}(1-e^{-kt/m})$.

</details>

**RPA5.** Demand is $D(q) = 100 - q^2$ and supply is $S(q) = 10 + q$ (dollars, $q$ in thousands). (a) Find the equilibrium $(q^*, p^*)$. (b) Set up and evaluate the consumer surplus integral. (c) One sentence: what does each thin slice of the surplus integral measure, and which buyers does it come from?

<details>
<summary>💡 Hint</summary>

$100-q^2 = 10+q$ → $q^2+q-90=0$ → $q^*=9$, $p^*=19$. $CS = \int_0^9(100-q^2-19)dq = \int_0^9(81-q^2)dq = [81q-\frac{q^3}{3}]_0^9 = 729-243 = 486$.

</details>

> Solutions: [Solutions](solutions/16C1B-solutions.md#rp-drills)

---

## Common Mistakes

### Mistake 1: Forgetting the exchange rate carries units

**Wrong**: "$\int e^{-rt}dt = -r e^{-rt}$." **Right**: substitution swaps drivers, and the exchange rate must convert units too: $dt = -\frac{du}{r}$ — dropping the $\frac1r$ silently loses a time unit and turns the answer's units wrong. Check the units of the final answer against the original integral.

### Mistake 2: Choosing $u$ by accident instead of by relation

**Wrong**: parts with $u = e^x$, $dv = x\,dx$ — the leftover integral gets *worse* ($\frac{x^2}{2}e^x$). **Right**: choose the factor whose degree of relation to $x$ simplifies. The choice of roles is a relation-choice; a bad choice hands the difficulty to the other channel.

---

## What We Just Did

```
(1) Substitution = chain rule backwards: u = g(x), du = g'(x)dx is the exchange
    rate between drivers. Collect the chained relation in the new driver.
(2) Parts = product rule backwards: ∫u dv = uv − ∫v du — one channel's collection
    = the whole product minus the other channel's. Choose u = the simplifying degree.
(3) Real laws: rocket v = u ln(m₀/m) — collecting the 1/m relation;
    capacitor/inductor E = ½CV², ½LI² — the growing-relation triangle;
    annuity PV = (R/r)(1−e^(−rT)) — swapping time for a dimensionless driver.
```

---

## Today's Procedure

| When you see... | Do this... |
|:---|:---|
| A composition $f(g(x))\,g'(x)$ | Substitution: $u=g(x)$, $du=g'(x)dx$ — rename the driver and collect in $u$ |
| A product of unrelated factors | Parts: $\int u\,dv = uv - \int v\,du$ — take the product, give back the other channel |
| A growth/decay law $\frac{dy}{dt}=ky$ | Separate and collect the reciprocal relation: $\int\frac{dy}{y} = \ln y$ |
| A "total work/energy" question | Write the growing relation, integrate the triangle, expect $\frac12 \times$ final $\times$ final |
| Money discounted over time | Swap to the dimensionless driver $u=-rt$; the $-\frac1r$ carries the units |

---

## How to Read These Symbols

| Symbol | Reads as | Meaning |
|:---:|:---:|------|
| $du = g'(x)\,dx$ | "d u equals g prime d x" | the exchange rate between drivers — a small step of x buys g'(x) units of u |
| $\int u\,dv$ | "integral u d v" | one channel of the product budget, to be collected |
| $\ln\frac{m_0}{m}$ | "log of the mass ratio" | the accumulated reciprocal relation — the rocket equation's price tag |
| $\frac12 CV^2$, $\frac12 LI^2$ | "half C V squared" | the growing-relation triangle: half of final × final |

---
