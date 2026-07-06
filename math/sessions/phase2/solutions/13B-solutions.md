# Solutions: 13B — Limits at Infinity

---

## Practice 1

$\frac{\sqrt{4x^2+3x}}{2x-1} = \frac{|x|\sqrt{4+3/x}}{x(2-1/x)}$. For $x\to\infty$, $|x|=x$:
$= \frac{\sqrt{4+3/x}}{2-1/x} \to \frac{\sqrt{4}}{2} = 1$.

---

## Practice 2

Divide by $x^3$: $\frac{2-5/x^2+1/x^3}{3+4/x} \to \frac{2}{3}$.

---

## Practice 3

Conjugate: $\frac{(x^2+5x)-(x^2-3x)}{\sqrt{x^2+5x}+\sqrt{x^2-3x}} = \frac{8x}{\sqrt{x^2+5x}+\sqrt{x^2-3x}}$.
Divide by $x$: $\frac{8}{\sqrt{1+5/x}+\sqrt{1-3/x}} \to \frac{8}{2} = 4$.

---

## Practice 4

$x^2 \to 0^+$ from both sides. $\frac{1}{0^+} \to +\infty$. Yes, the two-sided limit is $+\infty$.

---

## Practice 5

$(1+\frac{5}{n})^{2n} = \left[(1+\frac{5}{n})^{n}\right]^2 \to (e^5)^2 = e^{10}$.

---

## Practice 6

$\frac{e^x + x^{100}}{2^x + x!} = \frac{e^x/x! + x^{100}/x!}{2^x/x! + 1}$. All three fractions → 0 since factorial dominates. → **0**.

---

## Basic Drill

**D1.** $\frac{5-3/x^2}{2+1/x^2} \to \frac{5}{2}$.

**D2.** $\frac{1/x^2+1/x^3}{1-2/x^3} \to \frac{0}{1} = 0$.

**D3.** Leading terms: $\frac{2x^3}{x^2} = 2x \to \infty$.

**D4.** $\frac{4}{2-5/x^2} \to 2$.

**D5.** $x\to0^+$, denominator → $0^+$. $\frac{1}{0^+} \to +\infty$.

**D6.** $x^4 \to 0^+$ from both sides. → $+\infty$.

**D7.** $\frac{(x^2+2x)-x^2}{\sqrt{x^2+2x}+x} = \frac{2x}{\sqrt{x^2+2x}+x} \to \frac{2}{2} = 1$.

**D8.** $e^2$.

**D9.** $\frac{\ln x}{x^{0.5}} \to 0$ (log ≪ polynomial).

**D10.** $n^{1/n} \to 1$.

---

## Advanced Drill

**A1.** $\frac{\sqrt{9x^2+2}}{3x+1} = \frac{|x|\sqrt{9+2/x^2}}{x(3+1/x)}$. $x\to-\infty$, $|x|=-x$: $\frac{-x\sqrt{9}}{3x} = -\frac{3}{3} = -1$.

**A2.** $\frac{\sqrt{x^2+1}+\sqrt{x^2-1}}{x} = \sqrt{1+1/x^2} + \sqrt{1-1/x^2} \to 1+1 = 2$.

**A3.** $\frac{(x-1)(x-2)}{(x-2)(x+2)} = \frac{x-1}{x+2} \to \frac{1}{4}$.

**A4.** $\frac{x+2}{x-1} = 1+\frac{3}{x-1}$. $(1+\frac{3}{x-1})^{3x} = [(1+\frac{3}{x-1})^{x-1}]^3 \cdot (1+\frac{3}{x-1})^3 \to (e^3)^3 \cdot 1 = e^9$.

**A5.** Both → $-\infty$. $\frac{\ln\sin x}{\ln x} = \frac{\ln(x\cdot\sin x/x)}{\ln x} = \frac{\ln x + \ln(\sin x/x)}{\ln x} = 1 + \frac{\ln(\sin x/x)}{\ln x} \to 1+0 = 1$.

**A6.** $\frac{5^x((3/5)^x+(2/5)^x)}{5^x(1-(4/5)^x)} = \frac{(3/5)^x+(2/5)^x}{1-(4/5)^x} \to \frac{0+0}{1-0} = 0$.

**A7.** $a^3-b^3 = (a-b)(a^2+ab+b^2)$. $a=\sqrt[3]{x^3+x^2}$, $b=x$.
Difference = $\frac{(x^3+x^2)-x^3}{(\sqrt[3]{x^3+x^2})^2 + x\sqrt[3]{x^3+x^2} + x^2} = \frac{x^2}{\cdots}$.
Divide by $x^2$: denominator $\approx x^2+x^2+x^2 = 3x^2$. → $\frac{1}{3}$.

**A8.** $\frac{(\sqrt{x+3}-2)(\sqrt{x+3}+2)}{(\sqrt{x}-1)(\sqrt{x}+1)} \cdot \frac{\sqrt{x}+1}{\sqrt{x+3}+2} = \frac{(x+3-4)(\sqrt{x}+1)}{(x-1)(\sqrt{x+3}+2)} = \frac{(x-1)(\sqrt{x}+1)}{(x-1)(\sqrt{x+3}+2)} = \frac{\sqrt{x}+1}{\sqrt{x+3}+2} \to \frac{2}{4} = \frac{1}{2}$.

**A9.** $(1+\frac{1}{n^2})^{n^2} \to e^1 = e$.

**A10.** $\frac{1-\cos x}{x\sin x} = \frac{1-\cos x}{x^2} \cdot \frac{x}{\sin x} \to \frac{1}{2} \cdot 1 = \frac{1}{2}$.
