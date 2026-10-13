// math/graph/phase2/13A/13A-algebraic-limits.mjs — 세션 13A(대수적 극한 · 0/0 툴킷) 그림
//
// ── figure 목록 (키 = 출력 파일명 = 마크다운 태그 id) ──────────────
//    13a-1-hole           (x²−4)/(x−2) — x=2 의 구멍, 극한값 4        (Stewart §2.3 Ex 3)
//    13a-2-conjugate      (√(x+4)−2)/x — 켤레로 뚫은 구멍 1/4          (§2.3 Ex 6)
//    13a-3-sinx-over-x    sin x / x → 1 — 삼각 표준극한               (§2.2 Ex 2)
//    13a-4-onesided       |x|/x — 좌우가 달라 극한이 없다              (§2.3 Ex 8)
//    13a-5-squeeze        x² sin(1/x) — −x²·x² 사이에 압착            (§2.3 Ex 11)
//    13a-6-complex-fraction  (1/x−1/3)/(x−3) = −1/(3x), 구멍 (3,−1/9)
//
// ── 코어 API 만 쓴다 (기준 @jaywoo0830a/logos 0.5.1) ────────────────
//   곡선 curve.fn(f).on(dom) · 기준선 line.vertical/horizontal · 마커 point(x,y).dot({open})
//   영역 region.between · 라벨 annotate.text([x,y]).label() · 색 kit.palette.tab
import { annotate, curve, kit, line, point, region, tex } from '@jaywoo0830a/logos';

const { plot2d, subplots, palette } = kit;
const { blue, red, green, purple, orange, gray } = palette.tab;
const FAINT = '#dddddd', ASYMP = '#bbbbbb';
const AX = () => ({ x: { label: 'x' }, y: { label: 'y' } });

/** 표준 1×1 패널 */
const panel = (xr, yr, size = [440, 400]) =>
  plot2d(xr, yr, { size, axes: AX(), grid: { alpha: 0.3 } });

/** 열린 점 = 구멍(hole) 표시 */
const hole = (x, y, color) => point(x, y).dot({ open: true }).color(color).size(6.5);

/** 범례 대신 같은 색 라벨 */
const legend = (at, text, color, font = 11) =>
  annotate.text(at).label(text).font(font).color(color).bold();

// ══ 1. 0/0 의 구멍 — (x²−4)/(x−2) ═════════════════════════════════
//   x≠2 에서 x+2. x=2 에서만 값이 없으므로 그 자리에 구멍이 뚫린다.
function holeGraph() {
  const f = (x) => (x * x - 4) / (x - 2);
  return panel([-1, 5], [-1, 8]).title(tex`\frac{x^{2}-4}{x-2} = x+2 \;\;(x \neq 2)`).add(
    curve.fn(f).on([-1, 1.97]).color(blue).stroke(2.6).n(240),
    curve.fn(f).on([2.03, 5]).color(blue).stroke(2.6).n(240),
    line.vertical(2).color(ASYMP).stroke(1.1).dash([5, 5]),
    hole(2, 4, blue),
    annotate.text([2, 4]).label(tex`\text{hole } (2,\ 4)`).font(11).color(blue).bold().offset(8, 6),
    annotate.text([4.6, 3.4]).label(tex`\lim_{x\to 2} = 4`).font(12).color(red).anchor('end'),
  );
}

// ══ 2. 켤레로 뚫은 구멍 — (√(x+4)−2)/x ════════════════════════════
//   분모의 √ 를 없애면 1/(√(x+4)+2). x=0 에서 구멍, 극한값 1/4.
function conjugateGraph() {
  const f = (x) => (Math.sqrt(x + 4) - 2) / x;
  return panel([-4, 6], [-0.1, 0.6]).title(tex`\frac{\sqrt{x+4}-2}{x} \;\to\; \frac{1}{4}`).add(
    curve.fn(f).on([-3.98, -0.02]).color(purple).stroke(2.6).n(240),
    curve.fn(f).on([0.02, 6]).color(purple).stroke(2.6).n(240),
    line.vertical(0).color(ASYMP).stroke(1.1).dash([5, 5]),
    line.horizontal(0.25).color(FAINT).stroke(1).dash([2, 3]),
    hole(0, 0.25, purple),
    annotate.text([0, 0.25]).label(tex`\text{hole } (0,\ \tfrac14)`).font(11).color(purple).bold().offset(8, 8),
  );
}

// ══ 3. 삼각 표준극한 — sin x / x → 1 ══════════════════════════════
//   x=0 에서 0/0. 양옆에서 1 로 다가가므로 (0,1) 에 구멍.
function sinxGraph() {
  const f = (x) => Math.sin(x) / x;
  return panel([-9, 9], [-0.35, 1.15]).title(tex`\lim_{x\to 0}\frac{\sin x}{x} = 1`).add(
    curve.fn(f).on([-9, -0.001]).color(orange).stroke(2.6).n(500),
    curve.fn(f).on([0.001, 9]).color(orange).stroke(2.6).n(500),
    line.horizontal(1).color(FAINT).stroke(1).dash([2, 3]),
    line.horizontal(0).color(gray).stroke(0.5),
    hole(0, 1, orange),
    annotate.text([0, 1]).label(tex`(0,\ 1)`).font(11).color(orange).bold().offset(8, -14),
  );
}

// ══ 4. 한쪽 극한 — |x|/x 는 좌우가 다르다 ═════════════════════════
//   x>0 이면 +1, x<0 이면 −1. 0 에서 두 값이 만나지 않으므로 극한 없음.
function onesidedGraph() {
  return panel([-5, 5], [-1.8, 1.8]).title(tex`f(x) = \frac{|x|}{x}`).add(
    curve.fn(() => 1).on([0.001, 5]).color(green).stroke(2.8).n(60),
    curve.fn(() => -1).on([-5, -0.001]).color(red).stroke(2.8).n(60),
    line.vertical(0).color(ASYMP).stroke(1.1).dash([5, 5]),
    line.horizontal(0).color(gray).stroke(0.5),
    hole(0, 1, green), hole(0, -1, red),
    annotate.text([5, 1]).label(tex`\lim_{x\to 0^{+}} = 1`).font(11).color(green).anchor('end').offset(0, 10),
    annotate.text([-5, -1]).label(tex`\lim_{x\to 0^{-}} = -1`).font(11).color(red).offset(6, -16),
    annotate.text([0, 1.5]).label(tex`\text{left} \neq \text{right} \Rightarrow \text{DNE}`).font(11).color(gray).anchor('middle'),
  );
}

// ══ 5. 압착 정리 — x² sin(1/x) ════════════════════════════════════
//   −x² ≤ x² sin(1/x) ≤ x². 양쪽 껍질이 0 으로 가므로 가운데도 0 으로.
function squeezeGraph() {
  const g = (x) => x * x * Math.sin(1 / x);
  return panel([-0.65, 0.65], [-0.5, 0.5]).title(tex`-x^{2} \leq x^{2}\sin\tfrac{1}{x} \leq x^{2}`).add(
    region.between((x) => x * x, (x) => -x * x).on([-0.6, 0.6], { n: 200 }).fill('#bfdbfe').opacity(0.35),
    curve.fn(g).on([-0.6, -0.001]).color(red).stroke(1.6).n(1200),
    curve.fn(g).on([0.001, 0.6]).color(red).stroke(1.6).n(1200),
    curve.fn((x) => x * x).on([-0.6, 0.6]).color(blue).stroke(1.8).n(200),
    curve.fn((x) => -x * x).on([-0.6, 0.6]).color(blue).stroke(1.8).n(200),
    line.horizontal(0).color(gray).stroke(0.5),
    hole(0, 0, red),
    legend([-0.62, 0.42], tex`y = x^{2}`, blue, 10),
    legend([-0.62, -0.42], tex`y = -x^{2}`, blue, 10),
    annotate.text([0.3, 0.08]).label(tex`y = x^{2}\sin\tfrac{1}{x}`).font(10).color(red),
  );
}

// ══ 6. 복잡한 분수 — (1/x − 1/3)/(x−3) ════════════════════════════
//   통분하면 −1/(3x). x=3 에서 구멍, 극한값 −1/9.
function complexFractionGraph() {
  const f = (x) => -1 / (3 * x);
  return panel([-8, 8], [-1.6, 1.6]).title(tex`\frac{\tfrac{1}{x}-\tfrac{1}{3}}{x-3} = -\frac{1}{3x}`).add(
    curve.fn(f).on([0.2, 8]).color(blue).stroke(2.4).n(400),
    curve.fn(f).on([-8, -0.2]).color(blue).stroke(2.4).n(400),
    line.vertical(0).color(ASYMP).stroke(1).dash([5, 5]),
    line.horizontal(0).color(gray).stroke(0.5),
    hole(3, -1 / 9, red),
    annotate.text([3, -1 / 9]).label(tex`\text{hole } (3,\ -\tfrac19)`).font(11).color(red).bold().offset(-8, -16),
  );
}

// ── figure 레지스트리 (CLI 가 이 키를 출력 파일명으로 쓴다) ────────────
export const figures = {
  '13a-1-hole': holeGraph,
  '13a-2-conjugate': conjugateGraph,
  '13a-3-sinx-over-x': sinxGraph,
  '13a-4-onesided': onesidedGraph,
  '13a-5-squeeze': squeezeGraph,
  '13a-6-complex-fraction': complexFractionGraph,
};

