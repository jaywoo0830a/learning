# Physics Session Writing Guidelines v4

> Phase 0 (Pre-Kleppner): "Experience firsthand that without the method of splitting and gathering through limits, you can never reach the exact value."
> v4 change: **Every session must include a "necessity of limits" corner.** Deprecate the terms "differentiation" and "integration"; instead, use "change in a blink" and "split and gather."

---

## 0. 🔥 Essential Element for Every Session — "What Happens Without Splitting and Gathering?"

> **This is the identity of this entire curriculum.** No session may exist without this principle.

### Mandatory Pattern: approximate → finer approximate → still wrong → only the limit is correct

**Every session must include the following 3 steps:**

```
① Try with algebra alone → you get a value, but it's wrong.
② Split into finer intervals and try again → the value changes. (More accurate, but still approximate.)
③ "What if we split infinitely finely?" → Only the limit (infinite splitting and gathering) reaches the exact value.
```

### Required Examples per Session Topic

| Session Topic | Attempting with Algebra Alone | Why It Doesn't Work | The True Value from Limits |
|:---|:---|:---|:---|
| Distance with changing speed | Cut into 1-second chunks, add $v \times 1$ | No matter how many subdivisions, never reaches the true value | $\int v\,dt$, an exact value |
| Work done by a changing force | Add $F \times \Delta x$ per interval | Spring force changes continuously, only approximating | $\int kx\,dx = \frac{1}{2}kx^2$ |
| Motion of a spring | Assume "average force gives constant acceleration" | In reality, force changes as position changes | $x=A\cos(\omega t)$, complete trajectory |
| Falling with drag | Assume constant deceleration | Drag depends on velocity, so constant deceleration is false | $v(t)=v_t(1-e^{-bt/m})$ |
| Velocity before/after collision | Track every instant with $F=ma$ | Contact time too short, force too irregular | $\int F\,dt = \Delta p$, answer without knowing force details |
| Moment of inertia of a continuum | Split into a few chunks, $\sum m_i r_i^2$ | Finite chunks always approximate; exact value needs infinite division | $I = \int r^2 dm$, exact value |

### What This Pattern Trains

- **The intuition that "what we need is limits, not more calculation"**
- **The attitude of accepting splitting-and-gathering as inevitable, not optional**
- **The experience of directly feeling the gap between approximation and the true answer**

---

## 1. Core Principle: Equations Are Merely Tools for Painting a Scene

```
[Concrete physical scene] → [Attempt with algebra, fail] → [Finer attempt, fail again] → [Resolve with limits] → [Extract meaning]
          15%                       20%                         15%                      30%                20%
```

- **Scene first**: "A mass is pulled on a spring and released" — this scene comes first.
- **Experience failure**: Let the body feel that algebra alone can never reach the exact value.
- **Resolve with limits**: Show how the method of infinite splitting and gathering completely solves the problem.
- **Extract meaning**: "What we just did" — explain in words, without equations.

---

## 2. Four Training Principles for Cultivating Physical Meaning

### 2-1. Translate Every Formula into a "Story Sentence"

| Formula | Physical Story |
|------|---------------|
| $\vec{F}=m\vec{a}$ | "The harder you push, the faster the motion changes. But the heavier you are, the less it changes for the same push." |
| $\int F\,dx = \frac{1}{2}mv_2^2 - \frac{1}{2}mv_1^2$ | "When you gather all the work done by a force through space, that is exactly the change in motion-energy." |
| $\vec{\tau} = d\vec{L}/dt$ | "The more you twist, the more the total amount of rotation changes. If you don't twist, the total rotation stays the same." |
| $m\ddot{x} + kx = 0$ | "The farther you are from the origin, the harder it tries to pull you back. So it goes back and forth." |

### 2-2. Verify Meaning Through Units

Attach units to every result and check what those units mean.
- $[v] = \text{m/s}$ → "How many meters the position changes per second"
- $[F] = \text{kg}\cdot\text{m/s}^2$ → "The ability to change a 1kg object's velocity by 1 m/s in 1 second"
- $[E] = \text{kg}\cdot\text{m}^2/\text{s}^2$ → "The total capacity of an object with mass to move through space"

### 2-3. Test Meaning Through Extreme Cases

- What happens as $v \to 0$?
- What happens as $m \to \infty$?
- What happens as $k \to 0$ (no spring)?

In extreme cases, the answer must agree with common sense.

### 2-4. Speak the Same Situation in Multiple Languages

Training to describe one physical situation from three perspectives: ① $F=ma$, ② Energy, ③ Momentum.

---

## 3. FBD (Free Body Diagram) Special Principles

### FBD is "Listening." Draw It Before Calculating.

1. **Isolate**: Leave only one object; erase everything else.
2. **Contact forces**: Arrows at every point of contact (normal force $\perp$ surface, tension along the string, friction $\parallel$ surface).
3. **Action-at-a-distance forces**: Gravity is always downward. Add electric/magnetic forces if needed.
4. **Coordinate axes**: Align one axis with the acceleration direction to simplify equations.
5. **Equations**: $\sum F_x = ma_x$, $\sum F_y = ma_y$.

**Solving without an FBD is traveling without a map.**

---

## 4. Session Structure (60~120 minutes each)

### 4-1. Session Building Blocks

```
[Scene]       Present a concrete physical situation                        —  5 min
[❌ Fail]      Algebraic approximation → finer → experience failure         — 10 min
[✅ Resolve]   Introduce the limit, split and gather infinitely for exact   — 20 min
[💡 Examples]  Example 5~10 — apply the same principle to varied situations — 25 min
[Meaning]     "What we just did" — explain without equations                —  5 min
[🔧 Basic]    Basic Drills 5 problems — direct concept, simple calculation  — 10 min
[🔥 Advanced] Advanced Drills 5 problems — application, reasoning, traps    — 15 min
[🧠 Intuition] Intuitional Drills 5 problems — physical insight, no routine — 10 min
[📖 Symbols]   Reading Physical Symbols — how to interpret notation          —  5 min
[Terms]       Summarize today's physical concepts                           —  5 min
```

### 4-2. Drill Categories

| Category | Count | Purpose | Answer Location |
|:---|:---:|:---|:---|
| 🔧 Basic | 5 | Verify concept. 1~2 lines of calculation. Numbers-only variations of Examples. | `solutions/XX-solutions.md` |
| 🔥 Advanced | 5 | Apply, prove, avoid traps. Composite concepts, twists, counterintuitive results. | `solutions/XX-solutions.md` |
| 🧠 Intuitional | 5 | Physical insight. "What happens if...?" Qualitative reasoning with quantitative answers. No routine computation. | `solutions/XX-solutions.md` |

**Critical rule:** Session files contain **only questions**, never answers. All solutions live in `solutions/` directory, one file per session (`01-solutions.md`, `02-solutions.md`, etc.). The session files reference solutions with `*(solutions in `solutions/XX-solutions.md`)*`.

### 4-3. Intuitional Drills Guidelines

Each set of 5 problems should include:
- **1~2 "what-if" problems**: change a parameter mid-scenario and ask what happens
- **1~2 "comparison" problems**: compare two scenarios without calculation
- **1 "extreme/limiting case" problem**: push a variable to zero or infinity
- **0~1 "cross-session" problem**: combine concepts from earlier sessions

Answers must still be concrete (a number, a ratio, "yes/no with reason"), not vague hand-waving.

### 4-4. Reading Physical Symbols Section

Every session must include a `📖 Reading Physical Symbols` table before the Glossary. Format:

| Symbol | How to Read It | Physical Meaning |
|:---|:---|:---|

- Maximum 6~8 rows
- Each row: symbol, pronunciation, what it *means* physically (not mathematically)
- Focus on symbols **introduced in this session**

### 4-5. Example Writing Rules (5~10 examples)

| Rule | Description |
|:---|:---|
| **Progressive difficulty** | First 2~3: nearly identical, only numbers changed. Middle 2~3: variations of the situation. Last 2~4: trap elements added. |
| **Concrete numbers** | Use real numbers (2kg, 100 N/m, 5 m/s) instead of abstract variables ($m, k, v_0$). Answers should come out clean. |
| **Include failure examples** | At least 2 Examples must reproduce "this is how you get it wrong with algebra alone." Contrast with the correct approach. |
| **Units in every example** | Always attach units to answers, with one line explaining what those units physically mean. |

### 4-3. Basic Drills Rules (5 problems)

> **Purpose:** Verify the concept has settled in. Calculations should take 1~2 lines.

- Repeat the session's core idea with **only the numbers changed**
- Standard: "If you understood this session, you'll finish these in 5 minutes"
- Store answer keys separately in the `solutions/` directory

**Format example (Session 10: Spring Simple Harmonic Motion):**
1. $k=200\text{ N/m}$, $m=2\text{ kg}$ → period $T$?
2. $k=50\text{ N/m}$, $m=0.5\text{ kg}$, $A=0.1\text{ m}$ → maximum speed?
3. $x(t)=0.05\cos(10t)$ → amplitude, angular frequency, period?
4. $k=100$, $m=1$, $x_0=0.2$, $v_0=0$ → expression for $x(t)$?
5. Double the mass → period multiplied by? (Answer without calculation)

### 4-4. Advanced Drills Rules (5 problems)

> **Purpose:** Apply the concept and train to avoid common pitfalls.

- **1~2 problems:** Slightly twist the situation (e.g., horizontal spring → vertical spring)
- **1~2 problems:** Composite concepts (e.g., spring + collision, circular motion + drag)
- **1 problem:** "Trap" problem — where intuition is likely wrong (e.g., "Double the amplitude → double the period?" → No)
- Store answer keys in `solutions/` directory **with full solution steps**

### 4-6. Session Writing Checklist

- [ ] Is there a process where algebra alone produces a **wrong** answer? (with concrete numbers)
- [ ] Did you show the value **changing** as intervals get finer?
- [ ] Is there a moment where "split infinitely" → the limit yields the **exact value**?
- [ ] Are there **5 to 10** Examples? (progressive difficulty)
- [ ] Are there **5** Basic Drills, **5** Advanced Drills, and **5** Intuitional Drills?
- [ ] Do all problems have concrete numbers and units?
- [ ] Is there a **📖 Reading Physical Symbols** section with 6~8 rows?
- [ ] Are **all answers** stored in `solutions/XX-solutions.md` (not in the session file)?
- [ ] Do session files reference solutions with `*(solutions in `solutions/XX-solutions.md`)*`?

