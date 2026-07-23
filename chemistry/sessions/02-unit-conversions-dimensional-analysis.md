# Session 02: Unit Conversions & Dimensional Analysis

> **Topic:** Moving between units without getting lost. The chain method.
> **Time:** 150 minutes
> **Big Fat Notebook:** Chapter 4

---

## Opening Attack

Try this:

> A gas pump at an American station dispenses **12.5 gallons** of gasoline. The density of gasoline is **0.720 g/mL**.
>
> How many **milliliters** is 12.5 gallons?
>
> And given that density — what is the mass in **kilograms**?

Stuck on where to start? Good. By the end of this session, you'll chain conversions like dominoes.

---

## Worked Pattern

### Example 1 — Single-Step Metric Conversion

**Problem:** Convert 3500 mL to liters.

**Step 1:** Find the conversion factor.

> $1 \text{ L} = 1000 \text{ mL}$

**Step 2:** Write as a fraction so the unwanted unit cancels.

> $3500 \text{ mL} \times \dfrac{1 \text{ L}}{1000 \text{ mL}} = \text{?}$

**Step 3:** Multiply. mL cancels, L remains.

> $3500 \times 1 \text{ L} \div 1000 = 3.5 \text{ L}$

**Answer:** $\boxed{3.5 \text{ L}}$ (2 sig figs, from 3500 — ambiguous, but $3.5 \times 10^3$ would be clearer).

---

### Example 2 — Single-Step: Which Way Does the Fraction Go?

**Problem:** Convert 0.450 kg to grams.

> The question: should I multiply by $\dfrac{1000 \text{ g}}{1 \text{ kg}}$ or $\dfrac{1 \text{ kg}}{1000 \text{ g}}$?

**Rule:** Put the unit you **WANT** on top. Put the unit you **HAVE** on bottom.

> I HAVE kg. I WANT g.
>
> $\to \dfrac{1000 \text{ g}}{1 \text{ kg}}$ ← g on top, kg on bottom. Correct.
>
> $0.450 \text{ kg} \times \dfrac{1000 \text{ g}}{1 \text{ kg}} = 450 \text{ g}$
>
> $$\cancel{\text{kg}} \times \frac{\text{g}}{\cancel{\text{kg}}} = \text{g} \;\checkmark$$

**Answer:** $\boxed{450 \text{ g}}$ (3 sig figs).

---

### Example 3 — Multi-Step Chain Conversion

**Problem:** Convert 12.5 gallons to milliliters.

> Given: $1 \text{ gal} = 3.785 \text{ L}$, $1 \text{ L} = 1000 \text{ mL}$

**Step 1:** Plan the chain: gallons → liters → milliliters.

**Step 2:** Write each conversion so unwanted units cancel.

> $12.5 \text{ gal} \times \dfrac{3.785 \text{ L}}{1 \text{ gal}} \times \dfrac{1000 \text{ mL}}{1 \text{ L}}$

**Step 3:** Cancel and multiply.

> $\cancel{\text{gal}} \times \dfrac{\cancel{\text{L}}}{\cancel{\text{gal}}} \times \dfrac{\text{mL}}{\cancel{\text{L}}} = \text{mL}$
>
> $12.5 \times 3.785 \times 1000 = 47,\!312.5 \text{ mL}$

**Step 4:** Sig figs. 12.5 has 3 sig figs. 3.785 has 4. 1000 mL/L is exact.

> $\to 47,\!300 \text{ mL} \to 4.73 \times 10^4 \text{ mL}$ (3 sig figs)

**Answer:** $\boxed{4.73 \times 10^4 \text{ mL}}$ (3 sig figs).

---

### Example 4 — Multi-Step with Mass from Density

**Problem:** Using the 12.5 gallons from Example 3 (which we found is $4.73 \times 10^4$ mL), find the mass in kilograms. Density = 0.720 g/mL.

**Step 1:** Use density as a conversion factor: $\dfrac{0.720 \text{ g}}{1 \text{ mL}}$.

**Step 2:** Chain: mL → g → kg.

> $4.73 \times 10^4 \text{ mL} \times \dfrac{0.720 \text{ g}}{1 \text{ mL}} \times \dfrac{1 \text{ kg}}{1000 \text{ g}}$

**Step 3:** Cancel and multiply.

> $\cancel{\text{mL}} \times \dfrac{\cancel{\text{g}}}{\cancel{\text{mL}}} \times \dfrac{\text{kg}}{\cancel{\text{g}}} = \text{kg}$
>
> $4.73 \times 10^4 \times 0.720 \div 1000 = 34.056 \text{ kg}$

**Step 4:** Sig figs. 0.720 has 3 sig figs → $34.1 \text{ kg}$.

**Answer:** $\boxed{34.1 \text{ kg}}$ (3 sig figs).

---

### Example 5 — Derived Unit Conversion: km/h → m/s

**Problem:** A car travels at 90.0 km/h. Convert to m/s.

**Step 1:** Plan: km/h → m/h → m/s. Two conversions needed: km → m, and h → s.

**Step 2:** Write the chain.

> $\dfrac{90.0 \text{ km}}{1 \text{ h}} \times \dfrac{1000 \text{ m}}{1 \text{ km}} \times \dfrac{1 \text{ h}}{3600 \text{ s}}$

**Step 3:** Cancel and multiply.

> $\dfrac{\cancel{\text{km}}}{\cancel{\text{h}}} \times \dfrac{\text{m}}{\cancel{\text{km}}} \times \dfrac{\cancel{\text{h}}}{\text{s}} = \dfrac{\text{m}}{\text{s}}$
>
> $90.0 \times 1000 \div 3600 = 25.0 \text{ m/s}$

**Answer:** $\boxed{25.0 \text{ m/s}}$ (3 sig figs, from 90.0).

> Note: The conversion $1 \text{ h} = 3600 \text{ s}$ is exact. Sig figs come from 90.0.

---

### Example 6 — Density as a Conversion Factor (Both Directions)

**Problem:** Gold has density 19.3 g/cm³.
(a) What is the mass of 5.00 cm³ of gold?
(b) What is the volume of 100.0 g of gold?

**(a) Mass from volume:**

> $5.00 \text{ cm}^3 \times \dfrac{19.3 \text{ g}}{1 \text{ cm}^3} = 96.5 \text{ g}$
>
> $\cancel{\text{cm}^3} \times \dfrac{\text{g}}{\cancel{\text{cm}^3}} = \text{g}$ ✓ → 96.5 g (3 sig figs)

**(b) Volume from mass — flip the density:**

> $100.0 \text{ g} \times \dfrac{1 \text{ cm}^3}{19.3 \text{ g}} = 5.181... \text{ cm}^3$
>
> $\cancel{\text{g}} \times \dfrac{\text{cm}^3}{\cancel{\text{g}}} = \text{cm}^3$ ✓ → 5.18 cm³ (3 sig figs, limited by 19.3)

**Answers:** $\boxed{\text{(a) } 96.5 \text{ g} \qquad \text{(b) } 5.18 \text{ cm}^3}$

---

### Example 7 — Squared/Cubed Unit Conversion

**Problem:** A floor is 15.0 m². Convert to cm².

> **The trap:** 1 m = 100 cm, so many students write:
>
> $\color{red}{\cancel{15.0 \text{ m}^2 \times \dfrac{100 \text{ cm}}{1 \text{ m}} = 1500 \text{ cm}^2}}$ ← **WRONG!**

**Why?** Because m² means m × m. You need to square the conversion:

> $\left(\dfrac{100 \text{ cm}}{1 \text{ m}}\right)^2 = \dfrac{100^2 \text{ cm}^2}{1^2 \text{ m}^2} = \dfrac{10,\!000 \text{ cm}^2}{1 \text{ m}^2}$

**Correct:**

> $15.0 \text{ m}^2 \times \dfrac{10,\!000 \text{ cm}^2}{1 \text{ m}^2} = 150,\!000 \text{ cm}^2 = 1.50 \times 10^5 \text{ cm}^2$

**Answer:** $\boxed{1.50 \times 10^5 \text{ cm}^2}$ (3 sig figs).

> The conversion squared is NOT 100 — it's 10,000. This is the most common unit conversion error in chemistry.

---

### Example 8 — Volume Units: cm³ ↔ mL ↔ L

**Problem:** A container holds 250 cm³. How many liters is this?

> **Key fact (memorize this):** $1 \text{ cm}^3 = 1 \text{ mL}$. Always. Exactly.

**Step 1:** cm³ → mL (same number).

> $250 \text{ cm}^3 = 250 \text{ mL}$

**Step 2:** mL → L.

> $250 \text{ mL} \times \dfrac{1 \text{ L}}{1000 \text{ mL}} = 0.250 \text{ L}$

**Answer:** $\boxed{0.250 \text{ L}}$ (3 sig figs).

---

## ⚠️ THE TRAP — Forgetting to Square/Cube the Conversion Factor

**The wrong way:**

> Convert 3.0 m³ to cm³.
>
> *Wrong work:* $3.0 \text{ m}^3 \times \dfrac{100 \text{ cm}}{1 \text{ m}} = \color{red}{300 \text{ cm}^3}$
>
> This is off by a factor of **1,000,000**.

**Why is this wrong?** m³ = m × m × m. If 1 m = 100 cm, then 1 m³ = (100 cm)³ = 1,000,000 cm³.

**The right way:**

> $3.0 \text{ m}^3 \times \left(\dfrac{100 \text{ cm}}{1 \text{ m}}\right)^3 = 3.0 \text{ m}^3 \times \dfrac{1,\!000,\!000 \text{ cm}^3}{1 \text{ m}^3} = 3.0 \times 10^6 \text{ cm}^3$

**Spot the difference:** Whenever the unit has an exponent (m², m³), the conversion factor gets the SAME exponent. 100² = 10,000. 100³ = 1,000,000.

---

## What We Just Did — The Dimensional Analysis Chain

### Step 1: Write the starting quantity with its unit. Identify the target unit.

> "I have ___ in (unit A). I want (unit B)."

### Step 2: Build a chain of conversion fractions.

> Each fraction puts the unit you **WANT** on top and the unit you're **CANCELING** on bottom.
>
> Multiply across. Cancel units at every step.
>
> $$\cancel{\text{unit A}} \times \frac{\text{unit B}}{\cancel{\text{unit A}}} \times \frac{\text{unit C}}{\cancel{\text{unit B}}} = \text{unit C}$$

### Step 3: When the only unit left is the target unit, multiply all top numbers, divide by all bottom numbers.

> Round to correct sig figs. **If the unit has an exponent, the conversion factor gets that same exponent.**

---

Copy this. This is the procedure behind every unit conversion you will ever do in chemistry.

---

## 💡 Pro Tips — Calculator Shortcuts & Mental Checks

**Tip 1 — The "want on top, have on bottom" rule.** Never guess which way the fraction goes. If you have kg and want g, write $\frac{\text{g}}{\text{kg}}$. The unit you're canceling always goes on bottom.

**Tip 2 — 1 cm³ = 1 mL. Always. Exactly.** This is the single most useful volume conversion in chemistry. A 500 cm³ container holds exactly 500 mL. Never convert — just swap the label.

**Tip 3 — Density flips both ways.** Need mass from volume? $m = \rho V$. Need volume from mass? $V = m/\rho$. The density fraction just flips. Don't memorize two formulas — just use dimensional analysis and let the units tell you which way it goes.

**Tip 4 — km/h → m/s shortcut.** Divide by 3.6. $90.0 \div 3.6 = 25.0$ m/s. Reverse: m/s → km/h, multiply by 3.6. This saves 10 seconds on every speed conversion.

**Tip 5 — Squared/cubed sanity check.** If you're converting cm² to m² and get a number bigger than what you started with, you forgot to square. 1 m² = 10,000 cm² — converting TO m² should give a MUCH smaller number. $15,000 \text{ cm}^2 = 1.5 \text{ m}^2$, not $150 \text{ m}^2$.

---

## Basic Drills (B1–B10)

> Goal: Automate the chain. Units must cancel cleanly every time.

**B1.** Convert 5.00 km to meters.

**B2.** Convert 450 mg to grams.

**B3.** Convert 2.50 hours to seconds. (1 h = 60 min, 1 min = 60 s — both exact)

**B4.** Convert 65.0 mi/h to km/h. (1 mi = 1.609 km)

**B5.** A bottle holds 2.00 L. Convert to mL, then to cm³.

**B6.** Convert 0.850 g/mL to kg/L.

**B7.** A gold ring has volume 0.450 cm³. Gold's density is 19.3 g/cm³. Find mass in grams, then in kilograms.

**B8.** A swimming pool holds 50.0 m³ of water. Convert to liters. (1 m³ = 1000 L)

**B9.** (Two-part) Part 1: Convert 100.0 yards to meters (1 yd = 0.9144 m). Part 2: Convert that same distance to centimeters.

**B10.** (Speed round — under 2 min) Convert $3.00 \times 10^8$ m/s (speed of light) to km/h. Use scientific notation.

---

## Advanced Drills (A1–A10)

> Goal: Multi-step, traps, exam time pressure.

**A1.** (Multi-step integration with Session 01) A car travels 425.0 km on 32.5 L of fuel. (a) Convert km to miles (1 km = 0.6214 mi). (b) Convert L to gallons (1 gal = 3.785 L). (c) Calculate fuel economy in miles per gallon with correct sig figs.

**A2.** (Multi-step integration) A recipe calls for 2.50 cups of flour. 1 cup = 236.6 mL. Flour density = 0.593 g/mL. Find the mass of flour in pounds (1 lb = 453.6 g).

**A3.** (Trap-laden — squared conversion) A square plot of land is 250. m on each side. (a) Calculate area in m². (b) Convert to km². (c) A student does: $250 \times 250 = 62,500 \text{ m}^2$, then $62,500 \times (1/1000) = 62.5 \text{ km}^2$. What mistake did they make? Show the correct answer.

**A4.** (Reverse engineering) A student converts 45.0 m/s to km/h by writing: $45.0 \times (1 \text{ km}/1000 \text{ m}) \times (3600 \text{ s}/1 \text{ h}) = 162 \text{ km/h}$. Is this correct? If yes, explain why the 3600 went on top. If no, find the mistake.

**A5.** (Multi-step — English to metric to mass) A recipe calls for 3.00 cups of milk. Convert this to kilograms. Given: 1 cup = 236.6 mL, density of milk = 1.03 g/mL. (a) Show the complete dimensional analysis chain: cups $\to$ mL $\to$ g $\to$ kg. (b) What is the mass of the milk in kg with correct sig figs? (c) If the recipe uses 3.0 cups (2 sig figs), how does the answer change?

**A6.** (Cubed conversion trap) A fish tank is a cube with edge 2.00 m. (a) Calculate its volume in m³. (b) Convert the volume to cm³. (c) A student forgets to cube the conversion factor and writes: $8.00\text{ m}^3 \times (100\text{ cm}/1\text{ m}) = 800.\text{ cm}^3$. What did they do wrong? What is the correct answer in cm³ — and how many times larger is it than the wrong answer?

**A7.** (Table-based) A shipping manifest lists the following items:

| Item | Volume (cm³) | Density (g/cm³) |
|------|:---:|:---:|
| Steel bolt | 8.50 | 7.85 |
| Aluminum washer | 2.40 | 2.70 |
| Copper wire | 1.15 | 8.96 |

Calculate the total mass in kg. ($1 \text{ kg} = 1000 \text{ g}$)

**A8.** (Timed — under 3 min) A cylindrical tank has radius 1.50 m and height 4.00 m. Volume = $\pi r^2 h$. It is filled with a liquid of density 0.880 g/mL. Find the mass of the liquid in metric tons. (1 metric ton = 1000 kg. $1 \text{ m}^3 = 10^6 \text{ cm}^3 = 10^6 \text{ mL}$.)

**A9.** (Hardest variation) The "jer" is a made-up unit: $1 \text{ jer} = 3.50 \text{ meters}$. The "flerp" is another: $1 \text{ flerp} = 12.0 \text{ seconds}$. Convert $45.0 \text{ jer/flerp}$ to km/h. This tests whether you understand the structure of derived units.

**A10.** (Exam boss) A NASA contractor mixes up units. They calculate a satellite's mass as 150. kg and report it to a partner who assumes the number is in pounds (lb). The partner uses 150. lb in calculations. (1 kg = 2.205 lb). (a) What mass in kg did the partner actually use? (b) If the satellite needs at least 140. kg of fuel and the partner loads fuel based on their incorrect mass at a ratio of 0.200 kg fuel per 1 kg satellite mass, how much fuel (in kg) do they actually load? (c) Is it enough? Show all work in a clear chain.

---

## Now Read

You can now convert any unit to any other unit using dimensional analysis — at exam speed.

Read **Chapter 4** of *Everything You Need to Ace Chemistry in One Big Fat Notebook*.

The concepts — why unit cancellation works, how density bridges mass and volume, why squared conversions are the #1 trap — will lock into place. You've solved 20 problems harder than anything the book asks.

> **Note:** Chapter 4 is all about measurement and unit conversions. The book walks through metric prefixes, dimensional analysis, and temperature conversions — all of which you can now do at exam speed.

> Solutions: [solutions/02-solutions.md](../solutions/02-solutions.md)

---

## � Connecting the Dots — Session 02 → Future Sessions

Dimensional analysis is the **engine behind every stoichiometry calculation**:

- **Session 03** (Density): Density itself is a conversion factor between mass and volume.
- **Session 04** (The Mole): Molar mass is a conversion factor between grams and moles.
- **Session 05** (Stoichiometry): The mole ratio is a conversion factor between substances.
- **Session 06** (Limiting Reagent): Finding excess remaining is a dimensional analysis chain.
- **Session 07** (Molarity): Concentration (mol/L) is a conversion factor between volume and moles.
- **Session 08** (Titration): $M_a V_a = M_b V_b$ is dimensional analysis with an extra proton-counting step.

> **Every chemistry calculation is just a chain of conversion factors.** Master the chain now, and every future topic becomes a variation on the same theme.

---

## �📝 Key Terms — Quick Reference

| Term | What it means |
|------|---------------|
| **dimensional analysis** | the chain method — multiply by conversion fractions until units cancel |
| **conversion factor** | a fraction equal to 1 (e.g., $\frac{1000\text{ mL}}{1\text{ L}}$) |
| **derived unit** | unit made from base units: km/h, g/mL, g/cm³ |
| **metric prefixes** | k (10³), c (10⁻²), m (10⁻³), μ (10⁻⁶) |
| **density ($\rho$)** | $\rho = m/V$; bridge between mass and volume |
| **1 cm³ = 1 mL** | exactly — always, no exceptions |
| **squared/cubed conversion** | if the unit has an exponent, the conversion factor gets the same exponent: $(100)^2 = 10,\!000$ |
| **want/have rule** | unit you WANT on top, unit you HAVE on bottom |
| **exact numbers** | conversions like 1 min = 60 s have infinite sig figs — they never limit precision |
| **density flip** | $m = \rho V$ or $V = m/\rho$ — the fraction flips based on what you're solving for |
