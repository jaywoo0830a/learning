// math/graph/phase2/11C-hyperbolic-functions.mjs — 세션 11C(쌍곡선 함수) 그림 복원
//
// ── 무엇을 하는가 ────────────────────────────────────────────────
//   math/sessions/phase2/11C-hyperbolic-functions.md 의 그림 5장을
//   @jaywoo0830a/logos DSL 만으로 다시 그린다. 삼각함수(11A/11B)의 "쌍둥이 우주"인
//   쌍곡선 함수의 정의·그래프·역함수·응용(현수선)을 다룬다.
//
// ── figure 목록 (키 = 출력 파일명 = 마크다운 태그 id) ──────────────
//    11c-1-analogy    단위원 vs 단위쌍곡선 — (cos,sin) ↔ (cosh,sinh) 파라미터화
//    11c-2-even-odd   e^x = cosh x + sinh x — 짝함수부·홀함수부 분해
//    11c-3-graphs     cosh·sinh·tanh(위) + sech·csch·coth(아래) — 2×3
//    11c-4-inverse    arsinh·arcosh·artanh — 로그 그래프 3종
//    11c-5-catenary   현수선 y = 3cosh(x/3) vs 근처 포물선 비교
//
// ── mpl 대응 규칙 (11AB 예제와 같은 관례) ────────────────────────
//   · 수식 라벨    `latexToText`(SVG <text> 폴백)가 `\cosh` 같은 명령을 지우므로
//                 유니코드 평문('cosh x', '√(x²+1)', '±1')을 쓴다.
//   · 곡선        `curve.fn(f).on([a,b])` ← ax.plot(x, f(x))
//   · 수직 점근선  `branchCurves()` 로 점근선 사이 구간마다 잘라 그리고 ±clip 클램프
//   · 채운 부채꼴  `polygon(원점, 호의 표본 …).fill(c).opacity()` ← ax.fill(...)
//   · 여러 패널    `subplots([...], { cols })` ← plt.subplots(rows, cols)
//   · 범례        logos 에 legend 가 없어 **같은 색 라벨**로 대신한다.
import {
  point, circle, polygon, segment, line, curve, hyperbola, annotate, kit,
} from '@jaywoo0830a/logos';

// ── 색 — 함수마다 고정색 (그래프·라벨·범례가 같은 색을 공유) ──────────
const COSH = '#2980b9';   // cosh — 파랑
const SINH = '#e74c3c';   // sinh — 빨강
const TANH = '#27ae60';   // tanh — 초록
const SECH = '#9b59b6';   // sech — 보라
const CSCH = '#e67e22';   // csch — 주황
const COTH = '#1abc9c';   // coth — 청록
const GRAY = '#999999', FAINT = '#dddddd', ASYMP = '#cccccc', HL = '#f1c40f', CIRC = '#2c3e50';
const BOX = { facecolor: 'white', alpha: 0.85 };

const { plot2d, subplots } = kit;

// ── 미세 헬퍼 (전부 라이브러리 API 위의 얇은 별칭) ──────────────────
const P = (v) => point(v[0], v[1]);
const dotAt = (v, color, size = 5, shape = 'circle') => P(v).marker(shape).color(color).size(size);
const style = (d, { color, stroke = 1, dash, opacity } = {}) => {
  let s = d;
  if (color !== undefined) s = s.color(color);
  if (stroke !== undefined) s = s.stroke(stroke);
  if (dash !== undefined) s = s.dash(dash);
  if (opacity !== undefined) s = s.opacity(opacity);
  return s;
};
const labelAt = (at, text, { color, font = 12, bold = false, anchor, box, dx, dy, rotate } = {}) => {
  let t = annotate.text(P(at)).label(text).font(font);
  if (color !== undefined) t = t.color(color);
  if (bold) t = t.bold();
  if (anchor) t = t.anchor(anchor);
  if (box) t = t.box(box);
  if (dx !== undefined || dy !== undefined) t = t.offset(dx || 0, dy || 0);
  if (rotate !== undefined) t = t.rotate(rotate);
  return t;
};
const segAt = (a, b, o) => style(segment(P(a), P(b)), o);
const vlineAt = (x, o) => style(line.vertical(x), o);
const hlineAt = (y, o) => style(line.horizontal(y), o);
const circleAt = (c, r, o) => style(circle.center(P(c)).radius(r), o);
const polyAt = (pts, fill, opacity = 0.15, o = {}) => {
  let g = polygon(...pts.map(P)).fill(fill).opacity(opacity);
  if (o.color !== undefined) g = g.color(o.color).stroke(o.stroke ?? 1);
  return g;
};
const curveOf = (f, dom, { n, ...o } = {}) => {
  let c = curve.fn(f).on(dom);
  if (n) c = c.n(n);
  return style(c, { stroke: 2, ...o });
};
const branchCurves = (f, xr, breaks, { clip = 8, eps = 0.004, ...o } = {}) => {
  const xs = [xr[0], ...breaks.filter((b) => b > xr[0] && b < xr[1]), xr[1]];
  const out = [];
  for (let i = 0; i < xs.length - 1; i++) {
    const a = xs[i] + eps, b = xs[i + 1] - eps;
    if (b > a) out.push(curveOf((t) => Math.max(-clip, Math.min(clip, f(t))), [a, b], o));
  }
  return out;
};
const legendAt = (at, text, color, { font = 11, anchor = 'start' } = {}) =>
  labelAt(at, text, { color, font, bold: true, anchor });
/** 호의 표본 점들 ← np.linspace(θ₁, θ₂) 뒤 (cos, sin) */
const arcSamples = (r, d1, d2, n = 60) => Array.from({ length: n + 1 },
  (_, i) => [r * Math.cos(d1 + ((d2 - d1) * i) / n), r * Math.sin(d1 + ((d2 - d1) * i) / n)]);
/** 쌍곡선 오른쪽 가지 표본 (cosh s, sinh s), s∈[0,t] ← (cosh,sinh) 파라미터화 */
const hyperSamples = (t, n = 60) => Array.from({ length: n + 1 },
  (_, i) => { const s = (t * i) / n; return [Math.cosh(s), Math.sinh(s)]; });
const rad = (deg) => (deg * Math.PI) / 180;

/** 정사각 패널 (equal) */
const s2 = (xr, yr, o = {}) => plot2d(xr, yr, { size: [480, 460], equal: true, ...o });
/** 1×2 / 1×3 패널 */
const s2p = (xr, yr, size = [520, 440], o = {}) => plot2d(xr, yr, { size, ...o });
const OFF = { axes: false, grid: false };
const AX = (x = 'x', y = 'y') => ({ x: { label: x }, y: { label: y } });

// ══ 1. 단위원 vs 단위쌍곡선 ══════════════════════════════════════
//   왼쪽: x²+y²=1, (cos θ, sin θ), 부채꼴 넓이 θ/2.
//   오른쪽: x²−y²=1(오른쪽 가지), (cosh t, sinh t), 영역 넓이 t/2.
function analogy() {
  const theta = 60, t = 1.0;
  const c = Math.cos(rad(theta)), s = Math.sin(rad(theta));
  const px = Math.cosh(t), py = Math.sinh(t);

  const left = s2([-1.7, 1.7], [-1.5, 1.7], OFF).title('x² + y² = 1').add(
    polyAt([[0, 0], ...arcSamples(1, 0, rad(theta)), [0, 0]], HL, 0.20),
    circleAt([0, 0], 1, { color: CIRC, stroke: 1.8 }),
    hlineAt(0, { color: GRAY, stroke: 0.6 }), vlineAt(0, { color: GRAY, stroke: 0.6 }),
    segAt([0, 0], [c, s], { color: CIRC, stroke: 1.6 }),
    segAt([c, 0], [c, s], { color: SINH, stroke: 1.4, dash: [4, 3] }),
    segAt([0, 0], [c, 0], { color: COSH, stroke: 1.8 }),
    dotAt([c, s], CIRC, 5.5),
    labelAt([c, s], '(cos θ, sin θ)', { color: CIRC, font: 11, bold: true, dx: 6, dy: -12 }),
    labelAt([c / 2, -0.16], 'cos θ', { color: COSH, font: 11, anchor: 'middle' }),
    labelAt([c + 0.05, s / 2], 'sin θ', { color: SINH, font: 11, anchor: 'start' }),
    labelAt([0.24, 0.12], 'θ', { font: 12, box: BOX }),
    labelAt([0.45, 0.33], 'area = θ/2', { color: '#b8860b', font: 10, anchor: 'start' }),
  );

  const right = s2([-1.4, 3.0], [-1.5, 2.2], OFF).title('x² − y² = 1').add(
    polyAt([[0, 0], [1, 0], ...hyperSamples(t)], HL, 0.20),
    hyperbola.center(point(0, 0)).semi(1, 1).color(CIRC).stroke(1.8),
    hlineAt(0, { color: GRAY, stroke: 0.6 }), vlineAt(0, { color: GRAY, stroke: 0.6 }),
    segAt([0, 0], [px, py], { color: CIRC, stroke: 1.6 }),
    segAt([px, 0], [px, py], { color: SINH, stroke: 1.4, dash: [4, 3] }),
    segAt([0, 0], [1, 0], { color: COSH, stroke: 1.8 }),
    dotAt([px, py], CIRC, 5.5),
    dotAt([1, 0], COSH, 4),
    labelAt([px, py], '(cosh t, sinh t)', { color: CIRC, font: 11, bold: true, dx: 6, dy: -12 }),
    labelAt([1, -0.16], 'x = 1', { color: COSH, font: 11, anchor: 'middle' }),
    labelAt([px + 0.05, py / 2], 'sinh t', { color: SINH, font: 11, anchor: 'start' }),
    labelAt([1.15, 0.42], 'area = t/2', { color: '#b8860b', font: 10, anchor: 'start' }),
  );
  return subplots([left, right], { cols: 2, tight: true, title: 'Unit Circle vs Unit Hyperbola' });
}

// ══ 2. e^x 의 짝·홀 분해 ══════════════════════════════════════════
//   e^x = cosh x + sinh x. cosh 는 짝함수부, sinh 는 홀함수부.
function evenOdd() {
  const xr = [-2.2, 2.2], yr = [-2.6, 4.2];
  const thin = { stroke: 2.4, n: 300 };
  const p1 = s2p(xr, yr, [430, 400], { axes: AX(), grid: { alpha: 0.3 } }).title('eˣ = cosh x + sinh x').add(
    curveOf(Math.exp, xr, { ...thin, color: CIRC }),
    curveOf((x) => Math.exp(-x), xr, { color: FAINT, stroke: 1.4, dash: [5, 4] }),
    hlineAt(0, { color: GRAY, stroke: 0.5 }), vlineAt(0, { color: GRAY, stroke: 0.5 }),
    dotAt([0, 1], CIRC, 4),
    legendAt([-2.1, 3.8], 'eˣ', CIRC),
    legendAt([-2.1, 3.35], 'e⁻ˣ', GRAY),
  );
  const p2 = s2p(xr, yr, [430, 400], { axes: AX(), grid: { alpha: 0.3 } }).title('cosh x  (even part)').add(
    curveOf((x) => (Math.exp(x) + Math.exp(-x)) / 2, xr, { ...thin, color: COSH }),
    hlineAt(1, { color: COSH, stroke: 1, dash: [3, 3], opacity: 0.6 }),
    hlineAt(0, { color: GRAY, stroke: 0.5 }), vlineAt(0, { color: GRAY, stroke: 0.5 }),
    dotAt([0, 1], COSH, 4.5),
    labelAt([0, 1], 'min 1 at x = 0', { color: COSH, font: 10, anchor: 'middle', dy: 16 }),
    legendAt([-2.1, 3.8], '(eˣ + e⁻ˣ)/2', COSH),
  );
  const p3 = s2p(xr, yr, [430, 400], { axes: AX(), grid: { alpha: 0.3 } }).title('sinh x  (odd part)').add(
    curveOf((x) => (Math.exp(x) - Math.exp(-x)) / 2, xr, { ...thin, color: SINH }),
    hlineAt(0, { color: GRAY, stroke: 0.5 }), vlineAt(0, { color: GRAY, stroke: 0.5 }),
    dotAt([0, 0], SINH, 4.5),
    labelAt([0.15, -0.75], 'through origin', { color: SINH, font: 10, anchor: 'start' }),
    legendAt([-2.1, 3.8], '(eˣ − e⁻ˣ)/2', SINH),
  );
  return subplots([p1, p2, p3], { cols: 3, tight: true, title: 'Splitting eˣ into Even and Odd Parts' });
}


// ══ 3. 여섯 쌍곡선 함수 — 낱개 6장 (11c-3a … 11c-3f) ═════════════
//   한 사진에 6개를 몰아넣으면 각 그래프가 작아 읽기 어려우므로, 함수마다
//   **독립 figure** 로 나눈다(각자 제목·축을 가진 한 장짜리 그림).
/** 매끄러운 곡선 한 장 (cosh·sinh·tanh·sech) */
function smoothFig(title, f, color, yr) {
  return s2p([-3, 3], yr, [460, 400], { axes: AX(), grid: { alpha: 0.3 } })
    .title(title).add(
      curveOf(f, [-3, 3], { color, stroke: 2.4, n: 400 }),
      hlineAt(0, { color: GRAY, stroke: 0.5 }),
    );
}
/** x=0 에 점근선을 가진 두 갈래 곡선 한 장 (csch·coth) */
function branchFig(title, f, color) {
  return s2p([-3, 3], [-6, 6], [460, 400], { axes: AX(), grid: { alpha: 0.3 } })
    .title(title).add(
      ...branchCurves(f, [-3, 3], [0], { color, stroke: 2.4, clip: 5.6 }),
      vlineAt(0, { color: ASYMP, stroke: 1.2, dash: [5, 5] }),
      hlineAt(0, { color: GRAY, stroke: 0.5 }),
    );
}
const coshGraph = () => smoothFig('cosh x  (even, min 1)', Math.cosh, COSH, [-1, 8]).add(
  hlineAt(1, { color: COSH, stroke: 1, dash: [3, 3], opacity: 0.6 }),
  dotAt([0, 1], COSH, 4.5),
  labelAt([0, 1], 'min 1 at x = 0', { color: COSH, font: 10, anchor: 'middle', dy: 16 }),
);
const sinhGraph = () => smoothFig('sinh x  (odd)', Math.sinh, SINH, [-8, 8]).add(
  dotAt([0, 0], SINH, 4.5),
  labelAt([0.3, -1.3], 'through origin', { color: SINH, font: 10, anchor: 'start' }),
);
const tanhGraph = () => smoothFig('tanh x  (odd, → ±1)', Math.tanh, TANH, [-1.6, 1.6]).add(
  hlineAt(1, { color: ASYMP, stroke: 1, dash: [5, 5] }),
  hlineAt(-1, { color: ASYMP, stroke: 1, dash: [5, 5] }),
  labelAt([2.3, 1.18], 'y = 1', { color: GRAY, font: 9, anchor: 'end' }),
  labelAt([2.3, -1.18], 'y = −1', { color: GRAY, font: 9, anchor: 'end' }),
);
const sechGraph = () => smoothFig('sech x  (even, 0 < y ≤ 1)', (x) => 1 / Math.cosh(x), SECH, [-0.5, 1.6]).add(
  hlineAt(1, { color: SECH, stroke: 1, dash: [3, 3], opacity: 0.6 }),
  dotAt([0, 1], SECH, 4.5),
  labelAt([0, 1.32], 'max 1 at x = 0', { color: SECH, font: 10, anchor: 'middle' }),
);
const cschGraph = () => branchFig('csch x  (odd)', (x) => 1 / Math.sinh(x), CSCH);
const cothGraph = () => branchFig('coth x  (odd)', (x) => 1 / Math.tanh(x), COTH).add(
  hlineAt(1, { color: ASYMP, stroke: 1, dash: [5, 5] }),
  hlineAt(-1, { color: ASYMP, stroke: 1, dash: [5, 5] }),
);

// ══ 4. 역쌍곡선 함수 (로그 그래프) ══════════════════════════════════
//   arsinh: 모든 실수 / arcosh: x≥1 / artanh: |x|<1 (수직 점근 x=±1).
function inverseGraphs() {
  const p1 = s2p([-4, 4], [-3, 3], [430, 400], { axes: AX(), grid: { alpha: 0.3 } })
    .title('arsinh x = ln(x + √(x²+1))').add(
      curveOf(Math.asinh, [-4, 4], { color: SINH, stroke: 2.4, n: 300 }),
      hlineAt(0, { color: GRAY, stroke: 0.5 }), vlineAt(0, { color: GRAY, stroke: 0.5 }),
      dotAt([0, 0], SINH, 4.5),
      labelAt([3.6, 2.4], 'all real x', { color: SINH, font: 10, anchor: 'end' }),
    );
  const p2 = s2p([-0.5, 6], [-0.5, 3], [430, 400], { axes: AX(), grid: { alpha: 0.3 } })
    .title('arcosh x = ln(x + √(x²−1))').add(
      curveOf(Math.acosh, [1, 6], { color: COSH, stroke: 2.4, n: 300 }),
      vlineAt(1, { color: ASYMP, stroke: 1.2, dash: [5, 5] }),
      hlineAt(0, { color: GRAY, stroke: 0.5 }), vlineAt(0, { color: GRAY, stroke: 0.5 }),
      dotAt([1, 0], COSH, 4.5),
      labelAt([1.12, 0.28], 'starts at (1, 0)', { color: COSH, font: 10, anchor: 'start' }),
    );
  const p3 = s2p([-1.4, 1.4], [-3, 3], [430, 400], { axes: AX(), grid: { alpha: 0.3 } })
    .title('artanh x = ½ ln((1+x)/(1−x))').add(
      ...branchCurves(Math.atanh, [-0.999, 0.999], [], { color: TANH, stroke: 2.4, clip: 2.9, eps: 0 }),
      vlineAt(1, { color: ASYMP, stroke: 1.3, dash: [5, 5] }),
      vlineAt(-1, { color: ASYMP, stroke: 1.3, dash: [5, 5] }),
      hlineAt(0, { color: GRAY, stroke: 0.5 }), vlineAt(0, { color: GRAY, stroke: 0.5 }),
      dotAt([0, 0], TANH, 4.5),
      labelAt([0.6, 1.6], '|x| < 1', { color: TANH, font: 10, anchor: 'middle' }),
    );
  return subplots([p1, p2, p3], { cols: 3, tight: true, title: 'Inverse Hyperbolic Functions' });
}

// ══ 5. 현수선 vs 포물선 ════════════════════════════════════════════
//   y = 3cosh(x/3). 꼭짓점 (0,3). 근처 포물선 y = 3 + x²/6 과 비교 — 멀어지면 현수선이 더 가파르다.
function catenary() {
  const cat = (x) => 3 * Math.cosh(x / 3);
  const par = (x) => 3 + (x * x) / 6;              // cosh(x/3) ≈ 1 + x²/18 에서 유도
  return s2p([-6.5, 6.5], [0, 13], [640, 460], { axes: AX(), grid: { alpha: 0.3 } })
    .title('Catenary y = 3cosh(x/3) vs Parabola').add(
      curveOf(cat, [-6, 6], { color: COSH, stroke: 2.6, n: 400 }),
      curveOf(par, [-6, 6], { color: SINH, stroke: 2, dash: [6, 4] }),
      hlineAt(3, { color: GRAY, stroke: 0.6, dash: [2, 2] }),
      dotAt([0, 3], COSH, 5),
      labelAt([0, 3], 'min (0, 3)', { color: COSH, font: 11, bold: true, dx: 8, dy: 12 }),
      legendAt([-6.2, 12.4], 'y = 3cosh(x/3)', COSH),
      legendAt([-6.2, 11.4], 'y = 3 + x²/6', SINH, { font: 11 }),
      labelAt([4.4, 8.2], 'catenary rises faster', { color: COSH, font: 10, anchor: 'middle' }),
    ).compile();
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

