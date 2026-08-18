# Solutions — 18C: Taylor Series — Approximating Any Function

> Back to [18C — Taylor Series](../18C-taylor-series.md)

---

## Practice 1

**Find the Maclaurin series for $f(x)=xe^x$.**

Multiply the known series for $e^x$ by $x$:

$$xe^x = x\sum_{n=0}^\infty \frac{x^n}{n!} = \sum_{n=0}^\infty \frac{x^{n+1}}{n!} = \sum_{n=1}^\infty \frac{x^n}{(n-1)!} = x + x^2 + \frac{x^3}{2!} + \frac{x^4}{3!} + \cdots$$

> **Answer**: $xe^x = \sum_{n=1}^\infty \frac{x^n}{(n-1)!}$, radius $\infty$

---

## Practice 2

**Find the Taylor series for $f(x)=\ln x$ centered at $a=1$.**

$f(x) = \ln x = \ln(1 + (x-1))$. Use the Maclaurin series for $\ln(1+u)$ with $u = x-1$:

$$\ln x = \sum_{n=1}^\infty \frac{(-1)^{n+1}(x-1)^n}{n} = (x-1) - \frac{(x-1)^2}{2} + \frac{(x-1)^3}{3} - \cdots$$

Valid for $|x-1|<1$, i.e. $0 < x < 2$ (at $x=2$ it converges to $\ln 2$; at $x=0$ it diverges).

> **Answer**: $\ln x = \sum_{n=1}^\infty \frac{(-1)^{n+1}}{n}(x-1)^n$, interval $(0,2]$

---

## Practice 3

**Use Taylor series to evaluate $\lim_{x\to0}\frac{\cos x-1+x^2/2}{x^4}$.**

$\cos x = 1 - \frac{x^2}{2} + \frac{x^4}{24} - \frac{x^6}{720} + \cdots$, so

$$\frac{\cos x - 1 + \frac{x^2}{2}}{x^4} = \frac{\frac{x^4}{24} - \frac{x^6}{720} + \cdots}{x^4} = \frac{1}{24} - \frac{x^2}{720} + \cdots \to \frac{1}{24}.$$

> **Answer**: $\frac{1}{24}$

---

## Practice 4

**Estimate $\int_0^{0.5} \sin(x^2)dx$ to 4 decimal places using series.**

① $\sin(x^2) = \sum_{n=0}^\infty \frac{(-1)^n (x^2)^{2n+1}}{(2n+1)!} = \sum \frac{(-1)^n x^{4n+2}}{(2n+1)!}$.

② Integrate term-by-term:

$$\int_0^{0.5}\sin(x^2)\,dx = \sum_{n=0}^\infty \frac{(-1)^n (0.5)^{4n+3}}{(2n+1)!(4n+3)}.$$

Terms: $\frac{1}{24} - \frac{1}{5376} + \frac{1}{2703360} - \cdots = 0.041667 - 0.000186 + 0.00000037 - \cdots$

③ This is alternating; the first omitted term $3.7\times10^{-7}$ bounds the error — far below $0.00005$.

> **Answer**: $\approx 0.0415$ (sum $= 0.041481\ldots$)

---

## Practice 5: Real Battle

**Use the binomial series to find the Maclaurin series for $\arcsin x$. Integrate $(1-x^2)^{-1/2}$ term-by-term. Then use your series to evaluate $\lim_{x\to0}\frac{\arcsin x - x}{x^3}$.**

① Binomial series for $(1+u)^{-1/2} = 1 - \frac12 u + \frac{3}{8}u^2 - \frac{5}{16}u^3 + \cdots$; substitute $u = -x^2$:

$$(1-x^2)^{-1/2} = 1 + \frac{x^2}{2} + \frac{3x^4}{8} + \frac{5x^6}{16} + \cdots = \sum_{n=0}^\infty \frac{1\cdot3\cdot5\cdots(2n-1)}{2^n n!}x^{2n}.$$

② Integrate term-by-term:

$$\arcsin x = \int_0^x \frac{dt}{\sqrt{1-t^2}} = \sum_{n=0}^\infty \frac{1\cdot3\cdots(2n-1)}{2^n n!(2n+1)}x^{2n+1} = x + \frac{x^3}{6} + \frac{3x^5}{40} + \frac{5x^7}{112} + \cdots$$

③ Limit: $\frac{\arcsin x - x}{x^3} = \frac{\frac{x^3}{6} + \cdots}{x^3} \to \frac16$.

> **Answer**: $\arcsin x = x + \frac{x^3}{6} + \frac{3x^5}{40} + \cdots$; $\lim = \frac16$

---

## Practice 6: Real Battle — Error Analysis

**How many terms of the Maclaurin series for $e^x$ are needed to approximate $e$ (i.e., $e^1$) with error less than $10^{-6}$? Use the Lagrange remainder bound.**

① Lagrange remainder at $x=1$: $R_n(1) = \frac{e^c}{(n+1)!}$ for some $c\in(0,1)$, so

$$|R_n(1)| \le \frac{e}{(n+1)!} \le \frac{3}{(n+1)!}.$$

② Need $\frac{3}{(n+1)!} < 10^{-6}$, i.e. $(n+1)! > 3\times10^6$. Since $9! = 362880$ and $10! = 3628800 > 3\times10^6$, take $n+1 = 10$, i.e. $n = 9$.

③ So keep terms up to $\frac{x^9}{9!}$ — that's **10 terms** ($k=0$ through $9$). Error $\le \frac{3}{10!} \approx 8.3\times10^{-7} < 10^{-6}$. ✓

**Comparison with actual error**: $\sum_{k=10}^\infty \frac{1}{k!} \approx 2.73\times10^{-7}$ — comfortably under the bound, as expected.

> **Answer**: $n=9$ (10 terms, up to $x^9/9!$)

---

## Basic Drills

### D1. Write the Maclaurin series for $e^{-x}$ (first 4 terms).

Replace $x$ by $-x$: $1 - x + \frac{x^2}{2!} - \frac{x^3}{3!}$.

> **Answer**: $e^{-x} = 1 - x + \frac{x^2}{2} - \frac{x^3}{6} + \cdots$

### D2. Write the Maclaurin series for $\cos(2x)$ (first 4 nonzero terms).

$\cos(2x) = 1 - \frac{(2x)^2}{2!} + \frac{(2x)^4}{4!} - \frac{(2x)^6}{6!} + \cdots = 1 - 2x^2 + \frac{2}{3}x^4 - \frac{4}{45}x^6 + \cdots$

> **Answer**: $1 - 2x^2 + \frac23 x^4 - \frac4{45}x^6$

### D3. Find the 3rd-degree Taylor polynomial of $f(x)=\sqrt{x}$ at $a=4$.

$f(4)=2$, $f'(x)=\frac{1}{2\sqrt{x}}$ → $f'(4)=\frac14$, $f''(x)=-\frac{1}{4x^{3/2}}$ → $f''(4)=-\frac{1}{32}$, $f'''(x)=\frac{3}{8x^{5/2}}$ → $f'''(4)=\frac{3}{256}$.

$$T_3(x) = 2 + \frac14(x-4) - \frac{1}{32\cdot2}(x-4)^2 + \frac{3}{256\cdot6}(x-4)^3 = 2 + \frac{x-4}{4} - \frac{(x-4)^2}{64} + \frac{(x-4)^3}{512}.$$

> **Answer**: $T_3(x) = 2 + \frac{x-4}{4} - \frac{(x-4)^2}{64} + \frac{(x-4)^3}{512}$

### D4. Find the Maclaurin series for $\frac{1}{1+x^2}$ and its radius.

$\frac{1}{1+x^2} = \frac{1}{1-(-x^2)} = \sum_{n=0}^\infty (-x^2)^n = \sum_{n=0}^\infty (-1)^n x^{2n}$, radius $1$ (geometric in $x^2$).

> **Answer**: $\sum (-1)^n x^{2n}$, $R=1$

### D5. Find the Maclaurin series for $\ln(1-x)$.

$\ln(1-x) = -\sum_{n=1}^\infty \frac{x^n}{n} = -x - \frac{x^2}{2} - \frac{x^3}{3} - \cdots$

> **Answer**: $\ln(1-x) = -\sum_{n=1}^\infty \frac{x^n}{n}$

### D6. Use series to compute $\lim_{x\to0}\frac{e^x-1}{x}$.

$e^x - 1 = x + \frac{x^2}{2} + \cdots$, so $\frac{e^x-1}{x} = 1 + \frac{x}{2} + \cdots \to 1$.

> **Answer**: $1$

### D7. Find $T_2(x)$ (2nd-degree Taylor) for $f(x)=\tan x$ at $a=0$.

$\tan x = x + \frac{x^3}{3} + \cdots$ is an odd function, so there is **no $x^2$ term**: $T_2(x) = x$.

> **Answer**: $T_2(x) = x$

### D8. Write the binomial series for $\frac{1}{\sqrt{1+x}} = (1+x)^{-1/2}$ (first 3 terms).

$(1+x)^{-1/2} = 1 + \left(-\frac12\right)x + \frac{(-\frac12)(-\frac32)}{2}x^2 + \cdots = 1 - \frac{x}{2} + \frac{3x^2}{8} + \cdots$

> **Answer**: $1 - \frac{x}{2} + \frac{3x^2}{8} + \cdots$

### D9. Multiply the series for $e^x$ and $e^{-x}$. What do you get?

$e^x \cdot e^{-x} = e^0 = 1$. (Cauchy product: $\sum_n \left(\sum_{k=0}^n \frac{(-1)^k}{k!(n-k)!}\right)x^n$; the inner sum is $0$ for $n\ge1$ and $1$ for $n=0$.)

> **Answer**: $1$ — all non-constant terms cancel

### D10. Use $\cos x$ series to estimate $\cos(0.2)$ to 4 decimal places.

$\cos(0.2) = 1 - \frac{(0.2)^2}{2!} + \frac{(0.2)^4}{4!} - \cdots = 1 - 0.02 + 0.0000667 - \cdots = 0.9800667$

Next term $\frac{(0.2)^6}{6!} \approx 8.9\times10^{-9}$, negligible.

> **Answer**: $\cos(0.2) \approx 0.9801$

### D11. Use the binomial series to write the first 3 nonzero terms of $(1+2x)^{1/3}$.

$\binom{1/3}{1} = \frac13$, $\binom{1/3}{2} = \frac{(1/3)(-2/3)}{2} = -\frac19$, $\binom{1/3}{3} = \frac{(1/3)(-2/3)(-5/3)}{6} = \frac{5}{81}$.

$$(1+2x)^{1/3} = 1 + \frac13(2x) - \frac19(2x)^2 + \frac{5}{81}(2x)^3 + \cdots = 1 + \frac{2x}{3} - \frac{4x^2}{9} + \frac{40x^3}{81} + \cdots$$

> **Answer**: $1 + \frac{2x}{3} - \frac{4x^2}{9} + \frac{40x^3}{81}$

### D12. Find the Taylor series for $f(x)=x^3-2x^2+3x-4$ at $a=1$ directly using the formula.

$f(1) = -2$; $f'(x)=3x^2-4x+3$, $f'(1)=2$; $f''(x)=6x-4$, $f''(1)=2$; $f'''(x)=6$, $f'''(1)=6$; higher derivatives $0$.

$$T(x) = -2 + 2(x-1) + \frac{2}{2}(x-1)^2 + \frac{6}{6}(x-1)^3 = -2 + 2(x-1) + (x-1)^2 + (x-1)^3.$$

> **Answer**: $-2 + 2(x-1) + (x-1)^2 + (x-1)^3$ (check: expands back to $x^3-2x^2+3x-4$)

---

## Advanced Drills

### A1. Find the Maclaurin series for $\sinh x = \frac{e^x-e^{-x}}{2}$.

$\frac{1}{2}\left(\sum \frac{x^n}{n!} - \sum \frac{(-x)^n}{n!}\right)$: even powers cancel, odd powers double:

$$\sinh x = \sum_{n=0}^\infty \frac{x^{2n+1}}{(2n+1)!} = x + \frac{x^3}{6} + \frac{x^5}{120} + \cdots$$

> **Answer**: $\sinh x = \sum_{n=0}^\infty \frac{x^{2n+1}}{(2n+1)!}$, all positive terms, radius $\infty$

### A2. Prove $e^{i\theta} = \cos\theta + i\sin\theta$ using Maclaurin series.

$$e^{i\theta} = \sum_{n=0}^\infty \frac{(i\theta)^n}{n!}.$$

Separate even/odd $n$ (using $i^{2k} = (-1)^k$, $i^{2k+1} = (-1)^k i$):

$$e^{i\theta} = \sum_{k=0}^\infty \frac{(-1)^k\theta^{2k}}{(2k)!} + i\sum_{k=0}^\infty \frac{(-1)^k\theta^{2k+1}}{(2k+1)!} = \cos\theta + i\sin\theta.$$

> **Answer**: the real part sums to $\cos\theta$, the imaginary part to $\sin\theta$ — Euler's formula

### A3. Find the Taylor series for $f(x)=\frac{1}{x}$ about $a=2$.

$\frac{1}{x} = \frac{1}{2+(x-2)} = \frac12\cdot\frac{1}{1+(x-2)/2} = \frac12\sum_{n=0}^\infty \left(-\frac{x-2}{2}\right)^n = \sum_{n=0}^\infty \frac{(-1)^n}{2^{n+1}}(x-2)^n$.

Valid for $\left|\frac{x-2}{2}\right|<1$, i.e. $0<x<4$ (radius $2$).

> **Answer**: $\frac{1}{x} = \sum_{n=0}^\infty \frac{(-1)^n}{2^{n+1}}(x-2)^n$, radius $2$

### A4. Evaluate $\lim_{x\to0}\frac{\tan x - x}{x^3}$ using series.

$\tan x = x + \frac{x^3}{3} + \frac{2x^5}{15} + \cdots$, so $\frac{\tan x - x}{x^3} = \frac{\frac{x^3}{3} + \cdots}{x^3} \to \frac13$.

> **Answer**: $\frac13$

### A5. Compute $\int_0^1 \frac{\sin x}{x}dx$ to 4 decimal places using series.

$\frac{\sin x}{x} = 1 - \frac{x^2}{3!} + \frac{x^4}{5!} - \frac{x^6}{7!} + \cdots$

$$\int_0^1 \frac{\sin x}{x}dx = 1 - \frac{1}{3\cdot3!} + \frac{1}{5\cdot5!} - \frac{1}{7\cdot7!} + \cdots = 1 - \frac{1}{18} + \frac{1}{600} - \frac{1}{35280} + \cdots$$

$= 0.946083\ldots$; alternating, error $\le \frac{1}{35280} \approx 2.8\times10^{-5} < 0.00005$.

> **Answer**: $\approx 0.9461$

### A6. Find the Maclaurin series for $\arcsin x$.

$(1-x^2)^{-1/2} = 1 + \frac{x^2}{2} + \frac{3x^4}{8} + \frac{5x^6}{16} + \cdots$; integrate:

$$\arcsin x = x + \frac{x^3}{6} + \frac{3x^5}{40} + \frac{5x^7}{112} + \cdots$$

> **Answer**: $\arcsin x = \sum_{n=0}^\infty \frac{1\cdot3\cdots(2n-1)}{2^n n!(2n+1)}x^{2n+1}$ (same as Practice 5)

### A7. How many terms of $\sin x$ series are needed to estimate $\sin(1)$ with error $<10^{-6}$?

For $0\le x\le1$ the series is alternating with decreasing terms, so after keeping up to $x^{2n+1}$ the error is $\le \frac{1}{(2n+3)!}$.

Need $\frac{1}{(2n+3)!} < 10^{-6}$: $9! = 362880 < 10^6$, $10! = 3628800 > 10^6$, so take $2n+3 \ge 10$, i.e. keep up to $x^9/9!$ — **5 terms** ($n=0,\dots,4$). Error $\le \frac{1}{11!} \approx 2.5\times10^{-8}$.

> **Answer**: 5 terms (up to $x^9/9!$)

### A8. Find the sum: $1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\cdots$. Recognize the series.

$\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots$; at $x=1$: $1 - \frac12 + \frac13 - \frac14 + \cdots = \ln 2$.

> **Answer**: $\ln 2 \approx 0.6931$

### A9. Derive the Taylor series for $\frac{1}{(1-x)^2}$.

$\frac{1}{1-x} = \sum x^n$; $\frac{1}{(1-x)^2} = \frac{d}{dx}\frac{1}{1-x} = \sum_{n=1}^\infty n x^{n-1} = \sum_{n=0}^\infty (n+1)x^n$.

> **Answer**: $\frac{1}{(1-x)^2} = \sum_{n=0}^\infty (n+1)x^n$, $|x|<1$

### A10. Use the Lagrange remainder to prove that $e$ is irrational.

Assume $e = \frac{p}{q}$ with integers $p, q > 0$.

① For any $n \ge q$, multiply $e = \sum_{k=0}^n \frac{1}{k!} + R_n$ by $n!$:

$$n!\,e - \sum_{k=0}^n \frac{n!}{k!} = n!\,R_n.$$

The left side is an integer: $n!\,e = n!\frac{p}{q}$ is an integer when $n\ge q$, and each $\frac{n!}{k!}$ is an integer.

② Bound the remainder: $R_n = \frac{e^c}{(n+1)!}$ for some $c\in(0,1)$, so $0 < n!R_n \le \frac{3n!}{(n+1)!} = \frac{3}{n+1} < 1$ for $n \ge 3$.

③ Contradiction: an integer strictly between $0$ and $1$ is impossible. Hence $e$ is irrational.

> **Answer**: the integer-vs-fraction contradiction proves $e\notin\mathbb{Q}$

### A11. Use series to evaluate $\lim_{x\to 0}\frac{\sin x - x + x^3/6}{x^5}$. How many terms are needed?

$\sin x = x - \frac{x^3}{6} + \frac{x^5}{120} - \frac{x^7}{5040} + \cdots$, so

$$\frac{\sin x - x + \frac{x^3}{6}}{x^5} = \frac{\frac{x^5}{120} - \frac{x^7}{5040} + \cdots}{x^5} \to \frac{1}{120}.$$

Terms needed: up to $x^5$ — i.e. **3 terms** of $\sin x$ ($x$, $x^3/6$, $x^5/120$).

> **Answer**: $\frac{1}{120}$ (3 terms of the sine series)

### A12. Find the Maclaurin series for $\ln(1+\sin x)$ up to $x^4$.

① $u = \sin x = x - \frac{x^3}{6} + O(x^5)$; $\ln(1+u) = u - \frac{u^2}{2} + \frac{u^3}{3} - \frac{u^4}{4} + O(u^5)$.

② Compute each power up to $x^4$:
- $u^2 = x^2 - \frac{x^4}{3} + O(x^6)$
- $u^3 = x^3 + O(x^5)$
- $u^4 = x^4 + O(x^6)$

③ Substitute:

$$\ln(1+\sin x) = \left(x-\frac{x^3}{6}\right) - \frac12\left(x^2 - \frac{x^4}{3}\right) + \frac13 x^3 - \frac14 x^4 + O(x^5)$$

$$= x - \frac{x^2}{2} + \left(-\frac16+\frac13\right)x^3 + \left(\frac16-\frac14\right)x^4 + O(x^5) = x - \frac{x^2}{2} + \frac{x^3}{6} - \frac{x^4}{12} + O(x^5).$$

> **Answer**: $\ln(1+\sin x) = x - \frac{x^2}{2} + \frac{x^3}{6} - \frac{x^4}{12} + \cdots$

---

## Answer Check

| Problem | Answer |
|:--------|:-------|
| Practice 1 | $xe^x = \sum x^n/(n-1)!$ |
| Practice 2 | $\ln x = \sum \frac{(-1)^{n+1}}{n}(x-1)^n$, $(0,2]$ |
| Practice 3 | $\frac{1}{24}$ |
| Practice 4 | $\approx 0.0415$ |
| Practice 5 | $\arcsin x = x + x^3/6 + \cdots$; limit $\frac16$ |
| Practice 6 | $n=9$ (10 terms) |
| D1–D12 | see above |
