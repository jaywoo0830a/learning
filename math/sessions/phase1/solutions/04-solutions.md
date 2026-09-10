# Solutions — 04: The Domino Proof — Mathematical Induction
## Basic Drills

**D1.** $1+2+\cdots+n = \frac{n(n+1)}{2}$: base $1 = 1\cdot2/2$ ✓. Step: add $k+1$ to $\frac{k(k+1)}{2}$ → $\frac{(k+1)(k+2)}{2}$ ✓.
**D2.** $3+6+\cdots+3n = \frac{3n(n+1)}{2}$: base $3 = 3\cdot1\cdot2/2$ ✓. Step: add $3(k+1)$ → $\frac{3(k+1)(k+2)}{2}$ ✓.
**D3.** $2+4+\cdots+2n = n(n+1)$: base $2=1\cdot2$ ✓. Step: add $2(k+1)$ → $(k+1)(k+2)$ ✓.
**D4.** $1+2+4+\cdots+2^{n-1} = 2^n - 1$: base $1 = 2^1-1$ ✓. Step: add $2^k$ → $(2^k-1)+2^k = 2^{k+1}-1$ ✓.
**D5.** $n < 2^n$: base $1<2$ ✓. Step: $k+1 < 2k < 2\cdot 2^k = 2^{k+1}$ (using $k+1\le 2k$ for $k\ge1$) ✓.
**D6.** $3^n \geq 2n+1$: base $3 \geq 3$ ✓. Step: $3^{k+1} = 3\cdot 3^k \geq 3(2k+1) = 6k+3 \geq 2k+3 = 2(k+1)+1$ ✓.
**D7.** $n^2 \geq n$: base $1 \geq 1$ ✓. Step: $(k+1)^2 = k^2+2k+1 \geq k+2k+1 > k+1$ ✓.
**D8.** $2n+1 < 2^n$ for $n\geq3$: base $n=3$: $7 < 8$ ✓. Step: $2(k+1)+1 = 2k+3 < 2\cdot 2^k = 2^{k+1}$ (since $2k+3 < 2\cdot(2k+1)$ for $k\ge3$) ✓.
**D9.** $n^3-n$ divisible by 6: base $n=1$: $0$ ✓. Step: $(k+1)^3-(k+1) = (k^3-k)+3k(k+1)$. By hypothesis $6\mid(k^3-k)$; and $k(k+1)$ is even, so $6\mid 3k(k+1)$. Sum divisible by 6 ✓.
**D10.** The hypothesis is used when we replace $1+2+\cdots+k$ by $\frac{k(k+1)}{2}$ before adding $k+1$.

---

## Advanced Drills

### A1. $F_n \geq 2^{n/2}$ for $n \geq 6$
Base $n=6$: $F_6 = 8 = 2^3$ ✓; $n=7$: $F_7 = 13 > 2^{3.5}\approx 11.3$ ✓.
Step: $F_{n+1} = F_n + F_{n-1} \geq 2^{n/2} + 2^{(n-1)/2} = 2^{(n-1)/2}(1+\sqrt{2}) > 2^{(n-1)/2}\cdot 2 = 2^{(n+1)/2}$ ✓ (since $1+\sqrt2 > 2$).

### A2. Every integer $n \geq 2$ has a prime factor
Base $n=2$: 2 is prime. Strong step: if $k+1$ prime, done; if composite, $k+1 = ab$ with $2\leq a,b \leq k$; by strong hypothesis $a$ has a prime factor, which divides $k+1$ ✓.

### A3. $2^n \times 2^n$ board minus one square, L-tromino tiling
Index the argument by $n$: base $n=1$, split into four quadrants, central L, four recursive tilings.

### A4. Postage $\geq 8$ with 3- and 5-cent stamps
Base: $8=3+5$, $9=3+3+3$, $10=5+5$. Step: if $n$ is payable, then $n+3$ is payable (add one 3¢ stamp). Since every $n\geq 8$ differs from 8, 9, or 10 by a multiple of 3, all $n\geq8$ are covered ✓.

### A5. $1^3+2^3+\cdots+n^3 = \left(\frac{n(n+1)}{2}\right)^2$
Base $n=1$: $1 = 1^2$ ✓. Step: add $(k+1)^3$ to $\left(\frac{k(k+1)}{2}\right)^2$:
$= \frac{k^2(k+1)^2}{4} + (k+1)^3 = \frac{(k+1)^2(k^2 + 4k + 4)}{4} = \frac{(k+1)^2(k+2)^2}{4} = \left(\frac{(k+1)(k+2)}{2}\right)^2$ ✓.

### A6. $1\cdot2 + 2\cdot3 + \cdots + n(n+1) = \frac{n(n+1)(n+2)}{3}$
Base $n=1$: $2 = \frac{1\cdot2\cdot3}{3}$ ✓. Step: add $(k+1)(k+2)$:
$\frac{k(k+1)(k+2)}{3} + (k+1)(k+2) = (k+1)(k+2)\left(\frac{k}{3}+1\right) = \frac{(k+1)(k+2)(k+3)}{3}$ ✓.

### A7. $a_1 = 2$, $a_{n+1} = a_n + 2n + 1$ → $a_n = n^2 + 1$
Base $n=1$: $a_1 = 2 = 1^2+1$ ✓. Step: $a_{k+1} = a_k + 2k+1 = (k^2+1) + 2k+1 = k^2+2k+2 = (k+1)^2 + 1$ ✓.

### A8. Every $n$ is a sum of distinct powers of 2
Base $n=1$: $1 = 2^0$ ✓. Strong step: if $k+1$ is a power of 2, done. Otherwise $2^m < k+1 < 2^{m+1}$ for some $m$; then $k+1 - 2^m < 2^m$, so by strong hypothesis it's a sum of distinct powers $< 2^m$; add $2^m$ ✓.

### A9. $\sum_{i=1}^{n} \frac{1}{i(i+1)} = \frac{n}{n+1}$
Base $n=1$: $\frac{1}{2} = \frac{1}{2}$ ✓. Step: $\frac{k}{k+1} + \frac{1}{(k+1)(k+2)} = \frac{k(k+2)+1}{(k+1)(k+2)} = \frac{(k+1)^2}{(k+1)(k+2)} = \frac{k+1}{k+2}$ ✓.

### A10. Tower of Hanoi needs $2^n - 1$ moves for $n$ disks
Base $n=1$: 1 move = $2^1-1$ ✓. Step: to move $n+1$ disks: move top $n$ off (needs $2^n-1$ by hypothesis), move the big disk (1 move), move the $n$ back on ($2^n-1$). Total $2(2^n-1)+1 = 2^{n+1}-1$ ✓.
