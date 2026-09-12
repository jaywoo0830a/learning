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
import { annotate, curve, kit, line, point, segment } from '@jaywoo0830a/logos';

const { plot2d, subplots, palette } = kit;
const { blue, green, orange, purple, red, gray } = palette.tab;
const ASYMP = '#cccccc';   // 점근선·보조선(지면 톤 — 팔레트 밖)

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
    .title('s(t) = ½t²  —  m/s')
    .add(
      curve.fn(s).on([0, 6]).color(blue).stroke(2.6).n(200),
      curve.fn((t) => 4 * t - 8).on([2.5, 5.5]).color(red).stroke(1.8).dash([6, 4]).n(2),
      point(4, s(4)).dot().color(red).size(4.5),
      annotate.text([4.15, 6.4]).label("s'(4) = 4 m/s").font(11).color(red).bold(),
      legend([1.3, 17.2], 'tangent: “each extra second adds ≈ 4 m”', red, 9.5),
    );

  // 오른쪽: C(q) = q² + 4q + 144 — q=12 에서 접선 기울기 28 $/unit
  const C = (q) => q * q + 4 * q + 144;
  const right = plot2d([0, 22], [0, 750], { size: PANEL_W, axes: AX('quantity q (units)', 'cost C ($)'), grid: { alpha: 0.25 } })
    .title('C(q) = q² + 4q + 144  —  $/unit')
    .add(
      curve.fn(C).on([0, 22]).color(green).stroke(2.6).n(200),
      curve.fn((q) => 28 * q).on([4, 21]).color(red).stroke(1.8).dash([6, 4]).n(2),
      point(12, C(12)).dot().color(red).size(4.5),
      annotate.text([12.4, 250]).label("C'(12) = 28 $/unit").font(11).color(red).bold(),
      legend([0.6, 720], 'tangent: “the next unit costs ≈ $28”', red, 9.5),
    );

  return pair(left, right, 'The Same Geometric Object, Two Sentences');
}

// ── ② v·a 의 부호 → 운동 이야기 (위: 그래프 / 아래: 타임라인) ───
function motionStory() {
  const v = (t) => 3 * (t - 1) * (t - 3);
  const a = (t) => 6 * t - 12;

  const top = plot2d([0, 4], [-8, 10], { size: PANEL_TOP, axes: AX('time t (s)', 'v , a'), grid: { alpha: 0.25 } })
    .title('v(t) = 3t² − 12t + 9   and   a(t) = 6t − 12')
    .add(
      curve.fn(v).on([0, 4]).color(blue).stroke(2.6).n(200),
      curve.fn(a).on([0, 4]).color(orange).stroke(2.2).n(200),
      line.vertical(1).color(ASYMP).stroke(1).dash([4, 4]),
      line.vertical(2).color(ASYMP).stroke(1).dash([4, 4]),
      line.vertical(3).color(ASYMP).stroke(1).dash([4, 4]),
      point(1, 0).dot().color(blue).size(4),
      point(3, 0).dot().color(blue).size(4),
      point(2, 0).dot().color(orange).size(4),
      annotate.text([0.25, 8.7]).label('v').font(11).color(blue).bold(),
      annotate.text([0.25, -7.0]).label('a').font(11).color(orange).bold(),
      annotate.text([1, 5.2]).label('turning point').font(9).color(blue).anchor('middle'),
      annotate.text([3, 5.2]).label('turning point').font(9).color(blue).anchor('middle'),
      annotate.text([2, -3.6]).label('a changes sign').font(9).color(orange).anchor('middle'),
    );

  // 아래: 부호에서 만든 타임라인 (0<t<1 · 1<t<2 · 2<t<3 · t>3)
  //   각 구간 = 색 띠(굵은 segment) + 부호 두 줄. 요소를 먼저 모아 한 번에 add 한다.
  const bands = [
    { x0: 0, x1: 1, color: blue, sign: 'v +   a −', story: 'forward, slowing' },
    { x0: 1, x1: 2, color: orange, sign: 'v −   a −', story: 'backward, speeding up' },
    { x0: 2, x1: 3, color: purple, sign: 'v −   a +', story: 'backward, slowing' },
    { x0: 3, x1: 4, color: green, sign: 'v +   a +', story: 'forward, speeding up' },
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

// ── figure 레지스트리 (키 = 출력 파일명 = 마크다운 태그 id) ───────
export const figures = {
  '14d-01-derivative-units': derivativeUnits,
  '14d-02-motion-story': motionStory,
};
