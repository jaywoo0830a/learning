# Solutions — 11C: Hyperbolic Functions — The Trigonometric Functions of a Hyperbola

> Back to [11C — Hyperbolic Functions](../11C-hyperbolic-functions.md)

---

## Practice 1

**Use the $e^x$ definitions to find exact values: (a) $\cosh(\ln 2)$ (b) $\sinh(\ln 2)$ (c) $\tanh(\ln 2)$. Then verify $\cosh^2(\ln 2) - \sinh^2(\ln 2) = 1$.**

$e^{\ln 2} = 2$, $e^{-\ln 2} = \frac12$.

(a) $\cosh(\ln 2) = \frac{2 + \frac12}{2} = \frac{5/2}{2} = \frac54$.

(b) $\sinh(\ln 2) = \frac{2 - \frac12}{2} = \frac{3/2}{2} = \frac34$.

(c) $\tanh(\ln 2) = \frac{\sinh}{\cosh} = \frac{3/4}{5/4} = \frac35$.

**Verify**: $\cosh^2 - \sinh^2 = \frac{25}{16} - \frac{9}{16} = \frac{16}{16} = 1$. ✓

> **Answer**: $\cosh(\ln 2) = \frac54$, $\sinh(\ln 2) = \frac34$, $\tanh(\ln 2) = \frac35$

---

## Practice 2

**Prove from the $e^x$ definitions: (a) $\cosh^2 x - \sinh^2 x = 1$ (b) $\cosh(2x) = \cosh^2 x + \sinh^2 x$.**

(a) Square both definitions:

$\cosh^2 x = \frac{e^{2x}+2+e^{-2x}}{4}$, $\sinh^2 x = \frac{e^{2x}-2+e^{-2x}}{4}$.

Subtract: $\cosh^2 x - \sinh^2 x = \frac{(e^{2x}+2+e^{-2x}) - (e^{2x}-2+e^{-2x})}{4} = \frac{4}{4} = 1$. ✓

(b) $\cosh(2x) = \frac{e^{2x}+e^{-2x}}{2}$. And

$\cosh^2 x + \sinh^2 x = \frac{e^{2x}+2+e^{-2x}}{4} + \frac{e^{2x}-2+e^{-2x}}{4} = \frac{2e^{2x}+2e^{-2x}}{4} = \frac{e^{2x}+e^{-2x}}{2} = \cosh(2x)$. ✓

> **Answer**: both identities verified — the cross terms ($\pm 2$) cancel in (a) but add in (b)

---

## Practice 3

**Given $\sinh x = \frac{3}{4}$ with $x > 0$, find $\cosh x$, $\tanh x$, $\operatorname{sech} x$, $\operatorname{csch} x$, $\coth x$.**

① Core identity: $\cosh^2 x = 1 + \sinh^2 x = 1 + \frac{9}{16} = \frac{25}{16}$ → $\cosh x = \frac54$ (positive since $x>0$).

② $\tanh x = \frac{3/4}{5/4} = \frac35$.

③ Reciprocals: $\operatorname{sech} x = \frac{4}{5}$, $\operatorname{csch} x = \frac{4}{3}$, $\coth x = \frac{5}{3}$.

> **Answer**: $\cosh = \frac54$, $\tanh = \frac35$, $\operatorname{sech} = \frac45$, $\operatorname{csch} = \frac43$, $\coth = \frac53$

---

## Practice 4

**Use Osborne's rule to convert: (a) $\sin 2\theta = 2\sin\theta\cos\theta$ (b) $\cos 2\theta = \cos^2\theta - \sin^2\theta$ (c) $1 + \tan^2\theta = \sec^2\theta$. Then verify one from definitions.**

(a) Single sines — no flip: $\sinh 2x = 2\sinh x\cosh x$.

(b) $-\sin^2\theta$ is a product of two sines — flip: $\cosh 2x = \cosh^2 x + \sinh^2 x$.

(c) $\tan^2\theta$ hides a product of two sines — flip: $1 - \tanh^2 x = \operatorname{sech}^2 x$.

**Verify (b)** from definitions (as in Practice 2b): both sides equal $\frac{e^{2x}+e^{-2x}}{2}$. ✓

> **Answer**: (a) $\sinh 2x = 2\sinh x\cosh x$ (b) $\cosh 2x = \cosh^2x + \sinh^2x$ (c) $1-\tanh^2x = \operatorname{sech}^2x$

---

## Practice 5

**Solve exactly: (a) $\sinh x = 2$ (b) $\tanh x = \frac12$ (c) $\cosh x = 3$.**

(a) $x = \operatorname{arsinh} 2 = \ln(2 + \sqrt{5}) \approx \ln(4.236) \approx 1.444$.

(b) $x = \operatorname{artanh}\tfrac12 = \frac12\ln\left(\frac{1+1/2}{1-1/2}\right) = \frac12\ln\left(\frac{3/2}{1/2}\right) = \frac12\ln 3 \approx 0.549$.

(c) $x = \pm\operatorname{arcosh} 3 = \pm\ln(3 + \sqrt{8}) = \pm\ln(3+2\sqrt2) \approx \pm 1.763$.

> **Answer**: (a) $\ln(2+\sqrt5)$ (b) $\frac12\ln 3$ (c) $\pm\ln(3+2\sqrt2)$

---

## Practice 6

**Differentiate: (a) $\cosh(3x)$ (b) $\sinh(x^2)$ (c) $\tanh x$ (d) $\ln(\cosh x)$.**

(a) $\frac{d}{dx}\cosh(3x) = 3\sinh(3x)$ (chain rule).

(b) $\frac{d}{dx}\sinh(x^2) = 2x\cosh(x^2)$.

(c) $\frac{d}{dx}\tanh x = \operatorname{sech}^2 x$.

(d) $\frac{d}{dx}\ln(\cosh x) = \frac{\sinh x}{\cosh x} = \tanh x$.

> **Answer**: (a) $3\sinh(3x)$ (b) $2x\cosh(x^2)$ (c) $\operatorname{sech}^2 x$ (d) $\tanh x$

---

## Practice 7

**Evaluate: (a) $\int \sinh(2x)\,dx$ (b) $\int \operatorname{sech}^2(3x)\,dx$ (c) $\int_0^1 \frac{dx}{\sqrt{x^2+1}}$.**

(a) Since $\frac{d}{dx}\cosh(2x) = 2\sinh(2x)$: $\int \sinh(2x)\,dx = \frac12\cosh(2x) + C$.

(b) Since $\frac{d}{dx}\tanh(3x) = 3\operatorname{sech}^2(3x)$: $\int \operatorname{sech}^2(3x)\,dx = \frac13\tanh(3x) + C$.

(c) $\int_0^1 \frac{dx}{\sqrt{x^2+1}} = \operatorname{arsinh} x\Big|_0^1 = \operatorname{arsinh} 1 = \ln(1+\sqrt2) \approx 0.8814$.

> **Answer**: (a) $\frac12\cosh(2x)+C$ (b) $\frac13\tanh(3x)+C$ (c) $\ln(1+\sqrt2) \approx 0.8814$

---

## Practice 8: Real Battle

**(a) Show $y = \tanh x$ satisfies $y' = 1-y^2$ with $y(0)=0$. (b) A cable hangs as $y = 3\cosh(x/3)$ for $x\in[-3,3]$: lowest height, end heights, slope at $x=3$.**

(a) $y' = \operatorname{sech}^2 x = 1 - \tanh^2 x = 1 - y^2$ (using $1-\tanh^2 = \operatorname{sech}^2$). And $y(0) = \tanh 0 = 0$. ✓ So $\tanh$ solves the logistic equation $y' = 1-y^2$, $y(0)=0$.

(b) $y = 3\cosh(x/3)$.
- **Lowest point**: $x=0$: $y = 3\cosh 0 = 3$.
- **Ends**: $x=\pm3$: $y = 3\cosh 1 \approx 3(1.5431) = 4.629$.
- **Slope**: $y' = 3\cdot\frac13\sinh(x/3) = \sinh(x/3)$; at $x=3$: $\sinh 1 \approx 1.175$.

> **Answer**: (a) verified — $\tanh$ is the logistic solution (b) lowest $y=3$ at $x=0$; ends $y = 3\cosh 1 \approx 4.63$; slope $\sinh 1 \approx 1.18$

---

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
| Practice 1 | $5/4$, $3/4$, $3/5$; identity holds |
| Practice 2 | both proven from definitions |
| Practice 3 | $\cosh=5/4$, $\tanh=3/5$, reciprocals |
| Practice 4 | (a) no flip (b) flip (c) flip; (b) verified |
| Practice 5 | $\ln(2+\sqrt5)$, $\frac12\ln3$, $\pm\ln(3+2\sqrt2)$ |
| Practice 6 | $3\sinh(3x)$, $2x\cosh(x^2)$, $\operatorname{sech}^2x$, $\tanh x$ |
| Practice 7 | $\frac12\cosh(2x)$, $\frac13\tanh(3x)$, $\ln(1+\sqrt2)$ |
| Practice 8 | logistic check; catenary $y=3$, ends $3\cosh1$, slope $\sinh1$ |
| D1–D10 | see above |
