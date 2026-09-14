# Session 18C: Taylor Series — Approximating Any Function

**Phase 2 — Classical Techniques | 65 min**

*Prerequisites: 18B (power series), 14C (higher derivatives)*

> 💡 **Stuck?** Every problem has a collapsible **Hint** below it — click it only when you need a nudge.

> **Source.** Every example and drill below is taken from Stewart, *Calculus*, Chapter 11 (Sections 11.10–11.11). Each item cites its section and exercise number.

---

## Example 1: Taylor Polynomials — The Idea (§11.11 Ex 1, 🔗 14C)

A Taylor polynomial $T_n(x)$ matches $f$ and its first $n$ derivatives at $x=a$ (🔗 14C for higher derivatives).

$T_1$ = tangent line. $T_2$ = tangent parabola (matches curvature). $T_3$ = matches jerk too.

$f(x)=\sin x$ at $a=0$:
$T_1(x)=x$. $T_3(x)=x-\frac{x^3}{6}$. $T_5(x)=x-\frac{x^3}{6}+\frac{x^5}{120}$.

![Taylor polynomials of sin x]({{graph:18c-taylor-polynomials}})

*Graph 18C-1: Left — Taylor polynomials $T_1$, $T_3$, $T_5$, $T_7$ of $\sin x$ at $a=0$. Higher degree = better approximation over a wider interval. Right — Error $|\sin x - T_N(x)|$ on log scale: error decreases as degree increases, especially near the center.*

---

## Example 2: The Taylor Series Formula — Where the $n!$ Comes From (§11.10)

Suppose $f(x) = \sum c_k(x-a)^k$ near $a$. Differentiate both sides $k$ times and set $x=a$: every term of degree $<k$ has already died, and every term of degree $>k$ still contains $(x-a)$, so it vanishes at $x=a$. The sole survivor is $k!\,c_k$, hence

$$f^{(k)}(a) = k!\,c_k \quad\Rightarrow\quad c_k = \frac{f^{(k)}(a)}{k!}.$$

The coefficients are **forced** — there is no freedom. Equivalently (**uniqueness**): if any power series equals $f$ near $a$, it must be this one. That is the license behind every shortcut below — substitution, multiplication, and integration all produce *some* correct series, and uniqueness guarantees it is *the* Taylor series.

$$f(x) = \sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!}(x-a)^n.$$

When $a=0$, it is called a **Maclaurin series**.

---

## Example 3: Maclaurin Series — The Six You Must Memorize (§11.10 Ex 2, Ex 5, Ex 6)

| Function | Maclaurin Series | Radius |
|:--------:|:-----------------|:------:|
| $e^x$ | $\sum_{n=0}^\infty \frac{x^n}{n!} = 1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots$ | $\infty$ |
| $\sin x$ | $\sum_{n=0}^\infty \frac{(-1)^n x^{2n+1}}{(2n+1)!}$ | $\infty$ |
| $\cos x$ | $\sum_{n=0}^\infty \frac{(-1)^n x^{2n}}{(2n)!}$ | $\infty$ |
| $\frac{1}{1-x}$ | $\sum_{n=0}^\infty x^n$ | $1$ |
| $\ln(1+x)$ | $\sum_{n=1}^\infty \frac{(-1)^{n+1}x^n}{n}$ | $1$ |
| $\arctan x$ | $\sum_{n=0}^\infty \frac{(-1)^n x^{2n+1}}{2n+1}$ | $1$ |

> **Why these radii (🔗 18B):** $R=\infty$ for $e^x$, $\sin x$, $\cos x$ — no bad points anywhere. The three series with $R=1$ stop there because their closed forms have a bad point at distance 1 from the center: $\frac{1}{1-x}$ blows up at $x=1$; $\ln(1+x)$ at $x=-1$; and $\arctan x$ has complex bad points at $x=\pm i$ — the radius measures distance, not visibility.

![Taylor approximations of e^x]({{graph:18c-taylor-exp}})

*Graph 18C-2: Left — Taylor polynomials $T_1$, $T_2$, $T_3$, $T_5$ of $e^x$ at $a=0$. Right — Error on log scale: exponential convergence near $x=0$.*

---

## Example 4: Building New Taylor Series (§11.10 Ex 8, Ex 9, Ex 10)

**Substitution**: replace $x$ with something.
$\sin(x^2) = \sum (-1)^n \frac{(x^2)^{2n+1}}{(2n+1)!} = \sum (-1)^n \frac{x^{4n+2}}{(2n+1)!}$.

**Multiply/divide by $x$**:
$\frac{\sin x}{x} = \sum (-1)^n \frac{x^{2n}}{(2n+1)!}$.

**Binomial series**: $(1+x)^k = \sum_{n=0}^\infty \binom{k}{n}x^n = 1+kx+\frac{k(k-1)}{2!}x^2+\cdots$, $|x|<1$.

$\frac{1}{\sqrt{4-x}} = \frac{1}{2}\left(1-\frac{x}{4}\right)^{-1/2} = \frac12\sum_{n=0}^\infty \binom{-1/2}{n}\left(-\frac{x}{4}\right)^n$.

$x\cos x = x\sum_{n=0}^\infty \frac{(-1)^n x^{2n}}{(2n)!} = \sum_{n=0}^\infty \frac{(-1)^n x^{2n+1}}{(2n)!}$.

$\ln(1+3x^2) = \sum_{n=1}^\infty \frac{(-1)^{n+1}(3x^2)^n}{n} = \sum_{n=1}^\infty \frac{(-1)^{n+1}3^n x^{2n}}{n}$.

---

## Example 5: Error Bound — Taylor's Inequality (§11.11 Ex 1, Ex 2)

$f(x) = T_n(x) + R_n(x)$ where $R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$ for some $c$ between $a$ and $x$.

**Taylor's Inequality**: if $|f^{(n+1)}(t)|\le M$ on the interval between $a$ and $x$, then
$$|R_n(x)| \le \frac{M}{(n+1)!}|x-a|^{n+1}.$$

**Where it comes from:** for $n=0$ this is exactly the Mean Value Theorem. Lagrange's formula is the same statement after matching $n+1$ derivatives instead of one: the leftover of the *next* derivative, evaluated somewhere in between.

For an **alternating** series: $|R_n| \le |\text{first omitted term}|$.

**Estimate $\sqrt[3]{x}$ at $a=8$ by $T_2$ (§11.11 Ex 1):**
$f(8)=2$, $f'(8)=\frac{1}{12}$, $f''(8)=-\frac{1}{144}$, so $T_2(x)=2+\frac{x-8}{12}-\frac{(x-8)^2}{288}$.
On $7\le x\le 9$, $|f'''(x)|=\frac{10}{27}x^{-8/3}\le\frac{10}{27}7^{-8/3}\approx0.0021$, so
$|R_2(x)|\le\frac{0.0021}{6}|x-8|^3\le0.00035$. The approximation is good to about $3\times10^{-4}$.

**Estimate $\sin 12^\circ$ by $T_5$ (§11.11 Ex 2):** with $x=\frac{\pi}{15}$, $|R_5|\le\frac{1}{6!}|x|^6<10^{-6}$, so six decimals are safe.

---

## Example 6: Limits Using Taylor Series (§11.10 Ex 14, 🔗 13A)

$$\lim_{x\to0}\frac{e^x-1-x}{x^2} = \lim_{x\to0}\frac{\left(1+x+\frac{x^2}{2}+\cdots\right)-1-x}{x^2} = \frac12.$$

**Why this works**: the series shows exactly how fast numerator and denominator approach 0. The lowest surviving power of $x$ decides the limit.

---

## Example 7: Definite Integrals Using Series (§11.10 Ex 13, 🔗 18B, 16A)

$$\int_0^1 e^{-x^2}dx = \int_0^1\left(1-x^2+\frac{x^4}{2!}-\frac{x^6}{3!}+\cdots\right)dx = 1-\frac{1}{3}+\frac{1}{5\cdot2!}-\frac{1}{7\cdot3!}+\cdots$$

Term-by-term integration (🔗 18B) gives an alternating series — easy to estimate to any accuracy.

---

## Example 8: Multiplication and Division of Series (§11.10 Ex 15)

**Multiply** the known series and collect like powers:
$e^x\sin x = \left(1+x+\frac{x^2}{2}+\cdots\right)\left(x-\frac{x^3}{6}+\cdots\right) = x+x^2+\frac{x^3}{3}-\frac{x^5}{30}+\cdots$

**Divide** by solving for the unknown coefficients: $\tan x = x+\frac{x^3}{3}+\frac{2x^5}{15}+\cdots$

> **Up to here**: Taylor polynomial matches derivatives. Maclaurin = Taylor at 0. Six must-memorize series. Substitution / multiply / divide / integrate to build new ones. Error bound via Taylor's Inequality or the alternating first-term rule.

---

## Common Mistakes

### Mistake 1: Forgetting the factorial in the Taylor formula

**Wrong**: $f(x) = \sum f^{(n)}(a)(x-a)^n$. The correct formula divides by $n!$: $f(x) = \sum \frac{f^{(n)}(a)}{n!}(x-a)^n$.

### Mistake 2: Using the remainder without bounding the derivative

$R_n = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$ requires a bound $|f^{(n+1)}(c)| \le M$ **on the whole interval between $a$ and $x$**. Plugging in the center value instead of the maximum is a common error.

### Mistake 3: Dropping terms when composing series

When composing $\ln(1+u)$ with $u = \sin x$, keep enough terms of $u$ (and its powers) to reach the requested order — to get $x^4$ you also need $u^2$ to order $x^4$, because $u$ itself starts at $x$.

### Mistake 4: Confusing the degree with the number of terms

$T_n$ contains $n+1$ terms (from $x^0$ through $x^n$). Keeping terms up to $x^n$ leaves an error controlled by the $(n+1)$-st term.

---

## What We Just Did

```
(1) T_n matches f and its first n derivatives at a. Coeffs forced: c_n = f^(n)(a)/n!.
(2) Six Maclaurin series: e^x, sin x, cos x, 1/(1-x), ln(1+x), arctan x.
(3) Build new series by substitution, multiply/divide, differentiate, integrate.
(4) Error via Taylor's Inequality M|x-a|^(n+1)/(n+1)!; alternating ⇒ first omitted term.
(5) Limits and integrals: expand, keep the lowest surviving power.
```

---

## Basic Drills

**D1.** (§11.10 #14) Maclaurin series for $e^{-2x}$.

**D2.** (§11.10 #16) Maclaurin series for $\sin 3x$.

**D3.** (§11.11 #3) Find $T_3(x)$ for $f(x)=e^x$ at $a=1$.

<details>
<summary>💡 Hint</summary>

Every derivative of $e^x$ equals $e^x$, so all the values at $a=1$ are $e$.

</details>

**D4.** (§11.10 #12) Maclaurin series and radius for $\ln(1+x)$.

**D5.** (§11.10 #13) Maclaurin series and radius for $\cos x$.

**D6.** (§11.11 #5) Find $T_3(x)$ for $f(x)=\cos x$ at $a=\frac{\pi}{2}$.

<details>
<summary>💡 Hint</summary>

$\cos(\pi/2)=0$, $f'(\pi/2)=-1$, $f''(\pi/2)=0$, $f'''(\pi/2)=1$.

</details>

**D7.** (§11.10 #18) Maclaurin series for $x\cos x$.

**D8.** (§11.10 #11) Maclaurin series for $(1-x)^{-2}$.

**D9.** (§11.10 #42) Maclaurin series for $e^{3x}-e^{2x}$.

**D10.** (§11.11 #25) How many terms of the Maclaurin series for $e^x$ estimate $e^{0.1}$ within $10^{-5}$?

<details>
<summary>💡 Hint</summary>

Need $\frac{(0.1)^{n+1}}{(n+1)!}<10^{-5}$. Test $n=2,3$.

</details>

**D11.** (§11.10 #40) Maclaurin series for $\sin\left(\frac{\pi x}{4}\right)$.

**D12.** (§11.10 #44) Maclaurin series for $x^2\ln(1+x^3)$.

**D13.** (§11.10 #47) Maclaurin series for $\sin^2 x$.

<details>
<summary>💡 Hint</summary>

Use $\sin^2 x=\frac12(1-\cos 2x)$.

</details>

**D14.** (§11.10 #3) If $f^{(n)}(0)=(n+1)!$, find the Maclaurin series and identify $f$.

<details>
<summary>💡 Hint</summary>

$c_n=\frac{f^{(n)}(0)}{n!}=n+1$.

</details>

**D15.** (§11.11 #27) For which $x$ is $\sin x\approx x-\frac{x^3}{6}$ accurate to within $0.01$?

**D16.** (§11.10 #35) Binomial series for $\sqrt[4]{1-x}$.

<details>
<summary>💡 Hint</summary>

$(1+u)^{1/4}=1+\frac{u}{4}-\frac{3u^2}{32}+\frac{7u^3}{128}-\cdots$ with $u=-x$.

</details>

> Solutions: [Solutions](solutions/18C-solutions.md#basic-drill)

---

## Advanced Drills

**A1.** (§11.10 #49) Maclaurin series for $\sinh x=\frac{e^x-e^{-x}}{2}$.

**A2.** (§11.10 #50) Show $\tanh^{-1} x=\sum_{n=0}^\infty \frac{x^{2n+1}}{2n+1}$ using $\tanh^{-1}x=\frac12\ln\left(\frac{1+x}{1-x}\right)$.

**A3.** (§11.10 #21) Taylor series for $f(x)=x^5+2x^3+x$ at $a=2$.

**A4.** (§11.10 #24) Taylor series for $f(x)=\frac{1}{x}$ at $a=-3$.

<details>
<summary>💡 Hint</summary>

$\frac1x=-\frac{1}{3}\cdot\frac{1}{1-\frac{x+3}{3}}$ — geometric in $(x+3)$.

</details>

**A5.** (§11.11 #30) Given $f^{(n)}(4)=\frac{(-1)^n n!}{3^n(n+1)}$, show the fifth-degree Taylor polynomial approximates $f(5)$ with error $<0.0002$.

**A6.** (§11.10 #37) Binomial series and radius for $\frac{1}{(2+x)^3}$.

**A7.** (§11.11 #59) Evaluate $\lim_{x\to0}\frac{\sin x-x}{x^3}$ with a series.

**A8.** (§11.11 #26) How many terms of the Maclaurin series for $\ln(1+x)$ estimate $\ln 1.4$ within $0.001$?

<details>
<summary>💡 Hint</summary>

At $x=0.4$ the series alternates; the first omitted term must be below $0.001$.

</details>

**A9.** (§11.11 #57) For $f(x)=\sqrt{x}$, $a=1$, $n=3$, estimate the error on $0.9\le x\le1.1$.

**A10.** (§11.11 #60) Expand $F=\frac{mgR^2}{(R+h)^2}$ in powers of $h/R$; for which $h$ is $F\approx mg$ accurate to 1%?

<details>
<summary>💡 Hint</summary>

$F=mg\left(1+\frac{h}{R}\right)^{-2}=mg\left[1-\frac{2h}{R}+\frac{3h^2}{R^2}-\cdots\right]$. Use the alternating bound with $R=6400$ km.

</details>

**A11.** (§11 Review #62) If $f(x)=e^{x^2}$, show $f^{(2n)}(0)=\frac{(2n)!}{n!}$.

**A12.** (§11.11 #39) Use Taylor's Inequality with $n=1$, $a=x_n$, $x=r$ to prove Newton's method is quadratic: $|x_{n+1}-r|\le\frac{M}{2K}|x_n-r|^2$.

<details>
<summary>💡 Hint</summary>

Write $0=f(r)=f(x_n)+f'(x_n)(r-x_n)+\frac{f''(\xi)}{2}(r-x_n)^2$ and use the definition of $x_{n+1}$.

</details>

> Solutions: [Solutions](solutions/18C-solutions.md#advanced-drill)

---

## How to Read These Symbols

| Symbol | Reads as | Meaning |
|:---:|:---:|------|
| Taylor series | "Taylor series" | f(x) = Σ f^{(n)}(a)/n! · (x-a)^n — infinite polynomial matching all derivatives at a |
| Maclaurin series | "Maclaurin series" | Taylor series centered at a=0 — special case |
| $n!$ | "n factorial" | product 1×2×3×...×n — grows extremely fast |
| $\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots$ | "sine x equals x minus x cubed over 3 factorial plus x to the fifth over 5 factorial minus ..." | Maclaurin series for sine — odd powers, alternating signs |
| $\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots$ | "cosine x equals one minus x squared over 2 factorial plus ..." | Maclaurin series for cosine — even powers, alternating signs |
| $e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$ | "e to the x equals one plus x plus x squared over 2 factorial ..." | Maclaurin series for exponential — all positive |
| $\frac{1}{1-x} = 1 + x + x^2 + x^3 + \cdots$ | "one over one minus x equals one plus x plus x squared ..." | geometric series — converges for |x|<1 |
| $\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots$ | "ln of one plus x equals x minus x squared over 2 plus x cubed over 3 ..." | Maclaurin series for natural log — alternating, converges for -1<x≤1 |
| Lagrange remainder | "Lagrange remainder" | R_n = f^{(n+1)}(ξ)/(n+1)! · (x-a)^{n+1} — bounds error of Taylor polynomial |
| $|R_n| \leq \frac{M}{(n+1)!}|x-a|^{n+1}$ | "absolute remainder less than or equal to M over n+1 factorial times x minus a to the n+1" | Taylor's Inequality — M = max of |f^{(n+1)}| on the interval |

---

## Terminology

| What we call it | Math term | Notation |
|:---:|:---:|:---:|
| infinite polynomial matching derivatives | Taylor series | $\sum \frac{f^{(n)}(a)}{n!}(x-a)^n$ |
| Taylor series at 0 | Maclaurin series | $\sum \frac{f^{(n)}(0)}{n!}x^n$ |
| error of n-th degree approximation | Lagrange remainder | $R_n = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}$ |
| bounding the remainder | Taylor's Inequality | $|R_n| \leq \frac{M}{(n+1)!}|x-a|^{n+1}$ |
| product 1·2·3·...·n | factorial | $n!$ |
