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

![Units of the derivative: m/s for position, $/unit for cost]({{graph:14d-01-derivative-units}})

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

**The flat trap: $f' = 0$ promises flatness — nothing more.** It does not promise $f = 0$ (the ball in the table sits 25.4 m up), it does not promise a stop ($x^3$ passes straight through zero), and it does not even promise a peak or a valley — $f(x) = (x-1)^3 + 2$ is flat at $x=1$ with $f = 2$, yet it is neither a maximum nor a minimum there. Flat is flat; that is the entire promise.

**Why the confusion is natural — and the one-line fix.** Everyday language fuses direction into position: "it is low, so it is falling" feels right, and it is wrong. The fix is to keep the axes separate: $f'$ is a *degree of relation* (units $f$ per $x$), not a reading of $f$'s position. Read every derivative sentence twice: first "where is it?" (sign of $f$), then "where is it going?" (sign of $f'$). When the two disagree — a debt climbing, coffee sinking — nothing is wrong; both facts are true on their own axes.

### The Variable Jail — A Letter Means Only What Its Lock Says

The nastiest trap of the session: **one formula supports several different relations, and which one you are reading is decided by which letters you lock up — not by the letters themselves.** A letter is not born "variable" or "constant"; it is declared. Misread the declaration and the whole interpretation tangles.

**The anchor: the heater, reread.** $P = \frac{V^2}{R}$ contains three letters and supports two locks:

- **Lock the voltage** ($V = 120$ fixed): the driver is $R$, the response is $P$. $P(R) = \frac{14400}{R}$, so $\frac{dP}{dR} = -\frac{14400}{R^2} = -4$ W/Ω at $R = 60$ — "bigger resistance, less power."
- **Lock the resistance** ($R = 60\,\Omega$ fixed): the driver is $V$, the response is $P$. $P(V) = \frac{V^2}{60}$, so $\frac{dP}{dV} = \frac{2V}{60} = 4$ W/V at $V = 120$ — "higher voltage, more power."

Same letters, same formula, opposite verdicts — because the lock, not the letter, carries the meaning. "$V$ is fixed at 120" is not a detail; it *is* the sentence.

**The nastiest lock-mix: $t$ as duration vs $t$ as the flowing clock.** One letter, two roles, both live in this session:

- A 120 km trip at $v$ km/h: $t(v) = \frac{120}{v}$ — here $t$ is the trip's **duration**: a response bought by speed. "At 60 km/h, each extra km/h shaves 2 minutes off the trip."
- The motion stories: $s(t) = vt$ — here $t$ is the **flowing clock**: a driver that buys meters. "Each second of driving buys $v$ meters."

Duration is read from outside — the whole trip, one number. Flowing time is read from inside — the running coordinate of the current instant. A problem that keeps both in play ("the trip takes $T$ hours; at the instant $t$, …") is asking you to hold two jails open at once, and that is exactly where readings tangle.

**The minus reads the relation, never the quantity's nature.** In the duration jail, $\frac{dt}{dv} = -\frac{120}{v^2} < 0$ says the duration *number* shrinks as speed grows — it does not say time "runs backwards." A reversed relation is a shrinking total, not a reversed clock: the sign of a derivative flips only the direction of the relation, never what the quantity is. The duration jail in the drills is built on exactly this trap.

**The jail checklist, before differentiating anything:**

1. **Lock the parameters** — which letters are frozen numbers (the 120 V, the 120 km, the 200 m of fence)?
2. **Name the driver** — which letter moves first?
3. **Name the response** — which letter answers?

Then, and only then, write the function and differentiate. The jail *is* the interpretation.

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

![Motion story from signs of v and a]({{graph:14d-02-motion-story}})

*Graph 14D-2: Top — $v(t)$ and $a(t)$ with zero crossings marked. Bottom — the motion timeline built purely from signs.*

**Lens reading**: velocity is position's degree of relation to time, acceleration is velocity's — the timeline reads the two relations' signs against each other: same sign means the relation is strengthening.

---

## Basic Drills

*Goal: one clean move per item, at speed. Each item asks for a single sentence — and the sentence is wrong unless the units are printed with the number. Budget: 40 seconds each.*

> **The bank at a glance.** **Basic** (B1–B4): the relation lens, the two locks, the sign lens, and flow-versus-level — one clean move each. **Intermediate** (I1–I4): a secant against a tangent, an optimum found by sign change, a double zero against a simple zero, and a two-link chain solved twice. **Advanced** (A1–A4): a forced stationary inflection, a three-link chain eliminated, a family built to order, and a submitted solution to repair. Solutions: [Solutions](solutions/14D-solutions.md#basic-drills).

**B1.** A 120 km trip takes $t(v) = \frac{120}{v}$ minutes at speed $v$ km/h.
Compute $\frac{dt}{dv}$ at $v=60$. Then say which of these two sentences the number licenses: "each extra km/h shaves about 2 seconds off the trip" or "each extra km/h shaves about 33 seconds off the trip."

<details>
<summary>Hint</summary>

Differentiate first, then match the *size* of the number to the sentence. The units tell you that the answer must be minutes per km/h; take care that $\frac{1}{30}$ minute is 2 seconds, not 33.

</details>

**B2.** A heater of resistance $R$ ohms runs at fixed voltage $V=120$ V, so its power is $P = \frac{V^2}{R}$ watts.
Compute $\frac{\partial P}{\partial V}$ and $\frac{\partial P}{\partial R}$ at $R=10$, then read each as a sentence with its units.

<details>
<summary>Hint</summary>

Each letter gets its own lock: one differentiation holds $R$ fixed, the other holds $V$ fixed. The power itself is $P=1440$ W before either rate is written.

</details>

**B3.** A hiker's altitude profile is $j(x) = 3(x-2)^2 + 5$ hundred meters, $x$ km east of the trailhead.
Read the pair $\left(j, j'\right)$ at $x=2$ and at $x=0$ separately, and say which of the two readings a walker actually feels.

<details>
<summary>Hint</summary>

At $x=2$ one of the two numbers vanishes. Ask whether a vanishing number describes where the walker *is* or how the ground is *tilted*.

</details>

**B4.** A battery charges at $r(t) = 6 - \frac{t}{2}$ liters per minute for $t$ minutes, starting from empty.
Find the charge $S(t)$. Then decide whether the battery is filling or draining at $t=6$ and at $t=12$ — and whether the *charge* is ever negative on $0 \le t \le 12$.

<details>
<summary>Hint</summary>

Two different quantities are in play: the flow $r$ and the accumulated charge $S$. One of them reaches zero at $t=12$; check what the other is doing at that same instant.

</details>

---

## Intermediate Drills

*Goal: two or three sub-steps in a forced order, with one decision to make. Do the sub-parts in the order given — each answer feeds the next. Budget: 3 minutes each.*

**I1.** A vendor's monthly sales are $B(p) = \frac{900}{p}$ thousand units at price $p$ dollars.

- **I1.1** Estimate the rate at $p=30$ by two points: $\frac{B(31)-B(30)}{1}$.
- **I1.2** Compute the exact rate $\frac{dB}{dp}$ at $p=30$. Which direction did the estimate err, and by how much?
- **I1.3** Compute $\frac{dB}{dp}$ at $p=60$. A colleague claims that doubling the price halves the rate. Decide whether the claim is true, and correct it with the number you just computed.
- **I1.4** State the one sentence that is right at *every* $p$, and the one that is right only at $p=30$.

<details>
<summary>Hint</summary>

The exact rate is $-\frac{900}{p^2}$, and the two-point estimate is a secant, not a tangent. For the colleague's claim, compare the two rates as a *ratio*, not by eye.

</details>

**I2.** A packaging line's monthly cost runs as $C(x) = \frac{x^3}{12} + \frac{24}{x}$ thousand dollars, where $x$ is the lot size in hundreds of boxes. The first term is machine time (it grows with the lot); the second is changeover overhead (it is spread thinner as the lot grows).

- **I2.1** Differentiate. Write $C'(x)$ as a single fraction.
- **I2.2** Find the one positive $x$ where $C'=0$, in exact form. (It is not a whole number — a clean fourth root is fine.)
- **I2.3** Test $C''$ at that point and decide whether it is a minimum. Then compute $C$ at $x=4$, $6$, and $12$ to confirm by comparison.
- **I2.4** Each term owns the derivative's sign on one side: name which term rules at small $x$ and which at large $x$, and explain why the optimum is where control passes between them.

<details>
<summary>Hint</summary>

Combine over one denominator before solving. The derivative's sign is decided by its numerator alone, so find where the numerator changes sign — and use $C'$'s sign on either side rather than $C$'s values alone.

</details>

**I3.** A function is $g(x) = x^3 - 12x + 16$.

- **I3.1** Factor $g$ completely, then list the zeros of $g$, of $g'$, and of $g''$ as three separate rows.
- **I3.2** One zero of $g$ is also a zero of $g'$. Say what the graph is doing there, and why "the value is 0" and "the arrow is 0" coinciding does *not* mean they report the same thing.
- **I3.3** At $x=0$ the second derivative vanishes. Report $g(0)$ and state whether a zero of the *degree of the degree* predicts anything about where $g$ sits.
- **I3.4** Find an $x$ where $g>0$ while $g'<0$. Write the two sentences in order — where it sits, then where it goes — and note which of the two a sign-only reader would get backwards.

<details>
<summary>Hint</summary>

A repeated factor in $g$ is exactly what makes $g'$ vanish at the same spot. The three rows are independent ledgers: share the arithmetic, never the conclusions.

</details>

**I4.** A sand pile is filled to depth $d$ metres. The sand mass is $m = 1600d$ kg, and the hauling cost is $K = \frac{2}{5}m + \frac{m^2}{100000}$ dollars.

- **I4.1** Write the two links with their units, then chain them to get $\frac{dK}{dd}$.
- **I4.2** Evaluate $\frac{dK}{dd}$ at $d=5$ and at $d=10$. Why is the answer not constant, even though $\frac{dm}{dd}$ is?
- **I4.3** Get the same answer a second way: substitute $m$ into $K$ first, then differentiate in $d$. Show the two routes agree.
- **I4.4** Name which letter is locked in each of the two routes, and say what goes wrong if you lock the *wrong* one.

<details>
<summary>Hint</summary>

The inner link is linear, so all the variation lives in the outer link — and the outer link is evaluated at the *current* mass. Route two turns the composition into a single polynomial in $d$.

</details>

## Advanced Drills

*Goal: justify, construct, and repair. No hint is given for the reasoning — the check step is part of the question. Budget: 8–12 minutes each.*

**A1.** Consider the family $f(x) = x^4 + ax^3 + bx^2$.

- **A1.1** Impose both conditions "$f$ is flat at $x=2$" and "$f$ changes concavity at $x=2$" at once. Solve for $(a,b)$ and show the pair is forced — there is no second solution.
- **A1.2** With your $(a,b)$, factor $f'$ and $f''$ completely. Identify every critical point and classify it.
- **A1.3** Show that $x=2$ is a point of inflection that is *not* an extremum: give the two signs of $f'$ immediately on either side, and the two signs of $f''$.
- **A1.4** A student concludes: "the arrow is zero and the concavity flips, so the mountain must turn into a valley there." State precisely what the arrow and the concavity each report, and where the student's inference breaks.

<details>
<summary>Check</summary>

Two linear conditions in $(a,b)$ give one pair; verify by substituting back into both derivatives rather than trusting the algebra. For the classification, the *sign change* of $f'$ is the test — not its vanishing.

</details>

**A2.** A waffle stand sets price $P$ dollars. Weekly sales follow $q = 400 - 5P$ waffles, one batch is $w = \frac{q}{40}$ batches, and the gas bill is $G = 2 + w^2$ therms.

- **A2.1** Write the three links with units, and chain them to get $\frac{dG}{dP}$.
- **A2.2** Evaluate $\frac{dG}{dP}$ at $P=40$, at $P=60$, and at $P=80$. Explain the pattern of magnitudes, and say what the vanishing at $P=80$ means about the two ends of the chain.
- **A2.3** Obtain $\frac{dG}{dP}$ a second way: eliminate $q$ and $w$ first, then differentiate in $P$. Confirm the formula $G(P)$ you get, and the same three values.
- **A2.4** State the price at which raising the price *reduces* the gas bill, and the price at which it no longer matters. Justify each from your function, not from the numbers alone.

<details>
<summary>Check</summary>

The middle link is linear, so the whole curvature comes from the last one — evaluated at the current batch count. Compare the chained formula with the composite; a sign error in one of the three links shows up as a mismatch.

</details>

**A3.** Design a quartic $F(x) = x^4 + ax^3 + bx^2 + cx + d$ that meets **all four** requirements at once: it is flat at $x=1$; it changes concavity at $x=1$; it passes through $(1,4)$; and it is not constant.

- **A3.1** Impose the four conditions and solve. Show that one parameter stays free, and name the free parameter.
- **A3.2** Pin the free parameter to the value that makes the *quadratic term vanish*, and write $F$. Then check by direct substitution that all four requirements hold.
- **A3.3** Report $F'(1)$, $F''(1)$, and $F'''(1)$. Explain why the third derivative is the one that proves the concavity really flips.
- **A3.4** The family also contains a member with integer coefficients that still fails one of the requirements — the trap member $c=-4$. Compute its $F'''$ at $x=1$, factor $F$, and explain what has gone wrong: is $x=1$ an inflection there?
- **A3.5** For your pinned $F$, find every critical point, classify each, and then explain why "$F$ is flat at $x=1$" is compatible with "$F$ is increasing through $x=1$."
- **A3.6** Count: four conditions, five coefficients. State the general principle this illustrates about how many constraints a stationary inflection costs.

<details>
<summary>Check</summary>

Four conditions on five letters leaves one degree of freedom — check the count before solving. A stationary inflection is proved by the *odd* derivative that does not vanish; compute $F'''$ rather than arguing from the picture.

</details>

**A4.** Here is a piece of submitted work. A workshop produces widgets at $w = 4h$ from $h$ hours, and costs $C = 60 + 3w + \frac{w^2}{50}$ dollars.

> "Hours to widgets loses 4 widgets per hour, and widgets to dollars gains $\frac{w}{25}+3$ dollars per widget. So hours to dollars is the ratio:
> $$\frac{dC}{dh} = \frac{dw/dh}{dC/dw} = \frac{4}{\frac{w}{25}+3}\ \text{dollars per hour.}$$
> At $h=5$ that is about \$1.05 per hour."

- **A4.1** Locate the error. Not the arithmetic — the *structure*. Say exactly which two operations were conflated.
- **A4.2** Run the units of the submitted expression through the dimensional check, and state what kind of quantity it actually is.
- **A4.3** Compute $\frac{dC}{dh}$ correctly by the chain, then again by substituting $w=4h$ into $C$ and differentiating in $h$. Show the two routes agree at $h=5$.
- **A4.4** Explain, from the units, why the submitted number and the correct number cannot even be compared as "small."
- **A4.5** Repair the student's claim so that it becomes true. State plainly whether the ratio they computed can be kept.

<details>
<summary>Check</summary>

The inversion of a chain reverses the order as well as inverting each link. Test any candidate repair by plugging $h=5$ and checking it lands on $\frac{76}{5}$ dollars per hour.

</details>

> Solutions: [Solutions](solutions/14D-solutions.md#basic-drills)

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
    driver, then read. Same formula, different lock = a different relation (the heater).
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
| One formula, several letters | Write the jail first: lock the parameters, name the driver and response — the lock carries the meaning, not the letter (the heater's $P=V^2/R$) |
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
