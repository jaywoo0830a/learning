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

### D5. $\frac{1}{i}$
Multiply by $\frac{-i}{-i}$: $\frac{1}{i} \cdot \frac{-i}{-i} = \frac{-i}{-i^2} = \frac{-i}{1} = -i$. → **$-i$.**

### D6. $(3+2i) + (5-7i) - (1+4i)$
$(3+5-1) + (2-7-4)i = 7 - 9i$. → **$7 - 9i$.**

### D7. Modulus of $z = -6 + 8i$
$|z| = \sqrt{36 + 64} = \sqrt{100} = 10$. → **10.**

### D8. $e^{i\pi/2}$ in $a+bi$ form
$\cos\frac{\pi}{2} + i\sin\frac{\pi}{2} = 0 + i$. → **$i$.**

### D9. $\bar{z}$ and $|z|$ for $z = -3i$
$\bar{z} = 3i$. $|z| = \sqrt{0+9} = 3$. → **$\bar{z}=3i$, $|z|=3$.**

### D10. $i^{15} + i^{16} + i^{17} + i^{18}$
$i^{15}=i^3=-i$, $i^{16}=1$, $i^{17}=i$, $i^{18}=-1$. Sum = $(-i)+1+i+(-1)=0$. → **0.**

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

### A5. $z = \sqrt{3} - i$ in polar form. Then $z^6$.
$r = \sqrt{3+1} = 2$. $\cos\theta = \frac{\sqrt{3}}{2}$, $\sin\theta = -\frac{1}{2}$, $\theta = -\frac{\pi}{6}$.
$z = 2e^{-i\pi/6}$. $z^6 = 2^6 e^{-i\pi} = 64(-1) = -64$. → **$-64$.**

### A6. $z^2 + 2z + 5 = 0$
$z = \frac{-2 \pm \sqrt{4-20}}{2} = \frac{-2 \pm \sqrt{-16}}{2} = \frac{-2 \pm 4i}{2} = -1 \pm 2i$.
→ **$z = -1 + 2i$, $z = -1 - 2i$.**

### A7. $z^3 = 8i$
$8i = 8e^{i\pi/2}$. $z_k = 2e^{i(\pi/2 + 2\pi k)/3}$, $k=0,1,2$.
$k=0$: $2e^{i\pi/6} = \sqrt{3} + i$. $k=1$: $2e^{i5\pi/6} = -\sqrt{3} + i$. $k=2$: $2e^{i3\pi/2} = -2i$.
→ **$\sqrt{3}+i$, $-\sqrt{3}+i$, $-2i$.**

### A8. $z = 2e^{i\pi/6}$. Find $z^4$ and $1/z$.
$z^4 = 2^4 e^{i4\pi/6} = 16 e^{i2\pi/3} = 16(-\frac{1}{2} + i\frac{\sqrt{3}}{2}) = -8 + 8i\sqrt{3}$.
$1/z = \frac{1}{2}e^{-i\pi/6} = \frac{1}{2}(\frac{\sqrt{3}}{2} - i\frac{1}{2}) = \frac{\sqrt{3}}{4} - \frac{1}{4}i$.
→ **$z^4 = -8 + 8\sqrt{3}i$, $1/z = \frac{\sqrt{3}}{4} - \frac{1}{4}i$.**

### A9. Prove $|z_1 z_2| = |z_1||z_2|$
Let $z_1 = a+bi$, $z_2 = c+di$. $z_1z_2 = (ac-bd) + (ad+bc)i$.
$|z_1z_2|^2 = (ac-bd)^2 + (ad+bc)^2 = a^2c^2 + b^2d^2 + a^2d^2 + b^2c^2$.
$|z_1|^2|z_2|^2 = (a^2+b^2)(c^2+d^2) = a^2c^2 + a^2d^2 + b^2c^2 + b^2d^2$. Equal. Proved.

### A10. Area of triangle from cube roots of $8i$
Roots from A7: $(\sqrt{3}, 1)$, $(-\sqrt{3}, 1)$, $(0, -2)$. Equilateral triangle, radius 2.
Side length = distance between $(\sqrt{3},1)$ and $(-\sqrt{3},1)$ = $2\sqrt{3}$.
Area = $\frac{\sqrt{3}}{4}(2\sqrt{3})^2 = \frac{\sqrt{3}}{4}\cdot 12 = 3\sqrt{3}$. → **$3\sqrt{3}$.**

---

[Back to Table of Contents](../12A1-complex-numbers.md)
