# Solutions — 11B: Trigonometric Identities, Equations, and Beyond

> Back to [11B — Trigonometric Identities, Equations, and Beyond](../11B-trig-advanced.md)
## Basic Drills

**D1.** $\sin 75^\circ = \sin(45^\circ+30^\circ) = \frac{\sqrt{2}}{2}\cdot\frac{\sqrt{3}}{2} + \frac{\sqrt{2}}{2}\cdot\frac{1}{2} = \frac{\sqrt{6}+\sqrt{2}}{4}$.

**D2.** $\cos 105^\circ = \cos(60^\circ+45^\circ) = \frac{1}{2}\cdot\frac{\sqrt{2}}{2} - \frac{\sqrt{3}}{2}\cdot\frac{\sqrt{2}}{2} = \frac{\sqrt{2}-\sqrt{6}}{4}$.

**D3.** $\tan 15^\circ = \tan(45^\circ-30^\circ) = \frac{1 - 1/\sqrt{3}}{1 + 1/\sqrt{3}} = \frac{\sqrt{3}-1}{\sqrt{3}+1} = 2-\sqrt{3}$.

**D4.** $\sin A = \frac{3}{5}$ (QI) → $\cos A = \frac{4}{5}$. $\cos B = \frac{5}{13}$ (QI) → $\sin B = \frac{12}{13}$.
$\sin(A+B) = \frac{3}{5}\cdot\frac{5}{13} + \frac{4}{5}\cdot\frac{12}{13} = \frac{15}{65} + \frac{48}{65} = \frac{63}{65}$.

**D5.** $\cos\theta = -\frac{4}{5}$ (QII). $\cos 2\theta = 2\cos^2\theta - 1 = 2\cdot\frac{16}{25} - 1 = \frac{32}{25} - 1 = \frac{7}{25}$.

**D6.** $\sin 3x\cos x = \frac{1}{2}[\sin(3x+x) + \sin(3x-x)] = \frac{1}{2}[\sin 4x + \sin 2x]$.

**D7.** $\sin 5x + \sin x = 2\sin\frac{5x+x}{2}\cos\frac{5x-x}{2} = 2\sin 3x \cos 2x$.

**D8.** $\arcsin\frac{\sqrt{3}}{2} = \frac{\pi}{3}$. $\arccos(-\frac{1}{2}) = \frac{2\pi}{3}$.

**D9.** $\alpha = \arcsin\frac{3}{5}$ → $\sin\alpha = \frac{3}{5}$, $\cos\alpha = \frac{4}{5}$.
$\beta = \arccos\frac{5}{13}$ → $\cos\beta = \frac{5}{13}$, $\sin\beta = \frac{12}{13}$.
$\sin(\alpha+\beta) = \frac{3}{5}\cdot\frac{5}{13} + \frac{4}{5}\cdot\frac{12}{13} = \frac{15}{65} + \frac{48}{65} = \frac{63}{65}$.

**D10.** Law of Sines: $\frac{b}{\sin 60^\circ} = \frac{8}{\sin 40^\circ}$.
$b = 8 \cdot \frac{\sin 60^\circ}{\sin 40^\circ} = 8 \cdot \frac{\sqrt{3}/2}{\sin 40^\circ} \approx 8 \cdot \frac{0.8660}{0.6428} \approx 10.78$.

---

## Advanced Drills

### A1

$\frac{\sin 2x}{1+\cos 2x} = \frac{2\sin x\cos x}{1+(2\cos^2 x-1)} = \frac{2\sin x\cos x}{2\cos^2 x} = \frac{\sin x}{\cos x} = \tan x$. ✓

For $x = 15^\circ$: $\frac{\sin 30^\circ}{1+\cos 30^\circ} = \frac{1/2}{1+\sqrt{3}/2} = \frac{1}{2+\sqrt{3}} = 2-\sqrt{3}$. So $\tan 15^\circ = 2-\sqrt{3}$.

### A2

$\cos 2x + 3\sin x = 2$. Replace $\cos 2x = 1 - 2\sin^2 x$:
$1 - 2\sin^2 x + 3\sin x = 2$ → $-2\sin^2 x + 3\sin x - 1 = 0$ → $2\sin^2 x - 3\sin x + 1 = 0$.

$t = \sin x$: $(2t-1)(t-1) = 0$ → $t = \frac{1}{2}$ or $t = 1$.

$\sin x = \frac{1}{2}$ → $x = \frac{\pi}{6}, \frac{5\pi}{6}$.
$\sin x = 1$ → $x = \frac{\pi}{2}$.

Solutions on $[0, 2\pi]$: $x \in \{\frac{\pi}{6}, \frac{\pi}{2}, \frac{5\pi}{6}\}$.

### A3

$\tan^2 x - (1+\sqrt{3})\tan x + \sqrt{3} = 0$. $t = \tan x$:
$t^2 - (1+\sqrt{3})t + \sqrt{3} = 0$.

Quadratic formula: $t = \frac{(1+\sqrt{3}) \pm \sqrt{(1+\sqrt{3})^2 - 4\sqrt{3}}}{2} = \frac{(1+\sqrt{3}) \pm \sqrt{1+2\sqrt{3}+3-4\sqrt{3}}}{2}$
$= \frac{(1+\sqrt{3}) \pm \sqrt{4-2\sqrt{3}}}{2} = \frac{(1+\sqrt{3}) \pm (\sqrt{3}-1)}{2}$.

$t_1 = \frac{1+\sqrt{3}+\sqrt{3}-1}{2} = \sqrt{3}$.
$t_2 = \frac{1+\sqrt{3}-\sqrt{3}+1}{2} = 1$.

$\tan x = \sqrt{3}$ → $x = \frac{\pi}{3}, \frac{4\pi}{3}$.
$\tan x = 1$ → $x = \frac{\pi}{4}, \frac{5\pi}{4}$.

Solutions: $x \in \{\frac{\pi}{4}, \frac{\pi}{3}, \frac{5\pi}{4}, \frac{4\pi}{3}\}$.

### A4

$\cos 2x + \cos x < 0$. Replace $\cos 2x = 2\cos^2 x - 1$:
$2\cos^2 x - 1 + \cos x < 0$ → $2\cos^2 x + \cos x - 1 < 0$.

$t = \cos x$, $t \in [-1, 1]$: $(2t-1)(t+1) < 0$.
Roots: $t = \frac{1}{2}$, $t = -1$.
Sign chart: $t \in (-1, \frac{1}{2})$ makes product negative. ✓

So $-1 < \cos x < \frac{1}{2}$.

$\cos x > -1$: all $x$ except $\pi$.
$\cos x < \frac{1}{2}$: $x \in (\frac{\pi}{3}, \frac{5\pi}{3})$.

Intersection: $x \in (\frac{\pi}{3}, \pi) \cup (\pi, \frac{5\pi}{3})$.

### A5

$\sin^4\theta - \cos^4\theta = (\sin^2\theta - \cos^2\theta)(\sin^2\theta + \cos^2\theta) = (\sin^2\theta - \cos^2\theta) \cdot 1$
$= -(\cos^2\theta - \sin^2\theta) = -\cos 2\theta$.

Answer: $\sin^4\theta - \cos^4\theta = -\cos 2\theta$.

### A6

Let $P = \cos 20^\circ \cdot \cos 40^\circ \cdot \cos 80^\circ$. Multiply and divide by $\sin 20^\circ$:

$P = \frac{\sin 20^\circ \cos 20^\circ \cos 40^\circ \cos 80^\circ}{\sin 20^\circ}$.

$\sin 20^\circ \cos 20^\circ = \frac{1}{2}\sin 40^\circ$:
$P = \frac{\frac{1}{2}\sin 40^\circ \cos 40^\circ \cos 80^\circ}{\sin 20^\circ}$.

$\sin 40^\circ \cos 40^\circ = \frac{1}{2}\sin 80^\circ$:
$P = \frac{\frac{1}{4}\sin 80^\circ \cos 80^\circ}{\sin 20^\circ}$.

$\sin 80^\circ \cos 80^\circ = \frac{1}{2}\sin 160^\circ = \frac{1}{2}\sin 20^\circ$ (since $\sin 160^\circ = \sin 20^\circ$):
$P = \frac{\frac{1}{8}\sin 20^\circ}{\sin 20^\circ} = \frac{1}{8}$.

→ $\cos 20^\circ \cdot \cos 40^\circ \cdot \cos 80^\circ = \frac{1}{8}$.

![A6: Three cosines on the unit circle](../graphs/sol11b-a6-morrie.png)

### A7

$\sin 3x = \sin x$ → $\sin 3x - \sin x = 0$ → $2\cos\frac{3x+x}{2}\sin\frac{3x-x}{2} = 0$ → $2\cos 2x \sin x = 0$.

$\cos 2x = 0$: $2x = \frac{\pi}{2} + n\pi$ → $x = \frac{\pi}{4} + \frac{n\pi}{2}$.
On $[0, 2\pi]$: $x = \frac{\pi}{4}, \frac{3\pi}{4}, \frac{5\pi}{4}, \frac{7\pi}{4}$.

$\sin x = 0$: $x = n\pi$.
On $[0, 2\pi]$: $x = 0, \pi, 2\pi$.

All solutions: $x \in \{0, \frac{\pi}{4}, \frac{3\pi}{4}, \pi, \frac{5\pi}{4}, \frac{7\pi}{4}, 2\pi\}$.

### A8

Chebyshev recurrence: $T_{n+1}(x) = 2xT_n(x) - T_{n-1}(x)$.
$T_3 = 4x^3-3x$, $T_4 = 8x^4-8x^2+1$.

$T_5(x) = 2x(8x^4-8x^2+1) - (4x^3-3x)$
$= 16x^5 - 16x^3 + 2x - 4x^3 + 3x$
$= 16x^5 - 20x^3 + 5x$.

Thus $\cos 5\theta = T_5(\cos\theta) = 16\cos^5\theta - 20\cos^3\theta + 5\cos\theta$.

### A9

$p=2, q=5$: $a = q^2-p^2 = 25-4 = 21$. $b = 2pq = 20$. $c = q^2+p^2 = 25+4 = 29$.

Verify: $21^2 + 20^2 = 441 + 400 = 841 = 29^2$. ✓

Triple: $(21, 20, 29)$.

### A10

$b_n = \frac{2(-1)^{n+1}}{n}$. First three nonzero: $n=1,2,3$.
$b_1 = 2$, $b_2 = -1$, $b_3 = \frac{2}{3}$.

$f(x) = 2\sin x - \sin 2x + \frac{2}{3}\sin 3x + \cdots$

At $x = \frac{\pi}{2}$: $f(\frac{\pi}{2}) = 2(1) - (0) + \frac{2}{3}(-1) = 2 - \frac{2}{3} = \frac{4}{3}$.
The full Fourier series converges to $x$ on $(-\pi, \pi)$ (except at endpoints). At $x = \frac{\pi}{2}$, the exact value is $\frac{\pi}{2} \approx 1.571$; three-term approximation gives $\frac{4}{3} \approx 1.333$.

![A10: Fourier partial sums for f(x)=x](../graphs/sol11b-a10-fourier.png)
