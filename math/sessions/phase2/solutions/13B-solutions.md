# Solutions — 13B: Limits at Infinity — Degree Races, Asymptotes, and Growth

> Back to [13B — Limits at Infinity](../13B-limits-at-infinity.md)

> **Source.** Every solution below matches an item in Stewart, *Calculus*, Sections 2.6 and 2.2. Each heading cites its exercise number.

## Basic Drills

### D1. (§2.6 #15) $\displaystyle\lim_{x\to\infty}\frac{4x+3}{5x-1}$ — divide by $x$.

$$\frac{4+\frac3x}{5-\frac1x}\longrightarrow\frac{4}{5}.$$

> **Answer**: $\frac{4}{5}$

---

### D2. (§2.6 #16) $\displaystyle\lim_{x\to\infty}\frac{-2}{3x+7}$ — compare degrees.

$\deg(\text{num})=0<\deg(\text{den})=1$, so the limit is $0$.

> **Answer**: $0$

---

### D3. (§2.6 #13) $\displaystyle\lim_{x\to\infty}\frac{2x^2-7}{5x^2+x-3}$ — divide by $x^2$.

$$\frac{2-\frac{7}{x^2}}{5+\frac1x-\frac{3}{x^2}}\longrightarrow\frac{2}{5}.$$

> **Answer**: $\frac{2}{5}$

---

### D4. (§2.6 #17) $\displaystyle\lim_{t\to-\infty}\frac{3t^2+t}{t^3-4t+1}$ — compare degrees.

$\deg(\text{num})=2<\deg(\text{den})=3$, so the limit is $0$.

> **Answer**: $0$

---

### D5. (§2.6 #18) $\displaystyle\lim_{t\to-\infty}\frac{6t^2+t-5}{9-2t^2}$ — ratio of leading coefficients.

Degrees are equal, so the limit is $\dfrac{6}{-2}=-3$.

> **Answer**: $-3$

---

### D6. (§2.6 #20) $\displaystyle\lim_{x\to\infty}\frac{3x^3-8x+2}{4x^3-5x^2-2}$.

Equal degrees: the limit is the ratio of leading coefficients, $\dfrac34$.

> **Answer**: $\frac{3}{4}$

---

### D7. (§2.6 #21) $\displaystyle\lim_{x\to\infty}\frac{4-\sqrt{x}}{2+\sqrt{x}}$ — divide by $\sqrt{x}$.

$$\frac{\frac{4}{\sqrt{x}}-1}{\frac{2}{\sqrt{x}}+1}\longrightarrow\frac{-1}{1}=-1.$$

> **Answer**: $-1$

---

### D8. (§2.6 #29) $\displaystyle\lim_{t\to\infty}\left(\sqrt{25t^2+2}-5t\right)$ — conjugate.

$$\frac{(25t^2+2)-25t^2}{\sqrt{25t^2+2}+5t}=\frac{2}{\sqrt{25t^2+2}+5t}\longrightarrow 0 .$$

> **Answer**: $0$

---

### D9. (§2.6 #32) $\displaystyle\lim_{x\to\infty}\left(x-\sqrt{x}\right)$ — factor out $\sqrt{x}$.

$x-\sqrt{x}=\sqrt{x}\,(\sqrt{x}-1)\to\infty$.

> **Answer**: $\infty$

---

### D10. (§2.6 #37) $\displaystyle\lim_{x\to\infty}\frac{1-e^{x}}{1+2e^{x}}$ — divide by $e^x$.

$$\frac{e^{-x}-1}{e^{-x}+2}\longrightarrow\frac{0-1}{0+2}=-\frac12.$$

> **Answer**: $-\frac{1}{2}$

---

### D11. (§2.2 #29) $\displaystyle\lim_{x\to5^+}\frac{x+1}{x-5}$ — track the denominator's sign.

As $x\to5^+$, the numerator $\to6>0$ and the denominator $\to0^+$. So the quotient $\to+\infty$.

> **Answer**: $+\infty$

---

### D12. (§2.2 #31) $\displaystyle\lim_{x\to2}\frac{x^2}{(x-2)^2}$ — squared denominator.

$(x-2)^2\to0^+$ from both sides and the numerator $\to4>0$, so both one-sided limits are $+\infty$.

---

## Advanced Drills

### A1. (§2.6 #14) $\displaystyle\lim_{x\to\infty}\sqrt{\frac{9x^3+8x-4}{3-5x+x^3}}$ — inside limit first.

Inside: equal degrees, leading ratio $\dfrac91=9$. So the limit is $\sqrt{9}=3$.

> **Answer**: $3$

---

### A2. (§2.6 #22) $\displaystyle\lim_{u\to-\infty}\frac{(u^2+1)(2u^2-1)}{(u^2+2)^2}$ — expand the leading terms.

Numerator $=2u^4+u^2-1$; denominator $=u^4+4u^2+4$. Both have degree $4$:

$$\frac{2u^4+u^2-1}{u^4+4u^2+4}\longrightarrow\frac{2}{1}=2 .$$

> **Answer**: $2$

---

### A3. (§2.6 #23) $\displaystyle\lim_{x\to\infty}\frac{\sqrt{x+3x^2}}{4x-1}$.

For $x>0$, $\sqrt{3x^2+x}=x\sqrt{3+\frac1x}$, so

$$\frac{x\sqrt{3+\frac1x}}{4x-1}=\frac{\sqrt{3+\frac1x}}{4-\frac1x}\longrightarrow\frac{\sqrt3}{4}.$$

> **Answer**: $\frac{\sqrt3}{4}$

---

### A4. (§2.6 #24) $\displaystyle\lim_{t\to\infty}\frac{t+3}{\sqrt{2t^2-1}}$.

Divide by $t$ (positive): $\dfrac{1+\frac3t}{\sqrt{2-\frac{1}{t^2}}}\longrightarrow\dfrac{1}{\sqrt2}=\dfrac{\sqrt2}{2}$.

> **Answer**: $\frac{\sqrt2}{2}$

---

### A5. (§2.6 #25) $\displaystyle\lim_{x\to\infty}\frac{\sqrt{1+4x^{6}}}{2-x^{3}}$.

For $x>0$, $\sqrt{4x^6}=2x^3$, so the ratio is $\dfrac{2x^3}{2-x^3}\to\dfrac{2}{-1}=-2$.

> **Answer**: $-2$

---

### A6. (§2.6 #26) $\displaystyle\lim_{x\to-\infty}\frac{\sqrt{1+4x^{6}}}{2-x^{3}}$.

Now $x<0$, so $\sqrt{4x^6}=2|x^3|=-2x^3$. The ratio is $\dfrac{-2x^3}{2-x^3}\to\dfrac{-2}{-1}=2$.

> **Answer**: $2$ — the sign flips versus A5 (this is the $\sqrt{x^2}=|x|$ caution)

---

### A7. (§2.6 #30) $\displaystyle\lim_{x\to-\infty}\left(\sqrt{4x^2+3x}+2x\right)$.

Conjugate: $\dfrac{(4x^2+3x)-4x^2}{\sqrt{4x^2+3x}-2x}=\dfrac{3x}{\sqrt{4x^2+3x}-2x}$.

For $x<0$, $\sqrt{4x^2+3x}=-x\sqrt{4+\frac3x}$, so the denominator is $-x\sqrt{4+\frac3x}-2x\approx-2x-2x=-4x$. Hence

$$\frac{3x}{-4x}\longrightarrow-\frac34.$$

> **Answer**: $-\frac34$

---

### A8. (§2.6 #31) $\displaystyle\lim_{x\to\infty}\left(\sqrt{x^2+ax}-\sqrt{x^2+bx}\right)$.

Conjugate: $\dfrac{(x^2+ax)-(x^2+bx)}{\sqrt{x^2+ax}+\sqrt{x^2+bx}}=\dfrac{(a-b)x}{\sqrt{x^2+ax}+\sqrt{x^2+bx}}$.

Divide by $x$: $\dfrac{a-b}{\sqrt{1+\frac ax}+\sqrt{1+\frac bx}}\longrightarrow\dfrac{a-b}{2}$.

> **Answer**: $\frac{a-b}{2}$

---

### A9. (§2.6 #36) $\displaystyle\lim_{x\to\infty}\frac{\sin^2 x}{x^2+1}$ — squeeze.

$0\le\sin^2 x\le1$, so $0\le\dfrac{\sin^2 x}{x^2+1}\le\dfrac{1}{x^2+1}$. Both bounds $\to0$, so the limit is $0$.

> **Answer**: $0$

---

### A10. (§2.6 #41) $\displaystyle\lim_{x\to\infty}\left[\ln(1+x^2)-\ln(1+x)\right]$.

Combine: $\ln\dfrac{1+x^2}{1+x}$. As $x\to\infty$ the inside grows like $x$, so the logarithm $\to\infty$.

> **Answer**: $\infty$

---

### A11. (§2.6 #48) Asymptotes of $y=\dfrac{2x^2+1}{3x^2+2x-1}$.

Horizontal: equal degrees, leading ratio $\dfrac23$, so $y=\dfrac23$.

Vertical: $3x^2+2x-1=(3x-1)(x+1)=0$ gives $x=\dfrac13$ and $x=-1$; the numerator is nonzero at both. So the vertical asymptotes are $x=\dfrac13$ and $x=-1$.

> **Answer**: horizontal $y=\frac23$; vertical $x=\frac13$ and $x=-1$

---

## Answer Check

| Problem | Answer |
|:--------|:-------|
| D1–D4 | $\frac45$; $0$; $\frac25$; $0$ |
| D5–D8 | $-3$; $\frac34$; $-1$; $0$ |
| D9–D12 | $\infty$; $-\frac12$; $+\infty$; $+\infty$ |
| A1–A4 | $3$; $2$; $\frac{\sqrt3}{4}$; $\frac{\sqrt2}{2}$ |
| A5–A8 | $-2$; $2$; $-\frac34$; $\frac{a-b}{2}$ |
| A9–A11 | $0$; $\infty$; horiz. $y=\frac23$, vert. $x=\frac13,-1$ |


> **Answer**: $+\infty$
