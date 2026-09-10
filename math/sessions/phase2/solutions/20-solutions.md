# Solutions — 20: Rigorous Limits — ε-δ and ε-N
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
