# 11B Solutions — Trigonometric Identities, Equations, and Beyond

---

## Basic Drill

### D1. $\sin 75^\circ = \sin(45^\circ+30^\circ)$
$\sin 45^\circ\cos 30^\circ + \cos 45^\circ\sin 30^\circ = \frac{\sqrt{2}}{2}\cdot\frac{\sqrt{3}}{2} + \frac{\sqrt{2}}{2}\cdot\frac{1}{2} = \frac{\sqrt{6}+\sqrt{2}}{4}$.
→ **$\frac{\sqrt{6}+\sqrt{2}}{4}$.**

### D2. $\cos 105^\circ = \cos(60^\circ+45^\circ)$
$\cos 60^\circ\cos 45^\circ - \sin 60^\circ\sin 45^\circ = \frac{1}{2}\cdot\frac{\sqrt{2}}{2} - \frac{\sqrt{3}}{2}\cdot\frac{\sqrt{2}}{2} = \frac{\sqrt{2}-\sqrt{6}}{4}$.
→ **$\frac{\sqrt{2}-\sqrt{6}}{4}$.**

### D3. $\tan 15^\circ = \tan(45^\circ-30^\circ)$
$\frac{\tan 45^\circ - \tan 30^\circ}{1 + \tan 45^\circ\tan 30^\circ} = \frac{1 - 1/\sqrt{3}}{1 + 1/\sqrt{3}} = 2-\sqrt{3}$.
→ **$2-\sqrt{3}$.**

### D4. $\sin(A+B)$ with $\sin A=\frac{3}{5}$ (Q1), $\cos B=\frac{5}{13}$ (Q1)
$\cos A = \frac{4}{5}$, $\sin B = \frac{12}{13}$.
$\sin(A+B) = \frac{3}{5}\cdot\frac{5}{13} + \frac{4}{5}\cdot\frac{12}{13} = \frac{15+48}{65} = \frac{63}{65}$.
→ **$\frac{63}{65}$.**

### D5. $\cos\theta = -\frac{4}{5}$ (Q2). $\cos 2\theta$.
$\cos 2\theta = 2\cos^2\theta - 1 = 2\cdot\frac{16}{25} - 1 = \frac{32}{25} - 1 = \frac{7}{25}$.
→ **$\frac{7}{25}$.** (Positive — $2\theta$ in Q3 or Q4.)

### D6. $\sin 3x \cdot \cos x$ as a sum
$\sin A\cos B = \frac{1}{2}[\sin(A+B) + \sin(A-B)]$. $A=3x$, $B=x$.
$= \frac{1}{2}[\sin 4x + \sin 2x]$.
→ **$\frac{1}{2}(\sin 4x + \sin 2x)$.**

### D7. $\sin 5x + \sin x$ as a product
$\sin A + \sin B = 2\sin\frac{A+B}{2}\cos\frac{A-B}{2}$. $A=5x$, $B=x$.
$= 2\sin 3x \cos 2x$.
→ **$2\sin 3x \cos 2x$.**

### D8. $\arcsin(\frac{\sqrt{3}}{2})$, $\arccos(-\frac{1}{2})$
$\arcsin\frac{\sqrt{3}}{2} = \frac{\pi}{3}$. $\arccos(-\frac{1}{2}) = \frac{2\pi}{3}$.
→ **$\frac{\pi}{3}$, $\frac{2\pi}{3}$.**

### D9. $\sin(\arcsin\frac{3}{5} + \arccos\frac{5}{13})$
Let $\alpha = \arcsin\frac{3}{5}$ → $\sin\alpha = \frac{3}{5}$, $\cos\alpha = \frac{4}{5}$ (Q1).
$\beta = \arccos\frac{5}{13}$ → $\cos\beta = \frac{5}{13}$, $\sin\beta = \frac{12}{13}$ (Q1).
$\sin(\alpha+\beta) = \frac{3}{5}\cdot\frac{5}{13} + \frac{4}{5}\cdot\frac{12}{13} = \frac{15+48}{65} = \frac{63}{65}$.
→ **$\frac{63}{65}$.**

### D10. Triangle $A=40^\circ$, $B=60^\circ$, $a=8$. Find $b$.
$b = a\frac{\sin B}{\sin A} = 8\cdot\frac{\sin 60^\circ}{\sin 40^\circ} = 8\cdot\frac{\sqrt{3}/2}{\sin 40^\circ} \approx 8\cdot\frac{0.8660}{0.6428} \approx 10.78$.
→ **$b \approx 10.78$.** Exact: $b = \frac{4\sqrt{3}}{\sin 40^\circ}$.

---

## Practice 1

> $\cos 2x = \sin x$ on $[0, 2\pi]$.

(1) $1 - 2\sin^2 x = \sin x$ → $2\sin^2 x + \sin x - 1 = 0$.
(2) $(2\sin x - 1)(\sin x + 1) = 0$.
(3) $\sin x = \frac{1}{2}$ → $x = \frac{\pi}{6}, \frac{5\pi}{6}$. $\sin x = -1$ → $x = \frac{3\pi}{2}$.
→ **$x = \frac{\pi}{6}, \frac{5\pi}{6}, \frac{3\pi}{2}$.**

---

## Practice 2: Composition

> $5\sin x + 12\cos x = R\sin(x+\phi)$. Max value and $x$.

(1) $R = \sqrt{25+144} = 13$. $\phi = \arcsin\frac{12}{13} \approx 67.38^\circ$.
(2) $5\sin x + 12\cos x = 13\sin(x + \phi)$.
(3) Max = 13 at $\sin(x+\phi)=1$ → $x = \frac{\pi}{2} - \phi + 2n\pi \approx 22.62^\circ + 360^\circ n$.

→ **$R=13$, max at $x \approx 22.6^\circ + 360^\circ n$.**

---

## Practice 3

> Triangle $a=7$, $b=10$, $c=13$. Angles and area.

$\cos A = \frac{100+169-49}{260} = \frac{11}{13}$, $A \approx 32.2^\circ$.
$\cos B = \frac{49+169-100}{182} = \frac{59}{91}$, $B \approx 49.5^\circ$.
$C = 180^\circ - 32.2^\circ - 49.5^\circ = 98.3^\circ$.

$s=15$, Area = $\sqrt{15\cdot8\cdot5\cdot2} = 20\sqrt{3} \approx 34.64$.

---

## Practice 4: Real Battle

> $\sec x + \tan x = 2$. Find $\sec x - \tan x$ and $\sin x$.

(1) $(\sec x + \tan x)(\sec x - \tan x) = \sec^2 x - \tan^2 x = 1$.
(2) $2(\sec x - \tan x) = 1$ → $\sec x - \tan x = \frac{1}{2}$.
(3) Add: $2\sec x = \frac{5}{2}$ → $\sec x = \frac{5}{4}$ → $\cos x = \frac{4}{5}$.
Subtract: $2\tan x = \frac{3}{2}$ → $\tan x = \frac{3}{4}$.
(4) $\sin x = \tan x \cdot \cos x = \frac{3}{4} \cdot \frac{4}{5} = \frac{3}{5}$.

→ **$\sec x - \tan x = \frac{1}{2}$, $\sin x = \frac{3}{5}$.**

---

## Practice 5

> $\sin 3x = \cos x$ on $[0, 2\pi]$.

(1) $\sin 3x = \sin(\frac{\pi}{2} - x)$.

Case 1: $3x = \frac{\pi}{2} - x + 2n\pi$ → $x = \frac{\pi}{8} + \frac{n\pi}{2}$. → $\frac{\pi}{8}, \frac{5\pi}{8}, \frac{9\pi}{8}, \frac{13\pi}{8}$.

Case 2: $3x = \pi - (\frac{\pi}{2} - x) + 2n\pi$ → $x = \frac{\pi}{4} + n\pi$. → $\frac{\pi}{4}, \frac{5\pi}{4}$.

→ **$x = \frac{\pi}{8}, \frac{\pi}{4}, \frac{5\pi}{8}, \frac{9\pi}{8}, \frac{5\pi}{4}, \frac{13\pi}{8}$.**

---

## Practice 6: Composition

> Derive $\sin 3\theta$, $\cos 3\theta$ from $e^{i3\theta} = (e^{i\theta})^3$.

$e^{i3\theta} = (\cos\theta + i\sin\theta)^3 = \cos^3\theta + 3i\cos^2\theta\sin\theta - 3\cos\theta\sin^2\theta - i\sin^3\theta$.

Real: $\cos 3\theta = \cos^3\theta - 3\cos\theta\sin^2\theta = 4\cos^3\theta - 3\cos\theta$.
Imag: $\sin 3\theta = 3\cos^2\theta\sin\theta - \sin^3\theta = 3\sin\theta - 4\sin^3\theta$.

---

## Practice 7

> $x^3 - 3x + 1 = 0$ via trig. $p=-3$, $q=1$.

$x = 2\cos\theta$. $8\cos^3\theta - 6\cos\theta + 1 = 0$ → $2\cos 3\theta + 1 = 0$ → $\cos 3\theta = -\frac{1}{2}$.

$3\theta = \frac{2\pi}{3} + 2n\pi$ or $\frac{4\pi}{3} + 2n\pi$.
Roots: $x = 2\cos\frac{2\pi}{9},\; 2\cos\frac{4\pi}{9},\; 2\cos\frac{8\pi}{9}$.

---

## Practice 8: Real Battle

> $\sin 3^\circ = \sin(18^\circ - 15^\circ)$.

$\sin 18^\circ = \frac{\sqrt{5}-1}{4}$, $\cos 18^\circ = \frac{\sqrt{10+2\sqrt{5}}}{4}$.
$\sin 15^\circ = \frac{\sqrt{6}-\sqrt{2}}{4}$, $\cos 15^\circ = \frac{\sqrt{6}+\sqrt{2}}{4}$.

$\sin 3^\circ = \sin 18^\circ\cos 15^\circ - \cos 18^\circ\sin 15^\circ$.
$= \frac{\sqrt{30} + \sqrt{10} - \sqrt{6} - \sqrt{2} - (\sqrt{6}-\sqrt{2})\sqrt{10+2\sqrt{5}}}{16}$.

---

## Advanced Drill

### A1. $\frac{\sin 2x}{1 + \cos 2x}$
$\sin 2x = 2\sin x\cos x$, $\cos 2x = 2\cos^2 x - 1$ → $1 + \cos 2x = 2\cos^2 x$.
$\frac{2\sin x\cos x}{2\cos^2 x} = \frac{\sin x}{\cos x} = \tan x$. → **$\tan x$.**

### A2. $\sin^4\theta - \cos^4\theta$
Factor: $(\sin^2\theta - \cos^2\theta)(\sin^2\theta + \cos^2\theta) = (\sin^2\theta - \cos^2\theta) \cdot 1$.
$\sin^2\theta - \cos^2\theta = -(\cos^2\theta - \sin^2\theta) = -\cos 2\theta$. → **$-\cos 2\theta$.**

### A3. $\frac{\sin 2x}{1 - \cos 2x} = \cot x$
$\sin 2x = 2\sin x\cos x$, $1 - \cos 2x = 1 - (1-2\sin^2 x) = 2\sin^2 x$.
$\frac{2\sin x\cos x}{2\sin^2 x} = \frac{\cos x}{\sin x} = \cot x$. Proved.

### A4. Triangle $ABC$, $a=8$, $b=6$, $\angle C = 60^\circ$.
$c^2 = 64+36-2\cdot8\cdot6\cdot\frac{1}{2} = 100-48 = 52$, $c = 2\sqrt{13}$.
Area = $\frac{1}{2}\cdot8\cdot6\cdot\frac{\sqrt{3}}{2} = 12\sqrt{3}$.
→ **$c = 2\sqrt{13}$, Area = $12\sqrt{3}$.**

### A5. $\frac{\cos 3\theta}{\cos\theta} + \frac{\sin 3\theta}{\sin\theta}$
$\cos 3\theta = 4\cos^3\theta - 3\cos\theta$ → $\frac{\cos 3\theta}{\cos\theta} = 4\cos^2\theta - 3$.
$\sin 3\theta = 3\sin\theta - 4\sin^3\theta$ → $\frac{\sin 3\theta}{\sin\theta} = 3 - 4\sin^2\theta$.
Sum: $(4\cos^2\theta - 3) + (3 - 4\sin^2\theta) = 4(\cos^2\theta - \sin^2\theta) = 4\cos 2\theta$.
→ **$4\cos 2\theta$.**

### A6. $\sin 15^\circ \cdot \cos 15^\circ \cdot \cos 30^\circ$
$\sin 15^\circ\cos 15^\circ = \frac{1}{2}\sin 30^\circ = \frac{1}{4}$.
$\cos 30^\circ = \frac{\sqrt{3}}{2}$. Product = $\frac{1}{4} \cdot \frac{\sqrt{3}}{2} = \frac{\sqrt{3}}{8}$.
→ **$\frac{\sqrt{3}}{8}$.**

### A7. $3\sin x + \sqrt{3}\cos x = R\sin(x+\phi)$
$R = \sqrt{3^2 + (\sqrt{3})^2} = \sqrt{9+3} = \sqrt{12} = 2\sqrt{3}$.
$\cos\phi = \frac{3}{2\sqrt{3}} = \frac{\sqrt{3}}{2}$, $\sin\phi = \frac{\sqrt{3}}{2\sqrt{3}} = \frac{1}{2}$. → $\phi = \frac{\pi}{6}$.
→ **$R = 2\sqrt{3}$, $\phi = \frac{\pi}{6}$.**  → $2\sqrt{3}\sin(x + \frac{\pi}{6})$.

### A8. $2\sin^2 x - 3\sin x + 1 = 0$, $x \in [0, 2\pi]$
$t = \sin x$: $2t^2 - 3t + 1 = 0$ → $(2t-1)(t-1) = 0$.
$t = \frac{1}{2}$: $\sin x = \frac{1}{2}$ → $x = \frac{\pi}{6}, \frac{5\pi}{6}$.
$t = 1$: $\sin x = 1$ → $x = \frac{\pi}{2}$.
→ **$x = \frac{\pi}{6}, \frac{\pi}{2}, \frac{5\pi}{6}$.**

### A9. $\tan\theta = \frac{3}{4}$, $\theta \in Q3$. $\sin 2\theta$, $\cos 2\theta$.
Q3: both $\sin\theta$ and $\cos\theta$ negative.
$\sin\theta = -\frac{3}{5}$, $\cos\theta = -\frac{4}{5}$ (3-4-5 triangle, both negated).
$\sin 2\theta = 2\sin\theta\cos\theta = 2(-\frac{3}{5})(-\frac{4}{5}) = \frac{24}{25}$.
$\cos 2\theta = \cos^2\theta - \sin^2\theta = \frac{16}{25} - \frac{9}{25} = \frac{7}{25}$.
→ **$\sin 2\theta = \frac{24}{25}$, $\cos 2\theta = \frac{7}{25}$.**

### A10. Triangle $a=7$, $b=8$, $c=9$. Largest angle and area.
Largest angle is opposite longest side $c=9$: $\angle C$.
$\cos C = \frac{a^2+b^2-c^2}{2ab} = \frac{49+64-81}{2\cdot7\cdot8} = \frac{32}{112} = \frac{2}{7}$. $C \approx 73.4^\circ$.
$s = \frac{7+8+9}{2} = 12$. Area = $\sqrt{12\cdot5\cdot4\cdot3} = \sqrt{720} = 12\sqrt{5} \approx 26.83$.
→ **$\angle C = \arccos\frac{2}{7} \approx 73.4^\circ$, Area = $12\sqrt{5}$.**

---

[Back to Table of Contents](../11B-trig-advanced.md)
