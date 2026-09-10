# Solutions — 02: Handling "All" and "Some" — Quantifiers
## Basic Drills

**D1.** $\forall n\,(n \geq 0)$ over $\mathbb{N}$ → **True** (every natural is $\geq 0$).
**D2.** $\forall n\,(n$ multiple of 3) over $\mathbb{N}$ → **False** ($n=1$ is a counterexample).
**D3.** $\exists n\,(n > 1000)$ over $\mathbb{N}$ → **True** ($n=1001$).
**D4.** $\exists n\,(n < 0)$ over $\mathbb{N}$ → **False** (no negative natural).
**D5.** $\forall x\,(x^2 \geq 0)$ over $\mathbb{R}$ → **True**.
**D6.** $\exists x\,(x^2 = -1)$ over $\mathbb{R}$ → **False**.
**D7.** Negate "all students passed" → **"some student failed"** ($\exists$ one failure).
**D8.** Negate "some planet is habitable" → **"no planet is habitable"** (every planet is not habitable).
**D9.** $\neg\forall x\,(x>0)$ over $\mathbb{Z}$ → $\exists x\,(x\leq 0)$ → **True** ($x=0$).
**D10.** $\neg\exists n\,(n$ prime) over $\mathbb{N}$ → $\forall n\,(n$ not prime) → **False** (2 is prime).

> **Answers**: D1 T, D2 F, D3 T, D4 F, D5 T, D6 F, D7 "some failed", D8 "none habitable", D9 T, D10 F.

---

## Advanced Drills

### A1. $\forall x\,\exists y\,(x + y = 0)$ over $\mathbb{Z}$
For each $x$ choose $y = -x$ (which is an integer). → **True.**

### A2. $\exists y\,\forall x\,(x + y = 0)$ over $\mathbb{Z}$
One fixed $y$ would need $x+y=0$ for *every* $x$ — impossible. → **False.**

### A3. $\forall x\,\exists y\,(x < y)$ over $\mathbb{R}$
For each $x$ choose $y = x+1$. → **True** (reals have no top).

### A4. $\exists y\,\forall x\,(x < y)$ over $\mathbb{R}$
One $y$ larger than every real — no such largest real. → **False.**

### A5. $\exists x\,\forall y\,(x + y = 0)$ over $\mathbb{R}$, and its negation
Original: one $x$ with $x+y=0$ for all $y$ — impossible → **False.** Negation: $\forall x\,\exists y\,(x+y \neq 0)$ → **True** (e.g., $y=1$ fails for each $x$: $x+1\neq 0$ when $x\neq-1$… more carefully: for any $x$, pick $y$ such that $x+y\neq 0$, e.g., $y=1-x$ always gives $x+y=1\neq0$).

### A6. $\neg\big(\forall\varepsilon\,\exists\delta\,P(\varepsilon,\delta)\big)$
Flip each quantifier and negate the property: **$\exists\varepsilon\,\forall\delta\,\neg P(\varepsilon,\delta)$**.

### A7. $\forall n\,(n$ even $\lor$ $n$ odd) over $\mathbb{N}$
Every natural is even or odd → **True.**

### A8. Domain $\{1,2,3\}$, $P(x)$ = "$x$ is a factor of 6"
All of $1,2,3$ divide 6 → $\forall x\,P(x)$ **True**; $\exists x\,P(x)$ **True.**

### A9. "There is a largest natural number" and its negation
Symbols: $\exists m\,\forall n\,(n \leq m)$. Negation: $\forall m\,\exists n\,(n > m)$ — for every $m$ there's a bigger $n$ ($n=m+1$) → **True** (so the original is false; no largest natural).

### A10. $\forall x\,\exists y\,L(x,y)$ vs $\exists y\,\forall x\,L(x,y)$
First: "every person has someone they like." Second: "there is a person everyone likes."
Example where first true, second false — people A, B, C with $L$: A likes B, B likes C, C likes A (a cycle). Every person likes someone ✓; no single person is liked by everyone ✗.

> **Answers**: A1 T, A2 F, A3 T, A4 F, A5 original F / negation T, A6 $\exists\varepsilon\forall\delta\neg P$, A7 T, A8 both T, A9 negation T, A10 cycle example.
