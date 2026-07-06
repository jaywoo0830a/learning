# Solutions: 13A — Algebraic Limits

---

## Practice 1

$\lim_{x\to2}\frac{x^3-8}{x-2} = \frac{(x-2)(x^2+2x+4)}{x-2} = x^2+2x+4 \to 4+4+4 = 12$.

---

## Practice 2

$\lim_{x\to0}\frac{\sqrt{x+9}-3}{x} \cdot \frac{\sqrt{x+9}+3}{\sqrt{x+9}+3} = \frac{(x+9)-9}{x(\sqrt{x+9}+3)} = \frac{1}{\sqrt{x+9}+3} \to \frac{1}{6}$.

---

## Practice 3

$\frac{\sin7x}{\tan3x} = \frac{\sin7x}{7x} \cdot \frac{3x}{\tan3x} \cdot \frac{7}{3} \to 1\cdot1\cdot\frac{7}{3} = \frac{7}{3}$.

---

## Practice 4

Any three of the form $\frac{(x-a)g(x)}{x-a}$ where $g(a)=5$. Examples:
- $\lim_{x\to3}\frac{(x-3)(x+2)}{x-3}=5$ (since $3+2=5$)
- $\lim_{x\to0}\frac{x(x+5)}{x}=5$
- $\lim_{x\to-1}\frac{(x+1)(x+6)}{x+1}=5$

---

## Practice 5

$\frac{e^{3x}-1}{\ln(1+2x)} = \frac{e^{3x}-1}{3x} \cdot \frac{2x}{\ln(1+2x)} \cdot \frac{3}{2} \to 1\cdot1\cdot\frac{3}{2} = \frac{3}{2}$.

---

## Practice 6

Left: $\lim_{x\to0^-}\frac{\sin x}{x} = 1$. Right: $\lim_{x\to0^+}e^x = 1$. $f(0)=1$.
All three equal 1 → $f$ is continuous at $x=0$.

---

## Basic Drill

**D1.** $2(9)-5(3)+1 = 18-15+1 = 4$.

**D2.** $\frac{(x-1)(x+1)}{x+1} = x-1 \to -2$.

**D3.** $\frac{\sqrt{x}-2}{(\sqrt{x}-2)(\sqrt{x}+2)} = \frac{1}{\sqrt{x}+2} \to \frac{1}{4}$.

**D4.** $4\cdot\frac{\sin4x}{4x} \to 4$.

**D5.** $5\cdot\frac{e^{5x}-1}{5x} \to 5$.

**D6.** $3\cdot\frac{\ln(1+3x)}{3x} \to 3$.

**D7.** $\frac{(x-1)(x+2)}{x-1} = x+2 \to 3$.

**D8.** $\frac{(\sqrt{x+1}-1)(\sqrt{x+1}+1)}{x(\sqrt{x+1}+1)} = \frac{1}{\sqrt{x+1}+1} \to \frac{1}{2}$.

**D9.** $x\to0^+$: $|x|=x$, ratio = 1. Limit = 1.

**D10.** $\frac{\tan2x}{x} = \frac{\sin2x}{\cos2x \cdot x} = 2\cdot\frac{\sin2x}{2x}\cdot\frac{1}{\cos2x} \to 2\cdot1\cdot1 = 2$.

---

## Advanced Drill

**A1.** $x^4-16 = (x^2-4)(x^2+4) = (x-2)(x+2)(x^2+4)$. Cancel $(x-2)$: $(x+2)(x^2+4) \to 4\cdot8 = 32$.

**A2.** $\frac{(\sqrt{2x+4}-2)(\sqrt{2x+4}+2)}{x(\sqrt{2x+4}+2)} = \frac{2x}{x(\sqrt{2x+4}+2)} = \frac{2}{\sqrt{2x+4}+2} \to \frac{2}{4} = \frac{1}{2}$.

**A3.** $\sin3x-\sin x = 2\cos2x\sin x$. Limit: $2\cos0\cdot\frac{\sin x}{x} = 2$.

**A4.** $\frac{2^x-1}{3^x-1} = \frac{2^x-1}{x} \cdot \frac{x}{3^x-1} \to \frac{\ln2}{\ln3}$.

**A5.** $1-\cos2x = 2\sin^2x$. Limit: $\frac{2\sin^2x}{x^2} = 2\left(\frac{\sin x}{x}\right)^2 \to 2$.

**A6.** Conjugate: $\frac{(1+x)-(1-x)}{x(\sqrt{1+x}+\sqrt{1-x})} = \frac{2}{\sqrt{1+x}+\sqrt{1-x}} \to 1$.

**A7.** $\frac{\frac{1}{x}-\frac{1}{3}}{x-3} = \frac{\frac{3-x}{3x}}{x-3} = -\frac{1}{3x} \to -\frac{1}{9}$.

**A8.** $\frac{\sin(x^2)}{x} = x\cdot\frac{\sin(x^2)}{x^2} \to 0\cdot1 = 0$. (As $x\to0$, $x^2\to0$ too.)

**A9.** Let $t=\sqrt[3]{x}$, $x=t^3$. As $x\to1$, $t\to1$.
$\frac{t-1}{t^3-1} = \frac{t-1}{(t-1)(t^2+t+1)} = \frac{1}{t^2+t+1} \to \frac{1}{3}$.

**A10.** $\lim_{x\to1}\frac{x^2-1}{x-1} = \lim_{x\to1}(x+1) = 2$. Set $k=2$ for continuity.
