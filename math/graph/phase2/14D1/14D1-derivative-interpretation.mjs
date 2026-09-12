// math/graph/phase2/14D1/14D1-derivative-interpretation.mjs — 세션 14D1(도함수의 해석) 그림
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
// ── 코어 API 만 쓴다 (기준 @jaywoo0830a/logos 0.4.1) ────────────────
//   이 폴더에는 헬퍼 파일이 없다 — 아래 프리셋은 전부 이 파일 안의 1~2줄 별칭이다.
//   곡선 curve.fn(f).on(dom) · 링 region.annulus · 부호 띠 region.bar · 구간 region.between
//   구 sphere(3D) · 등각 상자 polygon(+toPoint) · 선분 segment([x,y,z],[x,y,z]) · 라벨 annotate.text
//   색 kit.palette.* (0.4.1 tick-step 자릿수 유도 덕분에 좁은 범위 눈금도 그대로 쓴다)
import { annotate, circle, curve, kit, line, point, polygon, region, segment, sphere, toPoint } from '@jaywoo0830a/logos';

const { plot2d, plot3d, subplots, palette } = kit;
const { blue, green, orange, purple, red, gray } = palette.tab;
const LIGHT = '#bbbbbb', ASYMP = '#cccccc';   // 보조 톤(지면 — 팔레트 밖)
const BOX = { facecolor: 'white', alpha: 0.85 };

// ── 이 파일 전용 프리셋 (코어 옵션 위의 1줄 별칭) ─────────────────
const PANEL = [520, 400];
const OFF = { axes: false, grid: false };
const AX = (x, y) => ({ x: { label: x }, y: { label: y } });
const pair = (l, r, title) => subplots([l, r], { cols: 2, tight: true, title });
const single = (p, title) => subplots([p], { cols: 1, tight: true, title });
/** 범례 대신 같은 색 라벨 */
const legend = (at, text, color, font = 10) => annotate.text(at).label(text).font(font).color(color).bold();
/** 부호 띠 — 코어 region.bar 위의 1줄 별칭 */
const barAt = (x0, x1, y0, y1, fill, opacity) => region.bar(x0, x1, y0, y1).fill(fill).opacity(opacity);

// ── ① 선형화: √x 를 x=4 의 접선으로 ──────────────────────────────
//   왼쪽: 전체 — 접선과 곡선이 거의 붙어 보인다(그게 요점이다).
//   오른쪽: x=4.1 확대 — 두 선이 벌어진 폭이 곧 근사 오차.
function linearization() {
  const f = Math.sqrt;
  const L = (x) => 2 + (x - 4) / 4;

  const left = plot2d([0, 9], [0, 3.4], { size: PANEL, axes: AX('x', 'y'), grid: { alpha: 0.25 } })
    .title('f(x) = √x  and its tangent at x = 4')
    .add(
      curve.fn(f).on([0, 9]).color(blue).stroke(2.6).n(240),
      curve.fn(L).on([0, 9]).color(red).stroke(1.8).dash([6, 4]).n(2),
      line.vertical(4).color(ASYMP).stroke(1).dash([4, 4]),
      point(4, 2).dot().color(red).size(4.5),
      legend([1.1, 3.25], 'L(x) = 2 + (x − 4)/4', red),
      annotate.text([4.15, 0.35]).label('touch point x = 4').font(9.5).color(red),
    );

  // 0.4.1 의 눈금 정밀도 수정(fmtTick 이 tick step 에서 자릿수를 유도) 덕분에 좁은 범위
  // (폭 0.012)에서도 y 눈금이 "2.02" 로 뭉개지지 않는다 → 예전처럼 눈금을 끌 필요가 없다.
  // (자릿수를 직접 정하고 싶으면 axes({ y: { decimals: n } }).)
  const right = plot2d([4.08, 4.12], [2.019, 2.031], { size: PANEL, axes: AX('x', 'y'), grid: { alpha: 0.25 } })
    .title('Zoom at x = 4.1   (gap ≈ 1.5 × 10⁻⁴)')
    .add(
      curve.fn(f).on([4.08, 4.12]).color(blue).stroke(2.4).n(120),
      curve.fn(L).on([4.08, 4.12]).color(red).stroke(1.8).dash([6, 4]).n(2),
      segment([4.1, f(4.1)], [4.1, L(4.1)]).color(gray).stroke(1.6),
      point(4.1, L(4.1)).marker('circle', { open: true }).color(red).size(4.5),
      point(4.1, f(4.1)).marker('circle').color(blue).size(4.5),
      annotate.text([4.1002, 2.0288]).label('L(4.1) = 2.025').font(9.5).color(red),
      annotate.text([4.1002, 2.0207]).label('√4.1 = 2.024846').font(9.5).color(blue),
      annotate.text([4.09, 2.02485]).label('error ≈ 1.5 × 10⁻⁴').font(9).color(gray).anchor('end'),
    );

  return pair(left, right, 'Linearization — the tangent is the best linear model');
}

// ── ② 원판의 링: A′(r) = 2πr = 둘레 ─────────────────────────────
//   두께 dr 짜리 링의 넓이가 곧 "둘레 × dr" — 넓이를 미분하면 경계가 나온다.
function circleRing() {
  const O = point(0, 0);
  const r = 2, dr = 0.22;

  const p = plot2d([-3.0, 3.6], [-2.8, 2.8], { size: [560, 460], axes: AX('x', 'y'), grid: { alpha: 0.2 }, equal: true })
    .title('Ring of width dr :  ΔA ≈ 2πr · dr')
    .add(
      region.annulus(O, r, r + dr).fill(blue).opacity(0.28),
      circle.center(O).radius(r).color(blue).stroke(2.2),
      circle.center(O).radius(r + dr).color(blue).stroke(1.4).dash([5, 3]),
      segment([0, 0], [r, 0]).color(red).stroke(1.8),
      point(0, 0).dot().color(red).size(4),
      point(r, 0).marker('circle').color(blue).size(4),
      point(r + dr, 0).marker('circle', { open: true }).color(blue).size(4),
      annotate.text([1.0, 0.16]).label('r').font(12).color(red).bold(),
      annotate.text([2.14, 0.62]).label('dr').font(10).color(blue),
      annotate.text([-2.75, 2.5]).label('A(r) = πr²').font(10).color(gray),
      annotate.text([-2.75, 2.2]).label("A′(r) = 2πr  =  circumference").font(10).color(blue).bold(),
      annotate.text([-2.75, 1.9]).label('the ring is a stretched circumference').font(9.5).color(gray),
    );

  return single(p, 'Differentiating the Area Gives the Circumference');
}

// ── ③ 구 껍질 (3D): V′(r) = 4πr² = 표면적 ───────────────────────
//   코어 3D 패널은 annotate/segment/marker 도 ctx.project 로 함께 투영한다 —
//   그래서 라벨·반지름 화살표를 3D 좌표로 주면 구 위에 정확히 얹힌다.
//   (Sphere.toIR 는 라벨을 범례로 보내므로 라벨은 직접 찍는다.)
function sphereShell() {
  const r = 2.0, dr = 0.30;

  const p = plot3d({ elev: 14, azim: -52, size: [560, 440] })
    .title('Shell of thickness dr :  ΔV ≈ 4πr² · dr')
    .add(
      // ① 바깥 구(r+dr)를 먼저 깔아 '껍질 띠'를 만든다 — 옅은 채움 + 얇은 점선
      sphere.center(point(0, 0, 0)).radius(r + dr).fill(palette.skyblue).opacity(0.45)
        .color(palette.steel).stroke(0.9).dash([4, 3]),
      // ② 안쪽 구(r)를 나중에 그려 진한 공이 위로 온다 → 가장자리에 halo(껍질)가 남는다
      sphere.center(point(0, 0, 0)).radius(r).fill(blue).opacity(0.26)
        .color(palette.skyblue).stroke(1.6),
      // ③ 반지름 r 과 껍질 두께 dr 을 같은 방향에 나란히
      segment([0, 0, 0], [r, 0, 0]).color(red).stroke(1.8),
      segment([r, 0, 0], [r + dr, 0, 0]).color(purple).stroke(1.8),
      point(0, 0, 0).dot().color(red).size(3.5),
      annotate.text([r * 0.52, 0, 0.14]).label('r').font(12).color(red).bold(),
      annotate.text([r + dr * 0.5, 0, -0.1]).label('dr').font(10.5).color(purple),
      annotate.text([0, 0, r + 0.42]).label('r + dr').font(10.5).color(purple).bold(),
      // ④ 설명 3줄 — 같은 3D 앵커에 px 오프셋(offset)으로 쌓아 겹침을 막는다
      annotate.text([-2.15, -1.75, 0]).label('V(r) = 4/3 πr³').font(10).color(gray).offset(0, -30),
      annotate.text([-2.15, -1.75, 0]).label("V′(r) = 4πr²  =  surface area").font(10.5).color(blue).bold().offset(0, -14),
      annotate.text([-2.15, -1.75, 0]).label('the shell is a stretched surface').font(9.5).color(gray),
    );

  return single(p, 'Differentiating the Volume Gives the Surface Area');
}

// ── ④ 한계비용 = 접선의 기울기, AC 와의 교차 ────────────────────
//   왼쪽: C(q) 위 q=12 의 접선 — 그 기울기가 "다음 한 단위"의 값.
//   오른쪽: MC 와 AC — 평균비용의 최소점에서 정확히 만난다.
function marginalCost() {
  const C = (q) => q * q + 4 * q + 144;
  const q0 = 12, MC0 = 2 * q0 + 4;          // C′(12) = 28
  const LEFT_X = [0, 22], LEFT_Y = [0, 750];

  const left = plot2d(LEFT_X, LEFT_Y, { size: PANEL, axes: AX('quantity q (units)', 'cost C ($)'), grid: { alpha: 0.25 } })
    .title('C(q) = q² + 4q + 144  —  tangent at q = 12')
    .add(
      curve.fn(C).on(LEFT_X).color(green).stroke(2.6).n(200),
      curve.fn((q) => MC0 * q).on([4, 21]).color(red).stroke(1.8).dash([6, 4]).n(2),
      point(q0, C(q0)).dot().color(red).size(4.5),
      annotate.text([12.4, 200]).label("C'(12) = 28 $/unit").font(10.5).color(red).bold(),
      legend([2.6, 700], 'slope here = price of the NEXT unit', red, 9.5),
      annotate.text([0.4, 715]).label('C ($)').font(9.5).color(gray),
      annotate.text([11, 90]).label('q (units)').font(9.5).color(gray).anchor('middle'),
    );

  const MC = (q) => 2 * q + 4;
  const AC = (q) => q + 4 + 144 / q;
  const right = plot2d([3, 22], [0, 60], { size: PANEL, axes: AX('quantity q (units)', '$ / unit'), grid: { alpha: 0.25 } })
    .title('MC crosses AC at the minimum of AC')
    .add(
      curve.fn(MC).on([3, 22]).color(red).stroke(2.4).n(200),
      curve.fn(AC).on([3, 22]).color(blue).stroke(2.4).n(200),
      line.vertical(q0).color(ASYMP).stroke(1).dash([4, 4]),
      point(q0, MC0).dot().color(purple).size(5),
      annotate.text([5.6, 53]).label('MC = 2q + 4').font(10.5).color(red).bold(),
      annotate.text([6.0, 46]).label('AC = q + 4 + 144/q').font(10.5).color(blue).bold(),
      annotate.text([13.2, 35.5]).label('meet at q = 12  ($28)').font(10).color(purple).bold(),
      annotate.text([13, 12]).label("AC'(12) = 0 — the average stops falling").font(9).color(gray),
      annotate.text([21.5, 56]).label('$ / unit').font(9.5).color(gray).anchor('end'),
      annotate.text([12.5, 6.5]).label('q (units)').font(9.5).color(gray).anchor('middle'),
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

  const left = plot2d([0, 50], [0, 520], { size: PANEL, axes: AX('price p ($)', 'quantity q'), grid: { alpha: 0.25 } })
    .title('Demand q(p) = 500 − 10p')
    .add(
      region.between(0, q).on([0, pStar]).fill(blue).opacity(0.12),    // |E| < 1
      region.between(0, q).on([pStar, 50]).fill(red).opacity(0.12),    // |E| > 1
      curve.fn(q).on([0, 50]).color(blue).stroke(2.6).n(2),
      line.vertical(pStar).color(ASYMP).stroke(1).dash([4, 4]),
      point(pStar, qStar).dot().color(purple).size(5),
      annotate.text([7, 300]).label('inelastic  (|E| < 1)').font(10).color(blue).bold(),
      annotate.text([48, 480]).label('elastic  (|E| > 1)').font(10).color(red).bold().anchor('end'),
      annotate.text([pStar + 0.6, 150]).label('E = −1  at p = 25').font(10).color(purple).bold(),
    );

  const right = plot2d([0, 50], [0, 6600], { size: PANEL, axes: AX('price p ($)', 'revenue R ($)'), grid: { alpha: 0.25 } })
    .title('Revenue R(p) = 500p − 10p²')
    .add(
      curve.fn(R).on([0, 50]).color(green).stroke(2.6).n(200),
      region.between(0, R).on([0, pStar]).fill(blue).opacity(0.10),
      region.between(0, R).on([pStar, 50]).fill(red).opacity(0.10),
      line.vertical(pStar).color(ASYMP).stroke(1).dash([4, 4]),
      point(pStar, rStar).dot().color(purple).size(5),
      annotate.text([pStar + 1.2, 6320]).label('R = 6250 max').font(10.5).color(purple).bold(),
      annotate.text([26.8, 4600]).label("R'(p) = 500 − 20p = 0").font(9.5).color(gray),
      annotate.text([5, 900]).label('raise price → revenue up').font(9).color(blue),
      annotate.text([47, 900]).label('raise price → revenue down').font(9).color(red).anchor('end'),
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

  const left = plot2d([-1.5, 5.5], [-9, 9], { size: PANEL, axes: AX('x', 'f′(x)'), grid: { alpha: 0.25 } })
    .title('Read by height — the sign of f′ is the direction of f')
    .add(
      barAt(-1.5, x0, -9, 0, red, 0.07),    // f′ < 0 인 사분면
      barAt(x0, 5.5, 0, 9, blue, 0.07),     // f′ > 0 인 사분면
      line.horizontal(0).color(ASYMP).stroke(1),
      curve.fn(fp).on([-1.5, 5.5]).color(blue).stroke(2.6).n(2),
      line.vertical(x0).color(ASYMP).stroke(1).dash([4, 4]),
      point(x0, 0).dot().color(purple).size(4.5),
      annotate.text([0.35, 7.7]).label('f′(x) = 2x − 4').font(10.5).color(blue).bold(),
      annotate.text([0.35, 6.4]).label('slope = 2  →  f″ = 2 > 0').font(9.5).color(gray),
      annotate.text([0.35, -7.7]).label('f′ < 0  →  f falls').font(10).color(red).bold(),
      annotate.text([2.3, 6.8]).label('f′ > 0  →  f rises').font(10).color(blue).bold(),
      annotate.text([2.2, -1.8]).label('f′(2) = 0  →  f is flat').font(9.5).color(purple),
    );

  const right = plot2d([-0.9, 5], [-5.5, 6.5], { size: PANEL, axes: AX('x', 'f(x)'), grid: { alpha: 0.25 } })
    .title('Read by slope — f′ rising means f bends upward')
    .add(
      curve.fn(f).on([-0.9, 5]).color(green).stroke(2.6).n(200),
      segment([0.6, -4], [3.4, -4]).color(red).stroke(1.8).dash([6, 4]),   // 최소점의 접선
      line.vertical(2).color(ASYMP).stroke(1).dash([4, 4]),
      point(2, -4).dot().color(green).size(4.5),
      annotate.text([0.15, 6.0]).label('f(x) = x² − 4x  (the +C is free)').font(10.5).color(green).bold(),
      annotate.text([0.15, 5.0]).label('falls → rises: minimum at x = 2').font(9.5).color(gray),
      annotate.text([2.15, -3.2]).label('f′ = 0 and f″ > 0  →  minimum').font(9.5).color(purple),
      annotate.text([0.62, -4.75]).label('tangent: slope 0').font(9).color(red),
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
    return toPoint(ISO(x, y, z));
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
    return plot2d([-0.8, 4.6], [-0.5, 3.655], { size: PANEL, ...OFF, equal: true })
      .title(title)
      .add(...slabs, ...lines);
  };

  const left = box('side', 'dV/ds = 3s² — respect the side s', [
    annotate.text([-0.75, 3.5]).label('only 3 faces move (normals +x, +y, +z)').font(10).color(blue).bold(),
    annotate.text([-0.75, 3.12]).label('dV/ds collects 3s² — three faces of area s²').font(9.5).color(gray),
    annotate.text([-0.75, -0.25]).label('front face stays put; dashed = the hidden face at z = s').font(9).color(gray),
  ]);

  const right = box('half', 'dV/du = 24u² = 6s² — respect the half-side u = s/2', [
    annotate.text([-0.75, 3.5]).label('all 6 faces move — two per direction').font(10).color(green).bold(),
    annotate.text([-0.75, 3.12]).label('a half-side step pushes both faces of every pair').font(9.5).color(gray),
    annotate.text([-0.75, -0.25]).label('front face moves too: 6s² appears only for this driver').font(9).color(gray),
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

  const left = plot2d([0, 4.5], [0, 20], { size: PANEL, axes: AX('v (m/s)', 'K (J)'), grid: { alpha: 0.25 } })
    .title('Respect v — the tangent’s slope is momentum')
    .add(
      curve.fn(K).on([0, 4.5]).color(green).stroke(2.6).n(200),
      curve.fn((v) => K(v0) + slopeV * (v - v0)).on([1.5, 4.5]).color(red).stroke(1.8).dash([6, 4]).n(2),
      line.vertical(v0).color(ASYMP).stroke(1).dash([4, 4]),
      point(v0, K(v0)).dot().color(red).size(4.5),
      annotate.text([0.5, 19.2]).label('K(v) = ½ m v²,  m = 2 kg').font(10.5).color(green).bold(),
      annotate.text([0.5, 17.0]).label('slope = m v = 6  →  p (momentum)').font(10).color(red).bold(),
      annotate.text([0.5, 15.0]).label('J ÷ (m/s) = kg·m/s').font(9.5).color(gray),
      annotate.text([3.05, 3.4]).label('tangent at v = 3').font(9).color(gray),
    );

  const right = plot2d([0, 2.2], [0, 45], { size: PANEL, axes: AX('t (s)', 'K (J)'), grid: { alpha: 0.25 } })
    .title('Respect t — the tangent’s slope is power')
    .add(
      curve.fn(Kt).on([0, 2.2]).color(green).stroke(2.6).n(200),
      curve.fn((t) => Kt(t0) + slopeT * (t - t0)).on([0.75, 2.2]).color(red).stroke(1.8).dash([6, 4]).n(2),
      line.vertical(t0).color(ASYMP).stroke(1).dash([4, 4]),
      point(t0, Kt(t0)).dot().color(red).size(4.5),
      annotate.text([0.15, 43]).label('K(t) = ½ m a²t²,  a = F/m = 3').font(10.5).color(green).bold(),
      annotate.text([0.15, 37.5]).label('slope = F v = 6 · 4.5 = 27  →  P').font(10).color(red).bold(),
      annotate.text([0.15, 32.5]).label('J ÷ s = W  (watts)').font(9.5).color(gray),
      annotate.text([1.62, 15]).label('tangent at t = 1.5').font(9).color(gray),
      annotate.text([1.62, 5.5]).label('same J, different driver').font(9).color(gray),
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
  const SLOW = green, FAST = red;
  const PHASES = [
    { from: 0, to: 1, kind: 'slow', text: 'slowing down' },
    { from: 1, to: 2, kind: 'fast', text: 'speeding up' },
    { from: 2, to: 3, kind: 'slow', text: 'slowing down' },
    { from: 3, to: 4.4, kind: 'fast', text: 'speeding up' },
  ];
  const bands = (y0, y1) => PHASES.map((p) => barAt(p.from, p.to, y0, y1, p.kind === 'slow' ? SLOW : FAST, 0.06));

  const left = plot2d([0, 4.4], [-2, 6], { size: PANEL, axes: AX('t (s)', 'v (m/s)'), grid: { alpha: 0.25 } })
    .title('v(t) = t² − 4t + 3 — the four phases')
    .add(
      ...bands(-2, 6),
      line.horizontal(0).color(ASYMP).stroke(1),
      curve.fn(v).on([0, 4.4]).color(blue).stroke(2.6).n(200),
      line.vertical(1).color(ASYMP).stroke(1).dash([4, 4]),
      line.vertical(3).color(ASYMP).stroke(1).dash([4, 4]),
      point(1, 0).dot().color(gray).size(4),
      point(3, 0).dot().color(gray).size(4),
      annotate.text([0.6, 5.7]).label('v > 0: forward    v < 0: backward').font(10).color(blue).bold(),
      annotate.text([0.6, 4.95]).label('v = 0 at t = 1 and t = 3').font(9.5).color(gray),
      ...PHASES.map((p) => annotate.text([(p.from + p.to) / 2, -1.6]).label(p.text)
        .font(9).color(p.kind === 'slow' ? SLOW : FAST).anchor('middle')),
    );

  const right = plot2d([0, 4.4], [-4, 6], { size: PANEL, axes: AX('t (s)', 'v , a'), grid: { alpha: 0.25 } })
    .title('Speeding up needs v and a to agree in sign')
    .add(
      ...bands(-4, 6),
      line.horizontal(0).color(ASYMP).stroke(1),
      curve.fn(a).on([0, 4.4]).color(orange).stroke(2.2).n(2),
      curve.fn(v).on([0, 4.4]).color(blue).stroke(2.6).n(200),
      line.vertical(2).color(ASYMP).stroke(1).dash([4, 4]),
      point(2, -1).dot().color(purple).size(4.5),
      annotate.text([0.55, 5.5]).label('a(t) = 2t − 4').font(10.5).color(orange).bold(),
      annotate.text([0.55, 4.75]).label('v(t) = t² − 4t + 3').font(10.5).color(blue).bold(),
      annotate.text([0.5, 3.6]).label('v · a > 0 → speeding up;   v · a < 0 → slowing down').font(9).color(gray),
      annotate.text([1.06, 0.4]).label('v = 0').font(9).color(gray),
      annotate.text([3.06, 0.4]).label('v = 0').font(9).color(gray),
      annotate.text([2.15, -3.6]).label('a = 0 at t = 2  (v is at its minimum)').font(9).color(purple),
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
