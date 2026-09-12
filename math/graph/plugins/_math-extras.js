// math/graph/plugins/_math-extras.js — math/graph 전용 플러그인 (코어 수정 0)
//
// 왜 필요한가
//   시리즈/급수 그림(18A·18B·18C)은 매번 두 가지가 반복되는데 코어에 1급 빌더가 없다.
//     · 부분합 궤적        — 여러 점을 잇는 **연속 폴리라인** (코어엔 선분만 있다)
//     · 항(term) 표시       — 0 에서 aₙ 까지 **수직 stem** + 끝점 마커 (막대 region.bar 뿐)
//   코어 파일을 고치는 대신 `use(mathExtras)` 한 줄로 두 빌더를 붙인다.
//
// 어떻게 붙는가 (PLUGIN.md ③ 새 빌더)
//   `api.define('polyline', …)` · `api.define('stem', …)` →
//   `plugins.polyline(…)` / `plugins.stem(…)` 로 즉시 사용. 두 클래스 다 Drawable 을
//   상속하므로 `.color() .stroke() .dash() .opacity()` 체이닝이 코어와 동일하게 동작한다.
import { Drawable, node } from '@jaywoo0830a/logos';

/** 코어 도형과 같은 관례의 스타일 키 추출 */
function styleOf(c) {
  const s = {};
  for (const k of ['color', 'stroke', 'fill', 'dash', 'opacity', 'z']) if (c[k] !== undefined) s[k] = c[k];
  return s;
}
/** 인자를 [ [x,y], … ] 로 정규화 — `f([p1, p2])` 도 `f(p1, p2)` 도 허용 */
function toPairs(args) {
  const list = (args.length === 1 && Array.isArray(args[0])) ? args[0] : args;
  return list.map((p) => (Array.isArray(p) ? p : p.coords));
}

// ── polyline — 점을 잇는 연속 선 (부분합 궤적 등) ──────────────
export class Polyline extends Drawable {
  /** @param {Array} pts 점 목록(Point 또는 [x,y]) */
  constructor(pts, conf = {}) { super('polyline', { pts, ...conf }); }
  toIR() {
    const c = this._conf;
    const ops = c.pts.map((p, i) => ({ op: i === 0 ? 'M' : 'L', x: p[0], y: p[1] }));
    return [node('path', {
      ops, color: c.color, stroke: c.stroke, dash: c.dash, opacity: c.opacity,
      transforms: c.transforms, clip: c.clip, style: styleOf(c),
    })];
  }
}
export function polyline(...args) { return new Polyline(toPairs(args)); }

// ── stem — 0(y=baseline)에서 aₙ 까지 수직선 + 끝점 마커 ────────
export class Stem extends Drawable {
  /** @param {Array} pts 점 목록(Point 또는 [x,y]); y=값, x=인덱스 */
  constructor(pts, conf = {}) { super('stem', { pts, ...conf }); }
  size(n) { return this.set({ size: n }); }     // 끝점 마커 크기(px)
  marker(m) { return this.set({ marker: m }); } // 끝점 마커 모양
  baseline(y) { return this.set({ baseline: y }); }
  toIR() {
    const c = this._conf;
    const base = c.baseline ?? 0;
    const out = [];
    for (const [x, y] of c.pts) {
      out.push(node('path', {
        ops: [{ op: 'M', x, y: base }, { op: 'L', x, y }],
        color: c.color, stroke: c.stroke ?? 1.3, dash: c.dash, opacity: c.opacity,
        transforms: c.transforms, style: styleOf(c),
      }));
      out.push(node('point', {
        x, y, marker: c.marker || 'dot', size: c.size ?? 3.2, color: c.color, style: styleOf(c),
      }));
    }
    return out;
  }
}
export function stem(...args) { return new Stem(toPairs(args)); }

// ── 플러그인 본체 ─────────────────────────────────────────────
const mathExtras = {
  name: 'math-extras',
  version: '1.0.0',
  install(api) {
    api.define('polyline', polyline, { ctor: Polyline, aliases: ['line-through-points'] });
    api.define('stem', stem, { ctor: Stem, aliases: ['stems'] });
  },
};

export default mathExtras;
