# Solutions — 18B: Power Series — Where Does It Converge?

> Back to [18B — Power Series](../18B-power-series.md)

## Basic Drills

### D1. (§11.8 #3) Radius and interval of $\sum_{n=1}^\infty \frac{x^n}{n}$.

$R=\lim\frac{n+1}{n}=1$. At $x=1$ the harmonic series diverges; at $x=-1$ the alternating series converges.

> **Answer**: $R=1$, interval $[-1,1)$

### D2. (§11.8 #7) $\sum_{n=1}^\infty \frac{n}{5^n}x^n$.

$R=\lim\frac{n/5^n}{(n+1)/5^{n+1}}=5$. At $x=\pm5$ the terms do not go to $0$.

> **Answer**: $R=5$, interval $(-5,5)$

### D3. (§11.8 #12) $\sum_{n=1}^\infty \frac{(-1)^n x^n}{n^2}$.

$R=1$. At $x=\pm1$ the terms are $\pm1/n^2$ — a convergent $p$-series.

> **Answer**: $R=1$, interval $[-1,1]$

### D4. (§11.8 #13) $\sum_{n=0}^\infty \frac{x^n}{n!}$.

$\frac{c_n}{c_{n+1}}=n+1\to\infty$.

> **Answer**: $R=\infty$

### D5. (§11.8 #21) $\sum_{n=0}^\infty \frac{(x-2)^n}{n^2+1}$.

$R=1$. At $x=3$: $\sum\frac{1}{n^2+1}$ converges; at $x=1$: $\sum\frac{(-1)^n}{n^2+1}$ converges.

> **Answer**: $R=1$, interval $[1,3]$

### D6. (§11.8 #4) $\sum_{n=1}^\infty (-1)^n n x^n$.

$R=\lim\frac{n}{n+1}=1$. At $x=\pm1$ the terms are $\pm n$ and do not go to $0$.

> **Answer**: $R=1$, interval $(-1,1)$

### D7. (§11.9 #3) $\frac{1}{1+x}$.

$\frac{1}{1-(-x)}=\sum(-1)^n x^n$.

> **Answer**: $\sum_{n=0}^\infty(-1)^n x^n$, $|x|<1$

### D8. (§11.9 #5) $\frac{1}{1-x^2}$.

$\sum(x^2)^n=\sum x^{2n}$.

> **Answer**: $\sum_{n=0}^\infty x^{2n}$, $|x|<1$

### D9. (§11.9 #7) $\frac{2}{3-x}$.

$\frac23\cdot\frac{1}{1-x/3}=\frac23\sum\left(\frac{x}{3}\right)^n$.

> **Answer**: $\sum_{n=0}^\infty \frac{2x^n}{3^{n+1}}$, $|x|<3$

### D10. (§11.9 #15a) $\frac{1}{(1+x)^2}$.

Differentiate $\frac{1}{1+x}=\sum(-1)^n x^n$: $-\frac{1}{(1+x)^2}=\sum(-1)^n n x^{n-1}$, so $\frac{1}{(1+x)^2}=\sum(-1)^n(n+1)x^n$.

> **Answer**: $\sum_{n=0}^\infty(-1)^n(n+1)x^n$, $R=1$

### D11. (§11.9 #16a) $\ln(1-x)$.

$\ln(1-x)=-\int\frac{dx}{1-x}=-\sum\frac{x^{n+1}}{n+1}=-\sum_{n=1}^\infty\frac{x^n}{n}$.

> **Answer**: $-\sum_{n=1}^\infty\frac{x^n}{n}$, interval $[-1,1)$

### D12. (§11.9 #46b) $\sum_{n=1}^\infty \frac{n}{2^n}$.

From $\sum n x^n=\frac{x}{(1-x)^2}$, set $x=\frac12$: $\frac{1/2}{(1/2)^2}=2$.

> **Answer**: $2$

### D13. (§11.9 #27) $\int \frac{t}{1-t^8}\,dt$.

$\frac{t}{1-t^8}=t\sum t^{8n}=\sum t^{8n+1}$, so the integral is $\sum\frac{t^{8n+2}}{8n+2}+C$.

> **Answer**: $\sum_{n=0}^\infty\frac{t^{8n+2}}{8n+2}+C$, $R=1$

### D14. (§11.8 #16) $\sum_{n=1}^\infty 2^n n^2 x^n$.

$R=\lim\frac{2^n n^2}{2^{n+1}(n+1)^2}=\frac12$.

> **Answer**: $R=\frac12$

### D15. (§11.8 #31) $\sum_{n=1}^\infty n!(2x-1)^n$.

Write $2x-1=2\left(x-\frac12\right)$, so $c_n=n!\,2^n$ and $\frac{c_n}{c_{n+1}}=\frac{1}{2(n+1)}\to0$.

> **Answer**: $R=0$ (converges only at $x=\frac12$)

### D16. (§11.8 #25) $\sum_{n=1}^\infty \frac{(x-2)^n}{n^n}$.

$\frac{c_n}{c_{n+1}}=\frac{(n+1)^{n+1}}{n^n}=(n+1)\left(1+\frac1n\right)^n\to\infty$.

> **Answer**: $R=\infty$

---

## Advanced Drills

### A1. (§11.8 #23) $\sum_{n=2}^\infty \frac{(x+2)^n}{2^n \ln n}$.

$R=2$ about $-2$, so $(-4,0)$. At $x=0$: $\sum\frac{1}{\ln n}$ diverges (compare to $\frac1n$); at $x=-4$: $\sum\frac{(-1)^n}{\ln n}$ converges.

> **Answer**: $R=2$, interval $[-4,0)$

### A2. (§11.9 #13) $\frac{2x-4}{x^2-4x+3}$.

$\frac{2x-4}{(x-1)(x-3)}=\frac{1}{x-1}+\frac{1}{x-3}=-\frac{1}{1-x}-\frac13\cdot\frac{1}{1-x/3}$.

> **Answer**: $-\sum_{n=0}^\infty x^n-\frac13\sum_{n=0}^\infty\left(\frac{x}{3}\right)^n$, interval $(-1,1)$

### A3. (§11.9 #22) $x^2\arctan(x^3)$.

$\arctan u=\sum(-1)^n\frac{u^{2n+1}}{2n+1}$ with $u=x^3$, then multiply by $x^2$.

> **Answer**: $\sum_{n=0}^\infty\frac{(-1)^n x^{6n+5}}{2n+1}$, $|x|<1$

### A4. (§11.9 #46a) Show $\sum_{n=1}^\infty n x^{n-1}=\frac{1}{(1-x)^2}$, then $\sum\frac{n}{2^n}=2$.

Differentiate $\sum x^n=\frac{1}{1-x}$ to get $\sum n x^{n-1}=\frac{1}{(1-x)^2}$. Multiplying by $x$: $\sum n x^n=\frac{x}{(1-x)^2}$. At $x=\frac12$: $\frac{1/2}{1/4}=2$.

> **Answer**: $2$

### A5. (§11.8 #26) $\sum_{n=1}^\infty \frac{(2x-1)^n}{5^n\sqrt n}$.

$R=\frac52$ about $x=\frac12$, so $-\frac34<x<\frac74$. At $x=\frac74$: $\sum\frac{1}{\sqrt n}$ diverges; at $x=-\frac34$: $\sum\frac{(-1)^n}{\sqrt n}$ converges.

> **Answer**: $R=\frac52$, interval $\left[-\frac34,\frac74\right)$

### A6. (§11.9 #34) $\int_0^{0.3} \frac{x^2}{1+x^4}\,dx$.

$\frac{x^2}{1+x^4}=\sum(-1)^n x^{4n+2}$; integrating, $\sum(-1)^n\frac{(0.3)^{4n+3}}{4n+3}=0.009-0.0000312+\cdots$

> **Answer**: $\approx0.008969$

### A7. (§11.8 #39) $\sum_{n=0}^\infty \frac{(n!)^k}{(kn)!}x^n$.

$\frac{c_n}{c_{n+1}}=\frac{(n+1)^k}{(kn+k)(kn+k-1)\cdots(kn+1)}\to\frac{1}{k^k}$.

> **Answer**: $R=k^k$

### A8. (§11.9 #37) $f(x)=\sum\frac{x^n}{n!}$: show $f'=f$ and identify $f$.

$f'(x)=\sum_{n=1}^\infty\frac{n x^{n-1}}{n!}=\sum_{n=1}^\infty\frac{x^{n-1}}{(n-1)!}=f(x)$, and $f(0)=1$. The unique solution is $f(x)=e^x$.

> **Answer**: $f=e^x$

### A9. (§11.8 #43) $f(x)=1+2x+x^2+2x^3+\cdots$.

$f=\sum x^{2n}+2\sum x^{2n+1}=\frac{1}{1-x^2}+\frac{2x}{1-x^2}=\frac{1+2x}{1-x^2}$.

> **Answer**: $f(x)=\frac{1+2x}{1-x^2}$, interval $(-1,1)$

### A10. (§11.9 #25) $\ln\left(\frac{1+x}{1-x}\right)$.

$\ln(1+x)-\ln(1-x)=\sum(-1)^{n-1}\frac{x^n}{n}+\sum\frac{x^n}{n}$; even powers cancel.

> **Answer**: $2\sum_{n=0}^\infty\frac{x^{2n+1}}{2n+1}$, interval $(-1,1)$

### A11. (§11.9 #16c) Express $\ln 2$ as a series.

Set $x=\frac12$ in $\ln(1-x)=-\sum\frac{x^n}{n}$: $\ln\frac12=-\sum\frac{(1/2)^n}{n}$, so $\ln2=\sum_{n=1}^\infty\frac{1}{n\,2^n}$.

> **Answer**: $\ln2=\sum_{n=1}^\infty\frac{1}{n\,2^n}$

### A12. (§11.8 #46) Radius of $\sum c_n x^{2n}$ if $\sum c_n x^n$ has radius $R$.

Let $u=x^2$. Convergence requires $|u|<R$, i.e. $|x|<\sqrt R$.

> **Answer**: $\sqrt R$

---

## Answer Check

| Problem | Answer |
|:--------|:-------|
| D1–D6 | $R=1,[-1,1)$ · $5,(-5,5)$ · $1,[-1,1]$ · $\infty$ · $1,[1,3]$ · $1,(-1,1)$ |
| D7–D11 | geometric-based series from $\frac{1}{1-x}$ |
| D12–D16 | $2$ · $\sum\frac{t^{8n+2}}{8n+2}$ · $\frac12$ · $0$ · $\infty$ |
| A1–A12 | see above |
