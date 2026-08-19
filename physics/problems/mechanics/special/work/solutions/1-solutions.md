# Solutions — Work — Feel Builder

> Back to [Work 1](../1.md)

---

## Problem 1 — The Case of the Missing Work

**1.1 — Forces:** weight $mg=50$ N (down), normal force $N=mg\cos30°=43.3$ N (perpendicular to the surface).
- **Gravity:** component along the slide is $mg\sin30°=25$ N, so $W_g = (mg\sin\theta)d = 25\times3 = 75$ J. (Equivalently $mg\,d\cos60°=50\times3\times0.5=75$ J.)
- **Normal force:** $N\perp d$, so $\cos90°=0$, $W_N = 0$ J. **The normal force never does work.**
- **Net work:** $75$ J $\Rightarrow \Delta KE = 75$ J (the block speeds up).

**1.2 —** Constant speed $\Rightarrow a=0\Rightarrow F_{\rm applied}=f_k=\mu_k mg=0.4\times50=20$ N.
- $W_{\rm applied}=20\times2=+40$ J, $W_{\rm friction}=-40$ J, $W_g=W_N=0$ J.
- **Net work $=0$** $\Rightarrow \Delta KE=0$ — constant speed means the energy you put in is exactly cancelled by friction (converted to heat).

**1.3 —** Up: $W_g=-mgh=-(2)(10)(5)=-100$ J (force opposes displacement). Down: $W_g=+100$ J. **Round trip $=0$ J.**
- Gravity is **conservative**: its work depends only on height change, not the path — a round trip returns exactly to zero. (Friction would not do this: it always opposes motion, so its work is always negative.)

> **The feel:** "no work" ≠ "no effort". Pushing a box at constant speed is exhausting, yet **net** work is zero — the box's KE doesn't change. And the normal force can be huge, but it never contributes work because it's always sideways to the motion.

---

## Problem 2 — Work From a Graph

**2.1 —** $F=kx=200x$ is a straight line through the origin. At $x=0.20$, $F=40$ N. The work is the **triangle** area:
$$W=\tfrac12(\text{base})(\text{height})=\tfrac12(0.20)(40)=4.0\text{ J}.$$

**2.2 —** $\frac12kx^2=\frac12(200)(0.04)=4.0$ J ✓. From $x=0.10$ to $0.20$: forces are $20$ N and $40$ N, so the area is a **trapezoid**:
$$W=\tfrac12(20+40)(0.10)=3.0\text{ J} \quad\left(=\tfrac12k(x_2^2-x_1^2)\right).$$
Only $3$ J is needed, not $4$ J — the first stretch already "paid" for the low-force region.

**2.3 —** $F=30x$ is linear; at $x=2.0$, $F=60$ N. Area $=\tfrac12(2)(60)=60$ J.

> **The feel:** work for a *constant* force is $F\cdot d$; for a *changing* force, work is the **area under the $F$–$x$ curve**. The spring is the model case — because the force grows as you stretch, the work grows as $x^2$, not $x$.

---

## Problem 3 — The Marathon of Lifting

**3.1 —** Constant speed $\Rightarrow F_{\rm you}=mg=100$ N up.
- $W_{\rm you}=+100\times2=+200$ J, $W_{\rm gravity}=-200$ J, **net $=0$** (KE unchanged).

**3.2 —** The upward force is **perpendicular** to the horizontal displacement: $W=\text{(force)}\times d\cos90°=0$. Gravity also does zero work.
- Mechanical work on the box is $0$, yet you get tired because your **muscles do internal work** — chemical energy is converted to heat inside your body. "Work" in physics counts energy *transferred to the box*, not your effort.

**3.3 —** Straight up: $W=200$ J, $F=100$ N.
- Frictionless ramp: **same work** $200$ J (gravity is conservative — only the height matters), but the force is smaller: $F=mg\sin\theta=100\times\tfrac{2}{4}=50$ N. The ramp **trades force for distance**.
- With friction: $\cos\theta=\sqrt{4^2-2^2}/4=0.866$, so $f_k=\mu_k mg\cos\theta=0.2\times100\times0.866=17.3$ N, and $W_f=17.3\times4\approx69$ J. Total work $\approx269$ J — **friction makes the work path-dependent** (you can't get that energy back).

> **The feel:** machines (ramps, pulleys, levers) never reduce the *work* for a conservative force — they trade force for distance. Only removing friction actually reduces the work you must do.

---

## Problem 4 — The Zero-Work Illusion

**4.1 —** Displacement $d=0$, so $W=F\,d\cos\theta=0$ J — **zero work on the wall**, no matter how hard or long you push. The exhaustion is **internal**: your muscles do chemical work that becomes heat inside your body; none of it is transferred to the wall.

**4.2 —** In uniform circular motion, gravity is always **perpendicular to the velocity**, so at every instant $W=F\,d\cos90°=0$. Full orbit: $0$ J; quarter orbit: $0$ J. The satellite keeps moving because **nothing removes its kinetic energy** — its speed is constant. Gravity's job is to change the *direction* of the velocity, not its magnitude.

**4.3 —** The error is confusing **force** with **work**. A force does work only when it has a component along the displacement; a centripetal (sideways) force changes direction but never speed, so it does zero work. The satellite "keeps moving" by inertia while gravity steers it — no work required.

> **The misconception fixed:** "force acting" does not mean "work being done." Perpendicular forces, and forces on stationary objects, do zero work — and that's fine, because work is what changes *speed*, not direction.

---

## Problem 5 — The Speed Trap

**5.1 —** Both do the **same work**: $W=mgh=20(10)(1.5)=300$ J (same weight, same height). Power differs: $P_A=300/2=150$ W, $P_B=300/4=75$ W. **Work is the task; power is how fast you do it.**

**5.2 —** $KE\propto v^2$: doubling speed $\Rightarrow 4\times$ KE. Stopping: the braking force does $W=f\cdot d$, which must equal $\Delta KE$, so $d\propto KE\Rightarrow$ **stopping distance also $4\times$**. (From $10$ to $20$ m/s the KE and stopping distance quadruple, not double.)

**5.3 —** People instinctively think linearly (2× speed → 2× danger), but energy is **quadratic** in speed. This is exactly why tailgating at highway speed is far riskier than people estimate — a 2× speed increase needs 4× the room to stop.

> **The misconception fixed:** doubling speed quadruples energy and stopping distance; and "doing the same work faster" is not more work — it's more power.
