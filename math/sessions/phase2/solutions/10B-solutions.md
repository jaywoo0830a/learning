# Solutions: 10B — Exponents and Logarithms Advanced

---

## Practice 1

> Radioactive substance decays 8% per year. 500g → below 100g: when?

(1) $N(t) = 500(0.92)^t$. Want $500(0.92)^t < 100$.
(2) $(0.92)^t < 0.2$.
(3) Take $\log$ of both sides: $t\log(0.92) < \log(0.2)$.
(4) $\log(0.92) \approx -0.036212$. $\log(0.2) \approx -0.698970$.
(5) Divide by the negative number, flip inequality:
$t > \frac{-0.698970}{-0.036212} \approx 19.31$.

→ **About 19.3 years. Starting from year 20, the mass is below 100g.**

---

## Practice 2

> $x \cdot 3^x = 9$. Use Lambert $W$.

(1) Rewrite $3^x = e^{x\ln 3}$. Then $x \cdot e^{x\ln 3} = 9$.
(2) Multiply both sides by $\ln 3$: $(x\ln 3) e^{x\ln 3} = 9\ln 3$.
(3) Let $u = x\ln 3$: $u e^u = 9\ln 3$.
(4) $u = W(9\ln 3)$ → $x = \frac{W(9\ln 3)}{\ln 3}$.

Numerically: $9\ln 3 \approx 9 \times 1.09861 = 9.8875$.
$W(9.8875) \approx 1.798$. $x \approx \frac{1.798}{1.09861} \approx 1.637$.

→ **$x = \frac{W(9\ln 3)}{\ln 3} \approx 1.637$.**

---

## Practice 3: Real Battle

> Show the infinite power tower converges only for $e^{-e} \leq x \leq e^{1/e}$.
> Solve $x^{x^{x^{\cdot^{\cdot^{\cdot}}}}} = y$ for $x$ in terms of $y$, evaluate for $y = e$.

**Convergence range (sketch)**:

Define $a_1 = x$, $a_{n+1} = x^{a_n}$. The limit $L$ (if it exists) satisfies $x^L = L$, so $x = L^{1/L}$.

The function $f(L) = L^{1/L} = e^{\frac{\ln L}{L}}$ has $f'(L) = L^{1/L} \cdot \frac{1-\ln L}{L^2}$. The maximum is at $L = e$: $f(e) = e^{1/e} \approx 1.4447$. As $L \to 0^+$, $f(L) \to 0$. As $L \to \infty$, $f(L) \to 1$.

The full convergence region is $[e^{-e}, e^{1/e}] \approx [0.0659, 1.4447]$ (Euler). Below $e^{-e}$, the sequence oscillates without converging.

**Solving for $x$**:

If the tower converges to $y$, then $x^y = y$ → $x = y^{1/y}$.

For $y = e$: $x = e^{1/e} \approx 1.4447$. (Boundary value — tower converges to $e$.)

For $y = 2$: $x = \sqrt{2} \approx 1.4142$.

→ **$x = y^{1/y}$. For $y = e$: $x = e^{1/e}$.**

---

## Practice 4

> Use logarithmic differentiation to find $dy/dx$ for $y = (\sin x)^{\cos x}$.

(1) $\ln y = \cos x \cdot \ln(\sin x)$.
(2) Differentiate: $\frac{y'}{y} = (-\sin x)\ln(\sin x) + \cos x \cdot \frac{\cos x}{\sin x} = -\sin x \ln(\sin x) + \frac{\cos^2 x}{\sin x}$.
(3) $y' = (\sin x)^{\cos x}\left[-\sin x \ln(\sin x) + \frac{\cos^2 x}{\sin x}\right]$.

→ **$y' = (\sin x)^{\cos x}\left[\frac{\cos^2 x}{\sin x} - \sin x \ln(\sin x)\right]$.**

---

## Practice 5

> The pH of a solution is 4.5. Find $[\text{H}^+]$.

(1) $\text{pH} = -\log[\text{H}^+] = 4.5$.
(2) $\log[\text{H}^+] = -4.5$.
(3) $[\text{H}^+] = 10^{-4.5} \approx 3.16 \times 10^{-5}$ mol/L.

→ **$[\text{H}^+] = 10^{-4.5} \approx 3.16 \times 10^{-5}$ mol/L.**

---

## Practice 6: Real Battle

> How many digits does $50!$ have? Use Stirling's approximation.

(1) Stirling: $n! \approx \sqrt{2\pi n} \left(\frac{n}{e}\right)^n$.
(2) $\log_{10}(50!) \approx \frac{1}{2}\log_{10}(100\pi) + 50\log_{10}(50/e)$.
(3) $\log_{10}(100\pi) \approx \log_{10}(314.16) \approx 2.497$. Half: $1.2486$.
(4) $50/e \approx 18.394$. $\log_{10}(18.394) \approx 1.2647$.
(5) $50 \times 1.2647 = 63.235$.
(6) Sum: $1.2486 + 63.235 = 64.484$.
(7) Number of digits = $\lfloor 64.484 \rfloor + 1 = 65$.

→ **$50!$ has 65 digits.** (Exact: $50! = 30414093201713378043612608166064768844377641568960512000000000000$ — 65 digits.)

---

## Advanced Drill

### A1. $\frac{2^{n+3} - 2^{n+1}}{2^{n}}$
$2^{n+3} = 8 \cdot 2^n$, $2^{n+1} = 2 \cdot 2^n$. Numerator: $6 \cdot 2^n$. Divide by $2^n$: $6$. → **6.**

### A2. $3^{2x} \cdot 9^{1-x} = \frac{1}{27}$
(1) $9^{1-x} = (3^2)^{1-x} = 3^{2-2x}$. So $3^{2x} \cdot 3^{2-2x} = 3^2 = 9$.
(2) But $\frac{1}{27} = 3^{-3}$. So $9 \neq 3^{-3}$... Wait, recheck.

Actually: $3^{2x} \cdot 3^{2-2x} = 3^{2x+2-2x} = 3^2 = 9$. Set equal to $1/27 = 3^{-3}$ → $9 \neq 3^{-3}$ → No solution? Let's recheck the algebra.

$3^{2x} \cdot 9^{1-x} = 3^{2x} \cdot (3^2)^{1-x} = 3^{2x} \cdot 3^{2-2x} = 3^{2x+2-2x} = 3^2 = 9$.

The LHS is always 9, regardless of $x$! So $9 = 1/27$ is impossible.

→ **No solution.** (The LHS simplifies to the constant 9.)

### A3. $\log_2 48 - \log_2 3$
$\log_2 \frac{48}{3} = \log_2 16 = 4$. → **4.**

### A4. $\log_2 5 \cdot \log_5 8 \cdot \log_8 3 \cdot \log_3 16$
Chain change-of-base: all logs to base 2.
$\log_2 5 \cdot \frac{\log_2 8}{\log_2 5} \cdot \frac{\log_2 3}{\log_2 8} \cdot \frac{\log_2 16}{\log_2 3} = \log_2 16 = 4$. → **4.**

### A5. $\frac{\log_3 16}{\log_9 4}$
(1) $\log_3 16 = \log_3(4^2) = 2\log_3 4$.
(2) $\log_9 4 = \frac{\log_3 4}{\log_3 9} = \frac{\log_3 4}{2}$.
(3) Ratio: $\frac{2\log_3 4}{\log_3 4 / 2} = 2 \times 2 = 4$. → **4.**

### A6. $\ln\!\left(\frac{e^3 \sqrt{e}}{e^{-2}}\right)$
(1) $\sqrt{e} = e^{1/2}$. Numerator: $e^3 \cdot e^{1/2} = e^{7/2}$.
(2) $\frac{e^{7/2}}{e^{-2}} = e^{7/2 + 2} = e^{11/2}$.
(3) $\ln(e^{11/2}) = \frac{11}{2}$. → **$\frac{11}{2}$.**

### A7. $\log_2(x-3) + \log_2(x+1) = 3$
(1) Combine: $\log_2[(x-3)(x+1)] = 3$.
(2) $(x-3)(x+1) = 8$ → $x^2 - 2x - 3 = 8$ → $x^2 - 2x - 11 = 0$.
(3) $x = \frac{2 \pm \sqrt{4+44}}{2} = 1 \pm \sqrt{12} = 1 \pm 2\sqrt{3}$.
(4) Arguments: $x-3 > 0$ → $x > 3$. $x+1 > 0$ → $x > -1$. Combined: $x > 3$.
(5) $1 - 2\sqrt{3} \approx -2.46 < 3$ → discard.
$1 + 2\sqrt{3} \approx 4.46 > 3$ → valid.

→ **$x = 1 + 2\sqrt{3}$.**

### A8. $\log_3 2 \cdot \log_4 3 \cdot \log_5 4 \cdot \log_6 5 \cdot \log_7 6 \cdot \log_8 7$
Telescoping via change-of-base (all to base 2):
$\frac{\log 2}{\log 3} \cdot \frac{\log 3}{\log 4} \cdot \frac{\log 4}{\log 5} \cdot \frac{\log 5}{\log 6} \cdot \frac{\log 6}{\log 7} \cdot \frac{\log 7}{\log 8} = \frac{\log 2}{\log 8} = \frac{\log 2}{3\log 2} = \frac{1}{3}$.

→ **$\frac{1}{3}$.**

### A9. $x^{\log_5 x} = 25x$
(1) Take $\log_5$: $\log_5(x^{\log_5 x}) = \log_5(25x)$.
(2) $(\log_5 x)^2 = \log_5 25 + \log_5 x = 2 + \log_5 x$.
(3) $t = \log_5 x$: $t^2 - t - 2 = 0$ → $(t-2)(t+1) = 0$ → $t = 2, -1$.
(4) $x = 5^2 = 25$ or $x = 5^{-1} = \frac{1}{5}$.
Check: $25^{\log_5 25} = 25^2 = 625$, $25 \cdot 25 = 625$ ✅. $\left(\frac{1}{5}\right)^{-1} = 5$, $25 \cdot \frac{1}{5} = 5$ ✅.

→ **$x = 25$ or $x = \frac{1}{5}$.**

### A10. Bacteria doubling every 4 hours. 1000 → 1,000,000: how many hours?
(1) $N(t) = 1000 \cdot 2^{t/4}$. Want $1000 \cdot 2^{t/4} = 10^6$.
(2) $2^{t/4} = 1000$.
(3) Take $\log_2$: $t/4 = \log_2 1000$.
(4) $\log_2 1000 = \frac{\log_{10} 1000}{\log_{10} 2} = \frac{3}{0.3010} \approx 9.966$.
(5) $t = 4 \times 9.966 \approx 39.86$ hours.

→ **About 39.9 hours (roughly 40 hours).**

---

## Basic Drill

### D1. $1000 at 6% compounded quarterly for 2 years
(1) $P = 1000$, $r = 0.06$, $n = 4$, $t = 2$.
(2) $A = 1000\left(1 + \frac{0.06}{4}\right)^{4 \times 2} = 1000(1.015)^8$.
(3) $(1.015)^8 \approx 1.1265$. $A \approx 1000 \times 1.1265 = 1126.50$.
→ **$1126.50.**

### D2. Half-life 10 hours. Find $k$ and fraction remaining after 25 hours.
(1) $k = \frac{\ln 2}{10} \approx 0.06931$ per hour.
(2) $N(25)/N_0 = e^{-0.06931 \times 25} = e^{-1.7328} \approx 0.1768$.
→ **$k \approx 0.0693$ hr$^{-1}$. About 17.7% remains.**

### D3. pH with $[\text{H}^+] = 2.5 \times 10^{-6}$
(1) $\text{pH} = -\log(2.5 \times 10^{-6}) = -[\log 2.5 + \log 10^{-6}]$.
(2) $\log 2.5 \approx 0.3979$. $\log 10^{-6} = -6$.
(3) $\text{pH} = -(0.3979 - 6) = 5.6021$.
→ **pH $\approx 5.60$ (weakly acidic).**

### D4. Sound intensity $I = 10^{-5}$ W/m². Find dB.
(1) $\beta = 10\log\frac{10^{-5}}{10^{-12}} = 10\log 10^7 = 10 \times 7 = 70$.
→ **70 dB (vacuum cleaner level).**

### D5. Midpoint between $10^2$ and $10^6$ on a log scale.
(1) Log scale: midpoint in log space = $\sqrt{10^2 \times 10^6} = \sqrt{10^8} = 10^4$.
(2) On a linear scale: $\frac{100 + 1000000}{2} = 500050$. On log scale: geometric mean = $10^4 = 10000$.
→ **$10^4 = 10000$ (the geometric mean).**

### D6. Rewrite $x \cdot 5^x = 10$ as $u e^u = k$.
(1) $5^x = e^{x\ln 5}$. So $x e^{x\ln 5} = 10$.
(2) Multiply by $\ln 5$: $(x\ln 5) e^{x\ln 5} = 10\ln 5$.
(3) $u = x\ln 5$, $k = 10\ln 5$. → **$u e^u = 10\ln 5$ where $u = x\ln 5$.**

### D7. Logarithmic differentiation setup for $y = x^{\sin x}$.
(1) $\ln y = \sin x \cdot \ln x$.
(2) $\frac{y'}{y} = \cos x \cdot \ln x + \sin x \cdot \frac{1}{x}$.
→ **$\displaystyle \frac{y'}{y} = \cos x \ln x + \frac{\sin x}{x}$.**

### D8. Estimate $\log_{10}(20!)$ using Stirling.
(1) $\ln(20!) \approx 20\ln 20 - 20 \approx 20 \times 2.9957 - 20 = 59.914 - 20 = 39.914$.
(2) $\log_{10}(20!) = \frac{\ln(20!)}{\ln 10} \approx \frac{39.914}{2.3026} \approx 17.33$.
(3) Number of digits = $\lfloor 17.33 \rfloor + 1 = 18$.
→ **$\log_{10}(20!) \approx 17.33$, so $20!$ has 18 digits.** (Exact: 19 digits — Stirling underestimates slightly for small $n$.)

### D9. Benford probability that first digit is 1.
(1) $P(1) = \log_{10}(2) \approx 0.30103$.
→ **About 30.1%.**

### D10. $2^4 = 4^2 = 16$. Find another pair with $t=3$.
(1) $x = 3^{1/(3-1)} = 3^{1/2} = \sqrt{3} \approx 1.732$.
(2) $y = 3^{3/(3-1)} = 3^{3/2} = 3\sqrt{3} \approx 5.196$.
(3) Check: $(\sqrt{3})^{3\sqrt{3}} = 3^{\frac{3\sqrt{3}}{2}}$. $(3\sqrt{3})^{\sqrt{3}} = 3^{\sqrt{3}} \cdot 3^{\frac{\sqrt{3}}{2}} = 3^{\frac{3\sqrt{3}}{2}}$. ✅
→ **$x = \sqrt{3}$ and $y = 3\sqrt{3}$.**
