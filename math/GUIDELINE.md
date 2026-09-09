# Mathematics Textbook Authoring Guideline v9

> Every session follows the rules in this document. v9: unified example-first structure, contradictions removed; scope and exemptions for symbols and sentence length clarified; synthesis sessions defined as assessment; pedagogy additions.

---

## 1. Core Principle: Example → Method Extraction → Practice → Vocabulary

```
[many concrete examples] → [extract the method ("what we just did")] → [practice] → [vocabulary (last)]
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

Memory strengthens 2–3× when the learner generates the information (Slamecka & Graf). At least 2 practice problems are **constructive**, not template-application.

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
| Practice | 20% | 5–6 problems. Last one labeled "Real-world". At least 2 constructive (§3-4) |
| Vocabulary summary | 5% | "You already learned the method. Now we name it." |

---

## 6. Separating Solutions

Solutions go in a separate file `solutions/0X-solutions.md`. The session file carries only a link:

```markdown
> Solutions: [solution set](solutions/01-solutions.md#exercise-1)
```

---

## 7. Exercise Placement

| Number | Type |
|:---:|------|
| 1–2 | Direct application — exactly the procedure from the examples |
| 3–4 | Variation + trap — bait a common mistake; at least 1 constructive |
| 5 | Integration |
| 6 | **Real-world** — highest difficulty |

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

---

## 12. Checklist

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
- [ ] At least 2 constructive practice problems?
- [ ] Sentences share one rhythm; 20 characters or fewer (formula exemption applied)?
- [ ] Most important step first in the list?

### Structure
- [ ] 4–8 examples? No abstract rule before the examples?
- [ ] "What we just did" corner extracts the pattern?
- [ ] Vocabulary summary last, with the standard opening?
- [ ] No mathematical symbols before the vocabulary summary?
- [ ] 5–6 exercises, last labeled "Real-world"?
- [ ] Difficulty order: 1–2 direct, 3–4 variation+trap, 5–6 integration?
- [ ] Solutions in a separate file, every exercise linked?
- [ ] Session ends with a procedure summary card (3–4 steps)?
- [ ] Title is method-descriptive?
- [ ] No emoji?

### Credit-bearing (v9)
- [ ] Behavioral objective stated?
- [ ] Synthesis sessions defined with a tool-chain summary, mixed problems, and a constructive task?
- [ ] Common-mistake feedback links to a corrective explanation?
