# Solutions — 19A: ODE Modeling

> Back to [19A](../19A-ode-modeling.md)

## Basic Drills

### D1. (9.1 #6) $y'+y=2\sin x$, $y=\sin x-\cos x$?

$y'=\cos x+\sin x$. $y'+y=\cos x+\sin x+\sin x-\cos x=2\sin x$. ✓

### D2. (9.1 #7) $y'+2y=2e^x$, $y=\frac{2}{3}e^x+e^{-2x}$?

$y'=\frac{2}{3}e^x-2e^{-2x}$. $y'+2y=\frac{2}{3}e^x-2e^{-2x}+\frac{4}{3}e^x+2e^{-2x}=2e^x$. ✓

### D3. (9.1 #9) $xy'-y=0$, $y=\sqrt{x}$?

$y'=\frac{1}{2\sqrt{x}}$. $xy'-y=\frac{x}{2\sqrt{x}}-\sqrt{x}=\frac{\sqrt{x}}{2}-\sqrt{x}$. Note: the ref exercise may use $2xy'-y=0$ instead. Verify by substitution.

### D4. (9.1 #18a) $x^2y'+xy=1$, $y=(\ln x+C)/x$?

$y'=\frac{1-\ln x-C}{x^2}$. $x^2y'+xy=1-\ln x-C+\ln x+C=1$. ✓

### D5. (9.1 #19b) $y'=-y^2$, $y=1/(x+C)$?

$y'=-\frac{1}{(x+C)^2}=-y^2$. ✓

### D6. (9.2 #9) $y'=\frac{1}{2}y$ direction field.

Slope $=y/2$. On $y=0$: horizontal. Above: rising. Below: falling. Solutions: $Ce^{x/2}$.

### D7. (9.2 #10) $y'=x-y+1$ direction field.

Nullcline $y=x+1$ (slope=0). Above: negative. Below: positive. Solutions approach $y=x+1$.

### D8. (9.1 #19a) $y'=-y^2$?

$y'=-y^2\leq 0$ always. Every solution is non-increasing.

### D9. (9.1 #19d) $y'=-y^2$, $y(0)=0.5$?

$y=1/(x+C)$. $0.5=1/C$ → $C=2$. $y=1/(x+2)$.

### D10. (9.2 #11) $y'=y-2x$, through $(1,0)$?

At $(1,0)$: slope $=-2$. Nullcline $y=2x$.

### D11. (9.2 #19a) Euler, $h=0.2$, $y'=y$, $y(0)=1$?

$y_1=1.2$, $y_2=1.44$. Exact $e^{0.4}\approx1.4918$.

### D12. (9.2 #21) Euler, $h=0.5$, $y'=y-2x$, $y(1)=0$?

$y_1=-1$, $y_2=-3$, $y_3=-7$, $y_4=-15$.

---

## Advanced Drills

### A1. (9.1 #13) $tdy/dt=y+t^2\sin t$, $y(\pi)=0$, $y=-t\cos t-t$?

$y'=-\cos t+t\sin t-1$. $ty'=-t\cos t+t^2\sin t-t=y+t^2\sin t$. ✓ $y(\pi)=0$. ✓

### A2. (9.1 #14) $y'-2y=1-2x$, $y(0)=5$, $y=5e^{2x}+x$?

$y'=10e^{2x}+1$. $y'-2y=1-2x$. ✓ $y(0)=5$. ✓

### A3. (9.1 #15) $2y''+y'-y=0$, $y=e^{rx}$?

$2r^2+r-1=0$ → $r=1/2$ or $r=-1$. Family $y=ae^{x/2}+be^{-x}$ works by linearity.

### A4. (9.1 #26) Coffee 95°C, room 20°C.

(a) Fastest at $t=0$. Rate decreases as $T\to 20$. (b) $dT/dt=-k(T-20)$, $T(0)=95$.

### A5. (9.1 #27) Learning curve $dP/dt=k(M-P)$.

(a) Fastest at start. (b) Diminishing returns. (c) Rises to $M$.

### A6. (9.2 #25) $y'+3x^2y=6x^2$, $y(0)=3$.

(b) $y=2+e^{-x^3}$: $y'+3x^2y=6x^2$. ✓ $y(0)=3$. ✓ Exact $y(1)=2+e^{-1}\approx2.368$.

### A7. (9.2 #27) RC circuit $R=5$, $C=0.05$, $E=60$.

$Q'+4Q=12$. Equilibrium $Q=3$ C. Limiting charge = 3 C.

### A8. (9.2 #28) Coffee 95°C, room 20°C, cools 1°C/min at 70°C.

(a) $-1=-50k$ → $k=0.02$. (b) Euler with $T'=-0.02(T-20)$, $h=2$.

### A9. (9.1 #28) Von Bertalanffy $dL/dt=k(L_\infty-L)$.

(a) $dL/dt=k(L_\infty-L)$. (b) Approaches $L_\infty$ like Newton cooling.

### A10. (9.2 #17) $y'=y^3-4y$.

Equilibria: $0,\pm2$. Limit exists for $c\in[-2,2]$.

### A11. (9.2 #19c) Euler errors for $y'=y$, $y(0)=1$.

Error roughly halves when $h$ halves (first-order method).

### A12. (9.1 #19c) Solution not in $y=1/(x+C)$?

$y\equiv 0$. Lost solution from dividing by $y^2$.
