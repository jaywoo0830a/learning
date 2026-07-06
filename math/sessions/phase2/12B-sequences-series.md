# Session 12B: Sequences and Series — Patterns That Stretch to Infinity

**Phase 2 — Classical Techniques | 120 min**

---

## Part A: Arithmetic and Geometric Sequences — The Two Pillars

---

## Example 1: Arithmetic Sequence — Add the Same Number Each Step

Start at 3. Add 2 each time.
Write out the first few terms: 3, 5, 7, 9, 11, 13, ...

**Finding the $n$th term — three steps:**
(1) Identify the first term $a_1$. → 3.
(2) Identify the common difference $d$ (the number added each step). → 2.
(3) Count how many times $d$ was added to reach term $n$. → $n-1$ times.
The $n$th term: $a_n = a_1 + (n-1)d$.

10th term: $3 + 9 \times 2 = 3 + 18 = 21$.
100th term: $3 + 99 \times 2 = 201$.

**Sum of the first $n$ terms — two equivalent formulas:**
Method 1 — pair first and last: $S_n = \frac{n(a_1 + a_n)}{2}$.
Method 2 — use $a_1$ and $d$ directly: $S_n = \frac{n}{2}[2a_1 + (n-1)d]$.

Sum of first 10 terms:
$S_{10} = \frac{10(3+21)}{2} = \frac{10 \cdot 24}{2} = 120$.
Check by adding manually: $3+5+7+9+11+13+15+17+19+21 = 120$. Matches perfectly.

---

## Example 2: Geometric Sequence — Multiply by the Same Number Each Step

Start at 2. Multiply by 3 each time.
Write out the first few terms: 2, 6, 18, 54, 162, ...

**Finding the $n$th term:**
(1) Identify the first term $a_1$. → 2.
(2) Identify the common ratio $r$ (the multiplier). → 3.
(3) Count how many times $r$ was multiplied: $n-1$ times.
The $n$th term: $a_n = a_1 \cdot r^{n-1}$.

5th term: $2 \times 3^4 = 2 \times 81 = 162$.

**Sum of the first $n$ terms:**
$S_n = a_1\frac{1-r^n}{1-r}$ (for $r \neq 1$).

Sum of first 5 terms:
$S_5 = 2 \cdot \frac{1-3^5}{1-3} = 2 \cdot \frac{1-243}{-2} = 2 \cdot \frac{-242}{-2} = 242$.
Check: $2+6+18+54+162 = 242$. Perfect.

**Alternate form** (sometimes more convenient when $r > 1$):
$S_n = a_1\frac{r^n-1}{r-1}$. Same result, fewer negatives.

---

## Example 3: Infinite Geometric Series — Adding Forever, Sum Is Finite

Condition: $|r| < 1$ (the ratio's absolute value must be less than 1).
When this holds, the terms shrink to zero and the infinite sum converges:
$S_\infty = \frac{a_1}{1-r}$.

**Example 1**: $2 + 1 + \frac{1}{2} + \frac{1}{4} + \cdots$
$a_1 = 2$, $r = \frac{1}{2}$.
$S_\infty = \frac{2}{1-\frac{1}{2}} = \frac{2}{\frac{1}{2}} = 4$.

**Example 2**: Prove $0.\overline{9} = 1$.
$0.999\ldots = \frac{9}{10} + \frac{9}{100} + \frac{9}{1000} + \cdots$
$a_1 = \frac{9}{10}$, $r = \frac{1}{10}$.
$S_\infty = \frac{9/10}{1 - 1/10} = \frac{9/10}{9/10} = 1$. Proven.

**Example 3**: A bouncing ball drops from 10 m, rebounds to 60% of its previous height each time. Total vertical distance traveled:
Drop: $10 + 2(10 \cdot 0.6) + 2(10 \cdot 0.6^2) + \cdots$
$= 10 + 20(0.6 + 0.6^2 + \cdots) = 10 + 20 \cdot \frac{0.6}{1-0.6} = 10 + 20 \cdot 1.5 = 40$ meters.

---

## Example 4: Recognizing Arithmetic vs. Geometric

Given the first few terms, decide which type it is:

**Sequence A**: 7, 11, 15, 19, ...
Differences: $11-7=4$, $15-11=4$, $19-15=4$. Constant difference → **arithmetic**, $d=4$.

**Sequence B**: 3, 6, 12, 24, ...
Ratios: $\frac{6}{3}=2$, $\frac{12}{6}=2$, $\frac{24}{12}=2$. Constant ratio → **geometric**, $r=2$.

**Sequence C**: 1, 4, 9, 16, ...
Differences: 3, 5, 7 (not constant). Ratios: 4, 2.25, 1.78 (not constant).
Neither arithmetic nor geometric — this is $n^2$, a quadratic sequence.

---

## Part B: Sigma Notation and Summation Formulas

---

## Example 5: Reading Sigma Notation

$\sum_{k=1}^{n} a_k$ means: "Plug $k=1,2,\dots,n$ into $a_k$ and add all the results."

$\sum_{k=1}^{5} k = 1+2+3+4+5 = 15$.
$\sum_{k=1}^{4} k^2 = 1+4+9+16 = 30$.
$\sum_{k=3}^{7} (2k-1) = 5+7+9+11+13 = 45$.

Sigma notation has three parts:
- Below: starting index ($k=1$).
- Above: ending index ($n$).
- Body: the expression to sum ($a_k$).

---

## Example 6: Three Essential Summation Formulas — Engrave Them

**(1) Sum of the first $n$ natural numbers:**
$\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$.
Sum from 1 to 100: $\frac{100 \cdot 101}{2} = 5050$.

**(2) Sum of the first $n$ squares:**
$\sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}$.
Sum of squares to 10: $\frac{10 \cdot 11 \cdot 21}{6} = \frac{2310}{6} = 385$.

**(3) Sum of the first $n$ cubes:**
$\sum_{k=1}^{n} k^3 = \left(\frac{n(n+1)}{2}\right)^2 = (\sum k)^2$.
Sum of cubes to 5: $(\frac{5 \cdot 6}{2})^2 = 15^2 = 225$.
Check: $1+8+27+64+125 = 225$. The sum of cubes equals the square of the sum — a beautiful identity.

**Bonus — sum of the first $n$ odd numbers:**
$\sum_{k=1}^{n} (2k-1) = 2\sum k - \sum 1 = n(n+1) - n = n^2$.
$1+3+5+7+9 = 25 = 5^2$. The sum of the first $n$ odd numbers is exactly $n^2$.

---

## Example 7: Using $S_n$ to Recover $a_n$

If you know the sum of the first $n$ terms ($S_n$), you can extract the $n$th term ($a_n$):

(1) The first term alone: $a_1 = S_1$.
(2) For $n \geq 2$: $a_n = S_n - S_{n-1}$. Subtract the previous sum from the current sum.

**Example**: $S_n = n^2$.
$a_1 = S_1 = 1$.
$a_2 = S_2 - S_1 = 4 - 1 = 3$.
$a_3 = S_3 - S_2 = 9 - 4 = 5$.
General: $a_n = n^2 - (n-1)^2 = 2n-1$.
The sequence is $1, 3, 5, 7, \dots$ — an arithmetic sequence with $d=2$.

**Example**: $S_n = 2^n - 1$.
$a_1 = S_1 = 1$.
$a_n = (2^n-1) - (2^{n-1}-1) = 2^n - 2^{n-1} = 2^{n-1}$.
The sequence is $1, 2, 4, 8, \dots$ — a geometric sequence with $r=2$.

---

## Part C: Advanced Sequence Techniques

---

## Example 8: Telescoping — The Middle Terms Cancel in Pairs

A telescoping sum has the form $\sum [f(k+1) - f(k)]$. When you write out all the terms, everything in the middle cancels, leaving only the endpoints.

**Classic example**: $\sum_{k=1}^{n} \frac{1}{k(k+1)}$.

(1) Decompose using partial fractions: $\frac{1}{k(k+1)} = \frac{1}{k} - \frac{1}{k+1}$.
(2) Write out the terms:
$k=1$: $\frac{1}{1} - \frac{1}{2}$.
$k=2$: $\frac{1}{2} - \frac{1}{3}$.
$k=3$: $\frac{1}{3} - \frac{1}{4}$.
$\vdots$
$k=n$: $\frac{1}{n} - \frac{1}{n+1}$.

(3) Add vertically: $-\frac{1}{2}+\frac{1}{2}$ cancels, $-\frac{1}{3}+\frac{1}{3}$ cancels, and so on.
Only $\frac{1}{1}$ and $-\frac{1}{n+1}$ survive.
Result: $1 - \frac{1}{n+1} = \frac{n}{n+1}$.

**Another telescoping pattern**: $\sum_{k=1}^{n} (\sqrt{k+1} - \sqrt{k}) = \sqrt{n+1} - 1$.
Every intermediate square root cancels.

**Key insight**: Look for expressions that can be rewritten as $f(k+1)-f(k)$.

---

## Example 9: Harmonic Sequence — Reciprocals Form an Arithmetic Sequence

A sequence is **harmonic** if taking the reciprocal of each term produces an arithmetic sequence.

**Example**: $\frac{1}{2}, \frac{1}{5}, \frac{1}{8}, \frac{1}{11}, \dots$
Look at the denominators: 2, 5, 8, 11, ... — arithmetic with $a_1=2$, $d=3$.
Denominator of the $n$th term: $2 + (n-1)\cdot 3 = 3n-1$.
The $n$th term: $\frac{1}{3n-1}$.

**Harmonic mean**: $a, b, c$ are in harmonic progression if $\frac{1}{a}, \frac{1}{b}, \frac{1}{c}$ are in arithmetic progression.

---

## Example 10: Recurrence Relations — Each Term Defined by Its Predecessors

A recurrence defines each term using previous terms.

**Type 1 — Simple multiplicative**: $a_{n+1} = 2a_n$, $a_1 = 1$.
Generate: 1, 2, 4, 8, 16, ... — geometric, $a_n = 2^{n-1}$.

**Type 2 — Additive with a function of $n$**: $a_{n+1} = a_n + 3n$, $a_1 = 2$.
The difference between consecutive terms is $3n$ (not constant — depends on $n$).
The $n$th term is the first term plus the sum of all previous differences:
$a_n = a_1 + \sum_{k=1}^{n-1} 3k = 2 + 3\cdot\frac{(n-1)n}{2} = 2 + \frac{3n(n-1)}{2}$.
Check: $a_2 = 2+3=5$, $a_3 = 5+6=11$, $a_4 = 11+9=20$.

**Type 3 — First-order linear**: $a_{n+1} = 3a_n - 4$, $a_1 = 5$.
(1) Find the fixed point $x$ where $x = 3x - 4$ → $x = 2$.
(2) Subtract $x$ from both sides: $a_{n+1} - 2 = 3(a_n - 2)$.
(3) Let $b_n = a_n - 2$. Then $b_{n+1} = 3b_n$ — geometric with ratio 3.
(4) $b_1 = a_1 - 2 = 3$. $b_n = 3 \cdot 3^{n-1} = 3^n$.
(5) $a_n = b_n + 2 = 3^n + 2$.
Check: $a_1 = 5$ ✓. $a_2 = 11$ ✓. $a_3 = 29$ ✓.

**General formula**: For $a_{n+1} = pa_n + q$, the fixed point is $x = \frac{q}{1-p}$ (if $p \neq 1$). Then $a_n - x$ is geometric with ratio $p$.

---

## Example 11: Second-Order Linear Recurrence — Fibonacci and Beyond

$a_{n+2} = 5a_{n+1} - 6a_n$, $a_1 = 1$, $a_2 = 2$.

(1) Form the **characteristic equation**: $r^2 = 5r - 6$ → $r^2 - 5r + 6 = 0$.
(2) Solve: $(r-2)(r-3) = 0$ → $r = 2, 3$.
(3) The general solution has the form $a_n = A \cdot 2^n + B \cdot 3^n$.
(4) Plug in $n=1,2$ to find $A$ and $B$:
$2A + 3B = 1$, $4A + 9B = 2$.
Solving: $A = \frac{1}{2}$, $B = 0$.
(5) $a_n = \frac{1}{2} \cdot 2^n = 2^{n-1}$.

**The Fibonacci sequence**: $F_{n+2} = F_{n+1} + F_n$, $F_1 = F_2 = 1$.
Characteristic equation: $r^2 = r + 1$ → $r = \frac{1 \pm \sqrt{5}}{2}$.
**Binet's formula**: $F_n = \frac{1}{\sqrt{5}}\left[\left(\frac{1+\sqrt{5}}{2}\right)^n - \left(\frac{1-\sqrt{5}}{2}\right)^n\right]$.
This produces integers from an expression full of $\sqrt{5}$ — a mathematical magic trick.

---

## Example 12: Method of Differences — When the Differences Form a Known Sequence

Sequence: 1, 3, 7, 13, 21, ...

(1) Compute differences: $3-1=2$, $7-3=4$, $13-7=6$, $21-13=8$.
The differences are $2, 4, 6, 8, \dots$ — an arithmetic sequence: $b_k = 2k$.

(2) The $n$th term is the first term plus the sum of the first $n-1$ differences:
$a_n = a_1 + \sum_{k=1}^{n-1} 2k = 1 + 2\cdot\frac{(n-1)n}{2} = 1 + n(n-1) = n^2 - n + 1$.

Check: $n=3$ → $9-3+1 = 7$ ✓. $n=5$ → $25-5+1 = 21$ ✓.

**The method**: If the differences $b_k = a_{k+1} - a_k$ form a known sequence, then:
$a_n = a_1 + \sum_{k=1}^{n-1} b_k$.

---

## Example 13: Grouped Sequences — Counting by Blocks

$(1), (2,3), (4,5,6), (7,8,9,10), \dots$

Rule: Group $n$ contains $n$ consecutive integers.

(1) How many numbers appear before group $n$?
$1 + 2 + \cdots + (n-1) = \frac{(n-1)n}{2}$ numbers.

(2) The first number in group $n$: $1 + \frac{(n-1)n}{2}$.
The last number in group $n$: $\frac{n(n+1)}{2}$.

Group 10: first = $1 + \frac{9\cdot 10}{2} = 46$, last = $\frac{10\cdot 11}{2} = 55$.
Group 10 contains: 46, 47, ..., 55 (10 numbers).

**Reverse lookup**: Which group contains the number 100?
Find $n$ such that $\frac{n(n+1)}{2} \geq 100$.
$13 \cdot 14 = 182 < 200$ (too small for $n=13$ since we need $n(n+1) \geq 200$).
$14 \cdot 15 = 210 \geq 200$. So $n=14$.
Group 14: first = $1 + \frac{13\cdot 14}{2} = 92$, last = $\frac{14\cdot 15}{2} = 105$.

---

## Example 14: Mathematical Induction — Proving for All $n$ at Once

Induction works like a row of dominoes: knock down the first, and each falling domino knocks down the next. If both conditions hold, all dominoes fall.

**Two-step structure**:
(1) Base case: Show the statement holds for $n=1$.
(2) Inductive step: Assume it holds for $n=k$. Prove it holds for $n=k+1$.

**Example**: Prove $1+2+\cdots+n = \frac{n(n+1)}{2}$ for all $n \geq 1$.

Base case ($n=1$): Left = $1$. Right = $\frac{1\cdot 2}{2} = 1$. ✓

Inductive step: Assume $1+2+\cdots+k = \frac{k(k+1)}{2}$.
For $n=k+1$:
$1+2+\cdots+k+(k+1) = \frac{k(k+1)}{2} + (k+1) = \frac{k(k+1) + 2(k+1)}{2} = \frac{(k+1)(k+2)}{2}$.
This matches the formula with $n=k+1$. ✓

Therefore the formula holds for all natural numbers $n$.

**Example**: Prove $n^3 - n$ is always a multiple of 6.

Base case ($n=1$): $1-1=0 = 6 \times 0$. ✓

Inductive step: Assume $k^3-k = 6m$. For $n=k+1$:
$(k+1)^3 - (k+1) = k^3 + 3k^2 + 3k + 1 - k - 1 = (k^3-k) + 3k(k+1) = 6m + 3k(k+1)$.
$k(k+1)$ is the product of two consecutive integers — always even. So $3k(k+1)$ is a multiple of 6.
Thus $(k+1)^3-(k+1)$ is a multiple of 6. ✓

---

## Example 15: Limits of Sequences — What Happens as $n \to \infty$

$a_n = \frac{n}{n+1}$.
Compute values: $n=1 \to 0.5$, $n=10 \to 0.909$, $n=100 \to 0.990$, $n=1000 \to 0.999$.
As $n$ grows without bound, $a_n$ approaches 1. We write $\lim_{n\to\infty} \frac{n}{n+1} = 1$.

**The $\frac{\infty}{\infty}$ trick — divide by the highest power of $n$:**

$a_n = \frac{3n^2 + 2n}{n^2 + 1}$. Divide numerator and denominator by $n^2$:
$a_n = \frac{3 + 2/n}{1 + 1/n^2}$. As $n \to \infty$, $2/n \to 0$ and $1/n^2 \to 0$.
So $\lim a_n = \frac{3+0}{1+0} = 3$.

**Key limit facts to memorize:**
- $\lim_{n\to\infty} \left(1 + \frac{1}{n}\right)^n = e \approx 2.718$.
- $\lim_{n\to\infty} \frac{\ln n}{n} = 0$ (polynomials grow faster than logarithms).
- $\lim_{n\to\infty} r^n = 0$ when $|r| < 1$ (the geometric decay to zero).
- $\lim_{n\to\infty} \sqrt[n]{n} = 1$.

---

## Example 16: The Floor Function in Sums — Counting by Groups

$\sum_{k=1}^{10} \lfloor\sqrt{k}\rfloor$.

Group the values of $\lfloor\sqrt{k}\rfloor$:
$k=1,2,3$: $\lfloor\sqrt{k}\rfloor = 1$ (3 numbers).
$k=4,5,6,7,8$: $\lfloor\sqrt{k}\rfloor = 2$ (5 numbers).
$k=9,10$: $\lfloor\sqrt{k}\rfloor = 3$ (2 numbers).

Sum = $3 \times 1 + 5 \times 2 + 2 \times 3 = 3 + 10 + 6 = 19$.

**Counting digits with floor**: $\sum_{k=1}^{100} \lfloor\log_{10} k\rfloor$.
1-digit numbers ($k=1$ to $9$): $\lfloor\log_{10}k\rfloor = 0$ → 9 terms → $0$.
2-digit numbers ($k=10$ to $99$): $\lfloor\log_{10}k\rfloor = 1$ → 90 terms → $90$.
3-digit numbers ($k=100$): $\lfloor\log_{10}k\rfloor = 2$ → 1 term → $2$.
Sum = $0 + 90 + 2 = 92$.

> **Up to here**: Arithmetic adds $d$, geometric multiplies by $r$. Infinite geometric sum converges when $|r|<1$.
> Three sigma formulas: $\sum k$, $\sum k^2$, $\sum k^3$. Extract $a_n$ from $S_n$ via $S_n - S_{n-1}$.
> Telescoping → middle cancels. Recurrence → characteristic equation. Induction → domino principle.
> Limits → divide by highest power of $n$.

---

## Common Mistakes

### Mistake 1: Using the wrong denominator in the geometric sum formula

**Wrong path**: Writing $S_n = a_1\frac{r^n-1}{1-r}$ and forgetting that the denominator must be $r-1$ when using $r^n-1$.

**Why wrong**: The two forms are $\frac{a_1(1-r^n)}{1-r}$ and $\frac{a_1(r^n-1)}{r-1}$. The sign of the denominator must match the sign of the numerator.

**Right path**: Pick one form and stick with it. $\frac{a_1(1-r^n)}{1-r}$ works for any $r \neq 1$. The numerator and denominator both flip sign when $r>1$, giving a positive result.

---

### Mistake 2: Applying the infinite geometric sum formula when $|r| \geq 1$

**Wrong path**: "$1 + 2 + 4 + 8 + \cdots = \frac{1}{1-2} = -1$."

**Why wrong**: The infinite sum formula requires $|r| < 1$. When $|r| \geq 1$, the terms do not shrink — the sum diverges to infinity.

**Right path**: Check $|r|$ first. If $|r| \geq 1$, the infinite sum does not exist (it diverges).

---

### Mistake 3: Forgetting the base case in induction

**Wrong path**: Proving only the inductive step ($k \to k+1$) without checking $n=1$.

**Why wrong**: The chain of implications has no starting point. Without the base case, the proof is incomplete — like a row of dominoes where no one pushes the first one.

**Right path**: Always verify the base case ($n=1$ or the smallest relevant $n$) before the inductive step.

---

### Mistake 4: Treating $\sum (a_k b_k)$ as $(\sum a_k)(\sum b_k)$

**Wrong path**: "$\sum k^2 = (\sum k)(\sum k)$."

**Why wrong**: $\sum k^2 = \frac{n(n+1)(2n+1)}{6}$, but $(\sum k)^2 = \frac{n^2(n+1)^2}{4}$. These are different. The sum of products is not the product of sums.

**Right path**: Use the specific formula for $\sum k^2$. Never split a sum across a product.

---

## What We Just Did

```
(1) Arithmetic — add d each step. Term = a₁ + (n−1)d. Sum = n(a₁+a_n)/2.
    Geometric — multiply by r each step. Term = a₁·r^{n−1}. Sum = a₁(1−r^n)/(1−r).
    Infinite geometric sum: a₁/(1−r) — works only when |r| < 1.

(2) Sigma — compact notation for sums. Three essential formulas: Σk, Σk², Σk³.
    Recover a_n from S_n: a_n = S_n − S_{n−1} (for n≥2).

(3) Advanced tools — telescoping cancels the middle. Harmonic = reciprocals form AP.
    Recurrences: +f(n) type → sum differences. pa_n+q type → fixed point trick.
    Second-order → characteristic equation r² = pr + q.
    Induction = base case + (k → k+1). Limits = divide by highest power of n.
```

---

## Practice 1

Find the 20th term and the sum of the first 20 terms of the arithmetic sequence: 5, 9, 13, 17, ...

→ Reference: **Example 1**

> Solutions: [Solutions](solutions/12B-solutions.md#practice-1)

---

## Practice 2

Find the sum of the first 8 terms of the geometric sequence: $3, 6, 12, 24, \dots$

→ Reference: **Example 2**

> Solutions: [Solutions](solutions/12B-solutions.md#practice-2)

---

## Practice 3

Evaluate the infinite sum: $5 + \frac{5}{3} + \frac{5}{9} + \frac{5}{27} + \cdots$

→ Reference: **Example 3**

> Solutions: [Solutions](solutions/12B-solutions.md#practice-3)

---

## Practice 4: Composition

A sequence is both arithmetic and geometric. Prove that all its terms must be equal. Give a real-world situation where a constant sequence naturally arises.

→ Reference: **Example 1, 2**

> Solutions: [Solutions](solutions/12B-solutions.md#practice-4)

---

## Practice 5

Compute $\sum_{k=1}^{n} (2k-1)$ using sigma formulas. Show the result equals $n^2$.

→ Reference: **Example 6**

> Solutions: [Solutions](solutions/12B-solutions.md#practice-5)

---

## Practice 6

Evaluate the telescoping sum: $\sum_{k=1}^{20} \frac{1}{k(k+1)}$.

→ Reference: **Example 8**

> Solutions: [Solutions](solutions/12B-solutions.md#practice-6)

---

## Practice 7

Solve the recurrence: $a_{n+1} = 2a_n + 3$, $a_1 = 1$. Find a formula for $a_n$.

→ Reference: **Example 10**

> Solutions: [Solutions](solutions/12B-solutions.md#practice-7)

---

## Practice 8

The differences of a sequence are $3, 5, 7, 9, \dots$ and the first term is 2. Find the 10th term.

→ Reference: **Example 12**

> Solutions: [Solutions](solutions/12B-solutions.md#practice-8)

---

## Practice 9: Composition

Invent your own telescoping sum by finding a function $f(k)$ such that $f(k+1)-f(k)$ produces a simple expression. Write out the sum of 10 terms and verify the cancellation.

→ Reference: **Example 8**

> Solutions: [Solutions](solutions/12B-solutions.md#practice-9)

---

## Practice 10

Prove by induction: $\sum_{k=1}^{n} k^3 = \left(\frac{n(n+1)}{2}\right)^2$.

→ Reference: **Example 14**

> Solutions: [Solutions](solutions/12B-solutions.md#practice-10)

---

## Practice 11

Find $\lim_{n\to\infty} \frac{5n^3 - 2n + 1}{3n^3 + n^2 + 4}$.

→ Reference: **Example 15**

> Solutions: [Solutions](solutions/12B-solutions.md#practice-11)

---

## Practice 12: Real Battle

The Fibonacci sequence satisfies $F_{n+2} = F_{n+1} + F_n$ with $F_1=F_2=1$. Prove by induction that $F_1 + F_2 + \cdots + F_n = F_{n+2} - 1$. Then use Binet's formula to find $\lim_{n\to\infty} \frac{F_{n+1}}{F_n}$ (the golden ratio).

→ Reference: **Example 11, 14, 15**

> Solutions: [Solutions](solutions/12B-solutions.md#practice-12)

---

## Basic Algebra Drill — Sequences and Series (10 Problems)

> Pure calculation. Master the fundamental formulas through repetition.

**D1.** Find the 15th term of the arithmetic sequence: $4, 10, 16, 22, \dots$

**D2.** Find the sum of the first 12 terms of the geometric sequence: $2, -4, 8, -16, \dots$

**D3.** Write $0.555\ldots$ (repeating) as a fraction using infinite geometric series.

**D4.** Evaluate $\sum_{k=1}^{50} k$ using the formula.

**D5.** Evaluate $\sum_{k=1}^{8} k^2$.

**D6.** For the sequence with $S_n = 3n^2 + n$, find $a_5$.

**D7.** Identify the type of sequence: $\frac{1}{3}, \frac{1}{7}, \frac{1}{11}, \frac{1}{15}, \dots$

**D8.** Compute $\sum_{k=1}^{6} (k^3 - k)$.

**D9.** Find the sum of the first 20 terms of the arithmetic sequence: $7, 12, 17, 22, \dots$

**D10.** Find the infinite sum: $8 + 4 + 2 + 1 + \frac{1}{2} + \cdots$

> Solutions: [Solutions](solutions/12B-solutions.md#basic-drill)

---

## Advanced Algebra Drill — Sequences and Series (10 Problems)

> Multi-step. Chain concepts across the full toolkit.

**A1.** Find $a_{20}$ for the sequence where $a_1 = 3$ and $a_{n+1} = a_n + 2n$.

**A2.** Solve the recurrence $a_{n+1} = 4a_n - 3$, $a_1 = 2$. Give the general term $a_n$.

**A3.** Compute $\sum_{k=1}^{n} \frac{1}{(2k-1)(2k+1)}$ using telescoping. Give a closed form in terms of $n$.

**A4.** The sum of an infinite geometric series is 12, and the second term is 3. Find the first term and the common ratio.

**A5.** Prove by induction: $1 \cdot 2 + 2 \cdot 3 + 3 \cdot 4 + \cdots + n(n+1) = \frac{n(n+1)(n+2)}{3}$.

**A6.** For the grouped sequence $(1,2), (3,4,5), (6,7,8,9), \dots$, find the first and last numbers in the 15th group.

**A7.** Find $\lim_{n\to\infty} \left(\sqrt{n^2 + 3n} - n\right)$. (Hint: rationalize the numerator.)

**A8.** A sequence has first term 1 and each term after the first is the sum of all previous terms. Find a formula for $a_n$ and prove it by induction.

**A9.** Find $\sum_{k=1}^{n} k(k+1)$ using the formulas for $\sum k^2$ and $\sum k$.

**A10.** The Fibonacci sequence satisfies $F_1=F_2=1$, $F_{n+2}=F_{n+1}+F_n$. Prove that $F_1+F_2+\cdots+F_n = F_{n+2}-1$ by induction.

> Solutions: [Solutions](solutions/12B-solutions.md#advanced-drill)

---

## Today's Procedure

```
Step 1: Identify the sequence type — constant difference → arithmetic.
         Constant ratio → geometric. Neither → look for differences of differences.
         For arithmetic: a_n = a₁ + (n−1)d, S_n = n(a₁+a_n)/2.
         For geometric: a_n = a₁·r^{n−1}, S_n = a₁(1−r^n)/(1−r).
         Infinite geometric: S∞ = a₁/(1−r), only when |r| < 1.

Step 2: Summation tools — Σk = n(n+1)/2, Σk² = n(n+1)(2n+1)/6, Σk³ = (Σk)².
         Recover a_n from S_n: a₁ = S₁, a_n = S_n − S_{n−1}.
         Telescoping: decompose into f(k+1)−f(k), watch the middle cancel.

Step 3: Advanced — recurrence a_{n+1}=a_n+f(n) → sum the differences.
         Recurrence a_{n+1}=pa_n+q → find fixed point, shift to geometric.
         Recurrence a_{n+2}=pa_{n+1}+qa_n → characteristic equation r²=pr+q.
         Induction: base case + (k → k+1). Limits: divide by highest power.
```

---

## Terminology

Up to now we used plain words like "first term", "common difference", "multiplier", "canceling sum".
**You have already learned all the methods.** Now we attach the formal mathematical names.

| What we called it | Mathematical term | Notation / Formula |
|:-----------------:|:-----------------:|:------------------:|
| common difference | common difference | $d$ |
| common ratio | common ratio | $r$ |
| arithmetic sequence | arithmetic progression (AP) | $a_n = a_1 + (n-1)d$ |
| geometric sequence | geometric progression (GP) | $a_n = a_1 r^{n-1}$ |
| arithmetic sum | arithmetic series | $S_n = \frac{n(a_1+a_n)}{2}$ |
| geometric sum | geometric series | $S_n = a_1\frac{1-r^n}{1-r}$ |
| infinite geometric sum | infinite geometric series | $S_\infty = \frac{a_1}{1-r}$, $|r|<1$ |
| sigma notation | summation notation | $\sum_{k=1}^{n} a_k$ |
| telescoping | telescoping series | $\sum [f(k+1)-f(k)]$ |
| harmonic sequence | harmonic progression | reciprocals form an AP |
| recurrence | recurrence relation | $a_{n+1} = f(a_n)$ |
| characteristic equation | characteristic equation | $r^2 = pr + q$ |
| mathematical induction | mathematical induction | base case + inductive step |
| limit of a sequence | limit | $\lim_{n\to\infty} a_n$ |
| Fibonacci sequence | Fibonacci sequence | $F_{n+2} = F_{n+1} + F_n$ |
| Binet's formula | Binet's formula | $F_n = \frac{\phi^n - \psi^n}{\sqrt{5}}$ |
