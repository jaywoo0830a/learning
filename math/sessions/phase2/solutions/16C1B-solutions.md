# Solutions — 16C1B: Integral Techniques

> Back to [16C1B — Integral Techniques](../16C1B-integral-techniques.md)

---

## RP Drills

### RPB1.

**(a)** $u = x^2+1$; exchange rate $\frac{du}{dx} = 2x$ — "each small step of $x$ buys $2x$ units of $u$." The leftover factor $6x = 3\cdot(2x)$.

**(b)** Limits: $u(0) = 1$, $u(1) = 2$. $\int_0^1 6x(x^2+1)^2\,dx = \int_1^2 3u^2\,du = [u^3]_1^2 = 8-1 = 7$.

**(c)** Undo: $\frac{d}{dx}(x^2+1)^3 = 3(x^2+1)^2\cdot 2x = 6x(x^2+1)^2$ ✓ — the chain rule reads the relation forward again.

> **Answer**: $7$

**Lens reading**: the exchange rate $2x$ converted x-steps into u-steps; the collection in $u$ is clean — 7.

### RPB2.

$u = \sin t$, so $du = \cos t\,dt$ — the cosine is exactly the exchange rate between $u$ and $t$. Limits: $u(0) = 0$, $u(\frac\pi2) = 1$.

$\int_0^{\pi/2}\sin t\cos t\,dt = \int_0^1 u\,du = \frac12$.

> **Answer**: $\frac12$

**Lens reading**: the cosine is the exchange rate; renaming the driver turned a product relation into a pure power — $\frac12$.

### RPB3.

$u = x$ (degree of relation to $x$ is 1 — it simplifies), $dv = \cos x\,dx$ → $v = \sin x$, $du = dx$.

$\int x\cos x\,dx = x\sin x - \int \sin x\,dx = x\sin x + \cos x + C$.

Undo: $(x\sin x + \cos x)' = \sin x + x\cos x - \sin x = x\cos x$ ✓.

> **Answer**: $x\sin x + \cos x + C$

**Lens reading**: parts handed the relation from $x$ (degree 1) to the other channel, then collected — $x\sin x + \cos x$.

### RPB4.

$u = t$ (degree 1 — simpler), $dv = e^{-t}dt$ → $v = -e^{-t}$, $du = dt$.

$\int_0^1 t\,e^{-t}dt = [-te^{-t}]_0^1 + \int_0^1 e^{-t}dt = -e^{-1} - [e^{-t}]_0^1 = -\frac1e - \left(\frac1e - 1\right) = 1 - \frac2e \approx 0.264$.

> **Answer**: $1 - \frac2e \approx 0.264$

**Lens reading**: parts traded the $t$-channel for the exponential's, collecting $1 - \frac2e$.

### RPB5.

$u = x^2+1$, $du = 2x\,dx$ — the numerator is exactly the exchange rate.

$\int\frac{2x}{x^2+1}\,dx = \int\frac{du}{u} = \ln|u| + C = \ln(x^2+1) + C$.

The collection recovered the reciprocal relation: $\ln u$'s degree of relation to $u$ is $\frac1u$ — integrating $\frac1u$ re-assembles the logarithm.

> **Answer**: $\ln(x^2+1) + C$

**Lens reading**: collecting the reciprocal relation reassembled the logarithm.

### RPA1.

**(a)** $V(q) = \frac{q}{C}$ — the voltage's degree of relation to charge is $\frac1C$, uniform: every coulomb already present raises the voltage by the same $\frac1C$ volts.

**(b)** Each parcel $dq$ must be pushed against the voltage already there: $dE = V\,dq$. Collecting all parcels: $E = \int_0^Q \frac{q}{C}\,dq = \frac{Q^2}{2C}$. With $V = \frac{Q}{C}$: $E = \frac12 QV = \frac12 CV^2$.

**(c)** Undo: $\frac{dE}{dQ} = \frac{Q}{C} = V$ ✓ — energy's degree of relation to charge is the voltage itself.

**(d)** The last coulomb climbs the highest voltage — the one all previous coulombs built. A growing relation charges each next step more, so the total is half of final × final.

> **Answer**: $E = \frac{Q^2}{2C} = \frac12 CV^2$; $\frac{dE}{dQ} = V$ ✓

**Lens reading**: the growing voltage relation collects into a triangle — $\frac12 CV^2$.

### RPA2.

**(a)** Voltage-current relation: $V = L\frac{di}{dt}$ — voltage's relation to time is $L$ times current's relation to time. Power: $P = Vi$.

**(b)** Energy = power collected over time: $E = \int P\,dt = \int L\,i\,\frac{di}{dt}\,dt$. Substitution $u = i$, $du = \frac{di}{dt}dt$ — the current is renamed the driver: $E = \int_0^I L\,i\,di = \frac12 LI^2$.

**(c)** Spring $\frac12 kx^2$, capacitor $\frac12 CV^2$, inductor $\frac12 LI^2$ — one grammar: a relation growing linearly from zero, collected, always pays half of final × final.

> **Answer**: $E = \frac12 LI^2$; the same triangle as spring and capacitor

**Lens reading**: renaming the driver to current collected power into energy — $\frac12 LI^2$.

### RPA3.

**(a)** $\frac{dN}{dt} = -kN$ → separate: $\frac{dN}{N} = -k\,dt$. Collect both sides: the reciprocal relation's collection is the logarithm — $\ln N = -kt + C$.

**(b)** Exponentiate: $N = e^C e^{-kt} = N_0 e^{-kt}$ ($N_0 = N(0)$).

**(c)** Half-life: $\frac{N_0}{2} = N_0 e^{-kt_{1/2}}$ → $e^{-kt_{1/2}} = \frac12$ → $t_{1/2} = \frac{\ln 2}{k}$. For $k = 0.1$/hr: $t_{1/2} = \frac{0.693}{0.1} \approx 6.93$ hr.

**(d)** $k$ is the percentage degree of relation of the amount to time — 10% of the drug decays per hour, and that one number fixes the whole decay curve.

> **Answer**: $N = N_0e^{-kt}$; $t_{1/2} = \frac{\ln2}{k} \approx 6.93$ hr for $k=0.1$

**Lens reading**: the decay relation's percentage degree $k$ alone fixes the half-life.

### RPA4.

**(a)** $m\frac{dv}{dt} = mg-kv$ → $\frac{dv}{mg-kv} = \frac{dt}{m}$. Substitution $u = mg-kv$: $\frac{du}{dv} = -k$ — the exchange rate is constant $-k$ — so $dv = -\frac{du}{k}$:

$\int\frac{dv}{mg-kv} = -\frac1k\ln(mg-kv) = \frac{t}{m} + C$.

**(b)** $v(0)=0$: $-\frac1k\ln(mg) = C$. Solve: $\ln\frac{mg-kv}{mg} = -\frac{kt}{m}$ → $v = \frac{mg}{k}\left(1-e^{-kt/m}\right)$.

**(c)** Terminal speed $\frac{mg}{k}$: the point where drag's relation to $v$ (degree $k$) exactly balances gravity's relation to $m$ (degree $g$). Two relations meet; speed stops changing.

**(d)** $v_T = \frac{70 \times 9.8}{14} = 49$ m/s; the time constant $\frac{m}{k} = 5$ s — after 5 s the diver is at 63% of terminal.

> **Answer**: $v = \frac{mg}{k}(1-e^{-kt/m})$; terminal 49 m/s, time constant 5 s

**Lens reading**: the terminal speed balances two relations — gravity's and drag's.

### RPA5.

**(a)** $100 - q^2 = 10 + q$ → $q^2 + q - 90 = 0$ → $q^* = 9$ (thousand), $p^* = 19$.

**(b)** $CS = \int_0^{9}\left[(100-q^2) - 19\right]dq = \int_0^9(81-q^2)\,dq = \left[81q - \frac{q^3}{3}\right]_0^9 = 729 - 243 = 486$ (thousand dollars).

**(c)** Each thin slice at quantity $q$ is one buyer's saved money: what that buyer was willing to pay ($100-q^2$) minus the market price ($19$). The slices come from the high-willingness buyers on the left, which is why the surplus is an area, not a point.

> **Answer**: $(q^*, p^*) = (9, 19)$; $CS = 486$

**Lens reading**: each buyer's saved relation stacks into the surplus triangle — 486.

---

## Answer Check

| Problem | Answer |
|:---:|:---|
| RPB1 | $7$ |
| RPB2 | $\frac12$ |
| RPB3 | $x\sin x + \cos x + C$ |
| RPB4 | $1 - \frac2e \approx 0.264$ |
| RPB5 | $\ln(x^2+1) + C$ |
| RPA1 | $\frac12 CV^2$; $\frac{dE}{dQ}=V$ |
| RPA2 | $\frac12 LI^2$ |
| RPA3 | $N_0e^{-kt}$; $\frac{\ln2}{k}\approx6.93$ hr |
| RPA4 | $\frac{mg}{k}(1-e^{-kt/m})$; 49 m/s |
| RPA5 | $(9,19)$; $CS=486$ |
