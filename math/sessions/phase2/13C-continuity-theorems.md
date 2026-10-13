# Session 13C: Continuity, Theorems, and Sequences

**Phase 2 — Classical Techniques | 75 min**

*Prerequisites: 13A (algebraic limits), 13B (limits at infinity), 12B1 (sequences & series), 08 (inequalities)*

> 💡 **Stuck?** Every problem has a collapsible **Hint** below it — click it only when you need a nudge.

> **Source.** Every example and drill below is drawn from Stewart, *Calculus*, Section 2.5 (Continuity) and Section 2.3 (The Squeeze Theorem), with a closing section on sequences from Section 11.1. Each item cites its example or exercise number. The three-condition definition of continuity, Theorems 4–9, and the Intermediate Value Theorem are Stewart's; the graphs redraw Stewart's Figures 2, 4, 8, and 9 of §2.5 and Figure 8 of §2.3.

---

## Part A: Continuity — Three Conditions to Check

---

## Example 1: The Definition, and What Breaks It (§2.5 Def 1, Ex 1–2)

Stewart's Definition 1: a function $f$ is **continuous at $a$** if

$$\lim_{x\to a}f(x)=f(a).$$

The single equation hides three separate requirements:

1. $f(a)$ is defined (the point exists).
2. $\lim_{x\to a}f(x)$ exists (the left and right limits agree).
3. The two numbers are equal.

Geometrically, a function continuous on an interval can be drawn without lifting the pencil.

**Stewart's Example 1** reads a graph and finds three different failures: at $a=1$ the reason is $f(1)$ undefined; at $a=3$ the reason is that $\lim_{x\to3}f(x)$ does not exist (the sides differ); at $a=5$ both exist but $\lim_{x\to5}f(x)\neq f(5)$.

**Stewart's Example 2** classifies the three failure types:

| Type | What fails | Example |
|:---:|:---:|:---:|
| **Removable** (hole) | $f(a)$ undefined, but the limit exists | $\dfrac{x^2-1}{x-1}$ at $1$ |
| **Jump** | the two one-sided limits differ | $\lfloor x\rfloor$ at $1$ |
| **Infinite** | the limit is $\pm\infty$ | $\dfrac1x$ at $0$ |

![Three types of discontinuity]({{graph:13c-1-discontinuities}})

*Graph 13C-1: (a) removable — a single missing point at $(1,2)$; (b) jump — the floor function steps up at each integer; (c) infinite — $\frac1x$ runs off to $\pm\infty$ at the origin.*

> **Geometric insight**: Continuity is an *agreement* between three quantities. A discontinuity is always a broken agreement — and the type of break tells you which of the three failed.

---

## Part B: Building Continuous Functions, and Repairing Them

---

## Example 2: Which Functions Are Automatically Continuous (§2.5 Thm 4, 5, 7, 9)

Stewart never checks continuity from scratch. Four theorems do the work.

**Theorem 4** (combinations): if $f$ and $g$ are continuous at $a$, then so are $f+g$, $f-g$, $cf$, $fg$, and $\frac fg$ (provided $g(a)\neq0$).

**Theorem 5**: every polynomial is continuous everywhere; every rational function is continuous wherever it is defined.

**Theorem 7**: polynomials, rational functions, root functions, trigonometric functions, inverse trigonometric functions, exponential functions, and logarithmic functions are continuous at every number in their domains.

**Theorem 9** (composition): if $g$ is continuous at $a$ and $f$ is continuous at $g(a)$, then $f\circ g$ is continuous at $a$.

**Stewart's Example 5** uses Theorem 5 on a rational function:

$$\lim_{x\to-2}\frac{x^3+2x^2-1}{5-3x}=f(-2)=\frac{-8+8-1}{5+6}=-\frac{1}{11}.$$

**Stewart's Example 9** uses Theorem 9 twice:

- $h(x)=\sin(x^2)$ is $f\circ g$ with $g=x^2$ and $f=\sin$ — both continuous, so $h$ is continuous on $\mathbb{R}$.
- $F(x)=\ln(1+\cos x)$ is continuous wherever it is defined; the domain is $1+\cos x>0$, i.e. all $x$ except odd multiples of $\pi$.

> **Geometric insight**: These theorems say that continuity is *inherited*. Once a short list of basic functions is known to be continuous, every combination of them — sum, product, quotient, composition — is continuous on its domain automatically.

---

## Example 3: Repairing a Hole, and Continuity on an Interval (§2.5 Ex 4, #25–26, #47)

**A removable hole** is a discontinuity you can patch by choosing the right value. Stewart's exercise bank (#25–26) asks for exactly that.

For $f(x)=\dfrac{x-3}{x^2-9}$ at $x=3$:

$$x^2-9=(x-3)(x+3),\qquad \frac{x-3}{(x-3)(x+3)}=\frac{1}{x+3}\longrightarrow\frac16 .$$

The limit exists, so the discontinuity is removable: define $f(3)=\dfrac16$ and the function becomes continuous at $3$.

For $f(x)=\dfrac{x^2-7x+12}{x-3}$ at $x=3$: $x^2-7x+12=(x-3)(x-4)$, so the limit is $x-4\to-1$. Define $f(3)=-1$.

![Piecewise repaired to be continuous]({{graph:13c-5-piecewise}})

*Graph 13C-5: A piecewise function sewn together at $x=1$. The left piece $x^2+1$ and the right piece $2x$ both arrive at height $2$, so the open circle of the left piece is filled by the closed dot of the right one — no break.*

**A constant that makes a piecewise function continuous** (§2.5 #47): find $c$ so that

$$f(x)=\begin{cases}cx^2+2x, & x<2\\ x^3-cx, & x\ge2\end{cases}$$

is continuous everywhere. The only place to check is the seam $x=2$:

$$4c+4=8-2c \quad\Longrightarrow\quad 6c=4 \quad\Longrightarrow\quad c=\frac23 .$$

**Continuity on a closed interval** (§2.5 Example 4): $f(x)=1-\sqrt{1-x^2}$ is continuous on $[-1,1]$. Inside $(-1,1)$ it is a composition of continuous functions; at the endpoints Stewart checks the *one-sided* limits $\lim_{x\to-1^+}f(x)=1=f(-1)$ and $\lim_{x\to1^-}f(x)=1=f(1)$.

![Continuity on a closed interval]({{graph:13c-4-continuity-interval}})

*Graph 13C-4: $f(x)=1-\sqrt{1-x^2}$ is the lower half of the circle $x^2+(y-1)^2=1$. It is continuous across the whole closed interval $[-1,1]$, including the endpoints where the curve meets the axis.*

> **Geometric insight**: "Continuous on $[a,b]$" means continuous on the open inside *and* continuous from the right at $a$ and from the left at $b$. The endpoint conditions are exactly what makes the closed interval different from the open one.

---

## Part C: The Intermediate Value Theorem — Roots Must Exist

---

## Example 4: Proving a Root Exists Without Solving (§2.5 IVT, Ex 10)

Stewart's **Intermediate Value Theorem** (Theorem 10): if $f$ is continuous on the closed interval $[a,b]$ and $N$ lies between $f(a)$ and $f(b)$, then there is a number $c$ in $(a,b)$ with $f(c)=N$.

The everyday version: a continuous graph cannot jump over a horizontal line. So if a continuous function changes sign, it must cross $0$ somewhere.

**Stewart's Example 10** shows that $4x^3-6x^2+3x-2=0$ has a solution between $1$ and $2$.

① Define $f(x)=4x^3-6x^2+3x-2$. It is a polynomial, hence continuous on $[1,2]$.

② Evaluate the endpoints: $f(1)=4-6+3-2=-1<0$ and $f(2)=32-24+6-2=12>0$.

③ The target value $N=0$ lies between $f(1)$ and $f(2)$. By the IVT there is a $c$ in $(1,2)$ with $f(c)=0$.

Stewart then *narrows* the root: since $f(1.2)<0<f(1.3)$, a solution lies in $(1.2,1.3)$; repeating gives $(1.22,1.23)$.

![Intermediate Value Theorem — sign change forces a root]({{graph:13c-3-ivt}})

*Graph 13C-3: $f(x)=4x^3-6x^2+3x-2$ is below the axis at $x=1$ (blue) and above it at $x=2$ (green). Because $f$ is continuous, the graph must cross the axis between them — the root sits at $c\approx1.22$.*

**Stewart's exercise bank** (#55–58) uses exactly this template:

- #55: $-x^3+4x+1=0$ on $(-1,0)$: $f(-1)=-2<0$, $f(0)=1>0$.
- #57: $e^x=3-2x$ on $(0,1)$: define $f(x)=e^x+2x-3$; $f(0)=-2<0$, $f(1)=e-1>0$.

> **Geometric insight**: The IVT is a *hypothesis-checking* tool, not a solving tool. You never find $c$ — you prove it exists by showing continuity and a sign change. That is enough for existence questions.
>
> **Caution**: the hypothesis matters. On $[-1,1]$ the function $1/x$ changes sign but is not continuous there, so it has no root — Stewart's exercise #52 makes this explicit.

---

## Part D: The Squeeze Theorem — Trap an Oscillation

---

## Example 5: The Squeeze Theorem at a Point and at Infinity (§2.3 Thm 3, Ex 11)

Stewart's **Squeeze Theorem** (§2.3, Theorem 3): if $f(x)\le g(x)\le h(x)$ near $a$, and $\lim_{x\to a}f(x)=\lim_{x\to a}h(x)=L$, then $\lim_{x\to a}g(x)=L$.

**Stewart's Example 11**: $\displaystyle\lim_{x\to0}x^2\sin\frac1x=0$.

① $\sin\frac1x$ has no limit at $0$ — it oscillates between $-1$ and $1$.

② Multiply $-1\le\sin\frac1x\le1$ by $x^2\ge0$: $-x^2\le x^2\sin\frac1x\le x^2$.

③ Both outer bounds go to $0$, so the trapped function does too.

![Squeeze — x² sin(1/x) trapped between ±x²]({{graph:13c-2-squeeze}})

*Graph 13C-2: The oscillation $x^2\sin(1/x)$ is pinned between $\pm x^2$. As the parabolas pinch shut at the origin, the oscillation is forced to $0$ — the limit exists even though $\sin(1/x)$ alone has none.*

**The same theorem at infinity** (Stewart's §2.6 exercise #36):

$$\lim_{x\to\infty}\frac{\sin^2 x}{x^2+1}=0, \qquad\text{because } 0\le\frac{\sin^2 x}{x^2+1}\le\frac{1}{x^2+1}\to0 .$$

> **Geometric insight**: The Squeeze Theorem is how a bounded oscillation is tamed. It appears three times in this chapter — at a point (here), at infinity (13B), and in sequences (Part E) — always with the same two bracketing functions.

---

## Part E: Sequences — Limits at Infinity with Integer Steps

---

## Example 6: Sequences Behave Like Functions at Infinity (§11.1 #27–33, #86–87)

A **sequence** $a_1,a_2,a_3,\dots$ is a function whose input runs over the integers $n=1,2,3,\dots$. Stewart's §11.1 defines $\lim_{n\to\infty}a_n=L$ exactly as for functions: the terms can be made arbitrarily close to $L$ by taking $n$ large.

**Direct computation** — divide by the highest power of $n$, exactly as in 13B:

$$\lim_{n\to\infty}\frac{5}{n+2}=0, \qquad
\lim_{n\to\infty}\frac{4n^2-3n}{2n^2+1}=2, \qquad
\lim_{n\to\infty}3^n7^{-n}=\lim_{n\to\infty}\left(\frac37\right)^n=0 .$$

**The Monotonic Sequence Theorem**: an increasing sequence that is bounded above must converge. This is the sequence version of "the graph cannot escape a ceiling," and it is how the hard recursive sequences are handled.

**Stewart's #86**: $a_1=\sqrt2$, $a_{n+1}=\sqrt{2+a_n}$.

① By induction $a_n$ is increasing and $a_n<3$, so the limit $L$ exists.

② Let $n\to\infty$ in the recursion. Since $\sqrt{\phantom{x}}$ is continuous, the limit passes through the root:

$$L=\sqrt{2+L} \quad\Longrightarrow\quad L^2-L-2=0 \quad\Longrightarrow\quad L=2 .$$

**Stewart's #87**: $a_1=1$, $a_{n+1}=3-\dfrac{1}{a_n}$ satisfies $a_n<3$ and is increasing, so it converges to $L$ with

$$L=3-\frac1L \quad\Longrightarrow\quad L^2-3L+1=0 \quad\Longrightarrow\quad L=\frac{3+\sqrt5}{2}\approx2.618 .$$

> **Geometric insight**: "Monotone + bounded $\Rightarrow$ convergent" is the engine behind every recursive-sequence problem. Once convergence is guaranteed, the limit equation $L=f(L)$ — a **fixed point** — turns the recursion into ordinary algebra.

---

## Common Mistakes

### Mistake 1: Confusing "the limit exists" with "the function is continuous"

**Wrong**: "$\lim_{x\to2}f(x)=2$, so $f(2)=2$." **Right**: the limit and the function value are independent. Continuity is exactly the extra statement that they agree.

### Mistake 2: Applying the IVT to a discontinuous function

**Wrong**: "$1/x$ changes sign on $[-1,1]$, so it has a root." **Right**: the IVT requires continuity on the whole closed interval. $1/x$ fails at $0$ and indeed has no root.

### Mistake 3: Assuming "increasing and bounded above" pins down the bound

**Wrong**: "the limit equals the bound." **Right**: monotone + bounded guarantees convergence to *some* $L$ that is at most the bound — the actual $L$ comes from solving $L=f(L)$.

### Mistake 4: Checking only the seam and ignoring the pieces

**Wrong**: for a piecewise function, only testing the boundary point. **Right**: each piece must also be continuous on its own interval (use Theorems 4, 5, 7, 9), and then the seam is matched with a one-sided limit check.

---

## What We Just Did

```
(1) Continuity = f(a) defined + lim_{x→a} f(x) exists + the two agree.   (§2.5 Def 1)
    Failure types: removable (hole), jump, infinite.                     (§2.5 Ex 1–2)

(2) Continuity is inherited: sums, products, quotients, compositions of  (§2.5 Thm 4, 5, 7, 9)
    polynomial / rational / root / trig / exp / log functions are continuous
    on their domains.

(3) Repair a removable hole by defining f(a) = lim_{x→a} f(x).           (§2.5 #25–26)
    Match a piecewise function at the seam: left limit = right limit = value. (§2.5 #47–48)

(4) IVT: continuous on [a,b] + N between f(a), f(b) ⇒ some c has f(c)=N. (§2.5 Thm 10, Ex 10)
    Used to prove a root exists without solving.

(5) Squeeze: f ≤ g ≤ h with equal outer limits ⇒ inner limit is the same.(§2.3 Thm 3, Ex 11)

(6) Sequences: n → ∞ like x → ∞. Monotone + bounded ⇒ convergent;   (§11.1 #27–33, #86–87)
    then solve the fixed-point equation L = f(L).
```

---

## Basic Drills

> Pure fluency: classify a discontinuity, evaluate a limit by continuity, or take a sequence limit.

**D1.** (§2.5 #13) Show that $f(x)=3x^2+(x+2)^5$ is continuous at $a=-1$ using the definition.

**D2.** (§2.5 #19) Explain why $f(x)=\dfrac{1}{x+2}$ is discontinuous at $a=-2$.

**D3.** (§2.5 #21) Explain why $f(x)=\begin{cases}x+3,&x\le-1\\ 2^{x},&x>-1\end{cases}$ is discontinuous at $a=-1$. Classify the type.

**D4.** (§2.5 #22) Explain why $f(x)=\begin{cases}\frac{x^2-x}{x^2-1},&x\neq1\\ 1,&x=1\end{cases}$ is discontinuous at $x=1$. Classify the type.

**D5.** (§2.5 #25) Show $f(x)=\dfrac{x-3}{x^2-9}$ has a removable discontinuity at $x=3$, and redefine $f(3)$ to remove it.

**D6.** (§2.5 #26) Show $f(x)=\dfrac{x^2-7x+12}{x-3}$ has a removable discontinuity at $x=3$, and redefine $f(3)$ to remove it.

**D7.** (§2.5 #35) Evaluate $\displaystyle\lim_{x\to2}x\sqrt{20-x^2}$ using continuity.

**D8.** (§2.5 #36) Evaluate $\displaystyle\lim_{\theta\to\pi/2}\sin\bigl(\tan(\cos\theta)\bigr)$ using continuity.

**D9.** (§2.5 #37) Evaluate $\displaystyle\lim_{x\to1}\ln\!\left(\frac{5-x^2}{1+x}\right)$ using continuity.

**D10.** (§11.1 #27) Find $\displaystyle\lim_{n\to\infty}\frac{5}{n+2}$.

**D11.** (§11.1 #29) Find $\displaystyle\lim_{n\to\infty}\frac{4n^2-3n}{2n^2+1}$.

**D12.** (§11.1 #33) Find $\displaystyle\lim_{n\to\infty}3^{n}7^{-n}$.

> Solutions: [Solutions](solutions/13C-solutions.md#basic-drill)

---

## Advanced Drills

> Multi-step: solve for constants, prove a root exists, or settle a recursive sequence.

**A1.** (§2.5 #47) Find the value of $c$ that makes $f(x)=\begin{cases}cx^2+2x,&x<2\\ x^3-cx,&x\ge2\end{cases}$ continuous on $(-\infty,\infty)$.

**A2.** (§2.5 #48) Find $a$ and $b$ that make $f$ continuous everywhere:
$$f(x)=\begin{cases}\frac{x^2-4}{x-2},&x<2\\ ax^2-bx+3,&2\le x<3\\ 2x-a+b,&x\ge3\end{cases}$$

**A3.** (§2.5 #51a) Is the discontinuity of $f(x)=\dfrac{x^4-1}{x-1}$ at $a=1$ removable? If so, find a continuous $g$ that agrees with $f$ off $a$.

**A4.** (§2.5 #51b) Same question for $f(x)=\dfrac{x^3-x^2-2x}{x-2}$ at $a=2$.

**A5.** (§2.5 #53) If $f(x)=x^2+10\sin x$, show there is a number $c$ with $f(c)=1000$.

**A6.** (§2.5 #55) Use the IVT to show $-x^3+4x+1=0$ has a solution in $(-1,0)$.

**A7.** (§2.5 #57) Use the IVT to show $e^{x}=3-2x$ has a solution in $(0,1)$.

**A8.** (§2.5 #73) Show that $f(x)=\begin{cases}x^4\sin(1/x),&x\neq0\\ 0,&x=0\end{cases}$ is continuous on $(-\infty,\infty)$.

**A9.** (§2.5 #65) Prove that $f$ is continuous at $a$ if and only if $\displaystyle\lim_{h\to0}f(a+h)=f(a)$.

**A10.** (§11.1 #86) For $a_1=\sqrt2$, $a_{n+1}=\sqrt{2+a_n}$, show the sequence converges and find its limit.

**A11.** (§11.1 #87) For $a_1=1$, $a_{n+1}=3-\dfrac{1}{a_n}$, show $a_n$ is increasing with $a_n<3$, deduce convergence, and find the limit.

<details>
<summary>💡 Hint</summary>

For **A2**, match the pieces at *both* seams $x=2$ and $x=3$; that gives two equations in $a$ and $b$.

For **A5**, evaluate $f$ at two convenient points — say $0$ and $1000$ — and compare them with $1000$.

For **A8**, handle $x\neq0$ with Theorems 4, 7, 9 and handle $x=0$ with the Squeeze Theorem on $|x^4\sin(1/x)|\le x^4$.

For **A10/A11**, first quote the Monotonic Sequence Theorem, then pass the limit through the recursion to get $L=f(L)$.

</details>

> Solutions: [Solutions](solutions/13C-solutions.md#advanced-drill)

---

## Today's Procedure

```
Step 1: Continuity check — three conditions:
    (a) f(a) is defined;  (b) lim_{x→a} f(x) exists;  (c) they are equal.   (§2.5 Def 1)
    If it fails, classify: removable (hole), jump, or infinite.              (§2.5 Ex 2)

Step 2: For a formula, do not check from scratch — use Theorems 4, 5, 7, 9.  (§2.5 Thm 4–9)
    Polynomials and rationals are continuous on their domains; compositions too.

Step 3: Piecewise → match the seam: left limit = right limit = f(a).         (§2.5 #47–48)
    Removable hole → define f(a) = lim_{x→a} f(x).                           (§2.5 #25–26)

Step 4: IVT — if f is continuous on [a,b] and f(a), f(b) straddle N, a c exists.(§2.5 Thm 10)
    Squeeze — bracket the ugly part between two functions with a common limit. (§2.3 Thm 3)

Step 5: Sequences — treat n → ∞ like x → ∞. Monotone + bounded ⇒ convergent; (§11.1)
    then the limit solves L = f(L).
```

---

## How to Read These Symbols

| Symbol | Reads as | Meaning |
|:---:|:---:|------|
| continuous at $x=a$ | "continuous at x equals a" | $\lim_{x\to a}f(x)=f(a)$ — no break, jump, or hole (§2.5 Def 1) |
| $\lim_{x\to a^-}f(x)=f(a)$ | "continuous from the left" | endpoint continuity for a closed interval (§2.5 Def 3) |
| removable discontinuity | "removable discontinuity" | limit exists; patch by redefining $f(a)$ |
| jump discontinuity | "jump discontinuity" | the two one-sided limits exist but differ |
| infinite discontinuity | "infinite discontinuity" | the limit is $\pm\infty$ |
| IVT | "I V T" / Intermediate Value Theorem | continuous $f$ on $[a,b]$ hits every value between $f(a)$, $f(b)$ (§2.5 Thm 10) |
| $[a,b]$ | "closed interval a b" | includes the endpoints — required for the IVT |
| $(a,b)$ | "open interval a b" | excludes the endpoints |
| Squeeze Theorem | "squeeze" / "sandwich" | $f\le g\le h$ with equal outer limits forces the inner limit (§2.3 Thm 3) |
| $\lim_{n\to\infty}a_n=L$ | "limit of the sequence" | the terms approach $L$ as $n$ grows (§11.1) |
| monotone | "monotonic sequence" | always increasing or always decreasing |
| bounded | "bounded sequence" | $m\le a_n\le M$ for every $n$ |
| $L=f(L)$ | "fixed point" | the limit equation of a recursion |

---

## Terminology

| What we call it | Math term | Notation |
|:---------------:|:---------:|:--------:|
| no break | continuity at a point | $\lim_{x\to a}f(x)=f(a)$ |
| inherited continuity | continuity of combinations | Theorems 4, 5, 7, 9 |
| hole | removable discontinuity | limit exists, $f(a)$ missing or wrong |
| jump | jump discontinuity | left limit $\neq$ right limit |
| blow-up | infinite discontinuity | limit is $\pm\infty$ |
| patched value | removable redefinition | $f(a):=\lim_{x\to a}f(x)$ |
| seam | boundary point of a piecewise function | match one-sided limits |
| root guaranteed | Intermediate Value Theorem | continuous $f$ changes sign |
| trap it | Squeeze Theorem | $f(x)\le g(x)\le h(x)$ |
| monotone + bounded | Monotonic Sequence Theorem | guarantees convergence |
| fixed point | limit equation of a recursion | $L=f(L)$ |




