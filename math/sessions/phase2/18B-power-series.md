# Session 18B: Power Series — Where Does It Converge?

**Phase 2 — Classical Techniques | 60 min**

*Prerequisites: 18A (convergence tests), 14B (chain rule), 16A (FTC)*

> 💡 **Stuck?** Every problem has a collapsible **Hint** below it — click it only when you need a nudge.

---

## Example 1: What Is a Power Series?

$\displaystyle \sum_{n=0}^\infty c_n(x-a)^n = c_0 + c_1(x-a) + c_2(x-a)^2 + \cdots$

$a$ = center. The series is a **function of $x$**. Question: for which $x$ does it converge?

---

## Example 2: Radius of Convergence (🔗 18A)

Use the **Ratio Test** (or Root Test) from 18A on the terms:

$\displaystyle \lim_{n\to\infty}\left|\frac{c_{n+1}(x-a)^{n+1}}{c_n(x-a)^n}\right| = |x-a|\lim_{n\to\infty}\left|\frac{c_{n+1}}{c_n}\right| < 1$.

**Radius** $R = \displaystyle \lim_{n\to\infty}\left|\frac{c_n}{c_{n+1}}\right|$ (if the limit exists).

**Where this formula comes from:** name $L=\lim|c_{n+1}/c_n|$. The ratio line above says the series converges when $|x-a|\,L<1$, i.e. when $|x-a|<1/L$. The radius is nothing but the ratio test solved for $|x-a|$: $R=1/L$.

**Why convergence is symmetric about the center:** the test compares only the *distance* $|x-a|$ against one fixed number. The verdict is always "inside a disk of radius $R$ around $a$" — a power series can never converge in a lopsided or disconnected region. This is a theorem about power series, not a coincidence of the examples.

**Where $R$ usually comes from — the nearest bad point:** when the series represents a known function, the radius is (typically) the distance from $a$ to the **nearest singular point** of that function.

| Series | Closed form | Nearest bad point | $R$ |
|:---:|:---:|:---:|:---:|
| $\sum x^n$ | $\frac{1}{1-x}$ | $x=1$ (denominator 0) | $1$ |
| $\sum (-1)^n x^n$ | $\frac{1}{1+x}$ | $x=-1$ | $1$ |
| $\ln(1+x)$ series | $\ln(1+x)$ | $x=-1$ (log of 0) | $1$ |
| $\arctan x$ series | $\arctan x$ | $x=\pm i$ (complex!) | $1$ |

The last row deserves a second look: the arctangent series stops at $R=1$ even though the function is smooth on the entire real line — the bad points of $\frac{1}{1+x^2}$ are $x=\pm i$, at distance 1 from the center. The radius measures distance, not visibility.

$\sum_{n=0}^\infty \frac{x^n}{n!}$: $R = \lim \frac{1/n!}{1/(n+1)!} = \lim (n+1) = \infty$. **Converges for all $x$.** This is $e^x$!

$\sum_{n=0}^\infty n!\,x^n$: $R = \lim \frac{n!}{(n+1)!} = \lim \frac{1}{n+1} = 0$. **Converges only at $x=0$.**

$\sum_{n=0}^\infty x^n$: $R = 1$. Converges for $|x|<1$, diverges for $|x|>1$. At $x=\pm1$: check separately (both diverge).

**Connection to geometric series** (🔗 12B1): This is the geometric series $\sum r^n$ with $r=x$. The radius $R=1$ comes directly from the geometric condition $|r|<1$.

**Root Test alternative:** when the coefficients are themselves powers, the Root Test is often shorter — the series converges when $\limsup \left|c_n(x-a)^n\right|^{1/n} = |x-a|\,\limsup|c_n|^{1/n} < 1$, giving $R = 1/\limsup|c_n|^{1/n}$. It shines exactly where the Ratio Test stalls (see Drill D16 and Advanced A7).

![Radius and interval of convergence](graphs/0721/18B/18b-radius-convergence.png)

*Graph 18B-1: Top-left — Three cases of radius of convergence. Top-right — Partial sums $S_N(x)$ of $\sum x^n$ converging to $1/(1-x)$ on $(-1,1)$. Bottom-left — Endpoint behavior of $\sum x^n/n$. Bottom-right — Interval of convergence reference.*

---

## Example 3: Interval of Convergence — Check the Endpoints

For $\sum \frac{x^n}{n}$: $R=1$. At $x=1$: $\sum 1/n$ diverges. At $x=-1$: $\sum (-1)^n/n$ converges (alternating).
**Interval**: $[-1, 1)$.

For $\sum \frac{x^n}{n^2}$: $R=1$. At $x=\pm1$: $\sum 1/n^2$ converges.
**Interval**: $[-1, 1]$.

---

## Example 4: Differentiation and Integration Term-by-Term (🔗 14A, 16A)

Within the radius of convergence, you can differentiate and integrate a power series **term by term** (🔗 14A for differentiation rules, 16A for FTC):

$\frac{d}{dx}\sum c_n(x-a)^n = \sum n c_n(x-a)^{n-1}$.
$\int \sum c_n(x-a)^n dx = C + \sum \frac{c_n}{n+1}(x-a)^{n+1}$.

**The radius of convergence stays the same**, but **the endpoints may change**.

**Why term-by-term is allowed:** inside the radius the series converges **absolutely** (18A), and absolutely convergent series can be differentiated and integrated term by term without changing the sum. The radius of the derived series also cannot grow, because differentiating or integrating the closed form does not move its singular points.

**Endpoints really do move — concrete example:** $\sum x^n/n^2$ has interval $[-1,1]$, but its derivative $\sum x^{n-1}/n$ diverges at $x=1$ (harmonic series) — differentiation **lost** the right endpoint. Integration can gain endpoints. This is why endpoints must be re-checked after every term-by-term operation (Mistake 3).

---

![Building series from geometric](graphs/0721/18B/18b-building-series.png)

*Graph 18B-2: Three key series built from $1/(1-x)$. Left — $1/(1+x)$ by substituting $x\to -x$. Middle — $\ln(1+x)$ by integrating $1/(1+x)$. Right — $\arctan x$ by integrating $1/(1+x^2)$. All converge on $(-1,1)$ and partial sums approach the true function.*

## Example 5: Building New Series from $\frac{1}{1-x}$ (🔗 12B1, 12C1)

The geometric series $\sum x^n$ from 12B1 is the foundation. By substituting, differentiating, and integrating, we build many series — similar to how 12C1 builds transformations from basic matrices.

$\frac{1}{1-x} = \sum_{n=0}^\infty x^n$, $|x|<1$.

Replace $x$ with $-x$: $\frac{1}{1+x} = \sum (-1)^n x^n$.
Replace $x$ with $x^2$: $\frac{1}{1-x^2} = \sum x^{2n}$.
Integrate: $\int \frac{1}{1-x}dx = -\ln(1-x) = \sum \frac{x^{n+1}}{n+1}$. So $\ln(1+x) = \sum_{n=1}^\infty \frac{(-1)^{n+1}x^n}{n}$.
Integrate $\frac{1}{1+x^2}$: $\arctan x = \sum_{n=0}^\infty \frac{(-1)^n x^{2n+1}}{2n+1}$.

---

## Common Mistakes

### Mistake 1: Forgetting to check the endpoints

**Wrong**: "$R=1$, so the interval is $(-1,1)$." The radius only guarantees convergence on $(a-R, a+R)$. The endpoints must be **checked separately** — e.g. $\sum x^n/n$ has interval $[-1,1)$, not $(-1,1)$.

### Mistake 2: Confusing the ratio with the radius

If the ratio test gives $\lim |c_{n+1}/c_n| = L$, the radius is $R = 1/L$, **not** $L$. ($L=0 \Rightarrow R=\infty$; $L=\infty \Rightarrow R=0$.)

### Mistake 3: Differentiating or integrating outside the radius

Term-by-term operations are only valid **inside** the radius of convergence. Differentiating can also change which endpoints converge (e.g. $\sum x^n/n^2$ vs its derivative $\sum x^{n-1}/n$).

### Mistake 4: Treating the power series as a finite polynomial

You cannot plug in $x$ values outside the radius, and you cannot truncate arbitrarily without an error bound. A power series is a function only where it converges.

---

## What We Just Did

```
(1) Power series: Σc_n(x-a)^n. Center a. Radius R from Ratio/Root test.
(2) Interval of convergence: (-R,R) guaranteed. Check endpoints separately.
(3) Term-by-term differentiation/integration preserves R.
(4) Build new series from geometric: substitute, differentiate, integrate.
```

---

## Practice 1

Find radius and interval for $\sum_{n=1}^\infty \frac{(x-2)^n}{3^n n}$.

<details>
<summary>💡 Hint</summary>

The center is $x=2$. Run the ratio test on the coefficients — the limit tells you the radius. Then exactly two boundary points remain undecided: test each one with the tools from 18A.

</details>

→ Solutions: [Solutions](solutions/18B-solutions.md#practice-1)

---

## Practice 2

Find a power series for $\ln(1-x^2)$.

<details>
<summary>💡 Hint</summary>

Start from the geometric series (Example 5): write $\ln(1-x^2) = \ln(1+u)$ with $u = -x^2$, then substitute into the series for $\ln(1+u)$.

</details>

→ Solutions: [Solutions](solutions/18B-solutions.md#practice-2)

---

## Practice 3

Differentiate $\sum_{n=0}^\infty \frac{x^n}{n!}$ term-by-term. What do you notice?

<details>
<summary>💡 Hint</summary>

$\frac{d}{dx}\frac{x^n}{n!} = \frac{x^{n-1}}{(n-1)!}$. Re-index with $k = n-1$ and compare with the original.

</details>

→ Solutions: [Solutions](solutions/18B-solutions.md#practice-3)

---

## Practice 4: Real Battle (🔗 18A)

Find the interval of convergence for $\displaystyle \sum_{n=1}^\infty \frac{(2x+1)^n}{\sqrt{n}}$. Check both endpoints.

<details>
<summary>💡 Hint</summary>

Read the center first — it is hidden: rewrite $(2x+1)^n = 2^n\left(x+\frac12\right)^n$ so the series is visibly centered. Then the ratio test gives the radius, and two boundary points remain — at one of them you meet a $p$-series, at the other an alternating series.

</details>

→ Solutions: [Solutions](solutions/18B-solutions.md#practice-4)

---

## Practice 5: Real Battle — Series for $\pi$ (🔗 18C)

Find a series for $\pi$. How many terms are needed to estimate $\pi$ to 3 decimal places?

<details>
<summary>💡 Hint</summary>

One value of $x$ turns the arctangent series into something very simple — and $4\arctan(\cdot)$ is $\pi$. The series is alternating, so the first omitted term controls the error: decide what tolerance "3 decimal places" demands, then see how many terms that forces.

</details>

→ Solutions: [Solutions](solutions/18B-solutions.md#practice-5)

---

## Basic Drills

**D1.** Find $R$ for $\sum_{n=0}^\infty \frac{x^n}{2^n}$.

**D2.** Find $R$ for $\sum_{n=1}^\infty \frac{n x^n}{3^n}$.

**D3.** Find interval for $\sum_{n=0}^\infty \frac{(-1)^n x^n}{n+1}$.

<details>
<summary>💡 Hint</summary>

The radius is $1$. At one endpoint the terms alternate; at the other they behave like a $p$-series. Classify each with the 18A tests.

</details>

**D4.** Write $\frac{1}{1+2x}$ as a power series. For which $x$?

**D5.** Find a series for $\frac{1}{(1-x)^2}$.

<details>
<summary>💡 Hint</summary>

$\frac{d}{dx}\left(\frac{1}{1-x}\right) = \frac{1}{(1-x)^2}$ — differentiate the geometric series term-by-term.

</details>

**D6.** Find a series for $\ln(1-x)$.

<details>
<summary>💡 Hint</summary>

$\int\frac{dx}{1-x} = -\ln(1-x)$ — integrate the geometric series $\frac{1}{1-x}=\sum x^n$ term-by-term, keeping the minus sign.

</details>

**D7.** Evaluate $\sum_{n=1}^\infty \frac{n}{2^n}$.

<details>
<summary>💡 Hint</summary>

The factor $n$ is the fingerprint of a differentiated power. Differentiate the geometric series once and look for the matching $x$.

</details>

**D8.** Find interval for $\sum_{n=1}^\infty \frac{(x+1)^n}{n^2}$.

**D9.** Differentiate the series for $\sin x = \sum (-1)^n \frac{x^{2n+1}}{(2n+1)!}$.

**D10.** Find $R$ for $\sum_{n=0}^\infty \frac{(2n)!}{(n!)^2}x^n$.

<details>
<summary>💡 Hint</summary>

The ratio of consecutive coefficients collapses to a ratio of quadratics — take its limit, and remember the radius is the reciprocal of that limit.

</details>

**D11.** Find a power series for $\frac{x}{(1-x)^2}$.

<details>
<summary>💡 Hint</summary>

Write $\frac{x}{(1-x)^2} = x\cdot\frac{1}{(1-x)^2}$ and multiply the series from D5 by $x$.

</details>

**D12.** Evaluate $\sum_{n=0}^\infty \frac{(-1)^n}{2^n}$.

<details>
<summary>💡 Hint</summary>

$\sum \left(-\frac12\right)^n$ with $r = -\frac12$. Sum $= \frac{1}{1-r}$.

</details>

**D13.** Evaluate $1 - \frac12 + \frac13 - \frac14 + \cdots$ — and justify that the endpoint you used is actually allowed.

<details>
<summary>💡 Hint</summary>

This is a series you already know, evaluated at one specific $x$. Before trusting the value, confirm that the interval of convergence includes that $x$.

</details>

**D14.** Write $\sum_{n=1}^\infty n x^{n-1}$ starting from $n=0$, and use the result to evaluate $\sum_{n=1}^\infty \frac{n}{2^{n-1}}$.

<details>
<summary>💡 Hint</summary>

Shift the index ($k=n-1$), then recognize the new series as a derivative of the geometric series. Choose the $x$ that matches $2^{n-1}$.

</details>

**D15.** Evaluate $\sum_{n=1}^\infty \frac{n^2}{2^n}$.

<details>
<summary>💡 Hint</summary>

Write $n^2 = n(n-1) + n$: the $n(n-1)$ piece comes from differentiating the geometric series **twice**, the $n$ piece from differentiating **once**. Then evaluate at the $x$ that matches $2^n$.

</details>

**D16.** Find $R$ for $\sum_{n=0}^\infty \left(\frac{x}{2}\right)^{n^2}$.

<details>
<summary>💡 Hint</summary>

The coefficients are $c_k = 2^{-k}$ when $k$ is a perfect square and $0$ otherwise — the ratio test cannot even start. The root test can: consider $\sqrt[k]{|c_k x^k|}$.

</details>

> Solutions: [Solutions](solutions/18B-solutions.md#basic-drill)

---

## Advanced Drills

**A1.** Find the interval for $\sum_{n=1}^\infty \frac{n(x+3)^n}{4^n}$.

<details>
<summary>💡 Hint</summary>

$R = 4$, center $-3$. At both endpoints the general term does NOT tend to $0$ — both diverge.

</details>

**A2.** Find a power series for $\frac{x}{1+x-2x^2}$.

<details>
<summary>💡 Hint</summary>

$1+x-2x^2 = (1-x)(1+2x)$. Split into partial fractions $\frac{A}{1-x} + \frac{B}{1+2x}$, then use the geometric series for each.

</details>

**A3.** Evaluate $\lim_{x\to0}\frac{e^x-1-x}{x^2}$.

<details>
<summary>💡 Hint</summary>

$e^x = 1 + x + \frac{x^2}{2} + \cdots$ — the numerator's lowest power of $x$ decides the limit.

</details>

**A4.** Prove $\sum_{n=1}^\infty \frac{n}{3^n} = \frac{3}{4}$.

<details>
<summary>💡 Hint</summary>

Differentiate $\sum x^n = \frac{1}{1-x}$ to get $\sum n x^{n-1}$, then set $x = \frac13$.

</details>

**A5.** Find the interval for $\sum_{n=1}^\infty \frac{(x-1)^n}{n\cdot5^n}$.

<details>
<summary>💡 Hint</summary>

$R=5$, center $1$: endpoints $x=6$ (harmonic) and $x=-4$ (alternating).

</details>

**A6.** Express $\int_0^{1/2} \frac{dx}{1+x^4}$ as a series. Compute to 4 decimal places.

<details>
<summary>💡 Hint</summary>

$\frac{1}{1+x^4} = 1 - x^4 + x^8 - \cdots$ is geometric with ratio $-x^4$. Integrate term-by-term — the result is an alternating series, so the first omitted term bounds the error.

</details>

**A7.** Find all $x$ for which $\sum_{n=0}^\infty \frac{n!\,(x-2)^n}{n^n}$ converges.

<details>
<summary>💡 Hint</summary>

The ratio limit is $\lim \left(\frac{n}{n+1}\right)^n |x-2| = \frac{|x-2|}{e}$ — the radius is $e$. Stirling gives the same answer via the root test.

</details>

**A8.** A power series satisfies $f'(x)=f(x)$ with $f(0)=1$. Find the series and identify $f$.

<details>
<summary>💡 Hint</summary>

Write $f = \sum c_n x^n$ and equate coefficients of $f'$ and $f$: $(n+1)c_{n+1} = c_n$.

</details>

**A9.** Find the radius for $\sum_{n=0}^\infty \binom{2n}{n}x^n$.

<details>
<summary>💡 Hint</summary>

$\frac{c_{n+1}}{c_n} = \frac{\binom{2n+2}{n+1}}{\binom{2n}{n}} = \frac{(2n+2)(2n+1)}{(n+1)^2} \to 4$.

</details>

**A10.** Multiply the series for $e^x$ by itself. Show the result is the series for $e^{2x}$.

<details>
<summary>💡 Hint</summary>

The $x^n$ coefficient is $\sum_{k=0}^n \frac{1}{k!(n-k)!}$. Factor out $\frac{1}{n!}$ — the rest is $\sum \binom{n}{k} = 2^n$.

</details>

**A11.** (🔗 18A) Find the radius and interval of convergence for $\sum_{n=1}^\infty \frac{(3x-1)^n}{n\cdot 2^n}$.

<details>
<summary>💡 Hint</summary>

After rewriting, $R = \lim \frac{c_n}{c_{n+1}} = \frac23$ with center $\frac13$. Endpoints: $x=1$ (harmonic) and $x=-\frac13$ (alternating).

</details>

**A12.** Find a power series for $\ln\left(\frac{1+x}{1-x}\right)$. What is its interval of convergence?

<details>
<summary>💡 Hint</summary>

Add $\sum \frac{(-1)^{n+1}x^n}{n}$ and $\sum \frac{x^n}{n}$: odd powers double, even powers cancel. The interval is where BOTH series converge — check the endpoints.

</details>

> Solutions: [Solutions](solutions/18B-solutions.md#advanced-drill)

---

## How to Read These Symbols

| Symbol | Reads as | Meaning |
|:---:|:---:|------|
| $\sum_{n=0}^{\infty} c_n (x-a)^n$ | "power series centered at a" | infinite polynomial — function represented as series around a |
| center | "center" / "a" | point around which the power series is expanded |
| radius of convergence $R$ | "radius of convergence" | series converges for |x-a|<R, diverges for |x-a|>R |
| interval of convergence | "interval of convergence" | (a-R, a+R) — endpoints must be checked separately |
| Ratio Test for $R$ | "ratio test for radius" | R = lim |c_n/c_{n+1}| if the limit exists |
| term-by-term differentiation | "term-by-term differentiation" | derivative of power series = sum of derivatives — valid inside radius |
| term-by-term integration | "term-by-term integration" | integral of power series = sum of integrals — valid inside radius |
| $e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}$ | "e to the x equals sum of x to the n over n factorial" | Maclaurin series for exponential — converges for all x |
| analytic function | "analytic function" | function that equals its power series in some interval |
| singular point | "singular point" | where function is not analytic — determines radius of convergence |

---

## Terminology

| What we call it | Math term | Notation |
|:---:|:---:|:---:|
| infinite polynomial around a | power series | $\sum c_n(x-a)^n$ |
| distance to nearest singularity | radius of convergence | $R$ |
| domain of convergence | interval of convergence | $(a-R, a+R)$ plus checked endpoints |
| differentiate/integrate term-by-term | termwise operations | valid for |x-a|<R |
| equals its power series | analytic function | locally represented by series |
