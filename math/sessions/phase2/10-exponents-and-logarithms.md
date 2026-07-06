# Session 10: Exponents and Logarithms — Mastering Powers

**Phase 2 — Classical Techniques | 120 min**

---

## Part A: Exponents — The Rules of Repeated Multiplication

---

## Example 1: Adding, Subtracting, and Multiplying Exponents

**Same base, multiply**: $2^3 \times 2^4$. Add the exponents. → $2^{3+4} = 2^7 = 128$.
$3^5 \div 3^2$. Subtract the exponents. → $3^{5-2} = 3^3 = 27$.

Hand check: $2^3=8$, $2^4=16$. $8 \times 16 = 128 = 2^7$. Correct.

**Power of a power**: $(2^3)^4$. Multiply the exponents. → $2^{3 \times 4} = 2^{12} = 4096$.

---

## Example 2: Zero and Negative Exponents

**Zero exponent**: $5^0 = 1$. $(-3)^0 = 1$. $x^0 = 1$ ($x \neq 0$).
Why: $5^3 \div 5^3 = 5^{3-3} = 5^0 = 1$.

**Negative exponent**: $2^{-3} = \frac{1}{2^3} = \frac{1}{8}$.
$\left(\frac{2}{3}\right)^{-2} = \left(\frac{3}{2}\right)^2 = \frac{9}{4}$. Flip it, then square.

**Exponent rules summary**:
- $a^m \cdot a^n = a^{m+n}$ (multiply → add)
- $a^m \div a^n = a^{m-n}$ (divide → subtract)
- $(a^m)^n = a^{mn}$ (power of power → multiply)
- $(ab)^n = a^n b^n$ (power of product → distribute)
- $a^{-n} = \frac{1}{a^n}$ (negative → reciprocal)

---

## Example 3: Fractional Exponents — Turn Them into Roots

$8^{\frac{1}{3}} = \sqrt[3]{8} = 2$. Denominator = root degree.
$16^{\frac{1}{4}} = \sqrt[4]{16} = 2$.

$8^{\frac{2}{3}}$: denominator = root, numerator = power.
$\sqrt[3]{8^2} = \sqrt[3]{64} = 4$. Or $(\sqrt[3]{8})^2 = 2^2 = 4$. Same result.

$27^{-\frac{2}{3}} = \frac{1}{(\sqrt[3]{27})^2} = \frac{1}{3^2} = \frac{1}{9}$.

**Rule**: $a^{\frac{m}{n}} = \sqrt[n]{a^m} = (\sqrt[n]{a})^m$.

---

## Visual Interlude: The Geometry of Powers — Three Views of $2^x$

**View 1 — Repeated Doubling on a Number Line.**

Place your finger at 1. Each step to the right multiplies by 2. Going right: multiply by 2. Going left: divide by 2. The number line is not additive — it is multiplicative. Equal steps in $x$ mean equal multiplicative jumps.

![Number line doubling](graphs/10e1-doubling-numberline.png)

**View 2 — Area Growth of a Square.**

A square of side $s$ has area $s^2$. Double the side ($s \to 2s$): area quadruples ($s^2 \to 4s^2$). The exponent 2 captures the dimension: 2D objects scale as side$^2$. A cube of side $s$ scales as $s^3$.

![Dimension scaling](graphs/10e2-dimension-scaling.png)

**View 3 — The Graph as a Curve That Is Its Own Slope.**

The slope (steepness) at any point on $y = e^x$ equals the height at that point. This unique property — being its own derivative — is why $e^x$ is the "natural" exponential.

![Slope equals height](graphs/10e3-exp-slope-equals-height.png)

---

## Example 4: Different Bases — Unify Them

$4^x = 2^{x+1}$.
(1) $4 = 2^2$ → $2^{2x} = 2^{x+1}$.
(2) $2x = x+1$ → $x = 1$.

$9^{x-1} = 27^{2x}$.
(1) Base 3: $3^{2x-2} = 3^{6x}$.
(2) $2x-2 = 6x$ → $x = -\frac{1}{2}$.

$25^{x} \cdot 125^{1-x} = 5$.
(1) $5^{2x} \cdot 5^{3(1-x)} = 5^1$ → $5^{2x+3(1-x)} = 5^1$.
(2) $2x+3-3x = 1$ → $-x+3 = 1$ → $x = 2$.

---

## Example 5: Substitute $a^x = t$ — Turn Into a Quadratic

$2^{2x} - 5 \cdot 2^x + 4 = 0$.
(1) $t = 2^x$ ($t>0$) → $t^2 - 5t + 4 = 0$.
(2) $(t-1)(t-4) = 0$ → $t=1,4$.
(3) $2^x = 1$ → $x=0$. $2^x = 4$ → $x=2$.

$3^{x+1} + 3^{x-1} = 30$.
(1) $3 \cdot 3^x + \frac{1}{3}\cdot 3^x = \frac{10}{3}\cdot 3^x = 30$.
(2) $3^x = 9$ → $x = 2$.

$5^x + 5^{2-x} = 26$.
(1) $5^x = t$. $5^{2-x} = 25 \cdot 5^{-x} = \frac{25}{t}$.
(2) $t + \frac{25}{t} = 26$ → $t^2 - 26t + 25 = 0$ → $(t-1)(t-25)=0$.
(3) $t=1$: $x=0$. $t=25$: $5^x=25$ → $x=2$.

---

## Example 6: Exponential Inequalities — Base Size Decides the Direction

$2^{x+1} > 8$. $8 = 2^3$. Base > 1 → keep inequality: $x+1 > 3$ → $x > 2$.

$\left(\frac{1}{2}\right)^{x} \geq 4$. $4 = 2^2 = \left(\frac{1}{2}\right)^{-2}$.
Base < 1 → flip inequality: $x \leq -2$.

$3^{x^2-4} < 1$. $1 = 3^0$. Base > 1 → $x^2-4 < 0$ → $-2 < x < 2$.

$\left(\frac{1}{3}\right)^{x^2} > \frac{1}{27}$.
$\frac{1}{27} = \left(\frac{1}{3}\right)^3$. Base < 1 → $x^2 < 3$ → $-\sqrt{3} < x < \sqrt{3}$.

> **Up to here**: 5 exponent rules. $a^x=t$ substitution for quadratics. Base > 1 keeps inequality sign; base < 1 flips it.

---

## Basic Algebra Drill — Exponents (6 Problems)

> Pure calculation. No tricks, no traps. Build speed and fluency.

**D1.** Simplify $3^4 \cdot 3^{-2}$. Write the answer as an integer.

**D2.** Simplify $\frac{5^6}{5^2}$. Write the answer as an integer.

**D3.** Simplify $(2^3)^2$. Write the answer as an integer.

**D4.** Rewrite $16^{-\frac{1}{2}}$ as a simple fraction.

**D5.** Rewrite $27^{\frac{2}{3}}$ as an integer.

**D6.** Simplify $\frac{10^4 \cdot 10^{-1}}{10^2}$. Write the answer as an integer.

**D7.** Rewrite $\left(\frac{8}{27}\right)^{-\frac{2}{3}}$ as a simple fraction.

**D8.** Compute $\log_5 125 + \log_5 \frac{1}{5}$. Write the answer as an integer.

> Solutions: [Solutions](solutions/10-solutions.md#basic-drill)

---

## Part B: Logarithms — Answering "What Power?"

---

## Example 7: What a Logarithm Means

$\log_2 8$: "2 to what power gives 8?" → $2^3=8$ → **3**.

$\log_3 81 = 4$. $\log_5 \frac{1}{25} = -2$. $\log_{10} 1000 = 3$.
$\log_a 1 = 0$ (any base). $\log_a a = 1$.

$\log_{10} 0.001 = -3$. $\log_2 0.5 = -1$.

---

## Example 8: Log Operations — Product Becomes Sum, Quotient Becomes Difference

$\log_2 (8 \times 4) = \log_2 8 + \log_2 4 = 3 + 2 = 5$. Check: $32 = 2^5$.

$\log_3 \frac{81}{9} = \log_3 81 - \log_3 9 = 4 - 2 = 2$. Check: $9 = 3^2$.

$\log_2 8^5 = 5 \log_2 8 = 5 \times 3 = 15$.

**Three rules**:
- $\log_a(MN) = \log_a M + \log_a N$
- $\log_a(M/N) = \log_a M - \log_a N$
- $\log_a(M^k) = k\log_a M$

---

## Visual Interlude: The Logarithm as Area Under $1/x$

**The natural log $\ln a$ is the area under the curve $y = 1/x$ from $x=1$ to $x=a$.**

This visual definition makes log rules obvious:

**$\ln(ab) = \ln a + \ln b$**: The area from 1 to $ab$ equals the area from 1 to $a$ plus the area from $a$ to $ab$.
Stretch the second piece horizontally by factor $1/a$ and vertically by factor $a$ (area unchanged!) — it becomes the area from 1 to $b$.

**$\ln(1/a) = -\ln a$**: The area from 1 to $1/a$ is the negative of the area from 1 to $a$ (by symmetry of $1/x$ under $x \to 1/x$).

**$\ln(a^k) = k\ln a$**: Stretching the $x$-axis by factor $k$ stretches the area by factor $k$.

This geometric picture — log as area — unifies all three rules under one visual principle: **stretching and compressing area under a hyperbola.**

![Log as area under 1/x](graphs/10f-log-as-area.png)

---

## Example 9: Change of Base — Any Base Works

$\log_4 8 = \frac{\log_2 8}{\log_2 4} = \frac{3}{2}$. $4^{3/2} = 8$. Correct.

$\log_8 2 = \frac{\log_2 2}{\log_2 8} = \frac{1}{3}$.

$\log_{27} 9 = \frac{\log_3 9}{\log_3 27} = \frac{2}{3}$.

**Change of base formula**: $\log_a b = \frac{\log_c b}{\log_c a}$ (any $c$).

Handy: $\log_a b \cdot \log_b a = 1$. Because $\frac{\log b}{\log a} \cdot \frac{\log a}{\log b} = 1$.

---

## Example 10: Common Log and Natural Log

**$\log x$** = $\log_{10} x$ (base 10 omitted). $\log 100 = 2$, $\log 0.001 = -3$.

**$\ln x$** = $\log_e x$. $e \approx 2.71828$.
$\ln e = 1$, $\ln 1 = 0$, $\ln e^2 = 2$.

Definition of $e$: $\lim_{n\to\infty} \left(1 + \frac{1}{n}\right)^n$. The limit of continuous compounding.

**$\ln$ ↔ $\log$ conversion**: $\log x = \frac{\ln x}{\ln 10} \approx \frac{\ln x}{2.3026}$.

---

## Example 11: Graphs of $e^x$ and $\ln x$ — Mirror Images

$y = e^x$: passes through $(0,1)$. $x \to -\infty$ → $0$. $x \to \infty$ → $\infty$. Explosive growth.

$y = \ln x$: passes through $(1,0)$. $x \to 0^+$ → $-\infty$. $x \to \infty$ → $\infty$. Slow growth.

The two are symmetric across the line $y=x$. $(0,1)$ ↔ $(1,0)$, $(1,e)$ ↔ $(e,1)$.

![Exponential and natural log](graphs/10b-exp-ln-inverse.png)

**Visual Comparison — A Race Between Functions:**

Superimpose four curves on one set of axes to feel their personalities. At $x=10$: $x=10$, $x^2=100$, $2^x=1024$, $\ln x=2.30$.
The exponential overtakes the quadratic at $x=4$ and never looks back. The log crawls.

![Growth race: x vs x² vs 2ˣ vs ln x](graphs/10h-growth-race.png)

**The mirror principle**: Flip the graph of $y = 2^x$ over the line $y=x$. What you get is $y = \log_2 x$.
Every point $(a, 2^a)$ becomes $(2^a, a)$. The roles of input and output swap.

---

## Example 12: Log Inequalities — Check the Argument First!

$\log_2 (x-1) < 3$.
(1) $3 = \log_2 8$. Base > 1 → $x-1 < 8$ → $x < 9$.
(2) Argument > 0: $x-1 > 0$ → $x > 1$.
→ **$1 < x < 9$.**

$\log_{\frac{1}{2}} (x+2) \geq 1$.
(1) $1 = \log_{\frac{1}{2}} \tfrac{1}{2}$. Base < 1 → $x+2 \leq \tfrac{1}{2}$ → $x \leq -\frac{3}{2}$.
(2) Argument > 0: $x+2 > 0$ → $x > -2$.
→ **$-2 < x \leq -\frac{3}{2}$.**

$\log_3(x^2-4) \leq 1$.
(1) $1 = \log_3 3$. Base > 1 → $x^2-4 \leq 3$ → $x^2 \leq 7$ → $-\sqrt{7} \leq x \leq \sqrt{7}$.
(2) Argument > 0: $x^2-4 > 0$ → $|x| > 2$.
(3) Intersect: $[-\sqrt{7}, -2) \cup (2, \sqrt{7}]$.

> **Up to here**: Log = mirror of exponent. 3 operation rules. $\ln$ uses base $e$, $\log$ uses base 10.
> Log inequalities: always impose argument > 0 on top of the solution.

---

## Part C: Exponential and Logarithmic Equations — Every Type

---

## Example 13: Combine Logs, Then Solve

$\log_2 (x+1) + \log_2 (x-1) = 3$.
(1) Combine: $\log_2[(x+1)(x-1)] = 3$.
(2) Solve: $(x+1)(x-1) = 2^3 = 8$ → $x^2-1=8$ → $x = \pm 3$.
(3) Check arguments: $x+1>0, x-1>0$ → $x>1$. $x=-3$ discarded. → **$x=3$.**

$\log(x+2) - \log(x-1) = 1$.
(1) $\log\frac{x+2}{x-1} = 1$ → $\frac{x+2}{x-1} = 10$.
(2) $x+2 = 10x-10$ → $12 = 9x$ → $x = \frac{4}{3}$.
(3) Arguments: $x+2>0, x-1>0$ → $x>1$. $\frac{4}{3} > 1$. Valid.

---

## Example 14: Substitute $\log$ as $t$

$(\log_2 x)^2 - 3\log_2 x + 2 = 0$.
(1) $t = \log_2 x$ → $t^2-3t+2=0$ → $t=1,2$.
(2) $x = 2^1 = 2$, $x = 2^2 = 4$. → **$x=2,4$.**

$(\ln x)^2 - 5\ln x + 6 = 0$.
$t=\ln x$ → $t^2-5t+6=0$ → $t=2,3$ → $x=e^2, e^3$.

---

## Example 15: Take $\ln$ on Both Sides

$2^x = 3^{x+1}$.
(1) $\ln(2^x) = \ln(3^{x+1})$ → $x\ln 2 = (x+1)\ln 3$.
(2) $x\ln 2 = x\ln 3 + \ln 3$ → $x(\ln 2 - \ln 3) = \ln 3$.
(3) $x = \frac{\ln 3}{\ln 2 - \ln 3} \approx -2.71$.

$3^{2x-1} = 5^{x}$.
(1) $(2x-1)\ln 3 = x\ln 5$ → $2x\ln 3 - \ln 3 = x\ln 5$.
(2) $x(2\ln 3 - \ln 5) = \ln 3$ → $x = \frac{\ln 3}{2\ln 3 - \ln 5}$.

$7^{x} = 2^{2x+3}$.
(1) $x\ln 7 = (2x+3)\ln 2$ → $x\ln 7 = 2x\ln 2 + 3\ln 2$.
(2) $x(\ln 7 - 2\ln 2) = 3\ln 2$ → $x = \frac{3\ln 2}{\ln 7 - 2\ln 2}$.

---

## Example 16: The Mixed Type — $x$ Appears in Both Exponent and Base

$x^{\log_2 x} = 8x$.
(1) Take $\log_2$ of both sides: $\log_2(x^{\log_2 x}) = \log_2(8x)$.
(2) $(\log_2 x)^2 = 3 + \log_2 x$.
(3) $t = \log_2 x$: $t^2 - t - 3 = 0$ → $t = \frac{1 \pm \sqrt{13}}{2}$.
(4) $x = 2^{\frac{1 \pm \sqrt{13}}{2}}$.

$x^{\log_3 x} = 9x$.
(1) $\log_3(x^{\log_3 x}) = \log_3(9x)$ → $(\log_3 x)^2 = 2 + \log_3 x$.
(2) $t^2 - t - 2 = 0$ → $t = -1, 2$ → $x = \frac{1}{3}, 9$.

---

## Part D: Exponents and Logs in the Real World

---

## Example 17: Compound Interest and Continuous Compounding

**Ordinary compound interest**: $A = P\left(1 + \frac{r}{n}\right)^{nt}$.
$n$ = number of compoundings per year. As $n \to \infty$, continuous compounding: $A = Pe^{rt}$.

1,000,000 won, 5%, 3 years.
Yearly ($n=1$): $100(1.05)^3 = 115.76$ ten-thousands.
Quarterly ($n=4$): $100\left(1 + \frac{0.05}{4}\right)^{12} = 116.08$ ten-thousands.
Continuous: $100 \cdot e^{0.15} = 116.18$ ten-thousands.

---

## Example 18: Half-Life and Doubling Time

**Half-life** $t_{1/2}$: time for quantity to halve.
$N(t) = N_0 e^{-kt}$, $k = \frac{\ln 2}{t_{1/2}}$.

Carbon-14 half-life = 5730 years. $k = \frac{\ln 2}{5730} \approx 0.000121$.
From 100g to 25g = 2 half-lives = 11460 years.

**Doubling time** $t_2 = \frac{\ln 2}{r}$.
7% annual growth: $t_2 = \frac{\ln 2}{0.07} \approx 9.9$ years. Doubles every 10 years.

---

## Example 19: pH, Decibels, Richter Scale — All Log Scales!

**pH**: $\text{pH} = -\log[\text{H}^+]$.
Neutral: $[\text{H}^+] = 10^{-7}$ → pH = 7.
Acidic: $[\text{H}^+] = 10^{-3}$ → pH = 3. pH drops by 1 = H+ concentration ×10.

**Decibels (dB)**: $\beta = 10\log\frac{I}{I_0}$.
$I_0 = 10^{-12}$ W/m² (threshold of hearing).
Conversation (50dB): $I = 10^{-7}$. Concert (110dB): $I = 10^{-1}$. 60dB difference = million-fold.

**Richter scale**: $M = \log\frac{A}{A_0}$.
Magnitude 5 → 6: amplitude ×10, energy ≈ ×32.

---

## Example 20: Exponential Growth vs. Log Growth

Exponential $2^x$: $x=10$ → 1024. $x=20$ → about 1,000,000. Explosive.
Logarithmic $\log_2 x$: $x=1024$ → 10. $x=$1,000,000 → about 20. Sluggish.

When data spans a huge range, use log scale:
1, 10, 100, 1000 → on log scale: 0, 1, 2, 3 — evenly spaced.

![Comparing log bases](graphs/10d-log-bases.png)

> **Up to here**: Compound interest, half-life, pH, dB, Richter — all applications of exponents and logs.
> Log scales compress wide ranges.

---

## Visual Interlude: The Log Scale — Compressing the Universe

A linear scale places 1, 2, 3, 4 at equal intervals. A log scale places 1, 10, 100, 1000 at equal intervals.

**Why this matters**: On a linear scale, the difference between 1 and 2 looks the same as the difference between 1001 and 1002.
On a log scale, 1 and 10 are as far apart as 1000 and 10000 — because both jumps are a factor of 10.

![Linear scale](graphs/10g1-linear-scale.png)

![Log scale](graphs/10g2-log-scale.png)

The entire history of the universe fits on a log scale: from Planck length ($10^{-35}$ m) to the observable universe ($10^{26}$ m) — a range of $10^{61}$.
Without log scales, we could not draw this on a single sheet of paper.

---

## Part E: Advanced Techniques — Beyond the Textbook

---

## Example 21: The Power Tower — Iterated Exponentiation (Tetration)

What is $x^{x^{x^{\cdot^{\cdot^{\cdot}}}}} = 2$? That is, an infinite stack of $x$ raised to $x$ raised to $x$...

(1) If the tower equals 2, then the whole tower *is* $x$ raised to (the tower), which equals 2.
So $x^2 = 2$ → $x = \sqrt{2}$.

(2) Check: $(\sqrt{2})^{(\sqrt{2})^{(\sqrt{2})^{\cdots}}} = 2$. Indeed it converges.

**What if the tower equals 4?** $x^4 = 4$ → $x = \sqrt[4]{4} = \sqrt{2}$. Wait — same $x$? That seems contradictory. The tower $\sqrt{2}^{\sqrt{2}^{\sqrt{2}^{\cdots}}}$ converges to 2, not 4. The equation $x^4 = 4$ gave a valid algebraic root, but the infinite tower actually converges only to values in $[e^{-e}, e^{1/e}] \approx [0.0659, 1.4447]$. So $x = \sqrt{2} \approx 1.414$ works and converges to 2. The tower does not converge to 4 from that starting value — 4 is outside the convergence range.

**Convergence condition**: The infinite tower $x^{x^{x^{\cdot^{\cdot^{\cdot}}}}}$ converges if and only if $e^{-e} \leq x \leq e^{1/e}$ (Euler, 1783). When it converges, the limit $L$ satisfies $x^L = L$.

**Special trick**: The maximum convergent value is $e$. At $x = e^{1/e}$, the limit is exactly $e$.

---

## Example 22: The Lambert $W$ Function — Solving $x e^x = k$

The equation $x e^x = 5$ cannot be solved with elementary functions. The Lambert $W$ function is defined as the inverse of $f(x) = x e^x$:
$W(k)$ is the solution to $W e^W = k$.

**Example**: $x \cdot 2^x = 3$.
(1) Rewrite $2^x = e^{x\ln 2}$. Then $x e^{x\ln 2} = 3$.
(2) Multiply both sides by $\ln 2$: $(x\ln 2) e^{x\ln 2} = 3\ln 2$.
(3) Now it is $u e^u = 3\ln 2$, where $u = x\ln 2$.
(4) $u = W(3\ln 2)$ → $x = \frac{W(3\ln 2)}{\ln 2}$.

**Example**: $x^x = 7$.
(1) $x^x = e^{x\ln x} = 7$. Take $\ln$: $x\ln x = \ln 7$.
(2) Set $u = \ln x$, so $x = e^u$: $e^u \cdot u = \ln 7$ → $u e^u = \ln 7$.
(3) $u = W(\ln 7)$ → $\ln x = W(\ln 7)$ → $x = e^{W(\ln 7)}$.
(4) Also expressible as $x = \frac{\ln 7}{W(\ln 7)}$. Numerically: $\ln 7 \approx 1.9459$, $W(1.9459) \approx 0.8689$, $x \approx 2.316$.

**The general trick for $x^x = k$**: take $\ln$, rearrange to $(\ln x) e^{\ln x} = \ln k$, then $W(\ln k) = \ln x$, so $x = e^{W(\ln k)}$.

**Another form**: $a^x = bx + c$. Rearrange to match $u e^u$ form, apply $W$.

---

## Example 23: The Log-Sum-Exp Trick (Numerical Stability)

When computing $\ln(e^{1000} + e^{1001})$ directly, $e^{1000}$ overflows double-precision floats. The log-sum-exp trick:

$\ln(e^a + e^b) = \max(a, b) + \ln\left(1 + e^{-|a-b|}\right)$.

For $a=1000, b=1001$: $\max = 1001$, $|a-b| = 1$.
$\ln(e^{1000} + e^{1001}) = 1001 + \ln(1 + e^{-1}) = 1001 + \ln(1 + 0.3679) = 1001 + 0.3133 \approx 1001.3133$.

This is how machine learning libraries compute stable softmax and cross-entropy. The small $e^{-|a-b|}$ sidesteps overflow completely. For $n$ terms: $\ln(\sum_i e^{a_i}) = \max(a_i) + \ln(\sum_i e^{a_i - \max(a_i)})$.

---

## Example 24: Logarithmic Differentiation — Tackle Messy Products and Powers

$y = x^x$. How to differentiate? Neither power rule (exponent not constant) nor exponential rule (base not constant) applies directly.

(1) Take $\ln$ of both sides: $\ln y = \ln(x^x) = x\ln x$.
(2) Differentiate implicitly: $\frac{y'}{y} = \ln x + x \cdot \frac{1}{x} = \ln x + 1$.
(3) $y' = y(\ln x + 1) = x^x(\ln x + 1)$.

More generally, for $y = f(x)^{g(x)}$:
(1) $\ln y = g(x) \ln f(x)$.
(2) $\frac{y'}{y} = g'(x)\ln f(x) + g(x)\frac{f'(x)}{f(x)}$.
(3) $y' = f(x)^{g(x)}\left[g'(x)\ln f(x) + \frac{g(x)f'(x)}{f(x)}\right]$.

**Another application**: $y = \frac{(x^2+1)^3 \sqrt{x-1}}{(x+2)^5}$.
(1) $\ln y = 3\ln(x^2+1) + \frac{1}{2}\ln(x-1) - 5\ln(x+2)$.
(2) Differentiate: $\frac{y'}{y} = \frac{6x}{x^2+1} + \frac{1}{2(x-1)} - \frac{5}{x+2}$.
(3) $y' = y \times$ (that expression). Clean one-step differentiation of a mess.

---

## Example 25: The AM–GM Inequality via Logs (Jensen)

For positive numbers $x_1, \ldots, x_n$, the arithmetic mean is at least the geometric mean:
$\frac{x_1+\cdots+x_n}{n} \geq \sqrt[n]{x_1\cdots x_n}$.

Proof via concavity of $\ln x$: $\ln x$ is concave on $(0,\infty)$. By Jensen's inequality:
$\ln\!\left(\frac{x_1+\cdots+x_n}{n}\right) \geq \frac{\ln x_1 + \cdots + \ln x_n}{n} = \ln\!\left(\sqrt[n]{x_1\cdots x_n}\right)$.

Exponentiate both sides (monotonic): $\frac{x_1+\cdots+x_n}{n} \geq \sqrt[n]{x_1\cdots x_n}$.

**Application**: Prove $a^2 + b^2 + c^2 \geq ab + bc + ca$.
By AM–GM on pairs: $\frac{a^2+b^2}{2} \geq ab$, $\frac{b^2+c^2}{2} \geq bc$, $\frac{c^2+a^2}{2} \geq ca$. Sum all three.

---

## Example 26: The Inequality $\ln(1+x) \leq x$ for $x > -1$

From the graph of $\ln(1+x)$: it lies below its tangent line $y=x$ at $x=0$.
This inequality is a workhorse of analysis.

**Proof sketch**: $\ln(1+x) = \int_0^x \frac{1}{1+t} dt \leq \int_0^x 1 dt = x$ for $x \geq 0$. For $-1 < x < 0$, the inequality still holds by concavity.

**Uses**:
- $\ln(n+1) - \ln n = \ln(1 + \frac{1}{n}) \leq \frac{1}{n}$. Summing to get a harmonic series bound.
- $\left(1 + \frac{1}{n}\right)^n \leq e$. Because $n\ln(1+\frac{1}{n}) \leq n \cdot \frac{1}{n} = 1$, exponentiate.
- For any $\varepsilon > 0$, $\ln x \leq \frac{x^\varepsilon - 1}{\varepsilon}$. A generalization via convexity.
- Sandwich: $\frac{x}{1+x} \leq \ln(1+x) \leq x$ for $x > -1$ (the left side follows from $\ln(1+x) = -\ln(\frac{1}{1+x})$).

---

## Example 27: Benford's Law — Why 1 Appears Most Often as the First Digit

In many real-world datasets (populations, stock prices, physical constants), the first digit $d$ occurs with probability $P(d) = \log_{10}\!\left(1 + \frac{1}{d}\right)$.

$P(1) \approx 30.1\%$, $P(2) \approx 17.6\%$, ..., $P(9) \approx 4.6\%$.

Why? A dataset whose log values are uniformly distributed (scale-invariant) produces this distribution. The mantissa of $\log_{10} x$ (the fractional part) determines the first digit. If the mantissa is uniformly distributed in $[0,1)$, then the probability of first digit $d$ is $\log_{10}(d+1) - \log_{10}(d) = \log_{10}\!\left(1 + \frac{1}{d}\right)$.

This is used to detect **fraud**: people fabricating numbers tend to distribute first digits uniformly; real data follows Benford.

---

## Example 28: Solving $a^b = b^a$ Type Equations

The equation $x^y = y^x$ for $x \neq y$ has nontrivial positive solutions. Take $\ln$:
$y\ln x = x\ln y$ → $\frac{\ln x}{x} = \frac{\ln y}{y}$.

So $x$ and $y$ are two points where $f(t) = \frac{\ln t}{t}$ takes the same value.

$f(t)$ increases on $(0, e]$, peaks at $t=e$ with $f(e)=1/e$, then decreases. For any $u \in (0, 1/e)$, there are two solutions $t_1 < e < t_2$ with $f(t_1) = f(t_2) = u$.

**Only integer solution with $x \neq y$**: $2^4 = 4^2 = 16$. Because $f(2) = f(4) = \frac{\ln 2}{2}$.

**Parametric form**: Let $y = tx$. Then $x^{tx} = (tx)^x$ → $x^t = tx$ → $x = t^{1/(t-1)}$, $y = t^{t/(t-1)}$. For rational $t$, this often generates integer pairs. $t=2$ gives $(2,4)$.

---

## Example 29: Stirling's Approximation — Factorials via Logs

$\ln(n!) = \sum_{k=1}^n \ln k$. Approximate by an integral:
$\ln(n!) \approx n\ln n - n + O(\ln n)$.

Stirling's formula: $n! \approx \sqrt{2\pi n} \left(\frac{n}{e}\right)^n$.

**Application**: How many digits in $100!$?
$\log_{10}(100!) \approx 100\ln(100)/\ln(10) - 100/\ln(10) + \tfrac{1}{2}\log_{10}(200\pi)$.
$\log_{10}(100!) \approx 157.97$. So $100!$ has 158 digits.

This log-integral technique is the only practical way to estimate huge factorials.

---

## Example 30: The Sophomore's Dream — When a Series Swaps Sum and Integral

The identity $\int_0^1 x^{-x} dx = \sum_{n=1}^\infty n^{-n}$ connects integration and infinite series.
Write $x^{-x} = e^{-x\ln x} = \sum_{n=0}^\infty \frac{(-x\ln x)^n}{n!}$.
Integrate term by term: $\int_0^1 (-x\ln x)^n dx = \frac{n!}{(n+1)^{n+1}}$.
The sum telescopes beautifully to $\sum_{n=1}^\infty n^{-n} \approx 1.29129$.

Similarly: $\int_0^1 x^x dx = \sum_{n=1}^\infty (-1)^{n+1} n^{-n}$.

These are rare cases where $x^x$ — which normally requires Lambert $W$ — yields an exact series solution through interchange of sum and integral.

---

## Part F: Ultimate Equation and Inequality Decision Tree

> For any exponent or log problem, pick your weapon using the decision tree below.

---

## Decision Tree — Equations

```
You encounter an exponential or logarithmic equation:
├── (1) Same base on both sides?
│   ├── YES → Set exponents equal: a^{f(x)} = a^{g(x)} → f = g
│   └── NO → Try to unify bases. If not possible:
│       ├── Bases like 2,4,8... or 3,9,27... → Unify possible
│       └── Bases with different primes (2 vs 3) → Take log/ln on both sides
├── (2) Does a^x repeat?
│   └── YES → Substitute t = a^x (t > 0). Solve the resulting quadratic/polynomial.
├── (3) Multiple log_a(...) terms?
│   ├── Sum/difference → Combine: log M + log N = log(MN)
│   └── log_a f(x) = number → a^{number} = f(x)
├── (4) (log x)^2 form?
│   └── YES → Substitute t = log x. Solve quadratic/polynomial.
├── (5) x in both exponent and base? (e.g., x^{log x})
│   └── YES → Take log of both sides. log(x^{log x}) = (log x)^2.
├── (6) x^x = k or x e^x = k?
│   └── YES → Rearrange to u e^u form. Use Lambert W.
├── (7) Power tower / tetration?
│   └── YES → x^{tower} = tower → x^{result} = result.
└── (8) Still stuck?
    └── Graph both sides. Count intersections. Numerical approximation.
```

---

## Example 31: Decision Tree in Action — Classify Before Solving

**Type 1 — Base unification**: $2^{x+2} = 4^{x-1}$ → $2^{x+2} = 2^{2x-2}$ → $x+2=2x-2$ → $x=4$.

**Type 2 — $t$-substitution**: $9^x - 4\cdot3^x + 3 = 0$.
$t=3^x$ → $t^2-4t+3=0$ → $t=1,3$ → $x=0,1$.

**Type 3 — Log combining**: $\log_2 x + \log_2(x-2) = 3$.
$\log_2[x(x-2)]=3$ → $x(x-2)=8$ → $x^2-2x-8=0$ → $x=4$ ($x=-2$ discarded).

**Type 4 — Log substitution**: $(\log_3 x)^2 - 2\log_3 x - 3 = 0$.
$t=\log_3 x$ → $t^2-2t-3=0$ → $t=-1,3$ → $x=\frac{1}{3}, 27$.

**Type 5 — $\ln$ on both sides**: $2^{x} = 5^{x-1}$.
$x\ln 2 = (x-1)\ln 5$ → $x(\ln 2 - \ln 5) = -\ln 5$ → $x = \frac{\ln 5}{\ln 5 - \ln 2}$.

**Type 6 — $x^{\log}$ form**: $x^{\log_3 x} = 9x$.
Take $\log_3$ → $(\log_3 x)^2 = 2 + \log_3 x$ → $t^2-t-2=0$ → $t=-1,2$ → $x=\frac{1}{3}, 9$.

**Type 7 — Lambert W**: $x \cdot 2^x = 5$.
$(x\ln 2) e^{x\ln 2} = 5\ln 2$ → $x = \frac{W(5\ln 2)}{\ln 2}$.

**Type 8 — Power tower**: $x^{x^{x^{\cdots}}} = 3$.
$x^3 = 3$ → $x = \sqrt[3]{3}$. (Check convergence: $\sqrt[3]{3} \approx 1.442 < e^{1/e} \approx 1.445$, so it converges.)

---

## Decision Tree — Inequalities

```
You encounter an exponential or logarithmic inequality:
├── (1) Exponential inequality?
│   ├── Base > 1 → Keep sign: a^f > a^g → f > g
│   ├── 0 < base < 1 → Flip sign: a^f > a^g → f < g
│   └── a^f > (different base) → Unify base or take log
├── (2) Logarithmic inequality?
│   ├── Base > 1 → Keep sign + enforce argument > 0
│   ├── 0 < base < 1 → Flip sign + enforce argument > 0
│   └── log f(x) > log g(x) → f > g > 0 (base>1) or 0 < f < g (base<1)
├── (3) Substitutable via a^x = t?
│   └── t > 0 constraint → t range → x range
├── (4) Quadratic in log or a^x?
│   └── Solve the inequality for t, then map back.
└── (5) Graph to confirm:
    └── Sketch y = a^x or y = log_a x. Compare heights.
```

---

## Example 32: Inequality Decision Tree in Action

**Base > 1 log inequality**: $\log_3(x^2-1) > \log_3(x+5)$.
(1) Base > 1 → $x^2-1 > x+5$ AND both arguments > 0.
(2) $x^2-x-6 > 0$ → $(x-3)(x+2) > 0$ → $x < -2$ or $x > 3$.
(3) Arguments: $x^2-1>0$ → $|x|>1$. $x+5>0$ → $x>-5$.
(4) Intersect: $(-5,-2) \cup (3,\infty)$.

**Base < 1 exponential inequality**: $\left(\frac{1}{3}\right)^{2x-1} > 9$.
(1) $9 = 3^2 = \left(\frac{1}{3}\right)^{-2}$.
(2) Base $\frac{1}{3} < 1$ → $2x-1 < -2$ → $2x < -1$ → $x < -\frac{1}{2}$.

**Mixed-base inequality**: $2^x < 3^{x-1}$.
(1) Take $\ln$: $x\ln 2 < (x-1)\ln 3$.
(2) $x\ln 2 - x\ln 3 < -\ln 3$ → $x(\ln 2 - \ln 3) < -\ln 3$.
(3) $\ln 2 - \ln 3 < 0$, divide and flip: $x > \frac{-\ln 3}{\ln 2 - \ln 3} = \frac{\ln 3}{\ln 3 - \ln 2}$.

**Quadratic log inequality**: $(\log_2 x)^2 - 3\log_2 x + 2 < 0$.
(1) $t = \log_2 x$: $t^2 - 3t + 2 < 0$ → $(t-1)(t-2) < 0$ → $1 < t < 2$.
(2) $1 < \log_2 x < 2$ → $2^1 < x < 2^2$ → $2 < x < 4$.

---

## Advanced Algebra Drill — Exponents and Logs (6 Problems)

> Intensive computation. These target the intermediate steps most students skip. Work each one fully.

**A1.** Simplify $\frac{2^{n+3} - 2^{n+1}}{2^{n}}$. Express as an integer.

**A2.** Solve for $x$: $3^{2x} \cdot 9^{1-x} = \frac{1}{27}$.

**A3.** Simplify $\log_2 48 - \log_2 3$. Express as a rational number.

**A4.** Compute $\log_2 5 \cdot \log_5 8 \cdot \log_8 3 \cdot \log_3 16$. (Hint: chain the change-of-base formula.)

**A5.** Simplify $\frac{\log_3 16}{\log_9 4}$. Express as a rational number.

**A6.** Write $\ln\!\left(\frac{e^3 \sqrt{e}}{e^{-2}}\right)$ as a single simplified number.

**A7.** Solve $\log_2(x-3) + \log_2(x+1) = 3$. Check all arguments after solving.

**A8.** Chain-simplify: $\log_3 2 \cdot \log_4 3 \cdot \log_5 4 \cdot \log_6 5 \cdot \log_7 6 \cdot \log_8 7$. Express as a rational number. (Hint: telescope via change-of-base.)

> Solutions: [Solutions](solutions/10-solutions.md#advanced-drill)

---

## Common Mistakes

### Mistake 1: Tearing $\log(x+y)$ as $\log x + \log y$

**Wrong path**: "$\log(x+y) = \log x + \log y$."

**Why wrong**: $\log(xy) = \log x + \log y$. A sum inside the log cannot be torn apart this way.

**Right path**: Only $\log(xy)$ splits into $\log x + \log y$. For $\log(x+y)$, leave it alone or factor if possible.

---

### Mistake 2: Forgetting the argument condition in log equations

**Wrong path**: "$\log_2(x-1) + \log_2(x+3) = 3$ → $x^2+2x-3=8$ → $x = \ldots$" (without checking).

**Why wrong**: Solutions must satisfy $x-1 > 0$ AND $x+3 > 0$. Any root violating this is invalid.

**Right path**: Solve the equation, then filter roots by argument > 0.

---

### Mistake 3: $a^0 = 0$

**Wrong path**: "$2^0 = 0$."

**Why wrong**: Any nonzero number to the zero power equals 1. $a^0 = 1$ ($a \neq 0$).

**Right path**: $2^0 = 1$, $10^0 = 1$, $e^0 = 1$.

---

### Mistake 4: $(e^x)^2 = e^{x^2}$

**Wrong path**: "$(e^x)^2 = e^{x^2}$."

**Why wrong**: Multiply the exponents when raising a power to a power: $(a^m)^n = a^{mn}$. So $(e^x)^2 = e^{2x}$. The expression $e^{x^2}$ is a different function — $e$ raised to $x^2$ — not the square of $e^x$.

**Right path**: $(e^x)^2 = e^{2x}$. Keep the two forms separate: $(e^x)^2$ squares after exponentiating; $e^{x^2}$ squares before exponentiating.

---

### Mistake 5: $\log_a(b-c) = \log_a b - \log_a c$

**Wrong path**: "$\log_2(8-2) = \log_2 8 - \log_2 2 = 3-1 = 2$."

**Why wrong**: $\log_2(8-2) = \log_2 6 \approx 2.585$, not 2. The log rules apply to multiplication/division inside the argument, never addition/subtraction.

**Right path**: $\log_a(b/c) = \log_a b - \log_a c$ is valid. $\log_a(b-c)$ has no simple expansion.

---

## What We Just Did

```
(1) Exponent rules — 5 laws for multiplying, dividing, and powering.
    Log rules — product becomes sum, quotient becomes difference, power pulls out.
    ln uses base e, log uses base 10. The two are mirror images across y = x.

(2) Equation types — unify bases first. If bases differ, take ln of both sides.
    Repeated a^x → t-substitution (t > 0). Multiple logs → combine into one.
    (log x)^2 form → t = log x. x in both exponent and base → take log of both sides.
    Inequality types — base > 1 keeps the sign. Base < 1 flips the sign.
    Always check arg > 0 for log inequalities.

(3) Advanced tools — Lambert W for x e^x and x^x. Power tower convergence.
    Log-differentiation for f(x)^{g(x)}. ln(1+x) ≤ x and the AM–GM proof.
    Real-world: half-life, compound interest, pH, dB, Richter scale.
```

---

## Practice 1

$2^{x+1} = 8^{x-2}$. Unify to base 2.

→ Reference: **Example 4**

> Solutions: [Solutions](solutions/10-solutions.md#practice-1)

---

## Practice 2

$\log_3(2x-1) - \log_3(x+1) = 1$. Log subtraction = division. Check arguments!

→ Reference: **Example 13**

> Solutions: [Solutions](solutions/10-solutions.md#practice-2)

---

## Practice 3

$4^x - 2^{x+2} - 32 = 0$. Substitute $t = 2^x$.

→ Reference: **Example 5**

> Solutions: [Solutions](solutions/10-solutions.md#practice-3)

---

## Practice 4: Composition

$2^a = 3$ and $3^b = 2$. Show that $ab = 1$.
Then check $5^c = 7$ and $7^d = 5$ for the same relationship.
State the general rule in words.

→ Reference: **Example 7, 9**

> Solutions: [Solutions](solutions/10-solutions.md#practice-4)

---

## Practice 5

$x^{\log_2 x} = 8x$. Take $\log_2$ of both sides.

→ Reference: **Example 16**

> Solutions: [Solutions](solutions/10-solutions.md#practice-5)

---

## Practice 6: Real Battle

A radioactive substance decays 8% per year. Starting with 500g, find when it falls below 100g.
$500(0.92)^t < 100$. Take $\log$ of both sides.

→ Reference: **Example 18**

> Solutions: [Solutions](solutions/10-solutions.md#practice-6)

---

## Practice 7

$3^{x+2} - 3^{x} = 72$. Factor out $3^x$.

→ Reference: **Example 5**

> Solutions: [Solutions](solutions/10-solutions.md#practice-7)

---

## Practice 8

$\log_2(x^2 - 3x) = 2$. Remove the log and check arguments.

→ Reference: **Example 7, 12**

> Solutions: [Solutions](solutions/10-solutions.md#practice-8)

---

## Practice 9: Composition

Invent two different exponential equations where the substitution $t = 2^x$ leads to $t^2 - 6t + 8 = 0$.
Solve both and explain why they both reduce to the same quadratic.

→ Reference: **Example 5**

> Solutions: [Solutions](solutions/10-solutions.md#practice-9)

---

## Practice 10

$\log_{\frac{1}{2}}(3x+1) \geq -2$. Handle base < 1 and argument > 0.

→ Reference: **Example 12**

> Solutions: [Solutions](solutions/10-solutions.md#practice-10)

---

## Practice 11

$x \cdot 3^x = 9$. Use the Lambert $W$ technique:
rewrite $3^x = e^{x\ln 3}$, multiply by $\ln 3$, match $u e^u$ form.

→ Reference: **Example 22**

> Solutions: [Solutions](solutions/10-solutions.md#practice-11)

---

## Practice 12: Real Battle

Show that the infinite power tower $x^{x^{x^{\cdot^{\cdot^{\cdot}}}}}$ converges only for $e^{-e} \leq x \leq e^{1/e}$.
Then solve $x^{x^{x^{\cdot^{\cdot^{\cdot}}}}} = y$ for $x$ in terms of $y$, and evaluate for $y = e$.
Hint: if the limit is $L$, then $x^L = L$, so $x = L^{1/L}$.

→ Reference: **Example 21**

> Solutions: [Solutions](solutions/10-solutions.md#practice-12)

---

## Today's Procedure

```
Step 1: Apply the rules — multiply→add exponents, divide→subtract exponents,
         power→multiply exponents. Log of product→sum of logs.
         Log of quotient→difference of logs. Log of power→pull exponent out.

Step 2: Choose your weapon — same base? equate exponents. Different bases?
         take ln. Repeated a^x? t-substitution. Multiple logs? combine.
         Base>1? keep inequality. Base<1? flip inequality.
         Always check argument > 0.

Step 3: Extend — Lambert W for unsolvable exponentials. Power towers converge
         only for x in [e^{-e}, e^{1/e}]. Log-differentiate to handle x^x.
         Apply to half-life, pH, dB, compound interest.
```

---

## Terminology

Up to now we used plain words like "exponent", "base", "argument", "take log", "half-life".
**You have already learned all the methods.** Now we attach the formal mathematical names.

| What we called it | Mathematical term | Notation / Explanation |
|:-----------------:|:-----------------:|:----------------------:|
| exponent | exponent | $a^n$ — the $n$ |
| base | base | $a^n$ or $\log_a b$ — the $a$ |
| argument (of log) | argument | $\log_a b$ — the $b$ |
| root / radical | radical | $\sqrt[n]{a}$ |
| reciprocal | reciprocal | $a^{-1} = 1/a$ |
| take the log | take logarithm | apply $\log$ or $\ln$ to both sides |
| change of base | change of base | $\log_a b = \frac{\log_c b}{\log_c a}$ |
| natural log | natural logarithm | $\ln x = \log_e x$ |
| common log | common logarithm | $\log x = \log_{10} x$ |
| continuous compounding | continuous compound interest | $A = Pe^{rt}$ |
| half-life | half-life | $t_{1/2} = \ln 2 / k$ |
| doubling time | doubling time | $t_2 = \ln 2 / r$ |
| pH | pH (hydrogen ion concentration) | $\text{pH} = -\log[\text{H}^+]$ |
| decibel | decibel | $\beta = 10\log(I/I_0)$ |
| Euler's number | Euler's number | $e \approx 2.718281828$ |
| tetration | tetration / power tower | $^{n}a = a^{a^{\cdot^{\cdot^{a}}}}$ ($n$ times) |
| Lambert W function | Lambert $W$ function | $W(x)$ solves $W e^W = x$ |
| log-sum-exp | log-sum-exp trick | $\ln(e^a+e^b) = \max(a,b) + \ln(1+e^{-|a-b|})$ |
| logarithmic differentiation | logarithmic differentiation | Take $\ln$ then differentiate implicitly |
| Benford's Law | Benford's Law | $P(d) = \log_{10}(1 + 1/d)$ for first digit $d$ |
| Stirling's approximation | Stirling's approximation | $n! \approx \sqrt{2\pi n}(n/e)^n$ |
