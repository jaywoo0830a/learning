// math/graph/phase2/18A-series-convergence.mjs — 세션 18A(무한급수 수렴판정) 그림 복원
//
// ── figure 목록 (키 = 출력 파일명 = 마크다운 태그 id) ──────────────
//    18a-1-geometric-series     등비급수: 수렴(r=0.5) vs 발산(r=1.2) — 항 stem + 부분합 궤적
//    18a-2-p-series             p-급수 부분합(p=2,1,1/2) + 적분판정(Σ1/n² vs ∫1/x²)
//    18a-3-alternating-series   교대조화급수 → ln2 지그재그 + Σ1/n 발산 대비
//    18a-4-ratio-test           비판정: Σn!/nⁿ 비 → 1/e(<1) vs Σn!/2ⁿ 비 → ∞(>1)
//
// ── 사용한 확장 (코어 수정 0) ────────────────────────────────────
//   부분합 궤적 = 플러그인 `polyline` · 항 표시 = 플러그인 `stem`  (plugins/_math-extras.js)
import { region } from '@jaywoo0830a/logos';
import {
  BLUE, ORANGE, GREEN, RED, PURPLE, GRAY, LIGHT, ASYMP,
  dotAt, labelAt, hlineAt, curveOf, legendAt, polyline, stem, termsOf, partialSums,
  s2p, subplots, AX,
} from './_helpers.mjs';

// ══ 1. 등비급수 — 수렴 vs 발산 (1×2) ═════════════════════════════
//   왼쪽: Σ(0.5)ⁿ — 항은 줄고 부분합은 S∞=2 로. 오른쪽: Σ(1.2)ⁿ — 항도 부분합도 발산.
function geometricSeries() {
  const conv = (n) => 0.5 ** n, div = (n) => 1.2 ** n;
  const left = s2p([0, 9], [0, 2.4], [520, 420], { axes: AX('n', 'aₙ , Sₙ'), grid: { alpha: 0.28 } })
    .title('Σ (0.5)ⁿ  — converges').add(
      stem(...termsOf(conv, 0, 8)).color(BLUE).stroke(1.3).size(3),
      polyline(...partialSums(conv, 0, 8)).color(RED).stroke(2.2),
      ...partialSums(conv, 0, 8).map(([x, y]) => dotAt([x, y], RED, 4)),
      hlineAt(2, { color: RED, stroke: 1.2, dash: [5, 4] }),
      labelAt([8.7, 2.08], 'S∞ = 2', { color: RED, anchor: 'end', bold: true }),
      legendAt([0.3, 2.28], 'aₙ = (0.5)ⁿ', BLUE),
      legendAt([0.3, 2.05], 'Sₙ = partial sums', RED),
    );
  const right = s2p([0, 9], [0, 22], [520, 420], { axes: AX('n', 'aₙ , Sₙ'), grid: { alpha: 0.28 } })
    .title('Σ (1.2)ⁿ  — diverges').add(
      stem(...termsOf(div, 0, 8)).color(ORANGE).stroke(1.2).size(2.6),
      polyline(...partialSums(div, 0, 8)).color(RED).stroke(2.2),
      ...partialSums(div, 0, 8).map(([x, y]) => dotAt([x, y], RED, 4)),
      legendAt([0.4, 20.6], 'aₙ = (1.2)ⁿ', ORANGE),
      legendAt([0.4, 19.0], 'Sₙ = partial sums', RED),
      labelAt([6.5, 12], 'Sₙ → ∞  (r > 1)', { color: RED, anchor: 'middle', bold: true }),
    );
  return subplots([left, right], { cols: 2, tight: true, title: 'Geometric Series — Converge vs Diverge' });
}


// ══ 2. p-급수 + 적분판정 (1×2) ═══════════════════════════════════
//   왼쪽: Σ1/nᵖ 부분합 — p=2 수렴(π²/6), p=1·p=1/2 발산. 오른쪽: Σ1/n² ≤ 1 + ∫1/x² dx.
function pSeries() {
  const left = s2p([0, 51], [0, 15], [520, 420], { axes: AX('N', 'S_N'), grid: { alpha: 0.28 } })
    .title('Partial sums of Σ 1/nᵖ').add(
      polyline(...partialSums((n) => n ** -0.5, 1, 50)).color(RED).stroke(2.2),
      polyline(...partialSums((n) => 1 / n, 1, 50)).color(GREEN).stroke(2.2),
      polyline(...partialSums((n) => n ** -2, 1, 50)).color(BLUE).stroke(2.4),
      hlineAt(Math.PI ** 2 / 6, { color: BLUE, stroke: 1, dash: [5, 4], opacity: 0.7 }),
      legendAt([30, 14.2], 'p = 1/2  → diverges', RED),
      legendAt([30, 4.6], 'p = 1  → diverges', GREEN),
      legendAt([40, 1.95], 'p = 2  → π²/6 ≈ 1.645', BLUE),
    );
  const right = s2p([0, 8], [0, 1.15], [520, 420], { axes: AX('n  /  x', 'value'), grid: { alpha: 0.28 } })
    .title('Integral test:  Σ 1/n²  vs  ∫₁^∞ 1/x² dx').add(
      region.between((x) => 1 / (x * x), 0).on([1, 8]).fill(BLUE).opacity(0.16),
      stem(...termsOf((n) => 1 / (n * n), 1, 8)).color(ORANGE).stroke(1.2).size(2.6),
      curveOf((x) => 1 / (x * x), [1, 8], { color: BLUE, stroke: 2.4, n: 200 }),
      legendAt([2.4, 0.96], 'f(x) = 1/x²', BLUE),
      legendAt([2.4, 0.84], 'aₙ = 1/n²  (stems)', ORANGE),
      labelAt([4.6, 0.30], '∫₁^∞ 1/x² dx = 1', { color: BLUE, anchor: 'middle', box: true }),
      labelAt([4.6, 0.12], '→ Σ 1/n² converges', { color: BLUE, anchor: 'middle', bold: true }),
    );
  return subplots([left, right], { cols: 2, tight: true, title: 'p-Series and the Integral Test' });
}

// ══ 3. 교대조화급수 (1×2) ════════════════════════════════════════
//   왼쪽: Σ(−1)ⁿ⁺¹/n 부분합이 ln2 로 지그재그 수렴. 오른쪽: Σ1/n(발산) 대비(조건수렴).
function alternatingSeries() {
  const alt = (n) => ((-1) ** (n + 1)) / n;
  const S = partialSums(alt, 1, 24);
  const left = s2p([0, 25], [0, 1.2], [520, 420], { axes: AX('N', 'S_N'), grid: { alpha: 0.28 } })
    .title('Σ (−1)ⁿ⁺¹/n  →  ln 2').add(
      polyline(...S).color(BLUE).stroke(1.8),
      ...S.map(([x, y]) => dotAt([x, y], BLUE, 3.4)),
      hlineAt(Math.LN2, { color: RED, stroke: 1.2, dash: [5, 4] }),
      labelAt([24, Math.LN2 + 0.04], 'ln 2 ≈ 0.693', { color: RED, anchor: 'end', bold: true }),
      labelAt([12, 1.1], 'partial sums zigzag in', { color: BLUE, anchor: 'middle' }),
    );
  const right = s2p([0, 25], [0, 4], [520, 420], { axes: AX('N', 'S_N'), grid: { alpha: 0.28 } })
    .title('Σ 1/n (diverges)  vs  Σ (−1)ⁿ⁺¹/n (converges)').add(
      polyline(...partialSums((n) => 1 / n, 1, 24)).color(GREEN).stroke(2.2),
      polyline(...S).color(BLUE).stroke(2.2),
      hlineAt(Math.LN2, { color: RED, stroke: 1, dash: [5, 4], opacity: 0.6 }),
      legendAt([18, 3.3], 'Σ 1/n  (diverges)', GREEN),
      legendAt([24, 0.95], 'Σ (−1)ⁿ⁺¹/n  (→ ln 2)', BLUE, { anchor: 'end' }),
    );
  return subplots([left, right], { cols: 2, tight: true, title: 'Alternating Series and Conditional Convergence' });
}

// ══ 4. 비판정 (1×2) ══════════════════════════════════════════════
//   왼쪽: Σn!/nⁿ 의 비 → 1/e < 1 (수렴). 오른쪽: Σn!/2ⁿ 의 비 = (n+1)/2 → ∞ (발산).
function ratioTest() {
  const rConv = (n) => (n / (n + 1)) ** n;
  const left = s2p([1, 20], [0.3, 1.08], [520, 420], { axes: AX('n', 'aₙ₊₁ / aₙ'), grid: { alpha: 0.28 } })
    .title('Σ n!/nⁿ :  ratio → 1/e < 1  → converges').add(
      polyline(...termsOf(rConv, 1, 20)).color(BLUE).stroke(2.2),
      ...termsOf(rConv, 1, 20).map(([x, y]) => dotAt([x, y], BLUE, 3)),
      hlineAt(1, { color: ASYMP, stroke: 1, dash: [4, 4] }),
      hlineAt(Math.exp(-1), { color: RED, stroke: 1.2, dash: [5, 4] }),
      labelAt([20, 1.03], 'ρ = 1', { color: GRAY, anchor: 'end' }),
      labelAt([20, Math.exp(-1) + 0.035], '1/e ≈ 0.368', { color: RED, anchor: 'end', bold: true }),
    );
  const rDiv = (n) => (n + 1) / 2;
  const right = s2p([1, 10], [0, 6], [520, 420], { axes: AX('n', 'aₙ₊₁ / aₙ'), grid: { alpha: 0.28 } })
    .title('Σ n!/2ⁿ :  ratio grows > 1  → diverges').add(
      polyline(...termsOf(rDiv, 1, 10)).color(ORANGE).stroke(2.2),
      ...termsOf(rDiv, 1, 10).map(([x, y]) => dotAt([x, y], ORANGE, 3)),
      hlineAt(1, { color: RED, stroke: 1.2, dash: [5, 4] }),
      labelAt([10, 1.12], 'ρ = 1', { color: RED, anchor: 'end', bold: true }),
      labelAt([5.5, 4.8], 'ratio → ∞', { color: ORANGE, anchor: 'middle' }),
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
