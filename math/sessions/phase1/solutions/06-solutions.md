# Solutions — 06: Gödel's Incompleteness Theorem — Mathematics That Cannot Decide

---

## Practice 1

**With the symbol table ($0$=1, $+$=2, $\times$=3, $=$=4, $\neg$=5, $\forall$=6, $x$=7, $y$=8), compute the Gödel number of "$0 = 0$".**

Code sequence: $0 \to 1$, $=$ → 4, $0 \to 1$ → $[1, 4, 1]$.

Gödel number: $2^1 \times 3^4 \times 5^1 = 2 \times 81 \times 5 = 810$.

> **Answer**: $2^1 \cdot 3^4 \cdot 5^1 = 810$.

---

## Practice 2

**Why can't a consistent system prove its own consistency? (Second Incompleteness, intuitive explanation.)**

The system can express "I am consistent" as a sentence. If it proved that sentence, then — since it cannot prove $G$ (the sentence "I am not provable") — the system would have to conclude "$G$ is true but unprovable," which is itself a proof of $G$'s truth. In fact, proving "I am consistent" is essentially proving $G$ (in the right system), and we know $G$ is unprovable. So consistency is unprovable from inside.

> **Answer**: Proving one's own consistency would amount to proving $G$, which is impossible. The system cannot certify itself from within.

---

## Practice 3

**The barber paradox ends "no such barber exists"; the Gödel sentence ends "the system cannot decide $G$." Why the same structure?**

Both are self-referential and both collapse under their own logic:

- Barber: the rule "shaves exactly the non-self-shavers" must apply to the barber himself. Applying it to himself gives a contradiction, so the object cannot exist.
- Gödel: the sentence $G$ = "I am not provable" must apply to itself. Asking "is $G$ provable?" gives a contradiction either way, so the system cannot decide it.

Both are the same loop — a description forced to include itself — producing an unavoidable limit.

> **Answer**: Self-reference: assuming the object/system satisfies its own description leads to contradiction; the conclusion is a limit (nonexistence / undecidability).

---

## Practice 4: Trap

**"Can't I add $G$ as an axiom and close the gap?"**

Adding $G$ as an axiom makes $G$ provable in the *extended* system. But the extended system has its own provability predicate, and the same diagonal construction produces a **new** sentence $G'$ = "I am not provable in the extended system." $G'$ is again true and unprovable there. The gap reappears at every level — no finite extension closes it.

> **Answer**: Every extension produces a new Gödel sentence. Incompleteness is not a hole you can patch; it's a permanent feature.

---

## Practice 5

**Why is proof-checking mechanical?**

A proof is a finite sequence of lines; each line is either an axiom or follows from earlier lines by an inference rule. Checking one rule application is a syntactic task:

Modus ponens: if line $i$ is $P$ and line $j$ is $P \to Q$, then line $\ell$ may be $Q$. To check line $\ell$, compare shapes: does line $i$ match the left side of line $j$'s implication, and does line $\ell$ match the right side? No meaning is involved — just symbol matching.

A computer (hence an arithmetic formula) can do this digit-by-digit check for every line. That's exactly what makes $\text{Provable}(x)$ expressible in arithmetic.

> **Answer**: Proof-checking is string comparison — purely syntactic — so it's a computation, and computations are expressible in arithmetic.

---

## Practice 6: Real Battle

**Why is the Halting Problem structurally the same as Gödel's theorem? Where is the self-reference?**

Halting Problem: assume a program $H(P, I)$ decides whether program $P$ halts on input $I$. Build a new program $D$ that, on input $P$, runs $H(P,P)$ and then does the opposite: loops forever if $H$ says "halts," halts if $H$ says "loops."

Now run $D$ on itself: $D(D)$ halts iff $H$ predicts $D(D)$ doesn't halt — contradiction. No such $H$ exists.

The structure matches Gödel exactly:
- Gödel: $G$ = "I am not provable" — if the system proves it, contradiction.
- Halting: $D$ = "I don't halt" (via the halting test) — if the decider says it halts, contradiction.

Both smuggle **self-reference** ("this very program/sentence") into the question, and both conclude a hard limit: no complete proof system, no halting decider.

> **Answer**: Both use self-reference ("about itself") to force a contradiction, proving that no system/program can answer every question about itself.

---

## Basic Drills

**D1.** "$x = x$" → codes $[7,4,7]$ → $2^7 \cdot 3^4 \cdot 5^7 = 128 \cdot 81 \cdot 78125 = 810{,}000{,}000$.
**D2.** "$0 + 0 = 0$" → codes $[1,2,1,4,1]$ → $2^1 \cdot 3^2 \cdot 5^1 \cdot 7^4 \cdot 11^1 = 2 \cdot 9 \cdot 5 \cdot 2401 \cdot 11 = 2{,}376{,}990$.
**D3.** $2^1 \cdot 3^4 \cdot 5^1$ → codes $[1,4,1]$ → "$0 = 0$".
**D4.** $2^6 \cdot 3^7 \cdot 5^4 \cdot 7^1$ → codes $[6,7,4,1]$ → "$\forall x = 0$" (the sentence "for all $x$, $x$ equals 0" in this code table).
**D5.** **True** — unique prime factorization is what makes decoding unambiguous.
**D6.** $\text{Provable}(\ulcorner\phi\urcorner)$ claims: "the sentence $\phi$ has a proof in this system."
**D7.** $G$: "I am not provable" — $G \leftrightarrow \neg\text{Provable}(\ulcorner G\urcorner)$.
**D8.** $G$ is **true but unprovable** (false is wrong).
**D9.** The extended system gets a new Gödel sentence $G'$; the gap reappears.
**D10.** First: every consistent system has a true unprovable sentence. Second: a consistent system cannot prove its own consistency.

---

## Advanced Drills

### A1. Encoding is reversible
Two different code sequences $[c_1,\dots,c_n]$ and $[d_1,\dots,d_m]$ produce numbers $2^{c_1}3^{c_2}\cdots p_n^{c_n}$ and $2^{d_1}3^{d_2}\cdots p_m^{d_m}$. By the Fundamental Theorem of Arithmetic (unique prime factorization), equal numbers force the same primes with the same exponents — hence the same sequence. So distinct sentences always get distinct Gödel numbers.

### A2. $\text{Provable}(x)$ is arithmetically definable
"Checking a proof" reduces to: does there exist a finite sequence of numbers (encoded proofs) where each line is an axiom or follows by a rule (a finitely-checkable shape comparison), ending in the target sentence? Finite searches and symbol comparisons are computable, and computable checks are expressible as arithmetical formulas. So "there is a proof of $x$" is a genuine statement about natural numbers.

### A3. "False" vs "not provable"
"False" is a semantic property (about the world) the system cannot talk about — so "this sentence is false" escapes the system's reach and becomes a paradox. "Provable" is a syntactic, mechanical property the system *can* express. Swapping in "not provable" keeps the self-reference but makes the sentence a legitimate arithmetical claim — turning a paradox into a theorem about the system's limits.

### A4. Both halves of the argument
Assume the system is consistent.
- If $G$ provable: the system proves "I am not provable" — but proving $G$ means $G$'s content is false, so the system proves a falsehood → inconsistent. Contradiction. Hence $G$ is not provable.
- If $\neg G$ provable: the system proves "G is provable." But $G$ is not provable (previous half), so the system proves a falsehood → inconsistent. Contradiction. Hence $\neg G$ is not provable.
Neither is provable; yet $G$'s content ("I am not provable") is exactly the truth.

### A5. Why consistency matters
If the system could prove false statements, then "G is provable" being false wouldn't be a problem — inconsistent systems prove both true and false claims, and the contradiction in A4 disappears. Consistency is what makes "the system proves only truths" available as a fact the argument leans on. Without it, incompleteness has no bite.

### A6. Barber vs diagonal argument
Both build "the object that must be left out":
- Diagonal (Session 05): the real $d$ differing from every listed number — left out of the list.
- Barber/Gödel: the rule applied to itself — the barber who can't exist, the sentence $G$ the system can't decide.
All three are the same move: assume completeness, construct the item that contradicts it.

### A7. Halting Problem — the self-referential program
Assume $H(P,I)$ decides halting. Define $D(P)$: run $H(P,P)$; if it says "halts," loop forever; if it says "loops," halt.
Run $D(D)$: $D(D)$ halts ⟺ $H(D,D)$ says "loops" ⟺ $D(D)$ does not halt. Contradiction. So $H$ cannot exist. (This is the full version of Practice 6.)

### A8. Same shape: uncountability and incompleteness
- Uncountability: assume a complete list of reals; construct $d$ differing from every entry; contradiction.
- Incompleteness: assume a complete proof system; construct $G$ (via the diagonal/self-reference) that the system cannot prove; contradiction.
Both: assume completeness → build the left-out object → contradiction. The diagonal construction is the shared engine.

### A9. "Every true sentence about natural numbers is provable" — false
$G$ is a true sentence about natural numbers (it correctly asserts its own unprovability — a fact about the system and numbers) that is not provable. So the claim "every true sentence is provable" is false. This is the very content of the First Incompleteness Theorem.

### A10. Does incompleteness apply to human reasoning?
- **For**: humans are finite; if human reasoning were a consistent formal system (say, capturing all our arithmetic beliefs), it would face the same $G$ — so no finite, consistent formalization captures all truth.
- **Against**: human reasoning may not be a fixed consistent formal system — we can "step outside" any proposed system, notice its $G$, and accept it (as we just did). The theorem binds *formal systems*, not necessarily minds.
- **Conclusion (one view)**: Gödel shows no formal system captures all arithmetic truth; whether the human mind is such a system is open — but the theorem famously inspired positions on both sides.
