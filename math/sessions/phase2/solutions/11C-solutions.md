# Solutions — 11C: Hyperbolic Functions — The Trigonometric Functions of a Hyperbola

> Back to [11C — Hyperbolic Functions](../11C-hyperbolic-functions.md)

> **Source.** Every solution below matches an item in Stewart, *Calculus*, Section 3.11. Each heading cites its exercise number.

## Basic Drills

### D1. (§3.11 #1) $\sinh 0$, $\cosh 0$.

$\sinh 0 = \frac{1-1}{2} = 0$; $\cosh 0 = \frac{1+1}{2} = 1$.

> **Answer**: $0$ and $1$

### D2. (§3.11 #2) $\tanh 0$, $\tanh 1$.

$\tanh 0 = \frac{0}{1} = 0$. $\tanh 1 = \frac{e - e^{-1}}{e + e^{-1}} = \frac{e^2-1}{e^2+1} \approx 0.7616$.

> **Answer**: $0$ and $0.762$

### D3. (§3.11 #3) $\cosh(\ln 5)$.

$\cosh(\ln 5) = \frac{5 + 1/5}{2} = \frac{13}{5}$.

> **Answer**: $\frac{13}{5} = 2.6$

### D4. (§3.11 #4) $\sinh(\ln 4)$.

$\sinh(\ln 4) = \frac{4 - 1/4}{2} = \frac{15}{8}$.

> **Answer**: $\frac{15}{8} = 1.875$

### D5. (§3.11 #5) $\operatorname{sech} 0$, $\cosh^{-1} 1$.

$\operatorname{sech} 0 = \frac{1}{\cosh 0} = 1$. $\cosh^{-1} 1 = 0$ since $\cosh 0 = 1$ and the principal value has $y \ge 0$.

> **Answer**: $1$ and $0$

### D6. (§3.11 #6) $\sinh 1$, $\sinh^{-1} 1$.

$\sinh 1 = \frac{e - e^{-1}}{2} \approx 1.1752$. $\sinh^{-1} 1 = \ln(1 + \sqrt2) \approx 0.8814$.

> **Answer**: $1.175$ and $\ln(1+\sqrt2) \approx 0.881$

### D7. (§3.11 #7) $8\sinh x + 5\cosh x$ in terms of $e^x$, $e^{-x}$.

$8\cdot\frac{e^x - e^{-x}}{2} + 5\cdot\frac{e^x + e^{-x}}{2} = \frac{13}{2}e^x - \frac{3}{2}e^{-x}$.

> **Answer**: $\frac{13}{2}e^x - \frac{3}{2}e^{-x}$

### D8. (§3.11 #8) $2e^{2x} + 3e^{-2x}$ in terms of $\sinh 2x$, $\cosh 2x$.

Use $e^{2x} = \cosh 2x + \sinh 2x$ and $e^{-2x} = \cosh 2x - \sinh 2x$:

$2(\cosh 2x + \sinh 2x) + 3(\cosh 2x - \sinh 2x) = 5\cosh 2x - \sinh 2x$.

> **Answer**: $5\cosh 2x - \sinh 2x$

### D9. (§3.11 #9) $\sinh(\ln x)$.

$\sinh(\ln x) = \frac{x - 1/x}{2} = \frac{x^2-1}{2x}$.

> **Answer**: $\frac{x^2-1}{2x}$

### D10. (§3.11 #10) $\cosh(4\ln x)$.

$\cosh(4\ln x) = \frac{x^4 + x^{-4}}{2} = \frac{x^8+1}{2x^4}$.

> **Answer**: $\frac{x^8+1}{2x^4}$

### D11. (§3.11 #11–12) Parity.

$\sinh(-x) = \frac{e^{-x}-e^x}{2} = -\frac{e^x-e^{-x}}{2} = -\sinh x$ (odd).
$\cosh(-x) = \frac{e^{-x}+e^x}{2} = \cosh x$ (even).

> **Answer**: $\sinh$ is odd; $\cosh$ is even

### D12. (§3.11 #13–14) $\cosh x \pm \sinh x$.

$\cosh x + \sinh x = \frac{e^x+e^{-x}}{2} + \frac{e^x-e^{-x}}{2} = e^x$; $\cosh x - \sinh x = e^{-x}$.

> **Answer**: $\cosh x + \sinh x = e^x$, $\cosh x - \sinh x = e^{-x}$

---

### D13. (§3.11 #17) $\coth^2 x - 1 = \operatorname{csch}^2 x$.

$\coth^2 x - 1 = \frac{\cosh^2 x}{\sinh^2 x} - 1 = \frac{\cosh^2 x - \sinh^2 x}{\sinh^2 x} = \frac{1}{\sinh^2 x} = \operatorname{csch}^2 x$. ✓

> **Answer**: follows from $\cosh^2 x - \sinh^2 x = 1$

### D14. (§3.11 #19–20) Double angle.

$\sinh 2x = \sinh(x+x) = \sinh x\cosh x + \cosh x\sinh x = 2\sinh x\cosh x$.
$\cosh 2x = \cosh(x+x) = \cosh x\cosh x + \sinh x\sinh x = \cosh^2 x + \sinh^2 x$.

> **Answer**: $\sinh 2x = 2\sinh x\cosh x$, $\cosh 2x = \cosh^2 x + \sinh^2 x$

### D15. (§3.11 #21) $\tanh(\ln x)$.

$\tanh(\ln x) = \frac{\sinh(\ln x)}{\cosh(\ln x)} = \frac{(x - 1/x)/2}{(x + 1/x)/2} = \frac{x^2-1}{x^2+1}$.

> **Answer**: $\frac{x^2-1}{x^2+1}$

### D16. (§3.11 #24) $\tanh x = \frac{12}{13}$.

Write $\sinh x = 12k$, $\cosh x = 13k$. Then $\cosh^2 x - \sinh^2 x = (169-144)k^2 = 25k^2 = 1$, so $k = \frac15$. Since $\tanh x > 0$, $x > 0$:

$\sinh x = \frac{12}{5}$, $\cosh x = \frac{13}{5}$, $\coth x = \frac{13}{12}$, $\operatorname{sech} x = \frac{5}{13}$, $\operatorname{csch} x = \frac{5}{12}$.

> **Answer**: $\sinh x = \frac{12}{5}$, $\cosh x = \frac{13}{5}$, $\coth x = \frac{13}{12}$, $\operatorname{sech} x = \frac{5}{13}$, $\operatorname{csch} x = \frac{5}{12}$

### D17. (§3.11 #25) $\cosh x = \frac53$, $x>0$.

$\sinh x = \sqrt{\cosh^2 x - 1} = \sqrt{\frac{25}{9} - 1} = \frac43$ (positive since $x>0$). Then

$\tanh x = \frac{4}{5}$, $\coth x = \frac{5}{4}$, $\operatorname{sech} x = \frac{3}{5}$, $\operatorname{csch} x = \frac{3}{4}$.

> **Answer**: $\sinh x = \frac43$, $\tanh x = \frac45$, $\coth x = \frac54$, $\operatorname{sech} x = \frac35$, $\operatorname{csch} x = \frac34$

### D18. (§3.11 #27) Limits of $\tanh$.

$\tanh x = \frac{e^x - e^{-x}}{e^x + e^{-x}} = \frac{1 - e^{-2x}}{1 + e^{-2x}}$. As $x\to\infty$, $e^{-2x}\to0$, so the limit is $1$. As $x\to-\infty$, $e^{-2x}\to\infty$, so the limit is $-1$.

> **Answer**: $1$ and $-1$

### D19. (§3.11 #35) $\frac{d}{dx}\cosh 3x$.

$\frac{d}{dx}\cosh 3x = 3\sinh 3x$.

> **Answer**: $3\sinh 3x$

### D20. (§3.11 #37) $\frac{d}{dx}\sinh(x^2)$.

$\frac{d}{dx}\sinh(x^2) = \cosh(x^2)\cdot 2x = 2x\cosh(x^2)$.

> **Answer**: $2x\cosh(x^2)$

### D21. (§3.11 #41) $\frac{d}{dx}\tanh\sqrt{x}$.

$\frac{d}{dx}\tanh\sqrt{x} = \operatorname{sech}^2\sqrt{x}\cdot\frac{1}{2\sqrt{x}} = \frac{\operatorname{sech}^2\sqrt{x}}{2\sqrt{x}}$.

> **Answer**: $\frac{\operatorname{sech}^2\sqrt{x}}{2\sqrt{x}}$

### D22. (§3.11 #47) $\frac{d}{dx}\sinh^{-1}(-2x)$.

$\frac{d}{dx}\sinh^{-1}(-2x) = \frac{1}{\sqrt{1+(-2x)^2}}\cdot(-2) = \frac{-2}{\sqrt{1+4x^2}}$.

> **Answer**: $\frac{-2}{\sqrt{1+4x^2}}$

### D23. (§3.11 #48) $\frac{d}{dx}\tanh^{-1}(x^3)$.

$\frac{d}{dx}\tanh^{-1}(x^3) = \frac{1}{1-(x^3)^2}\cdot 3x^2 = \frac{3x^2}{1-x^6}$.

> **Answer**: $\frac{3x^2}{1-x^6}$

### D24. (§3.11 #65) Slope $1$ on $y = \cosh x$.

Set $y' = \sinh x = 1$, so $x = \sinh^{-1} 1 = \ln(1+\sqrt2)$. At that $x$, $\cosh^2 x = 1 + \sinh^2 x = 2$, so $\cosh x = \sqrt2$.

> **Answer**: $\left(\ln(1+\sqrt2),\ \sqrt2\right)$

---

## Advanced Drills

### A1. (§3.11 #15) Prove $\sinh(x+y) = \sinh x\cosh y + \cosh x\sinh y$.

Right side: $\frac{(e^x-e^{-x})(e^y+e^{-y}) + (e^x+e^{-x})(e^y-e^{-y})}{4}$.

The first product is $e^{x+y}+e^{x-y}-e^{-x+y}-e^{-x-y}$; the second is $e^{x+y}-e^{x-y}+e^{-x+y}-e^{-x-y}$.

Their sum is $2e^{x+y}-2e^{-x-y}$, so the right side is $\frac{e^{x+y}-e^{-x-y}}{2} = \sinh(x+y)$. ✓

> **Answer**: the cross terms $e^{x-y}, e^{-x+y}$ erase, leaving $\sinh(x+y)$

### A2. (§3.11 #16) Prove $\cosh(x+y) = \cosh x\cosh y + \sinh x\sinh y$.

Right side: $\frac{(e^x+e^{-x})(e^y+e^{-y}) + (e^x-e^{-x})(e^y-e^{-y})}{4}$.

The first product is $e^{x+y}+e^{x-y}+e^{-x+y}+e^{-x-y}$; the second is $e^{x+y}-e^{x-y}-e^{-x+y}+e^{-x-y}$.

Their sum is $2e^{x+y}+2e^{-x-y}$, so the right side is $\frac{e^{x+y}+e^{-x-y}}{2} = \cosh(x+y)$. ✓

> **Answer**: the cross terms erase, leaving $\cosh(x+y)$

### A3. (§3.11 #18) Derive $\tanh(x+y)$.

$\tanh(x+y) = \frac{\sinh x\cosh y + \cosh x\sinh y}{\cosh x\cosh y + \sinh x\sinh y}$. Divide top and bottom by $\cosh x\cosh y$:

$$= \frac{\tanh x + \tanh y}{1 + \tanh x\,\tanh y}. ✓$$

> **Answer**: $\tanh(x+y) = \frac{\tanh x + \tanh y}{1 + \tanh x\tanh y}$ — the trig minus became a plus

### A4. (§3.11 #22) $\frac{1+\tanh x}{1-\tanh x} = e^{2x}$.

$1 + \tanh x = \frac{\cosh x + \sinh x}{\cosh x} = \frac{e^x}{\cosh x}$, and $1 - \tanh x = \frac{\cosh x - \sinh x}{\cosh x} = \frac{e^{-x}}{\cosh x}$.

The ratio is $\frac{e^x}{e^{-x}} = e^{2x}$. ✓

> **Answer**: both sides reduce to $e^{2x}$

### A5. (§3.11 #23) $(\cosh x + \sinh x)^n = \cosh nx + \sinh nx$.

$\cosh x + \sinh x = e^x$ (Exercise 13). So $(\cosh x + \sinh x)^n = (e^x)^n = e^{nx} = \cosh nx + \sinh nx$. ✓

> **Answer**: reduce the base to $e^x$, then use $e^{nx} = \cosh nx + \sinh nx$

### A6. (§3.11 #28) Prove $\frac{d}{dx}\operatorname{sech} x = -\operatorname{sech} x\tanh x$.

$\operatorname{sech} x = \frac{1}{\cosh x}$. By the Chain Rule,

$$\frac{d}{dx}\frac{1}{\cosh x} = -\frac{\sinh x}{\cosh^2 x} = -\frac{1}{\cosh x}\cdot\frac{\sinh x}{\cosh x} = -\operatorname{sech} x\tanh x. ✓$$

> **Answer**: $-\operatorname{sech} x\tanh x$

### A7. (§3.11 #29) Alternative solution to Example 3.

Let $y = \sinh^{-1} x$, so $\sinh y = x$. Then $\cosh^2 y = 1 + \sinh^2 y = 1 + x^2$, and $\cosh y = \sqrt{1+x^2}$ (positive). So

$$e^y = \cosh y + \sinh y = \sqrt{1+x^2} + x \quad\Rightarrow\quad y = \ln\left(x + \sqrt{1+x^2}\right). ✓$$

> **Answer**: use $e^y = \cosh y + \sinh y$ instead of the quadratic

### A8. (§3.11 #30) Prove $\cosh^{-1} x = \ln\left(x + \sqrt{x^2-1}\right)$, $x \ge 1$.

Let $y = \cosh^{-1} x$ with $y \ge 0$, so $x = \cosh y = \frac{e^y + e^{-y}}{2}$. Multiply by $2e^y$:

$$e^{2y} - 2x\,e^y + 1 = 0 \quad\Rightarrow\quad e^y = x \pm \sqrt{x^2-1}.$$

Since $y \ge 0$, $e^y \ge 1$; the root $x - \sqrt{x^2-1} \le 1$ is inadmissible (it equals $1$ only at $x=1$). So $e^y = x + \sqrt{x^2-1}$, and $y = \ln\left(x + \sqrt{x^2-1}\right)$. ✓

> **Answer**: $\cosh^{-1} x = \ln\left(x + \sqrt{x^2-1}\right)$

### A9. (§3.11 #31) Prove $\tanh^{-1} x = \frac12\ln\left(\frac{1+x}{1-x}\right)$.

(a) Let $y = \tanh^{-1} x$, so $x = \frac{e^y - e^{-y}}{e^y + e^{-y}}$. Then $x(e^y + e^{-y}) = e^y - e^{-y}$, so $xe^{2y} + x = e^{2y} - 1$, giving $e^{2y}(x-1) = -(1+x)$ and $e^{2y} = \frac{1+x}{1-x}$. Hence $y = \frac12\ln\frac{1+x}{1-x}$.

(b) Verify the log form: let $u = \frac12\ln\frac{1+x}{1-x}$, so $e^{2u} = \frac{1+x}{1-x}$. Then $\tanh u = \frac{e^{2u}-1}{e^{2u}+1} = \frac{(1+x)-(1-x)}{(1+x)+(1-x)} = \frac{2x}{2} = x$. ✓

> **Answer**: $\tanh^{-1} x = \frac12\ln\frac{1+x}{1-x}$

### A10. (§3.11 #33) Prove $\frac{d}{dx}\cosh^{-1} x = \frac{1}{\sqrt{x^2-1}}$.

Let $y = \cosh^{-1} x$, so $\cosh y = x$ and $y \ge 0$. Differentiate implicitly:

$$\sinh y\,\frac{dy}{dx} = 1 \quad\Rightarrow\quad \frac{dy}{dx} = \frac{1}{\sinh y} = \frac{1}{\sqrt{\cosh^2 y - 1}} = \frac{1}{\sqrt{x^2-1}}. ✓$$

> **Answer**: $\frac{1}{\sqrt{x^2-1}}$

---

### A11. (§3.11 #54) Show $\frac{d}{dx}\sqrt[4]{\frac{1+\tanh x}{1-\tanh x}} = \frac12 e^{x/2}$.

By Exercise 22, $\frac{1+\tanh x}{1-\tanh x} = e^{2x}$. So the function is $\left(e^{2x}\right)^{1/4} = e^{x/2}$, and its derivative is $\frac12 e^{x/2}$. ✓

> **Answer**: reduce the base to $e^{2x}$, so the function is $e^{x/2}$

### A12. (§3.11 #55) Show $\frac{d}{dx}\arctan(\tanh x) = \operatorname{sech} 2x$.

$$\frac{d}{dx}\arctan(\tanh x) = \frac{1}{1+\tanh^2 x}\cdot\operatorname{sech}^2 x = \frac{\operatorname{sech}^2 x}{1+\tanh^2 x}.$$

Now $\operatorname{sech} 2x = \frac{1}{\cosh 2x} = \frac{1}{\cosh^2 x + \sinh^2 x} = \frac{\operatorname{sech}^2 x}{1+\tanh^2 x}$, which matches. ✓

> **Answer**: both sides equal $\frac{\operatorname{sech}^2 x}{1+\tanh^2 x}$

### A13. (§3.11 #56) Gateway Arch $y = 211.49 - 20.96\cosh(0.03291765x)$.

(a) At $x=0$: $y = 211.49 - 20.96 = 190.53$ m.

(b) $211.49 - 20.96\cosh(0.03291765x) = 100$ gives $\cosh(0.03291765x) = \frac{111.49}{20.96} = 5.3192$. So $0.03291765x = \cosh^{-1}(5.3192) \approx 2.3556$, giving $x \approx \pm 71.6$ m.

(c) $y' = -20.96\cdot 0.03291765\sinh(0.03291765x) = -0.68995\sinh(0.03291765x)$. At $x \approx 71.6$, $\sinh(2.3556) \approx 5.224$, so the slope is $\approx -3.60$.

> **Answer**: (a) $190.5$ m (b) $x \approx \pm 71.6$ m (c) slope $\approx \mp 3.60$

### A14. (§3.11 #57) Deep-water wave speed.

In deep water $d/L \to \infty$, so $\frac{2\pi d}{L} \to \infty$ and $\tanh\left(\frac{2\pi d}{L}\right) \to 1$. Therefore $v = \sqrt{\frac{gL}{2\pi}\tanh\left(\frac{2\pi d}{L}\right)} \to \sqrt{\frac{gL}{2\pi}}$, which no longer contains $d$.

> **Answer**: $\tanh \to 1$ makes the depth $d$ drop out

### A15. (§3.11 #59) Telephone line $y = 20\cosh(x/20) - 15$.

(a) $y' = \sinh(x/20)$. At the right-hand pole $x = 7$: slope $= \sinh(0.35) \approx 0.357$.

(b) The tangent makes an angle $\arctan(0.357) \approx 19.7°$ with the horizontal, so it makes $90° - 19.7° \approx 70.3°$ with the vertical pole.

> **Answer**: (a) $\approx 0.357$ (b) $\approx 70.3°$

### A16. (§3.11 #60) Verify the catenary solves the hanging-cable equation.

$y = \frac{T}{\rho g}\cosh\left(\frac{\rho g x}{T}\right)$ gives $y' = \sinh\left(\frac{\rho g x}{T}\right)$ and $y'' = \frac{\rho g}{T}\cosh\left(\frac{\rho g x}{T}\right)$.

The right side is $\frac{\rho g}{T}\sqrt{1+(y')^2} = \frac{\rho g}{T}\sqrt{1+\sinh^2\left(\frac{\rho g x}{T}\right)} = \frac{\rho g}{T}\cosh\left(\frac{\rho g x}{T}\right) = y''$. ✓

> **Answer**: $1+(y')^2 = \cosh^2\left(\frac{\rho g x}{T}\right)$, so both sides are $\frac{\rho g}{T}\cosh\left(\frac{\rho g x}{T}\right)$

### A17. (§3.11 #62) Falling object.

(a) As $t\to\infty$, $\tanh \to 1$, so the terminal velocity is $\sqrt{\frac{mg}{k}}$.

(b) With $m = 60$ kg and $g = 9.8$ m/s², $mg = 588$. For $k = 0.515$: $\sqrt{\frac{588}{0.515}} \approx 33.8$ m/s. For $k = 0.067$: $\sqrt{\frac{588}{0.067}} \approx 93.7$ m/s.

> **Answer**: (a) $\sqrt{mg/k}$ (b) $\approx 33.8$ m/s and $\approx 93.7$ m/s

### A18. (§3.11 #63) $y'' = m^2 y$.

(a) $y = A\sinh mx + B\cosh mx$ gives $y' = Am\cosh mx + Bm\sinh mx$ and $y'' = Am^2\sinh mx + Bm^2\cosh mx = m^2 y$. ✓

(b) $y'' = 9y$ means $m = 3$. Write $y = A\sinh 3x + B\cosh 3x$. Then $y(0) = B = -4$, and $y'(0) = 3A = 6$, so $A = 2$. Thus $y = 2\sinh 3x - 4\cosh 3x$.

> **Answer**: (a) $y'' = m^2 y$ (b) $y = 2\sinh 3x - 4\cosh 3x$

### A19. (§3.11 #64) If $x = \ln(\sec\theta + \tan\theta)$, show $\sec\theta = \cosh x$.

$e^x = \sec\theta + \tan\theta$, and $e^{-x} = \frac{1}{\sec\theta + \tan\theta} = \frac{\sec\theta - \tan\theta}{\sec^2\theta - \tan^2\theta} = \sec\theta - \tan\theta$. Then

$$\cosh x = \frac{e^x + e^{-x}}{2} = \frac{(\sec\theta + \tan\theta) + (\sec\theta - \tan\theta)}{2} = \sec\theta. ✓$$

> **Answer**: the $\tan\theta$ terms erase, leaving $\sec\theta$

### A20. (§3.11 #67) $a e^x + b e^{-x}$ as a shifted sinh or cosh.

Write $a e^x + b e^{-x} = (a+b)\cosh x + (a-b)\sinh x$.

- If $ab > 0$: use $\alpha\cosh(x+\beta) = \alpha\cosh\beta\cosh x + \alpha\sinh\beta\sinh x$ with $\alpha\cosh\beta = a+b$, $\alpha\sinh\beta = a-b$, so $\alpha = 2\sqrt{ab}$ and $\beta = \tanh^{-1}\left(\frac{a-b}{a+b}\right)$.
- If $ab < 0$: use $\alpha\sinh(x+\beta) = \alpha\sinh\beta\cosh x + \alpha\cosh\beta\sinh x$ with $\alpha\sinh\beta = a+b$, $\alpha\cosh\beta = a-b$, so $\alpha = 2\sqrt{-ab}$ and $\beta = \tanh^{-1}\left(\frac{a+b}{a-b}\right)$.

> **Answer**: $\alpha\cosh(x+\beta)$ when $ab>0$, $\alpha\sinh(x+\beta)$ when $ab<0$

---

## Answer Check

| Problem | Answer |
|:--------|:-------|
| D1–D6 | values: $0,1$; $0,0.762$; $2.6$; $1.875$; $1,0$; $1.175,\ 0.881$ |
| D7–D12 | $\frac{13}{2}e^x-\frac32e^{-x}$; $5\cosh2x-\sinh2x$; $\frac{x^2-1}{2x}$; $\frac{x^8+1}{2x^4}$; parity; $\cosh x\pm\sinh x=e^{\pm x}$ |
| D13–D18 | $\coth^2-1=\operatorname{csch}^2$; double angle; $\frac{x^2-1}{x^2+1}$; $\frac{12}{5},\frac{13}{5},\dots$; $\frac43,\frac45,\dots$; $1,-1$ |
| D19–D24 | $3\sinh3x$; $2x\cosh(x^2)$; $\frac{\operatorname{sech}^2\sqrt x}{2\sqrt x}$; $\frac{-2}{\sqrt{1+4x^2}}$; $\frac{3x^2}{1-x^6}$; $\left(\ln(1+\sqrt2),\sqrt2\right)$ |
| A1–A20 | see above |