// math/graph/phase2/19A/19A-ode-modeling.mjs — 세션 19A(ODE 모델링 입문) 그림
//
// ── figure 목록 (키 = 출력 파일명 = 마크다운 태그 id) ──────────────
//    19a-1-slope-field       기울기장 y'=x+y(§9.1 예제) + y'=y-2x 해곡선(§9.2 #11)
//    19a-2-growth-decay      지수 모델 Ae^{kt}: 성장(k>0, 배가시간) vs 감쇠(k<0, 반감기)
//    19a-3-logistic          로지스틱 S-곡선 + 초기 지수 근사 + 변곡점 P=L/2
//    19a-4-phase-line        자율 ODE y'=y(1-y): 기울기장 + 위상선(source/sink)
//    19a-5-rl-circuit        RL 회로 I(t)=5(1-e^{-3t}) → 정상상태 5A, 시정수 τ=1/3
//    19a-6-euler-method      오일러 방법 — 계단 궤적 vs 정확해 vs 내장 RK4 (§9.2 #19)
//
// ── 코어 API (기준 @jaywoo0830a/logos 0.5.0) ─────────────────────
//   기울기장 = 코어 `vectorField((x,y)=>[1,f])` (docs/testing/TEXTBOOK.md #48)
//   곡선 = `curve.fn(f).on([a,b])` · 기준선 = `line.horizontal/vertical`
//   화살표 = `annotate.arrow(A,B)` · 점 = `point(x,y).dot({open})`
//   내장 ODE 솔버 = `curve.ode({dy, y0})` — RK4 (해석해 없이 수치해 곡선)
//   유계 선분 = `segment(A, B)` — 오일러 계단 한 스텝 (kit.seg 는 line.through 무한직선이라 부적합)
//   18A의 polyline/stem 플러그인이 필요 없다 — 코어 빌더만으로 충분.
import { annotate, curve, kit, line, point, segment, vectorField, tex } from '@jaywoo0830a/logos';

const { plot2d, subplots, palette } = kit;
const { blue, green, orange, red, purple, gray } = palette.tab;
const LIGHT = '#bbbbbb', ASYMP = '#cccccc';   // 지면 톤(팔레트 밖)

/** 축 설정 — 코어 plot2d 의 axes 옵션 그대로 */
const AX = (x, y) => ({ x: { label: x }, y: { label: y } });

/** 범례 대신 같은 색 라벨 (코어 annotate.text 체이닝의 1줄 별칭 — 이 파일 안에서만) */
const legend = (at, text, color, font = 10.5, anchor = 'start') =>
  annotate.text(at).label(text).font(font).color(color).bold().anchor(anchor);

// ══ 1. 기울기장 + 해곡선 (1×2) ═════════════════════════════════
//   왼쪽: y'=x+y — 해 y=-x-1+Ceˣ, nullcline y=-x-1 (§9.1 예제 검증 그림)
//   오른쪽: y'=y-2x (§9.2 #11) — (1,0) 통과 해 y=2x+2-4eˣ⁻¹
function slopeField() {
  const left = plot2d([-3, 3], [-4, 4], { size: [520, 420], axes: AX('x', 'y'), grid: { alpha: 0.25 } })
    .title("y' = x + y  — slope field").add(
      vectorField((x, y) => [1, x + y]).step(0.5).len(0.36).color(LIGHT).stroke(1.1),
      curve.fn((x) => -x - 1).on([-3, 3]).color(gray).stroke(1.4).dash([5, 4]),
      curve.fn((x) => -x - 1 + Math.exp(x)).on([-3, 1.35]).color(blue).stroke(2.2),
      curve.fn((x) => -x - 1 + 2 * Math.exp(x)).on([-3, 0.65]).color(orange).stroke(2.2),
      point(0, 0).dot().color(purple).size(4.5),
      legend([0.2, 3.5], tex`y = -x-1+Ce^{x}\;\;(C=1,2)`, blue),
      legend([0.2, 2.8], tex`\text{nullcline}\;\; y = -x-1`, gray),
    );
  const right = plot2d([-2, 3], [-6, 6], { size: [520, 420], axes: AX('x', 'y'), grid: { alpha: 0.25 } })
    .title("y' = y − 2x  — §9.2 #11, through (1,0)").add(
      vectorField((x, y) => [1, y - 2 * x]).step(0.5).len(0.36).color(LIGHT).stroke(1.1),
      curve.fn((x) => 2 * x).on([-2, 3]).color(gray).stroke(1.4).dash([5, 4]),
      curve.fn((x) => 2 * x + 2 - 4 * Math.exp(x - 1)).on([-2, 2.15]).color(red).stroke(2.2),
      point(1, 0).dot().color(purple).size(4.5),
      legend([-1.8, 5.2], tex`\text{solution}\;\; y = 2x+2-4e^{x-1}`, red),
      legend([-1.8, 4.4], tex`\text{nullcline}\;\; y = 2x`, gray),
    );
  return subplots([left, right], { cols: 2, tight: true, title: 'Slope Fields and Solution Curves' });
}

// ══ 2. 지수 모델 — 성장 vs 감쇠 (1×2) ═══════════════════════════
//   왼쪽: k>0 성장 — 배가시간 t₂ = ln2/k 는 모든 곡선에서 같은 수평 거리
//   오른쪽: k<0 감쇠 — 반감기 t½ = ln2/|k|
function growthDecay() {
  const LN2 = Math.LN2;
  const left = plot2d([0, 3], [0, 4.2], { size: [520, 420], axes: AX('t', 'P'), grid: { alpha: 0.28 } })
    .title(tex`\text{Growth:}\;\; P = Ae^{kt},\; k > 0`).add(
      curve.fn((t) => Math.exp(0.5 * t)).on([0, 3]).color(blue).stroke(2.2),
      curve.fn((t) => Math.exp(t)).on([0, 1.45]).color(orange).stroke(2.2),
      curve.fn((t) => 0.6 * Math.exp(t)).on([0, 1.85]).color(green).stroke(2.2),
      line.vertical(LN2).color(red).stroke(1.2).dash([5, 4]),
      line.horizontal(2).color(red).stroke(1.2).dash([5, 4]),
      point(LN2, 2).dot().color(red).size(4),
      legend([1.65, 3.95], tex`e^{t/2}`, blue),
      legend([1.65, 3.45], tex`e^{t},\;\; 0.6\,e^{t}`, orange),
      annotate.text([LN2 + 0.1, 0.25]).label(tex`t_2 = \ln 2/k`).font(10).color(red).bold(),
    );
  const right = plot2d([0, 4], [0, 1.2], { size: [520, 420], axes: AX('t', 'P'), grid: { alpha: 0.28 } })
    .title(tex`\text{Decay:}\;\; P = Ae^{kt},\; k < 0`).add(
      curve.fn((t) => Math.exp(-0.5 * t)).on([0, 4]).color(blue).stroke(2.2),
      curve.fn((t) => Math.exp(-t)).on([0, 4]).color(orange).stroke(2.2),
      line.vertical(LN2).color(red).stroke(1.2).dash([5, 4]),
      line.horizontal(0.5).color(red).stroke(1.2).dash([5, 4]),
      point(LN2, 0.5).dot().color(red).size(4),
      legend([2.3, 1.05], tex`e^{-t/2}`, blue),
      legend([2.3, 0.85], tex`e^{-t}`, orange),
      annotate.text([LN2 + 0.1, 0.1]).label(tex`t_{1/2} = \ln 2/|k|`).font(10).color(red).bold(),
    );
  return subplots([left, right], { cols: 2, tight: true, title: 'Exponential Growth and Decay — Doubling Time vs Half-Life' });
}

// ══ 3. 로지스틱 성장 — S-곡선 (단일) ═══════════════════════════
//   L=1000, P₀=100, k=0.8. 초기엔 지수근사 P₀e^{kt}(빨강 점선), 변곡점 P=L/2 에서 성장 최대.
function logistic() {
  const L = 1000, P0 = 100, k = 0.8;
  const P = (t) => L / (1 + 9 * Math.exp(-k * t));
  const tInf = Math.log(9) / k;                 // P = L/2 인 시각
  return plot2d([0, 10], [0, 1150], { size: [760, 480], axes: AX('t', 'P(t)'), grid: { alpha: 0.28 } })
    .title(tex`\text{Logistic Growth --- } L = 1000,\; P_{0} = 100`).add(
      curve.fn(P).on([0, 10]).color(blue).stroke(2.4),
      curve.fn((t) => P0 * Math.exp(k * t)).on([0, 2.05]).color(red).stroke(1.6).dash([5, 4]),
      line.horizontal(L).color(ASYMP).stroke(1.3).dash([5, 4]),
      line.horizontal(L / 2).color(gray).stroke(1).dash([4, 4]).opacity(0.7),
      line.vertical(tInf).color(gray).stroke(1).dash([4, 4]).opacity(0.7),
      point(tInf, L / 2).dot().color(red).size(5),
      annotate.text([9.9, 1065]).label(tex`\text{carrying capacity}\;\; L = 1000`).font(10.5).color(gray).anchor('end'),
      annotate.text([tInf + 0.15, 585]).label(tex`\text{inflection: } P = L/2\ \text{(fastest growth)}`).font(10).color(red).bold(),
      legend([0.55, 950], tex`P_0 e^{kt}\ \text{(early exponential approx.)}`, red),
      legend([0.55, 865], tex`P(t) = L/(1 + Ae^{-kt})`, blue),
    );
}

// ══ 4. 위상선 — 자율 ODE y'=y(1-y) (1×2) ═══════════════════════
//   왼쪽: 기울기장 + 해곡선(y₀=2 는 위에서 1 로, y₀=0.2 는 아래에서 1 로)
//   오른쪽: 위상선 — y=0 source(열린 점·화살표 밖), y=1 sink(채운 점·화살표 안)
function phaseLine() {
  const left = plot2d([0, 6], [-0.5, 2.5], { size: [520, 460], axes: AX('t', 'y'), grid: { alpha: 0.25 } })
    .title("y' = y(1 − y)  — slope field").add(
      vectorField((x, y) => [1, y * (1 - y)]).step(0.4).len(0.3).color(LIGHT).stroke(1.1),
      curve.fn((t) => 1 / (1 - 0.5 * Math.exp(-t))).on([0, 6]).color(orange).stroke(2.2),
      curve.fn((t) => 1 / (1 + 4 * Math.exp(-t))).on([0, 6]).color(blue).stroke(2.2),
      line.horizontal(1).color(ASYMP).stroke(1.2).dash([5, 4]),
      line.horizontal(0).color(ASYMP).stroke(1.2).dash([5, 4]),
      legend([2.4, 2.28], tex`y_0 > 1\ \to\ \text{falls to 1}`, orange),
      legend([2.4, 1.16], tex`0 < y_0 < 1\ \to\ \text{rises to 1}`, blue),
    );
  const right = plot2d([-1.4, 2.4], [-1.7, 2.7], { size: [340, 460], axes: { x: { ticks: false }, y: { label: 'y' } }, grid: { alpha: 0.15 } })
    .title('phase line').add(
      line.vertical(0).color(gray).stroke(2),
      // y=0 (source): 위쪽 화살표는 1 쪽으로, 아래쪽 화살표는 0 에서 멀어진다
      annotate.arrow(point(0, 0.3), point(0, 0.75)).color(orange).stroke(2),
      annotate.arrow(point(0, -0.55), point(0, -1.05)).color(orange).stroke(2),
      // y=1 (sink): 위쪽에서 안쪽으로
      annotate.arrow(point(0, 1.7), point(0, 1.25)).color(blue).stroke(2),
      point(0, 0).dot({ open: true }).color(red).size(6),
      point(0, 1).dot().color(blue).size(6),
      annotate.text([0.2, -0.35]).label(tex`y = 0\ \text{unstable (source)}`).font(10).color(red).bold(),
      annotate.text([0.2, 1.12]).label(tex`y = 1\ \text{stable (sink)}`).font(10).color(blue).bold(),
    );
  return subplots([left, right], { cols: 2, tight: true, title: "Autonomous ODE y' = y(1−y) — Slope Field and Phase Line" });
}

// ══ 5. RL 회로 — 정상상태 접근 (단일) ══════════════════════════
//   L=4H, R=12Ω, E=60V → I' = 15−3I, I(t)=5(1−e^{−3t}), τ = L/R = 1/3 s (63.2% 도달)
function rlCircuit() {
  const I = (t) => 5 * (1 - Math.exp(-3 * t));
  const tau = 1 / 3;
  return plot2d([0, 2.5], [0, 5.8], { size: [760, 480], axes: AX('t (s)', 'I (A)'), grid: { alpha: 0.28 } })
    .title(tex`\text{RL Circuit --- } I(t) = 5\left(1 - e^{-3t}\right)`).add(
      curve.fn(I).on([0, 2.5]).color(blue).stroke(2.4),
      line.horizontal(5).color(ASYMP).stroke(1.3).dash([5, 4]),
      line.vertical(tau).color(red).stroke(1.2).dash([5, 4]),
      point(tau, 5 * (1 - Math.exp(-1))).dot().color(red).size(5),
      annotate.text([2.45, 5.2]).label(tex`\text{steady state}\;\; I = E/R = 5\,\mathrm{A}`).font(10.5).color(gray).anchor('end'),
      annotate.text([tau + 0.06, 0.9]).label(tex`\tau = L/R = 1/3\,\mathrm{s}`).font(10.5).color(red).bold(),
      annotate.text([tau + 0.09, 3.45]).label(tex`63.2\%\ \text{of}\ I_{\mathrm{ss}}`).font(10).color(red),
      legend([0.95, 2.1], tex`I(t) = 5(1 - e^{-3t})`, blue),
    );
}

// ══ 6. 오일러 방법 — 계단 vs 정확해 (단일) ═════════════════════
//   §9.2 #19: y'=y, y(0)=1. 오일러 계단(kit.seg) h=0.8/0.4 — h 가 절반이면
//   오차도 절반(A11 논의용). 내장 RK4(curve.ode)는 정확해 eˣ 위에 겹친다.
function eulerMethod() {
  const exact = (x) => Math.exp(x);
  const euler = (h, n) => {                 // 오일러 궤적의 꼭짓점들
    const pts = [[0, 1]];
    for (let i = 1; i <= n; i++) pts.push([i * h, pts[i - 1][1] * (1 + h)]);
    return pts;
  };
  const stair = (h, n, color) =>
    euler(h, n).slice(0, -1).map((p, i) =>
      segment(point(...p), point(...euler(h, n)[i + 1])).color(color).stroke(2));
  const p08 = euler(0.8, 2), p04 = euler(0.4, 4);
  return plot2d([0, 1.7], [0.9, 5.4], { size: [760, 480], axes: AX('x', 'y'), grid: { alpha: 0.28 } })
    .title("Euler's Method — y' = y,  y(0) = 1  (§9.2 #19)").add(
      curve.fn(exact).on([0, 1.7]).color(blue).stroke(2.4),
      curve.ode({ dy: (x, y) => y, y0: 1 }).on([0, 1.7]).color(red).stroke(1.4).dash([6, 4]),
      ...stair(0.8, 2, orange),
      ...stair(0.4, 4, green),
      point(1.6, exact(1.6)).dot().color(blue).size(4.5),
      point(1.6, p04[4][1]).dot().color(green).size(4),
      point(1.6, p08[2][1]).dot().color(orange).size(4),
      legend([0.06, 4.55], tex`\text{exact}\;\; y = e^{x}\ \ (e^{1.6} = 4.95)`, blue),
      legend([0.06, 4.1], tex`\text{RK4 (curve.ode)} \approx \text{exact}`, red),
      legend([0.06, 3.65], tex`\text{Euler } h = 0.4\ \to\ 3.84`, green),
      legend([0.06, 3.2], tex`\text{Euler } h = 0.8\ \to\ 3.24`, orange),
      annotate.text([0.06, 2.75]).label(tex`\text{halve } h \to \text{halve error (first-order)}`).font(10).color(gray),
    );
}

// ── figure 레지스트리 ───────────────────────────────────────────
export const figures = {
  '19a-1-slope-field': slopeField,
  '19a-2-growth-decay': growthDecay,
  '19a-3-logistic': logistic,
  '19a-4-phase-line': phaseLine,
  '19a-5-rl-circuit': rlCircuit,
  '19a-6-euler-method': eulerMethod,
};

