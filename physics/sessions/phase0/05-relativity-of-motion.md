# 05 — Relativity of Motion: Who Is Watching?

> **Kleppner:** Ch 1.11 | **Time:** 50 min
> **Core Question:** Is "motion" absolute — or does it depend on who is asking?

---

## Scene: Throwing a Ball Inside a Moving Train

You're on a train moving at a steady $30\text{ m/s}$. You toss a ball straight up. To you, the ball goes straight up and comes straight back down into your hand.

Someone standing on the platform watches through the window. To them, the ball traces a **parabola** — it moves forward with the train while rising and falling.

Same ball. Same motion. Two completely different trajectories. Who is right?

**Both.** Motion is not absolute — it depends on the reference frame of the observer.

---

## ❌ What If You Try With Algebra Alone?

### The Trap of "Absolute Motion"

If you believe motion is absolute, you'd say: "The ball really moves in a parabola, and the person on the train is just moving with it, so they see it wrong."

But there is no "really." There's no preferred frame. Physics works in all inertial frames equally. The train-rider's description (straight up and down) is just as valid as the platform observer's (parabola).

**Algebra alone can describe each frame separately, but it cannot connect them.** To connect frames, you need the change-in-a-blink.

### Why Velocity Addition Needs the Change-in-a-Blink

Suppose frame $S'$ (train) moves at constant velocity $\vec{V}$ relative to frame $S$ (ground). A point has position $\vec{r}\,'$ in $S'$ and $\vec{r}$ in $S$:

$$\vec{r}(t) = \vec{r}\,'(t) + \vec{V}t$$

This is algebraic — position transforms by simple addition. But velocity?

$$\vec{v} = \frac{d\vec{r}}{dt} = \frac{d}{dt}\!\left(\vec{r}\,' + \vec{V}t\right) = \frac{d\vec{r}\,'}{dt} + \vec{V} = \vec{v}\,' + \vec{V}$$

The step $\frac{d}{dt}(\vec{V}t) = \vec{V}$ requires the change-in-a-blink. Without it, you can't prove that velocities simply add.

And acceleration:

$$\vec{a} = \frac{d\vec{v}}{dt} = \frac{d}{dt}\!\left(\vec{v}\,' + \vec{V}\right) = \frac{d\vec{v}\,'}{dt} + \frac{d\vec{V}}{dt} = \vec{a}\,' + 0 = \vec{a}\,'$$

The term $\frac{d}{dt}\vec{V} = 0$ is crucial — it says "constant velocity has zero change-in-a-blink." This proves acceleration is **the same** in all inertial frames. **Without the change-in-a-blink, you cannot prove this invariance.**

---

## ✅ Resolved Through the Change-in-a-Blink

### Galilean Transformation

For two frames $S$ and $S'$ moving at constant relative velocity $\vec{V}$:

| Quantity | Transformation |
|:---|:---|
| Position | $\vec{r} = \vec{r}\,' + \vec{V}t$ |
| Velocity | $\vec{v} = \vec{v}\,' + \vec{V}$ |
| Acceleration | $\vec{a} = \vec{a}\,'$ |

Position transformation is algebraic. Velocity transformation uses the change-in-a-blink once. Acceleration invariance uses it twice.

### Why This Matters

Because $\vec{a} = \vec{a}\,'$ in all inertial frames, **Newton's second law $\vec{F} = m\vec{a}$ has the same form everywhere.** If you do an experiment in a lab on the ground or in a smoothly-moving train, you get the same physics. This is the **principle of Galilean relativity.**

The change-in-a-blink is what makes this connection rigorous.

---

## 💡 Examples

### Example 1: Boat Crossing a River

River flows east at $3\text{ m/s}$. Boat moves north at $4\text{ m/s}$ relative to the water. What does a person on the shore see?

Let $S'$ = water frame, $S$ = shore frame. $\vec{V} = (3, 0)$ (east), $\vec{v}\,' = (0, 4)$ (north).

$$\vec{v} = \vec{v}\,' + \vec{V} = (0, 4) + (3, 0) = (3, 4)$$

Speed: $|\vec{v}| = \sqrt{9 + 16} = 5\text{ m/s}$. Direction: $\tan^{-1}(4/3) \approx 53^\circ$ north of east.

The boat moves diagonally as seen from shore.  To cross a $100\text{ m}$-wide river: time = $100/4 = 25\text{ s}$ (the northward component determines crossing time).

### Example 2: Rain in a Moving Car

Rain falls vertically at $10\text{ m/s}$. A car drives east at $20\text{ m/s}$. At what angle does rain appear to hit the windshield?

Car frame $S'$: $\vec{v}_{\text{rain}}' = \vec{v}_{\text{rain}} - \vec{V}_{\text{car}} = (0, -10) - (20, 0) = (-20, -10)$.

Angle from vertical: $\tan\theta = \frac{20}{10} = 2$, so $\theta \approx 63^\circ$ from the vertical. The rain appears to come from ahead, at a steep angle.

### Example 3: Acceleration Invariance Verification

In $S$: $\vec{r}(t) = (t^2,\; 3t)$. In $S'$ moving at $\vec{V} = (2, 0)$ relative to $S$:

$\vec{r}\,' = \vec{r} - \vec{V}t = (t^2 - 2t,\; 3t)$.

$\vec{v} = (2t,\; 3)$, $\vec{v}\,' = (2t - 2,\; 3)$. Note $\vec{v} = \vec{v}\,' + \vec{V}$.

$\vec{a} = (2,\; 0)$, $\vec{a}\,' = (2,\; 0)$. **Same acceleration in both frames.**

### Example 4: Airplane With Wind

Plane's airspeed: $200\text{ m/s}$ north. Wind: $50\text{ m/s}$ from the west (blowing east).

$\vec{v}_{\text{ground}} = (0, 200) + (50, 0) = (50, 200)$. Speed: $\sqrt{2500 + 40000} \approx 206.2\text{ m/s}$.

To fly due north (ground track north), the plane must aim slightly west: $\vec{v}_{\text{air}} = (-50, \sqrt{200^2 - 50^2}) = (-50, \sqrt{37500}) \approx (-50, 193.6)$.

### Example 5: Projectile Motion in a Moving Frame

From a train moving at $10\text{ m/s}$ east, you throw a ball straight up at $20\text{ m/s}$. Ground observer sees:

$$\vec{r}(t) = (10t,\; 20t - 5t^2)$$

This is a parabola with range $R = 10 \cdot 4 = 40\text{ m}$ (flight time $= 2v_{0y}/g = 4\text{ s}$).

In the train frame: $\vec{r}\,'(t) = (0,\; 20t - 5t^2)$ — straight up and down. Same $y(t)$, different $x(t)$.

### Example 6: Relative Velocity Puzzle

Car A: $30\text{ m/s}$ east. Car B: $20\text{ m/s}$ north. What is the velocity of B relative to A?

$\vec{v}_{B\text{ rel }A} = \vec{v}_B - \vec{v}_A = (0, 20) - (30, 0) = (-30, 20)$.

Speed: $\sqrt{900 + 400} \approx 36.1\text{ m/s}$. Direction: $\tan^{-1}(20/(-30))$ — in the 2nd quadrant, about $146^\circ$ from east (or $34^\circ$ west of north).

---

## Meaning: "What We Just Did"

Motion is not absolute — it depends on who is watching. The change-in-a-blink provides the bridge between reference frames: velocity adds, acceleration stays the same. This is why physics works the same in all steadily-moving labs.

**Galileo said "motion is relative." Einstein later said "even time is relative."** The Galilean transformation here is the seed that grows into special relativity (Kleppner Ch 12~14).

---

## 🔧 Basic Drills *(solutions in `solutions/05-solutions.md`)*

1. Car A: $25\text{ m/s}$ east. Car B: $15\text{ m/s}$ north. Find the velocity of A relative to B.
2. Train moves east at $30\text{ m/s}$. Passenger walks west at $2\text{ m/s}$ inside. Ground speed?
3. Rain falls at $8\text{ m/s}$ vertically. Cyclist rides at $6\text{ m/s}$. Angle of rain relative to vertical?
4. In $S$: $\vec{r}(t) = (4t,\; 2t^2)$. $S'$ moves at $\vec{V} = (1, 0)$. Find $\vec{a}$ and $\vec{a}\,'$.
5. Plane heads north at $150\text{ m/s}$ airspeed. Wind blows east at $40\text{ m/s}$. Ground speed and direction?

## 🔥 Advanced Drills *(solutions in `solutions/05-solutions.md`)*

1. A boat can go $5\text{ m/s}$ in still water. River flows $3\text{ m/s}$ east. To cross $200\text{ m}$ and land exactly opposite, what heading (angle) is needed? How long does it take?
2. Prove that if $\vec{v} = \vec{v}\,' + \vec{V}$ and $\vec{V}$ is constant, then $\vec{a} = \vec{a}\,'$ using the change-in-a-blink definition.
3. A projectile is launched on a flatbed truck moving at constant speed. Show that the range measured on the ground is the truck's displacement during flight time plus the range measured on the truck.
4. **Trap**: A train accelerates at $2\text{ m/s}^2$. You drop a ball. Is its acceleration still $g$ in the ground frame? In the train frame?
5. Two particles have $\vec{r}_1(t) = (t^2,\; 3t)$ and $\vec{r}_2(t) = (t^2 + 2t,\; 3t - t)$. Find the relative velocity $\vec{v}_{12}$ and relative acceleration $\vec{a}_{12}$. Are they constant?

## 🧠 Intuitional Drills *(solutions in `solutions/05-solutions.md`)*

1. You're on a train moving at a constant $30\text{ m/s}$. You toss a ball straight up. Where does it land relative to your hand?
2. An airplane flies a $1000\text{ km}$ round trip ($500\text{ km}$ out, $500\text{ km}$ back) at airspeed $200\text{ m/s}$. On the outbound leg there's a $50\text{ m/s}$ headwind; on the return, a $50\text{ m/s}$ tailwind. Is the total round-trip time longer, shorter, or the same as with no wind?
3. A person walks at $1\text{ m/s}$ sideways (perpendicular to the motion) inside a train moving at $20\text{ m/s}$. What is their ground speed? Compare to walking forward.
4. Two cars approach an intersection: Car A from the south at $20\text{ m/s}$, Car B from the west at $20\text{ m/s}$. At what speed and angle does Car A see Car B approaching?
5. A car drives east at $15\text{ m/s}$ and another drives north at $20\text{ m/s}$. The northbound driver looks out the window: at what angle do they see the eastbound car?

---

## 📖 Reading Physical Symbols

| Symbol | How to Read It | Physical Meaning |
|:---|:---|:---|
| $S$, $S'$ | "S, S-prime" | Two reference frames. The **prime** ($'$) marks quantities measured in the moving frame. |
| $\vec{V}$ | "capital V" | The constant velocity of frame $S'$ relative to $S$. Upper-case to distinguish from particle velocity $\vec{v}$. |
| $\vec{r}\,'$ | "r-prime" | Position as measured in the $S'$ frame. The prime reminds you: "this is from the moving observer's perspective." |
| $\vec{v} = \vec{v}\,' + \vec{V}$ | "v equals v-prime plus V" | **Galilean velocity addition.** Speeds simply add when switching frames (true only at low speeds — relativity modifies this). |
| $\vec{a} = \vec{a}\,'$ | "a equals a-prime" | Acceleration is **invariant** — the same number in all inertial frames. This is why $F=ma$ works everywhere. |
| $\vec{v}_{A\text{ rel }B}$ | "v of A relative to B" | "What velocity does A appear to have when you're sitting on B?" Computed as $\vec{v}_A - \vec{v}_B$. |

**Key habit:** When switching frames, always ask: "Who is the observer? What frame are they in?" The prime marks the moving observer's measurements.

---

## Glossary
