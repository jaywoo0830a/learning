// math/graph/phase2/18C/18C-taylor-series.mjs — 세션 18C(테일러 급수) 그림
//
// ── figure 목록 (키 = 출력 파일명 = 마크다운 태그 id) ──────────────
//    18c-taylor-polynomials  (1×2) sin x 의 T₁,T₃,T₅,T₇ + 로그 오차
//    18c-taylor-exp          (1×2) eˣ 의 T₁,T₂,T₃,T₅ + 로그 오차
//
// ── 코어 API 만 쓴다 (기준 @jaywoo0830a/logos 0.4.1 · 이 폴더 전용) ──
//   패널  `kit.plot2d(xr, yr, { size, axes, grid })` · 병치 `kit.subplots([...], { cols })`
//   곡선  `curve.fn(f).on(dom)` + `.color().stroke().n()` 체이닝
//   라벨  `annotate.text([x, y]).label(t).font(n).color(c).anchor()` (배열 좌표 허용)
//   색    `kit.palette.tab` 을 구조분해 — 이름 그대로 쓴다(hex 하드코딩 없음)
//   순수 JS 수학(fact·seriesFn·log10Err·clampFn)만 `./_helper.mjs` (다른 폴더와 공유하지 않는다)
import { annotate, curve, kit } from '@jaywoo0830a/logos';
import { clampFn, fact, log10Err, seriesFn } from './_helper.mjs';

const { plot2d, subplots, palette } = kit;
const { blue, green, orange, purple, red, gray } = palette.tab;

/** 이 세션의 패널 프리셋 — 크기·격자는 고정, y축 라벨만 바꾼다(코어 plot2d 옵션 위에 얹음) */
const panel = (xr, yr, yLabel) =>
  plot2d(xr, yr, { size: [520, 400], axes: { x: { label: 'x' }, y: { label: yLabel } }, grid: { alpha: 0.25 } });

/** 범례 대신 같은 색 라벨 — 코어 annotate.text 체이닝의 1줄 별칭(이 파일 안에서만) */
const legend = (at, text, color, font = 10) => annotate.text(at).label(text).font(font).color(color).bold();

// ── sin x 의 테일러 다항식 T_{2K+1}(x) ──────────────────────────
const sinT = (K) => seriesFn((n, x) => ((-1) ** n) * x ** (2 * n + 1) / fact(2 * n + 1), 0, K);
const SIN_TERMS = [[0, blue, 'T₁'], [1, green, 'T₃'], [2, orange, 'T₅'], [3, purple, 'T₇']];

/** 왼쪽: 다항식이 sin x 에 겹쳐지는 모습 */
function panelSinPoly() {
  const dom = [-3.1, 3.1];
  const draws = [curve.fn(Math.sin).on(dom).color(red).stroke(2.8).n(320)];
  for (const [K, c] of SIN_TERMS) draws.push(curve.fn(clampFn(sinT(K), -3.25, 3.25)).on(dom).color(c).stroke(1.8).n(320));
  draws.push(legend([-3.0, 3.0], 'sin x', red));
  for (const [K, c, name] of SIN_TERMS) draws.push(legend([-2.1 + K * 0.65, 3.0], name, c));
  draws.push(annotate.text([0, -3.0]).label('T₁ = tangent, T₃ = +curl, T₅·T₇ = closer further out').font(9).color(gray).anchor('middle'));
  return panel(dom, [-3.3, 3.3], 'y').title('Taylor polynomials of sin x  at  a = 0').add(...draws);
}

/** 오른쪽: 로그 오차 |sin x − T_N(x)| */
function panelSinError() {
  const dom = [0.15, 3.15];
  const draws = [];
  for (const [K, c] of SIN_TERMS) draws.push(curve.fn(clampFn(log10Err(Math.sin, sinT(K)), -11.9, 1.4)).on(dom).color(c).stroke(1.8).n(320));
  for (const [i, [, c, name]] of SIN_TERMS.entries()) draws.push(legend([0.3 + i * 0.45, 1.35], name, c));
  draws.push(annotate.text([3.05, -11.2]).label('error plunges near the center').font(9).color(gray).anchor('end'));
  return panel(dom, [-12, 1.5], 'log₁₀ |sin x − T_N(x)|').title('Error on log scale').add(...draws);
}

// ── eˣ 의 테일러 다항식 T_N(x) ──────────────────────────────────
const expT = (N) => seriesFn((n, x) => x ** n / fact(n), 0, N);
const EXP_TERMS = [[1, blue, 'T₁'], [2, green, 'T₂'], [3, orange, 'T₃'], [5, purple, 'T₅']];

/** 왼쪽: eˣ 근사 */
function panelExpPoly() {
  const dom = [-2, 2];
  const draws = [curve.fn(Math.exp).on(dom).color(red).stroke(2.8).n(320)];
  for (const [N, c] of EXP_TERMS) draws.push(curve.fn(clampFn(expT(N), -1.15, 7.9)).on(dom).color(c).stroke(1.8).n(320));
  draws.push(legend([-1.95, 7.4], 'eˣ', red));
  for (const [i, [, c, name]] of EXP_TERMS.entries()) draws.push(legend([-1.15 + i * 0.75, 7.4], name, c));
  return panel(dom, [-1.2, 8], 'y').title('Taylor polynomials of eˣ  at  a = 0').add(...draws);
}

/** 오른쪽: 로그 오차 |eˣ − T_N(x)| */
function panelExpError() {
  const dom = [0.1, 2.0];
  const draws = [];
  for (const [N, c] of EXP_TERMS) draws.push(curve.fn(clampFn(log10Err(Math.exp, expT(N)), -8.9, 0.9)).on(dom).color(c).stroke(1.8).n(320));
  for (const [i, [, c, name]] of EXP_TERMS.entries()) draws.push(legend([0.25 + i * 0.45, 0.85], name, c));
  draws.push(annotate.text([1.95, -8.4]).label('error plunges near the center').font(9).color(gray).anchor('end'));
  return panel(dom, [-9, 1], 'log₁₀ |eˣ − T_N(x)|').title('Error on log scale').add(...draws);
}

// ── figure 레지스트리 ───────────────────────────────────────────
export const figures = {
  '18c-taylor-polynomials': () => subplots([panelSinPoly(), panelSinError()],
    { cols: 2, tight: true, title: 'Taylor Polynomials and Their Error — sin x' }),
  '18c-taylor-exp': () => subplots([panelExpPoly(), panelExpError()],
    { cols: 2, tight: true, title: 'Taylor Polynomials and Their Error — eˣ' }),
};
