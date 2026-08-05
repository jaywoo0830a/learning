# Solutions — 03: Three Proof Templates — Direct, Contrapositive, Contradiction

---

## Practice 1

**Prove "if $n$ is odd, then $n^3$ is odd"** — direct proof.

Assume $n$ odd: $n = 2k+1$, $k$ integer.
$n^3 = (2k+1)^3 = 8k^3 + 12k^2 + 6k + 1 = 2(4k^3 + 6k^2 + 3k) + 1$.
$4k^3+6k^2+3k$ is an integer, so $n^3 = 2(\text{int}) + 1$ → odd.

> **Answer**: Direct proof — written $n=2k+1$, cubed, factored out the 2.

---

## Practice 2

**Prove "if $3n+2$ is even, then $n$ is even"** — contrapositive.

Contrapositive: "if $n$ is odd, then $3n+2$ is odd." Assume $n = 2k+1$.
$3n+2 = 3(2k+1)+2 = 6k+5 = 2(3k+2)+1$ → odd.

> **Answer**: Contrapositive proved — original follows.

---

## Practice 3

**Prove "if $n^2$ is a multiple of 3, then $n$ is a multiple of 3."**

**Template choice**: contrapositive — "not a multiple of 3" is easy to write as two cases; "$n^2$ multiple of 3" is awkward to handle directly.

Contrapositive: if $n$ is not a multiple of 3, then $n^2$ is not a multiple of 3.
- $n = 3k+1$: $n^2 = 9k^2+6k+1 = 3(3k^2+2k)+1$ → remainder 1, not a multiple of 3.
- $n = 3k+2$: $n^2 = 9k^2+12k+4 = 3(3k^2+4k+1)+1$ → remainder 1, not a multiple of 3.

> **Answer**: Contrapositive, two cases ($n=3k+1$, $n=3k+2$) — both give remainder 1.

---

## Practice 4: Trap

**Prove "$n^2+n$ is even for all integers $n$" without induction.**

Factor: $n^2 + n = n(n+1)$. The numbers $n$ and $n+1$ are consecutive — exactly one of them is even. The product of an even number with anything is even.

> **Answer**: $n(n+1)$ contains an even factor → even.

---

## Practice 5

**Prove "$\sqrt{3}$ cannot be written as a fraction"** — contradiction.

Assume $\sqrt{3} = \frac{a}{b}$ with integers $a,b$, $b\neq 0$, fraction fully reduced (no common factor).

Square: $3 = \frac{a^2}{b^2}$ → $a^2 = 3b^2$. So $a^2$ is a multiple of 3 → by Practice 3, $a$ is a multiple of 3. Write $a = 3k$.

Substitute: $(3k)^2 = 3b^2$ → $9k^2 = 3b^2$ → $b^2 = 3k^2$. So $b^2$ is a multiple of 3 → $b$ is a multiple of 3.

**Contradiction**: $a$ and $b$ are both multiples of 3, so $\frac{a}{b}$ is not fully reduced — but we assumed it was.

> **Answer**: $\sqrt{3}$ is irrational (proof by contradiction, exactly like $\sqrt{2}$).

---

## Practice 6: Real Battle

**Prove "the sum of a rational and an irrational is irrational."**

**Template choice**: contradiction — "not expressible as a fraction" is easiest to attack by assuming the opposite.

Assume $a$ rational, $b$ irrational, and suppose $a+b$ is rational. Then $b = (a+b) - a$ is a difference of two rationals — rational. But $b$ is irrational. Contradiction.

> **Answer**: Contradiction. $a+b$ rational would force $b$ rational, contradicting the hypothesis.

---

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
Direct (Practice 1). Chosen because the odd form $2k+1$ cubes cleanly.

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
