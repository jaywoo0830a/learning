# Solutions — 10B: Exponents and Logarithms — Applications and Advanced Techniques

---

## Practice 1

**A radioactive substance decays 8% per year. Starting with 500g, find when it falls below 100g. $500(0.92)^t < 100$.**

① Divide: $(0.92)^t < 0.2$.

② Take $\ln$ of both sides (base $<1$, so the inequality flips):
$t\ln(0.92) < \ln(0.2)$ → $t > \frac{\ln 0.2}{\ln 0.92}$.

③ $t > \frac{-1.6094}{-0.08338} \approx 19.30$ years.

> **Answer**: after about **19.3 years** (i.e., during the 20th year)

![Exponential decay: 500(0.92)^t crosses 100 at t≈19.3](graphs/10B/p1-decay.png)

---

## Practice 2

**$x \cdot 3^x = 9$. Use the Lambert $W$ technique.**

① Rewrite $3^x = e^{x\ln 3}$: $x e^{x\ln 3} = 9$.

② Multiply both sides by $\ln 3$: $(x\ln 3)\,e^{x\ln 3} = 9\ln 3$.

③ This is $u e^u = 9\ln 3$ with $u = x\ln 3$.

④ $u = W(9\ln 3)$ → $x = \frac{W(9\ln 3)}{\ln 3}$.

**Numerically**: $9\ln 3 \approx 9.8875$, $W(9.8875) \approx 1.735$, so $x \approx 1.58$.

> **Answer**: $x = \frac{W(9\ln 3)}{\ln 3} \approx 1.58$

![x·3^x = 9 solved at x≈1.58 via Lambert W](graphs/10B/p2-lambert.png)

---

## Practice 3: Real Battle

**Show the infinite power tower converges only for $e^{-e} \leq x \leq e^{1/e}$. Then solve $x^{x^{x^{\cdot^{\cdot^{\cdot}}}}} = y$ for $x$ in terms of $y$, and evaluate for $y = e$.**

① If the tower converges to a limit $L$, then the whole tower equals $x$ raised to (the tower), so $x^L = L$ → $x = L^{1/L}$.

② The function $f(L) = L^{1/L}$ attains its **maximum** at $L = e$: $f(e) = e^{1/e}$. (Check: $f'(L)=0$ at $L=e$.)

③ As the limit $L$ ranges over its valid values, $x = L^{1/L}$ ranges over $[e^{-e}, e^{1/e}]$ — the convergence interval (Euler, 1783).

④ **Solving $x^{\text{tower}} = y$**: the limit is $y$, so $x^y = y$ → $\boxed{x = y^{1/y}}$.

⑤ **For $y = e$**: $x = e^{1/e} \approx 1.4447$ — exactly the upper bound of the convergence interval.

> **Answer**: $x = y^{1/y}$; for $y=e$, $x = e^{1/e}$

---

## Practice 4

**Use logarithmic differentiation to find $dy/dx$ for $y = (\sin x)^{\cos x}$.**

① $\ln y = \cos x \ln(\sin x)$.

② Differentiate (product rule on the right):
$\frac{y'}{y} = -\sin x\ln(\sin x) + \cos x\cdot\frac{\cos x}{\sin x} = \cos x\cot x - \sin x\ln(\sin x)$.

③ Multiply by $y$:

> **Answer**: $y' = (\sin x)^{\cos x}\left[\cos x\cot x - \sin x\ln(\sin x)\right]$

---

## Practice 5

**The pH of a solution is 4.5. Find $[\text{H}^+]$.**

$\text{pH} = -\log[\text{H}^+] = 4.5$ → $[\text{H}^+] = 10^{-4.5} \approx 3.16 \times 10^{-5}$ M.

> **Answer**: $[\text{H}^+] = 10^{-4.5} \approx 3.2\times 10^{-5}$ M

---

## Practice 6: Real Battle

**How many digits does $50!$ have? Use Stirling's approximation.**

① $\log_{10}(50!) \approx \frac{1}{\ln 10}\left(50\ln 50 - 50 + \frac12\ln(2\pi\cdot 50)\right)$.

② $50\ln 50 \approx 195.60$, minus $50$ → $145.60$; $\frac12\ln(100\pi) \approx 2.876$ → sum $\approx 148.48$.

③ Divide by $\ln 10 \approx 2.3026$: $\log_{10}(50!) \approx 64.48$.

④ Number of digits $= \lfloor \log_{10}(50!) \rfloor + 1 = 64 + 1 = 65$.

> **Answer**: $50!$ has **65 digits**

---

## Basic Drills

### D1. $1000$ at 6% compounded quarterly for 2 years.

$A = 1000\left(1+\frac{0.06}{4}\right)^{4\cdot 2} = 1000(1.015)^8 \approx 1000(1.12649) = 1126.49$.

> **Answer**: $\$1126.49$

---

### D2. Half-life 10 hours: find $k$, then the fraction after 25 hours.

$k = \frac{\ln 2}{t_{1/2}} = \frac{\ln 2}{10} \approx 0.0693$ /hour.

Fraction after 25 h: $e^{-k\cdot 25} = e^{-1.7329} \approx 0.177$ (equivalently $(\frac12)^{2.5}$).

> **Answer**: $k \approx 0.0693$; about **17.7%** remains

---

### D3. pH of $[\text{H}^+] = 2.5 \times 10^{-6}$.

$\text{pH} = -\log(2.5\times 10^{-6}) = -\log(2.5) + 6 \approx -0.398 + 6 = 5.60$.

> **Answer**: $\text{pH} \approx 5.6$

---

### D4. Decibel level of $I = 10^{-5}$ W/m².

$\beta = 10\log\frac{10^{-5}}{10^{-12}} = 10\log 10^7 = 70$ dB.

> **Answer**: $70$ dB

---

### D5. Midpoint between $10^2$ and $10^6$ on a log scale.

Geometric mean: $\sqrt{10^2\cdot 10^6} = 10^4 = 10000$.

> **Answer**: $10^4 = 10000$

---

### D6. Rewrite $x\cdot 5^x = 10$ as $u e^u = k$.

$5^x = e^{x\ln 5}$ → $x e^{x\ln 5} = 10$ → multiply by $\ln 5$:
$(x\ln 5)e^{x\ln 5} = 10\ln 5$, so $u = x\ln 5$, $k = 10\ln 5$.

> **Answer**: $u e^u = 10\ln 5$ with $u = x\ln 5$

---

### D7. Set up log-differentiation for $y = x^{\sin x}$.

$\ln y = \sin x\ln x$; differentiating: $\frac{y'}{y} = \cos x\ln x + \frac{\sin x}{x}$.

> **Answer**: $\ln y = \sin x\ln x$, $\frac{y'}{y} = \cos x\ln x + \frac{\sin x}{x}$

---

### D8. Estimate $\log_{10}(20!)$ with Stirling.

$\log_{10}(20!) \approx \frac{20\ln 20 - 20}{\ln 10} = \frac{20(2.9957)-20}{2.3026} \approx \frac{39.914}{2.3026} \approx 17.33$ → about 18 digits.

> **Answer**: $\approx 17.3$ (so $20!$ has about 18 digits)

---

### D9. Probability the first digit is 1 (Benford).

$P(1) = \log_{10}(2) \approx 0.3010$.

> **Answer**: about **30.1%**

---

### D10. Verify $2^4 = 4^2$, then find another pair with $t=3$.

$2^4 = 16 = 4^2$ ✓.

Parametric form with $t=3$: $x = 3^{1/(3-1)} = 3^{1/2} = \sqrt3$, $y = 3^{3/2} = 3\sqrt3$.

Check: $(\sqrt3)^{3\sqrt3} = (3\sqrt3)^{\sqrt3}$ (both equal $3^{3\sqrt3/2}$) ✓.

> **Answer**: $(\sqrt3,\ 3\sqrt3)$

---

## Advanced Drills

### A1. Simplify $\frac{2^{n+3} - 2^{n+1}}{2^n}$.

Factor the numerator: $2^{n}(2^3 - 2) = 2^n(8-2) = 6\cdot 2^n$. Divide by $2^n$: $6$.

> **Answer**: $6$

---

### A2. Solve $3^{2x} \cdot 9^{x+1} = \frac{1}{27}$.

Write in base 3: $3^{2x}\cdot 3^{2x+2} = 3^{-3}$ → $3^{4x+2} = 3^{-3}$.

$4x+2 = -3$ → $x = -\frac54$.

> **Answer**: $x = -\frac54$

---

### A3. Simplify $\log_2 48 - \log_2 3$.

$\log_2\frac{48}{3} = \log_2 16 = 4$.

> **Answer**: $4$

---

### A4. Compute $\log_2 5 \cdot \log_5 8 \cdot \log_8 3 \cdot \log_3 16$.

Chain: $\log_2 5\cdot\log_5 8 = \log_2 8 = 3$; $\log_8 3\cdot\log_3 16 = \log_8 16 = \frac43$. Product $= 3\cdot\frac43 = 4$.

> **Answer**: $4$

---

### A5. Simplify $\frac{\log_3 16}{\log_9 4}$.

$\log_3 16 = \frac{4\ln 2}{\ln 3}$; $\log_9 4 = \frac{2\ln 2}{2\ln 3} = \frac{\ln 2}{\ln 3}$. Ratio $= 4$.

> **Answer**: $4$

---

### A6. Simplify $\ln\left(\frac{e^3 \sqrt{e}}{e^{-2}}\right)$.

Exponent of $e$: $3 + \frac12 + 2 = \frac{11}{2}$. $\ln e^{11/2} = \frac{11}{2}$.

> **Answer**: $\frac{11}{2}$

---

### A7. Solve $\log_2(x-3) + \log_2(x+1) = 3$.

① Combine: $\log_2[(x-3)(x+1)] = 3$ → $(x-3)(x+1) = 8$ → $x^2 - 2x - 11 = 0$.

② $x = \frac{2 \pm \sqrt{4+44}}{2} = 1 \pm 2\sqrt3$.

③ Arguments: $x-3>0$ → $x>3$. $1+2\sqrt3 \approx 4.46$ ✓; $1-2\sqrt3 \approx -2.46$ ✗.

> **Answer**: $x = 1 + 2\sqrt3$

---

### A8. Chain-simplify $\log_3 2 \cdot \log_4 3 \cdot \log_5 4 \cdot \log_6 5 \cdot \log_7 6 \cdot \log_8 7$.

Telescoping: $\log_3 2\cdot\log_4 3 = \log_4 2$, ... all the way to $\log_8 7\cdot\log_7 6 \cdots$ → net result $\log_8 2 = \frac13$.

> **Answer**: $\frac13$

---

### A9. Solve $x^{\log_5 x} = 25x$.

Take $\log_5$: $(\log_5 x)^2 = 2 + \log_5 x$ → $t^2 - t - 2 = 0$ → $t = 2, -1$.

$x = 5^2 = 25$ or $x = 5^{-1} = \frac15$.

> **Answer**: $x = 25$ or $x = \frac15$

---

### A10. Bacteria doubles every 4 hours; from 1000 to 1,000,000.

$1000\cdot 2^{t/4} = 1{,}000{,}000$ → $2^{t/4} = 1000$ → $t = 4\log_2 1000 = 4\cdot\frac{\ln 1000}{\ln 2} \approx 4\cdot 9.966 \approx 39.86$.

> **Answer**: about **40 hours**
