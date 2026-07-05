# 세션 14: 미분법 — 순간 기울기를 자유자재로

**Phase 2 — 고전 테크닉 | 105분**

---

## Part A: 미분이란 — 순간 변화율

---

## 예시 1: 미분계수의 뜻

미분이란 무엇일까? 한 마디로 **순간 기울기**다. 곡선 위의 한 점에서 접선의 기울기를 구하는 것이다. 평균 기울기는 두 점을 이은 직선의 기울기다. 이 두 점을 점점 가까이 붙여서 거의 한 점으로 만들면, 그 극한이 바로 순간 기울기 — 즉 미분계수다. 식으로 쓰면 $\frac{f(x+h)-f(x)}{h}$에서 $h\to0$ 극한을 취한 것이다.

$f(x)=x^2$의 $x=3$에서 미분계수.

① 평균변화율을 먼저 구한다: $\frac{f(3+h)-f(3)}{h}$.
② $f(3+h)=(3+h)^2=9+6h+h^2$. $f(3)=9$.
③ $\frac{(9+6h+h^2)-9}{h}=\frac{6h+h^2}{h}=6+h$.
④ $h\to0$으로 보낸다 → $6$.
⑤ 이 값이 $x=3$에서의 **순간 기울기**다. $f'(3)=6$.

**미분 = 극한이다**: $f'(x) = \lim_{h\to0}\frac{f(x+h)-f(x)}{h}$.

![접선](graphs/14a-tangent.png)

---

## Part B: 기본 미분법 — 함수별 공식

---

## 예시 2: 거듭제곱 — $x^n$ 미분

가장 기본이 되는 미분 공식이다. 거듭제곱을 미분할 때는 **지수를 앞으로 내리고, 지수에서 1을 뺀다**. 이 규칙 하나로 모든 다항함수를 미분할 수 있다. $\frac{d}{dx}$라는 기호는 "$x$에 대해 미분하라"는 뜻이다.

$\frac{d}{dx}x^n = nx^{n-1}$. 지수를 앞으로 내리고, 지수에서 1을 뺀다.

$\frac{d}{dx}x^5 = 5x^4$.
$\frac{d}{dx}x^{100} = 100x^{99}$.
$\frac{d}{dx}x = 1\cdot x^0 = 1$.
$\frac{d}{dx}\sqrt{x} = \frac{d}{dx}x^{1/2} = \frac{1}{2}x^{-1/2} = \frac{1}{2\sqrt{x}}$.
$\frac{d}{dx}\frac{1}{x} = \frac{d}{dx}x^{-1} = -1\cdot x^{-2} = -\frac{1}{x^2}$.
$\frac{d}{dx}\frac{1}{x^3} = \frac{d}{dx}x^{-3} = -3x^{-4} = -\frac{3}{x^4}$.

**상수 미분**: $\frac{d}{dx}7 = 0$. 상수는 변하지 않으니 기울기가 0이다.
**상수배**: $\frac{d}{dx}[5x^3] = 5\cdot3x^2 = 15x^2$. 상수는 그냥 앞에 둔다.

---

## 예시 3: 지수·로그 — $e^x$와 $\ln x$

$\frac{d}{dx}e^x = e^x$. (그대로! 유일하게 자기 자신이 나온다)
$\frac{d}{dx}e^{2x}$: 연쇄법칙 필요 → $e^{2x}\cdot2 = 2e^{2x}$.

$\frac{d}{dx}\ln x = \frac{1}{x}$ ($x>0$).
$\frac{d}{dx}\ln(5x) = \frac{1}{5x}\cdot5 = \frac{1}{x}$ (연쇄).

$\frac{d}{dx}a^x = a^x\ln a$. ($a>0$)
$\frac{d}{dx}2^x = 2^x\ln2$. $\frac{d}{dx}10^x = 10^x\ln10$.

$\frac{d}{dx}\log_a x = \frac{1}{x\ln a}$.

---

## 예시 4: 삼각함수 — $\sin$/$\cos$/$\tan$

삼각함수의 미분은 서로 춤추듯 연결되어 있다. $\sin$을 미분하면 $\cos$이 되고, $\cos$을 미분하면 $-\sin$이 된다 — 부호가 뒤집히면서 제자리로 돌아온다. 이 순환 구조 덕분에 네 번 미분하면 원래 함수로 돌아온다. $\tan$의 미분은 $\sec^2 x$인데, 이건 몫의 미분으로 직접 증명할 수 있다.

$\frac{d}{dx}\sin x = \cos x$.
$\frac{d}{dx}\cos x = -\sin x$. (부호 뒤집힘!)
$\frac{d}{dx}\tan x = \sec^2 x = \frac{1}{\cos^2 x}$.

$\frac{d}{dx}\csc x = -\csc x\cot x$.
$\frac{d}{dx}\sec x = \sec x\tan x$.
$\frac{d}{dx}\cot x = -\csc^2 x$.

**암기 요령**: $\sin\to\cos$, $\cos\to-\sin$ (부호 뒤집힘).
$\tan$은 $\sec^2$이 나온다.

![sin의 도함수는 cos](graphs/14b-sin-derivative.png)

---

## 예시 5: 합·차·상수배 — 찢어서 미분

$\frac{d}{dx}[f(x) \pm g(x)] = f'(x) \pm g'(x)$.

$\frac{d}{dx}(3x^4 - 2x^2 + 5x - 7)$.
① 각 항 따로 미분: $3\cdot4x^3 - 2\cdot2x^1 + 5\cdot1 - 0$.
② $= 12x^3 - 4x + 5$.

$\frac{d}{dx}(2\sin x + e^x - \ln x) = 2\cos x + e^x - \frac{1}{x}$.

> **여기까지**: 거듭제곱(지수내리기), $e^x$는 그대로, $\ln x$는 $1/x$,
> $\sin\to\cos$, $\cos\to-\sin$, $\tan\to\sec^2$. 합·차는 찢어서 각각.

---

## Part C: 곱·몫·연쇄 — 미분의 3대 무기

---

## 예시 6: 곱의 미분 — $(fg)' = f'g + fg'$

두 함수가 곱해져 있을 때는 한꺼번에 미분할 수 없다. 그래서 **한쪽씩 번갈아 미분해서 더한다**. "앞 미분 × 뒤 그대로 + 앞 그대로 × 뒤 미분"이라는 규칙이다. 순서를 바꿔도 수학적으로는 같지만, 한 가지 순서로 고정해서 연습하는 게 실수를 줄이는 비결이다.

$f(x)=x^2\sin x$.

① $f' = 2x$, $g' = \cos x$.
② $(fg)' = 2x\cdot\sin x + x^2\cdot\cos x$.
→ $2x\sin x + x^2\cos x$.

$(x^3+1)(e^x)$.
① $f'=3x^2$, $g'=e^x$.
② $= 3x^2\cdot e^x + (x^3+1)\cdot e^x = e^x(3x^2+x^3+1) = e^x(x^3+3x^2+1)$.

**순서**: 앞 미분 × 뒤 그대로 + 앞 그대로 × 뒤 미분.

---

## 예시 7: 몫의 미분 — $(f/g)' = \frac{f'g - fg'}{g^2}$

분수꼴 함수의 미분이다. 곱의 미분과 비슷하지만, **분자에서 뺄셈**이고 **분모는 제곱**이 된다. "분자 먼저 미분, 분모는 제곱"이라고 외우면 된다. $\tan x$의 미분을 이 규칙으로 직접 증명해보면 $\sec^2 x$가 나온다 — 외워서 쓰는 것보다 훨씬 오래 기억에 남는다.

$f(x)=\frac{x^2}{x+1}$.

① $f'=2x$, $g'=1$.
② $\frac{2x(x+1) - x^2\cdot1}{(x+1)^2} = \frac{2x^2+2x - x^2}{(x+1)^2} = \frac{x^2+2x}{(x+1)^2}$.

$\frac{d}{dx}\tan x = \frac{d}{dx}\frac{\sin x}{\cos x}$.
① $=\frac{\cos x\cdot\cos x - \sin x\cdot(-\sin x)}{\cos^2 x} = \frac{\cos^2 x + \sin^2 x}{\cos^2 x}$.
② $=\frac{1}{\cos^2 x} = \sec^2 x$. (증명 완료!)

**주의**: 분자 순서 — $f'g - fg'$. $fg'$가 먼저 오지 않게!

---

## 예시 8: 연쇄법칙 — $(f(g(x)))' = f'(g(x)) \cdot g'(x)$

미분의 3대 무기 중 가장 강력한 무기다. 함수 안에 함수가 들어 있을 때, **겉부터 미분하고 안쪽 미분을 곱한다**. 양파 까는 순서와 똑같다. 겉껍질부터 벗기고, 그다음 안쪽 껍질을 벗긴다. "겉미분 × 속미분"이라고 외우면 된다.

$\frac{d}{dx}(x^2+1)^5$.
① 겉미분: $5(x^2+1)^4$ (거듭제곱 미분).
② 속미분: $2x$ ($x^2+1$ 미분).
③ → $5(x^2+1)^4\cdot2x = 10x(x^2+1)^4$.

$\frac{d}{dx}\sin(x^3)$.
① 겉: $\cos(x^3)$. ② 속: $3x^2$. → $3x^2\cos(x^3)$.

$\frac{d}{dx}e^{\sin x}$.
① 겉: $e^{\sin x}$. ② 속: $\cos x$. → $e^{\sin x}\cos x$.

$\frac{d}{dx}\ln(\cos x)$.
① 겉: $\frac{1}{\cos x}$. ② 속: $-\sin x$. → $-\frac{\sin x}{\cos x} = -\tan x$.

---

## 예시 9: 연쇄 중첩 — 3겹 4겹도 똑같이

$\frac{d}{dx}\sin(e^{x^2})$.
① 겉: $\cos(e^{x^2})$.
② 중간: $e^{x^2}$.
③ 속: $2x$.
→ $\cos(e^{x^2})\cdot e^{x^2}\cdot 2x$.

$\frac{d}{dx}\sqrt{\ln(\sin x)}$.
① $= \frac{1}{2\sqrt{\ln(\sin x)}} \cdot \frac{1}{\sin x} \cdot \cos x = \frac{\cot x}{2\sqrt{\ln(\sin x)}}$.

---

## 예시 10: 음함수 미분 — $y$가 섞여 있을 때

지금까지는 $y=f(x)$ 꼴로 깔끔하게 정리된 함수만 미분했다. 하지만 $x^2+y^2=25$처럼 $x$와 $y$가 뒤섞여 있으면 $y$를 $x$에 대해 풀기 어렵거나 불가능할 수 있다. 이럴 때는 **$y$를 $x$의 함수라고 믿고 양변을 그냥 $x$로 미분**한다. $y$가 나오면 연쇄법칙에 따라 $\frac{dy}{dx}$를 곱해준다. 그다음 $\frac{dy}{dx}$ 항들을 한쪽으로 몰아서 풀면 끝.

$x^2 + y^2 = 25$에서 $\frac{dy}{dx}$ 구하기.

① 양변을 $x$로 미분. $y$는 $x$의 함수로 본다.
② $2x + 2y\cdot\frac{dy}{dx} = 0$.
③ $\frac{dy}{dx}$ 항을 모은다: $2y\frac{dy}{dx} = -2x$.
④ $\frac{dy}{dx} = -\frac{x}{y}$.

$x^3 + y^3 = 6xy$에서 점 $(3,3)$에서의 기울기.
① $3x^2 + 3y^2\frac{dy}{dx} = 6y + 6x\frac{dy}{dx}$.
② $\frac{dy}{dx}$항 모으기: $3y^2\frac{dy}{dx} - 6x\frac{dy}{dx} = 6y - 3x^2$.
③ $\frac{dy}{dx}(3y^2-6x) = 6y-3x^2$.
④ $\frac{dy}{dx} = \frac{6y-3x^2}{3y^2-6x}$.
⑤ $(3,3)$ 대입: $\frac{18-27}{27-18} = \frac{-9}{9} = -1$.

---

## 예시 11: 로그미분 — 복잡한 지수·거듭제곱 처리

$x^x$처럼 밑도 $x$고 지수도 $x$인 함수, 또는 $(x^2+1)^{\sin x}$처럼 복잡한 거듭제곱은 기존 규칙으로는 미분할 수 없다. 이럴 때 **로그의 힘**을 빌린다. 양변에 $\ln$을 취하면 지수가 앞으로 내려와 평범한 곱셈이 된다. $\ln y = x\ln x$로 바꾸고 양변을 미분하면 끝. 이 기법은 로그가 **지수를 계수로 바꾸는 마법**을 부리기 때문에 가능하다.

$y = x^x$ 미분.

① 양변에 $\ln$ 취함: $\ln y = x\ln x$.
② 양변 $x$로 미분: $\frac{1}{y}\frac{dy}{dx} = 1\cdot\ln x + x\cdot\frac{1}{x} = \ln x + 1$.
③ $\frac{dy}{dx} = y(\ln x + 1) = x^x(\ln x + 1)$.

$y = (x^2+1)^{\sin x}$.
① $\ln y = \sin x \cdot \ln(x^2+1)$.
② $\frac{1}{y}\frac{dy}{dx} = \cos x\cdot\ln(x^2+1) + \sin x\cdot\frac{2x}{x^2+1}$.
③ $\frac{dy}{dx} = (x^2+1)^{\sin x}\left[\cos x\ln(x^2+1) + \frac{2x\sin x}{x^2+1}\right]$.

---

## 예시 12: 역함수 미분

$f^{-1}$의 미분: $(f^{-1})'(y) = \frac{1}{f'(x)}$ (단 $y=f(x)$).

$f(x)=x^3+x$. $f(1)=2$. $(f^{-1})'(2)$ 구하기.
① $f'(x)=3x^2+1$. $f'(1)=4$.
② $(f^{-1})'(2) = \frac{1}{f'(1)} = \frac{1}{4}$.

---

## 예시 13: 매개변수 미분

$x=t^2$, $y=t^3$일 때 $\frac{dy}{dx}$.

① $\frac{dx}{dt}=2t$, $\frac{dy}{dt}=3t^2$.
② $\frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{3t^2}{2t} = \frac{3t}{2}$.

$x=\cos t$, $y=\sin t$일 때 $t=\frac{\pi}{4}$에서 접선 기울기.
$\frac{dy}{dx} = \frac{\cos t}{-\sin t} = -\cot t$. $t=\frac{\pi}{4}$ → $-1$.

> **여기까지**: 곱은 앞미분×뒤+앞×뒤미분. 몫은 (분자미분×분모-분자×분모미분)/분모².
> 연쇄는 겉미분×속미분. 음함수는 양변 미분 후 $\frac{dy}{dx}$ 모으기.
> 로그미분은 $\ln$ 취하고 미분. 역함수는 $1/f'$. 매개변수는 $(dy/dt)/(dx/dt)$.

---

## 예시 13-B: 역삼각함수 미분 — $\arcsin$, $\arccos$, $\arctan$

$\frac{d}{dx}\arcsin x = \frac{1}{\sqrt{1-x^2}}$ ($|x|<1$).
$\frac{d}{dx}\arccos x = -\frac{1}{\sqrt{1-x^2}}$ ($|x|<1$).
$\frac{d}{dx}\arctan x = \frac{1}{1+x^2}$.

손으로: $\frac{d}{dx}\arcsin(2x) = \frac{1}{\sqrt{1-(2x)^2}}\cdot2 = \frac{2}{\sqrt{1-4x^2}}$.
$\frac{d}{dx}\arctan(x^2) = \frac{1}{1+(x^2)^2}\cdot2x = \frac{2x}{1+x^4}$.

---

## 예시 13-C: 절댓값 함수 미분 — 구간 나눠서

$f(x)=|x| = \begin{cases} -x, & x<0 \\ x, & x\geq0 \end{cases}$

$x<0$: $f'(x)=-1$. $x>0$: $f'(x)=1$. $x=0$: 미분 불가 (좌우 기울기 다름).

$f(x)=|x^2-1|$.
$x<-1$: $f(x)=x^2-1$, $f'=2x$.
$-1<x<1$: $f(x)=-(x^2-1)=1-x^2$, $f'=-2x$.
$x>1$: $f(x)=x^2-1$, $f'=2x$.
$x=\pm1$: $f=0$에서 꺾임 → 미분 불가.

---

## 예시 13-D: 혼합 종합 — 다 섞인 함수 미분

**삼각+지수+ロ그**: $f(x)=e^x\sin x + \ln(\cos x)$.
$f'(x)=e^x\sin x + e^x\cos x + \frac{-\sin x}{\cos x} = e^x(\sin x+\cos x) - \tan x$.

**지수+거듭제곱+삼각**: $f(x)=x^3 e^{2x}\tan x$.
곱 3개 → $(fgh)'=f'gh+fg'h+fgh'$.
$=3x^2 e^{2x}\tan x + x^3\cdot2e^{2x}\tan x + x^3 e^{2x}\sec^2 x$.
$=x^2 e^{2x}[3\tan x + 2x\tan x + x\sec^2 x]$.

**역삼각+로그**: $f(x)=\arctan(\ln x)$.
$f'(x)=\frac{1}{1+(\ln x)^2}\cdot\frac{1}{x} = \frac{1}{x(1+(\ln x)^2)}$.

**$x^x$ 일반화 — $\ln$ 미분으로만**: $y=(x^2+1)^{\sin x}$.
$\ln y = \sin x\cdot\ln(x^2+1)$.
$\frac{y'}{y} = \cos x\ln(x^2+1) + \sin x\cdot\frac{2x}{x^2+1}$.
$y' = (x^2+1)^{\sin x}\left[\cos x\ln(x^2+1) + \frac{2x\sin x}{x^2+1}\right]$.
> 로그미분은 $\ln$ 취하고 미분. 역함수는 $1/f'$. 매개변수는 $(dy/dt)/(dx/dt)$.

---

## Part D: 고계도함수와 변곡

---

## 예시 14: 2계·3계 도함수

$f(x)=x^4-3x^3+2x$.
① $f'(x)=4x^3-9x^2+2$.
② $f''(x)=12x^2-18x$.
③ $f'''(x)=24x-18$.
④ $f^{(4)}(x)=24$.
⑤ $f^{(5)}(x)=0$.

**의미**: $f'$=기울기(변화율), $f''$=기울기의 변화율(가속도), $f'''$=가속도의 변화율(저크).

---

## 예시 15: 여러 함수가 섞인 종합 미분

$f(x) = \frac{e^{x}\sin x}{x^2+1}$.

① 몫의 미분으로 접근. 분자 $u=e^x\sin x$는 곱의 미분.
② $u' = e^x\sin x + e^x\cos x = e^x(\sin x+\cos x)$.
③ $f' = \frac{u'(x^2+1) - u\cdot2x}{(x^2+1)^2} = \frac{e^x(\sin x+\cos x)(x^2+1) - 2xe^x\sin x}{(x^2+1)^2}$.
④ $= \frac{e^x[(\sin x+\cos x)(x^2+1) - 2x\sin x]}{(x^2+1)^2}$.

---

## 자주 하는 실수

### 실수 1: 연쇄에서 속미분을 빼먹는다

**틀린 길**: "$\frac{d}{dx}\sin(x^2)=\cos(x^2)$."

**왜 틀렸나**: 연쇄법칙 — 겉미분 $\cos(x^2)$에 속미분 $2x$를 곱해야.

**옳은 길**: $\frac{d}{dx}\sin(x^2)=2x\cos(x^2)$.

---

### 실수 2: 몫의 미분 순서를 거꾸로

**틀린 길**: "$\frac{d}{dx}\frac{f}{g}=\frac{fg'-f'g}{g^2}$."

**왜 틀렸나**: 분자는 $f'g-fg'$. $fg'$가 뒤.

**옳은 길**: $\frac{f'g-fg'}{g^2}$. "분자부터 미분"으로 외운다.

---

### 실수 3: 음함수에서 $y$ 미분할 때 $\frac{dy}{dx}$ 누락

**틀린 길**: "$y^2$을 $x$로 미분하면 $2y$."

**왜 틀렸나**: $y$는 $x$의 함수 → $\frac{d}{dx}y^2=2y\frac{dy}{dx}$.

**옳은 길**: $y$가 나오면 무조건 $\frac{dy}{dx}$를 붙인다.

---

## 방금 우리가 한 일

```
① 기본공식: x^n→nx^{n-1}, e^x→e^x, lnx→1/x, sin→cos, cos→-sin, tan→sec².
② 곱: f'g+fg'. 몫: (f'g-fg')/g². 연쇄: f'(g)·g'.
③ 음함수: 양변 x로 미분 → dy/dx 항 모으기.
④ 로그미분: lny 미분 → y'/y = (lny)' → y' = y·(lny)'.
⑤ 역함수: (f⁻¹)'(y)=1/f'(x). 매개변수: dy/dx=(dy/dt)/(dx/dt).
```

---

## 연습 1

$\frac{d}{dx}(3x^4-2x^3+x-5)$. 기본 미분.

→ 따라하기: **예시 2, 5**

> 풀이: [풀이집](solutions/14-solutions.md#연습-1)

---

## 연습 2

$\frac{d}{dx}(x^2\cos x)$. 곱의 미분.

→ 따라하기: **예시 6**

> 풀이: [풀이집](solutions/14-solutions.md#연습-2)

---

## 연습 3

$\frac{d}{dx}\frac{x^2+1}{x-1}$. 몫의 미분.

→ 따라하기: **예시 7**

> 풀이: [풀이집](solutions/14-solutions.md#연습-3)

---

## 연습 4

$\frac{d}{dx}\sqrt{\sin(x^2)}$. 연쇄 중첩.

→ 따라하기: **예시 8**

> 풀이: [풀이집](solutions/14-solutions.md#연습-4)

---

## 연습 5

$x^3+y^3=6xy$에서 $\frac{dy}{dx}$를 구하고 점 $(3,3)$에서의 값을 구하라. 음함수.

→ 따라하기: **예시 9**

> 풀이: [풀이집](solutions/14-solutions.md#연습-5)

---

## 연습 6: 구성형

미분하면 자기 자신이 되는 함수를 3개 말하고, 그런 함수의 일반형을 찾아보라.
($f'(x)=f(x)$를 만족하는 $f$)

→ 따라하기: **예시 3**

> 풀이: [풀이집](solutions/14-solutions.md#연습-6)

---

## 연습 7

$y=(\sin x)^x$를 로그미분으로 미분하라.

→ 따라하기: **예시 10**

> 풀이: [풀이집](solutions/14-solutions.md#연습-7)

---

## 연습 8: 실전

$x=t-\sin t$, $y=1-\cos t$일 때 $\frac{dy}{dx}$와 $\frac{d^2y}{dx^2}$를 $t$로 표현하라.

→ 따라하기: **예시 12**

> 풀이: [풀이집](solutions/14-solutions.md#연습-8)

---

## 연습 9

$\frac{d}{dx}(x^2 e^x)$. 곱의 미분.

→ 따라하기: **예시 6**

> 풀이: [풀이집](solutions/14-solutions.md#연습-9)

---

## 연습 10

$\frac{d}{dx}\frac{\ln x}{x}$. 몫의 미분.

→ 따라하기: **예시 7**

> 풀이: [풀이집](solutions/14-solutions.md#연습-10)

---

## 연습 11

$\frac{d}{dx}\cos(x^3)$. 연쇄법칙.

→ 따라하기: **예시 8**

> 풀이: [풀이집](solutions/14-solutions.md#연습-11)

---

## 연습 12: 실전2

$\frac{d}{dx}\frac{x}{\sqrt{x^2+1}}$. 몫+연쇄. $f''(0)$도 구하라.

→ 따라하기: **예시 7, 8**

> 풀이: [풀이집](solutions/14-solutions.md#연습-12)

---

## 오늘 배운 절차

```
1단계: 기본 미분공식 암기 — x^n, e^x, lnx, sin/cos/tan.
       합·차·상수배는 찢어서 각각.
2단계: 3대 무기 — 곱(f'g+fg'), 몫((f'g-fg')/g²), 연쇄(겉미분×속미분).
3단계: 특수 상황 — 음함수(dy/dx 모으기), 로그미분(ln취하고 미분),
       역함수(1/f'), 매개변수((dy/dt)/(dx/dt)).
```

---

## 용어 정리

지금까지 우리는 "순간 기울기", "겉미분×속미분", "음함수", "로그 씌워서 미분" 같은 쉬운 말만 썼다.
**방법은 이미 다 배웠다.** 이제 수학에서 쓰는 이름을 소개한다.

| 우리가 써온 말 | 수학 용어 | 기호/설명 |
|:------------:|:--------:|:---:|
| 순간 기울기 | 도함수(미분계수) | $f'(x)$, $\frac{dy}{dx}$ |
| 겉미분×속미분 | 연쇄법칙 | chain rule |
| 앞미분×뒤+앞×뒤미분 | 곱의 미분 | product rule |
| (분자미분×분모-분자×분모미분)/분모² | 몫의 미분 | quotient rule |
| $y$ 숨긴 채 미분 | 음함수 미분 | implicit differentiation |
| $\ln$ 씌우고 미분 | 로그미분 | logarithmic differentiation |
| $1/f'(x)$ | 역함수 미분 | inverse function theorem |
| $(dy/dt)/(dx/dt)$ | 매개변수 미분 | parametric differentiation |
| $f''$, $f'''$ | 고계도함수 | higher-order derivatives |
