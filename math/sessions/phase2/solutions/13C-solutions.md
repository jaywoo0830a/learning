# Solutions — 13C: Continuity, Theorems, and Sequences

> Back to [13C — Continuity, Theorems, and Sequences](../13C-continuity-theorems.md)

> **Source.** Every solution below matches an item in Stewart, *Calculus*, Sections 2.5 and 2.3, and Section 11.1 for the sequence items. Each heading cites its exercise number.

## Basic Drills

### D1. (§2.5 #13) $f(x)=3x^2+(x+2)^5$ continuous at $a=-1$.

By the Limit Laws (sum, constant multiple, power), $\displaystyle\lim_{x\to-1}f(x)=3(-1)^2+\bigl((-1)+2\bigr)^5=3+1=4$, and $f(-1)=4$. The limit equals the value, so $f$ is continuous at $-1$.

> **Answer**: continuous at $-1$ (both sides equal $4$)

---

### D2. (§2.5 #19) $f(x)=\dfrac{1}{x+2}$ at $a=-2$.

As $x\to-2^+$ the denominator $\to0^+$, so $f\to+\infty$; as $x\to-2^-$, $f\to-\infty$. The limit does not exist.

> **Answer**: infinite discontinuity (vertical asymptote at $x=-2$)

---

### D3. (§2.5 #21) $f(x)=\begin{cases}x+3,&x\le-1\\ 2^{x},&x>-1\end{cases}$ at $a=-1$.

Left limit: $x+3\to2$. Right limit: $2^{x}\to2^{-1}=\tfrac12$. The two differ.

> **Answer**: jump discontinuity at $x=-1$ (left $2$, right $\tfrac12$)

---

### D4. (§2.5 #22) $f(x)=\begin{cases}\frac{x^2-x}{x^2-1},&x\neq1\\ 1,&x=1\end{cases}$ at $x=1$.

$\dfrac{x^2-x}{x^2-1}=\dfrac{x(x-1)}{(x-1)(x+1)}=\dfrac{x}{x+1}\longrightarrow\dfrac12$. So the limit exists ($\tfrac12$) but $f(1)=1$.

> **Answer**: removable discontinuity at $x=1$ (limit $\tfrac12\neq f(1)=1$)

---

### D5. (§2.5 #25) $f(x)=\dfrac{x-3}{x^2-9}$ at $x=3$.

$x^2-9=(x-3)(x+3)$, so $f(x)=\dfrac{1}{x+3}\to\dfrac16$ as $x\to3$. The limit exists, so the discontinuity is removable.

> **Answer**: removable; set $f(3)=\dfrac16$

---

### D6. (§2.5 #26) $f(x)=\dfrac{x^2-7x+12}{x-3}$ at $x=3$.

$x^2-7x+12=(x-3)(x-4)$, so $f(x)=x-4\to-1$ as $x\to3$.

> **Answer**: removable; set $f(3)=-1$

---

### D7. (§2.5 #35) $\displaystyle\lim_{x\to2}x\sqrt{20-x^2}$ by continuity.

The function is a product/composition of continuous functions and is defined at $x=2$:

$$2\sqrt{20-4}=2\sqrt{16}=8.$$

> **Answer**: $8$

---

### D8. (§2.5 #36) $\displaystyle\lim_{\theta\to\pi/2}\sin\bigl(\tan(\cos\theta)\bigr)$ by continuity.

All three functions are continuous, so substitute: $\cos\frac\pi2=0$, $\tan0=0$, $\sin0=0$.

> **Answer**: $0$

---

### D9. (§2.5 #37) $\displaystyle\lim_{x\to1}\ln\!\left(\frac{5-x^2}{1+x}\right)$ by continuity.

The inside is positive at $x=1$, so substitute: $\ln\dfrac{5-1}{1+1}=\ln2$.

> **Answer**: $\ln 2$

---

### D10. (§11.1 #27) $\displaystyle\lim_{n\to\infty}\frac{5}{n+2}$.

The denominator grows without bound, so the term $\to0$.

> **Answer**: $0$

---

### D11. (§11.1 #29) $\displaystyle\lim_{n\to\infty}\frac{4n^2-3n}{2n^2+1}$.

Divide by $n^2$: $\dfrac{4-\frac3n}{2+\frac{1}{n^2}}\longrightarrow\dfrac{4}{2}=2$.

> **Answer**: $2$

---

### D12. (§11.1 #33) $\displaystyle\lim_{n\to\infty}3^{n}7^{-n}$.

$3^n7^{-n}=\left(\dfrac37\right)^n$, and $\left|\dfrac37\right|<1$, so the term $\to0$.

---

## Advanced Drills

### A1. (§2.5 #47) Find $c$ so $f(x)=\begin{cases}cx^2+2x,&x<2\\ x^3-cx,&x\ge2\end{cases}$ is continuous everywhere.

The pieces are polynomials, so the only place to check is the seam $x=2$. Match the one-sided limits:

$$4c+4=8-2c \quad\Longrightarrow\quad 6c=4 \quad\Longrightarrow\quad c=\frac23 .$$

> **Answer**: $c=\frac23$

---

### A2. (§2.5 #48) Find $a,b$ so the piecewise $f$ is continuous everywhere.

**At $x=2$**: the left piece $\dfrac{x^2-4}{x-2}=x+2\to4$, the middle piece $\to4a-2b+3$. So

$$4a-2b+3=4 \quad\Longrightarrow\quad 4a-2b=1 .$$

**At $x=3$**: the middle piece $\to9a-3b+3$, the right piece $\to6-a+b$. So

$$9a-3b+3=6-a+b \quad\Longrightarrow\quad 10a-4b=3 .$$

Solve: from the first, $b=2a-\tfrac12$. Substitute: $10a-4\left(2a-\tfrac12\right)=3\Rightarrow 2a+2=3\Rightarrow a=\tfrac12$, then $b=\tfrac12$.

> **Answer**: $a=b=\frac12$

---

### A3. (§2.5 #51a) Removable discontinuity of $f(x)=\dfrac{x^4-1}{x-1}$ at $a=1$?

$x^4-1=(x-1)(x^3+x^2+x+1)$, so $f(x)=x^3+x^2+x+1$ for $x\neq1$, and the limit at $1$ is $4$. The discontinuity is removable.

> **Answer**: removable; $g(x)=x^3+x^2+x+1$ (so $g(1)=4$)

---

### A4. (§2.5 #51b) Removable discontinuity of $f(x)=\dfrac{x^3-x^2-2x}{x-2}$ at $a=2$?

$x^3-x^2-2x=x(x-2)(x+1)$, so $f(x)=x(x+1)$ for $x\neq2$, and the limit at $2$ is $6$.

> **Answer**: removable; $g(x)=x(x+1)$ (so $g(2)=6$)

---

### A5. (§2.5 #53) Show $f(x)=x^2+10\sin x$ takes the value $1000$.

$f$ is continuous (sum of a polynomial and a bounded oscillation). Evaluate at two points:

$$f(0)=0<1000, \qquad f(1000)=10^6+10\sin(1000)\ge 10^6-10>1000 .$$

Since $1000$ lies between $f(0)$ and $f(1000)$, the IVT gives a $c$ with $f(c)=1000$.

> **Answer**: such a $c$ exists by the IVT

---

### A6. (§2.5 #55) IVT for $-x^3+4x+1=0$ on $(-1,0)$.

Let $f(x)=-x^3+4x+1$, a polynomial (continuous everywhere). Then

$$f(-1)=1-4+1=-2<0, \qquad f(0)=1>0 .$$

By the IVT there is a $c\in(-1,0)$ with $f(c)=0$.

> **Answer**: a solution exists in $(-1,0)$

---

### A7. (§2.5 #57) IVT for $e^{x}=3-2x$ on $(0,1)$.

Rewrite as $f(x)=e^{x}+2x-3$, continuous on $[0,1]$. Then

$$f(0)=1-3=-2<0, \qquad f(1)=e+2-3=e-1>0 .$$

By the IVT there is a $c\in(0,1)$ with $f(c)=0$, i.e. $e^{c}=3-2c$.

> **Answer**: a solution exists in $(0,1)$

---

### A8. (§2.5 #73) $f(x)=\begin{cases}x^4\sin(1/x),&x\neq0\\ 0,&x=0\end{cases}$ is continuous on $(-\infty,\infty)$.

**For $x\neq0$**: $x^4$ is a polynomial and $\sin(1/x)$ is a composition of continuous functions on $\mathbb{R}\setminus\{0\}$, so the product is continuous there (Theorems 4, 7, 9).

**At $x=0$**: squeeze. Since $|\sin(1/x)|\le1$,

$$0\le\left|x^4\sin\frac1x\right|\le x^4\longrightarrow0,$$

so $\lim_{x\to0}f(x)=0=f(0)$. Hence $f$ is continuous at $0$ as well.

> **Answer**: continuous on $(-\infty,\infty)$

---

### A9. (§2.5 #65) $f$ is continuous at $a$ iff $\displaystyle\lim_{h\to0}f(a+h)=f(a)$.

Substitute $x=a+h$. As $x\to a$ we have $h=x-a\to0$, and conversely. So the two statements

$$\lim_{x\to a}f(x)=f(a) \qquad\text{and}\qquad \lim_{h\to0}f(a+h)=f(a)$$

are the same limit written in two variables. Hence one holds exactly when the other does. $\square$

> **Answer**: proven — a change of variable $h=x-a$ shows the two limits are identical

---

### A10. (§11.1 #86) $a_1=\sqrt2$, $a_{n+1}=\sqrt{2+a_n}$.

**Convergence**: by induction $a_n$ is increasing and $a_n<3$ for every $n$, so by the Monotonic Sequence Theorem the limit $L$ exists.

**Limit**: $\sqrt{\phantom{x}}$ is continuous, so the limit passes through the recursion:

$$L=\sqrt{2+L}\quad\Longrightarrow\quad L^2=2+L\quad\Longrightarrow\quad L^2-L-2=0\quad\Longrightarrow\quad L=2 \text{ (positive root)}.$$

> **Answer**: $L=2$

---

### A11. (§11.1 #87) $a_1=1$, $a_{n+1}=3-\dfrac{1}{a_n}$.

**Convergence**: $0<a_n\le2$ and $a_n$ is increasing, and $a_n<3$ for all $n$, so the Monotonic Sequence Theorem gives a limit $L$.

**Limit**: pass the limit through the recursion:

$$L=3-\frac1L\quad\Longrightarrow\quad L^2-3L+1=0\quad\Longrightarrow\quad L=\frac{3\pm\sqrt5}{2}.$$

Since $a_n$ increases toward a value below $3$, the limit is the larger root.

> **Answer**: $L=\dfrac{3+\sqrt5}{2}\approx2.618$

---

## Answer Check

| Problem | Answer |
|:--------|:-------|
| D1–D4 | continuous ($4$); infinite; jump; removable |
| D5–D8 | $f(3)=\frac16$; $f(3)=-1$; $8$; $0$ |
| D9–D12 | $\ln 2$; $0$; $2$; $0$ |
| A1–A4 | $c=\frac23$; $a=b=\frac12$; $g=x^3+x^2+x+1$; $g=x(x+1)$ |
| A5–A8 | IVT; IVT; IVT; continuous on $\mathbb{R}$ |
| A9–A11 | proof; $L=2$; $L=\frac{3+\sqrt5}{2}$ |


> **Answer**: $0$
