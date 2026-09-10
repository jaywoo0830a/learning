# Solutions — 11C: Hyperbolic Functions — The Trigonometric Functions of a Hyperbola

> Back to [11C — Hyperbolic Functions](../11C-hyperbolic-functions.md)
## Basic Drills

### D1. $\cosh 0$, $\sinh 0$, $\tanh 0$.

$\cosh 0 = \frac{1+1}{2} = 1$; $\sinh 0 = \frac{1-1}{2} = 0$; $\tanh 0 = \frac{0}{1} = 0$.

> **Answer**: $1, 0, 0$

### D2. Compute $\cosh(\ln 2)$ and $\sinh(\ln 2)$.

$\cosh(\ln 2) = \frac{2+1/2}{2} = \frac54$; $\sinh(\ln 2) = \frac{2-1/2}{2} = \frac34$.

> **Answer**: $\frac54$, $\frac34$

### D3. $\cosh^2 x - \sinh^2 x = ?$

$= 1$ — the core identity.

> **Answer**: $1$

### D4. Write $e^x$ and $e^{-x}$ in terms of $\cosh x$ and $\sinh x$.

$e^x = \cosh x + \sinh x$; $e^{-x} = \cosh x - \sinh x$.

> **Answer**: $e^x = \cosh x + \sinh x$, $e^{-x} = \cosh x - \sinh x$

### D5. True or false: $\cosh x \ge 1$ for all real $x$.

**True** — since $e^x + e^{-x} \ge 2$ (AM-GM), $\cosh x = \frac{e^x+e^{-x}}{2} \ge 1$, with equality only at $x=0$.

> **Answer**: True

### D6. Compute $\sinh(2\ln 2)$.

Directly: $e^{2\ln2} = 4$, $e^{-2\ln2} = \frac14$, so $\sinh(2\ln2) = \frac{4-1/4}{2} = \frac{15/4}{2} = \frac{15}{8}$. (Or double-angle: $2\sinh(\ln2)\cosh(\ln2) = 2\cdot\frac34\cdot\frac54 = \frac{15}{8}$.)

> **Answer**: $\frac{15}{8}$

### D7. $\lim_{x\to\infty}\tanh x$ and $\lim_{x\to-\infty}\tanh x$.

As $x\to\infty$, $e^{-x}\to0$: $\tanh x = \frac{e^x-e^{-x}}{e^x+e^{-x}} \to 1$. As $x\to-\infty$: $\to -1$.

> **Answer**: $1$ and $-1$

### D8. Simplify $\operatorname{sech}^2 x + \tanh^2 x$.

From $1-\tanh^2 x = \operatorname{sech}^2 x$: $\operatorname{sech}^2 x + \tanh^2 x = 1$.

> **Answer**: $1$

### D9. $\operatorname{arsinh} 0$ and $\operatorname{artanh} 0$.

$\operatorname{arsinh} 0 = \ln(0+\sqrt{1}) = 0$. $\operatorname{artanh} 0 = \frac12\ln\left(\frac{1}{1}\right) = 0$.

> **Answer**: $0, 0$

### D10. $\frac{d}{dx}\sinh x$ and $\frac{d}{dx}\cosh x$.

$\frac{d}{dx}\sinh x = \cosh x$; $\frac{d}{dx}\cosh x = \sinh x$.

> **Answer**: $\cosh x$ and $\sinh x$ — no sign changes

---

## Advanced Drills

### A1. Prove $\cosh(x+y) = \cosh x\cosh y + \sinh x\sinh y$ from the $e^x$ definitions.

Compute $4\cosh(x+y) = 2(e^{x+y} + e^{-x-y})$. Meanwhile:

$\cosh x\cosh y + \sinh x\sinh y = \frac{(e^x+e^{-x})(e^y+e^{-y})}{4} + \frac{(e^x-e^{-x})(e^y-e^{-y})}{4}$

$= \frac{(e^{x+y}+e^{x-y}+e^{-x+y}+e^{-x-y}) + (e^{x+y}-e^{x-y}-e^{-x+y}+e^{-x-y})}{4} = \frac{2e^{x+y}+2e^{-x-y}}{4} = \frac{e^{x+y}+e^{-x-y}}{2} = \cosh(x+y)$. ✓

> **Answer**: the cross terms $e^{x-y}, e^{-x+y}$ cancel, leaving $2(e^{x+y}+e^{-x-y})/4 = \cosh(x+y)$

### A2. Derive $\tanh(x+y) = \frac{\tanh x + \tanh y}{1 + \tanh x\,\tanh y}$.

Divide $\sinh(x+y)$ by $\cosh(x+y)$:

$\tanh(x+y) = \frac{\sinh x\cosh y + \cosh x\sinh y}{\cosh x\cosh y + \sinh x\sinh y}$.

Divide top and bottom by $\cosh x\cosh y$:

$= \frac{\tanh x + \tanh y}{1 + \tanh x\,\tanh y}$. ✓ (Note: the denominator is $1 + \tanh x\tanh y$ — Osborne's rule flipped the trig minus.)

> **Answer**: $\tanh(x+y) = \frac{\tanh x + \tanh y}{1 + \tanh x\tanh y}$

### A3. Solve $\cosh x = 2$. Minimum value of $\cosh x$?

$x = \pm\operatorname{arcosh} 2 = \pm\ln(2 + \sqrt{3})$. (Check: $2+\sqrt3 \approx 3.732$, $\cosh(1.317) = 2$.)

Since $\cosh x \ge 1$ with equality at $x=0$: minimum value is $1$.

> **Answer**: $x = \pm\ln(2+\sqrt3)$; minimum of $\cosh$ is $1$ at $x=0$

### A4. Show $\sinh(3x) = 3\sinh x + 4\sinh^3 x$. Compare with $\sin 3\theta = 3\sin\theta - 4\sin^3\theta$.

$\sinh(3x) = \sinh(2x+x) = \sinh 2x\cosh x + \cosh 2x\sinh x$
$= (2\sinh x\cosh x)\cosh x + (1+2\sinh^2 x)\sinh x$
$= 2\sinh x(1+\sinh^2 x) + \sinh x + 2\sinh^3 x$
$= 2\sinh x + 2\sinh^3 x + \sinh x + 2\sinh^3 x = 3\sinh x + 4\sinh^3 x$. ✓

**Comparison**: trig has $-4\sin^3\theta$, hyperbolic has $+4\sinh^3 x$. By Osborne's rule, $\sin 3\theta$ contains three sines (odd product) — one pair flips sign; the surviving single sine doesn't. The hyperbolic version keeps everything positive.

> **Answer**: $\sinh(3x) = 3\sinh x + 4\sinh^3 x$ — the sign of the cubic term flips from trig

### A5. Derive $\operatorname{arsinh} x = \ln(x + \sqrt{x^2+1})$.

Let $y = \sinh x = \frac{e^x - e^{-x}}{2}$. Multiply by $2e^x$:

$2y e^x = e^{2x} - 1$ → $e^{2x} - 2y\,e^x - 1 = 0$ → $e^x = y \pm \sqrt{y^2+1}$.

Since $e^x > 0$ and $y - \sqrt{y^2+1} < 0$, take $+$: $x = \ln(y + \sqrt{y^2+1})$.

> **Answer**: $\operatorname{arsinh} x = \ln(x+\sqrt{x^2+1})$, valid for all real $x$

### A6. Sketch $\tanh x$ and $\coth x$; label asymptotes.

**$\tanh x$**: passes through $(0,0)$, odd, increasing, horizontal asymptotes $y = 1$ (as $x\to\infty$) and $y = -1$ (as $x\to-\infty$); never leaves $(-1,1)$.

**$\coth x = 1/\tanh x$**: vertical asymptote $x=0$; horizontal asymptotes $y = \pm 1$; range $(-\infty,-1)\cup(1,\infty)$; for $x>0$ it drops from $+\infty$ (just right of $0$) down toward $1$; for $x<0$ it rises from $-\infty$ up toward $-1$.

> **Answer**: $\tanh$: between $y=\pm1$, through origin. $\coth$: asymptotes $x=0$ and $y=\pm1$, range outside $[-1,1]$

### A7. Differentiate $\operatorname{arsinh} x$ and show $\frac{d}{dx}\operatorname{arsinh} x = \frac{1}{\sqrt{x^2+1}}$.

$\operatorname{arsinh} x = \ln(x+\sqrt{x^2+1})$.

$\frac{d}{dx} = \frac{1}{x+\sqrt{x^2+1}}\cdot\left(1 + \frac{x}{\sqrt{x^2+1}}\right) = \frac{1}{x+\sqrt{x^2+1}}\cdot\frac{\sqrt{x^2+1}+x}{\sqrt{x^2+1}} = \frac{1}{\sqrt{x^2+1}}$. ✓

> **Answer**: $\frac{d}{dx}\operatorname{arsinh} x = \frac{1}{\sqrt{x^2+1}}$

### A8. Catenary $y = a\cosh(x/a)$: lowest point, height at $x=a$, slope at $x=a$.

(a) Lowest at $x=0$: $y = a\cosh 0 = a$.

(b) At $x = a$: $y = a\cosh 1 \approx 1.543a$.

(c) $y' = a\cdot\frac1a\sinh(x/a) = \sinh(x/a)$; at $x=a$: $\sinh 1 \approx 1.175$.

> **Answer**: (a) $(0,a)$ (b) $a\cosh 1 \approx 1.543a$ (c) slope $\sinh 1 \approx 1.18$

### A9. Evaluate $\int_0^1 \frac{dx}{\sqrt{x^2+1}}$ exactly.

$\int_0^1 \frac{dx}{\sqrt{x^2+1}} = \operatorname{arsinh} x\Big|_0^1 = \operatorname{arsinh} 1 - \operatorname{arsinh} 0 = \ln(1+\sqrt2) \approx 0.8814$.

> **Answer**: $\ln(1+\sqrt2)$

### A10. Prove $\cosh(2x) = 1 + 2\sinh^2 x$ and find all $x$ with $\cosh(2x) = 2$.

$\cosh(2x) = \cosh^2 x + \sinh^2 x = (1+\sinh^2 x) + \sinh^2 x = 1 + 2\sinh^2 x$. ✓

Set $\cosh(2x) = 2$: $1 + 2\sinh^2 x = 2$ → $\sinh^2 x = \frac12$ → $\sinh x = \pm\frac{1}{\sqrt2}$.

$x = \pm\operatorname{arsinh}\frac{1}{\sqrt2} = \pm\ln\left(\frac{1}{\sqrt2} + \sqrt{\frac12+1}\right) = \pm\ln\left(\frac{1+\sqrt3}{\sqrt2}\right)$.

> **Answer**: $x = \pm\ln\left(\frac{1+\sqrt3}{\sqrt2}\right)$

---

## Answer Check

| Problem | Answer |
|:--------|:-------|
| D1–D10 | see above |
