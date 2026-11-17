# Solutions — 14D: The Relation Lens

> Back to [14D — The Relation Lens](../14D-relation-lens.md)

---

## Basic Drills

### B1.

$$\frac{dt}{dv} = -\frac{120}{v^2},\qquad \left.\frac{dt}{dv}\right|_{v=60} = -\frac{120}{3600} = -\frac{1}{30}\ \text{min per km/h}$$

The rate is $-\frac{1}{30}$ min per km/h, and $\frac{1}{30}$ minute is **2 seconds**. So the correct sentence is the *first* one: "each extra km/h shaves about 2 seconds off the trip."

The tempting wrong reading is 33 seconds, produced by rescaling $-\frac{1}{30}$ as if the denominator were per *second* rather than per *km/h*. Write the units before speaking and the factor of 60 appears on its own. For comparison, the two-point estimate from $v=60$ to $v=61$ is
$$\frac{t(61)-t(60)}{1} = \frac{120}{61} - 2 = -\frac{2}{61}\ \text{min} \approx -1.967\ \text{s},$$
close to the tangent but not equal to it: a secant is not a derivative.

> **Answer**: $-\frac{1}{30}$ min per km/h $= -2$ s per km/h — the "2 seconds" sentence.

### B2.

Here are the two locks, each with its own table:

$$\frac{\partial P}{\partial V} = \frac{2V}{R} = \frac{2(120)}{10} = 24\quad \text{W per V},\qquad
\frac{\partial P}{\partial R} = -\frac{V^2}{R^2} = -\frac{14400}{100} = -144\quad \text{W per }\Omega$$

Two sentences, two locks: "at 120 V through 10 Ω, each extra volt adds about 24 W" and "with the voltage held at 120 V, each extra ohm takes about 144 W away."

The wrong-but-feels-right reading swaps the drivers: "$-144$ W per ohm" is *not* "each ohm of resistance costs 144 volts." The sign belongs to the relation, and the denominator names which letter was moving.

> **Answer**: $+24$ W/V and $-144$ W/Ω, at $V=120$ V, $R=10$ Ω.

### B3.

$$\begin{aligned}
x=2 &: \quad j = 5, \quad j' = 0 \\
x=0 &: \quad j = 17, \quad j' = -12
\end{aligned}$$

At $x=2$ the walker stands **5 hundred metres up (500 m) on flat ground** — the arrow vanishes, the altitude does not. At $x=0$ the walker is at 1700 m on ground sloping **down at 12 hundred metres per km**.

The walker feels the *tilt*, and the tilt is the second number. The failure this catches is the compact one: "$j'=0$ at the peak, so the altitude there is 0." The zero in the arrow column says where the ground is level; the zero in the value column is a different question entirely, and here it happens nowhere.

> **Answer**: $(5,\ 0)$ at $x=2$ and $(17,\ -12)$ at $x=0$; the slope is what is felt, and $j'=0$ says "level," never "zero height."

### B4.

$$S(t) = \int_0^t \left(6 - \frac{s}{2}\right) ds = 6t - \frac{t^2}{4}\ \text{liters}$$

| $t$ (min) | flow $r$ (L/min) | charge $S$ (L) |
|:---:|:---:|:---:|
| 0 | 6 | 0 |
| 6 | 3 | 27 |
| 12 | 0 | 36 |

At $t=6$ the battery is still **filling** ($r = 3 > 0$). At $t=12$ the flow has reached $0$ — the charger has stopped — while the charge sits at its maximum, 36 L. The charge is never negative: $S(t) = t\left(6 - \frac{t}{4}\right) > 0$ on the whole interval.

The wrong reading is "the rate hit zero, so the battery is empty." Zero flow and zero level are different axes, and at $t=12$ they are at opposite extremes.

> **Answer**: $S(t) = 6t - \frac{t^2}{4}$; filling at $t=6$; flat flow but maximal charge (36 L) at $t=12$; $S>0$ throughout.

## Intermediate Drills

### I1.

**I1.1** $\dfrac{B(31)-B(30)}{31-30} = \dfrac{900}{31} - 30 = 29.032 - 30 = -0.968$ thousand units per dollar.

**I1.2** $\dfrac{dB}{dp} = -\dfrac{900}{p^2}$, so at $p=30$: $-\dfrac{900}{900} = -1.000$ exactly. The secant gave $-0.968$ — the estimate is *smaller in size* than the tangent, because the secant is drawn between two points and the curve steepens as the price rises. The *order* is what matters here: differentiate first, then watch the estimate approach the answer. Taken the other way — estimate first, then call the estimate "the rate" — the number $-0.968$ gets quoted as exact, and the error of $0.032$ becomes invisible.

**I1.3** At $p=60$: $-\dfrac{900}{3600} = -\dfrac{1}{4}$. Doubling the price did **not** halve the rate — it quartered it. The rate carries a $p^{-2}$, not a $p^{-1}$, so every doubling divides by four.

**I1.4** Right at every $p$: "each extra dollar of price lowers monthly sales by about $\frac{900}{p^2}$ thousand units." Right only at $p=30$: "each extra dollar costs about 1 thousand units." Local data do not travel.

> **Answer**: $-0.968$, then exactly $-1$; second exactly $-\frac14$; doubling the price quarters the rate.

### I2.

**I2.1**
$$C'(x) = \frac{x^2}{4} - \frac{24}{x^2} = \frac{x^4 - 96}{4x^2}$$

**I2.2** The sign of $C'$ is the sign of the numerator alone, so $x^4 = 96$ and
$$x = 96^{1/4} = \left(16 \cdot 6\right)^{1/4} = 2\sqrt[4]{6} \approx 3.130\ \text{hundred boxes}.$$

**I2.3** $C''(x) = \frac{x}{2} + \frac{48}{x^3}$, which is positive at $x = 2\sqrt[4]{6}$ (both terms are positive), so this is a minimum. By comparison, in thousand dollars:

| $x$ | 4 | $2\sqrt[4]{6}\approx3.13$ | 6 | 12 |
|:---:|:---:|:---:|:---:|:---:|
| $C(x)$ | $\frac{34}{3}\approx 11.33$ | $10.223$ | 22 | 146 |

The comparison alone only tells you that 4 beats 6 and 12 — it cannot certify a minimum between grid points. It is the derivative's *sign change* that certifies the minimum, and the table merely confirms it.

**I2.4** At small $x$ the changeover term dominates the derivative ($-\frac{24}{x^2}$ is huge and negative), so $C'$ is negative and the cost **falls** as the lot grows. At large $x$ the machine-time term $\frac{x^2}{4}$ dominates and $C'$ is positive. The two terms trade control exactly where the numerator $x^4-96$ changes sign — which is why the optimum is a balance point, not a corner of the feasible range.

> **Answer**: $x^\* = 2\sqrt[4]{6} \approx 3.13$ hundred boxes, a minimum; the changeover term rules at small $x$, the machine-time term at large $x$.

### I3.

**I3.1** Factor first: $g(x) = (x-2)^2(x+4)$. Then three independent rows:

$$\begin{array}{c|c}
\text{row} & \text{zeros} \\
\hline
g(x)=0 & x=-4,\quad x=2\ (\text{double}) \\
g'(x)=3(x-2)(x+2)=0 & x=-2,\quad x=2 \\
g''(x)=6x=0 & x=0
\end{array}$$

**I3.2** At $x=2$ the value and the arrow vanish *together*, because $x=2$ is a **double** zero: the graph descends, kisses the axis, and climbs away ($g''(2)=12>0$ confirms it turns upward). At $x=-4$ the value vanishes while the arrow does not ($g'(-4)=36$): a crossing. So $g=0$ and $g'=0$ are two separate claims that happen to share a location here — the value tells you the height, the arrow tells you which way the curve is travelling, and one can be zero while the other is not.

**I3.3** $g''(x) = 6x$, so the second derivative vanishes at $x=0$, where $g(0) = 16$ — comfortably positive. A zero of $g''$ reports a change in *bending*, never a height: it says nothing at all about where $g$ sits.

**I3.4** At $x=-1$: $g(-1) = 27 > 0$ but $g'(-1) = -9 < 0$. Two sentences, in order — "the graph sits at 27, above the axis," then "it is heading down at 9 per unit." A sign-only reader hears "negative derivative" and concludes "negative value," which reverses the truth here.


### I4.

**I4.1** Two links, each carrying its own units:

$$\frac{dm}{dd} = 1600\ \frac{\text{kg}}{\text{m}},\qquad
\frac{dK}{dm} = \frac{2}{5} + \frac{m}{50000}\ \frac{\$}{\text{kg}}$$

Chained, with the kg cancelling:
$$\frac{dK}{dd} = \left(\frac{2}{5} + \frac{m}{50000}\right)\cdot 1600 = 640 + \frac{256}{5}d\ \frac{\$}{\text{m}}$$

**I4.2** At $d=5$: $640 + 256 = 896$ \$/m. At $d=10$: $640 + 512 = 1152$ \$/m. The inner link is *constant* — 1600 kg per metre, forever — yet the chained rate grows. The outer link is evaluated at the *current* mass, and the current mass keeps climbing: a constant link multiplied by a moving one gives a moving answer.

**I4.3** Second route — substitute first, then differentiate:
$$K(d) = \frac{2}{5}(1600d) + \frac{(1600d)^2}{100000} = 640d + \frac{256}{5}d^2
\quad\Longrightarrow\quad
\frac{dK}{dd} = 640 + \frac{512}{5}d$$

The same expression as I4.1, so at $d=5$ both give 896.

**I4.4** Route one differentiates in $d$ with the mass *treated as a value* $m(d)$; route two eliminates the intermediate letter entirely. The failure is mixing them: differentiating $K$ in $d$ while holding $m$ frozen returns $\frac{dK}{dd} = \frac25$ — the rate for a pile whose mass never grows. The chain rule is exactly the statement that the frozen letter must move with $d$, and the kg/m link is the record of how fast.

> **Answer**: $\dfrac{dK}{dd} = 640 + \dfrac{256}{5}d$ \$/m — 896 at $d=5$, 1152 at $d=10$; the two routes agree because the mass link is exactly what converts \$/kg into \$/m.

> **Answer**: $g=(x-2)^2(x+4)$; a double zero at $x=2$ (value and arrow both zero) against a simple zero at $x=-4$ (value zero, arrow 36); $g''=6x$ vanishes at $x=0$ where $g=16$, and predicts no height.

## Advanced Drills

### A1.

**A1.1** With $f = x^4+ax^3+bx^2$:

$$f'(x) = 4x^3+3ax^2+2bx,\qquad f''(x)=12x^2+6ax+2b$$

Both conditions at $x=2$ give a linear system:
$$\begin{cases}
32 + 12a + 4b = 0 & \text{(flat at } x=2) \\
48 + 12a + 2b = 0 & \text{(concavity flips at } x=2)
\end{cases}$$

Subtracting gives $2b = 16$, so $b = 8$; then $12a = -32-32 = -64$, so $a = -\frac{16}{3}$. One solution, and only one: two linear conditions on two unknowns with a nonzero coefficient matrix.

**A1.2** Substituting back:
$$f(x) = x^4 - \frac{16}{3}x^3 + 8x^2,\qquad f'(x) = 4x\left(x-2\right)^2,\qquad f''(x) = 4(x-2)(3x-2)$$

Critical points: $x=0$ and $x=2$. Classification by the *sign* of $f'$: to the left of $0$ it is negative, to the right it is positive ($f'(x) = 4x(x-2)^2$, and $(x-2)^2 \ge 0$). So $x=0$ is a local **minimum**, with $f(0) = 0$. At $x=2$ the factor $(x-2)^2$ does not change sign, so $f'$ is positive on both sides: $x=2$ is **not** an extremum.

**A1.3** Immediately left of $2$: $f' > 0$. Immediately right of $2$: $f' > 0$ — the arrow never switches. Meanwhile $f''(x) = 4(x-2)(3x-2)$ is negative just left of $2$ and positive just right of it: concavity flips. So the curve keeps climbing while its bending reverses — a stationary inflection, sitting at $f(2) = \frac{16}{3}$.

**A1.4** The arrow reports **direction of travel**; concavity reports **which way the curve bends**. Neither reports whether a turn occurs — that requires a *sign change* of the arrow. The student substituted one zero for another: because $f'(2)=0$ and $f''$ changes sign, they concluded "the mountain becomes a valley," when in fact $x=2$ is a shelf on a continuing staircase. The check that would have caught it: test the sign of $f'$ at $x=2\pm\varepsilon$ before classifying anything.

> **Answer**: $(a,b) = \left(-\frac{16}{3},\,8\right)$, forced; $f'=4x(x-2)^2$, $f''=4(x-2)(3x-2)$; local min at $x=0$ ($f=0$); stationary inflection at $x=2$ with $f(2)=\frac{16}{3}$; the arrow is what classifies, and it does not change sign at $2$.

### A2.

**A2.1** Three links:

$$\frac{dq}{dP} = -5\ \frac{\text{waffles}}{\$},\qquad
\frac{dw}{dq} = \frac{1}{40}\ \frac{\text{batch}}{\text{waffle}},\qquad
\frac{dG}{dw} = 2w\ \frac{\text{therm}}{\text{batch}}$$

Chained (waffles and batches both cancel):
$$\frac{dG}{dP} = 2w\cdot\frac{1}{40}\cdot(-5) = -\frac{w}{4}\ \frac{\text{therm}}{\$},\qquad w = \frac{400-5P}{40}$$

**A2.2** At $P=40$: $q=200$, $w=5$, so $\frac{dG}{dP} = -\frac{5}{4} = -1.25$ therms per dollar. At $P=60$: $q=100$, $w=\frac52$, giving $-\frac{5}{8} = -0.625$. At $P=80$: $q=0$, $w=0$, giving $0$. The magnitude halves each time the price rises by 20 dollars, because the batch count halves and $\frac{dG}{dw}$ is linear in $w$. The sign never flips inside the model — it reaches zero exactly where sales dry up.

**A2.3** Eliminate the intermediates:
$$w = \frac{400-5P}{40} = 10 - \frac{P}{8}
\quad\Longrightarrow\quad
G(P) = 2 + \left(10-\frac{P}{8}\right)^2 = \frac{P^2}{64} - \frac{5P}{2} + 102$$

Then $G'(P) = \frac{P}{32} - \frac{5}{2}$, which gives $-\frac{5}{4}$, $-\frac{5}{8}$, and $0$ at the same three prices. The two routes agree at every point, not just at those three.

**A2.4** From $G'(P) = \frac{P}{32}-\frac52$: for $P < 80$ the derivative is negative, so **raising the price reduces the gas bill**. At $P=80$ it is zero — the bill stops responding, because there are no waffles left to bake and the price axis no longer reaches the gas axis at all. Notice what this does *not* say: it says nothing about profit, only about the therm bill.

> **Answer**: $\frac{dG}{dP} = -\frac{w}{4}$ with $w=\frac{400-5P}{40}$; $-1.25$, $-0.625$, $0$ at $P=40,60,80$; $G(P)=\frac{P^2}{64}-\frac{5P}{2}+102$; below \$80 a price rise cuts the bill, and at \$80 it stops mattering.

### A3.

**A3.1** Five coefficients, four conditions, so one parameter should survive. Imposing $F(1)=4$, $F'(1)=0$, $F''(1)=0$:

$$F'(x) = 4x^3+3ax^2+2bx+c,\qquad F''(x)=12x^2+6ax+2b$$

$$\begin{cases}
1 + a + b + c + d = 4 \\
4 + 3a + 2b + c = 0 \\
12 + 6a + 2b = 0
\end{cases}$$

Solving for $(a,b,d)$ in terms of $c$ gives
$$a = \frac{c}{3} - \frac{8}{3},\qquad b = 2 - c,\qquad d = \frac{11}{3} - \frac{c}{3}.$$

The free parameter is the **linear coefficient $c$**. Every member of the family is
$$F(x) = x^4 + \left(\frac{c}{3}-\frac{8}{3}\right)x^3 + (2-c)x^2 + cx + \frac{11-c}{3},$$
and in every member
$$F'(x) = (x-1)^2(4x + c).$$

**A3.2** The quadratic term vanishes when $c = 2$:
$$F(x) = x^4 - 2x^3 + 2x + 3.$$

Checks by substitution: $F(1) = 1-2+2+3 = 4$; $F'(x) = 4x^3-6x^2+2$, so $F'(1) = 4-6+2 = 0$; $F''(x) = 12x^2-12x = 12x(x-1)$, so $F''(1) = 0$; and $F(x) \ne$ constant since $F'(0) = 2 \ne 0$.

**A3.3** $F'(1) = 0$, $F''(1) = 0$, and
$$F'''(x) = 24x - 12,\qquad F'''(1) = 12 \ne 0.$$

$F''$ has a zero of *odd* order at $x=1$ (order one), which is exactly what forces a sign change: $F''$ goes from negative to positive through $x=1$. A vanishing second derivative alone proves nothing — $F''=0$ is also satisfied by a parabola's extremum. The odd-order third derivative is the witness that the sign really flips.

**A3.4** Take $c=-4$: then $a=-4$, $b=6$, $d=5$, so
$$F(x) = x^4-4x^3+6x^2-4x+5 = (x-1)^4 + 4.$$
Here $F'''(1) = 24-12-16 = 0$ as well: the derivatives vanish to order three. And $F''(x) = 12(x-1)^2 \ge 0$ on both sides — the concavity does **not** flip. So $x=1$ is *not* an inflection for this member; it is a fourth-order flat point. The family's requirement "$F'''(1)\ne 0$" is what excludes this member: a stationary inflection needs the first nonzero higher derivative to be of **odd** order, and here the first nonzero one is $F^{(4)} = 24$, which is even.

**A3.5** For the pinned $F$: $F'(x) = 2(x-1)^2(2x+1)$, so the critical points are $x=1$ and $x=-\frac12$. At $x=-\frac12$ the arrow changes from negative to positive: a local **minimum**, with $F\!\left(-\frac12\right) = \frac{37}{16}$. At $x=1$ the arrow does not change sign (positive on both sides), so there is no extremum. "$F$ is flat at $x=1$" and "$F$ is increasing through $x=1$" coexist because flatness is a statement about the *instantaneous* rate being zero, while increasing is a statement about the rate on *neighbourhoods* — a curve can pause without turning around.

**A3.6** Each equation "$F^{(k)}(x_0)=0$" costs one degree of freedom; the height condition $F(1)=4$ costs one more. Four independent constraints on five coefficients leave $5-4=1$ parameter — exactly the $c$ found in A3.1. The general principle: **a stationary inflection is two conditions, not one** (the arrow vanishes *and* the second derivative vanishes), so it consumes two degrees of freedom before any height or any other feature is fixed.

The degenerate member is where the lesson bites twice: at $c=-4$ all three of $F'$, $F''$, $F'''$ vanish, so "$F''(1)=0$" is satisfied while the concavity never flips. **A count of satisfied equations never proves a geometric property; the lowest non-vanishing derivative has to be checked, and it has to be odd.**

> **Answer**: $a=\frac{c}{3}-\frac83$, $b=2-c$, $d=\frac{11-c}{3}$ with $c$ free; pinned member $F = x^4-2x^3+2x+3$; $F'''(1)=12\ne0$ proves the flip; $c=-4$ gives $(x-1)^4+4$ with $F'''=0$ and no inflection; one critical point at $x=-\frac12$ (min, $\frac{37}{16}$) and a non-extremal flat point at $x=1$.

### A4.

**A4.1** The structure error: the student **inverted one link and then multiplied**, instead of **multiplying and then inverting**. The correct chain multiplies three rates:

$$\frac{dC}{dh} = \frac{dC}{dw}\cdot\frac{dw}{dh}.$$

The submitted expression computes $\dfrac{dw/dh}{dC/dw}$, which is $\dfrac{dw}{dh}\cdot\dfrac{dw}{dC}$ — the numerator is not a reciprocal, so the two links were never properly composed.

**A4.2** Dimensions of the submitted expression:
$$\frac{\text{widgets/hour}}{\$/\text{widget}} = \frac{\text{widgets}^2}{\text{hour}\cdot\$}.$$

That is not dollars per hour, nor anything else anyone wanted. The dimensional check fails immediately, which is why printing units belongs at the *start* of the computation, not the end.

**A4.3** Correct chain: $\frac{dw}{dh} = 4$ widgets per hour, $\frac{dC}{dw} = \frac{w}{25}+3$ dollars per widget, so
$$\frac{dC}{dh} = 4\left(\frac{w}{25}+3\right) = \frac{4w}{25}+12\ \frac{\$}{\text{hour}}.$$

Second route — substitute $w=4h$ first:
$$C(h) = 60 + 12h + \frac{16h^2}{50} = 60+12h+\frac{8h^2}{25}
\quad\Longrightarrow\quad
\frac{dC}{dh} = 12 + \frac{16h}{25}.$$

At $h=5$ (so $w=20$): the chain gives $\frac{80}{25}+12 = \frac{16}{5}+12 = \frac{76}{5} = 15.20$, and the composite gives $12+\frac{80}{25} = 15.20$. Agreement.

**A4.4** The submitted $\$1.05$ carries units of widgets²/(hour·\$), while the correct $\$15.20$ carries \$/hour. Comparing them "as small" is comparing a reciprocal-shaped quantity with a rate-shaped one; the numbers happen to sit near each other and mean nothing alike. This is exactly the failure the unit lens exists to catch: *a wrong unit is a wrong answer, however plausible the magnitude.*

**A4.5** A true repair keeps the student's two numbers but multiplies them instead of dividing:
> "One hour adds 4 widgets, and at that point each widget costs $\frac{20}{25}+3 = \$3.80$, so one hour adds $4 \times 3.80 = \$15.20$ to the bill."

The student's ratio $\dfrac{dw/dh}{dC/dw} = \dfrac{4}{3+w/25}$ is not a useful intermediate at all; its units (widgets² per dollar-hour) show that no correction to the *number* can save it. The repair must replace the operation — division becomes multiplication — and then the check at $h=5$ lands on $\frac{76}{5}$ dollars per hour. Note the secondary lesson: the student's answer was off by a factor of $\frac{76/5}{20/19} = \frac{361}{25} \approx 14.4$, which is why "it looks small and reasonable" is never evidence.

> **Answer**: the error is inverting a link before composing; the submitted quantity is widgets²/(hour·\$); correct $\frac{dC}{dh} = \frac{4w}{25}+12 = 12+\frac{16h}{25}$ \$/h, giving \$$15.20$ at $h=5$; a comparison of \$1.05 with \$15.20 is meaningless until the units match.

---

---

## Answer Check

| Problem | Answer |
|:---:|:---|
| B1 | $-\frac{1}{30}$ min per km/h $= -2$ s per km/h — the 2-second sentence |
| B2 | $+24$ W/V and $-144$ W/Ω at $V=120$ V, $R=10$ Ω |
| B3 | $(5,0)$ at $x=2$; $(17,-12)$ at $x=0$ — the tilt is what is felt |
| B4 | $S=6t-\frac{t^2}{4}$; filling at $t=6$; charge peaks (36 L) at $t=12$ |
| I1 | $-0.968$, then exactly $-1$; at $p=60$ exactly $-\frac14$ — doubling quarters the rate |
| I2 | $x^*=2\sqrt[4]{6}\approx3.13$ (hundred boxes); $C(x^*)\approx10.22$ thousand \$; minimum by sign change |
| I3 | $g=(x-2)^2(x+4)$; double zero at 2 (arrow also 0) vs simple zero at $-4$ ($g'=36$); $g''=6x$, zero at 0 where $g=16$ |
| I4 | $\frac{dK}{dd}=640+\frac{256}{5}d$; 896 at $d=5$, 1152 at $d=10$; both routes agree |
| A1 | $(a,b)=\left(-\frac{16}{3},8\right)$ forced; min at $x=0$ ($f=0$); stationary inflection at $x=2$, $f(2)=\frac{16}{3}$ |
| A2 | $\frac{dG}{dP}=-\frac{w}{4}$, $w=\frac{400-5P}{40}$; $-1.25,-0.625,0$ at $P=40,60,80$; $G=\frac{P^2}{64}-\frac{5P}{2}+102$ |
| A3 | $a=\frac{c}{3}-\frac83$, $b=2-c$, $d=\frac{11-c}{3}$; pinned $F=x^4-2x^3+2x+3$ with $F'''(1)=12$; $c=-4$ gives $(x-1)^4+4$, no inflection |
| A4 | Error: inverted a link before composing. Correct $\frac{dC}{dh}=12+\frac{16h}{25}$; \$15.20 at $h=5$ |
