# 04 — Curvilinear Motion: Acceleration Without Changing Speed

> **Kleppner:** Ch 1.8~1.10 | **Time:** 75 min
> **Core Question:** Can acceleration exist even when speed stays exactly the same?

---

## Scene: A Child on a Merry-Go-Round

A child rides a merry-go-round at a steady speed. The speed never changes — yet the child *feels* pushed outward, pressed against the rail.

If speed is constant, where does this "force" come from? The answer: **the direction of the velocity vector is changing.** And changing a vector — even just its direction — is acceleration.

---

## ❌ What If You Try With Algebra Alone?

### The Paradox of Uniform Circular Motion

An object moves in a circle of radius $r$ at constant speed $v$. Since $|\vec{v}| = v$ never changes, you might think $\vec{a} = 0$.

**But that's wrong.** Let's try to see why.

### Attempt: Approximate the Direction Change

After a short time $\Delta t$, the object has moved an angle $\Delta\theta = v\Delta t / r$ along the circle. The velocity vectors at the start and end have the **same length** $v$, but their directions differ by $\Delta\theta$.

Draw the two velocity vectors tail-to-tail. The change $\Delta\vec{v}$ is the vector connecting their tips. For small $\Delta\theta$, the triangle is isosceles with two sides of length $v$ and a small angle $\Delta\theta$ between them:

$$\frac{|\Delta\vec{v}|}{v} \approx \Delta\theta \quad\text{(similar triangles, but an approximation!)}$$

So:

$$|\Delta\vec{v}| \approx v\Delta\theta = v \cdot \frac{v\Delta t}{r} = \frac{v^2}{r}\Delta t$$

$$|\vec{a}| \approx \frac{|\Delta\vec{v}|}{\Delta t} \approx \frac{v^2}{r}$$

This looks like it should be exact — but we used a geometric approximation ($\sin\theta \approx \theta$ for small angles). The exact relation is $|\Delta\vec{v}| = 2v\sin(\Delta\theta/2)$. Only in the limit $\Delta t \to 0$ does the approximation become equality:

$$|\vec{a}| = \lim_{\Delta t \to 0} \frac{2v\sin(v\Delta t / 2r)}{\Delta t} = \lim_{\Delta t \to 0} \frac{2v \cdot (v\Delta t / 2r)}{\Delta t} = \frac{v^2}{r}$$

**Without the limit, $v^2/r$ is merely an approximation.**

---

## ✅ Resolved Through Limits

### The Exact Derivation

From the geometry of the circle: position $\vec{r}(t) = (r\cos\omega t,\; r\sin\omega t)$ with $\omega = v/r$. Take the change-in-a-blink twice:

$$\vec{v} = \frac{d\vec{r}}{dt} = (-r\omega\sin\omega t,\; r\omega\cos\omega t)$$

$$\vec{a} = \frac{d\vec{v}}{dt} = (-r\omega^2\cos\omega t,\; -r\omega^2\sin\omega t) = -\omega^2\vec{r}$$

Magnitude: $|\vec{a}| = r\omega^2 = r(v/r)^2 = v^2/r$. Direction: always toward the center (the negative sign in $-\omega^2\vec{r}$).

This is exact — no approximations needed. **The limit handled the direction change precisely.**

### The General Decomposition: Tangential + Normal

For *any* curved path (not just circles), acceleration splits into two perpendicular parts:

$$\vec{a} = \frac{dv}{dt}\,\hat{t} + \frac{v^2}{\rho}\,\hat{n}$$

| Component | Cause | Effect |
|:---:|:---|:---|
| $\frac{dv}{dt}\hat{t}$ (tangential) | Change in **speed** | Speeds up or slows down |
| $\frac{v^2}{\rho}\hat{n}$ (normal/centripetal) | Change in **direction** | Curves the path, always toward the inside of the turn |

$\rho$ is the **radius of curvature** — at any point on a curve, you can fit a circle that matches the curve's bend. A sharp turn has small $\rho$ (large centripetal acceleration). A straight line has $\rho = \infty$ (zero centripetal acceleration).

### The Two Components Are Independent

A car can brake while turning: $\frac{dv}{dt} < 0$ (tangential, slowing down) while $\frac{v^2}{\rho} > 0$ (normal, holding the curve). The total acceleration is the vector sum.

---

## 💡 Examples

### Example 1: Uniform Circular Motion

$r = 2\text{ m}$, $v = 4\text{ m/s}$.  Find the centripetal acceleration.

$$a_c = \frac{v^2}{r} = \frac{16}{2} = 8\text{ m/s}^2$$

The direction is toward the center at every instant.  In terms of $g = 10\text{ m/s}^2$: $a_c = 0.8g$.

### Example 2: Car on a Curve

A car takes a turn of radius $100\text{ m}$ at $20\text{ m/s}$ ($72\text{ km/h}$).

$$a_c = \frac{400}{100} = 4\text{ m/s}^2 \approx 0.4g$$

The driver feels pushed sideways with about 40% of their weight.  At $30\text{ m/s}$: $a_c = \frac{900}{100} = 9\text{ m/s}^2 \approx 0.9g$ — near the limit of tire grip.

### Example 3: Radius of Curvature From a Trajectory

$y = x^2$ (a parabola).  At $x = 1$, what is the radius of curvature?  Formula: $\rho = \dfrac{(1 + (y')^2)^{3/2}}{|y''|}$.

$y' = 2x$, $y'' = 2$.  At $x = 1$: $\rho = \dfrac{(1 + 4)^{3/2}}{2} = \dfrac{5\sqrt{5}}{2} \approx 5.59\text{ m}$.

At $x = 0$ (the vertex): $y' = 0$, so $\rho = \dfrac{1^{3/2}}{2} = \frac{1}{2}\text{ m}$ — the tightest bend is at the vertex.

### Example 4: Speed-Up While Turning

$v(t) = 3t$ (linearly increasing speed), $\rho = 9\text{ m}$ (constant radius).

Tangential: $a_t = \frac{dv}{dt} = 3\text{ m/s}^2$.  Normal: $a_n = \frac{v^2}{\rho} = \frac{9t^2}{9} = t^2$.

At $t = 2$: $a_t = 3$, $a_n = 4$, total $a = \sqrt{3^2 + 4^2} = 5\text{ m/s}^2$.

### Example 5: Tangential + Normal Decomposition

$\vec{r}(t) = (t^2,\; t^3)$.  At $t = 1$, find the radius of curvature.

$\vec{v} = (2t,\; 3t^2)$, $\vec{a} = (2,\; 6t)$.  At $t = 1$: $\vec{v} = (2, 3)$, $|\vec{v}| = \sqrt{13}$, $\vec{a} = (2, 6)$.

Tangential component: $a_t = \frac{\vec{v}\cdot\vec{a}}{|\vec{v}|} = \frac{4 + 18}{\sqrt{13}} = \frac{22}{\sqrt{13}}$.

Normal component: $a_n = \sqrt{|\vec{a}|^2 - a_t^2} = \sqrt{40 - \frac{484}{13}} = \sqrt{\frac{36}{13}} = \frac{6}{\sqrt{13}}$.

Then $\rho = \frac{v^2}{a_n} = \frac{13}{6/\sqrt{13}} = \frac{13\sqrt{13}}{6} \approx 7.8\text{ m}$.

### Example 6: Full Acceleration With Both Components

$\vec{r}(t) = (4\cos t,\; 4\sin t,\; 3t)$.  This is a helix — circular in $xy$, rising in $z$.

$\vec{v} = (-4\sin t,\; 4\cos t,\; 3)$, $|\vec{v}| = \sqrt{16 + 9} = 5$ (constant speed!).
$\vec{a} = (-4\cos t,\; -4\sin t,\; 0)$, $|\vec{a}| = 4$.

Since speed is constant, $a_t = 0$.  All acceleration is centripetal: $a_n = 4$.  The radius of curvature: $\rho = \frac{v^2}{a_n} = \frac{25}{4} = 6.25\text{ m}$.

Note: the physical radius of the helix in the $xy$-plane is $4\text{ m}$, but the radius of curvature is larger ($6.25\text{ m}$) because the path also climbs in $z$, making it less sharply curved.

---

## Meaning: "What We Just Did"

Acceleration is the change-in-a-blink of the **velocity vector**, not just the speed. A vector can change in two independent ways: magnitude (tangential) and direction (normal).

With algebra alone, $a_c = v^2/r$ is an approximation from similar triangles. The limit makes it exact. This decomposition of acceleration into tangential and normal components is one of the most powerful tools in mechanics — it turns any curved path into a local circle.

---

## 🔧 Basic Drills *(solutions in `solutions/04-solutions.md`)*

1. $r = 3\text{ m}$, $v = 6\text{ m/s}$.  Find the centripetal acceleration.
2. $r = 50\text{ m}$, $v = 10\text{ m/s}$.  Centripetal acceleration in m/s² and in $g$'s ($g = 10$).
3. $v(t) = 4t$, $\rho = 8\text{ m}$.  Find $a_t$, $a_n$, and total $a$ at $t = 1$.
4. $\vec{r}(t) = (5\cos 2t,\; 5\sin 2t)$.  Find $|\vec{a}|$ and confirm it equals $v^2/r$.
5. A car at constant speed $15\text{ m/s}$ takes a turn. The centripetal acceleration is $4.5\text{ m/s}^2$.  What is the radius?

## 🔥 Advanced Drills *(solutions in `solutions/04-solutions.md`)*

1. A rollercoaster car at the top of a hill (radius $20\text{ m}$) has speed $10\text{ m/s}$.  Find the centripetal acceleration.  If $g=10$, does the car leave the track?
2. A particle moves on $y = \frac{1}{2}x^2$ with constant $x$-speed $v_x = 2\text{ m/s}$.  Find the acceleration vector at $x = 1$.
3. For $\vec{r}(t) = (t,\; t^2,\; t^3)$, find the radius of curvature at $t = 0$.
4. **Trap**: An object moves at constant speed $v$ in a circle of radius $r$.  If the radius doubles but the speed stays the same, what happens to the centripetal acceleration?
5. Derive the formula $a_n = \frac{|\vec{v}\times\vec{a}|}{|\vec{v}|}$ for the normal component of acceleration.  Verify it gives the same answer as Example 5.

## 🧠 Intuitional Drills *(solutions in `solutions/04-solutions.md`)*

1. A car turns left at constant speed. Which way does the driver's body lean, and why?
2. A satellite in a circular orbit has constant speed. Is work being done on it by gravity?
3. A rollercoaster enters a circular loop of radius $10\text{ m}$. At the **top** of the loop, what minimum speed keeps the car on the track?
4. Two identical cars take the same curve. Car A goes at $20\text{ m/s}$, Car B at $40\text{ m/s}$. How many times larger is the centripetal force needed by Car B?
5. A ball on a string is swung in a vertical circle. At which point in the circle is the tension in the string **greatest** — top or bottom?

---

## 📖 Reading Physical Symbols

| Symbol | How to Read It | Physical Meaning |
|:---|:---|:---|
| $\hat{t}$ | "t-hat" | The unit vector **tangent** to the path — points in the direction of motion at each instant. |
| $\hat{n}$ | "n-hat" | The unit vector **normal** to the path — points toward the center of curvature (the "inside" of the turn). |
| $\rho$ | "rho" | **Radius of curvature.** The radius of the circle that best hugs the curve at a given point. Small $\rho$ = sharp turn; $\rho=\infty$ = straight line. |
| $\frac{dv}{dt}$ | "dee-v dee-t" | **Tangential acceleration.** How fast the *speed* is changing. Can be positive (speeding up) or negative (slowing down). |
| $\frac{v^2}{\rho}$ | "v-squared over rho" | **Normal (centripetal) acceleration.** How hard the path is curving. Always points toward the inside of the turn. |
| $\times$ in $\vec{v}\times\vec{a}$ | "cross" | The cross product extracts the perpendicular component. $|\vec{v}\times\vec{a}|/|\vec{v}|$ isolates the part of acceleration that is $\perp$ to velocity. |

**Key habit:** Any curved path can be thought of as a sequence of tangent circles. At each instant, find $\hat{t}$ (where you're going) and $\hat{n}$ (where you're turning toward). Acceleration lives in these two directions.

---

## Glossary
