# Solutions — 19B: First-Order Solution Methods

> Back to [19B](../19B-first-order-solution.md)

## Basic Drills

### D1. (9.3 #1) $dy/dx=3x^2y^2$.

Separate: $\int y^{-2}dy=\int 3x^2dx$. $-1/y=x^3+C$. $y=-1/(x^3+C)$.

### D2. (9.3 #5) $xyy'=x^2+1$.

$yy'=(x^2+1)/x=x+1/x$. $\int y\,dy=\int(x+1/x)dx$. $y^2/2=x^2/2+\ln|x|+C$. $y^2=x^2+2\ln|x|+C'$.

### D3. (9.3 #8) $dy/dx=2x(y^2+1)$.

$\int\frac{dy}{y^2+1}=\int 2x\,dx$. $\arctan y=x^2+C$. $y=\tan(x^2+C)$.

### D4. (9.3 #13) $y'=xe^y$, $y(0)=0$.

$\int e^{-y}dy=\int x\,dx$. $-e^{-y}=x^2/2+C$. $y(0)=0$: $-1=C$. $e^{-y}=1-x^2/2$. $y=-\ln(1-x^2/2)$.

### D5. (9.3 #17) $du/dt=(2t+\sec^2 t)/(2u)$, $u(0)=-5$.

$\int 2u\,du=\int(2t+\sec^2 t)dt$. $u^2=t^2+\tan t+C$. $u(0)=-5$: $25=C$. $u=-\sqrt{t^2+\tan t+25}$ (negative root).

### D6. (9.3 #20) $dy/dx=(x\sin x)/y$, $y(0)=-1$.

$\int y\,dy=\int x\sin x\,dx$. $y^2/2=-x\cos x+\sin x+C$. $y(0)=-1$: $1/2=C$. $y=-\sqrt{-2x\cos x+2\sin x+1}$ (negative root).

### D7. (9.5 #5) $y'+y=1$.

$P=1$, $\mu=e^x$. $(e^xy)'=e^x$. $e^xy=e^x+C$. $y=1+Ce^{-x}$.

### D8. (9.5 #7) $y'=x-y$.

$y'+y=x$. $P=1$, $\mu=e^x$. $(e^xy)'=xe^x$. $e^xy=xe^x-e^x+C$. $y=x-1+Ce^{-x}$.

### D9. (9.5 #9) $xy'+y=\sqrt{x}$.

$(xy)'=\sqrt{x}$. $xy=\frac{2}{3}x^{3/2}+C$. $y=\frac{2}{3}\sqrt{x}+\frac{C}{x}$.

### D10. (9.5 #12) $y'-3x^2y=x^2$.

$P=-3x^2$, $\mu=e^{-x^3}$. $(e^{-x^3}y)'=x^2e^{-x^3}$. $e^{-x^3}y=-\frac{1}{3}e^{-x^3}+C$. $y=-\frac{1}{3}+Ce^{x^3}$.

### D11. (9.4 #1) $dP/dt=0.04P(1-P/1200)$, $P(0)=60$.

Carrying capacity $M=1200$, $k=0.04$. $B=(1200-60)/60=19$. $P(t)=\frac{1200}{1+19e^{-0.04t}}$. $P(10)=\frac{1200}{1+19e^{-0.4}}\approx79$.

### D12. (9.4 #6) $dP/dt=0.4P-0.001P^2$, $P(0)=50$.

$=0.4P(1-P/1000)$. Carrying capacity $=1000$. $P'(0)=0.4(50)-0.001(2500)=20-2.5=17.5$.

---

## Advanced Drills

### A1. (9.3 #23) $y'=x+y$, $u=x+y$.

$u'=1+y'=1+u$. $\int du/(1+u)=\int dx$. $\ln|1+u|=x+C$. $1+u=Ae^x$. $y=Ae^x-x-1$.

### A2. (9.3 #24) $xy'=y+xe^{y/x}$, $v=y/x$.

$y=xv$, $y'=v+xv'$. $x(v+xv')=xv+xe^v$ → $xv'=e^v$. $\int e^{-v}dv=\int dx/x$. $-e^{-v}=\ln|x|+C$. $e^{-y/x}=-\ln|x|-C$.

### A3. (9.3 #25) $y'=2x\sqrt{1-y^2}$.

(a) $\int\frac{dy}{\sqrt{1-y^2}}=\int 2x\,dx$. $\arcsin y=x^2+C$. $y=\sin(x^2+C)$. (b) $y(0)=0$: $C=0$. $y=\sin(x^2)$. (c) $y(0)=2$: no solution since $\sin$ range is $[-1,1]$.

### A4. (9.5 #17) $xy'+y=3x^2$, $y(1)=4$.

$(xy)'=3x^2$. $xy=x^3+C$. $y(1)=4$: $4=1+C$ → $C=3$. $y=x^2+3/x$.

### A5. (9.5 #23) $xy'=y+x^2\sin x$, $y(\pi)=0$.

$y'-y/x=x\sin x$. $P=-1/x$, $\mu=1/x$. $(y/x)'=\sin x$. $y/x=-\cos x+C$. $y(\pi)=0$: $0=-(-1)+C\pi$... Actually: $y(\pi)/\pi=-\cos\pi+C=1+C$. $0=\pi(1+C)$ → $C=-1$. $y=x(-\cos x-1)=-x(\cos x+1)$.

### A6. (9.5 #24) $(x^2+1)y'+3x(y-1)=0$, $y(0)=2$.

$y'+\frac{3x}{x^2+1}y=\frac{3x}{x^2+1}$. $P=3x/(x^2+1)$, $\mu=(x^2+1)^{3/2}$. $((x^2+1)^{3/2}y)'=3x(x^2+1)^{1/2}$. RHS integral $=(x^2+1)^{3/2}+C$. $y=1+\frac{C}{(x^2+1)^{3/2}}$. $y(0)=2$: $C=1$. $y=1+(x^2+1)^{-3/2}$.

### A7. (9.5 #28) $xy'+y=-xy^2$ (Bernoulli $n=2$).

Divide by $y^2$: $xy^{-2}y'+y^{-1}=-x$. $v=y^{-1}$, $v'=-y^{-2}y'$. $-xv'+v=-x$ → $xv'-v=x$. $v'-v/x=1$. $P=-1/x$, $\mu=1/x$. $(v/x)'=1/x$. $v/x=\ln|x|+C$. $v=x\ln|x|+Cx$. $y=1/v=\frac{1}{x(\ln|x|+C)}$.

### A8. (9.4 #5) Halibut: $M=8\times10^7$, $k=0.71$, $y(0)=2\times10^7$.

$B=(8-2)/2=3$. $y(t)=\frac{8\times10^7}{1+3e^{-0.71t}}$. (a) $y(1)=\frac{8\times10^7}{1+3e^{-0.71}}\approx\frac{8\times10^7}{1+3(0.492)}\approx\frac{8\times10^7}{2.476}\approx3.23\times10^7$ kg. (b) $4\times10^7$: $1+3e^{-0.71t}=2$ → $t=\ln 3/0.71\approx1.54$ years.

### A9. (9.4 #7) Logistic: $P(0)=1000$, $M=10000$, $P(1)=2500$.

$P(t)=\frac{10000}{1+9e^{-kt}}$. $P(1)=2500$: $1+9e^{-k}=4$ → $e^{-k}=1/3$ → $k=\ln 3$. $P(4)=\frac{10000}{1+9e^{-4\ln 3}}=\frac{10000}{1+9/81}=\frac{10000}{10/9}=9000$.

### A10. (9.5 #31) RL circuit: $E=40$, $L=2$, $R=10$, $I(0)=0$.

$2I'+10I=40$ → $I'+5I=20$. $\mu=e^{5t}$. $I_{ss}=4$. $I(t)=4(1-e^{-5t})$. (b) $I(0.1)=4(1-e^{-0.5})\approx4(0.3935)\approx1.57$ A.

### A11. (9.5 #33) RC circuit: $R=5$, $C=0.05$, $E=60$, $Q(0)=0$.

$5Q'+20Q=60$ → $Q'+4Q=12$. $\mu=e^{4t}$. $Q_{ss}=3$. $Q(t)=3(1-e^{-4t})$. $I(t)=Q'(t)=12e^{-4t}$.

### A12. (Torricelli #1) Cylindrical tank: $h=2$m, $R=1$m, hole $r=1$ inch.

(a) $a=\pi(0.0254)^2\approx2.026\times10^{-3}$ m². $\frac{dh}{dt}=-\frac{a\sqrt{2gh}}{\pi R^2}=-\frac{2.026\times10^{-3}\sqrt{19.6h}}{\pi}\approx-0.0004\sqrt{20h}$. ✓ (b) $2\sqrt{h}=-0.0004\sqrt{20}\,t+2\sqrt{2}$. $h(t)=(\sqrt{2}-0.0002\sqrt{20}\,t)^2$. (c) Set $h=0$: $t=\frac{\sqrt{2}}{0.0002\sqrt{20}}\approx\frac{1.414}{0.000894}\approx1582$ s $\approx26.4$ min.
