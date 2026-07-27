# Solutions — Session 9B: 2D Geometry

---

## Practice 1

> A line passes through $(1, 4)$ and $(5, -2)$. Write it in all five forms. What is its $x$-intercept?

**Step 1: Find the slope.**
$$m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{-2 - 4}{5 - 1} = \frac{-6}{4} = -\frac{3}{2}$$

**Step 2: Write all five forms.**

| # | Form | Equation |
|:--:|:-----:|:--------:|
| ① | Point-slope | $y - 4 = -\frac{3}{2}(x - 1)$ |
| ② | Slope-intercept | $y = -\frac{3}{2}x + \frac{11}{2}$ |
| ③ | Two-point | $\frac{y-4}{x-1} = \frac{-2-4}{5-1} = -\frac{3}{2}$ |
| ④ | Intercept | $\frac{x}{11/3} + \frac{y}{11/2} = 1$ |
| ⑤ | General | $3x + 2y - 11 = 0$ |

- ②: $y = -\frac{3}{2}(x-1) + 4 = -\frac{3}{2}x + \frac{3}{2} + 4 = -\frac{3}{2}x + \frac{11}{2}$
- ④: $x$-intercept: $0 = -\frac{3}{2}x + \frac{11}{2}$ → $x = \frac{11}{3}$. $y$-intercept: $y = \frac{11}{2}$.
- ⑤: $2y = -3x + 11$ → $3x + 2y - 11 = 0$.

**Answer: $x$-intercept is $\frac{11}{3}$.**

---

## Practice 2

> Find the acute angle between the lines $y = 3x + 1$ and $2x + y = 5$.

**Step 1: Extract slopes.**
$L_1: y = 3x + 1$ → $m_1 = 3$.
$L_2: 2x + y = 5$ → $y = -2x + 5$ → $m_2 = -2$.

**Step 2: Apply the angle formula.**
$$\tan\phi = \left|\frac{m_2 - m_1}{1 + m_1 m_2}\right| = \left|\frac{-2 - 3}{1 + 3(-2)}\right| = \left|\frac{-5}{1 - 6}\right| = \left|\frac{-5}{-5}\right| = 1$$

$\phi = \tan^{-1}(1) = 45°$.

**Answer: 45°.**

---

## Practice 3

> Find the distance from $(2, -1)$ to the line $4x - 3y + 5 = 0$, and find the foot of the perpendicular.

**Step 1: Distance.**
$A = 4$, $B = -3$, $C = 5$ (note: the constant is $+5$, not $-d$).
Standard form: $4x - 3y + 5 = 0$.
$$d = \frac{|4(2) - 3(-1) + 5|}{\sqrt{4^2 + (-3)^2}} = \frac{|8 + 3 + 5|}{5} = \frac{16}{5} = 3.2$$

**Step 2: Foot of the perpendicular.**
The perpendicular line through $(2, -1)$ has direction parallel to the normal $(4, -3)$.
Parametric: $(x, y) = (2, -1) + t(4, -3) = (2 + 4t,\; -1 - 3t)$.
Plug into line equation:
$4(2+4t) - 3(-1-3t) + 5 = 0$ → $8 + 16t + 3 + 9t + 5 = 0$ → $25t + 16 = 0$ → $t = -\frac{16}{25}$.

Foot: $(2 + 4(-\frac{16}{25}),\; -1 - 3(-\frac{16}{25})) = (2 - \frac{64}{25},\; -1 + \frac{48}{25}) = (-\frac{14}{25},\; \frac{23}{25})$.

Verify: $4(-\frac{14}{25}) - 3(\frac{23}{25}) + 5 = -\frac{56}{25} - \frac{69}{25} + \frac{125}{25} = 0$. ✓

**Answer: $d = \frac{16}{5}$, foot $(-\frac{14}{25}, \frac{23}{25})$.**

---

## Practice 4

> Find the center, vertices, foci, and eccentricity of $9x^2 + 25y^2 = 225$.

**Step 1: Standard form.**
Divide by 225: $\frac{x^2}{25} + \frac{y^2}{9} = 1$.
$a^2 = 25$, $b^2 = 9$ → $a = 5$, $b = 3$. Since $a > b$, major axis is horizontal.

**Step 2: Find $c$ and $e$.**
$c^2 = a^2 - b^2 = 25 - 9 = 16$ → $c = 4$.
$e = \frac{c}{a} = \frac{4}{5} = 0.8$.

**Step 3: Key features.**
- Center: $(0, 0)$
- Vertices: $(\pm 5, 0)$
- Co-vertices: $(0, \pm 3)$
- Foci: $(\pm 4, 0)$
- Eccentricity: $0.8$

---

## Practice 5

> A parabola has focus $(2, 1)$ and directrix $y = -3$. Find its equation in standard form and vertex form.

**Step 1: Find vertex.**
Vertex is halfway between focus and directrix.
Focus: $(2, 1)$, directrix $y = -3$.
Vertex $y$-coordinate: $\frac{1 + (-3)}{2} = -1$. $x$-coordinate same as focus: $2$.
Vertex: $(2, -1)$.

**Step 2: Find $p$ (directed distance from vertex to focus).**
$p = 1 - (-1) = 2$. Positive → opens upward.

**Step 3: Write equations.**
Standard form: $(x - 2)^2 = 4p(y + 1) = 8(y + 1)$.
Vertex form: $y = \frac{1}{8}(x - 2)^2 - 1$.

**Answer: $(x-2)^2 = 8(y+1)$, or $y = \frac{1}{8}(x-2)^2 - 1$.**

---

## Practice 6: Real Battle

> A hyperbola has asymptotes $y = \pm\frac{4}{3}x$ and passes through $(5, 0)$. Find its equation, foci, and eccentricity. Then find the distance from the origin to either asymptote.

**Step 1: Identify $a$ and $b$.**
Since the hyperbola passes through $(5, 0)$ and the asymptotes are symmetric, the transverse axis is the $x$-axis.
With center at $(0, 0)$: $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$.
Asymptotes: $y = \pm\frac{b}{a}x = \pm\frac{4}{3}x$ → $\frac{b}{a} = \frac{4}{3}$ → $b = \frac{4}{3}a$.

Plug $(5, 0)$: $\frac{25}{a^2} - 0 = 1$ → $a^2 = 25$ → $a = 5$.
Then $b = \frac{4}{3} \cdot 5 = \frac{20}{3}$, $b^2 = \frac{400}{9}$.

**Equation**: $\frac{x^2}{25} - \frac{y^2}{400/9} = 1$, or $\frac{x^2}{25} - \frac{9y^2}{400} = 1$.

**Step 2: Foci and eccentricity.**
$c^2 = a^2 + b^2 = 25 + \frac{400}{9} = \frac{225 + 400}{9} = \frac{625}{9}$ → $c = \frac{25}{3}$.
Foci: $(\pm\frac{25}{3}, 0)$.
$e = \frac{c}{a} = \frac{25/3}{5} = \frac{5}{3}$.

**Step 3: Distance from origin to asymptote.**
Asymptote: $y = \frac{4}{3}x$ → $4x - 3y = 0$.
$d = \frac{|4(0) - 3(0)|}{\sqrt{16 + 9}} = 0$. Wait — the line passes through the origin!

The asymptotes $y = \pm\frac{4}{3}x$ **pass through the origin**, so the distance from the origin to either asymptote is **0**. But that's trivial. The intended meaning: the distance from an *arbitrary* point to the asymptote — or perhaps the distance between the two asymptotes at a given $x$. Let's re-read the prompt...

The prompt says "the distance from the origin to either asymptote (they are the same)." Both asymptotes are $y = \frac{4}{3}x$ and $y = -\frac{4}{3}x$, both pass through $(0,0)$, so indeed distance = 0. This is a trick — the hyperbola's center IS the origin, so asymptotes always pass through the center.

**Answer: $\frac{x^2}{25} - \frac{9y^2}{400} = 1$, foci $(\pm\frac{25}{3}, 0)$, $e = \frac{5}{3}$, distance to asymptote = 0 (they pass through origin).**

---

## Basic Drills

---

### D1
> Write the equation of the line through $(3, -1)$ with slope $\frac{2}{5}$ in point-slope, slope-intercept, and general form.

**Point-slope**: $y + 1 = \frac{2}{5}(x - 3)$.
**Slope-intercept**: $y = \frac{2}{5}x - \frac{6}{5} - 1 = \frac{2}{5}x - \frac{11}{5}$.
**General**: $5y = 2x - 11$ → $2x - 5y - 11 = 0$.

---

### D2
> Find the midpoint of the segment joining $(-3, 7)$ and $(9, -5)$.

$$M = \left(\frac{-3 + 9}{2},\; \frac{7 + (-5)}{2}\right) = \left(\frac{6}{2},\; \frac{2}{2}\right) = (3, 1)$$

---

### D3
> Determine whether the lines $6x - 3y + 1 = 0$ and $y = 2x - 4$ are parallel, perpendicular, or neither.

$L_1: 6x - 3y + 1 = 0$ → $3y = 6x + 1$ → $y = 2x + \frac{1}{3}$ → $m_1 = 2$.
$L_2: y = 2x - 4$ → $m_2 = 2$.
$m_1 = m_2 = 2$ → **Parallel**.

---

### D4
> Find the distance from $(-2, 8)$ to the line $5x + 12y - 10 = 0$.

$d = \frac{|5(-2) + 12(8) - 10|}{\sqrt{25 + 144}} = \frac{|-10 + 96 - 10|}{13} = \frac{76}{13} \approx 5.846$.

---

### D5
> Find the center and radius of $x^2 + y^2 + 8x - 6y + 21 = 0$.

$(x^2 + 8x) + (y^2 - 6y) = -21$.
$(x^2 + 8x + 16) + (y^2 - 6y + 9) = -21 + 16 + 9$.
$(x + 4)^2 + (y - 3)^2 = 4$.
**Center: $(-4, 3)$, radius: $2$.**

---

### D6
> Identify the conic: $4x^2 + 9y^2 - 16x + 18y - 11 = 0$. Find its center and vertices.

$B = 0$, $A = 4$, $C = 9$. $B^2 - 4AC = -144 < 0$ → **Ellipse**.

Complete squares:
$4(x^2 - 4x) + 9(y^2 + 2y) = 11$.
$4(x - 2)^2 + 9(y + 1)^2 = 11 + 16 + 9 = 36$.
$\frac{(x-2)^2}{9} + \frac{(y+1)^2}{4} = 1$.

$a^2 = 9$, $b^2 = 4$ → $a = 3$, $b = 2$. Major axis horizontal.
Center: $(2, -1)$. Vertices: $(2 \pm 3, -1) = (5, -1)$ and $(-1, -1)$.

---

### D7
> Identify the conic: $y^2 - 4x^2 = 16$. Find its asymptotes and foci.

Rewrite: $\frac{y^2}{16} - \frac{x^2}{4} = 1$. $B^2 - 4AC = 0 - 4(-4)(1) = 16 > 0$ → **Hyperbola**.
Vertical transverse axis ($y^2$ positive).

$a^2 = 16$ → $a = 4$. $b^2 = 4$ → $b = 2$.
$c^2 = a^2 + b^2 = 20$ → $c = 2\sqrt{5}$.
Center: $(0, 0)$. Vertices: $(0, \pm 4)$. Foci: $(0, \pm 2\sqrt{5})$.
Asymptotes: $y = \pm\frac{a}{b}x = \pm 2x$.

---

### D8
> Find the equation of the parabola with vertex $(3, -2)$ and focus $(3, 1)$.

Focus is above vertex → opens upward.
$p = 1 - (-2) = 3$.
Standard form: $(x - 3)^2 = 4(3)(y + 2) = 12(y + 2)$.
Vertex form: $y = \frac{1}{12}(x - 3)^2 - 2$.

---

### D9
> A line segment from $(2, 3)$ to $(8, 9)$ is divided by a point that is twice as far from the first endpoint as from the second. Find the coordinates of the dividing point.

"Twice as far from first as from second" means ratio $2:1$ from the first endpoint.
Using section formula with $m = 2$, $n = 1$, $(x_1,y_1) = (2,3)$, $(x_2,y_2) = (8,9)$:
$$P = \left(\frac{2(8) + 1(2)}{3},\; \frac{2(9) + 1(3)}{3}\right) = \left(\frac{18}{3},\; \frac{21}{3}\right) = (6, 7)$$

---

### D10
> Find the tangent length from $(13, 0)$ to the circle $x^2 + y^2 = 25$. Find the equation of one tangent line.

**Tangent length**: Center $(0,0)$, $R = 5$. $PC = 13$.
$PT = \sqrt{13^2 - 5^2} = \sqrt{169 - 25} = \sqrt{144} = 12$.

**Tangent line equation**: Tangent points satisfy $x^2 + y^2 = 25$ and $(x,y) \perp (x-13, y)$ from $(13,0)$.
Dot product: $x(x-13) + y(y-0) = 0$ → $x^2 - 13x + y^2 = 0$ → $(x^2 + y^2) - 13x = 0$ → $25 - 13x = 0$ → $x = \frac{25}{13}$.
Then $y^2 = 25 - (\frac{25}{13})^2 = 25(1 - \frac{25}{169}) = 25 \cdot \frac{144}{169} = \frac{3600}{169}$ → $y = \pm\frac{60}{13}$.

Tangent line through $(13, 0)$ and $(\frac{25}{13}, \frac{60}{13})$:
$m = \frac{60/13 - 0}{25/13 - 13} = \frac{60/13}{(25-169)/13} = \frac{60}{-144} = -\frac{5}{12}$.
Line: $y - 0 = -\frac{5}{12}(x - 13)$ → $12y = -5x + 65$ → $5x + 12y = 65$.

---

### ◆ D11
> Without computing the distance formula explicitly, explain geometrically why $(3, 4)$ to the line $3x + 4y = 0$ is exactly 5 units away.

The distance from origin to $(3,4)$ is $\sqrt{3^2+4^2} = 5$. The line $3x+4y=0$ passes through the origin. The vector $(3,4)$ from the origin to the point is **parallel to the normal** $(3,4)$ of the line. So the perpendicular from $(3,4)$ to the line is exactly the segment from $(3,4)$ back to the origin along that same direction. The line passes through the origin, so the foot of the perpendicular is $(0,0)$. Thus the distance is simply $|OP| = 5$.

---

### ◆ D12
> Two points $A(0, 0)$ and $B(6, 0)$ form the base of a triangle. The third vertex $C$ moves such that the area is always 12. What curve does $C$ trace?

Area = $\frac{1}{2} \cdot \text{base} \cdot \text{height} = \frac{1}{2} \cdot 6 \cdot h = 3h = 12$ → $h = 4$.

The height from $C$ to base $AB$ (the $x$-axis) must be 4. So $C$ has $y = \pm 4$.
**$C$ traces two parallel lines: $y = 4$ and $y = -4$.** These are horizontal lines at distance 4 from the $x$-axis.

---

### ◆ D13
> A line with slope $m$ passes through $(0, 0)$. For what values of $m$ does the line intersect the circle $x^2 + y^2 - 4x - 4y + 4 = 0$ at exactly one point?

Circle: $(x-2)^2 + (y-2)^2 = 4 + 4 - 4 = 4$. Center $(2,2)$, $R=2$.

Line: $y = mx$. Substitute: $x^2 + m^2x^2 - 4x - 4mx + 4 = 0$ → $(1+m^2)x^2 - 4(1+m)x + 4 = 0$.
For tangency (one intersection), discriminant = 0:
$\Delta = 16(1+m)^2 - 16(1+m^2) = 16(1 + 2m + m^2 - 1 - m^2) = 16(2m) = 32m = 0$ → $m = 0$.

But wait — geometrically, from the origin $(0,0)$ to circle center $(2,2)$, the distance is $\sqrt{8} \approx 2.828 > R=2$, so the origin is outside. There are two tangent lines from origin. Let me re-check...

The discriminant gives $m=0$ as the only solution? That seems wrong. Let me recalculate:
$\Delta = [-4(1+m)]^2 - 4(1+m^2)(4) = 16(1+m)^2 - 16(1+m^2) = 16(1+2m+m^2-1-m^2) = 32m$.

Set $32m = 0$ → $m = 0$. But this only gives one tangent? The issue: when $m$ is infinite (vertical line $x=0$), that's the other tangent. The vertical line $x=0$: $0 + y^2 - 0 - 4y + 4 = 0$ → $y^2 - 4y + 4 = 0$ → $(y-2)^2 = 0$ → $y=2$ (double root). ✓

So $m = 0$ (horizontal) and $m \to \infty$ (vertical). **$m = 0$ or the vertical line ($m$ undefined).**

---

### ◆ D14
> The parametric curve $(x(t), y(t)) = (t^2, t)$ for $t \in \mathbb{R}$ describes a parabola. Find its Cartesian equation and identify the vertex and focus.

$y = t$, so $x = t^2 = y^2$. Cartesian: $x = y^2$, or $y^2 = x$.
This is a parabola opening right. Standard form: $y^2 = 4px$ with $4p = 1$ → $p = \frac{1}{4}$.
Vertex: $(0, 0)$. Focus: $(\frac{1}{4}, 0)$. Directrix: $x = -\frac{1}{4}$.

---

### ◆ D15
> Consider the family of lines $y = mx + (1-m)$ for all real $m$. Show that ALL these lines pass through a single fixed point. Find that point.

Rewrite: $y = mx + 1 - m = m(x - 1) + 1$.
When $x = 1$: $y = m(0) + 1 = 1$, independent of $m$.
**All lines pass through $(1, 1)$.**

---

## Advanced Drills

---

### A1
> Find the equation of the circle passing through the three points $(1, 2)$, $(4, 1)$, and $(2, -3)$.

General form: $x^2 + y^2 + Dx + Ey + F = 0$.

$(1,2)$: $1 + 4 + D + 2E + F = 0$ → $D + 2E + F = -5$  …①
$(4,1)$: $16 + 1 + 4D + E + F = 0$ → $4D + E + F = -17$  …②
$(2,-3)$: $4 + 9 + 2D - 3E + F = 0$ → $2D - 3E + F = -13$  …③

②−①: $3D - E = -12$  …④
②−③: $2D + 4E = -4$ → $D + 2E = -2$  …⑤

From ⑤: $D = -2 - 2E$. Plug into ④: $3(-2-2E) - E = -12$ → $-6 - 6E - E = -12$ → $-7E = -6$ → $E = \frac{6}{7}$.

$D = -2 - 2(\frac{6}{7}) = -2 - \frac{12}{7} = -\frac{26}{7}$.

From ①: $-\frac{26}{7} + 2(\frac{6}{7}) + F = -5$ → $-\frac{26}{7} + \frac{12}{7} + F = -5$ → $-\frac{14}{7} + F = -5$ → $F = -3$.

So $D = -\frac{26}{7}$, $E = \frac{6}{7}$, $F = -3$.

Circle: $x^2 + y^2 - \frac{26}{7}x + \frac{6}{7}y - 3 = 0$, or $7x^2 + 7y^2 - 26x + 6y - 21 = 0$.

Center: $(-\frac{D}{2}, -\frac{E}{2}) = (\frac{13}{7}, -\frac{3}{7})$.
$R = \sqrt{(\frac{13}{7})^2 + (-\frac{3}{7})^2 + 3} = \sqrt{\frac{169+9}{49} + 3} = \sqrt{\frac{178}{49} + \frac{147}{49}} = \sqrt{\frac{325}{49}} = \frac{5\sqrt{13}}{7}$.

---

### A2
> Find the distance between the parallel lines $3x - 4y + 7 = 0$ and $6x - 8y - 15 = 0$.

First, normalize to same $A,B$: divide second by 2: $3x - 4y - \frac{15}{2} = 0$.
$C_1 = 7$, $C_2 = -\frac{15}{2}$.
$d = \frac{|C_2 - C_1|}{\sqrt{A^2 + B^2}} = \frac{|-\frac{15}{2} - 7|}{5} = \frac{|-\frac{29}{2}|}{5} = \frac{29}{10} = 2.9$.

---

### A3
> A line through $(2, 3)$ has slope $m$. It intersects the circle $x^2 + y^2 = 20$ at two points. For what values of $m$ is the line tangent?

Line: $y - 3 = m(x - 2)$ → $y = mx - 2m + 3$.
Substitute into $x^2 + y^2 = 20$:
$x^2 + (mx - 2m + 3)^2 = 20$.
$x^2 + m^2x^2 + 2mx(3-2m) + (3-2m)^2 - 20 = 0$.
$(1+m^2)x^2 + 2m(3-2m)x + (3-2m)^2 - 20 = 0$.

For tangency, $\Delta = 0$:
$4m^2(3-2m)^2 - 4(1+m^2)[(3-2m)^2 - 20] = 0$.
$m^2(3-2m)^2 - (1+m^2)(3-2m)^2 + 20(1+m^2) = 0$.
$(3-2m)^2(m^2 - 1 - m^2) + 20(1+m^2) = 0$.
$-(3-2m)^2 + 20(1+m^2) = 0$.
$-(9 - 12m + 4m^2) + 20 + 20m^2 = 0$.
$16m^2 + 12m + 11 = 0$.
$\Delta_m = 144 - 704 = -560 < 0$ → No real $m$!

Meaning the point $(2,3)$ is inside the circle (check: $2^2+3^2=13 < 20$). **No tangent line exists through an interior point.** Answer: no real $m$.

---

### A4
> The ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ has eccentricity $\frac{3}{5}$ and passes through $(4, \frac{12}{5})$. Find $a$ and $b$.

$e = \frac{c}{a} = \frac{3}{5}$ → $c = \frac{3}{5}a$. Then $c^2 = a^2 - b^2$ → $\frac{9}{25}a^2 = a^2 - b^2$ → $b^2 = \frac{16}{25}a^2$ → $b = \frac{4}{5}a$.

Point $(4, \frac{12}{5})$: $\frac{16}{a^2} + \frac{144/25}{b^2} = 1$.
Substitute $b^2 = \frac{16}{25}a^2$: $\frac{16}{a^2} + \frac{144/25}{16a^2/25} = 1$ → $\frac{16}{a^2} + \frac{144}{16a^2} = 1$ → $\frac{16}{a^2} + \frac{9}{a^2} = 1$ → $\frac{25}{a^2} = 1$ → $a^2 = 25$ → $a = 5$.

$b = \frac{4}{5} \cdot 5 = 4$. **$a = 5$, $b = 4$.**

---

### A5
> Find the equation of the hyperbola with foci $(\pm 5, 0)$ that passes through $(4, 0)$.

Foci at $(\pm c, 0)$ → $c = 5$. Transverse axis is horizontal.
Passes through $(4,0)$ → $(4,0)$ is a vertex → $a = 4$.
$c^2 = a^2 + b^2$ → $25 = 16 + b^2$ → $b^2 = 9$.

Equation: $\frac{x^2}{16} - \frac{y^2}{9} = 1$.

---

### A6
> Reflect the point $(3, -2)$ across the line $y = 2x + 1$. Find the coordinates of the reflected point.

Line: $2x - y + 1 = 0$. $A=2$, $B=-1$, $C=1$.
$Ax_0 + By_0 + C = 2(3) - (-2) + 1 = 6 + 2 + 1 = 9$.
$A^2 + B^2 = 4 + 1 = 5$.

Reflection formula: $P' = P - 2\frac{Ax_0+By_0+C}{A^2+B^2}(A,B)$.
$P' = (3, -2) - 2 \cdot \frac{9}{5}(2, -1) = (3, -2) - (\frac{36}{5}, -\frac{18}{5}) = (3 - \frac{36}{5}, -2 + \frac{18}{5}) = (-\frac{21}{5}, \frac{8}{5}) = (-4.2, 1.6)$.

Check: midpoint $(\frac{3-4.2}{2}, \frac{-2+1.6}{2}) = (-0.6, -0.2)$. On line? $2(-0.6) - (-0.2) + 1 = -1.2 + 0.2 + 1 = 0$. ✓

---

### A7
> The parametric curve $(x(t), y(t)) = (\sec t,\; \tan t)$ for $t \in (-\pi/2, \pi/2)$ describes part of a hyperbola. Eliminate $t$ to find the Cartesian equation.

Identity: $\sec^2 t - \tan^2 t = 1$.
So $x^2 - y^2 = 1$. This is a hyperbola with $a=b=1$, opening left-right.
Since $t \in (-\pi/2, \pi/2)$, $\sec t \geq 1$, so only the right branch ($x \geq 1$).

---

### A8
> Find the area of the quadrilateral with vertices $(1, 1)$, $(6, 2)$, $(5, 7)$, $(2, 5)$.

Shoelace formula (vertices in order):
$\begin{array}{cc} x & y \\ 1 & 1 \\ 6 & 2 \\ 5 & 7 \\ 2 & 5 \\ 1 & 1 \end{array}$

Sum down: $1\cdot2 + 6\cdot7 + 5\cdot5 + 2\cdot1 = 2 + 42 + 25 + 2 = 71$.
Sum up: $1\cdot6 + 2\cdot5 + 7\cdot2 + 5\cdot1 = 6 + 10 + 14 + 5 = 35$.

Area = $\frac{1}{2}|71 - 35| = \frac{1}{2} \cdot 36 = 18$.

---

### A9
> A line passes through $(3, 0)$ and intersects the parabola $y = x^2$ at two points $P$ and $Q$. Find the equation of the line if the midpoint of $PQ$ lies on the line $x = 1$.

Line: $y = m(x - 3)$. Intersect with $y = x^2$:
$x^2 = m(x-3)$ → $x^2 - mx + 3m = 0$.

Roots $x_1, x_2$ are the $x$-coordinates of $P$ and $Q$.
Sum of roots: $x_1 + x_2 = m$. Midpoint $x$-coordinate: $\frac{m}{2}$.

Condition: midpoint $x = 1$ → $\frac{m}{2} = 1$ → $m = 2$.

Line equation: $y = 2(x - 3) = 2x - 6$.

---

### A10
> Two circles: $x^2 + y^2 = 4$ and $(x-3)^2 + (y-4)^2 = 1$. Find the shortest distance between them. Do they intersect?

$C_1 = (0,0)$, $R_1 = 2$. $C_2 = (3,4)$, $R_2 = 1$.
Distance between centers: $d = \sqrt{9+16} = 5$.

Since $d = 5 > R_1 + R_2 = 3$, circles are separate (no intersection).
Shortest distance = $d - R_1 - R_2 = 5 - 2 - 1 = 2$.

---

### ◆ A11
> A point moves such that its distance from $(1, 0)$ is always twice its distance from the line $x = 4$. Find the equation of its path and identify the conic. What is its eccentricity?

Let the point be $(x, y)$.
$\sqrt{(x-1)^2 + y^2} = 2|x - 4|$.
Square: $(x-1)^2 + y^2 = 4(x-4)^2$.
$x^2 - 2x + 1 + y^2 = 4x^2 - 32x + 64$.
$0 = 3x^2 - 30x - y^2 + 63$.
$3(x^2 - 10x) - y^2 = -63$.
$3(x-5)^2 - y^2 = -63 + 75 = 12$.
$\frac{(x-5)^2}{4} - \frac{y^2}{12} = 1$.

This is a **hyperbola** with center $(5, 0)$. Since the distance to a point is $k$ times the distance to a line, and $k = 2 > 1$, the conic is a hyperbola with **eccentricity $e = 2$**.

---

### ◆ A12
> The line $y = mx + c$ is tangent to the ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$. Derive the condition on $m$ and $c$. Show $c^2 = a^2 m^2 + b^2$.

Substitute $y = mx + c$ into $\frac{x^2}{a^2} + \frac{(mx+c)^2}{b^2} = 1$.
$\frac{x^2}{a^2} + \frac{m^2x^2 + 2mcx + c^2}{b^2} = 1$.
$b^2x^2 + a^2m^2x^2 + 2a^2mcx + a^2c^2 = a^2b^2$.
$(b^2 + a^2m^2)x^2 + 2a^2mcx + a^2(c^2 - b^2) = 0$.

For tangency, $\Delta = 0$:
$4a^4m^2c^2 - 4(b^2 + a^2m^2)a^2(c^2 - b^2) = 0$.
$a^2m^2c^2 - (b^2 + a^2m^2)(c^2 - b^2) = 0$.
$a^2m^2c^2 - b^2c^2 + b^4 - a^2m^2c^2 + a^2m^2b^2 = 0$.
$-b^2c^2 + b^4 + a^2m^2b^2 = 0$.
Divide by $b^2$: $-c^2 + b^2 + a^2m^2 = 0$.
**$c^2 = a^2m^2 + b^2$.** ✓

---

### ◆ A13
> Rotate the rectangle with vertices $(0,0), (a,0), (a,b), (0,b)$ by angle $\theta$ about the origin. Find the area using the shoelace formula, and verify that area is invariant under rotation.

Rotation matrix: $R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$.

Rotated vertices:
$A: (0,0)$.
$B: (a\cos\theta, a\sin\theta)$.
$C: (a\cos\theta - b\sin\theta, a\sin\theta + b\cos\theta)$.
$D: (-b\sin\theta, b\cos\theta)$.

Shoelace:
Sum down: $0\cdot a\sin\theta + a\cos\theta(a\sin\theta+b\cos\theta) + (a\cos\theta-b\sin\theta)(b\cos\theta) + (-b\sin\theta)(0)$
$= a\cos\theta(a\sin\theta+b\cos\theta) + (a\cos\theta-b\sin\theta)b\cos\theta$
$= a^2\sin\theta\cos\theta + ab\cos^2\theta + ab\cos^2\theta - b^2\sin\theta\cos\theta$
$= (a^2 - b^2)\sin\theta\cos\theta + 2ab\cos^2\theta$.

Sum up: $0\cdot a\cos\theta + a\sin\theta(a\cos\theta-b\sin\theta) + (a\sin\theta+b\cos\theta)(-b\sin\theta) + b\cos\theta(0)$
$= a\sin\theta(a\cos\theta-b\sin\theta) - b\sin\theta(a\sin\theta+b\cos\theta)$
$= a^2\sin\theta\cos\theta - ab\sin^2\theta - ab\sin^2\theta - b^2\sin\theta\cos\theta$
$= (a^2 - b^2)\sin\theta\cos\theta - 2ab\sin^2\theta$.

Difference: $2ab\cos^2\theta - (-2ab\sin^2\theta) = 2ab(\cos^2\theta + \sin^2\theta) = 2ab$.

Area = $\frac{1}{2}|2ab| = ab$, which equals the original rectangle area. **Area is invariant under rotation.** ✓

---

### ◆ A14
> Two perpendicular lines through the origin intersect the ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ at four points. Show that $\frac{1}{OP_1^2} + \frac{1}{OP_2^2}$ is constant.

Let line 1 have direction angle $\theta$: $y = (\tan\theta)x$. Line 2: $y = (-\cot\theta)x$ (perpendicular).

Intersection of line 1 with ellipse: $x = r\cos\theta, y = r\sin\theta$.
$\frac{r^2\cos^2\theta}{a^2} + \frac{r^2\sin^2\theta}{b^2} = 1$ → $\frac{1}{OP_1^2} = \frac{\cos^2\theta}{a^2} + \frac{\sin^2\theta}{b^2}$.

Intersection of line 2 (angle $\theta+90°$):
$\frac{1}{OP_2^2} = \frac{\cos^2(\theta+90°)}{a^2} + \frac{\sin^2(\theta+90°)}{b^2} = \frac{\sin^2\theta}{a^2} + \frac{\cos^2\theta}{b^2}$.

Sum: $\frac{1}{OP_1^2} + \frac{1}{OP_2^2} = \frac{\cos^2\theta + \sin^2\theta}{a^2} + \frac{\sin^2\theta + \cos^2\theta}{b^2} = \frac{1}{a^2} + \frac{1}{b^2}$.

**Constant for any $\theta$!** This is a beautiful geometric property of the ellipse. ✓

---

### ◆ A15
> Consider all chords of the parabola $y = x^2$ that pass through the point $(0, 1)$. Prove that the midpoints of these chords all lie on another parabola. Find its equation.

A chord through $(0,1)$ with slope $m$: $y = mx + 1$.
Intersect with $y = x^2$: $x^2 = mx + 1$ → $x^2 - mx - 1 = 0$.
Roots $x_1, x_2$: $x_1 + x_2 = m$, $x_1x_2 = -1$.

Midpoint: $x_M = \frac{x_1+x_2}{2} = \frac{m}{2}$.
$y_M = \frac{y_1+y_2}{2} = \frac{x_1^2 + x_2^2}{2} = \frac{(x_1+x_2)^2 - 2x_1x_2}{2} = \frac{m^2 + 2}{2} = \frac{m^2}{2} + 1$.

From $x_M = m/2$: $m = 2x_M$.
$y_M = \frac{(2x_M)^2}{2} + 1 = 2x_M^2 + 1$.

**Locus: $y = 2x^2 + 1$.** This is another parabola, vertex $(0,1)$, narrower than the original. ✓
