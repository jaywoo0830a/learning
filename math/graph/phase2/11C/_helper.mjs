// math/graph/phase2/11C/_helper.mjs — 11C(쌍곡선 함수) **전용**. 다른 폴더와 공유하지 않는다.
// 코어(@jaywoo0830a/logos 0.4.1)에 없는 **순수 JS 수학(표본 생성)**만 여기 둔다.

/** 각도를 라디안으로 */
export const rad = (deg) => (deg * Math.PI) / 180;

/** 호의 표본 점들 ← np.linspace(θ₁, θ₂) 뒤 (cos, sin) */
export const arcSamples = (r, d1, d2, n = 60) =>
  Array.from({ length: n + 1 }, (_, i) => [
    r * Math.cos(d1 + ((d2 - d1) * i) / n),
    r * Math.sin(d1 + ((d2 - d1) * i) / n),
  ]);

/** 쌍곡선 오른쪽 가지 표본 (cosh s, sinh s), s∈[0,t] ← (cosh,sinh) 파라미터화 */
export const hyperSamples = (t, n = 60) =>
  Array.from({ length: n + 1 }, (_, i) => { const s = (t * i) / n; return [Math.cosh(s), Math.sinh(s)]; });
