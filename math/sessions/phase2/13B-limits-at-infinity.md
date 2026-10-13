# Session 13B: Limits at Infinity — Degree Races, Asymptotes, and Growth

**Phase 2 — Classical Techniques | 75 min**

*Prerequisites: 13A (algebraic limits), 10B (exponential growth rates), 12B1 (sequences intuition)*

> 💡 **Stuck?** Every problem has a collapsible **Hint** below it — click it only when you need a nudge.

> **Source.** Every example and drill below is drawn from Stewart, *Calculus*, Section 2.6 (Limits at Infinity; Horizontal Asymptotes) and Section 2.2 (The Limit of a Function, infinite limits). Each item cites its example or exercise number in those sections. The degree rule, the $x\to-\infty$ radical caution, and the infinite-limit notation are Stewart's; the graphs redraw Stewart's Figures 1, 8, 11, and 12 of §2.6. The closing preview on the number $e$ is §11.6.

---

## Part A: $\frac{\infty}{\infty}$ — Divide by the Highest Power

---

## Example 1: The Race of Polynomials (§2.6 Ex 3, Figure 1)

When $x\to\infty$, both numerator and denominator blow up, and the winner is the term of **highest degree**. Stewart's Example 3 evaluates

$$\lim_{x\to\infty}\frac{3x^2-x-2}{5x^2+4x-1}.$$

① Form $\frac{\infty}{\infty}$. Divide numerator and denominator by the highest power of the denominator, $x^2$:

$$\frac{3-\frac1x-\frac{2}{x^2}}{5+\frac4x-\frac1{x^2}}.$$

② As $x\to\infty$, every $\frac{1}{x}$ and $\frac{1}{x^2}$ term goes to $0$.

③ The limit is the ratio of the surviving leading coefficients:

$$\lim_{x\to\infty}\frac{3x^2-x-2}{5x^2+4x-1}=\frac{3}{5}.$$

Stewart's Figure 1 makes the same point for $f(x)=\dfrac{x^2-1}{x^2+1}$: the graph flattens onto the horizontal line $y=1$.

![Horizontal asymptote — the graph flattens onto y = 1]({{graph:13b-1-horizontal-asymptote}})

*Graph 13B-1: $\dfrac{x^2-1}{x^2+1}$ rises from $-1$ at the origin toward the horizontal asymptote $y=1$. Both $x\to\infty$ and $x\to-\infty$ give the same height.*

**The Rational Function Rule for $x\to\pm\infty$:**

| Degree comparison | Limit |
|:-----------------:|:-----:|
| $\deg(\text{num}) > \deg(\text{den})$ | $\pm\infty$ (sign from the leading terms) |
| $\deg(\text{num}) = \deg(\text{den})$ | ratio of the leading coefficients |
| $\deg(\text{num}) < \deg(\text{den})$ | $0$ |

![Degree comparison — three cases]({{graph:13b-2-degree-cases}})

*Graph 13B-2: Three rational functions, one per case. Top-heavy ($\deg$ num $>\deg$ den) runs off to $+\infty$; balanced degrees settle on the ratio $3$; bottom-heavy ($\deg$ num $<\deg$ den) flattens onto $0$.*

> **Geometric insight**: Dividing by the highest power is not algebra for its own sake — it isolates the one term that decides the race. Every lower-degree term becomes $\frac{1}{x^k}\to0$ and disappears.

---

## Part B: $x\to-\infty$ — Watch the Radicals

---

## Example 2: Two Horizontal Asymptotes from One Function (§2.6 Ex 4)

Stewart's Example 4 finds the horizontal asymptotes of

$$f(x)=\frac{\sqrt{2x^2+1}}{3x-5}.$$

Divide numerator and denominator by $x$ — the highest power in the denominator.

**For $x\to\infty$**, $\sqrt{x^2}=x$ (since $x>0$):

$$\frac{\sqrt{2x^2+1}}{3x-5}=\frac{\sqrt{2+\frac{1}{x^2}}}{3-\frac5x}\longrightarrow\frac{\sqrt{2}}{3}.$$

**For $x\to-\infty$**, the caution bites: $\sqrt{x^2}=|x|=-x$ (since $x<0$). So dividing the numerator by $x$ produces a minus sign:

$$\frac{\sqrt{2x^2+1}}{x}=\frac{\sqrt{2x^2+1}}{-\sqrt{x^2}}=-\sqrt{2+\frac{1}{x^2}},$$

$$\lim_{x\to-\infty}\frac{\sqrt{2x^2+1}}{3x-5}=\frac{-\sqrt{2}}{3}.$$

The graph therefore has **two** horizontal asymptotes, $y=\frac{\sqrt2}{3}$ and $y=-\frac{\sqrt2}{3}$.

![Radical with two horizontal asymptotes]({{graph:13b-3-radical-asymptotes}})

*Graph 13B-3: $\dfrac{\sqrt{2x^2+1}}{3x-5}$ approaches $+\frac{\sqrt2}{3}$ on the right and $-\frac{\sqrt2}{3}$ on the left. The vertical asymptote at $x=\frac53$ splits the two branches.*

**The rule to memorize**: for $x\to-\infty$, always write $\sqrt{x^2}=|x|=-x$. Dropping the minus sign is the single most common error in this section.

> **Geometric insight**: A square root is always non-negative, but $x$ is negative on the left. The quotient flips sign exactly because the numerator cannot — that is the whole content of the caution.

---

## Part C: $\infty-\infty$ — Conjugate or Common Denominator

---

## Example 3: The Difference of Two Growing Quantities (§2.6 Ex 5)

Both terms go to infinity, so the difference is undecided. Merge them into a single expression and look again.

Stewart's Example 5:

$$\lim_{x\to\infty}\left(\sqrt{x^2+1}-x\right).$$

① Form $\infty-\infty$. Multiply by the conjugate $\sqrt{x^2+1}+x$:

$$\left(\sqrt{x^2+1}-x\right)\cdot\frac{\sqrt{x^2+1}+x}{\sqrt{x^2+1}+x}
=\frac{(x^2+1)-x^2}{\sqrt{x^2+1}+x}=\frac{1}{\sqrt{x^2+1}+x}.$$

② The denominator grows without bound (it is bigger than $x$), so

$$\lim_{x\to\infty}\left(\sqrt{x^2+1}-x\right)=\lim_{x\to\infty}\frac{1}{\sqrt{x^2+1}+x}=0 .$$

**A second shape** — a difference of two radicals:

$$\lim_{x\to\infty}\left(\sqrt{x^2+3x}-\sqrt{x^2-2x}\right)
=\lim_{x\to\infty}\frac{(x^2+3x)-(x^2-2x)}{\sqrt{x^2+3x}+\sqrt{x^2-2x}}
=\lim_{x\to\infty}\frac{5x}{\sqrt{x^2+3x}+\sqrt{x^2-2x}}.$$

Divide by $x$: $\dfrac{5}{\sqrt{1+\frac3x}+\sqrt{1-\frac2x}}\longrightarrow\dfrac{5}{1+1}=\dfrac52.$

> **Geometric insight**: The conjugate converts $\infty-\infty$ into a quotient whose denominator grows faster than the numerator — so the answer is $0$. When the numerator keeps a surviving $x$, the answer is a finite ratio instead.

---

## Part D: Infinite Limits at Infinity — Running Off the Top

---

## Example 4: When the Value Itself Runs Away (§2.6 Ex 9–12, Figures 11–12)

Sometimes the limit is not a number at all. Stewart writes

$$\lim_{x\to\infty}f(x)=\infty$$

to mean the values of $f(x)$ become arbitrarily large.

**Example 9**: $\displaystyle\lim_{x\to\infty}x^3=\infty$ and $\displaystyle\lim_{x\to-\infty}x^3=-\infty$ — the sign of an odd power follows $x$.

**Example 10**: $\displaystyle\lim_{x\to\infty}(x^2-x)=\lim_{x\to\infty}x(x-1)=\infty$ — the Limit Laws do not apply to $\infty-\infty$, but factoring settles it.

**Example 11**: $\displaystyle\lim_{x\to\infty}\frac{x^2+x}{3-x}=\lim_{x\to\infty}\frac{x+1}{\frac3x-1}=-\infty$, because the numerator grows while the denominator approaches $-1$.

**Example 12** uses the same limits to sketch $y=(x-2)^4(x+1)^3(x-1)$: the four powers decide the sign at each end, giving $\infty$ at both $x\to\infty$ and $x\to-\infty$.

Stewart's Figures 11 and 12 compare the *rates*: $e^x$ is already far above $x^3$ for large $x$, and the gap keeps widening.

![Growth race — e^x overtakes x^3]({{graph:13b-4-growth-race}})

*Graph 13B-4: $y=e^x$ (red) and $y=x^3$ (blue). For $x>3$ the exponential is already many times larger, and the ratio $e^x/x^3\to\infty$. Exponential growth beats every polynomial.*

**Growth hierarchy** (slowest to fastest as $x\to\infty$):

$$\ln x \;\ll\; x^{0.0001} \;\ll\; x \;\ll\; x^2 \;\ll\; x^{100} \;\ll\; 1.01^{x} \;\ll\; e^{x} \;\ll\; x! .$$

> **Geometric insight**: "Infinite limit at infinity" is a statement about the *rate* of growth, not about a value. The hierarchy ranks those rates: any exponential outruns any polynomial, and any positive power outruns the logarithm.

---

## Part E: Exponentials, Inverse Trig, and Oscillation at Infinity

---

## Example 5: The Three Behaviours at Infinity (§2.6 Ex 6–8)

Not every function at infinity settles, blows up, or vanishes — some oscillate.

**Stewart's Example 6** substitutes $t=\frac{1}{x-2}$, so $t\to\infty$ as $x\to2^+$:

$$\lim_{x\to2^+}\arctan\!\left(\frac{1}{x-2}\right)=\lim_{t\to\infty}\arctan t=\frac{\pi}{2}.$$

**Stewart's Example 7** uses the exponential end behaviour $e^x\to0$ as $x\to-\infty$ (equation (6) of §2.6). With $t=\frac1x\to-\infty$ as $x\to0^-$:

$$\lim_{x\to0^-}e^{1/x}=\lim_{t\to-\infty}e^{t}=0 .$$

**Stewart's Example 8**: $\displaystyle\lim_{x\to\infty}\sin x$ does **not** exist — the values oscillate between $1$ and $-1$ forever and never settle.

The three behaviours, side by side:

| Function at $x\to\infty$ | Limit | Reason |
|:---:|:---:|------|
| $\arctan x$ | $\frac{\pi}{2}$ | inverse tangent saturates |
| $e^{-x}$ | $0$ | exponential decay |
| $\sin x$ | DNE | oscillation between $-1$ and $1$ |

**A mixed case** — the oscillation dies because a decaying factor multiplies it:

$$\lim_{x\to\infty}e^{-x}\cos 3x=0, \qquad\text{because } -e^{-x}\le e^{-x}\cos 3x\le e^{-x}\ \text{and both bounds}\to0 .$$

> **Geometric insight**: At infinity, a bounded oscillating factor ($\sin$, $\cos$) can be tamed only by a factor that decays to $0$. Without such a factor the oscillation wins and the limit does not exist.

---

## Part F: Infinite Limits at a Finite Point — Vertical Asymptotes

---

## Example 6: When the Denominator Goes to Zero (§2.2 #29–43)

A different kind of infinite limit happens when $x$ approaches a *finite* point and the denominator goes to $0$ while the numerator does not. Stewart's §2.2 exercise bank drills this sign chase.

**#29 and #30** — the same function from two sides:

$$\lim_{x\to5^+}\frac{x+1}{x-5}=+\infty \quad(\text{numerator}\to6>0,\ \text{denominator}\to0^+),$$
$$\lim_{x\to5^-}\frac{x+1}{x-5}=-\infty \quad(\text{denominator}\to0^-).$$

Because the two one-sided limits differ, $\displaystyle\lim_{x\to5}\frac{x+1}{x-5}$ does not exist — there is a vertical asymptote at $x=5$.

![Vertical asymptote — sign chase at x = 2]({{graph:13b-5-vertical-asymptote}})

*Graph 13B-5: The same sign chase, drawn for $\dfrac{1}{x-2}$: the value shoots up to $+\infty$ from the right and down to $-\infty$ from the left, so the vertical line $x=2$ is an asymptote and the two-sided limit does not exist.*

**#31** — a **squared** denominator is always positive near the point:

$$\lim_{x\to2}\frac{x^2}{(x-2)^2}=+\infty,$$

because $(x-2)^2\to0^+$ from *both* sides, so the two one-sided limits agree.

**#43** — the sign chase again, on a cubic denominator:

$$\lim_{x\to1^-}\frac{1}{x^3-1}=-\infty, \qquad \lim_{x\to1^+}\frac{1}{x^3-1}=+\infty .$$

**#41 and #42** turn the chase around: find the vertical asymptotes of a rational function by setting the denominator to $0$ (after cancelling any common factor with the numerator).

> **Geometric insight**: $\frac{\text{nonzero}}{0}$ is not a number — it is a sign statement. An even power of the vanishing factor gives the same sign on both sides (so the limit is $+\infty$ or $-\infty$); an odd power flips the sign (so the two-sided limit does not exist).

---

## Part G: Finding Horizontal and Vertical Asymptotes

---

## Example 7: The Full Asymptote Hunt (§2.6 #47–52)

For a rational function, the two kinds of asymptote are found by two different limits.

**Horizontal asymptote**: evaluate $\displaystyle\lim_{x\to\pm\infty}f(x)$ with the degree rule (Part A).

**Vertical asymptote**: find where the denominator is $0$ but the numerator is not — the sign chase of Part F.

**Worked example — #47**: $y=\dfrac{5+4x}{x+3}$.

- Horizontal: $\deg$ num $=\deg$ den $=1$, so the limit is $\dfrac41=4$. The line $y=4$ is the horizontal asymptote.
- Vertical: the denominator is $0$ at $x=-3$ and the numerator there is $5+4(-3)=-7\neq0$. The line $x=-3$ is the vertical asymptote.

**#52** mixes in an exponential: $y=\dfrac{2e^x}{e^x-5}$ has a horizontal asymptote found by dividing by $e^x$:

$$\lim_{x\to\infty}\frac{2}{1-5e^{-x}}=2, \qquad \lim_{x\to-\infty}\frac{2e^x}{e^x-5}=\frac{0}{0-5}=0,$$

so this curve has **two** horizontal asymptotes, $y=2$ and $y=0$, plus a vertical asymptote at $x=\ln 5$.

> **Geometric insight**: A rational function can have at most one horizontal asymptote on each side and any number of vertical ones. The horizontal one comes from the degree race; each vertical one sits where a surviving denominator factor hits $0$.

---

## Part H: Preview — The Number $e$ as a Limit (🔗 12B1, 18A)

---

## Example 8: $1^\infty$ and the Constant $e$ (§11.6)

One more shape appears at infinity: a base that goes to $1$ raised to a power that goes to $\infty$. The classic case defines $e$ itself,

$$\lim_{n\to\infty}\left(1+\frac1n\right)^n=e \qquad(\text{Stewart §11.6, with the constant } e \approx 2.71828\ldots).$$

The general pattern — **a constant in the numerator** — is

$$\lim_{n\to\infty}\left(1+\frac{k}{n}\right)^n=e^{k}.$$

**Why**: write $\left(1+\frac{k}{n}\right)^n=\left[\left(1+\frac{k}{n}\right)^{n/k}\right]^{k}$. The bracket is the defining form of $e$ (with $n/k\to\infty$), and raising to the fixed power $k$ gives $e^k$.

**A rational tweak**:

$$\lim_{n\to\infty}\left(\frac{n+3}{n-1}\right)^n:\qquad \frac{n+3}{n-1}=1+\frac{4}{n-1},$$

$$\left(1+\frac{4}{n-1}\right)^{n}=\left(1+\frac{4}{n-1}\right)^{n-1}\cdot\left(1+\frac{4}{n-1}\right)\longrightarrow e^{4}\cdot1=e^{4}.$$

> **Geometric insight**: This is the same "growth race" of Part D, now written as a power. The limit $e$ is the exchange rate between continuous compounding and the integer step $n$ — the subject of §11.6 and of Session 18A.

---

## Common Mistakes

### Mistake 1: Forgetting $\sqrt{x^2}=|x|$ when $x\to-\infty$

**Wrong**: $\dfrac{\sqrt{x^2+1}}{x}=\sqrt{1+1/x^2}\to1$ as $x\to-\infty$. **Right**: for $x<0$, $|x|=-x$, so the expression is $-\sqrt{1+1/x^2}\to-1$. The sign flips because the square root cannot be negative.

### Mistake 2: Saying $0\cdot\infty=0$ or $\infty-\infty=0$

**Wrong.** Both are indeterminate. Rewrite as a quotient (for $0\cdot\infty$) or conjugate / combine (for $\infty-\infty$) before deciding.

### Mistake 3: Writing $\frac{1}{0}=\infty$ without a sign

**Wrong.** It could be $+\infty$, $-\infty$, or neither — check which side the denominator approaches from, and whether the two sides agree.

### Mistake 4: Using the Limit Laws on infinite limits

**Wrong**: splitting $\lim_{x\to\infty}(x^2-x)$ into $\infty-\infty$ and applying Law 2. **Right**: the laws require the individual limits to *exist* (be finite numbers); $\infty$ is not a number. Factor, divide, or conjugate first.

---

## What We Just Did

```
(1) ∞/∞ rational: divide by the highest power → degree comparison.  (§2.6 Ex 3)
    deg(num) > deg(den) → ±∞ ; = → ratio of leading coefficients ; < → 0.

(2) x→−∞: √(x²) = |x| = −x (since x < 0). Watch odd-degree signs.    (§2.6 Ex 4)

(3) ∞−∞: conjugate (for √A−√B) or common denominator (for fractions). (§2.6 Ex 5)

(4) Infinite limits: at infinity → growth-rate comparison (e^x ≫ x³ ≫ ln x);  (§2.6 Ex 9–12)
    at a finite point → sign chase when the denominator → 0.        (§2.2 #29–43)

(5) Asymptotes: horizontal from lim_{x→±∞}; vertical where a surviving  (§2.6 #47–52)
    denominator factor hits 0.

(6) 1^∞: (1+k/n)^n → e^k.  (§11.6, preview of 18A)
```

---

## Basic Drills

> Pure fluency: identify the form, apply the degree rule or the sign chase. One clean move per item.

**D1.** (§2.6 #15) Evaluate $\displaystyle\lim_{x\to\infty}\frac{4x+3}{5x-1}$. Divide by $x$.

**D2.** (§2.6 #16) Evaluate $\displaystyle\lim_{x\to\infty}\frac{-2}{3x+7}$. Compare degrees.

**D3.** (§2.6 #13) Evaluate $\displaystyle\lim_{x\to\infty}\frac{2x^2-7}{5x^2+x-3}$. Divide by $x^2$.

**D4.** (§2.6 #17) Evaluate $\displaystyle\lim_{t\to-\infty}\frac{3t^2+t}{t^3-4t+1}$. Compare degrees.

**D5.** (§2.6 #18) Evaluate $\displaystyle\lim_{t\to-\infty}\frac{6t^2+t-5}{9-2t^2}$. Ratio of leading coefficients.

**D6.** (§2.6 #20) Evaluate $\displaystyle\lim_{x\to\infty}\frac{3x^3-8x+2}{4x^3-5x^2-2}$.

**D7.** (§2.6 #21) Evaluate $\displaystyle\lim_{x\to\infty}\frac{4-\sqrt{x}}{2+\sqrt{x}}$. Divide by $\sqrt{x}$.

**D8.** (§2.6 #29) Evaluate $\displaystyle\lim_{t\to\infty}\left(\sqrt{25t^2+2}-5t\right)$. Conjugate.

**D9.** (§2.6 #32) Evaluate $\displaystyle\lim_{x\to\infty}\left(x-\sqrt{x}\right)$. Factor out $\sqrt{x}$.

**D10.** (§2.6 #37) Evaluate $\displaystyle\lim_{x\to\infty}\frac{1-e^{x}}{1+2e^{x}}$. Divide by $e^x$.

**D11.** (§2.2 #29) Evaluate $\displaystyle\lim_{x\to5^+}\frac{x+1}{x-5}$. Track the sign of the denominator.

**D12.** (§2.2 #31) Evaluate $\displaystyle\lim_{x\to2}\frac{x^2}{(x-2)^2}$. Note the squared denominator.

> Solutions: [Solutions](solutions/13B-solutions.md#basic-drill)

---

## Advanced Drills

> Chains two or three moves: radicals at $-\infty$, difference of radicals, and the asymptote hunt.

**A1.** (§2.6 #14) Evaluate $\displaystyle\lim_{x\to\infty}\sqrt{\frac{9x^3+8x-4}{3-5x+x^3}}$. Take the inside limit first.

**A2.** (§2.6 #22) Evaluate $\displaystyle\lim_{u\to-\infty}\frac{(u^2+1)(2u^2-1)}{(u^2+2)^2}$. Expand the leading terms.

**A3.** (§2.6 #23) Evaluate $\displaystyle\lim_{x\to\infty}\frac{\sqrt{x+3x^2}}{4x-1}$.

**A4.** (§2.6 #24) Evaluate $\displaystyle\lim_{t\to\infty}\frac{t+3}{\sqrt{2t^2-1}}$.

**A5.** (§2.6 #25) Evaluate $\displaystyle\lim_{x\to\infty}\frac{\sqrt{1+4x^{6}}}{2-x^{3}}$.

**A6.** (§2.6 #26) Evaluate $\displaystyle\lim_{x\to-\infty}\frac{\sqrt{1+4x^{6}}}{2-x^{3}}$. Compare with A5.

**A7.** (§2.6 #30) Evaluate $\displaystyle\lim_{x\to-\infty}\left(\sqrt{4x^2+3x}+2x\right)$. Conjugate, and use $\sqrt{x^2}=-x$.

**A8.** (§2.6 #31) Evaluate $\displaystyle\lim_{x\to\infty}\left(\sqrt{x^2+ax}-\sqrt{x^2+bx}\right)$ for constants $a,b$.

**A9.** (§2.6 #36) Evaluate $\displaystyle\lim_{x\to\infty}\frac{\sin^2 x}{x^2+1}$. Squeeze.

**A10.** (§2.6 #41) Evaluate $\displaystyle\lim_{x\to\infty}\left[\ln(1+x^2)-\ln(1+x)\right]$. Combine the logarithms.

**A11.** (§2.6 #48) Find the horizontal and vertical asymptotes of $y=\dfrac{2x^2+1}{3x^2+2x-1}$.

<details>
<summary>💡 Hint</summary>

For **A5/A6**, $\sqrt{4x^6}=2|x^3|$. When $x<0$, $|x^3|=-x^3$ — that single sign is the difference between the two answers.

For **A8**, multiply by the conjugate first, then divide numerator and denominator by $x$.

For **A11**, factor the denominator $3x^2+2x-1=(3x-1)(x+1)$ to locate the vertical asymptotes, then compare degrees for the horizontal one.

</details>

> Solutions: [Solutions](solutions/13B-solutions.md#advanced-drill)

---

## Today's Procedure

```
Step 1: x → ±∞ with a rational function → divide by the highest power.
    Compare degrees: num > den → ±∞ ; num = den → ratio ; num < den → 0.   (§2.6 Ex 3)

Step 2: x → −∞ with a radical → √(x²) = |x| = −x. Watch the sign.        (§2.6 Ex 4)

Step 3: ∞ − ∞ → conjugate (√A − √B) or common denominator.               (§2.6 Ex 5)
    0 · ∞ → rewrite as a quotient.

Step 4: Denominator → 0 at a finite point → sign chase from each side.
    Even power → same sign both sides; odd power → sign flips (DNE).      (§2.2 #29–43)

Step 5: Asymptotes — horizontal from lim_{x→±∞}; vertical where a surviving
    denominator factor is 0.                                              (§2.6 #47–52)
```

---

## How to Read These Symbols

| Symbol | Reads as | Meaning |
|:---:|:---:|------|
| $\lim_{x \to \infty} f(x) = L$ | "limit as x goes to infinity of f of x equals L" | horizontal asymptote at $y=L$ (§2.6 Def 1) |
| $\lim_{x \to -\infty} f(x) = L$ | "limit as x goes to negative infinity" | end behaviour on the left (§2.6 Def 2) |
| $\deg(P) < \deg(Q)$ | "degree of P less than degree of Q" | rational function $\to 0$ |
| $\deg(P) = \deg(Q)$ | "degrees equal" | limit = ratio of leading coefficients |
| $\deg(P) > \deg(Q)$ | "degree of P greater than degree of Q" | limit = $\pm\infty$ — check the leading signs |
| leading coefficient | "leading coefficient" | coefficient of the highest-degree term |
| $\lim_{x\to\infty}f(x)=\infty$ | "limit is infinity" | values grow without bound (§2.6 infinite limits) |
| $\sqrt{x^2}=\lvert x\rvert$ | "root of x squared equals absolute x" | equals $x$ for $x>0$, $-x$ for $x<0$ |
| horizontal asymptote | "horizontal asymptote" | the line $y=L$ the graph flattens onto |
| vertical asymptote | "vertical asymptote" | the line $x=a$ where the value runs to $\pm\infty$ |
| growth hierarchy | "growth rate hierarchy" | $x! \gg e^x \gg x^n \gg \ln x$ |
| $1^\infty$ | "one to the infinity" | indeterminate; the form that produces $e$ (§11.6) |

---

## Terminology

| What we call it | Math term | Notation |
|:---------------:|:---------:|:--------:|
| divide by highest power | dominant-term method | divide by $x^{\deg}$ |
| degree comparison | degree test for rational functions | $\deg(\text{num})$ vs $\deg(\text{den})$ |
| sign chase | sign analysis | $0^+$, $0^-$ |
| squared denominator | even-power denominator | $(x-a)^{2k}$ |
| conjugate | rationalization | multiply by $\sqrt{A}+B$ |
| growth hierarchy | asymptotic growth rates | $x!\gg e^x\gg x^n\gg\ln x$ |
| end behaviour | behaviour as $x\to\pm\infty$ | leading term dominates |
| $e$ as a limit | Euler's limit definition | $(1+k/n)^n\to e^k$ |
| horizontal asymptote | horizontal asymptote | $y=L$ from $\lim_{x\to\pm\infty}f$ |
| vertical asymptote | vertical asymptote | $x=a$ from $\frac{\text{nonzero}}{0}$ |
| indeterminate | indeterminate form | $\frac{\infty}{\infty}$, $\infty-\infty$, $0\cdot\infty$, $1^\infty$ |





