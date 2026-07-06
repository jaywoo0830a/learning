# Solutions: 10A — Exponents and Logarithms Core

---

## Practice 1

> $2^{x+1} = 8^{x-2}$. Unify to base 2.

(1) $8 = 2^3$. → $2^{x+1} = (2^3)^{x-2} = 2^{3x-6}$.
(2) $x+1 = 3x-6$ → $7 = 2x$ → $x = \frac{7}{2}$.

→ **$x = \frac{7}{2}$.**

---

## Practice 2

> $\log_3(2x-1) - \log_3(x+1) = 1$.

(1) Log subtraction = division: $\log_3 \frac{2x-1}{x+1} = 1$.
(2) Remove log: $\frac{2x-1}{x+1} = 3^1 = 3$.
(3) $2x-1 = 3(x+1)$ → $2x-1 = 3x+3$ → $-4 = x$ → $x = -4$.

(4) Argument check:
$2x-1 > 0$ → $-8-1 = -9 < 0$. **Fail**.
$x+1 > 0$ → $-4+1 = -3 < 0$. **Fail**.

→ **No solution.**

---

## Practice 3

> $4^x - 2^{x+2} - 32 = 0$.

(1) $4^x = (2^2)^x = 2^{2x}$. $2^{x+2} = 4 \cdot 2^x$.
(2) $2^{2x} - 4 \cdot 2^x - 32 = 0$.
(3) $t = 2^x$ ($t > 0$): $t^2 - 4t - 32 = 0$.
(4) $(t-8)(t+4) = 0$ → $t = 8$ or $t = -4$.
(5) $t > 0$ → discard $t = -4$. $t = 8$.
(6) $2^x = 8 = 2^3$ → $x = 3$.

→ **$x = 3$.**

---

## Practice 4: Composition

> $2^a = 3$, $3^b = 2$. Show $ab = 1$. Check $5^c = 7$, $7^d = 5$. State the general rule.

(1) $\log_2 3 = a$. $\log_3 2 = b$.
(2) Change of base: $\log_3 2 = \frac{\log_2 2}{\log_2 3} = \frac{1}{\log_2 3}$ → $b = \frac{1}{a}$.
(3) Therefore $ab = 1$.

(4) For $5^c = 7$ and $7^d = 5$: $c = \log_5 7$, $d = \log_7 5 = \frac{1}{\log_5 7}$. So $cd = 1$.

(5) General rule: If $x^p = y$ and $y^q = x$ with $x, y > 0$ and $x, y \neq 1$, then $pq = 1$.
Because $\log_x y = p$ and $\log_y x = q = \frac{1}{\log_x y} = \frac{1}{p}$.

---

## Practice 5

> $x^{\log_2 x} = 8x$. Take $\log_2$ of both sides.

(1) $\log_2(x^{\log_2 x}) = \log_2(8x)$.
(2) Left: $(\log_2 x)(\log_2 x) = (\log_2 x)^2$.
(3) Right: $\log_2 8 + \log_2 x = 3 + \log_2 x$.
(4) $t = \log_2 x$: $t^2 = 3 + t$ → $t^2 - t - 3 = 0$.
(5) $t = \frac{1 \pm \sqrt{13}}{2}$.
(6) $x = 2^t = 2^{\frac{1 \pm \sqrt{13}}{2}}$.

Argument: $x > 0$ for $\log_2 x$. Both $2^{\frac{1 \pm \sqrt{13}}{2}} > 0$. Both valid.

→ **$x = 2^{\frac{1 + \sqrt{13}}{2}}$ or $x = 2^{\frac{1 - \sqrt{13}}{2}}$.**

---

## Practice 6

> $3^{x+2} - 3^{x} = 72$. Factor out $3^x$.

(1) $3^{x+2} = 3^2 \cdot 3^x = 9 \cdot 3^x$.
(2) $9 \cdot 3^x - 3^x = 72$ → $8 \cdot 3^x = 72$.
(3) $3^x = 9$ → $3^x = 3^2$ → $x = 2$.

→ **$x = 2$.**

---

## Practice 7

> $\log_2(x^2 - 3x) = 2$. Remove the log and check arguments.

(1) Remove log: $x^2 - 3x = 2^2 = 4$.
(2) $x^2 - 3x - 4 = 0$ → $(x-4)(x+1) = 0$ → $x = 4$ or $x = -1$.
(3) Argument check: $x^2 - 3x > 0$ → $x(x-3) > 0$ → $x < 0$ or $x > 3$.
(4) $x = -1$: $(-1)^2 - 3(-1) = 4 > 0$. Valid.
(5) $x = 4$: $16 - 12 = 4 > 0$. Valid.

→ **$x = -1$ or $x = 4$.**

---

## Practice 8: Composition

> Invent two different exponential equations where $t = 2^x$ leads to $t^2 - 6t + 8 = 0$.

**Equation A**: $4^x - 6 \cdot 2^x + 8 = 0$.
(1) $4^x = (2^2)^x = 2^{2x} = (2^x)^2 = t^2$.
(2) Substitute: $t^2 - 6t + 8 = 0$ → $(t-2)(t-4) = 0$ → $t = 2, 4$.
(3) $2^x = 2$ → $x = 1$. $2^x = 4$ → $x = 2$.

**Equation B**: $2^{2x+2} - 24 \cdot 2^x + 32 = 0$.
(1) $2^{2x+2} = 2^2 \cdot 2^{2x} = 4(2^x)^2 = 4t^2$.
(2) $4t^2 - 24t + 32 = 0$ → divide by 4: $t^2 - 6t + 8 = 0$.
(3) Same quadratic → $t = 2, 4$ → $x = 1, 2$.

**Why they reduce to the same quadratic**: Both are built around $2^x$. Any equation of the form $A \cdot 2^{2x} + B \cdot 2^x + C = 0$ with $\frac{B}{A} = -6$ and $\frac{C}{A} = 8$ reduces to $t^2 - 6t + 8 = 0$ after appropriate scaling.

---

## Practice 9

> $\log_{\frac{1}{2}}(3x+1) \geq -2$. Handle base < 1 and argument > 0.

(1) $-2 = \log_{\frac{1}{2}}\!\left(\left(\frac{1}{2}\right)^{-2}\right) = \log_{\frac{1}{2}} 4$.
(2) Base $\frac{1}{2} < 1$ → flip inequality: $3x+1 \leq 4$.
(3) $3x \leq 3$ → $x \leq 1$.
(4) Argument > 0: $3x+1 > 0$ → $x > -\frac{1}{3}$.
(5) Intersect: $-\frac{1}{3} < x \leq 1$.

→ **$x \in \left(-\frac{1}{3}, 1\right]$.**

---

## Practice 10: Real Battle

> $25^x + 5^{x+1} - 6 = 0$. Unify to base 5, then use $t = 5^x$.

(1) $25^x = (5^2)^x = 5^{2x} = (5^x)^2$. $5^{x+1} = 5 \cdot 5^x$.
(2) Let $t = 5^x$ ($t > 0$): $t^2 + 5t - 6 = 0$.
(3) $(t+6)(t-1) = 0$ → $t = -6$ or $t = 1$.
(4) $t > 0$ → $t = 1$. $5^x = 1$ → $x = 0$.

→ **$x = 0$.**

---

## Basic Drill

### D1. $3^4 \cdot 3^{-2}$
$3^4 \cdot 3^{-2} = 3^{4+(-2)} = 3^2 = 9$. → **9.**

### D2. $\frac{5^6}{5^2}$
$\frac{5^6}{5^2} = 5^{6-2} = 5^4 = 625$. → **625.**

### D3. $(2^3)^2$
$(2^3)^2 = 2^{3 \times 2} = 2^6 = 64$. → **64.**

### D4. $16^{-\frac{1}{2}}$
$16^{-\frac{1}{2}} = \frac{1}{16^{\frac{1}{2}}} = \frac{1}{\sqrt{16}} = \frac{1}{4}$. → **$\frac{1}{4}$.**

### D5. $27^{\frac{2}{3}}$
$27^{\frac{2}{3}} = (\sqrt[3]{27})^2 = 3^2 = 9$. → **9.**

### D6. $\frac{10^4 \cdot 10^{-1}}{10^2}$
$\frac{10^4 \cdot 10^{-1}}{10^2} = \frac{10^3}{10^2} = 10^{3-2} = 10$. → **10.**

### D7. $\left(\frac{8}{27}\right)^{-\frac{2}{3}}$
Flip and make exponent positive: $\left(\frac{27}{8}\right)^{\frac{2}{3}} = \left(\sqrt[3]{\frac{27}{8}}\right)^2 = \left(\frac{3}{2}\right)^2 = \frac{9}{4}$. → **$\frac{9}{4}$.**

### D8. $\log_5 125 + \log_5 \frac{1}{5}$
$\log_5 125 = 3$, $\log_5 \frac{1}{5} = -1$. Sum: $3 + (-1) = 2$. → **2.**

### D9. $\log_3 27 - \log_3 \frac{1}{9}$
$\log_3 27 = 3$, $\log_3 \frac{1}{9} = -2$. Difference: $3 - (-2) = 5$. → **5.**

### D10. $\ln e^5 + \ln 1 - \ln e^{-2}$
$\ln e^5 = 5$, $\ln 1 = 0$, $\ln e^{-2} = -2$. Result: $5 + 0 - (-2) = 7$. → **7.**

---

## Advanced Drill

### A1. $2^{x+2} + 2^{x} = 40$
(1) $2^{x+2} = 4 \cdot 2^x$. So $4 \cdot 2^x + 2^x = 40$ → $5 \cdot 2^x = 40$.
(2) $2^x = 8 = 2^3$ → $x = 3$. → **$x=3$.**

### A2. $9^{x} - 3^{x+1} + 2 = 0$
(1) $9^x = (3^2)^x = 3^{2x} = (3^x)^2 = t^2$. $3^{x+1} = 3 \cdot 3^x = 3t$.
(2) $t^2 - 3t + 2 = 0$ → $(t-1)(t-2) = 0$ → $t = 1, 2$.
(3) $3^x = 1$ → $x = 0$. $3^x = 2$ → $x = \log_3 2$.
→ **$x = 0$ or $x = \log_3 2$.**

### A3. $\log_4(x+3) + \log_4(x-3) = 2$
(1) Combine: $\log_4[(x+3)(x-3)] = 2$.
(2) $(x+3)(x-3) = 4^2 = 16$ → $x^2 - 9 = 16$ → $x^2 = 25$ → $x = \pm 5$.
(3) Arguments: $x+3 > 0 \implies x > -3$, $x-3 > 0 \implies x > 3$. Combined: $x > 3$.
(4) $x = -5$ discarded. $x = 5$ valid. → **$x = 5$.**

### A4. $\left(\frac{1}{3}\right)^{2x-1} < \frac{1}{9}$
(1) $\frac{1}{9} = \left(\frac{1}{3}\right)^2$. Base $\frac{1}{3} < 1$ → flip inequality.
(2) $2x - 1 > 2$ → $2x > 3$ → $x > \frac{3}{2}$. → **$x > \frac{3}{2}$.**

### A5. $5^{2x} - 6 \cdot 5^{x} + 5 = 0$
(1) $t = 5^x$ ($t > 0$): $t^2 - 6t + 5 = 0$ → $(t-1)(t-5) = 0$ → $t = 1, 5$.
(2) $5^x = 1$ → $x = 0$. $5^x = 5$ → $x = 1$. → **$x = 0$ or $x = 1$.**

### A6. $\log_3 8 \cdot \log_4 9 \cdot \log_2 27$
Chain to base 2: $\frac{\log_2 8}{\log_2 3} \cdot \frac{\log_2 9}{\log_2 4} \cdot \frac{\log_2 27}{\log_2 2} = \frac{3}{\log_2 3} \cdot \frac{2\log_2 3}{2} \cdot \frac{3\log_2 3}{1}$.
Simplify: $\frac{3}{\log_2 3} \cdot \log_2 3 \cdot 3\log_2 3 = 3 \cdot 1 \cdot 3\log_2 3 = 9\log_2 3$.

Wait — recheck. $\log_2 9 = 2\log_2 3$. $\log_2 4 = 2$. So $\frac{2\log_2 3}{2} = \log_2 3$.
$\log_2 27 = 3\log_2 3$. $\log_2 2 = 1$. So product: $\frac{3}{\log_2 3} \cdot \log_2 3 \cdot 3\log_2 3 = 3 \cdot 3\log_2 3 = 9\log_2 3$. That's correct — it doesn't fully telescope to an integer.

Actually let me recompute more carefully:
$\log_3 8 \cdot \log_4 9 \cdot \log_2 27 = \frac{\ln 8}{\ln 3} \cdot \frac{\ln 9}{\ln 4} \cdot \frac{\ln 27}{\ln 2} = \frac{3\ln 2}{\ln 3} \cdot \frac{2\ln 3}{2\ln 2} \cdot \frac{3\ln 3}{\ln 2}$.
$= \frac{3\ln 2}{\ln 3} \cdot \frac{\ln 3}{\ln 2} \cdot \frac{3\ln 3}{\ln 2} = 3 \cdot 1 \cdot \frac{3\ln 3}{\ln 2} = \frac{9\ln 3}{\ln 2} = 9\log_2 3$.

Hmm, that's not a clean integer. Let me design a cleaner problem. Actually let me adjust A6 to something that telescopes neatly:

Let me change A6 to: $\log_2 3 \cdot \log_3 4 \cdot \log_4 5 \cdot \log_5 8$

$\frac{\ln 3}{\ln 2} \cdot \frac{\ln 4}{\ln 3} \cdot \frac{\ln 5}{\ln 4} \cdot \frac{\ln 8}{\ln 5} = \frac{\ln 8}{\ln 2} = \frac{3\ln 2}{\ln 2} = 3$.

That telescopes! Let me fix this in the session file too. I'll update both the question and answer. 

Actually, to keep things simple: the current problem A6 in the session file is `\log_3 8 \cdot \log_4 9 \cdot \log_2 27` and the answer is `9\log_2 3`. That's a valid answer, not an integer but it's a simplified form. I could also express it differently. Let me just leave it as is and provide the solution — it's an advanced drill, so not everything needs to come out as an integer. The answer simplifies to $9\log_2 3$, which is fine.

Actually wait, the answer is $9\log_2 3$? Let me double-check the original problem: `\log_3 8 \cdot \log_4 9 \cdot \log_2 27`. I computed it as $9\log_2 3$. That seems correct. Let me provide the solution as is.

### A7. $\log_2(x^2 - 5x + 6) \leq 1$
(1) $1 = \log_2 2$. Base > 1 → $x^2 - 5x + 6 \leq 2$.
(2) $x^2 - 5x + 4 \leq 0$ → $(x-1)(x-4) \leq 0$ → $1 \leq x \leq 4$.
(3) Argument: $x^2 - 5x + 6 > 0$ → $(x-2)(x-3) > 0$ → $x < 2$ or $x > 3$.
(4) Intersect $[1,4]$ with $(-\infty,2) \cup (3,\infty)$: $[1, 2) \cup (3, 4]$.
→ **$x \in [1, 2) \cup (3, 4]$.**

### A8. $\ln(2x+1) - \ln(x-2) = 1$
(1) $\ln\frac{2x+1}{x-2} = 1$ → $\frac{2x+1}{x-2} = e$.
(2) $2x+1 = e(x-2)$ → $2x+1 = ex - 2e$ → $2x - ex = -2e - 1$ → $x(2-e) = -(2e+1)$.
(3) $x = \frac{2e+1}{e-2}$.
(4) Arguments: $2x+1 > 0$ and $x-2 > 0$ → $x > 2$. Check: $e \approx 2.718$, $x \approx \frac{6.436}{0.718} \approx 8.96 > 2$. ✅
→ **$x = \frac{2e+1}{e-2} \approx 8.96$.**

### A9. $x^{\log_3 x} = 81$
(1) Take $\log_3$: $\log_3(x^{\log_3 x}) = \log_3 81$ → $(\log_3 x)^2 = 4$.
(2) $\log_3 x = \pm 2$ → $x = 3^2 = 9$ or $x = 3^{-2} = \frac{1}{9}$.
(3) $x > 0$ for $\log_3 x$. Both valid. → **$x = 9$ or $x = \frac{1}{9}$.**

### A10. $e^{2x} - 5e^{x} + 6 = 0$
(1) $t = e^x$ ($t > 0$): $t^2 - 5t + 6 = 0$ → $(t-2)(t-3) = 0$ → $t = 2, 3$.
(2) $e^x = 2$ → $x = \ln 2$. $e^x = 3$ → $x = \ln 3$.
→ **$x = \ln 2$ or $x = \ln 3$.**
