# 03 — Free Fall and Projectile Motion: The Simplest 2D Motion

> **Kleppner:** Ch 1.7 | **Time:** 60 min
> **Core Question:** In a world with only gravity, how does everything move?

---

## Scene: The Trajectory of a Cannonball

A cannon is fired from a fortress wall. With the same speed at different angles, it travels farthest at **45°.** Why?

Also, in the absence of air resistance, the cannonball traces a perfect parabola. Where does this parabola come from?

---

## ❌ What If You Try With Algebra Alone?

### Why Must We Wrestle With This?

We know one fact: $a_y = -g$ (the change-in-a-blink of vertical velocity is constant and downward). But the moment we ask **"So what's the position?"** we hit a wall.

Acceleration is the rate at which velocity changes. Velocity is the rate at which position changes. To go from acceleration all the way to position, you must **accumulate change twice.** The tool for accumulating change is split-and-gather. Algebra has no such tool — it can only handle *fixed* values.

### Attempt 1: Guess With Common Sense

"Gravity pulls downward... so it'll go up, then fall."  True, but **how high? When? Where does it land?**  You can't give numbers.

### Attempt 2: Calculate in Chunks (And See It Fail)

Let $g = 10\text{ m/s}^2$.  Launch: $v_0 = 30\text{ m/s}$ at $\theta = 30^\circ$.

Vertical initial speed: $v_{0y} = 30 \cdot \frac{1}{2} = 15\text{ m/s}$

"Each second, speed drops by 10..."

| Time $t$ | $v_y$ (chunk guess) | Actual $v_y = 15 - 10t$ |
|:---:|:---:|:---:|
| 0 | 15 | 15 |
| 1 | 5 | 5 |
| 2 | $-5$ | $-5$ |
| 3 | $-15$ | $-15$ |

The velocities match — because $a$ is constant! But now try **displacement:**

"Move 15 m in the 1st second, 5 m in the 2nd, $-5$ in the 3rd..."

$$15 + 5 + (-5) + (-15) = 0\text{ m}$$

**Zero?** That would mean it landed right back at launch height after 4 seconds — but the real flight time is only 3 seconds ($t_f = 2v_{0y}/g = 3$). The chunk method completely fails because **it uses the velocity at the start of each chunk, ignoring that velocity changes *within* the chunk.**

The exact peak height comes from $v_y=0$ at $t = \frac{3}{2}$:

$$y_{\text{max}} = 15 \cdot \frac{3}{2} - 5 \cdot \left(\frac{3}{2}\right)^{\!2} = \frac{45}{2} - \frac{45}{4} = \frac{45}{4}$$

**When velocity changes continuously, only split-and-gather gives the exact answer.**

---

## ✅ Resolved Through Split-and-Gather

### Step-by-Step: From Acceleration to Velocity

We start with the change-in-a-blink equation:

$$\frac{dv_y}{dt} = -g$$

This says: "at every instant, $v_y$ drops by $g$."  To recover $v_y(t)$ from this, we **gather** all those instant-changes from time $0$ to time $t$:

$$
\begin{aligned}
\int_0^t \frac{dv_y}{dt'}\,dt' &= \int_0^t (-g)\,dt' \\[4pt]
v_y(t) - v_y(0) &= \big[-g \cdot t'\big]_{0}^{t} = -gt \\[4pt]
v_y(t) &= v_{0y} - gt
\end{aligned}
$$

The integration of a constant: $\int_0^t (-g)\,dt' = -g \cdot t$ — the area of a rectangle of height $-g$ and width $t$.

### Step-by-Step: From Velocity to Position

Now $v_y(t) = v_{0y} - gt$ tells us the speed at each instant.  To get position, we gather the displacements from all those instants:

$$
\begin{aligned}
\frac{dy}{dt} &= v_y(t) = v_{0y} - gt \\[4pt]
\int_0^t \frac{dy}{dt'}\,dt' &= \int_0^t (v_{0y} - gt')\,dt' \\[4pt]
y(t) - y(0) &= \left[v_{0y}t' - \frac{1}{2}gt'^{\,2}\right]_{0}^{t} = v_{0y}t - \frac{1}{2}gt^2 \\[4pt]
y(t) &= y_0 + v_{0y}t - \frac{1}{2}gt^2
\end{aligned}
$$

**Where the $\frac{1}{2}$ comes from:**  The term $\int_0^t gt'\,dt' = g \cdot \frac{1}{2}t^2$.  The integral of a linearly-growing quantity $gt'$ is a triangle of area $\frac{1}{2} \cdot \text{base} \cdot \text{height} = \frac{1}{2} \cdot t \cdot gt = \frac{1}{2}gt^2$.  The factor $\frac{1}{2}$ is the geometry of accumulation — it is **not** something you could guess with algebra.

### The Horizontal Story (Trivial Because $a_x = 0$)

$$\frac{dv_x}{dt} = 0 \;\Rightarrow\; v_x(t) = v_{0x} \;\Rightarrow\; x(t) = x_0 + v_{0x}t$$

### The Complete Trajectory

Combining both axes with initial position $(0,0)$ and launch angle $\theta$:

$$
\begin{aligned}
x(t) &= v_0\cos\theta \cdot t \\[4pt]
y(t) &= v_0\sin\theta \cdot t - \frac{1}{2}gt^2
\end{aligned}
$$

**Time of flight:**  Set $y=0$:

$$v_0\sin\theta \cdot t - \frac{1}{2}gt^2 = 0 \;\Rightarrow\; t\left(v_0\sin\theta - \frac{1}{2}gt\right) = 0 \;\Rightarrow\; t=0 \text{ or } t = \frac{2v_0\sin\theta}{g}$$

**Range:**  Substitute $t_f$ into $x(t)$:

$$R = v_0\cos\theta \cdot \frac{2v_0\sin\theta}{g} = \frac{v_0^2 \cdot 2\sin\theta\cos\theta}{g} = \frac{v_0^2\sin 2\theta}{g}$$

Since $\sin 2\theta \leq 1$, the maximum range is $v_0^2/g$, achieved at $2\theta = 90^\circ \Rightarrow \theta = 45^\circ$.

**Peak height:**  Set $v_y=0$:

$$v_0\sin\theta - gt_{\text{top}} = 0 \;\Rightarrow\; t_{\text{top}} = \frac{v_0\sin\theta}{g}$$
$$y_{\text{max}} = v_0\sin\theta \cdot \frac{v_0\sin\theta}{g} - \frac{1}{2}g\!\left(\frac{v_0\sin\theta}{g}\right)^{\!2} = \frac{v_0^2\sin^2\theta}{2g}$$

---

## 💡 Examples — Reading Projectile Motion

### Example 1: Basic Parabola

$v_0 = 20\text{ m/s}$, $\theta = 30^\circ$, $g = 10\text{ m/s}^2$

- $v_{0x} = 20\cos 30^\circ = 10\sqrt{3}\text{ m/s}$ (exact), $v_{0y} = 20 \cdot \frac{1}{2} = 10\text{ m/s}$
- Flight time: $t_f = \frac{2 \cdot 10}{10} = 2\text{ s}$
- Range: $R = 10\sqrt{3} \cdot 2 = 20\sqrt{3}\text{ m}$ (exact; $\approx 34.6\text{ m}$)
- Peak: $t_{\text{top}} = \frac{10}{10} = 1\text{ s}$, $y_{\text{max}} = \frac{10^2}{20} = \frac{100}{20} = 5\text{ m}$

### Example 2: Horizontal Launch From a Cliff

Cliff height 100 m, launch horizontal at 30 m/s. $g = 10$.

- Vertical: $100 = \frac{1}{2} \cdot 10 \cdot t^2$ → $t^2 = 20$ → $t = \sqrt{20} = 2\sqrt{5}\text{ s}$ (exact; $\approx 4.47\text{ s}$)
- Horizontal: $x = 30 \cdot 2\sqrt{5} = 60\sqrt{5}\text{ m}$ (exact; $\approx 134\text{ m}$)

### Example 3: Maximum Range Angle

$v_0 = 50\text{ m/s}$, $g = 10$. $R = \frac{2500}{10}\sin 2\theta = 250\sin 2\theta$.

- $\theta = 45^\circ$: $R = 250 \cdot 1 = 250\text{ m}$ (maximum)
- $\theta = 30^\circ$: $R = 250 \cdot \frac{\sqrt{3}}{2} = 125\sqrt{3}\text{ m}$ (exact; $\approx 216.5\text{ m}$)
- $\theta = 60^\circ$: same as 30° because $\sin 120^\circ = \sin 60^\circ = \frac{\sqrt{3}}{2}$

### Example 4: Firing From an Elevated Position

Height $h = 50\text{ m}$, $v_0 = 30\text{ m/s}$, $\theta = 30^\circ$, $g = 10$.

$v_{0y} = 30 \cdot \frac{1}{2} = 15$, $v_{0x} = 30 \cdot \frac{\sqrt{3}}{2} = 15\sqrt{3}$

$y(t) = 50 + 15t - 5t^2 = 0$ → divide by 5: $10 + 3t - t^2 = 0$ → $t^2 - 3t - 10 = 0$ → $(t-5)(t+2)=0$ → $t=5\text{ s}$

Range: $x = 15\sqrt{3} \cdot 5 = 75\sqrt{3}\text{ m}$ (exact; $\approx 130\text{ m}$)

### Example 5: Two Angles Giving the Same Range

$v_0 = 40\text{ m/s}$, $g = 10$. To achieve $R = 120\text{ m}$:

$\frac{1600}{10}\sin 2\theta = 120$ → $160\sin 2\theta = 120$ → $\sin 2\theta = \frac{3}{4}$

$2\theta = \arcsin\!\left(\frac{3}{4}\right)$ or $180^\circ - \arcsin\!\left(\frac{3}{4}\right)$ → $\theta \approx 24.3^\circ$ or $65.7^\circ$

**The two angles always sum to exactly 90°.**

### Example 6: Trajectory Equation — $y$ as a Function of $x$

From $x = v_0\cos\theta \cdot t$, we have $t = \dfrac{x}{v_0\cos\theta}$.  Substitute into $y(t)$:

$$
\begin{aligned}
y &= v_0\sin\theta \cdot \frac{x}{v_0\cos\theta} - \frac{1}{2}g\!\left(\frac{x}{v_0\cos\theta}\right)^{\!2} \\[4pt]
  &= x\tan\theta - \frac{g}{2v_0^2\cos^2\theta}\,x^2
\end{aligned}
$$

This is $y = Ax - Bx^2$ with $B > 0$ — a downward-opening parabola through the origin.

---

## Meaning: "What We Just Did"

All formulas for constant-acceleration motion arise from **a single fact: the acceleration is constant.**

$$a = \text{constant} \;\xrightarrow{\text{split-and-gather}}\; v(t) \;\xrightarrow{\text{split-and-gather}}\; x(t)$$

With algebra alone, you can never explain **why the $\frac{1}{2}$** appears in $x = v_0t + \frac{1}{2}at^2$. You just have to memorize it.

But with split-and-gather, you know: splitting-and-gathering $at$ through time yields $\frac{1}{2}at^2$. **The $\frac{1}{2}$ is the fingerprint left by split-and-gather.**

---

## 🔧 Basic Drills *(solutions in `solutions/03-solutions.md`)*

1. $v_0 = 30\text{ m/s}$, $\theta = 60^\circ$, $g = 10$. Find flight time, range, and peak height.
2. An 80 m cliff, launched horizontally at 25 m/s. $g = 10$. Find time to impact and horizontal distance.
3. $v_0 = 20$, $\theta = 45^\circ$, $g = 10$. Find the range. Compare with $\theta = 30^\circ$.
4. $y(t) = 40t - 5t^2$. What is the physical meaning of the two instants when $y=0$?
5. $\vec{r}(t) = (10t,\; 20t - 5t^2)$. Find the magnitude of initial velocity and the launch angle. (Using $g=10$.)

## 🔥 Advanced Drills *(solutions in `solutions/03-solutions.md`)*

1. Prove that the range is exactly 4 times the maximum height.
2. Explain why angles above and below 45° give the same range, using $\sin 2\theta = \sin(180^\circ-2\theta)$.
3. A parabola is given by $y(x) = x - \frac{1}{20}x^2$. Find $v_0$ and $\theta$. ($g = 10$)
4. **Trap**: $v_0 = 20$, $\theta = 90^\circ$. What is the range? The formula gives 0 — what is the physically meaningful reason?
5. A projectile is fired horizontally with speed $v_0$ onto an incline of angle $\alpha$. Find the flight time until it hits the incline.

## 🧠 Intuitional Drills *(solutions in `solutions/03-solutions.md`)*

1. A ball is thrown at $30^\circ$ and another at $60^\circ$, both at the same speed. Which is in the air longer? Which goes higher?
2. Mid-flight, gravity suddenly doubles ($g \to 2g$). Does the range increase, decrease, or stay the same? What about the flight time?
3. A projectile is launched from ground level. At the **exact midpoint** of its flight time, what fraction of the total range has it covered?
4. A basketball player shoots from a height of $2\text{ m}$ with the hoop at $3\text{ m}$ and $5\text{ m}$ away horizontally. Is $45^\circ$ still the optimal launch angle for the minimum required speed?
5. On the Moon ($g_{\text{moon}} = g/6$), a golf ball is hit at $45^\circ$ with the same speed as on Earth. How many times farther does it go?

---

## 📖 Reading Physical Symbols

| Symbol | How to Read It | Physical Meaning |
|:---|:---|:---|
| $\int_a^b f(t)\,dt$ | "integral from a to b of f of t dee-t" | **Split-and-gather.** Chop the interval $[a,b]$ into infinitely many pieces, multiply each piece's value $f(t)$ by its width $dt$, and gather them all. The result is the total accumulated quantity. |
| $\int_0^t (-g)\,dt'$ | "integral from 0 to t of minus-g dee-t-prime" | "Gather all the tiny downward speed-changes from time 0 to time $t$." The $t'$ is a dummy variable — it sweeps through all instants. |
| $\big[F(t)\big]_0^t$ | "F of t evaluated from 0 to t" | Shorthand for $F(t)-F(0)$. The net change accumulated between the two limits. |
| $v_{0x}, v_{0y}$ | "v-zero-x, v-zero-y" | The velocity components at $t=0$. The **starting conditions** that determine the entire trajectory. |
| $\theta$ | "theta" | The launch angle measured from the horizontal. $\theta=0^\circ$ is purely horizontal; $\theta=90^\circ$ is straight up. |
| $\propto$ | "is proportional to" | "Scales directly with." $R \propto v_0^2$ means if you double the speed, the range quadruples. |

**Key habit:** When you see $\int_a^b$, picture the area under a graph. The physical meaning is always: **"How much total stuff accumulated between here and there?"**

---

## Glossary
