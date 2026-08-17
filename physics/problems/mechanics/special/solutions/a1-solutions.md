# Mechanics — Special A1 — Solutions

> Full worked solutions. Solve all 20 problems fully on paper before reading.

---

# Part A — Circular Motion

## Problem A1 — The Tilted String

**(a)** Forces: tension $T$ along the string, weight $mg$ down. The bob moves in a horizontal circle, so the **horizontal component of tension** $T\sin\theta$ is the centripetal force; the vertical component $T\cos\theta$ balances the weight.

$$T\cos\theta=mg \;\Rightarrow\; T=\frac{mg}{\cos\theta}=\frac{(0.50)(9.8)}{0.80}=6.13\ \text{N}$$

**(b)** Radius of the circle: $r=L\sin\theta=2.0(0.60)=1.2$ m. Radial force law:

$$T\sin\theta=\frac{mv^2}{r}\;\Rightarrow\; v=\sqrt{\frac{T\sin\theta\,r}{m}}=\sqrt{\frac{(6.13)(0.60)(1.2)}{0.50}}=\sqrt{8.82}=2.97\ \text{m/s}$$

Equivalently $v=\sqrt{gr\tan\theta}=\sqrt{(9.8)(1.2)(0.75)}=2.97$ m/s.

**(c)** Period: $T_{\text{period}}=2\pi r/v=2\pi(1.2)/2.97=2.54$ s. Symbolically:

$$T_{\text{period}}=\frac{2\pi(L\sin\theta)}{\sqrt{gL\sin\theta\tan\theta}}=2\pi\sqrt{\frac{L\cos\theta}{g}}$$

As $\theta\to0°$, $\cos\theta\to1$, so $T_{\text{period}}\to2\pi\sqrt{L/g}$ — the **simple pendulum** period. (And indeed a conical pendulum at tiny angles behaves like a pendulum swinging in a plane.)

**(d)** As $\theta\to90°$: $\cos\theta\to0$ so $T=mg/\cos\theta\to\infty$ and $v=\sqrt{gL\sin\theta\tan\theta}\to\infty$. Physically the string tension grows without bound (and its horizontal component must supply the ever-larger centripetal force), so the string snaps at some large-but-finite angle long before $90°$.

---

## Problem A2 — The Rotor That Never Drops

**(a)** Forces: weight $mg$ down, normal $N$ from the wall pointing **inward** (this is the centripetal force), and static friction $f$ pointing **up** (this supports the weight). There is no vertical acceleration: $f=mg$.

**(b)** Centripetal: $N=m\omega^2R$. No-slip condition: $f_{\max}=\mu_s N\ge mg$.

$$\mu_s m\omega^2R\ge mg\;\Rightarrow\; \omega_{\min}=\sqrt{\frac{g}{\mu_s R}}=\sqrt{\frac{9.8}{(0.40)(3.0)}}=\sqrt{8.17}=2.86\ \text{rad/s}$$

Period: $T=2\pi/\omega_{\min}=2\pi/2.86=2.20$ s (about one revolution every 2.2 s).

**(c)** At $\omega_{\min}$: $N=m\omega_{\min}^2R=m(g/\mu_s R)R=mg/\mu_s=\dfrac{60\cdot9.8}{0.40}=1470$ N $=2.5\,mg$.

So the wall presses on the person with **2.5 times their weight**. The friction needed is only $mg$, so a friction coefficient of only $1/2.5=0.40$ suffices. The normal force is $mg/\mu_s$ because friction is $f=\mu_sN$ — the smaller $\mu_s$, the harder the wall must push.

**(d)** $\omega_{\min}\propto 1/\sqrt{\mu_s}$, so doubling $\mu_s$ gives $\omega_{\min}\to \omega_{\min}/\sqrt2$ — a factor $0.707$. The square root appears because friction scales with $\mu_s N$ and $N$ scales with $\omega^2$.

---

## Problem A3 — The Curve With an Attitude

**(a)** Flat curve: friction is the centripetal force.

$$\mu_s mg=\frac{mv^2}{R}\;\Rightarrow\; v_{\max}=\sqrt{\mu_s gR}=\sqrt{(0.60)(9.8)(50)}=\sqrt{294}=17.1\ \text{m/s}$$

**(b)** Frictionless bank: the horizontal component of the normal provides centripetal force.

$$N\sin\theta=\frac{mv^2}{R},\qquad N\cos\theta=mg\;\Rightarrow\; \tan\theta=\frac{v^2}{gR}$$

For $v\approx20$ m/s: $\tan\theta=\dfrac{400}{(9.8)(50)}=0.816\approx0.80\Rightarrow \theta\approx38.7°$.

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

**(d)** Flat curve: $v_{\max}=\sqrt{\mu_s gR}$ drops by factor $\sqrt{0.30/0.60}=0.707$: $17.1\to12.1$ m/s. A banked curve at the design speed needs **no friction at all**, so rain doesn't change the safe speed at $v=\sqrt{gR\tan\theta}$ — only the *range* around it narrows.

---

## Problem A4 — The Ball That Swings in a Circle

**(a)** At the bottom, radial $F=ma$:

$$T_b-mg=\frac{mv_b^2}{L}\;\Rightarrow\; T_b=m\left(g+\frac{v_b^2}{L}\right)=2\left(9.8+\frac{81}{1.5}\right)=2(63.8)=127.6\ \text{N}$$

Energy from bottom to top (height gain $2L$):

$$v_t^2=v_b^2-4gL=81-4(9.8)(1.5)=81-58.8=22.2\;\Rightarrow\; v_t=4.71\ \text{m/s}$$

At the top, both tension and weight point down (radially inward):

$$T_t+mg=\frac{mv_t^2}{L}\;\Rightarrow\; T_t=m\left(\frac{v_t^2}{L}-g\right)=2\left(\frac{22.2}{1.5}-9.8\right)=2(5.0)=10.0\ \text{N}$$

**(b)** Taut condition at top: $T_t\ge0 \Rightarrow v_t^2\ge gL$.

$$v_{t,\min}=\sqrt{gL}=\sqrt{(9.8)(1.5)}=\sqrt{14.7}=3.83\ \text{m/s}$$

Energy: $v_b^2=v_t^2+4gL=gL+4gL=5gL$:

$$v_{b,\min}=\sqrt{5gL}=\sqrt{73.5}=8.57\ \text{m/s}$$

**(c)** Released from the horizontal: bottom speed from energy $v_b^2=2gL$.

$$v_b=\sqrt{2gL}=\sqrt{29.4}=5.42\ \text{m/s},\qquad T_b=mg+\frac{mv_b^2}{L}=mg+2mg=3mg=58.8\ \text{N}$$

The $L$ cancels: for a ball released from the side, the tension at the bottom is always $3mg$, because $v_b^2/L=2g$ regardless of $L$.

**(d)** Released from rest at angle $\theta_0$ from the bottom. Height dropped by the bottom $=L(1-\cos\theta_0)$:

$$v_b^2=2gL(1-\cos\theta_0)\;\Rightarrow\; T_b=mg+\frac{mv_b^2}{L}=mg+2mg(1-\cos\theta_0)=mg(3-2\cos\theta_0)$$

Checks: $\theta_0=90°\Rightarrow T_b=mg(3-0)=3mg$ ✓; $\theta_0=0°\Rightarrow T_b=mg(3-2)=mg$ ✓. For $\theta_0=120°$: $\cos\theta_0=-\tfrac12$,

$$T_b=mg(3+1)=4mg=4(2.0)(9.8)=78.4\ \text{N}$$

---

## Problem A5 — The Hill, the Dip, and the Feeling in Your Stomach

**(a)** At the top of the hump, $N$ points up, $mg$ points down, and both the required centripetal acceleration $v^2/R$ is down:

$$mg-N=\frac{mv^2}{R}\;\Rightarrow\; N=m\left(g-\frac{v^2}{R}\right)=1200\left(9.8-\frac{100}{30}\right)=1200(6.47)=7760\ \text{N}$$

**(b)** Lose contact when $N=0$: $v=\sqrt{gR}=\sqrt{(9.8)(30)}=\sqrt{294}=17.1$ m/s. The driver feels weightless — the car and driver are both in free fall over the crest.

**(c)** In the dip, the centripetal acceleration points up:

$$N-mg=\frac{mv^2}{R}\;\Rightarrow\; N=m\left(g+\frac{v^2}{R}\right)=1200\left(9.8+3.33\right)=15760\ \text{N}$$

**(d)** Heaviest in the dip ($N=15760$ N > weight $11760$ N), lightest over the hump ($N=7760$ N). The apparent weight is $N$ itself. Weightlessness over the hump happens exactly when $v^2=gR$; in the dip you can never feel weightless (the car pushes *up* harder than $mg$).

---

# Part B — Linear Momentum

## Problem B1 — The Cannon That Punches Back

**(a)** Conservation of horizontal momentum (cannon + shell):

$$0=M V+m v\;\Rightarrow\; V=\frac{m v}{M}=\frac{(10)(300)}{800}=3.75\ \text{m/s}$$

**(b)** At $30°$, only the horizontal component matters:

$$0=MV+mv\cos30°\;\Rightarrow\; V=\frac{(10)(300)(0.866)}{800}=3.25\ \text{m/s}$$

The vertical component of the shell's momentum is given to the **ground** through the normal force during firing — momentum is conserved for the cannon+shell+Earth system vertically, but the Earth is too massive to notice.

**(c)** After the shot, only kinetic friction does work (cannon slides with no external horizontal force other than friction):

$$\tfrac12 M V^2=\mu_k M g\,d\;\Rightarrow\; d=\frac{V^2}{2\mu_k g}=\frac{(3.75)^2}{2(0.20)(9.8)}=\frac{14.06}{3.92}=3.59\ \text{m}$$

**(d)** Uniform acceleration down a $L=2.0$ m barrel: $v^2=2aL$, so

$$a=\frac{v^2}{2L}=\frac{(300)^2}{2(2.0)}=22500\ \text{m/s}^2,\qquad t=\frac{v}{a}=\frac{300}{22500}=0.0133\ \text{s}$$

$$F_{\text{avg}}=m a=(10)(22500)=2.25\times10^5\ \text{N}$$

Impulse: $J=F_{\text{avg}}t=(2.25\times10^5)(0.0133)=3000$ N·s $=mv=10\cdot300$ ✓ — impulse equals the shell's momentum change, as required by impulse–momentum.

---

## Problem B2 — The Firework That Divides

**(a)** At the top, total momentum is zero. Conservation of momentum:

$$0=m_1v_1+m_2v_2\;\Rightarrow\; v_2=-\frac{m_1}{m_2}v_1=-\frac{1.0}{2.0}(40)=-20\ \text{m/s}$$

Piece 2 moves to the **left** at $20$ m/s. The principle applies even though chemical energy is released because the explosion forces are **internal** — no external force acts on the (already-split) system during the explosion, and momentum is conserved regardless of energy.

**(b)** $KE_{\text{before}}=0$ (top of flight). After:

$$KE=\tfrac12(1.0)(40)^2+\tfrac12(2.0)(20)^2=800+400=1200\ \text{J}$$

The extra $1200$ J comes from the **chemical potential energy** of the explosive.

**(c)** Both pieces start at height $h=80$ m; piece 1 falls straight down from rest horizontally:

$$t_1=\sqrt{\frac{2h}{g}}=\sqrt{\frac{160}{9.8}}=4.04\ \text{s},\qquad x_1=v_1t_1=40(4.04)=161.6\ \text{m}$$

Piece 2 also starts at $h$ with zero vertical velocity:

$$t_2=t_1=4.04\ \text{s},\qquad x_2=v_2t_2=-20(4.04)=-80.8\ \text{m}$$

Both hit the ground simultaneously (same vertical initial velocity, same height) — on opposite sides of the explosion point.

**(d)** Three equal pieces, total momentum zero: $\vec p_C=-(\vec p_A+\vec p_B)$.

$$\vec p_A=1.0(30\,\hat x),\qquad \vec p_B=1.0(40\,\hat y)$$
$$\vec p_C=-30\hat x-40\hat y\;\Rightarrow\; v_C=\sqrt{30^2+40^2}=50\ \text{m/s}$$

Direction: $\tan\phi=40/30$, $\phi=53°$ **below** the $-x$ axis. The three momentum vectors sum to zero — they form a closed triangle.

---

## Problem B3 — The Bullet and the Block on Strings

**(a)** Energy after collision (block+bullet rises $h$, stops at top):

$$\tfrac12(m+M)v^2=(m+M)gh\;\Rightarrow\; v=\sqrt{2gh}=\sqrt{2(9.8)(0.20)}=\sqrt{3.92}=1.98\ \text{m/s}$$

**(b)** Momentum during collision:

$$m v_b=(m+M)v\;\Rightarrow\; v_b=\frac{m+M}{m}v=\frac{2.02}{0.020}(1.98)=101(1.98)=200\ \text{m/s}$$

**(c)** $KE_{\text{before}}=\tfrac12(0.020)(200)^2=400$ J. $KE_{\text{after}}=\tfrac12(2.02)(1.98)^2=3.96$ J. Lost fraction:

$$\frac{400-3.96}{400}=0.99=99\%$$

Essentially all the bullet's kinetic energy goes into heating/deforming the block and bullet.

**(d)** Bullet rebounds at $v_b/4=50$ m/s (opposite direction). Momentum:

$$m v_b=m(-50)+M V\;\Rightarrow\; 0.020(200)=-1.0+2.00V\;\Rightarrow\; V=2.5\ \text{m/s}$$

$$h=\frac{V^2}{2g}=\frac{(2.5)^2}{2(9.8)}=\frac{6.25}{19.6}=0.319\ \text{m}$$

The block rises higher because the rebounding bullet carries away *less* energy (its KE after is $\tfrac12(0.020)(50)^2=25$ J vs. 0 for the embedding case), leaving more for the block.

---

## Problem B4 — The Perfect Two-Dimensional Collision

**(a)** Take $+x$ along the initial motion, $+y$ upward. Momentum:

$$x:\ m v_0=m v_1\cos37°+m v_2\cos\theta_2\;\Rightarrow\; 5.0=4.0(0.80)+v_2\cos\theta_2\;\Rightarrow\; v_2\cos\theta_2=1.8$$
$$y:\ 0=m v_1\sin37°-m v_2\sin\theta_2\;\Rightarrow\; v_2\sin\theta_2=4.0(0.60)=2.4$$

Divide: $\tan\theta_2=\dfrac{2.4}{1.8}=1.333\Rightarrow\theta_2=53°$ below the $+x$ axis. Then

$$v_2=\sqrt{1.8^2+2.4^2}=\sqrt{9}=3.0\ \text{m/s}$$

**(b)** $KE_{\text{before}}=\tfrac12(0.50)(5.0)^2=6.25$ J.
$KE_{\text{after}}=\tfrac12(0.50)(4.0)^2+\tfrac12(0.50)(3.0)^2=4.0+2.25=6.25$ J ✓ — elastic.

**(c)** The final velocities make angles $37°$ and $53°$ on opposite sides of the original line; $37°+53°=90°$. The angle between them is $90°$.

**(d)** General proof: mass $m$ at $\vec v_0$ hits identical mass at rest; final velocities $\vec v_1,\vec v_2$. Momentum and energy:

$$\vec v_0=\vec v_1+\vec v_2,\qquad v_0^2=v_1^2+v_2^2$$

Square the momentum equation: $v_0^2=v_1^2+v_2^2+2\vec v_1\cdot\vec v_2$. Subtract the energy equation: $2\vec v_1\cdot\vec v_2=0$, so $\vec v_1\cdot\vec v_2=0$ — the final velocities are **perpendicular**, for any elastic equal-mass collision with one target initially at rest. (Unless one piece stops entirely, the trivial case.)

---

## Problem B5 — The Train That Couples, Couples, Couples

**(a)** First coupling (momentum): $m v_0=2m v_2\Rightarrow v_2=v_0/2=1.5$ m/s.
Second coupling: $2m v_2=3m v_3\Rightarrow v_3=\tfrac23 v_2=v_0/3=1.0$ m/s.
Pattern: $v_n=v_0/n$.

**(b)** Induction: suppose $n-1$ cars move at $v_{n-1}=v_0/(n-1)$. Coupling to car $n$:

$$(n-1)m\,v_{n-1}=n m\,v_n\;\Rightarrow\; v_n=\frac{n-1}{n}v_{n-1}=\frac{n-1}{n}\cdot\frac{v_0}{n-1}=\frac{v_0}{n}$$

**(c)** After 5 cars: $v_5=v_0/5=0.6$ m/s. Energy remaining:

$$\frac{\tfrac12(5m)v_5^2}{\tfrac12 m v_0^2}=\frac{5m(v_0/5)^2}{m v_0^2}=\frac{1}{5}=20\%$$

Original $KE=\tfrac12(10^4)(3)^2=45000$ J; remaining $\tfrac15=9000$ J; lost $36000$ J to heat, sound, and permanent deformation of the couplings.

**(d)** Just before the $k$-th coupling, $k-1$ cars move at $v_{k-1}=v_0/(k-1)$ with $KE_{\text{before}}=\tfrac12(k-1)m v_{k-1}^2$. Just after, $k$ cars move at $v_k=v_0/k$:

$$KE_{\text{after}}=\tfrac12 k m\, v_k^2=\tfrac12 km\frac{v_0^2}{k^2}=\frac{mv_0^2}{2k},\qquad KE_{\text{before}}=\tfrac12(k-1)m\frac{v_0^2}{(k-1)^2}=\frac{mv_0^2}{2(k-1)}$$

Ratio: $\dfrac{KE_{\text{after}}}{KE_{\text{before}}}=\dfrac{k-1}{k}$. So each coupling destroys exactly $1/k$ of the energy present before it — for the *first* coupling ($k=2$), that's $1/2$: half the energy is destroyed by the very first hit. This is the signature of a completely inelastic collision: relative kinetic energy is converted to internal energy, and the "lost" fraction is largest when the relative speed is largest (the first coupling).

---

# Part C — Rotation of a Rigid Body

## Problem C1 — The Flywheel That Stores Energy

**(a)** $I=\tfrac12MR^2=\tfrac12(2.0)(0.50)^2=0.25$ kg·m². Rotational Newton's 2nd law:

$$\alpha=\frac{\tau}{I}=\frac{5.0}{0.25}=20\ \text{rad/s}^2$$

**(b)** $\omega=\alpha t=(20)(10)=200$ rad/s. Angle: $\theta=\tfrac12\alpha t^2=\tfrac12(20)(100)=1000$ rad $=\dfrac{1000}{2\pi}=159$ rev.

**(c)** $KE=\tfrac12I\omega^2=\tfrac12(0.25)(200)^2=5000$ J.

**(d)** $W=\tau\theta=(5.0)(1000)=5000$ J $=KE$ ✓. Rotational work–energy theorem: $W_{\text{net}}=\Delta(\tfrac12I\omega^2)$, the exact analogue of $W_{\text{net}}=\Delta(\tfrac12mv^2)$. The rotational analogues: $\tau\leftrightarrow F$, $\theta\leftrightarrow x$, $\omega\leftrightarrow v$, $\alpha\leftrightarrow a$, $I\leftrightarrow m$.

---

## Problem C2 — Two Disks, One Spin

**(a)** Conservation of angular momentum (no external torque):

$$I_1\omega_1=(I_1+I_2)\omega_f\;\Rightarrow\; \omega_f=\frac{(0.40)(20)}{1.00}=8\ \text{rad/s}$$

**(b)** $KE_{\text{before}}=\tfrac12(0.40)(20)^2=80$ J. $KE_{\text{after}}=\tfrac12(1.00)(8)^2=32$ J. Lost $48$ J, fraction $48/80=0.60=60\%$.

This mirrors the linear inelastic collision of **Problem B5**: kinetic energy is lost while momentum (angular momentum) is conserved. The difference: here the "masses" ($I$) add directly, and the lost energy is dissipated in the clutch surfaces as heat.

**(c)** Disk 2 spins opposite at $10$ rad/s (take it negative):

$$\omega_f=\frac{I_1\omega_1+I_2\omega_2}{I_1+I_2}=\frac{0.40(20)+0.60(-10)}{1.00}=\frac{8-6}{1.00}=2\ \text{rad/s}$$

The pair spins slowly in disk 1's original direction.

**(d)** The "lost" rotational KE becomes thermal energy in the clutch/contact surfaces during the locking. If the coupling were perfectly elastic, angular momentum would still be conserved but the disks could not lock — they would exchange energy through a lossless interaction and end with different speeds satisfying both $L$ and $KE$ conservation (like an elastic collision in rotation).

---

## Problem C3 — The Race Down the Hill

**(a)** Rolling: $KE=\tfrac12mv^2+\tfrac12I\omega^2$, with $\omega=v/R$ (no slip). Energy:

$$mgh=\tfrac12mv^2+\tfrac12I\frac{v^2}{R^2}=\tfrac12mv^2\left(1+\frac{I}{mR^2}\right)\;\Rightarrow\; v=\sqrt{\frac{2gh}{1+I/mR^2}}$$

- Hoop, $I/mR^2=1$: $v=\sqrt{gh}=\sqrt{9.8}=3.13$ m/s
- Disk, $I/mR^2=\tfrac12$: $v=\sqrt{2gh/1.5}=\sqrt{13.07}=3.61$ m/s
- Sphere, $I/mR^2=\tfrac25$: $v=\sqrt{2gh/1.4}=\sqrt{14}=3.74$ m/s

**(b)** The **sphere wins** (smallest $I/mR^2$), the hoop loses. The smaller the moment of inertia, the less energy is diverted into rotation, so more goes into linear motion. Mass and radius cancel out of $v$ entirely — a big solid sphere and a tiny solid sphere roll with identical speeds.

**(c)** Frictionless slide: no rotation, $mgh=\tfrac12mv^2\Rightarrow v=\sqrt{2gh}=\sqrt{19.6}=4.43$ m/s — the fastest of all. Rolling is slower because some of the gravitational energy must spin the object up. Friction itself does no work (the contact point is instantaneously at rest, so $W_f=f\cdot0=0$) — it merely *converts* translational energy into rotational energy.

**(d)** For rolling, $a=\dfrac{g\sin\theta}{1+I/mR^2}$ and friction $f=I\alpha/R^2=I a/R^2=(I/mR^2)ma$. No-slip requires $f\le\mu_s mg\cos\theta$:

$$\mu_s\ge\frac{I/mR^2}{1+I/mR^2}\,\tan\theta$$

With $\tan30°=0.577$:
- Hoop: $\mu_s\ge\dfrac{1}{2}(0.577)=0.289$
- Disk: $\mu_s\ge\dfrac{0.5}{1.5}(0.577)=0.192$
- Sphere: $\mu_s\ge\dfrac{0.4}{1.4}(0.577)=0.165$

The **hoop** needs the grippiest surface; the sphere the least.

---

## Problem C4 — The Falling Rod

**(a)** $I=\tfrac13mL^2=\tfrac13(3.0)(2.0)^2=4.0$ kg·m².

**(b)** The weight acts at the center of mass, distance $L/2$ from the pivot:

$$\tau=mg\frac{L}{2}=(3.0)(9.8)(1.0)=29.4\ \text{N·m},\qquad \alpha=\frac{\tau}{I}=\frac{29.4}{4.0}=7.35\ \text{rad/s}^2$$

The weight is "effectively applied" at the center of mass — that's why the torque arm is $L/2$, not $L$.

**(c)** Energy: the CM drops $L/2$.

$$mg\frac{L}{2}=\tfrac12 I\omega^2\;\Rightarrow\; \omega=\sqrt{\frac{mgL}{I}}=\sqrt{\frac{(3.0)(9.8)(2.0)}{4.0}}=\sqrt{14.7}=3.83\ \text{rad/s}$$

**(d)** Tip speed: $v_{\text{tip}}=\omega L=(3.83)(2.0)=7.67$ m/s. A point mass falling from height $L$: $v=\sqrt{2gL}=\sqrt{39.2}=6.26$ m/s. The tip is **faster** because the pivot is fixed — the tip travels a full $L$ while the center of mass only falls $L/2$, yet all the gravitational energy (from the CM's $L/2$ drop) is converted to rotation. The tip "beats" free fall.

---

## Problem C5 — The Skater, the Platform, and Where the Energy Comes From

**(a)** Conservation of angular momentum:

$$I_1\omega_1=I_2\omega_2\;\Rightarrow\; \omega_2=\frac{4.0}{1.0}(2.0)=8\ \text{rad/s}$$

**(b)** $KE_1=\tfrac12(4.0)(2.0)^2=8$ J; $KE_2=\tfrac12(1.0)(8)^2=32$ J. The KE **increases by 24 J** even though no external torque acts. Angular momentum conservation says $I\omega=$ const; it does **not** say energy is conserved. The extra energy comes from the **muscular work** the skater does pulling her arms in against the centrifugal force. Angular momentum conservation and energy conservation are independent laws; here only the former holds (the system is not closed energetically — the skater is an internal energy source).

**(c)** Student at rim: $I_s=mr^2=(60)(1.0)^2=60$ kg·m². Total $I_1=I_p+I_s=80$ kg·m².

$$\omega_2=\frac{I_1}{I_2}\omega_0=\frac{80}{20}(3.0)=12\ \text{rad/s}$$

**(d)** $KE_1=\tfrac12(80)(3.0)^2=360$ J; $KE_2=\tfrac12(20)(12)^2=1440$ J. The increase, $+1080$ J, is work done by the student's muscles as they pull themselves inward against the "centrifugal" tendency to fly outward. If the student walks back out to the rim, $\omega$ drops back to $3.0$ rad/s and the KE returns to $360$ J — the student's muscles must now do **negative** work (absorb energy) to slow the spin, i.e., they resist being flung outward. The system is like a "rotational battery": energy is stored in the faster spin and can be recovered.

---

# Part D — Torque & Machines

## Problem D1 — The Seesaw That Asks Questions

**(a)** Take CCW positive. A at left end ($+$), B at right end ($-$):

$$\tau_{\text{net}}=(25)(9.8)(2.0)-(20)(9.8)(2.0)=490-392=+98\ \text{N·m}$$

A's side goes down. The board's weight acts at the pivot (center of mass of a uniform board is at its center), so its torque arm is zero — it contributes nothing.

**(b)** Keep B at the end ($2.0$ m). Balance: $(25)(9.8)d_A=(20)(9.8)(2.0)$:

$$d_A=\frac{20\cdot2.0}{25}=1.6\ \text{m}$$

So A must sit $1.6$ m from the pivot (closer in). If instead A stays at the end and B moves: $d_B=(25)(9.8)(2.0)/(20)(9.8)=2.5$ m — but the board is only $2.0$ m long on B's side, so B **cannot** sit far enough out. The heavier child must sit closer to the pivot.

**(c)** Torques with A at $1.6$ m and C on the right end:

$$\tau_{\text{net}}=(25)(9.8)(1.6)-(20)(9.8)(2.0)-(10)(9.8)(2.0)=392-392-196=-196\ \text{N·m}$$

Right side down. Restore balance by moving A outward:

$$(25)(9.8)d_A=392+196=588\;\Rightarrow\; d_A=\frac{588}{245}=2.4\ \text{m}$$

A must move out to $2.4$ m from the pivot.

**(d)** Board CM displaced a distance $d$ from the pivot (on one side). With A at the left end and B at the right end:

$$(25)(9.8)(2.0)=(20)(9.8)(2.0)+(10)(9.8)d\;\Rightarrow\; 490=392+98d\;\Rightarrow\; d=1.0\ \text{m}$$

The board's center of mass must lie $1.0$ m to the **right** of the pivot — toward B's heavier side... (checking: B is *lighter* here, so the board's extra weight must sit on B's side to balance A). Yes: board CM $1.0$ m right of pivot.

---

## Problem D2 — The Wheelbarrow That Multiplies Force

**(a)** Torques about the wheel (fulcrum): load at $a=0.40$ m, hands at $b=1.6$ m.

$$F b=W a\;\Rightarrow\; F=W\frac{a}{b}=600\frac{0.40}{1.6}=150\ \text{N}$$

**(b)** $MA=\dfrac{b}{a}=\dfrac{1.6}{0.40}=4$, and indeed $W/F=600/150=4$. The wheelbarrow multiplies your force by 4.

**(c)** Include the wheelbarrow body (mass $10$ kg, weight $98$ N) at $0.60$ m from the wheel:

$$F(1.6)=(600)(0.40)+(98)(0.60)=240+58.8=298.8\;\Rightarrow\; F=186.8\ \text{N}$$

**(d)** Load moved to $a=0.30$ m: $F=600(0.30)/1.6=112.5$ N (down from $150$ N, a saving of $37.5$ N).

Compare with lengthening the handles to $b=1.8$ m (keeping $a=0.40$): $F=600(0.40)/1.8=133.3$ N (saving $16.7$ N). Moving the load $0.10$ m closer saves more than lengthening the handles $0.20$ m — because $F\propto a$ while $F\propto1/b$; a small change in the small arm $a$ packs more leverage.

---

## Problem D3 — The Ladder That Wants to Slip

**(a)** Forces: $N_w$ horizontal at the top (frictionless wall), $N_g$ up and $f$ horizontal at the foot, weight $mg$ at the ladder's center. Torques about the **foot** (so $N_g$ and $f$ drop out). The CG is $2.5$ m along the ladder; its horizontal distance from the foot is $2.5\cos\theta$, where $\cos\theta=3/5=0.60$ (3–4–5 triangle), so $1.5$ m. The wall contact is $4.0$ m up.

$$N_w(4.0)=mg(1.5)\;\Rightarrow\; N_w=\frac{(15)(9.8)(1.5)}{4.0}=\frac{220.5}{4.0}=55.1\ \text{N}$$

Vertical and horizontal force balance: $N_g=mg=147$ N, $f=N_w=55.1$ N.

**(b)** No slip: $f\le\mu_s N_g$:

$$\mu_s\ge\frac{f}{N_g}=\frac{55.1}{147}=0.375$$

**(c)** Person of mass $75$ kg at distance $s$ up the ladder; their horizontal distance from the foot is $s\cos\theta=0.60s$. Torque about the foot:

$$N_w(4.0)=mg(1.5)+m_pg(0.60s)=220.5+(75)(9.8)(0.60s)=220.5+441s$$

Slip limit: $N_w=f_{\max}=\mu_sN_g=0.375(15+75)(9.8)=0.375(882)=330.75$ N.

$$(330.75)(4.0)=220.5+441s\;\Rightarrow\; 1323=220.5+441s\;\Rightarrow\; s=2.5\ \text{m}$$

The person can climb halfway up the ladder ($2.5$ m of $5.0$ m) before it slips.

**(d)** Wet floor, $\mu_s=0.20$: $f_{\max}=0.20(882)=176.4$ N.

$$(176.4)(4.0)=220.5+441s\;\Rightarrow\; 705.6=220.5+441s\;\Rightarrow\; s=1.10\ \text{m}$$

Only $1.10$ m up — the allowed height collapses because (i) the friction budget roughly halves, and (ii) the ladder's own weight already uses up a fixed slice of it ($220.5$ N·m of torque), so the person's extra torque allowance is small.

---

## Problem D4 — The Pulley System That Shares the Load

**(a)** Fixed pulley: tension is the same throughout the rope, so $F=T=W=400$ N. $MA=1$. Its purpose is to **change direction** — you pull down, the load goes up — not to multiply force.

**(b)** Movable pulley: the rope supports the pulley on **two strands**, each carrying tension $T$. $2T=W$:

$$F=T=\frac{W}{2}=200\ \text{N},\qquad MA=2$$

**(c)** Four supporting strands: $4T=W$:

$$F=\frac{W}{4}=100\ \text{N},\qquad MA=4$$

$MA$ equals the number of strands supporting the movable block, because the load is shared equally among them (same rope, same tension, ideal pulleys).

**(d)** $80\%$ efficiency: work in $=W\cdot h/0.80$, so $F_{\text{actual}}=F_{\text{ideal}}/0.80=100/0.80=125$ N.

If you pull $4.0$ m of rope, the load rises $h=4.0/MA=4.0/4=1.0$ m (ideal). Work by you: $125\times4.0=500$ J; work on the load: $400\times1.0=400$ J; the missing $100$ J is dissipated as heat in the pulley bearings. (With ideal pulleys both would be $400$ J.)

---

## Problem D5 — Gears, Cranks, and the Winch

**(a)** Contact force at the meshing teeth: $F=\tau_1/r_1=8.0/0.10=80$ N. Torque on the driven gear: $\tau_2=F r_2=(80)(0.25)=20$ N·m.

$$MA=\frac{\tau_2}{\tau_1}=\frac{20}{8.0}=2.5=\frac{r_2}{r_1}=\frac{50}{20}=\frac{N_2}{N_1}\quad ✓$$

**(b)** Teeth mesh one-for-one, so the tangential speed at the contact is the same: $r_1\omega_1=r_2\omega_2$.

$$\omega_2=\omega_1\frac{r_1}{r_2}=40\frac{0.10}{0.25}=16\ \text{rad/s}\qquad\left(=40\frac{20}{50}=16\ \text{rad/s by teeth}\right)$$

Power: $\tau_1\omega_1=(8.0)(40)=320$ W; $\tau_2\omega_2=(20)(16)=320$ W ✓. For an ideal (frictionless, massless) gear train, energy is conserved, so input power must equal output power — the gear multiplies torque at the price of angular speed.

**(c)** Winch: torque balance about the drum axis: $F R=W r$.

$$F=W\frac{r}{R}=1200\frac{0.05}{0.30}=200\ \text{N},\qquad MA=\frac{R}{r}=\frac{0.30}{0.05}=6$$

**(d)** $75\%$ efficiency: $F_{\text{actual}}=F/0.75=200/0.75=267$ N. Friction dissipates work, so to lift the load at constant speed you must supply more work than the load gains — extra force on the crank compensates for the energy leaking into heat.
