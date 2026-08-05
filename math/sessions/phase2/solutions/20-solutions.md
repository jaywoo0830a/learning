# Solutions — 20: Rigorous Limits — ε-δ and ε-N

---

## Practice 1

**Prove $\lim_{x \to 1} (4x-3) = 1$ using ε-δ. State δ in terms of ε.**

$|f(x)-L| = |(4x-3)-1| = |4x-4| = 4|x-1|$.

We want $4|x-1| < \varepsilon$, i.e. $|x-1| < \varepsilon/4$.

Choose $\delta = \varepsilon/4$. Then $0 < |x-1| < \delta$ gives $|f(x)-1| = 4|x-1| < 4\delta = \varepsilon$. ✓

> **Answer**: $\delta = \varepsilon/4$ (the linear pattern $\delta = \varepsilon/|m|$ with $m=4$).

---

## Practice 2

**Prove $\lim_{x \to 3} x^2 = 9$ using ε-δ.**

$|x^2 - 9| = |x-3| \cdot |x+3|$.

Restrict $\delta \leq 1$: $|x-3|<1$ means $2 < x < 4$, so $|x+3| < 7$.

Then $|x^2-9| < 7|x-3| < 7\delta$. Choose $\delta = \min(1, \varepsilon/7)$.

**Verification**: If $0<|x-3|<\delta$, then $|x-3|<1$ (so $|x+3|<7$) and $|x-3|<\varepsilon/7$. Multiply: $|x^2-9| < 7 \cdot \varepsilon/7 = \varepsilon$. ✓

> **Answer**: $\delta = \min(1, \varepsilon/7)$.

---

## Practice 3

**Prove $\lim_{n \to \infty} \frac{3n+2}{n} = 3$ using ε-N. Find N in terms of ε.**

$\left|\frac{3n+2}{n} - 3\right| = \left|3 + \frac{2}{n} - 3\right| = \frac{2}{n}$.

We want $\frac{2}{n} < \varepsilon$, i.e. $n > 2/\varepsilon$. Choose $N = \lceil 2/\varepsilon \rceil$.

If $n \geq N$, then $n \geq 2/\varepsilon$, so $\frac{2}{n} \leq \varepsilon$ (strict for $n > 2/\varepsilon$). ✓

> **Answer**: $N = \lceil 2/\varepsilon \rceil$.

---

## Practice 4

**Prove: if $\lim_{x \to a} f(x) = L$ and $L > 0$, then there exists $\delta > 0$ such that $f(x) > L/2$ for all $x$ with $0 < |x-a| < \delta$.**

Take $\varepsilon = L/2 > 0$. The ε-δ definition gives a $\delta > 0$ with $0<|x-a|<\delta \Rightarrow |f(x)-L| < L/2$.

But $|f(x)-L| < L/2$ means $-L/2 < f(x)-L < L/2$, so $f(x) > L - L/2 = L/2$. ✓

> **Answer**: Choose $\varepsilon = L/2$; the definition's $\delta$ works — this is the *sign-preserving* property.

---

## Practice 5

**Prove the product law for sequences: if $\lim a_n = L$ and $\lim b_n = M$, then $\lim (a_n b_n) = LM$.**

Since $b_n \to M$, $b_n$ is bounded: $|b_n| \leq K$ for all $n$ (take $\varepsilon=1$ in the definition, then $|b_n| \leq |M|+1 =: K$).

Write the cross-term trick: $a_n b_n - LM = (a_n - L)b_n + L(b_n - M)$.

Given $\varepsilon > 0$: choose $N_1$ with $n\geq N_1 \Rightarrow |a_n-L| < \frac{\varepsilon}{2(K+1)}$, and $N_2$ with $n\geq N_2 \Rightarrow |b_n-M| < \frac{\varepsilon}{2(|L|+1)}$. Let $N = \max(N_1, N_2)$.

For $n \geq N$:
$|a_n b_n - LM| \leq |a_n-L|\cdot|b_n| + |L|\cdot|b_n-M| < K\cdot\frac{\varepsilon}{2(K+1)} + |L|\cdot\frac{\varepsilon}{2(|L|+1)} < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$. ✓

> **Answer**: Uses boundedness of the convergent sequence $b_n$ + triangle inequality + the $\varepsilon/2$ split.

---

## Practice 6: Real Battle

**A student claims: "$\lim_{x \to 0} \frac{x}{|x|}$ exists because the left and right limits are both finite numbers."**

**(a) One-sided limits**: For $x>0$: $\frac{x}{|x|} = \frac{x}{x} = 1$ → right limit $= 1$. For $x<0$: $\frac{x}{|x|} = \frac{x}{-x} = -1$ → left limit $= -1$.

**(b) Two-sided limit does NOT exist — by negation**: Suppose $L$ is the limit. Choose $\varepsilon = 1$. For any $\delta > 0$, pick $x_1 = \delta/2 > 0$ (so $f(x_1)=1$) and $x_2 = -\delta/2 < 0$ (so $f(x_2)=-1$). Both satisfy $0<|x_i|<\delta$. If both were within $1$ of $L$:
$|1-L| < 1$ and $|-1-L| < 1$ → by triangle inequality $2 = |1-(-1)| \leq |1-L| + |L+1| < 2$ — impossible. So no $L$ works.

**(c) Why the student fails**: "Finite" is not enough — the two-sided limit requires the one-sided limits to be **equal**. Here $1 \neq -1$, so the two-sided limit doesn't exist regardless of both being finite.

> **Answers**: (a) $1$ and $-1$. (b) No two-sided limit (negation with $\varepsilon=1$). (c) Finite $\neq$ equal.

---

## Basic Drills

**D1.** $\lim_{x\to5}(3x+2)=17$: $|3x+2-17|=3|x-5|<\varepsilon$ → $\delta=\varepsilon/3$.

**D2.** $\lim_{x\to-1}(2x-4)=-6$: $|2x-4+6|=2|x+1|<\varepsilon$ → $\delta=\varepsilon/2$.

**D3.** $\lim_{x\to0}5x=0$: $5|x|<\varepsilon$ → $\delta=\varepsilon/5$.

**D4.** $\lim 5/n=0$: $5/n<\varepsilon$ → $N=\lceil 5/\varepsilon\rceil$.

**D5.** $\lim 1/n^2=0$: $1/n^2<\varepsilon$ → $n>1/\sqrt\varepsilon$ → $N=\lceil 1/\sqrt\varepsilon\rceil$.

**D6.** $\lim 2n/(n+1)=2$: $\left|\frac{2n}{n+1}-2\right|=\left|\frac{2n-2n-2}{n+1}\right|=\frac{2}{n+1}<\varepsilon$ → $N=\lceil 2/\varepsilon\rceil$.

**D7.** $\varepsilon=0.01$, $f=3x+1$ at $a=2$: $\delta=\varepsilon/3 \approx 0.0033$.

**D8.** $\varepsilon=0.001$, $1/\sqrt n$: $1/\sqrt n<0.001$ → $\sqrt n>1000$ → $N=10^6$.

**D9.** Negation of $\lim_{x\to a}f(x)=L$: $\exists\varepsilon>0\,\forall\delta>0\,\exists x\,(0<|x-a|<\delta \land |f(x)-L|\geq\varepsilon)$. English: there is a tolerance such that, no matter how close $x$ gets to $a$, $f(x)$ escapes the band infinitely often.

**D10.** $\lim(f-L)=0$: given $\varepsilon>0$, the definition of $\lim f=L$ gives $\delta$ with $|f(x)-L|<\varepsilon$, which is exactly $|(f(x)-L)-0|<\varepsilon$. ✓

**D11.** Negation of $\lim_{n\to\infty}a_n=L$ (ε-N): $\exists\varepsilon>0\,\forall N\,\exists n\geq N\,(|a_n-L|\geq\varepsilon)$. English: eventually never stays within ε — the sequence keeps escaping.

**D12.** $\lim_{x\to1^+}(3x-2)=1$: for $x>1$, $|3x-2-1|=3|x-1|=3(x-1)$. Choose $\delta=\varepsilon/3$. If $0<x-1<\delta$, then $|3x-3|=3(x-1)<3\delta=\varepsilon$. ✓

> **Answers**: D1 $\varepsilon/3$; D2 $\varepsilon/2$; D3 $\varepsilon/5$; D4 $\lceil5/\varepsilon\rceil$; D5 $\lceil1/\sqrt\varepsilon\rceil$; D6 $\lceil2/\varepsilon\rceil$; D7 $0.0033$; D8 $10^6$; D11 $\exists\varepsilon\forall N\exists n\geq N(|a_n-L|\geq\varepsilon)$; D12 $\varepsilon/3$.

---

## Advanced Drills

### A1. $\lim_{x\to1}(x^2+x)=2$
$|x^2+x-2|=|(x-1)(x+2)|$. Restrict $\delta\leq1$: $0<x<2$ → $|x+2|<4$. Then $|x^2+x-2|<4|x-1|$. Choose $\delta=\min(1,\varepsilon/4)$. ✓

### A2. $\lim_{x\to4}\sqrt{x}=2$
$|\sqrt{x}-2|=\frac{|x-4|}{\sqrt{x}+2}$. Restrict $\delta\leq1$: $x\in(3,5)$ → $\sqrt{x}+2>3$. Then $|\sqrt{x}-2|<\frac{|x-4|}{3}$. Choose $\delta=\min(1,3\varepsilon)$. ✓

### A3. $\lim_{n\to\infty}\frac{n^2+1}{2n^2+3}=\frac12$
$\left|\frac{n^2+1}{2n^2+3}-\frac12\right|=\left|\frac{2n^2+2-2n^2-3}{2(2n^2+3)}\right|=\frac{1}{2(2n^2+3)}<\frac{1}{4n^2}$. Want $\frac{1}{4n^2}<\varepsilon$ → $n>\frac{1}{2\sqrt\varepsilon}$ → $N=\lceil 1/(2\sqrt\varepsilon)\rceil$. ✓

### A4. Quotient law for sequences
Since $b_n\to M\neq0$, eventually $|b_n|>|M|/2$ (take $\varepsilon=|M|/2$). Then:
$|1/b_n-1/M|=\frac{|M-b_n|}{|b_n||M|}<\frac{2|b_n-M|}{M^2}$.
Given $\varepsilon$, pick $N$ with $|b_n-M|<\varepsilon M^2/2$; then $|1/b_n-1/M|<\varepsilon$. So $1/b_n\to1/M$, and $a_n/b_n=a_n\cdot(1/b_n)\to L/M$ (product law). ✓

### A5. $f\geq0$ near $a$ and $\lim f=L$ ⇒ $L\geq0$
Contradiction: assume $L<0$. Take $\varepsilon=|L|/2$. The definition gives $\delta$ with $|f(x)-L|<|L|/2$, so $f(x)<L+|L|/2=L/2<0$ — contradicting $f(x)\geq0$. Hence $L\geq0$. ✓

### A6. $\lim_{x\to0}x\sin(1/x)=0$
$|x\sin(1/x)|\leq|x|$, so $-|x|\leq x\sin(1/x)\leq|x|$. Both bounds $\to0$; squeeze gives $0$. ✓

### A7. $|f(x)-3|\leq2|x-1|$ ⇒ $\lim_{x\to1}f(x)=3$
Given $\varepsilon>0$, choose $\delta=\varepsilon/2$. If $0<|x-1|<\delta$: $|f(x)-3|\leq2|x-1|<2\delta=\varepsilon$. ✓ (Lipschitz gives δ directly.)

### A8. Does $\lim_{x\to a}f(x)=L$ force $f$ to be defined at $a$? **No.**
Counterexample: $f(x)=\frac{x^2-1}{x-1}$ at $a=1$. $\lim_{x\to1}f(x)=2$ exists, but $f(1)$ is undefined. The $0<|x-a|$ in the definition deliberately ignores the point itself.

### A9. $a_n=(-1)^n$ does not converge
Take $\varepsilon=1$. For any $N$, pick even $m\geq N$ and odd $n\geq N$: $|a_m-a_n|=|1-(-1)|=2\geq\varepsilon$. So the Cauchy condition fails → no limit. ✓

### A10. Cauchy forward direction
Given $\varepsilon>0$, since $a_n\to L$, pick $N$ with $n\geq N\Rightarrow|a_n-L|<\varepsilon/2$. Then for $m,n\geq N$: $|a_m-a_n|\leq|a_m-L|+|L-a_n|<\varepsilon/2+\varepsilon/2=\varepsilon$. ✓

### A11. Product law for functions (from scratch)
Lemma (locally bounded): take $\varepsilon=1$ in $f\to L$ → $\delta_0$ with $|f(x)-L|<1$ → $|f(x)|\leq|f(x)-L|+|L|<1+|L|=:C$. Then, given $\varepsilon$, choose $\delta_1,\delta_2$ for $|f-L|<\frac{\varepsilon}{2(C+1)}$, $|g-M|<\frac{\varepsilon}{2(|M|+1)}$. Let $\delta=\min(\delta_0,\delta_1,\delta_2)$. Cross-term:
$|fg-LM|\leq|f||g-M|+|M||f-L|<C\cdot\frac{\varepsilon}{2(C+1)}+|M|\cdot\frac{\varepsilon}{2(|M|+1)}<\varepsilon$.
Triangle inequality is used in the lemma ($|f|\leq|f-L|+|L|$) and in the final estimate. ✓

### A12. $\lim_{x\to0}\frac{|x|}{x}$ DNE by negation
Take $\varepsilon=1$. For ANY $\delta>0$, let $x_1=\delta/2$ (so $f=1$) and $x_2=-\delta/2$ (so $f=-1$); both satisfy $0<|x_i|<\delta$. For any candidate $L$: if $|1-L|<1$ and $|-1-L|<1$, then $2=|1-(-1)|\leq|1-L|+|L+1|<2$ — contradiction. The negation holds for every $L$. ✓
