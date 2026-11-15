// math/graph/phase2/14D/14D-relation-lens.mjs — 세션 14D(관계 렌즈: 단위·부호) 그림
//
// ── figure 목록 (키 = 출력 파일명 = 마크다운 태그 id) ──────────────
//    14d-01-derivative-units  (1×2) 같은 탄젠트, 다른 문장 — m/s vs $/unit
//    14d-02-motion-story      (2×1) v·a 의 부호에서 읽는 운동 이야기 + 타임라인
//
// ── 코어 API 만 쓴다 (기준 @jaywoo0830a/logos 0.4.1) ────────────────
//   이 폴더에는 헬퍼 파일이 없다 — 아래 별칭은 전부 이 파일 안의 1줄 프리셋이다.
//   곡선 curve.fn(f).on(dom) (접선도 같은 API) · 구간 막대 segment([x,y],[x,y]).stroke(16)
//   기준선 line.vertical/horizontal · 마커 point(x,y).dot() · 라벨 annotate.text([x,y])
import { annotate, curve, kit, line, point, polygon, segment, tex } from '@jaywoo0830a/logos';

const { plot2d, subplots, palette } = kit;
const { blue, green, orange, purple, red, gray, cyan } = palette.tab;
const ASYMP = '#cccccc';   // 점근선·보조선(지면 톤 — 팔레트 밖)
const INK = '#333333';     // 본문 잉크(지면 톤 — 팔레트 밖)

// 이 세션의 패널은 14D1 보다 가로로 길다 — 크기만 로컬 상수로 둔다.
const PANEL_W = [560, 320];
const PANEL_TOP = [560, 280];
const PANEL_BOT = [560, 280];

/** 병치 — 코어 subplots 옵션 위의 1줄 별칭(이 파일 안에서만) */
const pair = (l, r, title) => subplots([l, r], { cols: 2, tight: true, title });
const stack = (panels, title) => subplots(panels, { cols: 1, tight: true, title });
/** 축 설정 — 코어 plot2d 의 axes 옵션 그대로 */
const AX = (x, y) => ({ x: { label: x }, y: { label: y } });
/** 범례 대신 같은 색 라벨 (코어 annotate.text 체이닝의 1줄 별칭) */
const legend = (at, text, color, font = 10.5) => annotate.text(at).label(text).font(font).color(color).bold();

// ── ① 같은 기하(탄젠트), 다른 단위 ──────────────────────────────
function derivativeUnits() {
  // 왼쪽: s(t) = ½t² — t=4 에서 접선 기울기 4 m/s
  const s = (t) => 0.5 * t * t;
  const left = plot2d([0, 6], [-2, 18], { size: PANEL_W, axes: AX('time t (s)', 'position s (m)'), grid: { alpha: 0.25 } })
    .title(tex`s(t) = \tfrac{1}{2}t^{2} \;\text{--- m/s}`)
    .add(
      curve.fn(s).on([0, 6]).color(blue).stroke(2.6).n(200),
      curve.fn((t) => 4 * t - 8).on([2.5, 5.5]).color(red).stroke(1.8).dash([6, 4]).n(2),
      point(4, s(4)).dot().color(red).size(4.5),
      annotate.text([4.15, 6.4]).label(tex`s'(4) = 4\ \mathrm{m/s}`).font(11).color(red).bold(),
      legend([1.3, 17.2], 'tangent: “each extra second adds ≈ 4 m”', red, 9.5),
    );

  // 오른쪽: C(q) = q² + 4q + 144 — q=12 에서 접선 기울기 28 $/unit
  const C = (q) => q * q + 4 * q + 144;
  const right = plot2d([0, 22], [0, 750], { size: PANEL_W, axes: AX('quantity q (units)', 'cost C ($)'), grid: { alpha: 0.25 } })
    .title(tex`C(q) = q^{2} + 4q + 144 \;\text{--- \$/unit}`)
    .add(
      curve.fn(C).on([0, 22]).color(green).stroke(2.6).n(200),
      curve.fn((q) => 28 * q).on([4, 21]).color(red).stroke(1.8).dash([6, 4]).n(2),
      point(12, C(12)).dot().color(red).size(4.5),
      annotate.text([12.4, 250]).label(tex`C'(12) = 28\ \text{\$/unit}`).font(11).color(red).bold(),
      legend([0.6, 720], 'tangent: “the next unit costs ≈ $28”', red, 9.5),
    );

  return pair(left, right, 'The Same Geometric Object, Two Sentences');
}

// ── ② v·a 의 부호 → 운동 이야기 (위: 그래프 / 아래: 타임라인) ───
function motionStory() {
  const v = (t) => 3 * (t - 1) * (t - 3);
  const a = (t) => 6 * t - 12;

  const top = plot2d([0, 4], [-8, 10], { size: PANEL_TOP, axes: AX('time t (s)', 'v , a'), grid: { alpha: 0.25 } })
    .title(tex`v(t) = 3t^{2} - 12t + 9 \quad\text{and}\quad a(t) = 6t - 12`)
    .add(
      curve.fn(v).on([0, 4]).color(blue).stroke(2.6).n(200),
      curve.fn(a).on([0, 4]).color(orange).stroke(2.2).n(200),
      line.vertical(1).color(ASYMP).stroke(1).dash([4, 4]),
      line.vertical(2).color(ASYMP).stroke(1).dash([4, 4]),
      line.vertical(3).color(ASYMP).stroke(1).dash([4, 4]),
      point(1, 0).dot().color(blue).size(4),
      point(3, 0).dot().color(blue).size(4),
      point(2, 0).dot().color(orange).size(4),
      annotate.text([0.25, 8.7]).label(tex`v`).font(11).color(blue).bold(),
      annotate.text([0.25, -7.0]).label(tex`a`).font(11).color(orange).bold(),
      annotate.text([1, 5.2]).label('turning point').font(9).color(blue).anchor('middle'),
      annotate.text([3, 5.2]).label('turning point').font(9).color(blue).anchor('middle'),
      annotate.text([2, -3.6]).label('a changes sign').font(9).color(orange).anchor('middle'),
    );

  // 아래: 부호에서 만든 타임라인 (0<t<1 · 1<t<2 · 2<t<3 · t>3)
  //   각 구간 = 색 띠(굵은 segment) + 부호 두 줄. 요소를 먼저 모아 한 번에 add 한다.
  const bands = [
    { x0: 0, x1: 1, color: blue, sign: tex`v{+}\;\;a{-}`, story: 'forward, slowing' },
    { x0: 1, x1: 2, color: orange, sign: tex`v{-}\;\;a{-}`, story: 'backward, speeding up' },
    { x0: 2, x1: 3, color: purple, sign: tex`v{-}\;\;a{+}`, story: 'backward, slowing' },
    { x0: 3, x1: 4, color: green, sign: tex`v{+}\;\;a{+}`, story: 'forward, speeding up' },
  ];
  const bandParts = bands.flatMap((b) => {
    const mid = (b.x0 + b.x1) / 2;
    return [
      segment([b.x0, 0.5], [b.x1, 0.5]).color(b.color).stroke(16),
      annotate.text([mid, 0.76]).label(b.sign).font(10).color(b.color).bold().anchor('middle'),
      annotate.text([mid, 0.22]).label(b.story).font(9.5).color(gray).anchor('middle'),
    ];
  });
  const tickParts = [0, 1, 2, 3, 4].flatMap((t) => [
    line.vertical(t).color(ASYMP).stroke(1).dash([3, 3]),
    annotate.text([t, 0.06]).label(String(t)).font(9).color(gray).anchor('middle'),
  ]);

  const bottom = plot2d([0, 4], [0, 1], { size: PANEL_BOT, axes: false, grid: false })
    .title('The motion timeline — read straight off the signs')
    .add(...bandParts, ...tickParts);

  return stack([top, bottom], 'Motion Story from the Signs of v and a');
}


// ══════════════════════════════════════════════════════════════════════
//  문제별 도표 — 한 문제 = 한 그림
// ══════════════════════════════════════════════════════════════════════
//  규격(모든 문제 동일):
//    · 제목 = 문제 ID + 그 문제의 함수
//    · 그림 = 그 문제가 요구하는 것만 (축은 데이터 좌표)
//  코어 API 만 쓴다 — point(x,y) · curve.fn(f).on(dom) · segment(A,B)
//                    · annotate.text(point).label().font().color() · annotate.arrow(A,B)
const PW = 640, PH = 400;

/** 문제 패널 — 제목 + 축 + (선택) x 눈금. 축은 라벨 자리만큼 자동으로 넓힌다. */
const panel = (id, title, xr, yr, xlabel, ylabel, xTicks) =>
  plot2d(wide(...xr, 0.09), wide(...yr, 0.05), {
    size: [PW, PH],
    grid: { alpha: 0.25 },
    axes: { x: { label: xlabel, ...(xTicks ? { ticks: xTicks } : {}) }, y: { label: ylabel } },
  }).title(`${id} — ${title}`);

/** 라벨 자리를 위해 데이터 범위를 살짝 넓힌다 */
const wide = (a, b, frac = 0.10) => {
  const d = Math.abs(b - a) * frac || 1;
  return [a - d, b + d];
};
/** 1줄 텍스트 */
const txt = (x, y, s, c = INK, font = 9.5) =>
  annotate.text(point(x, y)).label(s).font(font).color(c);
/** 굵은 한 줄 */
const bold = (x, y, s, c = INK, font = 10) =>
  annotate.text(point(x, y)).label(s).font(font).color(c).bold();
/** 가운데 정렬 */
const mid = (x, y, s, c = '#8a8a8a', font = 9) =>
  annotate.text(point(x, y)).label(s).font(font).color(c).anchor('middle');
/** 점 + 라벨 */
const pin = (x, y, s, c = red, dy = 0) => [
  point(x, y).dot().color(c).size(5),
  annotate.text(point(x, y + dy)).label(s).font(9.5).color(c),
];
/** (x0,f(x0)) → (x1,f(x1)) 선분 */
const chord = (f, x0, x1, c = red, w = 2.4) =>
  segment(point(x0, f(x0)), point(x1, f(x1))).color(c).stroke(w);
/** 상승분 쐐기 — x0 에서 dx 만큼 갈 때의 세로 증가를 삼각형으로 */
const rise = (f, x0, dx, c = red, op = 0.22) => {
  const [a, b] = dx > 0 ? [x0, x0 + dx] : [x0 + dx, x0];
  const lo = Math.min(f(a), f(b)), hi = Math.max(f(a), f(b));
  return polygon(point(a, lo), point(b, lo), point(b, hi)).fill(c).opacity(op).stroke(0).color(c);
};
/** 세로/가로 기준선 */
const vref = (x, c = ASYMP) => line.vertical(x).color(c).stroke(1).dash([4, 4]);
const href = (y = 0, c = ASYMP) => line.horizontal(y).color(c).stroke(1.2);
const hor = (y, x0, x1, c = red, w = 2.4) => segment(point(x0, y), point(x1, y)).color(c).stroke(w);

// ── RP — 문제 4장 ──────────────────────────────────────────────────
//   RP1: 상수 기울기 / RP2: 커지는 기울기 / RP3: 역수 / RP4: 사슬
const figures = {};   // 아래에서 문제별로 채운 뒤 마지막에 export 한다

// 세션 본문의 렌즈 예시 (Example 1 · Example 2) — 기존 그림 그대로
figures['14d-01-derivative-units'] = derivativeUnits;
figures['14d-02-motion-story'] = motionStory;

figures['14d-rp1'] = () => {
  const F = (d) => 4 + 2 * d;
  return panel('RP1', 'F = 4 + 2d', [0, 6], [0, 18], 'distance d (km)', 'fare F (dollars)')
    .add(
      curve.fn(F).on([0, 6]).color(blue).stroke(2.6).n(40),
      chord(F, 1, 2), chord(F, 3, 4), chord(F, 4, 5),
      rise(F, 1, 1), rise(F, 3, 1), rise(F, 4, 1),
      ...pin(1.5, F(1.5), '+2', red, 1.3),
      ...pin(3.5, F(3.5), '+2', red, 1.3),
      ...pin(4.5, F(4.5), '+2', red, 1.3),
      bold(0.25, 16.6, "F' = 2 dollars/km — the same at every d", blue),
    );
};

figures['14d-rp2'] = () => {
  const A = (s) => s * s;
  return panel('RP2', 'A = s²', [0, 10], [0, 100], 'side s (cm)', 'area A (cm²)')
    .add(
      curve.fn(A).on([0, 10]).color(green).stroke(2.6).n(200),
      chord(A, 2, 3), chord(A, 7, 8),
      rise(A, 2, 1, red), rise(A, 7, 1, orange),
      ...pin(3.1, A(2.5), '+5 cm² at s≈2.5', red, 5),
      ...pin(8.1, A(7.5), '+15 cm² at s≈7.5', orange, 5),
      bold(0.35, 90, "A' = 2s — the degree grows with the side", green),
      txt(0.35, 80, 'the same +1 cm buys more area further out', '#8a8a8a'),
    );
};

figures['14d-rp3'] = () => {
  const t = (v) => 120 / v;
  return panel('RP3', 't = 120/v', [0, 120], [0, 7], 'speed v (km/h)', 'trip time t (h)')
    .add(
      href(0),
      curve.fn(t).on([12, 120]).color(blue).stroke(2.6).n(300),
      ...pin(60, t(60), 't(60) = 2 h', red, 0.55),
      annotate.arrow(point(55, 2.25), point(72, 1.75)).color(red),
      bold(6, 6.3, "t' = −120/v² — h per (km/h)", blue),
      txt(6, 5.4, 'the minus shrinks the duration; it never goes below 0', '#8a8a8a'),
    );
};

figures['14d-rp4'] = () => {
  const P = (tt) => 0.4 * (300 + 2 * tt);
  return panel('RP4', 'P = 0.4T, T = 300 + 2t', [0, 60], [110, 175], 'time t (s)', 'pressure P (kPa)')
    .add(
      curve.fn(P).on([0, 60]).color(purple).stroke(2.6).n(40),
      ...pin(20, P(20), "P' = 0.8 kPa/s", red, 7),
      bold(2, 170, '0.4 kPa/K  ×  2 K/s  =  0.8 kPa/s', purple),
      txt(2, 163, 'chained degrees multiply', '#8a8a8a'),
    );
};

// ── RPB — 문제 5장 ─────────────────────────────────────────────────
//   RPB1: 값+정도 / RPB2: 커지는 정도 / RPB3: 역수(분 단위) / RPB4: 역수 관계 / RPB5: 가속
figures['14d-rpb1'] = () => {
  const V = (tt) => 50 + 12 * tt;
  return panel('RPB1', 'V = 50 + 12t', [0, 5], [0, 120], 't (min)', 'V (L)')
    .add(
      curve.fn(V).on([0, 5]).color(blue).stroke(2.6).n(40),
      ...pin(0, 50, '50 L = a VALUE', blue, 7),
      chord(V, 2, 3), rise(V, 2, 1),
      ...pin(3.05, V(2.5), '+12 L per min = a DEGREE', red, -8),
    );
};

figures['14d-rpb2'] = () => {
  const A = (s) => (Math.sqrt(3) / 4) * s * s;
  return panel('RPB2', 'A = (√3/4)s²', [0, 8], [0, 30], 'side s (cm)', 'A (cm²)')
    .add(
      curve.fn(A).on([0, 8]).color(green).stroke(2.6).n(200),
      chord(A, 2, 3), chord(A, 6, 7),
      rise(A, 2, 1, red), rise(A, 6, 1, orange),
      ...pin(3.1, A(2.5), '+1.7 cm²', red, 1.8),
      ...pin(7.05, A(6.5), '+5.2 cm²', orange, -2.6),
      bold(0.35, 27, "dA/ds = (√3/2)s", green),
    );
};

figures['14d-rpb3'] = () => {
  const t = (v) => 120 / v;
  return panel('RPB3', 't = 120/v', [0, 120], [0, 7], 'speed v (km/h)', 'trip time t (h)')
    .add(
      href(0),
      curve.fn(t).on([15, 120]).color(blue).stroke(2.6).n(300),
      ...pin(60, t(60), '2 h', red, 0.5),
      ...pin(90, t(90), '−2 min per km/h', orange, 0.5),
      bold(6, 6.3, "t' = −120/v²  (at v=60: −1/30 h per km/h)", blue),
      txt(6, 5.4, 'the minus says the duration number shrinks', '#8a8a8a'),
    );
};

figures['14d-rpb4'] = () => {
  const C = (w) => 3 * w;
  return panel('RPB4', 'C = 3w', [0, 5], [0, 16], 'weight w (kg)', 'cost C (dollars)')
    .add(
      curve.fn(C).on([0, 5]).color(blue).stroke(2.6).n(20),
      ...pin(2, C(2), 'C = 3w: 3 dollars/kg', blue, 1.2),
      bold(0.35, 14.4, 'the reverse reading: w = C/3, dw/dC = 1/3 kg/dollar', green),
      txt(0.35, 13.1, '3 × 1/3 = 1 — the two degrees are reciprocals', '#8a8a8a'),
    );
};

figures['14d-rpb5'] = () => {
  const d = (tt) => 4.9 * tt * tt;
  return panel('RPB5', 'd = 4.9t²', [0, 5], [0, 130], 't (s)', 'd (m)')
    .add(
      curve.fn(d).on([0, 5]).color(orange).stroke(2.6).n(200),
      chord(d, 1, 2), chord(d, 4, 5),
      rise(d, 1, 1, red), rise(d, 4, 1, red),
      ...pin(2.1, d(1.5), '≈14.7 m', red, 12),
      ...pin(4.6, d(4.5), '≈44.1 m', red, 12),
      bold(0.25, 118, "d' = 9.8t — the relation strengthens as it falls", orange),
    );
};

// ── RPA — 문제 5장 ─────────────────────────────────────────────────
figures['14d-rpa1'] = () => {
  const C = (x) => 0.02 * (80 * x + 2 * x * x);
  return panel('RPA1', 'C(x) = 0.02(80x + 2x²)', [0, 6], [0, 12], 'base side x (cm)', 'cost C (dollars)')
    .add(
      curve.fn(C).on([0, 6]).color(purple).stroke(2.6).n(120),
      chord(C, 5, 6), rise(C, 5, 1, red),
      ...pin(5.15, C(5.5), '+1.2 dollars per extra cm of base', red, -0.9),
      bold(0.2, 11, 'dC/dx = 0.02 × 60 = 1.2 dollars/cm', purple),
      txt(0.2, 10.1, 'the units chain: dollars/cm² × cm²/cm = dollars/cm', '#8a8a8a'),
    );
};

figures['14d-rpa2'] = () => {
  const V = (h) => (Math.PI * 9 * h) / 3;
  return panel('RPA2', 'V = 3πh (fixed base)', [0, 10], [0, 100], 'height h (m)', 'V (m³)')
    .add(
      curve.fn(V).on([0, 10]).color(blue).stroke(2.6).n(20),
      chord(V, 4, 7), rise(V, 4, 3, red),
      ...pin(5.5, V(5.5), "V' = 3π ≈ 9.42 m³/m", red, 9),
      txt(0.3, 90, 'constant degree: each extra metre stacks the same base disk', '#8a8a8a'),
    );
};

figures['14d-rpa3'] = () => {
  const P = (R) => 14400 / R;
  return panel('RPA3', 'P = V²/R with V = 120 locked', [30, 240], [40, 400], 'resistance R (Ω)', 'power P (W)')
    .add(
      curve.fn(P).on([36, 240]).color(blue).stroke(2.6).n(300),
      ...pin(60, P(60), "P'(60) = −4 W/Ω", red, 42),
      annotate.arrow(point(55, P(60) - 34), point(95, P(95) - 26)).color(red),
      bold(36, 366, 'more resistance, less power', blue),
      txt(36, 344, 'the other lock (R = 60 fixed) gives +4 W/V', '#8a8a8a'),
    );
};

figures['14d-rpa4'] = () => {
  const R = (p) => 200 * p - 5 * p * p;
  return panel('RPA4', 'R = 200p − 5p²', [0, 45], [0, 2200], 'price p (dollars)', 'revenue R (dollars)')
    .add(
      vref(20),
      curve.fn(R).on([0, 42]).color(cyan).stroke(2.6).n(200),
      ...pin(20, R(20), "R'(20) = 0 — the peak", red, 140),
      ...pin(35, R(35), "R'(35) = −150", orange, 140),
      bold(1.2, 2060, 'the driver is price, not time', cyan),
      txt(1.2, 1930, "R' hits zero at a place on the p-axis, not a moment", '#8a8a8a'),
    );
};

figures['14d-rpa5'] = () => {
  const g = (x) => x * x * x - 3 * x + 3;
  return panel('RPA5', 'g = x³ − 3x + 3', [0, 2], [0.5, 4], 'x', 'g (x)')
    .add(
      href(g(1)), vref(1),
      curve.fn(g).on([0, 2]).color(blue).stroke(2.6).n(200),
      ...pin(1, g(1), "g'(1) = 0 — flat here", red, 0.3),
      bold(0.06, 3.78, "g' = 3x² − 3 = 0 ⇒ x = 1", blue),
    );
};

// ── SN — 문제 10장 (부호 렌즈: f 는 위치, f' 는 방향) ─────────────
figures['14d-sn1'] = () => {
  const B = (t) => -800 + 50 * t;
  return panel('SN1', 'B = −800 + 50t', [-2, 20], [-900, 200], 't (days)', 'balance B (dollars)')
    .add(
      href(0), vref(16),
      curve.fn(B).on([0, 20]).color(blue).stroke(2.6).n(40),
      ...pin(10, B(10), '−300 (sits below)', red, 85),
      annotate.arrow(point(3, B(3) - 40), point(7, B(4.7) - 30)).color(red),
      bold(0.2, 150, "B' = +50 — climbing", red),
      txt(0.2, 58, 'crosses zero at t = 16; the degree never changes', '#8a8a8a'),
    );
};

figures['14d-sn2'] = () => {
  const T = (t) => 85 - 3 * t;
  return panel('SN2', 'T = 85 − 3t', [-1, 22], [0, 100], 't (min)', 'temperature T (°C)')
    .add(
      curve.fn(T).on([0, 21]).color(orange).stroke(2.6).n(40),
      ...pin(10, T(10), '55 °C (still hot)', red, 8),
      annotate.arrow(point(4, T(4) - 7), point(8, T(3.4) - 7)).color(red),
      bold(0.8, 92, "T' = −3 — cooling", red),
      txt(0.8, 82, 'reaches 25 °C at t = 20; the degree stays −3', '#8a8a8a'),
    );
};

figures['14d-sn3'] = () => {
  const f = (x) => x * x * x;
  return panel('SN3', 'f = x³', [-1.4, 1.4], [-2.4, 2.4], 'x', 'f (x)')
    .add(
      ...pin(0, 0, "f(0) = 0 and f'(0) = 0", red, 0.44),
      ...pin(0.1, f(0.1), '0.001', blue, 0.32),
      ...pin(-0.1, f(-0.1), '−0.001', blue, -0.34),
      bold(-1.33, 2.04, 'flat for an instant — nothing stops', blue),
      txt(-1.33, 1.7, 'the curve passes straight through and keeps rising', '#8a8a8a'),
    );
};

figures['14d-sn4'] = () => {
  const s = (t) => 5 + 20 * t - 4.9 * t * t;
  return panel('SN4', 's = 5 + 20t − 4.9t²', [0, 4.3], [0, 30], 't (s)', 'height s (m)')
    .add(
      vref(2.041), hor(s(2.041), 0.3, 3.7),
      curve.fn(s).on([0, 4.1]).color(orange).stroke(2.6).n(200),
      ...pin(2.041, s(2.041), 'v = 0 at 25.4 m up', red, 1.7),
      bold(0.25, 27, 'the process pauses; the height never vanishes', orange),
    );
};

figures['14d-sn5'] = () => {
  const f = (x) => x + 2, g = (x) => x - 5;
  return panel('SN5', 'f = x + 2, g = x − 5', [-1, 8], [-7, 6], 'x', 'f , g')
    .add(
      href(0),
      curve.fn(f).on([-0.6, 5.6]).color(blue).stroke(2.6).n(20),
      curve.fn(g).on([-0.6, 5.6]).color(red).stroke(2.6).n(20),
      ...pin(0, 2, 'f(0) = 2', blue, 0.55),
      ...pin(0, -5, 'g(0) = −5', red, -0.8),
      bold(-0.85, 5.1, "f' = g' = 1 — identical arrows", green),
      txt(-0.85, 4.3, 'direction is shared; position is not', '#8a8a8a'),
    );
};

figures['14d-sn6'] = () => {
  const s = (t) => t * t - 25;
  return panel('SN6', 's = t² − 25', [0, 6.5], [-30, 20], 't (s)', 'position s (m)')
    .add(
      href(0), vref(5),
      curve.fn(s).on([0, 6.5]).color(blue).stroke(2.6).n(160),
      ...pin(3, s(3), '−16 m (behind the line)', red, 3.5),
      ...pin(5, 0, 'crosses at t = 5 with v = 10', green, 4),
      bold(0.2, 16, 'v = 2t > 0 — moving forward the whole time', blue),
    );
};

figures['14d-sn7'] = () => {
  const B = (t) => -200 - 30 * t;
  return panel('SN7', 'B = −200 − 30t', [-1, 12], [-600, 60], 't (days)', 'balance B (dollars)')
    .add(
      href(0),
      curve.fn(B).on([0, 11]).color(red).stroke(2.6).n(30),
      ...pin(5, B(5), '−350 (below zero)', red, 50),
      annotate.arrow(point(2, B(2) + 34), point(8, B(8) + 34)).color(red),
      bold(0.2, 22, "B' = −30 — sinking deeper", red),
      txt(0.2, -60, 'the arrow stays −30 whether the debt is −200 or −2,000,000', '#8a8a8a'),
    );
};

figures['14d-sn8'] = () => {
  const f = (x) => (x - 1) ** 3 + 2;
  return panel('SN8', 'f = (x − 1)³ + 2', [0, 2], [1.4, 2.75], 'x', 'f (x)')
    .add(
      hor(2, 0.3, 1.7),
      curve.fn(f).on([0, 2]).color(purple).stroke(2.6).n(200),
      ...pin(1, 2, "f'(1) = 0, f(1) = 2", red, 0.17),
      bold(0.05, 2.66, 'flat — but neither a peak nor a valley', purple),
      txt(0.05, 2.55, 'f(0.9) = 1.999 and f(1.1) = 2.001', '#8a8a8a'),
    );
};

figures['14d-sn9'] = () => {
  const T = (t) => -10 + 0.5 * t;
  return panel('SN9', 'T = −10 + 0.5t', [-2, 30], [-14, 8], 't (min)', 'temperature T (°C)')
    .add(
      href(0), vref(20),
      curve.fn(T).on([0, 30]).color(cyan).stroke(2.6).n(30),
      ...pin(10, T(10), '−5 °C (below freezing)', red, 1.4),
      annotate.arrow(point(3, T(3) + 0.8), point(9, T(6) + 0.8)).color(red),
      bold(0.2, 6.4, "T' = +0.5 — warming", red),
      txt(0.2, 5.2, 'crosses 0 °C at t = 20; the degree stays +0.5', '#8a8a8a'),
    );
};

figures['14d-sn10'] = () => {
  const f = (x) => 1000 * x;
  return panel('SN10', 'f = 1000x', [-1, 2], [-600, 1600], 'x', 'f (x)')
    .add(
      href(0),
      curve.fn(f).on([-0.8, 1.4]).color(blue).stroke(2.6).n(20),
      ...pin(0, 0, "f(0) = 0 with f' = 1000", red, 190),
      bold(-0.9, 1500, 'a giant arrow at zero — and g = 100 has no arrow at all', blue),
      txt(-0.9, 1330, "the arrow's size is its own axis, in both directions", '#8a8a8a'),
    );
};


// ── JA — 문제 7장 (변수 감옥: 잠그는 글자가 관계를 고른다) ──────────
figures['14d-ja1'] = () => {
  const P = (R) => 14400 / R;
  return panel('JA1', 'P = V²/R, V = 120 locked', [30, 240], [40, 400], 'resistance R (Ω)', 'power P (W)')
    .add(
      curve.fn(P).on([36, 240]).color(blue).stroke(2.6).n(300),
      ...pin(60, P(60), "P'(60) = −4 W/Ω", red, 42),
      bold(36, 366, 'lock V: power fights resistance', blue),
      txt(36, 344, 'lock R instead and the same formula gives +4 W/V', '#8a8a8a'),
    );
};

figures['14d-ja2'] = () => {
  const T = (v) => 240 / v;
  return panel('JA2', 'T = 240/v', [0, 200], [0, 8], 'speed v (km/h)', 'duration T (h)')
    .add(
      href(0),
      curve.fn(T).on([30, 200]).color(orange).stroke(2.6).n(300),
      ...pin(80, T(80), "T'(80) = −0.0375 h/(km/h)", red, 0.75),
      bold(6, 7.2, 'T is a duration — a response, not the clock', orange),
      txt(6, 6.2, 'the flowing clock is s(t) = 80t, with s′ = +80 km/h', '#8a8a8a'),
    );
};

figures['14d-ja3'] = () => {
  const V = (t) => 100 - 2 * t;
  return panel('JA3', 'V = 100 − 2t', [0, 55], [0, 105], 't (min)', 'V (L)')
    .add(
      href(0),
      curve.fn(V).on([0, 50]).color(blue).stroke(2.6).n(40),
      ...pin(30, V(30), '40 L at t = 30 (a value)', red, 7),
      ...pin(50, 0, 'empties at 50 min', orange, 8),
      bold(1, 96, "V' = −2 L/min (a degree) — both live at the same instant", blue),
    );
};

figures['14d-ja4'] = () => {
  const P = (V) => 2490 / V;
  return panel('JA4', 'P = 2490/V with T = 300 locked', [3, 30], [0, 700], 'volume V (m³)', 'pressure P (kPa)')
    .add(
      curve.fn(P).on([3.6, 30]).color(purple).stroke(2.6).n(300),
      ...pin(10, P(10), "P'(10) = −24.9 kPa/m³", red, 70),
      bold(4, 640, 'locking T makes the relation reciprocal (V⁻¹)', purple),
      txt(4, 590, 'locking P instead gives V = 0.083T — a straight line', '#8a8a8a'),
    );
};

figures['14d-ja5'] = () => {
  const P = (tt) => 14400 / (60 + 0.2 * tt);
  return panel('JA5', 'R = 60 + 0.2t, so P(t)', [0, 120], [150, 245], 'heating time t (s)', 'power P (W)')
    .add(
      curve.fn(P).on([0, 120]).color(green).stroke(2.6).n(160),
      ...pin(0, P(0), "P'(0) = −4 W/Ω × 0.2 Ω/s = −0.8 W/s", red, 11),
      bold(4, 190, 'two degrees for one heater — chained by the 0.2 Ω/s', green),
      txt(4, 180, '−4 W/Ω is per ohm; −0.8 W/s is per second', '#8a8a8a'),
    );
};

figures['14d-ja6'] = () => {
  const t = (v) => 120 / v;
  return panel('JA6', 't = 120/v', [0, 200], [0, 7], 'speed v (km/h)', 'trip time t (h)')
    .add(
      href(0),
      curve.fn(t).on([18, 200]).color(blue).stroke(2.6).n(300),
      ...pin(60, t(60), 't(60) = 2 h (sits at +2)', red, 0.6),
      annotate.arrow(point(55, 2.35), point(80, 1.6)).color(red),
      bold(5, 6.3, 't is a duration, not a clock', blue),
      txt(5, 5.5, 'down forever, never below zero — the minus is the relation', '#8a8a8a'),
    );
};

figures['14d-ja7'] = () => {
  const T = (v) => 240 / v;
  return panel('JA7', 'T = 240/v (duration jail)', [0, 200], [0, 8], 'speed v (km/h)', 'duration T (h)')
    .add(
      href(0),
      curve.fn(T).on([30, 200]).color(orange).stroke(2.6).n(300),
      ...pin(80, T(80), "T'(80) = −2.25 min per km/h", red, 0.8),
      bold(6, 7.2, 'the minus lives in the duration jail only', orange),
      txt(6, 6.2, 'the clock jail s = 80t has s′ = +80 — no minus anywhere', '#8a8a8a'),
    );
};

// ── DC — 문제 10장 (기간 감옥: 총량 ÷ 비율 = 수명. 시계가 아니다) ────
//   모든 DC 는 같은 모양의 반비례 곡선이다. 문제마다 총량·비율·단위만 다르다.

figures['14d-dc1'] = () => {
  const T = (r) => 400 / r;
  return panel('DC1', 'T = 400/r minutes', [0, 60], [0, 28], 'drain rate r (L/min)', 'emptying time T (min)')
    .add(
      href(0), vref(20),
      curve.fn(T).on([15, 60]).color(orange).stroke(2.6).n(300),
      ...pin(20, T(20), 'T(20) = 20 min', red, 1.8),
      bold(2, 25.5, "T'(20) = −1 min per (L/min)", orange),
      txt(2, 23.6, 'r → 0⁺ sends T → +∞; r → ∞ sends T → 0⁺ (never below)', '#8a8a8a'),
    );
};

figures['14d-dc2'] = () => {
  const T = (P) => 60 / P;
  return panel('DC2', 'T = 60/P hours', [0, 30], [0, 26], 'power draw P (kW)', 'lifetime T (h)')
    .add(
      href(0), vref(6),
      curve.fn(T).on([2.6, 30]).color(orange).stroke(2.6).n(300),
      ...pin(6, T(6), 'T(6) = 10 h', red, 1.6),
      bold(0.6, 23.5, "T'(6) = −5/3 ≈ −1.67 h per kW", orange),
      txt(0.6, 21.8, 'a lifetime, not a clock — the number shrinks, time flows on', '#8a8a8a'),
    );
};

figures['14d-dc3'] = () => {
  const T = (p) => 300 / p;
  return panel('DC3', 'T = 300/p days', [0, 100], [0, 40], 'reading speed p (pages/day)', 'reading time T (days)')
    .add(
      href(0), vref(30),
      curve.fn(T).on([8, 100]).color(orange).stroke(2.6).n(300),
      ...pin(30, T(30), 'T(30) = 10 days', red, 2.4),
      bold(2, 36.5, "T'(30) = −1/3 day per (page/day) = −8 h", orange),
      txt(2, 34, 'duration, not clock: positive, sinking, never below zero', '#8a8a8a'),
    );
};

figures['14d-dc4'] = () => {
  const T = (b) => 5000 / b;
  return panel('DC4', 'T = 5000/b seconds', [0, 200], [0, 280], 'bandwidth b (MB/s)', 'download time T (s)')
    .add(
      href(0), vref(50),
      curve.fn(T).on([18, 200]).color(orange).stroke(2.6).n(300),
      ...pin(50, T(50), 'T(50) = 100 s', red, 15),
      bold(3, 258, "T'(50) = −2 s per (MB/s)", orange),
      txt(3, 240, 'each extra MB/s shaves 2 seconds — the clock never reverses', '#8a8a8a'),
    );
};

figures['14d-dc5'] = () => {
  const T = (d) => 1200 / d;
  return panel('DC5', 'T = 1200/d weeks', [0, 160], [0, 70], 'saving rate d (dollars/week)', 'saving time T (weeks)')
    .add(
      href(0), vref(40),
      curve.fn(T).on([18, 160]).color(orange).stroke(2.6).n(300),
      ...pin(40, T(40), 'T(40) = 30 weeks', red, 3.6),
      bold(2, 64, "T'(40) = −0.75 week per (dollar/week) ≈ −5 days", orange),
    );
};

figures['14d-dc6'] = () => {
  const T = (q) => 50 / q;
  return panel('DC6', 'T = 50/q hours', [0, 12], [0, 32], 'pump rate q (m³/h)', 'fill time T (h)')
    .add(
      href(0), vref(2.5),
      curve.fn(T).on([1.6, 12]).color(orange).stroke(2.6).n(300),
      ...pin(2.5, T(2.5), 'T(2.5) = 20 h', red, 2.2),
      bold(0.2, 29, "T'(2.5) = −8 h per (m³/h)", orange),
      txt(0.2, 26.8, 'a faster pump shortens the fill; it never reverses the clock', '#8a8a8a'),
    );
};

figures['14d-dc7'] = () => {
  const T = (v) => 42 / v;
  return panel('DC7', 'T = 42/v hours', [0, 30], [0, 12], 'running speed v (km/h)', 'race time T (h)')
    .add(
      href(0), vref(14),
      curve.fn(T).on([3.6, 30]).color(orange).stroke(2.6).n(300),
      ...pin(14, T(14), 'T(14) = 3 h', red, 0.9),
      bold(0.5, 10.9, "T'(14) = −3/14 h per (km/h) ≈ −13 min", orange),
    );
};

figures['14d-dc8'] = () => {
  const T = (n) => 1000 / n;
  return panel('DC8', 'T = 1000/n minutes', [0, 80], [0, 120], 'print speed n (pages/min)', 'print time T (min)')
    .add(
      href(0), vref(20),
      curve.fn(T).on([9, 80]).color(orange).stroke(2.6).n(300),
      ...pin(20, T(20), 'T(20) = 50 min', red, 7),
      bold(1, 111, "T'(20) = −2.5 min per (page/min)", orange),
      txt(1, 103, 'duration, not clock — the page count is what shrinks', '#8a8a8a'),
    );
};

figures['14d-dc9'] = () => {
  const V = (t) => 400 - 20 * t;
  return panel('DC9', 'V = 400 − 20t (clock jail)', [0, 22], [0, 420], 'flowing time t (min)', 'V (L)')
    .add(
      href(0),
      curve.fn(V).on([0, 20]).color(blue).stroke(2.6).n(40),
      ...pin(10, V(10), '200 L at t = 10', red, 26),
      bold(0.8, 390, "here t IS the clock: V' = −20 L/min", blue),
      txt(0.8, 366, 'the minus drains a volume — compare DC1, where it shrank a duration', '#8a8a8a'),
    );
};

figures['14d-dc10'] = () => {
  const T = (r) => 400 / r;
  return panel('DC10', 'T = 400/r, the limits', [0, 12], [0, 120], 'drain rate r (L/min)', 'emptying time T (min)')
    .add(
      href(0),
      curve.fn(T).on([3.4, 12]).color(orange).stroke(2.6).n(300),
      annotate.arrow(point(9.5, T(4) + 8), point(4.2, T(4) + 8)).color(orange),
      bold(3.6, 112, 'r → 0⁺ ⇒ T → +∞ (a stopped drain never empties)', orange),
      txt(3.6, 104, 'r → ∞ ⇒ T → 0⁺ — and no r > 0 ever gives T < 0', '#8a8a8a'),
    );
};

// ── JT — 문제 24장 (감옥 트랩 갤러리: 같은 'per'라도 자물쇠가 다르다) ──
//   JT1–JT6: 시간 관련 잠금 / JT7–JT16: 시간 밖의 패턴 / JT17–JT24: 드라이버가 시간이 아님
figures['14d-jt1'] = () => {
  const t = (v) => 120 / v;
  return panel('JT1', 'two 2s in one trip', [0, 200], [0, 7], 'speed v (km/h)', 'trip time t (h)')
    .add(
      href(0),
      curve.fn(t).on([18, 200]).color(blue).stroke(2.6).n(300),
      ...pin(60, t(60), 't(60) = 2 h — a VALUE', red, 0.65),
      bold(4, 6.2, "t'(60) = −2 min per (km/h) — a DEGREE", blue),
      txt(4, 5.4, 'same digit, different jails: the units are the jail’s ID card', '#8a8a8a'),
    );
};

figures['14d-jt2'] = () => {
  const T = (tt) => 85 - 3 * tt;
  return panel('JT2', 'the letter T, two jails', [-1, 26], [0, 100], 'minutes t', 'temperature T (°C)')
    .add(
      curve.fn(T).on([0, 25]).color(orange).stroke(2.6).n(40),
      ...pin(10, T(10), 'here T is temperature: −3 °C/min', red, 6),
      bold(0.8, 92, 'the letter carries nothing — the jail carries everything', orange),
      txt(0.8, 83, 'elsewhere T = 240/v is a duration: −0.0375 h per (km/h)', '#8a8a8a'),
    );
};

figures['14d-jt3'] = () => {
  const V = (tt) => 0.1 * tt;
  return panel('JT3', 'drip: V = 0.1t', [0, 60], [0, 8], 't (s)', 'V (mL)')
    .add(
      curve.fn(V).on([0, 60]).color(blue).stroke(2.6).n(20),
      ...pin(30, V(30), "V' = 0.1 mL/s — a degree", red, 0.7),
      bold(1, 7.2, '2 drops/s and 0.05 mL/drop are LOCKED parameters', blue),
      txt(1, 6.4, 'rates going in are not degrees coming out', '#8a8a8a'),
    );
};

figures['14d-jt4'] = () => {
  const T = (r) => 400 / r;
  return panel('JT4', 'the units name the jail', [0, 40], [0, 60], 'rate (L/min)', 'T (min) / flow')
    .add(
      curve.fn(T).on([8, 40]).color(orange).stroke(2.6).n(200),
      bold(1, 55, 'quantity per time = clock jail (L/min)', blue),
      txt(1, 49, 'time per rate = duration jail (min/(L/min))', orange),
      txt(1, 43, 'fingerprint: a duration jail has time on top of a rate', '#8a8a8a'),
    );
};

figures['14d-jt5'] = () => {
  const T = (v) => 120 / v;
  return panel('JT5', 'T = 120/v outside the bars', [-80, 140], [-6, 9], 'speed v (km/h)', 'trip time T (h)')
    .add(
      href(0),
      curve.fn(T).on([-80, -15]).color(gray).stroke(2).dash([6, 4]).n(120),
      curve.fn(T).on([15, 140]).color(blue).stroke(2.6).n(300),
      ...pin(-58, T(-58), 'T = −2 h here fails to be a duration', gray, 1.5),
      bold(20, 8, 'the model lives on v > 0; outside, the formula answers and the model is silent', blue),
    );
};

figures['14d-jt6'] = () => {
  const f = (v) => 1800 / v;
  return panel('JT6', 'fuel f = 1800/v for a 300 km trip', [0, 200], [0, 40], 'speed v (km/h)', 'fuel f (L)')
    .add(
      href(0),
      curve.fn(f).on([50, 200]).color(purple).stroke(2.6).n(300),
      ...pin(100, f(100), "f'(100) = −0.18 L per (km/h)", red, 4.4),
      bold(4, 36, '6 L/h is a locked rate; T′(v) is the duration jail', purple),
      txt(4, 32.5, 'the chain multiplies one jail’s degree into the other', '#8a8a8a'),
    );
};

figures['14d-jt7'] = () => {
  const V = (tt) => 5000000 - 30 * tt;
  return panel('JT7', 'reservoir: level vs flow', [0, 4000], [4800000, 5100000], 't (s)', 'V (m³)')
    .add(
      curve.fn(V).on([0, 3600]).color(blue).stroke(2.6).n(20),
      ...pin(1200, V(1200), "5,000,000 m³ is a LEVEL (a value)", blue, 55000),
      bold(40, 5060000, "V' = −30 m³/s is a FLOW (a degree)", red),
      txt(40, 5035000, 'same unit family, two jails — the "/s" is the ID card', '#8a8a8a'),
    );
};

figures['14d-jt8'] = () => {
  const e1 = (tt) => -50 + 3 * tt;
  const e2 = (tt) => -20 - 2 * tt;
  return panel('JT8', 'two submarines, two minus jobs', [0, 15], [-60, 10], 't (min)', 'elevation e (m)')
    .add(
      href(0),
      curve.fn(e1).on([0, 15]).color(blue).stroke(2.6).n(20),
      curve.fn(e2).on([0, 15]).color(red).stroke(2.6).n(20),
      ...pin(10.4, e1(10), '(i) −20 m, climbing', blue, 2.4),
      ...pin(10.4, e2(10), '(ii) −40 m, sinking deeper', red, -3.4),
      bold(0.4, 7, 'the minus in the value is depth; the minus in the degree is a direction', blue),
    );
};

figures['14d-jt9'] = () => {
  const q = (p) => 200 - 5 * p;
  return panel('JT9', 'q = 200 − 5p', [0, 50], [-40, 220], 'price p (dollars)', 'demand q (units)')
    .add(
      href(0), vref(40),
      curve.fn(q).on([0, 40]).color(blue).stroke(2.6).n(20),
      curve.fn(q).on([40, 48]).color(gray).stroke(2).dash([6, 4]).n(20),
      ...pin(45, q(45), 'q(45) = −25 — outside the model', gray, 16),
      bold(1, 196, "q' = −5: price and demand move oppositely", blue),
      txt(1, 178, 'a direction, not negative customers', '#8a8a8a'),
    );
};



figures['14d-jt10'] = () => {
  const f = (d) => 0.08 * d;
  return panel('JT10', 'f = 0.08d (8 L per 100 km)', [0, 500], [0, 44], 'distance d (km)', 'fuel f (L)')
    .add(
      curve.fn(f).on([0, 500]).color(blue).stroke(2.6).n(20),
      ...pin(250, f(250), '0.08 L/km — driver is km, response is L', red, 3.2),
      bold(6, 40, 'read backwards: dd/df = 12.5 km/L — driver is L', green),
      txt(6, 36.5, '0.08 × 12.5 = 1 — the reader swapped the drivers, not the car', '#8a8a8a'),
    );
};

figures['14d-jt11'] = () => {
  const B = (tt) => 1000 * Math.exp(0.05 * tt);
  return panel('JT11', 'balance earning 5% per year', [0, 20], [0, 2800], 'years t', 'balance B (dollars)')
    .add(
      curve.fn(B).on([0, 20]).color(green).stroke(2.6).n(200),
      ...pin(0, 1000, "at B = 1000: B' = 0.05 × 1000 = 50 dollars/yr", red, 240),
      bold(1, 2450, 'the 5% is a LOCKED parameter; the 50 is a DEGREE', green),
      txt(1, 2250, '0.05 appears twice — input rate and output rate', '#8a8a8a'),
    );
};

figures['14d-jt12'] = () => {
  const P = (V) => 2490 / V;
  return panel('JT12', 'P, two jails: pressure or power', [3, 30], [0, 700], 'volume V (m³) / resistance R (Ω)', 'P')
    .add(
      curve.fn(P).on([3.6, 30]).color(purple).stroke(2.6).n(300),
      ...pin(10, P(10), "P'(10) = −24.9 kPa/m³ (pressure)", red, 72),
      bold(4, 640, "elsewhere P'(60) = −4 W/Ω (power)", purple),
      txt(4, 592, 'kPa/m³ vs W/Ω — the units are the ID card, P is just ink', '#8a8a8a'),
    );
};

figures['14d-jt13'] = () => {
  const R = (p) => 200 * p - 5 * p * p;
  return panel('JT13', 'R = 200p − 5p²', [0, 45], [0, 2200], 'price p (dollars)', 'revenue R (dollars)')
    .add(
      href(0), vref(20),
      curve.fn(R).on([0, 42]).color(blue).stroke(2.6).n(200),
      ...pin(20, R(20), "R'(20) = 0 at R = 2000 — a pause, not a zero", red, 150),
      ...pin(30, R(30), "R(30) = 1500, R' = −100", orange, 150),
      bold(1, 2060, 'flat at the top; the value is still large', blue),
    );
};

figures['14d-jt14'] = () => {
  const V = (h) => Math.PI * 4 * h;
  return panel('JT14', 'cylinder V = πr²h, r = 2 locked', [0, 14], [0, 180], 'height h (m)', 'V (m³)')
    .add(
      curve.fn(V).on([0, 14]).color(blue).stroke(2.6).n(20),
      ...pin(7, V(7), "dV/dh = πr² = 4π ≈ 12.6 m³/m", red, 12),
      bold(0.4, 168, 'lock r instead: dV/dr = 2πrh = 40π ≈ 125.7 — a shell', blue),
      txt(0.4, 154, 'the frame question picks the driver', '#8a8a8a'),
    );
};

figures['14d-jt15'] = () => {
  const f = (d) => 0.08 * d;
  return panel('JT15', '8 L per 100 km vs 50 L tank', [0, 300], [0, 60], 'distance d (km)', 'f (L)')
    .add(
      href(50),
      curve.fn(f).on([0, 300]).color(blue).stroke(2.6).n(20),
      ...pin(150, f(150), '12 L used — a VALUE along the line', blue, 3.4),
      bold(8, 46, '"per" marks the degree (8 L per 100 km)', green),
      txt(8, 40, 'a bare "50 L" is a value — a position, no denominator', '#8a8a8a'),
    );
};

figures['14d-jt16'] = () => {
  const s = (tt) => 80 * tt;
  return panel('JT16', 'odometer vs speedometer', [0, 6], [0, 520], 'hours t', 's (km)')
    .add(
      curve.fn(s).on([0, 6]).color(green).stroke(2.6).n(20),
      ...pin(1.5, s(1.5), '120 km — the odometer (a value)', green, 42),
      bold(0.25, 470, '80 km/h — the speedometer (a degree)', blue),
      txt(0.25, 430, 'same word "drove", two jails', '#8a8a8a'),
    );
};

figures['14d-jt17'] = () => {
  const P = (h) => 101 - 12 * h;
  return panel('JT17', 'air pressure P = 101 − 12h', [0, 10], [0, 110], 'altitude h (km)', 'P (kPa)')
    .add(
      href(0), vref(101 / 12),
      curve.fn(P).on([0, 8.4]).color(blue).stroke(2.6).n(20),
      ...pin(2, P(2), 'P(2) = 77 kPa > 0', red, 8),
      bold(0.2, 100, "P' = −12 kPa/km — the driver is a PLACE, not a clock", blue),
      txt(0.2, 92, 'P = 0 at h ≈ 8.42 km — the model’s edge, not "anti-pressure"', '#8a8a8a'),
    );
};

figures['14d-jt18'] = () => {
  const q = (p) => 200 - 5 * p;
  return panel('JT18', 'q = 200 − 5p, driver is price', [0, 45], [0, 220], 'price p (dollars)', 'demand q (units)')
    .add(
      curve.fn(q).on([0, 40]).color(blue).stroke(2.6).n(20),
      ...pin(20, q(20), "q' = −5 units per dollar", red, 14),
      bold(0.8, 200, 'per dollar, not per second — the denominator is the jail', blue),
      txt(0.8, 183, 'the driver’s jail IS the sentence’s tense', '#8a8a8a'),
    );
};


figures['14d-jt19'] = () => {
  const A = (r) => Math.PI * r * r;
  return panel('JT19', 'circle A = πr²', [0, 8], [0, 210], 'radius r (m)', 'A (m²)')
    .add(
      curve.fn(A).on([0, 8]).color(green).stroke(2.6).n(200),
      ...pin(3, A(3), "A'(3) = 2πr ≈ 18.8 m² per metre", red, 26),
      bold(0.4, 196, 'the driver is a LENGTH — no seconds in the formula', green),
      txt(0.4, 180, 'time enters only when r itself depends on t (chain rule)', '#8a8a8a'),
    );
};

figures['14d-jt20'] = () => {
  const V = (T) => 0.083 * T;
  return panel('JT20', 'gas V = 0.083T at fixed pressure', [0, 400], [0, 36], 'temperature T (K)', 'V (m³)')
    .add(
      curve.fn(V).on([0, 400]).color(orange).stroke(2.6).n(20),
      ...pin(300, V(300), "V'(T) = 0.083 m³/K", red, 3.6),
      bold(12, 33, 'per kelvin, not per second — a static trade', orange),
      txt(12, 30, 'V′(t) would need T(t) chained in', '#8a8a8a'),
    );
};

figures['14d-jt21'] = () => {
  const f = (d) => 0.08 * d;
  return panel('JT21', 'f = 0.08d', [0, 300], [0, 26], 'distance d (km)', 'fuel f (L)')
    .add(
      curve.fn(f).on([0, 300]).color(blue).stroke(2.6).n(20),
      ...pin(150, f(150), '0.08 L per km — the denominator is km', red, 2),
      bold(8, 23.5, 'identical digits 0.08 — km vs s changes the sentence', blue),
      txt(8, 21.5, 'the jail is the denominator', '#8a8a8a'),
    );
};

figures['14d-jt22'] = () => {
  const R = (x) => 2 * x - 0.05 * x * x;
  return panel('JT22', 'response R = 2x − 0.05x²', [0, 40], [0, 22], 'dose x (mg)', 'response R')
    .add(
      vref(20),
      curve.fn(R).on([0, 40]).color(purple).stroke(2.6).n(200),
      ...pin(10, R(10), "R'(10) = 1 per mg", red, 1.8),
      ...pin(20, R(20), "R'(20) = 0 — peaks at 20 mg", orange, 1.8),
      bold(1, 20.4, 'the driver is dose — an amount, not a moment in time', purple),
    );
};

figures['14d-jt23'] = () => {
  const P = (d) => 101 + 9.8 * d;
  return panel('JT23', 'water pressure P = 101 + 9.8d', [0, 50], [90, 610], 'depth d (m)', 'P (kPa)')
    .add(
      curve.fn(P).on([0, 50]).color(blue).stroke(2.6).n(20),
      ...pin(0, 101, 'at the surface: 101 kPa, arrow +9.8', red, 34),
      bold(2, 570, "P' = 9.8 kPa/m — the driver is a PLACE", blue),
      txt(2, 535, 'pressure does not flow deeper; depth drives it', '#8a8a8a'),
    );
};

figures['14d-jt24'] = () => {
  const C = (q) => 400 + 2 * q;
  return panel('JT24', 'C = 400 + 2q', [0, 150], [0, 760], 'quantity q (units)', 'cost C (dollars)')
    .add(
      curve.fn(C).on([0, 150]).color(green).stroke(2.6).n(20),
      ...pin(0, 400, '400 = the fixed cost (a VALUE)', green, 46),
      bold(4, 720, '2 dollars/unit is a DEGREE — per unit, not per hour', blue),
      txt(4, 680, 'value and degree side by side in one formula', '#8a8a8a'),
    );
};


export { figures };
