# Session 18A: Infinite Series — Does It Converge?

**Phase 2 — Classical Techniques | 70 min**

*Prerequisites: 12B (sequences), 13C (limits of sequences), 17B (improper integrals)*

> 💡 **Stuck?** Every problem has a collapsible **Hint** below it — click it only when you need a nudge.

> **Source.** Every example and drill below is taken from Stewart, *Calculus*, Chapter 11 (Sections 11.2–11.7). Each item cites its section and exercise number.

---

## Part A: What Is a Series?

---

## Example 1: From Partial Sums to a Series (§11.2 Ex 1)

A **series** $\sum_{n=1}^\infty a_n$ is the limit of its **partial sums** $S_N = \sum_{n=1}^N a_n$.

Suppose we only know that the sum of the first $n$ terms is
$$S_n = \frac{2n}{3n+5}.$$
Then the sum of the series is the limit of these partial sums:
$$\sum_{n=1}^\infty a_n = \lim_{n\to\infty} S_n = \lim_{n\to\infty}\frac{2n}{3n+5} = \frac{2}{3}.$$

If $\lim_{N\to\infty} S_N = S$ (finite), the series **converges** to $S$. Otherwise it **diverges**.

**Divergence Test** (§11.2 Ex 9, 🔗 13C): if $\lim_{n\to\infty} a_n \neq 0$, the series diverges.
$$\sum_{n=1}^\infty \frac{n^2}{5n^2+4}: \quad \lim_{n\to\infty}\frac{n^2}{5n^2+4} = \frac15 \neq 0 \;\Rightarrow\; \text{diverges.}$$
A limit of $0$ proves nothing — the harmonic series has $a_n\to 0$ and still diverges.

---

## Part B: The Two Series You Must Memorize

---

## Example 2: Geometric Series (§11.2 Ex 3, Ex 4)

$$\sum_{n=1}^\infty ar^{n-1} = \frac{a}{1-r} \quad \text{if and only if } |r|<1. \qquad \text{Diverges if } |r|\ge 1.$$

$5-\frac{10}{3}+\frac{20}{9}-\frac{40}{27}+\cdots$: $a=5$, $r=-\frac23$, so $\frac{5}{1-(-2/3)}=3$.

$\sum_{n=1}^\infty 2^{2n}3^{1-n}=\sum_{n=1}^\infty 3\left(\frac43\right)^n$: $r=\frac43\ge1$ → diverges.

![Geometric series — convergence vs divergence]({{graph:18a-1-geometric-series}})

*Graph 18A-1: Left — Convergent geometric series $\sum (0.5)^n$: terms shrink, partial sums approach $S_\infty=2$. Right — Divergent geometric series $\sum (1.2)^n$: terms grow, partial sums diverge to infinity.*

---

## Example 3: Telescoping Series (§11.2 Ex 2, Ex 10)

When terms cancel in pairs, only the first and last survive.

$$\sum_{n=1}^\infty \frac{1}{n(n+1)} = \sum_{n=1}^\infty\left(\frac1n-\frac1{n+1}\right), \qquad S_N = 1-\frac{1}{N+1} \to 1.$$

$$\sum_{n=1}^\infty\left(\frac{3}{n(n+1)}+\frac{1}{2^n}\right) = 3\sum\frac{1}{n(n+1)}+\sum\frac{1}{2^n} = 3\cdot1+1 = 4.$$

---

## Example 4: $p$-Series and the Integral Test (§11.3 Ex 1, Ex 2, Ex 4)

$$\sum_{n=1}^\infty \frac{1}{n^p} \text{ converges} \iff p>1.$$

**Integral Test**: if $f$ is positive, continuous, decreasing on $[1,\infty)$ and $f(n)=a_n$, then $\sum f(n)$ and $\int_1^\infty f(x)\,dx$ converge or diverge together.

$\sum\frac{1}{n^2+1}$: $\int_1^\infty\frac{dx}{x^2+1}=\frac{\pi}{4}$ converges → series converges.

$\sum\frac{\ln n}{n}$: $f(x)=\frac{\ln x}{x}$ decreases for $x>e$, and $\int_1^\infty\frac{\ln x}{x}\,dx$ diverges → diverges.

![p-series and integral test]({{graph:18a-2-p-series}})

*Graph 18A-2: Left — Partial sums of $\sum 1/n^p$ for $p=2$ (converges), $p=1$ (diverges), $p=1/2$ (diverges). Right — Integral test: $\sum 1/n^2$ converges because $\int_1^\infty 1/x^2\,dx$ converges.*

---

## Part C: Convergence Tests — The Workflow

> **Decision order** (§11.7): Divergence Test → Geometric? → Telescoping? → $p$-series? → Integral Test → Comparison → Limit Comparison → Ratio → Root → Alternating.

---

## Example 5: Comparison Test (§11.4 Ex 1, Ex 2)

Given $0\le a_n\le b_n$: if $\sum b_n$ converges then $\sum a_n$ converges; if $\sum a_n$ diverges then $\sum b_n$ diverges.

$\sum\frac{5}{2n^2+4n+3}$: $\frac{5}{2n^2+4n+3}\le\frac{5}{2n^2}$ and $\sum\frac{1}{n^2}$ converges → converges.

$\sum\frac{\ln k}{k}$: for $k\ge3$, $\frac{\ln k}{k}\ge\frac1k$, and $\sum\frac1k$ diverges → diverges.

---

## Example 6: Limit Comparison Test (§11.4 Ex 3, Ex 4)

If $\lim_{n\to\infty}\frac{a_n}{b_n}=L$ with $0<L<\infty$, the two positive series share their fate.

$\sum\frac{1}{2^n-1}$: take $b_n=\frac{1}{2^n}$. Then $\frac{a_n}{b_n}=\frac{2^n}{2^n-1}\to1$ → converges.

$\sum\frac{2n^2+3n}{\sqrt{5+n^5}}$: dominant parts give $b_n=\frac{2n^2}{n^{5/2}}=\frac{2}{n^{1/2}}$, a divergent $p$-series with $p=\frac12$ → diverges.

---

## Example 7: Ratio Test (§11.6 Ex 1, Ex 2)

$$\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=\rho. \quad \rho<1 \Rightarrow \text{converges}, \quad \rho>1 \Rightarrow \text{diverges}, \quad \rho=1 \Rightarrow \text{no information.}$$

$\sum(-1)^n\frac{n^3}{3^n}$: $\rho=\lim\frac{(n+1)^3}{3n^3}=\frac13<1$ → converges (absolutely).

$\sum\frac{n^n}{n!}$: $\rho=\lim\frac{(n+1)^{n+1}}{(n+1)!}\cdot\frac{n!}{n^n}=\lim\left(1+\frac1n\right)^n=e>1$ → diverges.

![Ratio test visualization]({{graph:18a-4-ratio-test}})

*Graph 18A-4: Left — $\sum n!/n^n$: the ratio $a_{n+1}/a_n$ converges to $1/e < 1$, so the series converges. Right — $\sum n!/2^n$: the ratio grows without bound ($> 1$), so the series diverges.*

---

## Example 8: Root Test (§11.6 Ex 4, Ex 5)

$$\lim_{n\to\infty}\sqrt[n]{|a_n|}=\rho, \text{ with the same criteria as the Ratio Test.}$$

$\sum\left(\frac{2n+3}{3n+2}\right)^n$: $\rho=\frac23<1$ → converges.

$\sum\left(\frac{n}{n+1}\right)^n$: $\rho=1$, so the Root Test says nothing; but $\left(\frac{n}{n+1}\right)^n\to\frac1e\neq0$, so the Divergence Test gives divergence.

---

## Example 9: Alternating Series Test (§11.5 Ex 1)

If $b_n>0$, $b_{n+1}\le b_n$, and $\lim b_n=0$, then $\sum(-1)^{n-1}b_n$ converges.

$\sum_{n=1}^\infty\frac{(-1)^{n-1}}{n}=1-\frac12+\frac13-\cdots$ converges.

**Error bound**: $|S-S_N|\le b_{N+1}$ — the error is at most the first omitted term.

![Alternating series — conditional convergence]({{graph:18a-3-alternating-series}})

*Graph 18A-3: Left — Alternating harmonic series $\sum (-1)^{n+1}/n$ converges to $\ln 2$. Terms alternate sign and shrink to zero; partial sums converge in a zigzag pattern. Right — Comparison of $\sum 1/n$ (divergent) vs $\sum (-1)^{n+1}/n$ (convergent conditional): the absolute series diverges while the alternating series converges.*

---

## Example 10: Absolute vs Conditional Convergence (§11.5 Ex 5, Ex 6, Ex 7)

- $\sum|a_n|$ converges → $\sum a_n$ converges **absolutely** (rearrangement never changes the sum).
- $\sum a_n$ converges but $\sum|a_n|$ diverges → **conditionally convergent** (rearrangement can change the sum).

$\sum(-1)^{n-1}\frac{1}{n^2}$: $\sum\frac{1}{n^2}$ converges → absolutely convergent.

$\sum(-1)^{n-1}\frac1n$: $\sum\frac1n$ diverges → conditionally convergent.

$\sum\frac{\cos n}{n^2}$: not alternating, but $\left|\frac{\cos n}{n^2}\right|\le\frac{1}{n^2}$ → absolutely convergent.

---

## Example 11: The Strategy in Action (§11.7 Ex 1–6)

Classify by form, then pick the test.

| Series | Form | Test | Verdict |
|:--|:--|:--|:--|
| $\sum\frac{n-1}{2n+1}$ | $a_n\not\to0$ | Divergence | diverges |
| $\sum\frac{\sqrt{n^3+1}}{3n^3+4n^2+2}$ | algebraic | Limit Comparison, $b_n=\frac{1}{3n^{3/2}}$ | converges |
| $\sum n e^{-n^2}$ | integrable $f$ | Integral | converges |
| $\sum(-1)^n\frac{n^2}{n^4+1}$ | alternating | Alternating, abs. via $\sum 1/n^2$ | converges absolutely |
| $\sum\frac{2^k}{k!}$ | factorial | Ratio | converges |
| $\sum\frac{1}{2+3^n}$ | like geometric | Comparison, $\sum 1/3^n$ | converges |

> **Up to here**: 10 convergence tests. Geometric: $|r|<1$. $p$-series: $p>1$. Integral / Comparison / Limit Comparison / Ratio / Root / Alternating + Divergence Test.

---

## Common Mistakes

### Mistake 1: $\lim a_n = 0$ guarantees convergence

**Wrong**. The harmonic series $\sum 1/n$ has $a_n \to 0$ but diverges.

### Mistake 2: Ratio test gives $\rho=1$ and you conclude divergence

**Wrong**. $\rho=1$ is inconclusive. Try comparison or the integral test.

### Mistake 3: Root test gives $\rho=1$ and you stop thinking

At $\rho=1$ the Root Test says nothing, yet $\sum\left(\frac{n}{n+1}\right)^n$ still diverges — because its terms tend to $1/e$, not $0$.

---

## What We Just Did

```
(1) Series = limit of partial sums. Divergence Test: a_n →/ 0 ⇒ diverges.
(2) Geometric: Σar^{n-1} = a/(1-r), |r|<1. Telescoping: terms cancel. p-series: Σ1/n^p, p>1.
(3) Integral Test: Σf(n) ↔ ∫f(x)dx. Comparison / Limit Comparison: bound by a known series.
(4) Ratio / Root: ρ<1 ⇒ converges, ρ>1 ⇒ diverges, ρ=1 ⇒ no information.
(5) Alternating: decreasing + →0 ⇒ converges, error ≤ first omitted term.
(6) Absolute convergence ⇒ convergence. Conditional: rearrangements matter.
```

---

## Basic Drills

**D1.** (§11.2 #5) The partial sums are $S_n=2-3(0.8)^n$. Find the sum.

**D2.** (§11.2 #23) $3-4+\frac{16}{3}-\frac{64}{9}+\cdots$. Converge or diverge?

**D3.** (§11.2 #25) $10-2+0.4-0.08+\cdots$. Sum if convergent.

**D4.** (§11.2 #35) $\frac25+\frac{4}{25}+\frac{8}{125}+\cdots$. Sum if convergent.

**D5.** (§11.2 #37) $\sum_{n=1}^\infty\frac{2+n}{1-2n}$. Converge or diverge?

**D6.** (§11.2 #19) Telescoping: $\sum_{n=1}^\infty\frac{3}{n(n+3)}$.

<details>
<summary>💡 Hint</summary>

$\frac{3}{n(n+3)} = \frac1n-\frac1{n+3}$. Write out $S_N$ and see which terms survive.

</details>

**D7.** (§11.3 #3) $p$-series: $\sum_{n=1}^\infty n^{-3}$.

**D8.** (§11.3 #4) $p$-series: $\sum_{n=1}^\infty n^{-0.3}$.

**D9.** (§11.3 #23) Integral test: $\sum_{n=2}^\infty\frac{1}{n\ln n}$.

<details>
<summary>💡 Hint</summary>

$\int_1^\infty\frac{dx}{x\ln x}$. Substitute $u=\ln x$, so $du=dx/x$.

</details>

**D10.** (§11.4 #7) Comparison: $\sum_{n=1}^\infty\frac{1}{n^3+8}$.

**D11.** (§11.6 #3) Ratio: $\sum_{n=1}^\infty\frac{n}{5^n}$.

**D12.** (§11.6 #21) Root: $\sum_{n=1}^\infty\left(\frac{n^2+1}{2n^2+1}\right)^n$.

<details>
<summary>💡 Hint</summary>

$\sqrt[n]{a_n}=\frac{n^2+1}{2n^2+1}$. What is its limit?

</details>

> Solutions: [Solutions](solutions/18A-solutions.md#basic-drill)

---

## Advanced Drills

**A1.** (§11.3 #31) For which $p$ does $\sum_{n=2}^\infty\frac{1}{n(\ln n)^p}$ converge?

<details>
<summary>💡 Hint</summary>

Integral test with $u=\ln x$ turns it into $\int u^{-p}\,du$ — a $p$-integral.

</details>

**A2.** (§11.6 #14) $\sum_{n=1}^\infty\frac{n!}{n^n}$. Determine convergence.

<details>
<summary>💡 Hint</summary>

$\frac{a_{n+1}}{a_n}=\frac{n^n}{(n+1)^n}=\left(1+\frac1n\right)^{-n}$.

</details>

**A3.** (§11.5 #29) $\sum_{n=1}^\infty\frac{1+2\sin n}{n^3}$. Determine convergence.

<details>
<summary>💡 Hint</summary>

$|1+2\sin n|\le3$, so the terms are bounded by $3/n^3$.

</details>

**A4.** (§11.5 #30) $\sum_{n=1}^\infty(-1)^{n-1}\frac{n}{n^2+4}$. Absolute or conditional?

<details>
<summary>💡 Hint</summary>

$b_n=\frac{n}{n^2+4}$ decreases to $0$, so the series converges. Compare $\sum b_n$ to the harmonic series.

</details>

**A5.** (§11.7 #31) $\sum_{n=1}^\infty\left(\frac{n}{n+1}\right)^{n^2}$. Determine convergence.

<details>
<summary>💡 Hint</summary>

$\sqrt[n]{a_n}=\left(\frac{n}{n+1}\right)^n=\left(1-\frac{1}{n+1}\right)^n\to\frac1e$.

</details>

**A6.** (§11.5 #46) For which $p$ does $\sum_{n=1}^\infty\frac{(-1)^{n-1}}{n^p}$ converge?

<details>
<summary>💡 Hint</summary>

Check the two conditions of the Alternating Series Test for $b_n=n^{-p}$.

</details>

**A7.** (§11.7 #13) $\sum_{n=1}^\infty\frac{1\cdot3\cdot5\cdots(2n-1)}{2\cdot5\cdot8\cdots(3n-1)}$. Determine convergence.

<details>
<summary>💡 Hint</summary>

The next factor is $2n+1$ on top and $3n+2$ on the bottom.

</details>

**A8.** (§11.4 #54) Prove: if $a_n\ge0$ and $\sum a_n$ converges, then $\sum a_n^2$ converges.

<details>
<summary>💡 Hint</summary>

Use $a_n\to0$ to get $a_n\le1$ eventually, then $a_n^2\le a_n$.

</details>

**A9.** (§11.4 #48) If $a_n,b_n>0$, $\sum b_n$ converges, and $a_n/b_n\to0$, prove $\sum a_n$ converges. Apply it to $\sum\frac{\ln n}{n^3}$.

<details>
<summary>💡 Hint</summary>

For the application choose $b_n=\frac{1}{n^2}$ and compute $\frac{a_n}{b_n}=\frac{\ln n}{n}\to0$.

</details>

**A10.** (§11.6 #39) For which series is the Ratio Test inconclusive?
(a) $\sum\frac{1}{n^3}$ (b) $\sum\frac{n}{2^n}$ (c) $\sum\frac{(-3)^{n-1}}{\sqrt n}$ (d) $\sum\frac{\sqrt n}{1+n^2}$

<details>
<summary>💡 Hint</summary>

Inconclusive means $\rho=1$. All four are algebraic or rational in $n$ — which two are also $p$-series in disguise?

</details>

**A11.** (§11.7 #12) $\sum_{n=1}^\infty\frac{\sqrt{n^4+1}}{n^3+n}$. Determine convergence.

<details>
<summary>💡 Hint</summary>

Keep the highest powers: $\frac{n^2}{n^3}=\frac1n$. Limit-compare with the harmonic series.

</details>

**A12.** (§11.3 #42) How many terms of $\sum_{n=2}^\infty\frac{1}{n(\ln n)^2}$ give the sum within $0.01$?

<details>
<summary>💡 Hint</summary>

Remainder bound: $R_N\le\int_N^\infty\frac{dx}{x(\ln x)^2}=\frac{1}{\ln N}$. Solve $\frac{1}{\ln N}<0.01$.

</details>

> Solutions: [Solutions](solutions/18A-solutions.md#advanced-drill)

---

## How to Read These Symbols

| Symbol | Reads as | Meaning |
|:---:|:---:|------|
| $\sum_{n=1}^{\infty} a_n$ converges | "the series converges" | partial sums approach a finite limit |
| $\sum a_n$ diverges | "the series diverges" | partial sums → ∞, −∞, or oscillate |
| $\lim_{n\to\infty} a_n \neq 0$ | "limit of a n does not equal zero" | Divergence Test: if limit ≠ 0, series MUST diverge (but limit=0 does NOT guarantee convergence!) |
| geometric series | "geometric series" | $\sum ar^{n-1}$ — converges to $a/(1-r)$ if |r|<1 |
| $p$-series | "p series" | $\sum 1/n^p$ — converges if p>1, diverges if p≤1 |
| Integral Test | "integral test" | compare series to $\int f(x)dx$ where $f(n)=a_n$ — same convergence behavior |
| Comparison Test | "comparison test" / "direct comparison" | term-by-term ≤ known series — if bigger converges, smaller also converges |
| Limit Comparison Test | "limit comparison test" | if $\lim a_n/b_n = c > 0$ (finite), series share convergence fate |
| Ratio Test | "ratio test" | $\lim |a_{n+1}/a_n| = \rho$: ρ<1→converges, ρ>1→diverges, ρ=1→inconclusive |
| Root Test | "root test" | $\lim \sqrt[n]{|a_n|} = \rho$ — same criteria as Ratio Test |
| Alternating Series Test | "alternating series test" | terms decrease to 0 in absolute value → converges |
| absolutely / conditionally convergent | "absolutely convergent" / "conditionally convergent" | ∑|a_n| converges / ∑|a_n| diverges but ∑a_n converges |

---

## Today's Procedure

```
Step 1: Divergence Test first — if a_n →/ 0, stop.
Step 2: Recognize the type — geometric? p-series? telescoping?
Step 3: Choose test in order: Integral → Comparison → Limit Comparison → Ratio → Root.
Step 4: For alternating: check decreasing + limit zero. Check absolute vs conditional.
```
