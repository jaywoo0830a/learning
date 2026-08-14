# E&M — Day 2 — Solutions

> Full worked solutions. Solve each problem fully on paper before reading.

---

## Problem 1 — Four Charges, Quiet Center

**(a)** Distance from the center to each corner: $r=a/\sqrt2=0.30/\sqrt2=0.212$ m. Each charge contributes $E=kq/r^2$ along its diagonal. By symmetry the two $+q$ fields point away from their corners and the two $-q$ fields point toward theirs; opposite corners cancel in pairs → **$E_{center}=0$**.

**(b)** Potential is a scalar sum: $V=\frac{k}{r}(q_1+q_2+q_3+q_4)=\frac{k}{r}(2+2-2-2)\,\mu$C $=0$.

**(c)** At the midpoint of the edge between the two $+$ charges, say $(0.15,0)$:

- The two $+$ charges are at $0.15$ m: their fields point in $\pm x$ and cancel.
- The two $-$ charges are at $r=\sqrt{0.15^2+0.30^2}=0.335$ m, each contributing:

$$E=kq/r^2=\frac{(8.99e9)(2e-6)}{(0.335)^2}=1.60\times10^5\ \text{N/C}$$

Their $y$-components add (upward), the $x$-components cancel:

$$E=2(1.60e5)\frac{0.30}{0.335}=2.9\times10^5\ \text{N/C}\ \text{(upward)}$$

Potential:

$$V=kq\left[\frac{1}{0.15}+\frac{1}{0.15}-\frac{1}{0.335}-\frac{1}{0.335}\right]=(17980)(13.33-5.97)=1.3\times10^5\ \text{V}$$

---

## Problem 2 — The Dielectric Two-Step

**(a)** $C=\varepsilon_0A/d=(8.85e-12)(0.01)/0.001=8.9\times10^{-11}$ F ≈ 88.5 pF.

**(b)** $Q=CV=(8.9e-11)(100)=8.9\times10^{-9}$ C. $U=\tfrac12CV^2=\tfrac12(8.9e-11)(10^4)=4.4\times10^{-7}$ J.

**(c)** Connected to battery → $V$ stays at $100$ V:

$$C'=\kappa C=3(88.5)=265\ \text{pF},\quad Q'=C'V=2.7\times10^{-8}\ \text{C},\quad U'=\tfrac12C'V^2=1.3\times10^{-6}\ \text{J}$$

Energy **rises** — the battery does work pushing extra charge onto the plates.

**(d)** Disconnected → $Q$ stays at $8.9$ nC:

$$V'=\frac{Q}{C'}=\frac{8.9e-9}{2.65e-10}=33.3\ \text{V},\quad U'=\tfrac12QV'=\tfrac12(8.9e-9)(33.3)=1.5\times10^{-7}\ \text{J}$$

Energy **falls** — the dielectric is pulled in, doing work on the plates (it does positive work, converting field energy into mechanical).

**One rule, two directions:** battery connected → $V$ constant; disconnected → $Q$ constant. The energy behavior is opposite in the two cases.

---

## Problem 3 — The Bridge That Measures

**(a)** $R_{branch1}=8+4=12\,\Omega$; $R_{branch2}=6+12=18\,\Omega$:

$$R_{eq}=\frac{(12)(18)}{12+18}=7.2\,\Omega,\qquad I_{tot}=\frac{24}{7.2}=3.3\ \text{A}$$

**(b)** Branch 1: $24/12=2$ A through both $R_1,R_2$. Branch 2: $24/18=1.33$ A through both $R_3,R_4$.

**(c)** $V_{R1}=2(8)=16$ V; $V_{R2}=2(4)=8$ V; $V_{R3}=1.33(6)=8$ V; $V_{R4}=1.33(12)=16$ V.

**(d)** $P=I^2R$: $R_1$: 32 W, $R_2$: 16 W, $R_3$: 10.7 W, $R_4$: 21.3 W. Sum $=80$ W $=V_{batt}I_{tot}=24(3.33)$ ✓.

**(e)** Midpoint 1 (between $R_1$ and $R_2$) is at $24-16=8$ V above the bottom rail. Midpoint 2 (between $R_3$ and $R_4$) is at $24-8=16$ V. Voltmeter reads $|16-8|=8$ V.

**(f)** Balance ⇒ no current through the meter ⇒ the two midpoints sit at the same potential. Then $V_{R2}=V_{R4}$ and $V_{R1}=V_{R3}$. With branch currents $I_1,I_2$:

$$I_1R_2=I_2R_4,\qquad I_1R_1=I_2R_3\;\Rightarrow\;\frac{R_1}{R_2}=\frac{R_3}{R_4}$$

With $R_4=3\,\Omega$: $8/4=6/3$ ✓. A null reading is the classic way to measure an unknown resistance.

---

## Problem 4 — The Helix

**(a)** $F=qvB\sin30=(1.6e-19)(4e6)(0.2)(0.5)=6.4\times10^{-14}$ N.

**(b)** Only the perpendicular component drives circular motion:

$$v_\perp=v\sin30=2.0\times10^6\ \text{m/s},\qquad r=\frac{mv_\perp}{qB}=\frac{(1.67e-27)(2e6)}{(1.6e-19)(0.2)}=0.10\ \text{m}$$

**(c)** Period of the circular component: $T=2\pi m/(qB)=2\pi(1.67e-27)/\big((1.6e-19)(0.2)\big)=3.3\times10^{-7}$ s. Parallel speed: $v_\parallel=v\cos30=3.5\times10^6$ m/s. Pitch:

$$p=v_\parallel T=(3.5e6)(3.3e-7)=1.1\ \text{m}$$

**(d)** No work: $\mathbf F\perp\mathbf v$ at every instant, so $W=0$ and the speed (hence KE) never changes — only the direction does. Magnetic fields steer; they never speed up or slow down a particle.

---

## Problem 5 — Coil in a Collapsing Field

**(a)** $\Phi=NBA=50(0.6)\pi(0.1)^2=0.94$ Wb.

**(b)** $\mathcal{E}=|\Delta\Phi/\Delta t|=0.94/0.05=18.8$ V.

**(c)** Rotating $90°$ changes the flux from $\Phi$ to $0$ — the same total change, over $0.10$ s:

$$\mathcal{E}=\frac{0.94}{0.10}=9.4\ \text{V}$$

Only the *rate* of flux change matters, not how you produce it.

**(d)** $I=\mathcal{E}/R=18.8/10=1.9$ A. Lenz's law: the induced current must oppose the *decrease* of the field (into the page). It circulates to produce a field **out of the page** — counterclockwise when viewed along the original field direction.

**(e)** Twice the rate ⇒ twice the emf: $\mathcal{E}=37.7$ V, $I=3.8$ A (still $I=\mathcal{E}/R$).
