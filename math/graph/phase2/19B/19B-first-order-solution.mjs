// math/graph/phase2/19B/19B-first-order-solution.mjs — 세션 19B(1계 ODE 풀이법) 그림
//
// ── figure 목록 (키 = 출력 파일명 = 마크다운 태그 id) ──────────────
//    19b-1-separable-family    분리해의 묵시적 해족: y²=x²+C 쌍곡선 / y³=x³+C 3차 (§9.3 Ex 1·Ex 7)
//    19b-2-integrating-factor  적분인자 해의 transient vs steady: ½e⁻ˣ+Ce⁻³ˣ (§9.5 Ex 5)
//    19b-3-mixing              혼합 문제: 고정 부피 A→200g / 가변 부피 A vs V (§9.3 Ex 13·Ex 16)
//    19b-4-interval-validity   해의 존재 구간: y=1/(1−x) 가 x=1 에서 발산 (§9.3)
//
// ── 코어 API (기준 @jaywoo0830a/logos 0.4.1) ─────────────────────
//   곡선 = `curve.fn(f).on([a,b])` · 기준선 = `line.horizontal/vertical`
//   영역 셰이딩 = `region.betweenX(f, g, domain)` (fill_betweenx — 수직 스트립)
//   점 = `point().dot()` · 라벨 = `annotate.text` — 플러그인 없이 코어만으로 충분.
import { annotate, curve, kit, line, point, region } from '@jaywoo0830a/logos';

const { plot2d, subplots, palette } = kit;
const { blue, green, orange, red, purple, gray } = palette.tab;
const LIGHT = '#bbbbbb', ASYMP = '#cccccc';   // 지면 톤(팔레트 밖)

/** 축 설정 — 코어 plot2d 의 axes 옵션 그대로 */
const AX = (x, y) => ({ x: { label: x }, y: { label: y } });

/** 범례 대신 같은 색 라벨 (코어 annotate.text 체이닝의 1줄 별칭 — 이 파일 안에서만) */
const legend = (at, text, color, font = 10.5, anchor = 'start') =>
  annotate.text(at).label(text).font(font).color(color).bold().anchor(anchor);

// ══ 1. 분리해의 묵시적 해족 (1×2) ═══════════════════════════════
//   왼쪽: y² = x² + C 쌍곡선족 — §9.3 Ex 7: y(0)=−3 → C=9, 음의 근 선택
//   오른쪽: y³ = x³ + C — §9.3 Ex 1: y(0)=2 → C=8
function separableFamily() {
  const left = plot2d([-4, 4], [-5.5, 5.5], { size: [520, 440], axes: AX('x', 'y'), grid: { alpha: 0.25 } })
    .title('implicit family  y² = x² + C').add(
      // 다른 해족 원본들 (C = 1, −4) — 회색
      curve.fn((x) => Math.sqrt(x * x + 1)).on([-4, 4]).color(LIGHT).stroke(1.3),
      curve.fn((x) => -Math.sqrt(x * x + 1)).on([-4, 4]).color(LIGHT).stroke(1.3),
      curve.fn((x) => Math.sqrt(x * x - 4)).on([-4, -2]).color(LIGHT).stroke(1.3),
      curve.fn((x) => Math.sqrt(x * x - 4)).on([2, 4]).color(LIGHT).stroke(1.3),
      curve.fn((x) => -Math.sqrt(x * x - 4)).on([-4, -2]).color(LIGHT).stroke(1.3),
      curve.fn((x) => -Math.sqrt(x * x - 4)).on([2, 4]).color(LIGHT).stroke(1.3),
      // C = 9 — 윗 가지(점선, IC 와 불일치)와 아랫 가지(우리 해)
      curve.fn((x) => Math.sqrt(x * x + 9)).on([-4, 4]).color(red).stroke(1.4).dash([5, 4]),
      curve.fn((x) => -Math.sqrt(x * x + 9)).on([-4, 4]).color(red).stroke(2.4),
      point(0, -3).dot().color(purple).size(5),
      legend([-3.8, 5.1], 'C = 1, −4', gray, 10),
      legend([-3.8, -4.8], 'C = 9: y = −√(x²+9)', red),
    );
  const right = plot2d([-3, 3], [-3.5, 3.5], { size: [520, 440], axes: AX('x', 'y'), grid: { alpha: 0.25 } })
    .title('family  y³ = x³ + C').add(
      curve.fn((x) => Math.cbrt(x ** 3 - 8)).on([-3, 3]).color(LIGHT).stroke(1.3),
      curve.fn((x) => x).on([-3, 3]).color(LIGHT).stroke(1.3),
      curve.fn((x) => Math.cbrt(x ** 3 + 8)).on([-3, 3]).color(blue).stroke(2.4),
      point(0, 2).dot().color(purple).size(5),
      legend([-2.8, 3.1], 'C = 0, −8', gray, 10),
      legend([-2.8, -3.15], 'C = 8: y = ∛(x³+8)', blue),
    );
  return subplots([left, right], { cols: 2, tight: true, title: 'Separable ODEs — Implicit Solution Families' });
}

// ══ 2. 적분인자 — transient vs steady (단일) ════════════════════
//   §9.5 Ex 5: y' + 3y = e⁻ˣ → y = ½e⁻ˣ + Ce⁻³ˣ. C 와 무관하게 steady ½e⁻ˣ 로 수렴.
function integratingFactor() {
  const steady = (x) => 0.5 * Math.exp(-x);
  const sol = (x, C) => steady(x) + C * Math.exp(-3 * x);
  return plot2d([0, 3], [-0.25, 2.7], { size: [760, 480], axes: AX('x', 'y'), grid: { alpha: 0.28 } })
    .title("Integrating Factor — y' + 3y = e⁻ˣ  (§9.5 #5)").add(
      curve.fn((x) => sol(x, 2)).on([0, 3]).color(blue).stroke(2.2),
      curve.fn((x) => sol(x, 0.8)).on([0, 3]).color(green).stroke(2.2),
      curve.fn((x) => sol(x, -0.4)).on([0, 3]).color(orange).stroke(2.2),
      curve.fn(steady).on([0, 3]).color(red).stroke(1.6).dash([5, 4]),
      legend([0.15, 2.38], 'C = 2', blue),
      legend([0.42, 1.05], 'C = 0.8', green),
      legend([0.72, 0.44], 'C = −0.4', orange),
      legend([1.95, 0.33], 'steady ½e⁻ˣ', red),
      annotate.text([1.35, 1.75]).label('transient  Ce⁻³ˣ → 0').font(10).color(gray),
    );
}

// ══ 3. 혼합 문제 — 고정 vs 가변 부피 (1×2) ══════════════════════
//   왼쪽: §9.3 Ex 13 — A = 200 − 170e^(−t/50) → 200 g (정상상태 = 유입 농도)
//   오른쪽: §9.3 Ex 16 — 가변 부피 A = (100+t) − 700000/(100+t)², V = 100+t
function mixing() {
  const A1 = (t) => 200 - 170 * Math.exp(-t / 50);
  const left = plot2d([0, 250], [0, 220], { size: [520, 440], axes: AX('t (min)', 'A (g)'), grid: { alpha: 0.28 } })
    .title('fixed volume — A → 200 g').add(
      curve.fn(A1).on([0, 250]).color(blue).stroke(2.4),
      line.horizontal(200).color(ASYMP).stroke(1.2).dash([5, 4]),
      point(0, 30).dot().color(purple).size(4.5),
      annotate.text([245, 207]).label('steady state = inflow 1 g/L × 200 L').font(10).color(gray).anchor('end'),
      legend([35, 70], 'A(t) = 200 − 170e^(−t/50)', blue),
    );
  const A2 = (t) => 100 + t - 700000 / (100 + t) ** 2;
  const V = (t) => 100 + t;
  const right = plot2d([0, 120], [0, 240], { size: [520, 440], axes: AX('t (min)', 'A, V'), grid: { alpha: 0.28 } })
    .title('variable volume (§9.3 Ex 16)').add(
      curve.fn(V).on([0, 120]).color(ASYMP).stroke(1.4).dash([5, 4]),
      curve.fn(A2).on([0, 120]).color(green).stroke(2.4),
      point(0, 30).dot().color(purple).size(4.5),
      legend([72, 200], 'V(t) = 100 + t', gray),
      legend([52, 128], 'A(t) = (100+t) − 700000/(100+t)²', green),
      annotate.text([58, 32]).label('concentration A/V → 1 g/L').font(10).color(green).bold(),
    );
  return subplots([left, right], { cols: 2, tight: true, title: 'Mixing — Fixed vs Variable Volume' });
}

// ══ 4. 해의 존재 구간 — 유한 시간 발산 (단일) ═══════════════════
//   y' = y², y(0)=1 → y = 1/(1−x). x=1 에서 발산 — 해의 구간은 (−∞, 1).
//   x > 1 의 가지는 같은 공식이지만 IVP 의 해가 아닌 별개 해.
function intervalValidity() {
  const y = (x) => 1 / (1 - x);
  return plot2d([-1.5, 2.5], [-4.5, 5.5], { size: [760, 480], axes: AX('x', 'y'), grid: { alpha: 0.28 } })
    .title("Interval of Validity — y' = y²,  y(0) = 1  →  y = 1/(1 − x)").add(
      region.betweenX(() => -1.5, () => 1, [-4.5, 5.5]).fill(blue).opacity(0.06),
      curve.fn(y).on([-1.5, 0.93]).color(blue).stroke(2.4),
      curve.fn(y).on([1.07, 2.5]).color(LIGHT).stroke(1.6).dash([6, 4]),
      line.vertical(1).color(red).stroke(1.3).dash([5, 4]),
      point(0, 1).dot().color(purple).size(5),
      annotate.text([1.12, 4.7]).label('blow-up at x = 1').font(10.5).color(red).bold(),
      annotate.text([-1.35, 5.0]).label('valid on (−∞, 1)').font(10.5).color(blue).bold(),
      annotate.text([1.25, -3.7]).label('x > 1: separate branch — not our solution').font(10).color(gray),
    );
}

// ── figure 레지스트리 ───────────────────────────────────────────
export const figures = {
  '19b-1-separable-family': separableFamily,
  '19b-2-integrating-factor': integratingFactor,
  '19b-3-mixing': mixing,
  '19b-4-interval-validity': intervalValidity,
};

