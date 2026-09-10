# Solutions — 01: Judging the Truth of Sentences — Truth Tables
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
True exactly on the rows where the implication columns match → equals **$A \leftrightarrow B$**.

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
