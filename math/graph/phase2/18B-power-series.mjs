// math/graph/phase2/18B-power-series.mjs — 세션 18B(멱급수) 그림 복원
//
// ── figure 목록 (키 = 출력 파일명 = 마크다운 태그 id) ──────────────
//    18b-radius-convergence  (2×2) R 의 세 경우 · Σxⁿ 부분합 · 끝점 검사 · 수렴구간 표
//    18b-building-series     (1×3) 1/(1−x) 에서 치환·적분으로 만든 세 급수
//
// ── 사용한 확장 (코어 수정 0) ────────────────────────────────────
//   곡선 = 코어 `curve.fn` · 구간 막대 = 코어 `segment`.stroke · 열린/닫힌 끝점 =
//   코어 `point.marker({ open })`. (plugins/_math-extras 는 여기서 쓰지 않는다.)
import {
  BLUE, ORANGE, GREEN, RED, PURPLE, GRAY, ASYMP,
  curveOf, segAt, markerAt, dotAt, labelAt, vlineAt, hlineAt, legendAt,
  seriesFn, clampFn, s2p, subplots, AX, AXx,
} from './_helpers.mjs';

const P2 = [430, 330];   // 2×2 패널 크기
const P3 = [430, 360];   // 1×3 패널 크기

// ── TL : 반지름의 세 가지 경우 (R=1 · R=∞ · R=0) ────────────────
function panelRadiusCases() {
  const cases = [
    { y: 2.30, color: BLUE, half: 1, name: 'Σ xⁿ', tag: 'R = 1' },
    { y: 1.30, color: GREEN, half: 3, name: 'Σ xⁿ/n!', tag: 'R = ∞' },
    { y: 0.30, color: ORANGE, half: 0, name: 'Σ n! xⁿ', tag: 'R = 0' },
  ];
  const p = s2p([-3, 3], [-0.6, 3], P2, { axes: AXx('x'), grid: { alpha: 0.25 } })
    .title('Radius of convergence — three cases');
  const add = [];
  for (const c of cases) {
    add.push(labelAt([-2.85, c.y + 0.26], c.name, { color: c.color, bold: true, font: 10 }));
    add.push(labelAt([2.85, c.y + 0.26], c.tag, { color: c.color, anchor: 'end', bold: true, font: 10 }));
    if (c.half === 0) {
      add.push(markerAt([0, c.y], c.color, { size: 5.5 }));
      add.push(labelAt([0.4, c.y], 'converges only at x = 0', { color: c.color, font: 9 }));
    } else {
      add.push(segAt([-c.half, c.y], [c.half, c.y], { color: c.color, stroke: 6.5 }));
      if (c.half === 1) {                    // 끝점은 따로 판정 — 빈 원
        add.push(markerAt([-1, c.y], c.color, { open: true }));
        add.push(markerAt([1, c.y], c.color, { open: true }));
        add.push(labelAt([2.85, c.y - 0.4], 'endpoints: check separately', { color: c.color, font: 9, anchor: 'end' }));
      } else {
        add.push(labelAt([2.85, c.y - 0.4], 'converges for every x', { color: c.color, font: 9, anchor: 'end' }));
      }
    }
  }
  return p.add(...add);
}

// ── TR : Σxⁿ 의 부분합이 1/(1−x) 로 수렴 ────────────────────────
function panelGeomPartials() {
  const Sg = (N) => seriesFn((n, x) => x ** n, 0, N);
  const dom = [-0.8, 0.8];
  return s2p(dom, [-1, 6], P2, { axes: AX('x', 'S_N(x)'), grid: { alpha: 0.25 } })
    .title('Partial sums: Σ xⁿ → 1/(1−x)')
    .add(
      curveOf((x) => 1 / (1 - x), dom, { color: RED, stroke: 2.6, n: 240 }),
      curveOf(clampFn(Sg(1), -0.95, 5.9), dom, { color: BLUE, stroke: 1.6, n: 240 }),
      curveOf(clampFn(Sg(3), -0.95, 5.9), dom, { color: GREEN, stroke: 1.6, n: 240 }),
      curveOf(clampFn(Sg(7), -0.95, 5.9), dom, { color: ORANGE, stroke: 1.6, n: 240 }),
      legendAt([-0.77, 5.5], '1/(1−x)  (true sum)', RED, { font: 10 }),
      legendAt([-0.77, 5.0], 'S₁', BLUE, { font: 10 }),
      legendAt([-0.52, 5.0], 'S₃', GREEN, { font: 10 }),
      legendAt([-0.28, 5.0], 'S₇', ORANGE, { font: 10 }),
      labelAt([0.4, 0.45], 'converges only for |x| < 1', { color: GRAY, font: 9, anchor: 'middle' }),
    );
}

// ── BL : Σxⁿ/n 의 끝점 — x=1 발산 vs x=−1 수렴 ──────────────────
function panelEndpoints() {
  const SN = (x, N) => { let s = 0; for (let n = 1; n <= N; n++) s += x ** n / n; return s; };
  const Ns = Array.from({ length: 60 }, (_, i) => i + 1);
  return s2p([0, 60], [-1.4, 5], P2, { axes: AX('N', 'S_N'), grid: { alpha: 0.25 } })
    .title('Endpoint check:  Σ xⁿ/n   at   x = 1, −1, 0.9')
    .add(
      ...Ns.map((N) => dotAt([N, SN(1, N)], RED, 2.6)),
      ...Ns.map((N) => dotAt([N, SN(0.9, N)], GREEN, 2.6)),
      ...Ns.map((N) => dotAt([N, SN(-1, N)], BLUE, 2.6)),
      hlineAt(-Math.LN2, { color: BLUE, stroke: 1, dash: [4, 4], opacity: 0.7 }),
      labelAt([59, 4.7], 'x = 1 :  harmonic  →  diverges', { color: RED, anchor: 'end', bold: true, font: 9.5 }),
      labelAt([59, 2.75], 'x = 0.9 :  →  −ln(0.1) ≈ 2.303', { color: GREEN, anchor: 'end', font: 9.5 }),
      labelAt([59, -1.05], 'x = −1 :  →  −ln 2 ≈ −0.693', { color: BLUE, anchor: 'end', font: 9.5 }),
    );
}

// ── BR : 수렴구간 요약표 (● 수렴 · ○ 발산) ──────────────────────
function panelIntervalTable() {
  const rows = [
    { y: 4.2, name: 'Σ xⁿ', lo: -1, hi: 1, loOpen: true, hiOpen: true, tag: 'R = 1' },
    { y: 3.3, name: 'Σ xⁿ/n', lo: -1, hi: 1, loOpen: false, hiOpen: true, tag: 'R = 1' },
    { y: 2.4, name: 'Σ xⁿ/n²', lo: -1, hi: 1, loOpen: false, hiOpen: false, tag: 'R = 1' },
    { y: 1.5, name: 'Σ xⁿ/n!', lo: -2.8, hi: 2.8, loOpen: true, hiOpen: true, tag: 'R = ∞' },
    { y: 0.6, name: 'Σ n!(x−1)ⁿ', lo: 1, hi: 1, loOpen: false, hiOpen: false, tag: 'R = 0' },
  ];
  const p = s2p([-5, 3.6], [-0.6, 4.9], P2, { axes: AXx('x'), grid: { alpha: 0.2 } })
    .title('Intervals of convergence');
  const add = [];
  for (const r of rows) {
    add.push(labelAt([-4.9, r.y + 0.06], r.name, { color: GRAY, font: 10 }));
    add.push(labelAt([3.55, r.y + 0.06], r.tag, { color: RED, anchor: 'end', bold: true, font: 9.5 }));
    if (r.lo === r.hi) {
      add.push(markerAt([r.lo, r.y], GREEN, { size: 5 }));
    } else {
      add.push(segAt([r.lo, r.y], [r.hi, r.y], { color: GREEN, stroke: 6 }));
      add.push(r.loOpen ? markerAt([r.lo, r.y], RED, { open: true }) : markerAt([r.lo, r.y], GREEN));
      add.push(r.hiOpen ? markerAt([r.hi, r.y], RED, { open: true }) : markerAt([r.hi, r.y], GREEN));
    }
  }
  add.push(labelAt([-4.9, 4.72], '● converges      ○ diverges', { color: GRAY, font: 9 }));
  return p.add(...add);
}

// ── figure 1 : 반지름과 수렴구간 (2×2) ──────────────────────────
function radiusConvergence() {
  return subplots(
    [panelRadiusCases(), panelGeomPartials(), panelEndpoints(), panelIntervalTable()],
    { cols: 2, tight: true, title: 'Power Series — Radius and Interval of Convergence' },
  );
}

// ══ 2. 1/(1−x) 에서 새 급수 만들기 (1×3) ═════════════════════════
//   ① x→−x : 1/(1+x)   ② 적분 : ln(1+x)   ③ 1/(1+x²) 적분 : arctan x
function buildingSeries() {
  // ① 1/(1+x) = Σ (−1)ⁿ xⁿ   (x → −x 치환)
  const g1 = (x) => 1 / (1 + x);
  const d1 = [-0.85, 0.85];
  const s1 = s2p(d1, [-0.6, 7], P3, { axes: AX('x', 'value'), grid: { alpha: 0.25 } })
    .title('1/(1+x)   ←   x → −x')
    .add(
      curveOf(g1, d1, { color: RED, stroke: 2.6, n: 240 }),
      ...[[1, BLUE], [3, GREEN], [7, ORANGE], [15, PURPLE]].map(([N, c]) =>
        curveOf(clampFn(seriesFn((n, x) => (-1) ** n * x ** n, 0, N), 0.02, 6.9), d1, { color: c, stroke: 1.6, n: 240 })),
      legendAt([-0.8, 6.55], '1/(1+x)', RED, { font: 9.5 }),
      legendAt([-0.05, 6.55], 'S₁, S₃, S₇, S₁₅', BLUE, { font: 9.5 }),
    );

  // ② ln(1+x) = Σ (−1)ⁿ⁺¹ xⁿ/n   (적분)
  const g2 = (x) => Math.log(1 + x);
  const d2 = [-0.9, 1.0];
  const s2 = s2p(d2, [-2.3, 1.6], P3, { axes: AX('x', 'value'), grid: { alpha: 0.25 } })
    .title('ln(1+x)   ←   ∫ 1/(1+x) dx')
    .add(
      curveOf(g2, d2, { color: RED, stroke: 2.6, n: 240 }),
      ...[[1, BLUE], [2, GREEN], [5, ORANGE], [20, PURPLE]].map(([N, c]) =>
        curveOf(clampFn(seriesFn((n, x) => ((-1) ** (n + 1)) * x ** n / n, 1, N), -2.25, 1.55), d2, { color: c, stroke: 1.6, n: 240 })),
      vlineAt(-1, { color: ASYMP, stroke: 1, dash: [4, 4] }),
      legendAt([-0.86, 1.45], 'ln(1+x)', RED, { font: 9.5 }),
      legendAt([-0.86, 1.15], 'partial sums  S₁, S₂, S₅, S₂₀', BLUE, { font: 9.5 }),
      labelAt([0.95, -2.05], 'x = −1 : log 0', { color: GRAY, font: 9, anchor: 'end' }),
    );

  // ③ arctan x = Σ (−1)ⁿ x^{2n+1}/(2n+1)   (1/(1+x²) 적분, 반지름 1)
  const g3 = Math.atan;
  const d3 = [-1.15, 1.15];
  const s3 = s2p(d3, [-1.4, 1.4], P3, { axes: AX('x', 'value'), grid: { alpha: 0.25 } })
    .title('arctan x   ←   ∫ 1/(1+x²) dx')
    .add(
      curveOf(g3, d3, { color: RED, stroke: 2.6, n: 240 }),
      ...[[0, BLUE], [1, GREEN], [2, ORANGE], [4, PURPLE]].map(([K, c]) =>
        curveOf(clampFn(seriesFn((n, x) => ((-1) ** n) * x ** (2 * n + 1) / (2 * n + 1), 0, K), -1.35, 1.35), d3, { color: c, stroke: 1.6, n: 240 })),
      vlineAt(-1, { color: ASYMP, stroke: 1, dash: [4, 4] }),
      vlineAt(1, { color: ASYMP, stroke: 1, dash: [4, 4] }),
      legendAt([-1.1, 1.28], 'arctan x', RED, { font: 9.5 }),
      legendAt([-1.1, 1.02], 'partial sums  S₁, S₂, S₃, S₅', BLUE, { font: 9.5 }),
      labelAt([0, -1.3], '|x| < 1   (bad points at x = ±i)', { color: GRAY, font: 9, anchor: 'middle' }),
    );

  return subplots([s1, s2, s3], {
    cols: 3, tight: true,
    title: 'Building New Series from 1/(1−x)',
  });
}

// ── figure 레지스트리 ───────────────────────────────────────────
export const figures = {
  '18b-radius-convergence': radiusConvergence,
  '18b-building-series': buildingSeries,
};
