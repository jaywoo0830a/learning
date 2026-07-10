# Session 04 — Solutions

## 🔧 Basic Drills

**1.** $a_c = v^2/r = 36/3 = 12\text{ m/s}^2$.

**2.** $a_c = 100/50 = 2\text{ m/s}^2 = 0.2g$.

**3.** At $t=1$: $v=4$, $a_t = dv/dt = 4$, $a_n = v^2/\rho = 16/8 = 2$. Total $a = \sqrt{16+4} = \sqrt{20} \approx 4.47\text{ m/s}^2$.

**4.** $\vec{v} = (-10\sin 2t,\; 10\cos 2t)$, $|\vec{v}| = 10$. $\vec{a} = (-20\cos 2t,\; -20\sin 2t)$, $|\vec{a}| = 20$. $v^2/r = 100/5 = 20$. Confirmed.

**5.** $a_c = v^2/r \Rightarrow r = v^2/a_c = 225/4.5 = 50\text{ m}$.

---

## 🔥 Advanced Drills

**1.** $a_c = 100/20 = 5\text{ m/s}^2 = 0.5g$. The track exerts normal force $N = mg - mv^2/r$ downward (or upward on the car). For the car to stay on the track, we need $N \ge 0$, i.e., $mg \ge mv^2/r \Rightarrow v^2 \le gr = 200 \Rightarrow v \le \sqrt{200} \approx 14.1\text{ m/s}$. At $10\text{ m/s}$, $100 < 200$ — the car stays on.

**2.** $y = \frac{1}{2}x^2$, $x(t) = 2t$, so $y(t) = 2t^2$. $\vec{r}(t) = (2t, 2t^2)$, $\vec{v}=(2,4t)$, $\vec{a}=(0,4)$. At $x=1$ ($t=1/2$): still $\vec{a}=(0,4)$. Radius of curvature: $v=\sqrt{4+16t^2}=\sqrt{4+4}=2\sqrt{2}$ at $t=1/2$, $a_n = \frac{|\vec{v}\times\vec{a}|}{|\vec{v}|} = \frac{|(2,4t,0)\times(0,4,0)|}{2\sqrt{2}} = 8/(2\sqrt{2}) = 2\sqrt{2}$, $\rho = v^2/a_n = 8/(2\sqrt{2}) = 2\sqrt{2} \approx 2.83\text{ m}$.

**3.** At $t=0$: $\vec{v}=(1,0,0)$, $\vec{a}=(0,2,0)$. $\rho = v^2/|\vec{a}| = 1/2 = 0.5\text{ m}$.

**4.** $a_c = v^2/r$. If $r \to 2r$, $a_c \to v^2/(2r) = a_c/2$ — it halves, not doubles. Intuition fails because we think "bigger circle = more acceleration needed," but acceleration depends on how tight the turn is.

**5.** $\vec{v}\times\vec{a}$ has magnitude $|\vec{v}||\vec{a}|\sin\phi$ where $\phi$ is the angle between velocity and acceleration. This equals $|\vec{v}|a_n$ because $a_n = |\vec{a}|\sin\phi$ (the component perpendicular to velocity). So $a_n = |\vec{v}\times\vec{a}|/|\vec{v}|$.

---

## 🧠 Intuitional Drills

**1.** The driver's body leans toward the **outside** of the turn (right, if turning left). The car accelerates left (centripetal), but the body's inertia resists — it "wants" to continue straight. The sensation is centrifugal, but the real force (friction from the seat) pushes inward.

**2.** No work. $\vec{F} \perp \vec{v}$ always, so $P = \vec{F}\cdot\vec{v} = 0$. Zero power means constant kinetic energy. The satellite's speed never changes in a circular orbit.

**3.** At the top, $mg + N = mv^2/r$. Minimum speed when $N=0$: $mg = mv^2/r \Rightarrow v = \sqrt{gr} = \sqrt{10\cdot 10} = 10\text{ m/s}$.

**4.** $F_c = mv^2/r$. Speed $20 \to 40$ is a factor of 2, so $v^2$ goes up by factor 4. The required centripetal force quadruples.

**5.** At the bottom: $T - mg = mv^2/r \Rightarrow T = mg + mv^2/r$. At the top: $T + mg = mv^2/r \Rightarrow T = mv^2/r - mg$. Bottom tension is larger by $2mg$.
