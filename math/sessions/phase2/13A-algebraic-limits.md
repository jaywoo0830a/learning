# Session 13A: Algebraic Limits — The $\frac{0}{0}$ Toolkit

**Phase 2 — Classical Techniques | 75 min**

*Prerequisites: 07 (polynomial factoring), 11A (trig foundations), 10A (exponents & logarithms)*

> 💡 **Stuck?** Every problem has a collapsible **Hint** below it — click it only when you need a nudge.

> **Source.** Every example and drill below is drawn from Stewart, *Calculus*, Section 2.3 (Calculating Limits Using the Limit Laws) and Section 2.2 (The Limit of a Function). Each item cites its example or exercise number in those sections. The Limit Laws, the Direct Substitution Property, and the Squeeze Theorem are Stewart's; the graphs redraw Stewart's Figures 1, 4, 5, and 8 of §2.3.

---

## Part A: The Limit Laws — Plug In When You Are Allowed

---

## Example 1: Reading Limits Off the Limit Laws (§2.3 Limit Laws, Ex 1)

Stewart's five Limit Laws say that limits pass straight through the four arithmetic operations. If $\lim_{x\to a}f(x)$ and $\lim_{x\to a}g(x)$ both exist, then

$$\lim_{x\to a}\bigl[f(x)+g(x)\bigr]=\lim_{x\to a}f(x)+\lim_{x\to a}g(x),\qquad
\lim_{x\to a}\bigl[f(x)g(x)\bigr]=\lim_{x\to a}f(x)\cdot\lim_{x\to a}g(x),$$

$$\lim_{x\to a}\frac{f(x)}{g(x)}=\frac{\lim_{x\to a}f(x)}{\lim_{x\to a}g(x)}\quad\text{provided }\lim_{x\to a}g(x)\neq 0 .$$

The rule to remember is the **Quotient Law's fine print**: it is legal only when the bottom limit is not $0$. Every hard case in this session is a case where that fine print blocks the shortcut.

**Stewart's Example 1** applies the laws to graphs of $f$ and $g$ at $x=-2$, $1$, and $2$. At $x=-2$ the limits are $1$ and $-1$, so

$$\lim_{x\to-2}\bigl[f(x)+5g(x)\bigr]=1+5(-1)=-4 .$$

At $x=2$ the graphs give $\lim_{x\to2}g(x)=0$, so the Quotient Law is forbidden and $\lim_{x\to2}\frac{f(x)}{g(x)}$ does not exist.

> **Geometric insight**: The laws are bookkeeping, not new mathematics. They let you split one hard limit into several easy ones — until a denominator hits $0$ and the bookkeeping stops.

---

## Example 2: Direct Substitution — Why Plugging In Usually Works (§2.3 Direct Substitution Property)

Stewart proves a **Direct Substitution Property**: if $f$ is a polynomial, or a rational function, or a root, trigonometric, exponential, or logarithmic function, then

$$\lim_{x\to a}f(x)=f(a)$$

at every point $a$ where $f(a)$ is defined. (Section 2.5 later names the reason: such functions are *continuous* on their domains.)

So the very first move on any limit problem is **plug in the number**:

$$\lim_{x\to 5}(4x^2-5x)=4(25)-25=75, \qquad \lim_{x\to -2}(3x-7)=-6-7=-13,$$

$$\lim_{x\to 7}\frac{3t^2+1}{t^2-5t+2}\Big|_{t=7}=\frac{148}{16}=\frac{37}{4}, \qquad \lim_{u\to-2}\sqrt{9-u^3+2u^2}=\sqrt{9+8+8}=5 .$$

> **Geometric insight**: Direct substitution is not a trick — it is the definition of continuity in disguise. It fails only when the function is undefined at $a$, and then $\frac{0}{0}$ (or $\frac{\text{nonzero}}{0}$) appears.

---

## Part B: $\frac{0}{0}$ — Factor, Cancel, Evaluate

---

## Example 3: A Hole in a Straight Line (§2.3 Ex 3)

$$\lim_{x\to 2}\frac{x^2-4}{x-2}.$$

① Plug in $x=2$: $\dfrac{0}{0}$ — the Quotient Law is blocked.

② Factor the numerator as a difference of squares: $x^2-4=(x-2)(x+2)$.

③ Cancel the common factor $x-2$. Since $x\neq 2$ while we take the limit, $x-2\neq 0$ and cancelling is legal:

$$\frac{(x-2)(x+2)}{x-2}=x+2 \qquad (x\neq 2).$$

④ Now direct substitution works: $2+2=4$.

![0/0 limit — a hole at x=2]({{graph:13a-1-hole}})

*Graph 13A-1: $\dfrac{x^2-4}{x-2}$ is the line $y=x+2$ with the single point $(2,4)$ removed. The limit asks "what height fills the hole?" — the answer is $4$.*

**Stewart's Example 4** makes the fine point explicit. The function

$$g(x)=\begin{cases}x+1, & x\neq 1\\ \pi, & x=1\end{cases}$$

also satisfies $\lim_{x\to1}g(x)=2$, even though $g(1)=\pi$. The limit never looks at the value at the point.

**Stewart's Example 5** applies the same cancel to a formula that appears constantly in derivative work:

$$\lim_{h\to 0}\frac{(3+h)^2-9}{h}=\lim_{h\to0}\frac{9+6h+h^2-9}{h}=\lim_{h\to0}\frac{h(6+h)}{h}=\lim_{h\to0}(6+h)=6 .$$

> **Geometric insight**: The cancelled factor is exactly the "hole-maker." Once it is gone, the remaining expression is continuous at the point, and direct substitution finishes the job. This is the whole engine of §2.3.

---

## Part C: $\frac{0}{0}$ with Radicals — Multiply by the Conjugate

---

## Example 4: The Conjugate Clears the Root (§2.3 Ex 6)

Factoring cannot help when a square root makes the $\frac{0}{0}$. The weapon is the **conjugate**: multiply numerator and denominator by $\sqrt{A}+B$ so that the difference of roots becomes a difference of squares.

$$\lim_{t\to 0}\frac{\sqrt{t^2+9}-3}{t^2}.$$

① Plug in $t=0$: $\dfrac{0}{0}$.

② Multiply top and bottom by the conjugate $\sqrt{t^2+9}+3$:

$$\frac{\sqrt{t^2+9}-3}{t^2}\cdot\frac{\sqrt{t^2+9}+3}{\sqrt{t^2+9}+3}
=\frac{(t^2+9)-9}{t^2\bigl(\sqrt{t^2+9}+3\bigr)}.$$

③ The root is gone from the numerator. The numerator is now $t^2$, so cancel $t^2$:

$$\frac{t^2}{t^2\bigl(\sqrt{t^2+9}+3\bigr)}=\frac{1}{\sqrt{t^2+9}+3}.$$

④ Direct substitution: $\dfrac{1}{\sqrt{9}+3}=\dfrac{1}{6}$.

Stewart's Example 1 of §2.2 estimated this same limit numerically and guessed $0.1666\ldots$; the conjugate now proves the guess exactly.

![Conjugate: (√(x+4)−2)/x has a hole at (0, 1/4)]({{graph:13a-2-conjugate}})

*Graph 13A-2: The conjugate rewrite turns $\dfrac{\sqrt{x+4}-2}{x}$ into $\dfrac{1}{\sqrt{x+4}+2}$, which is continuous at $0$. The hole at $\bigl(0,\tfrac14\bigr)$ is the limit.*

> **Geometric insight**: The conjugate is not a new idea — it is the difference-of-squares identity $\bigl(\sqrt{A}-B\bigr)\bigl(\sqrt{A}+B\bigr)=A-B^2$ applied on purpose. It converts a root into a polynomial so that Example 3's cancel can run.

---

## Part D: The Trig Standard Limit — $\frac{\sin\square}{\square}\to 1$

---

## Example 5: The Most Important Trigonometric Limit (§2.2 Ex 2, §2.3 Ex 11)

Stewart's §2.2 Example 2 builds the table

| $x$ | $\pm 0.5$ | $\pm 0.1$ | $\pm 0.01$ | $\pm 0.001$ |
|:---:|:---:|:---:|:---:|:---:|
| $\dfrac{\sin x}{x}$ | $0.958851$ | $0.998334$ | $0.999983$ | $0.9999998$ |

and concludes

$$\lim_{x\to 0}\frac{\sin x}{x}=1 .$$

(§2.3 Example 11 later gives the rigorous proof, using the Squeeze Theorem and the inequality $\sin\theta<\theta$ from §3.3.)

![sin x / x → 1]({{graph:13a-3-sinx-over-x}})

*Graph 13A-3: $\dfrac{\sin x}{x}$ dips and rises but is pulled to height $1$ at the origin. The hole at $(0,1)$ is the limit.*

**The one rule that matters**: $\dfrac{\sin\square}{\square}\to 1$ only when the two $\square$ symbols are **exactly the same expression**. Force them to match by multiplying and dividing.

$$\lim_{\theta\to 0}\frac{\sin 3\theta}{\tan 2\theta}=\lim_{\theta\to0}\frac{\sin3\theta}{3\theta}\cdot\frac{2\theta}{\sin2\theta}\cdot\frac{3\theta}{2\theta}\cdot\cos2\theta
=\frac{3}{2}\cdot 1=\frac{3}{2}. \qquad\text{(§2.2 \#25)}$$

$$\lim_{x\to 0}\frac{\sin 5x}{\sin 2x}=\frac{\sin5x}{5x}\cdot\frac{2x}{\sin2x}\cdot\frac{5}{2}\longrightarrow 1\cdot1\cdot\frac{5}{2}=\frac{5}{2}.$$

$$\lim_{x\to0}\frac{\tan x}{x}=\lim_{x\to0}\frac{\sin x}{x}\cdot\frac{1}{\cos x}=1\cdot 1=1, \qquad
\lim_{x\to0}\frac{1-\cos x}{x^2}=\lim_{x\to0}\frac{2\sin^2(x/2)}{x^2}=\frac{1}{2}.$$

> **Geometric insight**: For small $x$ measured in radians, the arc, the sine, and the tangent are interchangeable — $\sin x\approx x\approx\tan x$. The three limits above are the arithmetic shadow of that single geometric fact.

---

## Part E: One-Sided Limits — Check Left and Right Separately

---

## Example 6: When the Two Sides Disagree (§2.3 Ex 7–10)

Stewart's Theorem 1 of §2.3 says

$$\lim_{x\to a}f(x)=L \quad\Longleftrightarrow\quad \lim_{x\to a^-}f(x)=L=\lim_{x\to a^+}f(x).$$

So when the two one-sided limits differ, the two-sided limit does not exist.

**Stewart's Example 7** shows $\lim_{x\to0}|x|=0$ by splitting $|x|=x$ for $x>0$ and $|x|=-x$ for $x<0$. **Stewart's Example 8** uses the same split on the ratio:

$$\lim_{x\to0^+}\frac{|x|}{x}=\lim_{x\to0^+}\frac{x}{x}=1, \qquad
\lim_{x\to0^-}\frac{|x|}{x}=\lim_{x\to0^-}\frac{-x}{x}=-1 .$$

The two sides differ, so $\lim_{x\to0}\dfrac{|x|}{x}$ does not exist.

![One-sided limits — left ≠ right]({{graph:13a-4-onesided}})

*Graph 13A-4: $\dfrac{|x|}{x}$ is the flat line $y=1$ to the right and $y=-1$ to the left. The open circles at $(0,1)$ and $(0,-1)$ show that neither value is attained, and the two sides never meet.*

**Stewart's Example 9** handles a piecewise function at the seam:

$$f(x)=\begin{cases}\sqrt{x-4}, & x>4\\ 8-2x, & x<4\end{cases}
\quad\Longrightarrow\quad \lim_{x\to4^+}f(x)=0=\lim_{x\to4^-}f(x),$$

so the two-sided limit exists and equals $0$.

**Stewart's Example 10** handles the greatest-integer (floor) function $\lfloor x\rfloor$:

$$\lim_{x\to3^+}\lfloor x\rfloor=3, \qquad \lim_{x\to3^-}\lfloor x\rfloor=2, \qquad \text{so } \lim_{x\to3}\lfloor x\rfloor \text{ does not exist.}$$

> **Geometric insight**: A limit exists exactly when the graph arrives at the same height from both directions. A jump, a hole you cannot fill, or two different flats all break that agreement — and each is caught by comparing the one-sided limits.

---

## Part F: The Squeeze Theorem — Trap an Untouchable Function

---

## Example 7: Squeezing an Oscillation to Zero (§2.3 Squeeze Theorem, Ex 11)

Stewart's **Squeeze Theorem** (§2.3, Theorem 3): if $f(x)\le g(x)\le h(x)$ near $a$, and

$$\lim_{x\to a}f(x)=\lim_{x\to a}h(x)=L, \qquad\text{then}\qquad \lim_{x\to a}g(x)=L .$$

It is used exactly when a piece of the function oscillates so wildly that its own limit does not exist.

**Stewart's Example 11** evaluates $\displaystyle\lim_{x\to0}x^2\sin\frac{1}{x}$.

① $\sin\frac1x$ does not have a limit at $0$ — it oscillates between $-1$ and $1$. So the Product Law cannot be used.

② But $-1\le\sin\frac1x\le1$ always. Multiply by the non-negative $x^2$:

$$-x^2\;\le\; x^2\sin\frac{1}{x}\;\le\; x^2 .$$

③ $\displaystyle\lim_{x\to0}(-x^2)=0$ and $\displaystyle\lim_{x\to0}x^2=0$ — the two outer functions share the limit $0$.

④ By the Squeeze Theorem the trapped function must also go to $0$:

$$\lim_{x\to0}x^2\sin\frac{1}{x}=0 .$$

![Squeeze: x² sin(1/x) trapped between −x² and x²]({{graph:13a-5-squeeze}})

*Graph 13A-5: The red oscillation $x^2\sin(1/x)$ is pinned between the blue parabolas $\pm x^2$. As the parabolas pinch shut at the origin, the oscillation is forced to $0$.*

The same trick handles a function at infinity:

$$\lim_{x\to\infty}\frac{\sin x}{x}=0, \qquad\text{because } -\frac{1}{x}\le\frac{\sin x}{x}\le\frac{1}{x}\ \text{ and both bounds go to }0 .$$

> **Geometric insight**: The Squeeze Theorem trades a hard limit for two easy ones. The only requirement is a pair of simple functions that share a limit and bracket the ugly one — the sine's bounded range $-1\le\sin\le1$ supplies the bracket almost every time.

---

## Part G: $\frac{0}{0}$ with Complex Fractions — Combine First

---

## Example 8: A Fraction Inside a Fraction (§2.3 #25–34)

When the numerator or the denominator is itself a fraction, the $\frac{0}{0}$ is pure algebra. The move is always the same: **combine the little fractions into one fraction first**, then cancel.

$$\lim_{x\to 3}\frac{\dfrac{1}{x}-\dfrac{1}{3}}{x-3}. \qquad\text{(§2.3 \#25)}$$

① Plug in $x=3$: the numerator is $\frac13-\frac13=0$ and the denominator is $0$ — form $\frac{0}{0}$.

② Combine the numerator over the common denominator $3x$:

$$\frac{1}{x}-\frac{1}{3}=\frac{3-x}{3x}=\frac{-(x-3)}{3x}.$$

③ The whole expression is now a big fraction. Divide by $x-3$ and cancel the genuine common factor:

$$\frac{\dfrac{-(x-3)}{3x}}{x-3}=\frac{-(x-3)}{3x(x-3)}=-\frac{1}{3x}.$$

④ Direct substitution: $-\dfrac{1}{3\cdot3}=-\dfrac{1}{9}$.

**The general pattern** — this one is the derivative of $1/x$ in disguise:

$$\lim_{x\to a}\frac{\dfrac{1}{x}-\dfrac{1}{a}}{x-a}=-\frac{1}{a^2}.$$

Two more from the same exercise bank:

$$\lim_{t\to 0}\left(\frac{1}{t}-\frac{1}{t^2+t}\right)=\lim_{t\to0}\frac{(t+1)-1}{t(t+1)}=\lim_{t\to0}\frac{1}{t+1}=1, \qquad\text{(§2.3 \#28)}$$

$$\lim_{h\to 0}\frac{(-2+h)^{-1}+2^{-1}}{h}=\lim_{h\to0}\frac{2+(-2+h)}{2(-2+h)\,h}=\lim_{h\to0}\frac{h}{2(-2+h)h}=\lim_{h\to0}\frac{1}{2(-2+h)}=-\frac{1}{4}. \quad\text{(§2.3 \#26)}$$

![Complex fraction: (1/x − 1/3)/(x−3) = −1/(3x) with a hole at (3, −1/9)]({{graph:13a-6-complex-fraction}})

*Graph 13A-6: After combining, $\dfrac{\frac1x-\frac13}{x-3}$ collapses to the hyperbola $-\dfrac{1}{3x}$. The graph has a hole at $\bigl(3,-\tfrac19\bigr)$; the limit is that missing height.*

> **Geometric insight**: A complex fraction is never a new weapon. Combining the pieces exposes a $\frac{0}{0}$ you already know how to beat — factor, cancel, plug in.

---

## Common Mistakes

### Mistake 1: "$\frac{0}{0}$ equals $0$"

**Wrong.** $\frac{0}{0}$ is the signal "race undecided," not a value. Factor, conjugate, or combine to find the real limit.

### Mistake 2: Writing $\frac{\sin 5x}{x}\to 1$

**Wrong.** The two $\square$ symbols must match. $\dfrac{\sin 5x}{x}=5\cdot\dfrac{\sin 5x}{5x}\to 5$, not $1$.

### Mistake 3: Cancelling across a sum

**Wrong**: $\dfrac{\frac1x-\frac13}{x-3}\to$ "cancel the $x$'s." **Right**: combine the numerator into one fraction *first* — $\frac1x-\frac13=\frac{3-x}{3x}$ — and only then cancel the genuine common factor $x-3$. Pieces inside a sum can never be cancelled individually.

### Mistake 4: Using the Quotient Law when the bottom limit is $0$

**Wrong**: applying $\lim\frac{f}{g}=\frac{\lim f}{\lim g}$ when $\lim g=0$. **Right**: that is exactly the case the law forbids; the $\frac{0}{0}$ (or $\frac{\text{nonzero}}{0}$) form must be resolved some other way.

---

## What We Just Did

```
(1) Direct substitution: plug in. If a number comes out, you are done. (§2.3 Direct Substitution Property)

(2) 0/0 → pick the weapon that matches the structure:
    polynomials  → factor and cancel the common zero-maker        (§2.3 Ex 3–5)
    radicals     → multiply by the conjugate (difference of squares)(§2.3 Ex 6)
    trig         → force sin(□)/□ → 1, with matching □            (§2.2 Ex 2, §2.3 Ex 11)
    complex frac → combine the little fractions first, then cancel (§2.3 #25–34)

(3) One-sided: compare left and right. |x| splits at 0; a jump or two flats → DNE. (§2.3 Ex 7–10)

(4) Oscillating factor: bracket it with ±(simple function) and squeeze. (§2.3 Squeeze Theorem, Ex 11)
```

---

## Basic Drills

> Pure fluency: identify the form and apply the one matching weapon. One clean move per item.

**D1.** (§2.3 #3) Evaluate $\displaystyle\lim_{x\to 5}(4x^2-5x)$ by direct substitution.

**D2.** (§2.3 #11) Evaluate $\displaystyle\lim_{x\to -2}(3x-7)$ by direct substitution.

**D3.** (§2.3 #13) Evaluate $\displaystyle\lim_{t\to 4}\frac{t^2-2t-8}{t-4}$. Factor and cancel.

**D4.** (§2.3 #19) Evaluate $\displaystyle\lim_{t\to 3}\frac{t^3-27}{t^2-9}$. Factor a difference of cubes and of squares.

**D5.** (§2.3 #20) Evaluate $\displaystyle\lim_{u\to -1}\frac{u+1}{u^3+1}$. Factor a sum of cubes.

**D6.** (§2.3 #23) Evaluate $\displaystyle\lim_{h\to 0}\frac{\sqrt{9+h}-3}{h}$. Multiply by the conjugate.

**D7.** (§2.3 #27) Evaluate $\displaystyle\lim_{t\to 0}\frac{\sqrt{1+t}-\sqrt{1-t}}{t}$. Multiply by the conjugate.

**D8.** (§2.3 #22) Evaluate $\displaystyle\lim_{x\to 9}\frac{9-x}{3-\sqrt{x}}$. Multiply by the conjugate.

**D9.** (§2.2 #25) Evaluate $\displaystyle\lim_{\theta\to 0}\frac{\sin 3\theta}{\tan 2\theta}$. Match the arguments.

**D10.** (§2.3 #25) Evaluate $\displaystyle\lim_{x\to 3}\frac{\ \frac1x-\frac13\ }{x-3}$. Combine the numerator first.

**D11.** (§2.3 #28) Evaluate $\displaystyle\lim_{t\to 0}\left(\frac1t-\frac{1}{t^2+t}\right)$. Combine into one fraction.

**D12.** (§2.3 Ex 10) Evaluate $\displaystyle\lim_{x\to 3}\lfloor x\rfloor$. Compare the two one-sided limits.

> Solutions: [Solutions](solutions/13A-solutions.md#basic-drill)

---

## Advanced Drills

> Chains two or three moves, and adds the "solve for a constant" and proof items.

**A1.** (§2.3 #66) Evaluate $\displaystyle\lim_{x\to 2}\frac{\sqrt{6-x}-2}{\sqrt{3-x}-1}$. Conjugate the numerator and the denominator.

**A2.** (§2.3 #29) Evaluate $\displaystyle\lim_{x\to 16}\frac{4-\sqrt{x}}{16x-x^2}$. Factor the denominator first.

**A3.** (§2.3 #31) Evaluate $\displaystyle\lim_{t\to 0}\left(\frac{1}{t\sqrt{1+t}}-\frac1t\right)$. Combine into one fraction, then conjugate.

**A4.** (§2.3 #32) Evaluate $\displaystyle\lim_{x\to -4}\frac{\sqrt{x^2+9}-5}{x+4}$. Conjugate the numerator.

**A5.** (§2.3 #33) Evaluate $\displaystyle\lim_{h\to 0}\frac{(x+h)^3-x^3}{h}$, treating $x$ as a constant.

**A6.** (§2.3 #34) Evaluate $\displaystyle\lim_{h\to 0}\frac{\ \frac{1}{(x+h)^2}-\frac{1}{x^2}\ }{h}$, treating $x$ as a constant.

**A7.** (§2.3 #61) If $\displaystyle\lim_{x\to 1}\frac{f(x)-8}{x-1}=10$, find $\displaystyle\lim_{x\to 1}f(x)$.

**A8.** (§2.3 #62) If $\displaystyle\lim_{x\to 0}\frac{f(x)}{x^2}=5$, find $\displaystyle\lim_{x\to 0}f(x)$ and $\displaystyle\lim_{x\to 0}\frac{f(x)}{x}$.

**A9.** (§2.3 #67) Find the number $a$ such that $\displaystyle\lim_{x\to -2}\frac{3x^2+ax+a+3}{x^2+x-2}$ exists, and give the value of the limit.

**A10.** (§2.3 #59) Prove that if $p$ is a polynomial, then $\displaystyle\lim_{x\to a}p(x)=p(a)$.

**A11.** (§2.3 #63) Let $f(x)=x^2$ when $x$ is rational and $f(x)=0$ when $x$ is irrational. Prove $\displaystyle\lim_{x\to 0}f(x)=0$ using the Squeeze Theorem.

<details>
<summary>💡 Hint</summary>

For **A9**, a rational limit at a point where the denominator is $0$ exists only if the numerator is also $0$ there — that gives an equation for $a$. Then factor and cancel.

For **A11**, bracket $f$ with $0\le f(x)\le x^2$: every value of $f(x)$ is either $x^2$ or $0$, and both lie between $0$ and $x^2$.

</details>

> Solutions: [Solutions](solutions/13A-solutions.md#advanced-drill)

---

## Today's Procedure

```
Step 1: Always try direct substitution first. If you get a number, you are done. (§2.3)

Step 2: If you get 0/0, read the structure and pick one weapon:
    polynomial  → factor and cancel the common zero-maker.      (§2.3 Ex 3–5)
    radical     → multiply by the conjugate.                    (§2.3 Ex 6)
    trig        → force sin(□)/□ → 1 (matching □), or (1−cos x)/x² → 1/2. (§2.2 Ex 2)
    complex frac→ combine the little fractions first, then cancel.(§2.3 #25–34)

Step 3: If the point is a ≠ 0, the same moves work — cancel the factor (x−a) directly.
    If a factor oscillates, bracket it with ±(simple function) and squeeze. (§2.3 Ex 11)

Step 4: One-sided problems: evaluate left and right separately.
    |x| splits into two cases; if the two sides disagree, the limit does not exist. (§2.3 Ex 7–10)
```

---

## How to Read These Symbols

| Symbol | Reads as | Meaning |
|:---:|:---:|------|
| $\lim_{x \to a} f(x)$ | "limit as x approaches a of f of x" | the height $f(x)$ approaches as $x$ nears $a$ (never using $x=a$) |
| $\lim_{x \to a^-}$, $\lim_{x \to a^+}$ | "left-hand limit", "right-hand limit" | approach $a$ from smaller / larger values (§2.2 Def 2) |
| $\frac{0}{0}$ | "zero over zero" / indeterminate form | undecided — factor, conjugate, or combine |
| Direct Substitution Property | "plug it in" | $\lim_{x\to a}f(x)=f(a)$ when $f$ is continuous at $a$ (§2.3) |
| Quotient Law | "limit of a quotient" | legal only when the bottom limit is not $0$ (§2.3 Law 5) |
| conjugate | "conjugate" | $\sqrt{A}+B$ paired with $\sqrt{A}-B$; the product is $A-B^2$ |
| $\frac{\sin x}{x} \to 1$ | "sine x over x goes to one" | the fundamental trig limit, valid only with matching arguments (§2.2 Ex 2) |
| Squeeze Theorem | "squeeze" / "sandwich" | $f\le g\le h$ with equal outer limits forces the inner limit (§2.3 Thm 3) |
| DNE | "does not exist" | the left and right limits differ, or the function oscillates |
| $\lfloor x\rfloor$ | "floor x" / greatest integer | the largest integer $\le x$; has a jump at every integer (§2.3 Ex 10) |

---

## Terminology

| What we call it | Math term | Notation |
|:---------------:|:---------:|:--------:|
| plug it in | direct substitution | $\lim_{x\to a}f(x)=f(a)$ |
| the fine print on division | Quotient Law condition | $\lim g\neq0$ required |
| 0/0 undecided | indeterminate form | $\frac{0}{0}$ |
| tear apart | factor | $x^2-a^2=(x-a)(x+a)$ |
| cancel the troublemaker | cancel the common factor | $\frac{\cancel{(x-a)}\,g(x)}{\cancel{x-a}}$ |
| conjugate | rationalization | multiply by $\sqrt{A}+B$ |
| match the square | argument matching | $\frac{\sin 3x}{3x}\to1$ |
| one-sided | left-hand / right-hand limit | $\lim_{x\to a^-}$, $\lim_{x\to a^+}$ |
| trap it | Squeeze Theorem | $f(x)\le g(x)\le h(x)$ |
| hole | removable discontinuity | limit exists, $f(a)$ undefined |
| floor | greatest-integer function | $\lfloor x\rfloor$ |





