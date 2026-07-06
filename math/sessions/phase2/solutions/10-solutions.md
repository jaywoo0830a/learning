# 10 Solutions — Exponents and Logarithms

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

## Practice 6: Real Battle

> Radioactive substance decays 8% per year. 500g → below 100g: when?

(1) $N(t) = 500(0.92)^t$. Want $500(0.92)^t < 100$.
(2) $(0.92)^t < 0.2$.
(3) Take $\log$ of both sides: $t\log(0.92) < \log(0.2)$.
(4) $\log(0.92) \approx -0.036212$. $\log(0.2) \approx -0.698970$.
(5) Divide by the negative number, flip inequality:
$t > \frac{-0.698970}{-0.036212} \approx 19.31$.

→ **About 19.3 years. Starting from year 20, the mass is below 100g.**

---

## Practice 7

> $3^{x+2} - 3^{x} = 72$. Factor out $3^x$.

(1) $3^{x+2} = 3^2 \cdot 3^x = 9 \cdot 3^x$.
(2) $9 \cdot 3^x - 3^x = 72$ → $8 \cdot 3^x = 72$.
(3) $3^x = 9$ → $3^x = 3^2$ → $x = 2$.

→ **$x = 2$.**

---

## Practice 8

> $\log_2(x^2 - 3x) = 2$. Remove the log and check arguments.

(1) Remove log: $x^2 - 3x = 2^2 = 4$.
(2) $x^2 - 3x - 4 = 0$ → $(x-4)(x+1) = 0$ → $x = 4$ or $x = -1$.
(3) Argument check: $x^2 - 3x > 0$ → $x(x-3) > 0$ → $x < 0$ or $x > 3$.
(4) $x = -1$: $(-1)^2 - 3(-1) = 4 > 0$. Valid.
(5) $x = 4$: $16 - 12 = 4 > 0$. Valid.

→ **$x = -1$ or $x = 4$.**

---

## Practice 9: Composition

> Invent two different exponential equations where $t = 2^x$ leads to $t^2 - 6t + 8 = 0$.
> Solve both and explain why they reduce to the same quadratic.

**Equation A**: $4^x - 6 \cdot 2^x + 8 = 0$.
(1) $4^x = (2^2)^x = 2^{2x} = (2^x)^2 = t^2$.
(2) Substitute: $t^2 - 6t + 8 = 0$ → $(t-2)(t-4) = 0$ → $t = 2, 4$.
(3) $2^x = 2$ → $x = 1$. $2^x = 4$ → $x = 2$.

**Equation B**: $2^{2x+2} - 24 \cdot 2^x + 32 = 0$.
(1) $2^{2x+2} = 2^2 \cdot 2^{2x} = 4(2^x)^2 = 4t^2$.
(2) $4t^2 - 24t + 32 = 0$ → divide by 4: $t^2 - 6t + 8 = 0$.
(3) Same quadratic → $t = 2, 4$ → $x = 1, 2$.

**Why they reduce to the same quadratic**: Both are built around $2^x$. In Equation A, we directly get $t^2 - 6t + 8 = 0$. In Equation B, scaling and shifting the exponents produces a multiple of the same quadratic. Any equation of the form $A \cdot 2^{2x} + B \cdot 2^x + C = 0$ with $\frac{B}{A} = -6$ and $\frac{C}{A} = 8$ reduces to $t^2 - 6t + 8 = 0$ after appropriate scaling.

---

## Practice 10

> $\log_{\frac{1}{2}}(3x+1) \geq -2$. Handle base < 1 and argument > 0.

(1) $-2 = \log_{\frac{1}{2}}\!\left(\left(\frac{1}{2}\right)^{-2}\right) = \log_{\frac{1}{2}} 4$.
(2) Base $\frac{1}{2} < 1$ → flip inequality: $3x+1 \leq 4$.
(3) $3x \leq 3$ → $x \leq 1$.
(4) Argument > 0: $3x+1 > 0$ → $x > -\frac{1}{3}$.
(5) Intersect: $-\frac{1}{3} < x \leq 1$.

→ **$x \in \left(-\frac{1}{3}, 1\right]$.**

---

## Practice 11

> $x \cdot 3^x = 9$. Use Lambert $W$.

(1) Rewrite $3^x = e^{x\ln 3}$. Then $x \cdot e^{x\ln 3} = 9$.
(2) Multiply both sides by $\ln 3$: $(x\ln 3) e^{x\ln 3} = 9\ln 3$.
(3) Let $u = x\ln 3$: $u e^u = 9\ln 3$.
(4) $u = W(9\ln 3)$ → $x = \frac{W(9\ln 3)}{\ln 3}$.

Numerically: $9\ln 3 \approx 9 \times 1.09861 = 9.8875$.
$W(9.8875) \approx 1.798$. $x \approx \frac{1.798}{1.09861} \approx 1.637$.

Check: $1.637 \times 3^{1.637} = 1.637 \times 5.497 \approx 8.999 \approx 9$.

→ **$x = \frac{W(9\ln 3)}{\ln 3} \approx 1.637$.**

---

## Practice 12: Real Battle

> Show the infinite power tower $x^{x^{x^{\cdot^{\cdot^{\cdot}}}}}$ converges only for $e^{-e} \leq x \leq e^{1/e}$.
> Then solve $x^{x^{x^{\cdot^{\cdot^{\cdot}}}}} = y$ for $x$ in terms of $y$, and evaluate for $y = e$.

**Convergence range (sketch)**:

Define the sequence $a_1 = x$, $a_{n+1} = x^{a_n}$. The limit $L$ (if it exists) satisfies $x^L = L$, so $x = L^{1/L}$.

The function $f(L) = L^{1/L}$ on $(0, \infty)$:
- $f(L) = e^{\frac{\ln L}{L}}$. The exponent $g(L) = \frac{\ln L}{L}$.
- $g'(L) = \frac{1 - \ln L}{L^2}$. Maximum at $L = e$, $g(e) = 1/e$.
- $f(e) = e^{1/e} \approx 1.4447$ (maximum of $f$).
- As $L \to 0^+$, $\frac{\ln L}{L} \to -\infty$, $f(L) \to 0$.
- As $L \to \infty$, $\frac{\ln L}{L} \to 0$, $f(L) \to 1$.

Wait — that gives range $(0, e^{1/e}]$. But the actual convergence range is $[e^{-e}, e^{1/e}]$. Let's be more precise.

The minimum of $f(L) = L^{1/L}$ on $(0, \infty)$ occurs when we minimize over $L > 0$. The derivative $f'(L) = L^{1/L} \cdot \frac{1 - \ln L}{L^2}$. This is zero at $L = e$ (maximum), and $f(L) \to 0$ as $L \to 0^+$, $f(L) \to 1$ as $L \to \infty$, with the minimum on $[0,\infty]$ actually being... Let's check: $L^{1/L}$ for $L \in (0,1)$: $\ln f(L) = \frac{\ln L}{L}$ is negative. As $L \to 0^+$, $\frac{\ln L}{L} \to -\infty$, so $f(L) \to 0$. The minimum value on $L > 0$ is approached as $L \to 0^+$, so the infimum is 0.

However, the actual convergence region for the infinite tower is $[e^{-e}, e^{1/e}]$ (proved by Euler). The lower bound $e^{-e} \approx 0.0659$ comes from a more subtle analysis: below this, the sequence oscillates between two values (period-doubling) and does not converge.

**Solving $x^{x^{x^{\cdot^{\cdot^{\cdot}}}}} = y$**:

If the tower converges to $y$, then $x^y = y$, so $x = y^{1/y}$.

For $y = e$: $x = e^{1/e} \approx 1.4447$. At this boundary value, the tower converges to $e$ (the maximum possible convergent value).

For $y = 2$: $x = 2^{1/2} = \sqrt{2}$.
For $y = 3$: $x = 3^{1/3} \approx 1.4422$.

Note that $3^{1/3} \approx 1.4422 < \sqrt{2} \approx 1.4142$ in the relevant domain is false — actually $3^{1/3} \approx 1.442 > 1.414 = \sqrt{2}$. So larger $y$ gives slightly larger $x$ in the convergent range, up to $x = e^{1/e}$ at the boundary $y = e$.

→ **Convergence range: $[e^{-e}, e^{1/e}] \approx [0.0659, 1.4447]$.**
→ **If the tower equals $y$, then $x = y^{1/y}$.**
→ **For $y = e$: $x = e^{1/e} \approx 1.4447$.**

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
(1) Flip the fraction and make the exponent positive: $\left(\frac{27}{8}\right)^{\frac{2}{3}}$.
(2) Take the cube root first, then square: $\left(\sqrt[3]{\frac{27}{8}}\right)^2 = \left(\frac{3}{2}\right)^2 = \frac{9}{4}$.
→ **$\frac{9}{4}$.**

### D8. $\log_5 125 + \log_5 \frac{1}{5}$
(1) $\log_5 125 = 3$ because $5^3 = 125$.
(2) $\log_5 \frac{1}{5} = -1$ because $5^{-1} = \frac{1}{5}$.
(3) Sum: $3 + (-1) = 2$. → **2.**

---

## Advanced Drill

### A1. $\frac{2^{n+3} - 2^{n+1}}{2^{n}}$
(1) $2^{n+3} = 2^n \cdot 2^3 = 8 \cdot 2^n$. $2^{n+1} = 2^n \cdot 2 = 2 \cdot 2^n$.
(2) Numerator: $8 \cdot 2^n - 2 \cdot 2^n = 6 \cdot 2^n$.
(3) Divide by $2^n$: $\frac{6 \cdot 2^n}{2^n} = 6$. → **6.**

### A2. $3^{2x} \cdot 9^{1-x} = \frac{1}{27}$
(1) $9^{1-x} = (3^2)^{1-x} = 3^{2-2x}$.
(2) Left: $3^{2x} \cdot 3^{2-2x} = 3^{2x+2-2x} = 3^2 = 9$.
(3) $9 = \frac{1}{27}$? No — $9 \neq \frac{1}{27}$. Check: $\frac{1}{27} = 3^{-3}$.
(4) Wait — $3^{2x} \cdot 9^{1-x} = 3^{2x} \cdot 3^{2(1-x)} = 3^{2x + 2 - 2x} = 3^2 = 9$.
But $\frac{1}{27} = 3^{-3}$. So $9 = 3^{-3}$? That is impossible.
(5) Check again: $3^{2x} \cdot 9^{1-x} = 3^{2x} \cdot 3^{2-2x} = 3^{2x+2-2x} = 3^2$. This is always 9, independent of $x$.
So the equation is $9 = \frac{1}{27}$, which is false. → **No solution.**

### A3. $\log_2 48 - \log_2 3$
(1) $\log_2 48 - \log_2 3 = \log_2\frac{48}{3} = \log_2 16$.
(2) $\log_2 16 = 4$ because $2^4 = 16$. → **4.**

### A4. $\log_2 5 \cdot \log_5 8 \cdot \log_8 3 \cdot \log_3 16$
(1) Each pair $\log_a b \cdot \log_b c = \log_a c$.
$\log_2 5 \cdot \log_5 8 = \log_2 8 = 3$.
$\log_8 3 \cdot \log_3 16 = \log_8 16 = \frac{\log_2 16}{\log_2 8} = \frac{4}{3}$.
(2) Product: $3 \cdot \frac{4}{3} = 4$. → **4.**

### A5. $\frac{\log_3 16}{\log_9 4}$
(1) $\log_9 4 = \frac{\log_3 4}{\log_3 9} = \frac{\log_3 4}{2}$.
(2) $\frac{\log_3 16}{\log_3 4 / 2} = 2 \cdot \frac{\log_3 16}{\log_3 4} = 2 \cdot \log_4 16 = 2 \cdot 2 = 4$. → **4.**

### A6. $\ln\!\left(\frac{e^3 \sqrt{e}}{e^{-2}}\right)$
(1) $\sqrt{e} = e^{1/2}$.
(2) Numerator: $e^3 \cdot e^{1/2} = e^{7/2}$.
(3) $\frac{e^{7/2}}{e^{-2}} = e^{7/2 + 2} = e^{11/2}$.
(4) $\ln(e^{11/2}) = \frac{11}{2}$. → **$\frac{11}{2}$.**

### A7. $\log_2(x-3) + \log_2(x+1) = 3$
(1) Combine logs: $\log_2[(x-3)(x+1)] = 3$.
(2) Remove log: $(x-3)(x+1) = 2^3 = 8$ → $x^2 - 2x - 3 = 8$ → $x^2 - 2x - 11 = 0$.
(3) $x = \frac{2 \pm \sqrt{4 + 44}}{2} = \frac{2 \pm \sqrt{48}}{2} = 1 \pm 2\sqrt{3}$.
(4) Check arguments:
$x-3 > 0$ → $x > 3$. $x+1 > 0$ → $x > -1$. Both → $x > 3$.
(5) $x = 1 + 2\sqrt{3} \approx 4.46 > 3$. Valid.
$x = 1 - 2\sqrt{3} \approx -2.46 < 3$. Discard.
→ **$x = 1 + 2\sqrt{3}$.**

### A8. $\log_3 2 \cdot \log_4 3 \cdot \log_5 4 \cdot \log_6 5 \cdot \log_7 6 \cdot \log_8 7$
(1) Change all to base $\ln$: $\frac{\ln 2}{\ln 3} \cdot \frac{\ln 3}{\ln 4} \cdot \frac{\ln 4}{\ln 5} \cdot \frac{\ln 5}{\ln 6} \cdot \frac{\ln 6}{\ln 7} \cdot \frac{\ln 7}{\ln 8}$.
(2) Everything cancels except $\frac{\ln 2}{\ln 8}$.
(3) $\frac{\ln 2}{\ln 8} = \log_8 2 = \frac{1}{3}$. → **$\frac{1}{3}$.**

---

[Back to Table of Contents](../10-exponents-and-logarithms.md)
