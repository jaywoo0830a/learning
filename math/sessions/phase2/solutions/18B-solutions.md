# Solutions — 18B: Power Series — Where Does It Converge?

> Back to [18B — Power Series](../18B-power-series.md)
## Basic Drills

### D1. Find $R$ for $\sum_{n=0}^\infty \frac{x^n}{2^n}$.

This is geometric in $\frac{x}{2}$: converges for $\left|\frac{x}{2}\right|<1$, i.e. $|x|<2$.

> **Answer**: $R = 2$

### D2. Find $R$ for $\sum_{n=1}^\infty \frac{n x^n}{3^n}$.

$c_n = \frac{n}{3^n}$: $R = \lim \frac{n/3^n}{(n+1)/3^{n+1}} = 3\lim\frac{n}{n+1} = 3$.

> **Answer**: $R = 3$

### D3. Find interval for $\sum_{n=0}^\infty \frac{(-1)^n x^n}{n+1}$.

$R = \lim \frac{1/(n+1)}{1/(n+2)} = 1$. Endpoints:
- $x=1$: $\sum \frac{(-1)^n}{n+1}$ — converges (alternating).
- $x=-1$: $\sum \frac{1}{n+1}$ — diverges (harmonic).

> **Answer**: interval $(-1, 1]$

### D4. Write $\frac{1}{1+2x}$ as a power series. For which $x$?

$\frac{1}{1+2x} = \frac{1}{1-(-2x)} = \sum_{n=0}^\infty (-2x)^n = \sum_{n=0}^\infty (-2)^n x^n$, valid for $|-2x|<1$, i.e. $|x|<\frac12$.

> **Answer**: $\sum (-2)^n x^n$, $|x| < \frac12$

### D5. Find a series for $\frac{1}{(1-x)^2}$.

$\frac{d}{dx}\frac{1}{1-x} = \frac{1}{(1-x)^2} = \frac{d}{dx}\sum_{n=0}^\infty x^n = \sum_{n=1}^\infty n x^{n-1} = \sum_{n=0}^\infty (n+1)x^n$.

> **Answer**: $\frac{1}{(1-x)^2} = \sum_{n=0}^\infty (n+1)x^n$, $|x|<1$

### D6. Find a series for $\ln(1-x)$.

$-\ln(1-x) = \int \frac{dx}{1-x} = \int \sum x^n dx = \sum \frac{x^{n+1}}{n+1} = \sum_{n=1}^\infty \frac{x^n}{n}$. So $\ln(1-x) = -\sum_{n=1}^\infty \frac{x^n}{n}$.

> **Answer**: $\ln(1-x) = -\sum_{n=1}^\infty \frac{x^n}{n}$, $|x|<1$

### D7. Evaluate $\sum_{n=1}^\infty \frac{n}{2^n}$.

$\sum_{n=1}^\infty n x^n = x\sum n x^{n-1} = x\cdot\frac{1}{(1-x)^2} = \frac{x}{(1-x)^2}$ (using D5). At $x=\frac12$:

$\sum \frac{n}{2^n} = \frac{1/2}{(1/2)^2} = 2$.

> **Answer**: $2$

### D8. Find interval for $\sum_{n=1}^\infty \frac{(x+1)^n}{n^2}$.

$R=1$, center $-1$. Endpoints: $x=0$: $\sum \frac{1}{n^2}$ converges; $x=-2$: $\sum \frac{(-1)^n}{n^2}$ converges (absolutely).

> **Answer**: interval $[-2, 0]$

### D9. Differentiate the series for $\sin x = \sum (-1)^n \frac{x^{2n+1}}{(2n+1)!}$.

$\frac{d}{dx}\sin x = \sum (-1)^n \frac{(2n+1)x^{2n}}{(2n+1)!} = \sum_{n=0}^\infty \frac{(-1)^n x^{2n}}{(2n)!} = \cos x$. ✓

> **Answer**: $\cos x = \sum \frac{(-1)^n x^{2n}}{(2n)!}$ — term-by-term differentiation recovers the cosine series

### D10. Find $R$ for $\sum_{n=0}^\infty \frac{(2n)!}{(n!)^2}x^n$.

$\frac{c_{n+1}}{c_n} = \frac{(2n+2)!}{(n+1)!(n+1)!}\cdot\frac{n!n!}{(2n)!} = \frac{(2n+2)(2n+1)}{(n+1)^2} \to 4$. So $R = \frac{1}{4}$.

> **Answer**: $R = \frac14$

### D11. Find a power series for $\frac{x}{(1-x)^2}$.

$\frac{x}{(1-x)^2} = x\cdot\sum_{n=0}^\infty (n+1)x^n = \sum_{n=0}^\infty (n+1)x^{n+1} = \sum_{n=1}^\infty n x^n$.

> **Answer**: $\frac{x}{(1-x)^2} = \sum_{n=1}^\infty n x^n$, $|x|<1$

### D12. Evaluate $\sum_{n=0}^\infty \frac{(-1)^n}{2^n}$.

$\sum \left(-\frac12\right)^n = \frac{1}{1-(-1/2)} = \frac{1}{3/2} = \frac23$.

> **Answer**: $\frac23$

### D13. Evaluate $1 - \frac12 + \frac13 - \frac14 + \cdots$ — and justify that the endpoint is allowed.

This is $\sum_{n=1}^\infty \frac{(-1)^{n+1}}{n}$, i.e. the series for $\ln(1+x)$ at $x=1$. The interval of the $\ln(1+x)$ series is $(-1,1]$ — at $x=1$ the alternating series converges, at $x=-1$ it is the harmonic series. Since $x=1$ lies inside the interval, the value is legitimate:

$$1-\frac12+\frac13-\frac14+\cdots = \ln 2.$$

> **Answer**: $\ln 2$ — endpoint values are only trustworthy after the endpoint check.

### D14. Write $\sum_{n=1}^\infty n x^{n-1}$ starting from $n=0$, then evaluate $\sum_{n=1}^\infty \frac{n}{2^{n-1}}$.

Shift $k=n-1$: $\sum_{n=1}^\infty n x^{n-1} = \sum_{k=0}^\infty (k+1)x^k$. This is the derivative of the geometric series:

$$\sum_{k=0}^\infty (k+1)x^k = \frac{1}{(1-x)^2}, \qquad |x|<1.$$

At $x=\frac12$: $\sum_{n=1}^\infty \frac{n}{2^{n-1}} = \frac{1}{(1-\frac12)^2} = 4$.

> **Answer**: $4$

### D15. Evaluate $\sum_{n=1}^\infty \frac{n^2}{2^n}$.

Split $n^2 = n(n-1)+n$. Differentiating the geometric series twice:

$$\sum_{n=0}^\infty n(n-1)x^{n-2} = \frac{2}{(1-x)^3} \;\Rightarrow\; \sum_{n=1}^\infty n(n-1)x^n = \frac{2x^2}{(1-x)^3},$$
$$\sum_{n=1}^\infty n x^n = \frac{x}{(1-x)^2}.$$

At $x=\frac12$: $\sum \frac{n(n-1)}{2^n} = \frac{2\cdot\frac14}{(\frac12)^3} = 4$ and $\sum \frac{n}{2^n} = \frac{\frac12}{(\frac12)^2} = 2$. Total $4+2=6$.

> **Answer**: $6$ — $n^2=n(n-1)+n$ decomposes any polynomial-in-$n$ sum into derivatives of the geometric series.

### D16. Find $R$ for $\sum_{n=0}^\infty \left(\frac{x}{2}\right)^{n^2}$.

The coefficients are $c_k = 2^{-k}$ when $k$ is a perfect square and $c_k=0$ otherwise. The ratio test is helpless (infinitely many zero coefficients). Root test:

$$\limsup_{k\to\infty}\left|c_k x^k\right|^{1/k} = \left|\frac{x}{2}\right| \quad (\text{limit over square indices}).$$

Convergence when $\left|\frac{x}{2}\right|<1$, i.e. $|x|<2$.

> **Answer**: $R=2$ — the root test handles "gappy" series where the ratio test cannot even start.

---

## Advanced Drills

### A1. Find the interval for $\sum_{n=1}^\infty \frac{n(x+3)^n}{4^n}$.

$c_n = \frac{n}{4^n}$: $R = \lim \frac{n/4^n}{(n+1)/4^{n+1}} = 4$. Center $-3$ → interval $(-7, 1)$.

Endpoints:
- $x=1$: $\sum \frac{n\cdot4^n}{4^n} = \sum n$ — diverges (terms $\to\infty$).
- $x=-7$: $\sum \frac{n(-4)^n}{4^n} = \sum (-1)^n n$ — diverges (terms $\to\infty$, not even $\to 0$).

> **Answer**: interval $(-7, 1)$ — both endpoints excluded

### A2. Find a power series for $\frac{x}{1+x-2x^2}$.

① Factor: $1+x-2x^2 = (1-x)(1+2x)$.

② Partial fractions: $\frac{x}{(1-x)(1+2x)} = \frac{A}{1-x} + \frac{B}{1+2x}$.
$x = A(1+2x) + B(1-x)$ → $A+B=0$, $2A-B=1$ → $A=\frac13$, $B=-\frac13$.

③ Geometric series: $\frac{1}{3}\sum x^n - \frac{1}{3}\sum (-2x)^n = \sum \frac{1-(-2)^n}{3}x^n$.

> **Answer**: $\frac{x}{1+x-2x^2} = \sum_{n=0}^\infty \frac{1-(-2)^n}{3}x^n$, $|x|<\frac12$

### A3. Evaluate $\lim_{x\to0}\frac{e^x-1-x}{x^2}$.

$e^x = 1+x+\frac{x^2}{2}+\frac{x^3}{6}+\cdots$, so $\frac{e^x-1-x}{x^2} = \frac{\frac{x^2}{2}+\cdots}{x^2} \to \frac12$.

> **Answer**: $\frac12$

### A4. Prove $\sum_{n=1}^\infty \frac{n}{3^n} = \frac{3}{4}$.

$\sum_{n=0}^\infty x^n = \frac{1}{1-x}$; differentiate: $\sum_{n=1}^\infty n x^{n-1} = \frac{1}{(1-x)^2}$, so $\sum_{n=1}^\infty n x^n = \frac{x}{(1-x)^2}$.

At $x=\frac13$: $\frac{1/3}{(1-1/3)^2} = \frac{1/3}{(2/3)^2} = \frac{1/3}{4/9} = \frac{3}{4}$.

> **Answer**: $\sum \frac{n}{3^n} = \frac34$ ✓

### A5. Find the interval for $\sum_{n=1}^\infty \frac{(x-1)^n}{n\cdot5^n}$.

$R=5$, center $1$ → interval $(-4, 6)$.
- $x=6$: $\sum \frac{1}{n}$ — diverges.
- $x=-4$: $\sum \frac{(-1)^n}{n}$ — converges.

> **Answer**: interval $[-4, 6)$

### A6. Express $\int_0^{1/2} \frac{dx}{1+x^4}$ as a series. Compute to 4 decimal places.

$\frac{1}{1+x^4} = \sum_{n=0}^\infty (-1)^n x^{4n}$, so

$$\int_0^{1/2}\frac{dx}{1+x^4} = \sum_{n=0}^\infty (-1)^n \frac{(1/2)^{4n+1}}{4n+1}.$$

Terms: $\frac12 - \frac{1}{5\cdot32} + \frac{1}{9\cdot512} - \frac{1}{13\cdot8192} + \cdots = 0.5 - 0.00625 + 0.000217 - 0.0000094 + \cdots$

Alternating: after $0.5 - 0.00625 + 0.000217 = 0.493967$, the next term ($\approx 9.4\times10^{-6}$) bounds the error, well under $0.00005$.

> **Answer**: $\sum_{n=0}^\infty \frac{(-1)^n}{4n+1}\left(\frac12\right)^{4n+1} \approx 0.4940$

### A7. Find all $x$ for which $\sum_{n=0}^\infty \frac{n!\,(x-2)^n}{n^n}$ converges.

**Ratio**: $\frac{a_{n+1}}{a_n} = \frac{(n+1)!\,(x-2)^{n+1}/(n+1)^{n+1}}{n!(x-2)^n/n^n} = \left(\frac{n}{n+1}\right)^n |x-2| \to \frac{|x-2|}{e}$.

So the series converges for $|x-2| < e$, i.e. $R = e$.

**Stirling check**: $\frac{n!}{n^n} \sim \sqrt{2\pi n}\,e^{-n}$, so $\sqrt[n]{|a_n|} \to \frac{|x-2|}{e}$ — same radius $e$.

> **Answer**: converges for $|x-2| < e$ (radius $R = e$, center $2$)

### A8. A power series satisfies $f'(x)=f(x)$ with $f(0)=1$. Find the series and identify $f$.

Let $f = \sum_{n=0}^\infty c_n x^n$, $c_0 = f(0) = 1$. Then $f' = \sum_{n=1}^\infty n c_n x^{n-1} = \sum_{k=0}^\infty (k+1)c_{k+1}x^k$.

Equating $f' = f$: $(k+1)c_{k+1} = c_k$, so $c_{k+1} = \frac{c_k}{k+1}$ → $c_n = \frac{1}{n!}$.

> **Answer**: $f(x) = \sum_{n=0}^\infty \frac{x^n}{n!} = e^x$

### A9. Find the radius for $\sum_{n=0}^\infty \binom{2n}{n}x^n$.

$\frac{c_{n+1}}{c_n} = \frac{\binom{2n+2}{n+1}}{\binom{2n}{n}} = \frac{(2n+2)(2n+1)}{(n+1)(n+1)} \to 4$, so $R = \frac14$.

> **Answer**: $R = \frac14$

### A10. Multiply the series for $e^x$ by itself. Show the result is the series for $e^{2x}$.

$(e^x)^2 = \left(\sum \frac{x^n}{n!}\right)\left(\sum \frac{x^n}{n!}\right) = \sum_{n=0}^\infty \left(\sum_{k=0}^n \frac{1}{k!}\frac{1}{(n-k)!}\right)x^n$.

Inner sum: $\frac{1}{n!}\sum_{k=0}^n \frac{n!}{k!(n-k)!} = \frac{1}{n!}\sum_{k=0}^n \binom{n}{k} = \frac{2^n}{n!}$ (binomial theorem).

So $(e^x)^2 = \sum \frac{2^n}{n!}x^n = e^{2x}$. ✓

> **Answer**: Cauchy product gives $\sum \frac{2^n}{n!}x^n = e^{2x}$

### A11. Find the radius and interval of convergence for $\sum_{n=1}^\infty \frac{(3x-1)^n}{n\cdot 2^n}$.

Rewrite: $\frac{(3x-1)^n}{n2^n} = \frac{3^n}{n2^n}\left(x-\frac13\right)^n$. Center $a=\frac13$.

$R = \lim \frac{c_n}{c_{n+1}} = \lim \frac{3^n/(n2^n)}{3^{n+1}/((n+1)2^{n+1})} = \frac23 \lim \frac{n+1}{n} = \frac23$.

Interval: $\left(\frac13 - \frac23,\, \frac13 + \frac23\right) = \left(-\frac13,\, 1\right)$.
- $x=1$: $\sum \frac{1}{n}$ — diverges.
- $x=-\frac13$: $\sum \frac{(-1)^n}{n}$ — converges.

> **Answer**: radius $\frac23$, interval $[-\frac13, 1)$

### A12. Find a power series for $\ln\left(\frac{1+x}{1-x}\right)$. What is its interval of convergence?

$\ln\frac{1+x}{1-x} = \ln(1+x) - \ln(1-x) = \sum_{n=1}^\infty \frac{(-1)^{n+1}x^n}{n} + \sum_{n=1}^\infty \frac{x^n}{n}$.

Odd $n$: $(-1)^{n+1} = 1$, terms double: $\frac{2x^n}{n}$. Even $n$: $(-1)^{n+1} = -1$, terms cancel.

So $\ln\frac{1+x}{1-x} = 2\sum_{k=0}^\infty \frac{x^{2k+1}}{2k+1} = 2\left(x + \frac{x^3}{3} + \frac{x^5}{5} + \cdots\right)$.

Interval: $\ln(1+x)$ needs $x\in(-1,1]$, $\ln(1-x)$ needs $x\in[-1,1)$ → intersection $(-1,1)$; both endpoints diverge (the log blows up).

> **Answer**: $\ln\frac{1+x}{1-x} = 2\sum_{k=0}^\infty \frac{x^{2k+1}}{2k+1}$, interval $(-1,1)$

---

## Answer Check

| Problem | Answer |
|:--------|:-------|
| D1–D12 | see above |
