# 13 풀이집 — 극한

---

## 연습 1

> $\lim_{x\to2} \frac{x^3-8}{x-2}$.

① $x=2$ → $\frac{8-8}{0} = \frac{0}{0}$.
② 세제곱 공식: $x^3-8 = (x-2)(x^2+2x+4)$.
③ 약분: $\frac{(x-2)(x^2+2x+4)}{x-2} = x^2+2x+4$ ($x\neq2$).
④ $x=2$ 대입: $4+4+4 = 12$.

→ **12.**

---

## 연습 2

> $\lim_{x\to0} \frac{\sqrt{x+9}-3}{x}$.

① $x=0$ → $\frac{3-3}{0} = \frac{0}{0}$.
② 켤레 $\sqrt{x+9}+3$ 곱하기:
$\frac{(\sqrt{x+9}-3)(\sqrt{x+9}+3)}{x(\sqrt{x+9}+3)}$.
③ 분자 = $(x+9)-9 = x$.
④ 약분: $\frac{x}{x(\sqrt{x+9}+3)} = \frac{1}{\sqrt{x+9}+3}$.
⑤ $x=0$ 대입: $\frac{1}{\sqrt{9}+3} = \frac{1}{3+3} = \frac{1}{6}$.

→ **$\frac{1}{6}$.**

---

## 연습 3

> $\lim_{x\to0} \frac{\sin 7x}{\tan 3x}$.

① $\tan 3x = \frac{\sin 3x}{\cos 3x}$.
② $\frac{\sin 7x}{\sin 3x} \cdot \cos 3x$.
③ $\frac{\sin 7x}{\sin 3x} = \frac{\sin 7x}{7x} \cdot \frac{3x}{\sin 3x} \cdot \frac{7}{3}$.
④ $\frac{\sin 7x}{7x}\to1$, $\frac{3x}{\sin 3x}\to1$, $\cos 3x\to1$.
⑤ → $1 \cdot 1 \cdot \frac{7}{3} \cdot 1 = \frac{7}{3}$.

→ **$\frac{7}{3}$.**

---

## 연습 4: 구성형

> 극한값이 5가 되는 $\frac{0}{0}$ 꼴 유리함수 3개.

**공식**: $\lim_{x\to a}\frac{(x-a)\cdot g(x)}{(x-a)\cdot h(x)} = \frac{g(a)}{h(a)}$ (단 $h(a)\neq0$).

① $\lim_{x\to2}\frac{x^2+x-6}{x-2} = \lim_{x\to2}\frac{(x-2)(x+3)}{x-2} = 5$.
② $\lim_{x\to3}\frac{2x^2-5x-3}{x-3} = \lim_{x\to3}\frac{(x-3)(2x+1)}{x-3} = 7$? 아니, 5가 되게:
$\lim_{x\to1}\frac{x^2+4x-5}{x-1} = \lim_{x\to1}\frac{(x-1)(x+5)}{x-1} = 6$? 다시:
$\lim_{x\to1}\frac{x^2+3x-4}{x-1} = \frac{(x-1)(x+4)}{x-1} \to 5$ ✓.
③ $\lim_{x\to0}\frac{5x}{x} = 5$ (가장 간단).
④ $\lim_{x\to-1}\frac{x^3+6x^2+10x+5}{x+1}$ — 분자에 $x+1$ 인수, 몫 $x^2+5x+5$ → $1-5+5=1$? 다시.

간단히: $\frac{5x}{x}$, $\frac{x^2+3x-4}{x-1}$, $\frac{5x^2}{x^2}$ (후자는 $\frac{0}{0}$이 아님 — $\frac{5x^2}{x^2}=5$으로 상수).

---

## 연습 5

> $\lim_{x\to\infty} \frac{\sqrt{4x^2+3x}}{2x-1}$.

① $x\to\infty$ → $\frac{\infty}{\infty}$.
② 분자: $\sqrt{4x^2+3x} = \sqrt{x^2(4+\frac{3}{x})} = |x|\sqrt{4+\frac{3}{x}}$.
   $x>0$이므로 $|x| = x$. → $x\sqrt{4+\frac{3}{x}}$.
③ $\frac{x\sqrt{4+3/x}}{x(2-1/x)} = \frac{\sqrt{4+3/x}}{2-1/x}$.
④ $x\to\infty$: $\frac{3}{x}\to0$, $\frac{1}{x}\to0$.
⑤ → $\frac{\sqrt{4+0}}{2-0} = \frac{2}{2} = 1$.

→ **1.**

---

## 연습 6: 실전

> $\lim_{x\to0} \frac{e^{3x}-1}{\ln(1+2x)}$.

① $x=0$ → $\frac{1-1}{\ln1} = \frac{0}{0}$.

② $e^{3x}-1 = 3x \cdot \frac{e^{3x}-1}{3x}$.
   $\frac{e^{3x}-1}{3x} \to 1$ (표준극한).

③ $\ln(1+2x) = 2x \cdot \frac{\ln(1+2x)}{2x}$.
   $\frac{\ln(1+2x)}{2x} \to 1$ (표준극한).

④ $\frac{e^{3x}-1}{\ln(1+2x)} = \frac{3x}{2x} \cdot \frac{(e^{3x}-1)/3x}{\ln(1+2x)/2x}$.
   $\to \frac{3}{2} \cdot \frac{1}{1} = \frac{3}{2}$.

→ **$\frac{3}{2}$.**

---

## 연습 7

> $\lim_{x\to1}\frac{x^2+x-2}{x-1}$.

① $x=1$ → $\frac{1+1-2}{0}=\frac{0}{0}$.
② $x^2+x-2=(x-1)(x+2)$. 약분 → $x+2$.
③ $x=1$ → $3$.

→ **3.**

---

## 연습 8

> $\lim_{x\to0}\frac{\sqrt{x+1}-1}{x}$.

① $x=0$ → $\frac{0}{0}$. 켤레 $\sqrt{x+1}+1$ 곱함.
② $\frac{x}{x(\sqrt{x+1}+1)}=\frac{1}{\sqrt{x+1}+1}$.
③ $x=0$ → $\frac{1}{2}$.

→ **$\frac{1}{2}$.**

---

## 연습 9

> $\lim_{x\to0}\frac{\sin4x}{\tan2x}$.

① $\tan2x=\frac{\sin2x}{\cos2x}$. → $\frac{\sin4x}{\sin2x}\cdot\cos2x$.
② $\frac{\sin4x}{\sin2x}=\frac{\sin4x}{4x}\cdot\frac{2x}{\sin2x}\cdot2 \to 1\cdot1\cdot2=2$.
③ $\cos2x\to1$. → $2\cdot1=2$.

→ **2.**

---

## 연습 10

> $\lim_{x\to\infty}\frac{2x^3-5x+1}{3x^3+4x^2}$.

① 분자·분모 $x^3$으로 나누기: $\frac{2-5/x^2+1/x^3}{3+4/x}$.
② $x\to\infty$: $\frac{5}{x^2},\frac{1}{x^3},\frac{4}{x}\to0$. → $\frac{2}{3}$.

→ **$\frac{2}{3}$.**

---

## 연습 11

> $\lim_{x\to\infty}(\sqrt{x^2+5x}-\sqrt{x^2-3x})$.

① 유리화: $\frac{8x}{\sqrt{x^2+5x}+\sqrt{x^2-3x}}$.
② $x$로 나누기: $\frac{8}{\sqrt{1+5/x}+\sqrt{1-3/x}} \to \frac{8}{1+1}=4$.

→ **4.**

---

## 연습 12: 실전

① $x\to0^-$: $\frac{\sin x}{x}\to1$. $x\to0^+$: $e^x\to1$.
② 좌극한=우극한=1. $f(0)=e^0=1$.
③ $\lim_{x\to0}f(x)=f(0)=1$ → 연속.

→ **좌극한 1, 우극한 1, 연속.**

---

[목차로 돌아가기](../13-limits.md)
