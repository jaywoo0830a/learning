# Others — Day 1 — Solutions

> Full worked solutions. Solve each problem fully on paper before reading.

---

## Problem 1 — The String That Sings

**(a)** Fundamental on a string fixed at both ends: $\lambda_1=2L$, so:

$$v=\lambda_1f_1=2Lf_1=2(1.5)(80)=240\ \text{m/s}$$

**(b)** Mass per length: $\mu=m/L=0.003/1.5=0.002$ kg/m. Wave speed relation:

$$v=\sqrt{\frac{T}{\mu}}\;\Rightarrow\;T=\mu v^2=0.002(240)^2=115\ \text{N}$$

**(c)** Harmonics are integer multiples: $f_3=3f_1=240$ Hz.

**(d)** Same tension ⇒ same $v=240$ m/s. Shortened to $1.0$ m:

$$f_1'=\frac{v}{2L'}=\frac{240}{2(1.0)}=120\ \text{Hz}$$

**(e)** Moving observer toward a stationary source:

$$f'=f\frac{v_{sound}+v_o}{v_{sound}}=240\frac{343+20}{343}=254\ \text{Hz}$$

---

## Problem 2 — The Fish, the Bird, and the Window

**(a)** Apparent depth of an object at real depth $d$ seen through a medium of index $n$:

$$d_{app}=\frac{d}{n}=\frac{1.0}{1.33}=0.75\ \text{m}$$

The fish looks shallower than it is.

**(b)** For an object in air seen from water, the apparent distance from the interface is $n\times$ the real distance:

$$h_{app}=n\,d=1.33(2.0)=2.66\ \text{m}$$

The bird looks higher (and the whole outside world is compressed into a cone).

**(c)** Critical angle for water → air:

$$\theta_c=\arcsin\frac{n_{air}}{n_{water}}=\arcsin\frac{1}{1.33}=48.8°$$

Beyond $\theta_c$, light undergoes **total internal reflection** — the surface becomes a mirror, so the fish sees the pond floor reflected instead of the sky.

**(d)** The "sky window": rays that can escape into air come from within the critical-angle cone:

$$r=d\tan\theta_c=1.0\tan48.8°=1.14\ \text{m}$$

The entire sky is squeezed into this circle at the surface.

---

## Problem 3 — The Ice Cube With an Attitude

**(a)** Heat to warm ice from $-10°$C to $0°$C: $0.1(2100)(10)=2100$ J. Heat to melt all ice: $0.1(3.34e5)=33400$ J. Total needed: $35500$ J.
Heat available from water cooling $30°\to0°$: $0.5(4186)(30)=62790$ J. Since $62790>35500$, **all the ice melts** and the final temperature is above $0°$C.

**(b)** Leftover heat heats the combined $0.60$ kg of water:

$$\Delta T=\frac{62790-35500}{(0.6)(4186)}=\frac{27290}{2512}=10.9°\text{C}\;\Rightarrow\;T_f=10.9°\text{C}$$

**(c)** With $0.30$ kg of ice: warm to $0°$: $0.3(2100)(10)=6300$ J; melt all: $0.3(3.34e5)=100200$ J; total $106500$ J $>62790$ J → **not all melts**. Melting budget after warming the ice:

$$m_{melt}=\frac{62790-6300}{3.34e5}=0.169\ \text{kg}$$

Final state: **$T=0°$C** with $0.30-0.169=0.131$ kg of ice remaining.

**(d)** Decision procedure: (1) warm all ice to $0°$C — if the water can't afford it, stop ($T_f<0$). (2) melt all ice — if it can't, stop ($T_f=0$, partial ice). (3) otherwise, warm the combined water to $T_f$. Never assume the final state; check it.

---

## Problem 4 — The Rectangle Engine

**(a)** $T=PV/(nR)$ with $R=0.0821$ L·atm/mol·K:

$$T_A=\frac{1\cdot20}{2(0.0821)}=121.8\ \text{K},\quad T_B=\frac{1\cdot60}{2(0.0821)}=365.4\ \text{K}$$

$$T_C=\frac{3\cdot60}{2(0.0821)}=1096\ \text{K},\quad T_D=\frac{3\cdot20}{2(0.0821)}=365.4\ \text{K}$$

$T_B=T_D$ — nice symmetry.

**(b)** Work per cycle = area of the rectangle on the $P$–$V$ diagram:

$$W=\Delta P\Delta V=(3-1)(60-20)=80\ \text{atm·L}=80(101.3)=8104\ \text{J}$$

**(c)** Over a full cycle $\Delta U=0$, so $Q_{net}=W$ (heat added minus heat rejected $=$ net work). Heat is **added** on:
- A→B (isobaric expansion): $Q=\frac52\Delta(PV)=\frac52(40)(101.3)=10130$ J
- B→C (isochoric pressure rise): $Q=\frac32\Delta(PV)=\frac32(120)(101.3)=18234$ J

$$Q_{in}=10130+18234=28364\ \text{J}$$

(Check: rejected on C→D and D→A totals $36468$ J, so $Q_{net}=28364-36468=-8104$ J $=-W$ ✓)

**(d)** $e=W/Q_{in}=8104/28364=28.6\%$.

**(e)** Carnot between the extremes:

$$e_{Carnot}=1-\frac{T_A}{T_C}=1-\frac{121.8}{1096}=88.9\%$$

The rectangle is far worse because its constant-pressure and constant-volume legs exchange heat at non-constant temperature — a highly irreversible heat-exchange profile. Carnot is the ceiling.

---

## Problem 5 — The Photon That Kicks an Electron

**(a)** Photon energy:

$$E_{ph}=\frac{hc}{\lambda}=\frac{1240\ \text{eV·nm}}{250\ \text{nm}}=4.96\ \text{eV}$$

$$KE_{max}=E_{ph}-\phi=4.96-2.28=2.68\ \text{eV}$$

Stopping voltage (energy in eV = voltage): $V_s=2.68$ V.

**(b)** Doubling intensity doubles the number of photons per second → **more electrons**, each with the **same** $KE_{max}$. The electron energy depends only on frequency (wavelength), not intensity — the heart of the photoelectric effect.

**(c)** $KE=2.68(1.6e-19)=4.29\times10^{-19}$ J:

$$v=\sqrt{\frac{2KE}{m}}=\sqrt{\frac{2(4.29e-19)}{9.11e-31}}=9.7\times10^5\ \text{m/s}$$

$$\lambda_{dB}=\frac{h}{mv}=\frac{6.63e-34}{(9.11e-31)(9.7e5)}=7.5\times10^{-10}\ \text{m}\approx0.75\ \text{nm}$$

**(d)** Threshold: $KE=0$ when $E_{ph}=\phi$:

$$\lambda_{max}=\frac{hc}{\phi}=\frac{1240}{2.28}=544\ \text{nm}$$

Longer (lower-energy) photons eject nothing, no matter how intense. This wavelength dependence — not intensity — is what classical wave theory could not explain.
