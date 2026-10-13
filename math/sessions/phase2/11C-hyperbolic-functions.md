# Session 11C: Hyperbolic Functions — The Trigonometric Functions of a Hyperbola

**Phase 2 — Classical Techniques | 90 min**

*Prerequisites: 11A (trig foundations), 11B (identities, Euler's formula), 10A (exponentials & logarithms)*

> 💡 **Stuck?** Every problem has a collapsible **Hint** below it — click it only when you need a nudge.

> **Source.** Every example and drill below is drawn from Stewart, *Calculus*, Section 3.11 (Hyperbolic Functions). Each item cites its example or exercise number in that section. The definitions, the identity list, and the derivative tables are Stewart's; the graphs redraw Stewart's Figures 1–10.

---

## Part A: Definitions — The Hyperbola's Trigonometry

---

## Example 1: The Analogy — Circle vs Hyperbola (§3.11, Figures 6–7)

The unit circle is $x^2 + y^2 = 1$. The **unit hyperbola** is $x^2 - y^2 = 1$.

The point $(\cos t,\ \sin t)$ runs around the circle because $\cos^2 t + \sin^2 t = 1$. Stewart defines the hyperbolic functions so that the point $(\cosh t,\ \sinh t)$ runs along the right branch of the hyperbola because $\cosh^2 t - \sinh^2 t = 1$ and $\cosh t \ge 1$ (Figures 6 and 7). The number $t$ is not an angle: it equals **twice the area** of the shaded sector — the same area interpretation that radians give on the circle.

**The parallel that matters:**
- Every point on the circle satisfies $\cos^2 t + \sin^2 t = 1$.
- Every point on the hyperbola satisfies $\cosh^2 t - \sinh^2 t = 1$.

![Unit circle vs unit hyperbola — same parametrization idea]({{graph:11c-1-analogy}})

*Graph 11C-1: Left — the unit circle $x^2+y^2=1$ with the point $(\cos t,\sin t)$. Right — the unit hyperbola $x^2-y^2=1$ with the point $(\cosh t,\sinh t)$. On both sides the shaded sector has area $t/2$.*

> **Geometric insight**: The minus sign in $x^2 - y^2 = 1$ is the whole story. It turns a circle into a hyperbola, and every identity in 11C inherits that single sign change.

---

## Example 2: Definitions via $e^x$, and the Values They Give (§3.11 Definitions box, Ex 1–10)

Stewart defines all six functions from the two exponentials $e^x$ and $e^{-x}$:

$$\cosh x = \frac{e^x + e^{-x}}{2} \qquad \sinh x = \frac{e^x - e^{-x}}{2}$$

$$\tanh x = \frac{\sinh x}{\cosh x}, \qquad \operatorname{sech} x = \frac{1}{\cosh x}, \qquad \operatorname{csch} x = \frac{1}{\sinh x}, \qquad \coth x = \frac{\cosh x}{\sinh x}.$$

(Read: "kosh", "sinch", "tanch", "setch", "cosetch", "cotanch".)

**Values straight from the definition** (Exercises 1–6):

$$\sinh 0 = \frac{1-1}{2} = 0, \qquad \cosh 0 = \frac{1+1}{2} = 1, \qquad \tanh 0 = 0.$$

$$\cosh(\ln 5) = \frac{5 + 1/5}{2} = \frac{13}{5}, \qquad \sinh(\ln 4) = \frac{4 - 1/4}{2} = \frac{15}{8}.$$

**Rewriting in terms of $e^x$** (Exercises 7–10): add and subtract the two definitions to get the no-$i$ twin of Euler's formula (🔗 11B),

$$e^x = \cosh x + \sinh x, \qquad e^{-x} = \cosh x - \sinh x.$$

Combine the two to convert any $a\,e^x + b\,e^{-x}$ back into $\cosh$ and $\sinh$:

$$8\sinh x + 5\cosh x = 8\cdot\frac{e^x - e^{-x}}{2} + 5\cdot\frac{e^x + e^{-x}}{2} = \frac{13}{2}e^x - \frac{3}{2}e^{-x}.$$

$$\sinh(\ln x) = \frac{x - 1/x}{2} = \frac{x^2 - 1}{2x}.$$

**Parity** (Exercises 11–12): $\cosh(-x) = \cosh x$ (even), $\sinh(-x) = -\sinh x$ (odd), and $\tanh$ is odd.

![e^x split into its even part (cosh) and odd part (sinh)]({{graph:11c-2-even-odd}})

*Graph 11C-2: Every function splits into an even part $\frac{f(x)+f(-x)}{2}$ and an odd part $\frac{f(x)-f(-x)}{2}$. For $f(x)=e^x$ those halves are exactly $\cosh x$ and $\sinh x$.*

> **Geometric insight**: $\cosh$ is the even half of $e^x$; $\sinh$ is the odd half. Removing the $i$ from Euler's formula unbounds the functions: $\sinh$ and $\cosh$ grow exponentially, while $\sin$ and $\cos$ stay trapped in $[-1,1]$.

---

## Part B: Identities — The Parallel Universe

---

## Example 3: The Core Identity and Its Family (§3.11 Ex 1, Identities box, Ex 11–23)

Stewart's **Example 1** proves the core identity directly from the definitions:

$$\cosh^2 x - \sinh^2 x = \left(\frac{e^x+e^{-x}}{2}\right)^2 - \left(\frac{e^x-e^{-x}}{2}\right)^2 = \frac{e^{2x}+2+e^{-2x}}{4} - \frac{e^{2x}-2+e^{-2x}}{4} = \frac{4}{4} = 1.$$

Divide both sides by $\cosh^2 x$ to get Example 1(b), and by $\sinh^2 x$ to get Exercise 17:

$$1 - \tanh^2 x = \operatorname{sech}^2 x, \qquad \coth^2 x - 1 = \operatorname{csch}^2 x.$$

**Every 11B trig identity has a hyperbolic twin.** Stewart's identity box and Exercises 11–23 give the pattern (**Osborne's rule**): **a minus sign in the trig column becomes a plus in the hyperbolic column exactly when a product of two sines is involved.**

| 11B (trig) | 11C (hyperbolic) | §3.11 |
|:---|:---|:---:|
| $\cos^2 t + \sin^2 t = 1$ | $\cosh^2 x - \sinh^2 x = 1$ | Ex 1 |
| $\cos 2t = \cos^2 t - \sin^2 t$ | $\cosh 2x = \cosh^2 x + \sinh^2 x$ | Ex 20 |
| $\sin 2t = 2\sin t\cos t$ | $\sinh 2x = 2\sinh x\cosh x$ | Ex 19 |
| $1 + \tan^2 t = \sec^2 t$ | $1 - \tanh^2 x = \operatorname{sech}^2 x$ | Ex 1 |
| $\cot^2 t + 1 = \csc^2 t$ | $\coth^2 x - 1 = \operatorname{csch}^2 x$ | Ex 17 |
| $\cos(A+B) = \cos A\cos B - \sin A\sin B$ | $\cosh(x+y) = \cosh x\cosh y + \sinh x\sinh y$ | Ex 16 |

**Addition formulas from $e^{x+y} = e^x e^y$** (Exercises 15, 16): multiply $(\cosh x + \sinh x)(\cosh y + \sinh y)$ and match the even and odd parts:

$$\sinh(x+y) = \sinh x\cosh y + \cosh x\sinh y,$$
$$\cosh(x+y) = \cosh x\cosh y + \sinh x\sinh y.$$

Divide the two to get Stewart's Exercise 18:

$$\tanh(x+y) = \frac{\tanh x + \tanh y}{1 + \tanh x\,\tanh y}.$$

**Double angle** (Exercises 19, 20): $\sinh 2x = 2\sinh x\cosh x$ and $\cosh 2x = \cosh^2 x + \sinh^2 x = 2\cosh^2 x - 1 = 1 + 2\sinh^2 x$.

> **Geometric insight**: Trig identities live on a circle where $\sin^2 + \cos^2 = 1$; hyperbolic identities live on a hyperbola where $\cosh^2 - \sinh^2 = 1$. One sign carries all the difference.

---

## Example 4: Graphs and Limits (§3.11 Figures 1–3, Ex 26–27)

Stewart builds the graphs in Figures 1–3 by adding the two pieces $\frac12 e^x$ and $\pm\frac12 e^{-x}$:

| function | parity | range | special values | behavior |
|:---:|:---:|:---:|:---:|------|
| $\cosh x$ | even | $[1, \infty)$ | $\cosh 0 = 1$ | grows like $\frac{1}{2}e^x$ |
| $\sinh x$ | odd | $\mathbb{R}$ | $\sinh 0 = 0$ | grows like $\pm\frac{1}{2}e^{\pm x}$ |
| $\tanh x$ | odd | $(-1, 1)$ | $\tanh 0 = 0$ | $\to \pm 1$ as $x \to \pm\infty$ |
| $\operatorname{sech} x$ | even | $(0, 1]$ | $\operatorname{sech} 0 = 1$ | $\to 0$ as $x\to\pm\infty$ |
| $\operatorname{csch} x$ | odd | $\mathbb{R}\setminus\{0\}$ | — | blows up at $x=0$ |
| $\coth x$ | odd | $(-\infty,-1)\cup(1,\infty)$ | — | blows up at $x=0$; $\to\pm1$ |

![cosh x — even, dips to 1 at the origin]({{graph:11c-3a-cosh}})

![sinh x — odd, through the origin]({{graph:11c-3b-sinh}})

![tanh x — odd, squeezed between −1 and 1]({{graph:11c-3c-tanh}})

![sech x — even, range between 0 and 1]({{graph:11c-3d-sech}})

![csch x — odd, asymptote at x = 0]({{graph:11c-3e-csch}})

![coth x — odd, asymptotes x = 0 and y = ±1]({{graph:11c-3f-coth}})

*Graphs 11C-3a–f: The six hyperbolic functions, one graph each — $\cosh x$ (even, dips to 1 at the origin), $\sinh x$ (odd, through the origin), $\tanh x$ (odd, between $-1$ and $1$), and their reciprocals $\operatorname{sech} x$, $\operatorname{csch} x$, $\coth x$ (asymptote at $x=0$).*

**Limits from the definitions** (Exercise 27): as $x\to\infty$, $e^{-x}\to 0$, so

$$\lim_{x\to\infty}\tanh x = \lim_{x\to\infty}\frac{e^x - e^{-x}}{e^x + e^{-x}} = 1, \qquad \lim_{x\to-\infty}\tanh x = -1, \qquad \lim_{x\to\infty}\operatorname{sech} x = 0.$$

> **Geometric insight**: Only $\tanh$ (and $\coth$) are bounded. The graph of $\tanh$ is a smooth "S" — two horizontal asymptotes glued by one vertical step.

---

## Part C: Calculus and Applications (🔗 14A, 16A)

---

## Example 5: Derivatives of the Hyperbolic Functions (§3.11 Table 1, Ex 2, Ex 28)

Stewart differentiates the definitions directly — for instance

$$\frac{d}{dx}(\sinh x) = \frac{d}{dx}\left(\frac{e^x - e^{-x}}{2}\right) = \frac{e^x + e^{-x}}{2} = \cosh x,$$

and collects the results in **Table 1**:

$$\frac{d}{dx}\sinh x = \cosh x, \qquad \frac{d}{dx}\cosh x = \sinh x, \qquad \frac{d}{dx}\tanh x = \operatorname{sech}^2 x,$$

$$\frac{d}{dx}\operatorname{csch} x = -\operatorname{csch} x\,\coth x, \qquad \frac{d}{dx}\operatorname{sech} x = -\operatorname{sech} x\,\tanh x, \qquad \frac{d}{dx}\coth x = -\operatorname{csch}^2 x.$$

**Example 2 in the text**: with $y = \cosh\sqrt{x}$ and the Chain Rule,

$$\frac{dy}{dx} = \sinh\sqrt{x}\cdot\frac{d}{dx}\sqrt{x} = \frac{\sinh\sqrt{x}}{2\sqrt{x}}.$$

**More from Exercises 35–46**:

$$\frac{d}{dx}\cosh 3x = 3\sinh 3x, \qquad \frac{d}{dx}\sinh(x^2) = 2x\cosh(x^2), \qquad \frac{d}{dx}\sinh^2 x = 2\sinh x\cosh x = \sinh 2x.$$

$$\frac{d}{dx}\tanh\sqrt{x} = \frac{\operatorname{sech}^2\sqrt{x}}{2\sqrt{x}}, \qquad \frac{d}{dx}\operatorname{sech}(\tanh x) = -\operatorname{sech}(\tanh x)\,\tanh(\tanh x)\,\operatorname{sech}^2 x.$$

**Compare with trig**: $\frac{d}{dx}\cos x = -\sin x$ carries a minus; $\frac{d}{dx}\cosh x = \sinh x$ does not. The hyperbola's sign change removes the minus from the circular pair — that is the payoff of the hyperbolic construction.

> **Geometric insight**: These six formulas are the "native" answers to the hyperbolic integrals $\int \cosh x\,dx = \sinh x + C$ and $\int \operatorname{sech}^2 x\,dx = \tanh x + C$, which 16A meets again through trig substitution.

---

## Example 6: Inverse Hyperbolic Functions — Logarithmic Forms (§3.11 Ex 3, Formulas 3–5)

$\sinh$ and $\tanh$ are one-to-one (Figures 1 and 3); $\cosh$ is not, so Stewart restricts its domain to $[0,\infty)$ (Figure 2) before inverting. This gives **Formulas 2**:

$$y = \sinh^{-1} x \iff \sinh y = x, \quad y = \cosh^{-1} x \iff \cosh y = x \text{ and } y \ge 0, \quad y = \tanh^{-1} x \iff \tanh y = x.$$

**Stewart's Example 3** derives the logarithmic form of $\sinh^{-1}$. Let $y = \sinh^{-1} x$, so $x = \sinh y = \frac{e^y - e^{-y}}{2}$. Multiply by $2e^y$:

$$e^{2y} - 2x\,e^y - 1 = 0.$$

This is a quadratic in $e^y$, so $e^y = x \pm \sqrt{x^2+1}$. Since $e^y > 0$ while $x - \sqrt{x^2+1} < 0$, the minus sign is inadmissible, and

$$\sinh^{-1} x = \ln\left(x + \sqrt{x^2+1}\right), \qquad x \in \mathbb{R}.$$

The same trick gives **Formulas 4 and 5** (Exercises 30–31):

$$\cosh^{-1} x = \ln\left(x + \sqrt{x^2-1}\right), \quad x \ge 1; \qquad \tanh^{-1} x = \frac{1}{2}\ln\left(\frac{1+x}{1-x}\right), \quad -1 < x < 1.$$

![Inverse hyperbolic functions — logarithmic graphs]({{graph:11c-4-inverse}})

*Graph 11C-4: $\operatorname{arsinh} x$ (all reals), $\operatorname{arcosh} x$ (only $x\ge1$), $\operatorname{artanh} x$ (only $|x|<1$, blows up at $\pm1$).*

> **Geometric insight**: Unlike $\arcsin$ and $\arccos$ (bounded because $\sin$ and $\cos$ are bounded), $\operatorname{arsinh}$ is defined everywhere — because $\sinh$ grows without bound. Domain restrictions appear only where the original function is bounded: $\cosh \ge 1$ and $|\tanh| < 1$.

---

## Example 7: Derivatives of the Inverse Hyperbolic Functions (§3.11 Table 6, Ex 4, Ex 5)

Stewart collects the results in **Table 6**:

$$\frac{d}{dx}\sinh^{-1} x = \frac{1}{\sqrt{1+x^2}}, \qquad \frac{d}{dx}\cosh^{-1} x = \frac{1}{\sqrt{x^2-1}}, \qquad \frac{d}{dx}\tanh^{-1} x = \frac{1}{1-x^2},$$

$$\frac{d}{dx}\operatorname{csch}^{-1} x = -\frac{1}{|x|\sqrt{x^2+1}}, \qquad \frac{d}{dx}\operatorname{sech}^{-1} x = -\frac{1}{x\sqrt{1-x^2}}, \qquad \frac{d}{dx}\coth^{-1} x = \frac{1}{1-x^2}.$$

**Stewart's Example 4** proves the first formula. Let $y = \sinh^{-1} x$, so $\sinh y = x$. Differentiate implicitly:

$$\cosh y\,\frac{dy}{dx} = 1 \quad\Rightarrow\quad \frac{dy}{dx} = \frac{1}{\cosh y} = \frac{1}{\sqrt{1+\sinh^2 y}} = \frac{1}{\sqrt{1+x^2}},$$

using $\cosh^2 y - \sinh^2 y = 1$ and $\cosh y \ge 0$.

**Stewart's Example 5** combines Table 6 with the Chain Rule:

$$\frac{d}{dx}\left[\tanh^{-1}(\sin x)\right] = \frac{1}{1-\sin^2 x}\cdot\cos x = \frac{\cos x}{\cos^2 x} = \sec x.$$

**More from Exercises 47–53**:

$$\frac{d}{dx}\sinh^{-1}(-2x) = \frac{-2}{\sqrt{1+4x^2}}, \qquad \frac{d}{dx}\tanh^{-1}(x^3) = \frac{3x^2}{1-x^6}.$$

> **Geometric insight**: These three derivative formulas are the native answers to $\int \frac{dx}{\sqrt{1+x^2}}$, $\int \frac{dx}{\sqrt{x^2-1}}$, and $\int \frac{dx}{1-x^2}$ — the integrals 16A handles by trig substitution. The hyperbolic route makes the answers immediate.

---

## Example 8: Applications — Catenary, Waves, and Terminal Velocity (§3.11 Figures 4–5, Ex 56–62)

**Catenary (Figure 4, Exercises 58–61).** A heavy flexible cable hanging between two points at the same height takes the shape $y = c + a\cosh(x/a)$, called a **catenary** (Latin *catena*, "chain"). Exercise 60 verifies that $y = \frac{T}{\rho g}\cosh\left(\frac{\rho g x}{T}\right)$ satisfies the hanging-cable equation

$$\frac{d^2 y}{dx^2} = \frac{\rho g}{T}\sqrt{1 + \left(\frac{dy}{dx}\right)^2}.$$

Exercise 59's telephone line $y = 20\cosh(x/20) - 15$ has slope $\sinh(x/20)$; at the right-hand pole, $x = 7$, the slope is $\sinh(0.35) \approx 0.357$.

![Catenary — the hanging-cable curve]({{graph:11c-5-catenary}})

*Graph 11C-5: The catenary $y = 3\cosh(x/3)$ with its minimum at $(0,3)$, compared with a parabola that matches it near the bottom — the catenary rises faster away from the center.*

**Water waves (Figure 5, Exercise 57).** A wave of length $L$ over water of depth $d$ moves at

$$v = \sqrt{\frac{gL}{2\pi}\tanh\left(\frac{2\pi d}{L}\right)}.$$

In deep water $d/L \to \infty$ and $\tanh \to 1$, so $v \approx \sqrt{gL/(2\pi)}$ — the depth drops out.

**Gateway Arch (Exercise 56).** The central curve is $y = 211.49 - 20.96\cosh(0.03291765\,x)$, $|x| \le 91.20$; at the center $x=0$ the height is $211.49 - 20.96 \approx 190.5$ m.

**Falling object (Exercise 62).** A falling object's velocity is modeled by $v(t) = \sqrt{\frac{mg}{k}}\tanh\left(t\sqrt{\frac{gk}{m}}\right)$. As $t\to\infty$, $\tanh \to 1$, so the terminal velocity is $\sqrt{mg/k}$.

> **Geometric insight**: "Where do hyperbolic functions appear?" — anything hanging under gravity (cosh), anything that saturates (tanh), and any quantity built from two opposing exponentials (sinh).

---

## Common Mistakes

### Mistake 1: $\cosh^2 x + \sinh^2 x = 1$

**Wrong.** Stewart's Example 1(a) gives $\cosh^2 x - \sinh^2 x = 1$. There is no "hyperbolic unit circle" — the points $(\cosh x, \sinh x)$ lie on the **hyperbola** $x^2 - y^2 = 1$.

### Mistake 2: $\cosh(x+y)$ with a minus sign

Exercise 16 gives $\cosh(x+y) = \cosh x\cosh y + \sinh x\sinh y$ — the sign is **plus**, unlike $\cos(A+B) = \cos A\cos B - \sin A\sin B$. Only $\cosh(x-y)$ has the minus.

### Mistake 3: Forgetting $\cosh x \ge 1$

$\cosh$ never goes below $1$ (Figure 2). So $\cosh x = 0$ and $\cosh x = \frac12$ have **no solutions**, while $\sinh x$ can equal anything.

### Mistake 4: Forgetting the domains of the inverses

Formula 4 needs $x \ge 1$; Formula 5 needs $|x| < 1$. $\sinh^{-1}$ is the only one defined on all of $\mathbb{R}$ (Figures 8–10).

### Mistake 5: Sign slips in the derivative tables

In Table 1 only $\sinh$ and $\cosh$ avoid a minus sign; the other four derivatives each carry one. In Table 6, $\coth^{-1}$ shares the formula $\frac{1}{1-x^2}$ with $\tanh^{-1}$.

---

## What We Just Did

```
(1) Hyperbolic = trig of the hyperbola x²−y²=1. (cosh t, sinh t) parametrize it just as
    (cos t, sin t) parametrize the circle. t = hyperbolic angle = 2 × sector area. (§3.11 Figs 6–7)
(2) Built from e^x: cosh x = (e^x+e^−x)/2, sinh x = (e^x−e^−x)/2. e^x = cosh x + sinh x. (§3.11 Ex 1–10)
(3) Core identity cosh²x − sinh²x = 1; its family, and the addition formulas for
    sinh(x+y), cosh(x+y), tanh(x+y). (§3.11 Ex 1, 15–20)
(4) Graphs and limits: cosh even ≥ 1, sinh/tanh odd, tanh → ±1. (§3.11 Figs 1–3, Ex 26–27)
(5) Derivatives (Table 1): sinh→cosh, cosh→sinh, tanh→sech²; the rest pick up minus signs. (§3.11 Ex 2, 28)
(6) Inverses (Formulas 3–5): arsinh x = ln(x+√(x²+1)); arcosh x = ln(x+√(x²−1)) for x≥1;
    artanh x = ½ln((1+x)/(1−x)) for |x|<1. (§3.11 Ex 3, 29–31)
(7) Inverse derivatives (Table 6): 1/√(1+x²), 1/√(x²−1), 1/(1−x²). (§3.11 Ex 4–5, 33–34)
(8) Applications: catenary y = a cosh(x/a); water-wave speed; Gateway Arch; terminal velocity. (§3.11 Ex 56–62)
```

---

## Basic Drills

> Pure fluency: definitions, values, identities, and the derivative tables. One clean move per item.

**D1.** (§3.11 #1) Find $\sinh 0$ and $\cosh 0$.

**D2.** (§3.11 #2) Find $\tanh 0$ and $\tanh 1$ (give $\tanh 1$ to three decimals).

**D3.** (§3.11 #3) Find $\cosh(\ln 5)$ exactly.

**D4.** (§3.11 #4) Find $\sinh(\ln 4)$ exactly.

**D5.** (§3.11 #5) Find $\operatorname{sech} 0$ and $\cosh^{-1} 1$.

**D6.** (§3.11 #6) Find $\sinh 1$ (three decimals) and $\sinh^{-1} 1$.

**D7.** (§3.11 #7) Write $8\sinh x + 5\cosh x$ in terms of $e^x$ and $e^{-x}$.

**D8.** (§3.11 #8) Write $2e^{2x} + 3e^{-2x}$ in terms of $\sinh 2x$ and $\cosh 2x$.

**D9.** (§3.11 #9) Write $\sinh(\ln x)$ as a rational function of $x$.

**D10.** (§3.11 #10) Write $\cosh(4\ln x)$ as a rational function of $x$.

**D11.** (§3.11 #11–12) Prove $\sinh(-x) = -\sinh x$ and $\cosh(-x) = \cosh x$.

**D12.** (§3.11 #13–14) Show $\cosh x + \sinh x = e^x$ and $\cosh x - \sinh x = e^{-x}$.

**D13.** (§3.11 #17) Prove $\coth^2 x - 1 = \operatorname{csch}^2 x$.

**D14.** (§3.11 #19–20) Prove $\sinh 2x = 2\sinh x\cosh x$ and $\cosh 2x = \cosh^2 x + \sinh^2 x$.

**D15.** (§3.11 #21) Show $\tanh(\ln x) = \dfrac{x^2-1}{x^2+1}$.

**D16.** (§3.11 #24) If $\tanh x = \frac{12}{13}$, find the other five hyperbolic functions at $x$.

**D17.** (§3.11 #25) If $\cosh x = \frac53$ and $x > 0$, find the other five hyperbolic functions at $x$.

**D18.** (§3.11 #27) Evaluate $\displaystyle\lim_{x\to\infty}\tanh x$ and $\displaystyle\lim_{x\to-\infty}\tanh x$.

**D19.** (§3.11 #35) Differentiate $f(x) = \cosh 3x$.

**D20.** (§3.11 #37) Differentiate $h(x) = \sinh(x^2)$.

**D21.** (§3.11 #41) Differentiate $f(x) = \tanh\sqrt{x}$.

**D22.** (§3.11 #47) Differentiate $f(x) = \sinh^{-1}(-2x)$.

**D23.** (§3.11 #48) Differentiate $g(x) = \tanh^{-1}(x^3)$.

**D24.** (§3.11 #65) At what point of $y = \cosh x$ does the tangent have slope $1$?

> Solutions: [Solutions](solutions/11C-solutions.md#basic-drill)

---

## Advanced Drills

> Chains two or three moves. Covers the identity proofs, the inverse formulas, and the applications.

**A1.** (§3.11 #15) Prove $\sinh(x+y) = \sinh x\cosh y + \cosh x\sinh y$ from the $e^x$ definitions.

**A2.** (§3.11 #16) Prove $\cosh(x+y) = \cosh x\cosh y + \sinh x\sinh y$ from the $e^x$ definitions.

**A3.** (§3.11 #18) Derive $\tanh(x+y) = \dfrac{\tanh x + \tanh y}{1 + \tanh x\,\tanh y}$.

**A4.** (§3.11 #22) Prove $\dfrac{1+\tanh x}{1-\tanh x} = e^{2x}$.

**A5.** (§3.11 #23) Prove $(\cosh x + \sinh x)^n = \cosh nx + \sinh nx$ for any real number $n$.

<details>
<summary>💡 Hint</summary>

Write $\cosh x + \sinh x = e^x$ and raise both sides to the $n$-th power.

</details>

**A6.** (§3.11 #28) Prove the Table 1 formula for $\operatorname{sech}$: $\dfrac{d}{dx}\operatorname{sech} x = -\operatorname{sech} x\tanh x$.

**A7.** (§3.11 #29) Give an alternative solution to Example 3: set $y = \sinh^{-1} x$, then use $\cosh^2 y - \sinh^2 y = 1$ to reach the logarithmic form.

**A8.** (§3.11 #30) Prove Formula 4: $\cosh^{-1} x = \ln\left(x + \sqrt{x^2-1}\right)$, $x \ge 1$.

**A9.** (§3.11 #31) Prove Formula 5, $\tanh^{-1} x = \frac12\ln\left(\frac{1+x}{1-x}\right)$, by (a) the method of Example 3 and (b) the addition formula for $\tanh$.

**A10.** (§3.11 #33) Prove the Table 6 formula for $\cosh^{-1}$: $\dfrac{d}{dx}\cosh^{-1} x = \dfrac{1}{\sqrt{x^2-1}}$.

**A11.** (§3.11 #54) Show $\dfrac{d}{dx}\sqrt[4]{\dfrac{1+\tanh x}{1-\tanh x}} = \dfrac{1}{2}e^{x/2}$.

**A12.** (§3.11 #55) Show $\dfrac{d}{dx}\arctan(\tanh x) = \operatorname{sech} 2x$.

**A13.** (§3.11 #56) The Gateway Arch is $y = 211.49 - 20.96\cosh(0.03291765\,x)$, $|x| \le 91.20$. (a) Find the height at the center. (b) Find the points where the height is 100 m. (c) Find the slope there.

**A14.** (§3.11 #57) For the water-wave speed $v = \sqrt{\dfrac{gL}{2\pi}\tanh\left(\dfrac{2\pi d}{L}\right)}$, explain why $v \approx \sqrt{\dfrac{gL}{2\pi}}$ in deep water.

**A15.** (§3.11 #59) The telephone line $y = 20\cosh(x/20) - 15$ meets the right-hand pole at $x = 7$. (a) Find the slope there. (b) Find the angle between the line and the pole.

**A16.** (§3.11 #60) Verify that $y = \dfrac{T}{\rho g}\cosh\left(\dfrac{\rho g x}{T}\right)$ solves $\dfrac{d^2 y}{dx^2} = \dfrac{\rho g}{T}\sqrt{1+\left(\dfrac{dy}{dx}\right)^2}$.

<details>
<summary>💡 Hint</summary>

Compute $y' = \sinh\left(\frac{\rho g x}{T}\right)$, then $y'' = \frac{\rho g}{T}\cosh\left(\frac{\rho g x}{T}\right)$. Compare $1+(y')^2 = \cosh^2\left(\frac{\rho g x}{T}\right)$.

</details>

**A17.** (§3.11 #62) A falling object has velocity $v(t) = \sqrt{\dfrac{mg}{k}}\tanh\left(t\sqrt{\dfrac{gk}{m}}\right)$. (a) Find the terminal velocity. (b) For a 60-kg person, compute it for $k = 0.515$ (belly-to-earth) and $k = 0.067$ (feet-first).

**A18.** (§3.11 #63) (a) Show that $y = A\sinh mx + B\cosh mx$ satisfies $y'' = m^2 y$. (b) Find $y$ with $y'' = 9y$, $y(0) = -4$, and $y'(0) = 6$.

**A19.** (§3.11 #64) If $x = \ln(\sec\theta + \tan\theta)$, show $\sec\theta = \cosh x$.

**A20.** (§3.11 #67) Show that if $a \ne 0$ and $b \ne 0$, then $a e^x + b e^{-x}$ equals either $\alpha\sinh(x+\beta)$ or $\alpha\cosh(x+\beta)$.

<details>
<summary>💡 Hint</summary>

Write $a e^x + b e^{-x} = \frac{a+b}{2}(e^x + e^{-x}) + \frac{a-b}{2}(e^x - e^{-x}) = (a+b)\cosh x + (a-b)\sinh x$, then combine the two into one shifted function.

</details>

> Solutions: [Solutions](solutions/11C-solutions.md#advanced-drill)

---

## Today's Procedure

```
Step 1: Definitions — cosh x = (e^x+e^−x)/2, sinh x = (e^x−e^−x)/2, tanh = sinh/cosh. (§3.11)
         e^x = cosh x + sinh x. cosh even and ≥ 1; sinh/tanh odd.

Step 2: Identities — cosh²x − sinh²x = 1. Addition: sinh(x±y), cosh(x±y) (the + sign!).
         Double angle. For any 11B identity, apply Osborne's rule: sin→sinh, and flip
         the sign of every product of two sines.

Step 3: Inverses — arsinh x = ln(x+√(x²+1)) (all x). arcosh x = ln(x+√(x²−1)) (x≥1).
         artanh x = ½ln((1+x)/(1−x)) (|x|<1). To solve, use the log forms.

Step 4: Calculus (14A/16A) — d/dx sinh = cosh, cosh = sinh, tanh = sech² (no minus signs!).
         ∫ dx/√(x²+1) = arsinh, ∫ dx/√(x²−1) = arcosh, ∫ dx/(1−x²) = artanh.

Step 5: Recognize — catenary y = a cosh(x/a); water-wave speed; tanh saturates (→ ±1).
```

---

## How to Read These Symbols

| Symbol | Reads as | Meaning |
|:---:|:---:|------|
| $\cosh x$ | "kosh x" / hyperbolic cosine | $\frac{e^x+e^{-x}}{2}$ — the even half of $e^x$ (§3.11) |
| $\sinh x$ | "sinch x" / hyperbolic sine | $\frac{e^x-e^{-x}}{2}$ — the odd half of $e^x$ |
| $\tanh x$ | "tanch x" | $\sinh x/\cosh x$ — range $(-1,1)$, a smoothed step |
| $\operatorname{sech} x$ | "setch x" | $1/\cosh x$ — range $(0,1]$ |
| $\operatorname{csch} x$ | "cosetch x" | $1/\sinh x$ |
| $\coth x$ | "cotanch x" | $1/\tanh x$ |
| $\sinh^{-1} x$ | "inverse sinch x" | inverse hyperbolic sine: $\ln(x+\sqrt{x^2+1})$ |
| $\cosh^{-1} x$ | "inverse kosh x" | inverse hyperbolic cosine: $\ln(x+\sqrt{x^2-1})$, $x\ge1$ |
| $\tanh^{-1} x$ | "inverse tanch x" | inverse hyperbolic tangent: $\frac12\ln\frac{1+x}{1-x}$, $\lvert x\rvert<1$ |
| $e^x = \cosh x + \sinh x$ | "e to the x equals kosh plus sinch" | the no-$i$ twin of Euler's formula from 11B |
| catenary | "catenary" | hanging-cable curve $y = a\cosh(x/a)$ (§3.11 Fig 4) |
| $\tanh$ | "tanch" | the sigmoid — saturates toward $\pm1$ (§3.11 Ex 27) |

---

## Terminology

| What we call it | Math term | Notation |
|:---:|:---:|:---:|
| the trig of the hyperbola | hyperbolic functions | $\cosh, \sinh, \tanh, \operatorname{sech}, \operatorname{csch}, \coth$ |
| sector parameter on the hyperbola | hyperbolic angle | $t$ in $(\cosh t, \sinh t)$ (§3.11 Figs 6–7) |
| parallel version of a trig identity | hyperbolic identity | $\cosh^2-\sinh^2=1$, addition formulas |
| inverse of a hyperbolic function | inverse hyperbolic function | $\sinh^{-1}, \cosh^{-1}, \tanh^{-1}$ |
| shape of a hanging chain | catenary | $y = a\cosh(x/a)$ (§3.11 Fig 4) |
| S-shaped saturating curve | sigmoid | $y = \tanh x$, range $(-1,1)$ |
