# Solutions — 18A: Infinite Series — Does It Converge?

> Back to [18A — Infinite Series](../18A-series-convergence.md)

---

## Practice 1

**$\displaystyle \sum_{n=0}^\infty \frac{3}{4^n}$. Identify $a$ and $r$, find the sum.**

① This is a geometric series $\sum ar^n$ with first term $a = 3$ and ratio $r = \frac14$.

② $|r| = \frac14 < 1$, so it converges and

$$S = \frac{a}{1-r} = \frac{3}{1-\frac14} = \frac{3}{3/4} = 4.$$

> **Answer**: $a=3$, $r=\tfrac14$, sum $= 4$

---

## Practice 2

**Determine convergence: $\displaystyle \sum_{n=1}^\infty \frac{n}{n^2+4}$. Use comparison or limit comparison.**

**Limit comparison** with $b_n = \frac{1}{n}$ (harmonic):

$$\lim_{n\to\infty}\frac{a_n}{b_n} = \lim_{n\to\infty}\frac{n/(n^2+4)}{1/n} = \lim_{n\to\infty}\frac{n^2}{n^2+4} = 1 > 0.$$

Since $\sum \frac{1}{n}$ diverges, the series **diverges**.

**Direct comparison check** (alternative): for $n \ge 2$, $n^2 + 4 \le 2n^2$, so $\frac{n}{n^2+4} \ge \frac{n}{2n^2} = \frac{1}{2n}$. Same conclusion.

> **Answer**: diverges (like the harmonic series)

---

## Practice 3

**Determine convergence: $\displaystyle \sum_{n=1}^\infty \frac{3^n}{n!}$. Ratio test.**

$$\rho = \lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right| = \lim_{n\to\infty}\frac{3^{n+1}/(n+1)!}{3^n/n!} = \lim_{n\to\infty}\frac{3}{n+1} = 0 < 1.$$

> **Answer**: converges (absolutely) — factorial outruns the exponential

---

## Practice 4

**Determine convergence: $\displaystyle \sum_{n=1}^\infty \frac{(-1)^{n+1}}{\sqrt{n}}$. Alternating series test. Absolute or conditional?**

① **Alternating test**: $a_n = \frac{1}{\sqrt{n}}$ is positive, decreasing, and $a_n \to 0$ → **converges**.

② **Absolute convergence?** $\sum |a_n| = \sum \frac{1}{n^{1/2}}$ is a $p$-series with $p = \frac12 \le 1$ → **diverges**.

> **Answer**: converges, but only **conditionally**

---

## Practice 5: Real Battle

**$\displaystyle \sum_{n=2}^\infty \frac{1}{n(\ln n)^p}$. For which $p$ does this converge? Use the integral test.**

① $f(x) = \frac{1}{x(\ln x)^p}$ is positive and decreasing for $x \ge 2$ (for any $p$), so the integral test applies.

② $\displaystyle \int_2^\infty \frac{dx}{x(\ln x)^p}$. Substitute $u = \ln x$, $du = \frac{dx}{x}$:

$$\int_{\ln 2}^{\infty} \frac{du}{u^p}.$$

③ This is a $p$-integral over $u$: converges $\iff p > 1$.

> **Answer**: converges **iff $p > 1$** — exactly like the $p$-series, with $\ln n$ playing the role of $n$. (Check: $p=1$ gives $\int \frac{du}{u} = \ln\ln x \to \infty$, diverges.)

---

## Practice 6: Real Battle — Strategy Challenge

**Determine convergence of $\displaystyle \sum_{n=1}^\infty \frac{n!}{n^n}$. Use the ratio test. Then use the comparison test to show $\frac{n!}{n^n} \leq \frac{1}{2^n}$ for $n\geq 6$. Which approach is simpler?**

**Method 1 — Ratio test**:

$$\rho = \lim_{n\to\infty}\frac{(n+1)!/(n+1)^{n+1}}{n!/n^n} = \lim_{n\to\infty}\left(\frac{n}{n+1}\right)^n = \frac{1}{e} < 1.$$

→ **converges** (absolutely).

**Method 2 — Comparison test**:

① First check the bound at $n=6$ directly: $\frac{6!}{6^6} = \frac{720}{46656} \approx 0.01543 < \frac{1}{64} \approx 0.01563$. ✓

② Then induct: $\frac{a_{n+1}}{a_n} = \left(\frac{n}{n+1}\right)^n \le \frac12$ for every $n \ge 1$, so if $a_n \le \frac{1}{2^n}$ then $a_{n+1} \le \frac{1}{2^{n+1}}$. Hence $\frac{n!}{n^n} \le \frac{1}{2^n}$ for all $n \ge 6$.

③ Since $\sum \frac{1}{2^n}$ (geometric, $r=\frac12$) converges, the series converges.

> **Answer**: converges. The **ratio test is far simpler** — one limit gives $1/e < 1$. The comparison requires a clever (and carefully checked) bound. This is the moral of 18A: use the ratio test when factorials and powers appear.

---

## Basic Drills

### D1. $\sum_{n=0}^\infty \left(\frac{2}{5}\right)^n$. Sum if convergent.

Geometric with $a=1$, $r=\frac25$. $|r|<1$: $S = \frac{1}{1-2/5} = \frac{5}{3}$.

> **Answer**: $\frac{5}{3}$

### D2. $\sum_{n=1}^\infty \frac{1}{n^3}$. $p$-series — converge or diverge?

$p = 3 > 1$ → **converges**.

> **Answer**: converges

### D3. $\sum_{n=1}^\infty \frac{1}{\sqrt[3]{n}}$. $p$-series.

$\frac{1}{\sqrt[3]{n}} = \frac{1}{n^{1/3}}$, so $p = \frac13 \le 1$ → **diverges**.

> **Answer**: diverges

### D4. Apply the Divergence Test to $\sum_{n=1}^\infty \frac{n}{n+1}$.

$\lim a_n = \lim \frac{n}{n+1} = 1 \neq 0$ → **diverges** (by the Divergence Test — no need for anything fancier).

> **Answer**: diverges

### D5. $\sum_{n=1}^\infty \frac{2}{n^2+1}$. Compare to $p$-series.

$\frac{2}{n^2+1} \le \frac{2}{n^2}$ and $\sum \frac{2}{n^2}$ converges ($p=2$) → **converges**.

> **Answer**: converges

### D6. $\sum_{n=1}^\infty \frac{(-1)^{n}}{n^2+1}$. Absolute convergence?

$\sum |a_n| = \sum \frac{1}{n^2+1}$ converges (compare to $\sum \frac{1}{n^2}$) → **absolutely convergent**.

> **Answer**: absolutely convergent

### D7. $\sum_{n=1}^\infty \frac{5^n}{n!}$. Ratio test.

$\rho = \lim \frac{5}{n+1} = 0 < 1$ → **converges**.

> **Answer**: converges

### D8. $\sum_{n=1}^\infty \frac{1}{n\ln n}$. Integral test.

$\int_2^\infty \frac{dx}{x\ln x} = \ln(\ln x)\Big|_2^\infty = \infty$ → **diverges**.

> **Answer**: diverges

### D9. Telescoping: $\sum_{n=1}^\infty \frac{2}{(2n-1)(2n+1)}$.

Partial fractions: $\frac{2}{(2n-1)(2n+1)} = \frac{1}{2n-1} - \frac{1}{2n+1}$.

$S_N = \left(1-\frac13\right)+\left(\frac13-\frac15\right)+\cdots+\left(\frac{1}{2N-1}-\frac{1}{2N+1}\right) = 1 - \frac{1}{2N+1} \to 1$.

> **Answer**: converges to $1$

### D10. Root test on $\sum_{n=1}^\infty \left(1+\frac{1}{n}\right)^{-n^2}$.

$\sqrt[n]{|a_n|} = \left(1+\frac1n\right)^{-n} \to e^{-1} = \frac1e < 1$ → **converges**.

> **Answer**: converges ($\rho = 1/e$)

### D11. $\sum_{n=1}^\infty \frac{n^{10}}{10^n}$. Ratio test — which dominates, polynomial or exponential?

$\rho = \lim \frac{(n+1)^{10}/10^{n+1}}{n^{10}/10^n} = \frac{1}{10}\lim\left(\frac{n+1}{n}\right)^{10} = \frac{1}{10} < 1$ → **converges**. The **exponential $10^n$ dominates** the polynomial $n^{10}$.

> **Answer**: converges — exponential beats polynomial

### D12. $\sum_{n=1}^\infty \frac{n\cos(n\pi)}{n^3+1}$. Determine absolute vs conditional convergence.

$\cos(n\pi) = (-1)^n$, so $a_n = \frac{(-1)^n n}{n^3+1}$. Absolute: $\sum \frac{n}{n^3+1} \le \sum \frac{n}{n^3} = \sum \frac{1}{n^2}$, which converges → **absolutely convergent**.

> **Answer**: absolutely convergent

---

## Advanced Drills

### A1. Determine convergence of $\sum_{n=2}^\infty \frac{1}{n(\ln n)^2}$.

$\int_2^\infty \frac{dx}{x(\ln x)^2}$; $u=\ln x$: $\int_{\ln 2}^\infty \frac{du}{u^2} = \left[-\frac{1}{u}\right]_{\ln 2}^\infty = \frac{1}{\ln 2}$, finite → **converges**.

> **Answer**: converges (to a finite value $< 1/\ln 2 \approx 1.44$; the series value is not $1/\ln 2$, the integral only decides convergence)

### A2. $\sum_{n=1}^\infty \frac{n!}{2^n}$. Determine convergence.

$\rho = \lim \frac{(n+1)!}{2^{n+1}}\cdot\frac{2^n}{n!} = \lim \frac{n+1}{2} = \infty > 1$ → **diverges**.

> **Answer**: diverges

### A3. $\sum_{n=1}^\infty \frac{\sin n}{n^2}$. Determine convergence.

$\left|\frac{\sin n}{n^2}\right| \le \frac{1}{n^2}$ and $\sum \frac{1}{n^2}$ converges → $\sum \left|\frac{\sin n}{n^2}\right|$ converges → **absolutely convergent** (hence convergent).

> **Answer**: converges absolutely

### A4. $\sum_{n=1}^\infty \frac{(-1)^n n}{n^2+1}$. Determine convergence; absolute or conditional?

① **Alternating test**: $a_n = \frac{n}{n^2+1}$. For $x \ge 1$, $f(x) = \frac{x}{x^2+1}$ has $f'(x) = \frac{1-x^2}{(x^2+1)^2} < 0$, so $a_n \searrow 0$ → **converges**.

② **Absolute**: $\sum \frac{n}{n^2+1}$ behaves like $\sum \frac{1}{n}$ → **diverges** (e.g., $\frac{n}{n^2+1} \ge \frac{n}{2n^2} = \frac{1}{2n}$ for $n\ge1$).

> **Answer**: converges **conditionally**

### A5. $\sum_{n=1}^\infty \left(\frac{n}{n+1}\right)^{n^2}$. Determine convergence.

$\sqrt[n]{|a_n|} = \left(\frac{n}{n+1}\right)^n = \left(1 - \frac{1}{n+1}\right)^n \to \frac{1}{e} < 1$ → **converges**.

> **Answer**: converges ($\rho = 1/e$)

### A6. Determine all $x$ where $\sum_{n=1}^\infty \frac{x^n}{n}$ converges.

Ratio test: $|x| \lim \frac{n}{n+1} = |x|$ → converges for $|x| < 1$, diverges for $|x| > 1$. Radius $R=1$.

Endpoints:
- $x = 1$: $\sum \frac1n$ — harmonic, **diverges**.
- $x = -1$: $\sum \frac{(-1)^n}{n}$ — alternating, **converges**.

> **Answer**: converges for all $x \in [-1, 1)$

### A7. $\sum_{n=1}^\infty \frac{1\cdot3\cdot5\cdots(2n-1)}{n!\,3^n}$. Determine convergence.

$\frac{a_{n+1}}{a_n} = \frac{1\cdot3\cdots(2n+1)}{(n+1)!3^{n+1}} \cdot \frac{n!3^n}{1\cdot3\cdots(2n-1)} = \frac{2n+1}{(n+1)\cdot3} \to \frac{2}{3} < 1$ → **converges**.

> **Answer**: converges ($\rho = 2/3$)

### A8. Prove $\sum_{n=1}^\infty \frac{1}{n^2}$ converges.

① For $n \ge 2$: $n^2 \ge n(n-1) > 0$, so $\frac{1}{n^2} \le \frac{1}{n(n-1)}$.

② $\sum_{n=2}^\infty \frac{1}{n(n-1)} = \sum_{n=2}^\infty \left(\frac{1}{n-1} - \frac{1}{n}\right)$ telescopes to $1$ (only the first term survives).

③ Since $\sum \frac{1}{n(n-1)}$ converges, so does $\sum \frac{1}{n^2}$ (in fact $\sum_{n=1}^\infty \frac{1}{n^2} \le 1 + 1 = 2$).

> **Answer**: $\frac{1}{n^2} \le \frac{1}{n(n-1)}$ for $n\ge2$; the comparison series telescopes to $1$ → converges

### A9. $\sum_{n=1}^\infty \frac{\ln n}{n^2}$. Determine convergence.

For large $n$, $\ln n \le n^{1/2}$ (log grows slower than any positive power). So $\frac{\ln n}{n^2} \le \frac{n^{1/2}}{n^2} = \frac{1}{n^{1.5}}$. $\sum \frac{1}{n^{1.5}}$ converges ($p = 1.5 > 1$) → **converges**.

> **Answer**: converges

### A10. True or false: if $\sum a_n$ converges, then $\sum a_n^2$ converges?

**False.** Take $a_n = \frac{(-1)^n}{\sqrt{n}}$:
- $\sum a_n = \sum \frac{(-1)^n}{\sqrt{n}}$ converges (alternating, $1/\sqrt{n} \searrow 0$).
- $\sum a_n^2 = \sum \frac{1}{n}$ — the harmonic series, **diverges**.

> **Answer**: False — the counterexample $\sum \frac{(-1)^n}{\sqrt{n}}$ converges while its square-series diverges

### A11. Determine convergence of $\sum_{n=1}^\infty \frac{\sqrt{n}}{\sqrt{n^3+1}}$.

The general term behaves like $\frac{\sqrt{n}}{\sqrt{n^3}} = \frac{1}{n}$, so try $b_n = \frac{1}{n}$:

$$\lim_{n\to\infty}\frac{\sqrt{n}/\sqrt{n^3+1}}{1/n} = \lim_{n\to\infty}\frac{n\sqrt{n}}{\sqrt{n^3+1}} = 1 > 0.$$

$\sum \frac1n$ diverges → the series **diverges**.

> **Answer**: diverges (limit-comparison with $b_n = 1/n$, limit $=1$)

### A12. Determine convergence of $\sum_{n=2}^\infty \frac{\ln n}{n(\ln n)^2-1}$.

① $f(x) = \frac{\ln x}{x(\ln x)^2 - 1}$ is positive and (eventually) decreasing → integral test applies.

② Substitute $u = \ln x$, $du = \frac{dx}{x}$, so $dx = e^u du$ and the $e^u$ in the denominator cancels:

$$\int \frac{\ln x}{x(\ln x)^2-1}\,dx = \int \frac{u\,e^u\,du}{e^u u^2 - 1} = \int \frac{u}{u^2-1}\,du = \frac12\ln(u^2-1) \to \infty \text{ as } u\to\infty.$$

③ The integral diverges → the **series diverges**.

> **Answer**: diverges

---

## Answer Check

| Problem | Convergence | Key test |
|:--------|:-----------:|:--------:|
| Practice 1 | sum $= 4$ | geometric |
| Practice 2 | diverges | limit comparison with $1/n$ |
| Practice 3 | converges | ratio |
| Practice 4 | converges conditionally | alternating |
| Practice 5 | converges iff $p>1$ | integral |
| Practice 6 | converges | ratio (or comparison) |
| D1–D12 | see above | — |
