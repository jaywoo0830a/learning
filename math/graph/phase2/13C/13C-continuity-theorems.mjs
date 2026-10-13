// math/graph/phase2/13C/13C-continuity-theorems.mjs — 세션 13C(연속성·정리) 그림
//
// ── figure 목록 (키 = 출력 파일명 = 마크다운 태그 id) ──────────────
//    13c-1-discontinuities    불연속 3종 — 제거가능 / 도약 / 무한        (§2.5 Ex 2)
//    13c-2-squeeze            x² sin(1/x) 압착                          (§2.3 Ex 11)
//    13c-3-ivt                중간값 정리 — 4x³−6x²+3x−2 의 근          (§2.5 Ex 10)
//    13c-4-continuity-interval  1−√(1−x²) 는 [−1,1] 에서 연속            (§2.5 Ex 4)
//    13c-5-piecewise          조각함수를 이어 붙여 연속으로 만들기        (§2.5)
//
// ── 코어 API (기준 @jaywoo0830a/logos 0.5.1) ────────────────────────
import { annotate, curve, kit, line, point, tex } from '@jaywoo0830a/logos';

const { plot2d, subplots, palette } = kit;
const { blue, red, green, purple, orange, gray } = palette.tab;
const FAINT = '#dddddd', ASYMP = '#bbbbbb';
const AX = () => ({ x: { label: 'x' }, y: { label: 'y' } });
const panel = (xr, yr, size = [440, 400]) =>
  plot2d(xr, yr, { size, axes: AX(), grid: { alpha: 0.3 } });
const hole = (x, y, color) => point(x, y).dot({ open: true }).color(color).size(6.5);
const dot = (x, y, color) => point(x, y).dot().color(color).size(5.5);
const legend = (at, text, color, font = 11) =>
  annotate.text(at).label(text).font(font).color(color).bold();

// ══ 1. 불연속 3종 ════════════════════════════════════════════════
function discontinuities() {
  const a = panel([-1.5, 4], [-1, 5]).title(tex`\text{(a) removable — hole at } (1,2)`).add(
    curve.fn((x) => x + 1).on([-1.5, 0.97]).color(blue).stroke(2.4).n(120),
    curve.fn((x) => x + 1).on([1.03, 4]).color(blue).stroke(2.4).n(120),
    line.vertical(1).color(FAINT).stroke(1).dash([3, 3]),
    hole(1, 2, blue),
  );
  const b = panel([-2.5, 3.5], [-3, 3.5]).title(tex`\text{(b) jump — } \lfloor x\rfloor`).add(
    curve.fn(() => -2).on([-2, -1]).color(red).stroke(2.6).n(20),
    curve.fn(() => -1).on([-1, 0]).color(red).stroke(2.6).n(20),
    curve.fn(() => 0).on([0, 1]).color(red).stroke(2.6).n(20),
    curve.fn(() => 1).on([1, 2]).color(red).stroke(2.6).n(20),
    curve.fn(() => 2).on([2, 3]).color(red).stroke(2.6).n(20),
    dot(-1, -1, red), dot(0, 0, red), dot(1, 1, red), dot(2, 2, red),
    hole(-1, -2, red), hole(0, -1, red), hole(1, 0, red), hole(2, 1, red),
    annotate.text([1.06, 0.55]).label(tex`\text{jump at } x=1`).font(10).color(red),
  );
  const c = panel([-3, 3], [-6, 6]).title(tex`\text{(c) infinite — } \frac{1}{x}`).add(
    curve.fn((x) => 1 / x).on([-3, -0.16]).color(purple).stroke(2.4).n(300),
    curve.fn((x) => 1 / x).on([0.16, 3]).color(purple).stroke(2.4).n(300),
    line.vertical(0).color(ASYMP).stroke(1.1).dash([5, 5]),
    line.horizontal(0).color(gray).stroke(0.5),
    annotate.text([0.1, 4.6]).label(tex`\pm\infty`).font(11).color(purple),
  );
  return subplots([a, b, c], { cols: 3, tight: true, title: 'Three Types of Discontinuity' });
}

// ══ 2. 압착 정리 — x² sin(1/x) ════════════════════════════════════
function squeeze() {
  const g = (x) => x * x * Math.sin(1 / x);
  return panel([-0.65, 0.65], [-0.5, 0.5]).title(tex`\lim_{x\to 0} x^{2}\sin\tfrac{1}{x} = 0`).add(
    curve.fn(g).on([-0.6, -0.001]).color(red).stroke(1.6).n(1200),
    curve.fn(g).on([0.001, 0.6]).color(red).stroke(1.6).n(1200),
    curve.fn((x) => x * x).on([-0.6, 0.6]).color(blue).stroke(1.8).n(200),
    curve.fn((x) => -x * x).on([-0.6, 0.6]).color(blue).stroke(1.8).n(200),
    line.horizontal(0).color(gray).stroke(0.5),
    hole(0, 0, red),
    legend([-0.62, 0.42], tex`\pm x^{2}`, blue, 11),
    annotate.text([0.3, 0.08]).label(tex`x^{2}\sin\tfrac{1}{x}`).font(10).color(red),
  );
}

// ══ 3. 중간값 정리 — 4x³−6x²+3x−2 ════════════════════════════════
function ivt() {
  const f = (x) => 4 * x ** 3 - 6 * x * x + 3 * x - 2;
  return panel([0.6, 2.4], [-3, 14]).title(tex`4x^{3}-6x^{2}+3x-2 = 0 \;\text{on}\; (1,2)`).add(
    curve.fn(f).on([0.6, 2.4]).color(blue).stroke(2.6).n(300),
    line.horizontal(0).color(gray).stroke(1),
    dot(1, -1, red), dot(2, 12, green), dot(1.2226, 0, purple),
    annotate.text([1, -1]).label(tex`f(1) = -1 < 0`).font(11).color(red).offset(4, -14),
    annotate.text([2, 12]).label(tex`f(2) = 12 > 0`).font(11).color(green).anchor('end').offset(-4, 4),
    annotate.text([1.2226, 0]).label(tex`\text{root } c \approx 1.22`).font(10).color(purple).offset(6, -14),
  );
}

// ══ 4. 닫힌구간에서 연속 — 1−√(1−x²) ═════════════════════════════
function continuityInterval() {
  const f = (x) => 1 - Math.sqrt(1 - x * x);
  return panel([-1.4, 1.4], [-0.4, 1.4]).title(tex`f(x) = 1-\sqrt{1-x^{2}} \;\text{on}\; [-1,1]`).add(
    curve.fn(f).on([-1, 1]).color(orange).stroke(2.8).n(400),
    line.vertical(-1).color(FAINT).stroke(1).dash([3, 3]),
    line.vertical(1).color(FAINT).stroke(1).dash([3, 3]),
    dot(-1, 1, orange), dot(1, 1, orange), dot(0, 0, orange),
    annotate.text([-1, 1]).label(tex`(-1,1)`).font(10).color(orange).anchor('end').offset(-4, 10),
    annotate.text([1, 1]).label(tex`(1,1)`).font(10).color(orange).offset(4, 10),
    annotate.text([0, 0]).label(tex`\text{min } (0,0)`).font(10).color(orange).offset(6, -14),
  );
}

// ══ 5. 조각함수 — 이어 붙이기 ═════════════════════════════════════
function piecewise() {
  const left = (x) => x * x + 1;   // x<1
  const right = (x) => 2 * x;      // x>=1
  return panel([-1, 3.2], [-0.5, 6]).title(tex`f(x)=\begin{cases}x^{2}+1 & x<1\\ 2x & x\geq 1\end{cases}`).add(
    curve.fn(left).on([-1, 0.97]).color(blue).stroke(2.6).n(160),
    curve.fn(right).on([1, 3.2]).color(red).stroke(2.6).n(160),
    line.vertical(1).color(FAINT).stroke(1).dash([3, 3]),
    hole(1, 2, blue), dot(1, 2, red),
    annotate.text([1, 2]).label(tex`f(1)=2 \;\text{— continuous}`).font(11).color(green).bold().offset(8, 8),
  );
}

// ── figure 레지스트리 ──────────────────────────────────────────────
export const figures = {
  '13c-1-discontinuities': discontinuities,
  '13c-2-squeeze': squeeze,
  '13c-3-ivt': ivt,
  '13c-4-continuity-interval': continuityInterval,
  '13c-5-piecewise': piecewise,
};

