# Session 02 — Solutions

## 🔧 Basic Drills

**1.** $\vec{v} = (4, 6t)$, at $t=2$: $\vec{v}=(4,12)$. $\vec{a}=(0,6)$ at all $t$.

**2.** $\vec{v} = (-10\sin 2t,\; 10\cos 2t)$, $|\vec{v}|=10$ (constant). $\vec{a} = (-20\cos 2t,\; -20\sin 2t) = -4\vec{r}$, always toward the center.

**3.** $\vec{r}(t) = \int_0^t (6t', 8)dt' = (3t^2, 8t)$. At $t=3$: $\vec{r} = (27, 24)$.

**4.** $\vec{v}(t) = (10,\; 20-10t)$, $\vec{r}(t) = (10t,\; 30+20t-5t^2)$.

**5.** $\vec{v} = (2t,\; 3t^2-1) = (0,0) \Rightarrow 2t=0$ and $3t^2-1=0$. From $2t=0$: $t=0$. $t=0$ gives $\vec{v}=(0,-1) \neq (0,0)$. Never simultaneously zero → check: $2t=0 \to t=0$, $3(0)^2-1=-1 \neq 0$. Wait, redo: $\vec{v}=(2t, 3t^2-1)$. $2t=0 \Rightarrow t=0$. $3t^2-1=0 \Rightarrow t=\pm 1/\sqrt{3}$. Not the same $t$ → **never at rest.**

---

## 🔥 Advanced Drills

**1.** $\vec{v} = e^t(\cos t - \sin t,\; \sin t + \cos t)$, $\vec{a} = e^t(-2\sin t,\; 2\cos t)$. The $e^t$ factor means the spiral grows exponentially outward — a **logarithmic spiral.**

**2.** $\vec{v} = (\cos t - t\sin t,\; \sin t + t\cos t)$. At $t=2\pi$: $\vec{v} = (1,\; 2\pi)$. $|\vec{v}| = \sqrt{1+4\pi^2}$.

**3.** $\vec{v} = (v_0\cos\theta,\; v_0\sin\theta - gt)$, $\vec{a} = (0, -g)$. $|\vec{v}|^2 = v_0^2\cos^2\theta + (v_0\sin\theta-gt)^2$. Derivative: $\frac{d}{dt}|\vec{v}|^2 = 2(v_0\sin\theta-gt)(-g) = 0 \Rightarrow t = v_0\sin\theta/g = t_{\text{top}}$. Second derivative positive → minimum.

**4.** $\vec{v}(t) = (\sin t+1,\; \cos t,\; t)$, $\vec{r}(t) = (-\cos t + t + 1,\; \sin t + 1,\; \frac{1}{2}t^2)$.

**5.** $\vec{v} = (2t, 4t^3)$. $|\vec{v}|=0 \Rightarrow t=0$. At $t=0$: $\vec{a} = (2, 12t^2) = (2, 0) \neq (0,0)$. Zero velocity does **not** imply zero acceleration.

---

## 🧠 Intuitional Drills

**1.** Speed is constant. $\vec{a} \perp \vec{v}$ means $a_t = dv/dt = 0$, so $v$ never changes. All acceleration is centripetal — the path curves but speed stays the same.

**2.** Acceleration is $(0, -g)$ at **every** instant, including the peak. Gravity doesn't pause.

**3.** Same time. Both have $v_{0y}=0$ and $y_0 = h$, so $t = \sqrt{2h/g}$ for both. Horizontal motion is irrelevant to fall time.

**4.** Straight line. $\vec{r}(t) = (3t, 4t) = t(3,4)$ — motion along a fixed direction vector $(3,4)$ at constant speed $5$.

**5.** Segment 1 ($0\le t\le 3$): $\vec{v}=(2t,0)$, $\vec{r}=(t^2,0)$ — parabola along $x$-axis, ending at $(9,0)$. Segment 2 ($3\le t\le 6$): $\vec{v}=(6, -2(t-3))$, $\vec{r}=(9+6(t-3), -(t-3)^2)$. The path bends at $(9,0)$, first moving right, then curving downward.
