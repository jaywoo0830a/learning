# Session 07B: Partial Fractions, Systems, and Advanced Equation Solving

**Phase 2 — Classical Techniques | 50 min**

*Prerequisites: 07A (factoring), 10A (exponents)*

---

## Part A: Partial Fractions — Tearing Rational Expressions Apart

> **Why this matters**: partial fractions exist to integrate rational functions (Session 16B). Each denominator type integrates to a known form — $\int\frac{1}{x-a}dx=\ln|x-a|$, $\int\frac{1}{(x-a)^2}dx=-\frac{1}{x-a}$, $\int\frac{1}{x^2+1}dx=\arctan x$ — so decomposing a rational function turns a hard integral into a sum of easy ones.

---

## Example 1: Distinct Linear Factors

$\frac{3x+5}{(x-1)(x+2)} = \frac{A}{x-1} + \frac{B}{x+2}$.

Multiply by $(x-1)(x+2)$: $3x+5 = A(x+2) + B(x-1)$.
$x=1$: $8=3A$ → $A=8/3$. $x=-2$: $-1=-3B$ → $B=1/3$.

$\frac{3x+5}{(x-1)(x+2)} = \frac{8/3}{x-1} + \frac{1/3}{x+2}$.

---

## Example 2: Repeated Linear Factor

$\frac{2x+1}{(x-1)^2} = \frac{A}{x-1} + \frac{B}{(x-1)^2}$.

$2x+1 = A(x-1) + B$. Compare coefficients: $A=2$, $-A+B=1$ → $B=3$.

$\frac{2x+1}{(x-1)^2} = \frac{2}{x-1} + \frac{3}{(x-1)^2}$.

---

## Example 3: Improper — Divide First

$\frac{x^3+2x}{x^2-1}$. Degree(num)=3 > degree(den)=2. Divide:
$x^3+2x = x(x^2-1) + 3x$. So $\frac{x^3+2x}{x^2-1} = x + \frac{3x}{x^2-1}$.

Now decompose $\frac{3x}{(x-1)(x+1)} = \frac{3/2}{x-1} + \frac{3/2}{x+1}$.

---

## Example 3A: Irreducible Quadratic Factor — $\frac{Ax+B}{x^2+px+q}$

**$\frac{3x^2+2x+1}{(x-1)(x^2+1)}$**. The quadratic $x^2+1$ doesn't factor over the reals — its partial fraction needs a **linear numerator**:

$\frac{3x^2+2x+1}{(x-1)(x^2+1)} = \frac{A}{x-1} + \frac{Bx+C}{x^2+1}$.

Multiply through: $3x^2+2x+1 = A(x^2+1)+(Bx+C)(x-1)$.

- $x=1$: $6 = 2A$ → $A=3$.
- Compare coefficients: $(A+B)x^2 + (C-B)x + (A-C)$. So $A+B=3$, $C-B=2$, $A-C=1$. With $A=3$: $B=0$, $C=2$.

$\frac{3x^2+2x+1}{(x-1)(x^2+1)} = \frac{3}{x-1} + \frac{2}{x^2+1}$.

> **Why a linear numerator?** $\int\frac{Bx+C}{x^2+px+q}dx$ splits into a log part ($\int\frac{x}{x^2+1}dx$) plus an arctan part ($\int\frac{1}{x^2+1}dx$) — the linear numerator is what makes both pieces integrate cleanly.

---

## Example 3B: Repeated Quadratic Factor

**$\frac{4x^3+8x^2+4x+3}{(x^2+1)^2}$**: the quadratic appears twice, so use both forms:

$\frac{4x^3+8x^2+4x+3}{(x^2+1)^2} = \frac{Ax+B}{x^2+1} + \frac{Cx+D}{(x^2+1)^2}$.

Multiply: $4x^3+8x^2+4x+3 = (Ax+B)(x^2+1)+Cx+D$.

Compare coefficients: $A=4$, $B=8$, $A+C=4$ → $C=0$, $B+D=3$ → $D=-5$.

$\frac{4x^3+8x^2+4x+3}{(x^2+1)^2} = \frac{4x+8}{x^2+1} - \frac{5}{(x^2+1)^2}$.

> **The complete setup table**: each distinct linear factor $x-a$ → $\frac{A}{x-a}$; each repeated linear factor $(x-a)^m$ → $\frac{A_1}{x-a}+\cdots+\frac{A_m}{(x-a)^m}$; each irreducible quadratic $x^2+px+q$ → $\frac{Ax+B}{x^2+px+q}$; repeated quadratics stack like linear ones.

---

## Part B: Systems of Equations

---

## Example 4: Substitution

$\begin{cases} 2x+y=7 \\ x^2+y^2=25 \end{cases}$. From first: $y=7-2x$. Plug:
$x^2+(7-2x)^2=25$ → $5x^2-28x+24=0$ → $(5x-6)(x-4)=0$. Solutions: $(6/5, 23/5), (4,-1)$.

![Substitution: line 2x+y=7 meets the circle x²+y²=25](graphs/0812/07B/07b-line-circle.png)

---

## Example 5: Elimination

$\begin{cases} 3x+2y=8 \\ 2x-y=3 \end{cases}$. Multiply second by 2: $4x-2y=6$. Add: $7x=14$ → $x=2,y=1$.

![Elimination: two lines meet at (2,1)](graphs/0812/07B/07b-elimination.png)

---

## Example 6: Three Variables

$\begin{cases} x+y+z=6 \\ 2x-y+z=3 \\ x+2y-z=3 \end{cases}$. Eliminate $z$ from first two → $x-2y=-3$. Eliminate $z$ from first and third → $2x+3y=9$. Solve 2×2: $x=1,y=2,z=3$.

---

## Example 6A: Cramer's Rule — Determinants Decide (🔗 12A2)

For $\begin{cases} ax+by=e \\ cx+dy=f \end{cases}$, the **determinant** $D=\det\begin{pmatrix}a&b\\c&d\end{pmatrix}=ad-bc$ decides everything:

- $D\neq0$: a unique solution $x=\frac{ed-bf}{D}$, $y=\frac{af-ec}{D}$.
- $D=0$: no solution OR infinitely many (the lines are parallel or identical).

**Recompute Example 5**: $\begin{cases} 3x+2y=8 \\ 2x-y=3 \end{cases}$. $D=3(-1)-2(2)=-7$.
$x=\frac{8(-1)-2(3)}{-7}=\frac{-14}{-7}=2$, $y=\frac{3(3)-8(2)}{-7}=\frac{-7}{-7}=1$. ✓ Same $(2,1)$ as elimination.

> Determinants give a formula instead of a procedure — and they tell you up front whether a solution exists. This is the same $\det$ you use for area scaling in 12A2.

---

## Example 6B: No Solution vs. Infinite Solutions

**$\begin{cases} x+y=3 \\ 2x+2y=7 \end{cases}$**: the second is $2\times$first with a different constant ($6\neq7$) → the lines are **parallel** → **no solution** (inconsistent).

**$\begin{cases} x+y=3 \\ 2x+2y=6 \end{cases}$**: the second is exactly $2\times$first → the **same line** → **infinitely many** solutions: $(t, 3-t)$ for any $t$ (dependent).

> **Test**: after elimination, a false statement like $0=1$ means no solution; a true identity like $0=0$ means infinitely many.

![Inconsistent vs dependent systems](graphs/0812/07B/07b-consistent-inconsistent.png)

---

## Example 7: Symmetric Systems

$\begin{cases} x+y=5 \\ xy=6 \end{cases}$. $x,y$ are roots of $t^2-5t+6=0$ → $t=2,3$. Solutions: $(2,3),(3,2)$.

![System of equations intersection](graphs/0812/07B/07b-system-intersection.png)

> **Up to here**: Partial fractions = decompose rational functions. Distinct linear → A/(x−a). Repeated → A/(x−a) + B/(x−a)². Improper → divide first.
> Systems: substitution or elimination. Symmetric → sum-and-product → quadratic.

---

## What We Just Did

```
(1) Partial fractions: factor denominator fully. Set up the form from the factor types:
    distinct linear → A/(x−a); repeated → stack powers; irreducible quadratic → (Ax+B)/….
    Multiply through. Plug convenient x or compare coefficients.
    If degree(num) ≥ degree(den), divide first.

(2) Systems: substitution isolates one variable. Elimination aligns coefficients.
    Three variables → eliminate to 2×2. Cramer: D=ad−bc; D≠0 unique, D=0 → 0 or ∞.
    Symmetric systems: use sum S and product P → roots of t²−St+P=0.
    Purpose: partial fractions power integration in Session 16B.
```

---

## Common Mistakes

### Mistake 1: Not dividing first in partial fractions when degree(num) ≥ degree(den)
### Mistake 2: Forgetting to check all solutions satisfy ALL equations in a system
### Mistake 3: Missing the $x \neq$ restrictions from the original denominator

---

## Practice 1

Decompose: $\frac{5x-1}{(x+1)(x-2)}$.

→ Solutions: [Solutions](solutions/07B-solutions.md#practice-1)

---

## Practice 2

Decompose: $\frac{x^2+3x}{(x-1)^2(x+2)}$.

→ Solutions: [Solutions](solutions/07B-solutions.md#practice-2)

---

## Practice 3

Solve: $\begin{cases} x^2+y^2=13 \\ xy=6 \end{cases}$.

→ Solutions: [Solutions](solutions/07B-solutions.md#practice-3)

---

## Practice 4: Real Battle

Decompose $\frac{x^3+2x^2+1}{x(x^2+1)}$ and solve $\begin{cases} xy+x+y=11 \\ x^2y+xy^2=30 \end{cases}$.

→ Solutions: [Solutions](solutions/07B-solutions.md#practice-4)

---

## Practice 5: Composition

Create a system of two equations whose only solutions are $(1,2)$ and $(3,-1)$. Hint: each point must satisfy both equations.

→ Solutions: [Solutions](solutions/07B-solutions.md#practice-5)

---

## Basic Drills

**D1.** Decompose $\frac{4}{(x-1)(x+3)}$.

**D2.** Decompose $\frac{x+2}{x(x-1)}$.

**D3.** Decompose $\frac{2x}{(x+1)^2}$.

**D4.** Solve $\begin{cases} x+y=4 \\ x-y=2 \end{cases}$.

**D5.** Solve $\begin{cases} 2x+3y=7 \\ 5x-2y=8 \end{cases}$.

**D6.** Decompose $\frac{x^2}{x^2-1}$ (improper — divide first).

**D7.** Solve $\begin{cases} x+y+z=4 \\ x-y+z=2 \\ x+y-z=0 \end{cases}$.

**D8.** Decompose $\frac{3}{x^2+x-2}$ (factor denominator first).

**D9.** Solve $\begin{cases} x+y=7 \\ x^2-y^2=21 \end{cases}$. Use $x^2-y^2=(x-y)(x+y)$.

**D10.** Find partial fractions for $\frac{1}{x(x+1)}$ and use it to compute $\sum_{n=1}^{10}\frac{1}{n(n+1)}$.

> Solutions: [Solutions](solutions/07B-solutions.md#basic-drill)

---

## Advanced Drills

**A1.** Decompose $\frac{x^3+1}{x(x-1)^2}$.

**A2.** Decompose $\frac{2x^2+3x+4}{(x+1)(x^2+1)}$ (quadratic factor).

**A3.** Solve $\begin{cases} x^2+y^2=25 \\ x+y=1 \end{cases}$.

**A4.** Solve $\begin{cases} \frac{1}{x}+\frac{1}{y}=5 \\ \frac{1}{x^2}+\frac{1}{y^2}=13 \end{cases}$. Let $u=1/x$, $v=1/y$.

**A5.** Decompose $\frac{1}{x^3-1}$ using difference of cubes.

**A6.** Solve $\begin{cases} xy=12 \\ yz=20 \\ zx=15 \end{cases}$. Multiply all three equations.

**A7.** Find $A,B,C$ such that $\frac{1}{x(x+1)(x+2)} = \frac{A}{x}+\frac{B}{x+1}+\frac{C}{x+2}$.

**A8.** Solve $\begin{cases} x^3+y^3=35 \\ x+y=5 \end{cases}$. Use $x^3+y^3=(x+y)(x^2-xy+y^2)$.

**A9.** Decompose $\frac{x^4}{(x^2+1)^2}$. Division first, then partial fractions.

**A10.** A system has exactly 8 solutions: $(\pm2,\pm3)$ and $(\pm3,\pm2)$ (any sign combination). Find the system of equations. (Hint: think about $x^2+y^2$ and $x^2y^2$.)

> Solutions: [Solutions](solutions/07B-solutions.md#advanced-drill)

---

## Today's Procedure

```
Step 1: Partial fractions — factor the denominator completely.
         Linear factor → A/(x−a). Repeated → A/(x−a)+B/(x−a)²+…
         Irreducible quadratic → (Ax+B)/(x²+px+q), stacked if repeated.
         Improper rational function: divide polynomials first.
Step 2: Systems — substitution: isolate one variable, plug into the other.
         Elimination: align coefficients, subtract to cancel one variable.
         Cramer: compute D=ad−bc. D≠0 → unique; D=0 → parallel (0) or same line (∞).
Step 3: Symmetric systems — rewrite in terms of S=x+y, P=xy.
         Then x,y are roots of t²−St+P=0.
```

---

## How to Read These Symbols

| Symbol | Reads as | Meaning |
|:---:|:---:|------|
| $\frac{P(x)}{Q(x)}$ | "P of x over Q of x" | rational function — polynomial divided by polynomial |
| $\frac{A}{x-a}$ | "A over x minus a" | partial fraction — linear factor term |
| $\frac{Ax+B}{x^2+bx+c}$ | "A x plus B over x squared plus b x plus c" | partial fraction — irreducible quadratic term |
| $\begin{cases} ax+by=e \\ cx+dy=f \end{cases}$ | "system: a x plus b y equals e, c x plus d y equals f" | 2×2 linear system |
| elimination | "elimination" / "Gaussian elimination" | add/subtract equations to remove a variable |
| substitution | "substitution" | solve one equation for a variable, plug into the other |
| $\det = ad-bc$ | "determinant equals a d minus b c" | determines if system has unique solution (≠0) |
| consistent / inconsistent | "consistent" / "inconsistent" | has solution(s) / has no solution |
| $n \times n$ | "n by n" | square system with n equations and n unknowns |

---

## Terminology

| What we called it | Math term | Notation |
|:---------------:|:---------:|:--------:|
| tear a fraction apart | partial fraction decomposition | $\frac{P(x)}{Q(x)}=\sum\frac{A}{x-a}+\cdots$ |
| undetermined constants | unknown coefficients | $A,B,C,\ldots$ |
| distinct linear factors | distinct linear denominator factors | $\frac{A}{x-a}+\frac{B}{x-b}$ |
| repeated factor | repeated linear factor | $\frac{A}{x-a}+\frac{B}{(x-a)^2}$ |
| improper fraction | improper rational function | deg(num) ≥ deg(den) |
| substitute and solve | substitution method | isolate one variable |
| align and subtract | elimination method | cancel one variable |
| symmetric system | symmetric system | sum $S$, product $P$ |
