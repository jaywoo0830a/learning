# Solutions — Work — Bank Ledger

> Back to [Work 2](../2.md)

---

## Problem 1 — Cash, Deposit, or Balance?

**1.1 — Classifications:**
- (a) skier's energy of motion → **Cash** (her own KE, spendable by her alone).
- (b) the book's $mgh$ → **Deposit** — but owned by the **book + Earth pair** ($=2\times10\times3=60$ J), not by the book alone.
- (c) stretched slingshot → **Deposit** (elastic PE stored in the band).
- (d) brake heat → **outside the ledger** — it has already left the mechanical account.
- (e) pendulum at the lowest point: (almost) all **Cash**; at the highest point: all **Deposit** — yet the **Balance is identical** at both.

**1.2 — Ledger** for $m=0.5$ kg (all values in J):

| Moment | Cash (KE) | Deposit ($mgh$) | Balance |
|---|---|---|---|
| (i) release, $h=4$ | $0$ | $20$ | $20$ |
| (ii) $h=2$ | $10$ | $10$ | $20$ |
| (iii) ground | $20$ | $0$ | $20$ |

- At $h=2$: $v=\sqrt{2g(2)}=\sqrt{40}=6.32$ m/s, so Cash $=\tfrac12(0.5)(40)=10$ J ✓.
- The Balance is constant ($20$ J) → **only internal transfers happened; no external work was done**.

**1.3 —** Strictly, the statement is loose. The Deposit belongs to the **ball + Earth system** jointly — gravity is an interaction between them, so neither owns the money alone. When the ball falls, the Deposit converts to Cash shared between ball and Earth: the ball's speed is $\sqrt{2gh}$, but Earth's speed is $\frac{m}{M}\sqrt{2gh}\approx 0$ — so the ball walks away with essentially **all** the Cash, which makes it *look* like the ball owned the Deposit all along. It didn't: it was a joint account.

> **The feel:** classification is half the game. Deposit entries are always *jointly* owned — there is no "the ball's PE" strictly speaking, only "the ball–Earth account's PE".

---

## Problem 2 — Reading the Balance

**2.1 —** System = box + Earth, $m=2$ kg, $d=3$ m.
- $\Delta\text{Cash}=\Delta K=0$ (rest to rest). $\Delta\text{Deposit}=mg\Delta h=2(10)(3)=+60$ J.
- $\Delta\text{Balance}=+60$ J → an outside agent (the **cable**) did $+60$ J of work **on** the system.
- Direct check: $W_{\text{cable}}=T\,d=mg\,d=20\times3=60$ J ✓ — the balance reading and the force × distance computation are the *same law*.

**2.2 —** Ends at $v=2$ m/s.
- $\Delta\text{Cash}=\tfrac12(2)(4)=4$ J, $\Delta\text{Deposit}=+60$ J → $\Delta\text{Balance}=+64$ J → $W_{\text{cable}}=64$ J.
- The cable's money split: **$60$ J filled the Deposit, $4$ J topped up the Cash.**
- Kinematics check: $a=v^2/2d=4/6=\tfrac23$ m/s²; $T=m(g+a)=2(10+\tfrac23)=\tfrac{64}{3}$ N; $W=Td=\tfrac{64}{3}\times3=64$ J ✓.

**2.3 —** Lowering $3$ m at constant speed:
- $\Delta\text{Deposit}=-60$ J, $\Delta\text{Cash}=0$ → $\Delta\text{Balance}=-60$ J → the **system did $+60$ J of work on the cable** (the cable's ledger received $60$ J).
- Gravity does **no separate work here** — with Earth inside the system, gravity is internal and its effect is already inside the Deposit change. Counting it again would be double counting.

> **The feel:** the Balance column *is* the work–energy theorem at the system level: $\Delta\text{Balance}=W_{\text{external}}$. You never need to list internal forces — they've already been folded into the Deposit.

---

## Problem 3 — Moving the Boundary

**3.1 — System A (ball + Earth):** top: Deposit $=mgh=200$ J, Cash $0$ → Balance $200$ J. Ground: Cash $=\tfrac12(1)(20)^2=200$ J, Deposit $0$ → Balance $200$ J. Balance constant → **no external work**. Gravity is *internal* — its entire effect lives inside the Deposit column.

**3.2 — System B (ball alone):** top: Balance = Cash $=0$. Ground: Cash $=200$ J → **Balance rose $200$ J** → something outside did $200$ J of work on the system: the **Earth**, via gravity. $W=mgd=1(10)(20)=200$ J ✓.

**3.3 —** Both statements are true, but in **different ledgers**:
- "Gravity does $200$ J of work on the ball" → ball-only ledger.
- "The ball's PE decreased $200$ J" → joint ledger.

They are the *same transaction viewed from two sides* — adding both into one equation double counts it. Correct single-ledger equations:
$$\text{System A: }\Delta K+\Delta U=0; \qquad \text{System B: }\Delta K=W_{\text{gravity}}=200\text{ J}.$$
Writing $\Delta K = W_g - \Delta U = 200 - (-200) = 400$ J is the double-counted error.

> **The feel:** the teacher's rule — "Balance rose → someone did work on the system" — needs the **boundary stated**. Move the boundary and the same fall reads as "no work" or "Earth did $200$ J of work". Both ledgers are correct; mixing them is the classic mistake.

---

## Problem 4 — The Fee

**4.1 —** $h=L\sin30°=2.5$ m → starting Deposit $=mgh=4(10)(2.5)=100$ J.
- **Fee:** $f_k=\mu_k mg\cos30°=0.3(40)(0.866)=10.4$ N; $W_f=f_kL=10.4\times5\approx52$ J (leaves the ledger as heat).
- Final Cash $=100-52=48$ J → $v=\sqrt{2(48)/4}=\sqrt{24}\approx4.9$ m/s.
- Balance dropped $100\to48$: the **system did $52$ J of work on the surroundings** (heat in ramp + block).

**4.2 —** No — the fee is **non-refundable**. Heat never spontaneously converts back into the cart's Cash or Deposit. That is exactly why the Balance is only conserved when the ledger has no fees, and why a friction problem always ends with less Balance than it started.

**4.3 —** Frictionless: **no external agent changes the Balance** — the normal force does zero work (perpendicular to motion, surface fixed), and gravity is internal. Balance stays $100$ J: $v=\sqrt{2(100)/4}=\sqrt{50}\approx7.07$ m/s (vs. $4.9$ m/s with the fee). The fee is the only transaction with the outside.

> **The feel:** friction is not "a force that stops motion" in this ledger — it is a **withdrawal** from the joint account, paid to the surroundings as heat, and it never comes back.

---

## Problem 5 — Auditing Wrong Ledgers

**5.1 —** $m=2$ kg, $h=4$ m: $W_g=+80$ J, $\Delta U=-80$ J, $\Delta K=+80$ J are all correct — but $W_g$ and $\Delta U$ are the **same transaction recorded twice** (ball-only ledger vs. joint ledger). The correct ledgers:
$$\text{Ball alone: }\Delta K=W_g=+80\text{ J}; \qquad \text{Joint: }\Delta K+\Delta U=80-80=0.$$
The Balance did not gain anything — $\Delta\text{Balance}=0$, and no external work was done on the ball–Earth system.

**5.2 —** The true part: net force on the box is zero, so the **net work on the box** is zero and the box's **Cash is unchanged** — correct. The missing part: the Balance is not just the box's Cash; it includes the **joint Deposit**, which rose by $60$ J. The cable (outside the system) deposited $60$ J into the joint account. Confusing *one object's statement of account* with *the system's Balance* is the error.

**5.3 —** "Normal forces never do work" is false — it should be "a normal force does no work when its point of application does not move along the normal." A fixed floor does zero work, but a **rising elevator floor** does: $W_N=N\,d=mg\,d=60(10)(10)=6000$ J.
- **Passenger alone:** net work $=(N-mg)d=0$ → Cash unchanged ✓ (consistent with constant speed).
- **Passenger + Earth:** $\Delta\text{Deposit}=mgd=+6000$ J, $\Delta\text{Cash}=0$ → Balance $+6000$ J → the **floor (outside) did $+6000$ J of work on the system** ✓.

Both ledgers agree; the deposit came from the elevator's motor, through the floor.

> **The feel:** *any* force can do work if its point of application moves with a component along the force — even a normal force. The ledger tells you who to credit: follow the Balance change, then ask which agent sits **outside** the boundary.
