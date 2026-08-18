# 02 — Map Note: Compressing Information into a Mental Map

> Definition of compression: not storing more, but **growing the size of a single chunk** (Miller, Cowan).
> Goal: a chapter ultimately becomes **one page you can reconstruct on blank paper**.

## 1. Neuroscientific Basis

- Working memory holds ~4 items, but **chunk size is unlimited** (chess-master studies, Chase & Simon)
- **Hierarchical organization** doubles or triples recall (Bower)
- A formed **schema** sharply lowers cognitive load on related problems (Sweller)
- **Spatial layout** is the strongest memory format — position on the page is a retrieval cue
- Copying someone else's map is not compression — **you must draw it yourself** for the generation effect

## 2. 3-Layer Structure (what lives where)

| Layer | Holds | Location | Change rate |
|---|---|---|---|
| **Map** | nodes + edges + labels (structure only) | head + 1 page | weekly |
| **Indexing note** | conditions, exceptions, violated problems | small note | daily |
| **Textbook** | full detail | shelf | — |

Like an expert: **skeleton in the head, detail outside, only pointers managed.**

## 3. 7 Compression Operators

1. **Naming** — one label per procedure ("decision tree", "dimensional analysis")
2. **3-level hierarchy** — more than 7 nodes on one level means split it
3. **Contrast pairs** — confusable pairs go together via `→contrast→` + 1 discriminator
4. **The boundary is the body** — encode one boundary case via `→but,~→` and the interior follows
5. **Causal chains `→`** — ordered as "without this, that fails"
6. **Spatialize** — reproduce positions too (same concept, always same spot)
7. **Example check** — one typical problem per node (Example); if none comes to mind, it's a hollow label (fluency illusion)

## 4. Drawing Rules

- Blank paper, **5 min cap** per drawing
- Node labels 1–2 words, **no prose** (explanations belong to the note/textbook)
- Every edge is `→` + a label word (00-symbols.md)
- One Example per node
- Fixed positions → easy to compare against blank-paper reconstruction

## 5. Example (logs & powers)

```
[powers] →inverse→ [logs]
  │ →condition in note→ (base>0, ≠1)   │ →condition in note→ (argument>0)
  ▼                                     ▼
[power rules] →contrast→ [log rules]   (discriminator: a^m·a^n=a^(m+n) vs log(xy)=log x+log y)
  Example: Ex 2.1(a)                    Example: Ex 3.5(b)
```

## 6. Data Flow and Pitfalls

```
textbook → note (`?`) → 3 straight `○` → absorbed into map as a one-word edge → delete
```

- Pitfall = **nominal fallacy**: knowing the label without the condition. The defense is the note's condition entries and violated problems.
- The map **grows** — normal. The note **shrinks and refills** — normal.

## 7. Weekly Routine

- Weekend, 5 min: merge this week's chapter maps into a one-page **subject master map**
- The highest-value work = drawing **cross-chapter links** ("this is a special case of that concept from 2 weeks ago →")
