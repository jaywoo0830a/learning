# Others — Day 3 — Solutions

> Full worked solutions. Solve each problem fully on paper before reading.

---

## Problem 1 — Beats, Horns, and Echoes

**(a)** Beat frequency is the difference: $f_{beat}=443-440=3$ Hz.

**(b)** Moving source toward a stationary observer:

$$f'=f\frac{v}{v-v_s}=440\frac{343}{343-10}=453\ \text{Hz}$$

Beats with the stationary $443$ Hz fork: $f_{beat}=453-443=10$ Hz.

**(c)** Two-step Doppler:

Step 1 — the wall is a stationary "observer" of the approaching train:

$$f_{wall}=500\frac{343}{343-25}=539\ \text{Hz}$$

Step 2 — the wall re-emits this frequency; the engineer moves toward the wall at $25$ m/s (moving observer):

$$f'=f_{wall}\frac{v+v_o}{v}=539\frac{343+25}{343}=579\ \text{Hz}$$

Beats between horn and echo: $579-500=79$ Hz. One motion, two Doppler shifts — the echo is always *higher* than the horn for a moving source approaching a reflector.

---

## Problem 2 — The Fish and the Mirror-Surface

**(a)** Critical angle water→air:

$$\theta_c=\arcsin\frac{1}{1.33}=48.8°$$

Incidence $60°>48.8°$ → **total internal reflection**; the surface acts as a perfect mirror for this ray.

**(b)** The largest angle that still escapes is the critical angle itself: $\theta_c=48.8°$.

**(c)** Rays escaping into air come from inside the critical cone:

$$r=d\tan\theta_c=1.0\tan48.8°=1.14\ \text{m}$$

**(d)** The half-angle of the cone is fixed at $48.8°$ (a property of the two media), but the window radius scales with depth: $r=d\tan\theta_c$ → at $2.0$ m, $r=2.28$ m. The *angular* view is constant; the *physical* window grows with depth.

---

## Problem 3 — The Grating That Separates Colors

**(a)** $d=1/6000$ cm $=1.667\times10^{-4}$ cm $=1.667\times10^{-6}$ m.

**(b)** Grating equation $d\sin\theta=m\lambda$:

- Violet (400 nm): $\sin\theta=\dfrac{4e-7}{1.667e-6}=0.24$ → $\theta=13.9°$
- Red (700 nm): $\sin\theta=\dfrac{7e-7}{1.667e-6}=0.42$ → $\theta=24.8°$

**(c)** Highest order requires $\sin\theta\le1$, i.e. $m\le d/\lambda$:

$$m_{max}(red)=\frac{1.667e-6}{7e-7}=2.38\;\Rightarrow\;\text{m}=1,2\ \text{only}$$

For red, $m=2$ gives $\sin\theta=0.84$ ($\theta=57°$); $m=3$ would need $\sin\theta=1.26>1$ — not possible. (For violet, $m$ up to 4 fits.)

**(d)** Violet 2nd order: $\sin\theta=2(4e-7)/1.667e-6=0.48$ → $\theta=28.7°$. First-order red ends at $24.8°$, so **no overlap** in this setup. Overlap in general occurs when the $m$-th order of a short wavelength spreads past the $(m-1)$-th order of a long wavelength — the condition $m\lambda_{short}\ge(m-1)\lambda_{long}$ for some pair. Overlapping orders are why gratings are usually used over a limited spectral range.

---

## Problem 4 — The Engine That Thinks

**(a)** Carnot efficiency:

$$e=1-\frac{T_C}{T_H}=1-\frac{300}{600}=0.5$$

$$W=eQ_H=0.5(1000)=500\ \text{J},\qquad Q_C=Q_H-W=500\ \text{J}$$

**(b)** Running in reverse as a refrigerator, the COP is:

$$\text{COP}=\frac{T_C}{T_H-T_C}=\frac{300}{300}=1$$

$$Q_C=\text{COP}\cdot W=1(200)=200\ \text{J}\ \text{removed},\qquad Q_H=Q_C+W=400\ \text{J}\ \text{dumped}$$

**(c)** Engine 1 (600→450 K): $e_1=1-450/600=0.25$ → per 1 J absorbed, does 0.25 J, rejects 0.75 J. Engine 2 (450→300 K): $e_2=1-300/450=\tfrac13$ → on its 0.75 J input, does 0.25 J, rejects 0.50 J. Total work $=0.25+0.25=0.5$ J per 1 J absorbed:

$$e_{total}=0.5=1-\frac{300}{600}$$

Identical to a single Carnot engine between the two end temperatures. **Staging gains nothing** — the maximum efficiency is fixed by the two extreme temperatures alone.

**(d)** Real engines lose to Carnot through irreversibilities: heat exchange across finite temperature differences, friction, turbulence, uncontrolled combustion — all of which generate entropy. Carnot is the theoretical ceiling, unreachable in practice.

---

## Problem 5 — The Muon That Shouldn't Arrive

**(a)** Classically, in one half-life:

$$d=vt=0.995(3\times10^8)(2.2\times10^{-6})=656\ \text{m}$$

$656$ m $\ll10$ km — classically muons would essentially never reach the ground, yet they do. That's the paradox relativity resolves.

**(b)** Lorentz factor:

$$\gamma=\frac{1}{\sqrt{1-v^2/c^2}}=\frac{1}{\sqrt{1-0.995^2}}=\frac{1}{\sqrt{0.009975}}=10.0$$

Dilated half-life in the Earth frame: $T_{1/2}^{lab}=\gamma T_{1/2}^{proper}=10(2.2\,\mu\text{s})=22\,\mu$s. Distance in that time:

$$d=0.995(3\times10^8)(22\times10^{-6})=6.6\ \text{km}$$

**(c)** Journey time in the Earth frame:

$$t=\frac{10000}{0.995(3\times10^8)}=33.5\,\mu\text{s}$$

Number of lab half-lives $=33.5/22=1.52$:

$$\frac{N}{N_0}=\left(\frac12\right)^{1.52}=0.35=35\%$$

**(d)** From the muon's frame, the atmosphere is length-contracted:

$$L=\frac{10\ \text{km}}{\gamma}=1.0\ \text{km}$$

The ground rushes up at $0.995c$ while the muon lives its normal $2.2\,\mu$s — and the fraction that survives the 1.0 km is the same 35%. **Both frames must agree on the physics; relativity just lets each frame describe it in its own terms.**
