# Solutions — 18A: Infinite Series — Does It Converge?

> Back to [18A — Infinite Series](../18A-series-convergence.md)

## Basic Drills

### D1. (§11.2 #5) The partial sums are $S_n=2-3(0.8)^n$. Find the sum.

$(0.8)^n\to0$, so $S_n\to2$.

> **Answer**: converges to $2$

### D2. (§11.2 #23) $3-4+\frac{16}{3}-\frac{64}{9}+\cdots$

Geometric with $a=3$, $r=-\frac43$. $|r|=\frac43\ge1$, so it diverges.

> **Answer**: diverges

### D3. (§11.2 #25) $10-2+0.4-0.08+\cdots$

$a=10$, $r=-\frac15$, $|r|<1$: $S=\frac{10}{1+1/5}=\frac{10}{6/5}=\frac{25}{3}$.

> **Answer**: $\frac{25}{3}$

### D4. (§11.2 #35) $\frac25+\frac{4}{25}+\frac{8}{125}+\cdots$

$a=\frac25$, $r=\frac25$: $S=\frac{2/5}{1-2/5}=\frac{2/5}{3/5}=\frac23$.

> **Answer**: $\frac23$

### D5. (§11.2 #37) $\sum_{n=1}^\infty\frac{2+n}{1-2n}$

$a_n=\frac{2+n}{1-2n}\to-\frac12\neq0$, so the series diverges by the Divergence Test.

> **Answer**: diverges

### D6. (§11.2 #19) Telescoping: $\sum_{n=1}^\infty\frac{3}{n(n+3)}$

$\frac{3}{n(n+3)}=\frac1n-\frac1{n+3}$. Then $S_N=1+\frac12+\frac13-\frac{1}{N+1}-\frac{1}{N+2}-\frac{1}{N+3}\to\frac{11}{6}$.

> **Answer**: converges to $\frac{11}{6}$

### D7. (§11.3 #3) $\sum_{n=1}^\infty n^{-3}$

$p$-series with $p=3>1$.

> **Answer**: converges

### D8. (§11.3 #4) $\sum_{n=1}^\infty n^{-0.3}$

$p$-series with $p=0.3\le1$.

> **Answer**: diverges

### D9. (§11.3 #23) Integral test: $\sum_{n=2}^\infty\frac{1}{n\ln n}$

$\int_2^\infty\frac{dx}{x\ln x}=\left[\ln(\ln x)\right]_2^\infty=\infty$.

> **Answer**: diverges

### D10. (§11.4 #7) $\sum_{n=1}^\infty\frac{1}{n^3+8}$

$\frac{1}{n^3+8}\le\frac{1}{n^3}$ and $\sum\frac{1}{n^3}$ converges.

> **Answer**: converges

### D11. (§11.6 #3) Ratio: $\sum_{n=1}^\infty\frac{n}{5^n}$

$\rho=\lim\frac{n+1}{5n}=\frac15<1$.

> **Answer**: converges

### D12. (§11.6 #21) Root: $\sum_{n=1}^\infty\left(\frac{n^2+1}{2n^2+1}\right)^n$

$\rho=\lim\frac{n^2+1}{2n^2+1}=\frac12<1$.

> **Answer**: converges

---

## Advanced Drills

### A1. (§11.3 #31) For which $p$ does $\sum_{n=2}^\infty\frac{1}{n(\ln n)^p}$ converge?

$u=\ln x$ gives $\int_2^\infty\frac{du}{u^p}$, which converges iff $p>1$.

> **Answer**: converges iff $p>1$

### A2. (§11.6 #14) $\sum_{n=1}^\infty\frac{n!}{n^n}$

$\rho=\lim\frac{n^n}{(n+1)^n}=\lim\left(1+\frac1n\right)^{-n}=\frac1e<1$.

> **Answer**: converges

### A3. (§11.5 #29) $\sum_{n=1}^\infty\frac{1+2\sin n}{n^3}$

$\left|\frac{1+2\sin n}{n^3}\right|\le\frac{3}{n^3}$ and $\sum\frac{1}{n^3}$ converges.

> **Answer**: absolutely convergent

### A4. (§11.5 #30) $\sum_{n=1}^\infty(-1)^{n-1}\frac{n}{n^2+4}$

$b_n=\frac{n}{n^2+4}$ decreases to $0$, so the alternating series converges. But $\sum\frac{n}{n^2+4}$ behaves like $\sum\frac1n$ (limit comparison, ratio $\to1$), which diverges.

> **Answer**: conditionally convergent

### A5. (§11.7 #31) $\sum_{n=1}^\infty\left(\frac{n}{n+1}\right)^{n^2}$

$\rho=\lim\left(\frac{n}{n+1}\right)^n=\lim\left(1-\frac{1}{n+1}\right)^n=\frac1e<1$.

> **Answer**: converges

### A6. (§11.5 #46) For which $p$ does $\sum_{n=1}^\infty\frac{(-1)^{n-1}}{n^p}$ converge?

$b_n=n^{-p}$ must decrease to $0$, which happens exactly when $p>0$.

> **Answer**: converges iff $p>0$

### A7. (§11.7 #13) $\sum_{n=1}^\infty\frac{1\cdot3\cdot5\cdots(2n-1)}{2\cdot5\cdot8\cdots(3n-1)}$

$\left|\frac{a_{n+1}}{a_n}\right|=\frac{2n+1}{3n+2}\to\frac23<1$.

> **Answer**: converges

### A8. (§11.4 #54) Prove: if $a_n\ge0$ and $\sum a_n$ converges, then $\sum a_n^2$ converges.

Since $\sum a_n$ converges, $a_n\to0$; hence $0\le a_n\le1$ for all $n\ge N$. Then $a_n^2\le a_n$ for $n\ge N$, so $\sum a_n^2$ converges by the Direct Comparison Test.

> **Answer**: proved by comparison with $\sum a_n$

### A9. (§11.4 #48) If $a_n,b_n>0$, $\sum b_n$ converges, and $a_n/b_n\to0$, prove $\sum a_n$ converges.

$\frac{a_n}{b_n}\to0$ means $a_n\le b_n$ eventually, so comparison applies. Applied to $\frac{\ln n}{n^3}$: take $b_n=\frac{1}{n^2}$, then $\frac{a_n}{b_n}=\frac{\ln n}{n}\to0$ and $\sum\frac{1}{n^2}$ converges.

> **Answer**: $\sum\frac{\ln n}{n^3}$ converges

### A10. (§11.6 #39) Ratio Test inconclusive?

Inconclusive means $\rho=1$. (a) $\frac{1}{n^3}$ and (d) $\frac{\sqrt n}{1+n^2}$ have $\rho=1$ — both are $p$-series in disguise and converge. (b) $\rho=\frac12$ (converges); (c) $\rho=3$ (diverges).

> **Answer**: (a) and (d)

### A11. (§11.7 #12) $\sum_{n=1}^\infty\frac{\sqrt{n^4+1}}{n^3+n}$

$a_n\sim\frac{n^2}{n^3}=\frac1n$; limit comparison with $\sum\frac1n$ (ratio $\to1$) shows divergence.

> **Answer**: diverges

### A12. (§11.3 #42) How many terms to get $\sum_{n=2}^\infty\frac{1}{n(\ln n)^2}$ within $0.01$?

$R_N\le\int_N^\infty\frac{dx}{x(\ln x)^2}=\frac{1}{\ln N}$. Need $\frac{1}{\ln N}<0.01$, i.e. $N>e^{100}$.

> **Answer**: more than $e^{100}\approx2.7\times10^{43}$ terms

---

## Answer Check

| Problem | Convergence | Key test |
|:--------|:-----------:|:--------:|
| D1–D6 | 2, diverge, 25/3, 2/3, diverge, 11/6 | geometric / telescoping / divergence |
| D7–D9 | converge, diverge, diverge | p-series / integral |
| D10–D12 | converge, converge, converge | comparison / ratio / root |
| A1–A6 | see above | integral / ratio / comparison / alternating / root |
| A7–A12 | see above | ratio / proof / limit comparison |
