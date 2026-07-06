# 12A1 Solutions — Complex Numbers

---

## Practice 1

> $\frac{3-i}{2+i}$ in $a+bi$ form.

(1) Multiply numerator and denominator by the conjugate $2-i$:
$\frac{3-i}{2+i} \cdot \frac{2-i}{2-i} = \frac{(3-i)(2-i)}{(2+i)(2-i)}$.

(2) Numerator: $6 - 3i - 2i + i^2 = 6 - 5i - 1 = 5 - 5i$.

(3) Denominator: $4 - i^2 = 5$.

(4) $\frac{5-5i}{5} = 1 - i$. → **$z = 1 - i$.**

---

## Practice 2

> $z = 1-i$ in polar form. Then $z^8$ via De Moivre.

(1) $r = \sqrt{1^2 + (-1)^2} = \sqrt{2}$.
$\cos\theta = \frac{1}{\sqrt{2}}$, $\sin\theta = -\frac{1}{\sqrt{2}}$, so $\theta = -\frac{\pi}{4}$.

(2) $z = \sqrt{2}\,e^{-i\pi/4}$.

(3) $z^8 = (\sqrt{2})^8 e^{i\cdot8(-\pi/4)} = 16 \cdot e^{-i2\pi} = 16(1 + 0i) = 16$.
→ **$z^8 = 16$.**

---

## Practice 3

> Three cube roots of $-8$ in $a+bi$ form.

(1) $-8 = 8e^{i\pi}$.

(2) $z_k = 2 \cdot e^{i(\pi + 2\pi k)/3}$ for $k = 0,1,2$.

(3) $k=0$: $2e^{i\pi/3} = 1 + i\sqrt{3}$.
$k=1$: $2e^{i\pi} = -2$.
$k=2$: $2e^{i5\pi/3} = 1 - i\sqrt{3}$.
→ **$1 + i\sqrt{3},\; -2,\; 1 - i\sqrt{3}$.**

---

## Practice 4: Composition

> Why does multiplying by $i$ rotate by $90^\circ$? Find $i^3(3+4i)$ and describe.

(1) $i = 1 \cdot e^{i\pi/2}$. Multiplying by $i$ adds $\pi/2$ to the argument — a $90^\circ$ counterclockwise rotation, with no stretching ($|i| = 1$).

(2) $i^3 = -i = 1 \cdot e^{i3\pi/2}$ — this is a $270^\circ$ counterclockwise rotation (or $90^\circ$ clockwise).

(3) $i^3(3+4i) = -i(3+4i) = -3i - 4i^2 = -3i + 4 = 4 - 3i$.

(4) Geometric description: $(3,4)$ rotated $270^\circ$ counterclockwise lands at $(4,-3)$. The vector keeps its length ($\sqrt{9+16}=5$) but now points down-right instead of up-right.
→ **$4 - 3i$. Rotation by $270^\circ$ CCW (or $90^\circ$ CW).**

---

## Practice 5

> $z = -1 + i\sqrt{3}$ in polar form. Then $z^6$.

(1) $r = \sqrt{1 + 3} = 2$. $\cos\theta = -\frac{1}{2}$, $\sin\theta = \frac{\sqrt{3}}{2}$, so $\theta = \frac{2\pi}{3}$.

(2) $z = 2e^{i2\pi/3}$.

(3) $z^6 = 2^6 \cdot e^{i\cdot 6(2\pi/3)} = 64 \cdot e^{i4\pi} = 64(1 + 0i) = 64$.
→ **$z^6 = 64$.**

---

## Practice 6: Real Battle

> Cube roots of $-8$: triangle area. Rotation matrix for $120^\circ$.

(1) Roots: $P_1 = (1, \sqrt{3})$, $P_2 = (-2, 0)$, $P_3 = (1, -\sqrt{3})$.

(2) Vectors: $\vec{P_1P_2} = (-3, -\sqrt{3})$, $\vec{P_1P_3} = (0, -2\sqrt{3})$.

(3) 2D cross product magnitude: $|(-3)(-2\sqrt{3}) - (-\sqrt{3})(0)| = 6\sqrt{3}$. Area = $\frac{1}{2} \cdot 6\sqrt{3} = 3\sqrt{3}$.

(4) Rotation matrix for $120^\circ$: $R = \begin{pmatrix} -\frac{1}{2} & -\frac{\sqrt{3}}{2} \\ \frac{\sqrt{3}}{2} & -\frac{1}{2} \end{pmatrix}$. $R^3 = I$.
→ **Area = $3\sqrt{3}$.**

---

## Basic Drill

### D1. $i^{27}$
$27 = 4 \times 6 + 3$. $i^{27} = i^3 = -i$. → **$-i$.**

### D2. $(2-3i)(1+4i)$
$2 + 8i - 3i - 12i^2 = 2 + 5i + 12 = 14 + 5i$. → **$14 + 5i$.**

### D3. Conjugate and modulus of $z = 5 - 12i$
$\bar{z} = 5 + 12i$. $|z| = \sqrt{25+144} = 13$. → **$\bar{z} = 5+12i$, $|z| = 13$.**

### D4. $i^{4k+3}$
$i^{4k+3} = (i^4)^k \cdot i^3 = 1^k \cdot (-i) = -i$. → **$-i$.**

---

## Advanced Drill

### A1. $(1+i)z + 3 = 2i - z$
(1) $(1+i)z + z = 2i - 3$ → $(2+i)z = 2i - 3$.
(2) $z = \frac{2i-3}{2+i} \cdot \frac{2-i}{2-i} = \frac{-4+7i}{5}$.
→ **$z = -\frac{4}{5} + \frac{7}{5}i$.**

### A2. $(1+i\sqrt{3})^9$
(1) $r = 2$, $\theta = \pi/3$. $z = 2e^{i\pi/3}$.
(2) $z^9 = 2^9 e^{i9\pi/3} = 512 e^{i3\pi} = 512(-1) = -512$.
→ **$-512$.**

### A3. Four 4th roots of $-16$
(1) $-16 = 16e^{i\pi}$. $r^{1/4} = 2$.
(2) $z_k = 2e^{i(\pi + 2\pi k)/4}$ for $k = 0,1,2,3$.
$k=0$: $2e^{i\pi/4} = \sqrt{2} + i\sqrt{2}$.
$k=1$: $2e^{i3\pi/4} = -\sqrt{2} + i\sqrt{2}$.
$k=2$: $2e^{i5\pi/4} = -\sqrt{2} - i\sqrt{2}$.
$k=3$: $2e^{i7\pi/4} = \sqrt{2} - i\sqrt{2}$.
→ **$\sqrt{2}+i\sqrt{2},\; -\sqrt{2}+i\sqrt{2},\; -\sqrt{2}-i\sqrt{2},\; \sqrt{2}-i\sqrt{2}$.**

### A4. Area of square from 4th roots of 1
Roots: $(1,0), (0,1), (-1,0), (0,-1)$. Side length = $\sqrt{2}$. Area = $(\sqrt{2})^2 = 2$.
→ **2.**

---

[Back to Table of Contents](../12A1-complex-numbers.md)
