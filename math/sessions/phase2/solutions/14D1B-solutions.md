# Solutions — 14D1B: Product & Quotient Rules

> Back to [14D1B — Product & Quotient Rules](../14D1B-product-quotient-interpretation.md)

---

## Advanced Drill

### A1.

**(a)** $m$ constant: $F = \frac{dp}{dt} = \frac{d}{dt}(mv) = m\frac{dv}{dt} + \frac{dm}{dt}v = ma + 0 = ma$.

**(b)** $F = m\frac{dv}{dt} + v\frac{dm}{dt}$. Channel 1, $m\frac{dv}{dt}$: freeze the mass, vary the speed — "accelerating the mass that is already here." Channel 2, $v\frac{dm}{dt}$: freeze the speed, vary the mass — the momentum carried by the mass flow itself, at the rate $v \times (\mathrm{kg/s})$. Units: $\mathrm{kg}\cdot\mathrm{m/s}^2 = \mathrm{N}$ and $(\mathrm{m/s})(\mathrm{kg/s}) = \mathrm{N}$ — both channels are forces, sharing one budget.

**(c)** $v$ is constant, so channel 1 is zero; the sand arrives at $v_{flow}=0$, so channel 2 carries the whole budget: $F = v\dot m = 2 \times 3 = 6$ N. Each second, 3 kg must be sped from rest to 2 m/s — that costs $3 \times 2$ kg·m/s of push per second.

**(d)** The exhaust leaves at $v_{flow} = v-u$, not at $v$. The closed-system law: $F_{ext} = m\frac{dv}{dt} + \frac{dm}{dt}(v - v_{flow}) = m\frac{dv}{dt} - u\frac{dm}{dt}$. With $\frac{dm}{dt} = -5$ kg/s: thrust $= -u\frac{dm}{dt} = 2000 \times 5 = 10{,}000$ N — **independent of $v$**. The naive channel reads $v\frac{dm}{dt}$: at $v = 3000$ m/s it says $-15{,}000$ N — wrong, because it counts the leaving mass at the rocket's own velocity instead of the exhaust's.

**(e)** The frame question: *at what velocity does the mass actually enter or leave?* Then use $F_{ext} = m\frac{dv}{dt} + \frac{dm}{dt}(v - v_{flow})$. Water dripping straight down from a moving truck leaves with the truck's horizontal velocity: $v_{flow} = v$, so the second channel is zero and $F_{ext} = m\frac{dv}{dt}$ — no thrust, no drag. The same mass flow can push (exhaust, $v_{flow}=v-u$), do nothing (leak, $v_{flow}=v$), or resist (sand poured against the motion) — all decided by $v_{flow}$.

> **Answer**: (a) $F=ma$; (b) two force-channels: accelerate-current-mass + momentum-of-mass-flow; (c) $6$ N, all in the mass channel; (d) thrust $=-u\dot m = 10{,}000$ N, independent of $v$; (e) ask $v_{flow}$ first

### A2.

**(a)** $A = xy$, so $\frac{dA}{dt} = x\frac{dy}{dt} + y\frac{dx}{dt}$. Channel 1, $x\frac{dy}{dt} = (3+0.2t)(-0.1)$: the width is frozen at its current value while the height shrinks — "the height shrinking costs area." Channel 2, $y\frac{dx}{dt} = (2-0.1t)(0.2)$: the height is frozen while the width grows — "the width growing adds area."

**(b)** At $t=0$: channel 1 $= 3(-0.1) = -0.3$ cm²/s, channel 2 $= 2(0.2) = 0.4$ cm²/s → total $+0.1$ cm²/s: the width channel wins, the area grows. At $t=10$: $x=5$, $y=1$, channel 1 $= -0.5$, channel 2 $= 0.2$ → total $-0.3$ cm²/s: the height channel wins, the area shrinks. (The balance flips at $t=2.5$, where $\frac{dA}{dt} = 0.1 - 0.04t = 0$.)

> **Answer**: $\frac{dA}{dt} = x\dot y + y\dot x$; at $t=0$: $-0.3 + 0.4 = +0.1$ cm²/s (growing); at $t=10$: $-0.5 + 0.2 = -0.3$ cm²/s (shrinking)

### A3.

**(a)** $R' = q + p\,q'$. Channel 1, $q$: price frozen — "selling one more unit at the current price adds $q$ dollars." Channel 2, $p\,q'$: volume frozen — "changing the price on the $q$ units we already sell changes revenue by $p\,q'$ dollars."

**(b)** At $p=20$: $q = 300$, $q' = -10$. Channel 1: $+300$; channel 2: $20(-10) = -200$. Net $R' = 100 > 0$ — the volume channel wins: a small price hike still raises revenue (inelastic, $|E| = \frac23 < 1$, as in 14D1 Ex8).

**(c)** At $p=25$: $q=250$, channel 1 $= +250$, channel 2 $= 25(-10) = -250$ — equal and opposite, so $R' = 0$: the budget balances exactly at the revenue peak, which is exactly $E = -1$.

> **Answer**: (b) $+300$ vs $-200$ → $R'=100$ (volume channel winning); (c) balanced channels $= R'=0 = E=-1$ = revenue peak

### A4.

**(a)** Thrust $= -u\frac{dm}{dt} = u\left|\frac{dm}{dt}\right| = 2500 \times 4 = 10{,}000$ N.

**(b)** $F_{ext} = 0$, so $m\frac{dv}{dt} - u\frac{dm}{dt} = 0$ → $a = \frac{10{,}000}{m}$. At launch ($m = 1000$ kg): $a = 10$ m/s². At $m = 600$ kg: $a = \frac{10{,}000}{600} \approx 16.7$ m/s².

**(c)** The thrust is constant, but the mass it must accelerate is melting away — the same force pushes a shrinking object, so the acceleration climbs. (This is exactly why rockets stage: discard empty tanks and the same thrust buys more acceleration.)

**(d)** The student's equation is the product-rule split of the rocket's *own* momentum, and its second channel uses the rocket's velocity for the leaving mass. At launch the exhaust actually leaves at $v_{flow} = v - u = -2500$ m/s — not at $v = 0$. The closed-system law is $F_{ext} = m\frac{dv}{dt} - u\frac{dm}{dt}$, whose second term is $+10{,}000$ N of thrust. Setting $v = 0$ in the wrong channel and declaring the force zero is exactly the trap Example 1 warns about: ask $v_{flow}$ before reading any $\frac{dm}{dt}$ term.

> **Answer**: (a) 10,000 N; (b) 10 → 16.7 m/s²; (c) constant force, shrinking mass; (d) the exhaust leaves at $v-u$, not $v$

### A5.

**(a)** $AC = \frac{C}{q}$ → $AC' = \frac{C'\,q - C\cdot 1}{q^2} = \frac{C' - C/q}{q} = \frac{MC - AC}{q}$.

**(b)** Channels: numerator $+\frac{C'}{q}$, dilution $-\frac{C}{q^2}$.
- $q=6$: $C' = 16$, $C = 204$. Channels: $+\frac{16}{6} \approx +2.67$ and $-\frac{204}{36} \approx -5.67$ → $AC' = -3$ \$/item per item. The dilution channel wins: $MC = 16 < AC = 34$, so the next unit *drags the average down*.
- $q=20$: $C' = 44$, $C = 624$. Channels: $+\frac{44}{20} = +2.2$ and $-\frac{624}{400} = -1.56$ → $AC' = +0.64$. The numerator channel wins: $MC = 44 > AC = 31.2$, so the next unit *pulls the average up*.

**(c)** $AC' = 0$ ⟺ $MC = AC$: $2q+4 = q+4+\frac{144}{q}$ → $q^2 = 144$ → $q = 12$ — the minimum of $AC$ from 14D1 Ex6, where both equal 28.

> **Answer**: $AC' = (MC-AC)/q$; at $q=6$: $+2.67 - 5.67 = -3$ (falling); at $q=20$: $+2.2 - 1.56 = +0.64$ (rising); still at $q=12$

### A6.

**(a)** $\bar v = \frac{s}{t}$ → $\bar v' = \frac{s'\,t - s}{t^2} = \frac{v - s/t}{t} = \frac{v - \bar v}{t}$.

**(b)** At $t=8$: $s = 224$, $v = 36$, $\bar v = 28$. Channels: $+\frac{v}{t} = \frac{36}{8} = 4.5$ and $-\frac{s}{t^2} = -\frac{224}{64} = -3.5$ → $\bar v' = 1$ m/s². Sentence: "the instantaneous speed (36 m/s) sits above the average (28 m/s), so the average is being pulled up at 1 m/s per second."

**(c)** Both channels have units $\frac{\mathrm{m/s}}{\mathrm{s}} = \mathrm{m/s^2}$ — the average speed has an acceleration of its own.

**(d)** $\bar v' = 0$ ⟺ $v = \bar v$: the average turns exactly when the instantaneous value meets it. Here $20 + 2t = 20 + t$ → $t = 0$ only — an accelerating car's average speed keeps climbing forever.

> **Answer**: $\bar v' = (v-\bar v)/t$; at $t=8$: $4.5 - 3.5 = +1$ m/s²; $v = \bar v$ only at $t=0$

### A7.

**(a)** $g = \frac{G}{P} = 2000\,e^{0.01t}$ \$/person ($g(0) = 2000$ \$/person).

**(b)** At $t=0$: $G' = 80$ million \$/yr, $P' = 0.03$ million/yr. Numerator channel $= \frac{G'}{P} = 80$ \$/yr. Dilution channel $= -\frac{G\,P'}{P^2} = -2000(0.03) = -60$ \$/yr. Net $g' = +20$ \$/yr — 1% growth.

**(c)** $\frac{g'}{g} = 0.01 = 0.04 - 0.03 = \frac{G'}{G} - \frac{P'}{P}$ ✓.

**(d)** Flat when $\frac{G'}{G} = \frac{P'}{P}$; falling when the population rate exceeds the economy's. The levels never enter: a \$20-trillion economy growing 2% while its population grows 3% still gets poorer per person. A ratio hears differences of rates, not sizes.

> **Answer**: $g = 2000e^{0.01t}$; channels $+80 - 60 = +20$ \$/yr (1%); flat ⟺ equal percentage rates

### A8.

**(a)** $I = \frac{230}{460} = 0.5$ A. Channels: $+\frac{V'}{R} = \frac{-2.3}{460} = -0.005$ and $-\frac{V\,R'}{R^2} = -\frac{230 \times 9.2}{460^2} = -0.01$ → $\frac{dI}{dt} = -0.015$ A/s.

**(b)** $V'/V = -2.3/230 = -1\%$/s; $R'/R = 9.2/460 = +2\%$/s; $I'/I = -0.015/0.5 = -3\%$/s $= (-1\%) - (+2\%)$ ✓.

**(c)** The voltage sag alone would cost 1%; but the filament's heating raises the resistance, spreading the same voltage over more ohms — the dilution channel adds another 2%. Two channels, both working against the current.

> **Answer**: $I = 0.5$ A; channels $-0.005 - 0.01 = -0.015$ A/s $= -1\% - 2\% = -3\%$/s

---

## Answer Check

| Problem | Answer |
|:---:|:---|
| A1 | $F=ma$; channels $m\dot v$ + $v\dot m$ (both N); belt $6$ N; thrust $-u\dot m = 10^4$ N; ask $v_{flow}$ |
| A2 | $A' = x\dot y + y\dot x$; $+0.1$ → $-0.3$ cm²/s |
| A3 | channels $q$ vs $p\,q'$; balanced at $p=25$ ($R'=0$) |
| A4 | $10^4$ N; $10$ → $16.7$ m/s²; exhaust leaves at $v-u$ |
| A5 | $AC' = (MC-AC)/q$; $q{=}6$: $-3$; $q{=}20$: $+0.64$; still at $q{=}12$ |
| A6 | $\bar v' = (v-\bar v)/t$; $4.5 - 3.5 = +1$ m/s² |
| A7 | $g = 2000e^{0.01t}$; $+80 - 60 = +20$ \$/yr |
| A8 | $0.5$ A; $-0.015$ A/s = $-3\%$/s |
