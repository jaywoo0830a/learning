# Mechanics — Special A1 — Solutions

> Full worked solutions. Solve all 20 problems fully on paper before reading.

---

# Part A — Circular Motion

## Problem A1 — The Tilted String

> 💡 **Key insight**: The bob moves in a **horizontal circle**, so decompose the tension into horizontal (centripetal) and vertical (balances the weight) components, and the circle's radius is $r=L\sin\theta$. Miss this and you'll mistake the radius for $L$ or treat the pendulum as 2D planar motion — the equations get tangled and the solution gets much longer. The clean period formula $2\pi\sqrt{L\cos\theta/g}$ in (c) also only emerges after substituting $r=L\sin\theta$ into $v$.

> 💡 **(a) — Concept needed**: vector force decomposition (split tension into horizontal/vertical components). **Key insight**: vertical equilibrium alone fixes $T=\tfrac{mg}{\cos\theta}$. **If missed**: you carry both $T$ and $v$ as unknowns and can't even start.

**(a)** Forces: tension $T$ along the string, weight $mg$ down. The bob moves in a horizontal circle, so the **horizontal component of tension** $T\sin\theta$ is the centripetal force; the vertical component $T\cos\theta$ balances the weight.

$$T\cos\theta=mg \;\Rightarrow\; T=\frac{mg}{\cos\theta}=\frac{(0.50)(9.8)}{0.80}=6.13\ \text{N}$$

> 💡 **(b) — Concept needed**: centripetal force $F=mv^2/r$, and the bob's circle has radius $r=L\sin\theta$ (not $L$). **Key insight**: radial equation $T\sin\theta=mv^2/r$ combines with (a) into $v=\sqrt{gr\tan\theta}$. **If missed**: using $L$ as the radius makes $v$ wrong by $\sqrt{\sin\theta}$ and the (c) check fails.

**(b)** Radius of the circle: $r=L\sin\theta=2.0(0.60)=1.2$ m. Radial force law:

$$T\sin\theta=\frac{mv^2}{r}\;\Rightarrow\; v=\sqrt{\frac{T\sin\theta\,r}{m}}=\sqrt{\frac{(6.13)(0.60)(1.2)}{0.50}}=\sqrt{8.82}=2.97\ \text{m/s}$$

Equivalently $v=\sqrt{gr\tan\theta}=\sqrt{(9.8)(1.2)(0.75)}=2.97$ m/s.

> 💡 **(c) — Concept needed**: period $T_{\text{period}}=2\pi r/v$ and small-angle limits ($\cos\theta\to1$). **Key insight**: substituting (a)+(b) collapses everything into $T=2\pi\sqrt{L\cos\theta/g}$. **If missed**: you compute a number but never see the simple-pendulum limit — which is the point of the question.

**(c)** Period: $T_{\text{period}}=2\pi r/v=2\pi(1.2)/2.97=2.54$ s. Symbolically:

$$T_{\text{period}}=\frac{2\pi(L\sin\theta)}{\sqrt{gL\sin\theta\tan\theta}}=2\pi\sqrt{\frac{L\cos\theta}{g}}$$

As $\theta\to0°$, $\cos\theta\to1$, so $T_{\text{period}}\to2\pi\sqrt{L/g}$ — the **simple pendulum** period. (And indeed a conical pendulum at tiny angles behaves like a pendulum swinging in a plane.)

> 💡 **(d) — Concept needed**: limits of $\cos\theta$ and $\tan\theta$ as $\theta\to90°$. **Key insight**: $\cos\theta\to0$ makes $T$ and $v$ diverge — physically the string snaps. **If missed**: you quote "$\infty$" without the physical reason (the horizontal component must supply an ever-larger centripetal force).

**(d)** As $\theta\to90°$: $\cos\theta\to0$ so $T=mg/\cos\theta\to\infty$ and $v=\sqrt{gL\sin\theta\tan\theta}\to\infty$. Physically the string tension grows without bound (and its horizontal component must supply the ever-larger centripetal force), so the string snaps at some large-but-finite angle long before $90°$.

---

## Problem A2 — The Rotor That Never Drops

> 💡 **Key insight**: Split the roles: the **normal force is the centripetal force, friction supports the weight**. At the threshold $f=\mu_s N=mg$, so $N=mg/\mu_s$. Mistake friction for the centripetal force and the equations flip upside down; miss the $N=mg/\mu_s$ relation in (c) and the computations drag on.

> 💡 **(a) — Concept needed**: free-body diagram on a vertical line; static friction opposes the tendency to slip (points **up**). **Key insight**: no vertical acceleration $\Rightarrow f=mg$ exactly. **If missed**: you write $f=\mu N$ immediately and confuse *needed* friction with *available* friction.

**(a)** Forces: weight $mg$ down, normal $N$ from the wall pointing **inward** (this is the centripetal force), and static friction $f$ pointing **up** (this supports the weight). There is no vertical acceleration: $f=mg$.

> 💡 **(b) — Concept needed**: centripetal force $N=m\omega^2R$; static friction limit $f_{\max}=\mu_sN$. **Key insight**: need $\mu_s m\omega^2R\ge mg$, so $\omega_{\min}=\sqrt{g/(\mu_sR)}$. **If missed**: you mistake friction for the centripetal force — the wall must *push*, not rub.

**(b)** Centripetal: $N=m\omega^2R$. No-slip condition: $f_{\max}=\mu_s N\ge mg$.

$$\mu_s m\omega^2R\ge mg\;\Rightarrow\; \omega_{\min}=\sqrt{\frac{g}{\mu_s R}}=\sqrt{\frac{9.8}{(0.40)(3.0)}}=\sqrt{8.17}=2.86\ \text{rad/s}$$

Period: $T=2\pi/\omega_{\min}=2\pi/2.86=2.20$ s (about one revolution every 2.2 s).

> 💡 **(c) — Concept needed**: at the threshold, $N=mg/\mu_s$ (from (b)). **Key insight**: here $N=2.5\,mg$ — the smaller $\mu_s$, the harder the wall must push. **If missed**: the counterintuitive "wall presses with 2.5× the weight" looks like an arithmetic mistake.

**(c)** At $\omega_{\min}$: $N=m\omega_{\min}^2R=m(g/\mu_s R)R=mg/\mu_s=\dfrac{60\cdot9.8}{0.40}=1470$ N $=2.5\,mg$.

So the wall presses on the person with **2.5 times their weight**. The friction needed is only $mg$, so a friction coefficient of only $1/2.5=0.40$ suffices. The normal force is $mg/\mu_s$ because friction is $f=\mu_sN$ — the smaller $\mu_s$, the harder the wall must push.

> 💡 **(d) — Concept needed**: proportional reasoning with a square root. **Key insight**: $\omega_{\min}\propto1/\sqrt{\mu_s}$, so doubling $\mu_s$ multiplies $\omega_{\min}$ by $1/\sqrt2$. **If missed**: you answer "half" instead of $0.707\times$ — friction enters through $N\propto\omega^2$, hence the root.

**(d)** $\omega_{\min}\propto 1/\sqrt{\mu_s}$, so doubling $\mu_s$ gives $\omega_{\min}\to \omega_{\min}/\sqrt2$ — a factor $0.707$. The square root appears because friction scales with $\mu_s N$ and $N$ scales with $\omega^2$.

---

## Problem A3 — The Curve With an Attitude

> 💡 **Key insight**: For a frictionless bank, $\tan\theta=v^2/gR$. With friction, handle **two cases — too slow (friction up the slope) and too fast (friction down)** — which differ only by a sign. Without this, trying to force both cases into one equation scrambles the signs and lengthens the work. The (d) conclusion that the design speed needs no friction also follows from here.

> 💡 **(a) — Concept needed**: on a flat road friction *is* the centripetal force, limited by $\mu_s mg$. **Key insight**: masses cancel: $v_{\max}=\sqrt{\mu_s gR}$. **If missed**: you keep $m$ in the answer or forget the static-friction limit.

**(a)** Flat curve: friction is the centripetal force.

$$\mu_s mg=\frac{mv^2}{R}\;\Rightarrow\; v_{\max}=\sqrt{\mu_s gR}=\sqrt{(0.60)(9.8)(50)}=\sqrt{294}=17.1\ \text{m/s}$$

> 💡 **(b) — Concept needed**: frictionless bank — decompose the normal into horizontal (centripetal) and vertical (weight). **Key insight**: dividing the two equations kills $N$ and $m$: $\tan\theta=v^2/(gR)$. **If missed**: you solve for $N$ explicitly and get tangled; the design-speed formula is the payoff.

**(b)** Frictionless bank: the horizontal component of the normal provides centripetal force.

$$N\sin\theta=\frac{mv^2}{R},\qquad N\cos\theta=mg\;\Rightarrow\; \tan\theta=\frac{v^2}{gR}$$

For $v\approx20$ m/s: $\tan\theta=\dfrac{400}{(9.8)(50)}=0.816\approx0.80\Rightarrow \theta\approx38.7°$.

> 💡 **(c) — Concept needed**: with friction, its direction depends on speed — too slow (friction **up** the slope) vs too fast (friction **down**); each case is two coupled equations. **Key insight**: both cases share one structure with a single sign flipped, giving $v_{\min}$ and $v_{\max}$. **If missed**: you force one equation onto both cases and get a bogus symmetric range.

**(c)** With friction $\mu_s=0.50$, $\sin\theta=0.625$, $\cos\theta=0.781$ (from $\tan\theta=0.80$).

**Too slow (friction up the slope).** Force balance perpendicular to the slope and radially:

$$N=mg\cos\theta+f\sin\theta,\qquad \frac{mv^2}{R}=N\sin\theta-f\cos\theta$$

with $f=\mu_sN$. Solving:

$$v_{\min}^2=gR\,\frac{\sin\theta-\mu_s\cos\theta}{\cos\theta+\mu_s\sin\theta}
=9.8(50)\,\frac{0.625-0.3905}{0.781+0.3125}=490\,\frac{0.2345}{1.0935}=105.1$$

$$v_{\min}=\sqrt{105.1}=10.3\ \text{m/s}$$

**Too fast (friction down the slope).** Now the friction term changes sign in the radial equation:

$$v_{\max}^2=gR\,\frac{\sin\theta+\mu_s\cos\theta}{\cos\theta-\mu_s\sin\theta}
=9.8(50)\,\frac{0.625+0.3905}{0.781-0.3125}=490\,\frac{1.0155}{0.4685}=1062$$

$$v_{\max}=\sqrt{1062}=32.6\ \text{m/s}$$

Range: $10.3\ \text{m/s}\le v\le 32.6\ \text{m/s}$. Note the range is not symmetric about the design speed — the bank makes it much easier to go fast than slow.

> 💡 **(d) — Concept needed**: at the design speed the normal alone supplies the centripetal force — friction contributes **zero**. **Key insight**: rain narrows only the allowed *range*; on a flat curve $v_{\max}\propto\sqrt{\mu_s}$. **If missed**: you think rain slows every banked curve uniformly.

**(d)** Flat curve: $v_{\max}=\sqrt{\mu_s gR}$ drops by factor $\sqrt{0.30/0.60}=0.707$: $17.1\to12.1$ m/s. A banked curve at the design speed needs **no friction at all**, so rain doesn't change the safe speed at $v=\sqrt{gR\tan\theta}$ — only the *range* around it narrows.

---

## Problem A4 — The Ball That Swings in a Circle

> 💡 **Key insight**: Combine the **radial $F=ma$ at each point with energy conservation**. Trying to get the acceleration kinematically at every instant (non-uniform circular motion) leads to a differential equation and an exploding solution. Clean results like the constant $3mg$ in (c) come straight out of this combination.

> 💡 **(a) — Concept needed**: radial Newton's 2nd law at the bottom + energy conservation to relate $v_b$ and $v_t$. **Key insight**: $T_b-mg=mv_b^2/L$ and $v_t^2=v_b^2-4gL$. **If missed**: kinematic acceleration for non-uniform circular motion becomes a differential equation and explodes.

**(a)** At the bottom, radial $F=ma$:

$$T_b-mg=\frac{mv_b^2}{L}\;\Rightarrow\; T_b=m\left(g+\frac{v_b^2}{L}\right)=2\left(9.8+\frac{81}{1.5}\right)=2(63.8)=127.6\ \text{N}$$

Energy from bottom to top (height gain $2L$):

$$v_t^2=v_b^2-4gL=81-4(9.8)(1.5)=81-58.8=22.2\;\Rightarrow\; v_t=4.71\ \text{m/s}$$

At the top, both tension and weight point down (radially inward):

$$T_t+mg=\frac{mv_t^2}{L}\;\Rightarrow\; T_t=m\left(\frac{v_t^2}{L}-g\right)=2\left(\frac{22.2}{1.5}-9.8\right)=2(5.0)=10.0\ \text{N}$$

> 💡 **(b) — Concept needed**: the string stays taut only while $T_t\ge0$ at the top. **Key insight**: $v_t\ge\sqrt{gL}$, and energy back-transfers to $v_b=\sqrt{5gL}$. **If missed**: you allow negative tension — the ball leaves the circle — and get an impossible speed.

**(b)** Taut condition at top: $T_t\ge0 \Rightarrow v_t^2\ge gL$.

$$v_{t,\min}=\sqrt{gL}=\sqrt{(9.8)(1.5)}=\sqrt{14.7}=3.83\ \text{m/s}$$

Energy: $v_b^2=v_t^2+4gL=gL+4gL=5gL$:

$$v_{b,\min}=\sqrt{5gL}=\sqrt{73.5}=8.57\ \text{m/s}$$

> 💡 **(c) — Concept needed**: energy from the horizontal release — the ball drops a full $L$. **Key insight**: $v_b^2=2gL$ makes $T_b=mg+2mg=3mg$, **independent of $L$**. **If missed**: you compute a number but lose the beautiful $L$-independent $3mg$ fact.

**(c)** Released from the horizontal: bottom speed from energy $v_b^2=2gL$.

$$v_b=\sqrt{2gL}=\sqrt{29.4}=5.42\ \text{m/s},\qquad T_b=mg+\frac{mv_b^2}{L}=mg+2mg=3mg=58.8\ \text{N}$$

The $L$ cancels: for a ball released from the side, the tension at the bottom is always $3mg$, because $v_b^2/L=2g$ regardless of $L$.

> 💡 **(d) — Concept needed**: energy for a release from angle $\theta_0$ — the drop is $L(1-\cos\theta_0)$. **Key insight**: $T_b=mg(3-2\cos\theta_0)$ reproduces both the (c) result and the rest-at-bottom check. **If missed**: a sign slip on $\cos\theta_0$ flips the $\theta_0=120°$ answer.

**(d)** Released from rest at angle $\theta_0$ from the bottom. Height dropped by the bottom $=L(1-\cos\theta_0)$:

$$v_b^2=2gL(1-\cos\theta_0)\;\Rightarrow\; T_b=mg+\frac{mv_b^2}{L}=mg+2mg(1-\cos\theta_0)=mg(3-2\cos\theta_0)$$

Checks: $\theta_0=90°\Rightarrow T_b=mg(3-0)=3mg$ ✓; $\theta_0=0°\Rightarrow T_b=mg(3-2)=mg$ ✓. For $\theta_0=120°$: $\cos\theta_0=-\tfrac12$,

$$T_b=mg(3+1)=4mg=4(2.0)(9.8)=78.4\ \text{N}$$

---

## Problem A5 — The Hill, the Dip, and the Feeling in Your Stomach

> 💡 **Key insight**: Apparent weight is the normal force $N$, and the sign of $\pm mv^2/R$ is set by the **direction of the centripetal acceleration** (down over the hump, up in the dip). Skip the sign analysis and you'll use the same equation for both, flipping the answers. The (d) conclusion that you can never feel weightless in the dip also comes from here.

> 💡 **(a) — Concept needed**: apparent weight = normal force $N$; over a hump the centripetal acceleration points **down**. **Key insight**: $mg-N=mv^2/R$, so $N=m(g-v^2/R)<mg$. **If missed**: you add instead of subtract and report a normal *larger* than the weight.

**(a)** At the top of the hump, $N$ points up, $mg$ points down, and both the required centripetal acceleration $v^2/R$ is down:

$$mg-N=\frac{mv^2}{R}\;\Rightarrow\; N=m\left(g-\frac{v^2}{R}\right)=1200\left(9.8-\frac{100}{30}\right)=1200(6.47)=7760\ \text{N}$$

> 💡 **(b) — Concept needed**: losing contact means $N=0$. **Key insight**: $v=\sqrt{gR}$ — beyond that, car and driver are in free fall. **If missed**: you never set $N=0$ and can't find the threshold speed.

**(b)** Lose contact when $N=0$: $v=\sqrt{gR}=\sqrt{(9.8)(30)}=\sqrt{294}=17.1$ m/s. The driver feels weightless — the car and driver are both in free fall over the crest.

> 💡 **(c) — Concept needed**: in a dip the centripetal acceleration points **up**. **Key insight**: $N-mg=mv^2/R$, so $N=m(g+v^2/R)>mg$. **If missed**: reusing the hump sign makes the dip feel light instead of heavy.

**(c)** In the dip, the centripetal acceleration points up:

$$N-mg=\frac{mv^2}{R}\;\Rightarrow\; N=m\left(g+\frac{v^2}{R}\right)=1200\left(9.8+3.33\right)=15760\ \text{N}$$

> 💡 **(d) — Concept needed**: compare $N$ across locations; weightlessness requires $N=0$. **Key insight**: in the dip $N>mg$ always, so weightlessness is impossible there; over the hump it happens exactly at $v^2=gR$. **If missed**: you can't justify why you can never float in a dip.

**(d)** Heaviest in the dip ($N=15760$ N > weight $11760$ N), lightest over the hump ($N=7760$ N). The apparent weight is $N$ itself. Weightlessness over the hump happens exactly when $v^2=gR$; in the dip you can never feel weightless (the car pushes *up* harder than $mg$).

---

# Part B — Linear Momentum

## Problem B1 — The Cannon That Punches Back

> 💡 **Key insight**: Split the process into **phases** — momentum conservation (horizontal) at the instant of firing, then friction work = loss of kinetic energy while sliding. Without the split, you try to handle all forces at once and the equations entangle. You also need the (b) insight that the vertical component is absorbed by the ground.

> 💡 **(a) — Concept needed**: conservation of (horizontal) momentum — the external forces (weight, ground) act vertically. **Key insight**: $0=MV+mv$ gives the recoil $V=mv/M$. **If missed**: you try to conserve total energy (wrong — an explosion) or conserve vertical momentum (the ground absorbs it).

**(a)** Conservation of horizontal momentum (cannon + shell):

$$0=M V+m v\;\Rightarrow\; V=\frac{m v}{M}=\frac{(10)(300)}{800}=3.75\ \text{m/s}$$

> 💡 **(b) — Concept needed**: only the **horizontal** component of the shell's momentum is conserved. **Key insight**: $0=MV+mv\cos30°$, so firing at an angle weakens the recoil. **If missed**: you conserve the full vector momentum and invent a vertical recoil the ground vetoes.

**(b)** At $30°$, only the horizontal component matters:

$$0=MV+mv\cos30°\;\Rightarrow\; V=\frac{(10)(300)(0.866)}{800}=3.25\ \text{m/s}$$

The vertical component of the shell's momentum is given to the **ground** through the normal force during firing — momentum is conserved for the cannon+shell+Earth system vertically, but the Earth is too massive to notice.

> 💡 **(c) — Concept needed**: work–energy with kinetic friction: $\tfrac12MV^2=\mu_k Mg\,d$. **Key insight**: friction is the only horizontal force after firing; $M$ cancels, so $d=V^2/(2\mu_kg)$. **If missed**: you keep the recoil force acting during the slide and double-count.

**(c)** After the shot, only kinetic friction does work (cannon slides with no external horizontal force other than friction):

$$\tfrac12 M V^2=\mu_k M g\,d\;\Rightarrow\; d=\frac{V^2}{2\mu_k g}=\frac{(3.75)^2}{2(0.20)(9.8)}=\frac{14.06}{3.92}=3.59\ \text{m}$$

> 💡 **(d) — Concept needed**: uniform acceleration $v^2=2aL$ and impulse–momentum $J=F_{\text{avg}}t=\Delta p$. **Key insight**: $F_{\text{avg}}=ma$ and $J=mv$ — the impulse equals the shell's momentum change. **If missed**: you confuse impulse (force×time) with work (force×distance).

**(d)** Uniform acceleration down a $L=2.0$ m barrel: $v^2=2aL$, so

$$a=\frac{v^2}{2L}=\frac{(300)^2}{2(2.0)}=22500\ \text{m/s}^2,\qquad t=\frac{v}{a}=\frac{300}{22500}=0.0133\ \text{s}$$

$$F_{\text{avg}}=m a=(10)(22500)=2.25\times10^5\ \text{N}$$

Impulse: $J=F_{\text{avg}}t=(2.25\times10^5)(0.0133)=3000$ N·s $=mv=10\cdot300$ ✓ — impulse equals the shell's momentum change, as required by impulse–momentum.

---

## Problem B2 — The Firework That Divides

> 💡 **Key insight**: The explosion is an **internal** force, so momentum is conserved even though energy is released. Also, both pieces start at the same height with zero vertical velocity, so they land **simultaneously**. Forcing energy conservation while the explosion energy is unknown leaves you stuck with an unsolvable equation.

> 💡 **(a) — Concept needed**: momentum conservation even when energy is released — the explosion forces are **internal**. **Key insight**: $0=m_1v_1+m_2v_2$, so $v_2=-(m_1/m_2)v_1$. **If missed**: you try energy conservation while the chemical energy is unknown, and the problem is unsolvable.

**(a)** At the top, total momentum is zero. Conservation of momentum:

$$0=m_1v_1+m_2v_2\;\Rightarrow\; v_2=-\frac{m_1}{m_2}v_1=-\frac{1.0}{2.0}(40)=-20\ \text{m/s}$$

Piece 2 moves to the **left** at $20$ m/s. The principle applies even though chemical energy is released because the explosion forces are **internal** — no external force acts on the (already-split) system during the explosion, and momentum is conserved regardless of energy.

> 💡 **(b) — Concept needed**: kinetic energy before vs after; energy is **not** conserved in an explosion. **Key insight**: the extra 1200 J is the chemical potential energy converted to KE. **If missed**: you treat the explosion as elastic and get $v_2$ wrong.

**(b)** $KE_{\text{before}}=0$ (top of flight). After:

$$KE=\tfrac12(1.0)(40)^2+\tfrac12(2.0)(20)^2=800+400=1200\ \text{J}$$

The extra $1200$ J comes from the **chemical potential energy** of the explosive.

> 💡 **(c) — Concept needed**: projectile motion — both pieces start at the same height with **zero vertical velocity**. **Key insight**: equal fall time $t=\sqrt{2h/g}$, so both land **simultaneously** on opposite sides. **If missed**: you let the horizontal speeds affect the fall time.

**(c)** Both pieces start at height $h=80$ m; piece 1 falls straight down from rest horizontally:

$$t_1=\sqrt{\frac{2h}{g}}=\sqrt{\frac{160}{9.8}}=4.04\ \text{s},\qquad x_1=v_1t_1=40(4.04)=161.6\ \text{m}$$

Piece 2 also starts at $h$ with zero vertical velocity:

$$t_2=t_1=4.04\ \text{s},\qquad x_2=v_2t_2=-20(4.04)=-80.8\ \text{m}$$

Both hit the ground simultaneously (same vertical initial velocity, same height) — on opposite sides of the explosion point.

> 💡 **(d) — Concept needed**: vector momentum conservation in 2D — momenta add as vectors, forming a closed triangle. **Key insight**: $\vec p_C=-(\vec p_A+\vec p_B)=-30\hat x-40\hat y$, so $v_C=50$ m/s at $53°$ below $-x$. **If missed**: you add the magnitudes and get 70 m/s.

**(d)** Three equal pieces, total momentum zero: $\vec p_C=-(\vec p_A+\vec p_B)$.

$$\vec p_A=1.0(30\,\hat x),\qquad \vec p_B=1.0(40\,\hat y)$$
$$\vec p_C=-30\hat x-40\hat y\;\Rightarrow\; v_C=\sqrt{30^2+40^2}=50\ \text{m/s}$$

Direction: $\tan\phi=40/30$, $\phi=53°$ **below** the $-x$ axis. The three momentum vectors sum to zero — they form a closed triangle.

---

## Problem B3 — The Bullet and the Block on Strings

> 💡 **Key insight**: **Separate the collision (inelastic → momentum only) from the subsequent swing (energy)**. Applying energy conservation to the collision (99% is lost as heat) gives a completely wrong answer. The rebound case in (d) also collapses quickly with the same two-phase structure.

> 💡 **(a) — Concept needed**: energy conservation **after** the collision — the block+bullet rises and stops. **Key insight**: $\tfrac12(m+M)v^2=(m+M)gh \Rightarrow v=\sqrt{2gh}$. **If missed**: you apply energy *through* the collision (invalid — it's inelastic) and get the wrong $v$.

**(a)** Energy after collision (block+bullet rises $h$, stops at top):

$$\tfrac12(m+M)v^2=(m+M)gh\;\Rightarrow\; v=\sqrt{2gh}=\sqrt{2(9.8)(0.20)}=\sqrt{3.92}=1.98\ \text{m/s}$$

> 💡 **(b) — Concept needed**: momentum conservation **during** the (impulsive, inelastic) collision. **Key insight**: $mv_b=(m+M)v \Rightarrow v_b=\tfrac{m+M}{m}v$. **If missed**: you use energy here and 'lose' ~99% to heat — the classic ballistic-pendulum trap.

**(b)** Momentum during collision:

$$m v_b=(m+M)v\;\Rightarrow\; v_b=\frac{m+M}{m}v=\frac{2.02}{0.020}(1.98)=101(1.98)=200\ \text{m/s}$$

> 💡 **(c) — Concept needed**: compute KE before vs after and take the ratio. **Key insight**: $(400-3.96)/400\approx99\%$ is converted to heat and deformation. **If missed**: you assume a 'perfect' collision and never quantify the loss.

**(c)** $KE_{\text{before}}=\tfrac12(0.020)(200)^2=400$ J. $KE_{\text{after}}=\tfrac12(2.02)(1.98)^2=3.96$ J. Lost fraction:

$$\frac{400-3.96}{400}=0.99=99\%$$

Essentially all the bullet's kinetic energy goes into heating/deforming the block and bullet.

> 💡 **(d) — Concept needed**: a rebound flips the bullet's velocity sign in the momentum equation; then energy gives the height. **Key insight**: $mv_b=m(-50)+MV \Rightarrow V=2.5$ m/s and $h=V^2/2g=0.319$ m. **If missed**: you forget the negative sign or reuse the (b) embedding equation.

**(d)** Bullet rebounds at $v_b/4=50$ m/s (opposite direction). Momentum:

$$m v_b=m(-50)+M V\;\Rightarrow\; 0.020(200)=-1.0+2.00V\;\Rightarrow\; V=2.5\ \text{m/s}$$

$$h=\frac{V^2}{2g}=\frac{(2.5)^2}{2(9.8)}=\frac{6.25}{19.6}=0.319\ \text{m}$$

The block rises higher because the rebounding bullet carries away *less* energy (its KE after is $\tfrac12(0.020)(50)^2=25$ J vs. 0 for the embedding case), leaving more for the block.

---

## Problem B4 — The Perfect Two-Dimensional Collision

> 💡 **Key insight**: For a 2D collision, **split into x/y components** and use momentum conservation; (d) asks you to show that equal-mass elastic collisions give $\vec v_1\cdot\vec v_2=0$ (final velocities perpendicular). Handling the vectors whole, without components, drags the proof out.

> 💡 **(a) — Concept needed**: 2D momentum conservation split into **x and y components**. **Key insight**: two equations, two unknowns ($v_2,\theta_2$); divide $y$ by $x$ to get $\tan\theta_2$. **If missed**: you try to solve the vector equation as a whole and get stuck.

**(a)** Take $+x$ along the initial motion, $+y$ upward. Momentum:

$$x:\ m v_0=m v_1\cos37°+m v_2\cos\theta_2\;\Rightarrow\; 5.0=4.0(0.80)+v_2\cos\theta_2\;\Rightarrow\; v_2\cos\theta_2=1.8$$
$$y:\ 0=m v_1\sin37°-m v_2\sin\theta_2\;\Rightarrow\; v_2\sin\theta_2=4.0(0.60)=2.4$$

Divide: $\tan\theta_2=\dfrac{2.4}{1.8}=1.333\Rightarrow\theta_2=53°$ below the $+x$ axis. Then

$$v_2=\sqrt{1.8^2+2.4^2}=\sqrt{9}=3.0\ \text{m/s}$$

> 💡 **(b) — Concept needed**: kinetic-energy comparison to test elasticity. **Key insight**: KE before = KE after = 6.25 J → **elastic**. **If missed**: you assume elasticity without checking, or compare only speed magnitudes.

**(b)** $KE_{\text{before}}=\tfrac12(0.50)(5.0)^2=6.25$ J.
$KE_{\text{after}}=\tfrac12(0.50)(4.0)^2+\tfrac12(0.50)(3.0)^2=4.0+2.25=6.25$ J ✓ — elastic.

> 💡 **(c) — Concept needed**: angles are measured from the original direction of motion. **Key insight**: $37°+53°=90°$ — the two final velocities are **perpendicular**. **If missed**: you add the angles to the wrong reference line.

**(c)** The final velocities make angles $37°$ and $53°$ on opposite sides of the original line; $37°+53°=90°$. The angle between them is $90°$.

> 💡 **(d) — Concept needed**: for equal masses, momentum gives $\vec v_0=\vec v_1+\vec v_2$ and energy gives $v_0^2=v_1^2+v_2^2$. **Key insight**: squaring the momentum equation and subtracting the energy equation yields $\vec v_1\cdot\vec v_2=0$. **If missed**: you can't see that the $90°$ result is **general** (not a coincidence of the numbers).

**(d)** General proof: mass $m$ at $\vec v_0$ hits identical mass at rest; final velocities $\vec v_1,\vec v_2$. Momentum and energy:

$$\vec v_0=\vec v_1+\vec v_2,\qquad v_0^2=v_1^2+v_2^2$$

Square the momentum equation: $v_0^2=v_1^2+v_2^2+2\vec v_1\cdot\vec v_2$. Subtract the energy equation: $2\vec v_1\cdot\vec v_2=0$, so $\vec v_1\cdot\vec v_2=0$ — the final velocities are **perpendicular**, for any elastic equal-mass collision with one target initially at rest. (Unless one piece stops entirely, the trivial case.)

---

## Problem B5 — The Train That Couples, Couples, Couples

> 💡 **Key insight**: Treat each coupling as an **inelastic collision**, update the speed by momentum conservation, and **generalize by induction** to $v_n=v_0/n$. Energy conservation fails every time (heat is produced), and grinding through the five couplings one by one without induction is far longer.

> 💡 **(a) — Concept needed**: a completely inelastic collision conserves **momentum only**. **Key insight**: each coupling divides $v$ by the new car count, so $v_n=v_0/n$. **If missed**: you use energy (fails — heat) or compute each coupling separately instead of spotting the pattern.

**(a)** First coupling (momentum): $m v_0=2m v_2\Rightarrow v_2=v_0/2=1.5$ m/s.
Second coupling: $2m v_2=3m v_3\Rightarrow v_3=\tfrac23 v_2=v_0/3=1.0$ m/s.
Pattern: $v_n=v_0/n$.

> 💡 **(b) — Concept needed**: proof by induction. **Key insight**: assume $v_{n-1}=v_0/(n-1)$; then $(n-1)m\,v_{n-1}=nm\,v_n$ gives $v_n=v_0/n$. **If missed**: without induction you can't justify the pattern for *all* $n$.

**(b)** Induction: suppose $n-1$ cars move at $v_{n-1}=v_0/(n-1)$. Coupling to car $n$:

$$(n-1)m\,v_{n-1}=n m\,v_n\;\Rightarrow\; v_n=\frac{n-1}{n}v_{n-1}=\frac{n-1}{n}\cdot\frac{v_0}{n-1}=\frac{v_0}{n}$$

> 💡 **(c) — Concept needed**: kinetic energy of the coupled train after $n$ couplings. **Key insight**: the remaining fraction is exactly $1/n$ — here $1/5=20\%$, so 36,000 J is lost. **If missed**: you subtract KE car by car and miss that each coupling already accounts for the loss.

**(c)** After 5 cars: $v_5=v_0/5=0.6$ m/s. Energy remaining:

$$\frac{\tfrac12(5m)v_5^2}{\tfrac12 m v_0^2}=\frac{5m(v_0/5)^2}{m v_0^2}=\frac{1}{5}=20\%$$

Original $KE=\tfrac12(10^4)(3)^2=45000$ J; remaining $\tfrac15=9000$ J; lost $36000$ J to heat, sound, and permanent deformation of the couplings.

> 💡 **(d) — Concept needed**: ratio of KE before/after the $k$-th coupling. **Key insight**: the ratio is $(k-1)/k$ — the first coupling ($k=2$) destroys **half**. **If missed**: you assume every coupling destroys the same fraction.

**(d)** Just before the $k$-th coupling, $k-1$ cars move at $v_{k-1}=v_0/(k-1)$ with $KE_{\text{before}}=\tfrac12(k-1)m v_{k-1}^2$. Just after, $k$ cars move at $v_k=v_0/k$:

$$KE_{\text{after}}=\tfrac12 k m\, v_k^2=\tfrac12 km\frac{v_0^2}{k^2}=\frac{mv_0^2}{2k},\qquad KE_{\text{before}}=\tfrac12(k-1)m\frac{v_0^2}{(k-1)^2}=\frac{mv_0^2}{2(k-1)}$$

Ratio: $\dfrac{KE_{\text{after}}}{KE_{\text{before}}}=\dfrac{k-1}{k}$. So each coupling destroys exactly $1/k$ of the energy present before it — for the *first* coupling ($k=2$), that's $1/2$: half the energy is destroyed by the very first hit. This is the signature of a completely inelastic collision: relative kinetic energy is converted to internal energy, and the "lost" fraction is largest when the relative speed is largest (the first coupling).

---

# Part C — Rotation of a Rigid Body

## Problem C1 — The Flywheel That Stores Energy

> 💡 **Key insight**: In rotation, $\tau=I\alpha$, $KE=\tfrac12I\omega^2$, and $W=\tau\theta=\Delta KE$ are **exactly parallel** to their linear counterparts. Without this analogy you re-derive every part from force/kinematics from scratch — much longer.

> 💡 **(a) — Concept needed**: moment of inertia of a solid disk $I=\tfrac12MR^2$ and the rotational 2nd law $\tau=I\alpha$. **Key insight**: $\alpha=\tau/I$ is the exact analogue of $a=F/m$. **If missed**: you invent an 'effective mass' or write $\tau=m\alpha$.

**(a)** $I=\tfrac12MR^2=\tfrac12(2.0)(0.50)^2=0.25$ kg·m². Rotational Newton's 2nd law:

$$\alpha=\frac{\tau}{I}=\frac{5.0}{0.25}=20\ \text{rad/s}^2$$

> 💡 **(b) — Concept needed**: rotational kinematics under constant $\alpha$: $\omega=\alpha t$ and $\theta=\tfrac12\alpha t^2$. **Key insight**: plug in directly; convert radians to revolutions. **If missed**: you integrate from scratch or forget the $\tfrac12$ in $\theta$.

**(b)** $\omega=\alpha t=(20)(10)=200$ rad/s. Angle: $\theta=\tfrac12\alpha t^2=\tfrac12(20)(100)=1000$ rad $=\dfrac{1000}{2\pi}=159$ rev.

> 💡 **(c) — Concept needed**: rotational kinetic energy $KE=\tfrac12I\omega^2$. **Key insight**: $KE=\tfrac12(0.25)(200)^2=5000$ J. **If missed**: you write $\tfrac12mv^2$ with an undefined 'v'.

**(c)** $KE=\tfrac12I\omega^2=\tfrac12(0.25)(200)^2=5000$ J.

> 💡 **(d) — Concept needed**: rotational work $W=\tau\theta$ and the rotational work–energy theorem. **Key insight**: $W=\tau\theta=\Delta(\tfrac12I\omega^2)=5000$ J — the linear theorem in disguise. **If missed**: you can't justify where the 5000 J came from.

**(d)** $W=\tau\theta=(5.0)(1000)=5000$ J $=KE$ ✓. Rotational work–energy theorem: $W_{\text{net}}=\Delta(\tfrac12I\omega^2)$, the exact analogue of $W_{\text{net}}=\Delta(\tfrac12mv^2)$. The rotational analogues: $\tau\leftrightarrow F$, $\theta\leftrightarrow x$, $\omega\leftrightarrow v$, $\alpha\leftrightarrow a$, $I\leftrightarrow m$.

---

## Problem C2 — Two Disks, One Spin

> 💡 **Key insight**: A rotational collision is the analogue of a linear inelastic one — **angular momentum is conserved, energy is not** (heat is produced at the instant of locking). Using energy conservation runs straight into a contradiction (80 J ≠ 32 J).

> 💡 **(a) — Concept needed**: conservation of angular momentum when no external torque acts. **Key insight**: $I_1\omega_1=(I_1+I_2)\omega_f \Rightarrow \omega_f=8$ rad/s. **If missed**: you use energy (invalid — locking dissipates heat) and get a different $\omega_f$.

**(a)** Conservation of angular momentum (no external torque):

$$I_1\omega_1=(I_1+I_2)\omega_f\;\Rightarrow\; \omega_f=\frac{(0.40)(20)}{1.00}=8\ \text{rad/s}$$

> 💡 **(b) — Concept needed**: rotational KE before/after — an inelastic *rotational* collision. **Key insight**: 80 J → 32 J, losing 60% — the rotational twin of Problem B5. **If missed**: you expect KE conserved and the numbers look 'wrong'.

**(b)** $KE_{\text{before}}=\tfrac12(0.40)(20)^2=80$ J. $KE_{\text{after}}=\tfrac12(1.00)(8)^2=32$ J. Lost $48$ J, fraction $48/80=0.60=60\%$.

This mirrors the linear inelastic collision of **Problem B5**: kinetic energy is lost while momentum (angular momentum) is conserved. The difference: here the "masses" ($I$) add directly, and the lost energy is dissipated in the clutch surfaces as heat.

> 💡 **(c) — Concept needed**: a sign convention for opposite spins. **Key insight**: $\omega_2=-10$, so $\omega_f=(I_1\omega_1+I_2\omega_2)/(I_1+I_2)=2$ rad/s. **If missed**: adding magnitudes gives the wrong (slower-but-opposite) answer.

**(c)** Disk 2 spins opposite at $10$ rad/s (take it negative):

$$\omega_f=\frac{I_1\omega_1+I_2\omega_2}{I_1+I_2}=\frac{0.40(20)+0.60(-10)}{1.00}=\frac{8-6}{1.00}=2\ \text{rad/s}$$

The pair spins slowly in disk 1's original direction.

> 💡 **(d) — Concept needed**: where the 'lost' energy goes; an elastic coupling would have to conserve *both* $L$ and $KE$. **Key insight**: heat in the clutch — locking can't be elastic. **If missed**: you think the energy simply vanishes.

**(d)** The "lost" rotational KE becomes thermal energy in the clutch/contact surfaces during the locking. If the coupling were perfectly elastic, angular momentum would still be conserved but the disks could not lock — they would exchange energy through a lossless interaction and end with different speeds satisfying both $L$ and $KE$ conservation (like an elastic collision in rotation).

---

## Problem C3 — The Race Down the Hill

> 💡 **Key insight**: Split the rolling energy into $KE=\tfrac12mv^2+\tfrac12I\omega^2$ and substitute $\omega=v/R$. Miss this (or wrongly think friction does work) and you get tangled in forces and the no-slip condition — very long. The conclusion that mass and radius cancel also falls out of this equation.

> 💡 **(a) — Concept needed**: rolling KE = translational + rotational, with $\omega=v/R$ (no slip). **Key insight**: $v=\sqrt{2gh/(1+I/mR^2)}$ — mass and radius cancel. **If missed**: you write $KE=\tfrac12mv^2$ only (forgetting rotation) and get free-fall speed.

**(a)** Rolling: $KE=\tfrac12mv^2+\tfrac12I\omega^2$, with $\omega=v/R$ (no slip). Energy:

$$mgh=\tfrac12mv^2+\tfrac12I\frac{v^2}{R^2}=\tfrac12mv^2\left(1+\frac{I}{mR^2}\right)\;\Rightarrow\; v=\sqrt{\frac{2gh}{1+I/mR^2}}$$

- Hoop, $I/mR^2=1$: $v=\sqrt{gh}=\sqrt{9.8}=3.13$ m/s
- Disk, $I/mR^2=\tfrac12$: $v=\sqrt{2gh/1.5}=\sqrt{13.07}=3.61$ m/s
- Sphere, $I/mR^2=\tfrac25$: $v=\sqrt{2gh/1.4}=\sqrt{14}=3.74$ m/s

> 💡 **(b) — Concept needed**: a smaller $I/mR^2$ means less energy diverted into rotation → more into linear motion. **Key insight**: sphere ($\tfrac25$) beats disk ($\tfrac12$) beats hoop ($1$); mass and radius cancel entirely. **If missed**: you rank by mass or radius, which cancel.

**(b)** The **sphere wins** (smallest $I/mR^2$), the hoop loses. The smaller the moment of inertia, the less energy is diverted into rotation, so more goes into linear motion. Mass and radius cancel out of $v$ entirely — a big solid sphere and a tiny solid sphere roll with identical speeds.

> 💡 **(c) — Concept needed**: a frictionless slide never spins, so all energy goes to translation; and rolling friction does **no work** (the contact point is instantaneously at rest). **Key insight**: $v=\sqrt{2gh}$ is the fastest of all — friction *converts* translational energy into rotational, without doing work. **If missed**: you think friction slows rolling by doing negative work.

**(c)** Frictionless slide: no rotation, $mgh=\tfrac12mv^2\Rightarrow v=\sqrt{2gh}=\sqrt{19.6}=4.43$ m/s — the fastest of all. Rolling is slower because some of the gravitational energy must spin the object up. Friction itself does no work (the contact point is instantaneously at rest, so $W_f=f\cdot0=0$) — it merely *converts* translational energy into rotational energy.

> 💡 **(d) — Concept needed**: the no-slip condition $f\le\mu_s mg\cos\theta$, with rolling $a=g\sin\theta/(1+I/mR^2)$. **Key insight**: $\mu_s\ge\frac{I/mR^2}{1+I/mR^2}\tan\theta$ — the hoop needs the most grip. **If missed**: you set $f=\mu N$ for the rolling case and over-constrain.

**(d)** For rolling, $a=\dfrac{g\sin\theta}{1+I/mR^2}$ and friction $f=I\alpha/R^2=I a/R^2=(I/mR^2)ma$. No-slip requires $f\le\mu_s mg\cos\theta$:

$$\mu_s\ge\frac{I/mR^2}{1+I/mR^2}\,\tan\theta$$

With $\tan30°=0.577$:
- Hoop: $\mu_s\ge\dfrac{1}{2}(0.577)=0.289$
- Disk: $\mu_s\ge\dfrac{0.5}{1.5}(0.577)=0.192$
- Sphere: $\mu_s\ge\dfrac{0.4}{1.4}(0.577)=0.165$

The **hoop** needs the grippiest surface; the sphere the least.

---

## Problem C4 — The Falling Rod

> 💡 **Key insight**: The weight acts at the **center of mass ($L/2$ from the pivot)**, so the torque arm is $L/2$ and the CM drops $L/2$ in the energy equation. Using $L$ as the arm doubles the torque and breaks the answer; solving by rotational kinematics instead of energy is much longer.

> 💡 **(a) — Concept needed**: moment of inertia of a uniform rod about its **end**: $I=\tfrac13mL^2$. **Key insight**: $I=\tfrac13(3)(2)^2=4.0$ kg·m². **If missed**: you use $I=\tfrac{1}{12}mL^2$ (about the CM) and everything downstream is wrong.

**(a)** $I=\tfrac13mL^2=\tfrac13(3.0)(2.0)^2=4.0$ kg·m².

> 💡 **(b) — Concept needed**: torque = force × perpendicular arm; the rod's weight acts at the **CM**. **Key insight**: the arm is $L/2$, not $L$: $\tau=mgL/2$. **If missed**: doubling the arm doubles $\tau$ and $\alpha$.

**(b)** The weight acts at the center of mass, distance $L/2$ from the pivot:

$$\tau=mg\frac{L}{2}=(3.0)(9.8)(1.0)=29.4\ \text{N·m},\qquad \alpha=\frac{\tau}{I}=\frac{29.4}{4.0}=7.35\ \text{rad/s}^2$$

The weight is "effectively applied" at the center of mass — that's why the torque arm is $L/2$, not $L$.

> 💡 **(c) — Concept needed**: energy conservation with the **CM** dropping only $L/2$. **Key insight**: $mg(L/2)=\tfrac12I\omega^2 \Rightarrow \omega=\sqrt{mgL/I}$. **If missed**: you use the tip's drop $L$ and get $\omega$ too large by $\sqrt2$.

**(c)** Energy: the CM drops $L/2$.

$$mg\frac{L}{2}=\tfrac12 I\omega^2\;\Rightarrow\; \omega=\sqrt{\frac{mgL}{I}}=\sqrt{\frac{(3.0)(9.8)(2.0)}{4.0}}=\sqrt{14.7}=3.83\ \text{rad/s}$$

> 💡 **(d) — Concept needed**: $v=\omega r$ for a point on a rotating body, and comparison with free fall. **Key insight**: $v_{\text{tip}}=\omega L > \sqrt{2gL}$ because the CM falls only $L/2$ while the tip sweeps a full $L$. **If missed**: you conclude the tip can't beat free fall — energy seems to appear from nowhere.

**(d)** Tip speed: $v_{\text{tip}}=\omega L=(3.83)(2.0)=7.67$ m/s. A point mass falling from height $L$: $v=\sqrt{2gL}=\sqrt{39.2}=6.26$ m/s. The tip is **faster** because the pivot is fixed — the tip travels a full $L$ while the center of mass only falls $L/2$, yet all the gravitational energy (from the CM's $L/2$ drop) is converted to rotation. The tip "beats" free fall.

---

## Problem C5 — The Skater, the Platform, and Where the Energy Comes From

> 💡 **Key insight**: **Angular momentum conservation does not imply energy conservation** — the KE increase is the work done by the skater's muscles. Forcing energy conservation gives the contradiction 8 J ≠ 32 J. Without the 'rotational battery' view, the +1080 J in (d) makes no sense.

> 💡 **(a) — Concept needed**: conservation of angular momentum with no external torque. **Key insight**: $I_1\omega_1=I_2\omega_2 \Rightarrow \omega_2=(I_1/I_2)\omega_1=8$ rad/s. **If missed**: you conserve energy (invalid — muscles do work) and get a different $\omega$.

**(a)** Conservation of angular momentum:

$$I_1\omega_1=I_2\omega_2\;\Rightarrow\; \omega_2=\frac{4.0}{1.0}(2.0)=8\ \text{rad/s}$$

> 💡 **(b) — Concept needed**: rotational KE; energy is **not** conserved here. **Key insight**: KE jumps 8→32 J; the +24 J is muscular work pulling the arms in against the centrifugal tendency. **If missed**: you force energy conservation and hit a contradiction.

**(b)** $KE_1=\tfrac12(4.0)(2.0)^2=8$ J; $KE_2=\tfrac12(1.0)(8)^2=32$ J. The KE **increases by 24 J** even though no external torque acts. Angular momentum conservation says $I\omega=$ const; it does **not** say energy is conserved. The extra energy comes from the **muscular work** the skater does pulling her arms in against the centrifugal force. Angular momentum conservation and energy conservation are independent laws; here only the former holds (the system is not closed energetically — the skater is an internal energy source).

> 💡 **(c) — Concept needed**: moment of inertia of a point mass $I=mr^2$, added to the platform's. **Key insight**: $I_1=20+60=80$, so $\omega_2=(80/20)(3)=12$ rad/s. **If missed**: you fold the student into the platform's $I$ or forget the $\omega$ jump.

**(c)** Student at rim: $I_s=mr^2=(60)(1.0)^2=60$ kg·m². Total $I_1=I_p+I_s=80$ kg·m².

$$\omega_2=\frac{I_1}{I_2}\omega_0=\frac{80}{20}(3.0)=12\ \text{rad/s}$$

> 💡 **(d) — Concept needed**: work done to change $I$ while $L$ is fixed — the 'rotational battery'. **Key insight**: KE rises +1080 J (muscular work) and is *recovered* when the student walks back out. **If missed**: you can't explain where the energy comes from, or that it's reversible.

**(d)** $KE_1=\tfrac12(80)(3.0)^2=360$ J; $KE_2=\tfrac12(20)(12)^2=1440$ J. The increase, $+1080$ J, is work done by the student's muscles as they pull themselves inward against the "centrifugal" tendency to fly outward. If the student walks back out to the rim, $\omega$ drops back to $3.0$ rad/s and the KE returns to $360$ J — the student's muscles must now do **negative** work (absorb energy) to slow the spin, i.e., they resist being flung outward. The system is like a "rotational battery": energy is stored in the faster spin and can be recovered.

---

# Part D — Torque & Machines

## Problem D1 — The Seesaw That Asks Questions

> 💡 **Key insight**: Set up equilibrium as **sum of torques about the pivot = 0**; the uniform board's weight acts at its center (the pivot), contributing nothing. Resolving every force and using force balance instead brings in more unknowns and lengthens the work.

> 💡 **(a) — Concept needed**: torque = $rF\sin\theta$ with a sign convention (CCW positive), taken about the pivot. **Key insight**: the uniform board's weight acts at the pivot → zero arm; net $\tau=+98$ N·m. **If missed**: you treat the board's weight as off-center and get the wrong tipping direction.

**(a)** Take CCW positive. A at left end ($+$), B at right end ($-$):

$$\tau_{\text{net}}=(25)(9.8)(2.0)-(20)(9.8)(2.0)=490-392=+98\ \text{N·m}$$

A's side goes down. The board's weight acts at the pivot (center of mass of a uniform board is at its center), so its torque arm is zero — it contributes nothing.

> 💡 **(b) — Concept needed**: balance means net torque = 0. **Key insight**: $d_A=(20\cdot2.0)/25=1.6$ m; the board's length forbids moving B far enough. **If missed**: you give the symmetric answer 2.5 m that the board can't realize.

**(b)** Keep B at the end ($2.0$ m). Balance: $(25)(9.8)d_A=(20)(9.8)(2.0)$:

$$d_A=\frac{20\cdot2.0}{25}=1.6\ \text{m}$$

So A must sit $1.6$ m from the pivot (closer in). If instead A stays at the end and B moves: $d_B=(25)(9.8)(2.0)/(20)(9.8)=2.5$ m — but the board is only $2.0$ m long on B's side, so B **cannot** sit far enough out. The heavier child must sit closer to the pivot.

> 💡 **(c) — Concept needed**: three torques; solve for the position that restores balance. **Key insight**: restoring balance needs $d_A=2.4$ m. **If missed**: you get C's torque sign wrong — it adds to B's side, not against it.

**(c)** Torques with A at $1.6$ m and C on the right end:

$$\tau_{\text{net}}=(25)(9.8)(1.6)-(20)(9.8)(2.0)-(10)(9.8)(2.0)=392-392-196=-196\ \text{N·m}$$

Right side down. Restore balance by moving A outward:

$$(25)(9.8)d_A=392+196=588\;\Rightarrow\; d_A=\frac{588}{245}=2.4\ \text{m}$$

A must move out to $2.4$ m from the pivot.

> 💡 **(d) — Concept needed**: the board's own weight acts at its CM, an unknown distance $d$ from the pivot. **Key insight**: solve $490=392+98d \Rightarrow d=1.0$ m on B's side. **If missed**: you forget the board contributes any torque at all.

**(d)** Board CM displaced a distance $d$ from the pivot (on one side). With A at the left end and B at the right end:

$$(25)(9.8)(2.0)=(20)(9.8)(2.0)+(10)(9.8)d\;\Rightarrow\; 490=392+98d\;\Rightarrow\; d=1.0\ \text{m}$$

The board's center of mass must lie $1.0$ m to the **right** of the pivot — toward B's heavier side... (checking: B is *lighter* here, so the board's extra weight must sit on B's side to balance A). Yes: board CM $1.0$ m right of pivot.

---

## Problem D2 — The Wheelbarrow That Multiplies Force

> 💡 **Key insight**: Take torques about the **wheel (fulcrum)**: $Fb=Wa$. Force balance would drag in the ground reaction and lengthen the equations. The (d) conclusion that shortening the small arm $a$ beats lengthening the handles follows directly from $F\propto a$, $F\propto 1/b$.

> 💡 **(a) — Concept needed**: torques about the fulcrum (the wheel): $F\cdot b=W\cdot a$. **Key insight**: $F=W\cdot a/b=150$ N. **If missed**: you use force balance and drag in the ground reaction.

**(a)** Torques about the wheel (fulcrum): load at $a=0.40$ m, hands at $b=1.6$ m.

$$F b=W a\;\Rightarrow\; F=W\frac{a}{b}=600\frac{0.40}{1.6}=150\ \text{N}$$

> 💡 **(b) — Concept needed**: mechanical advantage = output force / input force = $b/a$. **Key insight**: $MA=1.6/0.40=4$ and $W/F=4$. **If missed**: you confuse MA with a ratio of distances along some other line.

**(b)** $MA=\dfrac{b}{a}=\dfrac{1.6}{0.40}=4$, and indeed $W/F=600/150=4$. The wheelbarrow multiplies your force by 4.

> 💡 **(c) — Concept needed**: include the body's weight acting at **its own CM**. **Key insight**: $F(1.6)=600(0.40)+98(0.60) \Rightarrow F=186.8$ N. **If missed**: you place the body's weight at the load or at the hands.

**(c)** Include the wheelbarrow body (mass $10$ kg, weight $98$ N) at $0.60$ m from the wheel:

$$F(1.6)=(600)(0.40)+(98)(0.60)=240+58.8=298.8\;\Rightarrow\; F=186.8\ \text{N}$$

> 💡 **(d) — Concept needed**: sensitivity analysis — $F\propto a$ but $F\propto1/b$. **Key insight**: moving the load 0.10 m closer saves 37.5 N, beating a 0.20 m handle extension (16.7 N). **If missed**: you can't rank the two improvements without the proportionality.

**(d)** Load moved to $a=0.30$ m: $F=600(0.30)/1.6=112.5$ N (down from $150$ N, a saving of $37.5$ N).

Compare with lengthening the handles to $b=1.8$ m (keeping $a=0.40$): $F=600(0.40)/1.8=133.3$ N (saving $16.7$ N). Moving the load $0.10$ m closer saves more than lengthening the handles $0.20$ m — because $F\propto a$ while $F\propto1/b$; a small change in the small arm $a$ packs more leverage.

---

## Problem D3 — The Ladder That Wants to Slip

> 💡 **Key insight**: Take torques about the **foot** so the unknowns $N_g$ and $f$ drop out. Choosing another axis (e.g., the wall contact) leaves two extra unknowns and longer equations. Also read the horizontal distance ($1.5$ m) and wall height ($4.0$ m) straight off the 3–4–5 triangle.

> 💡 **(a) — Concept needed**: static equilibrium (forces + torques); choose the axis to eliminate unknowns. **Key insight**: torques about the **foot** kill $N_g$ and $f$: $N_w(4.0)=mg(1.5)$. **If missed**: with another axis you solve 3 equations instead of 1.

**(a)** Forces: $N_w$ horizontal at the top (frictionless wall), $N_g$ up and $f$ horizontal at the foot, weight $mg$ at the ladder's center. Torques about the **foot** (so $N_g$ and $f$ drop out). The CG is $2.5$ m along the ladder; its horizontal distance from the foot is $2.5\cos\theta$, where $\cos\theta=3/5=0.60$ (3–4–5 triangle), so $1.5$ m. The wall contact is $4.0$ m up.

$$N_w(4.0)=mg(1.5)\;\Rightarrow\; N_w=\frac{(15)(9.8)(1.5)}{4.0}=\frac{220.5}{4.0}=55.1\ \text{N}$$

Vertical and horizontal force balance: $N_g=mg=147$ N, $f=N_w=55.1$ N.

> 💡 **(b) — Concept needed**: no-slip condition $f\le\mu_s N_g$. **Key insight**: $\mu_s\ge f/N_g=0.375$. **If missed**: you use the wall's $N_w$ as the normal for friction.

**(b)** No slip: $f\le\mu_s N_g$:

$$\mu_s\ge\frac{f}{N_g}=\frac{55.1}{147}=0.375$$

> 💡 **(c) — Concept needed**: the person adds a torque; slipping happens when the required $N_w$ hits $f_{\max}$. **Key insight**: $N_w(4.0)=220.5+441s$ with $N_w\le330.75 \Rightarrow s=2.5$ m. **If missed**: you put the person at the top by default.

**(c)** Person of mass $75$ kg at distance $s$ up the ladder; their horizontal distance from the foot is $s\cos\theta=0.60s$. Torque about the foot:

$$N_w(4.0)=mg(1.5)+m_pg(0.60s)=220.5+(75)(9.8)(0.60s)=220.5+441s$$

Slip limit: $N_w=f_{\max}=\mu_sN_g=0.375(15+75)(9.8)=0.375(882)=330.75$ N.

$$(330.75)(4.0)=220.5+441s\;\Rightarrow\; 1323=220.5+441s\;\Rightarrow\; s=2.5\ \text{m}$$

The person can climb halfway up the ladder ($2.5$ m of $5.0$ m) before it slips.

> 💡 **(d) — Concept needed**: a smaller $\mu$ shrinks the friction budget, and the ladder's own weight already consumes a fixed slice of it. **Key insight**: $s$ collapses to 1.10 m. **If missed**: you scale $s$ linearly with $\mu$ (2.5→1.25) instead of subtracting the fixed 220.5 N·m.

**(d)** Wet floor, $\mu_s=0.20$: $f_{\max}=0.20(882)=176.4$ N.

$$(176.4)(4.0)=220.5+441s\;\Rightarrow\; 705.6=220.5+441s\;\Rightarrow\; s=1.10\ \text{m}$$

Only $1.10$ m up — the allowed height collapses because (i) the friction budget roughly halves, and (ii) the ladder's own weight already uses up a fixed slice of it ($220.5$ N·m of torque), so the person's extra torque allowance is small.

---

## Problem D4 — The Pulley System That Shares the Load

> 💡 **Key insight**: **Same rope = same tension**, so $MA$ equals the number of strands supporting the movable pulley. Solving pulley by pulley with free-body diagrams (especially the 4-strand case in (c)) is far more tedious.

> 💡 **(a) — Concept needed**: in an ideal fixed pulley the tension is uniform along one rope. **Key insight**: $F=T=W=400$ N; $MA=1$ — it only changes direction. **If missed**: you expect a fixed pulley to halve the force.

**(a)** Fixed pulley: tension is the same throughout the rope, so $F=T=W=400$ N. $MA=1$. Its purpose is to **change direction** — you pull down, the load goes up — not to multiply force.

> 💡 **(b) — Concept needed**: a movable pulley is supported by **two rope strands**, each carrying the same tension. **Key insight**: $2T=W \Rightarrow F=W/2=200$ N; $MA=2$. **If missed**: you count the pulley's own wheel instead of the strands.

**(b)** Movable pulley: the rope supports the pulley on **two strands**, each carrying tension $T$. $2T=W$:

$$F=T=\frac{W}{2}=200\ \text{N},\qquad MA=2$$

> 💡 **(c) — Concept needed**: $MA$ = the number of supporting strands (same tension throughout). **Key insight**: $4T=W \Rightarrow F=100$ N; $MA=4$. **If missed**: you free-body-diagram each pulley and the work explodes.

**(c)** Four supporting strands: $4T=W$:

$$F=\frac{W}{4}=100\ \text{N},\qquad MA=4$$

$MA$ equals the number of strands supporting the movable block, because the load is shared equally among them (same rope, same tension, ideal pulleys).

> 💡 **(d) — Concept needed**: efficiency = useful work out / work in. **Key insight**: $F_{\text{actual}}=F_{\text{ideal}}/0.80=125$ N; the 100 J difference heats the bearings. **If missed**: you apply efficiency the wrong way ($0.80\times$ instead of $\div$).

**(d)** $80\%$ efficiency: work in $=W\cdot h/0.80$, so $F_{\text{actual}}=F_{\text{ideal}}/0.80=100/0.80=125$ N.

If you pull $4.0$ m of rope, the load rises $h=4.0/MA=4.0/4=1.0$ m (ideal). Work by you: $125\times4.0=500$ J; work on the load: $400\times1.0=400$ J; the missing $100$ J is dissipated as heat in the pulley bearings. (With ideal pulleys both would be $400$ J.)

---

## Problem D5 — Gears, Cranks, and the Winch

> 💡 **Key insight**: The **tangential force is the same at the meshing teeth** (so $\tau\propto r$ and $MA=r_2/r_1$), and in an ideal gear train **power is conserved**: $\tau_1\omega_1=\tau_2\omega_2$. Solving each gear with its own rotational equation of motion drags in inertia and gets long.

> 💡 **(a) — Concept needed**: at the meshing teeth the contact force is the **same** on both gears; $\tau=Fr$. **Key insight**: $\tau_2=F\cdot r_2=80(0.25)=20$ N·m; $MA=r_2/r_1=N_2/N_1$. **If missed**: you assume torque itself is conserved through the mesh.

**(a)** Contact force at the meshing teeth: $F=\tau_1/r_1=8.0/0.10=80$ N. Torque on the driven gear: $\tau_2=F r_2=(80)(0.25)=20$ N·m.

$$MA=\frac{\tau_2}{\tau_1}=\frac{20}{8.0}=2.5=\frac{r_2}{r_1}=\frac{50}{20}=\frac{N_2}{N_1}\quad ✓$$

> 💡 **(b) — Concept needed**: meshing means equal **tangential speed** $r_1\omega_1=r_2\omega_2$; ideal gears conserve power. **Key insight**: $\omega_2=16$ rad/s and $\tau_1\omega_1=\tau_2\omega_2=320$ W. **If missed**: you set $\omega_1=\omega_2$ even though the radii differ.

**(b)** Teeth mesh one-for-one, so the tangential speed at the contact is the same: $r_1\omega_1=r_2\omega_2$.

$$\omega_2=\omega_1\frac{r_1}{r_2}=40\frac{0.10}{0.25}=16\ \text{rad/s}\qquad\left(=40\frac{20}{50}=16\ \text{rad/s by teeth}\right)$$

Power: $\tau_1\omega_1=(8.0)(40)=320$ W; $\tau_2\omega_2=(20)(16)=320$ W ✓. For an ideal (frictionless, massless) gear train, energy is conserved, so input power must equal output power — the gear multiplies torque at the price of angular speed.

> 💡 **(c) — Concept needed**: winch torque balance about the drum axis: $F\cdot R=W\cdot r$. **Key insight**: $F=200$ N, $MA=R/r=6$. **If missed**: you use the load's weight as the input force.

**(c)** Winch: torque balance about the drum axis: $F R=W r$.

$$F=W\frac{r}{R}=1200\frac{0.05}{0.30}=200\ \text{N},\qquad MA=\frac{R}{r}=\frac{0.30}{0.05}=6$$

> 💡 **(d) — Concept needed**: efficiency again — more work in than out. **Key insight**: $F_{\text{actual}}=F/0.75=267$ N; the extra force compensates for energy leaking to heat. **If missed**: you divide the load by MA after efficiency, or apply efficiency in the wrong direction.

**(d)** $75\%$ efficiency: $F_{\text{actual}}=F/0.75=200/0.75=267$ N. Friction dissipates work, so to lift the load at constant speed you must supply more work than the load gains — extra force on the crank compensates for the energy leaking into heat.
