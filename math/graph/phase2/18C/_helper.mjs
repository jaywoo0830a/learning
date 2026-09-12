// math/graph/phase2/18C/_helper.mjs — 18C(테일러 급수) **전용**. 다른 폴더와 공유하지 않는다.
//
// 여기에는 **코어(@jaywoo0830a/logos 0.4.1)에 없는 것 — 순수 JS 수학**만 둔다.
// 그림 그리기(패널·곡선·라벨·색)는 전부 코어 API 를 이 폴더의 스케치에서 직접 쓴다.
// (예전에는 phase2 전 스케치가 `../_helpers.mjs` 한 파일을 공유해 관리가 어려웠다.)

/** n! — 테일러 계수용 */
export const fact = (n) => {
  let r = 1;
  for (let i = 2; i <= n; i++) r *= i;
  return r;
};

/** 멱급수 부분합 Σ_{n=n0}^{N} a(n, x) — 테일러 다항식 S_N(x) */
export const seriesFn = (a, n0, N) => (x) => {
  let s = 0;
  for (let n = n0; n <= N; n++) s += a(n, x);
  return s;
};

/** log10|f(x) − g(x)| — 0(로그 발산)은 floor 로 클램프. 코어에 로그축이 없어 선형축에 그린다. */
export const log10Err = (f, g, floor = 1e-16) => (x) => Math.log10(Math.max(Math.abs(f(x) - g(x)), floor));

/** 곡선값을 [lo, hi] 로 잘라 그린다 — "차트 밖" 꼬리를 가장자리 평탄선으로.
 *  코어 `.clip(region)` 이 아직 무효(clip-path 참조만 방출)라서 이 JS 클램프를 쓴다. */
export const clampFn = (f, lo, hi) => (x) => Math.max(lo, Math.min(hi, f(x)));
