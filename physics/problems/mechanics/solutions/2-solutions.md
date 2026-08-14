# Mechanics — Day 2 — Solutions

> Full worked solutions. Solve each problem fully on paper before reading.

---

## Problem 1 — From the Cliff, Two Angles

**(a)** Launch at $37°$: $v_x=25\cos37=20$ m/s, $v_{y0}=25\sin37=15$ m/s. Take the cliff top as $y=0$, ground as $y=-20$:

$$-20=15t-\tfrac12(9.8)t^2\;\Rightarrow\;4.9t^2-15t-20=0$$

$$t=\frac{15+\sqrt{15^2+4(4.9)(20)}}{2(4.9)}=\frac{15+\sqrt{617}}{9.8}=4.07\ \text{s}$$

Range $=v_x t=20(4.07)=81$ m.

**(b)** $v_y=15-9.8(4.07)=-24.8$ m/s. Speed:

$$v=\sqrt{20^2+24.8^2}=31.9\ \text{m/s}$$

Direction: $\tan\phi=\frac{24.8}{20}=1.24$ → $\phi=51°$ **below horizontal**.

**(c)** At $53°$: $v_x=15$ m/s, $v_{y0}=20$ m/s:

$$-20=20t-4.9t^2\;\Rightarrow\;t=\frac{20+\sqrt{400+392}}{9.8}=4.91\ \text{s}$$

Range $=15(4.91)=74$ m — **shorter** than the $37°$ shot (81 m).

**Why:** on level ground, complementary angles give equal ranges because the flight times are equal ($2v\sin\theta/g$). From a cliff, the fall adds the same extra drop time to both, which *favors the flatter shot* (larger $v_x$). The $53°$ shot spends its extra hang time going up, not forward.

**(d)** Below $45°$. Extra airtime is free from the cliff, so you want the largest horizontal speed.

---

## Problem 2 — The Crate That Won't Decide

**(a)** $mg\sin25=10(9.8)(0.42)=41.4$ N vs. $f_{s,max}=0.45(10)(9.8)(0.91)=40.0$ N. Since $41.4>40.0$, it slides down on its own.

**(b)** To hold it, static friction must point up the slope at its maximum:

$$F+f_{s,max}=mg\sin25\;\Rightarrow\;F=41.4-40.0=1.4\ \text{N}$$

**(c)** $F=60$ N. Without friction, the net up-slope force would be $60-41.4=18.6$ N (up). Since $18.6<f_{s,max}=40.0$ N, static friction opposes the tendency with $18.6$ N **down the slope**, and the crate stays at rest.

**(d)** Moving **up** ⇒ friction acts down (kinetic):

$$F=mg\sin25+\mu_k mg\cos25=41.4+0.3(10)(9.8)(0.91)=41.4+26.8=68\ \text{N}$$

---

## Problem 3 — Collision With a Choice

**(a)** $v=\sqrt{2gh}=\sqrt{2(9.8)(2)}=6.26$ m/s.

**(b)** Elastic collision ($m_1=3$, $m_2=1$, $u_1=6.26$):

$$v_1'=\frac{m_1-m_2}{m_1+m_2}u_1=\frac{2}{4}(6.26)=3.13\ \text{m/s}$$

$$v_2'=\frac{2m_1}{m_1+m_2}u_1=\frac{6}{4}(6.26)=9.39\ \text{m/s}$$

The $1.0$ kg block then climbs: $h=v_2'^2/2g=(9.39)^2/19.6=4.5$ m.

**(c)** Inelastic (stick):

$$v'=\frac{m_1u_1}{m_1+m_2}=\frac{3(6.26)}{4}=4.70\ \text{m/s}$$

$$h=\frac{(4.70)^2}{19.6}=1.13\ \text{m}$$

**Why lower:** in the inelastic collision, kinetic energy is not conserved. KE before $=\tfrac12(3)(6.26)^2=58.8$ J; after $=\tfrac12(4)(4.70)^2=44.1$ J — about $25\%$ is destroyed at impact, so only $44.1$ J is available to climb the ramp ($44.1/(m_2g)=44.1/9.8=4.5$ m if all went to one block, but it's shared). In (c) the combined mass moves as one, and its KE is $44.1$ J → height $=44.1/[(4)(9.8)]=1.13$ m.

---

## Problem 4 — The Falling Rod

**(a)** Torque about the pivot when horizontal: the weight acts at the center of mass, $L/2$ from the pivot:

$$\tau=mg\frac{L}{2}=3(9.8)(1)=29.4\ \text{N·m}$$

$$I=\tfrac13mL^2=\tfrac13(3)(4)=4\ \text{kg·m}^2$$

$$\alpha=\frac{\tau}{I}=\frac{29.4}{4}=7.35\ \text{rad/s}^2$$

**(b)** Energy: the center of mass falls $L/2$, so $\Delta U=mgL/2$:

$$\tfrac12I\omega^2=mg\frac{L}{2}\;\Rightarrow\;\omega=\sqrt{\frac{3g}{L}}=\sqrt{\frac{3(9.8)}{2}}=3.83\ \text{rad/s}$$

**(c)** Tip speed $=\omega L=3.83(2)=7.67$ m/s. A point mass falling freely through height $L$ reaches $\sqrt{2gL}=\sqrt{39.2}=6.26$ m/s.

**Why the tip is faster:** the rod's mass is distributed; only a fraction is near the tip. The same gravitational energy produces rotation, and since the pivot end barely moves, the tip must sweep much faster to keep the rigid rod consistent.

---

## Problem 5 — The Spring That Knows Its Amplitude

**(a)** $\omega=v_{max}/A=0.8/0.12=6.67$ rad/s, so:

$$k=m\omega^2=0.6(6.67)^2=26.7\ \text{N/m}$$

**(b)** $T=2\pi/\omega=2\pi/6.67=0.94$ s.

**(c)** Total energy $=\tfrac12mv_{max}^2=\tfrac12(0.6)(0.8)^2=0.19$ J. At $x=A/2$:

$$v=\omega\sqrt{A^2-x^2}=6.67\sqrt{(0.12)^2-(0.06)^2}=6.67(0.104)=0.69\ \text{m/s}$$

**(d)** Doubling $m$ with the same $k$: $\omega=\sqrt{k/m}\to\omega/\sqrt2$. Then $T=2\pi/\omega$ grows by $\sqrt2$ (→1.33 s) and $v_{max}=\omega A$ drops by $\sqrt2$ (→0.57 m/s). A heavier mass on the same spring oscillates slower with smaller maximum speed.
