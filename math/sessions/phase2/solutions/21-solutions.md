# Solutions — 21: Rigorous Continuity and Derivatives

---

## Practice 1

**Prove $f(x)=5x-3$ is continuous at $x=2$ using ε-δ.**

$f(2)=7$. $|f(x)-f(2)| = |5x-3-7| = 5|x-2|$.

Given $\varepsilon>0$, choose $\delta=\varepsilon/5$. If $|x-2|<\delta$, then $|f(x)-f(2)|=5|x-2|<5\delta=\varepsilon$. ✓

> **Answer**: $\delta = \varepsilon/5$.

---

## Practice 2

**Prove $f(x)=\sqrt{x}$ is continuous at $x=4$ using ε-δ.**

$|\sqrt{x}-2| = \frac{|x-4|}{\sqrt{x}+2} \leq \frac{|x-4|}{2}$ (since $\sqrt{x}+2\geq2$).

Choose $\delta = \min(4, 2\varepsilon)$ (the $\min(4,\cdot)$ keeps $x\geq0$ so $\sqrt{x}$ is real). If $|x-4|<\delta$, then $|\sqrt{x}-2|\leq\frac{|x-4|}{2}<\frac{2\varepsilon}{2}=\varepsilon$. ✓

> **Answer**: $\delta = \min(4, 2\varepsilon)$.

---

## Practice 3

**Use IVT to prove $x^5 - 3x + 1 = 0$ has at least one real root.**

$f(x)=x^5-3x+1$. $f(0)=1>0$; $f(1)=1-3+1=-1<0$. $f$ is a polynomial, hence continuous on $[0,1]$. By IVT, since $0$ lies between $f(0)$ and $f(1)$, there is $c\in(0,1)$ with $f(c)=0$. ✓

> **Answer**: Root in $(0,1)$ by IVT.

---

## Practice 4

**Using the limit definition, find $f'(a)$ for $f(x)=\frac{1}{x}$, $a\neq0$.**

$\frac{f(a+h)-f(a)}{h} = \frac{\frac{1}{a+h}-\frac{1}{a}}{h} = \frac{a-(a+h)}{h\cdot a(a+h)} = \frac{-1}{a(a+h)}$.

As $h\to0$: $a(a+h)\to a^2$, so $f'(a) = -\frac{1}{a^2}$. ✓

> **Answer**: $f'(a) = -1/a^2$.

---

## Practice 5

**Prove the product rule for three functions: $(fgh)' = f'gh + fg'h + fgh'$.**

First apply the two-function product rule to $(fg)$: $(fg)' = f'g + fg'$.

Then $((fg)h)' = (fg)'h + (fg)h' = (f'g+fg')h + fgh' = f'gh + fg'h + fgh'$. ✓

> **Answer**: Apply the product rule twice.

---

## Practice 6: Real Battle

**$f$ satisfies $|f(x)-f(y)| \leq (x-y)^2$ for all $x,y$. Prove (a) continuous everywhere, (b) differentiable everywhere with $f'=0$, (c) $f$ is constant.**

**(a)**: Fix $a$. $|f(x)-f(a)| \leq (x-a)^2 \to 0$ as $x\to a$. So $\lim_{x\to a}f(x)=f(a)$ — continuous at every $a$.

**(b)**: For $x\neq a$: $\left|\frac{f(x)-f(a)}{x-a}\right| \leq |x-a| \to 0$ as $x\to a$. So the difference quotient $\to 0$: $f'(a)=0$ for every $a$.

**(c)**: By MVT (Session 22, Corollary 1): $f'=0$ everywhere ⇒ $f$ is constant. ✓

> **Answer**: Squeeze on the difference quotient gives $f'(a)=0$ everywhere → constant.

---

## Basic Drills

**D1.** $f=2x+7$ at $3$: $|2x+7-13|=2|x-3|<\varepsilon$ → $\delta=\varepsilon/2$.

**D2.** $f=4-x$ at any $a$: $|4-x-(4-a)|=|a-x|=|x-a|<\varepsilon$ → $\delta=\varepsilon$.

**D3.** $f=\frac{x^2-4}{x-2}$ at $2$: $\lim_{x\to2}f=4$ exists but $f(2)$ undefined → **removable** (hole at $(2,4)$).

**D4.** $x^3-2$ on $[1,2]$: $f(1)=-1<0$, $f(2)=6>0$, continuous → root in $(1,2)$ by IVT.

**D5.** $f=3x+1$: $\frac{3(a+h)+1-(3a+1)}{h}=\frac{3h}{h}=3$ → $f'(a)=3$.

**D6.** $f=x^2+2x$: $\frac{(a+h)^2+2(a+h)-(a^2+2a)}{h}=\frac{2ah+h^2+2h}{h}=2a+h+2\to2a+2$.

**D7.** $(f-g)'=f'-g'$: write $f-g=f+(-1)g$; sum rule + constant multiple give $f'+(-1)g'=f'-g'$. ✓

**D8.** $(cf)'=cf'$: $\frac{cf(a+h)-cf(a)}{h}=c\cdot\frac{f(a+h)-f(a)}{h}\to c f'(a)$. ✓

**D9.** $|x-2|$ at $2$: continuous since $||x-2|-0|=|x-2|\to0$. Difference quotients: for $h>0$, $\frac{|2+h-2|}{h}=\frac{h}{h}=1$; for $h<0$, $\frac{|2+h-2|}{h}=\frac{-h}{h}=-1$. Disagree → not differentiable.

**D10.** Negation of "continuous at $a$": $\exists\varepsilon>0\,\forall\delta>0\,\exists x\,(|x-a|<\delta \land |f(x)-f(a)|\geq\varepsilon)$. English: arbitrarily close to $a$ there are points where $f$ jumps by at least $\varepsilon$ from $f(a)$.

**D11.** $\sin(1/x)$ not continuous at $0$ (sequential criterion): take $x_n=\frac{1}{2n\pi}\to0$ → $f(x_n)=\sin(2n\pi)=0\to0$; take $y_n=\frac{1}{2n\pi+\pi/2}\to0$ → $f(y_n)=1\to1$. Different limits → no limit → not continuous.

**D12.** $|x|$ continuous at $0$ (sequential criterion): for any $x_n\to0$, $||x_n|-0|=|x_n|\to0$ → $f(x_n)\to0=f(0)$. ✓

> **Answers**: D1 $\varepsilon/2$; D2 $\varepsilon$; D3 removable; D4 root in (1,2); D5 $3$; D6 $2a+2$; D9 $1$ vs $-1$; D11 two sequences $0$ vs $1$.

---

## Advanced Drills

### A1. $f(x)=x^3$ continuous at any $a$
$|x^3-a^3|=|x-a||x^2+ax+a^2|$. Restrict $\delta\leq1$: $|x|<|a|+1$, so $|x^2+ax+a^2|\leq|x|^2+|a||x|+|a|^2 < (|a|+1)^2+|a|(|a|+1)+|a|^2 =: B$. Choose $\delta=\min(1,\varepsilon/B)$. ✓

### A2. Sign-preserving property
Take $\varepsilon=f(a)/2>0$. Continuity gives $\delta$ with $|f(x)-f(a)|<f(a)/2$, hence $f(x)>f(a)-f(a)/2=f(a)/2$. ✓

### A3. $f(c)=c$ for some $c\in(0,1)$
$g(x)=f(x)-x$ is continuous; $g(0)=f(0)-0=1>0$; $g(1)=f(1)-1=0-1=-1<0$. By IVT, $\exists c\in(0,1)$ with $g(c)=0$, i.e. $f(c)=c$. ✓

### A4. Quotient rule from product + reciprocal
$(f/g)'=(f\cdot(1/g))'=f'(1/g)+f(-g'/g^2)=\frac{f'}{g}-\frac{fg'}{g^2}=\frac{f'g-fg'}{g^2}$. ✓

### A5. Symmetric difference quotient
$\frac{f(a+h)-f(a-h)}{2h}=\frac{f(a+h)-f(a)+f(a)-f(a-h)}{2h}\to\frac{f'(a)+f'(a)}{2}=f'(a)$.
For $f=|x|$ at $a=0$: $\frac{|h|-|-h|}{2h}=0$ for all $h\neq0$, so the symmetric quotient $\to0$ — yet $f$ is not differentiable at $0$. So the converse fails. ✓

### A6. Power rule by induction
Base $n=1$: $\frac{d}{dx}x=1=nx^0$. Step: assume $(x^n)'=nx^{n-1}$. Then $(x^{n+1})'=(x\cdot x^n)'=1\cdot x^n+x\cdot nx^{n-1}=x^n+nx^n=(n+1)x^n$. ✓

### A7. $f(x)=x^2\sin(1/x)$, $f(0)=0$, at $0$
$f'(0)=\lim_{h\to0}\frac{h^2\sin(1/h)}{h}=\lim_{h\to0}h\sin(1/h)=0$ (squeeze: $|h\sin(1/h)|\leq|h|$). So $f'(0)=0$ exists. (For $x\neq0$, $f'(x)=2x\sin(1/x)-\cos(1/x)$, which oscillates — so $f'$ is not continuous at $0$.)

### A8. $|f(x)|\leq x^2$ for all $x$
$|f(0)|\leq0$ → $f(0)=0$. Continuity: $|f(x)-0|\leq x^2\to0$. Derivative: $\left|\frac{f(h)}{h}\right|\leq|h|\to0$ → $f'(0)=0$. ✓

### A9. Chain rule for $g(x)=mx+b$
$\frac{f(m(a+h)+b)-f(ma+b)}{h}=m\cdot\frac{f(ma+b+mh)-f(ma+b)}{mh}$.
As $h\to0$, $mh\to0$, so the second factor $\to f'(ma+b)$. Result: $m f'(mx+b)$. ✓

### A10. Critique the IVT application
The student uses IVT without verifying that $f$ is **continuous** — that's the unstated assumption. Rigorous version: let $f(x)=x^3-1$ on $[0,2]$. $f$ is a polynomial (continuous), $f(0)=-1$, $f(2)=7$, and $2$ is between them. By IVT, $\exists c\in(0,2)$ with $f(c)=2$, i.e. $c^3-1=2$, so $c=\sqrt[3]{3}$. ✓

### A11. $1/g$ continuous where $g(a)\neq0$ (sequential criterion)
For $x_n\to a$: $g(x_n)\to g(a)\neq0$ (continuity of $g$ + quotient law for sequences, Session 20). So $1/g(x_n)\to 1/g(a)$. Hence $1/g$ is continuous at $a$; then $f/g=f\cdot(1/g)$ is continuous (product closure). ✓

### A12. Composition law two ways
(i) *Sequential*: $x_n\to a$ → $g(x_n)\to g(a)$ (continuity of $g$) → $f(g(x_n))\to f(g(a))$ (continuity of $f$ at $g(a)$). So $f\circ g$ is continuous at $a$.
(ii) *ε-δ*: given $\varepsilon>0$, continuity of $f$ at $g(a)$ gives $\eta>0$ with $|y-g(a)|<\eta\Rightarrow|f(y)-f(g(a))|<\varepsilon$. Continuity of $g$ at $a$ gives $\delta>0$ with $|x-a|<\delta\Rightarrow|g(x)-g(a)|<\eta$. Chain: $|x-a|<\delta\Rightarrow|f(g(x))-f(g(a))|<\varepsilon$. ✓
