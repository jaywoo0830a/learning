# Solutions: 13C — Continuity, Theorems, and Sequences

---

## Practice 1

$f(2)$ undefined. $\lim_{x\to2}\frac{(x-2)(x+2)}{x-2} = 4$. Removable discontinuity (hole at $(2,4)$).

---

## Practice 2

Left: $\lim_{x\to1^-}(2x+k)=2+k$. Right: $\lim_{x\to1^+}x^2=1$, $f(1)=1$.
$2+k=1 \to k=-1$.

---

## Practice 3

$-1\leq\cos\frac{1}{x^2}\leq1$. Multiply by $x^3$ (sign changes for $x<0$, but $|x^3\cos(1/x^2)| \leq |x|^3$).
$-|x|^3 \leq x^3\cos\frac{1}{x^2} \leq |x|^3$. Both bounds → 0. → **0**.

---

## Practice 4

$f(0)=-1$ (negative). $f(2)=32-16+2-1=17$ (positive). Polynomial = continuous. IVT → root in $(0,2)$.

---

## Practice 5

If $L$ exists: $L = \frac{L+4}{2} \to 2L=L+4 \to L=4$.
The sequence is monotone (can check $a_{n+1}-a_n = \frac{4-a_n}{2}$; starts at 3<4, so increasing toward 4). → **Limit = 4.**

---

## Practice 6

Left: $\lim_{x\to0^-}\frac{\sin x}{x}=1$. Right: $\lim_{x\to0^+}\frac{e^x-1}{x}=1$. $f(0)=1$.
All three equal 1 → continuous at $x=0$.

---

## Basic Drill

**D1.** Infinite discontinuity (vertical asymptote at $x=3$).

**D2.** Removable discontinuity (hole at $x=1$, limit = 2).

**D3.** Jump discontinuity (left=1, right=2 at $x=2$).

**D4.** Left: $-a$. Right: $0$, $f(0)=0$. $-a=0 \to a=0$.

**D5.** $f(1)=1-1-2=-2$. $f(2)=8-2-2=4$. Sign change → root in $(1,2)$ by IVT. Yes.

**D6.** $-\frac{1}{x^2}\leq\frac{\cos x}{x^2}\leq\frac{1}{x^2}$. Both → 0. → **0**.

**D7.** $|(-1)^n/n| = 1/n \to 0$. → **0.** (Sequence converges.)

**D8.** $(2/3)^n \to 0$.

**D9.** 1) $f(0)=0$ defined. 2) Left limit = 0, right limit = 0 → limit exists = 0. 3) limit = $f(0)$. → Continuous. ✅

**D10.** $a_n = 8\cdot(1/2)^{n-1} \to 0$.

---

## Advanced Drill

**A1.** $f$ is continuous (polynomial). $f(0)=-1$, $f(1)=1$. IVT → at least one root in $(0,1)$.
$f'(x)=3x^2+1>0$ for all $x$ → strictly increasing → at most one root. → Exactly one real root.

**A2.** Factor: $\frac{(x-1)(x-2)}{(x-2)(x+3)}$. Cancel $(x-2)$: $\frac{x-1}{x+3}$ for $x\neq2$.
Discontinuities: $x=-3$ (infinite, denominator→0), $x=2$ (removable hole, limit $= \frac{1}{5}$).

**A3.** At $x=1$: left = $a+b$, right = $1$. → $a+b=1$.
At $x=2$: left = $4$, right = undefined ($\frac{1}{0}$ — infinite discontinuity at $x=2$).
The right piece $\frac{1}{x-2}$ has a vertical asymptote at $x=2$, so $f$ CANNOT be continuous at $x=2$ no matter what $a,b$ are. No solution — the function is fundamentally broken at $x=2$.

**A4.** $-|x| \leq x\sin\frac{1}{x} \leq |x|$. Both bounds → 0. → **0**.

**A5.** $L = \frac{1}{2}(L+\frac{2}{L}) \to 2L = L+\frac{2}{L} \to L = \frac{2}{L} \to L^2=2 \to L=\sqrt{2}$.

**A6.** $|x^2\sin(1/x)| \leq x^2$ (since $|\sin|\leq1$). Given $\epsilon>0$, choose $\delta=\sqrt{\epsilon}$.
If $|x|<\delta$, then $|x^2\sin(1/x)| \leq x^2 < \delta^2 = \epsilon$. ✓

**A7.** $g(0)=f(0)-0=1$, $g(1)=f(1)-1=-1$. $g$ is continuous. By IVT, there exists $c\in(0,1)$ with $g(c)=0 \to f(c)=c$.

**A8.** No, $\sin n$ does not converge. As $n$ increases, $\sin n$ oscillates densely in $[-1,1]$ (since integer multiples of 1 radian are dense mod $2\pi$). No single limit exists.

**A9.** $\sqrt{n^2+n}-n = \frac{(n^2+n)-n^2}{\sqrt{n^2+n}+n} = \frac{n}{\sqrt{n^2+n}+n} = \frac{1}{\sqrt{1+1/n}+1} \to \frac{1}{2}$.

**A10.** For any $x\neq y$: $\frac{|f(x)-f(y)|}{|x-y|} \leq |x-y|$. Take limit as $y\to x$: $|f'(x)| \leq 0 \to f'(x)=0$ for all $x$. Constant derivative → $f$ is constant.
