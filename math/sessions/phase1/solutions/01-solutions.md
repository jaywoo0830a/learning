# Solutions — 01: Judging the Truth of Sentences — Truth Tables

---

## Practice 1

**"If I lie, I get punished" AND "if I do not lie, I do not get punished" — is this whole sentence always true?**

Let $A$ = "I lie", $B$ = "I get punished". The sentence is $(A \to B) \land (\neg A \to \neg B)$.

| $A$ | $B$ | $A \to B$ | $\neg A$ | $\neg B$ | $\neg A \to \neg B$ | $(A \to B) \land (\neg A \to \neg B)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | F | F | T | T |
| T | F | F | F | T | T | F |
| F | T | T | T | F | F | F |
| F | F | T | T | T | T | T |

The last column is **not all T**. The sentence is not always true — it is true exactly when $A$ and $B$ agree (which is the "iff" column).

> **Answer**: Not a tautology. True only when $A$ and $B$ have the same value (i.e., it equals $A \leftrightarrow B$).

---

## Practice 2

**When "$A$ implies $B$" is true, must "$B$ implies $A$" also be true?**

Look only at rows where $A \to B$ is T: rows 1, 3, 4. Among these, which have $B$ = T? Rows 1 and 3. Row 3 is $B$=T with $A$=F — a counterexample.

> **Answer**: The claim is **false**. $A \to B$ true does not force $B \to A$. (Row 3: $A$=F, $B$=T makes $A \to B$ true but $B \to A$ false.)

---

## Practice 3

**"(A implies B) and (B implies A)" — which single connector gives the same column?**

| $A$ | $B$ | $A \to B$ | $B \to A$ | $(A \to B) \land (B \to A)$ |
|:---:|:---:|:---:|:---:|:---:|
| T | T | T | T | T |
| T | F | F | T | F |
| F | T | T | F | F |
| F | F | T | T | T |

The last column is T exactly when $A$ and $B$ match.

> **Answer**: It equals **$A \leftrightarrow B$** ("iff"). "A iff B" is literally "A implies B and B implies A."

---

## Practice 4: Trap

**"(A or B) and (not A)" — in which rows is it true?**

| $A$ | $B$ | $A \lor B$ | $\neg A$ | $(A \lor B) \land \neg A$ |
|:---:|:---:|:---:|:---:|:---:|
| T | T | T | F | F |
| T | F | T | F | F |
| F | T | T | T | **T** |
| F | F | F | T | F |

> **Answer**: True only when $A$=F and $B$=T — i.e., the sentence means "not $A$, and $B$".

---

## Practice 5

**"(A and B) implies C" vs "(A implies C) or (B implies C)" — equivalent?**

| $A$ | $B$ | $C$ | $A\land B$ | $(A\land B)\to C$ | $A\to C$ | $B\to C$ | $(A\to C)\lor(B\to C)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | T | T | T | T | T |
| T | T | F | T | F | F | F | F |
| T | F | T | F | T | T | T | T |
| T | F | F | F | T | F | T | T |
| F | T | T | F | T | T | T | T |
| F | T | F | F | T | T | F | T |
| F | F | T | F | T | T | T | T |
| F | F | F | F | T | T | T | T |

The two last columns match.

> **Answer**: **Yes — equivalent.** $(A \land B) \to C \equiv (A \to C) \lor (B \to C)$.

---

## Practice 6: Real Battle

**If $A \to B$ and $B \to C$ are both true, prove $A \to C$ is always true.**

Consider only rows where both $A \to B$ and $B \to C$ are T. With $A,B,C$ there are 8 rows; the four where both implications hold are:

| $A$ | $B$ | $C$ | $A\to B$ | $B\to C$ | $A\to C$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | T | T | **T** |
| F | T | T | T | T | **T** |
| F | F | T | T | T | **T** |
| F | F | F | T | T | **T** |

(Also check: row $A$=T, $B$=T, $C$=F fails $B\to C$; row $A$=T, $B$=F fails $A\to B$; etc.)

In every row where both premises are true, $A \to C$ is true.

> **Answer**: **Always true** — this is the *syllogism* (transitivity of implication).

---

## Basic Drills

### D1. Table for $A \land B$
T only on (T,T). Otherwise F.

### D2. Table for $A \lor B$
F only on (F,F). Otherwise T.

### D3. Table for $A \to B$
F only on (T,F). Otherwise T.

### D4. Table for $A \leftrightarrow B$
T on (T,T) and (F,F); F on (T,F) and (F,T).

### D5. Table for $\neg A$
T when $A$=F; F when $A$=T.

### D6. $\neg(A \lor B)$
| $A$ | $B$ | $A\lor B$ | $\neg(A\lor B)$ |
|:---:|:---:|:---:|:---:|
| T | T | T | F |
| T | F | T | F |
| F | T | T | F |
| F | F | F | T |
Equivalent to $\neg A \land \neg B$.

### D7. $\neg(A \land B)$
| $A$ | $B$ | $A\land B$ | $\neg(A\land B)$ |
|:---:|:---:|:---:|:---:|
| T | T | T | F |
| T | F | F | T |
| F | T | F | T |
| F | F | F | T |
Equivalent to $\neg A \lor \neg B$.

### D8. $A \lor \neg A$
Both rows T → **tautology**.

### D9. $A \land \neg A$
Both rows F → **contradiction**.

### D10. $\neg(\neg A)$
Restores $A$. $\neg(\neg A) \equiv A$.

> **Answers**: D6 $\equiv \neg A\land\neg B$; D7 $\equiv \neg A\lor\neg B$; D8 tautology; D9 contradiction; D10 $A$.

---

## Advanced Drills

### A1. Exclusive or: $(A \lor B) \land \neg(A \land B)$

| $A$ | $B$ | $A\lor B$ | $A\land B$ | $\neg(A\land B)$ | result |
|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | T | F | F |
| T | F | T | F | T | T |
| F | T | T | F | T | T |
| F | F | F | F | T | F |

> **Answer**: True exactly on (T,F) and (F,T) — "exactly one of them."

### A2. $A \to B \equiv \neg B \to \neg A$

| $A$ | $B$ | $A\to B$ | $\neg B$ | $\neg A$ | $\neg B\to\neg A$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | F | F | T |
| T | F | F | T | F | F |
| F | T | T | F | T | T |
| F | F | T | T | T | T |

Same column → equivalent (the contrapositive).

### A3. $\neg(A \to B) \equiv A \land \neg B$

| $A$ | $B$ | $A\to B$ | $\neg(A\to B)$ | $\neg B$ | $A\land\neg B$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | F | F | F |
| T | F | F | T | T | T |
| F | T | T | F | F | F |
| F | F | T | F | T | F |

Same column → equivalent.

### A4. $A \to (B \to C)$ vs $(A \land B) \to C$

| $A$ | $B$ | $C$ | $B\to C$ | $A\to(B\to C)$ | $A\land B$ | $(A\land B)\to C$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | T | T | T | T |
| T | T | F | F | F | T | F |
| T | F | T | T | T | F | T |
| T | F | F | T | T | F | T |
| F | T | T | T | T | F | T |
| F | T | F | F | T | F | T |
| F | F | T | T | T | F | T |
| F | F | F | T | T | F | T |

> **Answer**: Equivalent. "$A$ implies (if $B$ then $C$)" is the same as "if $A$ and $B$ then $C$."

### A5. $(A \lor B) \land C$ vs $A \lor (B \land C)$

Counterexample row: $A$=T, $B$=F, $C$=F.
Left: $(T \lor F)\land F = F$. Right: $T \lor (F\land F) = T$. Different.

> **Answer**: **Not equivalent.** "or" does not distribute over "and" this way. ($\lor$ distributes over $\land$: $A \lor (B\land C) \equiv (A\lor B)\land(A\lor C)$ — that's the correct direction.)

### A6. $(A \to B) \land (B \to A)$
Same as Practice 3 → equals **$A \leftrightarrow B$**.

### A7. $A \to (B \land C)$ vs $(A\to B)\land(A\to C)$

| $A$ | $B$ | $C$ | $B\land C$ | $A\to(B\land C)$ | $A\to B$ | $A\to C$ | both |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | T | T | T | T | T |
| T | T | F | F | F | T | F | F |
| T | F | T | F | F | F | T | F |
| T | F | F | F | F | F | F | F |
| F | T | T | T | T | T | T | T |
| F | T | F | F | T | T | T | T |
| F | F | T | F | T | T | T | T |
| F | F | F | F | T | T | T | T |

> **Answer**: Equivalent. "If $A$ then $B$ and $C$" = "if $A$ then $B$ and if $A$ then $C$."

### A8. True exactly on (T,F) and (F,T)
That's exactly the exclusive-or pattern of A1.

> **Answer**: $(A \lor B) \land \neg(A \land B)$.

### A9. $A \leftrightarrow B \equiv (A \land B) \lor (\neg A \land \neg B)$

| $A$ | $B$ | $A\leftrightarrow B$ | $A\land B$ | $\neg A\land\neg B$ | $(A\land B)\lor(\neg A\land\neg B)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | T | F | T |
| T | F | F | F | F | F |
| F | T | F | F | F | F |
| F | F | T | F | T | T |

Same column → equivalent. "Iff" = "both true, or both false."

### A10. $A \to B \equiv \neg A \lor B$, and $A \to B \equiv A \to (A \land B)$

$A \to B \equiv \neg A \lor B$ was proved in the session (Example 10).
For the second: rows (T,T)→T, (T,F)→F, (F,T)→T, (F,F)→T — identical to $A\to B$.

> **Answer**: Both equivalences hold. In particular "$A$ implies $B$" is the same as "$A$ implies ($A$ and $B$)".
