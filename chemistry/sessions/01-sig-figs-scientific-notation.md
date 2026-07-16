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

**Step 1:** Multiply the numbers.

> $12.3 \times 5.6 = 68.88$

**Step 2:** Count sig figs in each measurement.

> $12.3 \text{ cm}$ → 3 sig figs
>
> $5.6 \text{ cm}$ → 2 sig figs ← **limiting**

**Step 3:** The answer gets the smaller count: 2 sig figs.

> $68.88 \to 69 \text{ cm}^2$ (2 sig figs)

**Answer:** $\boxed{69 \text{ cm}^2}$ (limited by 5.6 cm, which has only 2 sig figs).

---

### Example 3 — Multiplying and Dividing: Another One

**Problem:** Density = mass ÷ volume. Mass = 24.50 g. Volume = 8.0 mL. Calculate density.

**Step 1:** Divide.

> $24.50 \div 8.0 = 3.0625$

**Step 2:** Count sig figs.

> $24.50 \text{ g}$ → 4 sig figs
>
> $8.0 \text{ mL}$ → 2 sig figs ← **limiting**

**Step 3:** Round to 2 sig figs.

> $3.0625 \to 3.1 \text{ g/mL}$

**Answer:** $\boxed{3.1 \text{ g/mL}}$ (2 sig figs).

---

### Example 4 — Adding and Subtracting: Decimal Places Rule

**Problem:** Add 12.34 g + 0.5 g + 3.210 g.

**Step 1:** Line up the decimal points and add.

> $12.34 + 0.5 + 3.210 = 16.050$

**Step 2:** Look at decimal places (digits after the decimal point).

> $12.34$ → 2 decimal places
>
> $0.5$ → 1 decimal place ← **limiting**
>
> $3.210$ → 3 decimal places

**Step 3:** Round the answer to 1 decimal place.

> $16.050 \to 16.1 \text{ g}$

**Answer:** $\boxed{16.1 \text{ g}}$ (1 decimal place, limited by 0.5).

> **Key distinction:** Adding/subtracting uses **decimal places**, NOT sig figs. Multiplying/dividing uses **sig figs**. These are two different rules — don't mix them up.

---

### Example 5 — Adding and Subtracting: Another One

**Problem:** Subtract 25.0 mL − 3.25 mL.

**Step 1:** Subtract.

> $25.0 - 3.25 = 21.75$

**Step 2:** Count decimal places.

> $25.0$ → 1 decimal place ← **limiting**
>
> $3.25$ → 2 decimal places

**Step 3:** Round to 1 decimal place.

> $21.75 \to 21.8 \text{ mL}$

**Answer:** $\boxed{21.8 \text{ mL}}$ (1 decimal place).

---

### Example 6 — Scientific Notation: Writing

**Problem:** Write 0.000340 in scientific notation with correct sig figs.

**Step 1:** Move the decimal point until exactly one nonzero digit is to the left.

> $0.000340 \;\to\;$ move decimal 4 places right $\;\to\; 3.40$

**Step 2:** Write as: coefficient × $10^{\text{exponent}}$.

> Moving right → negative exponent.
>
> $3.40 \times 10^{-4}$

**Step 3:** Check: the coefficient (3.40) shows the sig figs: **3**.

**Answer:** $\boxed{3.40 \times 10^{-4}}$ (3 sig figs).

---

### Example 7 — Scientific Notation on Your Calculator

**Entering $6.022 \times 10^{23}$:**

> Do NOT type: `6.022 × 10 ^ 23` (slow and error-prone).
>
> Use the **EE** or **EXP** key: `6.022 EE 23`
>
> The display shows: `6.022E23` or `6.022 × 10²³`
>
> This means $6.022 \times 10^{23}$ — the "E" stands for "×10^".

**Practice:** Enter $1.67 \times 10^{-27}$ → press `1.67 EE (-) 27` → displays `1.67E-27`.

---

## ⚠️ THE TRAP — Rounding Too Early

**The wrong way:**

> A block has mass 15.8 g and volume 6.0 mL. Calculate density.
>
> *Wrong work:* 15.8 ÷ 6.0 = 2.63333... → "I'll round now to 2.6" → Then later: 2.6 × (some other number)... $\color{red}{= \text{wrong final answer}}$

**Why is this wrong?** Rounding before the final answer discards information. The calculator holds 10+ digits — use ALL of them until the very end.

**The right way:**

> **Step 1:** 15.8 ÷ 6.0 = 2.63333... (keep all digits on the calculator)
>
> **Step 2:** × 3.00 (next step) = 7.90
>
> **Step 3:** Now round to 2 sig figs (from 6.0) → **7.9 g**

**Spot the difference:** Intermediate values stay unrounded. Only the final answer gets rounded.

---

## What We Just Did — The Sig Fig Procedure

### Step 1: Count the sig figs (or decimal places) in each measured number.

> **×/÷:** count **sig figs**.
>
> **+/−:** count **decimal places**.

### Step 2: Do the math on your calculator. Keep ALL digits — do not round yet.

> The calculator has 10+ digits of precision. Use all of them.

### Step 3: Round the final answer to match the LEAST precise measurement.

> **×/÷:** smallest number of **sig figs**.
>
> **+/−:** smallest number of **decimal places**.

---

Copy this. You will use it for every problem in the drills.

---

## 💡 Pro Tips — Calculator Shortcuts & Mental Checks

**Tip 1 — The Pacific-Atlantic rule.** If a decimal point is **Present**, start counting sig figs from the **Pacific** (left) side — skip leading zeros, then count everything. If the decimal is **Absent**, start from the **Atlantic** (right) side — skip trailing zeros, then count everything.

> Pacific (decimal Present): 0.00450 → skip 0.00, count 450 → 3 sig figs.
>
> Atlantic (decimal Absent): 2500 → skip 00 from right, count 25 → 2 sig figs.

**Tip 2 — ×/÷ sig fig shortcut.** Find the measurement with the fewest sig figs. That's it. Your answer gets that many. Don't overthink it. $12.3 \times 5.6$ → 5.6 has 2 sig figs → answer has 2 sig figs. Done in 2 seconds.

**Tip 3 — +/− decimal place shortcut.** Find the measurement with the fewest digits after the decimal. That's how many decimal places your answer gets. $12.34 + 0.5$ → 0.5 has 1 decimal place → answer gets 1 decimal place.

**Tip 4 — Scientific notation always has exactly one digit before the decimal.** $3450 = 3.450 \times 10^3$, not $34.50 \times 10^2$. The coefficient must satisfy $1 \leq a < 10$. This is the fastest way to check if you did it right.

**Tip 5 — EE key doubles your exam speed.** On a timed test, typing `6.022 EE 23` instead of `6.022 × 10 ^ 23` saves 3–5 seconds per calculation. Over 20 problems, that's a full minute saved. Use the EE key every time.

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

**B10.** (Speed round) Count sig figs in under 1 minute: (a) 0.03040 (b) 1.200 (c) 5000 (d) $5.000 \times 10^3$ (e) 0.001 (f) $2.50 \times 10^{-2}$

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

**A8.** (Timed — under 3 min) The speed of light is $2.998 \times 10^8$ m/s. Light takes 8.3 minutes to reach Earth from the Sun. Calculate the Earth-Sun distance in kilometers with correct sig figs. (Watch the units: minutes → seconds, meters → km.)

**A9.** (Hardest variation) A student measures the radius of a sphere as 2.0 cm. They calculate volume = $\frac{4}{3}\pi r^3$. The $\frac{4}{3}$ and $\pi$ are exact. (a) What is the volume with correct sig figs? (b) If they had measured the radius as 2.00 cm, how would the volume change? (c) Why does a small change in sig figs cause a bigger effect in volume?

**A10.** (Exam boss) A student determines density five times: 2.71, 2.65, 2.68, 2.73, 2.60 g/cm³. The accepted value for aluminum is 2.70 g/cm³. (a) Calculate average density with correct sig figs for each operation. (b) Calculate percent error: $|\text{avg} - \text{accepted}| / \text{accepted} \times 100\%$. (c) Are the measurements more precise or more accurate? (d) The student realizes the balance was tared with a 0.05 g error. Does this affect precision, accuracy, or both?

---

## Now Read

You can now count sig figs, round correctly after ×/÷ and +/−, write scientific notation, and distinguish precision from accuracy — at exam speed.

Read **Chapters 1–2** of *Everything You Need to Ace Chemistry in One Big Fat Notebook*.

The concepts — why measurements have uncertainty, how sig figs communicate that uncertainty, why precision ≠ accuracy — will lock into place. You've solved 20 problems harder than anything the book asks.

> Solutions: [solutions/01-solutions.md](../solutions/01-solutions.md)

---

## 📝 Key Terms — Quick Reference

| Term | What it means |
|------|---------------|
| **sig figs** | digits in a measurement that carry meaning about precision |
| **precision** | how close repeated measurements are to each other (reproducibility) |
| **accuracy** | how close a measurement is to the true value |
| **leading zero** | zero before the first nonzero digit (0.0045 → never significant) |
| **trailing zero** | zero after last nonzero; significant ONLY if decimal point present (3.40 vs 340) |
| **scientific notation** | $a \times 10^n$ where $1 \leq a < 10$; coefficient shows sig figs |
| **×/÷ rule** | answer gets the **fewest sig figs** among inputs |
| **+/− rule** | answer gets the **fewest decimal places** among inputs |
| **EE key** | calculator button for ×10^; use it instead of typing `× 10 ^` |
| **rounding** | done only at the **final answer** — never intermediate steps |
