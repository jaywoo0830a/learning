# Solutions — Momentum — Feel Builder

> Back to [Momentum 1](../1.md)

---

## Problem 1 — The Egg and the Sheet

**1.1 —** $v=\sqrt{2gh}=\sqrt{40}\approx6.3$ m/s. Stopping it means $\Delta p=0-mv=-(0.1)(6.3)=-0.63$ kg·m/s, so the **impulse is $0.63$ N·s** — identical for concrete and sheet. The change in momentum is the same; only the *time* differs.

**1.2 —** From $J=F\Delta t$:
- Concrete: $F=0.63/0.002\approx315$ N.
- Sheet: $F=0.63/0.2\approx3.2$ N.
Same impulse, **100× smaller force**. The sheet stretches the stopping time, and force is inversely proportional to time.

**1.3 —** $\Delta p=1200\times15=18000$ kg·m/s.
- With airbag: $F=18000/0.1=1.8\times10^5$ N.
- Without: $F=18000/0.01=1.8\times10^6$ N — ten times worse.

> **The feel:** it's never about "absorbing the momentum" — it's about **spreading the stop over time**. Airbags, crumple zones, padded dashboards, bending your knees when landing: all of them buy time to shrink the force.

---

## Problem 2 — The Recoil Dance

**2.1 —** No external forces on the person–ball system, so **momentum is conserved**: $0=m_p v_p + m_b v_b$.
$$v_p=-\frac{m_b}{m_p}v_b=-\frac{2(10)}{50}=-0.4\text{ m/s (opposite the ball)}.$$

**2.2 —** Before the catch: person moves at $-0.4$ m/s (say left), ball at $+10$ m/s (right). Total momentum:
$$p=(50)(-0.4)+(2)(10)=-20+20=0.$$
After the catch the pair has $p=(52)v$, so **$v=0$ — the person stops dead.** The throw and the catch are mirror images: what the throw created, the catch undoes.

**2.3 —** Before: $KE=\tfrac12(2)(100)+\tfrac12(50)(0.16)=100+4=104$ J. After: $0$ J. **All $104$ J lost** — converted to heat and deformation of the ball/arms on impact. Momentum was conserved; energy was not.

> **The feel:** momentum conservation is a **vector** bookkeeping that always balances, even when energy vanishes. Internal forces (your throw, your catch) move momentum around but never change the total.

---

## Problem 3 — The Head-On Decision

**3.1 —** For a 1-D elastic collision (moving mass $m_1$ into stationary $m_2$):
$$v_1'=\frac{m_1-m_2}{m_1+m_2}v_1=\frac{1}{3}(3)=1.0\text{ m/s}, \qquad v_2'=\frac{2m_1}{m_1+m_2}v_1=\frac{4}{3}(3)=4.0\text{ m/s}.$$
Check: $p$: $2(3)=2(1)+1(4)=6$ ✓. KE: $9=1+8=9$ ✓.

**3.2 —** Sticking: $v=\frac{m_1}{m_1+m_2}v_1=\frac{2}{3}(3)=2.0$ m/s.
$$KE_{\rm before}=\tfrac12(2)(9)=9\text{ J}, \qquad KE_{\rm after}=\tfrac12(3)(4)=6\text{ J} \Rightarrow 3\text{ J lost.}$$

**3.3 —** With $m_1=m_2=m$: $v_1'=\frac{0}{2m}v=0$ and $v_2'=\frac{2m}{2m}v=v$. **The speeds swap.** This is the pool-ball result — and it's exactly why a head-on elastic collision between equal masses looks like the first ball "passes through" the second.

> **The feel:** momentum conservation alone can't decide a collision — you need to know whether energy is also conserved (elastic) or not (inelastic). The equal-mass swap is the cleanest example: momentum and energy together force the unique answer.

---

## Problem 4 — Which Ball Hits Harder?

**4.1 —** Speeds are **equal**: $v=\sqrt{2gh}=\sqrt{40}\approx6.3$ m/s (mass cancels in energy). Momenta: $p_{\rm heavy}=2(6.3)=12.6$ vs $p_{\rm light}=6.3$ kg·m/s (2× for the heavier). KE: $\tfrac12(2)(40)=40$ J vs $\tfrac12(1)(40)=20$ J (2×).

**4.2 —** Impulse $=\Delta p$: heavy $12.6$ N·s, light $6.3$ N·s. Force $=\Delta p/\Delta t$ (same $\Delta t=0.05$ s): heavy $252$ N, light $126$ N.

**4.3 —** Momentum alone is not the whole story — **damage involves energy too**. Counterexample: two objects with the *same* momentum but different KE — a $2$ kg object at $5$ m/s ($p=10$, KE $=25$ J) vs a $1$ kg object at $10$ m/s ($p=10$, KE $=50$ J): same momentum, double the energy. A bullet has tiny momentum compared to a slow truck but enormous energy. "Danger" needs both $p$ and $KE$.

> **The misconception fixed:** momentum and energy are different quantities that don't move together. Equal heights give equal speeds; momentum scales with mass while energy scales with mass × speed² — so "bigger momentum" is not automatically "more dangerous".

---

## Problem 5 — The Coupling Paradox

**5.1 —** Momentum: $mv_0=2mv'$ → $v'=v_0/2=2.0$ m/s. KE before $=\tfrac12mv_0^2$; after $=\tfrac12(2m)(v_0/2)^2=\tfrac14mv_0^2$ — **half** of the initial KE remains.

**5.2 —** After coupling to $n$ total cars: $v_n=v_0/n$. Speeds: $2$ cars → $2.0$; $3$ cars → $4/3\approx1.33$; $4$ cars → $1.0$ m/s. Pattern: $v=v_0/n$.

**5.3 —** Momentum **is** conserved; **energy is not** in an inelastic collision. The "missing" energy becomes **heat, sound, and deformation** of the couplers — that's what "sticking" means. With 4 cars: $v=v_0/4=1.0$ m/s, KE $=\tfrac12(4m)(1)^2=2m$ vs original $\tfrac12m(4)^2=8m$ → **$6m$ J (75%) destroyed**.

> **The misconception fixed:** momentum conservation does NOT imply energy conservation. Perfectly inelastic collisions always destroy KE; the momentum "bookkeeping" balances while the energy book leaks into heat — the same reason the egg in Problem 1 stops.
