# E&M — Day 1 — Solutions

> Full worked solutions. Solve each problem fully on paper before reading.

---

## Problem 1 — Three Charges, One Balance Point

**(a)** Let the test charge be at distance $x$ from $+q$. Forces balance:

$$\frac{kqQ}{x^2}=\frac{k(4q)Q}{(d-x)^2}\;\Rightarrow\;(d-x)^2=4x^2\;\Rightarrow\;d-x=2x\;\Rightarrow\;x=\frac{d}{3}=0.20\ \text{m}$$

**(b)** Yes — the force on any test charge is proportional to $q_{test}$, which cancels from the balance equation. The location $d/3$ is independent of the sign or magnitude of the test charge.

**(c)** Along the line: **unstable**. Nudge toward $+4q$: the $4q$ force grows and the $q$ force shrinks, so the net force pushes further away from equilibrium. Perpendicular to the line: **stable** (both charges pull/push the test charge back toward the line). This makes the point a **saddle point** — stable in one direction, unstable in the other.

---

## Problem 2 — The Switch That Raises Resistance

**(a)** Parallel combination: $R_{12}=(6)(3)/(6+3)=2\,\Omega$. Total: $R_{eq}=2+4=6\,\Omega$. Battery current: $I=12/6=2$ A. The parallel pair is at $V=IR_{12}=4$ V:

$$I_{R1}=\frac{4}{6}=0.67\ \text{A},\qquad I_{R2}=\frac{4}{3}=1.33\ \text{A},\qquad I_{R3}=2\ \text{A}$$

**(b)** Switch closed shorts $R_2$: $R_{eq}=6+4=10\,\Omega$, $I=1.2$ A through $R_1$ and $R_3$, and $I_{R2}=0$.

**(c)** Open: battery power $=VI=24$ W; $P_{R2}=V^2/R=16/3=5.3$ W. Closed: battery $=14.4$ W; $P_{R2}=0$.

**Why the counterintuitive result:** $R_2$ was in *parallel* with $R_1$, so shorting it removed a parallel path. Total resistance went from $6\to10\,\Omega$, and the battery delivers *less* power. A "short" only reduces resistance when it bypasses a **series** element.

---

## Problem 3 — Where Does the Energy Go?

**(a)** $U_i=\tfrac12C_1V^2=\tfrac12(6e-6)(144)=4.3\times10^{-4}$ J = 432 μJ. Charge: $Q=C_1V=72\,\mu$C.

**(b)** Charge is conserved. In parallel, $C_{tot}=9\,\mu$F:

$$V_f=\frac{Q}{C_{tot}}=\frac{72}{9}=8\ \text{V},\qquad U_f=\tfrac12(9e-6)(8)^2=2.9\times10^{-4}\ \text{J}=288\ \mu\text{J}$$

**(c)** Lost: $432-288=144\,\mu$J. Energy is **not** conserved in the instantaneous connection because a surge current flows and dissipates $I^2R$ heat (plus a little EM radiation) in the wires. Only *charge* is conserved. In general the loss fraction is:

$$\frac{U_i-U_f}{U_i}=1-\frac{C_1}{C_1+C_2}=\frac{C_2}{C_1+C_2}=\frac{1}{3}$$

If $C_2\to\infty$ (a huge capacitor), $V_f\to0$ and all the energy is lost.

---

## Problem 4 — The Velocity Selector

**(a)** Straight motion requires the electric and magnetic forces to cancel:

$$qE=qvB\;\Rightarrow\;v=\frac{E}{B}=\frac{2000}{0.5}=4.0\times10^3\ \text{m/s}$$

**(b)** At 10% higher speed, $qvB>qE$: the magnetic force ($q\mathbf v\times\mathbf B$) dominates and the path bends in its direction.

**(c)** Yes, still straight. The condition $v=E/B$ contains neither $m$ nor $q$ — *any* charged particle at exactly $E/B$ passes undeflected. That's why it's called a velocity selector.

**(d)** In the pure $B$ region, $qvB=mv^2/r$:

$$r=\frac{mv}{qB}=\frac{(1.67e-27)(4.0e3)}{(1.6e-19)(0.5)}=8.4\times10^{-5}\ \text{m}$$

---

## Problem 5 — Pulling the Rod Through a Field

**(a)** The moving rod generates motional emf $\mathcal{E}=BLv$, driving $I=BLv/R$. The magnetic "drag" force on the rod is $F_B=BIL=B^2L^2v/R$. At terminal speed, the external force balances this drag:

$$F=\frac{B^2L^2v}{R}\;\Rightarrow\;v=\frac{FR}{B^2L^2}=\frac{0.2(2)}{(0.4)^2(0.5)^2}=10\ \text{m/s}$$

**(b)** $P_{mech}=Fv=0.2(10)=2$ W. Current: $I=BLv/R=0.4(0.5)(10)/2=1$ A. $P_R=I^2R=1^2(2)=2$ W. Equal ✓ — the mechanical work is exactly converted to Joule heating.

**(c)** $v=FR/(B^2L^2)\propto1/B^2$: doubling $B$ quarters the speed → $v=2.5$ m/s.

**(d)** With rod resistance $r=0.50\,\Omega$, total resistance $R_{tot}=2.5\,\Omega$:

$$v=\frac{FR_{tot}}{B^2L^2}=\frac{0.2(2.5)}{0.04}=12.5\ \text{m/s}$$
