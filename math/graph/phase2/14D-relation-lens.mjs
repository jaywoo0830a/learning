// math/graph/phase2/14D-relation-lens.mjs — 세션 14D(관계 렌즈: 단위·부호) 그림
//
// ── figure 목록 (키 = 출력 파일명 = 마크다운 태그 id) ──────────────
//    14d-01-derivative-units  (1×2) 같은 탄젠트, 다른 문장 — m/s vs $/unit
//    14d-02-motion-story      (2×1) v·a 의 부호에서 읽는 운동 이야기 + 타임라인
//
// ── 사용한 확장 (코어 수정 0 · 기준 logos 0.4.1) ────────────────────
//   곡선 = 코어 `curve.fn` · 접선 = 코어 `curve.fn`(직선) · 구간 막대 = 코어 `segment`.stroke
import {
  BLUE, ORANGE, GREEN, RED, PURPLE, GRAY, ASYMP,
  curveOf, segAt, dotAt, labelAt, vlineAt, legendAt, s2p, pair, stack, AX, OFF,
} from './_helpers.mjs';

// 이 세션의 패널은 14D1 보다 가로로 길다 — 그림마다 크기를 적지 않도록 프리셋으로 둔다.
// (`P` 는 _helpers 에서 "점"을 뜻하므로 헷갈리지 않게 PANEL_W 로 부른다.)
const PANEL_W = [560, 320];
const PANEL_TOP = [560, 280];
// 하단 타임라인도 같은 높이 — subplots 는 한 행의 높이를 패널 최대 높이로 맞추므로,
// 200 짜리 패널을 주면 아래에 빈 공간이 남는다.
const PANEL_BOT = [560, 280];

// ── ① 같은 기하(탄젠트), 다른 단위 ──────────────────────────────
function derivativeUnits() {
  // 왼쪽: s(t) = ½t² — t=4 에서 접선 기울기 4 m/s
  const s = (t) => 0.5 * t * t;
  const left = s2p([0, 6], [-2, 18], PANEL_W, { axes: AX('time t (s)', 'position s (m)'), grid: { alpha: 0.25 } })
    .title('s(t) = ½t²  —  m/s')
    .add(
      curveOf(s, [0, 6], { color: BLUE, stroke: 2.6, n: 200 }),
      curveOf((t) => 4 * t - 8, [2.5, 5.5], { color: RED, stroke: 1.8, dash: [6, 4], n: 2 }),
      dotAt([4, s(4)], RED, 4.5),
      labelAt([4.15, 6.4], "s'(4) = 4 m/s", { color: RED, bold: true, font: 11 }),
      legendAt([1.3, 17.2], 'tangent: “each extra second adds ≈ 4 m”', RED, { font: 9.5 }),
    );

  // 오른쪽: C(q) = q² + 4q + 144 — q=12 에서 접선 기울기 28 $/unit
  const C = (q) => q * q + 4 * q + 144;
  const right = s2p([0, 22], [0, 750], PANEL_W, { axes: AX('quantity q (units)', 'cost C ($)'), grid: { alpha: 0.25 } })
    .title('C(q) = q² + 4q + 144  —  $/unit')
    .add(
      curveOf(C, [0, 22], { color: GREEN, stroke: 2.6, n: 200 }),
      curveOf((q) => 28 * q, [4, 21], { color: RED, stroke: 1.8, dash: [6, 4], n: 2 }),
      dotAt([12, C(12)], RED, 4.5),
      labelAt([12.4, 250], "C'(12) = 28 $/unit", { color: RED, bold: true, font: 11 }),
      legendAt([0.6, 720], 'tangent: “the next unit costs ≈ $28”', RED, { font: 9.5 }),
    );

  return pair(left, right, 'The Same Geometric Object, Two Sentences');
}

// ── ② v·a 의 부호 → 운동 이야기 (위: 그래프 / 아래: 타임라인) ───
function motionStory() {
  const v = (t) => 3 * (t - 1) * (t - 3);
  const a = (t) => 6 * t - 12;

  const top = s2p([0, 4], [-8, 10], PANEL_TOP, { axes: AX('time t (s)', 'v , a'), grid: { alpha: 0.25 } })
    .title('v(t) = 3t² − 12t + 9   and   a(t) = 6t − 12')
    .add(
      curveOf(v, [0, 4], { color: BLUE, stroke: 2.6, n: 200 }),
      curveOf(a, [0, 4], { color: ORANGE, stroke: 2.2, n: 200 }),
      vlineAt(1, { color: ASYMP, stroke: 1, dash: [4, 4] }),
      vlineAt(2, { color: ASYMP, stroke: 1, dash: [4, 4] }),
      vlineAt(3, { color: ASYMP, stroke: 1, dash: [4, 4] }),
      dotAt([1, 0], BLUE, 4),
      dotAt([3, 0], BLUE, 4),
      dotAt([2, 0], ORANGE, 4),
      labelAt([0.25, 8.7], 'v', { color: BLUE, bold: true, font: 11 }),
      labelAt([0.25, -7.0], 'a', { color: ORANGE, bold: true, font: 11 }),
      labelAt([1, 5.2], 'turning point', { color: BLUE, font: 9, anchor: 'middle' }),
      labelAt([3, 5.2], 'turning point', { color: BLUE, font: 9, anchor: 'middle' }),
      labelAt([2, -3.6], 'a changes sign', { color: ORANGE, font: 9, anchor: 'middle' }),
    );

  // 아래: 부호에서 만든 타임라인 (0<t<1 · 1<t<2 · 2<t<3 · t>3)
  //   각 구간 = 색 띠(굵은 segment) + 부호 두 줄. 요소를 먼저 모아 한 번에 add 한다.
  const bands = [
    { x0: 0, x1: 1, color: BLUE, sign: 'v +   a −', story: 'forward, slowing' },
    { x0: 1, x1: 2, color: ORANGE, sign: 'v −   a −', story: 'backward, speeding up' },
    { x0: 2, x1: 3, color: PURPLE, sign: 'v −   a +', story: 'backward, slowing' },
    { x0: 3, x1: 4, color: GREEN, sign: 'v +   a +', story: 'forward, speeding up' },
  ];
  const bandParts = bands.flatMap((b) => {
    const mid = (b.x0 + b.x1) / 2;
    return [
      segAt([b.x0, 0.5], [b.x1, 0.5], { color: b.color, stroke: 16 }),
      labelAt([mid, 0.76], b.sign, { color: b.color, bold: true, font: 10, anchor: 'middle' }),
      labelAt([mid, 0.22], b.story, { color: GRAY, font: 9.5, anchor: 'middle' }),
    ];
  });
  const tickParts = [0, 1, 2, 3, 4].flatMap((t) => [
    vlineAt(t, { color: ASYMP, stroke: 1, dash: [3, 3] }),
    labelAt([t, 0.06], String(t), { color: GRAY, font: 9, anchor: 'middle' }),
  ]);

  const bottom = s2p([0, 4], [0, 1], PANEL_BOT, OFF)
    .title('The motion timeline — read straight off the signs')
    .add(...bandParts, ...tickParts);

  return stack([top, bottom], 'Motion Story from the Signs of v and a');
}

// ── figure 레지스트리 (키 = 출력 파일명 = 마크다운 태그 id) ───────
export const figures = {
  '14d-01-derivative-units': derivativeUnits,
  '14d-02-motion-story': motionStory,
};
