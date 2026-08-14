# E&M — Day 3 — Solutions

> Full worked solutions. Solve each problem fully on paper before reading.

---

## Problem 1 — The Floating Oil Drop

**(a)** $E=V/d=500/0.02=2.5\times10^4$ V/m.

**(b)** Suspended motionless ⇒ electric force balances weight:

$$qE=mg\;\Rightarrow\;q=\frac{mg}{E}=\frac{(2.5e-15)(9.8)}{2.5e4}=9.8\times10^{-19}\ \text{C}$$

**(c)** Number of excess electrons:

$$n=\frac{q}{e}=\frac{9.8e-19}{1.6e-19}=6.1$$

Charge is quantized — the drop must carry an **integer** number of electrons, so it almost surely has **6** excess electrons ($q=9.6\times10^{-19}$ C). The 0.1 discrepancy just reflects approximate input numbers. The integer result is the physics: this is exactly the quantization that Millikan measured.

**(d)** With exactly 5 electrons, $q=5e=8.0\times10^{-19}$ C:

$$V=\frac{mgd}{q}=\frac{(2.5e-15)(9.8)(0.02)}{8.0e-19}=612.5\ \text{V}$$

---

## Problem 2 — Two Capacitors, Two Ways

**(a)** $Q_1=C_1V_1=(4e-6)(100)=400\,\mu$C, $U_1=\tfrac12(4e-6)(100)^2=0.020$ J.
$Q_2=(6e-6)(50)=300\,\mu$C, $U_2=\tfrac12(6e-6)(50)^2=0.0075$ J.

**(b)** Same polarity, parallel: charges add, capacitances add:

$$Q_{net}=700\,\mu\text{C},\quad C_{tot}=10\,\mu\text{F},\quad V_f=\frac{700}{10}=70\ \text{V}$$

$$U_f=\tfrac12(10e-6)(70)^2=0.0245\ \text{J}$$

Lost: $U_i-U_f=(0.020+0.0075)-0.0245=0.003$ J = 3 mJ (dissipated as heat in the connecting wires).

**(c)** Opposite polarity: the net charge is the *difference*:

$$Q_{net}=400-300=100\,\mu\text{C}\;\Rightarrow\;V_f=\frac{100}{10}=10\ \text{V}$$

$$U_f=\tfrac12(10e-6)(10)^2=0.5\ \text{mJ}$$

Lost: $0.0275-0.0005=27$ mJ — nine times more than in (b). Connecting opposite polarities forces a huge surge current as charges annihilate across the junction, dissipating far more energy. **Always track the sign of the net charge.**

---

## Problem 3 — Maximum Power, Minimum Efficiency

**(a)** $I=\mathcal{E}/(R+r)=12/(4+2)=2$ A; $V_{term}=\mathcal{E}-Ir=12-2(2)=8$ V.

**(b)** Power delivered to $R$:

$$P(R)=I^2R=\frac{\mathcal{E}^2R}{(R+r)^2}$$

To maximize, set $dP/dR=0$ (or note the standard result): the maximum occurs at $R=r=2\,\Omega$:

$$P_{max}=\frac{\mathcal{E}^2}{4r}=\frac{144}{8}=18\ \text{W}$$

**(c)** Check:

| $R$ (Ω) | 0.5 | 1 | 2 | 4 | 8 |
|--------|----|----|----|----|----|
| $P$ (W) | 11.5 | 16 | 18 | 16 | 11.5 |

Max confirmed at $R=2\,\Omega$.

**(d)** At $R=r$, half the battery's power is dissipated inside the battery:

$$\text{efficiency}=\frac{P_{load}}{P_{total}}=\frac{I^2R}{I^2(R+r)}=\frac{R}{R+r}=50\%$$

Max power and max efficiency cannot coexist — that's the power/efficiency trade-off.

---

## Problem 4 — The Loop That Slides Into the Field

**(a)** While partially inside, only the leading edge of length $w$ cuts flux:

$$\mathcal{E}=Bwv=0.5(0.2)(2)=0.2\ \text{V},\qquad I=\frac{\mathcal{E}}{R}=\frac{0.2}{0.5}=0.4\ \text{A}$$

Magnetic drag (Lenz: current opposes motion):

$$F=BIw=0.5(0.4)(0.2)=0.04\ \text{N}$$

You must pull with $0.04$ N to keep $v$ constant.

**(b)** Fully inside: the flux through the loop is constant → $\mathcal{E}=0$, no current, no force.

**(c)** Exiting: the flux is *decreasing*, so Lenz reverses the current direction. Magnitudes are identical: $\mathcal{E}=0.2$ V, $I=0.4$ A, $F=0.04$ N (again opposing the pull).

**(d)** $P_{you}=Fv=0.04(2)=0.08$ W. $P_R=I^2R=(0.4)^2(0.5)=0.08$ W ✓. The resistor's power bill is paid exactly by your mechanical work.

---

## Problem 5 — The Magnet, the Tube, and the Solenoid

**(a)** In copper, the falling magnet induces eddy currents; by Lenz's law these create fields that oppose the magnet's motion → strong magnetic drag → the magnet falls slowly, near terminal speed. In plastic there are no free charges, no eddy currents → free fall. Energy chain: gravitational PE → electrical (eddy) energy → heat.

**(b)** $B=\mu_0 nI=4\pi(10^{-7})(200/0.4)(3)=1.9\times10^{-3}$ T.

**(c)** Flux through the small 10-turn coil: $\Phi=10\,B(\pi r^2)=10(1.9e-3)\pi(0.01)^2=5.9\times10^{-6}$ Wb. When the current is switched off, this flux collapses to zero in $0.010$ s:

$$\mathcal{E}=\frac{\Delta\Phi}{\Delta t}=\frac{5.9e-6}{0.01}=5.9\times10^{-4}\ \text{V}$$

**(d)** By Lenz's law, the induced current flows in the **same sense** as the original solenoid current — it tries to maintain the collapsing field. Lenz's law in one sentence: the induced effect always opposes the change that created it.
