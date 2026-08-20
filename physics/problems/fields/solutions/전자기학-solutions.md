# Solutions — Fields & Potential 2단계: 전자기학

> Back to [전자기학](../전자기학.md)

---

## Problem 1 — 균일장: 직선 지형 읽기

**1.1 —** $E = \Delta V/d = 200/0.02 = \mathbf{1.0\times10^4\ V/m}$, 방향은 **고전위 판 → 저전위 판** (내리막). 그래프에서 $E$는 **$V(x)$ 직선의 기울기(부호 반대)**입니다.

**1.2 —** $F = qE = 3\times10^{-6}\times10^4 = \mathbf{0.030\ N}$. 건너며 얻는 KE: $\Delta KE = q\Delta V = 3\times10^{-6}\times200 = \mathbf{6.0\times10^{-4}\ J}$.

**1.3 —** 전자는 음전하 → $F = qE$가 $E$의 **반대 방향**, 즉 **저전위 → 고전위** (내리막을 "역주행"). 그래도 에너지는 얻습니다:
$$\Delta KE = |q|\Delta V = 1.6\times10^{-19}\times200 = \mathbf{3.2\times10^{-17}\ J} = \mathbf{200\ eV}.$$
eV가 편한 이유: "1 V 내려갈 때 전자 1개가 얻는 에너지"라서 **전압 숫자가 곧 eV 숫자**입니다.

> **The feel:** 직선 지형에서는 $E = \Delta V/d$ 하나로 힘·일·에너지가 전부 나옵니다. 미분 불필요 — 그것이 균일장이 쉬운 이유입니다.

---

## Problem 2 — 점전하: 곡선 지형 읽기 (접선 vs 현)

**2.1 —** $kQ = 9\times10^9\times2\times10^{-6} = 1.8\times10^4$ V·m.
$$V(1)=1.8\times10^4\ \text{V}, \quad V(2)=9.0\times10^3\ \text{V}, \quad V(4)=4.5\times10^3\ \text{V}.$$

**2.2 —** 접선 ($r=2$ m): $\dfrac{dV}{dr} = -\dfrac{kQ}{r^2} = -\dfrac{1.8\times10^4}{4} = -4500$ V/m → **순간 $E = 4500$ N/C**.
현 ($r=2\to4$ m): $\dfrac{\Delta V}{\Delta r} = \dfrac{4500-9000}{4-2} = -2250$ V/m → **평균 $E = 2250$ N/C**.
다른 이유: $V \propto 1/r$은 **곡선**이라 두 점을 잇는 현의 기울기(평균)와 중간 지점의 접선 기울기(순간)가 다릅니다 — 직선(균일장)에서만 둘이 같습니다.

**2.3 —** 무한대에서 $V_\infty = 0$, $r=2$ m에서 $V=9000$ V.
$$W_{\text{당신}} = \Delta U = q(V_{\rm final}-V_\infty) = (-2\times10^{-6})(9000) = \mathbf{-0.018\ J}.$$
음수 = **당신이 일을 얻습니다** — 음전하는 $+Q$에 끌려오므로, 끌려오는 것을 **붙잡아야** 합니다(필드가 일을 해줌). $+2\,\mu$C라면 밀어내는 힘에 맞서야 하므로 $W = \mathbf{+0.018\ J}$.

> **The feel:** $W = q\Delta V$는 "고도 차이 × 내가 가진 것". 내리막이면 필드가 일해주고, 오르막이면 내가 일합니다 — 산에서 물건을 내리고 올리는 것과 동일.

---

## Problem 3 — 등전위선 지도 읽기

**3.1 —** $\mathbf{W = 0}$. 등전위선 위에서는 $\Delta V = 0$이므로 $W = q\Delta V = 0$ — 등고선을 따라 걸으면 높이가 안 변하는 것과 같습니다.

**3.2 —** $\vec{E}$(초록 화살표)는 등전위선에 **항상 수직**이고, **전위가 낮아지는 쪽(내리막)**을 가리킵니다 — 물길이 등고선을 직각으로 가로지르는 것과 같습니다.

**3.3 —** 등고선이 촘촘 = 같은 $\Delta V$가 짧은 거리 안에 발생 = **경사가 급함** = $E = \Delta V/\Delta d$가 큼. 양전하는 어디에 놓아도 **내리막**으로, 즉 $\vec{E}$ 방향(높은 $V$ → 낮은 $V$)으로 밀립니다.

> **The feel:** 지도 한 장에 "어디로, 얼마나 세게"가 전부 들어 있습니다 — 방향은 등고선의 수직(내리막), 세기는 등고선의 밀도.

---

## Problem 4 — 일과 경로: $W = q\Delta V$

**4.1 —** 경로 A: $\Delta V = 0$ → $W = q\Delta V = \mathbf{0}$.

**4.2 —** 경로 B: $\Delta V = V_{\rm end} - V_{\rm start} = 0 - 120 = -120$ V.
$$W = q\Delta V = (2\times10^{-6})(-120) = \mathbf{-2.4\times10^{-4}\ J}.$$
음수 = **필드가 일을 해줌** (내리막을 내려가므로 에너지를 얻음).

**4.3 —** 일이 경로가 아니라 **출발점과 도착점의 $V$ 차이만으로** 결정되기 때문입니다. 이것이 정전기력이 **보존력(conservative)**이라는 뜻이고, 그래서 경로와 무관한 "고도" $V$가 존재할 수 있습니다. 마찰은 경로마다 일이 달라서 이러한 고도를 정의할 수 없습니다.

> **The feel:** $W = q\Delta V$는 보존력의 정의이자 전위의 존재 증명입니다. "고도가 존재한다"와 "일이 경로에 무관하다"는 같은 말입니다.

---

## Problem 5 — 유도를 직접 재현하기

**5.1 —** (i) $W = F\,\Delta r$ (일의 정의). (ii) $\Delta U = -W$ (**마이너스는 여기서 태어납니다** — "힘이 일을 해주면 예금이 줄어든다"). (iii) $U = qV$ 대입:
$$\Delta U = q\,\Delta V = -F\,\Delta r \;\Rightarrow\; F = -q\frac{\Delta V}{\Delta r} \;\xrightarrow{\ \div q\ }\; E = -\frac{\Delta V}{\Delta r} \;\xrightarrow{\ \Delta r\to0\ }\; \boxed{E = -\frac{dV}{dr}}.$$

**5.2 —** 통분해서 직접:
$$\Delta V = kQ\Big[\frac{1}{r+\Delta r} - \frac{1}{r}\Big] = kQ\frac{r-(r+\Delta r)}{r(r+\Delta r)} = -\frac{kQ\,\Delta r}{r(r+\Delta r)}$$
$$\frac{\Delta V}{\Delta r} = -\frac{kQ}{r(r+\Delta r)} \;\xrightarrow{\ \Delta r \to 0\ }\; -\frac{kQ}{r^2} \;\Rightarrow\; E = -\frac{dV}{dr} = \mathbf{+\frac{kQ}{r^2}}.$$
$r=2$ m, $Q=2\,\mu$C에서: $E = 1.8\times10^4/4 = \mathbf{4500\ N/C}$ — Problem 2.2의 접선 값과 일치 ✓.

**5.3 —** $V=Ed$는 **$V=kQ/r$ 곡선의 접선(직선 근사)**입니다 — 균일장이란 "곡선 지형을 판 사이에서 평평하게 본 것"입니다 (역학에서 $mgh$가 $U=-GMm/r$의 접선이었던 것과 동일). 요약 한 문장: **"전기장은 전위 지형의 경사도이고, 마이너스는 내리막 방향이다"** — $E=-dV/dr$.

> **The feel:** 유도를 재현할 수 있다면 공식이 외우는 대상이 아니라 **재발견하는 대상**이 됩니다. 2단계의 전부가 일의 정의 + $\Delta U=-W$ + $U=qV$ 세 줄 안에 있었습니다.
