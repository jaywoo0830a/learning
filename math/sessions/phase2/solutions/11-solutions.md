# 11 풀이집 — 삼각함수

---

## 연습 1

> $\sin\theta = -\frac{\sqrt{3}}{2}$, $\theta$는 4사분면. $\cos\theta$, $\tan\theta$, $\sec\theta$, $\csc\theta$, $\cot\theta$ 구하기.

① $\theta$가 4사분면 → $\cos\theta > 0$, $\sin\theta < 0$.

② $\sin^2\theta + \cos^2\theta = 1$:
$\frac{3}{4} + \cos^2\theta = 1$ → $\cos^2\theta = \frac{1}{4}$ → $\cos\theta = \frac{1}{2}$ (4사분면에서 양수).

③ $\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{-\sqrt{3}/2}{1/2} = -\sqrt{3}$.

④ $\sec\theta = \frac{1}{\cos\theta} = 2$.

⑤ $\csc\theta = \frac{1}{\sin\theta} = \frac{1}{-\sqrt{3}/2} = -\frac{2}{\sqrt{3}} = -\frac{2\sqrt{3}}{3}$.

⑥ $\cot\theta = \frac{1}{\tan\theta} = -\frac{1}{\sqrt{3}} = -\frac{\sqrt{3}}{3}$.

→ **$\cos\theta=\frac{1}{2}$, $\tan\theta=-\sqrt{3}$, $\sec\theta=2$, $\csc\theta=-\frac{2\sqrt{3}}{3}$, $\cot\theta=-\frac{\sqrt{3}}{3}$.**

---

## 연습 2

> $y = 2\sin(3x + \pi) - 1$의 진폭, 주기, 위상, 수직 이동.

$a = 2$, $b = 3$, $c = \pi$, $d = -1$.

진폭: $|a| = 2$.
주기: $\frac{2\pi}{|b|} = \frac{2\pi}{3}$.
위상 이동: $3x + \pi = 0$ → $x = -\frac{\pi}{3}$ (왼쪽으로 $\frac{\pi}{3}$).
수직 이동: $-1$ (아래로 1).

그래프: $y = \sin x$에서 시작.
세로로 2배, 가로로 $\frac{1}{3}$배(주기 $\frac{2\pi}{3}$), 왼쪽으로 $\frac{\pi}{3}$, 아래로 1.
치역: $[-3, 1]$.

---

## 연습 3

> $\cos 2x = \sin x$, $[0, 2\pi]$.

① $\cos 2x = 1 - 2\sin^2 x$: $1 - 2\sin^2 x = \sin x$.
② $2\sin^2 x + \sin x - 1 = 0$.
③ $t = \sin x$: $2t^2 + t - 1 = 0$ → $(2t-1)(t+1) = 0$.
④ $t = \frac{1}{2}$: $\sin x = \frac{1}{2}$ → $x = \frac{\pi}{6}, \frac{5\pi}{6}$.
⑤ $t = -1$: $\sin x = -1$ → $x = \frac{3\pi}{2}$.

→ **$x = \frac{\pi}{6}, \frac{5\pi}{6}, \frac{3\pi}{2}$.**

---

## 연습 4: 구성형

> $5\sin x + 12\cos x$를 $R\sin(x+\phi)$ 꼴로. 최댓값과 그때의 $x$.

① $R = \sqrt{5^2+12^2} = \sqrt{169} = 13$.
② $\cos\phi = \frac{5}{13}$, $\sin\phi = \frac{12}{13}$. $\phi = \arcsin\frac{12}{13} \approx 67.38^\circ$.
③ $5\sin x + 12\cos x = 13\sin(x + \phi)$.

④ 최댓값: $13$. $\sin(x+\phi)=1$일 때 → $x+\phi = \frac{\pi}{2} + 2n\pi$.
$x = \frac{\pi}{2} - \phi + 2n\pi \approx 22.62^\circ + 360^\circ n$.

⑤ 다른 예: 전기공학에서 교류 신호 합성. $V_1\sin(\omega t) + V_2\cos(\omega t)$를 하나의 사인파로.

---

## 연습 5

> $a=7$, $b=10$, $c=13$인 삼각형의 세 각과 넓이.

코사인법칙으로 각.
$\cos A = \frac{10^2+13^2-7^2}{2\cdot10\cdot13} = \frac{100+169-49}{260} = \frac{220}{260} = \frac{11}{13}$. $A \approx 32.2^\circ$.
$\cos B = \frac{7^2+13^2-10^2}{2\cdot7\cdot13} = \frac{49+169-100}{182} = \frac{118}{182} = \frac{59}{91}$. $B \approx 49.5^\circ$.
$C = 180^\circ - 32.2^\circ - 49.5^\circ = 98.3^\circ$.

넓이(헤론): $s = \frac{7+10+13}{2} = 15$. $\sqrt{15\cdot8\cdot5\cdot2} = \sqrt{1200} = 20\sqrt{3} \approx 34.64$.

---

## 연습 6: 실전

> $\sec x + \tan x = 2$. $\sec x - \tan x$와 $\sin x$ 구하기.

① $(\sec x + \tan x)(\sec x - \tan x)$ 펼치기:
$= \sec^2 x - \tan^2 x = (1+\tan^2 x) - \tan^2 x = 1$.

② $\sec x + \tan x = 2$이므로 $2(\sec x - \tan x) = 1$ → $\sec x - \tan x = \frac{1}{2}$.

③ 두 식 연립:
더하기: $2\sec x = 2 + \frac{1}{2} = \frac{5}{2}$ → $\sec x = \frac{5}{4}$.
빼기: $2\tan x = 2 - \frac{1}{2} = \frac{3}{2}$ → $\tan x = \frac{3}{4}$.

④ $\sec x = \frac{1}{\cos x}$ → $\cos x = \frac{4}{5}$.
$\tan x = \frac{\sin x}{\cos x}$ → $\sin x = \tan x \cdot \cos x = \frac{3}{4} \cdot \frac{4}{5} = \frac{3}{5}$.

→ **$\sec x - \tan x = \frac{1}{2}$, $\sin x = \frac{3}{5}$.**

---

[목차로 돌아가기](../11-trigonometry.md)
