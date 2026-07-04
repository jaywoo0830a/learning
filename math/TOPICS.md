# 수학 커리큘럼: 중학교 졸업 → 공학수학 + 현대수학

> **학습자:** 방법(절차)을 빠르게 체화하는 사람
> **원칙:** 방법 먼저, 용어는 나중에. 모든 세션은 $①$ $②$ $③$ 단계로 구성.
> **규모:** 130세션, 세션당 1.5~2시간, 총 약 225시간

---

## 전체 구조

| 단계 | 주제 | 세션 | 시간 |
|:---:|------|:---:|:---:|
| 1 | 논리 + 집합 + 대수 + 그래프 | 26 | 46h |
| 2 | 미분적분학 | 26 | 46h |
| 3 | 선형대수학 | 14 | 24h |
| 4 | 현대대수학 (군, 환, 체) | 10 | 18h |
| 5 | 확률과 통계 | 15 | 26h |
| 6 | 수치해석 입문 | 5 | 9h |
| 7 | 공학수학 1 — 상미분방정식 | 17 | 30h |
| 8 | 공학수학 2 — 벡터·푸리에·편미방·복소 | 17 | 30h |
| **계** | | **130** | **225h** |

---

## Phase 1: 논리 + 집합 + 대수 + 그래프 (26세션)

### 1-0. 현대 논리학 (6세션)

| # | 제목 | 배우는 절차 |
|:--:|------|-----------|
| 01 | 명제 논리: 진리표 | $①$ 연결사($\neg, \land, \lor, \to, \leftrightarrow$)별 규칙 암기 $②$ 복합명제 진리표 열별로 채우기 $③$ 모든 행이 $\text{T}$ = 항진식, 모두 $\text{F}$ = 모순 |
| 02 | 논리적 동치와 타당한 추론 | $①$ 동치법칙 적용 (드모르간: $\neg(p \land q) \equiv \neg p \lor \neg q$, $\neg(p \to q) \equiv p \land \neg q$ 등) $②$ modus ponens: $p, p\!\to\!q \;\therefore\; q$, modus tollens: $\neg q, p\!\to\!q \;\therefore\; \neg p$ $③$ 전제 모두 $\text{T}$인데 결론 $\text{F}$인 반례 있으면 부당 |
| 03 | 술어 논리: $\forall$, $\exists$ | $①$ 정의역 설정 $②$ $\forall x\,P(x)$: 모든 원소 대입해 참, $\exists x\,P(x)$: 하나라도 참 $③$ $\neg\forall \equiv \exists\neg$, $\neg\exists \equiv \forall\neg$ 규칙으로 부정문 만들기 |
| 04 | 증명 방법론 | $①$ 직접증명: $P$ 가정 $\to$ $Q$ 유도 $②$ 대우증명: $\neg Q$ 가정 $\to$ $\neg P$ 유도 $③$ 귀류법: $P \land \neg Q$ 가정 $\to$ 모순 도출 $④$ 귀납법: $P(1)$ 확인 $\to$ $P(k) \to P(k+1)$ 증명 |
| 05 | 집합과 무한: Cantor의 대각선 논법 | $①$ $\lvert\mathbb{N}\rvert = \lvert\mathbb{Z}\rvert = \lvert\mathbb{Q}\rvert = \aleph_0$ 확인 (일대일대응) $②$ $\lvert\mathbb{R}\rvert > \aleph_0$: 실수를 나열했다 가정 $\to$ 대각선으로 빠진 수 구성 $③$ 멱집합: $\lvert\mathcal{P}(A)\rvert = 2^{\lvert A\rvert} > \lvert A\rvert$ |
| 06 | 괴델의 불완전성 정리 | $①$ 기호에 번호 할당 $\to$ 식의 괴델 수 $\ulcorner\phi\urcorner$ 계산 $②$ $\text{Provable}(x)$ 술어를 산술식으로 구성 $③$ 대각선 논법으로 $G \leftrightarrow \neg\text{Provable}(\ulcorner G\urcorner)$ 구성 $④$ 무모순이면 $G$도 $\neg G$도 증명불가 — 그러나 $G$는 참. 어떤 체계도 자신의 무모순성을 증명할 수 없다 |

### 1-1. 식 다루기 (5세션)

| # | 제목 | 배우는 절차 |
|:--:|------|-----------|
| 07 | 조립제법과 고차 인수분해 | $①$ 상수항 약수 중 근 후보 목록 작성 $②$ 후보를 조립제법에 넣어 나머지 $0$ 확인 $③$ 인수 확정 $\to$ 차수 낮춰 반복 $\to$ 완전 인수분해 |
| 08 | 고차방정식·연립방정식 | $①$ 인수분해로 차수 낮춰 근 구하기 $②$ $3$원 연립: 변수 하나씩 소거 $\to$ $2$원 $\to$ $1$원 $\to$ 역대입 $③$ 이차연립: 일차식을 대입 $\to$ 일변수 이차방정식 |
| 09 | 부등식: 이차·유리·절댓값 | $①$ 인수분해 $\to$ 부호표 작성 $\to$ 해 구간 결정 $②$ 유리부등식: 분모 $\neq 0$ 주의 $③$ 절댓값: 부호 기준 구간 나누기 $\to$ 각 구간 풀기 $\to$ 합집합 |
| 10 | 함수의 언어 | $①$ 정의역 제한조건 $4$가지 적용 (분모 $\neq 0$, $\sqrt{\;\;}\geq 0$, $\log > 0$, $\tan$ 점근선) $②$ 그래프에서 $5$대 정보 읽기 $③$ $y = f(x)$ 표기법으로 식과 그래프 연결 |
| 11 | 다항함수와 유리함수 | $①$ $1$차: $y = mx + b$ ($m$ = 기울기, $b$ = $y$절편) $②$ $2$차: $a$ 부호·꼭짓점 $(-\frac{b}{2a}, f(-\frac{b}{2a}))$·절편 $\to$ 포물선 $③$ $n$차: 최고차항으로 끝행동 판단 $④$ 유리: 분모 $=0$ = 수직점근선, 차수비교 = 수평점근선 |

### 1-2. 초월함수 (4세션)

| # | 제목 | 배우는 절차 |
|:--:|------|-----------|
| 12 | 지수와 로그 | $①$ 지수법칙: $a^m a^n = a^{m+n}$, $(a^m)^n = a^{mn}$ $②$ $\log_a b = c \leftrightarrow a^c = b$, 로그 성질: $\log(MN) = \log M + \log N$, $\log(M^k) = k\log M$ $③$ 방정식: 밑 통일 or 로그 합치기, 진수 $>0$ 조건 확인 |
| 13 | 삼각함수: 정의와 그래프 | $①$ 호도법: $\pi\ \text{rad} = 180^\circ$, 비례 변환 $②$ 단위원: $(\cos\theta, \sin\theta)$, $\tan\theta = \frac{\sin\theta}{\cos\theta}$, 사분면별 부호 $③$ 그래프: $\sin, \cos$ 주기 $= \frac{2\pi}{\lvert b\rvert}$, 진폭 $= \lvert a\rvert$, $\tan$ 주기 $= \frac{\pi}{\lvert b\rvert}$ |
| 14 | 삼각방정식과 삼각법 | $①$ 기본해 $+ n \cdot \text{주기}$ 로 일반해 $②$ 사인법칙: $\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R$ $③$ 코사인법칙: $a^2 = b^2 + c^2 - 2bc\cos A$ |
| 15 | 함수 변형·합성·역함수·복소수 | $①$ 평행이동: $x$에 하는 건 반대방향 ($f(x-h)$: 오른쪽 $h$) $②$ 합성: $f(g(x))$ 안쪽부터 계산 $③$ 역함수: $y = x$ 에 대칭, $y$ 에 대해 풀기 $④$ 복소수 극형식: $z = r(\cos\theta + i\sin\theta) = re^{i\theta}$ |

### 1-3. 이산 수학 (5세션)

| # | 제목 | 배우는 절차 |
|:--:|------|-----------|
| 16 | 수열과 급수의 기초 | $①$ 등차: $a_n = a_1 + (n-1)d$, $S_n = \frac{n(a_1 + a_n)}{2}$ $②$ 등비: $a_n = a_1 r^{n-1}$, $S_n = a_1\frac{1-r^n}{1-r}$ $③$ $\sum_{k=1}^n k = \frac{n(n+1)}{2}$, $\sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6}$ $④$ 수학적 귀납법 $3$단계 |
| 17 | 그래프 이론: 기초 | $①$ 정점 $v$·변 $e$·차수 $\deg(v)$, $\sum\deg(v) = 2\lvert E\rvert$ $②$ walk $\to$ trail $\to$ path $\to$ cycle 구별법 $③$ 연결그래프 판정: 모든 정점쌍 경로 존재 |
| 18 | 트리와 최소신장트리 | $①$ 트리 조건: $n$정점, $n-1$변, 비순환, 연결 중 셋이면 트리 $②$ Kruskal: 모든 변을 가중치순 정렬 $\to$ 사이클 안 생기면 추가 $③$ Prim: 임의 정점 시작 $\to$ 가장 가벼운 변으로 확장 |
| 19 | 평면그래프와 색칠 | $①$ 오일러 공식: $v - e + f = 2$ $②$ 평면성 판정: $K_5$ 나 $K_{3,3}$ 을 포함하지 않으면 평면 $③$ 색칠수: 이분그래프 $= 2$, 평면그래프 $\leq 4$ |
| 20 | 그래프 알고리즘 | $①$ Dijkstra 최단경로: 출발점 거리 $0$, 나머지 $\infty$ $\to$ 인접 정점 거리 갱신 반복 $②$ Ford-Fulkerson 최대유량: 증가경로 찾아 흘려보내기 반복, $\text{max flow} = \text{min cut}$ |

### 1-4. Phase 1 마무리 (6세션)

| # | 제목 | 배우는 절차 |
|:--:|------|-----------|
| 21 | 유리·무리 방정식 총정리 | $①$ 분모 곱하기·제곱 $\to$ 무연근 검사 $②$ 부등식: 부호표로 영역 판단 $③$ 무리: $\sqrt{\;\;}$ 안 $\geq 0$ 확인부터 |
| 22 | 좌표기하: 직선·원·도형이동 | $①$ 거리공식 $\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$, 내분점 $(\frac{mx_2+nx_1}{m+n}, \frac{my_2+ny_1}{m+n})$ $②$ 원: $(x-a)^2+(y-b)^2 = r^2$ $③$ 평행이동: $x \to x-h$, $y \to y-k$ |
| 23 | 복소수 심화 | $①$ 사칙연산, 켤레복소수 $\overline{z}$ $②$ 극형식 $z = re^{i\theta}$, 곱셈 $z_1 z_2 = r_1 r_2 e^{i(\theta_1+\theta_2)}$ $③$ 드무아브르: $z^n = r^n e^{in\theta}$, $1$의 $n$제곱근 |
| 24 | **종합: 식·함수·그래프 혼합** | |
| 25 | **종합: 논리·증명·집합 연결** | |
| 26 | **Phase 1 최종 점검** | |

---

## Phase 2: 미분적분학 (26세션)

### 2-1. 극한 (4세션)

| # | 제목 | 배우는 절차 |
|:--:|------|-----------|
| 27 | 극한의 직관과 계산 | $①$ $\displaystyle\lim_{x\to a^-}f(x) = \lim_{x\to a^+}f(x)$ 이면 극한 존재 $②$ $\frac{0}{0}$ 꼴: 인수분해 $\to$ 약분 $\to$ 재대입 or 켤레곱 $\to$ 약분 $③$ $\frac{\infty}{\infty}$ 꼴: 최고차항으로 분자분모 나누기 |
| 28 | 연속과 주요 정리 | $①$ 연속 판정: $f(a)$ 존재? $\lim_{x\to a}f(x)$ 존재? $\lim_{x\to a}f(x) = f(a)$? $②$ 중간값 정리: 연속함수는 구간 내 모든 중간값을 지난다 $③$ 최대최소 정리: 닫힌구간 연속함수는 반드시 최대·최소를 가진다 |
| 29 | 특수 극한과 압축 정리 | $①$ $\displaystyle\lim_{x\to 0}\frac{\sin x}{x} = 1$, $\displaystyle\lim_{x\to\infty}\Bigl(1+\frac{1}{x}\Bigr)^x = e$ $②$ 압축 정리: $g(x) \leq f(x) \leq h(x)$ 이고 $g, h \to L$ 이면 $f \to L$ |
| 30 | **종합: 수식만 보고 극한 판단** | |

### 2-2. 미분법 (5세션)

| # | 제목 | 배우는 절차 |
|:--:|------|-----------|
| 31 | 미분계수의 정의와 기본 공식 | $①$ $f'(x) = \displaystyle\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}$ 계산 $②$ 기본 도함수: $\frac{d}{dx}x^n = nx^{n-1}$, $\frac{d}{dx}e^x = e^x$, $\frac{d}{dx}\ln x = \frac{1}{x}$, $\frac{d}{dx}\sin x = \cos x$, $\frac{d}{dx}\cos x = -\sin x$, $\frac{d}{dx}\tan x = \sec^2 x$ |
| 32 | 곱·몫·연쇄법칙 | $①$ 곱: $(fg)' = f'g + fg'$ $②$ 몫: $(\frac{f}{g})' = \frac{f'g - fg'}{g^2}$ $③$ 연쇄: $\frac{d}{dx}f(g(x)) = f'(g(x)) \cdot g'(x)$ |
| 33 | 음함수·역함수·로그·매개 미분 | $①$ 음함수: 양변 $x$로 미분 $\to$ $\frac{dy}{dx}$ 항 모아 풀기 $②$ 역함수: $\frac{dx}{dy} = \frac{1}{dy/dx}$ $③$ 로그미분: $\ln$ 취하고 미분 $④$ 매개: $\frac{dy}{dx} = \frac{dy/dt}{dx/dt}$ |
| 34 | 삼각·역삼각 미분 총정리 | $①$ $\frac{d}{dx}\tan x = \sec^2 x$, $\frac{d}{dx}\cot x = -\csc^2 x$, $\frac{d}{dx}\sec x = \sec x\tan x$, $\frac{d}{dx}\csc x = -\csc x\cot x$ $②$ $\frac{d}{dx}\arcsin x = \frac{1}{\sqrt{1-x^2}}$, $\frac{d}{dx}\arctan x = \frac{1}{1+x^2}$ |
| 35 | **종합: 어떤 함수든 미분 가능한가** | |

### 2-3. 미분 응용 (4세션)

| # | 제목 | 배우는 절차 |
|:--:|------|-----------|
| 36 | 접선·법선·평균값 정리 | $①$ 접선: $(a, f(a))$ 에서 $y - f(a) = f'(a)(x - a)$ $②$ 법선: 기울기 $= -1/f'(a)$ $③$ 평균값 정리: $f'(c) = \frac{f(b)-f(a)}{b-a}$ 를 만족하는 $c$ 찾기 |
| 37 | 극값·오목·곡선 스케치 | $①$ $f'$ 부호 = 증감, $f'=0$ 에서 부호변화 = 극값 $②$ $f''$ 부호 = 오목, $f''=0$ 에서 부호변화 = 변곡점 $③$ $7$단계 스케치: 정의역 $\to$ 절편 $\to$ 점근선 $\to$ 증감 $\to$ 극값 $\to$ 오목 $\to$ 그리기 |
| 38 | 최적화·관련비율 | $①$ 최적화: 변수정의 $\to$ 목적함수 $\to$ 제약소거 $\to$ $f' = 0$ $\to$ 검증 $②$ 관련비율: 관계식을 $t$로 미분 $\to$ 값 대입 $\to$ 변화율 구하기 |
| 39 | **종합: 미분 응용 실전** | |

### 2-4. 적분법 (6세션)

| # | 제목 | 배우는 절차 |
|:--:|------|-----------|
| 40 | 부정적분과 치환적분 | $①$ 역미분: $\int x^n dx = \frac{x^{n+1}}{n+1} + C$, $\int e^x dx = e^x + C$, $\int \frac{1}{x} dx = \ln\lvert x\rvert + C$ $②$ 치환: $u = g(x)$, $du = g'(x)dx$, $u$로 적분, 원래 변수로 복원 |
| 41 | 부분적분·삼각적분 | $①$ $\int u\,dv = uv - \int v\,du$, $u$ 선택은 LIATE 순서 $②$ $\sin^2 x = \frac{1-\cos 2x}{2}$, $\cos^2 x = \frac{1+\cos 2x}{2}$ $③$ $\tan^n x \sec^m x$ 분리 전략 |
| 42 | 유리함수 적분·삼각치환 | $①$ 부분분수: $\frac{P(x)}{Q(x)} = \frac{A}{x-a} + \frac{B}{x-b} + \cdots$, 계수비교 $②$ $\sqrt{a^2-x^2} \to x = a\sin\theta$, $\sqrt{a^2+x^2} \to x = a\tan\theta$, $\sqrt{x^2-a^2} \to x = a\sec\theta$ |
| 43 | 정적분·FTC·넓이·부피 | $①$ FTC: $\int_a^b f(x)dx = F(b) - F(a)$ $②$ 곡선 사이 넓이: $\int_a^b [f(x) - g(x)]dx$ $③$ 디스크: $\pi\int R^2 dx$, 와셔: $\pi\int (R^2-r^2)dx$, 껍질: $2\pi\int r h\,dx$ |
| 44 | 곡선길이·겉넓이·이상적분 | $①$ 곡선길이: $L = \int_a^b \sqrt{1 + (y')^2}\,dx$ $②$ 겉넓이: $S = 2\pi\int_a^b y\sqrt{1+(y')^2}\,dx$ $③$ 이상적분: $\int_a^\infty f = \lim_{b\to\infty}\int_a^b f$, 불연속점에서 편측극한 |
| 45 | **종합: 적분 방법 선택 알고리즘** | |

### 2-5. 급수와 다변수 기초 (7세션)

| # | 제목 | 배우는 절차 |
|:--:|------|-----------|
| 46 | 기하·$p$-급수·적분판정·비교판정 | $①$ 기하급수: $\sum_{n=0}^\infty ar^n = \frac{a}{1-r}\;(\lvert r\rvert < 1)$ $②$ $p$-급수: $\sum \frac{1}{n^p}$ 수렴 $\leftrightarrow$ $p > 1$ $③$ 적분판정: $\int_1^\infty f(x)dx$ 와 $\sum f(n)$ 동시수렴 $④$ 비교: 더 큰 수렴급수로 묶기 |
| 47 | 교대급수·비판정·근판정 | $①$ 교대급수: $a_n \searrow 0$ 이면 수렴, $\lvert S - S_n\rvert \leq a_{n+1}$ $②$ 비판정: $\lim\lvert\frac{a_{n+1}}{a_n}\rvert < 1 \to$ 절대수렴 $③$ 근판정: $\lim\lvert a_n\rvert^{1/n} < 1$ |
| 48 | 멱급수·테일러 전개 | $①$ 수렴반경: $\lvert x-a\rvert < R$, 양끝점 따로 검사 $②$ 테일러: $f(x) = \sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!}(x-a)^n$, 매클로린은 $a=0$ |
| 49 | 편도함수·기울기벡터 | $①$ 편미분: 변수 하나만 미분, 나머지는 상수 취급 $②$ $\nabla f = (\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z})$, $D_{\mathbf{u}}f = \nabla f \cdot \mathbf{u}$, $\nabla f$ 방향이 최대 증가 |
| 50 | 이중적분 | $①$ 직사각형: $\iint f(x,y)\,dy\,dx$, Fubini로 순서 교환 가능 $②$ 극좌표: $x = r\cos\theta$, $y = r\sin\theta$, $dA = r\,dr\,d\theta$ |
| 51 | 삼중적분·야코비안 | $①$ 직교·원통·구면좌표계 변환 $②$ 구면: $dV = \rho^2\sin\phi\,d\rho\,d\phi\,d\theta$ $③$ 변수변환: $dx\,dy = \lvert\det J\rvert\,du\,dv$ |
| 52 | **Phase 2 최종 점검** | |

---

## Phase 3: 선형대수학 (14세션)

| # | 제목 | 배우는 절차 |
|:--:|------|-----------|
| 53 | 행렬 연산·가우스 소거법 | $①$ 곱셈: $(AB)_{ij} = \sum_k a_{ik}b_{kj}$ $②$ 소거법: 피벗 아래 $0$ 만들기 $\to$ 후진대입 $③$ RREF: 피벗 $=1$, 피벗열 나머지 $=0$ |
| 54 | Rank·역행렬 (Gauss-Jordan) | $①$ $\operatorname{rank}(A) = \operatorname{rank}([A\mid\mathbf{b}]) = n$: 유일해, $<n$: 무한해, 불일치: 무해 $②$ $[A\mid I] \xrightarrow{\text{행연산}} [I\mid A^{-1}]$ |
| 55 | 행렬식 | $①$ $2\times2$: $ad-bc$, $n\times n$: 여인수 전개 $②$ 성질: 행교환 $\to -\det$, 비례행 $\to 0$, 삼각행렬 $\to$ 대각곱 $③$ $A^{-1} = \frac{\operatorname{adj}(A)}{\det(A)}$, 크래머: $x_i = \frac{\det(A_i)}{\det(A)}$ |
| 56 | 벡터공간·부분공간·일차독립 | $①$ 부분공간 판정: $\mathbf{0}\in W$, $\mathbf{u}+\mathbf{v}\in W$, $c\mathbf{u}\in W$ $②$ 독립: $c_1\mathbf{v}_1 + \cdots + c_n\mathbf{v}_n = \mathbf{0} \Rightarrow c_i = 0$ |
| 57 | 기저·차원·4대 부분공간 | $①$ 기저 = 최대일차독립집합, 차원 = 기저 원소 수 $②$ $\operatorname{rank}(A) = \dim(\operatorname{col}A) = \dim(\operatorname{row}A)$ $③$ $\dim(\ker A) + \operatorname{rank}(A) = n$ |
| 58 | 선형변환 | $①$ $T(\mathbf{x}) = A\mathbf{x}$, $\ker T = \{\mathbf{x}\mid A\mathbf{x}=\mathbf{0}\}$, $\operatorname{range} T = \{A\mathbf{x}\}$ $②$ 단사 $\leftrightarrow$ $\ker = \{\mathbf{0}\}$, 전사 $\leftrightarrow$ $\operatorname{range} =$ 공역 |
| 59 | 고유값·고유벡터 | $①$ $\det(A-\lambda I) = 0 \to \lambda_i$ $②$ $(A-\lambda_i I)\mathbf{v} = \mathbf{0}$ 풀어 고유벡터 $③$ 대각화: $P^{-1}AP = \operatorname{diag}(\lambda_1,\ldots,\lambda_n)$, $P = [\mathbf{v}_1\cdots\mathbf{v}_n]$ |
| 60 | 직교대각화·Gram-Schmidt·SVD | $①$ Gram-Schmidt: $\mathbf{v}_1$ 정규화 $\to$ $\mathbf{v}_2$에서 투영빼고 정규화 $\to$ 반복 $②$ $Q^\mathsf{T}AQ = \operatorname{diag}(\lambda)$ ($A$ 대칭) $③$ SVD: $A = U\Sigma V^\mathsf{T}$, $\sigma_i = \sqrt{\lambda_i(A^\mathsf{T}A)}$ |
| 61 | 이차형식·양한정·최소제곱법 | $①$ $\mathbf{x}^\mathsf{T}A\mathbf{x}$, 고유값 모두 $>0 \to$ 양한정 $②$ 최소제곱: $A^\mathsf{T}A\hat{\mathbf{x}} = A^\mathsf{T}\mathbf{b}$ $③$ 투영행렬: $H = A(A^\mathsf{T}A)^{-1}A^\mathsf{T}$ |
| 62 | 응용: 연립미방·PageRank | $①$ $\mathbf{x}' = A\mathbf{x} \to$ 고유값/벡터 $\to$ $\mathbf{x} = \sum c_i e^{\lambda_i t}\mathbf{v}_i$ $②$ PageRank: $(P^\mathsf{T} - I)\mathbf{x} = \mathbf{0}$, $\sum x_i = 1$ 인 고유벡터 |
| 63 | **Phase 3 중간 점검** | |
| 64 | 그래프 스펙트럼·마르코프·기저변환 | $①$ 인접행렬 고유값과 그래프 성질 연결 $②$ 정상분포: $\boldsymbol{\pi}P = \boldsymbol{\pi}$, $\sum\pi_i = 1$ $③$ 기저변환: $[\mathbf{v}]_{B'} = P^{-1}[\mathbf{v}]_B$ |
| 65 | **Phase 3 최종 점검** | |
| 66 | **Phase 1~3 통합: 논리로 미적분·대수 해석하기** | |

---

## Phase 4: 현대대수학 — 군, 환, 체 (10세션)

| # | 제목 | 배우는 절차 |
|:--:|------|-----------|
| 67 | 군의 정의와 예시 | $①$ $4$공리 순서 체크: 닫힘 $\to$ 결합 $(ab)c = a(bc)$ $\to$ 항등원 $e$ $\to$ 역원 $a^{-1}$ $②$ 예시: $(\mathbb{Z},+)$, $(\mathbb{Z}_n,+)$, $(\mathbb{R}\setminus\{0\},\times)$, $S_n$, $D_n$, $\mathrm{GL}_n(\mathbb{R})$ |
| 68 | 부분군과 순환군 | $①$ 부분군 판정: $H \subseteq G$, $e \in H$, $a,b \in H \Rightarrow ab^{-1} \in H$ $②$ 순환군: $\langle g\rangle = \{g^n \mid n \in \mathbb{Z}\}$, 구조는 $\mathbb{Z}_n$ 또는 $\mathbb{Z}$ |
| 69 | 라그랑주 정리와 대칭군 | $①$ $\lvert H\rvert \mid \lvert G\rvert$, $[G:H] = \frac{\lvert G\rvert}{\lvert H\rvert}$ $②$ $S_n$: 순환분해, 호환, 부호 $\operatorname{sgn}$ $③$ $A_n \trianglelefteq S_n$, $\lvert A_n\rvert = \frac{n!}{2}$ |
| 70 | 잉여류와 정규부분군 | $①$ 좌잉여류 $aH = \{ah \mid h \in H\}$, 우잉여류 $Ha$ 계산 $②$ $H \trianglelefteq G$ 판정: $\forall g,\; gH = Hg$ $③$ $[G:H] =$ 잉여류 개수 |
| 71 | 준동형사상과 동형정리 | $①$ $\varphi(ab) = \varphi(a)\varphi(b)$ 확인 $②$ $\ker\varphi \trianglelefteq G$, $\operatorname{im}\varphi \leq H$ $③$ 제$1$동형정리: $G/{\ker\varphi} \cong \operatorname{im}\varphi$ $④$ 몫군: $(aH)(bH) = abH$ |
| 72 | 환의 정의와 아이디얼 | $①$ 환 공리: 덧셈군 $+$ 곱셈결합 $+$ 분배법칙 $②$ 예: $\mathbb{Z}$, $\mathbb{Z}_n$, $M_n(\mathbb{R})$, $\mathbb{R}[x]$ $③$ 아이디얼 $I \trianglelefteq R$ 판정법 |
| 73 | 정역·체·다항식환 | $①$ 정역: $ab = 0 \Rightarrow a = 0 \lor b = 0$ (영인자 없음) $②$ 체: $0$ 아닌 모든 원소에 역원 존재 $③$ $\mathbb{Z}_p$ 는 체, $\mathbb{R}[x]$ 는 PID, $\mathbb{Z}[x]$ 는 UFD |
| 74 | 유한체와 RSA 암호 | $①$ 유한체 $\mathbb{F}_{p^n}$ 구성 개념 $②$ RSA: $n = pq$, $\varphi(n) = (p-1)(q-1)$, $ed \equiv 1 \pmod{\varphi(n)}$ $③$ 암호화: $c = m^e \bmod n$, 복호화: $m = c^d \bmod n$ |
| 75 | 갈루아 이론 맛보기 | $①$ 체의 확대 $K/F$ 와 차수 $[K:F]$ $②$ 갈루아 군 $\operatorname{Gal}(K/F)$ $③$ $5$차 이상 일반방정식의 해 공식 불가능, $3$대 작도 불가능 |
| 76 | **Phase 4 최종 점검 + 현대대수 종합** | |

---

## Phase 5: 확률과 통계 (15세션)

### 5-1. 확률 (4세션)

| # | 제목 | 배우는 절차 |
|:--:|------|-----------|
| 77 | 확률의 공리와 계산 | $①$ $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ $②$ $P(A^c) = 1 - P(A)$ $③$ $P(A \cap B) = P(A)P(B\mid A)$, 독립이면 $P(A \cap B) = P(A)P(B)$ |
| 78 | 조건부 확률과 베이즈 정리 | $①$ $P(A\mid B) = \frac{P(A \cap B)}{P(B)}$ $②$ 베이즈: $P(A\mid B) = \frac{P(B\mid A)P(A)}{P(B)}$ $③$ 전확률: $P(B) = \sum_i P(B\mid A_i)P(A_i)$ |
| 79 | 이산확률분포 | $①$ $E(X) = \sum xP(x)$, $\operatorname{Var}(X) = E(X^2) - [E(X)]^2$ $②$ 이항 $B(n,p)$: $P(X=k) = \binom{n}{k}p^k(1-p)^{n-k}$ $③$ 포아송 $\operatorname{Poisson}(\lambda)$: $P(X=k) = \frac{e^{-\lambda}\lambda^k}{k!}$ |
| 80 | 연속확률분포 | $①$ PDF $f(x)$: $P(a < X < b) = \int_a^b f(x)dx$, $\int_{-\infty}^\infty f = 1$ $②$ CDF $F(x) = P(X \leq x) = \int_{-\infty}^x f(t)dt$ $③$ 균등·지수분포 |

### 5-2. 추론의 기초 (4세션)

| # | 제목 | 배우는 절차 |
|:--:|------|-----------|
| 81 | 정규분포와 $z$-점수 | $①$ $z = \frac{x-\mu}{\sigma}$, 표준정규표 왼쪽 면적 읽기 $②$ $68$-$95$-$99.7$ 규칙 $③$ 역계산: 면적 $\to$ $z$값 $\to$ $x = \mu + z\sigma$ |
| 82 | 표본분포와 CLT | $①$ $\bar{x} \sim N(\mu, \frac{\sigma}{\sqrt{n}})$ ($n \geq 30$ or 정규모집단) $②$ $\hat{p} \sim N(p, \sqrt{\frac{p(1-p)}{n}})$ ($np \geq 10$, $n(1-p) \geq 10$) $③$ $t$분포: $\sigma$ 모를 때, $\text{df} = n-1$ |
| 83 | 신뢰구간 | $①$ 평균($z$): $\bar{x} \pm z^*\frac{\sigma}{\sqrt{n}}$ $②$ 평균($t$): $\bar{x} \pm t^*\frac{s}{\sqrt{n}}$, $\text{df} = n-1$ $③$ 비율($z$): $\hat{p} \pm z^*\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$ |
| 84 | 가설검정 $5$단계 | $①$ $H_0$, $H_1$ 설정 $②$ 유의수준 $\alpha$ 결정 $③$ 검정통계량 계산 $④$ $p$-value or 기각역 $⑤$ $H_0$ 기각/채택 결론 — 모든 검정에 동일 적용 |

### 5-3. 검정 방법들 (4세션)

| # | 제목 | 배우는 절차 |
|:--:|------|-----------|
| 85 | $z$-검정·$t$-검정 | $①$ 일표본 $z$: $z = \frac{\bar{x}-\mu_0}{\sigma/\sqrt{n}}$ $②$ 일표본 $t$: $t = \frac{\bar{x}-\mu_0}{s/\sqrt{n}}$, $\text{df} = n-1$ $③$ 독립이표본 $t$: $t = \frac{\bar{x}_1-\bar{x}_2}{\text{SE}}$, $\text{df}$는 계산기 $④$ 쌍체 $t$: 차이 $d$로 일표본 $t$ |
| 86 | 비율 검정·오류·검정력 | $①$ 비율 $z$: $z = \frac{\hat{p}-p_0}{\sqrt{p_0(1-p_0)/n}}$ $②$ $\alpha = P(\text{Type I})$, $\beta = P(\text{Type II})$, $\text{Power} = 1-\beta$ $③$ 표본크기: $n \geq (\frac{z^*\sigma}{E})^2$ |
| 87 | 카이제곱 검정 | $①$ 적합도: $\chi^2 = \sum\frac{(O-E)^2}{E}$, $\text{df} = k-1$ $②$ 독립성/동질성: 이원표, $E = \frac{\text{행합}\times\text{열합}}{n}$, $\text{df} = (r-1)(c-1)$ $③$ $p$-value $= \chi^2$ 오른쪽 꼬리 면적 |
| 88 | 회귀분석 | $①$ 최소제곱선: $b_1 = r\frac{s_y}{s_x}$, $b_0 = \bar{y} - b_1\bar{x}$ $②$ 기울기 추론: $t = \frac{b_1}{\text{SE}_{b_1}}$, $\text{df} = n-2$ $③$ 잔차그림으로 선형성·등분산성 확인 |

### 5-4. 종합 (3세션)

| # | 제목 | 배우는 절차 |
|:--:|------|-----------|
| 89 | 정보이론 기초: 엔트로피 | $①$ $H(X) = -\sum p(x)\log p(x)$, 정보량 $= -\log p(x)$ $②$ KL 발산 $D_{KL}(P\|Q) = \sum P\log\frac{P}{Q}$, 교차엔트로피와 손실함수 $③$ 데이터 압축·통신의 수학적 원리 |
| 90 | **종합: 데이터만 보고 올바른 분석 선택하기** | |
| 91 | **Phase 5 최종 점검 + Phase 1~5 통합** | |

---

## Phase 6: 수치해석 입문 (5세션)

| # | 제목 | 배우는 절차 |
|:--:|------|-----------|
| 92 | 부동소수점과 오차 | $①$ IEEE 754 구조 (부호·지수·가수) $②$ 절대오차 $= \lvert\tilde{x}-x\rvert$, 상대오차 $= \frac{\lvert\tilde{x}-x\rvert}{\lvert x\rvert}$ $③$ 오차전파: 덧셈/뺄셈 $\to$ 절대오차합, 곱셈/나눗셈 $\to$ 상대오차합 |
| 93 | 방정식 풀이: 이분법·Newton | $①$ 이분법: $f(a)f(b) < 0 \to$ 중점 $c \to$ 부호 따라 구간 반쪽 $\to$ 반복 $②$ Newton: $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$, $2$차수렴 $③$ 수렴조건과 초기값 선택 |
| 94 | 수치적분 | $①$ 사다리꼴: $\frac{h}{2}(f_0 + 2f_1 + \cdots + 2f_{n-1} + f_n)$, 오차 $O(h^2)$ $②$ Simpson: $\frac{h}{3}(f_0 + 4f_1 + 2f_2 + 4f_3 + \cdots + f_n)$, 오차 $O(h^4)$ $③$ Gauss 구적법: 최적 가중치·노드로 정확도 극대화 |
| 95 | 선형계: LU분해·반복법 | $①$ $A = LU \to L\mathbf{y} = \mathbf{b}$ (전진대입) $\to$ $U\mathbf{x} = \mathbf{y}$ (후진대입) $②$ Jacobi: $x_i^{(k+1)} = \frac{b_i - \sum_{j \neq i}a_{ij}x_j^{(k)}}{a_{ii}}$ $③$ Gauss-Seidel: 갱신된 값 즉시 사용 |
| 96 | ODE: Euler·RK4 | $①$ Euler: $y_{n+1} = y_n + h\cdot f(t_n, y_n)$, $1$차 정확도 $②$ RK4: $k_1 \sim k_4$ 계산 $\to$ $y_{n+1} = y_n + \frac{h}{6}(k_1+2k_2+2k_3+k_4)$, $4$차 정확도 $③$ 안정성·step size 선택 |

---

## Phase 7: 공학수학 1 — 상미분방정식 (17세션)

### 7-1. 1계 ODE (5세션)

| # | 제목 | 배우는 절차 |
|:--:|------|-----------|
| 097 | 변수분리·1계 선형 | $①$ 분리형: $\frac{dy}{g(y)} = f(x)dx \to$ 양변 적분 $②$ 선형 $y' + Py = Q$: 적분인자 $\mu = e^{\int Pdx} \to (\mu y)' = \mu Q \to$ 적분 |
| 098 | 완전미방·동차형·베르누이 | $①$ 완전: $Mdx + Ndy = 0$, $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$ 확인 $\to$ 적분 $②$ 동차: $\frac{y}{x} = v$ 치환 $③$ 베르누이: $u = y^{1-n}$ 치환 $\to$ 선형 |
| 099 | 1계 미방 종합과 모델링 | $①$ 유형 판별 순서도: 분리가능? $\to$ 선형? $\to$ 완전? $\to$ 베르누이? $\to$ 동차? $②$ 냉각·인구·혼합·RC회로 모델링 |
| 100 | 방향장·존재성·자율미방 | $①$ 방향장: 격자점에 $y'$ 기울기 선분 $\to$ 해곡선 추적 $②$ Picard: $f$ 와 $\frac{\partial f}{\partial y}$ 연속 $\to$ 국소적 유일해 $③$ 자율 $y' = f(y) \to$ 위상선 분석 |
| 101 | **1계 미방 중간 점검** | |

### 7-2. 2계 선형 ODE (5세션)

| # | 제목 | 배우는 절차 |
|:--:|------|-----------|
| 102 | 제차: 특성방정식 | $①$ $ay'' + by' + cy = 0 \to ar^2 + br + c = 0$ $②$ 두 실근 $r_1 \neq r_2$: $c_1e^{r_1t} + c_2e^{r_2t}$ $③$ 중근 $r$: $(c_1 + c_2t)e^{rt}$ $④$ 켤레복소 $\alpha \pm i\beta$: $e^{\alpha t}(c_1\cos\beta t + c_2\sin\beta t)$ |
| 103 | 비제차: 미정계수법 | $①$ 우변 형태 보고 $y_p$ 추측 (다항·지수·삼각 각각 템플릿) $②$ $y_p$ 를 미방에 대입 $\to$ 계수 결정 $③$ 제차해와 겹치는 항 있으면 $t$ 곱하기 |
| 104 | 매개변수 변환법·차수 축소 | $①$ $y_p = -y_1\!\int\!\frac{y_2 g}{W}dt + y_2\!\int\!\frac{y_1 g}{W}dt$ ($W = y_1y_2' - y_1'y_2$) $②$ 한 해 알 때: $y_2 = y_1\!\int\!\frac{e^{-\int P}}{y_1^2}dt$ |
| 105 | 역학적 진동 | $①$ $m\ddot{y} + c\dot{y} + ky = F(t)$, $\zeta = \frac{c}{2\sqrt{mk}}$ $②$ $\zeta < 1$ 과소감쇠, $\zeta = 1$ 임계감쇠, $\zeta > 1$ 과대감쇠 $③$ $\omega_d = \omega_n\sqrt{1-\zeta^2}$, 공진: $\omega \approx \omega_n \to$ 진폭 $\uparrow$ |
| 106 | **2계 미방 중간 점검** | |

### 7-3. 고계·연립·라플라스 (5세션)

| # | 제목 | 배우는 절차 |
|:--:|------|-----------|
| 107 | 고계 선형 ODE | $①$ $n$계 $\to$ $n$차 특성방정식 $\to$ $n$개 근 $②$ 근 종류별 해 조합, 비제차는 미정계수법 확장 |
| 108 | 연립 ODE | $①$ 소거법: $D = \frac{d}{dt}$ 연산자로 한 변수 소거 $②$ 행렬법: $\mathbf{x}' = A\mathbf{x} \to$ 고유값/벡터로 일반해 (Phase 3) $③$ 중복·복소 고유값 처리 (Jordan 블록, 실수화) |
| 109 | 라플라스 변환: 정의와 성질 | $①$ $\mathcal{L}\{f\} = \int_0^\infty e^{-st}f(t)dt$ $②$ 기본쌍: $\mathcal{L}\{1\} = \frac{1}{s}$, $\mathcal{L}\{t^n\} = \frac{n!}{s^{n+1}}$, $\mathcal{L}\{e^{at}\} = \frac{1}{s-a}$, $\mathcal{L}\{\sin\omega t\} = \frac{\omega}{s^2+\omega^2}$ $③$ $\mathcal{L}\{f'\} = sF - f(0)$, $\mathcal{L}\{e^{at}f(t)\} = F(s-a)$ |
| 110 | 라플라스로 미방 풀기 | $①$ 미방 전체에 $\mathcal{L}$ 적용 $\to$ $Y(s)$에 대한 대수방정식 $②$ $Y(s) = \cdots$ 로 풀기 $③$ 부분분수 분해 $\to$ 역변환 표 매칭 $\to$ $y(t)$ |
| 111 | 계단·충격·합성곱 | $①$ 단위계단 $u_c(t)$: $\mathcal{L}\{u_c(t)f(t-c)\} = e^{-cs}F(s)$ $②$ Dirac $\delta(t-a)$: $\mathcal{L}\{\delta(t-a)\} = e^{-as}$ $③$ 합성곱: $\mathcal{L}\{f*g\} = F(s)G(s)$, $(f*g)(t) = \int_0^t f(\tau)g(t-\tau)d\tau$ |

### 7-4. 급수해법 (2세션)

| # | 제목 | 배우는 절차 |
|:--:|------|-----------|
| 112 | 멱급수해·Frobenius | $①$ $y = \sum a_n(x-x_0)^n$ 가정 $\to$ 미방 대입 $\to$ 계수비교 $\to$ 점화식 $②$ 정칙특이점: $y = x^r\sum a_nx^n \to$ 결정방정식 $\to$ $r$에 따른 해 |
| 113 | **Phase 7 최종 점검** | |

---

## Phase 8: 공학수학 2 — 벡터·푸리에·편미방·복소 (17세션)

### 8-1. 벡터해석 (5세션)

| # | 제목 | 배우는 절차 |
|:--:|------|-----------|
| 114 | $\nabla$·$\operatorname{div}$·$\operatorname{curl}$ | $①$ $\nabla = (\frac{\partial}{\partial x}, \frac{\partial}{\partial y}, \frac{\partial}{\partial z})$ $②$ $\nabla f =$ 기울기벡터, $\nabla\cdot\mathbf{F} =$ 발산, $\nabla\times\mathbf{F} =$ 회전 $③$ $\nabla^2 f = \nabla\cdot(\nabla f) = f_{xx}+f_{yy}+f_{zz}$ (라플라시안) |
| 115 | 선적분·보존장 | $①$ $\int_C f\,ds = \int f(\mathbf{r}(t))\,\lvert\mathbf{r}'(t)\rvert\,dt$ $②$ $\int_C \mathbf{F}\cdot d\mathbf{r} = \int \mathbf{F}(\mathbf{r}(t))\cdot\mathbf{r}'(t)\,dt$ $③$ $\nabla\times\mathbf{F} = \mathbf{0}$ (단순연결) $\to$ $\mathbf{F} = \nabla\phi$ $\to$ 선적분 $= \phi(\text{끝}) - \phi(\text{시작})$ |
| 116 | 그린·발산·스토크스 정리 | $①$ 그린: $\oint_C Pdx+Qdy = \iint_D (\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y})dA$ $②$ 발산: $\oiint_S \mathbf{F}\cdot d\mathbf{S} = \iiint_V \nabla\cdot\mathbf{F}\,dV$ $③$ 스토크스: $\oint_C \mathbf{F}\cdot d\mathbf{r} = \iint_S (\nabla\times\mathbf{F})\cdot d\mathbf{S}$ |
| 117 | 곡선좌표계 | $①$ 원통좌표 $(r,\theta,z)$: $\nabla f = (\frac{\partial f}{\partial r}, \frac{1}{r}\frac{\partial f}{\partial\theta}, \frac{\partial f}{\partial z})$ $②$ 구면좌표 $(\rho,\phi,\theta)$: $\nabla f = (\frac{\partial f}{\partial\rho}, \frac{1}{\rho}\frac{\partial f}{\partial\phi}, \frac{1}{\rho\sin\phi}\frac{\partial f}{\partial\theta})$ |
| 118 | **벡터해석 중간 점검** | |

### 8-2. 푸리에 해석 (4세션)

| # | 제목 | 배우는 절차 |
|:--:|------|-----------|
| 119 | 푸리에 급수 | $①$ $f(x) = \frac{a_0}{2} + \sum_{n=1}^\infty (a_n\cos\frac{n\pi x}{L} + b_n\sin\frac{n\pi x}{L})$ $②$ $a_n = \frac{1}{L}\int_{-L}^L f(x)\cos\frac{n\pi x}{L}dx$, $b_n = \frac{1}{L}\int_{-L}^L f(x)\sin\frac{n\pi x}{L}dx$ $③$ 짝함수: $b_n=0$, 홀함수: $a_n=0$ |
| 120 | 반구간·수렴·깁스 | $①$ $[0,L]$ $\to$ 짝/홀 확장 $\to$ $\cos$/$\sin$ 급수 $②$ 불연속점 $\to$ $\frac{f(x^+)+f(x^-)}{2}$ 로 수렴, $9\%$ 오버슛 (깁스) |
| 121 | 푸리에 변환 | $①$ $F(\omega) = \int_{-\infty}^\infty f(x)e^{-i\omega x}dx$, $f(x) = \frac{1}{2\pi}\int_{-\infty}^\infty F(\omega)e^{i\omega x}d\omega$ $②$ 미분 $\to$ $i\omega F$, 합성곱 $\leftrightarrow$ 곱, 스케일링·이동 성질 |
| 122 | DFT·FFT·스펙트럼 | $①$ 이산화: $N$개 샘플 $\to$ DFT 행렬 $②$ FFT: Cooley-Tukey, $O(N\log N)$ $③$ 주파수 영역 해석: 저주파·고주파·필터링 개념 |

### 8-3. 편미분방정식 (4세션)

| # | 제목 | 배우는 절차 |
|:--:|------|-----------|
| 123 | 분류·변수분리법 | $①$ $B^2-AC$ 부호: $<0$ 타원, $=0$ 포물, $>0$ 쌍곡 $②$ $u(x,t) = X(x)T(t)$ 가정 $\to$ 두 상미방 $③$ 경계조건으로 고유값·고유함수 결정 |
| 124 | 파동·열방정식 (1D) | $①$ 파동 $u_{tt} = c^2u_{xx}$: $X''+\lambda X = 0 \to \sin$/$\cos$, d'Alembert 해 $②$ 열 $u_t = k u_{xx}$: $X''+\lambda X = 0$, $T' + k\lambda T = 0 \to$ 지수감쇠 $③$ 초기조건으로 계수 결정 |
| 125 | 라플라스·비제차 | $①$ $u_{xx}+u_{yy} = 0$, Dirichlet/Neumann 경계조건 $②$ 비제차: 우변을 고유함수 급수로 전개 $\to$ 모드별 상미방 |
| 126 | 극좌표·원통·구면 PDE | $①$ 원판에서 라플라스: $r$분리 $\to$ Bessel 방정식 $②$ 구면: $\phi$분리 $\to$ Legendre 방정식 $③$ 변수분리로 특수함수 등장 |

### 8-4. 복소해석 (4세션)

| # | 제목 | 배우는 절차 |
|:--:|------|-----------|
| 127 | 복소함수와 해석성 | $①$ $f(z) = u(x,y) + iv(x,y)$ $②$ Cauchy-Riemann: $u_x = v_y$, $u_y = -v_x$ $\to$ 해석적 $③$ 해석함수는 무한번 미분가능, $u$와 $v$는 조화함수 ($\nabla^2 u = \nabla^2 v = 0$) |
| 128 | 복소적분·Cauchy 정리 | $①$ $\int_C f(z)dz = \int (u+iv)(dx+idy)$ $②$ 해석함수의 단순닫힌곡선 적분 $= 0$ $③$ 적분공식: $f(a) = \frac{1}{2\pi i}\oint_C \frac{f(z)}{z-a}dz$ |
| 129 | Laurent·유수 정리 | $①$ Laurent 전개: $f(z) = \sum_{n=-\infty}^\infty a_n(z-z_0)^n$, $\operatorname{Res}(f,z_0) = a_{-1}$ $②$ 유수정리: $\oint_C f = 2\pi i\sum\operatorname{Res}$ $③$ 실적분 응용: $\int_0^{2\pi}R(\cos\theta,\sin\theta)d\theta$, $\int_{-\infty}^\infty \frac{P(x)}{Q(x)}dx$ |
| 130 | **전 과정 최종 점검** | |

---

## 일정 (하루 3시간, 19주)

| 주 | 세션 | 내용 |
|:--:|:----:|------|
| 1 | 01-07 | 논리(괴델까지) + 식 다루기 시작 |
| 2 | 08-14 | 식 다루기 완료 + 초월함수 |
| 3 | 15-21 | 함수 변형·그래프 이론 + 유리·무리 |
| 4 | 22-28 | 좌표기하·복소수·종합 + 극한 시작 |
| 5 | 29-35 | 극한 완료 + 미분법 전부 |
| 6 | 36-42 | 미분 응용 + 적분법 시작 |
| 7 | 43-49 | 적분 마무리 + 급수 + 편도함수 |
| 8 | 50-56 | 다변수·Phase 2 완료 + 선형대수 시작 |
| 9 | 57-63 | 선형대수 계속 + 중간점검 |
| 10 | 64-70 | 선형대수 완료 + 현대대수 시작 |
| 11 | 71-77 | 현대대수 완료 + 확률 시작 |
| 12 | 78-84 | 확률 완료 + 추론 기초 |
| 13 | 85-91 | 검정·회귀·정보이론 + Phase 5 완료 |
| 14 | 92-98 | 수치해석 + 1계 ODE |
| 15 | 99-105 | ODE 계속 + 2계 미방 |
| 16 | 106-112 | 고계·연립·라플라스 + 급수해 |
| 17 | 113-119 | Phase 7 완료 + 벡터해석·푸리에 |
| 18 | 120-126 | 푸리에·편미방 |
| 19 | 127-130 | 복소해석 + 최종 점검 |

---

## 세션 진행 방식 (전 세션 공통)

```
[ 5분] 오늘 배울 기술이 필요한 이유 — 실전 상황 제시
[25분] 절차 설명: ①→②→③ 단계로 보여주고 숫자 예시로 따라하기
[45분] 연습: 난이도 순 4~6문제 (마지막 2문제는 이전 내용 통합)
[10분] 용어 공개: 여기서 처음으로 수학 용어 등장
[ 5분] 다음 세션 연결고리 + 오늘 배운 절차 카드 정리
```

종합·점검 세션은 풀이 없는 실전 문제로만 구성한다. 해설은 다음 세션 시작 시 제공한다.
