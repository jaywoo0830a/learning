// math/graph/phase2/18A/18A-series-convergence.mjs — 세션 18A(무한급수 수렴판정) 그림
//
// ── figure 목록 (키 = 출력 파일명 = 마크다운 태그 id) ──────────────
//    18a-1-geometric-series     등비급수: 수렴(r=0.5) vs 발산(r=1.2) — 항 stem + 부분합 궤적
//    18a-2-p-series             p-급수 부분합(p=2,1,1/2) + 적분판정(Σ1/n² vs ∫1/x²)
//    18a-3-alternating-series   교대조화급수 → ln2 지그재그 + Σ1/n 발산 대비
//    18a-4-ratio-test           비판정: Σn!/nⁿ 비 → 1/e(<1) vs Σn!/2ⁿ 비 → ∞(>1)
//
// ── 코어 API + 이 폴더 전용 확장 (기준 @jaywoo0830a/logos 0.4.1) ────
//   곡선·기준선·영역·마커·라벨 = 코어 `curve.fn` · `line.horizontal/vertical` · `region.between`
//                                · `point(x,y).dot()` · `annotate.text([x,y])`
//   항(stem)과 부분합 궤적(polyline)만 `./_plugin.mjs` — 코어에 1급 빌더가 없다
//   (코어 `curve.piecewise` 는 구간별 함수, `curve.spline` 은 매끄러운 곡선이라 점 목록을 직선으로 잇지 못한다)
//   순수 JS 수학(termsOf·partialSums)은 `./_helper.mjs`
import { annotate, curve, kit, line, plugins, point, region, use } from '@jaywoo0830a/logos';
import mathExtras from './_plugin.mjs';
import { partialSums, termsOf } from './_helper.mjs';

use(mathExtras);   // plugins.polyline · plugins.stem (코어 수정 0 · 이 폴더 전용)

const { plot2d, subplots, palette } = kit;
const { blue, green, orange, red, purple, gray } = palette.tab;
const LIGHT = '#bbbbbb', ASYMP = '#cccccc';   // 지면 톤(팔레트 밖)

/** 축 설정 — 코어 plot2d 의 axes 옵션 그대로 */
const AX = (x, y) => ({ x: { label: x }, y: { label: y } });

/** 범례 대신 같은 색 라벨 (코어 annotate.text 체이닝의 1줄 별칭 — 이 파일 안에서만) */
const legend = (at, text, color, font = 10.5, anchor = 'start') =>
  annotate.text(at).label(text).font(font).color(color).bold().anchor(anchor);

// ══ 1. 등비급수 — 수렴 vs 발산 (1×2) ═════════════════════════════
//   왼쪽: Σ(0.5)ⁿ — 항은 줄고 부분합은 S∞=2 로. 오른쪽: Σ(1.2)ⁿ — 항도 부분합도 발산.
function geometricSeries() {
  const conv = (n) => 0.5 ** n, div = (n) => 1.2 ** n;
  const sums = partialSums(conv, 0, 8);
  const left = plot2d([0, 9], [0, 2.4], { size: [520, 420], axes: AX('n', 'aₙ , Sₙ'), grid: { alpha: 0.28 } })
    .title('Σ (0.5)ⁿ  — converges').add(
      plugins.stem(...termsOf(conv, 0, 8)).color(blue).stroke(1.3).size(3),
      plugins.polyline(...sums).color(red).stroke(2.2),
      ...sums.map(([x, y]) => point(x, y).dot().color(red).size(4)),
      line.horizontal(2).color(red).stroke(1.2).dash([5, 4]),
      annotate.text([8.7, 2.08]).label('S∞ = 2').font(10.5).color(red).bold().anchor('end'),
      legend([0.3, 2.28], 'aₙ = (0.5)ⁿ', blue),
      legend([0.3, 2.05], 'Sₙ = partial sums', red),
    );
  const divSums = partialSums(div, 0, 8);
  const right = plot2d([0, 9], [0, 22], { size: [520, 420], axes: AX('n', 'aₙ , Sₙ'), grid: { alpha: 0.28 } })
    .title('Σ (1.2)ⁿ  — diverges').add(
      plugins.stem(...termsOf(div, 0, 8)).color(orange).stroke(1.2).size(2.6),
      plugins.polyline(...divSums).color(red).stroke(2.2),
      ...divSums.map(([x, y]) => point(x, y).dot().color(red).size(4)),
      legend([0.4, 20.6], 'aₙ = (1.2)ⁿ', orange),
      legend([0.4, 19.0], 'Sₙ = partial sums', red),
      annotate.text([6.5, 12]).label('Sₙ → ∞  (r > 1)').font(10.5).color(red).bold().anchor('middle'),
    );
  return subplots([left, right], { cols: 2, tight: true, title: 'Geometric Series — Converge vs Diverge' });
}

// ══ 2. p-급수 + 적분판정 (1×2) ═══════════════════════════════════
//   왼쪽: Σ1/nᵖ 부분합 — p=2 수렴(π²/6), p=1·p=1/2 발산. 오른쪽: Σ1/n² ≤ 1 + ∫1/x² dx.
function pSeries() {
  const left = plot2d([0, 51], [0, 15], { size: [520, 420], axes: AX('N', 'S_N'), grid: { alpha: 0.28 } })
    .title('Partial sums of Σ 1/nᵖ').add(
      plugins.polyline(...partialSums((n) => n ** -0.5, 1, 50)).color(red).stroke(2.2),
      plugins.polyline(...partialSums((n) => 1 / n, 1, 50)).color(green).stroke(2.2),
      plugins.polyline(...partialSums((n) => n ** -2, 1, 50)).color(blue).stroke(2.4),
      line.horizontal(Math.PI ** 2 / 6).color(blue).stroke(1).dash([5, 4]).opacity(0.7),
      legend([30, 14.2], 'p = 1/2  → diverges', red),
      legend([30, 4.6], 'p = 1  → diverges', green),
      legend([40, 1.95], 'p = 2  → π²/6 ≈ 1.645', blue),
    );
  const right = plot2d([0, 8], [0, 1.15], { size: [520, 420], axes: AX('n  /  x', 'value'), grid: { alpha: 0.28 } })
    .title('Integral test:  Σ 1/n²  vs  ∫₁^∞ 1/x² dx').add(
      region.between((x) => 1 / (x * x)).on([1, 8]).fill(blue).opacity(0.16),
      plugins.stem(...termsOf((n) => 1 / (n * n), 1, 8)).color(orange).stroke(1.2).size(2.6),
      curve.fn((x) => 1 / (x * x)).on([1, 8]).color(blue).stroke(2.4).n(200),
      legend([2.4, 0.96], 'f(x) = 1/x²', blue),
      legend([2.4, 0.84], 'aₙ = 1/n²  (stems)', orange),
      annotate.text([4.6, 0.30]).label('∫₁^∞ 1/x² dx = 1').font(10.5).color(blue).bold().anchor('middle').box(true),
      annotate.text([4.6, 0.12]).label('→ Σ 1/n² converges').font(10.5).color(blue).bold().anchor('middle'),
    );
  return subplots([left, right], { cols: 2, tight: true, title: 'p-Series and the Integral Test' });
}

// ══ 3. 교대조화급수 (1×2) ════════════════════════════════════════
//   왼쪽: Σ(−1)ⁿ⁺¹/n 부분합이 ln2 로 지그재그 수렴. 오른쪽: Σ1/n(발산) 대비(조건수렴).
function alternatingSeries() {
  const alt = (n) => ((-1) ** (n + 1)) / n;
  const S = partialSums(alt, 1, 24);
  const left = plot2d([0, 25], [0, 1.2], { size: [520, 420], axes: AX('N', 'S_N'), grid: { alpha: 0.28 } })
    .title('Σ (−1)ⁿ⁺¹/n  →  ln 2').add(
      plugins.polyline(...S).color(blue).stroke(1.8),
      ...S.map(([x, y]) => point(x, y).dot().color(blue).size(3.4)),
      line.horizontal(Math.LN2).color(red).stroke(1.2).dash([5, 4]),
      annotate.text([24, Math.LN2 + 0.04]).label('ln 2 ≈ 0.693').font(10.5).color(red).bold().anchor('end'),
      annotate.text([12, 1.1]).label('partial sums zigzag in').font(10.5).color(blue).anchor('middle'),
    );
  const right = plot2d([0, 25], [0, 4], { size: [520, 420], axes: AX('N', 'S_N'), grid: { alpha: 0.28 } })
    .title('Σ 1/n (diverges)  vs  Σ (−1)ⁿ⁺¹/n (converges)').add(
      plugins.polyline(...partialSums((n) => 1 / n, 1, 24)).color(green).stroke(2.2),
      plugins.polyline(...S).color(blue).stroke(2.2),
      line.horizontal(Math.LN2).color(red).stroke(1).dash([5, 4]).opacity(0.6),
      legend([18, 3.3], 'Σ 1/n  (diverges)', green),
      legend([24, 0.95], 'Σ (−1)ⁿ⁺¹/n  (→ ln 2)', blue, 10.5, 'end'),
    );
  return subplots([left, right], { cols: 2, tight: true, title: 'Alternating Series and Conditional Convergence' });
}

// ══ 4. 비판정 (1×2) ══════════════════════════════════════════════
//   왼쪽: Σn!/nⁿ 의 비 → 1/e < 1 (수렴). 오른쪽: Σn!/2ⁿ 의 비 = (n+1)/2 → ∞ (발산).
function ratioTest() {
  const rConv = (n) => (n / (n + 1)) ** n;
  const convTerms = termsOf(rConv, 1, 20);
  const left = plot2d([1, 20], [0.3, 1.08], { size: [520, 420], axes: AX('n', 'aₙ₊₁ / aₙ'), grid: { alpha: 0.28 } })
    .title('Σ n!/nⁿ :  ratio → 1/e < 1  → converges').add(
      plugins.polyline(...convTerms).color(blue).stroke(2.2),
      ...convTerms.map(([x, y]) => point(x, y).dot().color(blue).size(3)),
      line.horizontal(1).color(ASYMP).stroke(1).dash([4, 4]),
      line.horizontal(Math.exp(-1)).color(red).stroke(1.2).dash([5, 4]),
      annotate.text([20, 1.03]).label('ρ = 1').font(10.5).color(gray).anchor('end'),
      annotate.text([20, Math.exp(-1) + 0.035]).label('1/e ≈ 0.368').font(10.5).color(red).bold().anchor('end'),
    );
  const rDiv = (n) => (n + 1) / 2;
  const divTerms = termsOf(rDiv, 1, 10);
  const right = plot2d([1, 10], [0, 6], { size: [520, 420], axes: AX('n', 'aₙ₊₁ / aₙ'), grid: { alpha: 0.28 } })
    .title('Σ n!/2ⁿ :  ratio grows > 1  → diverges').add(
      plugins.polyline(...divTerms).color(orange).stroke(2.2),
      ...divTerms.map(([x, y]) => point(x, y).dot().color(orange).size(3)),
      line.horizontal(1).color(red).stroke(1.2).dash([5, 4]),
      annotate.text([10, 1.12]).label('ρ = 1').font(10.5).color(red).bold().anchor('end'),
      annotate.text([5.5, 4.8]).label('ratio → ∞').font(10.5).color(orange).anchor('middle'),
    );
  return subplots([left, right], { cols: 2, tight: true, title: 'Ratio Test' });
}

// ── figure 레지스트리 ───────────────────────────────────────────
export const figures = {
  '18a-1-geometric-series': geometricSeries,
  '18a-2-p-series': pSeries,
  '18a-3-alternating-series': alternatingSeries,
  '18a-4-ratio-test': ratioTest,
};
