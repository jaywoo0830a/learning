# Solutions — 13A: Algebraic Limits — The $\frac{0}{0}$ Toolkit

> Back to [13A — Algebraic Limits](../13A-algebraic-limits.md)

> **Source.** Every solution below matches an item in Stewart, *Calculus*, Sections 2.3 and 2.2. Each heading cites its exercise number (or, for D12, the example number).

## Basic Drills

### D1. (§2.3 #3) $\displaystyle\lim_{x\to 5}(4x^2-5x)$ — direct substitution.

$4(5)^2-5(5)=100-25=75$.

> **Answer**: $75$

---

### D2. (§2.3 #11) $\displaystyle\lim_{x\to -2}(3x-7)$ — direct substitution.

$3(-2)-7=-6-7=-13$.

> **Answer**: $-13$

---

### D3. (§2.3 #13) $\displaystyle\lim_{t\to 4}\frac{t^2-2t-8}{t-4}$ — factor and cancel.

$t^2-2t-8=(t-4)(t+2)$, so the ratio is $t+2\to 4+2=6$.

> **Answer**: $6$

---

### D4. (§2.3 #19) $\displaystyle\lim_{t\to 3}\frac{t^3-27}{t^2-9}$ — factor cubes and squares.

$t^3-27=(t-3)(t^2+3t+9)$ and $t^2-9=(t-3)(t+3)$. Cancel $t-3$:

$$\frac{t^2+3t+9}{t+3}\longrightarrow\frac{9+9+9}{6}=\frac{27}{6}=\frac{9}{2}.$$

> **Answer**: $\frac{9}{2}$

---

### D5. (§2.3 #20) $\displaystyle\lim_{u\to -1}\frac{u+1}{u^3+1}$ — factor a sum of cubes.

$u^3+1=(u+1)(u^2-u+1)$. Cancel $u+1$:

$$\frac{1}{u^2-u+1}\longrightarrow\frac{1}{1+1+1}=\frac{1}{3}.$$

> **Answer**: $\frac{1}{3}$

---

### D6. (§2.3 #23) $\displaystyle\lim_{h\to 0}\frac{\sqrt{9+h}-3}{h}$ — multiply by the conjugate.

$$\frac{\sqrt{9+h}-3}{h}\cdot\frac{\sqrt{9+h}+3}{\sqrt{9+h}+3}
=\frac{(9+h)-9}{h\bigl(\sqrt{9+h}+3\bigr)}=\frac{1}{\sqrt{9+h}+3}\longrightarrow\frac{1}{6}.$$

> **Answer**: $\frac{1}{6}$

---

### D7. (§2.3 #27) $\displaystyle\lim_{t\to 0}\frac{\sqrt{1+t}-\sqrt{1-t}}{t}$ — multiply by the conjugate.

$$\frac{\bigl(\sqrt{1+t}-\sqrt{1-t}\bigr)\bigl(\sqrt{1+t}+\sqrt{1-t}\bigr)}{t\bigl(\sqrt{1+t}+\sqrt{1-t}\bigr)}
=\frac{2t}{t\bigl(\sqrt{1+t}+\sqrt{1-t}\bigr)}=\frac{2}{\sqrt{1+t}+\sqrt{1-t}}\longrightarrow\frac{2}{2}=1.$$

> **Answer**: $1$

---

### D8. (§2.3 #22) $\displaystyle\lim_{x\to 9}\frac{9-x}{3-\sqrt{x}}$ — factor the numerator.

$9-x=(3-\sqrt{x})(3+\sqrt{x})$, so the ratio is $3+\sqrt{x}\to 3+3=6$.

> **Answer**: $6$

---

### D9. (§2.2 #25) $\displaystyle\lim_{\theta\to 0}\frac{\sin 3\theta}{\tan 2\theta}$ — match the arguments.

$$\frac{\sin 3\theta}{\tan 2\theta}=\frac{\sin 3\theta}{3\theta}\cdot\frac{2\theta}{\sin 2\theta}\cdot\frac{3}{2}\cdot\cos 2\theta
\longrightarrow 1\cdot 1\cdot\frac{3}{2}\cdot 1=\frac{3}{2}.$$

> **Answer**: $\frac{3}{2}$

---

### D10. (§2.3 #25) $\displaystyle\lim_{x\to 3}\frac{\ \frac1x-\frac13\ }{x-3}$ — combine the numerator first.

$\frac1x-\frac13=\frac{3-x}{3x}=\frac{-(x-3)}{3x}$, so the whole expression is

$$\frac{-(x-3)}{3x(x-3)}=-\frac{1}{3x}\longrightarrow-\frac{1}{3\cdot 3}=-\frac{1}{9}.$$

> **Answer**: $-\frac{1}{9}$ (the pattern $-\frac{1}{a^2}$ with $a=3$)

---

### D11. (§2.3 #28) $\displaystyle\lim_{t\to 0}\left(\frac1t-\frac{1}{t^2+t}\right)$ — combine into one fraction.

$$\frac1t-\frac{1}{t(t+1)}=\frac{(t+1)-1}{t(t+1)}=\frac{t}{t(t+1)}=\frac{1}{t+1}\longrightarrow 1.$$

> **Answer**: $1$

---

### D12. (§2.3 Ex 10) $\displaystyle\lim_{x\to 3}\lfloor x\rfloor$ — compare the one-sided limits.

For $3\le x<4$, $\lfloor x\rfloor=3$, so $\lim_{x\to3^+}\lfloor x\rfloor=3$. For $2\le x<3$, $\lfloor x\rfloor=2$, so $\lim_{x\to3^-}\lfloor x\rfloor=2$. The two sides differ.

> **Answer**: does not exist (left $=2$, right $=3$)

---

## Advanced Drills

### A1. (§2.3 #66) $\displaystyle\lim_{x\to 2}\frac{\sqrt{6-x}-2}{\sqrt{3-x}-1}$ — conjugate both.

Numerator: $\sqrt{6-x}-2=\dfrac{(6-x)-4}{\sqrt{6-x}+2}=\dfrac{2-x}{\sqrt{6-x}+2}$.

Denominator: $\sqrt{3-x}-1=\dfrac{(3-x)-1}{\sqrt{3-x}+1}=\dfrac{2-x}{\sqrt{3-x}+1}$.

Ratio $=\dfrac{\sqrt{3-x}+1}{\sqrt{6-x}+2}\longrightarrow\dfrac{1+1}{2+2}=\dfrac{1}{2}$.

> **Answer**: $\frac{1}{2}$

---

### A2. (§2.3 #29) $\displaystyle\lim_{x\to 16}\frac{4-\sqrt{x}}{16x-x^2}$ — factor the denominator.

$16x-x^2=x(16-x)=x(4-\sqrt{x})(4+\sqrt{x})$. Cancel $4-\sqrt{x}$:

$$\frac{1}{x(4+\sqrt{x})}\longrightarrow\frac{1}{16\cdot 8}=\frac{1}{128}.$$

> **Answer**: $\frac{1}{128}$

---

### A3. (§2.3 #31) $\displaystyle\lim_{t\to 0}\left(\frac{1}{t\sqrt{1+t}}-\frac1t\right)$ — combine, then conjugate.

$$\frac{1}{t\sqrt{1+t}}-\frac1t=\frac{1-\sqrt{1+t}}{t\sqrt{1+t}}
=\frac{\bigl(1-\sqrt{1+t}\bigr)\bigl(1+\sqrt{1+t}\bigr)}{t\sqrt{1+t}\bigl(1+\sqrt{1+t}\bigr)}
=\frac{-t}{t\sqrt{1+t}\bigl(1+\sqrt{1+t}\bigr)}.$$

Cancel $t$: $-\dfrac{1}{\sqrt{1+t}\bigl(1+\sqrt{1+t}\bigr)}\longrightarrow-\dfrac{1}{1\cdot 2}=-\dfrac{1}{2}$.

> **Answer**: $-\frac{1}{2}$

---

### A4. (§2.3 #32) $\displaystyle\lim_{x\to -4}\frac{\sqrt{x^2+9}-5}{x+4}$ — conjugate the numerator.

$$\frac{\sqrt{x^2+9}-5}{x+4}\cdot\frac{\sqrt{x^2+9}+5}{\sqrt{x^2+9}+5}
=\frac{x^2-16}{(x+4)\bigl(\sqrt{x^2+9}+5\bigr)}
=\frac{(x-4)(x+4)}{(x+4)\bigl(\sqrt{x^2+9}+5\bigr)}.$$

Cancel $x+4$: $\dfrac{x-4}{\sqrt{x^2+9}+5}\longrightarrow\dfrac{-8}{5+5}=-\dfrac{4}{5}$.

> **Answer**: $-\frac{4}{5}$

---

### A5. (§2.3 #33) $\displaystyle\lim_{h\to 0}\frac{(x+h)^3-x^3}{h}$, with $x$ held fixed.

Expand the cube: $(x+h)^3=x^3+3x^2h+3xh^2+h^3$, so

$$\frac{(x+h)^3-x^3}{h}=\frac{3x^2h+3xh^2+h^3}{h}=3x^2+3xh+h^2\longrightarrow 3x^2.$$

> **Answer**: $3x^2$

---

### A6. (§2.3 #34) $\displaystyle\lim_{h\to 0}\frac{\ \frac{1}{(x+h)^2}-\frac{1}{x^2}\ }{h}$, with $x$ held fixed.

Combine over $x^2(x+h)^2$:

$$\frac{1}{(x+h)^2}-\frac{1}{x^2}=\frac{x^2-(x+h)^2}{x^2(x+h)^2}=\frac{-2xh-h^2}{x^2(x+h)^2}.$$

Divide by $h$: $\dfrac{-2x-h}{x^2(x+h)^2}\longrightarrow\dfrac{-2x}{x^4}=-\dfrac{2}{x^3}$.

> **Answer**: $-\frac{2}{x^3}$

---

### A7. (§2.3 #61) If $\displaystyle\lim_{x\to 1}\frac{f(x)-8}{x-1}=10$, find $\displaystyle\lim_{x\to 1}f(x)$.

The denominator $x-1\to 0$. If the numerator $f(x)-8$ did not also go to $0$, the quotient would blow up and no finite limit $10$ could exist. So $\lim_{x\to1}\bigl(f(x)-8\bigr)=0$, giving $\lim_{x\to1}f(x)=8$.

> **Answer**: $8$

---

### A8. (§2.3 #62) If $\displaystyle\lim_{x\to 0}\frac{f(x)}{x^2}=5$, find $\displaystyle\lim_{x\to 0}f(x)$ and $\displaystyle\lim_{x\to 0}\frac{f(x)}{x}$.

Write $f(x)=\dfrac{f(x)}{x^2}\cdot x^2$. Then $\lim_{x\to0}f(x)=5\cdot 0=0$.

Write $\dfrac{f(x)}{x}=\dfrac{f(x)}{x^2}\cdot x$. Then $\lim_{x\to0}\dfrac{f(x)}{x}=5\cdot 0=0$.

> **Answer**: both are $0$

---

### A9. (§2.3 #67) Find $a$ so $\displaystyle\lim_{x\to -2}\frac{3x^2+ax+a+3}{x^2+x-2}$ exists.

The denominator is $(x+2)(x-1)\to 0$ at $x=-2$. The limit exists only if the numerator also vanishes there:

$$3(-2)^2+a(-2)+a+3=12-2a+a+3=15-a=0\ \Longrightarrow\ a=15 .$$

Then $3x^2+15x+18=3(x^2+5x+6)=3(x+2)(x+3)$, so

$$\frac{3(x+2)(x+3)}{(x+2)(x-1)}=\frac{3(x+3)}{x-1}\longrightarrow\frac{3(1)}{-3}=-1 .$$

> **Answer**: $a=15$, and the limit is $-1$

---

### A10. (§2.3 #59) Prove $\displaystyle\lim_{x\to a}p(x)=p(a)$ for a polynomial $p$.

Write $p(x)=c_nx^n+\cdots+c_1x+c_0$. The Power Law (§2.3 Law 10) gives $\lim_{x\to a}x^m=a^m$ for each $m$, the Constant Law gives $\lim_{x\to a}c_0=c_0$, and the Sum and Constant-Multiple Laws assemble the pieces:

$$\lim_{x\to a}p(x)=c_na^n+\cdots+c_1a+c_0=p(a). \qquad\square$$

> **Answer**: proven — polynomials pass through the limit (the Direct Substitution Property)

---

### A11. (§2.3 #63) For $f(x)=x^2$ (rational $x$) and $f(x)=0$ (irrational $x$), prove $\displaystyle\lim_{x\to 0}f(x)=0$.

Every value of $f$ is either $x^2$ or $0$, so for all $x$,

$$0\ \le\ f(x)\ \le\ x^2 .$$

Both bounds have limit $0$ as $x\to 0$. By the Squeeze Theorem,

$$\lim_{x\to 0}f(x)=0. \qquad\square$$

> **Answer**: proven by squeezing $0\le f(x)\le x^2$

---

## Answer Check

| Problem | Answer |
|:--------|:-------|
| D1–D4 | $75$; $-13$; $6$; $\frac92$ |
| D5–D8 | $\frac13$; $\frac16$; $1$; $6$ |
| D9–D12 | $\frac32$; $-\frac19$; $1$; DNE (left $2$, right $3$) |
| A1–A4 | $\frac12$; $\frac{1}{128}$; $-\frac12$; $-\frac45$ |
| A5–A8 | $3x^2$; $-\frac{2}{x^3}$; $8$; $0$ and $0$ |
| A9–A11 | $a=15$, limit $-1$; proof; proof |

