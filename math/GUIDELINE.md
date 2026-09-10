# Mathematics Textbook Authoring Guideline v10

> Every session follows the rules in this document. v9: unified example-first structure, contradictions removed; scope and exemptions for symbols and sentence length clarified; synthesis sessions defined as assessment; pedagogy additions. v10: drill-tier guidelines (Basic / Intermediate / Advanced) added, modeled on the drill banks in `sessions/`.

---

## 1. Core Principle: Example → Method Extraction → Drills → Vocabulary

```
[many concrete examples] → [extract the method ("what we just did")] → [drills] → [vocabulary (last)]
             60%                               15%                             20%                5%
```

- **Examples**: never state an abstract rule first. Show 4–8 concrete cases first.
- **Method extraction**: in the "What we just did" corner, pull out the common pattern across the examples.
- **Vocabulary and symbols appear only at the very end** of a session. Until then, plain language only.
- Session titles are method-descriptive, not concept-names. Example: "Judging whether a sentence is true or false using a table."
- **Upper-phase note (v9):** in Phases 6–10, "examples" shift from *computation cases* (a concrete number to plug in) to *structural cases* (a concrete group, ring, space, or measure). The 60% share stays; the kind of example changes.

---

## 2. Principles of Linguistic Clarity

### 2-1. Sentence structure: action → object → result

Every procedure sentence keeps this order. Conditions come before the action.

```
[condition, if any, first] → [what] → [do what] → [then what results]
```

| Bad | Good |
|------|------|
| "If the remainder of $a$ divided by $b$ is 0, it is a factor." | "Divide $a$ by $b$. If the remainder is 0, then $b$ is a factor." |
| "An extremum may occur where $f'(x)=0$." | "Find the points where $f'(x)=0$. If the sign of $f'$ changes there, it is an extremum." |
| "Diagonalize the matrix." | "Line up the eigenvectors as columns to form $P$. Compute $P^{-1}AP$. Only the eigenvalues remain on the diagonal." |

Key rule: **one sentence = one action**. Split two actions into two sentences.

### 2-2. Location-based pointing: "the thing that is where"

Point at a visual or spatial location instead of an abstract variable name.

| Bad | Good |
|------|------|
| "$a_n$ = the $n$-th term of the sequence" | "the number written in the $n$-th slot of the sequence" |
| "$A_{ij}$ = the $(i,j)$ entry of the matrix" | "the number written in the $i$-th horizontal row and $j$-th vertical column" |
| "$f^{-1}$ = the inverse function" | "the function that overlaps when folded over the line $y=x$" |

Once a location is defined, use **the same wording only** for the rest of that session. Do not switch to "row" or "column" mid-session.

### 2-3. Vocabulary consistency: one action = one word

| Action | Use only this word | Not this |
|:---:|:---:|------|
| + | "add" | sum, plus |
| − | "subtract" | minus, take the difference |
| × | "multiply" | times |
| ÷ | "divide" | divide out |
| substitute | "plug in" | substitute, replace |
| differentiate | "differentiate" | take the derivative |
| integrate | "integrate" | find the antiderivative |
| move | "move" | transpose, carry over |
| eliminate | "erase" | cancel, remove |

Within a single session, one action uses one word only.

### 2-4. Conditionals: at the front of the sentence

"If ~" goes at the very front. Do not tuck it in the middle.

| Bad | Good |
|------|------|
| "Cancel, provided the denominator is nonzero." | "First check whether the denominator is 0. If it is not 0, then cancel." |

### 2-5. No negative imperatives — say "do" instead of "don't"

| Bad | Good |
|------|------|
| "Do not divide by zero." | "If the denominator is 0, leave it as is." |
| "Do not change the subscript." | "Leave the subscript as is. Change only the leading coefficient." |

### 2-6. Give numbers emotion

Mark clean results with language: "the remainder is exactly 0.", "it cancels in one shot.", "it comes out a clean integer."

---

## 3. Principles from Neuroscience & Linguistics

### 3-1. Chunking into threes

Working memory holds only 3–5 items (Miller, Sweller). **Every procedure has 3 steps.** If there are 4+, nest as top-level 3 + sub-level 3.

### 3-2. Prediction-error imprinting — the "Common Mistake" corner

The brain reacts most strongly to information that differs from prediction (Friston).

1. **First show the wrong way** — "Many people do this: (the wrong way)."
2. **State the reason in one line** — "But then ___ fails."
3. **Then show the right way.**

**Standard template (v9):** the wrong way is shown **without negative imperatives**, as a *consequence description* rather than a *prohibition*.

| Prohibited form (§2-5) | Consequence form (use this) |
|------|------|
| "Do not multiply the two numerators like this." | "Many people multiply the two numerators directly. Then the denominator is wrong, so the result does not match." |

In other words: describe what *happens* when the mistake is made (a result that fails), never what *not to do*. This keeps §2-5 and §3-2 compatible.

### 3-3. Motor language — "let the hand remember"

Embodied-cognition research: action words activate motor cortex and strengthen memory.

| Abstract verb | → Motor verb |
|------|------|
| transpose | **move** to the right |
| substitute | **push into** that spot |
| eliminate | **erase** |
| factor | **tear apart** |
| expand | **spread out** |
| cancel | **fold** |
| simplify | **gather** |
| multiply matrices | make a horizontal row **meet** a vertical column |

### 3-4. Generation effect — constructive problems

Memory strengthens 2–3× when the learner generates the information (Slamecka & Graf). At least 2 drill problems are **constructive**, not template-application (§3-4).

| Template application | Constructive |
|------|------|
| "Compute $2^3 \times 2^4$." | "Make three pairs of exponents whose product is $2^7$." |
| "Differentiate $f(x)=x^2$." | "Write three functions that differentiate to $2x$, and find what they share." |

### 3-5. Processing fluency

- Every procedure sentence keeps the same rhythm: "___ the ___. Then ___ comes out."
- Do not vary sentence structure within a session.
- Sentence length: 20 characters or fewer. If longer, break it.
- **Formula exemption (v9):** a procedural sentence that *contains a formula* is exempt from the 20-character limit. Keep the higher rule of one-action-per-sentence (§2-1) regardless.

### 3-6. Primacy & recency

- Put the most important step **first** in the procedure list.
- Imprint the core twice with the end-of-session "Today's Procedure" card.

### 3-7. Avoiding the curse of knowledge

- Ban "obviously", "easily", "trivially".
- Introduce variables and symbols by location first.
- Never skip an intermediate step (5→7 is forbidden; write 5→6→7).

---

## 4. Rules for Symbol Usage

**Every mathematical symbol first appears only in the Vocabulary Summary.** Until then, plain language only.

| Symbol | Before the summary (body) | Revealed in the summary |
|:----:|------|:---:|
| $\neg$ | "not" | negation |
| $\land$ | "and" | conjunction |
| $\lor$ | "or" | disjunction |
| $\to$ | "implies" | implication |
| $\forall$ | "all" | universal quantifier |
| $\exists$ | "some" | existential quantifier |
| variables $x,y$ | start concrete: 2, 3, 5 | generalize after the summary |
| T, F | "correct", "wrong" | true, false |

**Scope (v9):** this rule applies to **session bodies**. The curriculum overview (`TOPICS.md`) is a summary document for instructors and may use symbols freely.

---

## 5. Session Structure

| Section | Share | Content |
|:----:|:----:|------|
| Examples | 60% | 4–8 concrete cases. No abstract rules mentioned. |
| Method extraction | 15% | "What we just did" — distill the common pattern into 3 steps. |
| Common mistake | included | wrong way → reason → right way (§3-2) |
| Drills | 20% | Three tiers (§7, §12). At least 2 constructive (§3-4). |
| Vocabulary summary | 5% | "You already learned the method. Now we name it." |

---

## 6. Separating Solutions

Solutions go in a separate file `solutions/0X-solutions.md`. The session file carries only a link:

```markdown
> Solutions: [solution set](solutions/01-solutions.md#basic-drill)
```

---

## 7. Drill Placement

Sessions train the procedure in **drills** rather than a separate exercise list (§12). For each skill, the drill items climb this order:

| Tier | What the learner decides |
|:---:|------|
| Basic | exactly the procedure from the examples — same rule, one clean move |
| Intermediate | which sub-step, in what order — 2–3 rules chained |
| Advanced | the "why": explain, verify, design |

At least one **constructive** item per tier and at least two Advanced problems that compute-then-explain (§3-4, §12-4).

---

## 8. Vocabulary Summary

At the very end of a session. The standard opening is required.

```markdown
## Vocabulary Summary

So far we have used only (plain words). **You have already learned the method.**
Now we introduce the names and symbols used in mathematics.

| The words we used | Mathematical term | Symbol |
|:------------:|:--------:|:---:|
```

---

## 9. Procedure Summary Card

```markdown
## Today's Procedure

```
Step 1: ...
Step 2: ...
Step 3: ...
```
```

3–4 steps. It appears after the vocabulary summary, so symbols may be mixed in.

---

## 10. Synthesis Sessions (v9)

Every phase ends in a **synthesis session**. Unlike a tool session, it is an *assessment and integration* milestone with a fixed role and time.

| Phase | Synthesis session | Role | Time |
|:---:|------|------|:---:|
| 1 | 07 | formative milestone — mixed proofs | 60m |
| 2 | 21 | mixed-technique problems (decide which tool) | 60m |
| 3–9 | (per phase) | chain the phase's tools into one narrative + mixed problems | 60–90m |
| 10 | 111 | capstone — full dependency graph | 90m |

A synthesis session always contains:
1. A **tool-chain summary**: how the phase's tools connect into one chain.
2. **Mixed problems** that force the learner to choose among tools.
3. A **constructive task**: build or extend something, not just apply.

Phase 1's synthesis doubles as the **formative diagnostic** that gates entry into Phase 2.

---

## 11. Learning Objectives & Feedback (v9)

For credit-bearing operation, every session states a **behavioral objective** in addition to its method procedure.

```markdown
> **Objective:** Given [condition], the learner can [observable action].
> Example: "Given a separable ODE, the learner can write the separated integrals and solve them."
```

Feedback loop: each "Common Mistake" corner links to a corrective explanation in the solution set, so that a wrong answer always leads to a readable correction — not just a right answer.

Prerequisite diagnostic: before Phase 2, measure algebraic manipulation with a short placement set (§10).

## 12. Drill Design: Basic → Intermediate → Advanced (v10)

Every session ends with a **drill bank** — the session's working layer. Drills exist to push the same procedure from *slow and careful* to *fast and automatic*, then from *automatic* to *transferable*. Modeled on the drill banks in `sessions/` (e.g. `sessions/phase1/01-judging-truth-of-sentences.md`, `sessions/phase2/16A-integration-fundamentals.md`, `sessions/phase2/9A1-function-fundamentals.md`).

### 12-1. The three-tier ladder — one skill at three cognitive depths

| Tier | Cognitive goal | The learner's question | Working-memory load | Typical count |
|:---:|------|------|:---:|:---:|
| **Basic** | Fluency (automatization) | "Which rule, one clean time?" | lowest — one rule, no choice | 8–10 items |
| **Intermediate** | Selection + chaining | "Which sub-step now, in what order?" | medium — 2–3 rules chained, some choice | 6–8 items |
| **Advanced** | Reasoning + transfer + generation | "Why does it work, what if, prove it" | highest — explain, verify, design | 5–10 items |

Rationale: working memory holds only 3–5 items (§3-1). If a rule is not yet automatic, it consumes that scarce capacity and the learner cannot see the structure above it. **Automatize in Basic, so that Intermediate and Advanced spend their attention on *choice* and *reason*, not on recall.** The ladder is a three-step lift of the single drill tier: one tier drills *how*, the next drills *which*, the last drills *why*.

Three rules govern the ladder:

1. **Each tier changes only ONE thing.** Basic changes the number, keeps the rule. Intermediate changes the rule-mix, keeps the size. Advanced changes the task itself (explain / prove / design), keeps the topic.
2. **No tier announces an abstract rule first.** Every drill is concrete (§1, §2-4). The tier's caption line states the goal, not the formula.
3. **Every drill set links to its solution anchor** (§6): `> Solutions: [Solutions](solutions/0X-solutions.md#basic-drill)`. A learner who errs must land on a readable correction, never just on a right answer (§11).

The `.1 / .2 / .3` sub-problem scaffolding seen in `16A` is allowed at every tier, but its weight shrinks as the tier rises: **Basic and Intermediate may hint behind folds; Advanced rests the hint in a check step** (see 12-4).

### 12-2. Basic Drills — fluency and automatization

**Purpose.** Make the *single* procedure of this session effortless, so the hand remembers before the head has to think (§3-3 motor memory). Repeat one rule until it needs no attention.

**Format — blocked, same stem, one variable at a time (D1…D10).** Keep the stem identical and change only the operand or the size:

- `sessions/phase1/01` D1–D10: "Build the table for $A \land B$. / … for $A \lor B$. / … for $A \to B$." — only the *rule* differs; every row is built the same way.
- `sessions/phase2/14C-higher-derivatives.md` D1–D4: "Find $f''(x)$ for …" — a new function each time, the same two differentiating actions.

**Authoring rules**

| # | Rule | Example (good) |
|:---:|------|------|
| 1 | One rule type per item; the item names a concrete function / number | "Find $\int x^5\,dx$" — not "integrate any monomial" |
| 2 | Keep the same stem wording across all items (§2-2) | restate "$f''(x)$ for $f(x)=…$" identically |
| 3 | Clean results — the number "comes out clean" (§2-6) | designs whose answers are integers or neat powers |
| 4 | Scaffold, if needed, as nested sub-hints (`.1` then `.2`) | `16A-B1`: rule hint → compute |
| 5 | End with a "what kind is it?" item that names the concept | `01` D8–D10: tautology, contradiction, involution |

**Time target.** The captioned goal is speed with zero hesitation. Give a per-item budget (e.g. "each under 30 seconds") so fluency is measured, not just correctness.

**Pedagogy note.** These are *retrieval events*, not new information — each lookup is trivial but it still produces the testing effect. Keep them fast, numerous, and easily re-issued as spaced retests (12-5), never struggles.

### 12-3. Intermediate Drills — interleaving, selection, and chaining

**Purpose.** Stop the learner from knowing *which* rule was just taught. Intermediate chains 2–3 sub-steps and forces a *decision*: "which sub-rule goes first, and in what order?" This is interleaved practice (Rohrer & Taylor): mixing rules from this and nearby sessions lifts long-term retention over blocked drill.

**Format — pure computation, sub-steps cued in order, no hints free.** This is exactly the `Calculation Drills` bank in `sessions/phase2/16A-integration-fundamentals.md` (C1–C5); its caption is *"Pure computation — solve each sub-problem in order, then the full problem. No hints."* Each item is split into `.1 → .2` (→ `.3`) so the learner is told the *order* of actions without being told the *results*.

Concrete worked examples (16A C1–C3):

- **C1** $\int \frac{(x^2+1)^3}{x^4}\,dx$ → C1.1 "Expand $(x^2+1)^3$ and split into a sum of powers." → C1.2 "Integrate each term."
- **C2** $\int (e^x + e^{-x})^2\,dx$ → C2.1 "Expand the square." → C2.2 "Integrate each term."
- **C3** $\int \frac{\ln(x\sqrt{x})}{x}\,dx$ → C3.1 "Simplify $\ln(x\sqrt{x})$ with log laws." → C3.2 "Substitute $u=\ln x$." → C3.3 "Integrate."

Each chain is a **small method** (2–3 moves total). Chaining more than 3 moves violates §3-1 — nest.

**Binding rules (4).**

1. **Chain exactly 2–3 licensed sub-steps** — every move comes from the session's procedure or a previously licensed one.
2. **Interleave:** vary which sub-rule appears first so the learner cannot predict the tool (`C1` expand, `C2` expand the square, `C3` log-law then substitution — three different first moves).
3. **One trap per bank, placed mid-way** — bait a common error with a condition-first tweak (§2-4, §3-2). The Item's misordering must make the error visible.
4. **The `.1` hints are procedural cues, not answers** — they name the action ("expand", "simplify"), never the result.

**Selection quality bar.** For each Intermediate item, the solution set must answer three things: *(a) which sub-rule drives the move, (b) why this order, (c) what fails if the order is swapped.* That three-part note is what §2-1 and §3-2 make printable.

### 12-4. Advanced Drills — reasoning, transfer, and generation

**Purpose.** Engineering the *generation effect* (§3-4) and self-explanation (Chi) at the highest tier: the learner must not only produce a result but *justify, verify, compare, or design* it. This is where the deepest encoding happens.

**The six Advanced tasks (drawn from the session banks).**

| Task | What the learner does | Session precedent |
|:---:|------|------|
| **Compute-then-explain** | Solve, verify by a second route, then say *why* a term/factor is needed | `16A` A1–A4: "compute, verify by differentiating, explain where $\frac13$ comes from" |
| **Compare-and-contrast** | Two similar-looking problems; explain *why* the answers differ | `16A` A2: "why arctan and not logarithm" |
| **Prove / derive** | Derive a given formula from the licensed procedure | `14C` A1: "prove the Leibniz rule for $n=2$" |
| **Pattern-spot + generalize** | Compute first few cases, infer the closed form | `14C` A3: $f^{(n)}(x)$ for $\frac{1}{1-x}$ |
| **Design / constructive** | Build a new object meeting a constraint list | `9A1` A10: "Design a piecewise function with 3 pieces, one jump, one hole …" |
| **Error forensics** | Given a wrong result, locate and repair the mistake | the §3-2 consequence form turned into an item |

**Every Advanced bank must include at least one *compute-then-explain* and one *constructive*** problem (the §3-4 constructive floor, now with an explaining component). Constructive items state a decided target ("exactly", "at most", "must") so the answer set has a goal — see `14C` A8's "for an odd function, under what conditions on $a,b,h,k$ is $g$ also odd?".

**Verification as a habit.** Advanced items close with a self-check action repeated until internal: differentiate to check an integral, plug back in to check a derivative, test the boundary rows of a table, $f(f^{-1}(x))=x$ for inverses. The answer set states the check explicitly, so the learner sees *how* to confirm, not just the number.

**Profile rule.** The wrong-way / reason / right-way of §3-2 stays in the *solution's* correction paragraph. In the problem stem, give only bare prompts ("compute", "verify", "explain") so the learner is not told the answer-to-be.

---

### 12-5. Placement, ordering, and spacing (v10)

**Where in the session.** Drills come **after "What we just did" and before "Today's Procedure"** (§5 → §9). Each tier is its own `##` heading: `## Basic Drills` → `## Intermediate Drills` → `## Advanced Drills`. Keep these tier headings exactly this way across the whole curriculum for every session.

**Order inside a tier.** List items easiest → hardest. *Most important step first* (§3-1, primacy) means the first item of each tier states the session's core procedure once more.

**Ladder the same problem across tiers.** Strongest drill design "recasts" the same underlying object at three depths — run it, then execute it, then explain it. Example (for substitution in $16A$):

- **Basic:** "Find $\int 3x^2(x^3+1)^4\,dx$" — the substitution is signaled. *(`16A-B5`)*
- **Intermediate:** "Find $\int x^2\sqrt{x^3+1}\,dx$" — choose $u$ yourself. *(`16A-A1` stem)*
- **Advanced:** "Find $\int x^2\sqrt{x^3+1}\,dx$, verify by differentiating, then explain where the $\frac13$ factor comes from." *(`16A-A1.1–A1.3`)*

**Spacing retest rule.** A Basic item may re-issue a previous session's Advanced item as a speeded lookup (spacing/retrieval, §3-7). Example: after `01` proves $A\to B\equiv\neg A \lor B$ in Advanced, a later session's Basic bank re-issues it as a speeded negated-table drill.

---

### 12-6. Feedback and error per tier

Different tiers produce different errors, so they need different corrections:

| Tier | Typical error | Correction target |
|:---:|------|------|
| **Basic** | wrong rule choice / sign slip | re-run the one detached step; fix the *rule*, not the arithmetic |
| **Intermediate** | wrong sub-step order | trace the *order* chain; show the later result that fails if the sub-step is swapped (consequence form, §3-2) |
| **Advanced** | check skipped, explanation excused | force the verify/explain step; give the model explanation to copy |

Every drill link resolves to the correction paragraph, never a bare "answer: …" (§11). A drill error is a detection event: it turns a mistake into prediction-error imprinting (§3-2).

---

> **Summary rule.** Ask one filter question — **"What exactly is being decided by the learner at this tier?"** — and code it: **Basic** decides the rule (blocked, one clean move); **Intermediate** decides the *move* / the order (interleaved, chained); **Advanced** decides the *why*, checked and rebuilt (generated). When you design a drill set, let that single question determine every item.

---

## 13. Checklist

### Language
- [ ] Every procedure sentence follows [action→object→result]? One action per sentence?
- [ ] The same concept is called the same word throughout the session?
- [ ] One action uses one word only? (§2-3)
- [ ] Conditionals at the front of the sentence?
- [ ] Affirmative instead of negative imperatives?
- [ ] No "obviously", "easily", "trivially"?
- [ ] No intermediate steps skipped?

### Neuroscience & linguistics
- [ ] Every procedure chunked into threes?
- [ ] "Common Mistake" follows wrong-way → reason → right-way, in consequence form (§3-2)?
- [ ] Abstract verbs replaced with motor verbs? (§3-3)
- [ ] At least 2 constructive drill problems?
- [ ] Sentences share one rhythm; 20 characters or fewer (formula exemption applied)?
- [ ] Most important step first in the list?

### Structure
- [ ] 4–8 examples? No abstract rule before the examples?
- [ ] "What we just did" corner extracts the pattern?
- [ ] Vocabulary summary last, with the standard opening?
- [ ] No mathematical symbols before the vocabulary summary?
- [ ] Drills in three tiers: Basic → Intermediate → Advanced (§7)?
- [ ] Difficulty order within each tier: same rule → chained → explain/design?
- [ ] Solutions in a separate file, every drill item linked?
- [ ] Session ends with a procedure summary card (3–4 steps)?
- [ ] Title is method-descriptive?
- [ ] No emoji?

### Credit-bearing (v9)
- [ ] Behavioral objective stated?
- [ ] Synthesis sessions defined with a tool-chain summary, mixed problems, and a constructive task?
- [ ] Common-mistake feedback links to a corrective explanation?

### Drills (v10)
- [ ] Three tier headings present: "Basic Drills", "Intermediate Drills", "Advanced Drills"?
- [ ] Basic: one rule, blocked, same stem, concrete, speed target set?
- [ ] Intermediate: each item chains 2–3 licensed sub-steps, interleaved, one mid-way trap?
- [ ] Advanced: at least one compute-then-explain and one constructive problem?
- [ ] Advanced verification step stated; §3-2 wrong/right kept in the solution only?
- [ ] Every tier links to its solution anchor (§6)?
- [ ] Same procedure re-cast across tiers (run → execute → explain) and spaced retests used?
