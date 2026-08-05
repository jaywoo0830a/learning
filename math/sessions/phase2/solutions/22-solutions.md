# Solutions — 22: The Crown Jewels — MVT, FTC, and Taylor's Theorem

---

## Practice 1

**Verify Rolle's theorem for $f(x)=x^2-4x$ on $[0,4]$ and find the $c$ with $f'(c)=0$.**

$f(0)=0$, $f(4)=16-16=0$ — equal endpoints ✓. $f$ is a polynomial, continuous on $[0,4]$ and differentiable on $(0,4)$ ✓.

$f'(x)=2x-4$. Set $f'(c)=0$: $2c-4=0$ → $c=2\in(0,4)$. ✓

> **Answer**: $c=2$.

---

## Practice 2

**Apply MVT to $f(x)=x^3$ on $[1,3]$. Find the $c$ guaranteed.**

Average slope: $\frac{f(3)-f(1)}{3-1}=\frac{27-1}{2}=13$.

$f'(x)=3x^2$. Set $3c^2=13$ → $c^2=\frac{13}{3}$ → $c=\sqrt{13/3}\approx2.08\in(1,3)$. ✓

> **Answer**: $c=\sqrt{13/3}$.

---

## Practice 3

**Prove: if $f'(x)<0$ on $(a,b)$, then $f$ is strictly decreasing on $[a,b]$.**

Take any $x_1<x_2$ in $[a,b]$. By MVT on $[x_1,x_2]$: $f(x_2)-f(x_1)=f'(c)(x_2-x_1)$ for some $c\in(x_1,x_2)$. Since $f'(c)<0$ and $x_2-x_1>0$, the product is negative: $f(x_2)<f(x_1)$. Strictly decreasing. ✓

> **Answer**: $f(x_2)-f(x_1)=f'(c)(x_2-x_1)<0$.

---

## Practice 4

**Use FTC Part 2 to evaluate $\int_0^{\pi}\sin x\,dx$, and FTC Part 1 to find $\frac{d}{dx}\int_0^x \sin t\,dt$.**

$\int_0^{\pi}\sin x\,dx=[-\cos x]_0^{\pi}=-\cos\pi+\cos 0=1+1=2$.

$\frac{d}{dx}\int_0^x \sin t\,dt=\sin x$ (FTC Part 1).

> **Answers**: $\int_0^\pi\sin x\,dx=2$; $\frac{d}{dx}\int_0^x\sin t\,dt=\sin x$.

---

## Practice 5

**Degree-3 Taylor polynomial for $f(x)=e^x$ at $a=0$, and error bound for $e^{0.5}$.**

$f^{(k)}(0)=e^0=1$ for all $k$. So $P_3(x)=1+x+\frac{x^2}{2}+\frac{x^3}{6}$.

Remainder: $|R_3(0.5)|=\left|\frac{f^{(4)}(\xi)}{4!}(0.5)^4\right|=\frac{e^{\xi}}{24}\cdot\frac{1}{16}$ for some $\xi\in(0,0.5)$.

Max $e^{\xi}=e^{0.5}\approx1.6487$. So $|R_3(0.5)|\leq\frac{e^{0.5}}{24\cdot16}\approx\frac{1.6487}{384}\approx0.00429$.

$P_3(0.5)=1+0.5+0.125+0.02083=1.64583$; true $e^{0.5}\approx1.64872$ — within the bound.

> **Answer**: $P_3=1+x+\frac{x^2}{2}+\frac{x^3}{6}$; $|R_3(0.5)|\leq e^{0.5}/(24\cdot16)\approx0.0043$.

---

## Practice 6: Real Battle

**Prove $2^x=x^2$ has exactly three real solutions.**

Let $f(x)=2^x-x^2$.

**Existence**: $f(2)=4-4=0$ and $f(4)=16-16=0$ — two exact roots. Also $f(-1)=\frac12-1=-\frac12<0$ and $f(0)=1-0=1>0$, so by IVT there is a root in $(-1,0)$. At least three roots.

**At most three**: Suppose there were $\geq4$ distinct roots. By Rolle, $f'(x)=2^x\ln2-2x$ would have $\geq3$ roots; applying Rolle again, $f''(x)=2^x(\ln2)^2-2$ would have $\geq2$ roots. But $f''(x)=0$ has exactly one solution ($2^x=2/(\ln2)^2$). Contradiction. So there are at most three roots.

Combining: **exactly three** real solutions — $x=2$, $x=4$, and one in $(-1,0)$.

> **Answer**: Exactly three: $2$, $4$, and one negative root in $(-1,0)$ (existence via IVT, uniqueness bound via two Rolle applications).

---

## Basic Drills

**D1.** Rolle for $x^3-x$ on $[-1,1]$: $f(-1)=0$, $f(1)=0$ ✓. $f'=3x^2-1=0$ → $x=\pm\frac{1}{\sqrt3}$, both in $(-1,1)$.

**D2.** MVT for $\sqrt x$ on $[4,9]$: average $=\frac{3-2}{9-4}=\frac15$. $f'(c)=\frac{1}{2\sqrt c}=\frac15$ → $\sqrt c=\frac52$ → $c=\frac{25}{4}=6.25$.

**D3.** $x^5+2x-1$: $f(0)=-1$, $f(1)=2$ → root by IVT. $f'=5x^4+2>0$ → strictly increasing → unique root.

**D4.** $\int_1^4 3x^2\,dx=[x^3]_1^4=64-1=63$.

**D5.** $\frac{d}{dx}\int_0^{x^2}\sin(t^2)\,dt=\sin((x^2)^2)\cdot 2x=2x\sin(x^4)$ (FTC1 + chain rule).

**D6.** $\ln(1+x)$ at $0$: $f(0)=0$, $f'(0)=1$, $f''(0)=-1$ → $P_2(x)=x-\frac{x^2}{2}$.

**D7.** $e^{0.3}$ with $P_2$: $|R_2|\leq\frac{e^{0.3}}{6}(0.3)^3\approx\frac{1.3499}{6}\cdot0.027\approx0.00607$.

**D8.** Cauchy MVT: if $f,g$ continuous on $[a,b]$, differentiable on $(a,b)$, $g'\neq0$, then $\exists c$ with $\frac{f'(c)}{g'(c)}=\frac{f(b)-f(a)}{g(b)-g(a)}$. With $g(x)=x$: $g'(c)=1$, $g(b)-g(a)=b-a$ → $\frac{f'(c)}{1}=\frac{f(b)-f(a)}{b-a}$ — that's MVT. ✓

**D9.** $f'=0$ ⇒ constant: for any $x_1<x_2$, MVT gives $f(x_2)-f(x_1)=f'(c)(x_2-x_1)=0$ → all values equal. ✓

**D10.** $|\sin x-x|\leq|x|^3/6$: Taylor $n=2$ at $0$: $\sin x = x + R_2(x)$ where $R_2(x)=\frac{f'''(ξ)}{3!}x^3=-\frac{\cos ξ}{6}x^3$. So $|\sin x-x|=|R_2|\leq\frac{1}{6}|x|^3$. ✓

> **Answers**: D1 $c=\pm1/\sqrt3$; D2 $c=25/4$; D4 $63$; D5 $2x\sin(x^4)$; D6 $x-\frac{x^2}{2}$; D7 $\approx0.00607$; D10 via Taylor remainder.

---

## Advanced Drills

### A1. Cauchy MVT
$h(x)=[f(b)-f(a)]g(x)-[g(b)-g(a)]f(x)$ is continuous on $[a,b]$, differentiable on $(a,b)$.
$h(a)=[f(b)-f(a)]g(a)-[g(b)-g(a)]f(a)$;
$h(b)=[f(b)-f(a)]g(b)-[g(b)-g(a)]f(b)$.
$h(a)-h(b)=[f(b)-f(a)](g(a)-g(b))-[g(b)-g(a)](f(a)-f(b))=[f(b)-f(a)](g(a)-g(b))+[g(b)-g(a)](f(b)-f(a))=0$. So $h(a)=h(b)$. By Rolle, $\exists c$ with $h'(c)=0$:
$[f(b)-f(a)]g'(c)-[g(b)-g(a)]f'(c)=0$ → $\frac{f'(c)}{g'(c)}=\frac{f(b)-f(a)}{g(b)-g(a)}$. ✓

### A2. L'Hôpital (0/0) via Cauchy MVT
$f(a)=g(a)=0$. For $x$ near $a$ ($x>a$), apply Cauchy MVT on $[a,x]$: $\frac{f(x)}{g(x)}=\frac{f(x)-f(a)}{g(x)-g(a)}=\frac{f'(c_x)}{g'(c_x)}$ with $c_x$ between $a$ and $x$. As $x\to a$, $c_x\to a$, and $\frac{f'(c_x)}{g'(c_x)}\to L$ by hypothesis. So $\lim_{x\to a}\frac{f(x)}{g(x)}=L$. ✓

### A3. $f''>0$ ⇒ convex
Let $x<y$, $t\in(0,1)$, $z=tx+(1-t)y$. By MVT: $f(z)-f(x)=f'(c_1)(z-x)$ and $f(y)-f(z)=f'(c_2)(y-z)$ with $x<c_1<z<c_2<y$. Since $f''>0$, $f'$ is increasing, so $f'(c_1)<f'(c_2)$. Hence $\frac{f(z)-f(x)}{z-x}<\frac{f(y)-f(z)}{y-z}$. Cross-multiplying (all denominators positive) and using $z-x=t(y-x)$, $y-z=(1-t)(y-x)$ gives $f(z)\leq(1-t)f(x)+t f(y)$ — the secant lies above the graph. ✓

### A4. Integral Mean Value Theorem
$f$ continuous on $[a,b]$ → EVT gives $m=\min f$, $M=\max f$ on $[a,b]$. So $m(b-a)\leq\int_a^b f\leq M(b-a)$, hence $m\leq\frac{1}{b-a}\int_a^b f\leq M$. By IVT, $\exists c$ with $f(c)=\frac{1}{b-a}\int_a^b f$, i.e. $\int_a^b f=f(c)(b-a)$. ✓

### A5. FTC Part 1, left-hand limit
For $h<0$, write $k=-h>0$: $\frac{F(x-k)-F(x)}{-k}=\frac{1}{k}\int_{x-k}^{x}f(t)\,dt$. EVT on $[x-k,x]$: $m_k k\leq\int_{x-k}^{x}f\leq M_k k$, so $m_k\leq\frac{1}{k}\int_{x-k}^{x}f\leq M_k$. As $k\to0^+$, continuity gives $m_k,M_k\to f(x)$; squeeze gives the middle $\to f(x)$. So $F'(x)=f(x)$ from the left too. ✓

### A6. Taylor $n=1$ via integration by parts
$f(x)-f(a)=\int_a^x f'(t)\,dt$. Since $f'(t)=-\frac{d}{dt}(x-t)$, integrate by parts:
$\int_a^x f'(t)\,dt=[-f'(t)(x-t)]_a^x+\int_a^x f''(t)(x-t)\,dt=f'(a)(x-a)+\int_a^x f''(t)(x-t)\,dt$.
Apply the integral MVT to the remainder: $\int_a^x f''(t)(x-t)\,dt=f''(\xi)\int_a^x(x-t)\,dt=f''(\xi)\frac{(x-a)^2}{2}$ (the weight $(x-t)\geq0$ on $[a,x]$). So $f(x)=f(a)+f'(a)(x-a)+\frac{f''(\xi)}{2}(x-a)^2$. ✓

### A7. Uniqueness of Taylor polynomials
$P-Q$ is a polynomial of degree $\leq n$ and $\lim_{x\to a}\frac{P(x)-Q(x)}{(x-a)^n}=0$. Write $P-Q=\sum_{k=0}^n c_k(x-a)^k$. Then $\lim_{x\to a}\frac{P-Q}{(x-a)^n}=c_n$ (all lower terms vanish). So $c_n=0$; removing the top term and repeating gives $c_{n-1}=\cdots=c_0=0$. Hence $P=Q$. ✓

### A8. $f'=f$, $f(0)=1$ ⇒ $f=e^x$
Let $g(x)=f(x)e^{-x}$. $g'(x)=f'(x)e^{-x}-f(x)e^{-x}=e^{-x}(f'(x)-f(x))=0$ for all $x$. By MVT Corollary 1, $g$ is constant; $g(0)=f(0)e^0=1$. So $g(x)=1$ → $f(x)=e^x$. ✓

### A9. Second derivative test via Taylor
$f'(a)=0$, $f''(a)>0$. Taylor to degree 2: $f(x)=f(a)+\frac{f''(\xi)}{2}(x-a)^2$ for $\xi$ between $a$ and $x$. Since $f''$ is continuous and $f''(a)>0$, for $x$ close to $a$ we have $f''(\xi)>0$. Hence $f(x)-f(a)=\frac{f''(\xi)}{2}(x-a)^2>0$ for $x\neq a$ near $a$ — a strict local minimum. ✓

### A10. Find the flaw in "all functions are constant"
MVT gives $f(x)-f(y)=f'(c)(x-y)$ for *some* $c$ between $x$ and $y$. The "proof" then lets $y\to x$: $x-y\to0$, so $f(x)-f(y)\to0$, "hence $f(x)=f(y)$." The flaw: $f(x)-f(y)\to0$ as $y\to x$ is just **continuity** — every continuous function satisfies it. It does not make $f(x)$ and $f(y)$ *equal*; it makes them *close*. Concluding $f(x)=f(y)$ for all $x,y$ requires the difference to be exactly $0$, which MVT's formula (with $c$ depending on $x,y$) never gives. The argument proves nothing beyond continuity.
