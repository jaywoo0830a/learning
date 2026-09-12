// math/graph/phase2/18B/_helper.mjs — 18B(멱급수) **전용**. 다른 폴더와 공유하지 않는다.
// 코어(@jaywoo0830a/logos 0.4.1)에 없는 **순수 JS 수학**만. 그리기는 스케치에서 코어 API 로 직접.

/** 멱급수 부분합 Σ_{n=n0}^{N} a(n, x) — S_N(x) */
export const seriesFn = (a, n0, N) => (x) => {
  let s = 0;
  for (let n = n0; n <= N; n++) s += a(n, x);
  return s;
};

/** 곡선값을 [lo, hi] 로 잘라 그린다 — |x|→1 에서 폭주하는 부분합을 차트 안쪽 평탄선으로.
 *  코어 `.clip(region)` 이 아직 무효(clip-path 참조만 방출)라서 이 JS 클램프를 쓴다. */
export const clampFn = (f, lo, hi) => (x) => Math.max(lo, Math.min(hi, f(x)));
