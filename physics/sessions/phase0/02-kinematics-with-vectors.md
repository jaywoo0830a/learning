# 02 — Position, Velocity, Acceleration as Vectors: The Story of Motion

> **Kleppner:** Ch 1.5~1.7 | **Time:** 70 min
> **Core Question:** How do we extend the 1D idea "change-in-a-blink = velocity" into three dimensions?

---

## Scene: A Drone Tracing a Curve Through the Sky

A drone flies in a figure-eight pattern. Its position changes every instant, and the direction of its velocity changes too.

How do we capture this motion in a single equation?

---

## ❌ What If You Try With Algebra Alone?

### Why Must We Wrestle With This?

Nature changes ceaselessly. Velocity changes at every instant, and the change itself changes too. But the mathematics we know (algebra) can only handle **fixed values.**

"Average velocity" crushes an entire interval into a single number. But real physics asks: **"Right at this instant, how fast is it moving?"** To answer this question, you need a way of thinking that captures change *as* it changes. That is the change-in-a-blink.

### Attempt: Split the Interval Finer and Finer

Suppose a drone's position is given by $\vec{r}(t) = (t^2,\; t^3)$. We want the **instantaneous velocity** at $t=2$ seconds.

Pick clean fractions of a second: $1$, $\frac{1}{2}$, $\frac{1}{4}$, $\frac{1}{8}$, $\frac{1}{16}$.

**Interval = 1:**  from $t=2$ to $t=3$

$$\vec{r}(3) = (3^2,\; 3^3) = (9,\; 27)$$
$$\vec{v}_{\text{rough}} = \frac{(9, 27) - (4, 8)}{1} = \left(\frac{5}{1},\; \frac{19}{1}\right) = (5,\; 19)$$

**Interval = $\frac{1}{2}$:**  from $t=2$ to $t = 2 + \frac{1}{2} = \frac{5}{2}$

$$\vec{r}\!\left(\frac{5}{2}\right) = \left(\frac{25}{4},\; \frac{125}{8}\right)$$
$$\vec{v} = \frac{\left(\frac{25}{4}, \frac{125}{8}\right) - \left(4,\; 8\right)}{1/2} = \frac{\left(\frac{9}{4},\; \frac{61}{8}\right)}{1/2} = \left(\frac{9}{2},\; \frac{61}{4}\right) = (4.5,\; 15.25)$$

**Interval = $\frac{1}{4}$:**  from $t=2$ to $t = 2 + \frac{1}{4} = \frac{9}{4}$

$$\vec{r}\!\left(\frac{9}{4}\right) = \left(\frac{81}{16},\; \frac{729}{64}\right)$$
$$\vec{v} = \frac{\left(\frac{81}{16}, \frac{729}{64}\right) - \left(\frac{64}{16},\; \frac{512}{64}\right)}{1/4} = \frac{\left(\frac{17}{16},\; \frac{217}{64}\right)}{1/4} = \left(\frac{17}{4},\; \frac{217}{16}\right) = (4.25,\; 13.5625)$$

**Interval = $\frac{1}{8}$:**  from $t=2$ to $t = 2 + \frac{1}{8} = \frac{17}{8}$

After similar algebra (try it yourself!): $\vec{v} \approx (4.125,\; 12.7656)$

**Interval = $\frac{1}{16}$:**  from $t=2$ to $t = 2 + \frac{1}{16} = \frac{33}{16}$

After similar algebra: $\vec{v} \approx (4.0625,\; 12.3789)$

| Interval | Approximate $\vec{v}$ | Distance from $(4, 12)$ |
|:---:|:---|:---|
| $1$ | $(5,\; 19)$ | $(1,\; 7)$ |
| $1/2$ | $(4.5,\; 15.25)$ | $(0.5,\; 3.25)$ |
| $1/4$ | $(4.25,\; 13.56)$ | $(0.25,\; 1.56)$ |
| $1/8$ | $(4.125,\; 12.77)$ | $(0.125,\; 0.77)$ |
| $1/16$ | $(4.0625,\; 12.38)$ | $(0.0625,\; 0.38)$ |

The pattern is clear: each time we **halve** the interval, the error is roughly halved too. But — critically — **the error never reaches zero.** With any finite interval, you can only get closer. To hit $(4,12)$ exactly, you need a leap: **erase the interval entirely.** That leap is the limit.

---

## ✅ Resolved Through Limits

### From Approximation to Exact: The Leap

The table shows a sequence approaching $(4, 12)$. Now ask: **"If the interval becomes zero, what value does the sequence reach?"**

That question is the limit. Writing it formally:

$$\vec{v}(t) = \lim_{\Delta t \to 0} \frac{\vec{r}(t+\Delta t) - \vec{r}(t)}{\Delta t} = \frac{d\vec{r}}{dt}$$

Now, instead of computing endlessly, we use the **rule for change-in-a-blink** that we already know. For $\vec{r}(t) = (t^2,\; t^3)$:

The $x$-component: $x(t)=t^2$. Its rate of change at any $t$ is $2t$. Why? We can verify algebraically:

$$\frac{(t+\Delta t)^2 - t^2}{\Delta t} = \frac{t^2 + 2t\Delta t + (\Delta t)^2 - t^2}{\Delta t} = \frac{2t\Delta t + (\Delta t)^2}{\Delta t} = 2t + \Delta t \xrightarrow{\Delta t \to 0} 2t$$

The $y$-component: $y(t)=t^3$. Expanding:

$$\frac{(t+\Delta t)^3 - t^3}{\Delta t} = \frac{3t^2\Delta t + 3t(\Delta t)^2 + (\Delta t)^3}{\Delta t} = 3t^2 + 3t\Delta t + (\Delta t)^2 \xrightarrow{\Delta t \to 0} 3t^2$$

So the rule is: $\frac{d}{dt}(t^2,\; t^3) = (2t,\; 3t^2)$.

At $t=2$: $\vec{v} = (4,\; 12)$ — **clean, exact, arrived at in one step.**

### What This Means

**Nature speaks in "change-in-a-blink."** The rules we learned — $x'(t)=2t$, $\frac{d}{dt}t^3=3t^2$ — are not arbitrary formulas. They are the result of asking: "What happens when the interval truly vanishes?" Each rule is the fingerprint of that limit.

### Each Axis Is Independent

$$\vec{v} = \frac{d\vec{r}}{dt} = \left(\frac{dx}{dt},\; \frac{dy}{dt},\; \frac{dz}{dt}\right)$$

- $x$-direction: only $x(t)$ matters. $y$-direction: only $y(t)$ matters.
- **In a horizontal throw: horizontal is constant velocity, vertical is free-fall — completely independent.**
- Acceleration: $\vec{a} = \frac{d\vec{v}}{dt} = \left(\frac{d^2x}{dt^2},\; \frac{d^2y}{dt^2},\; \frac{d^2z}{dt^2}\right)$

---

## 💡 Examples — Reading Motion Through Change-in-a-Blink

### Example 1: Uniform Straight-Line Motion

$\vec{r}(t) = (3t, 4t)$ → $\vec{v} = (3, 4)$, $\vec{a} = (0, 0)$
"Every second: 3 m in $x$, 4 m in $y$, unchanged. No acceleration whatsoever."

### Example 2: Constant-Acceleration Motion

$\vec{r}(t) = (2t, 5t - 5t^2)$ → $\vec{v} = (2, 5 - 10t)$, $\vec{a} = (0, -10)$
"Horizontal: constant 2 m/s. Vertical: accelerating downward at 10 m/s². Projectile motion!"  (Using $g=10$ for simplicity.)

### Example 3: Circular Motion

$\vec{r}(t) = (R\cos\omega t, R\sin\omega t)$ → $\vec{v} = (-R\omega\sin\omega t, R\omega\cos\omega t)$ → $\vec{a} = (-R\omega^2\cos\omega t, -R\omega^2\sin\omega t) = -\omega^2\vec{r}$

"The velocity vector leads the position vector by 90°. Acceleration always points toward the center."

### Example 4: Helical Motion

$\vec{r}(t) = (\cos t, \sin t, t)$ → $\vec{v} = (-\sin t, \cos t, 1)$ → $\vec{a} = (-\cos t, -\sin t, 0)$
"Circular motion in the $xy$-plane, steady climb in $z$. Acceleration is purely centripetal."

### Example 5: Detecting Rest via Change-in-a-Blink

$\vec{r}(t) = (t^3 - 3t, t^2 - 2t)$ → $\vec{v} = (3t^2 - 3, 2t - 2)$
At $t=1$: $\vec{v} = (0, 0)$ — momentarily at rest!
But $\vec{a} = (6t, 2) = (6, 2)$ — acceleration is still present. It will start moving again immediately.

### Example 6: Reconstructing a Trajectory From Initial Conditions

$\vec{a} = (0, -10)$, $\vec{v}_0 = (20, 30)$, $\vec{r}_0 = (0, 0)$
→ $\vec{v}(t) = (20, 30 - 10t)$
→ $\vec{r}(t) = (20t, 30t - 5t^2)$
"Gather the change-in-a-blink of velocity and position is restored. The path is open in the reverse direction too."

---

## Meaning: "What We Just Did"

When the 1D concept "change-in-a-blink = velocity, change-in-a-blink of velocity = acceleration" extends to 3D, the fact that **each axis is independent** makes everything simple.

With algebra alone, you can only forever approximate the instantaneous velocity of $\vec{r}(t)=(t^2, t^3)$. The moment you introduce the limit $\Delta t \to 0$, the exact value $(4, 12)$ emerges in one stroke.

**"Capturing the change-in-a-blink — this is the first letter of the language that describes motion."**

---

## 🔧 Basic Drills *(solutions in `solutions/02-solutions.md`)*

1. For $\vec{r}(t) = (4t, 3t^2)$, find velocity and acceleration at $t=2$.
2. For $\vec{r}(t) = (5\cos 2t, 5\sin 2t)$, is the magnitude of velocity constant? What is the direction of acceleration?
3. Given $\vec{v}(t) = (6t, 8)$ and $\vec{r}(0)=(0,0)$, find $\vec{r}(3)$.
4. Given $\vec{a} = (0, -10)$, $\vec{v}_0=(10, 20)$, $\vec{r}_0=(0, 30)$, find $\vec{r}(t)$.
5. For $\vec{r}(t)=(t^2, t^3-t)$, find the time $t$ when the object is momentarily at rest.

## 🔥 Advanced Drills *(solutions in `solutions/02-solutions.md`)*

1. For $\vec{r}(t) = (e^t\cos t, e^t\sin t)$, find velocity and acceleration. What shape is this motion?
2. For $\vec{r}(t) = (t\cos t, t\sin t)$, find the speed $|\vec{v}|$ at $t=2\pi$.
3. Projectile motion: $\vec{r}(t) = (v_0\cos\theta\cdot t,\; v_0\sin\theta\cdot t - \frac{1}{2}gt^2)$. Find $\vec{v}(t)$ and $\vec{a}(t)$, and prove that $|\vec{v}|$ is minimized at the peak.
4. Given $\vec{a}(t) = (\cos t, -\sin t, 1)$, $\vec{v}(0)=(1,0,0)$, $\vec{r}(0)=(0,1,0)$, find $\vec{r}(t)$. (Warning: two rounds of the reverse of change-in-a-blink.)
5. **Trap**: For $\vec{r}(t) = (t^2, t^4)$, at what $t$ does $|\vec{v}|$ become zero? And at that instant, is the acceleration zero?

## 🧠 Intuitional Drills *(solutions in `solutions/02-solutions.md`)*

1. A particle's acceleration vector is **always perpendicular** to its velocity vector. What can you conclude about the speed?
2. A particle is at its **maximum height** in projectile motion. At this instant, is its acceleration zero? If not, what is it?
3. Two identical balls are launched from a cliff: one is dropped straight down, the other is fired horizontally. Which hits the ground first?
4. A particle moves with $\vec{v}(t) = (3, 4)$ and starts at $\vec{r}(0) = (0, 0)$. What is the shape of its path?
5. A particle starts from rest with $\vec{a} = (2, 0)$ for $t=0$ to $t=3$, then $\vec{a} = (0, -2)$ for $t=3$ to $t=6$. Sketch the path. What shape is it?

---

## 📖 Reading Physical Symbols

| Symbol | How to Read It | Physical Meaning |
|:---|:---|:---|
| $d\vec{r}/dt$ | "dee-r dee-t" | **Change-in-a-blink.** How much $\vec{r}$ changes in an infinitely small interval of time. The core idea of all kinematics. |
| $\vec{v}(t)$ | "v of t" | Velocity at time $t$. A **function**: its value changes as $t$ changes. |
| $\vec{a}(t)$ | "a of t" | Acceleration at time $t$. The change-in-a-blink of the change-in-a-blink of position. |
| $\lim_{\Delta t\to 0}$ | "limit as delta-t goes to zero" | The operation that **erases the interval.** What remains is the exact instantaneous value. |
| $\vec{r}_0, \vec{v}_0$ | "r-nought, v-nought" | Initial conditions — where the object starts and how fast it's moving at $t=0$. Without these, the future is not uniquely determined. |
| $x(t), y(t), z(t)$ | "x of t, y of t, z of t" | The three **independent** stories of motion. Each axis evolves on its own. |

**Key habit:** When you see $d\vec{r}/dt$, don't just compute — visualize the arrow $\vec{r}$ getting a tiny nudge at its tip. That nudge *is* the velocity.

---

## Glossary
