// math/graph/phase2/14D1-derivative-interpretation.mjs — 세션 14D1(도함수의 해석) 그림
//
// ── figure 목록 (키 = 출력 파일명 = 마크다운 태그 id) ──────────────
//   아래 순서 = 마크다운 등장 순서. 캡션 번호(Graph 14D1-n)도 이 순서를 따른다.
//    14d1-03-linearization       (1×2) √x 의 x=4 접선 + x=4.1 확대 (오차 1.5e−4)
//    14d1-08-sign-story          (1×2) f′ 그래프를 두 번 읽기 — 높이=방향, 기울기=휨
//    14d1-09-cube-driver         (1×2) 정육면체: dV/ds = 3s² vs 반변 u=s/2 → 6s²
//    14d1-04-circle-ring         (1×1) 원판 링: A′(r) = 2πr (둘레)
//    14d1-05-sphere-shell        (3D)  구 껍질: V′(r) = 4πr² (표면적)
//    14d1-06-marginal-cost       (1×2) C(q) 접선 = 한계비용, MC 와 AC 의 교차
//    14d1-10-energy-two-meanings (1×2) K = ½mv²: dK/dv = mv(운동량) vs dK/dt = Fv(일률)
//    14d1-07-elasticity          (1×2) 탄력/비탄력 구간 + 매출 최대 (E = −1)
//    14d1-11-motion-signs        (1×2) v 와 a 의 부호 — 빨라짐/느려짐 판별
//
// ── 사용한 확장 (코어 수정 0, 전부 _helpers 의 얇은 별칭 · 기준 logos 0.4.1) ────────
//   곡선 = 코어 `curve.fn` · 링 = 코어 `region.annulus` · 부호 띠 = 코어 `region.bar`
//   구 = 코어 `sphere`(3D)          · 등각 상자 = 코어 `polygon`
//   색 = 코어 `kit.palette` 이름    · 좁은 범위 눈금 = 0.4.1 의 tick-step 자릿수 유도
import { circle, polygon, region, sphere } from '@jaywoo0830a/logos';
import {
  palette,
  BLUE, ORANGE, GREEN, RED, PURPLE, GRAY, LIGHT, ASYMP,
  curveOf, segAt, markerAt, dotAt, labelAt, vlineAt, hlineAt, legendAt, barAt,
  s2p, plot3d, pair, single, AX, OFF, PANEL, P,
} from './_helpers.mjs';

// ── ① 선형화: √x 를 x=4 의 접선으로 ──────────────────────────────
//   왼쪽: 전체 — 접선과 곡선이 거의 붙어 보인다(그게 요점이다).
//   오른쪽: x=4.1 확대 — 두 선이 벌어진 폭이 곧 근사 오차.
function linearization() {
  const f = Math.sqrt;
  const L = (x) => 2 + (x - 4) / 4;

  const left = s2p([0, 9], [0, 3.4], PANEL, { axes: AX('x', 'y'), grid: { alpha: 0.25 } })
    .title('f(x) = √x  and its tangent at x = 4')
    .add(
      curveOf(f, [0, 9], { color: BLUE, stroke: 2.6, n: 240 }),
      curveOf(L, [0, 9], { color: RED, stroke: 1.8, dash: [6, 4], n: 2 }),
      vlineAt(4, { color: ASYMP, stroke: 1, dash: [4, 4] }),
      dotAt([4, 2], RED, 4.5),
      legendAt([1.1, 3.25], 'L(x) = 2 + (x − 4)/4', RED, { font: 10 }),
      labelAt([4.15, 0.35], 'touch point x = 4', { color: RED, font: 9.5 }),
    );

  // 0.4.1 의 눈금 정밀도 수정(`fmtTick` 이 tick step 에서 자릿수를 유도) 덕분에 좁은 범위
  // (폭 0.012)에서도 y 눈금이 "2.02" 로 뭉개지지 않는다 → 예전처럼 눈금을 끌 필요가 없다.
  // (자릿수를 직접 정하고 싶으면 `axes({ y: { decimals: n } })`.)
  const right = s2p([4.08, 4.12], [2.019, 2.031], PANEL, {
    axes: { x: { label: 'x' }, y: { label: 'y' } },
    grid: { alpha: 0.25 },
  })
    .title('Zoom at x = 4.1   (gap ≈ 1.5 × 10⁻⁴)')
    .add(
      curveOf(f, [4.08, 4.12], { color: BLUE, stroke: 2.4, n: 120 }),
      curveOf(L, [4.08, 4.12], { color: RED, stroke: 1.8, dash: [6, 4], n: 2 }),
      segAt([4.1, f(4.1)], [4.1, L(4.1)], { color: GRAY, stroke: 1.6 }),
      markerAt([4.1, L(4.1)], RED, { open: true, size: 4.5 }),
      markerAt([4.1, f(4.1)], BLUE, { size: 4.5 }),
      labelAt([4.1002, 2.0288], 'L(4.1) = 2.025', { color: RED, font: 9.5 }),
      labelAt([4.1002, 2.0207], '√4.1 = 2.024846', { color: BLUE, font: 9.5 }),
      labelAt([4.09, 2.02485], 'error ≈ 1.5 × 10⁻⁴', { color: GRAY, font: 9, anchor: 'end' }),
    );

  return pair(left, right, 'Linearization — the tangent is the best linear model');
}

// ── ② 원판의 링: A′(r) = 2πr = 둘레 ─────────────────────────────
//   두께 dr 짜리 링의 넓이가 곧 "둘레 × dr" — 넓이를 미분하면 경계가 나온다.
function circleRing() {
  const O = P([0, 0]);
  const r = 2, dr = 0.22;

  const panel = s2p([-3.0, 3.6], [-2.8, 2.8], [560, 460], {
    axes: AX('x', 'y'), grid: { alpha: 0.2 }, equal: true,
  })
    .title('Ring of width dr :  ΔA ≈ 2πr · dr')
    .add(
      region.annulus(O, r, r + dr).fill(BLUE).opacity(0.28),
      circle.center(O).radius(r).color(BLUE).stroke(2.2),
      circle.center(O).radius(r + dr).color(BLUE).stroke(1.4).dash([5, 3]),
      segAt([0, 0], [r, 0], { color: RED, stroke: 1.8 }),
      dotAt([0, 0], RED, 4),
      markerAt([r, 0], BLUE, { size: 4 }),
      markerAt([r + dr, 0], BLUE, { open: true, size: 4 }),
      labelAt([1.0, 0.16], 'r', { color: RED, bold: true, font: 12 }),
      labelAt([2.14, 0.62], 'dr', { color: BLUE, font: 10 }),
      labelAt([-2.75, 2.5], 'A(r) = πr²', { color: GRAY, font: 10 }),
      labelAt([-2.75, 2.2], "A′(r) = 2πr  =  circumference", { color: BLUE, font: 10, bold: true }),
      labelAt([-2.75, 1.9], 'the ring is a stretched circumference', { color: GRAY, font: 9.5 }),
    );

  return single(panel, 'Differentiating the Area Gives the Circumference');
}


// ── ③ 구 껍질 (3D): V′(r) = 4πr² = 표면적 ───────────────────────
//   코어 3D 패널은 annotate/segment/marker 도 ctx.project 로 함께 투영한다 —
//   그래서 라벨·반지름 화살표를 3D 좌표로 주면 구 위에 정확히 얹힌다.
//   (Sphere.toIR 는 라벨을 범례(legendIR)로 보내므로 라벨은 직접 찍는다.)
function sphereShell() {
  const r = 2.0, dr = 0.30;

  const panel = plot3d({ elev: 14, azim: -52, size: [560, 440] })
    .title('Shell of thickness dr :  ΔV ≈ 4πr² · dr')
    .add(
      // ① 바깥 구(r+dr)를 먼저 깔아 '껍질 띠'를 만든다 — 옅은 채움 + 얇은 점선
      sphere.center(P([0, 0, 0])).radius(r + dr).fill(palette.skyblue).opacity(0.45)
        .color(palette.steel).stroke(0.9).dash([4, 3]),
      // ② 안쪽 구(r)를 나중에 그려 진한 공이 위로 온다 → 가장자리에 halo(껍질)가 남는다
      sphere.center(P([0, 0, 0])).radius(r).fill(BLUE).opacity(0.26)
        .color(palette.skyblue).stroke(1.6),
      // ③ 반지름 r 과 껍질 두께 dr 을 같은 방향에 나란히
      segAt([0, 0, 0], [r, 0, 0], { color: RED, stroke: 1.8 }),
      segAt([r, 0, 0], [r + dr, 0, 0], { color: PURPLE, stroke: 1.8 }),
      dotAt([0, 0, 0], RED, 3.5),
      labelAt([r * 0.52, 0, 0.14], 'r', { color: RED, bold: true, font: 12 }),
      labelAt([r + dr * 0.5, 0, -0.1], 'dr', { color: PURPLE, font: 10.5 }),
      labelAt([0, 0, r + 0.42], 'r + dr', { color: PURPLE, font: 10.5, bold: true }),
      // ④ 설명 3줄 — 같은 3D 앵커에 px 오프셋(dy)으로 쌓아 겹침을 막는다
      labelAt([-2.15, -1.75, 0], 'V(r) = 4/3 πr³', { color: GRAY, font: 10, dy: -30 }),
      labelAt([-2.15, -1.75, 0], "V′(r) = 4πr²  =  surface area", { color: BLUE, font: 10.5, bold: true, dy: -14 }),
      labelAt([-2.15, -1.75, 0], 'the shell is a stretched surface', { color: GRAY, font: 9.5, dy: 0 }),
    );

  return single(panel, 'Differentiating the Volume Gives the Surface Area');
}

// ── ④ 한계비용 = 접선의 기울기, AC 와의 교차 ────────────────────
//   왼쪽: C(q) 위 q=12 의 접선 — 그 기울기가 "다음 한 단위"의 값.
//   오른쪽: MC 와 AC — 평균비용의 최소점에서 정확히 만난다.
function marginalCost() {
  const C = (q) => q * q + 4 * q + 144;
  const q0 = 12, MC0 = 2 * q0 + 4;          // C′(12) = 28
  const LEFT_X = [0, 22], LEFT_Y = [0, 750];

  const left = s2p(LEFT_X, LEFT_Y, PANEL, { axes: AX('quantity q (units)', 'cost C ($)'), grid: { alpha: 0.25 } })
    .title('C(q) = q² + 4q + 144  —  tangent at q = 12')
    .add(
      curveOf(C, LEFT_X, { color: GREEN, stroke: 2.6, n: 200 }),
      curveOf((q) => MC0 * q, [4, 21], { color: RED, stroke: 1.8, dash: [6, 4], n: 2 }),
      dotAt([q0, C(q0)], RED, 4.5),
      labelAt([12.4, 200], "C'(12) = 28 $/unit", { color: RED, bold: true, font: 10.5 }),
      legendAt([2.6, 700], 'slope here = price of the NEXT unit', RED, { font: 9.5 }),
      labelAt([0.4, 715], 'C ($)', { color: GRAY, font: 9.5 }),
      labelAt([11, 90], 'q (units)', { color: GRAY, font: 9.5, anchor: 'middle' }),
    );

  const MC = (q) => 2 * q + 4;
  const AC = (q) => q + 4 + 144 / q;
  const right = s2p([3, 22], [0, 60], PANEL, { axes: AX('quantity q (units)', '$ / unit'), grid: { alpha: 0.25 } })
    .title('MC crosses AC at the minimum of AC')
    .add(
      curveOf(MC, [3, 22], { color: RED, stroke: 2.4, n: 200 }),
      curveOf(AC, [3, 22], { color: BLUE, stroke: 2.4, n: 200 }),
      vlineAt(q0, { color: ASYMP, stroke: 1, dash: [4, 4] }),
      dotAt([q0, MC0], PURPLE, 5),
      labelAt([5.6, 53], 'MC = 2q + 4', { color: RED, bold: true, font: 10.5 }),
      labelAt([6.0, 46], 'AC = q + 4 + 144/q', { color: BLUE, bold: true, font: 10.5 }),
      labelAt([13.2, 35.5], 'meet at q = 12  ($28)', { color: PURPLE, bold: true, font: 10 }),
      labelAt([13, 12], "AC'(12) = 0 — the average stops falling", { color: GRAY, font: 9 }),
      labelAt([21.5, 56], '$ / unit', { color: GRAY, font: 9.5, anchor: 'end' }),
      labelAt([12.5, 6.5], 'q (units)', { color: GRAY, font: 9.5, anchor: 'middle' }),
    );

  return pair(left, right, 'Marginal Cost — the Cost of the Next Unit');
}

// ── ⑤ 탄력성: 매출이 최대가 되는 가격 ──────────────────────────
//   왼쪽: 수요곡선 위 |E| = 1 인 점(p = 25)을 경계로 비탄력/탄력 구간.
//   오른쪽: 매출 R(p) — 같은 p = 25 에서 최대. E = −1 ⇔ R′ = 0.
function elasticity() {
  const q = (p) => 500 - 10 * p;            // 수요
  const R = (p) => 500 * p - 10 * p * p;    // 매출 = p · q(p)
  const pStar = 25, qStar = q(pStar), rStar = R(pStar);   // E = −1, R 최대 = 6250

  const left = s2p([0, 50], [0, 520], PANEL, { axes: AX('price p ($)', 'quantity q'), grid: { alpha: 0.25 } })
    .title('Demand q(p) = 500 − 10p')
    .add(
      region.between(0, q).on([0, pStar]).fill(BLUE).opacity(0.12),    // |E| < 1
      region.between(0, q).on([pStar, 50]).fill(RED).opacity(0.12),    // |E| > 1
      curveOf(q, [0, 50], { color: BLUE, stroke: 2.6, n: 2 }),
      vlineAt(pStar, { color: ASYMP, stroke: 1, dash: [4, 4] }),
      dotAt([pStar, qStar], PURPLE, 5),
      labelAt([7, 300], 'inelastic  (|E| < 1)', { color: BLUE, bold: true, font: 10 }),
      labelAt([48, 480], 'elastic  (|E| > 1)', { color: RED, bold: true, font: 10, anchor: 'end' }),
      labelAt([pStar + 0.6, 150], 'E = −1  at p = 25', { color: PURPLE, bold: true, font: 10 }),
    );

  const right = s2p([0, 50], [0, 6600], PANEL, { axes: AX('price p ($)', 'revenue R ($)'), grid: { alpha: 0.25 } })
    .title('Revenue R(p) = 500p − 10p²')
    .add(
      curveOf(R, [0, 50], { color: GREEN, stroke: 2.6, n: 200 }),
      region.between(0, R).on([0, pStar]).fill(BLUE).opacity(0.10),
      region.between(0, R).on([pStar, 50]).fill(RED).opacity(0.10),
      vlineAt(pStar, { color: ASYMP, stroke: 1, dash: [4, 4] }),
      dotAt([pStar, rStar], PURPLE, 5),
      labelAt([pStar + 1.2, 6320], 'R = 6250 max', { color: PURPLE, bold: true, font: 10.5 }),
      labelAt([26.8, 4600], "R'(p) = 500 − 20p = 0", { color: GRAY, font: 9.5 }),
      labelAt([5, 900], 'raise price → revenue up', { color: BLUE, font: 9 }),
      labelAt([47, 900], 'raise price → revenue down', { color: RED, font: 9, anchor: 'end' }),
    );

  return pair(left, right, 'Elasticity — Where a Price Hike Still Raises Revenue');
}

// ── ⑥ f′ 그래프를 두 번 읽기: 높이 = 방향, 기울기 = 휨 ──────────
//   왼쪽: f′ 의 부호를 사분면 띠로 표시(f′ < 0 → f 는 내려간다).
//   오른쪽: 그 f′ 를 적분해 복원한 f — 최소점과 볼록성이 그대로 보인다.
//   (예: f′ = 2x − 4 ⇒ f = x² − 4x + C. 상수 C 는 그림만 위아래로 옮긴다.)
function signStory() {
  const fp = (x) => 2 * x - 4;              // f′
  const f = (x) => x * x - 4 * x;           // f′(= 2x − 4) 의 한 원시함수 (C = 0)
  const x0 = 2;                             // f′(x0) = 0

  const left = s2p([-1.5, 5.5], [-9, 9], PANEL, { axes: AX('x', 'f′(x)'), grid: { alpha: 0.25 } })
    .title('Read by height — the sign of f′ is the direction of f')
    .add(
      barAt(-1.5, x0, -9, 0, RED, 0.07),    // f′ < 0 인 사분면
      barAt(x0, 5.5, 0, 9, BLUE, 0.07),     // f′ > 0 인 사분면
      hlineAt(0, { color: ASYMP, stroke: 1 }),
      curveOf(fp, [-1.5, 5.5], { color: BLUE, stroke: 2.6, n: 2 }),
      vlineAt(x0, { color: ASYMP, stroke: 1, dash: [4, 4] }),
      dotAt([x0, 0], PURPLE, 4.5),
      labelAt([0.35, 7.7], 'f′(x) = 2x − 4', { color: BLUE, bold: true, font: 10.5 }),
      labelAt([0.35, 6.4], 'slope = 2  →  f″ = 2 > 0', { color: GRAY, font: 9.5 }),
      labelAt([0.35, -7.7], 'f′ < 0  →  f falls', { color: RED, bold: true, font: 10 }),
      labelAt([2.3, 6.8], 'f′ > 0  →  f rises', { color: BLUE, bold: true, font: 10 }),
      labelAt([2.2, -1.8], 'f′(2) = 0  →  f is flat', { color: PURPLE, font: 9.5 }),
    );

  const right = s2p([-0.9, 5], [-5.5, 6.5], PANEL, { axes: AX('x', 'f(x)'), grid: { alpha: 0.25 } })
    .title('Read by slope — f′ rising means f bends upward')
    .add(
      curveOf(f, [-0.9, 5], { color: GREEN, stroke: 2.6, n: 200 }),
      segAt([0.6, -4], [3.4, -4], { color: RED, stroke: 1.8, dash: [6, 4] }),   // 최소점의 접선
      vlineAt(2, { color: ASYMP, stroke: 1, dash: [4, 4] }),
      dotAt([2, -4], GREEN, 4.5),
      labelAt([0.15, 6.0], 'f(x) = x² − 4x  (the +C is free)', { color: GREEN, bold: true, font: 10.5 }),
      labelAt([0.15, 5.0], 'falls → rises: minimum at x = 2', { color: GRAY, font: 9.5 }),
      labelAt([2.15, -3.2], "f′ = 0 and f″ > 0  →  minimum", { color: PURPLE, font: 9.5 }),
      labelAt([0.62, -4.75], 'tangent: slope 0', { color: RED, font: 9 }),
    );

  return pair(left, right, "The Story of f′ — Height Tells Direction, Slope Tells Bending");
}


// ── ⑦ 정육면체: 같은 상자, 두 가지 driver ────────────────────────
//   V = s³  →  dV/ds = 3s² : 변 s 를 존중하면 법선이 +x·+y·+z 인 면 3장만 밀린다.
//   u = s/2 →  V = 8u³ → dV/du = 24u² = 6s² : 반변 u 를 존중하면 6장 모두가 경계다.
//   사선(등각) 투영은 코어 polygon 만으로 충분하다 — z 축만 화면에서 (0.45, 0.30) 어긋난다.
const ISO = (x, y, z) => [x + 0.45 * z, y + 0.30 * z];

/** 정육면체(한 변 s)의 한 면을 등각 투영한 polygon. axis ∈ {x,y,z} 는 고정 축, at = 0 | s */
const cubeFace = (s, axis, at, { fill, opacity, dash, color, stroke } = {}) => {
  const corner = (a, b) => {
    const [x, y, z] = { x: [at, a, b], y: [a, at, b], z: [a, b, at] }[axis];
    return P(ISO(x, y, z));
  };
  let q = polygon(corner(0, 0), corner(s, 0), corner(s, s), corner(0, s));
  if (fill !== undefined) q = q.fill(fill);
  if (opacity !== undefined) q = q.opacity(opacity);
  if (dash !== undefined) q = q.dash(dash);
  if (color !== undefined) q = q.color(color);
  if (stroke !== undefined) q = q.stroke(stroke);
  return q;
};

function cubeDriver() {
  const s = 2;
  // 면 음영 — 세 면을 서로 다른 색으로 칠하지 않고 **같은 팔레트 색 + 면별 opacity** 로 구분한다.
  const FACE = palette.skyblue;
  //  이 투영에서 보이는 면 = z=0(앞) · x=s(오른쪽) · y=s(위)
  //  가려진 면 = x=0 · y=0 · z=s  → 뒤에서 앞 순으로 그려 겹침 순서를 만든다
  const FACES = [
    { axis: 'x', at: 0, hidden: true }, { axis: 'y', at: 0, hidden: true }, { axis: 'z', at: s, hidden: true },
    { axis: 'z', at: 0, hidden: false }, { axis: 'x', at: s, hidden: false }, { axis: 'y', at: s, hidden: false },
  ];

  /** driver = 'side'(dV/ds) → 면 3장만, 'half'(dV/du, u = s/2) → 6장 모두가 밀린다 */
  const box = (driver, title, lines) => {
    const slabs = FACES.map((f) => {
      const tinted = driver === 'half' || f.at === s;
      if (!tinted) return cubeFace(s, f.axis, f.at, { fill: 'none', color: palette.steel, stroke: 1.2 });
      return cubeFace(s, f.axis, f.at, {
        fill: FACE,
        opacity: f.hidden ? 0.35 : 0.85,
        dash: f.hidden ? [5, 4] : undefined,
        color: f.hidden ? LIGHT : palette.steel,
        stroke: f.hidden ? 1 : 1.4,
      });
    });
    return s2p([-0.8, 4.6], [-0.5, 3.655], PANEL, { ...OFF, equal: true })
      .title(title)
      .add(...slabs, ...lines);
  };

  const left = box('side', 'dV/ds = 3s² — respect the side s', [
    labelAt([-0.75, 3.5], 'only 3 faces move (normals +x, +y, +z)', { color: BLUE, bold: true, font: 10 }),
    labelAt([-0.75, 3.12], 'dV/ds collects 3s² — three faces of area s²', { color: GRAY, font: 9.5 }),
    labelAt([-0.75, -0.25], 'front face stays put; dashed = the hidden face at z = s', { color: GRAY, font: 9 }),
  ]);

  const right = box('half', 'dV/du = 24u² = 6s² — respect the half-side u = s/2', [
    labelAt([-0.75, 3.5], 'all 6 faces move — two per direction', { color: GREEN, bold: true, font: 10 }),
    labelAt([-0.75, 3.12], 'a half-side step pushes both faces of every pair', { color: GRAY, font: 9.5 }),
    labelAt([-0.75, -0.25], 'front face moves too: 6s² appears only for this driver', { color: GRAY, font: 9 }),
  ]);

  return pair(left, right, 'The Cube Check — the Driver Decides How Many Faces Count');
}

// ── ⑧ K = ½mv²: 한 함수, 두 가지 driver ─────────────────────────
//   왼쪽: v 로 미분 → 접선 기울기 = mv (운동량). 단위 [J ÷ (m/s)] = kg·m/s.
//   오른쪽: t 로 미분 → 접선 기울기 = Fv (일률).   단위 [J ÷ s] = W.
//   수치: m = 2 kg, F = 6 N → a = F/m = 3 m/s². K(v) = v², K(t) = ½m(at)² = 9t².
function energyTwoMeanings() {
  const m = 2, F = 6, a = F / m;
  const K = (v) => 0.5 * m * v * v;            // = v²
  const v0 = 3, slopeV = m * v0;               // K′(v) = mv = 6 (운동량)
  const Kt = (t) => 0.5 * m * (a * t) ** 2;    // = 9t²
  const t0 = 1.5, slopeT = F * a * t0;         // K′(t) = F·v = 27 (일률)

  const left = s2p([0, 4.5], [0, 20], PANEL, { axes: AX('v (m/s)', 'K (J)'), grid: { alpha: 0.25 } })
    .title('Respect v — the tangent’s slope is momentum')
    .add(
      curveOf(K, [0, 4.5], { color: GREEN, stroke: 2.6, n: 200 }),
      curveOf((v) => K(v0) + slopeV * (v - v0), [1.5, 4.5], { color: RED, stroke: 1.8, dash: [6, 4], n: 2 }),
      vlineAt(v0, { color: ASYMP, stroke: 1, dash: [4, 4] }),
      dotAt([v0, K(v0)], RED, 4.5),
      labelAt([0.5, 19.2], 'K(v) = ½ m v²,  m = 2 kg', { color: GREEN, bold: true, font: 10.5 }),
      labelAt([0.5, 17.0], 'slope = m v = 6  →  p (momentum)', { color: RED, bold: true, font: 10 }),
      labelAt([0.5, 15.0], 'J ÷ (m/s) = kg·m/s', { color: GRAY, font: 9.5 }),
      labelAt([3.05, 3.4], 'tangent at v = 3', { color: GRAY, font: 9 }),
    );

  const right = s2p([0, 2.2], [0, 45], PANEL, { axes: AX('t (s)', 'K (J)'), grid: { alpha: 0.25 } })
    .title('Respect t — the tangent’s slope is power')
    .add(
      curveOf(Kt, [0, 2.2], { color: GREEN, stroke: 2.6, n: 200 }),
      curveOf((t) => Kt(t0) + slopeT * (t - t0), [0.75, 2.2], { color: RED, stroke: 1.8, dash: [6, 4], n: 2 }),
      vlineAt(t0, { color: ASYMP, stroke: 1, dash: [4, 4] }),
      dotAt([t0, Kt(t0)], RED, 4.5),
      labelAt([0.15, 43], 'K(t) = ½ m a²t²,  a = F/m = 3', { color: GREEN, bold: true, font: 10.5 }),
      labelAt([0.15, 37.5], 'slope = F v = 6 · 4.5 = 27  →  P', { color: RED, bold: true, font: 10 }),
      labelAt([0.15, 32.5], 'J ÷ s = W  (watts)', { color: GRAY, font: 9.5 }),
      labelAt([1.62, 15], 'tangent at t = 1.5', { color: GRAY, font: 9 }),
      labelAt([1.62, 5.5], 'same J, different driver', { color: GRAY, font: 9 }),
    );

  return pair(left, right, 'One Formula, Two Laws — Momentum and Power');
}


// ── ⑨ v 와 a 의 부호: 언제 빨라지고 언제 느려지나 ────────────────
//   v(t) = t² − 4t + 3 = (t−1)(t−3),  a(t) = v′(t) = 2t − 4.
//   v·a > 0(같은 부호) = 빨라짐,  v·a < 0(반대 부호) = 느려짐.
//   왼쪽: v(t) 아래 네 구간을 색으로 표시. 오른쪽: v 와 a 를 같이 그려 부호 비교.
function motionSigns() {
  const v = (t) => t * t - 4 * t + 3;
  const a = (t) => 2 * t - 4;
  const SLOW = GREEN, FAST = RED;
  const PHASES = [
    { from: 0, to: 1, kind: 'slow', text: 'slowing down' },
    { from: 1, to: 2, kind: 'fast', text: 'speeding up' },
    { from: 2, to: 3, kind: 'slow', text: 'slowing down' },
    { from: 3, to: 4.4, kind: 'fast', text: 'speeding up' },
  ];
  const bands = (y0, y1) => PHASES.map((p) => barAt(p.from, p.to, y0, y1, p.kind === 'slow' ? SLOW : FAST, 0.06));

  const left = s2p([0, 4.4], [-2, 6], PANEL, { axes: AX('t (s)', 'v (m/s)'), grid: { alpha: 0.25 } })
    .title('v(t) = t² − 4t + 3 — the four phases')
    .add(
      ...bands(-2, 6),
      hlineAt(0, { color: ASYMP, stroke: 1 }),
      curveOf(v, [0, 4.4], { color: BLUE, stroke: 2.6, n: 200 }),
      vlineAt(1, { color: ASYMP, stroke: 1, dash: [4, 4] }),
      vlineAt(3, { color: ASYMP, stroke: 1, dash: [4, 4] }),
      dotAt([1, 0], GRAY, 4),
      dotAt([3, 0], GRAY, 4),
      labelAt([0.6, 5.7], 'v > 0: forward    v < 0: backward', { color: BLUE, bold: true, font: 10 }),
      labelAt([0.6, 4.95], 'v = 0 at t = 1 and t = 3', { color: GRAY, font: 9.5 }),
      ...PHASES.map((p) => labelAt([(p.from + p.to) / 2, -1.6], p.text,
        { color: p.kind === 'slow' ? SLOW : FAST, font: 9, anchor: 'middle' })),
    );

  const right = s2p([0, 4.4], [-4, 6], PANEL, { axes: AX('t (s)', 'v , a'), grid: { alpha: 0.25 } })
    .title('Speeding up needs v and a to agree in sign')
    .add(
      ...bands(-4, 6),
      hlineAt(0, { color: ASYMP, stroke: 1 }),
      curveOf(a, [0, 4.4], { color: ORANGE, stroke: 2.2, n: 2 }),
      curveOf(v, [0, 4.4], { color: BLUE, stroke: 2.6, n: 200 }),
      vlineAt(2, { color: ASYMP, stroke: 1, dash: [4, 4] }),
      dotAt([2, -1], PURPLE, 4.5),
      labelAt([0.55, 5.5], 'a(t) = 2t − 4', { color: ORANGE, bold: true, font: 10.5 }),
      labelAt([0.55, 4.75], 'v(t) = t² − 4t + 3', { color: BLUE, bold: true, font: 10.5 }),
      labelAt([0.5, 3.6], 'v · a > 0 → speeding up;   v · a < 0 → slowing down', { color: GRAY, font: 9 }),
      labelAt([1.06, 0.4], 'v = 0', { color: GRAY, font: 9 }),
      labelAt([3.06, 0.4], 'v = 0', { color: GRAY, font: 9 }),
      labelAt([2.15, -3.6], 'a = 0 at t = 2  (v is at its minimum)', { color: PURPLE, font: 9 }),
    );

  return pair(left, right, 'Speeding Up or Slowing Down — It Depends on Two Signs');
}

// ── figure 레지스트리 (키 = 출력 파일명 = 마크다운 태그 id) ───────
export const figures = {
  '14d1-03-linearization': linearization,
  '14d1-04-circle-ring': circleRing,
  '14d1-05-sphere-shell': sphereShell,
  '14d1-06-marginal-cost': marginalCost,
  '14d1-07-elasticity': elasticity,
  '14d1-08-sign-story': signStory,
  '14d1-09-cube-driver': cubeDriver,
  '14d1-10-energy-two-meanings': energyTwoMeanings,
  '14d1-11-motion-signs': motionSigns,
};

