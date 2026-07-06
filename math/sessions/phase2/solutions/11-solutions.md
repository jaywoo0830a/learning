# 11 Solutions — Trigonometry

---

## Practice 1

> $\sin\theta = -\frac{\sqrt{3}}{2}$, $\theta$ in Q4. Find $\cos\theta$, $\tan\theta$, $\sec\theta$, $\csc\theta$, $\cot\theta$.

(1) $\theta$ in Q4 → $\cos\theta > 0$, $\sin\theta < 0$.

(2) $\sin^2\theta + \cos^2\theta = 1$:
$\frac{3}{4} + \cos^2\theta = 1$ → $\cos^2\theta = \frac{1}{4}$ → $\cos\theta = \frac{1}{2}$ (positive in Q4).

(3) $\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{-\sqrt{3}/2}{1/2} = -\sqrt{3}$.

(4) $\sec\theta = \frac{1}{\cos\theta} = 2$.

(5) $\csc\theta = \frac{1}{\sin\theta} = \frac{1}{-\sqrt{3}/2} = -\frac{2}{\sqrt{3}} = -\frac{2\sqrt{3}}{3}$.

(6) $\cot\theta = \frac{1}{\tan\theta} = -\frac{1}{\sqrt{3}} = -\frac{\sqrt{3}}{3}$.

→ **$\cos\theta = \frac{1}{2}$, $\tan\theta = -\sqrt{3}$, $\sec\theta = 2$, $\csc\theta = -\frac{2\sqrt{3}}{3}$, $\cot\theta = -\frac{\sqrt{3}}{3}$.**

---

## Practice 2

> $y = 2\sin(3x + \pi) - 1$. Amplitude, period, phase shift, vertical shift, max/min.

$a = 2$, $b = 3$, $c = \pi$, $d = -1$.

- Amplitude: $|a| = 2$.
- Period: $\frac{2\pi}{|b|} = \frac{2\pi}{3}$.
- Phase shift: $3x + \pi = 0$ → $x = -\frac{\pi}{3}$ (left by $\frac{\pi}{3}$).
- Vertical shift: $-1$ (down by 1).

Graph: start from $y = \sin x$.
Stretch vertically by 2, compress horizontally by factor $\frac{1}{3}$ (period $\frac{2\pi}{3}$),
shift left by $\frac{\pi}{3}$, shift down by 1.

Range: $[-1-2, -1+2] = [-3, 1]$.
Maximum: $1$ at $\sin(3x+\pi)=1$ → $3x+\pi = \frac{\pi}{2} + 2n\pi$ → $x = -\frac{\pi}{6} + \frac{2n\pi}{3}$.
Minimum: $-3$ at $\sin(3x+\pi)=-1$ → $3x+\pi = \frac{3\pi}{2} + 2n\pi$ → $x = \frac{\pi}{6} + \frac{2n\pi}{3}$.

---

## Practice 3

> Solve $\cos 2x = \sin x$ on $[0, 2\pi]$.

(1) $\cos 2x = 1 - 2\sin^2 x$: $1 - 2\sin^2 x = \sin x$.
(2) $2\sin^2 x + \sin x - 1 = 0$.
(3) $t = \sin x$: $2t^2 + t - 1 = 0$ → $(2t-1)(t+1) = 0$.
(4) $t = \frac{1}{2}$: $\sin x = \frac{1}{2}$ → $x = \frac{\pi}{6}, \frac{5\pi}{6}$.
(5) $t = -1$: $\sin x = -1$ → $x = \frac{3\pi}{2}$.

All three values are within $[0, 2\pi]$.

→ **$x = \frac{\pi}{6}, \frac{5\pi}{6}, \frac{3\pi}{2}$.**

---

## Practice 4: Composition

> Write $5\sin x + 12\cos x$ as $R\sin(x+\phi)$. Max value and the $x$ where it occurs.
> Give another example.

(1) $R = \sqrt{5^2 + 12^2} = \sqrt{25 + 144} = \sqrt{169} = 13$.
(2) $\cos\phi = \frac{5}{13}$, $\sin\phi = \frac{12}{13}$. $\phi = \arcsin\frac{12}{13} \approx 67.38^\circ \approx 1.176$ rad.
(3) $5\sin x + 12\cos x = 13\sin(x + \phi)$.

(4) Maximum: $13$. Occurs when $\sin(x+\phi) = 1$ → $x + \phi = \frac{\pi}{2} + 2n\pi$.
$x = \frac{\pi}{2} - \phi + 2n\pi \approx 22.62^\circ + 360^\circ n$.

(5) Another example — electrical engineering: combining two AC signals.
$V_1\sin(\omega t) + V_2\cos(\omega t) = \sqrt{V_1^2 + V_2^2} \sin(\omega t + \phi)$,
enabling phase analysis of a single combined sinusoid instead of two separate ones.

---

## Practice 5

> $a=7$, $b=10$, $c=13$. All three angles and area.

**Law of cosines for each angle**:

$\cos A = \frac{b^2 + c^2 - a^2}{2bc} = \frac{100 + 169 - 49}{2 \cdot 10 \cdot 13} = \frac{220}{260} = \frac{11}{13}$.
$A = \arccos\frac{11}{13} \approx 32.20^\circ$.

$\cos B = \frac{a^2 + c^2 - b^2}{2ac} = \frac{49 + 169 - 100}{2 \cdot 7 \cdot 13} = \frac{118}{182} = \frac{59}{91}$.
$B = \arccos\frac{59}{91} \approx 49.46^\circ$.

$C = 180^\circ - A - B \approx 180^\circ - 32.20^\circ - 49.46^\circ = 98.34^\circ$.

**Area (Heron)**:
$s = \frac{7 + 10 + 13}{2} = 15$.
Area = $\sqrt{15 \cdot (15-7) \cdot (15-10) \cdot (15-13)} = \sqrt{15 \cdot 8 \cdot 5 \cdot 2} = \sqrt{1200} = 20\sqrt{3} \approx 34.64$.

**Check with $\frac{1}{2}ab\sin C$**:
$\frac{1}{2} \cdot 7 \cdot 10 \cdot \sin 98.34^\circ \approx 35 \cdot 0.9897 \approx 34.64$. Matches.

→ **$A \approx 32.20^\circ$, $B \approx 49.46^\circ$, $C \approx 98.34^\circ$, Area $= 20\sqrt{3} \approx 34.64$.**

---

## Practice 6: Real Battle

> $\sec x + \tan x = 2$. Find $\sec x - \tan x$ and $\sin x$.

(1) Expand $(\sec x + \tan x)(\sec x - \tan x)$:
$= \sec^2 x - \tan^2 x = (1 + \tan^2 x) - \tan^2 x = 1$.

(2) Given $\sec x + \tan x = 2$: $2(\sec x - \tan x) = 1$ → $\sec x - \tan x = \frac{1}{2}$.

(3) Solve the linear system:
Add: $(\sec x + \tan x) + (\sec x - \tan x) = 2\sec x = 2 + \frac{1}{2} = \frac{5}{2}$ → $\sec x = \frac{5}{4}$.
Subtract: $(\sec x + \tan x) - (\sec x - \tan x) = 2\tan x = 2 - \frac{1}{2} = \frac{3}{2}$ → $\tan x = \frac{3}{4}$.

(4) From $\sec x = \frac{1}{\cos x}$: $\cos x = \frac{4}{5}$.
From $\tan x = \frac{\sin x}{\cos x}$: $\sin x = \tan x \cdot \cos x = \frac{3}{4} \cdot \frac{4}{5} = \frac{3}{5}$.

→ **$\sec x - \tan x = \frac{1}{2}$, $\sin x = \frac{3}{5}$.**

---

## Practice 7

> Solve $\sin 3x = \cos x$ on $[0, 2\pi]$.

Method: Use $\cos x = \sin(\frac{\pi}{2} - x)$.

(1) $\sin 3x = \sin(\frac{\pi}{2} - x)$.
(2) $\sin A = \sin B$ implies either:
$A = B + 2n\pi$ or $A = \pi - B + 2n\pi$.

(3) Case 1: $3x = \frac{\pi}{2} - x + 2n\pi$ → $4x = \frac{\pi}{2} + 2n\pi$ → $x = \frac{\pi}{8} + \frac{n\pi}{2}$.
In $[0, 2\pi]$: $n=0$: $\frac{\pi}{8}$. $n=1$: $\frac{5\pi}{8}$. $n=2$: $\frac{9\pi}{8}$. $n=3$: $\frac{13\pi}{8}$.
$n=4$ gives $\frac{17\pi}{8} > 2\pi$, stop.

(4) Case 2: $3x = \pi - (\frac{\pi}{2} - x) + 2n\pi$ → $3x = \frac{\pi}{2} + x + 2n\pi$ → $2x = \frac{\pi}{2} + 2n\pi$ → $x = \frac{\pi}{4} + n\pi$.
In $[0, 2\pi]$: $n=0$: $\frac{\pi}{4}$. $n=1$: $\frac{5\pi}{4}$.

(5) All solutions in $[0, 2\pi]$: $\frac{\pi}{8}, \frac{\pi}{4}, \frac{5\pi}{8}, \frac{9\pi}{8}, \frac{5\pi}{4}, \frac{13\pi}{8}$.

→ **$x = \frac{\pi}{8}, \frac{\pi}{4}, \frac{5\pi}{8}, \frac{9\pi}{8}, \frac{5\pi}{4}, \frac{13\pi}{8}$.**

---

## Practice 8

> Prove $\tan x + \sec x = \tan(\frac{x}{2} + \frac{\pi}{4})$ using the tangent half-angle substitution.

Let $t = \tan\frac{x}{2}$.

(1) $\tan x = \frac{2t}{1-t^2}$.
(2) $\sec x = \frac{1}{\cos x} = \frac{1+t^2}{1-t^2}$.

(3) Left side: $\tan x + \sec x = \frac{2t}{1-t^2} + \frac{1+t^2}{1-t^2} = \frac{2t + 1 + t^2}{1-t^2} = \frac{(t+1)^2}{(1-t)(1+t)} = \frac{t+1}{1-t}$.

(4) Right side: $\tan(\frac{x}{2} + \frac{\pi}{4}) = \frac{\tan\frac{x}{2} + \tan\frac{\pi}{4}}{1 - \tan\frac{x}{2}\tan\frac{\pi}{4}} = \frac{t + 1}{1 - t \cdot 1} = \frac{t+1}{1-t}$.

(5) Left side = Right side. Proved.

Equivalently: $\tan x + \sec x = \tan(\frac{x}{2} + \frac{\pi}{4})$.

This identity is useful because the right side is often easier to integrate or manipulate.

---

## Practice 9: Composition

> Using Euler's formula $e^{i\theta} = \cos\theta + i\sin\theta$, derive $\sin 3\theta$ and $\cos 3\theta$ algebraically.

(1) $e^{i3\theta} = (e^{i\theta})^3 = (\cos\theta + i\sin\theta)^3$.

(2) Expand using the binomial theorem:
$(\cos\theta + i\sin\theta)^3 = \cos^3\theta + 3i\cos^2\theta\sin\theta + 3i^2\cos\theta\sin^2\theta + i^3\sin^3\theta$.

(3) Simplify powers of $i$: $i^2 = -1$, $i^3 = -i$.
$= \cos^3\theta + 3i\cos^2\theta\sin\theta - 3\cos\theta\sin^2\theta - i\sin^3\theta$.

(4) Group real and imaginary parts:
Real: $\cos^3\theta - 3\cos\theta\sin^2\theta$.
Imaginary: $3\cos^2\theta\sin\theta - \sin^3\theta$.

(5) On the other hand, $e^{i3\theta} = \cos 3\theta + i\sin 3\theta$ by Euler's formula.
Equating:
$\cos 3\theta = \cos^3\theta - 3\cos\theta\sin^2\theta$.
$\sin 3\theta = 3\cos^2\theta\sin\theta - \sin^3\theta$.

(6) Convert to standard forms using $\sin^2\theta = 1 - \cos^2\theta$ and $\cos^2\theta = 1 - \sin^2\theta$:
$\cos 3\theta = \cos^3\theta - 3\cos\theta(1-\cos^2\theta) = 4\cos^3\theta - 3\cos\theta$.
$\sin 3\theta = 3(1-\sin^2\theta)\sin\theta - \sin^3\theta = 3\sin\theta - 4\sin^3\theta$.

These match the standard triple-angle formulas perfectly. Euler's formula yields them in one clean step.

---

## Practice 10

> Solve $x^3 - 3x + 1 = 0$ using the trigonometric method.

The cubic is in the form $x^3 + px + q = 0$ with $p = -3$, $q = 1$.

(1) Check the discriminant: $4p^3 + 27q^2 = 4(-27) + 27(1) = -108 + 27 = -81 < 0$.
Three real roots → use the trigonometric method.

(2) Set $x = 2\sqrt{-\frac{p}{3}} \cos\theta = 2\sqrt{1}\cos\theta = 2\cos\theta$.

(3) Substitute into $x^3 - 3x + 1 = 0$:
$(2\cos\theta)^3 - 3(2\cos\theta) + 1 = 0$ → $8\cos^3\theta - 6\cos\theta + 1 = 0$.

(4) Recall $4\cos^3\theta - 3\cos\theta = \cos 3\theta$.
Multiply the equation by 2: $2(8\cos^3\theta - 6\cos\theta + 1) = 0$ → wait, let's use:
$8\cos^3\theta - 6\cos\theta = 2(4\cos^3\theta - 3\cos\theta) = 2\cos 3\theta$.
So $2\cos 3\theta + 1 = 0$ → $\cos 3\theta = -\frac{1}{2}$.

(5) $\cos 3\theta = -\frac{1}{2}$ → $3\theta = \frac{2\pi}{3} + 2n\pi$ or $3\theta = \frac{4\pi}{3} + 2n\pi$.
$\theta = \frac{2\pi}{9} + \frac{2n\pi}{3}$ or $\theta = \frac{4\pi}{9} + \frac{2n\pi}{3}$.

(6) Choose three distinct values for $\theta$ in $[0, \pi]$ (since $\cos$ is even and $x = 2\cos\theta$ uses only the cosine):
$n=0$ from the first set: $\theta = \frac{2\pi}{9} = 40^\circ$. $x_1 = 2\cos 40^\circ$.
$n=1$ from the first set: $\theta = \frac{2\pi}{9} + \frac{2\pi}{3} = \frac{8\pi}{9} = 160^\circ$. $x_2 = 2\cos 160^\circ$.
$n=0$ from the second set: $\theta = \frac{4\pi}{9} = 80^\circ$. $x_3 = 2\cos 80^\circ$.

(7) Check: $2\cos 160^\circ = 2\cos(180^\circ - 20^\circ) = -2\cos 20^\circ$.
But wait — let's verify $\frac{2\pi}{9} = 40^\circ$, $\frac{4\pi}{9} = 80^\circ$, $\frac{8\pi}{9} = 160^\circ$.
These give $2\cos 40^\circ \approx 1.532$, $2\cos 80^\circ \approx 0.347$, $2\cos 160^\circ \approx -1.879$.
Sum ≈ 0 (should be 0 for depressed cubic). The three roots sum to 0. Correct.

→ **$x = 2\cos\frac{2\pi}{9}, \; 2\cos\frac{4\pi}{9}, \; 2\cos\frac{8\pi}{9}$.**

---

## Practice 11

> Prove $\cos\frac{\pi}{7} \cos\frac{2\pi}{7} \cos\frac{3\pi}{7} = \frac{1}{8}$.

(1) Let $P = \cos\frac{\pi}{7} \cos\frac{2\pi}{7} \cos\frac{3\pi}{7}$.

(2) Multiply and divide by $\sin\frac{\pi}{7}$:
$P = \frac{\sin\frac{\pi}{7} \cos\frac{\pi}{7} \cos\frac{2\pi}{7} \cos\frac{3\pi}{7}}{\sin\frac{\pi}{7}}$.

(3) $\sin\frac{\pi}{7} \cos\frac{\pi}{7} = \frac{1}{2}\sin\frac{2\pi}{7}$.
$P = \frac{\frac{1}{2}\sin\frac{2\pi}{7} \cos\frac{2\pi}{7} \cos\frac{3\pi}{7}}{\sin\frac{\pi}{7}}$.

(4) $\sin\frac{2\pi}{7} \cos\frac{2\pi}{7} = \frac{1}{2}\sin\frac{4\pi}{7}$.
$P = \frac{\frac{1}{4}\sin\frac{4\pi}{7} \cos\frac{3\pi}{7}}{\sin\frac{\pi}{7}}$.

(5) Use $\sin\frac{4\pi}{7} \cos\frac{3\pi}{7} = \frac{1}{2}[\sin(\frac{4\pi}{7}+\frac{3\pi}{7}) + \sin(\frac{4\pi}{7}-\frac{3\pi}{7})] = \frac{1}{2}[\sin\pi + \sin\frac{\pi}{7}]$.
Since $\sin\pi = 0$: $= \frac{1}{2}\sin\frac{\pi}{7}$.

(6) $P = \frac{\frac{1}{4} \cdot \frac{1}{2}\sin\frac{\pi}{7}}{\sin\frac{\pi}{7}} = \frac{\frac{1}{8}\sin\frac{\pi}{7}}{\sin\frac{\pi}{7}} = \frac{1}{8}$.

→ **Proved: $\cos\frac{\pi}{7} \cos\frac{2\pi}{7} \cos\frac{3\pi}{7} = \frac{1}{8}$.**

---

## Practice 12: Real Battle

> Find the exact value of $\sin 3^\circ$ as a radical expression.

Approach: $\sin 3^\circ = \sin(18^\circ - 15^\circ)$.

**Step 1: Known exact values**.
$\sin 18^\circ = \frac{\sqrt{5}-1}{4}$ (from the regular pentagon / golden ratio).
$\cos 18^\circ = \sqrt{1 - \sin^2 18^\circ} = \sqrt{1 - \frac{6-2\sqrt{5}}{16}} = \sqrt{\frac{10+2\sqrt{5}}{16}} = \frac{\sqrt{10+2\sqrt{5}}}{4}$.

$\sin 15^\circ = \frac{\sqrt{6}-\sqrt{2}}{4}$ (from $\sin(45^\circ-30^\circ)$).
$\cos 15^\circ = \frac{\sqrt{6}+\sqrt{2}}{4}$.

**Step 2: Apply the difference formula**.
$\sin 3^\circ = \sin(18^\circ - 15^\circ) = \sin 18^\circ \cos 15^\circ - \cos 18^\circ \sin 15^\circ$.

(1) $\sin 18^\circ \cos 15^\circ = \frac{\sqrt{5}-1}{4} \cdot \frac{\sqrt{6}+\sqrt{2}}{4} = \frac{(\sqrt{5}-1)(\sqrt{6}+\sqrt{2})}{16}$.

Numerator: $(\sqrt{5}-1)(\sqrt{6}+\sqrt{2}) = \sqrt{5}\sqrt{6} + \sqrt{5}\sqrt{2} - \sqrt{6} - \sqrt{2} = \sqrt{30} + \sqrt{10} - \sqrt{6} - \sqrt{2}$.

(2) $\cos 18^\circ \sin 15^\circ = \frac{\sqrt{10+2\sqrt{5}}}{4} \cdot \frac{\sqrt{6}-\sqrt{2}}{4} = \frac{\sqrt{10+2\sqrt{5}} \cdot (\sqrt{6}-\sqrt{2})}{16}$.

(3) $\sin 3^\circ = \frac{(\sqrt{30} + \sqrt{10} - \sqrt{6} - \sqrt{2}) - \sqrt{10+2\sqrt{5}} \cdot (\sqrt{6}-\sqrt{2})}{16}$.

**Step 3: Simplify the nested radical term**.
This is the compact radical form. Further simplification requires manipulating the nested radical. The expression $\sqrt{10+2\sqrt{5}}$ can be denested, but the result is not elementary-simpler.

→ **$\sin 3^\circ = \frac{\sqrt{30} + \sqrt{10} - \sqrt{6} - \sqrt{2} - (\sqrt{6}-\sqrt{2})\sqrt{10+2\sqrt{5}}}{16}$.**

This is an exact closed-form radical expression — a result that is rarely seen even in advanced courses. Every integer degree from 3° upward has such an explicit radical form, derivable by chaining the 15°, 18°, and 36° values with sum/difference and half-angle formulas.

---

## Basic Drill

### D1. Convert to radians: $150^\circ$, $225^\circ$, $330^\circ$
$150^\circ \times \frac{\pi}{180^\circ} = \frac{5\pi}{6}$.
$225^\circ \times \frac{\pi}{180^\circ} = \frac{5\pi}{4}$.
$330^\circ \times \frac{\pi}{180^\circ} = \frac{11\pi}{6}$.
→ **$\frac{5\pi}{6}, \frac{5\pi}{4}, \frac{11\pi}{6}$.**

### D2. Evaluate: $\sin\frac{5\pi}{6}$, $\cos\frac{7\pi}{4}$, $\tan\frac{4\pi}{3}$
$\sin\frac{5\pi}{6} = \sin(150^\circ) = \sin(180^\circ-30^\circ) = \sin 30^\circ = \frac{1}{2}$.
$\cos\frac{7\pi}{4} = \cos(315^\circ) = \cos(360^\circ-45^\circ) = \cos 45^\circ = \frac{\sqrt{2}}{2}$.
$\tan\frac{4\pi}{3} = \tan(240^\circ) = \tan(180^\circ+60^\circ) = \tan 60^\circ = \sqrt{3}$.
→ **$\frac{1}{2}, \frac{\sqrt{2}}{2}, \sqrt{3}$.**

### D3. $\sin\theta = \frac{5}{13}$, $\theta$ in Q2. Find $\cos\theta$, $\tan\theta$
(1) Q2: $\cos\theta < 0$, $\sin\theta > 0$.
(2) $\cos^2\theta = 1 - \sin^2\theta = 1 - \frac{25}{169} = \frac{144}{169}$.
$\cos\theta = -\frac{12}{13}$ (negative in Q2).
(3) $\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{5/13}{-12/13} = -\frac{5}{12}$.
→ **$\cos\theta = -\frac{12}{13}$, $\tan\theta = -\frac{5}{12}$.**

### D4. $\frac{\sin x}{\csc x} + \frac{\cos x}{\sec x}$
(1) $\csc x = \frac{1}{\sin x}$, so $\frac{\sin x}{\csc x} = \sin x \cdot \sin x = \sin^2 x$.
(2) $\sec x = \frac{1}{\cos x}$, so $\frac{\cos x}{\sec x} = \cos x \cdot \cos x = \cos^2 x$.
(3) Sum: $\sin^2 x + \cos^2 x = 1$. → **1.**

### D5. $\sin^2 15^\circ + \sin^2 75^\circ$
(1) $\sin 75^\circ = \sin(90^\circ-15^\circ) = \cos 15^\circ$.
(2) $\sin^2 15^\circ + \cos^2 15^\circ = 1$. → **1.**

### D6. Period and amplitude of $y = -4\cos(\frac{\pi}{2}x) + 3$
$a = -4$, $b = \frac{\pi}{2}$, $d = 3$.
Amplitude: $|a| = 4$.
Period: $\frac{2\pi}{|b|} = \frac{2\pi}{\pi/2} = 4$.
→ **Amplitude = 4, Period = 4.**

### D7. $\sin\theta = \frac{4}{5}$, $\theta \in Q1$. Find $\sin 2\theta$, $\cos 2\theta$.
(1) Q1: both $\sin\theta$ and $\cos\theta$ positive.
(2) $\cos\theta = \sqrt{1 - \sin^2\theta} = \sqrt{1 - \frac{16}{25}} = \sqrt{\frac{9}{25}} = \frac{3}{5}$.
(3) $\sin 2\theta = 2\sin\theta\cos\theta = 2 \cdot \frac{4}{5} \cdot \frac{3}{5} = \frac{24}{25}$.
(4) $\cos 2\theta = 1 - 2\sin^2\theta = 1 - 2 \cdot \frac{16}{25} = 1 - \frac{32}{25} = -\frac{7}{25}$.
→ **$\sin 2\theta = \frac{24}{25}$, $\cos 2\theta = -\frac{7}{25}$.**

### D8. $\sin\frac{2\pi}{3} \cdot \cos\frac{\pi}{6} + \cos\frac{2\pi}{3} \cdot \sin\frac{\pi}{6}$
(1) This matches the pattern $\sin A\cos B + \cos A\sin B = \sin(A+B)$.
(2) $A = \frac{2\pi}{3}$, $B = \frac{\pi}{6}$.
(3) $\sin(\frac{2\pi}{3} + \frac{\pi}{6}) = \sin(\frac{4\pi}{6} + \frac{\pi}{6}) = \sin\frac{5\pi}{6} = \frac{1}{2}$.
→ **$\frac{1}{2}$.**

---

## Advanced Drill

### A1. $\frac{\sin 2x}{1 + \cos 2x}$
(1) $\sin 2x = 2\sin x\cos x$.
(2) $\cos 2x = 2\cos^2 x - 1$ → $1 + \cos 2x = 2\cos^2 x$.
(3) $\frac{2\sin x\cos x}{2\cos^2 x} = \frac{\sin x}{\cos x} = \tan x$. → **$\tan x$.**

### A2. $\sin 15^\circ \cdot \cos 15^\circ \cdot \cos 30^\circ$
(1) $\sin 15^\circ \cos 15^\circ = \frac{1}{2}\sin 30^\circ = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$.
(2) $\cos 30^\circ = \frac{\sqrt{3}}{2}$.
(3) $\frac{1}{4} \cdot \frac{\sqrt{3}}{2} = \frac{\sqrt{3}}{8}$. → **$\frac{\sqrt{3}}{8}$.**

### A3. $\sin^4\theta - \cos^4\theta$ in terms of $\cos 2\theta$
(1) Factor as $(\sin^2\theta - \cos^2\theta)(\sin^2\theta + \cos^2\theta) = (\sin^2\theta - \cos^2\theta) \cdot 1$.
(2) $\sin^2\theta - \cos^2\theta = -(\cos^2\theta - \sin^2\theta) = -\cos 2\theta$.
→ **$-\cos 2\theta$.**

### A4. $\sin x + \sin 2x + \sin 3x = 0$, $x \in [0, 2\pi]$
(1) Sum-to-product on $\sin x + \sin 3x$:
$\sin x + \sin 3x = 2\sin\frac{x+3x}{2}\cos\frac{x-3x}{2} = 2\sin 2x\cos x$.
(2) Equation: $2\sin 2x\cos x + \sin 2x = 0$ → $\sin 2x(2\cos x + 1) = 0$.
(3) $\sin 2x = 0$: $2x = n\pi$ → $x = \frac{n\pi}{2}$.
In $[0,2\pi]$: $x = 0, \frac{\pi}{2}, \pi, \frac{3\pi}{2}, 2\pi$.
(4) $2\cos x + 1 = 0$: $\cos x = -\frac{1}{2}$ → $x = \frac{2\pi}{3}, \frac{4\pi}{3}$.
(5) All solutions: $0, \frac{\pi}{2}, \frac{2\pi}{3}, \pi, \frac{4\pi}{3}, \frac{3\pi}{2}, 2\pi$.
→ **$x = 0, \frac{\pi}{2}, \frac{2\pi}{3}, \pi, \frac{4\pi}{3}, \frac{3\pi}{2}, 2\pi$.**

### A5. $\tan\theta = \frac{3}{4}$, $\theta \in Q3$. Find $\sin 2\theta$, $\cos 2\theta$
(1) Q3: both $\sin\theta$ and $\cos\theta$ are negative.
(2) $\tan\theta = \frac{3}{4}$ → opposite = 3, adjacent = 4 (both negated in Q3). Hypotenuse = 5.
$\sin\theta = -\frac{3}{5}$, $\cos\theta = -\frac{4}{5}$.
(3) $\sin 2\theta = 2\sin\theta\cos\theta = 2(-\frac{3}{5})(-\frac{4}{5}) = \frac{24}{25}$.
(4) $\cos 2\theta = \cos^2\theta - \sin^2\theta = \frac{16}{25} - \frac{9}{25} = \frac{7}{25}$.
→ **$\sin 2\theta = \frac{24}{25}$, $\cos 2\theta = \frac{7}{25}$.**

### A6. $\frac{\cos 3\theta}{\cos\theta} + \frac{\sin 3\theta}{\sin\theta}$
(1) $\cos 3\theta = 4\cos^3\theta - 3\cos\theta$, $\sin 3\theta = 3\sin\theta - 4\sin^3\theta$.
(2) $\frac{4\cos^3\theta - 3\cos\theta}{\cos\theta} = 4\cos^2\theta - 3$.
(3) $\frac{3\sin\theta - 4\sin^3\theta}{\sin\theta} = 3 - 4\sin^2\theta$.
(4) Sum: $(4\cos^2\theta - 3) + (3 - 4\sin^2\theta) = 4(\cos^2\theta - \sin^2\theta) = 4\cos 2\theta$.
→ **$4\cos 2\theta$.**

### A7. Prove $\frac{\sin 2x}{1 - \cos 2x} = \cot x$
(1) Left numerator: $\sin 2x = 2\sin x\cos x$.
(2) Left denominator: $1 - \cos 2x = 1 - (1 - 2\sin^2 x) = 2\sin^2 x$.
(3) Left side: $\frac{2\sin x\cos x}{2\sin^2 x} = \frac{\cos x}{\sin x} = \cot x$.
(4) Right side: $\cot x$. Left = Right. Proved.

### A8. Triangle $ABC$, $a=8$, $b=6$, $\angle C = 60^\circ$. Find $c$, area, $\angle A$.
(1) Law of cosines for $c$: $c^2 = a^2 + b^2 - 2ab\cos C = 64 + 36 - 2\cdot8\cdot6\cdot\frac{1}{2} = 100 - 48 = 52$.
$c = \sqrt{52} = 2\sqrt{13}$.
(2) Area: $\frac{1}{2}ab\sin C = \frac{1}{2} \cdot 8 \cdot 6 \cdot \frac{\sqrt{3}}{2} = 12\sqrt{3}$.
(3) Law of sines for $\angle A$: $\frac{a}{\sin A} = \frac{c}{\sin C}$ → $\sin A = \frac{a\sin C}{c} = \frac{8 \cdot \frac{\sqrt{3}}{2}}{2\sqrt{13}} = \frac{4\sqrt{3}}{2\sqrt{13}} = \frac{2\sqrt{3}}{\sqrt{13}} = \frac{2\sqrt{39}}{13}$.
$A = \arcsin\frac{2\sqrt{39}}{13} \approx 73.90^\circ$.
→ **$c = 2\sqrt{13}$, Area $= 12\sqrt{3}$, $A = \arcsin\frac{2\sqrt{39}}{13} \approx 73.9^\circ$.**

---

[Back to Table of Contents](../11-trigonometry.md)
