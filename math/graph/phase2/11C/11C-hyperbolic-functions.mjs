// math/graph/phase2/11C/11C-hyperbolic-functions.mjs — 세션 11C(쌍곡선 함수) 그림
//
// ── figure 목록 (키 = 출력 파일명 = 마크다운 태그 id) ──────────────
//    11c-1-analogy    단위원 vs 단위쌍곡선 — (cos,sin) ↔ (cosh,sinh) 파라미터화
//    11c-2-even-odd   eˣ = cosh x + sinh x — 짝함수부·홀함수부 분해
//    11c-3a…3f        cosh · sinh · tanh · sech · csch · coth — 낱개 6장
//    11c-4-inverse    arsinh·arcosh·artanh — 로그 그래프 3종
//    11c-5-catenary   현수선 y = 3cosh(x/3) vs 근처 포물선 비교
//
// ── 코어 API 만 쓴다 (기준 @jaywoo0830a/logos 0.4.1) ────────────────
//   곡선 curve.fn(f).on(dom) · 원 circle.center().radius() · 쌍곡선 hyperbola.center().semi()
//   부채꼴 polygon(...pts.map(toPoint)) · 선분 segment([x,y],[x,y]) · 기준선 line.vertical/horizontal
//   마커 point(x,y).dot() · 라벨 annotate.text([x,y]).label()…
//   색 kit.palette.tab 구조분해 · 표본 생성(순수 JS 수학)만 ./_helper.mjs
import { annotate, circle, curve, hyperbola, kit, line, point, polygon, segment, toPoint } from '@jaywoo0830a/logos';
import { arcSamples, hyperSamples, rad } from './_helper.mjs';

const { plot2d, subplots, palette } = kit;
const { blue, red, green, purple, orange, cyan, gray } = palette.tab;
const NAVY = palette.navy;             // 기준 도형(단위원·단위쌍곡선)
const GOLD = '#b8860b';                // 부채꼴 채움 강조
const FAINT = '#dddddd', ASYMP = '#cccccc';   // 보조 톤(지면)
const BOX = { facecolor: 'white', alpha: 0.85 };

// ── 함수별 고정색 (그래프·라벨·범례가 같은 색을 공유) ──────────────────
const COSH = blue, SINH = red, TANH = green, SECH = purple, CSCH = orange, COTH = cyan;

// ── 패널 프리셋 (코어 plot2d 옵션 위의 1줄 별칭 — 이 파일 안에서만) ────
const AX = () => ({ x: { label: 'x' }, y: { label: 'y' } });
/** 1×1 / 1×2 표준 패널 */
const panel = (xr, yr, size = [430, 400]) => plot2d(xr, yr, { size, axes: AX(), grid: { alpha: 0.3 } });
/** 정사각 도식 패널 (equal · 축 없음) */
const square = (xr, yr) => plot2d(xr, yr, { size: [480, 460], equal: true, axes: false, grid: false });
/** 범례 대신 같은 색 라벨 */
const legend = (at, text, color, font = 11) => annotate.text(at).label(text).font(font).color(color).bold();
/** 채운 부채꼴 — 코어 polygon + toPoint (배열 좌표 허용) */
const sector = (pts, fill, opacity = 0.2) => polygon(...pts.map(toPoint)).fill(fill).opacity(opacity);
/** x=0 등 점근선을 가진 함수를 구간마다 잘라 코어 curve 배열로 (점근선 사이마다 별도 곡선 + ±클램프) */
const branchCurves = (f, xr, breaks, { clip = 8, eps = 0.004, color, stroke = 2.4 } = {}) => {
  const xs = [xr[0], ...breaks.filter((b) => b > xr[0] && b < xr[1]), xr[1]];
  const out = [];
  for (let i = 0; i < xs.length - 1; i++) {
    const a = xs[i] + eps, b = xs[i + 1] - eps;
    if (b > a) out.push(curve.fn((t) => Math.max(-clip, Math.min(clip, f(t)))).on([a, b]).color(color).stroke(stroke).n(300));
  }
  return out;
};

// ══ 1. 단위원 vs 단위쌍곡선 ══════════════════════════════════════
//   왼쪽: x²+y²=1, (cos θ, sin θ), 부채꼴 넓이 θ/2.
//   오른쪽: x²−y²=1(오른쪽 가지), (cosh t, sinh t), 영역 넓이 t/2.
function analogy() {
  const theta = 60, t = 1.0;
  const c = Math.cos(rad(theta)), s = Math.sin(rad(theta));
  const px = Math.cosh(t), py = Math.sinh(t);

  const left = square([-1.7, 1.7], [-1.5, 1.7]).title('x² + y² = 1').add(
    sector([[0, 0], ...arcSamples(1, 0, rad(theta)), [0, 0]], GOLD, 0.2),
    circle.center(point(0, 0)).radius(1).color(NAVY).stroke(1.8),
    line.horizontal(0).color(gray).stroke(0.6), line.vertical(0).color(gray).stroke(0.6),
    segment([0, 0], [c, s]).color(NAVY).stroke(1.6),
    segment([c, 0], [c, s]).color(SINH).stroke(1.4).dash([4, 3]),
    segment([0, 0], [c, 0]).color(COSH).stroke(1.8),
    point(c, s).dot().color(NAVY).size(5.5),
    annotate.text([c, s]).label('(cos θ, sin θ)').font(11).color(NAVY).bold().offset(6, -12),
    annotate.text([c / 2, -0.16]).label('cos θ').font(11).color(COSH).anchor('middle'),
    annotate.text([c + 0.05, s / 2]).label('sin θ').font(11).color(SINH),
    annotate.text([0.24, 0.12]).label('θ').font(12).box(BOX),
    annotate.text([0.45, 0.33]).label('area = θ/2').font(10).color(GOLD),
  );

  const right = square([-1.4, 3.0], [-1.5, 2.2]).title('x² − y² = 1').add(
    sector([[0, 0], [1, 0], ...hyperSamples(t)], GOLD, 0.2),
    hyperbola.center(point(0, 0)).semi(1, 1).color(NAVY).stroke(1.8),
    line.horizontal(0).color(gray).stroke(0.6), line.vertical(0).color(gray).stroke(0.6),
    segment([0, 0], [px, py]).color(NAVY).stroke(1.6),
    segment([px, 0], [px, py]).color(SINH).stroke(1.4).dash([4, 3]),
    segment([0, 0], [1, 0]).color(COSH).stroke(1.8),
    point(px, py).dot().color(NAVY).size(5.5),
    point(1, 0).dot().color(COSH).size(4),
    annotate.text([px, py]).label('(cosh t, sinh t)').font(11).color(NAVY).bold().offset(6, -12),
    annotate.text([1, -0.16]).label('x = 1').font(11).color(COSH).anchor('middle'),
    annotate.text([px + 0.05, py / 2]).label('sinh t').font(11).color(SINH),
    annotate.text([1.15, 0.42]).label('area = t/2').font(10).color(GOLD),
  );
  return subplots([left, right], { cols: 2, tight: true, title: 'Unit Circle vs Unit Hyperbola' });
}

// ══ 2. e^x 의 짝·홀 분해 ══════════════════════════════════════════
//   e^x = cosh x + sinh x. cosh 는 짝함수부, sinh 는 홀함수부.
function evenOdd() {
  const xr = [-2.2, 2.2], yr = [-2.6, 4.2];
  const p1 = panel(xr, yr).title('eˣ = cosh x + sinh x').add(
    curve.fn(Math.exp).on(xr).color(NAVY).stroke(2.4).n(300),
    curve.fn((x) => Math.exp(-x)).on(xr).color(FAINT).stroke(1.4).dash([5, 4]),
    line.horizontal(0).color(gray).stroke(0.5), line.vertical(0).color(gray).stroke(0.5),
    point(0, 1).dot().color(NAVY).size(4),
    legend([-2.1, 3.8], 'eˣ', NAVY),
    legend([-2.1, 3.35], 'e⁻ˣ', gray),
  );
  const p2 = panel(xr, yr).title('cosh x  (even part)').add(
    curve.fn((x) => (Math.exp(x) + Math.exp(-x)) / 2).on(xr).color(COSH).stroke(2.4).n(300),
    line.horizontal(1).color(COSH).stroke(1).dash([3, 3]).opacity(0.6),
    line.horizontal(0).color(gray).stroke(0.5), line.vertical(0).color(gray).stroke(0.5),
    point(0, 1).dot().color(COSH).size(4.5),
    annotate.text([0, 1]).label('min 1 at x = 0').font(10).color(COSH).anchor('middle').offset(0, 16),
    legend([-2.1, 3.8], '(eˣ + e⁻ˣ)/2', COSH),
  );
  const p3 = panel(xr, yr).title('sinh x  (odd part)').add(
    curve.fn((x) => (Math.exp(x) - Math.exp(-x)) / 2).on(xr).color(SINH).stroke(2.4).n(300),
    line.horizontal(0).color(gray).stroke(0.5), line.vertical(0).color(gray).stroke(0.5),
    point(0, 0).dot().color(SINH).size(4.5),
    annotate.text([0.15, -0.75]).label('through origin').font(10).color(SINH),
    legend([-2.1, 3.8], '(eˣ − e⁻ˣ)/2', SINH),
  );
  return subplots([p1, p2, p3], { cols: 3, tight: true, title: 'Splitting eˣ into Even and Odd Parts' });
}

// ══ 3. 여섯 쌍곡선 함수 — 낱개 6장 (11c-3a … 11c-3f) ═════════════
//   한 사진에 6개를 몰아넣으면 각 그래프가 작아 읽기 어려우므로 함수마다 독립 figure 로.
/** 매끄러운 곡선 한 장 (cosh·sinh·tanh·sech) */
function smoothFig(title, f, color, yr) {
  return plot2d([-3, 3], yr, { size: [460, 400], axes: AX(), grid: { alpha: 0.3 } })
    .title(title)
    .add(curve.fn(f).on([-3, 3]).color(color).stroke(2.4).n(400), line.horizontal(0).color(gray).stroke(0.5));
}
/** x=0 에 점근선을 가진 두 갈래 곡선 한 장 (csch·coth) */
function branchFig(title, f, color) {
  return plot2d([-3, 3], [-6, 6], { size: [460, 400], axes: AX(), grid: { alpha: 0.3 } })
    .title(title)
    .add(...branchCurves(f, [-3, 3], [0], { color, clip: 5.6 }), line.vertical(0).color(ASYMP).stroke(1.2).dash([5, 5]), line.horizontal(0).color(gray).stroke(0.5));
}
const coshGraph = () => smoothFig('cosh x  (even, min 1)', Math.cosh, COSH, [-1, 8]).add(
  line.horizontal(1).color(COSH).stroke(1).dash([3, 3]).opacity(0.6),
  point(0, 1).dot().color(COSH).size(4.5),
  annotate.text([0, 1]).label('min 1 at x = 0').font(10).color(COSH).anchor('middle').offset(0, 16),
);
const sinhGraph = () => smoothFig('sinh x  (odd)', Math.sinh, SINH, [-8, 8]).add(
  point(0, 0).dot().color(SINH).size(4.5),
  annotate.text([0.3, -1.3]).label('through origin').font(10).color(SINH),
);
const tanhGraph = () => smoothFig('tanh x  (odd, → ±1)', Math.tanh, TANH, [-1.6, 1.6]).add(
  line.horizontal(1).color(ASYMP).stroke(1).dash([5, 5]),
  line.horizontal(-1).color(ASYMP).stroke(1).dash([5, 5]),
  annotate.text([2.3, 1.18]).label('y = 1').font(9).color(gray).anchor('end'),
  annotate.text([2.3, -1.18]).label('y = −1').font(9).color(gray).anchor('end'),
);
const sechGraph = () => smoothFig('sech x  (even, 0 < y ≤ 1)', (x) => 1 / Math.cosh(x), SECH, [-0.5, 1.4]).add(
  line.horizontal(1).color(SECH).stroke(1).dash([3, 3]).opacity(0.6),
  point(0, 1).dot().color(SECH).size(4.5),
  annotate.text([0, 1.32]).label('max 1 at x = 0').font(10).color(SECH).anchor('middle'),
);
const cschGraph = () => branchFig('csch x  (odd)', (x) => 1 / Math.sinh(x), CSCH);
const cothGraph = () => branchFig('coth x  (odd)', (x) => 1 / Math.tanh(x), COTH).add(
  line.horizontal(1).color(ASYMP).stroke(1).dash([5, 5]),
  line.horizontal(-1).color(ASYMP).stroke(1).dash([5, 5]),
);

// ══ 4. 역쌍곡선 함수 (로그 그래프) ══════════════════════════════════
//   arsinh: 모든 실수 / arcosh: x≥1 / artanh: |x|<1 (수직 점근 x=±1).
function inverseGraphs() {
  const p1 = panel([-4, 4], [-3, 3]).title('arsinh x = ln(x + √(x²+1))').add(
    curve.fn(Math.asinh).on([-4, 4]).color(SINH).stroke(2.4).n(300),
    line.horizontal(0).color(gray).stroke(0.5), line.vertical(0).color(gray).stroke(0.5),
    point(0, 0).dot().color(SINH).size(4.5),
    annotate.text([3.6, 2.4]).label('all real x').font(10).color(SINH).anchor('end'),
  );
  const p2 = panel([-0.5, 6], [-0.5, 3]).title('arcosh x = ln(x + √(x²−1))').add(
    curve.fn(Math.acosh).on([1, 6]).color(COSH).stroke(2.4).n(300),
    line.vertical(1).color(ASYMP).stroke(1.2).dash([5, 5]),
    line.horizontal(0).color(gray).stroke(0.5), line.vertical(0).color(gray).stroke(0.5),
    point(1, 0).dot().color(COSH).size(4.5),
    annotate.text([1.12, 0.28]).label('starts at (1, 0)').font(10).color(COSH),
  );
  const p3 = panel([-1.4, 1.4], [-3, 3]).title('artanh x = ½ ln((1+x)/(1−x))').add(
    ...branchCurves(Math.atanh, [-0.999, 0.999], [], { color: TANH, clip: 2.9, eps: 0 }),
    line.vertical(1).color(ASYMP).stroke(1.3).dash([5, 5]),
    line.vertical(-1).color(ASYMP).stroke(1.3).dash([5, 5]),
    line.horizontal(0).color(gray).stroke(0.5), line.vertical(0).color(gray).stroke(0.5),
    point(0, 0).dot().color(TANH).size(4.5),
    annotate.text([0.6, 1.6]).label('|x| < 1').font(10).color(TANH).anchor('middle'),
  );
  return subplots([p1, p2, p3], { cols: 3, tight: true, title: 'Inverse Hyperbolic Functions' });
}

// ══ 5. 현수선 vs 포물선 ════════════════════════════════════════════
//   y = 3cosh(x/3). 꼭짓점 (0,3). 근처 포물선 y = 3 + x²/6 과 비교 — 멀어지면 현수선이 더 가파르다.
function catenary() {
  const cat = (x) => 3 * Math.cosh(x / 3);
  const par = (x) => 3 + (x * x) / 6;              // cosh(x/3) ≈ 1 + x²/18 에서 유도
  return plot2d([-6.5, 6.5], [0, 13], { size: [640, 460], axes: AX(), grid: { alpha: 0.3 } })
    .title('Catenary y = 3cosh(x/3) vs Parabola').add(
      curve.fn(cat).on([-6, 6]).color(COSH).stroke(2.6).n(400),
      curve.fn(par).on([-6, 6]).color(SINH).stroke(2).dash([6, 4]),
      line.horizontal(3).color(gray).stroke(0.6).dash([2, 2]),
      point(0, 3).dot().color(COSH).size(5),
      annotate.text([0, 3]).label('min (0, 3)').font(11).color(COSH).bold().offset(8, 12),
      legend([-6.2, 12.4], 'y = 3cosh(x/3)', COSH),
      legend([-6.2, 11.4], 'y = 3 + x²/6', SINH, 11),
      annotate.text([4.4, 8.2]).label('catenary rises faster').font(10).color(COSH).anchor('middle'),
    );
}

// ── figure 레지스트리 (CLI 가 이 키를 출력 파일명으로 쓴다) ────────────
export const figures = {
  '11c-1-analogy': analogy,
  '11c-2-even-odd': evenOdd,
  '11c-3a-cosh': coshGraph,
  '11c-3b-sinh': sinhGraph,
  '11c-3c-tanh': tanhGraph,
  '11c-3d-sech': sechGraph,
  '11c-3e-csch': cschGraph,
  '11c-3f-coth': cothGraph,
  '11c-4-inverse': inverseGraphs,
  '11c-5-catenary': catenary,
};
