# 01 — What Is a Vector: A Physical Quantity with Magnitude and Direction

> **Kleppner:** Ch 1.1~1.4 | **Time:** 60 min
> **Core Question:** Why isn't a single number enough for physics?

---

## Scene: How Do You Describe an Airplane's Location?

"The airplane is flying at 500 km/h."

Can you find the airplane with just this information? **No.** You don't know which direction it's going.

"The airplane is flying at 500 km/h **eastward** from Seoul."

Now you can find it. **Physics needs direction.**

---

## ❌ What If You Try With Algebra Alone?

### Attempt 1: Express Everything as a Single Number

The airplane is flying northeast at 500 km/h. Express this as a single number — "500"?

- After 1 hour, you can't know the position. Is it 500 km north? 500 km east? Somewhere in between?

### Attempt 2: Split Into Two Numbers

Northward 353.6 km/h, eastward 353.6 km/h. Using **two numbers**, you can determine the position.

But this is still inconvenient: the single piece of information "northeast 500" has been scattered into two fragments. And if the direction changes, the numbers change too.

### Conclusion: A single number isn't enough. You need a tool that bundles multiple numbers together and handles them as one.

---

## ✅ Resolved With Vectors

### Vector = Magnitude + Direction Bundled Together

$$\vec{v} = (353.6,\; 353.6)\;\text{km/h}$$

What this notation means: **"Every hour, move 353.6 km east and 353.6 km north."**

### The Three Operations on Vectors — Their Physical Meaning

| Operation | Formula | Physical Scene |
|:---:|:---:|:---|
| **Addition** | $\vec{a}+\vec{b}$ | "First go by $\vec{a}$, then from there go by $\vec{b}$." — pathfinding |
| **Dot Product** | $\vec{a}\cdot\vec{b}=ab\cos\theta$ | "How much does $\vec{a}$ contribute in the direction of $\vec{b}$." — **the length of a shadow.** Work is maximized when force and displacement share the same direction. |
| **Cross Product** | $\vec{a}\times\vec{b}=ab\sin\theta\,\hat{n}$ | "The parallelogram formed by $\vec{a}$ and $\vec{b}$." Direction given by the right-hand rule. — The root of **rotational effects.** The origin of torque and angular momentum. |

### Scalar vs. Vector

- **Scalar**: A single number suffices. Mass (5 kg), temperature (300 K), time (3 s).
- **Vector**: Needs a direction attached to the number to have meaning. Position, velocity, acceleration, force.
- Why? **Because space is three-dimensional.** Every point in space is described only by "how far from the origin, and in which direction."

---

## 💡 Examples — Thinking With Vectors

### Example 1: Airplane on a Windy Day

An airplane flies north at 200 km/h. Wind blows east at 50 km/h. What is the airplane's actual velocity?

$$\vec{v}_{\text{actual}} = \vec{v}_{\text{plane}} + \vec{v}_{\text{wind}} = (0, 200) + (50, 0) = (50, 200)$$

Magnitude: $\sqrt{50^2 + 200^2} = \sqrt{2500 + 40000} = \sqrt{42500} \approx 206.2\text{ km/h}$
Direction: $\tan^{-1}(50/200) \approx 14.0^\circ$ — tilted about 14° east of north.

### Example 2: Resolving a Force Into Components

A 10 N force makes a 30° angle with the $x$-axis:

$$F_x = 10\cos 30^\circ = 10 \times \frac{\sqrt{3}}{2} \approx 8.66\text{ N}$$
$$F_y = 10\sin 30^\circ = 10 \times \frac{1}{2} = 5.00\text{ N}$$

### Example 3: Net Force From Two Forces

$\vec{F}_1 = (3, 4)\text{ N}$, $\vec{F}_2 = (-1, 2)\text{ N}$

$$\vec{F}_{\text{net}} = (3-1,\; 4+2) = (2, 6)\text{ N}$$

Magnitude: $\sqrt{4 + 36} = \sqrt{40} \approx 6.32\text{ N}$

### Example 4: Meaning of the Dot Product — Work

A 5 N force moves an object 10 m at a 60° angle to the force. How much work is done?

$$W = \vec{F}\cdot\vec{s} = 5 \times 10 \times \cos 60^\circ = 50 \times \frac{1}{2} = 25\text{ J}$$

If force and displacement were aligned (0°): $W = 50 \times 1 = 50\text{ J}$ — maximum.
If they were perpendicular (90°): $W = 50 \times 0 = 0\text{ J}$ — no work at all.

**The dot product measures "how aligned two directions are."**

### Example 5: Meaning of the Cross Product — Torque

Apply a 20 N force perpendicular to a wrench at a distance of 0.3 m.

$$\tau = rF\sin 90^\circ = 0.3 \times 20 \times 1 = 6\text{ N·m}$$

If you push along the wrench ($\theta=0^\circ$): $\tau = 0$ — it doesn't turn at all.
**The cross product measures "how much twisting is attempted."**

### Example 6: Unit Vectors

$\hat{i} = (1,0,0)$, $\hat{j} = (0,1,0)$, $\hat{k} = (0,0,1)$

Any vector can be expressed as a combination of these three: $\vec{v} = 3\hat{i} + 4\hat{j} - 2\hat{k}$

---

## Meaning: "What We Just Did"

Every physical phenomenon in space is described using vectors. Without vectors, you cannot:
- Decompose projectile motion into components
- State the direction of centripetal acceleration in circular motion
- Express the direction of a force

**Vectors are the mathematical translation of the simple fact that "space has direction."**
Vector operations themselves are algebraic, but the real story unfolds starting next session, when we introduce the **change-in-a-blink of a vector.**

---

## 🔧 Basic Drills *(solutions in `solutions/01-solutions.md`)*

1. $\vec{a}=(3, -2, 5)$, $\vec{b}=(-1, 4, 2)$. Find the magnitude of $\vec{a}+\vec{b}$.
2. A 15 N force makes a 45° angle with the $x$-axis. Find its $x$ and $y$ components.
3. $\vec{F}_1=(5,0)\text{ N}$, $\vec{F}_2=(3,4)\text{ N}$. Find the magnitude and direction of the net force.
4. $\vec{a}=(2,3)$, $\vec{b}=(4,-1)$. Find the dot product. Is the angle between them greater or less than 90°?
5. $\vec{r}=(0, 2, 0)\text{ m}$, $\vec{F}=(3, 0, 0)\text{ N}$. Find the magnitude and direction of the torque $\vec{\tau}=\vec{r}\times\vec{F}$.

## 🔥 Advanced Drills *(solutions in `solutions/01-solutions.md`)*

1. Wind blows northwest at 15 m/s. An airplane flies north at 80 m/s. Find the magnitude and direction of the actual velocity.
2. Find a unit vector perpendicular to both $\vec{a}=(2, -1, 3)$ and $\vec{b}=(1, 2, -1)$.
3. A force $\vec{F}=(2,3)\text{ N}$ acts through displacement $\vec{s}=(4,1)\text{ m}$. How much work is done? How much does this force contribute in the direction $\vec{n}=(-3,2)\text{ N}$?
4. A river flows east at 3 m/s. A boat moves north at 4 m/s relative to the water. What is the boat's velocity relative to the ground? If the river is 100 m wide, how many seconds to cross?
5. Find a unit vector in the direction of $\vec{a}=(1,2,2)$. Find the angle between this vector and $\vec{b}=(2,-1,2)$.

## 🧠 Intuitional Drills *(solutions in `solutions/01-solutions.md`)*

1. Two equal-magnitude forces $\vec{F}_1$ and $\vec{F}_2$ act at an angle of $120^\circ$. The magnitude of each is $10\text{ N}$. What is the magnitude of the net force?
2. A force $\vec{F} = (6, 8)\text{ N}$ acts on a box. At what angle should the box be pushed so that only half the maximum possible work is done per meter of displacement?
3. A boat heads straight north at $4\text{ m/s}$ across a river flowing east at $3\text{ m/s}$. Without calculating: is the boat's ground speed greater than, less than, or equal to $5\text{ m/s}$?
4. Three forces $\vec{F}_1, \vec{F}_2, \vec{F}_3$ act on a point and the net force is zero. If $\vec{F}_1 = (5,0)$ and $\vec{F}_2 = (-3,4)$, find $\vec{F}_3$ using geometry — no equations, just draw and close the triangle.
5. $\vec{a} \cdot \vec{b} = 0$. What can you say about the angle? $\vec{a} \times \vec{b} = 0$. What can you say?

---

## 📖 Reading Physical Symbols

This session introduced symbols that appear throughout mechanics. Here is how to *read* them — not just compute with them.

| Symbol | How to Read It | Physical Meaning |
|:---|:---|:---|
| $\vec{a}$ | "vector a" | A quantity with **direction** attached. Not just a number — an arrow in space. |
| $\vec{a}+\vec{b}$ | "a plus b" | "Go along $\vec{a}$, then from there go along $\vec{b}$." The diagonal of the parallelogram. |
| $\vec{a}\cdot\vec{b}$ | "a dot b" | "How much of $\vec{a}$ points in the direction of $\vec{b}$." The **shadow** length times $|\vec{b}|$. Zero means they are perpendicular. |
| $\vec{a}\times\vec{b}$ | "a cross b" | "The area of the parallelogram spanned by $\vec{a}$ and $\vec{b}$, with a direction given by the right-hand rule." Zero means they are parallel. |
| $|\vec{a}|$ | "magnitude of a" | The **length** of the arrow. Always a positive number (or zero). |
| $\hat{i}, \hat{j}, \hat{k}$ | "i-hat, j-hat, k-hat" | The three **reference arrows** pointing along the $x$, $y$, $z$ axes, each of length 1. Any vector is built from these. |
| $\hat{n}$ | "n-hat" | A unit vector (length 1) in some direction of interest — often the result of a cross product. |
| $\perp$ | "perpendicular to" | Two things are at right angles. Critical for normal forces (always $\perp$ to surfaces). |
| $\parallel$ | "parallel to" | Two things point in the same (or opposite) direction. Friction is always $\parallel$ to the contact surface. |

**Key habit:** Every time you see a vector symbol, picture an arrow in space. Before calculating, ask: "Which way does it point? How long is it?"

---

## Glossary

- **Scalar**: A quantity with magnitude only (mass, temperature, time)
- **Vector**: A quantity with both magnitude and direction (position, velocity, force)
- **Unit vectors** $\hat{i},\hat{j},\hat{k}$: Reference direction vectors of length 1
- **Dot product** $\vec{a}\cdot\vec{b}$: The product of magnitudes × directional alignment. Result is a scalar.
- **Cross product** $\vec{a}\times\vec{b}$: The area and perpendicular direction formed by two vectors. Result is a vector.

