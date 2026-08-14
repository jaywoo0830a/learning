# Mechanics — Day 3 — Solutions

> Full worked solutions. Solve each problem fully on paper before reading.

---

## Problem 1 — The Satellite at 2R_E

**(a)** Orbital speed — gravity provides centripetal force:

$$\frac{GMm}{r^2}=\frac{mv^2}{r}\;\Rightarrow\;v=\sqrt{\frac{GM}{r}}=\sqrt{\frac{(6.67e-11)(5.97e24)}{2(6.37e6)}}=\sqrt{3.12e7}=5.6\times10^3\ \text{m/s}$$

**(b)** $T=2\pi r/v=2\pi(1.274e7)/5590=1.43\times10^4$ s $=3.98$ h ≈ 4.0 h.

**(c)** Escape speed from radius $r$:

$$v_{esc}=\sqrt{\frac{2GM}{r}}=v\sqrt2=7.9\times10^3\ \text{m/s}$$

**(d)** At $v<v_{circular}$ the satellite falls into an **elliptical** orbit with perigee inside the circular radius. If the reduction is small, the ellipse just dips; drag from the upper atmosphere progressively shrinks it until re-entry. (Exact "2%" details depend on drag, but the qualitative fate is decay of the orbit.)

---

## Problem 2 — The Ambitious Roller Coaster

**(a)** At the loop top (height $2R=6$ m), need $v^2\ge gR$:

$$mgH=mg(2R)+\tfrac12mv^2,\qquad v^2=gR$$

$$H=2R+\frac{gR}{2g}=6+\frac{29.4}{19.6}=7.5\ \text{m}$$

**(b)** $H=15$ m. Energy from release to max spring compression — the cart returns to height $2R$ after the loop, then crosses the rough $2.0$ m:

$$mgH=mg(2R)+\mu_k mgd+\tfrac12kx^2$$

$$294=117.6+0.3(2)(9.8)(2)+150x^2=117.6+11.8+150x^2$$

$$150x^2=164.6\;\Rightarrow\;x=1.05\ \text{m}$$

**(c)** Momentum during the stick collision (at the start of the rough stretch, speed $\sqrt{2g(15)}=17.15$ m/s):

$$(2.0)(17.15)=(3.0)v'\;\Rightarrow\;v'=11.4\ \text{m/s}$$

Then kinetic energy is dissipated by kinetic friction over distance $s$:

$$\tfrac12(3.0)(11.4)^2=\mu_k(3.0)g\,s\;\Rightarrow\;s=\frac{130.7}{2(0.3)(9.8)}=22.2\ \text{m}$$

---

## Problem 3 — The Yo-Yo That Teaches Rotation

**(a)** String unwinds without slipping: $a=\alpha R$. Torque about the center:

$$TR=I\alpha=\tfrac12MR^2\frac{a}{R}=\tfrac12MRa\;\Rightarrow\;T=\tfrac12Ma$$

Newton's 2nd law for the center of mass:

$$Mg-T=Ma\;\Rightarrow\;Mg-\tfrac12Ma=Ma\;\Rightarrow\;a=\tfrac23g=6.5\ \text{m/s}^2$$

$$T=\tfrac12M(\tfrac23g)=\tfrac13Mg=\tfrac13(0.2)(9.8)=0.65\ \text{N}$$

**(b)** From rest over $d=1.0$ m: $v=\sqrt{2ad}=\sqrt{2(6.5)(1.0)}=3.6$ m/s.
(Energy check: $Mgd=\tfrac12Mv^2+\tfrac12I\omega^2=\tfrac12Mv^2(1+\tfrac12)$ → $v^2=\tfrac43gd=13.07$, $v=3.6$ m/s ✓)

**(c)** Hoop ($I=MR^2$): $TR=MR^2\alpha$ → $T=Ma$; then $Mg-Ma=Ma$ → $a=\tfrac12g=4.9$ m/s².

**Physical point:** the hoop's entire mass is at the rim → larger $I$ → a bigger share of energy goes into rotation → slower fall. The disk's mass is spread inward, so it falls faster.

---

## Problem 4 — Spring, Table, Cliff

**(a)** $\tfrac12kx^2=\tfrac12mv^2$ → $v=x\sqrt{k/m}=0.2\sqrt{800/0.5}=8.0$ m/s.

**(b)** Vertical fall from $1.25$ m: $t=\sqrt{2h/g}=\sqrt{2.5/9.8}=0.505$ s. Range $=8.0(0.505)=4.0$ m.

**(c)** $v_y=gt=9.8(0.505)=4.95$ m/s:

$$v=\sqrt{v_x^2+v_y^2}=\sqrt{8.0^2+4.95^2}=9.4\ \text{m/s}$$

**(d)** Friction over the $1.0$ m patch:

$$v_x^2=8.0^2-2(0.40)(9.8)(1.0)=64-7.84=56.2\;\Rightarrow\;v_x=7.5\ \text{m/s}$$

Range $=7.5(0.505)=3.8$ m. The flight time is unchanged — friction only reduced the horizontal speed.

---

## Problem 5 — The Conical Pendulum

**(a)** Vertical balance (no vertical acceleration):

$$T\cos30=mg\;\Rightarrow\;T=\frac{0.5(9.8)}{0.866}=5.7\ \text{N}$$

**(b)** Radius: $r=L\sin30=2.0(0.5)=1.0$ m. Horizontal component provides centripetal force:

$$T\sin30=\frac{mv^2}{r}\;\Rightarrow\;v=\sqrt{\frac{T\sin30\cdot r}{m}}=\sqrt{\frac{5.7(0.5)(1.0)}{0.5}}=2.4\ \text{m/s}$$

**(c)** $\omega=v/r=2.38$ rad/s → $T_{period}=2\pi/\omega=2.6$ s. (Formula check: $T_{period}=2\pi\sqrt{L\cos\theta/g}=2\pi\sqrt{1.732/9.8}=2.64$ s ✓)

**(d)** As $\theta\to90°$, $\cos\theta\to0$: $T=mg/\cos\theta\to\infty$ and $v=\sqrt{(T\sin\theta)\,r/m}\to\infty$. The string can never be exactly horizontal — that would require infinite tension and speed. Gravity must always supply the vertical component of tension.
