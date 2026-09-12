// math/graph/phase2/_helpers.mjs — phase2 스케치 공용 헬퍼 (11C·14D·14D1·18A·18B·18C)
//
// `_` 로 시작하므로 logos 렌더러가 스케치로 취급하지 않고 건너뛴다(문서 규칙).
// 코어 위의 얇은 별칭 + 플러그인(_math-extras: polyline·stem) 설치만 담당한다.
// 여기 있는 것은 전부 **얇은 별칭**이다 — 새 그림 문법을 발명하지 않고
// 코어 빌더(`curve.fn`·`region.*`·`point/segment/annotate`)를 짧게 부르는 것뿐.
//
// ── 기준 버전: @jaywoo0830a/logos 0.4.1 (math/graph/package.json → `#v0.4.1`) ──────────
//   0.2.0~0.4.1 에 실사용 피드백이 반영되어, 예전의 우회는 더 이상 필요 없다.
//     · 좌표 정규화    `toPoint(v)` — 배열·객체 `{x,y}`·Point 를 모두 받는다 (shapes/point.js)
//     · 불변 업데이트  `Drawable.with({…})`(=`set`) — 중첩 설정은 깊은 복사로 공유 오염 방지
//     · 눈금 정밀도    `axes({ y: { decimals: 4 } })` — 좁은 범위에서도 라벨이 뭉개지지 않는다
//     · 라벨 자동배치  `scene().layout()` 이 눈금·축 라벨을 장애물로 취급 · CLI `--layout`
//     · 편의           `kit.seg` 좌표 배열 허용 · `palette.tab`(이름 있는 tab10) ·
//                      태그드 템플릿 `xy` · `view` · `range`
//     · 래스터 안전    화면 밖 도형이 있어도 resvg panic 으로 프로세스가 죽지 않는다(0.4.1)
//   색은 코어 팔레트에서 파생한다 — hex 를 스케치마다 다시 적지 않는다(아래 §색).
//
// ── 함정 (0.4.1 기준으로 계속 확인된 것) ──────────────────────────────────────────────
//   · `kit.seg(A,B)` — 좌표 배열을 이제 받지만 **2D 분기는 `line.through` 라 무한 직선**이다
//     (KIT.md §3.6 에 문서화된 의도된 동작). 선분이 필요하면 `segment` → 이 파일은 `segAt`.
//   · `Drawable.clip(region)` — 산출 SVG 가 `clip-path="url(#logosClipN)"` 를 **참조만 하고
//     `<clipPath>` 정의를 함께 내보내지 않아** 아무것도 잘리지 않는다.
//     재현: `curve.fn(f).on(d).clip(region.between(a,b))` → SVG 에 `clip-path="url(#…)"` 1회,
//     `<clipPath` 0회(backend/svg.js 의 clip 정의 방출 경로 vs 사용부). 그래서 곡선 꼬리
//     평탄화는 계속 아래 `clampFn` 이 담당한다(0.4.1 의 래스터 안전 패스 덕분에 크래시는 없다).
import {
  point, line, segment, curve, region, annotate, kit, use, plugins, toPoint, circle, polygon,
} from '@jaywoo0830a/logos';
import mathExtras from '../plugins/_math-extras.js';

// 플러그인 설치(코어 수정 0) — plugins.polyline / plugins.stem 이 살아난다
use(mathExtras);

export const { plot2d, plot3d, subplots } = kit;
/** 코어 이름 팔레트 — `palette.skyblue` 처럼 쓴다(clean-code 예제와 같은 관례). */
export const palette = kit.palette;

// ── 색 — 코어 `kit.palette.tab`(이름 있는 tab10)에서 파생 (hex 를 여기서 다시 적지 않는다) ──
//   tab: blue · orange · green · red · purple · brown · pink · gray · olive · cyan
const T = kit.palette.tab;
export const BLUE = T.blue, ORANGE = T.orange, GREEN = T.green, RED = T.red;
export const PURPLE = T.purple, BROWN = T.brown, PINK = T.pink, GRAY = T.gray;
export const OLIVE = T.olive, CYAN = T.cyan;
// 위 10색 밖의 '지면(furniture)' 톤만 hex 로 둔다 — 데이터 색이 아니라 축·보조선·강조용.
export const LIGHT = '#bbbbbb', ASYMP = '#cccccc', FAINT = '#dddddd', GOLD = '#b8860b';
export const NAVY = kit.palette.navy;   // 기준 도형(단위원·쌍곡선 등) 강조용 짙은 색
export const BOX = { facecolor: 'white', alpha: 0.85 };

// ── 미세 헬퍼 (전부 라이브러리 API 위의 얇은 별칭) ──────────────
/** 점 좌표 — 코어 `toPoint` 의 짧은 이름. `[x,y]`/`[x,y,z]` · `{x,y}` · Point 를 모두 받는다.
 *  라벨·선분·마커가 같은 규칙을 공유하므로, 스케치에 로컬 `P` 를 다시 만들지 않는다. */
export const P = toPoint;
/** 마커 한 점 — 열린(빈) 마커로 수렴하지 않는 끝점을 표시할 때 쓴다 (코어 `point.marker`) */
export const markerAt = (v, color, { size = 4.5, shape = 'circle', open = false } = {}) =>
  P(v).marker(shape, { open }).color(color).size(size);
/** 색·굵기·점선·투명도를 한 번에 — 코어 `Drawable.with()`(=`set()`, core/drawable.js) 위의 얇은 별칭.
 *  `with` 는 undefined 도 덮어쓰므로 **정의된 키만** 넘긴다(코어 기본색 보존). */
export const style = (d, { color, stroke = 1, dash, opacity } = {}) =>
  d.with(Object.fromEntries(Object.entries({ color, stroke, dash, opacity }).filter(([, v]) => v !== undefined)));
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
/** 중심 c · 반지름 r 인 원 — 코어 `circle.center().radius()` 위의 얇은 별칭 */
export const circleAt = (c, r, o) => style(circle.center(P(c)).radius(r), o);
/** 채운 부채꼴/다각형 — `[(x,y), …]` 목록을 코어 `polygon` 으로. 외곽선은 `{color, stroke}` 선택 */
export const polyAt = (pts, fill, opacity = 0.15, o = {}) => {
  let g = polygon(...pts.map(P)).fill(fill).opacity(opacity);
  if (o.color !== undefined) g = g.color(o.color).stroke(o.stroke ?? 1);
  return g;
};
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
 * 곡선값을 [lo, hi] 로 잘라 그린다 — "차트 밖으로 벗어남"을 가장자리 평탄선으로 표현한다.
 * 코어 `.clip(region)` 이 무효이기 때문이다(헤더 §함정 — SVG 가 `clip-path` 참조만 내보낸다).
 * 0.4.1 의 래스터 안전 패스 덕분에 폭주 좌표가 프로세스를 죽이지는 않지만, 잘라 그리지 않으면
 * 부분합·arctan 꼬리가 화면을 가로지른다(18B·18C 패널에서 확인).
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
/** 채워진 마커 한 점 — 위치 인자 축약(`dotAt(v, color, size)`). 새로 쓰는 자리는 `markerAt` 권장. */
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
