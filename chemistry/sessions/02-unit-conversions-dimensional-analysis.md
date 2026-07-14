# Session 02: Unit Conversions & Dimensional Analysis

> **Topic:** Moving between units without getting lost. The chain method.
> **Time:** 150 minutes
> **Big Fat Notebook:** Chapters 1–2

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

```
Step 1: Find the conversion factor.
  1 L = 1000 mL

Step 2: Write as a fraction so the unwanted unit cancels.
  3500 mL × (1 L / 1000 mL) = ?

Step 3: Multiply. mL cancels, L remains.
  3500 × 1 L ÷ 1000 = 3.5 L
```

**Answer: 3.5 L** (2 sig figs, from 3500 — ambiguous, but 3.5 × 10³ would be clearer).

---

### Example 2 — Single-Step: Which Way Does the Fraction Go?

**Problem:** Convert 0.450 kg to grams.

```
The question: should I multiply by (1000 g / 1 kg) or (1 kg / 1000 g)?

Rule: Put the unit you WANT on top. Put the unit you HAVE on bottom.

I HAVE kg. I WANT g.
  → (1000 g / 1 kg)   ← g on top, kg on bottom. Correct.

  0.450 kg × (1000 g / 1 kg) = 450 g
                              kg cancels with kg.
```

**Answer: 450 g** (3 sig figs).

---

### Example 3 — Multi-Step Chain Conversion

**Problem:** Convert 12.5 gallons to milliliters.

```
Given: 1 gal = 3.785 L, 1 L = 1000 mL

Step 1: Plan the chain: gallons → liters → milliliters.

Step 2: Write each conversion so unwanted units cancel.
  12.5 gal × (3.785 L / 1 gal) × (1000 mL / 1 L)

Step 3: Cancel and multiply.
  gal cancels. L cancels. mL remains.
  12.5 × 3.785 × 1000 = 47,312.5 mL

Step 4: Sig figs. 12.5 has 3 sig figs. 3.785 has 4. 1000 mL/L is exact.
  → 47,300 mL → 4.73 × 10⁴ mL (3 sig figs)
```

**Answer: 4.73 × 10⁴ mL** (3 sig figs).

---

### Example 4 — Multi-Step with Mass from Density

**Problem:** Using the 12.5 gallons from Example 3 (which we found is $4.73 \times 10^4$ mL), find the mass in kilograms. Density = 0.720 g/mL.

```
Step 1: Use density as a conversion factor: (0.720 g / 1 mL).

Step 2: Chain: mL → g → kg.
  4.73 × 10⁴ mL × (0.720 g / 1 mL) × (1 kg / 1000 g)

Step 3: Cancel and multiply.
  mL cancels. g cancels. kg remains.
  4.73 × 10⁴ × 0.720 ÷ 1000 = 34.056 kg

Step 4: Sig figs. 0.720 has 3 sig figs. → 34.1 kg.
```

**Answer: 34.1 kg** (3 sig figs).

---

### Example 5 — Derived Unit Conversion: km/h → m/s

**Problem:** A car travels at 90.0 km/h. Convert to m/s.

```
Step 1: Plan: km/h → m/h → m/s.
  Two conversions needed: km → m, and h → s.

Step 2: Write the chain.
  90.0 km   1000 m     1 h
  ────── × ────── × ────────
    1 h      1 km     3600 s

Step 3: Cancel and multiply.
  km cancels. h cancels. m/s remains.
  90.0 × 1000 ÷ 3600 = 25.0 m/s
```

**Answer: 25.0 m/s** (3 sig figs).

Notice: The conversion 1 h = 3600 s is exact. So sig figs come from 90.0 (3 sig figs).

---

### Example 6 — Density as a Conversion Factor (Both Directions)

**Problem:** Gold has density 19.3 g/cm³.
(a) What is the mass of 5.00 cm³ of gold?
(b) What is the volume of 100.0 g of gold?

```
(a) Mass from volume:
  5.00 cm³ × (19.3 g / 1 cm³) = 96.5 g
  cm³ cancels. → 96.5 g (3 sig figs)

(b) Volume from mass — flip the density:
  100.0 g × (1 cm³ / 19.3 g) = 5.181... cm³
  g cancels. → 5.18 cm³ (3 sig figs, limited by 19.3)
```

**Answers: (a) 96.5 g, (b) 5.18 cm³**

---

### Example 7 — Squared/Cubed Unit Conversion

**Problem:** A floor is 15.0 m². Convert to cm².

```
The trap: 1 m = 100 cm, so many students write:
  ✗ 15.0 m² × (100 cm / 1 m) = 1500 cm²  ← WRONG!

Why? Because m² means m × m. You need to square the conversion:
  (100 cm / 1 m)² = (100² cm² / 1² m²) = 10,000 cm² / 1 m²

Correct:
  15.0 m² × (10,000 cm² / 1 m²) = 150,000 cm² = 1.50 × 10⁵ cm²
```

**Answer: 1.50 × 10⁵ cm²** (3 sig figs).

The conversion squared is NOT 100 — it's 10,000. This is the most common unit conversion error in chemistry.

---

### Example 8 — Volume Units: cm³ ↔ mL ↔ L

**Problem:** A container holds 250 cm³. How many liters is this?

```
Key fact (memorize this): 1 cm³ = 1 mL. Always. Exactly.

Step 1: cm³ → mL (same number).
  250 cm³ = 250 mL

Step 2: mL → L.
  250 mL × (1 L / 1000 mL) = 0.250 L
```

**Answer: 0.250 L** (3 sig figs).

---

## ⚠️ THE TRAP — Forgetting to Square/Cube the Conversion Factor

**The wrong way:**

> Convert 3.0 m³ to cm³.
>
> *Wrong work:* 3.0 m³ × (100 cm / 1 m) = 300 cm³
>
> This is off by a factor of 10,000.

**Why is this wrong?** m³ = m × m × m. If 1 m = 100 cm, then 1 m³ = (100 cm)³ = 1,000,000 cm³.

**The right way:**

```
3.0 m³ × (100 cm / 1 m)³
= 3.0 m³ × (1,000,000 cm³ / 1 m³)
= 3.0 × 10⁶ cm³
```

**Spot the difference:** Whenever the unit has an exponent (m², m³), the conversion factor gets the SAME exponent. 100² = 10,000. 100³ = 1,000,000.

---

## What We Just Did — The Dimensional Analysis Chain

```
WHAT WE JUST DID — The Dimensional Analysis Procedure

Step 1: Write the starting quantity with its unit. Identify the target unit.
  → "I have ___ in (unit A). I want (unit B)."

Step 2: Build a chain of conversion fractions. Each fraction puts the unit
  you WANT on top and the unit you're CANCELING on bottom.
  → Multiply across. Cancel units at every step.

Step 3: When the only unit left is the target unit, multiply all top numbers,
  divide by all bottom numbers. Round to correct sig figs.
```

Copy this. This is the procedure behind every unit conversion you will ever do in chemistry.

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

**B10.** (Speed round — under 2 min) Convert 3.00 × 10⁸ m/s (speed of light) to km/h. Use scientific notation.

---

## Advanced Drills (A1–A10)

> Goal: Multi-step, traps, exam time pressure.

**A1.** (Multi-step integration with Session 01) A car travels 425.0 km on 32.5 L of fuel. (a) Convert km to miles (1 km = 0.6214 mi). (b) Convert L to gallons (1 gal = 3.785 L). (c) Calculate fuel economy in miles per gallon with correct sig figs.

**A2.** (Multi-step integration) A recipe calls for 2.50 cups of flour. 1 cup = 236.6 mL. Flour density = 0.593 g/mL. Find the mass of flour in pounds (1 lb = 453.6 g).

**A3.** (Trap-laden — squared conversion) A square plot of land is 250. m on each side. (a) Calculate area in m². (b) Convert to km². (c) A student does: $250 \times 250 = 62,500 \text{ m}^2$, then $62,500 \times (1/1000) = 62.5 \text{ km}^2$. What mistake did they make? Show the correct answer.

**A4.** (Reverse engineering) A student converts 45.0 m/s to km/h by writing: $45.0 \times (1 \text{ km}/1000 \text{ m}) \times (3600 \text{ s}/1 \text{ h}) = 162 \text{ km/h}$. Is this correct? If yes, explain why the 3600 went on top. If no, find the mistake.

**A5.** (Constructive) Write an exam problem that requires exactly 3 conversion steps and ends with a mass in kilograms. Use at least one English→metric conversion. Solve it with full dimensional analysis.

**A6.** (Constructive) Write a problem where a student who forgets to cube the conversion factor gets an answer that is off by a factor of exactly 1,000,000. Solve both the wrong way and the right way.

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

Read **Chapters 1–2** of *Everything You Need to Ace Chemistry in One Big Fat Notebook*.

Read it. You already know how to set up conversion chains, cancel units, and handle squared/cubed conversions. The concepts — SI units, metric prefixes, measurement systems — will click instantly. You've solved 20 problems harder than anything the book asks.

> Solutions: [solutions/02-solutions.md](../solutions/02-solutions.md)
