# Session 14D: Derivative Interpretation I — The Relation Lens

**Phase 2 — Classical Techniques | 100 min**

*The calculus in this session is trivial — that is the point. The exercise is reading: a derivative is first a fraction $\frac{dy}{dx}$ carrying y-units per x-unit, and "y is related to x" is a sentence missing its number $\frac{dy}{dx}$. You will learn the unit lens (write the units — they name the meaning), the relationship lens (how much is y related to x, with units y/x), the sign lens (the sign of $f'$ is an arrow, never a position), the variable jail (a letter means only what its lock says), and the motion signs of $v$ and $a$ together. Science, engineering, and economics all speak this language; by the end you will hear it fluently.*

**Prerequisites**: 14A (basic derivatives), 14B (product/chain rules), 14C (higher derivatives)

*Prerequisite for: [14D1 — Derivative Interpretation](14D1-derivative-interpretation.md), [14D1A — Implicit Relations](14D1A-derivative-interpretation.md), [14D1B — Product & Quotient Rules](14D1B-product-quotient-interpretation.md), [14D2 — Advanced Derivative Interpretation](14D2-advanced-derivative-interpretation.md)*

> 💡 **Stuck?** Every problem has a collapsible **Hint** below it — click it only when you need a nudge.

---

## Example 1: The Units of a Derivative — Name the Meaning First

A derivative is a fraction: $dy/dx$ carries **y-units per x-unit**. Writing the units forces the meaning out.

| Quantity (y) | Units | Derivative | Units | One-sentence meaning |
|:---:|:---:|:---:|:---:|:---|
| position $s(t)$ | m | $s'(t)$ | m/s | "each second adds about $s'$ meters" |
| cost $C(q)$ | \$ | $C'(q)$ | \$/unit | "each extra unit costs about $C'$ dollars" |
| population $P(t)$ | people | $P'(t)$ | people/yr | "each year adds about $P'$ people" |
| temperature $T(h)$ vs altitude | °C | $dT/dh$ | °C/km | "each km higher is $dT/dh$ degrees colder" |
| balloon volume $V(t)$ | m³ | $dV/dt$ | m³/s | "each second pumps in $dV/dt$ cubic meters" |

**The unit check**: units that look wrong mean the formula is wrong. If a "speed" comes out in m·s instead of m/s, the computation failed before the answer was read.

**Worked**: $s(t) = \frac12 t^2$ meters. $s'(t) = t$, so at $t=2$: $s'(2) = 2$ m/s. Read it as a sentence: "at $t=2$, each extra second adds about 2 meters of position." The number 2 alone means nothing — 2 m/s is the whole story.

![Units of the derivative: m/s for position, $/unit for cost](graphs/0821/14D1/14d1-derivative-units.png)

*Graph 14D-1: Left — position vs time, tangent slope 4 m/s. Right — cost vs quantity, tangent slope 28 \$/unit. The same geometric object (a tangent) says completely different sentences depending on its units.*

---

### The Relationship Lens — "How Much Is y Related to x?" Has a Unit

Everyday language says "temperature is related to altitude," "demand is related to price," "income is related to education." The word *related* hides a question — **how much?** — and calculus answers it with one symbol. If $y$ is a function of $x$, then

$$\frac{dy}{dx}\ \text{ has units }\ \left[\frac{y}{x}\right]$$

The derivative **is** the degree of relatedness, and its units name the relation:

| "x and y are related…" | Function | Degree of relation | Units | The sentence, with its number |
|:---|:---:|:---:|:---:|:---|
| temperature ↔ altitude | $T(h)$ | $\frac{dT}{dh} = -6.5$ | °C/km | "each km of altitude buys 6.5 °C of cold" |
| demand ↔ price | $q(p)$ | $\frac{dq}{dp} = -10$ | units/\$ | "each dollar of price costs 10 units of demand" |
| distance ↔ fuel | $d(f)$ | $\frac{dd}{df}$ | km/L | "each liter of fuel buys so many km" |
| mass ↔ volume | $m(V)$ | $\frac{dm}{dV}$ | kg/m³ | "each cubic meter weighs so many kg" (density!) |

**The relation is the function; the degree is the derivative.** "$y$ is related to $x$" is the *global* statement that a function $y(x)$ exists. $\frac{dy}{dx}$ is the *local* statement — how strong the relation is *right here*, at this value of $x$.

**Sign and size are the direction and strength of the relation.** Positive derivative: the two quantities move together; negative: in opposite directions. Large $|\frac{dy}{dx}|$: strongly related at this point; small: weakly. Because it is local, one pair can be strongly related here and weakly there — a single "correlation number" cannot say that; a derivative can.

**Zero derivative is not "no relation."** $y = x^3$ is related to $x$ everywhere, yet at $x=0$ the local degree is exactly 0 — momentarily flat (the same lesson as 14D1's A9). "Related" is a global fact; $\frac{dy}{dx}$ measures its strength at a point.

**The relation is symmetric; the rate is not.** "x and y are related" points both ways, but $\frac{dy}{dx}$ (units y/x) and $\frac{dx}{dy}$ (units x/y) are different questions — and locally they are **reciprocals**. Choosing the numerator is choosing *whose response per unit of whose driver* — the "with respect to WHAT" question, applied to relationships. Mileage (km/L) and fuel consumption (L/km) are the same relation, read in two directions.

**Comparing relations across domains needs the percentage form.** Raw $\frac{dy}{dx}$ carries units, so the "income–education relation" and the "temperature–altitude relation" cannot be compared number-to-number. Strip the units and the relation becomes **elasticity** (14D1 Example 6): $E = \frac{x}{y}\frac{dy}{dx}$ is dimensionless — it reads "1% of x buys $E$% of y". The unit lens says *how much*; elasticity says *how strongly, scale-free*.

**The mindset, in one sentence**: *"y is related to x" is a sentence missing its number — $\frac{dy}{dx}$ in units of y per x is that number. Write the units, and the vagueness disappears.*

### Relationship Practice: Building the Relation from Words

> The lens in action: verbal statement → function $y(x)$ → derivative $\frac{dy}{dx}$ → units → one-sentence reading. **Setting up the function is the whole skill** — everything after that is routine.

**RP1.** A taxi charges a \$4 flat fee plus \$2 per km.

- **A.** Set up the fare function $F(d)$ and compute $\frac{dF}{dd}$ with units.
- **B.** Read the relation in one sentence.
- **C.** $\frac{dF}{dd}$ is constant — what does a constant degree of relation say about this fare?

<details>
<summary>Hint</summary>

$F(d) = 4 + 2d$. Constant slope = the relation is uniform: every km buys the same \$2, everywhere.

</details>

**RP2.** A square metal plate has side $s$ cm and area $A$.

- **A.** Set up $A(s)$ and compute $\frac{dA}{ds}$ at $s=5$ with units.
- **B.** Read the relation in one sentence.
- **C.** Compute $\frac{dA}{ds}$ at $s=20$ — why does the same relation get *stronger* as the plate grows?

<details>
<summary>Hint</summary>

$A = s^2$, so $\frac{dA}{ds} = 2s$. The degree of relation is local: a bigger plate has more boundary to grow from.

</details>

**RP3.** A car consumes 8 L of fuel per 100 km.

- **A.** Set up fuel $f$ as a function of distance $d$ and compute $\frac{df}{dd}$ with units.
- **B.** Set up the *reverse* relation — distance as a function of fuel — and compute $\frac{dd}{df}$.
- **C.** Verify the two degrees are reciprocals and read the relation in both directions.

<details>
<summary>Hint</summary>

$f = 0.08d$ (L/km); $d = 12.5f$ (km/L). Reciprocals: $0.08 \times 12.5 = 1$.

</details>

**RP4.** A sealed gas container obeys $P = 0.4T$ (kPa vs kelvin), and its heater raises temperature as $T = 300 + 2t$ (K vs seconds).

- **A.** Set up each relation and write each derivative with units — there are two degrees of relation here.
- **B.** Use the chain rule to get $\frac{dP}{dt}$ and show the units multiply: $\frac{\mathrm{kPa}}{\mathrm{K}}\cdot\frac{\mathrm{K}}{\mathrm{s}} = \frac{\mathrm{kPa}}{\mathrm{s}}$.
- **C.** One sentence: how strongly is pressure related to time?

<details>
<summary>Hint</summary>

$\frac{dP}{dT} = 0.4$ kPa/K and $\frac{dT}{dt} = 2$ K/s. Composed relation: $\frac{dP}{dt} = 0.4 \times 2 = 0.8$ kPa/s — degrees of relation multiply when relations chain.

</details>

---

#### Basic RP — Straight Setups (RPB1–RPB5)

> One relation, one shape. Set up the function, differentiate, read the sentence.

**RPB1.** A tank starts with 50 L of water and a pump adds 12 L/min.

- **A.** Set up the volume function $V(t)$.
- **B.** Compute $\frac{dV}{dt}$ with units and read the relation in one sentence.
- **C.** Why is the degree of relation constant here?

<details>
<summary>Hint</summary>

$V(t) = 50 + 12t$. A constant rate means the relation is uniform — every minute buys the same 12 L.

</details>

**RPB2.** An equilateral triangle has side $s$ cm and area $A$.

- **A.** Set up $A(s) = \frac{\sqrt3}{4}s^2$.
- **B.** Compute $\frac{dA}{ds}$ at $s=4$ with units and read the sentence.
- **C.** Compute it at $s=10$ — why is the relation stronger there?

<details>
<summary>Hint</summary>

$\frac{dA}{ds} = \frac{\sqrt3}{2}s$. The degree grows with $s$ — the relation is local.

</details>

**RPB3.** A trip is 120 km long, driven at a constant speed $v$ km/h.

- **A.** Set up the time function $t(v)$.
- **B.** Compute $\frac{dt}{dv}$ at $v=60$ with units and read the sentence (convert to minutes).
- **C.** What does the minus sign say about the direction of the relation, and why is the degree smaller at $v=90$?

<details>
<summary>Hint</summary>

$t(v) = \frac{120}{v}$, so $\frac{dt}{dv} = -\frac{120}{v^2}$. At $v=60$: $-\frac{1}{30}$ h per km/h = 2 minutes shaved per extra km/h.

</details>

**RPB4.** Apples sell for \$3 per kg.

- **A.** Set up cost $C(w)$ and compute $\frac{dC}{dw}$ with units.
- **B.** Set up the reverse relation $w(C)$ and compute $\frac{dw}{dC}$.
- **C.** Verify the two degrees are reciprocals and read both sentences.

<details>
<summary>Hint</summary>

$C = 3w$ and $w = \frac13 C$. $3 \times \frac13 = 1$.

</details>

**RPB5.** A rock dropped from rest falls $d(t) = 4.9t^2$ meters in $t$ seconds.

- **A.** Compute $\frac{dd}{dt}$ at $t=2$ with units — this degree of relation has a name: what is it?
- **B.** Compute it at $t=5$.
- **C.** One sentence: how does the relation between distance and time change as the rock falls?

<details>
<summary>Hint</summary>

$\frac{dd}{dt} = 9.8t$ — velocity. At $t=2$: 19.6 m/s; at $t=5$: 49 m/s. The relation strengthens as it falls.

</details>

#### Advanced RP — Chained & Inverted Setups (RPA1–RPA5)

> Now the relation is a chain, an inverse, or a search for where the degree vanishes. Setting up the function is the whole battle.

**RPA1.** A box with a square base of side $x$ cm and fixed height 10 cm is built from material costing \$0.02 per cm².

- **A.** Set up the surface area $S(x)$.
- **B.** Compute $\frac{dS}{dx}$ at $x=5$.
- **C.** Set up the cost $C(x)$ and compute $\frac{dC}{dx}$ at $x=5$ — show the units chain: $(\frac{\$}{\mathrm{cm^2}})(\frac{\mathrm{cm^2}}{\mathrm{cm}}) = \frac{\$}{\mathrm{cm}}$.
- **D.** One sentence for the final degree.

<details>
<summary>Hint</summary>

$S(x) = 2x^2 + 40x$, $\frac{dS}{dx} = 4x + 40 = 60$ at $x=5$. $C = 0.02S$, so $\frac{dC}{dx} = 0.02(4x+40) = 1.2$ at $x=5$.

</details>

**RPA2.** Demand is $q(p) = 200 - 5p$ and revenue is $R = p\cdot q$.

- **A.** Set up $R(p)$ and compute $\frac{dR}{dp}$ at $p=10$ with units.
- **B.** Read the sentence.
- **C.** Find the price where the degree of relation is exactly zero, and say what that means (see 14D1 A9).

<details>
<summary>Hint</summary>

$R = 200p - 5p^2$, $\frac{dR}{dp} = 200 - 10p$. Zero at $p=20$ — revenue stops responding to price: the peak.

</details>

**RPA3.** A heater's power is $P = \frac{V^2}{R}$ with fixed voltage $V = 120$ V.

- **A.** Set up $P(R)$ and compute $\frac{dP}{dR}$ at $R = 60\,\Omega$ with units.
- **B.** Read the sentence — why is the degree negative?
- **C.** Compute the elasticity $E = \frac{R}{P}\frac{dP}{dR}$ and read the *dimensionless* degree of relation (compare with 14D1 Example 6).

<details>
<summary>Hint</summary>

$\frac{dP}{dR} = -\frac{V^2}{R^2} = -\frac{14400}{3600} = -4$ W/Ω. $P = 240$ W, so $E = \frac{60}{240}(-4) = -1$ — exactly unit elastic, because $P \propto R^{-1}$.

</details>

**RPA4.** A farmer fences a rectangular pen against a river (the river side needs no fence) using 200 m of fence.

- **A.** With width $x$ as the side perpendicular to the river, set up the area $A(x)$.
- **B.** Compute $\frac{dA}{dx}$ at $x=20$ with units and read the sentence.
- **C.** Find where the degree of relation is zero and say what the pen looks like there (see 14D1 A9).

<details>
<summary>Hint</summary>

$A(x) = x(200 - 2x) = 200x - 2x^2$, so $\frac{dA}{dx} = 200 - 4x$: $120$ m²/m at $x=20$; zero at $x=50$, where $A = 5000$ m² — the maximum.

</details>

**RPA5.** A faucet drips 2 drops per second, each drop 0.05 mL.

- **A.** Set up the wasted volume $V(t)$ in mL and compute $\frac{dV}{dt}$ with units.
- **B.** Chain the unit conversions — seconds → hours → days → years, mL → L — to find the yearly waste in liters.
- **C.** One sentence: what does this say about relations that chain?

<details>
<summary>Hint</summary>

$\frac{dV}{dt} = 2 \times 0.05 = 0.1$ mL/s. $0.1 \times 3600 \times 24 \times 365 = 3{,}153{,}600$ mL ≈ 3,154 L/yr — degrees of relation multiply through every unit conversion.

</details>

→ Solutions: [Solutions](solutions/14D-solutions.md#relationship-practice)

---

### The Sign Lens — Where the Number Sits vs Where It Goes

Every lens so far read the *derivative's* sign as direction. Now turn the question around and hunt the misconception that undoes them all: **the sign of $f'$ says nothing about the sign of $f$.** They live on different axes — $f$ marks where the number sits on the number line; $f'$ marks where it is going next. Reading one from the other is the most common misread in this session's territory. Two models make the split vivid before any trap is sprung: air temperature $T(h) = 20 - 6.5h$ sits at a warm $+13.5$ °C at $h = 1$ km while the arrow reads $T' = -6.5$ °C/km — a positive number with a negative arrow; and gravitational potential $U(r) = -\frac{GM}{r}$ sits negative everywhere while $U' = +\frac{GM}{r^2} > 0$ climbs toward zero — a negative number with a positive arrow.

**The four false inferences, and what actually follows.**

| False inference | The counterexample | The correction |
|:---|:---|:---|
| $f'>0$ ⟹ $f>0$ — "rising, so it must be above zero" | balance $B(t) = -800 + 50t$ at $t=10$: $B = -300$ (in debt), yet $B' = 50 > 0$ | **rising from below**: the arrow points up while the number sits negative — a debt being climbed out of |
| $f'<0$ ⟹ $f<0$ — "falling, so it must be below zero" | coffee $T(t) = 85 - 3t$ at $t=10$: $T = 55$ (hot), yet $T' = -3 < 0$ | **falling from above**: the arrow points down while the number sits positive — cooling, but still hot |
| $f'=0$ ⟹ $f=0$ or "it stopped" | ball $s(t) = 5 + 20t - 4.9t^2$ at the peak ($t \approx 2.04$): $v = 0$, yet $s \approx 25.4$ m | **flat for an instant**: the relation pauses; the number sits wherever it sits. $f'=0$ reads "momentarily flat" — never "zero", never "stopped" |
| $\|f'\|$ big ⟹ $\|f\|$ big — "a steep arrow means a big number" | $f(x) = 1000x$ at $x=0$: $f = 0$ with $f' = 1000$; and $g(x) = 100$: $g = 100$ with $g' = 0$ | **the arrow's size is its own axis** — a giant arrow at zero, and a giant number with no arrow |

**The two questions, kept apart.** "Where is the number?" is answered by $f$; "where is it going?" by the sign of $f'$. All four combinations are legal, and each has a live model:

| $f$ (sits) | $f'$ (goes) | Live model | One sentence |
|:---:|:---:|:---|:---|
| positive | positive | savings with interest | "ahead, moving further ahead" |
| positive | negative | coffee cooling | "above zero, sinking" |
| negative | positive | debt being paid off | "below zero, climbing" |
| negative | negative | debt growing | "below zero, sinking deeper" |

**The word trap.** "Negative" does two jobs at once: a *negative balance* ($f < 0$) is a fact about position, while a *negative slope* ($f' < 0$) is a fact about direction. Language lets the word leak from one axis to the other — "it's falling" starts to mean "it's low." The discipline: before saying "negative," name the axis. A negative balance can be climbing; a negative slope can be cooling a pot that is still hot.

**The flat trap: $f' = 0$ promises flatness — nothing more.** It does not promise $f = 0$ (the ball in the table sits 25.4 m up), it does not promise a stop ($x^3$ passes straight through zero), and it does not even promise a peak or a valley — $f(x) = (x-1)^3 + 2$ is flat at $x=1$ with $f = 2$, yet it is neither a maximum nor a minimum there (SN8). Flat is flat; that is the entire promise.

**Why the confusion is natural — and the one-line fix.** Everyday language fuses direction into position: "it is low, so it is falling" feels right, and it is wrong. The fix is to keep the axes separate: $f'$ is a *degree of relation* (units $f$ per $x$), not a reading of $f$'s position. Read every derivative sentence twice: first "where is it?" (sign of $f$), then "where is it going?" (sign of $f'$). When the two disagree — a debt climbing, coffee sinking — nothing is wrong; both facts are true on their own axes.

#### Sign Practice — Two Questions, Two Axes (SN1–SN10)

> For each: (a) where does the number sit (sign of $f$)? (b) where is it going (sign of $f'$)? (c) write the two-question sentence; (d) find where the position crosses zero, and read the direction there.

**SN1.** A bank balance is $B(t) = -800 + 50t$ dollars after $t$ days.

- **A.** Compute $B(10)$ — where does the number sit?
- **B.** Compute $B'(t)$ — where is it going?
- **C.** The two-question sentence.
- **D.** When does the balance cross zero — and does the degree change there?

<details>
<summary>Hint</summary>

$B(10) = -300$ (in debt); $B' = 50 > 0$ always. Crosses at $t = 16$; the degree is still $+50$ — crossing zero is an event in the position, not in the direction.

</details>

**SN2.** Coffee cools: $T(t) = 85 - 3t$ °C after $t$ minutes.

- **A.** Compute $T(10)$ — where does the number sit?
- **B.** Compute $T'(t)$ — where is it going?
- **C.** The two-question sentence.
- **D.** When does it reach 25 °C — what is the degree there?

<details>
<summary>Hint</summary>

$T(10) = 55$ °C (still hot); $T' = -3 < 0$. Reaches 25 at $t = 20$; the degree is still $-3$ — arriving at room temperature does not change the direction of cooling.

</details>

**SN3.** $f(x) = x^3$.

- **A.** Compute $f(0)$ and $f'(0)$ — both zero, or only one?
- **B.** Does $f$ "stop" at $x=0$? Check $f(0.1)$ and $f(-0.1)$.
- **C.** The two-question sentence.

<details>
<summary>Hint</summary>

$f(0) = 0$ and $f'(0) = 0$ — value and flatness coincide here. But $f(0.1) = 0.001$ and $f(-0.1) = -0.001$: the function passes through and keeps rising. "Flat for an instant — coincidence, not implication."

</details>

**SN4.** A ball: $s(t) = 5 + 20t - 4.9t^2$ meters.

- **A.** When is $v = 0$?
- **B.** What is the height at that instant?
- **C.** The two-question sentence for the instant $v = 0$.
- **D.** What is the velocity just after?

<details>
<summary>Hint</summary>

$v = 20 - 9.8t = 0$ at $t \approx 2.04$; $s \approx 25.4$ m — "paused at 25 m up: the process did not stop, the height did not vanish." Just after, $v < 0$ — it falls.

</details>

**SN5.** $f(x) = x + 2$ and $g(x) = x - 5$.

- **A.** Compute $f'(x)$ and $g'(x)$ — where does each go?
- **B.** Compute $f(0)$ and $g(0)$ — where does each sit?
- **C.** One sentence about lockstep motion on opposite sides of zero.

<details>
<summary>Hint</summary>

$f' = g' = 1$ — identical arrows. $f(0) = 2 > 0$, $g(0) = -5 < 0$ — opposite positions. Direction is shared; position is not.

</details>

**SN6.** A car's position is $s(t) = t^2 - 25$ meters ($t \ge 0$).

- **A.** Compute $s(3)$ — where does the number sit?
- **B.** Compute $v(t)$ and $v(3)$ — where is it going?
- **C.** The two-question sentence.
- **D.** When does it cross the start line, and what is the velocity there?

<details>
<summary>Hint</summary>

$s(3) = -16$ m (behind the line); $v = 2t = 6 > 0$ m/s — "behind the start line, moving forward." Crosses at $t = 5$ with $v = 10$ — the crossing does not pause the arrow.

</details>

**SN7.** A sinking balance: $B(t) = -200 - 30t$ dollars after $t$ days.

- **A.** Compute $B(5)$ — where does the number sit?
- **B.** Compute $B'(t)$ — where is it going?
- **C.** The two-question sentence (the fourth combination).
- **D.** Does the degree ever notice the debt doubling?

<details>
<summary>Hint</summary>

$B(5) = -350$, $B' = -30 < 0$ always — "below zero, sinking deeper." Never: the arrow stays $-30$ whether the debt is $-200$ or $-2{,}000{,}000$.

</details>

**SN8.** $f(x) = (x-1)^3 + 2$.

- **A.** Where is $f'(x) = 0$?
- **B.** What is $f$ there?
- **C.** Is that point a peak or a valley? Check $f(0.9)$ and $f(1.1)$.
- **D.** The two-question sentence.

<details>
<summary>Hint</summary>

$f' = 3(x-1)^2 = 0$ at $x = 1$; $f(1) = 2$. $f(0.9) = 1.999$, $f(1.1) = 2.001$ — the curve passes straight through: neither peak nor valley. "$f' = 0$ promises flatness only."

</details>

**SN9.** Freezing while warming: $T(t) = -10 + 0.5t$ °C after $t$ minutes.

- **A.** Compute $T(10)$ — where does the number sit?
- **B.** Compute $T'(t)$ — where is it going?
- **C.** The two-question sentence.
- **D.** When does it cross 0 °C, and what is the degree there?

<details>
<summary>Hint</summary>

$T(10) = -5$ °C; $T' = 0.5 > 0$ — "below freezing, warming." Crosses at $t = 20$; the degree is still $+0.5$ — the value's zero changes nothing in the arrow.

</details>

**SN10.** Two size traps: $f(x) = 1000x$ and $g(x) = 100$.

- **A.** Compute $f(0)$ and $f'(0)$ — where does the number sit, how big is the arrow?
- **B.** Compute $g(0)$ and $g'(0)$.
- **C.** One sentence pairing the two traps.

<details>
<summary>Hint</summary>

$f(0) = 0$ with $f' = 1000$ — a giant arrow at zero. $g(0) = 100$ with $g' = 0$ — a giant number with no arrow. The arrow's size is its own axis, in both directions.

</details>

→ Solutions: [Solutions](solutions/14D-solutions.md#sign-practice)

---

### The Variable Jail — A Letter Means Only What Its Lock Says

The nastiest trap of the session: **one formula supports several different relations, and which one you are reading is decided by which letters you lock up — not by the letters themselves.** A letter is not born "variable" or "constant"; it is declared. Misread the declaration and the whole interpretation tangles.

**The anchor: RPA3's heater, reread.** $P = \frac{V^2}{R}$ contains three letters and supports two locks:

- **Lock the voltage** ($V = 120$ fixed): the driver is $R$, the response is $P$. $P(R) = \frac{14400}{R}$, so $\frac{dP}{dR} = -\frac{14400}{R^2} = -4$ W/Ω at $R = 60$ — "bigger resistance, less power."
- **Lock the resistance** ($R = 60\,\Omega$ fixed): the driver is $V$, the response is $P$. $P(V) = \frac{V^2}{60}$, so $\frac{dP}{dV} = \frac{2V}{60} = 4$ W/V at $V = 120$ — "higher voltage, more power."

Same letters, same formula, opposite verdicts — because the lock, not the letter, carries the meaning. "$V$ is fixed at 120" is not a detail; it *is* the sentence.

**The nastiest lock-mix: $t$ as duration vs $t$ as the flowing clock.** One letter, two roles, both live in this session:

- RPB3: $t(v) = \frac{120}{v}$ — here $t$ is the trip's **duration**: a response bought by speed. "At 60 km/h, each extra km/h shaves 2 minutes off the trip."
- The motion stories: $s(t) = vt$ — here $t$ is the **flowing clock**: a driver that buys meters. "Each second of driving buys $v$ meters."

Duration is read from outside — the whole trip, one number. Flowing time is read from inside — the running coordinate of the current instant. A problem that keeps both in play ("the trip takes $T$ hours; at the instant $t$, …") is asking you to hold two jails open at once, and that is exactly where readings tangle.

**The minus reads the relation, never the quantity's nature.** In the duration jail, $\frac{dt}{dv} = -\frac{120}{v^2} < 0$ says the duration *number* shrinks as speed grows — it does not say time "runs backwards." A reversed relation is a shrinking total, not a reversed clock: the sign of a derivative flips only the direction of the relation, never what the quantity is. JA6 and JA7 dismantle this trap explicitly.

**The jail checklist, before differentiating anything:**

1. **Lock the parameters** — which letters are frozen numbers (the 120 V, the 120 km, the 200 m of fence)?
2. **Name the driver** — which letter moves first?
3. **Name the response** — which letter answers?

Then, and only then, write the function and differentiate. The jail *is* the interpretation.

#### Variable-Jail Practice — Read the Lock First (JA1–JA7)

> For each: run the jail checklist out loud, then compute.

**JA1.** $P = \frac{V^2}{R}$, both locks in one problem.

- **A.** Lock $V = 120$: compute $\frac{dP}{dR}$ at $R = 60$ and read the sentence.
- **B.** Lock $R = 60$: compute $\frac{dP}{dV}$ at $V = 120$ and read the sentence.
- **C.** What changed between (a) and (b) — the formula or the relation?

<details>
<summary>Hint</summary>

(a) $-4$ W/Ω — power fights resistance. (b) $+4$ W/V — power follows voltage. (c) The formula never changed; the lock picked a different relation out of it.

</details>

**JA2.** A 240 km trip.

- **A.** Set up the duration $T(v)$ and compute $\frac{dT}{dv}$ at $v = 80$ — which jail is $T$ in?
- **B.** Driving at constant 80 km/h, position is $s(t) = 80t$ — which jail is $t$ in? Compute $s'(t)$.
- **C.** One sentence contrasting the two time-letters.

<details>
<summary>Hint</summary>

(a) $T = \frac{240}{v}$, $\frac{dT}{dv} = -\frac{240}{v^2} = -0.0375$ h/(km/h) = −2.25 min per km/h at 80 — duration is bought by speed. (b) $s' = 80$ km/h — each hour of flowing time buys 80 km. (c) Duration is a response; flowing time is a driver.

</details>

**JA3.** A tank drains: $V(t) = 100 - 2t$ liters.

- **A.** Run the jail checklist and read $V'(t)$ in one sentence.
- **B.** The time to empty is $T = 50$ min — is 50 a derivative? What kind of number is it, compared to the $-2$?
- **C.** At $t = 30$: $V = 40$ L and $V' = -2$ L/min — why can 40 and $-2$ live in the same instant without contradiction?

<details>
<summary>Hint</summary>

(a) Driver $t$ (clock), response $V$; locked: the start 100 L and the rate 2 L/min. $V' = -2$ L/min — "each minute drains 2 L." (b) 50 min is a value in the duration jail (when $V$ hits 0); $-2$ L/min is a degree (how fast $V$ moves) — a number vs an arrow. (c) 40 L is the position, $-2$ L/min is the direction — different axes (the Sign Lens).

</details>

**JA4.** Ideal gas $PV = nRT$ with $nR = 8.3$.

- **A.** Lock $T = 300$: set up $P(V)$, compute $\frac{dP}{dV}$ at $V = 10$, and read the sentence.
- **B.** Lock $P = 100$: set up $V(T)$, compute $\frac{dV}{dT}$, and read the sentence.
- **C.** Which lock makes the relation inverse, which proportional — decide it from the solved formula's exponent directly.

<details>
<summary>Hint</summary>

(a) $P = \frac{2490}{V}$, $\frac{dP}{dV} = -24.9$ kPa/m³ at $V=10$ — inverse: squeeze → pressure up. (b) $V = 0.083\,T$, $\frac{dV}{dT} = 0.083$ m³/K — proportional: heat → expand. (c) Locking $T$ turns the law into a reciprocal ($V^{-1}$); locking $P$ turns it into a line ($V^{+1}$) — the lock chooses the power.

</details>

**JA5.** The heater, chained: $V = 120$ V fixed, but the resistance heats up: $R(t) = 60 + 0.2t$ Ω.

- **A.** Set up $P(t)$ through the chain and compute $\frac{dP}{dt}$ at $t = 0$ with units.
- **B.** Name each link's jail.
- **C.** Trap check — $\frac{dP}{dR} = -4$ W/Ω and $\frac{dP}{dt} = -0.8$ W/s: same heater, two degrees. Why are both true at once?

<details>
<summary>Hint</summary>

(a) Chain: $\frac{dP}{dt} = \frac{dP}{dR}\cdot\frac{dR}{dt} = -\frac{14400}{R^2}\cdot 0.2$; at $t=0$: $-4 \cdot 0.2 = -0.8$ W/s — each second of heating drops the power by 0.8 W. (b) Link 1: $P$ responds to $R$, with $V$ locked. Link 2: $R$ responds to $t$, with the start 60 and the rate 0.2 locked. (c) $-4$ W/Ω is the degree per ohm; $-0.8$ W/s is the degree per second — chained by the 0.2 Ω/s. Both true because they answer different "with respect to what" questions.

</details>

**JA6.** A 120 km trip takes $t(v) = \frac{120}{v}$ hours.

- **A.** Compute $\frac{dt}{dv}$ at $v = 60$ and read the sentence.
- **B.** The trap: "$v$ up → $t$ down, so $t$'s nature is reversed — time now flows backwards." Attack it: what exactly is $t$ here — a clock that flows, or a duration?
- **C.** The sign-lens check: where does $t$ sit at $v = 60$, and where is it going as $v$ rises? Can the number ever go below zero?
- **D.** What happens to $t$ as $v \to \infty$? Where does "backwards time" live in this picture?

<details>
<summary>Hint</summary>

$t(60) = 2$ h; $\frac{dt}{dv} = -\frac{120}{v^2} = -\frac{1}{30}$ h/(km/h) = −2 min per km/h. $t$ is the trip's total duration — a response the speed buys, not a clock. The number sits at $+2$ h and shrinks toward 0 as $v$ grows; it never crosses zero — "down forever, never below zero." The minus is the relation's direction, not time's nature.

</details>

**JA7.** One formula, two jails — a 240 km trip, both readings.

- **A.** Duration jail: $T(v) = \frac{240}{v}$. Compute $\frac{dT}{dv}$ at $v = 80$ and read the sentence.
- **B.** Clock jail: driving at the constant speed 80 km/h, position is $s(t) = 80t$. Compute $s'(t)$ and read the sentence.
- **C.** The minus lives in exactly one of the two. Where does "reversed" come from — from the nature of time, or from the relation's direction?
- **D.** Trap check: why is one degree negative and the other positive — and why is neither of them "time running backwards"?

<details>
<summary>Hint</summary>

(a) $T' = -\frac{240}{v^2} = -0.0375$ h/(km/h) = −2.25 min per km/h. (b) $s' = 80$ km/h. (c) The minus belongs to the relation's direction in the duration jail only; the clock jail has no minus because its driver is the clock itself. (d) Both are ordinary arrows — one shrinks a total, one builds a position. In (a) time is the response being counted; in (b) time is the driver doing the counting — different roles, different signs.

</details>

→ Solutions: [Solutions](solutions/14D-solutions.md#variable-jail-practice)

---

#### The Duration-Clock Drills — One Trap, Ten Disguises (DC1–DC10)

> One trap, ten disguises: a **total divided by a rate is a duration** — a response, never a clock. The minus in the degree shrinks the duration number; it never reverses time, and the number never crosses zero. For each: (A) compute the degree and read the sentence; (B) answer the trap question — what exactly is the time-letter here?; (C) run the sign-lens check; (D) the limit check.

**DC1.** A 400 L tank drains at rate $r$ L/min, so it takes $T(r) = \frac{400}{r}$ minutes to empty.

- **A.** Compute $\frac{dT}{dr}$ at $r = 20$ and read the sentence.
- **B.** Trap: "faster drain → time flows backwards." What is $T$ here — a clock or a duration?
- **C.** Where does $T$ sit at $r = 20$, and where is it going?
- **D.** What happens as $r \to 0^+$? As $r \to \infty$?

<details>
<summary>Hint</summary>

$T(20) = 20$ min; $\frac{dT}{dr} = -\frac{400}{r^2} = -1$ min per (L/min) — "each extra L/min of drain shaves 1 minute off the emptying time." $T$ is the emptying *duration*, not the clock. Positive number, down arrow, never below zero: $r\to0^{+}$ sends $T\to+\infty$; $r\to\infty$ sends $T\to0^{+}$.

</details>

**DC2.** A 60 kWh battery drawn at $P$ kW lasts $T(P) = \frac{60}{P}$ hours.

- **A.** Compute $\frac{dT}{dP}$ at $P = 6$ and read the sentence.
- **B.** Trap: "more power → time reversed?" What is $T$?
- **C.** The sign-lens check at $P = 6$.
- **D.** Where does $T$ go as $P \to 0^+$ and as $P \to \infty$?

<details>
<summary>Hint</summary>

$T(6) = 10$ h; $\frac{dT}{dP} = -\frac{60}{P^2} = -\frac{5}{3} \approx -1.67$ h/kW — "each extra kW of draw shortens the battery's life by about 1.7 hours." $T$ is a lifetime (duration): positive, shrinking, never negative; $T\to+\infty$ as $P\to0^{+}$, $T\to0^{+}$ as $P\to\infty$.

</details>

**DC3.** A 300-page book read at $p$ pages/day takes $T(p) = \frac{300}{p}$ days.

- **A.** Compute $\frac{dT}{dp}$ at $p = 30$ and read the sentence (convert to hours).
- **B.** Trap: "reading faster makes time run backwards?"
- **C.** The sign-lens check.
- **D.** The limit check as $p \to 0^+$ and $p \to \infty$.

<details>
<summary>Hint</summary>

$T(30) = 10$ days; $\frac{dT}{dp} = -\frac{300}{p^2} = -\frac{1}{3}$ day per (page/day) = −8 h per (page/day) — "each extra page per day shaves 8 hours off the reading time." Duration, not clock: positive, sinking, never below zero.

</details>

**DC4.** A 5000 MB file downloading at $b$ MB/s takes $T(b) = \frac{5000}{b}$ seconds.

- **A.** Compute $\frac{dT}{db}$ at $b = 50$ and read the sentence.
- **B.** Trap: "more bandwidth → the download clock runs backwards?"
- **C.** The sign-lens check.
- **D.** The limit check.

<details>
<summary>Hint</summary>

$T(50) = 100$ s; $\frac{dT}{db} = -\frac{5000}{b^2} = -2$ s per (MB/s) — "each extra MB/s shaves 2 seconds off the download." The duration shrinks; the clock never reverses.

</details>

**DC5.** Saving \$1200 at \$d per week takes $T(d) = \frac{1200}{d}$ weeks.

- **A.** Compute $\frac{dT}{dd}$ at $d = 40$ and read the sentence (convert to days).
- **B.** Trap: "saving faster → time backwards?"
- **C.** The sign-lens check.
- **D.** The limit check.

<details>
<summary>Hint</summary>

$T(40) = 30$ weeks; $\frac{dT}{dd} = -\frac{1200}{d^2} = -0.75$ week per (dollar/week) ≈ −5 days per (dollar/week). The saving *time* is a duration: positive, shrinking, never negative.

</details>

**DC6.** A 50 m³ pool filled at $q$ m³/h takes $T(q) = \frac{50}{q}$ hours.

- **A.** Compute $\frac{dT}{dq}$ at $q = 2.5$ and read the sentence.
- **B.** Trap: "a faster pump reverses time?"
- **C.** The sign-lens check.
- **D.** The limit check.

<details>
<summary>Hint</summary>

$T(2.5) = 20$ h; $\frac{dT}{dq} = -\frac{50}{q^2} = -8$ h per (m³/h) — "each extra m³/h shaves 8 hours off the fill." Duration, not clock.

</details>

**DC7.** A 42 km marathon run at $v$ km/h takes $T(v) = \frac{42}{v}$ hours.

- **A.** Compute $\frac{dT}{dv}$ at $v = 14$ and read the sentence (convert to minutes).
- **B.** Trap: "running faster makes the race clock run backwards?"
- **C.** The sign-lens check.
- **D.** The limit check.

<details>
<summary>Hint</summary>

$T(14) = 3$ h; $\frac{dT}{dv} = -\frac{42}{v^2} = -\frac{3}{14}$ h per (km/h) ≈ −13 min per (km/h). The finishing *time* is a duration: the faster you run, the smaller the total — never a reversed clock.

</details>

**DC8.** A 1000-page document printed at $n$ pages/min takes $T(n) = \frac{1000}{n}$ minutes.

- **A.** Compute $\frac{dT}{dn}$ at $n = 20$ and read the sentence.
- **B.** Trap: "a faster printer reverses time?"
- **C.** The sign-lens check.
- **D.** The limit check.

<details>
<summary>Hint</summary>

$T(20) = 50$ min; $\frac{dT}{dn} = -\frac{1000}{n^2} = -2.5$ min per (page/min). Duration, not clock.

</details>

**DC9.** The clock jail, side by side: the same 400 L tank drains at a fixed $r = 20$ L/min.

- **A.** In the clock jail, $V(t) = 400 - 20t$: compute $V'(t)$ and read the sentence — which jail is $t$ in now?
- **B.** Compare with DC1: both derivatives carry a minus. Do the two minuses say the same thing?
- **C.** One sentence: where does each minus live, and why does time flow forward in both?

<details>
<summary>Hint</summary>

$V' = -20$ L/min — "each flowing minute drains 20 L." Here $t$ IS the clock (driver), and the minus is the water going down. DC1's minus shrank a duration (response); DC9's minus drains a volume — two different axes, both clocks flowing forward.

</details>

**DC10.** The limit trap: $T(r) = \frac{400}{r}$ again.

- **A.** What is $\lim_{r\to0^{+}} T(r)$?
- **B.** What is $\lim_{r\to\infty} T(r)$?
- **C.** Is there any $r > 0$ with $T(r) < 0$? Where does "negative time" live?

<details>
<summary>Hint</summary>

$T \to +\infty$ as $r \to 0^{+}$ (a stopped drain never empties); $T \to 0^{+}$ as $r \to \infty$. Never negative: the duration jail contains no negative numbers — "down forever, never below zero."

</details>

→ Solutions: [Solutions](solutions/14D-solutions.md#duration-clock-drills)

---

#### The Jail Trap Gallery — Six More Locks (JT1–JT6)

> The jail checklist (lock the parameters, name the driver, name the response) is the same weapon; these six traps disguise the lock six different ways.

**JT1.** The two-2's trap: for the trip $t(v) = \frac{120}{v}$, both sentences use the word "time."

- **A.** Read $t(60) = 2$ h — what kind of number is the 2?
- **B.** Read $t'(60) = -2$ min per (km/h) — what kind of number is the 2?
- **C.** The units decide the jail: which 2 is a value, which 2 is a degree?

<details>
<summary>Hint</summary>

$2$ h is a *value* (the duration, in hours). $-2$ min/(km/h) is a *degree* (duration per speed). Same digit, different jails — the units are the jail's ID card.

</details>

**JT2.** The letter-soup trap: coffee cools $T(t) = 85 - 3t$ °C while a 240 km trip takes $T(v) = \frac{240}{v}$ hours.

- **A.** Compute $T'(t)$ — which jail is each letter in?
- **B.** Compute $T'(v)$ at $v = 80$ — which jail is each letter in now?
- **C.** Same letter $T$, two jails. Read both sentences.

<details>
<summary>Hint</summary>

(a) $T' = -3$ °C/min — $T$ is temperature, $t$ is the flowing clock. (b) $T' = -\frac{240}{v^2} = -0.0375$ h/(km/h) — $T$ is duration, $v$ is speed. The letter carries nothing; the jail carries everything.

</details>

**JT3.** The parameter trap: a faucet drips 2 drops per second, 0.05 mL per drop.

- **A.** Build $V(t) = 0.1t$ and compute $V'(t)$ — which jail is the 0.1 in?
- **B.** Is "2 drops per second" a derivative? It is a rate, but of what?
- **C.** Classify every number in this problem: locked parameter or degree?

<details>
<summary>Hint</summary>

$V'(t) = 0.1$ mL/s — the degree of the built function $V$. The 2 drops/s and 0.05 mL/drop are *locked parameters* that feed the function — rates going in, not degrees coming out. A rate is not automatically a derivative.

</details>

**JT4.** The units-name-the-jail trap: match each degree to its jail.

- **A.** $m^3/s$ — clock jail or duration jail?
- **B.** $s/(m^3/s)$ — clock jail or duration jail?
- **C.** $\mathrm{L/min}$ vs $\mathrm{min/(L/min)}$ — which is which, and what is the fingerprint?

<details>
<summary>Hint</summary>

quantity per time (m³/s, L/min) = clock jail — something flows per second. Time per quantity (h/(km/h), min/(L/min)) = duration jail — a lifetime per rate. The fingerprint: a duration jail's units have time on top of a rate.

</details>

**JT5.** The domain trap: in $T(v) = \frac{120}{v}$, someone plugs $v = -60$.

- **A.** What does the formula print out?
- **B.** Is "$-2$ h" time running backwards? What does $v < 0$ even mean physically?
- **C.** State the jail's bars — the domain where the model means something real.

<details>
<summary>Hint</summary>

$T(-60) = -2$ h — but $v = -60$ is outside the model: speed is nonnegative. $-2$ h is not reversed time; it is an invalid input. The model lives on $v > 0$; outside the bars, the formula answers but the model is silent.

</details>

**JT6.** The chain-with-a-duration trap: a 300 km trip at speed $v$ takes $T(v) = \frac{300}{v}$ hours, and the car burns 6 L of fuel per flowing hour.

- **A.** Set up fuel $f(v)$ through the chain and compute $\frac{df}{dv}$ at $v = 100$ with units.
- **B.** Name each link's jail: what does the 6 L/h lock, and what does $T'(v)$ measure?
- **C.** Read the chained sentence.

<details>
<summary>Hint</summary>

$f = 6\cdot T(v) = \frac{1800}{v}$; $\frac{df}{dv} = -\frac{1800}{v^2} = -0.18$ L per (km/h) at $v=100$ — "each extra km/h saves 0.18 L of fuel for the whole trip." The 6 L/h is a clock-jail rate (fuel per flowing hour, a locked parameter); $T'(v)$ is the duration jail — the chain multiplies one jail's degree into the other.

</details>

→ Solutions: [Solutions](solutions/14D-solutions.md#jail-trap-gallery)

---

#### The Jail Trap Gallery II — Ten Patterns Beyond Time (JT7–JT16)

> Ten more patterns, none of them time: the jail checklist scales to every quantity. Each one hides the lock in a different disguise.

**JT7.** The level-vs-flow trap: a reservoir holds 5,000,000 m³ and releases 30 m³/s.

- **A.** Write $V(t) = 5{,}000{,}000 - 30t$ and compute $V'(t)$ — value or degree, and which jail?
- **B.** "5,000,000 m³" — value or degree?
- **C.** Both numbers use cubic meters — why can they live side by side, and where does the jail difference hide?

<details>
<summary>Hint</summary>

$5{,}000{,}000$ m³ is a **level** (a value — how much water sits there); $30$ m³/s is a **flow** (a degree — how fast it leaves). Same unit family, two jails: the "/s" is the jail's ID card, not the "m³".

</details>

**JT8.** The depth trap: two submarines — (i) $e_1(t) = -50 + 3t$, (ii) $e_2(t) = -20 - 2t$ meters, $t$ in minutes.

- **A.** Sub (i) at $t = 10$: compute $e_1$ and $e_1'$ — the two-question sentence.
- **B.** Sub (ii) at $t = 10$: compute $e_2$ and $e_2'$ — the two-question sentence.
- **C.** The minus appears in the *value* and in the *degree*. Which minus is a real quantity (depth), which is an arrow — and is depth "anti-height"?

<details>
<summary>Hint</summary>

(i) $e_1 = -20$ m, $e_1' = +3$ m/min — "below sea level, climbing." (ii) $e_2 = -40$ m, $e_2' = -2$ m/min — "below sea level, sinking deeper." Depth is a legitimate negative coordinate, not reversed height; the degree's minus is the direction of motion. Same symbol, two jobs.

</details>

**JT9.** The negative-demand trap: $q(p) = 200 - 5p$ units at price $p$.

- **A.** Compute $q(45)$ — what does the formula print?
- **B.** "Negative demand = customers selling to the store?" What is the model's real domain?
- **C.** Does $q' = -5$ mean "demand is a reversed quantity"? What does it actually say?

<details>
<summary>Hint</summary>

$q(45) = -25$ — but the model lives on $0 \le p \le 40$; at $p = 45$ the formula answers and the model is silent. $q' = -5$ says price and demand move oppositely — a direction, not negative customers.

</details>

**JT10.** The reciprocal-read trap: a car burns 8 L per 100 km.

- **A.** Read it as a degree $\frac{df}{dd} = 0.08$ L/km — which jail (driver? response?)?
- **B.** The same relation read backwards: $\frac{dd}{df} = 12.5$ km/L — which jail now?
- **C.** How are 0.08 and 12.5 related — and why does the same car feel "reversed" between the two readings?

<details>
<summary>Hint</summary>

$0.08$ L/km: driver = km, response = L (small is good). $12.5$ km/L: driver = L, response = km (big is good) — reciprocals, $0.08 \times 12.5 = 1$. The "reversed" feeling is the reader swapping drivers, not the car changing.

</details>

**JT11.** The parameter trap, finance: a balance $B(t)$ earns 5% per year.

- **A.** At $B = 1000$, compute $B'(t) = 0.05 \cdot B(t)$ — is the 50 a value or a degree?
- **B.** The "5%" — is it a derivative? What jail does it live in?
- **C.** The digit 0.05 appears twice — once as a locked parameter, once inside the degree. Separate the two jobs.

<details>
<summary>Hint</summary>

$B' = 50$ \$/yr is a **degree** (balance per year); the 5%/yr is a **locked parameter** (a rate per dollar per year, unitless per year) feeding the function. $B'(t) = 0.05 \cdot B(t)$: the parameter multiplies the current value to produce the degree — input rate vs output rate.

</details>

**JT12.** The letter-soup trap, physics: $P(V) = \frac{2490}{V}$ and $P(R) = \frac{14400}{R}$.

- **A.** In the first, $P$ is pressure: compute $\frac{dP}{dV}$ at $V = 10$ and read the sentence.
- **B.** In the second, $P$ is power: compute $\frac{dP}{dR}$ at $R = 60$ and read the sentence.
- **C.** Same letter $P$, same minus — what separates the two readings?

<details>
<summary>Hint</summary>

(a) $-24.9$ kPa/m³ — "squeezing one m³ buys 24.9 kPa." (b) $-4$ W/Ω — "each extra ohm costs 4 W." The units (kPa/m³ vs W/Ω) are the jail's ID card; the letter $P$ is just ink.

</details>

**JT13.** The peak trap: revenue $R(p) = 200p - 5p^2$.

- **A.** Compute $R'(20)$ and $R(20)$ — "revenue is zero?" What does flat-at-the-top actually say?
- **B.** At $p = 30$: compute $R$ and $R'$ — the two-question sentence.
- **C.** Where does $R$ hit zero again, and what is $R'$ there?

<details>
<summary>Hint</summary>

$R'(20) = 0$ with $R(20) = 2000$ — a pause at the peak, not a zero. At $p=30$: $R = 1500 > 0$ but $R' = -100 < 0$ — "positive, sinking." $R = 0$ at $p = 40$ with $R' = -200$: the value dies at the boundary while the arrow was already pointing down.

</details>

**JT14.** The frame-question trap, geometry: a cylinder has $V = \pi r^2 h$.

- **A.** Lock $h = 10$: compute $\frac{dV}{dr}$ at $r = 2$ — which jail, and what shape does the degree have?
- **B.** Lock $r = 2$: compute $\frac{dV}{dh}$ — which jail, and what shape does the degree have?
- **C.** Same $V$, same letters, two different numbers — what picks one over the other?

<details>
<summary>Hint</summary>

(a) $\frac{dV}{dr} = 2\pi rh = 40\pi \approx 125.7$ m³/m — growing $r$ wraps a shell of side area $2\pi rh$. (b) $\frac{dV}{dh} = \pi r^2 = 4\pi \approx 12.6$ m³/m — growing $h$ stacks disks of area $\pi r^2$. The frame question picks the driver, and each driver carries its own degree (14D1A).

</details>

**JT15.** The word-"per" trap: two sentences about the same car.

- **A.** "The car burns 8 L per 100 km" — what kind of number is this?
- **B.** "The tank holds 50 L" — what kind of number is this?
- **C.** The word "per" appears in only one — what does "per" mark?

<details>
<summary>Hint</summary>

"8 L per 100 km" is a **degree** (a relation between two units); "50 L" is a **value** (a bare position). "Per" marks the degree — the "/km" is the jail.

</details>

**JT16.** The odometer-vs-speedometer trap: one trip, two numbers.

- **A.** "We drove 120 km" — value or degree?
- **B.** "We drove at 80 km/h" — value or degree?
- **C.** Same trip, same word "drove" — what separates the two numbers?

<details>
<summary>Hint</summary>

120 km is the trip's total (a value — the odometer); 80 km/h is the trip's speed (a degree — the speedometer). The odometer reads values; the speedometer reads degrees. Same word, two jails.

</details>

→ Solutions: [Solutions](solutions/14D-solutions.md#jail-trap-gallery)

---

#### The Jail Trap Gallery III — The Driver Is Not Time (JT17–JT24)

> The driver's identity is a jail of its own. Altitude, price, radius, temperature, distance, dose, depth, quantity — each carries its own "per." The trap: reading every "per" as "per second." The denominator is the jail.

**JT17.** The altitude driver: air pressure $P(h) = 101 - 12h$ kPa at altitude $h$ km.

- **A.** Compute $\frac{dP}{dh}$ at $h = 2$ and read the sentence.
- **B.** Trap: "$P' < 0$ → pressure is a negative quantity?" What is the driver — a clock or a place?
- **C.** Where does $P$ cross zero, and what does the minus actually flip?

<details>
<summary>Hint</summary>

$P(2) = 77$ kPa > 0; $\frac{dP}{dh} = -12$ kPa/km — "each km higher costs 12 kPa." The driver is altitude (a place); the minus is the direction of the relation, never negative pressure. $P = 0$ at $h = \frac{101}{12} \approx 8.42$ km — the model's edge, not "anti-pressure."

</details>

**JT18.** The price driver: demand $q(p) = 200 - 5p$.

- **A.** Compute $\frac{dq}{dp}$ and read the sentence.
- **B.** Trap: "demand falls per dollar — is the market running in time?" What is the driver's jail?
- **C.** How would the same formula read if the driver were $t$ instead of $p$?

<details>
<summary>Hint</summary>

$-5$ units/\$ — per dollar, not per second: the driver is price. If $p$ were $t$, the sentence would be a flow in time; here it is a trade in money. The driver's jail IS the sentence's tense.

</details>

**JT19.** The radius driver: circle area $A(r) = \pi r^2$.

- **A.** Compute $\frac{dA}{dr}$ at $r = 3$ and read the sentence.
- **B.** Trap: "the area grows fast — how many m² per second?" Does the formula answer that?
- **C.** Compare m²/m with m²/s — what would have to change for time to enter?

<details>
<summary>Hint</summary>

$\frac{dA}{dr} = 2\pi r = 6\pi \approx 18.8$ m² per meter of radius. The formula knows nothing about seconds — time enters only if $r$ itself depends on $t$ (the chain rule). A driver that is a length, not a clock.

</details>

**JT20.** The temperature driver: gas volume $V(T) = 0.083\,T$ m³ at fixed pressure.

- **A.** Compute $\frac{dV}{dT}$ and read the sentence.
- **B.** Trap: "heating speeds up the expansion?" Is there any speed in this picture?
- **C.** Which jail is $T$ in — and what would $V'(t)$ mean instead?

<details>
<summary>Hint</summary>

$\frac{dV}{dT} = 0.083$ m³/K — per kelvin, not per second: the driver is temperature. $V'(t)$ would need $T(t)$ chained in; $V'(T)$ is a static trade — "each kelvin buys 0.083 m³."

</details>

**JT21.** The distance driver: fuel $f(d) = 0.08d$ liters.

- **A.** Compute $\frac{df}{dd}$ and read the sentence.
- **B.** Trap: "0.08 L per km — is the fuel draining 0.08 L every second?"
- **C.** Same digit 0.08, two jails: 0.08 L/km vs 0.08 L/s — what changes?

<details>
<summary>Hint</summary>

Per kilometer, not per second. The 0.08 is identical ink; the driver's unit (km vs s) changes the entire sentence. The jail is the denominator.

</details>

**JT22.** The dose driver: a body's response $R(x) = 2x - 0.05x^2$ to a dose of $x$ mg.

- **A.** Compute $\frac{dR}{dx}$ at $x = 10$ and read the sentence.
- **B.** Trap: "response per milligram — is the body speeding up?" What is the driver?
- **C.** Where does $\frac{dR}{dx}$ hit zero — and is that a *moment in time*?

<details>
<summary>Hint</summary>

$\frac{dR}{dx} = 2 - 0.1x = 1$ per mg at $x=10$ — the driver is dose, not time. $\frac{dR}{dx} = 0$ at $x = 20$: the response peaks at 20 mg — a dose-location, not a moment.

</details>

**JT23.** The depth driver: water pressure $P(d) = 101 + 9.8d$ kPa at depth $d$ meters.

- **A.** Compute $\frac{dP}{dd}$ and read the sentence.
- **B.** Trap: "pressure grows — does pressure flow deeper?" What is the driver?
- **C.** At $d = 0$: read $P$ and $P'$ on the two axes.

<details>
<summary>Hint</summary>

$\frac{dP}{dd} = 9.8$ kPa/m — per meter of depth: the driver is a place, not a clock. At the surface: $P = 101$ kPa (positive position) and $P' = 9.8$ (positive arrow). Depth drives pressure; time is nowhere.

</details>

**JT24.** The quantity driver: cost $C(q) = 400 + 2q$ dollars for $q$ units.

- **A.** Compute $\frac{dC}{dq}$ and read the sentence.
- **B.** Trap: two numbers — is the 400 a degree? Is the 2 a value?
- **C.** Name each number's jail, and say why "2 dollars per unit" is not a speed.

<details>
<summary>Hint</summary>

400 is a locked **value** (the fixed cost); $2$ \$/unit is a **degree** (the marginal cost). Per unit, not per hour — the driver is quantity. Value and degree side by side in one formula.

</details>

→ Solutions: [Solutions](solutions/14D-solutions.md#jail-trap-gallery)

---

## Example 2: The Motion Story — Signs of $v$ and $a$ Together

$s(t) = t^3 - 6t^2 + 9t$ (meters, seconds, from 14C). $v(t) = s'(t) = 3(t-1)(t-3)$, $a(t) = s''(t) = 6t - 12$.

**Reading the sign of $v$**: $v>0$ = moving forward, $v<0$ = moving backward, $v=0$ = turning around (at $t=1$ and $t=3$).

**Reading the sign of $a$**: $a$ and $v$ have the **same sign** = speeding up. Opposite signs = slowing down. Negative $a$ is *not* automatically "decelerating" — it depends on the direction.

| Interval | $v$ | $a$ | Story |
|:---:|:---:|:---:|:---|
| $0 < t < 1$ | $+$ | $-$ | forward, slowing |
| $1 < t < 2$ | $-$ | $-$ | backward, speeding up |
| $2 < t < 3$ | $-$ | $+$ | backward, slowing |
| $t > 3$ | $+$ | $+$ | forward, speeding up |

The two turning points ($t=1, 3$) and the one acceleration switch ($t=2$) chop time into exactly four stories.

![Motion story from signs of v and a](graphs/0821/14D1/14d2-motion-story.png)

*Graph 14D-2: Top — $v(t)$ and $a(t)$ with zero crossings marked. Bottom — the motion timeline built purely from signs.*

**Lens reading**: velocity is position's degree of relation to time, acceleration is velocity's — the timeline reads the two relations' signs against each other: same sign means the relation is strengthening.

---

## What We Just Did

```
(1) Units: a derivative is y-units per x-unit. Write them first — they name the meaning.
(2) Relations: "y is related to x" is a sentence missing its number — dy/dx,
    in units of y per x, is that number. Sign = direction, size = strength, local at a point.
(3) Motion: sign of v = direction; v and a same sign = speeding up.
(4) Sign: f' is the arrow, f is the position — f' > 0 does not mean f > 0,
    f' < 0 does not mean f < 0, f' = 0 means "flat here", never "zero" and never "stopped".
(5) Jail: a letter means only what its lock says — lock the parameters, name the
    driver, then read. Same formula, different lock = a different relation (RPA3).
(6) Duration: a total divided by a rate is a lifetime — a duration (response), never
    a reversed clock; the minus shrinks the duration number, and it never crosses zero.
(7) Patterns: the jail scales to every quantity — level vs flow, depth vs height,
    price vs demand, mileage vs consumption; the sign flips the relation, never the
    quantity's nature.
(8) Drivers: the independent variable is a jail of its own — altitude, price, radius,
    temperature, distance, dose; "per driver" is never automatically "per second."
```

---

## Today's Procedure

| When you see... | Do this... |
|:---|:---|
| A derivative with real-world quantities | Write units first (y-units per x-unit), then sign, then size |
| "How related is y to x?" | The relation is a function $y(x)$; its degree is $dy/dx$ with units [y/x] — sign = direction, size = strength |
| A motion problem | Factor $v$ for turning points; compare signs of $v$ and $a$ for speeding/slowing |
| A derivative sign tempting you to read the value | Two questions, two axes: "where does the number sit?" ($f$) vs "where is it going?" ($f'$) — all four position × direction combinations are legal |
| One formula, several letters | Write the jail first: lock the parameters, name the driver and response — the lock carries the meaning, not the letter (RPA3's $P=V^2/R$) |
| A rate eating a total (tank, battery, trip, download) | Name the jail: the lifetime is a DURATION (a response), and the flowing clock is elsewhere — the minus shrinks the duration, never reverses time |
| A quantity whose sign looks like its nature (depth, debt, deficit) | Split the axes: the minus in the VALUE is a real position (depth); the minus in the DEGREE is a direction — same symbol, two jobs |
| A degree with a non-time driver (per km, per dollar, per meter of depth) | Name the driver: the units already say it — m²/m, L/km, kPa/m; "per X" means X is the jail, never a clock by default |

---

## How to Read These Symbols

| Symbol | Reads as | Meaning |
|:---:|:---:|------|
| $f'(x)$, $\frac{dy}{dx}$ | "f prime of x" / "d y d x" | instantaneous rate — y-units per x-unit |
| $dy/dx$ | "d y d x" | the degree of relation between two domains — y-units per x-unit |
| m/s, \$/unit, °C/km | "meters per second…" | the units that name the meaning of the derivative |
| $v$, $a$ | "velocity" / "acceleration" | $s'$ and $s''$ — sign of $v$ = direction; $v$ and $a$ same sign = speeding up |
| $f > 0$ vs $f' > 0$ | "the number sits above zero" vs "the number is going up" | position vs direction — independent axes |
| locked $V = 120$ | "voltage frozen at 120" | a parameter — the lock that turns $P = V^2/R$ into $P(R)$ |

---

## Terminology

| What we call it | Math term | Notation |
|:---:|:---:|:---:|
| degree of relation between x and y | derivative of y with respect to x | $\frac{dy}{dx}$, units y/x |
| moving forward / backward | sign of velocity | $v>0$ / $v<0$ |
| where the number sits vs where it goes | sign of $f$ vs sign of $f'$ | $f>0$ / $f'>0$ |
| freezing a letter | declaring a parameter | $V = 120$ fixed |
| driver / response | independent / dependent variable | $P(R)$ with $V$ locked |
| lifetime of a total under a rate | duration (a response, never a reversed clock) | $T(r) = \frac{400}{r}$, units time |
| level vs flow | value (a position) vs degree (a rate) | $5\cdot10^6$ m³ vs $30$ m³/s |
| the driver's identity | the independent variable's jail | per km, per \$, per kelvin — "per X" reads the jail |
