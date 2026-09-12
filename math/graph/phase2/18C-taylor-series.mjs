// math/graph/phase2/18C-taylor-series.mjs — 세션 18C(테일러 급수) 그림 복원
//
// ── figure 목록 (키 = 출력 파일명 = 마크다운 태그 id) ──────────────
//    18c-taylor-polynomials  (1×2) sin x 의 T₁,T₃,T₅,T₇ + 로그 오차
//    18c-taylor-exp          (1×2) eˣ 의 T₁,T₂,T₃,T₅ + 로그 오차
//
// ── 사용한 확장 (코어 수정 0 · 기준 logos 0.4.1) ────────────────────
//   곡선 = 코어 `curve.fn` · 로그 오차 = `_helpers.log10Err`(선형축에 log₁₀ 값을 그린다 —
//   코어에는 로그축이 없으므로 축 라벨로 명시한다) · 꼬리 평탄화 = `_helpers.clampFn`.
import {
  BLUE, ORANGE, GREEN, RED, PURPLE, GRAY,
  curveOf, labelAt, legendAt, seriesFn, fact, log10Err, clampFn, s2p, subplots, AX,
} from './_helpers.mjs';

const P = [520, 400];   // 1×2 패널 크기

// ── sin x 의 테일러 다항식 T_{2K+1}(x) ──────────────────────────
const sinT = (K) => seriesFn((n, x) => ((-1) ** n) * x ** (2 * n + 1) / fact(2 * n + 1), 0, K);
const SIN_TERMS = [[0, BLUE, 'T₁'], [1, GREEN, 'T₃'], [2, ORANGE, 'T₅'], [3, PURPLE, 'T₇']];

// ── 왼쪽 : 다항식이 sin x 에 겹쳐지는 모습 ──────────────────────
function panelSinPoly() {
  const dom = [-3.1, 3.1];
  const p = s2p(dom, [-3.3, 3.3], P, { axes: AX('x', 'y'), grid: { alpha: 0.25 } })
    .title('Taylor polynomials of sin x  at  a = 0');
  const add = [curveOf(Math.sin, dom, { color: RED, stroke: 2.8, n: 320 })];
  for (const [K, c] of SIN_TERMS) add.push(curveOf(clampFn(sinT(K), -3.25, 3.25), dom, { color: c, stroke: 1.8, n: 320 }));
  add.push(legendAt([-3.0, 3.0], 'sin x', RED));
  for (const [K, c, name] of SIN_TERMS) add.push(legendAt([-2.1 + K * 0.65, 3.0], name, c, { font: 10 }));
  add.push(labelAt([0, -3.0], 'T₁ = tangent, T₃ = +curl, T₅·T₇ = closer further out', { color: GRAY, font: 9, anchor: 'middle' }));
  return p.add(...add);
}

// ── 오른쪽 : 로그 오차 |sin x − T_N(x)| ─────────────────────────
function panelSinError() {
  const dom = [0.15, 3.15];
  const p = s2p(dom, [-12, 1.5], P, { axes: AX('x', 'log₁₀ |sin x − T_N(x)|'), grid: { alpha: 0.25 } })
    .title('Error on log scale');
  const add = [];
  for (const [K, c, name] of SIN_TERMS) add.push(curveOf(clampFn(log10Err(Math.sin, sinT(K)), -11.9, 1.4), dom, { color: c, stroke: 1.8, n: 320 }));
  add.push(legendAt([0.3, 1.35], 'T₁', BLUE, { font: 10 }));
  add.push(legendAt([0.75, 1.35], 'T₃', GREEN, { font: 10 }));
  add.push(legendAt([1.2, 1.35], 'T₅', ORANGE, { font: 10 }));
  add.push(legendAt([1.65, 1.35], 'T₇', PURPLE, { font: 10 }));
  add.push(labelAt([3.05, -11.2], 'error plunges near the center', { color: GRAY, font: 9, anchor: 'end' }));
  return p.add(...add);
}

// ── eˣ 의 테일러 다항식 T_N(x) ──────────────────────────────────
const expT = (N) => seriesFn((n, x) => x ** n / fact(n), 0, N);
const EXP_TERMS = [[1, BLUE, 'T₁'], [2, GREEN, 'T₂'], [3, ORANGE, 'T₃'], [5, PURPLE, 'T₅']];

// ── 왼쪽 : eˣ 근사 ─────────────────────────────────────────────
function panelExpPoly() {
  const dom = [-2, 2];
  const p = s2p(dom, [-1.2, 8], P, { axes: AX('x', 'y'), grid: { alpha: 0.25 } })
    .title('Taylor polynomials of eˣ  at  a = 0');
  const add = [curveOf(Math.exp, dom, { color: RED, stroke: 2.8, n: 320 })];
  for (const [N, c] of EXP_TERMS) add.push(curveOf(clampFn(expT(N), -1.15, 7.9), dom, { color: c, stroke: 1.8, n: 320 }));
  add.push(legendAt([-1.95, 7.4], 'eˣ', RED));
  for (const [i, [, c, name]] of EXP_TERMS.entries()) add.push(legendAt([-1.15 + i * 0.75, 7.4], name, c, { font: 10 }));
  return p.add(...add);
}

// ── 오른쪽 : 로그 오차 |eˣ − T_N(x)| ───────────────────────────
function panelExpError() {
  const dom = [0.1, 2.0];
  const p = s2p(dom, [-9, 1], P, { axes: AX('x', 'log₁₀ |eˣ − T_N(x)|'), grid: { alpha: 0.25 } })
    .title('Error on log scale');
  const add = [];
  for (const [N, c] of EXP_TERMS) add.push(curveOf(clampFn(log10Err(Math.exp, expT(N)), -8.9, 0.9), dom, { color: c, stroke: 1.8, n: 320 }));
  for (const [i, [, c, name]] of EXP_TERMS.entries()) add.push(legendAt([0.25 + i * 0.45, 0.85], name, c, { font: 10 }));
  add.push(labelAt([1.95, -8.4], 'error plunges near the center', { color: GRAY, font: 9, anchor: 'end' }));
  return p.add(...add);
}

// ── figure 레지스트리 ───────────────────────────────────────────
export const figures = {
  '18c-taylor-polynomials': () => subplots(
    [panelSinPoly(), panelSinError()],
    { cols: 2, tight: true, title: 'Taylor Polynomials and Their Error — sin x' },
  ),
  '18c-taylor-exp': () => subplots(
    [panelExpPoly(), panelExpError()],
    { cols: 2, tight: true, title: 'Taylor Polynomials and Their Error — eˣ' },
  ),
};
