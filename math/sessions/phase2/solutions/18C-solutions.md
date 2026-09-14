# Solutions — 18C: Taylor Series — Approximating Any Function

> Back to [18C — Taylor Series](../18C-taylor-series.md)

## Basic Drills

### D1. (§11.10 #14) Maclaurin series for $e^{-2x}$.

Replace $x$ by $-2x$: $\sum\frac{(-2x)^n}{n!}=\sum\frac{(-1)^n 2^n x^n}{n!}$.

> **Answer**: $1-2x+2x^2-\frac43x^3+\cdots$

### D2. (§11.10 #16) Maclaurin series for $\sin 3x$.

$\sum(-1)^n\frac{(3x)^{2n+1}}{(2n+1)!}$.

> **Answer**: $3x-\frac{27x^3}{3!}+\frac{243x^5}{5!}-\cdots$

### D3. (§11.11 #3) $T_3(x)$ for $f(x)=e^x$ at $a=1$.

All derivatives equal $e^x$, so $f^{(n)}(1)=e$.

> **Answer**: $T_3(x)=e+e(x-1)+\frac{e}{2}(x-1)^2+\frac{e}{6}(x-1)^3$

### D4. (§11.10 #12) $\ln(1+x)$, $R$.

> **Answer**: $\sum_{n=1}^\infty\frac{(-1)^{n+1}x^n}{n}$, $R=1$

### D5. (§11.10 #13) $\cos x$, $R$.

> **Answer**: $\sum_{n=0}^\infty\frac{(-1)^n x^{2n}}{(2n)!}$, $R=\infty$

### D6. (§11.11 #5) $T_3(x)$ for $\cos x$ at $a=\frac{\pi}{2}$.

$f=0$, $f'=-\sin=-1$, $f''=-\cos=0$, $f'''=\sin=1$ at $\pi/2$.

> **Answer**: $T_3(x)=-\left(x-\frac{\pi}{2}\right)+\frac{1}{6}\left(x-\frac{\pi}{2}\right)^3$

### D7. (§11.10 #18) $x\cos x$.

> **Answer**: $\sum_{n=0}^\infty\frac{(-1)^n x^{2n+1}}{(2n)!}$

### D8. (§11.10 #11) $(1-x)^{-2}$.

> **Answer**: $\sum_{n=0}^\infty(n+1)x^n$, $|x|<1$

### D9. (§11.10 #42) $e^{3x}-e^{2x}$.

> **Answer**: $\sum_{n=0}^\infty\frac{(3^n-2^n)x^n}{n!}$

### D10. (§11.11 #25) Terms for $e^{0.1}$ within $10^{-5}$.

Need $\frac{(0.1)^{n+1}}{(n+1)!}<10^{-5}$. For $n=3$: $\frac{10^{-4}}{24}\approx4.2\times10^{-6}<10^{-5}$; $n=2$ gives $\frac{10^{-3}}{6}\approx1.7\times10^{-4}$, too big.

> **Answer**: 4 terms (through $x^3$, $n=3$)

### D11. (§11.10 #40) $\sin\left(\frac{\pi x}{4}\right)$.

> **Answer**: $\sum_{n=0}^\infty\frac{(-1)^n}{ (2n+1)!}\left(\frac{\pi}{4}\right)^{2n+1}x^{2n+1}$

### D12. (§11.10 #44) $x^2\ln(1+x^3)$.

$\ln(1+u)=\sum(-1)^{n-1}\frac{u^n}{n}$ with $u=x^3$, then multiply by $x^2$.

> **Answer**: $\sum_{n=1}^\infty\frac{(-1)^{n-1}x^{3n+2}}{n}$

### D13. (§11.10 #47) $\sin^2 x$.

$\sin^2x=\frac12(1-\cos2x)=\frac12\sum_{n=1}^\infty(-1)^{n+1}\frac{(2x)^{2n}}{(2n)!}$.

> **Answer**: $\sum_{n=1}^\infty\frac{(-1)^{n+1}2^{2n-1}x^{2n}}{(2n)!}$

### D14. (§11.10 #3) $f^{(n)}(0)=(n+1)!$.

$c_n=\frac{(n+1)!}{n!}=n+1$.

> **Answer**: $f(x)=\sum_{n=0}^\infty(n+1)x^n=\frac{1}{(1-x)^2}$, $R=1$

### D15. (§11.11 #27) $\sin x\approx x-\frac{x^3}{6}$ within $0.01$.

Alternating: $|R_3|\le\frac{|x|^5}{120}<0.01$ gives $|x|<(1.2)^{1/5}$.

> **Answer**: $|x|\lesssim1.037$

### D16. (§11.10 #35) $\sqrt[4]{1-x}$.

$(1+u)^{1/4}=1+\frac u4-\frac{3u^2}{32}+\frac{7u^3}{128}-\cdots$ with $u=-x$.

> **Answer**: $1-\frac x4-\frac{3x^2}{32}-\frac{7x^3}{128}-\cdots$, $R=1$

---

## Advanced Drills

### A1. (§11.10 #49) $\sinh x$.

$\frac{e^x-e^{-x}}{2}$: even powers cancel.

> **Answer**: $\sum_{n=0}^\infty\frac{x^{2n+1}}{(2n+1)!}$, $R=\infty$

### A2. (§11.10 #50) $\tanh^{-1}x$.

$\tanh^{-1}x=\frac12\left[\ln(1+x)-\ln(1-x)\right]=\frac12\left[\sum(-1)^{n-1}\frac{x^n}{n}+\sum\frac{x^n}{n}\right]$; even powers cancel.

> **Answer**: $\sum_{n=0}^\infty\frac{x^{2n+1}}{2n+1}$, $|x|<1$

### A3. (§11.10 #21) $x^5+2x^3+x$ at $a=2$.

$f(2)=50$, $f'(2)=105$, $f''(2)=184$, $f'''(2)=252$, $f^{(4)}(2)=240$, $f^{(5)}(2)=120$.

> **Answer**: $50+105(x-2)+92(x-2)^2+42(x-2)^3+10(x-2)^4+(x-2)^5$

### A4. (§11.10 #24) $\frac1x$ at $a=-3$.

$\frac1x=-\frac13\cdot\frac{1}{1-\frac{x+3}{3}}=-\sum_{n=0}^\infty\frac{(x+3)^n}{3^{n+1}}$.

> **Answer**: $-\sum_{n=0}^\infty\frac{(x+3)^n}{3^{n+1}}$, $R=3$

### A5. (§11.11 #30) Error $<0.0002$ for $f(5)$.

Taylor at $a=4$: $\sum\frac{(-1)^n(x-4)^n}{3^n(n+1)}$. The degree-5 remainder at $x=5$ is bounded by the next term, $\frac{1}{3^6\cdot7}=\frac{1}{5103}\approx1.96\times10^{-4}<2\times10^{-4}$.

> **Answer**: $|R_5|\le\frac{1}{5103}<0.0002$

### A6. (§11.10 #37) $\frac{1}{(2+x)^3}$.

$\frac{1}{(2+x)^3}=\frac18\left(1+\frac x2\right)^{-3}=\frac18\sum\binom{-3}{n}\left(\frac x2\right)^n$, and $\binom{-3}{n}=(-1)^n\frac{(n+2)(n+1)}{2}$.

> **Answer**: $\sum_{n=0}^\infty\frac{(-1)^n(n+2)(n+1)x^n}{16\cdot2^n}$, $R=2$

### A7. (§11.11 #59) $\lim_{x\to0}\frac{\sin x-x}{x^3}$.

$\sin x=x-\frac{x^3}{6}+\cdots$, so the quotient is $-\frac16+\cdots$

> **Answer**: $-\frac16$

### A8. (§11.11 #26) $\ln1.4$ within $0.001$.

At $x=0.4$ the series alternates; need $\frac{0.4^{n+1}}{n+1}<0.001$. $\frac{0.4^6}{6}\approx6.8\times10^{-4}<10^{-3}$.

> **Answer**: 5 terms

### A9. (§11.11 #57) $\sqrt x$, $a=1$, $n=3$, $0.9\le x\le1.1$.

$f(1)=1$, $f'(1)=\frac12$, $f''(1)=-\frac14$, $f'''(1)=\frac38$. $|f^{(4)}(x)|=\frac{15}{16}x^{-7/2}\le\frac{15}{16}(0.9)^{-7/2}\approx1.36$.

> **Answer**: $T_3=1+\frac{x-1}{2}-\frac{(x-1)^2}{8}+\frac{(x-1)^3}{16}$, $|R_3|\le\frac{1.36}{24}(0.1)^4\approx5.7\times10^{-6}$

### A10. (§11.11 #60) $F=\frac{mgR^2}{(R+h)^2}$.

$F=mg\left(1+\frac hR\right)^{-2}=mg\left[1-\frac{2h}{R}+\frac{3h^2}{R^2}-\cdots\right]$. Alternating error $<1\%$ needs $\frac{2h}{R}<0.01$.

> **Answer**: $h<0.005R=32$ km

### A11. (§11 Review #62) $f(x)=e^{x^2}$.

$e^{x^2}=\sum\frac{x^{2n}}{n!}$, so the coefficient of $x^{2n}$ satisfies $\frac{f^{(2n)}(0)}{(2n)!}=\frac{1}{n!}$.

> **Answer**: $f^{(2n)}(0)=\frac{(2n)!}{n!}$

### A12. (§11.11 #39) Newton's method is quadratic.

Taylor with $n=1$ at $a=x_n$: $0=f(r)=f(x_n)+f'(x_n)(r-x_n)+\frac{f''(\xi)}{2}(r-x_n)^2$. Using $x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}$,
$$|r-x_{n+1}|=\frac{|f''(\xi)|}{2|f'(x_n)|}|r-x_n|^2\le\frac{M}{2K}|r-x_n|^2.$$

> **Answer**: $|x_{n+1}-r|\le\frac{M}{2K}|x_n-r|^2$

---

## Answer Check

| Problem | Answer |
|:--------|:-------|
| D1–D6 | series/taylor polynomials for $e^{-2x},\sin3x,e^x,\ln(1+x),\cos x,\cos x$ at $\pi/2$ |
| D7–D12 | $x\cos x$, $(1-x)^{-2}$, $e^{3x}-e^{2x}$, 4 terms, $\sin\frac{\pi x}{4}$, $x^2\ln(1+x^3)$ |
| D13–D16 | $\sin^2x$, $\frac{1}{(1-x)^2}$, $|x|\lesssim1.037$, $\sqrt[4]{1-x}$ |
| A1–A12 | see above |
