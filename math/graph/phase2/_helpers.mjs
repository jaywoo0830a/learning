// math/graph/phase2/_helpers.mjs — phase2 스케치 공용 헬퍼 (14D·14D1·18A·18B·18C …)
//
// `_` 로 시작하므로 logos 렌더러가 스케치로 취급하지 않고 건너뛴다(문서 규칙).
// 코어 위의 얇은 별칭 + 플러그인(_math-extras: polyline·stem) 설치만 담당한다.
// 여기 있는 것은 전부 **얇은 별칭**이다 — 새 그림 문법을 발명하지 않고
// 코어 빌더(`curve.fn`·`region.*`·`point/segment/annotate`)를 짧게 부르는 것뿐.
//
// ── 코어에 이미 있는 것 (재발명 금지 · KIT.md §3.6 / §7 FAQ) ──────────────
//   · 스타일 일괄 지정  `Drawable.set({color,stroke,dash,opacity})`  → 이 파일의 `style()`
//   · 라벨 배경 박스    `annotate.text(...).box({facecolor,alpha})`  → `labelAt(..., {box: BOX})`
//   · px 오프셋         `annotate.text(...).offset(dx,dy)`           → `labelAt(..., {dx,dy})`
//   · 3D 투영 라벨/선   `annotate.text([x,y,z])` · `curve3.through` · `kit.poly3`
//   · 화살표·치수·눈금  `annotate.arrow(A,B)` · `annotate.dimension(A,B).offset(n)` · `annotate.tick`
//   · 색 팔레트         `kit.palette.tab10` (아래 BLUE… 를 여기서 파생)
//   · 라벨 자동 배치    `scene().layout()` → SceneIR.layout (기본 꺼짐) · CLI `--layout`
//                       — 고정 버전에서는 눈금 라벨을 피하지 않는다(업스트림 PR 에서 수정 제안)
//   · 클립              `Drawable.clip(region)` — 단, backend/svg.js 는 `region.between/inside`
//                       (또는 cliprect 스트립)에만 clipPath 를 방출한다. `region.bar` 클립은
//                       조용히 무시되므로 꼬리 평탄화는 아래 `clampFn` 이 계속 담당한다.
//
// ── 함정(고정 버전 기준 · 업스트림 PR 에서 일부 수정 제안) ────────────────
//   · `kit.seg(A,B)` — 2D 분기가 `line.through` 라서 **무한 직선**을 그린다(KIT.md §3.6 에
//     문서화된 의도된 동작 — 선분은 `segment`). 게다가 raw 좌표 배열을 주면 컴파일 시
//     `Line.pointDir` 에서 죽는다(shapes/line.js:19). 그래서 이 파일은 `segment(P,P)` 를 쓴다.
//     (두 번째 문제는 수정 PR: fix/mathbook-workflow-feedback — 배열 인자 허용)
import {
  point, line, segment, curve, region, annotate, kit, use, plugins,
} from '@jaywoo0830a/logos';
import mathExtras from '../plugins/_math-extras.js';

// 플러그인 설치(코어 수정 0) — plugins.polyline / plugins.stem 이 살아난다
use(mathExtras);

export const { plot2d, plot3d, subplots } = kit;

// ── 색 — 코어 `kit.palette.tab10`(kit.js)에서 파생 (hex 를 여기서 다시 적지 않는다) ──
//   tab10 순서: blue · orange · green · red · purple · brown · pink · gray · olive · cyan
const TAB = kit.palette.tab10;
export const BLUE = TAB[0], ORANGE = TAB[1], GREEN = TAB[2], RED = TAB[3];
export const PURPLE = TAB[4], BROWN = TAB[5], PINK = TAB[6], GRAY = TAB[7];
export const LIGHT = '#bbbbbb', ASYMP = '#cccccc', GOLD = '#b8860b';
export const BOX = { facecolor: 'white', alpha: 0.85 };

// ── 미세 헬퍼 (전부 라이브러리 API 위의 얇은 별칭) ──────────────
/** 점 좌표 — [x, y] 는 2D, [x, y, z] 는 3D(3D 패널에서 코어가 투영). 라벨·선·마커가 공유한다. */
export const P = (v) => (v.length === 3 ? point(v[0], v[1], v[2]) : point(v[0], v[1]));
/** 마커 한 점 — 열린(빈) 마커로 수렴하지 않는 끝점을 표시할 때 쓴다 (코어 `point.marker`) */
export const markerAt = (v, color, { size = 4.5, shape = 'circle', open = false } = {}) =>
  P(v).marker(shape, { open }).color(color).size(size);
/** 색·굵기·점선·투명도를 한 번에 — 코어 `Drawable.set()` (core/drawable.js) 위의 얇은 별칭.
 *  `set` 은 undefined 도 덮어쓰므로 **정의된 키만** 넘긴다(코어 기본색 보존). */
export const style = (d, { color, stroke = 1, dash, opacity } = {}) =>
  d.set(Object.fromEntries(Object.entries({ color, stroke, dash, opacity }).filter(([, v]) => v !== undefined)));
export const labelAt = (at, text, { color, font = 11, bold = false, anchor, box, dx, dy } = {}) => {
  let t = annotate.text(P(at)).label(text).font(font);
  if (color !== undefined) t = t.color(color);
  if (bold) t = t.bold();
  if (anchor) t = t.anchor(anchor);
  if (box) t = t.box(box);
  if (dx !== undefined || dy !== undefined) t = t.offset(dx || 0, dy || 0);
  return t;
};
/** 선분 — `kit.seg` 는 2D 에서 무한 직선이라 쓸 수 없다(위 함정 참고). */
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
 * 코어 `.clip(region)` 은 `region.between/inside` 에만 clipPath 를 방출하고 `region.bar` 는
 * 조용히 무시되므로(backend/svg.js:78 regionRect 참고) |x|>R 에서 폭주하는 부분합을 그대로 두면
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
/** 채워진 마커 한 점 — `markerAt` 의 축약(마커 모양 지정 불가 시절 호출부 호환) */
export const dotAt = (v, color, size = 4.5, shape = 'circle') => markerAt(v, color, { size, shape });

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
