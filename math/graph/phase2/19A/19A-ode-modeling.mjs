// math/graph/phase2/19A/19A-ode-modeling.mjs — 세션 19A(ODE 모델링 입문) 그림
//
// ── figure 목록 (키 = 출력 파일명 = 마크다운 태그 id) ──────────────
//    19a-1-slope-field       기울기장 y'=x+y(§9.1 예제) + y'=y-2x 해곡선(§9.2 #11)
//    19a-2-growth-decay      지수 모델 Ae^{kt}: 성장(k>0, 배가시간) vs 감쇠(k<0, 반감기)
//    19a-3-logistic          로지스틱 S-곡선 + 초기 지수 근사 + 변곡점 P=L/2
//    19a-4-phase-line        자율 ODE y'=y(1-y): 기울기장 + 위상선(source/sink)
//    19a-5-rl-circuit        RL 회로 I(t)=5(1-e^{-3t}) → 정상상태 5A, 시정수 τ=1/3
//
// ── 코어 API (기준 @jaywoo0830a/logos 0.4.1) ─────────────────────
//   기울기장 = 코어 `vectorField((x,y)=>[1,f])` (docs/testing/TEXTBOOK.md #48)
//   곡선 = `curve.fn(f).on([a,b])` · 기준선 = `line.horizontal/vertical`
//   화살표 = `annotate.arrow(A,B)` · 점 = `point(x,y).dot({open})`
//   18A의 polyline/stem 플러그인이 필요 없다 — 코어 빌더만으로 충분.
import { annotate, curve, kit, line, point, vectorField } from '@jaywoo0830a/logos';

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
      legend([0.2, 3.5], 'y = −x−1+Ceˣ  (C=1,2)', blue),
      legend([0.2, 2.8], 'nullcline y = −x−1', gray),
    );
  const right = plot2d([-2, 3], [-6, 6], { size: [520, 420], axes: AX('x', 'y'), grid: { alpha: 0.25 } })
    .title("y' = y − 2x  — §9.2 #11, through (1,0)").add(
      vectorField((x, y) => [1, y - 2 * x]).step(0.5).len(0.36).color(LIGHT).stroke(1.1),
      curve.fn((x) => 2 * x).on([-2, 3]).color(gray).stroke(1.4).dash([5, 4]),
      curve.fn((x) => 2 * x + 2 - 4 * Math.exp(x - 1)).on([-2, 2.15]).color(red).stroke(2.2),
      point(1, 0).dot().color(purple).size(4.5),
      legend([-1.8, 5.2], 'solution  y = 2x+2−4eˣ⁻¹', red),
      legend([-1.8, 4.4], 'nullcline y = 2x', gray),
    );
  return subplots([left, right], { cols: 2, tight: true, title: 'Slope Fields and Solution Curves' });
}

// ══ 2. 지수 모델 — 성장 vs 감쇠 (1×2) ═══════════════════════════
//   왼쪽: k>0 성장 — 배가시간 t₂ = ln2/k 는 모든 곡선에서 같은 수평 거리
//   오른쪽: k<0 감쇠 — 반감기 t½ = ln2/|k|
function growthDecay() {
  const LN2 = Math.LN2;
  const left = plot2d([0, 3], [0, 4.2], { size: [520, 420], axes: AX('t', 'P'), grid: { alpha: 0.28 } })
    .title('Growth:  P = Aeᵏᵗ,  k > 0').add(
      curve.fn((t) => Math.exp(0.5 * t)).on([0, 3]).color(blue).stroke(2.2),
      curve.fn((t) => Math.exp(t)).on([0, 1.45]).color(orange).stroke(2.2),
      curve.fn((t) => 0.6 * Math.exp(t)).on([0, 1.85]).color(green).stroke(2.2),
      line.vertical(LN2).color(red).stroke(1.2).dash([5, 4]),
      line.horizontal(2).color(red).stroke(1.2).dash([5, 4]),
      point(LN2, 2).dot().color(red).size(4),
      legend([1.65, 3.95], 'e^(t/2)', blue),
      legend([1.65, 3.45], 'eᵗ ,  0.6eᵗ', orange),
      annotate.text([LN2 + 0.1, 0.25]).label('t₂ = ln 2 / k').font(10).color(red).bold(),
    );
  const right = plot2d([0, 4], [0, 1.2], { size: [520, 420], axes: AX('t', 'P'), grid: { alpha: 0.28 } })
    .title('Decay:  P = Aeᵏᵗ,  k < 0').add(
      curve.fn((t) => Math.exp(-0.5 * t)).on([0, 4]).color(blue).stroke(2.2),
      curve.fn((t) => Math.exp(-t)).on([0, 4]).color(orange).stroke(2.2),
      line.vertical(LN2).color(red).stroke(1.2).dash([5, 4]),
      line.horizontal(0.5).color(red).stroke(1.2).dash([5, 4]),
      point(LN2, 0.5).dot().color(red).size(4),
      legend([2.3, 1.05], 'e^(−t/2)', blue),
      legend([2.3, 0.85], 'e⁻ᵗ', orange),
      annotate.text([LN2 + 0.1, 0.1]).label('t½ = ln 2 / |k|').font(10).color(red).bold(),
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
    .title('Logistic Growth  —  L = 1000,  P₀ = 100').add(
      curve.fn(P).on([0, 10]).color(blue).stroke(2.4),
      curve.fn((t) => P0 * Math.exp(k * t)).on([0, 2.05]).color(red).stroke(1.6).dash([5, 4]),
      line.horizontal(L).color(ASYMP).stroke(1.3).dash([5, 4]),
      line.horizontal(L / 2).color(gray).stroke(1).dash([4, 4]).opacity(0.7),
      line.vertical(tInf).color(gray).stroke(1).dash([4, 4]).opacity(0.7),
      point(tInf, L / 2).dot().color(red).size(5),
      annotate.text([9.9, 1065]).label('carrying capacity L = 1000').font(10.5).color(gray).anchor('end'),
      annotate.text([tInf + 0.15, 585]).label('inflection: P = L/2 (fastest growth)').font(10).color(red).bold(),
      legend([0.55, 950], 'P₀eᵏᵗ  (early exponential approx)', red),
      legend([0.55, 865], 'P(t) = L / (1 + Ae⁻ᵏᵗ)', blue),
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
      legend([2.4, 2.28], 'y₀ > 1 → falls to 1', orange),
      legend([2.4, 1.16], '0 < y₀ < 1 → rises to 1', blue),
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
      annotate.text([0.2, -0.35]).label('y = 0 unstable (source)').font(10).color(red).bold(),
      annotate.text([0.2, 1.12]).label('y = 1 stable (sink)').font(10).color(blue).bold(),
    );
  return subplots([left, right], { cols: 2, tight: true, title: "Autonomous ODE y' = y(1−y) — Slope Field and Phase Line" });
}

// ══ 5. RL 회로 — 정상상태 접근 (단일) ══════════════════════════
//   L=4H, R=12Ω, E=60V → I' = 15−3I, I(t)=5(1−e^{−3t}), τ = L/R = 1/3 s (63.2% 도달)
function rlCircuit() {
  const I = (t) => 5 * (1 - Math.exp(-3 * t));
  const tau = 1 / 3;
  return plot2d([0, 2.5], [0, 5.8], { size: [760, 480], axes: AX('t (s)', 'I (A)'), grid: { alpha: 0.28 } })
    .title('RL Circuit  —  I(t) = 5(1 − e⁻³ᵗ)').add(
      curve.fn(I).on([0, 2.5]).color(blue).stroke(2.4),
      line.horizontal(5).color(ASYMP).stroke(1.3).dash([5, 4]),
      line.vertical(tau).color(red).stroke(1.2).dash([5, 4]),
      point(tau, 5 * (1 - Math.exp(-1))).dot().color(red).size(5),
      annotate.text([2.45, 5.2]).label('steady state  I = E/R = 5 A').font(10.5).color(gray).anchor('end'),
      annotate.text([tau + 0.06, 0.9]).label('τ = L/R = 1/3 s').font(10.5).color(red).bold(),
      annotate.text([tau + 0.09, 3.45]).label('63.2% of Iₛₛ').font(10).color(red),
      legend([0.95, 2.1], 'I(t) = 5(1 − e⁻³ᵗ)', blue),
    );
}

// ── figure 레지스트리 ───────────────────────────────────────────
export const figures = {
  '19a-1-slope-field': slopeField,
  '19a-2-growth-decay': growthDecay,
  '19a-3-logistic': logistic,
  '19a-4-phase-line': phaseLine,
  '19a-5-rl-circuit': rlCircuit,
};

