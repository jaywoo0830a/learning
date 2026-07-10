# Session 03 — Solutions

## 🔧 Basic Drills

**1.** $v_{0y}=30\sin 60^\circ=15\sqrt{3}\approx 26.0$. $t_f=2\cdot 15\sqrt{3}/10 = 3\sqrt{3}\approx 5.20\text{ s}$. $R=30\cos 60^\circ\cdot 3\sqrt{3}=15\cdot 3\sqrt{3}=45\sqrt{3}\approx 77.9\text{ m}$. $y_{\text{max}}=(15\sqrt{3})^2/20=675/20=33.75\text{ m}$.

**2.** $80 = 5t^2 \Rightarrow t=4\text{ s}$. $x=25\cdot 4=100\text{ m}$.

**3.** $\theta=45^\circ$: $R=400/10=40\text{ m}$. $\theta=30^\circ$: $v_{0y}=10$, $t_f=2$, $R=20\cos 30^\circ\cdot 2=20\sqrt{3}\approx 34.6\text{ m}$. $45^\circ$ goes farther.

**4.** $y=40t-5t^2=5t(8-t)=0$ at $t=0$ (launch) and $t=8$ (landing). Flight time is $8\text{ s}$.

**5.** $v_{0x}=10$, $v_{0y}=20$. $|\vec{v}_0|=\sqrt{100+400}=\sqrt{500}\approx 22.4\text{ m/s}$. $\tan\theta=20/10=2 \Rightarrow \theta\approx 63.4^\circ$.

---

## 🔥 Advanced Drills

**1.** $R = v_0^2\sin 2\theta/g$, $H = v_0^2\sin^2\theta/(2g)$. At $\theta=45^\circ$: $R=v_0^2/g$, $H=v_0^2/(4g)$. Ratio $R/H=4$. In general: $R/H = 4\cot\theta$ (not always 4; the statement holds at $45^\circ$).

**2.** $\sin 2\theta = \sin(180^\circ-2\theta)$, so angles $\theta$ and $90^\circ-\theta$ give the same $\sin 2\theta$, hence the same range.

**3.** Compare $y = x - \frac{1}{20}x^2$ to $y = x\tan\theta - \frac{g}{2v_0^2\cos^2\theta}x^2$. $\tan\theta=1 \Rightarrow \theta=45^\circ$. $\frac{g}{2v_0^2\cos^2\theta}=\frac{1}{20} \Rightarrow \frac{10}{2v_0^2\cdot\frac{1}{2}}=\frac{1}{20} \Rightarrow \frac{10}{v_0^2}=\frac{1}{20} \Rightarrow v_0^2=200 \Rightarrow v_0=10\sqrt{2}\approx 14.1\text{ m/s}$.

**4.** $\theta=90^\circ$ means the ball is thrown straight up. It comes straight back down — zero horizontal displacement. The formula gives 0 because $\sin 180^\circ=0$. Physically, it never "ranges" anywhere.

**5.** Intersection: $y_{\text{proj}} = -\frac{g}{2v_0^2}x^2$ (horizontal launch, so $\theta=0$). $y_{\text{incline}} = -x\tan\alpha$. Set equal: $-\frac{g}{2v_0^2}x^2 = -x\tan\alpha \Rightarrow x=0$ or $x = \frac{2v_0^2\tan\alpha}{g}$. Flight time: $t = x/v_0 = \frac{2v_0\tan\alpha}{g}$.

---

## 🧠 Intuitional Drills

**1.** $60^\circ$ ball: larger $v_{0y}$, so longer flight time and higher peak. But $\sin(2\cdot 60^\circ)=\sin 120^\circ=\sin 60^\circ$ and $\sin(2\cdot 30^\circ)=\sin 60^\circ$ — same range. This is the complementary-angle property.

**2.** $R=v_0^2\sin 2\theta/g$, $t_f=2v_0\sin\theta/g$. If $g\to 2g$, both $R$ and $t_f$ are halved. The trajectory is identical in shape but compressed horizontally and temporally.

**3.** At $t=t_f/2 = v_0\sin\theta/g$, horizontal distance $x = v_0\cos\theta\cdot v_0\sin\theta/g = v_0^2\sin\theta\cos\theta/g$. Total range $R = 2v_0^2\sin\theta\cos\theta/g$. Ratio: $x/R = 1/2$ — exactly halfway.

**4.** When launch and landing heights differ, the optimal angle $\theta_{\text{opt}} = 45^\circ - \frac{1}{2}\tan^{-1}\!\left(\frac{\Delta y}{R}\right)$ approximately. Here the hoop is $1\text{ m}$ higher than release, $5\text{ m}$ away, so $\theta_{\text{opt}} < 45^\circ$. Exact: about $41^\circ$.

**5.** $R \propto 1/g$. $g_{\text{moon}} = g/6$, so $R_{\text{moon}} = 6R_{\text{earth}}$.
