# Solutions — Energy — Bank Ledger

> Back to [Energy 2](../2.md)

---

## Problem 1 — The Ledger Never Lies

**1.1 — Ledger** for $m=0.5$ kg, $v_0=20$ m/s (all values in J):

| Moment | Cash (KE) | Deposit ($mgh$) | Balance |
|---|---|---|---|
| (i) launch, $h=0$ | $100$ | $0$ | $100$ |
| (ii) $h=10$, going up | $50$ | $50$ | $100$ |
| (iii) top, $h=20$ | $0$ | $100$ | $100$ |
| (iv) $h=10$, coming down | $50$ | $50$ | $100$ |
| (v) back at hand | $100$ | $0$ | $100$ |

- Cash at launch $=\tfrac12(0.5)(20)^2=100$ J; top height $h=v_0^2/2g=400/20=20$ m; at $h=10$ m, $v=\sqrt{2(50)/0.5}=\sqrt{200}\approx14.1$ m/s ✓.

**1.2 —** No. Rows (ii) and (iv) are **identical** — the ledger records only the *size* of the velocity, never its direction. Direction lives in **momentum**, the ledger's other column — energy is direction-blind.

**1.3 —** From launch to top: Deposit $0\to100$ J, Cash $100\to0$ J — a pure **internal transfer**, Balance pinned at $100$ J the whole flight. Since the Balance column never moved, **nothing outside did any work** (gravity is inside the system). That one column is a complete answer to the "was work done?" question.

> **The feel:** a thrown ball is the cleanest possible bank story — the Deposit is just Cash parked temporarily; the Balance never blinks.

---

## Problem 2 — Who Owns the Deposit?

**2.1 —** $U=\tfrac12kx^2=\tfrac12(600)(0.5)^2=75$ J. The money belongs to the **spring + A + B system jointly** — the spring's energy is a Deposit, not A's Cash or B's Cash, and you cannot point to a single owner.

**2.2 —** Momentum: $m_Av_A=m_Bv_B$ → $2v_A=3v_B$ → $v_A=1.5\,v_B$.
Energy: $\tfrac12(2)v_A^2+\tfrac12(3)v_B^2=75$ → $v_A^2+1.5v_B^2=75$ → $(2.25+1.5)v_B^2=3.75\,v_B^2=75$.
$$v_B=\sqrt{20}\approx4.47\text{ m/s},\qquad v_A=1.5\sqrt{20}=\sqrt{45}\approx6.71\text{ m/s}.$$
Check: Cash$_A=\tfrac12(2)(45)=45$ J, Cash$_B=\tfrac12(3)(20)=30$ J, total $75$ J ✓.

**2.3 —** The split is **$45$ J to A, $30$ J to B — not $50/50$**. The lighter block walks away with more Cash. The split is dictated by **momentum conservation** (the ledger's other column), not by fairness — and at no instant did either block own $37.5$ J. The Deposit was never theirs individually; it converted into Cash *in the ratio the momentum rule demands*.

> **The feel:** joint ownership is not a technicality — the spring's $75$ J has no individual owner until the release, and the two conservation laws together decide the payout.

---

## Problem 3 — The Non-Refundable Fee

**3.1 —** Starting Deposit $=mgh=2(10)(5)=100$ J. Fee $=20$ J. Final Cash $=100-20=80$ J:
$$v=\sqrt{2(80)/2}=\sqrt{80}\approx8.94\text{ m/s}.$$

**3.2 —** The $20$ J is now **heat** in the ramp, wheels, and air — outside the mechanical ledger. Both sentences are true: **energy of the universe is conserved** ($100$ J total, $80$ in the ledger + $20$ in heat), while the **Balance dropped** $100\to80$. The fee didn't destroy money; it moved it to an account you no longer control.

**3.3 —** Pushing back up the same rough ramp: you must refill the Deposit ($100$ J) **and** pay the fee again ($20$ J) → **$120$ J of work**. Lifting straight up: only $100$ J. Fees are charged per trip and are non-refundable, so every rough round trip costs more than $mgh$ — exactly why real machines are never friction-free round trips.

> **The feel:** friction is a toll booth, not a thief — it charges the same fee on every pass, and the fee is payable to the surroundings as heat, never back into the ledger.

---

## Problem 4 — Two Ledgers, One Slide

**4.1 — System A (skier + Earth):** top: Balance $=mgh=60(10)(10)=6000$ J, all Deposit. Bottom: all Cash, $6000$ J.
$$v=\sqrt{2gh}=\sqrt{200}\approx14.1\text{ m/s}.$$
Balance constant → **nothing outside did work**; gravity is internal.

**4.2 — System B (skier alone):** top: Balance $=0$ (no Cash, and the skier alone holds no Deposit). Bottom: Cash $=6000$ J. **Balance rose $6000$ J** → something outside did $6000$ J of work on the system: the **Earth, via gravity**.

**4.3 —** "Both, depending on the ledger." Gravity does $+6000$ J of work on the skier *in the skier-only ledger*; in the joint ledger that same transaction appears as a $6000$ J drop in the Deposit. The reconciliation is
$$W_{\text{gravity (skier-only)}} = -\Delta U_{\text{(joint)}} = +6000\text{ J}.$$
They are two entries for one transaction — use either ledger per calculation, never both in the same equation (that would double count).

> **The feel:** "Did gravity do work?" has no absolute answer — the ledger boundary decides. The discipline is: pick the boundary, then stay in it.

---

## Problem 5 — Audit the Statements

**5.1 —** The Balance is the **same at all three points**: $mgh$ at release, $mgh$ at the lowest point (all Cash), $mgh$ at the other-side turning point (all Deposit). Only the Cash/Deposit mix changes.

**5.2 —** Wrong statements:
- (a) "KE is conserved" — **wrong**: Cash swaps with Deposit constantly; only the **Balance** is conserved.
- (d) "Deposit is largest at the lowest point" — **wrong**: the Deposit is **zero** at the bottom (all Cash there).
- (b) "Energy is conserved" ✓ and (c) "at the lowest point all energy is Cash" ✓ are correct.

**5.3 —** It rose only $0.8h$, so the fee is
$$\text{fee}=mg(h-0.8h)=0.2\,mgh \;=\; 20\%\text{ of the original Balance}.$$
In the teacher's words: the Balance **dropped**, so the system did work **on something else** — the **air** — and the missing money is now heat in the air (plus a little sound). The money never vanished; it left the ledger through a one-way fee.

> **The feel:** conservation means *total* money, not *ledger* money. A falling Balance is never "energy destroyed" — it is the system paying the outside world for work, in a currency (heat) the ledger can never accept back.
