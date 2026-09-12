// math/graph/phase2/18A/_helper.mjs — 18A(수렴판정) **전용**. 다른 폴더와 공유하지 않는다.
// 코어(@jaywoo0830a/logos 0.4.1)에 없는 **순수 JS 수학**만. 그리기는 스케치에서 코어 API 로 직접.

/** a(n) 을 n=n0..n1 로 평가 → [ [n, aₙ], … ] (stem/polyline 에 그대로 넘긴다) */
export const termsOf = (a, n0 = 1, n1 = 10) =>
  Array.from({ length: n1 - n0 + 1 }, (_, i) => { const n = n0 + i; return [n, a(n)]; });

/** a(n) 의 부분합 → [ [n, Sₙ], … ] */
export const partialSums = (a, n0 = 1, n1 = 10) => {
  let s = 0;
  return Array.from({ length: n1 - n0 + 1 }, (_, i) => { const n = n0 + i; s += a(n); return [n, s]; });
};
