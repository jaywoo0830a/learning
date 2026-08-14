# Others — Day 2 — Solutions

> Full worked solutions. Solve each problem fully on paper before reading.

---

## Problem 1 — The Speaker's Sphere

**(a)** Isotropic radiation spreads over a sphere:

$$I=\frac{P}{4\pi r^2}=\frac{1.0}{4\pi(5.0)^2}=3.2\times10^{-3}\ \text{W/m}^2$$

**(b)** $L=10\log_{10}(I/I_0)=10\log_{10}(3.2\times10^9)=95$ dB.

**(c)** $80$ dB ⇒ $I=10^{-12}\cdot10^8=10^{-4}$ W/m²:

$$r^2=\frac{P}{4\pi I}=\frac{1.0}{4\pi(1e-4)}=795.8\;\Rightarrow\;r=28.2\ \text{m}$$

**(d)** Coherent, in-phase, path difference $=\lambda$: amplitudes add ($A\to2A$), so $I\propto A^2$ quadruples:

$$\Delta L=10\log_{10}(4)=+6.0\ \text{dB}$$

Incoherent speakers: intensities (powers) add, $I\to2I$:

$$\Delta L=10\log_{10}(2)=+3.0\ \text{dB}$$

Interference is about **amplitudes** (×4 for two in-phase); "adding sources" is about **powers** (×2). A 2× vs 4× factor — a 3 dB vs 6 dB difference.

---

## Problem 2 — Lens, Then Mirror

**(a)** Thin-lens equation:

$$\frac{1}{12}+\frac{1}{d_i}=\frac{1}{8}\;\Rightarrow\;\frac{1}{d_i}=\frac{1}{8}-\frac{1}{12}=\frac{1}{24}\;\Rightarrow\;d_i=24\ \text{cm}$$

Real, inverted, at $24$ cm past the lens — that is $4$ cm **behind** the mirror (mirror at 20 cm). Magnification $m=-d_i/d_o=-24/12=-2$.

**(b)** Step 1 — mirror: the lens's image at 4 cm behind the mirror produces a plane-mirror virtual image 4 cm **in front** of the mirror, i.e. $20-4=16$ cm to the right of the lens.

Step 2 — second lens pass: this virtual image acts as a **virtual object** at $d_o=-16$ cm (light appears to diverge from a point on the far side):

$$\frac{1}{8}=\frac{1}{-16}+\frac{1}{d_i}\;\Rightarrow\;\frac{1}{d_i}=\frac{1}{8}+\frac{1}{16}=\frac{3}{16}\;\Rightarrow\;d_i=+5.3\ \text{cm}$$

Positive ⇒ real, on the right side of the lens (between lens and mirror). Second-pass magnification:

$$m_2=-\frac{d_i}{d_o}=-\frac{5.3}{-16}=+\tfrac13$$

Total: $m=m_1\cdot m_{mirror}\cdot m_2=(-2)(1)(+\tfrac13)=-\tfrac23$.

**Final image:** real, inverted, $\tfrac23\times$ the object size, $5.3$ cm to the right of the lens.

---

## Problem 3 — The Double Slit Goes Swimming

**(a)** Fringe spacing:

$$\Delta y=\frac{\lambda L}{d}=\frac{(550e-9)(2.0)}{0.20e-3}=5.5\times10^{-3}\ \text{m}=5.5\ \text{mm}$$

**(b)** In water, $\lambda$ shrinks by $n$:

$$\lambda'=\frac{\lambda}{n}=\frac{550}{1.33}=413.5\ \text{nm}\;\Rightarrow\;\Delta y=\frac{(413.5e-9)(2.0)}{0.20e-3}=4.1\ \text{mm}$$

**(c)** $d$ halved ($0.10$ mm) doubles the spacing: $\Delta y=11$ mm.

**(d)** A half-wavelength delay adds $\pi$ of phase: where the beams were in phase they are now out of phase. The **central maximum becomes dark**, and bright/dark fringes swap. A full-wavelength delay shifts the pattern by exactly one fringe — the pattern *looks identical* but is displaced. This phase sensitivity is how interferometers measure sub-wavelength changes.

---

## Problem 4 — Steam Into the Cup

**(a)** Each gram of steam condensing releases latent heat $L_v$ *and* then cools from $100°$C to $50°$C. Energy balance:

$$m_s\big[L_v+c_w(100-50)\big]=m_w c_w(50-20)$$

$$m_s\big[2.26e6+4186(50)\big]=(0.4)(4186)(30)=50232$$

$$m_s=\frac{50232}{2.469\times10^6}=0.0203\ \text{kg}\approx20\ \text{g}$$

**(b)** To reach exactly $100°$C (condensed water no longer cools):

$$m_sL_v=m_w c_w(100-20)=(0.4)(4186)(80)=133952$$

$$m_s=\frac{133952}{2.26e6}=0.0593\ \text{kg}\approx59\ \text{g}$$

**(c)** No. Once the mixture is at $100°$C, adding more steam just condenses while the water stays at $100°$C (further heat would boil water, not raise its temperature). Steam at $100°$C can never push liquid water above its boiling point.

---

## Problem 5 — Carbon in the Artifact

**(a)** Activity ratio:

$$\frac{A}{A_0}=\frac{0.0575}{0.23}=\frac14=\left(\frac12\right)^2$$

Two half-lives: $t=2(5730)=11{,}460$ years.

**(b)** $\;^{14}_6\text{C}\to\;^{14}_7\text{N}+e^-+\bar\nu_e$ (beta-minus decay: a neutron converts to a proton).

**(c)** Mass defect:

$$\Delta m=14.003242-(14.003074+0.000549)=0.000381\ \text{u}$$

$$E=\Delta m\,c^2=0.000381(931.5)=0.355\ \text{MeV}$$

**(d)** Alphas are heavy and short-ranged — stopped by a few cm of air or the skin's dead layer — so outside the body they're harmless; but once inhaled/ingested they dump their full energy into a tiny volume of living tissue (high LET = high biological damage). Betas penetrate much further (tens of cm of air, through skin), so they can harm from outside the body, yet per unit distance inside tissue they're less damaging. The danger ranking flips depending on whether the source is outside or inside.
