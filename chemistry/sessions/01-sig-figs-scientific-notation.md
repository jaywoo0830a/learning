# Session 01: Significant Figures & Scientific Notation

> **Topic:** Learning to speak the language of measurement precision.
> **Time:** 120 minutes
> **Big Fat Notebook:** Chapters 1–2

---

## Opening Attack

Try this:

> A student measures a cube's edge as **3.40 cm**. Another student measures the same cube's edge as **3.4 cm**. Both students calculate the volume (edge³). The first student gets **39.3 cm³**. The second student gets **39 cm³**.
>
> Both used the same cube. Both did the math correctly. Why are their answers different — and which one is right?

Stuck? Good. Let's figure out why.

---

## Worked Pattern

### Example 1 — Counting Significant Figures

How many significant figures are in each measurement?

| Measurement | Count | Why? |
|:-----------:|:-----:|------|
| 3.40 cm | **3** | Nonzero digits (3, 4) are always significant. The trailing zero after the decimal counts — it was measured. |
| 3.4 cm | **2** | Nonzero digits only. No trailing zero was recorded, so it wasn't measured. |
| 0.00450 g | **3** | Leading zeros (0.00) are placeholders — they don't count. The 4, 5, and trailing zero after decimal all count. |
| 2500 mL | **2** (ambiguous) | Without a decimal point, the trailing zeros might or might not be measured. In Honors Chemistry, treat this as 2 sig figs unless told otherwise. |
| 2500. mL | **4** | The decimal point says: "All four digits were measured." |
| $6.022 \times 10^{23}$ | **4** | Only the coefficient (6.022) determines sig figs. The exponent is exact. |

---

### Example 2 — Multiplying and Dividing: Count Sig Figs

**Problem:** A rectangle measures 12.3 cm by 5.6 cm. Calculate its area.

```
Step 1: Multiply the numbers.
  12.3 × 5.6 = 68.88

Step 2: Count sig figs in each measurement.
  12.3 cm → 3 sig figs
  5.6 cm  → 2 sig figs

Step 3: The answer gets the smaller count: 2 sig figs.
  68.88 → rounds to 69 cm² (2 sig figs)
```

**Answer: 69 cm²** (limited by 5.6 cm, which has only 2 sig figs).

---

### Example 3 — Multiplying and Dividing: Another One

**Problem:** Density = mass ÷ volume. Mass = 24.50 g. Volume = 8.0 mL. Calculate density.

```
Step 1: Divide.
  24.50 ÷ 8.0 = 3.0625

Step 2: Count sig figs.
  24.50 g → 4 sig figs
  8.0 mL  → 2 sig figs ← limiting

Step 3: Round to 2 sig figs.
  3.0625 → 3.1 g/mL
```

**Answer: 3.1 g/mL** (2 sig figs).

---

### Example 4 — Adding and Subtracting: Decimal Places Rule

**Problem:** Add 12.34 g + 0.5 g + 3.210 g.

```
Step 1: Line up the decimal points.
  12.34
   0.5
+  3.210
--------
  16.050

Step 2: Look at decimal places (digits after the decimal point).
  12.34  → 2 decimal places
   0.5   → 1 decimal place  ← limiting
   3.210 → 3 decimal places

Step 3: Round the answer to 1 decimal place.
  16.050 → 16.1 g
```

**Answer: 16.1 g** (1 decimal place, limited by 0.5).

Notice: **Adding/subtracting uses decimal places, NOT sig figs.** This is different from multiplying/dividing.

---

### Example 5 — Adding and Subtracting: Another One

**Problem:** Subtract 25.0 mL − 3.25 mL.

```
Step 1: Subtract.
  25.0 − 3.25 = 21.75

Step 2: Count decimal places.
  25.0  → 1 decimal place  ← limiting
  3.25  → 2 decimal places

Step 3: Round to 1 decimal place.
  21.75 → 21.8 mL
```

**Answer: 21.8 mL** (1 decimal place).

---

### Example 6 — Scientific Notation

**Problem:** Write 0.000340 in scientific notation with correct sig figs.

```
Step 1: Move the decimal point until exactly one nonzero digit is to the left.
  0.000340 → move decimal 4 places right → 3.40

Step 2: Write as: coefficient × 10^(exponent).
  Moving right → negative exponent.
  3.40 × 10⁻⁴

Step 3: Check: the coefficient (3.40) shows the sig figs: 3.
```

**Answer: 3.40 × 10⁻⁴** (3 sig figs).

---

### Example 7 — Scientific Notation on Your Calculator

**Entering $6.022 \times 10^{23}$:**

- Do NOT type: `6.022 × 10 ^ 23` (this is slow and error-prone).
- Use the **EE** or **EXP** key: `6.022 EE 23`
- The display shows: `6.022E23` or `6.022 × 10²³`
- This means $6.022 \times 10^{23}$ — the "E" stands for "×10^".

**Practice:** Enter $1.67 \times 10^{-27}$ → press `1.67 EE (-) 27` → displays `1.67E-27`.

---

## ⚠️ THE TRAP — Rounding Too Early

**The wrong way:**

> A block has mass 15.8 g and volume 6.0 mL. Calculate density.
>
> *Wrong work:* 15.8 ÷ 6.0 = 2.63333... → "I'll round now to 2.6" → Then later: 2.6 × (some other number)...
>
> This answer (2.6) already lost precision. Every subsequent calculation using it will be slightly wrong.

**Why is this wrong?** Rounding before the final answer discards information. The calculator holds 10+ digits — use ALL of them until the very end.

**The right way:**

```
15.8 ÷ 6.0 = 2.63333... (keep all digits on the calculator)
× 3.00 (next step) = 7.90 (now round to 2 sig figs) → 7.9 g
```

**Spot the difference:** Intermediate values stay unrounded. Only the final answer gets rounded.

---

## What We Just Did — The Sig Fig Procedure

```
WHAT WE JUST DID — The Significant Figure Procedure

Step 1: Count the sig figs (or decimal places) in each measured number.
  → ×/÷: count sig figs. +/−: count decimal places.

Step 2: Do the math on your calculator. Keep ALL digits — do not round yet.

Step 3: Round the final answer to match the LEAST precise measurement.
  → ×/÷: smallest number of sig figs.
  → +/−: smallest number of decimal places.
```

Copy this. You will use it for every problem in the drills.

---

## Basic Drills (B1–B10)

> Goal: Automate sig fig counting and rounding. Finish all 10 smoothly.

**B1.** How many sig figs? (a) 0.0570 (b) 400 (c) 400.0 (d) $9.10 \times 10^3$

**B2.** Multiply: $6.42 \times 3.1$. Give the answer with correct sig figs.

**B3.** Divide: $45.00 \div 6.0$. Give the answer with correct sig figs.

**B4.** Add: $2.3 + 0.56 + 1.449$. Give the answer with correct decimal places.

**B5.** Subtract: $15.0 - 3.27$. Give the answer with correct decimal places.

**B6.** Write in scientific notation with correct sig figs: (a) 0.0000890 (b) 23,400 (3 sig figs)

**B7.** A student measures mass as 5.60 g and volume as 2.0 mL. Calculate density with correct sig figs.

**B8.** A rectangle is 14.55 cm by 2.0 cm. Calculate the perimeter (add all four sides) and area. Which rule applies to each?

**B9.** (Two-part) Part 1: A block has mass 125.0 g and volume 50.0 mL. Calculate density. Part 2: Multiply that density by 2.0 mL to find mass of a smaller piece. Use correct sig figs at each final answer.

**B10.** (Speed round) Count sig figs in under 1 minute: (a) 0.03040 (b) 1.200 (c) 5000 (d) 5.000 × 10³ (e) 0.001 (f) 2.50 × 10⁻²

---

## Advanced Drills (A1–A10)

> Goal: Exam-level. Time pressure. Traps. Multi-step integration.

**A1.** A cylinder has radius 1.25 cm (measured) and height 10.0 cm (measured). Volume of a cylinder = $\pi r^2 h$. $\pi$ is exact (infinite sig figs). Calculate volume with correct sig figs.

**A2.** A lab group measures three masses of the same sample: 4.52 g, 4.55 g, 4.48 g. The true mass is 4.50 g. (a) Calculate the average. (b) Are the measurements precise? (c) Are they accurate? (d) If a fourth measurement was 5.10 g, how would precision and accuracy change?

**A3.** (Trap-laden) A student calculates: $(12.3 + 0.45) \times 2.0$. They add first: $12.3 + 0.45 = 12.75$, then multiply: $12.75 \times 2.0 = 25.5$. Then round to 1 decimal place (from the addition rule) → 25.5. Is this correct? If not, where did they go wrong?

**A4.** (Reverse engineering) A student divides 15.0 by 3.00 and gets 5.000. Their partner says it should be 5.00. Who is right? Show the correct calculation and explain the mistake.

**A5.** (Constructive) Write an exam problem where the answer has exactly 3 sig figs and requires a multiplication followed by an addition. Solve it.

**A6.** (Constructive) Write a problem where a student would get the wrong answer by using the ×/÷ rule when they should use the +/− rule. Show both the wrong and right solutions.

**A7.** (Data table) Three students each measure the mass of a 10.00 g standard weight five times:

| | Trial 1 | Trial 2 | Trial 3 | Trial 4 | Trial 5 |
|---|:---:|:---:|:---:|:---:|:---:|
| **Student A** | 9.98 | 10.01 | 9.99 | 10.00 | 10.02 |
| **Student B** | 10.45 | 10.44 | 10.46 | 10.45 | 10.45 |
| **Student C** | 9.8 | 10.3 | 10.1 | 9.6 | 10.4 |

Which student is precise but not accurate? Which is accurate but not precise? Which is both? Which is neither?

**A8.** (Timed — under 3 min) Calculate with correct sig figs: $\frac{(14.25 - 3.0) \times 2.500}{(6.0 + 1.11)}$. Show each step's intermediate value BEFORE rounding.

**A9.** (Hardest variation) A cube's measured edge length is 2.0 cm. (a) Calculate volume. (b) Now the same cube's edge is remeasured as 2.00 cm. Calculate volume. (c) By what percent do the two volume answers differ? (d) Why does a small change in measurement precision cause a larger change in the calculated volume?

**A10.** (Exam boss) An irregular solid is placed in a graduated cylinder. The water level rises from 25.0 mL to 28.5 mL. The solid's mass is 15.74 g. (a) Calculate density with correct sig figs. (b) The solid is actually a cube — what is its edge length? (c) If the edge was measured with a ruler and found to be 1.58 cm, calculate density from the ruler measurement. (d) Which density — from water displacement or from ruler — is more precise? More accurate? Justify with sig figs.

---

## Now Read

You can now do every calculation involving significant figures and scientific notation — at exam speed.

Read **Chapters 1–2** of *Everything You Need to Ace Chemistry in One Big Fat Notebook*.

Read it. The concepts — measurement, precision, accuracy, scientific method — will make sense immediately. Your hands already know the math. You've solved 20 problems harder than anything the book asks.

> Solutions: [solutions/01-solutions.md](../solutions/01-solutions.md)
