# Solutions — 03: Three Proof Templates — Direct, Contrapositive, Contradiction
## Basic Drills

**D1.** $n$ even → $3n$ even: $n=2k$ → $3n=6k=2(3k)$. ✓ Direct.
**D2.** $n$ odd → $n^2$ odd: $n=2k+1$ → $n^2=4k^2+4k+1=2(2k^2+2k)+1$. ✓ Direct.
**D3.** $n^2$ even → $n$ even: contrapositive. $n$ odd → $n^2$ odd (D2). ✓
**D4.** $5n+1$ even → $n$ odd: contrapositive. $n$ even → $n=2k$ → $5n+1=10k+1=2(5k)+1$ odd. ✓
**D5.** $n$ even → $n^2$ divisible by 4: $n=2k$ → $n^2=4k^2$. ✓
**D6.** Product of two evens is even: $a=2k$, $b=2m$ → $ab=4km=2(2km)$. ✓
**D7.** Sum of two odds is even: $a=2k+1$, $b=2m+1$ → $a+b=2(k+m+1)$. ✓
**D8.** $\sqrt{5}$ irrational: $\sqrt{5}=a/b$ reduced → $a^2=5b^2$ → $a$ mult of 5 → $a=5k$ → $25k^2=5b^2$ → $b^2=5k^2$ → $b$ mult of 5. Both mult of 5 → not reduced. Contradiction. ✓
**D9.** No largest integer: assume $M$ is largest → $M+1 > M$ is an integer — contradiction. ✓
**D10.** $a<b$ → $a<\frac{a+b}{2}<b$: $2a<a+b<2b$ (add $a<b$ to itself; and $a<b$ gives $a+b<2b$). Divide by 2. ✓

---

## Advanced Drills

### A1. $n$ odd → $n^3$ odd
Direct. Chosen because the odd form $2k+1$ cubes cleanly.

### A2. $n^2$ multiple of 5 → $n$ multiple of 5
Contrapositive, four cases: $n=5k+1,5k+2,5k+3,5k+4$. Squaring each gives remainder $1,4,4,1$ mod 5 respectively — never 0. So $n^2$ not a multiple of 5.

### A3. $n!+1$ has a prime factor greater than $n$
$n!+1 > 1$, so it has some prime factor $p$. If $p \leq n$, then $p$ divides $n!$ (it's one of the factors) and $p$ divides $n!+1$, so $p$ divides their difference $1$ — impossible. Hence $p > n$.

### A4. $\sqrt{6}$ is irrational
Assume $\sqrt{6}=a/b$ reduced. $a^2=6b^2$ → $a^2$ even → $a$ even → $a=2k$ → $4k^2=6b^2$ → $2k^2=3b^2$. LHS even → $3b^2$ even → $b^2$ even → $b$ even. Both even → not reduced. Contradiction.

### A5. $a,b$ odd → $a^2+b^2$ even but not divisible by 4
$a=2m+1$, $b=2n+1$: $a^2+b^2 = (4m^2+4m+1)+(4n^2+4n+1) = 4(m^2+m+n^2+n)+2$. Even, with remainder 2 mod 4 → not divisible by 4.

### A6. Rational − irrational = irrational
Suppose $r - i = q$ rational → $i = r - q$ rational — contradiction.

### A7. $x$ irrational → $1/x$ irrational ($x\neq 0$)
Suppose $1/x = q$ rational → $x = 1/q$ rational ($q\neq 0$) — contradiction.

### A8. $\sqrt{2}+\sqrt{3}$ irrational
Suppose $r = \sqrt{2}+\sqrt{3}$ rational. Square: $r^2 = 5 + 2\sqrt{6}$ → $\sqrt{6} = (r^2-5)/2$ rational — contradicts A4.

### A9. $a\mid b$ and $b\mid c$ → $a\mid c$
$b = ak$, $c = bl$ → $c = a(kl)$ with $kl$ an integer → $a\mid c$.

### A10. Among 3 consecutive integers exactly one is a multiple of 3; and $n^3-n$ divisible by 3
$n, n+1, n+2$ have residues $0,1,2$ mod 3 in some order — exactly one is $0$ mod 3.
Then $n^3 - n = n(n-1)(n+1)$, the product of three consecutive integers → divisible by 3.
