// math/graph/phase2/13B/13B-limits-at-infinity.mjs — 세션 13B(무한에서의 극한) 그림
//
// ── figure 목록 (키 = 출력 파일명 = 마크다운 태그 id) ──────────────
//    13b-1-horizontal-asymptote  (x²−1)/(x²+1) → 1, 수평점근선          (§2.6 Fig 1)
//    13b-2-degree-cases          차수 비교 3종: deg> / deg= / deg<        (§2.6 Ex 3)
//    13b-3-radical-asymptotes    √(2x²+1)/(3x−5) → ±√2/3 (두 점근선)      (§2.6 Ex 4)
//    13b-4-growth-race           eˣ vs x³ — 지수는 다항식을 앞지른다       (§2.6 Fig 12)
//    13b-5-vertical-asymptote    1/(x−2) — 분모→0 의 부호 추적             (§2.2 Ex 29–30)
//
// ── 코어 API (기준 @jaywoo0830a/logos 0.5.1) ────────────────────────
import { annotate, curve, kit, line, point, tex } from '@jaywoo0830a/logos';

const { plot2d, subplots, palette } = kit;
const { blue, red, green, purple, orange, gray } = palette.tab;
const FAINT = '#dddddd', ASYMP = '#bbbbbb';
const AX = () => ({ x: { label: 'x' }, y: { label: 'y' } });
const panel = (xr, yr, size = [440, 400]) =>
  plot2d(xr, yr, { size, axes: AX(), grid: { alpha: 0.3 } });
const legend = (at, text, color, font = 11) =>
  annotate.text(at).label(text).font(font).color(color).bold();
/** 점근선(수평/수직) — 회색 점선 */
const asympV = (x) => line.vertical(x).color(ASYMP).stroke(1.2).dash([5, 5]);
const asympH = (y) => line.horizontal(y).color(ASYMP).stroke(1.2).dash([5, 5]);

// ══ 1. 수평점근선 — (x²−1)/(x²+1) → 1 ═════════════════════════════
function horizontalAsymptote() {
  const f = (x) => (x * x - 1) / (x * x + 1);
  return panel([-9, 9], [-1.4, 1.4]).title(tex`\lim_{x\to\pm\infty}\frac{x^{2}-1}{x^{2}+1} = 1`).add(
    curve.fn(f).on([-9, 9]).color(blue).stroke(2.6).n(600),
    asympH(1),
    line.horizontal(0).color(gray).stroke(0.5),
    legend([-8.6, 1.2], tex`y = 1`, gray, 11),
    annotate.text([8.6, 1]).label(tex`\text{horizontal asymptote}`).font(10).color(gray).anchor('end').offset(0, 12),
  );
}

// ══ 2. 차수 비교 3종 ══════════════════════════════════════════════
function degreeCases() {
  const p1 = panel([0, 12], [-20, 80]).title(tex`\deg(\text{num}) > \deg(\text{den}) \to \infty`).add(
    curve.fn((x) => (2 * x * x * x - x) / (x * x + 4)).on([0.5, 12]).color(red).stroke(2.4).n(400),
    legend([0.6, 62], tex`\frac{2x^{3}-x}{x^{2}+4}`, red, 11),
  );
  const p2 = panel([0, 12], [-1, 6]).title(tex`\deg(\text{num}) = \deg(\text{den}) \to \text{ratio}`).add(
    curve.fn((x) => (3 * x * x + 2 * x - 1) / (x * x + 5)).on([0.5, 12]).color(blue).stroke(2.4).n(400),
    asympH(3),
    legend([0.6, 4.4], tex`\frac{3x^{2}+2x-1}{x^{2}+5} \to 3`, blue, 11),
  );
  const p3 = panel([0, 12], [-1, 3]).title(tex`\deg(\text{num}) < \deg(\text{den}) \to 0`).add(
    curve.fn((x) => (x * x + 1) / (x * x * x - 2)).on([1.3, 12]).color(green).stroke(2.4).n(400),
    asympH(0),
    legend([0.6, 2.2], tex`\frac{x^{2}+1}{x^{3}-2} \to 0`, green, 11),
  );
  return subplots([p1, p2, p3], { cols: 3, tight: true, title: 'Degree Comparison for Rational Functions' });
}

// ══ 3. 근호와 두 수평점근선 — √(2x²+1)/(3x−5) ════════════════════
function radicalAsymptotes() {
  const f = (x) => Math.sqrt(2 * x * x + 1) / (3 * x - 5);
  const y0 = Math.SQRT2 / 3;
  return panel([-14, 14], [-1.4, 1.4]).title(tex`\frac{\sqrt{2x^{2}+1}}{3x-5}`).add(
    curve.fn(f).on([-14, -0.2]).color(purple).stroke(2.4).n(500),
    curve.fn(f).on([2.2, 14]).color(purple).stroke(2.4).n(500),
    asympH(y0), asympH(-y0), asympV(5 / 3),
    legend([-13.6, 0.62], tex`y = \tfrac{\sqrt{2}}{3}`, gray, 10),
    legend([-13.6, -0.72], tex`y = -\tfrac{\sqrt{2}}{3}`, gray, 10),
    annotate.text([0, -1.15]).label(tex`\sqrt{x^{2}} = |x| = -x \;\;(x<0)`).font(10).color(purple).anchor('middle'),
  );
}

// ══ 4. 성장 경주 — eˣ vs x³ ═══════════════════════════════════════
function growthRace() {
  return panel([-1, 4.4], [0, 70]).title(tex`e^{x} \;\text{grows faster than}\; x^{3}`).add(
    curve.fn(Math.exp).on([-1, 4.2]).color(red).stroke(2.6).n(400),
    curve.fn((x) => x * x * x).on([-1, 4.2]).color(blue).stroke(2.4).n(400),
    line.horizontal(0).color(gray).stroke(0.5),
    legend([2.0, 60], tex`y = e^{x}`, red, 12),
    legend([2.9, 26], tex`y = x^{3}`, blue, 12),
    point(3.5, Math.exp(3.5)).dot().color(red).size(4),
    annotate.text([3.5, Math.exp(3.5)]).label(tex`e^{x} \gg x^{3}`).font(10).color(red).anchor('end').offset(-8, 0),
  );
}

// ══ 5. 수직점근선 — 1/(x−2) 의 부호 추적 ══════════════════════════
function verticalAsymptote() {
  const f = (x) => 1 / (x - 2);
  return panel([-4, 8], [-6, 6]).title(tex`\lim_{x\to 2^{\pm}}\frac{1}{x-2}`).add(
    curve.fn(f).on([-4, 1.7]).color(blue).stroke(2.4).n(400),
    curve.fn(f).on([2.3, 8]).color(blue).stroke(2.4).n(400),
    asympV(2),
    line.horizontal(0).color(gray).stroke(0.5),
    annotate.text([1.85, 4]).label(tex`x\to 2^{-}\!:\, -\infty`).font(11).color(red).anchor('end'),
    annotate.text([2.15, 4]).label(tex`x\to 2^{+}\!:\, +\infty`).font(11).color(green),
    annotate.text([5, -4.6]).label(tex`\text{vertical asymptote } x = 2`).font(10).color(gray).anchor('middle'),
  );
}

// ── figure 레지스트리 ──────────────────────────────────────────────
export const figures = {
  '13b-1-horizontal-asymptote': horizontalAsymptote,
  '13b-2-degree-cases': degreeCases,
  '13b-3-radical-asymptotes': radicalAsymptotes,
  '13b-4-growth-race': growthRace,
  '13b-5-vertical-asymptote': verticalAsymptote,
};
