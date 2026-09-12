// math/graph/phase2/18B/18B-power-series.mjs — 세션 18B(멱급수) 그림
//
// ── figure 목록 (키 = 출력 파일명 = 마크다운 태그 id) ──────────────
//    18b-radius-convergence  (2×2) R 의 세 경우 · Σxⁿ 부분합 · 끝점 검사 · 수렴구간 표
//    18b-building-series     (1×3) 1/(1−x) 에서 치환·적분으로 만든 세 급수
//
// ── 코어 API 만 쓴다 (기준 @jaywoo0830a/logos 0.4.1 · 이 폴더 전용) ──
//   곡선   curve.fn(f).on(dom) + .color().stroke().n()
//   선분   segment([x,y], [x,y]) — 코어가 좌표 배열을 받는다(toPoint). 굵은 구간 막대도 같은 API
//   기준선 line.horizontal(y) · 마커 point(x,y).dot()/.marker('circle', { open })
//   라벨   annotate.text([x,y]).label(t).font(n).color(c).bold().anchor()
//   색     kit.palette.tab 구조분해
//   순수 JS 수학(seriesFn·clampFn)만 ./_helper.mjs (다른 폴더와 공유하지 않는다)
import { annotate, curve, kit, line, point, segment } from '@jaywoo0830a/logos';
import { clampFn, seriesFn } from './_helper.mjs';

const { plot2d, subplots, palette } = kit;
const { blue, green, orange, purple, red, gray } = palette.tab;

const P2 = [430, 330];   // 2×2 패널 크기
const P3 = [430, 360];   // 1×3 패널 크기
const ASYMP = '#cccccc'; // 점근선·경계 보조선(지면 톤 — 팔레트 밖)

/** 축 설정 — 코어 plot2d 의 axes 옵션 그대로 (y 눈금을 끄는 변형만 별도) */
const AX = (x, y) => ({ x: { label: x }, y: { label: y } });
const AXx = (x) => ({ x: { label: x }, y: { label: false, ticks: false } });

// ── TL : 반지름의 세 가지 경우 (R=1 · R=∞ · R=0) ────────────────
function panelRadiusCases() {
  const cases = [
    { y: 2.3, color: blue, half: 1, name: 'Σ xⁿ', tag: 'R = 1' },
    { y: 1.3, color: green, half: 3, name: 'Σ xⁿ/n!', tag: 'R = ∞' },
    { y: 0.3, color: orange, half: 0, name: 'Σ n! xⁿ', tag: 'R = 0' },
  ];
  const draws = [];
  for (const c of cases) {
    draws.push(annotate.text([-2.85, c.y + 0.26]).label(c.name).font(10).color(c.color).bold());
    draws.push(annotate.text([2.85, c.y + 0.26]).label(c.tag).font(10).color(c.color).bold().anchor('end'));
    if (c.half === 0) {
      draws.push(point(0, c.y).dot().color(c.color).size(5.5));
      draws.push(annotate.text([0.4, c.y]).label('converges only at x = 0').font(9).color(c.color));
    } else {
      draws.push(segment([-c.half, c.y], [c.half, c.y]).color(c.color).stroke(6.5));
      if (c.half === 1) {                    // 끝점은 따로 판정 — 빈 원
        draws.push(point(-1, c.y).marker('circle', { open: true }).color(c.color).size(4.5));
        draws.push(point(1, c.y).marker('circle', { open: true }).color(c.color).size(4.5));
        draws.push(annotate.text([2.85, c.y - 0.4]).label('endpoints: check separately').font(9).color(c.color).anchor('end'));
      } else {
        draws.push(annotate.text([2.85, c.y - 0.4]).label('converges for every x').font(9).color(c.color).anchor('end'));
      }
    }
  }
  return plot2d([-3, 3], [-0.6, 3], { size: P2, axes: AXx('x'), grid: { alpha: 0.25 } })
    .title('Radius of convergence — three cases')
    .add(...draws);
}

// ── TR : Σxⁿ 의 부분합이 1/(1−x) 로 수렴 ────────────────────────
function panelGeomPartials() {
  const Sg = (N) => seriesFn((n, x) => x ** n, 0, N);
  const dom = [-0.8, 0.8];
  return plot2d(dom, [-1, 6], { size: P2, axes: AX('x', 'S_N(x)'), grid: { alpha: 0.25 } })
    .title('Partial sums: Σ xⁿ → 1/(1−x)')
    .add(
      curve.fn((x) => 1 / (1 - x)).on(dom).color(red).stroke(2.6).n(240),
      curve.fn(clampFn(Sg(1), -0.95, 5.9)).on(dom).color(blue).stroke(1.6).n(240),
      curve.fn(clampFn(Sg(3), -0.95, 5.9)).on(dom).color(green).stroke(1.6).n(240),
      curve.fn(clampFn(Sg(7), -0.95, 5.9)).on(dom).color(orange).stroke(1.6).n(240),
      annotate.text([-0.77, 5.5]).label('1/(1−x)  (true sum)').font(10).color(red).bold(),
      annotate.text([-0.77, 5.0]).label('S₁').font(10).color(blue).bold(),
      annotate.text([-0.52, 5.0]).label('S₃').font(10).color(green).bold(),
      annotate.text([-0.28, 5.0]).label('S₇').font(10).color(orange).bold(),
      annotate.text([0.4, 0.45]).label('converges only for |x| < 1').font(9).color(gray).anchor('middle'),
    );
}

// ── BL : Σxⁿ/n 의 끝점 — x=1 발산 vs x=−1 수렴 ──────────────────
function panelEndpoints() {
  const SN = (x, N) => { let s = 0; for (let n = 1; n <= N; n++) s += x ** n / n; return s; };
  const Ns = Array.from({ length: 60 }, (_, i) => i + 1);
  return plot2d([0, 60], [-1.4, 5], { size: P2, axes: AX('N', 'S_N'), grid: { alpha: 0.25 } })
    .title('Endpoint check:  Σ xⁿ/n   at   x = 1, −1, 0.9')
    .add(
      ...Ns.map((N) => point(N, SN(1, N)).dot().color(red).size(2.6)),
      ...Ns.map((N) => point(N, SN(0.9, N)).dot().color(green).size(2.6)),
      ...Ns.map((N) => point(N, SN(-1, N)).dot().color(blue).size(2.6)),
      line.horizontal(-Math.LN2).color(blue).stroke(1).dash([4, 4]).opacity(0.7),
      annotate.text([59, 4.7]).label('x = 1 :  harmonic  →  diverges').font(9.5).color(red).bold().anchor('end'),
      annotate.text([59, 2.75]).label('x = 0.9 :  →  −ln(0.1) ≈ 2.303').font(9.5).color(green).anchor('end'),
      annotate.text([59, -1.05]).label('x = −1 :  →  −ln 2 ≈ −0.693').font(9.5).color(blue).anchor('end'),
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
  const draws = [];
  for (const r of rows) {
    draws.push(annotate.text([-4.9, r.y + 0.06]).label(r.name).font(10).color(gray));
    draws.push(annotate.text([3.55, r.y + 0.06]).label(r.tag).font(9.5).color(red).bold().anchor('end'));
    if (r.lo === r.hi) {
      draws.push(point(r.lo, r.y).dot().color(green).size(5));
    } else {
      draws.push(segment([r.lo, r.y], [r.hi, r.y]).color(green).stroke(6));
      draws.push(point(r.lo, r.y).marker('circle', { open: r.loOpen }).color(r.loOpen ? red : green).size(4.5));
      draws.push(point(r.hi, r.y).marker('circle', { open: r.hiOpen }).color(r.hiOpen ? red : green).size(4.5));
    }
  }
  draws.push(annotate.text([-4.9, 4.72]).label('● converges      ○ diverges').font(9).color(gray));
  return plot2d([-5, 3.6], [-0.6, 4.9], { size: P2, axes: AXx('x'), grid: { alpha: 0.2 } })
    .title('Intervals of convergence')
    .add(...draws);
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
  const s1 = plot2d(d1, [-0.6, 7], { size: P3, axes: AX('x', 'value'), grid: { alpha: 0.25 } })
    .title('1/(1+x)   ←   x → −x')
    .add(
      curve.fn(g1).on(d1).color(red).stroke(2.6).n(240),
      ...[[1, blue], [3, green], [7, orange], [15, purple]].map(([N, c]) =>
        curve.fn(clampFn(seriesFn((n, x) => (-1) ** n * x ** n, 0, N), 0.02, 6.9)).on(d1).color(c).stroke(1.6).n(240)),
      annotate.text([-0.8, 6.55]).label('1/(1+x)').font(9.5).color(red).bold(),
      annotate.text([-0.05, 6.55]).label('S₁, S₃, S₇, S₁₅').font(9.5).color(blue).bold(),
    );

  // ② ln(1+x) = Σ (−1)ⁿ⁺¹ xⁿ/n   (적분)
  const g2 = (x) => Math.log(1 + x);
  const d2 = [-0.9, 1.0];
  const s2 = plot2d(d2, [-2.3, 1.6], { size: P3, axes: AX('x', 'value'), grid: { alpha: 0.25 } })
    .title('ln(1+x)   ←   ∫ 1/(1+x) dx')
    .add(
      curve.fn(g2).on(d2).color(red).stroke(2.6).n(240),
      ...[[1, blue], [2, green], [5, orange], [20, purple]].map(([N, c]) =>
        curve.fn(clampFn(seriesFn((n, x) => ((-1) ** (n + 1)) * x ** n / n, 1, N), -2.25, 1.55)).on(d2).color(c).stroke(1.6).n(240)),
      line.vertical(-1).color(ASYMP).stroke(1).dash([4, 4]),
      annotate.text([-0.86, 1.45]).label('ln(1+x)').font(9.5).color(red).bold(),
      annotate.text([-0.86, 1.15]).label('partial sums  S₁, S₂, S₅, S₂₀').font(9.5).color(blue).bold(),
      annotate.text([0.95, -2.05]).label('x = −1 : log 0').font(9).color(gray).anchor('end'),
    );

  // ③ arctan x = Σ (−1)ⁿ x^{2n+1}/(2n+1)   (1/(1+x²) 적분, 반지름 1)
  const d3 = [-1.15, 1.15];
  const s3 = plot2d(d3, [-1.4, 1.4], { size: P3, axes: AX('x', 'value'), grid: { alpha: 0.25 } })
    .title('arctan x   ←   ∫ 1/(1+x²) dx')
    .add(
      curve.fn(Math.atan).on(d3).color(red).stroke(2.6).n(240),
      ...[[0, blue], [1, green], [2, orange], [4, purple]].map(([K, c]) =>
        curve.fn(clampFn(seriesFn((n, x) => ((-1) ** n) * x ** (2 * n + 1) / (2 * n + 1), 0, K), -1.35, 1.35)).on(d3).color(c).stroke(1.6).n(240)),
      line.vertical(-1).color(ASYMP).stroke(1).dash([4, 4]),
      line.vertical(1).color(ASYMP).stroke(1).dash([4, 4]),
      annotate.text([-1.1, 1.28]).label('arctan x').font(9.5).color(red).bold(),
      annotate.text([-1.1, 1.02]).label('partial sums  S₁, S₂, S₃, S₅').font(9.5).color(blue).bold(),
      annotate.text([0, -1.3]).label('|x| < 1   (bad points at x = ±i)').font(9).color(gray).anchor('middle'),
    );

  return subplots([s1, s2, s3], { cols: 3, tight: true, title: 'Building New Series from 1/(1−x)' });
}

// ── figure 레지스트리 ───────────────────────────────────────────
export const figures = {
  '18b-radius-convergence': radiusConvergence,
  '18b-building-series': buildingSeries,
};
