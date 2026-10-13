Show that the quadratic function that satisfies conditions (i), (ii), and (iii) is$$
P(x)=f(a)+f^{\prime}(a)(x-a)+\frac{1}{2} f^{\prime \prime}(a)(x-a)^{2}
$$
4. Find the quadratic approximation to $f(x)=\sqrt{x+3}$ near $a=1$. Graph $f$, the quadratic approximation, and the linear approximation from Example 3.10.2 on a common screen. What do you conclude?
5. Instead of being satisfied with a linear or quadratic approximation to $f(x)$ near $x=a$, let's try to find better approximations with higher-degree polynomials. We look for an $n$ th-degree polynomial
$$
T_{n}(x)=c_{0}+c_{1}(x-a)+c_{2}(x-a)^{2}+c_{3}(x-a)^{3}+\cdots+c_{n}(x-a)^{n}
$$
such that $T_{n}$ and its first $n$ derivatives have the same values at $x=a$ as $f$ and its first $n$ derivatives. By differentiating repeatedly and setting $x=a$, show that these conditions are satisfied if $c_{0}=f(a), c_{1}=f^{\prime}(a), c_{2}=\frac{1}{2} f^{\prime \prime}(a)$, and in general
$$
c_{k}=\frac{f^{(k)}(a)}{k!}
$$
where $k!=1 \cdot 2 \cdot 3 \cdot 4 \cdot \cdots \cdot k$. The resulting polynomial
$$
T_{n}(x)=f(a)+f^{\prime}(a)(x-a)+\frac{f^{\prime \prime}(a)}{2!}(x-a)^{2}+\cdots+\frac{f^{(n)}(a)}{n!}(x-a)^{n}
$$
is called the $\boldsymbol{n}$ th-degree Taylor polynomial of $\boldsymbol{f}$ centered at $\boldsymbol{a}$. (We will study Taylor polynomials in more detail in Chapter 11.)
6. Find the 8th-degree Taylor polynomial centered at $a=0$ for the function $f(x)=\cos x$. Graph $f$ together with the Taylor polynomials $T_{2}, T_{4}, T_{6}, T_{8}$ in the viewing rectangle [-5, 5] by [-1.4, 1.4] and comment on how well they approximate $f$.

### 3.11 Hyperbolic Functions

■ Hyperbolic Functions and Their Derivatives
Certain combinations of the exponential functions $e^{x}$ and $e^{-x}$ arise so frequently in mathematics and its applications that they deserve to be given special names. In many ways they are analogous to the trigonometric functions, and they have the same relationship to the hyperbola that the trigonometric functions have to the circle. For this reason they are collectively called hyperbolic functions and individually called hyperbolic sine, hyperbolic cosine, and so on.

Definition of the Hyperbolic Functions

$$
\begin{array}{ll}
\sinh x=\frac{e^{x}-e^{-x}}{2} & \operatorname{csch} x=\frac{1}{\sinh x} \\
\cosh x=\frac{e^{x}+e^{-x}}{2} & \operatorname{sech} x=\frac{1}{\cosh x} \\
\tanh x=\frac{\sinh x}{\cosh x} & \operatorname{coth} x=\frac{\cosh x}{\sinh x}
\end{array}
$$

![](https://cdn.mathpix.com/cropped/7c253dc4-acda-4600-96a4-6cafd187a142-0297.jpg?height=416&width=450&top_left_y=350&top_left_x=118)
FIGURE 1
$y=\sinh x=\frac{1}{2} e^{x}-\frac{1}{2} e^{-x}$

![](https://cdn.mathpix.com/cropped/7c253dc4-acda-4600-96a4-6cafd187a142-0297.jpg?height=273&width=482&top_left_y=1094&top_left_x=119)
FIGURE 4
A catenary $y=c+a \cosh (x / a)$

![](https://cdn.mathpix.com/cropped/7c253dc4-acda-4600-96a4-6cafd187a142-0297.jpg?height=192&width=520&top_left_y=1559&top_left_x=119)
FIGURE 5
Idealized water wave

The graphs of hyperbolic sine and hyperbolic cosine can be sketched using graphical addition as in Figures 1 and 2.

![](https://cdn.mathpix.com/cropped/7c253dc4-acda-4600-96a4-6cafd187a142-0297.jpg?height=407&width=486&top_left_y=353&top_left_x=710)
FIGURE 2
$y=\cosh x=\frac{1}{2} e^{x}+\frac{1}{2} e^{-x}$

![](https://cdn.mathpix.com/cropped/7c253dc4-acda-4600-96a4-6cafd187a142-0297.jpg?height=349&width=499&top_left_y=411&top_left_x=1378)
FIGURE 3
$y=\tanh x$

Note that sinh has domain $\mathbb{R}$ and range $\mathbb{R}$, whereas cosh has domain $\mathbb{R}$ and range $[1, \infty)$. The graph of tanh is shown in Figure 3. It has horizontal asymptotes $y= \pm 1$. (See Exercise 27.)

Some of the mathematical uses of hyperbolic functions will be seen in Chapter 7. Applications to science and engineering occur whenever an entity such as light, velocity, electricity, or radioactivity is gradually absorbed or extinguished because the decay can be represented by hyperbolic functions. The most famous application is the use of hyperbolic cosine to describe the shape of a hanging wire. It can be proved that if a heavy flexible cable (such as an overhead power line) is suspended between two points at the same height, then it takes the shape of a curve with equation

$$
y=c+a \cosh (x / a)
$$

called a catenary (see Figure 4). (The Latin word catena means "chain.")
Another application of hyperbolic functions occurs in the description of ocean waves: the velocity of a water wave with length $L$ moving across a body of water with depth $d$ is modeled by the function

$$
v=\sqrt{\frac{g L}{2 \pi} \tanh \left(\frac{2 \pi d}{L}\right)}
$$

where $g$ is the acceleration due to gravity (see Figure 5 and Exercise 57).
The hyperbolic functions satisfy a number of identities that are similar to well-known trigonometric identities. We list some of them here and leave most of the proofs to the exercises.

Hyperbolic Identities

$$
\begin{array}{lc}
\sinh (-x)=-\sinh x & \cosh (-x)=\cosh x \\
\cosh ^{2} x-\sinh ^{2} x=1 & 1-\tanh ^{2} x=\operatorname{sech}^{2} x \\
\sinh (x+y)=\sinh x \cosh y+\cosh x \sinh y \\
\cosh (x+y)=\cosh x \cosh y+\sinh x \sinh y
\end{array}
$$

![](https://cdn.mathpix.com/cropped/7c253dc4-acda-4600-96a4-6cafd187a142-0298.jpg?height=554&width=506&top_left_y=220&top_left_x=237)

The Gateway Arch in St. Louis was designed using a hyperbolic cosine function (see Exercise 56).

![](https://cdn.mathpix.com/cropped/7c253dc4-acda-4600-96a4-6cafd187a142-0298.jpg?height=369&width=445&top_left_y=1075&top_left_x=242)
FIGURE 6

![](https://cdn.mathpix.com/cropped/7c253dc4-acda-4600-96a4-6cafd187a142-0298.jpg?height=414&width=443&top_left_y=1540&top_left_x=243)
FIGURE 7

EXAMPLE 1 Prove (a) $\cosh ^{2} x-\sinh ^{2} x=1$ and (b) $1-\tanh ^{2} x=\operatorname{sech}^{2} x$. SOLUTION
(a)

$$
\begin{aligned}
\cosh ^{2} x-\sinh ^{2} x & =\left(\frac{e^{x}+e^{-x}}{2}\right)^{2}-\left(\frac{e^{x}-e^{-x}}{2}\right)^{2} \\
& =\frac{e^{2 x}+2+e^{-2 x}}{4}-\frac{e^{2 x}-2+e^{-2 x}}{4} \\
& =\frac{4}{4}=1
\end{aligned}
$$

(b) We start with the identity proved in part (a):

$$
\cosh ^{2} x-\sinh ^{2} x=1
$$

If we divide both sides by $\cosh ^{2} x$, we get
or $\square$

The identity proved in Example 1(a) gives a clue to the reason for the name "hyperbolic" functions:

If $t$ is any real number, then the point $P(\cos t, \sin t)$ lies on the unit circle $x^{2}+y^{2}=1$ because $\cos ^{2} t+\sin ^{2} t=1$. In fact, $t$ can be interpreted as the radian measure of $\angle P O Q$ in Figure 6. For this reason the trigonometric functions are sometimes called circular functions.

Likewise, if $t$ is any real number, then the point $P(\cosh t, \sinh t)$ lies on the right branch of the hyperbola $x^{2}-y^{2}=1$ because $\cosh ^{2} t-\sinh ^{2} t=1$ and $\cosh t \geqslant 1$. This time, $t$ does not represent the measure of an angle. However, it turns out that $t$ represents twice the area of the shaded hyperbolic sector in Figure 7, just as in the trigonometric case $t$ represents twice the area of the shaded circular sector in Figure 6.

The derivatives of the hyperbolic functions are easily computed. For example,

$$
\frac{d}{d x}(\sinh x)=\frac{d}{d x}\left(\frac{e^{x}-e^{-x}}{2}\right)=\frac{e^{x}+e^{-x}}{2}=\cosh x
$$

We list the differentiation formulas for the hyperbolic functions as Table 1. The remaining proofs are left as exercises. Note the analogy with the differentiation formulas for trigonometric functions, but note that the signs are different in some cases.

1 Derivatives of Hyperbolic Functions

$$
\begin{aligned}
\frac{d}{d x}(\sinh x) & =\cosh x & \frac{d}{d x}(\operatorname{csch} x) & =-\operatorname{csch} x \operatorname{coth} x \\
\frac{d}{d x}(\cosh x) & =\sinh x & \frac{d}{d x}(\operatorname{sech} x) & =-\operatorname{sech} x \tanh x \\
\frac{d}{d x}(\tanh x) & =\operatorname{sech}^{2} x & \frac{d}{d x}(\operatorname{coth} x) & =-\operatorname{csch}^{2} x
\end{aligned}
$$

Any of these differentiation rules can be combined with the Chain Rule, as in the next example.

EXAMPLE 2 If $y=\cosh \sqrt{x}$, find $d y / d x$.
SOLUTION Using (1) and the Chain Rule, we have

$$
\frac{d y}{d x}=\frac{d}{d x}(\cosh \sqrt{x})=\sinh \sqrt{x} \cdot \frac{d}{d x} \sqrt{x}=\frac{\sinh \sqrt{x}}{2 \sqrt{x}}
$$ $\square$

## ■ Inverse Hyperbolic Functions and Their Derivatives

You can see from Figures 1 and 3 that sinh and tanh are one-to-one functions and so they have inverse functions denoted by $\sinh ^{-1}$ and $\tanh ^{-1}$. Figure 2 shows that cosh is not one-to-one, but if we restrict the domain to the interval $[0, \infty)$, then the function $y=\cosh x$ is one-to-one and attains all the values in its range $[1, \infty)$. The inverse hyperbolic cosine function is defined as the inverse of this restricted function.

$$
\begin{align*}
& y=\sinh ^{-1} x \quad \Longleftrightarrow \quad \sinh y=x \\
& y=\cosh ^{-1} x \quad \Longleftrightarrow \cosh y=x \quad \text { and } \quad y \geqslant 0  \tag{2}\\
& y=\tanh ^{-1} x \quad \Longleftrightarrow \tanh y=x
\end{align*}
$$

The remaining inverse hyperbolic functions are defined similarly (see Exercise 32).
We sketch the graphs of $\sinh ^{-1}, \cosh ^{-1}$, and $\tanh ^{-1}$ in Figures 8, 9, and 10 by referring to Figures 1, 2, and 3.

![](https://cdn.mathpix.com/cropped/7c253dc4-acda-4600-96a4-6cafd187a142-0299.jpg?height=359&width=502&top_left_y=1315&top_left_x=161)
FIGURE $8 y=\sinh ^{-1} x$ domain $=\mathbb{R} \quad$ range $=\mathbb{R}$

![](https://cdn.mathpix.com/cropped/7c253dc4-acda-4600-96a4-6cafd187a142-0299.jpg?height=254&width=504&top_left_y=1367&top_left_x=806)
FIGURE $9 y=\cosh ^{-1} x$
domain $=[1, \infty)$ range $=[0, \infty)$

![](https://cdn.mathpix.com/cropped/7c253dc4-acda-4600-96a4-6cafd187a142-0299.jpg?height=358&width=385&top_left_y=1315&top_left_x=1451)
FIGURE $10 y=\tanh ^{-1} x$
domain $=(-1,1)$ range $=\mathbb{R}$

Since the hyperbolic functions are defined in terms of exponential functions, it's not surprising to learn that the inverse hyperbolic functions can be expressed in terms of logarithms. In particular, we have:

□ $$
\sinh ^{-1} x=\ln \left(x+\sqrt{x^{2}+1}\right) \quad x \in \mathbb{R}
$$
□
$$
\cosh ^{-1} x=\ln \left(x+\sqrt{x^{2}-1}\right) \quad x \geqslant 1
$$
□
$$
\tanh ^{-1} x=\frac{1}{2} \ln \left(\frac{1+x}{1-x}\right) \quad-1<x<1
$$

EXAMPLE 3 Show that $\sinh ^{-1} x=\ln \left(x+\sqrt{x^{2}+1}\right)$.
SOLUTION Let $y=\sinh ^{-1} x$. Then

$$
x=\sinh y=\frac{e^{y}-e^{-y}}{2}
$$

so

$$
e^{y}-2 x-e^{-y}=0
$$

or, multiplying by $e^{y}$,

$$
e^{2 y}-2 x e^{y}-1=0
$$

This is really a quadratic equation in $e^{y}$ :

$$
\left(e^{y}\right)^{2}-2 x\left(e^{y}\right)-1=0
$$

Solving by the quadratic formula, we get

$$
e^{y}=\frac{2 x \pm \sqrt{4 x^{2}+4}}{2}=x \pm \sqrt{x^{2}+1}
$$

Note that $e^{y}>0$, but $x-\sqrt{x^{2}+1}<0$ (because $x<\sqrt{x^{2}+1}$ ). Thus the minus sign is inadmissible and we have

$$
e^{y}=x+\sqrt{x^{2}+1}
$$

Therefore

$$
y=\ln \left(e^{y}\right)=\ln \left(x+\sqrt{x^{2}+1}\right)
$$

This shows that

$$
\sinh ^{-1} x=\ln \left(x+\sqrt{x^{2}+1}\right)
$$

(See Exercise 29 for another method.) $\square$
[6] Derivatives of Inverse Hyperbolic Functions

$$
\begin{aligned}
\frac{d}{d x}\left(\sinh ^{-1} x\right) & =\frac{1}{\sqrt{1+x^{2}}} & \frac{d}{d x}\left(\operatorname{csch}^{-1} x\right) & =-\frac{1}{|x| \sqrt{x^{2}+1}} \\
\frac{d}{d x}\left(\cosh ^{-1} x\right) & =\frac{1}{\sqrt{x^{2}-1}} & \frac{d}{d x}\left(\operatorname{sech}^{-1} x\right) & =-\frac{1}{x \sqrt{1-x^{2}}} \\
\frac{d}{d x}\left(\tanh ^{-1} x\right) & =\frac{1}{1-x^{2}} & \frac{d}{d x}\left(\operatorname{coth}^{-1} x\right) & =\frac{1}{1-x^{2}}
\end{aligned}
$$

The inverse hyperbolic functions are all differentiable because the hyperbolic functions are differentiable (see Appendix F). The formulas in Table 6 can be proved either by the method for inverse functions or by differentiating Formulas 3, 4, and 5.

EXAMPLE 4 Prove that $\frac{d}{d x}\left(\sinh ^{-1} x\right)=\frac{1}{\sqrt{1+x^{2}}}$.
SOLUTION 1 Let $y=\sinh ^{-1} x$. Then $\sinh y=x$. If we differentiate this equation implicitly with respect to $x$, we get

$$
\cosh y \frac{d y}{d x}=1
$$

Since $\cosh ^{2} y-\sinh ^{2} y=1$ and $\cosh y \geqslant 0$, we have $\cosh y=\sqrt{1+\sinh ^{2} y}$, so

$$
\frac{d y}{d x}=\frac{1}{\cosh y}=\frac{1}{\sqrt{1+\sinh ^{2} y}}=\frac{1}{\sqrt{1+x^{2}}}
$$

SOLUTION 2 From Equation 3 (proved in Example 3), we have

$$
\begin{aligned}
\frac{d}{d x}\left(\sinh ^{-1} x\right) & =\frac{d}{d x} \ln \left(x+\sqrt{x^{2}+1}\right) \\
& =\frac{1}{x+\sqrt{x^{2}+1}} \frac{d}{d x}\left(x+\sqrt{x^{2}+1}\right) \\
& =\frac{1}{x+\sqrt{x^{2}+1}}\left(1+\frac{x}{\sqrt{x^{2}+1}}\right) \\
& =\frac{\sqrt{x^{2}+1}+x}{\left(x+\sqrt{x^{2}+1}\right) \sqrt{x^{2}+1}} \\
& =\frac{1}{\sqrt{x^{2}+1}}
\end{aligned}
$$ $\square$

EXAMPLE 5 Find $\frac{d}{d x}\left[\tanh ^{-1}(\sin x)\right]$.
SOLUTION Using Table 6 and the Chain Rule, we have

$$
\begin{aligned}
\frac{d}{d x}\left[\tanh ^{-1}(\sin x)\right] & =\frac{1}{1-(\sin x)^{2}} \frac{d}{d x}(\sin x) \\
& =\frac{1}{1-\sin ^{2} x} \cos x=\frac{\cos x}{\cos ^{2} x}=\sec x
\end{aligned}
$$ $\square$

### 3.11 | Exercises

1-6 Find the numerical value of each expression.

1. (a) $\sinh 0$
(b) $\cosh 0$
2. (a) $\tanh 0$
(b) $\tanh 1$
3. (a) $\cosh (\ln 5)$
(b) $\cosh 5$
4. (a) $\sinh 4$
(b) $\sinh (\ln 4)$
5. (a) $\operatorname{sech} 0$
(b) $\cosh ^{-1} 1$
6. (a) $\sinh 1$
(b) $\sinh ^{-1} 1$
7. Write $8 \sinh x+5 \cosh x$ in terms of $e^{x}$ and $e^{-x}$.
8. Write $2 e^{2 x}+3 e^{-2 x}$ in terms of $\sinh 2 x$ and $\cosh 2 x$.
9. Write $\sinh (\ln x)$ as a rational function of $x$.
10. Write $\cosh (4 \ln x)$ as a rational function of $x$.
11-23 Prove the identity.
11. $\sinh (-x)=-\sinh x$
(This shows that sinh is an odd function.)
12. $\cosh (-x)=\cosh x$
(This shows that cosh is an even function.)
13. $\cosh x+\sinh x=e^{x}$
14. $\cosh x-\sinh x=e^{-x}$
15. $\sinh (x+y)=\sinh x \cosh y+\cosh x \sinh y$
16. $\cosh (x+y)=\cosh x \cosh y+\sinh x \sinh y$

17. $\operatorname{coth}^{2} x-1=\operatorname{csch}^{2} x$
18. $\tanh (x+y)=\frac{\tanh x+\tanh y}{1+\tanh x \tanh y}$
19. $\sinh 2 x=2 \sinh x \cosh x$
20. $\cosh 2 x=\cosh ^{2} x+\sinh ^{2} x$
21. $\tanh (\ln x)=\frac{x^{2}-1}{x^{2}+1}$
22. $\frac{1+\tanh x}{1-\tanh x}=e^{2 x}$
23. $(\cosh x+\sinh x)^{n}=\cosh n x+\sinh n x$ ( $n$ any real number)
24. If $\tanh x=\frac{12}{13}$, find the values of the other hyperbolic functions at $x$.
25. If $\cosh x=\frac{5}{3}$ and $x>0$, find the values of the other hyperbolic functions at $x$.
26. (a) Use the graphs of sinh, cosh, and tanh in Figures 1-3 to draw the graphs of csch, sech, and coth.
    (b) Check the graphs that you sketched in part (a) by using a graphing calculator or computer to produce them.
27. Use the definitions of the hyperbolic functions to find each of the following limits.
(a) $\lim _{x \rightarrow \infty} \tanh x$
(b) $\lim _{x \rightarrow-\infty} \tanh x$
(c) $\lim _{x \rightarrow \infty} \sinh x$
(d) $\lim _{x \rightarrow-\infty} \sinh x$
(e) $\lim _{x \rightarrow \infty} \operatorname{sech} x$
(f) $\lim _{x \rightarrow \infty} \operatorname{coth} x$
(g) $\lim _{x \rightarrow 0^{+}} \operatorname{coth} x$
(h) $\lim _{x \rightarrow 0^{-}} \operatorname{coth} x$
(i) $\lim _{x \rightarrow-\infty} \operatorname{csch} x$
(j) $\lim _{x \rightarrow \infty} \frac{\sinh x}{e^{x}}$
28. Prove the formulas given in Table 1 for the derivatives of the functions (a) cosh, (b) tanh, (c) csch, (d) sech, and (e) coth.
29. Give an alternative solution to Example 3 by letting $y=\sinh ^{-1} x$ and then using Exercise 13 and Example 1(a) with $x$ replaced by $y$.
30. Prove Equation 4.
31. Prove Equation 5 using (a) the method of Example 3 and (b) Exercise 22 with $x$ replaced by $y$.
32. For each of the following functions (i) give a definition like those in (2), (ii) sketch the graph, and (iii) find a formula similar to Equation 3.
(a) $\mathrm{csch}^{-1}$
(b) $\mathrm{sech}^{-1}$
(c) $\operatorname{coth}^{-1}$
33. Prove the formula given in Table 6 for the derivative of each of the following functions.
(a) $\cosh ^{-1}$
(b) $\tanh ^{-1}$
(c) $\operatorname{coth}^{-1}$
34. Prove the formula given in Table 6 for the derivative of each of the following functions.
(a) $\mathrm{sech}^{-1}$
(b) $\mathrm{csch}^{-1}$
35-53 Find the derivative. Simplify where possible.
35. $f(x)=\cosh 3 x$
36. $f(x)=e^{x} \cosh x$
37. $h(x)=\sinh \left(x^{2}\right)$
38. $g(x)=\sinh ^{2} x$
39. $G(t)=\sinh (\ln t)$
40. $F(t)=\ln (\sinh t)$
41. $f(x)=\tanh \sqrt{x}$
42. $H(v)=e^{\tanh 2 v}$
43. $y=\operatorname{sech} x \tanh x$
44. $y=\operatorname{sech}(\tanh x)$
45. $g(t)=t \operatorname{coth} \sqrt{t^{2}+1}$
46. $f(t)=\frac{1+\sinh t}{1-\sinh t}$
47. $f(x)=\sinh ^{-1}(-2 x)$
48. $g(x)=\tanh ^{-1}\left(x^{3}\right)$
49. $y=\cosh ^{-1}(\sec \theta), \quad 0 \leqslant \theta<\pi / 2$
50. $y=\operatorname{sech}^{-1}(\sin \theta), \quad 0<\theta<\pi / 2$
51. $G(u)=\cosh ^{-1} \sqrt{1+u^{2}}, \quad u>0$
52. $y=x \tanh ^{-1} x+\ln \sqrt{1-x^{2}}$
53. $y=x \sinh ^{-1}(x / 3)-\sqrt{9+x^{2}}$
54. Show that $\frac{d}{d x} \sqrt[4]{\frac{1+\tanh x}{1-\tanh x}}=\frac{1}{2} e^{x / 2}$.
55. Show that $\frac{d}{d x} \arctan (\tanh x)=\operatorname{sech} 2 x$.
56. The Gateway Arch The Gateway Arch in St. Louis was designed by Eero Saarinen and was constructed using the equation
$$
y=211.49-20.96 \cosh 0.03291765 x
$$
for the central curve of the arch, where $x$ and $y$ are measured in meters and $|x| \leqslant 91.20$.
    (a) Graph the central curve.
    (b) What is the height of the arch at its center?
    (c) At what points is the height 100 m?
    (d) What is the slope of the arch at the points in part (c)?

57. If a water wave with length $L$ moves with velocity $v$ in a body of water with depth $d$, then
$$
v=\sqrt{\frac{g L}{2 \pi} \tanh \left(\frac{2 \pi d}{L}\right)}
$$
where $g$ is the acceleration due to gravity. (See Figure 5.) Explain why the approximation
$$
v \approx \sqrt{\frac{g L}{2 \pi}}
$$
is appropriate in deep water.
58. A flexible cable always hangs in the shape of a catenary $y=c+a \cosh (x / a)$, where $c$ and $a$ are constants and $a>0$ (see Figure 4 and Exercise 60). Graph several members of the family of functions $y=a \cosh (x / a)$. How does the graph change as $a$ varies?
59. A telephone line hangs between two poles 14 m apart in the shape of the catenary $y=20 \cosh (x / 20)-15$, where $x$ and $y$ are measured in meters.
    (a) Find the slope of this curve where it meets the right-hand pole.
    (b) Find the angle $\theta$ between the line and the pole.
![](https://cdn.mathpix.com/cropped/7c253dc4-acda-4600-96a4-6cafd187a142-0303.jpg?height=270&width=492&top_left_y=1283&top_left_x=327)
60. Using principles from physics it can be shown that when a cable is hung between two poles, it takes the shape of a curve $y=f(x)$ that satisfies the differential equation
$$
\frac{d^{2} y}{d x^{2}}=\frac{\rho g}{T} \sqrt{1+\left(\frac{d y}{d x}\right)^{2}}
$$
where $\rho$ is the linear density of the cable, $g$ is the acceleration due to gravity, $T$ is the tension in the cable at its lowest point, and the coordinate system is chosen appropriately. Verify that the function
$$
y=f(x)=\frac{T}{\rho g} \cosh \left(\frac{\rho g x}{T}\right)
$$
is a solution of this differential equation.
61. A cable with linear density $\rho=2 \mathrm{~kg} / \mathrm{m}$ is strung from the tops of two poles that are 200 m apart.
    (a) Use Exercise 60 to find the tension $T$ so that the cable is 60 m above the ground at its lowest point. How tall are the poles?
    (b) If the tension is doubled, what is the new low point of the cable? How tall are the poles now?
62. A model for the velocity of a falling object after time $t$ is
$$
v(t)=\sqrt{\frac{m g}{k}} \tanh \left(t \sqrt{\frac{g k}{m}}\right)
$$
where $m$ is the mass of the object, $g=9.8 \mathrm{~m} / \mathrm{s}^{2}$ is the acceleration due to gravity, $k$ is a constant, $t$ is measured in seconds, and $v$ in m/s.
    (a) Calculate the terminal velocity of the object, that is, $\lim _{t \rightarrow \infty} v(t)$.
    (b) If a person skydives from a plane, the value of the constant $k$ depends on his or her position. For a "belly-to-earth" position, $k=0.515 \mathrm{~kg} / \mathrm{s}$, but for a "feet-first" position, $k=0.067 \mathrm{~kg} / \mathrm{s}$. If a 60-kg person descends in belly-to-earth position, what is the terminal velocity? What about feet-first?
Source: L. Long et al., "How Terminal Is Terminal Velocity?" American Mathematical Monthly 113 (2006): 752-55.
63. (a) Show that any function of the form
$$
y=A \sinh m x+B \cosh m x
$$
satisfies the differential equation $y^{\prime \prime}=m^{2} y$.
    (b) Find $y=y(x)$ such that $y^{\prime \prime}=9 y, y(0)=-4$, and $y^{\prime}(0)=6$.
64. If $x=\ln (\sec \theta+\tan \theta)$, show that $\sec \theta=\cosh x$.
65. At what point of the curve $y=\cosh x$ does the tangent have slope 1?
66. Investigate the family of functions

$$
f_{n}(x)=\tanh (n \sin x)
$$

where $n$ is a positive integer. Describe what happens to the graph of $f_{n}$ when $n$ becomes large.

67. Show that if $a \neq 0$ and $b \neq 0$, then there exist numbers $\alpha$ and $\beta$ such that $a e^{x}+b e^{-x}$ equals either
$$
\alpha \sinh (x+\beta) \quad \text { or } \quad \alpha \cosh (x+\beta)
$$
In other words, almost every function of the form $f(x)=a e^{x}+b e^{-x}$ is a shifted and stretched hyperbolic sine or hyperbolic cosine function.
