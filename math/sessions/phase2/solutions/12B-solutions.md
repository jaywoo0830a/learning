# 12B Solutions — Sequences and Series

---

## Practice 1

> 20th term and sum of first 20 terms of 5, 9, 13, 17, ...

(1) $a_1 = 5$, $d = 4$.
(2) $a_{20} = 5 + 19\cdot4 = 5 + 76 = 81$.
(3) $S_{20} = \frac{20(5+81)}{2} = 10 \cdot 86 = 860$.
→ **$a_{20} = 81$, $S_{20} = 860$.**

---

## Practice 2

> Sum of first 8 terms of 3, 6, 12, 24, ...

(1) $a_1 = 3$, $r = 2$.
(2) $S_8 = 3 \cdot \frac{1-2^8}{1-2} = 3 \cdot \frac{1-256}{-1} = 3 \cdot 255 = 765$.
→ **$S_8 = 765$.**

---

## Practice 3

> $5 + \frac{5}{3} + \frac{5}{9} + \frac{5}{27} + \cdots$

(1) $a_1 = 5$, $r = \frac{1}{3}$. $|r| < 1$, so the infinite sum converges.
(2) $S_\infty = \frac{5}{1 - \frac{1}{3}} = \frac{5}{\frac{2}{3}} = \frac{15}{2} = 7.5$.
→ **$S_\infty = \frac{15}{2}$.**

---

## Practice 4: Composition

> A sequence is both arithmetic and geometric. Prove all terms equal.

Let three consecutive terms be $a, b, c$.
Arithmetic: $2b = a + c$.
Geometric: $b^2 = ac$.
Substitute $b = \frac{a+c}{2}$: $(\frac{a+c}{2})^2 = ac$ → $a^2 + 2ac + c^2 = 4ac$ → $a^2 - 2ac + c^2 = 0$ → $(a-c)^2 = 0$ → $a = c$.
Then $b = \frac{a+a}{2} = a$. All three are equal. Extending: every term equals the first term. The only sequences that are both arithmetic and geometric are constant sequences.

Real-world example: a fixed annual fee (no increase, no compounding). A subscription that costs $100 every year forever — the sequence of annual payments is 100, 100, 100, ...

---

## Practice 5

> $\sum_{k=1}^{n} (2k-1) = n^2$ using sigma formulas.

$\sum_{k=1}^{n} (2k-1) = 2\sum_{k=1}^{n} k - \sum_{k=1}^{n} 1 = 2 \cdot \frac{n(n+1)}{2} - n = n(n+1) - n = n^2$.
→ **$n^2$.** (The sum of the first $n$ odd numbers equals $n^2$.)

---

## Practice 6

> $\sum_{k=1}^{20} \frac{1}{k(k+1)}$ (telescoping).

(1) $\frac{1}{k(k+1)} = \frac{1}{k} - \frac{1}{k+1}$.
(2) Sum = $(\frac{1}{1} - \frac{1}{2}) + (\frac{1}{2} - \frac{1}{3}) + \cdots + (\frac{1}{20} - \frac{1}{21})$.
(3) Everything cancels except $\frac{1}{1} - \frac{1}{21} = 1 - \frac{1}{21} = \frac{20}{21}$.
→ **$\frac{20}{21}$.**

---

## Practice 7

> $a_{n+1} = 2a_n + 3$, $a_1 = 1$. Find $a_n$.

(1) Fixed point: $x = 2x + 3$ → $x = -3$.
(2) Subtract $x$: $a_{n+1} + 3 = 2(a_n + 3)$.
(3) Let $b_n = a_n + 3$. $b_{n+1} = 2b_n$, $b_1 = a_1 + 3 = 4$.
(4) $b_n = 4 \cdot 2^{n-1} = 2^{n+1}$.
(5) $a_n = b_n - 3 = 2^{n+1} - 3$.
Check: $n=1$: $2^2-3=1$ ✓. $n=2$: $2^3-3=5$ ✓. $n=3$: $2^4-3=13$ ✓.
→ **$a_n = 2^{n+1} - 3$.**

---

## Practice 8

> Differences: 3, 5, 7, 9, ... First term: 2. Find the 10th term.

(1) Differences: $b_k = 2k+1$ (odd numbers starting from 3).
(2) $a_n = a_1 + \sum_{k=1}^{n-1} (2k+1) = 2 + \sum_{k=1}^{n-1} (2k+1)$.
(3) $\sum_{k=1}^{n-1} (2k+1) = 2\sum_{k=1}^{n-1} k + \sum_{k=1}^{n-1} 1 = 2\cdot\frac{(n-1)n}{2} + (n-1) = n(n-1) + n - 1 = n^2 - 1$.
(4) $a_n = 2 + (n^2-1) = n^2 + 1$.
(5) $a_{10} = 100 + 1 = 101$.
→ **$a_{10} = 101$.**

---

## Practice 9: Composition

> Invent a telescoping sum.

Choose $f(k) = k^2$. Then $f(k+1) - f(k) = (k+1)^2 - k^2 = 2k+1$.

Sum of 10 terms: $\sum_{k=1}^{10} (2k+1) = f(11) - f(1) = 121 - 1 = 120$.

Verify cancellation:
$k=1$: $3 = 4-1$
$k=2$: $5 = 9-4$
...
$k=10$: $21 = 121-100$
Sum = $3+5+7+\cdots+21 = 120$. The middle squares all cancel: $-1+4-4+9-9+\cdots+100-100+121 = 120$.

Any function $f(k)$ generates a telescoping sum via $f(k+1)-f(k)$.

---

## Practice 10

> Prove $\sum_{k=1}^{n} k^3 = (\frac{n(n+1)}{2})^2$ by induction.

Base case ($n=1$): Left = $1^3 = 1$. Right = $(\frac{1\cdot2}{2})^2 = 1^2 = 1$. ✓

Inductive step: Assume $\sum_{k=1}^{m} k^3 = (\frac{m(m+1)}{2})^2$.
For $n = m+1$:
$\sum_{k=1}^{m+1} k^3 = \sum_{k=1}^{m} k^3 + (m+1)^3 = (\frac{m(m+1)}{2})^2 + (m+1)^3$.
Factor $(m+1)^2$: $= (m+1)^2\left[\frac{m^2}{4} + (m+1)\right] = (m+1)^2 \cdot \frac{m^2 + 4m + 4}{4}$.
$= (m+1)^2 \cdot \frac{(m+2)^2}{4} = \left(\frac{(m+1)(m+2)}{2}\right)^2$.
This matches the formula with $n = m+1$. ✓

Therefore the formula holds for all $n \geq 1$.

---

## Practice 11

> $\lim_{n\to\infty} \frac{5n^3 - 2n + 1}{3n^3 + n^2 + 4}$

(1) Divide numerator and denominator by $n^3$:
$\frac{5 - 2/n^2 + 1/n^3}{3 + 1/n + 4/n^3}$.

(2) As $n\to\infty$: $2/n^2 \to 0$, $1/n^3 \to 0$, $1/n \to 0$, $4/n^3 \to 0$.

(3) Limit = $\frac{5 - 0 + 0}{3 + 0 + 0} = \frac{5}{3}$.
→ **$\frac{5}{3}$.**

---

## Practice 12: Real Battle

> Prove $F_1 + F_2 + \cdots + F_n = F_{n+2} - 1$ by induction. Find $\lim F_{n+1}/F_n$.

**Part 1 — Induction proof**:

Base case ($n=1$): $F_1 = 1$. $F_3 - 1 = 2 - 1 = 1$. ✓

Inductive step: Assume $\sum_{k=1}^{m} F_k = F_{m+2} - 1$.
For $n = m+1$:
$\sum_{k=1}^{m+1} F_k = (F_{m+2} - 1) + F_{m+1} = F_{m+2} + F_{m+1} - 1$.
Since $F_{m+2} + F_{m+1} = F_{m+3}$ (Fibonacci recurrence),
$= F_{m+3} - 1 = F_{(m+1)+2} - 1$. This matches the formula with $n = m+1$. ✓

**Part 2 — Limit of the ratio**:

Binet's formula: $F_n = \frac{\phi^n - \psi^n}{\sqrt{5}}$, where $\phi = \frac{1+\sqrt{5}}{2} \approx 1.618$, $\psi = \frac{1-\sqrt{5}}{2} \approx -0.618$.

$\frac{F_{n+1}}{F_n} = \frac{\phi^{n+1} - \psi^{n+1}}{\phi^n - \psi^n}$.
As $n\to\infty$, $|\psi| < 1$, so $\psi^n \to 0$.
$\frac{F_{n+1}}{F_n} \to \frac{\phi^{n+1}}{\phi^n} = \phi = \frac{1+\sqrt{5}}{2}$, the golden ratio.
→ **$\phi = \frac{1+\sqrt{5}}{2} \approx 1.618$.**

---

## Basic Drill

### D1. 15th term of 4, 10, 16, 22, ...
$a_1 = 4$, $d = 6$. $a_{15} = 4 + 14\cdot6 = 4 + 84 = 88$. → **88.**

### D2. Sum of first 12 terms of 2, -4, 8, -16, ...
$a_1 = 2$, $r = -2$. $S_{12} = 2\cdot\frac{1-(-2)^{12}}{1-(-2)} = 2\cdot\frac{1-4096}{3} = 2\cdot\frac{-4095}{3} = 2\cdot(-1365) = -2730$. → **$-2730$.**

### D3. $0.555\ldots$ as a fraction
$0.555\ldots = \frac{5}{10} + \frac{5}{100} + \frac{5}{1000} + \cdots$. $a_1 = \frac{5}{10}$, $r = \frac{1}{10}$.
$S_\infty = \frac{5/10}{1-1/10} = \frac{5/10}{9/10} = \frac{5}{9}$. → **$\frac{5}{9}$.**

### D4. $\sum_{k=1}^{50} k$
$\sum_{k=1}^{50} k = \frac{50\cdot51}{2} = 1275$. → **1275.**

### D5. $\sum_{k=1}^{8} k^2$
$\sum_{k=1}^{8} k^2 = \frac{8\cdot9\cdot17}{6} = \frac{1224}{6} = 204$. → **204.**

### D6. $S_n = 3n^2 + n$. Find $a_5$.
$a_5 = S_5 - S_4 = (3\cdot25 + 5) - (3\cdot16 + 4) = (75+5) - (48+4) = 80 - 52 = 28$.
→ **28.**

### D7. Type of sequence: $\frac{1}{3}, \frac{1}{7}, \frac{1}{11}, \frac{1}{15}, \dots$
Denominators: 3, 7, 11, 15, ... — arithmetic with $d = 4$. Reciprocals form an AP → **harmonic sequence.**

### D8. $\sum_{k=1}^{6} (k^3 - k)$
$\sum k^3 - \sum k = (\frac{6\cdot7}{2})^2 - \frac{6\cdot7}{2} = 21^2 - 21 = 441 - 21 = 420$.
→ **420.**

### D9. Sum of first 20 terms of $7, 12, 17, 22, \dots$
$a_1=7$, $d=5$, $a_{20} = 7+19\cdot5 = 102$.
$S_{20} = \frac{20(7+102)}{2} = 10\cdot109 = 1090$.
→ **1090.**

### D10. Infinite sum $8 + 4 + 2 + 1 + \frac{1}{2} + \cdots$
$a_1=8$, $r=\frac{1}{2}$. $S_\infty = \frac{8}{1-\frac{1}{2}} = 16$.
→ **16.**

---

## Advanced Drill

### A1. $a_1=3$, $a_{n+1}=a_n+2n$. Find $a_{20}$.
(1) Differences: $b_k = 2k$ for $k=1$ to $n-1$.
(2) $a_n = a_1 + \sum_{k=1}^{n-1} 2k = 3 + 2\cdot\frac{(n-1)n}{2} = 3 + n(n-1)$.
(3) $a_{20} = 3 + 20\cdot19 = 3 + 380 = 383$.
→ **383.**

### A2. $a_{n+1}=4a_n-3$, $a_1=2$. General term.
(1) Fixed point: $x = 4x - 3$ → $x = 1$.
(2) $a_{n+1} - 1 = 4(a_n - 1)$. Let $b_n = a_n - 1$, $b_{n+1} = 4b_n$, $b_1 = 1$.
(3) $b_n = 1 \cdot 4^{n-1} = 4^{n-1}$.
(4) $a_n = b_n + 1 = 4^{n-1} + 1$.
→ **$a_n = 4^{n-1} + 1$.**

### A3. $\sum_{k=1}^{n} \frac{1}{(2k-1)(2k+1)}$ via telescoping.
(1) Partial fractions: $\frac{1}{(2k-1)(2k+1)} = \frac{1}{2}\left(\frac{1}{2k-1} - \frac{1}{2k+1}\right)$.
(2) Sum: $\frac{1}{2}\left[(\frac{1}{1} - \frac{1}{3}) + (\frac{1}{3} - \frac{1}{5}) + \cdots + (\frac{1}{2n-1} - \frac{1}{2n+1})\right]$.
(3) All middle terms cancel. Remainder: $\frac{1}{2}(1 - \frac{1}{2n+1}) = \frac{1}{2} \cdot \frac{2n}{2n+1} = \frac{n}{2n+1}$.
→ **$\frac{n}{2n+1}$.**

### A4. Infinite GP: $S_\infty=12$, $a_2=3$. Find $a_1$ and $r$.
(1) $S_\infty = \frac{a_1}{1-r} = 12$. $a_2 = a_1 r = 3$.
(2) From $a_1 r = 3$: $a_1 = \frac{3}{r}$. Substitute into the sum:
$\frac{3/r}{1-r} = 12$ → $\frac{3}{r(1-r)} = 12$ → $3 = 12r(1-r)$ → $12r^2 - 12r + 3 = 0$.
(3) Divide by 3: $4r^2 - 4r + 1 = 0$ → $(2r-1)^2 = 0$ → $r = \frac{1}{2}$.
(4) $a_1 = \frac{3}{1/2} = 6$.
→ **$a_1 = 6$, $r = \frac{1}{2}$.**

### A5. Prove by induction: $\sum_{k=1}^{n} k(k+1) = \frac{n(n+1)(n+2)}{3}$.
Base ($n=1$): Left = $1\cdot2 = 2$. Right = $\frac{1\cdot2\cdot3}{3} = 2$. ✓

Assume true for $n=m$. For $n=m+1$:
$\sum_{k=1}^{m+1} k(k+1) = \frac{m(m+1)(m+2)}{3} + (m+1)(m+2)$.
$= (m+1)(m+2)\left[\frac{m}{3} + 1\right] = (m+1)(m+2) \cdot \frac{m+3}{3} = \frac{(m+1)(m+2)(m+3)}{3}$.
Matches the formula. ✓

### A6. Grouped sequence $(1,2),(3,4,5),(6,7,8,9),\dots$. 15th group.
(1) Numbers before group 15: $1+2+\cdots+14 = \frac{14\cdot15}{2} = 105$.
(2) First of group 15: $1 + 105 = 106$.
(3) Last of group 15: $\frac{15\cdot16}{2} = 120$.
→ **First = 106, Last = 120.**

### A7. $\lim_{n\to\infty} (\sqrt{n^2 + 3n} - n)$
(1) Rationalize: multiply by $\frac{\sqrt{n^2+3n} + n}{\sqrt{n^2+3n} + n}$:
$= \frac{(n^2+3n) - n^2}{\sqrt{n^2+3n} + n} = \frac{3n}{\sqrt{n^2+3n} + n}$.
(2) Divide numerator and denominator by $n$: $\frac{3}{\sqrt{1 + 3/n} + 1}$.
(3) As $n\to\infty$, $3/n \to 0$. Limit = $\frac{3}{\sqrt{1+0}+1} = \frac{3}{2}$.
→ **$\frac{3}{2}$.**

### A8. $a_1=1$, each term = sum of all previous. Find $a_n$.
(1) Compute: $a_1=1$, $a_2=1$, $a_3=2$, $a_4=4$, $a_5=8$, ...
(2) Pattern: $a_n = 2^{n-2}$ for $n \geq 2$, with $a_1 = 1$. Equivalently: $a_n = 2^{n-2}$ for $n \geq 2$.
(3) Prove by induction: Base $n=2$: $a_2 = 1 = 2^{0}$ ✓.
Assume $a_k = 2^{k-2}$ for $2 \leq k \leq m$. Then $a_{m+1} = \sum_{k=1}^{m} a_k = 1 + \sum_{k=2}^{m} 2^{k-2} = 1 + (2^{m-1} - 1) = 2^{m-1}$. Matches the pattern for $n=m+1$. ✓
→ **$a_1 = 1$, $a_n = 2^{n-2}$ for $n \geq 2$.**

### A9. $\sum_{k=1}^{n} k(k+1) = \sum (k^2 + k)$
$= \sum k^2 + \sum k = \frac{n(n+1)(2n+1)}{6} + \frac{n(n+1)}{2}$.
$= n(n+1)\left[\frac{2n+1}{6} + \frac{1}{2}\right] = n(n+1)\cdot\frac{2n+1+3}{6} = \frac{n(n+1)(n+2)}{3}$.
→ **$\frac{n(n+1)(n+2)}{3}$.**

### A10. Prove $\sum_{k=1}^{n} F_k = F_{n+2} - 1$ by induction.
Base $n=1$: $F_1 = 1$. $F_3 - 1 = 2 - 1 = 1$. ✓
Assume $\sum_{k=1}^{m} F_k = F_{m+2} - 1$.
Then $\sum_{k=1}^{m+1} F_k = (F_{m+2} - 1) + F_{m+1} = F_{m+2} + F_{m+1} - 1 = F_{m+3} - 1$.
This matches the formula with $n = m+1$. ✓ Proved.

---

[Back to Table of Contents](../12B-sequences-series.md)
