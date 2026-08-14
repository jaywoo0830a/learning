# Mechanics — Day 1 — Solutions

> Full worked solutions. Solve each problem fully on paper before reading.

---

## Problem 1 — Two Balls in the Air

**(a)** Ball B must reach height $H$ with zero speed at the top:

$$v_0=\sqrt{2gH}=\sqrt{2(9.8)(45)}=\sqrt{882}=29.7\ \text{m/s}$$

**(b)** Positions (up positive, ground = 0):

$$y_A=H-\tfrac12 gt^2,\qquad y_B=v_0t-\tfrac12 gt^2$$

They meet when $y_A=y_B$:

$$H-\tfrac12gt^2=v_0t-\tfrac12gt^2 \;\Rightarrow\; t=\frac{H}{v_0}=\frac{45}{29.7}=1.52\ \text{s}$$

Height: $y_B=v_0t-\tfrac12gt^2=45-\tfrac12(9.8)(1.52)^2=45-11.3=33.7\ \text{m}=\tfrac34H$.

**(c)** Velocities: $v_A=-gt$ (downward), $v_B=v_0-gt$ (upward). Their separation speed:

$$v_B-(-v_A)=v_B+v_A=(v_0-gt)+gt=v_0=\text{constant}$$

The $\tfrac12gt^2$ terms cancel because both balls experience the same $g$ — relative motion is uniform, so the meeting time is simply distance ÷ closing speed: $t=H/v_0$.

---

## Problem 2 — The Stubborn Crate on the Incline

**(a)** Down-slope component on $m_1$:

$$m_1g\sin30=4(9.8)(0.5)=19.6\ \text{N}$$

Max static friction:

$$f_{s,max}=\mu_s m_1g\cos30=0.5(4)(9.8)(0.866)=17.0\ \text{N}$$

The hanging block pulls with $m_2g=49$ N. Since $49>19.6+17.0$, static friction cannot hold → the system moves, $m_2$ descends. While moving, kinetic friction applies:

$$F_{net}=m_2g-m_1g\sin30-\mu_k m_1g\cos30=49-19.6-0.3(4)(9.8)(0.866)=49-19.6-10.2=19.2\ \text{N}$$

$$a=\frac{F_{net}}{m_1+m_2}=\frac{19.2}{9.0}=2.14\ \text{m/s}^2$$

**(b)** From $m_2$: $m_2g-T=m_2a$ → $T=5(9.8-2.14)=38.3$ N.
Check on $m_1$: $T-19.6-10.2=38.3-29.8=8.5$ N $=m_1a=4(2.14)=8.6$ N ✓.

**(c)** At rest, static friction can point either way, with magnitude up to $f_{s,max}$. The hanging force $m_2g$ must satisfy:

$$m_1g\sin30-f_{s,max}\le m_2g\le m_1g\sin30+f_{s,max}$$

$$2.6\ \text{N}\le m_2g\le 36.6\ \text{N}\;\Rightarrow\; m_2\in[0.27,\ 3.73]\ \text{kg}$$

$m_2=5.0$ kg is outside this range → it slides (consistent with (a)).

---

## Problem 3 — Down the Hill, Into the Spring

**(a)** Energy from start to max compression: gravity does work $mgh$; friction on the flat dissipates $\mu_k mgL$; the rest is stored in the spring.

$$mgh=\mu_k mgL+\tfrac12kx^2$$

$$h=\frac{\mu_k mgL+\tfrac12kx^2}{mg}=\frac{0.4(2)(9.8)(1.5)+22.5}{2(9.8)}=\frac{34.3}{19.6}=1.75\ \text{m}$$

(Here $\tfrac12kx^2=\tfrac12(500)(0.30)^2=22.5$ J.)

**(b)** On the way back, the spring's $22.5$ J must again pay friction ($\mu_k mgL=11.8$ J) and provide gravitational potential $mgh'$:

$$\tfrac12kx^2=\mu_k mgL+mgh'\;\Rightarrow\;h'=\frac{22.5-11.8}{19.6}=0.55\ \text{m}$$

The block returns to only $0.55$ m — friction eats $1.20$ m of the original height on the round trip.

**(c)** Frictionless: $mgh=\tfrac12kx^2$ → $h=22.5/19.6=1.15$ m, and since no energy is lost, the block returns to exactly $h=1.15$ m. The difference ($1.75$ vs $1.15$ m) is exactly the friction loss $\mu_k mgL=11.8$ J worth of height.

---

## Problem 4 — Bullet Into a Spring-Launcher

**(a)** Perfectly inelastic collision (bullet embeds). Momentum is conserved during the collision:

$$(0.020)(400)=(2.0)v\;\Rightarrow\;v=4.0\ \text{m/s}$$

**(b)** After the collision, mechanical energy is conserved (frictionless):

$$\tfrac12(2.0)(4.0)^2=\tfrac12(2000)x^2\;\Rightarrow\;x=\sqrt{\frac{16}{1000}}=0.127\ \text{m}\approx12.6\ \text{cm}$$

**(c)** From impact to max compression is one quarter of an SHM period:

$$t=\frac{T}{4}=\frac{\pi}{2}\sqrt{\frac{m}{k}}=\frac{\pi}{2}\sqrt{\frac{2.0}{2000}}=0.0497\ \text{s}$$

**(d)** $KE_i=\tfrac12(0.020)(400)^2=1600$ J; $KE_f=\tfrac12(2.0)(4.0)^2=16$ J. Lost:

$$1-\frac{16}{1600}=0.99=99\%$$

Nearly all the kinetic energy is converted to heat, sound, and deformation during the embedding. This is why inelastic collisions are only solvable via momentum, not energy.

---

## Problem 5 — The Loop That Is (Almost) Too Small

**(a)** At the top, contact requires $N\ge0$, so $mg$ alone must provide the centripetal force:

$$mg=m\frac{v_{top}^2}{R}\;\Rightarrow\;v_{top}^2=gR$$

Energy from bottom to top (height change $2R$):

$$v_{top}^2=v_0^2-2g(2R)=v_0^2-4gR=gR\;\Rightarrow\;v_0=\sqrt{5gR}=\sqrt{5(9.8)(8)}=19.8\ \text{m/s}$$

**(b)** At the bottom, normal force minus weight provides centripetal force:

$$N-mg=\frac{mv_0^2}{R}\;\Rightarrow\;N=m\left(g+\frac{v_0^2}{R}\right)=500\left(9.8+\frac{22^2}{8}\right)=500(70.3)=3.5\times10^4\ \text{N}$$

**(c)** Let $\theta$ be measured from the bottom; height above the bottom is $R(1-\cos\theta)$. Energy:

$$v^2=v_0^2-2gR(1-\cos\theta)$$

Radial force equation (inward positive, gravity's radial component is $-mg\cos\theta$):

$$N+mg\cos\theta=\frac{mv^2}{R}\;\Rightarrow\;N=\frac{mv^2}{R}+mg\cos\theta$$

Leaves the track when $N=0$:

$$\frac{v^2}{R}=-g\cos\theta\;\Rightarrow\;v^2=-gR\cos\theta$$

Equate the two expressions for $v^2$:

$$v_0^2-2gR(1-\cos\theta)=-gR\cos\theta$$

$$v_0^2=2gR-3gR\cos\theta\;\Rightarrow\;\cos\theta=\frac{2}{3}-\frac{v_0^2}{3gR}=0.667-\frac{324}{3(78.4)}=0.667-1.378=-0.711$$

$$\theta=\arccos(-0.711)=135°$$

Height $=R(1-\cos\theta)=8(1.711)=13.7$ m above the bottom. Speed there:

$$v^2=324-2(9.8)(8)(1.711)=55.8\;\Rightarrow\;v=7.5\ \text{m/s}$$

After leaving, the car is a projectile (with this velocity at $135°$ from the bottom, i.e. $45°$ above horizontal, moving up-and-outward).
