// math/graph/phase2/_helpers.mjs — phase2 스케치 공용 헬퍼 (14D·14D1·18A·18B·18C …)
//
// `_` 로 시작하므로 logos 렌더러가 스케치로 취급하지 않고 건너뛴다(문서 규칙).
// 코어 위의 얇은 별칭 + 플러그인(_math-extras: polyline·stem) 설치만 담당한다.
// 여기 있는 것은 전부 **얇은 별칭**이다 — 새 그림 문법을 발명하지 않고
// 코어 빌더(`curve.fn`·`region.*`·`point/segment/annotate`)를 짧게 부르는 것뿐.
import {
  point, line, segment, curve, region, annotate, kit, use, plugins,
} from '@jaywoo0830a/logos';
import mathExtras from '../plugins/_math-extras.js';

// 플러그인 설치(코어 수정 0) — plugins.polyline / plugins.stem 이 살아난다
use(mathExtras);

export const { plot2d, plot3d, subplots } = kit;

// ── 색 — mpl 기본 팔레트 계열 (곡선·라벨·범례가 같은 색 공유) ─────
export const BLUE = '#1f77b4', ORANGE = '#ff7f0e', GREEN = '#2ca02c', RED = '#d62728';
export const PURPLE = '#9467bd', BROWN = '#8c564b', PINK = '#e377c2', GRAY = '#7f7f7f';
export const LIGHT = '#bbbbbb', ASYMP = '#cccccc', GOLD = '#b8860b';
export const BOX = { facecolor: 'white', alpha: 0.85 };

// ── 미세 헬퍼 (전부 라이브러리 API 위의 얇은 별칭) ──────────────
/** 점 좌표 — [x, y] 는 2D, [x, y, z] 는 3D(3D 패널에서 코어가 투영). 라벨·선·마커가 공유한다. */
export const P = (v) => (v.length === 3 ? point(v[0], v[1], v[2]) : point(v[0], v[1]));
export const dotAt = (v, color, size = 4.5, shape = 'circle') => P(v).marker(shape).color(color).size(size);
export const style = (d, { color, stroke = 1, dash, opacity } = {}) => {
  let s = d;
  if (color !== undefined) s = s.color(color);
  if (stroke !== undefined) s = s.stroke(stroke);
  if (dash !== undefined) s = s.dash(dash);
  if (opacity !== undefined) s = s.opacity(opacity);
  return s;
};
export const labelAt = (at, text, { color, font = 11, bold = false, anchor, box, dx, dy } = {}) => {
  let t = annotate.text(P(at)).label(text).font(font);
  if (color !== undefined) t = t.color(color);
  if (bold) t = t.bold();
  if (anchor) t = t.anchor(anchor);
  if (box) t = t.box(box);
  if (dx !== undefined || dy !== undefined) t = t.offset(dx || 0, dy || 0);
  return t;
};
export const segAt = (a, b, o) => style(segment(P(a), P(b)), o);
export const vlineAt = (x, o) => style(line.vertical(x), o);
export const hlineAt = (y, o) => style(line.horizontal(y), o);
export const curveOf = (f, dom, { n, ...o } = {}) => {
  let c = curve.fn(f).on(dom);
  if (n) c = c.n(n);
  return style(c, { stroke: 2, ...o });
};
export const legendAt = (at, text, color, { font = 10.5, anchor = 'start', bold = true } = {}) =>
  labelAt(at, text, { color, font, bold, anchor });

// 플러그인 빌더 (부분합 궤적·항 stem)
export const polyline = (...pts) => plugins.polyline(...pts);
export const stem = (...pts) => plugins.stem(...pts);

// ── 급수 헬퍼 — 순수 JS, IR 이전 단계의 데이터 가공 ──────────────
/** a(n) 을 n=n0..n1 로 평가해 [ [n, aₙ], … ] 반환 */
export const termsOf = (a, n0 = 1, n1 = 10) =>
  Array.from({ length: n1 - n0 + 1 }, (_, i) => { const n = n0 + i; return [n, a(n)]; });
/** a(n) 의 부분합 [ [n, Sₙ], … ] */
export const partialSums = (a, n0 = 1, n1 = 10) => {
  let s = 0;
  return Array.from({ length: n1 - n0 + 1 }, (_, i) => { const n = n0 + i; s += a(n); return [n, s]; });
};
/** 로그 오차 등 — 값을 [lo, hi] 로 클램프 (플롯 밖으로 나가는 꼬리 방지) */
export const clamp = (v, lo, hi) => Math.max(lo, Math.min(hi, v));
/**
 * 곡선값을 [lo, hi] 로 잘라 그린다.
 * 코어에는 matplotlib 의 axes 클립이 없어서, |x|>R 에서 폭주하는 부분합을 그대로 두면
 * 좌표가 수만 px 로 나가 SVG 백엔드(resvg)가 죽는다(18B arctan 패널에서 재현).
 * 축 범위로 잘라 "차트 밖으로 벗어남"을 가장자리 평탄선으로 표현한다.
 */
export const clampFn = (f, lo, hi) => (x) => clamp(f(x), lo, hi);
/** n! — 테일러 계수용 */
export const fact = (n) => { let r = 1; for (let i = 2; i <= n; i++) r *= i; return r; };
/** 멱급수 부분합 Σ_{n=n0}^{N} a(n, x) — 테일러/거듭제곱 급수의 S_N(x) */
export const seriesFn = (a, n0, N) => (x) => {
  let s = 0;
  for (let n = n0; n <= N; n++) s += a(n, x);
  return s;
};
/** log10|f(x) − g(x)| — 0(로그 발산)은 floor 로 클램프 */
export const log10Err = (f, g, floor = 1e-16) => (x) => Math.log10(Math.max(Math.abs(f(x) - g(x)), floor));
/** 마커 한 점 — 열린(빈) 마커로 수렴하지 않는 끝점을 표시할 때 쓴다 */
export const markerAt = (v, color, { size = 4.5, shape = 'circle', open = false } = {}) =>
  P(v).marker(shape, { open }).color(color).size(size);

// ── 패널 프리셋 ────────────────────────────────────────────────
export const s2p = (xr, yr, size = [520, 420], o = {}) => plot2d(xr, yr, { size, ...o });
export const OFF = { axes: false, grid: false };
export const AX = (x = 'x', y = 'y') => ({ x: { label: x }, y: { label: y } });
/** x축만 보이는 설정 — 수직선 도식 패널에서 y 눈금/라벨을 끈다 */
export const AXx = (x = 'x') => ({ x: { label: x }, y: { label: false, ticks: false } });

// ── 패널 조합 · 자주 쓰는 캔버스 ─────────────────────────────────
/** 2D 패널 기본 크기 — 한 그림 안에서 모든 패널을 같은 크기로 맞춘다 */
export const PANEL = [520, 400];
/** 1×2 나란히 배치 (세션 그림의 90%가 이 모양) */
export const pair = (left, right, title, o = {}) =>
  subplots([left, right], { cols: 2, tight: true, title, ...o });
/** 세로로 쌓기 (패널 높이를 서로 다르게 줄 수 있다) */
export const stack = (panels, title, o = {}) => subplots(panels, { cols: 1, tight: true, title, ...o });
/** 1×1 단독 배치 — 3D 처럼 이미 넓은 패널 하나만 쓸 때 */
export const single = (panel, title, o = {}) => stack([panel], title, o);

// ── 영역 띠 — 부호 차트·구간 강조에 쓴다 (region.bar 의 얇은 별칭) ──
export const barAt = (x0, x1, y0, y1, color, opacity = 0.1) =>
  region.bar(x0, x1, y0, y1).fill(color).opacity(opacity);
