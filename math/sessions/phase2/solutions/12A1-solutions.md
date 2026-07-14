# Solutions — 12A1: Complex Numbers

---

## Practice 1

**Divide $\frac{3-i}{2+i}$.**

Multiply numerator and denominator by the conjugate of $2+i$, which is $2-i$:

$$\frac{3-i}{2+i} \cdot \frac{2-i}{2-i} = \frac{(3-i)(2-i)}{(2+i)(2-i)}$$

Numerator: $(3)(2) + (3)(-i) + (-i)(2) + (-i)(-i) = 6 - 3i - 2i + i^2 = 6 - 5i - 1 = 5 - 5i$.

Denominator: $(2)^2 + (1)^2 = 4 + 1 = 5$.

$$\frac{5-5i}{5} = 1 - i$$

> **Answer**: $1 - i$

---

## Practice 2

**Write $z = 1-i$ in polar form. Then compute $z^8$ using De Moivre.**

**Polar form**: $r = \sqrt{1^2 + (-1)^2} = \sqrt{2}$.

$\cos\theta = \frac{1}{\sqrt{2}}$, $\sin\theta = \frac{-1}{\sqrt{2}}$, so $\theta = -\frac{\pi}{4}$ (or $\frac{7\pi}{4}$).

$$z = \sqrt{2}\,e^{-i\pi/4}$$

**De Moivre**: $z^8 = (\sqrt{2})^8 \cdot e^{-i\cdot 8\pi/4} = 2^4 \cdot e^{-i\cdot 2\pi} = 16 \cdot e^{-i\cdot 2\pi}$.

Since $e^{-i\cdot 2\pi} = \cos(-2\pi) + i\sin(-2\pi) = 1$,

$$z^8 = 16$$

> **Answer**: $z = \sqrt{2}\,e^{-i\pi/4}$, $z^8 = 16$

---

## Practice 3

**Find all three cube roots of $-8$. Give each in $a+bi$ form.**

$-8 = 8e^{i\pi}$ (modulus 8, angle $\pi$).

Cube roots: $z_k = 8^{1/3} \cdot e^{i(\pi + 2\pi k)/3} = 2 \cdot e^{i(\pi + 2\pi k)/3}$ for $k = 0, 1, 2$.

- $k=0$: $2e^{i\pi/3} = 2(\cos\frac{\pi}{3} + i\sin\frac{\pi}{3}) = 2(\frac{1}{2} + i\frac{\sqrt{3}}{2}) = 1 + i\sqrt{3}$
- $k=1$: $2e^{i\pi} = 2(\cos\pi + i\sin\pi) = 2(-1 + 0) = -2$
- $k=2$: $2e^{i\cdot 5\pi/3} = 2(\cos\frac{5\pi}{3} + i\sin\frac{5\pi}{3}) = 2(\frac{1}{2} - i\frac{\sqrt{3}}{2}) = 1 - i\sqrt{3}$

Check: $(1+i\sqrt{3})^3 = 1^3 + 3\cdot1^2(i\sqrt{3}) + 3\cdot1(i\sqrt{3})^2 + (i\sqrt{3})^3 = 1 + 3i\sqrt{3} - 9 - 3i\sqrt{3} = -8$ ✓.
$(-2)^3 = -8$ ✓.

> **Answer**: $1 + i\sqrt{3},\; -2,\; 1 - i\sqrt{3}$

---

## Practice 4: Composition

**Explain why multiplying by $i$ rotates by $90^\circ$, then multiply $3+4i$ by $i^3$ and describe geometrically.**

$i = 0 + 1i = 1 \cdot e^{i\pi/2}$ — modulus 1, angle $\pi/2 = 90^\circ$. Multiplying by $i$ adds $\pi/2$ to the argument: the point rotates $90^\circ$ CCW without changing its distance from the origin.

$i^3 = i^2 \cdot i = (-1) \cdot i = -i = e^{-i\pi/2}$ (or $e^{i\cdot 3\pi/2}$).

$(3+4i) \cdot i^3 = (3+4i)(-i) = -3i - 4i^2 = -3i + 4 = 4 - 3i$.

Geometric interpretation: Multiplying by $i^3 = -i$ rotates the point $90^\circ$ **clockwise** (or $270^\circ$ CCW). The point $(3,4)$ rotates to $(4,-3)$. Modulus preserved: $|3+4i| = 5$, $|4-3i| = \sqrt{16+9} = 5$ ✓.

> **Answer**: $4 - 3i$; rotation by $90^\circ$ clockwise ($270^\circ$ CCW)

---

## Practice 5

**Write $z = -1 + i\sqrt{3}$ in polar form $re^{i\theta}$. Then find $z^6$.**

$r = \sqrt{(-1)^2 + (\sqrt{3})^2} = \sqrt{1+3} = 2$.

$\cos\theta = -\frac{1}{2}$, $\sin\theta = \frac{\sqrt{3}}{2}$, so $\theta = \frac{2\pi}{3}$ (Quadrant II).

Polar form: $z = 2e^{i\cdot 2\pi/3}$.

$z^6 = 2^6 \cdot e^{i\cdot 6 \cdot 2\pi/3} = 64 \cdot e^{i\cdot 4\pi} = 64(\cos 4\pi + i\sin 4\pi) = 64(1 + 0) = 64$.

> **Answer**: $z = 2e^{i\cdot 2\pi/3}$, $z^6 = 64$

---

## Practice 6: Real Battle

**The three cube roots of $-8$ form a triangle. Find its area. Also find a $2\times 2$ rotation matrix for $120^\circ$ and verify $R^3 = I$.**

From Practice 3, the roots are $z_0 = 1+i\sqrt{3}$, $z_1 = -2$, $z_2 = 1-i\sqrt{3}$. These lie on a circle of radius 2, equally spaced by $120^\circ$.

**Area**: The three points form an equilateral triangle inscribed in a circle of radius $r=2$. Area = $\frac{3\sqrt{3}}{4}r^2 = \frac{3\sqrt{3}}{4} \cdot 4 = 3\sqrt{3}$.

Alternatively using coordinates $(1,\sqrt{3})$, $(-2,0)$, $(1,-\sqrt{3})$:
$\text{Area} = \frac{1}{2}|x_1(y_2-y_3) + x_2(y_3-y_1) + x_3(y_1-y_2)|$
$= \frac{1}{2}|1(0-(-\sqrt{3})) + (-2)(-\sqrt{3}-\sqrt{3}) + 1(\sqrt{3}-0)|$
$= \frac{1}{2}|\sqrt{3} + 4\sqrt{3} + \sqrt{3}| = \frac{1}{2} \cdot 6\sqrt{3} = 3\sqrt{3}$.

**Rotation matrix for $120^\circ$ CCW**:
$R = \begin{pmatrix} \cos 120^\circ & -\sin 120^\circ \\ \sin 120^\circ & \cos 120^\circ \end{pmatrix} = \begin{pmatrix} -\frac{1}{2} & -\frac{\sqrt{3}}{2} \\ \frac{\sqrt{3}}{2} & -\frac{1}{2} \end{pmatrix}$.

Verify $R^3 = I$: Rotating by $120^\circ$ three times = $360^\circ$ = identity. Algebraically:
$R^2 = \begin{pmatrix} -\frac{1}{2} & \frac{\sqrt{3}}{2} \\ -\frac{\sqrt{3}}{2} & -\frac{1}{2} \end{pmatrix}$ (rotation by $240^\circ$).
$R^3 = R^2 \cdot R = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I$. ✓

> **Answer**: Area $= 3\sqrt{3}$, $R = \begin{pmatrix} -1/2 & -\sqrt{3}/2 \\ \sqrt{3}/2 & -1/2 \end{pmatrix}$

---

## Basic Drill

### D1. Simplify $i^{27}$

$27 \div 4 = 6$ remainder $3$. So $i^{27} = i^3 = -i$.

> **Answer**: $-i$

---

### D2. Compute $(2-3i)(1+4i)$

$(2-3i)(1+4i) = 2(1) + 2(4i) + (-3i)(1) + (-3i)(4i) = 2 + 8i - 3i - 12i^2 = 2 + 5i + 12 = 14 + 5i$.

> **Answer**: $14 + 5i$

---

### D3. Conjugate and modulus of $z = 5 - 12i$

$\bar{z} = 5 + 12i$.
$|z| = \sqrt{5^2 + (-12)^2} = \sqrt{25 + 144} = \sqrt{169} = 13$.

> **Answer**: $\bar{z} = 5+12i$, $|z| = 13$

---

### D4. Find $i^{4k+3}$ for any integer $k$

$i^{4k+3} = (i^4)^k \cdot i^3 = 1^k \cdot (-i) = -i$.

> **Answer**: $-i$

---

### D5. Simplify $\frac{1}{i}$

$\frac{1}{i} \cdot \frac{-i}{-i} = \frac{-i}{-i^2} = \frac{-i}{1} = -i$.
Alternatively: $\frac{1}{i} = i^{-1} = i^3 = -i$ (since $i^4 = 1$, $i^{-1} = i^3$).

> **Answer**: $-i$ (or $0 - i$)

---

### D6. Compute $(3+2i) + (5-7i) - (1+4i)$

Reals: $3 + 5 - 1 = 7$.
Imaginary: $2i - 7i - 4i = -9i$.

> **Answer**: $7 - 9i$

---

### D7. Find the modulus of $z = -6 + 8i$

$|z| = \sqrt{(-6)^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10$.

> **Answer**: $10$

---

### D8. Write $e^{i\pi/2}$ in $a+bi$ form

$e^{i\pi/2} = \cos\frac{\pi}{2} + i\sin\frac{\pi}{2} = 0 + i \cdot 1 = i$.

> **Answer**: $i$ (or $0 + i$)

---

### D9. Find $\bar{z}$ and $|z|$ for $z = -3i$

$\bar{z} = 3i$ (flip sign of imaginary part: $-3i \to 3i$).
$|z| = \sqrt{0^2 + (-3)^2} = 3$.

> **Answer**: $\bar{z} = 3i$, $|z| = 3$

---

### D10. Simplify $i^{15} + i^{16} + i^{17} + i^{18}$

$15 \div 4 = 3$ rem $3$: $i^{15} = -i$.
$16 \div 4 = 4$ rem $0$: $i^{16} = 1$.
$17 \div 4 = 4$ rem $1$: $i^{17} = i$.
$18 \div 4 = 4$ rem $2$: $i^{18} = -1$.

Sum: $(-i) + 1 + i + (-1) = 0$.

The 4-cycle sums to zero over any complete block: $i^k + i^{k+1} + i^{k+2} + i^{k+3} = 0$.

> **Answer**: $0$

---

## Advanced Drill

### A1. Solve $(1+i)z + 3 = 2i - z$

$(1+i)z + z = 2i - 3$
$(1+i+1)z = 2i - 3$
$(2+i)z = -3 + 2i$

$z = \frac{-3+2i}{2+i} \cdot \frac{2-i}{2-i} = \frac{(-3+2i)(2-i)}{4+1} = \frac{-6 + 3i + 4i - 2i^2}{5} = \frac{-6 + 7i + 2}{5} = \frac{-4 + 7i}{5} = -\frac{4}{5} + \frac{7}{5}i$.

> **Answer**: $z = -\frac{4}{5} + \frac{7}{5}i$

---

### A2. Compute $(1+i\sqrt{3})^9$ using De Moivre

$r = \sqrt{1^2 + (\sqrt{3})^2} = 2$. $\theta = \arctan(\sqrt{3}/1) = \pi/3$.
$1+i\sqrt{3} = 2e^{i\pi/3}$.

$(1+i\sqrt{3})^9 = 2^9 \cdot e^{i\cdot 9\pi/3} = 512 \cdot e^{i\cdot 3\pi} = 512(\cos 3\pi + i\sin 3\pi) = 512(-1 + 0) = -512$.

> **Answer**: $-512$

---

### A3. All four 4th roots of $-16$

$-16 = 16e^{i\pi}$. Fourth roots: $z_k = 16^{1/4} \cdot e^{i(\pi + 2\pi k)/4} = 2 \cdot e^{i(\pi + 2\pi k)/4}$ for $k = 0,1,2,3$.

- $k=0$: $2e^{i\pi/4} = 2(\frac{\sqrt{2}}{2} + i\frac{\sqrt{2}}{2}) = \sqrt{2} + i\sqrt{2}$
- $k=1$: $2e^{i\cdot 3\pi/4} = 2(-\frac{\sqrt{2}}{2} + i\frac{\sqrt{2}}{2}) = -\sqrt{2} + i\sqrt{2}$
- $k=2$: $2e^{i\cdot 5\pi/4} = 2(-\frac{\sqrt{2}}{2} - i\frac{\sqrt{2}}{2}) = -\sqrt{2} - i\sqrt{2}$
- $k=3$: $2e^{i\cdot 7\pi/4} = 2(\frac{\sqrt{2}}{2} - i\frac{\sqrt{2}}{2}) = \sqrt{2} - i\sqrt{2}$

> **Answer**: $\sqrt{2}+i\sqrt{2},\; -\sqrt{2}+i\sqrt{2},\; -\sqrt{2}-i\sqrt{2},\; \sqrt{2}-i\sqrt{2}$

---

### A4. Area of the square formed by 4th roots of 1

The 4th roots of 1 are $1, i, -1, -i$. These are vertices of a square with diagonal length 2.

Side length: $s = \sqrt{2}$ (Pythagoras: distance from $(1,0)$ to $(0,1)$ is $\sqrt{1^2+1^2} = \sqrt{2}$).
Area: $s^2 = 2$.

Alternatively: The square is inscribed in the unit circle. Area = $2r^2 = 2 \cdot 1 = 2$.

> **Answer**: $2$

---

### A5. Write $z = \sqrt{3} - i$ in polar form, then compute $z^6$

$r = \sqrt{(\sqrt{3})^2 + (-1)^2} = \sqrt{3+1} = 2$.
$\cos\theta = \frac{\sqrt{3}}{2}$, $\sin\theta = -\frac{1}{2}$, so $\theta = -\frac{\pi}{6}$ (or $\frac{11\pi}{6}$).
$z = 2e^{-i\pi/6}$.

$z^6 = 2^6 \cdot e^{-i\cdot 6\pi/6} = 64 \cdot e^{-i\pi} = 64(\cos(-\pi) + i\sin(-\pi)) = 64(-1 + 0) = -64$.

> **Answer**: $z = 2e^{-i\pi/6}$, $z^6 = -64$

---

### A6. Solve $z^2 + 2z + 5 = 0$ over complex numbers

Quadratic formula: $z = \frac{-2 \pm \sqrt{4 - 20}}{2} = \frac{-2 \pm \sqrt{-16}}{2} = \frac{-2 \pm 4i}{2} = -1 \pm 2i$.

> **Answer**: $z = -1 + 2i$ or $z = -1 - 2i$

---

### A7. Find all complex $z$ such that $z^3 = 8i$

$8i = 8e^{i\pi/2}$ (modulus 8, angle $\pi/2$).

Cube roots: $z_k = 8^{1/3} \cdot e^{i(\pi/2 + 2\pi k)/3} = 2 \cdot e^{i(\pi/2 + 2\pi k)/3}$ for $k = 0,1,2$.

- $k=0$: $2e^{i\pi/6} = 2(\frac{\sqrt{3}}{2} + i\frac{1}{2}) = \sqrt{3} + i$
- $k=1$: $2e^{i\cdot 5\pi/6} = 2(-\frac{\sqrt{3}}{2} + i\frac{1}{2}) = -\sqrt{3} + i$
- $k=2$: $2e^{i\cdot 3\pi/2} = 2(0 - i) = -2i$

Check: $(\sqrt{3}+i)^3$ — using De Moivre: $(2e^{i\pi/6})^3 = 8e^{i\pi/2} = 8i$ ✓.

> **Answer**: $\sqrt{3}+i,\; -\sqrt{3}+i,\; -2i$

---

### A8. If $z = 2e^{i\pi/6}$, find $z^4$ and $1/z$ in $a+bi$ form

$z^4 = 2^4 \cdot e^{i\cdot 4\pi/6} = 16 \cdot e^{i\cdot 2\pi/3} = 16(\cos\frac{2\pi}{3} + i\sin\frac{2\pi}{3}) = 16(-\frac{1}{2} + i\frac{\sqrt{3}}{2}) = -8 + 8i\sqrt{3}$.

$\frac{1}{z} = z^{-1} = 2^{-1} \cdot e^{-i\pi/6} = \frac{1}{2}(\cos\frac{\pi}{6} - i\sin\frac{\pi}{6}) = \frac{1}{2}(\frac{\sqrt{3}}{2} - i\frac{1}{2}) = \frac{\sqrt{3}}{4} - \frac{1}{4}i$.

> **Answer**: $z^4 = -8 + 8i\sqrt{3}$, $\frac{1}{z} = \frac{\sqrt{3}}{4} - \frac{1}{4}i$

---

### A9. Prove $|z_1 z_2| = |z_1| \cdot |z_2|$

Let $z_1 = a+bi$, $z_2 = c+di$.

$|z_1 z_2|^2 = (z_1 z_2)(\overline{z_1 z_2}) = (z_1 z_2)(\bar{z_1}\bar{z_2}) = (z_1\bar{z_1})(z_2\bar{z_2}) = |z_1|^2 |z_2|^2$.

Taking square roots: $|z_1 z_2| = |z_1| \cdot |z_2|$.

Geometric interpretation: multiplying complex numbers multiplies their moduli.

> **Answer**: Proof by conjugate property: $|z_1z_2|^2 = z_1z_2\overline{z_1z_2} = |z_1|^2 |z_2|^2$

---

### A10. Area of triangle formed by cube roots of $8i$

From A7, the roots are $\sqrt{3}+i$, $-\sqrt{3}+i$, $-2i$.

These lie on a circle of radius 2, equally spaced by $120^\circ$. Check: all have $|z| = 2$ ✓.

Area of equilateral triangle inscribed in radius $r=2$:
$\text{Area} = \frac{3\sqrt{3}}{4}r^2 = \frac{3\sqrt{3}}{4} \cdot 4 = 3\sqrt{3}$.

> **Answer**: $3\sqrt{3}$
