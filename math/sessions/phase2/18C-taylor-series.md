# Session 18C: Taylor Series — Approximating Any Function

**Phase 2 — Classical Techniques | 65 min**

*Prerequisites: 18B (power series), 14C (higher derivatives)*

> 💡 **Stuck?** Every problem has a collapsible **Hint** below it — click it only when you need a nudge.

---

## Example 1: Taylor Polynomials — The Idea (🔗 14C)

A Taylor polynomial $T_n(x)$ matches $f$ and its first $n$ derivatives at $x=a$ (🔗 14C for higher derivatives).

$T_1$ = tangent line. $T_2$ = tangent parabola (matches curvature). $T_3$ = matches jerk too.

$f(x)=\sin x$ at $a=0$:
$T_1(x)=x$. $T_3(x)=x-\frac{x^3}{6}$. $T_5(x)=x-\frac{x^3}{6}+\frac{x^5}{120}$.

![Taylor polynomials of sin x](graphs/0721/18C/18c-taylor-polynomials.png)

*Graph 18C-1: Left — Taylor polynomials $T_1$, $T_3$, $T_5$, $T_7$ of $\sin x$ at $a=0$. Higher degree = better approximation over a wider interval. Right — Error $|\sin x - T_N(x)|$ on log scale: error decreases as degree increases, especially near the center.*

---

## Example 2: The Taylor Series Formula

$f(x) = \displaystyle \sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!}(x-a)^n$.

When $a=0$, it's called a **Maclaurin series**.

---

## Example 3: Maclaurin Series — The Six You Must Memorize

| Function | Maclaurin Series | Radius |
|:--------:|:-----------------|:------:|
| $e^x$ | $\sum_{n=0}^\infty \frac{x^n}{n!} = 1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots$ | $\infty$ |
| $\sin x$ | $\sum_{n=0}^\infty \frac{(-1)^n x^{2n+1}}{(2n+1)!}$ | $\infty$ |
| $\cos x$ | $\sum_{n=0}^\infty \frac{(-1)^n x^{2n}}{(2n)!}$ | $\infty$ |
| $\frac{1}{1-x}$ | $\sum_{n=0}^\infty x^n$ | $1$ |
| $\ln(1+x)$ | $\sum_{n=1}^\infty \frac{(-1)^{n+1}x^n}{n}$ | $1$ |
| $\arctan x$ | $\sum_{n=0}^\infty \frac{(-1)^n x^{2n+1}}{2n+1}$ | $1$ |

![Taylor approximations of e^x](graphs/0721/18C/18c-taylor-exp.png)

*Graph 18C-2: Left — Taylor polynomials $T_1$, $T_2$, $T_3$, $T_5$ of $e^x$ at $a=0$. Right — Error on log scale: exponential convergence near $x=0$.*

---

## Example 4: Building New Taylor Series

**Substitution**: Replace $x$ with something.
$\sin(x^2) = \sum (-1)^n \frac{(x^2)^{2n+1}}{(2n+1)!} = \sum (-1)^n \frac{x^{4n+2}}{(2n+1)!}$.

**Multiply/divide by $x$**:
$\frac{\sin x}{x} = \sum (-1)^n \frac{x^{2n}}{(2n+1)!}$.

**Binomial series** (🔗 12B2): $(1+x)^k = \sum_{n=0}^\infty \binom{k}{n}x^n = 1+kx+\frac{k(k-1)}{2!}x^2+\cdots$, $|x|<1$.

$\sqrt{1+x} = (1+x)^{1/2} = 1+\frac{x}{2}-\frac{x^2}{8}+\frac{x^3}{16}-\cdots$.
$\frac{1}{\sqrt{1-x^2}} = (1-x^2)^{-1/2} = 1+\frac{x^2}{2}+\frac{3x^4}{8}+\cdots$.

---

## Example 5: Error Bound — Lagrange Remainder

$f(x) = T_n(x) + R_n(x)$ where $R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$ for some $c$ between $a$ and $x$.

For alternating series: $|R_n| \le |\text{first omitted term}|$.

**Estimate $e^{0.1}$ to 4 decimal places** using $n=3$: $1+0.1+\frac{0.01}{2}+\frac{0.001}{6}=1.105167$.
Error bound: $|R_3| \le \frac{e^{0.1}(0.1)^4}{24} \le \frac{3\cdot10^{-4}}{24} = 0.0000125 < 0.00005$. Good!

---

## Example 6: Limits Using Taylor Series (🔗 13A)

$\displaystyle \lim_{x\to0}\frac{\sin x - x}{x^3} = \lim_{x\to0}\frac{(x-\frac{x^3}{6}+\frac{x^5}{120}-\cdots)-x}{x^3} = -\frac{1}{6}$.

$\displaystyle \lim_{x\to0}\frac{e^x-1-x}{x^2} = \frac{1}{2}$.

**Why this works**: Taylor series reveal exactly how fast numerator and denominator approach 0. The lowest surviving power of $x$ determines the limit.

---

## Example 7: Definite Integrals Using Series (🔗 18B, 16A)

$\int_0^1 e^{-x^2}dx = \int_0^1\left(1-x^2+\frac{x^4}{2!}-\frac{x^6}{3!}+\cdots\right)dx = 1-\frac{1}{3}+\frac{1}{5\cdot2!}-\frac{1}{7\cdot3!}+\cdots$.

Term-by-term integration (🔗 18B) gives an alternating series — easy to estimate to any accuracy.

> **Up to here**: Taylor polynomial matches derivatives. Maclaurin series = Taylor at 0. Six must-memorize. Substitution/multiply/integrate to build new ones. Error bound via Lagrange or alternating first-term.

---

## Common Mistakes

### Mistake 1: Forgetting the factorial in the Taylor formula

**Wrong**: $f(x) = \sum f^{(n)}(a)(x-a)^n$. The correct formula divides by $n!$:
$f(x) = \sum \frac{f^{(n)}(a)}{n!}(x-a)^n$. Without the factorial, $\sin x$ would not come out right.

### Mistake 2: Using the Lagrange remainder without bounding the derivative

$R_n = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$ requires a bound $|f^{(n+1)}(c)| \le M$ **on the whole interval between $a$ and $x$**. Plugging in the center value instead of the max is a common error.

### Mistake 3: Dropping terms when composing series

When composing $\ln(1+u)$ with $u = \sin x$, you must keep enough terms of $u$ (and its powers) to reach the requested order — e.g. to get $x^4$ you need $u^2$ to order $x^4$ too, because $u$ itself starts at $x$.

### Mistake 4: Confusing the degree with the number of terms

The $n$-th degree Taylor polynomial $T_n$ contains $n+1$ terms (from the $x^0$ term through $x^n$). For error bounds, keeping terms up to $x^n$ leaves an error controlled by the $(n+1)$-st term.

---

## Practice 1

Find the Maclaurin series for $f(x)=xe^x$.

<details>
<summary>💡 Hint</summary>

Multiply the known Maclaurin series for $e^x$ by $x$, then shift the index.

</details>

→ Solutions: [Solutions](solutions/18C-solutions.md#practice-1)

---

## Practice 2

Find the Taylor series for $f(x)=\ln x$ centered at $a=1$.

<details>
<summary>💡 Hint</summary>

Write $\ln x = \ln(1 + (x-1))$ and use the Maclaurin series for $\ln(1+u)$ with $u = x-1$.

</details>

→ Solutions: [Solutions](solutions/18C-solutions.md#practice-2)

---

## Practice 3

Use Taylor series to evaluate $\lim_{x\to0}\frac{\cos x-1+x^2/2}{x^4}$.

<details>
<summary>💡 Hint</summary>

$\cos x = 1 - \frac{x^2}{2} + \frac{x^4}{24} - \frac{x^6}{720} + \cdots$. Subtract $1 - x^2/2$ and see which power of $x$ survives.

</details>

→ Solutions: [Solutions](solutions/18C-solutions.md#practice-3)

---

## Practice 4

Estimate $\int_0^{0.5} \sin(x^2)dx$ to 4 decimal places using series.

<details>
<summary>💡 Hint</summary>

$\sin(x^2) = x^2 - \frac{x^6}{3!} + \frac{x^{10}}{5!} - \cdots$. Integrate term-by-term and evaluate at $\frac12$ — it's an alternating series, so the first omitted term bounds the error.

</details>

→ Solutions: [Solutions](solutions/18C-solutions.md#practice-4)

---

## Practice 5: Real Battle (🔗 12B2, 13A, 18B)

Use the binomial series (🔗 12B2) to find the Maclaurin series for $\arcsin x$. Integrate $(1-x^2)^{-1/2}$ term-by-term (🔗 18B). Then use your series to evaluate $\lim_{x\to0}\frac{\arcsin x - x}{x^3}$ (🔗 13A).

<details>
<summary>💡 Hint</summary>

Expand $(1+u)^{-1/2}$ with the binomial series, substitute $u = -x^2$, then integrate. The first two terms of $\arcsin x$ are $x + \frac{x^3}{6}$.

</details>

→ Solutions: [Solutions](solutions/18C-solutions.md#practice-5)

---

## Practice 6: Real Battle — Error Analysis (🔗 18B)

How many terms of the Maclaurin series for $e^x$ are needed to approximate $e$ (i.e., $e^1$) with error less than $10^{-6}$? Use the Lagrange remainder bound. Compare with the actual error after that many terms.

<details>
<summary>💡 Hint</summary>

At $x=1$: $R_n \le \frac{e}{(n+1)!} \le \frac{3}{(n+1)!}$. Find the smallest $n$ with $(n+1)! > 3\times10^6$. Note $9! = 362880$, $10! = 3628800$.

</details>

→ Solutions: [Solutions](solutions/18C-solutions.md#practice-6)

---

## Basic Drills

**D1.** Write the Maclaurin series for $e^{-x}$ (first 4 terms).

**D2.** Write the Maclaurin series for $\cos(2x)$ (first 4 nonzero terms).

**D3.** Find the 3rd-degree Taylor polynomial of $f(x)=\sqrt{x}$ at $a=4$.

<details>
<summary>💡 Hint</summary>

Compute $f(4), f'(4), f''(4), f'''(4)$ from $f(x)=x^{1/2}$ — remember $f''$ and $f'''$ come with negative/alternating signs.

</details>

**D4.** Find the Maclaurin series for $\frac{1}{1+x^2}$ and its radius.

**D5.** Find the Maclaurin series for $\ln(1-x)$.

**D6.** Use series to compute $\lim_{x\to0}\frac{e^x-1}{x}$.

**D7.** Find $T_2(x)$ (2nd-degree Taylor) for $f(x)=\tan x$ at $a=0$.

<details>
<summary>💡 Hint</summary>

$\tan x$ is odd, so all even-degree coefficients vanish — the $x^2$ term is $0$.

</details>

**D8.** Write the binomial series for $\frac{1}{\sqrt{1+x}} = (1+x)^{-1/2}$ (first 3 terms).

**D9.** Multiply the series for $e^x$ and $e^{-x}$. What do you get?

**D10.** Use $\cos x$ series to estimate $\cos(0.2)$ to 4 decimal places.

<details>
<summary>💡 Hint</summary>

$\cos(0.2) = 1 - \frac{(0.2)^2}{2!} + \frac{(0.2)^4}{4!} - \cdots$ — alternating, so the next term bounds the error.

</details>

**D11.** Use the binomial series to write the first 3 nonzero terms of $(1+2x)^{1/3}$.

<details>
<summary>💡 Hint</summary>

Compute $\binom{1/3}{1}$, $\binom{1/3}{2}$, $\binom{1/3}{3}$ and plug $u=2x$ into $(1+u)^{1/3}$.

</details>

**D12.** Find the Taylor series for $f(x)=x^3-2x^2+3x-4$ at $a=1$ directly using the formula.

<details>
<summary>💡 Hint</summary>

$f$ is cubic, so $f^{(4)} = 0$ — the series stops after the $(x-1)^3$ term. Compute $f(1), f'(1), f''(1), f'''(1)$.

</details>

> Solutions: [Solutions](solutions/18C-solutions.md#basic-drill)

---

## Advanced Drills

**A1.** Find the Maclaurin series for $\sinh x = \frac{e^x-e^{-x}}{2}$.

<details>
<summary>💡 Hint</summary>

Subtract the series for $e^{-x}$ from $e^x$: even powers cancel, odd powers double.

</details>

**A2.** Prove $e^{i\theta} = \cos\theta + i\sin\theta$ using Maclaurin series.

<details>
<summary>💡 Hint</summary>

Plug $x = i\theta$ into $e^x = \sum \frac{x^n}{n!}$ and split the sum into even and odd $n$ (using $i^{2k} = (-1)^k$).

</details>

**A3.** Find the Taylor series for $f(x)=\frac{1}{x}$ about $a=2$.

<details>
<summary>💡 Hint</summary>

$\frac{1}{x} = \frac{1}{2+(x-2)} = \frac12\cdot\frac{1}{1+(x-2)/2}$ — geometric series.

</details>

**A4.** Evaluate $\lim_{x\to0}\frac{\tan x - x}{x^3}$ using series.

<details>
<summary>💡 Hint</summary>

$\tan x = x + \frac{x^3}{3} + \frac{2x^5}{15} + \cdots$.

</details>

**A5.** Compute $\int_0^1 \frac{\sin x}{x}dx$ to 4 decimal places using series.

<details>
<summary>💡 Hint</summary>

$\frac{\sin x}{x} = 1 - \frac{x^2}{3!} + \frac{x^4}{5!} - \cdots$; integrate to $\sum \frac{(-1)^n}{(2n+1)!(2n+1)}$ — alternating series.

</details>

**A6.** Find the Maclaurin series for $\arcsin x$.

<details>
<summary>💡 Hint</summary>

Same route as Practice 5: expand $(1-x^2)^{-1/2}$ binomially and integrate term-by-term.

</details>

**A7.** How many terms of $\sin x$ series are needed to estimate $\sin(1)$ with error $<10^{-6}$?

<details>
<summary>💡 Hint</summary>

At $x=1$ it's alternating: keeping up to $x^{2n+1}$ leaves error $\le \frac{1}{(2n+3)!}$. Find the smallest $2n+3$ with $(2n+3)! > 10^6$.

</details>

**A8.** Find the sum: $1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\cdots$. Recognize the series.

<details>
<summary>💡 Hint</summary>

Evaluate $\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots$ at $x=1$.

</details>

**A9.** Derive the Taylor series for $\frac{1}{(1-x)^2}$.

<details>
<summary>💡 Hint</summary>

$\frac{d}{dx}\frac{1}{1-x} = \frac{1}{(1-x)^2}$; differentiate $\sum x^n$ term by term and re-index.

</details>

**A10.** Use the Lagrange remainder to prove that $e$ is irrational.

<details>
<summary>💡 Hint</summary>

For $n \ge q$, $n!e$ and each $n!/k!$ are integers, so $n!R_n = n!e - \sum_{k=0}^n n!/k!$ is an integer. But $0 < n!R_n \le \frac{3}{n+1} < 1$ — contradiction.

</details>

**A11.** (🔗 13A, 18B) Use series to evaluate $\lim_{x\to 0}\frac{\sin x - x + x^3/6}{x^5}$. How many terms are needed?

<details>
<summary>💡 Hint</summary>

$\sin x = x - \frac{x^3}{6} + \frac{x^5}{120} - \frac{x^7}{5040} + \cdots$ — the first three terms cancel, leaving $\frac{x^5}{120}$.

</details>

**A12.** Find the Maclaurin series for $\ln(1+\sin x)$ up to $x^4$.

<details>
<summary>💡 Hint</summary>

Set $u = x - \frac{x^3}{6}$. You need $u^2, u^3, u^4$ only up to the $x^4$ power — e.g. $u^2 = x^2 - \frac{x^4}{3} + \cdots$.

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
| $|R_n| \leq \frac{M}{(n+1)!}|x-a|^{n+1}$ | "absolute remainder less than or equal to M over n+1 factorial times x minus a to the n+1" | error bound — M = max of |f^{(n+1)}| on the interval |

---

## Terminology

| What we call it | Math term | Notation |
|:---:|:---:|:---:|
| infinite polynomial matching derivatives | Taylor series | $\sum \frac{f^{(n)}(a)}{n!}(x-a)^n$ |
| Taylor series at 0 | Maclaurin series | $\sum \frac{f^{(n)}(0)}{n!}x^n$ |
| error of n-th degree approximation | Lagrange remainder | $R_n = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}$ |
| product 1·2·3·...·n | factorial | $n!$ |
| bounding the remainder | error estimation | $|R_n| \leq \frac{M}{(n+1)!}|x-a|^{n+1}$ |
