# Session 18B: Power Series — Where Does It Converge?

**Phase 2 — Classical Techniques | 60 min**

*Prerequisites: 18A (convergence tests), 14B (chain rule), 16A (FTC)*

> 💡 **Stuck?** Every problem has a collapsible **Hint** below it — click it only when you need a nudge.

> **Source.** Every example and drill below is taken from Stewart, *Calculus*, Chapter 11 (Sections 11.8–11.9). Each item cites its section and exercise number.

---

## Example 1: What Is a Power Series? (§11.8)

$$\sum_{n=0}^\infty c_n(x-a)^n = c_0 + c_1(x-a) + c_2(x-a)^2 + \cdots$$

$a$ is the **center**. The series is a **function of $x$**. The question: for which $x$ does it converge?

---

## Example 2: Radius of Convergence (§11.8 Ex 1–3, 🔗 18A)

Use the **Ratio Test** (or Root Test) from 18A on the terms:

$$\lim_{n\to\infty}\left|\frac{c_{n+1}(x-a)^{n+1}}{c_n(x-a)^n}\right| = |x-a|\lim_{n\to\infty}\left|\frac{c_{n+1}}{c_n}\right| < 1.$$

**Radius**: $$R = \lim_{n\to\infty}\left|\frac{c_n}{c_{n+1}}\right| \quad \text{(if the limit exists).}$$

**Where this formula comes from:** name $L=\lim|c_{n+1}/c_n|$. The ratio line says the series converges when $|x-a|\,L<1$, that is when $|x-a|<1/L$. So $R=1/L$ is just the Ratio Test solved for $|x-a|$.

**Why convergence is symmetric about the center:** the test compares only the *distance* $|x-a|$ against one fixed number, so the verdict is always "inside a disk of radius $R$ around $a$". A power series can never converge in a lopsided region.

**Where $R$ usually comes from — the nearest bad point:** the radius is (typically) the distance from $a$ to the nearest **singular point** of the closed form.

| Series | Closed form | Nearest bad point | $R$ |
|:---:|:---:|:---:|:---:|
| $\sum x^n$ | $\frac{1}{1-x}$ | $x=1$ (denominator 0) | $1$ |
| $\sum (-1)^n x^n$ | $\frac{1}{1+x}$ | $x=-1$ | $1$ |
| $\ln(1+x)$ series | $\ln(1+x)$ | $x=-1$ (log of 0) | $1$ |
| $\arctan x$ series | $\arctan x$ | $x=\pm i$ (complex!) | $1$ |

The last row: the arctangent series stops at $R=1$ even though the function is smooth on the whole real line — the bad points of $\frac{1}{1+x^2}$ are $x=\pm i$, at distance 1 from the center. The radius measures distance, not visibility.

$\sum_{n=1}^\infty \frac{(x-3)^n}{n}$: $R=\lim\frac{n+1}{n}=1$. (Intervals in Example 3.)

$\sum_{n=0}^\infty n!\,x^n$: $R=\lim\frac{n!}{(n+1)!}=\lim\frac{1}{n+1}=0$. **Converges only at $x=0$.**

$\sum_{n=0}^\infty \frac{x^n}{(2n)!}$: $R=\lim\frac{(2n)!}{(2n+2)!}=\lim\frac{1}{(2n+2)(2n+1)}=0 \Rightarrow R=\infty$. **Converges for all $x$.**

**Root Test alternative:** when the coefficients are themselves powers, the Root Test is shorter: $R = 1/\limsup |c_n|^{1/n}$. It shines exactly where the Ratio Test stalls.

![Radius and interval of convergence]({{graph:18b-radius-convergence}})

*Graph 18B-1: Top-left — Three cases of radius of convergence. Top-right — Partial sums $S_N(x)$ of $\sum x^n$ converging to $1/(1-x)$ on $(-1,1)$. Bottom-left — Endpoint behavior of $\sum x^n/n$. Bottom-right — Interval of convergence reference.*

---

## Example 3: Interval of Convergence — Check the Endpoints (§11.8 Ex 4, Ex 5)

$\sum_{n=0}^\infty \frac{(-3)^n x^n}{\sqrt{n+1}}$: the ratio gives $3|x|<1$, so $R=\frac13$. At $x=\frac13$: $\sum\frac{(-1)^n}{\sqrt{n+1}}$ converges (alternating). At $x=-\frac13$: $\sum\frac{1}{\sqrt{n+1}}$ diverges ($p=\frac12$). **Interval**: $\left(-\frac13,\frac13\right]$.

$\sum_{n=0}^\infty \frac{n(x+2)^n}{3^{n+1}}$: the ratio gives $\frac{|x+2|}{3}<1$, so $R=3$ and $-5<x<1$. At $x=1$: $\frac13\sum n$ diverges; at $x=-5$: $\frac13\sum(-1)^n n$ diverges. **Interval**: $(-5,1)$.

---

## Example 4: Differentiation and Integration Term-by-Term (§11.9 Ex 4, 🔗 14A, 16A)

Inside the radius you may differentiate and integrate a power series term by term:

$$\frac{d}{dx}\sum c_n(x-a)^n = \sum n c_n(x-a)^{n-1}, \qquad \int \sum c_n(x-a)^n\,dx = C + \sum \frac{c_n}{n+1}(x-a)^{n+1}.$$

**The radius stays the same**, but **the endpoints may change**.

Starting from $\frac{1}{1-x}=\sum x^n$ and differentiating:
$$\frac{1}{(1-x)^2}=1+2x+3x^2+\cdots=\sum_{n=1}^\infty n x^{n-1}=\sum_{n=0}^\infty (n+1)x^n, \qquad R=1.$$

**Why term-by-term is allowed:** inside the radius the series converges **absolutely** (18A), and absolutely convergent series can be differentiated and integrated term by term without changing the sum. The radius cannot grow, because differentiating the closed form does not move its singular points.

**Endpoints really do move:** $\sum x^n/n^2$ has interval $[-1,1]$, but its derivative $\sum x^{n-1}/n$ diverges at $x=1$ — differentiation **lost** the right endpoint. Integration can gain endpoints. Re-check endpoints after every term-by-term operation.

---

## Example 5: Building New Series from $\frac{1}{1-x}$ (§11.9 Ex 1, Ex 2, Ex 5, Ex 6, 🔗 12B1)

The geometric series $\sum x^n$ is the foundation. Substitute, differentiate, integrate.

$\frac{1}{1-x} = \sum_{n=0}^\infty x^n$, $|x|<1$.

Replace $x$ with $-x^2$: $\frac{1}{1+x^2} = \sum_{n=0}^\infty (-1)^n x^{2n}$.

Factor a 2: $\frac{1}{x+2} = \frac12\cdot\frac{1}{1+\frac{x}{2}} = \sum_{n=0}^\infty \frac{(-1)^n x^n}{2^{n+1}}$.

Integrate $\frac{1}{1+x}$: $\ln(1+x) = \sum_{n=1}^\infty \frac{(-1)^{n-1}x^n}{n}$.

Integrate $\frac{1}{1+x^2}$: $\arctan x = \sum_{n=0}^\infty \frac{(-1)^n x^{2n+1}}{2n+1}$.

![Building series from geometric]({{graph:18b-building-series}})

*Graph 18B-2: Three key series built from $1/(1-x)$. Left — $1/(1+x)$ by substituting $x\to -x$. Middle — $\ln(1+x)$ by integrating $1/(1+x)$. Right — $\arctan x$ by integrating $1/(1+x^2)$. All converge on $(-1,1)$ and partial sums approach the true function.*

---

## Example 6: Functions Defined by Power Series (§11.9 Ex 8)

Some functions are *defined* by a series. The Bessel function of order 0:

$$J_0(x)=\sum_{n=0}^\infty \frac{(-1)^n x^{2n}}{2^{2n}(n!)^2}.$$

Ratio: $\left|\frac{a_{n+1}}{a_n}\right|=\frac{x^2}{4(n+1)^2}\to0$ for every $x$, so the **domain is all of $\mathbb{R}$**.

Differentiate term by term: $J_0'(x)=\sum_{n=1}^\infty \frac{(-1)^n 2n\,x^{2n-1}}{2^{2n}(n!)^2}$.

---

## Common Mistakes

### Mistake 1: Forgetting to check the endpoints

**Wrong**: "$R=1$, so the interval is $(-1,1)$." The radius only guarantees convergence on $(a-R,a+R)$. The endpoints must be **checked separately** — e.g. $\sum x^n/n$ has interval $[-1,1)$.

### Mistake 2: Confusing the ratio with the radius

If the ratio test gives $\lim |c_{n+1}/c_n| = L$, the radius is $R = 1/L$, **not** $L$. ($L=0 \Rightarrow R=\infty$; $L=\infty \Rightarrow R=0$.)

### Mistake 3: Differentiating or integrating outside the radius

Term-by-term operations are only valid **inside** the radius. Differentiating can also change which endpoints converge.

### Mistake 4: Treating the power series as a finite polynomial

You cannot plug in $x$ values outside the radius, and you cannot truncate arbitrarily without an error bound.

---

## What We Just Did

```
(1) Power series: Σc_n(x-a)^n. Center a. Radius R from Ratio/Root test.
(2) Interval of convergence: (a-R, a+R) guaranteed. Check endpoints separately.
(3) Term-by-term differentiation/integration preserves R.
(4) R is the distance from a to the nearest bad point of the closed form.
(5) Build new series from geometric: substitute, factor, differentiate, integrate.
```

---

## Basic Drills

**D1.** (§11.8 #3) Radius and interval of $\sum_{n=1}^\infty \frac{x^n}{n}$.

**D2.** (§11.8 #7) Radius and interval of $\sum_{n=1}^\infty \frac{n}{5^n}x^n$.

**D3.** (§11.8 #12) Radius and interval of $\sum_{n=1}^\infty \frac{(-1)^n x^n}{n^2}$.

<details>
<summary>💡 Hint</summary>

$R=1$. At $x=\pm1$ the terms are $\pm 1/n^2$ — a convergent $p$-series.

</details>

**D4.** (§11.8 #13) Radius of $\sum_{n=0}^\infty \frac{x^n}{n!}$.

**D5.** (§11.8 #21) Radius and interval of $\sum_{n=0}^\infty \frac{(x-2)^n}{n^2+1}$.

<details>
<summary>💡 Hint</summary>

$R=1$. At both endpoints the terms behave like $1/n^2$ or $(-1)^n/n^2$.

</details>

**D6.** (§11.8 #4) Radius and interval of $\sum_{n=1}^\infty (-1)^n n x^n$.

**D7.** (§11.9 #3) A power series for $\frac{1}{1+x}$.

**D8.** (§11.9 #5) A power series for $\frac{1}{1-x^2}$.

**D9.** (§11.9 #7) A power series for $\frac{2}{3-x}$.

**D10.** (§11.9 #15a) A power series for $\frac{1}{(1+x)^2}$.

<details>
<summary>💡 Hint</summary>

Start from $\frac{1}{1+x}=\sum(-1)^n x^n$ and differentiate.

</details>

**D11.** (§11.9 #16a) A power series for $\ln(1-x)$.

**D12.** (§11.9 #46b) Evaluate $\sum_{n=1}^\infty \frac{n}{2^n}$.

**D13.** (§11.9 #27) $\int \frac{t}{1-t^8}\,dt$ as a power series.

**D14.** (§11.8 #16) Radius of $\sum_{n=1}^\infty 2^n n^2 x^n$.

**D15.** (§11.8 #31) Radius of $\sum_{n=1}^\infty n!(2x-1)^n$.

<details>
<summary>💡 Hint</summary>

Write it as $\sum c_n (x-\tfrac12)^n$ first. What is $\lim c_n/c_{n+1}$?

</details>

**D16.** (§11.8 #25) Radius of $\sum_{n=1}^\infty \frac{(x-2)^n}{n^n}$.

<details>
<summary>💡 Hint</summary>

$\frac{c_n}{c_{n+1}}=\frac{(n+1)^{n+1}}{n^n}=(n+1)\left(1+\frac1n\right)^n$.

</details>

> Solutions: [Solutions](solutions/18B-solutions.md#basic-drill)

---

## Advanced Drills

**A1.** (§11.8 #23) Radius and interval of $\sum_{n=2}^\infty \frac{(x+2)^n}{2^n \ln n}$.

<details>
<summary>💡 Hint</summary>

Center $-2$, $R=2$, so $(-4,0)$. At $x=0$ the terms are $1/\ln n$; at $x=-4$ they alternate.

</details>

**A2.** (§11.9 #13) Partial fractions first: a power series for $\frac{2x-4}{x^2-4x+3}$.

<details>
<summary>💡 Hint</summary>

$x^2-4x+3=(x-1)(x-3)$ and $\frac{2x-4}{(x-1)(x-3)}=\frac{1}{x-1}+\frac{1}{x-3}$.

</details>

**A3.** (§11.9 #22) A power series for $x^2\arctan(x^3)$.

<details>
<summary>💡 Hint</summary>

Use $\arctan u=\sum(-1)^n u^{2n+1}/(2n+1)$ with $u=x^3$, then multiply by $x^2$.

</details>

**A4.** (§11.9 #46a) Show $\sum_{n=1}^\infty n x^{n-1}=\frac{1}{(1-x)^2}$ and use it to prove $\sum_{n=1}^\infty \frac{n}{2^n}=2$.

**A5.** (§11.8 #26) Radius and interval of $\sum_{n=1}^\infty \frac{(2x-1)^n}{5^n\sqrt n}$.

<details>
<summary>💡 Hint</summary>

$R=\frac52$ about $x=\frac12$; endpoints $x=\frac74$ (diverges) and $x=-\frac34$ (alternating).

</details>

**A6.** (§11.9 #34) Use a series to compute $\int_0^{0.3} \frac{x^2}{1+x^4}\,dx$ to six decimals.

<details>
<summary>💡 Hint</summary>

$\frac{x^2}{1+x^4}=\sum(-1)^n x^{4n+2}$; an alternating series gives the error bound.

</details>

**A7.** (§11.8 #39) Find the radius for $\sum_{n=0}^\infty \frac{(n!)^k}{(kn)!}x^n$, $k$ a positive integer.

<details>
<summary>💡 Hint</summary>

$\frac{c_n}{c_{n+1}}=\frac{(n+1)^k}{(kn+k)(kn+k-1)\cdots(kn+1)}\to\frac{1}{k^k}$.

</details>

**A8.** (§11.9 #37) Show $f(x)=\sum \frac{x^n}{n!}$ satisfies $f'=f$ and identify $f$.

**A9.** (§11.8 #43) For $f(x)=1+2x+x^2+2x^3+\cdots$ (coefficients $c_{2n}=1$, $c_{2n+1}=2$), find the interval and a formula.

<details>
<summary>💡 Hint</summary>

$f(x)=\sum x^{2n}+2\sum x^{2n+1}=1/(1-x^2)+2x/(1-x^2)$.

</details>

**A10.** (§11.9 #25) A power series for $\ln\left(\frac{1+x}{1-x}\right)$ and its interval.

**A11.** (§11.9 #16c) Put $x=\frac12$ in the series for $\ln(1-x)$ to express $\ln 2$ as a series.

**A12.** (§11.8 #46) If $\sum c_n x^n$ has radius $R$, what is the radius of $\sum c_n x^{2n}$?

<details>
<summary>💡 Hint</summary>

The variable is now $u=x^2$. Convergence needs $|u|<R$, i.e. $x^2<R$.

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
