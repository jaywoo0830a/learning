### 2.1 The Tangent and Velocity Problems

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0113.jpg?height=624&width=478&top_left_y=341&top_left_x=118)
FIGURE 1

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0113.jpg?height=337&width=446&top_left_y=1081&top_left_x=118)
FIGURE 2

| $x$ | $m_{P Q}$ |
| :--- | :--- |
| 2 | 3 |
| 1.5 | 2.5 |
| 1.1 | 2.1 |
| 1.01 | 2.01 |
| 1.001 | 2.001 |


| $x$ | $m_{P Q}$ |
| :--- | :--- |
| 0 | 1 |
| 0.5 | 1.5 |
| 0.9 | 1.9 |
| 0.99 | 1.99 |
| 0.999 | 1.999 |

In this section we see how limits arise when we attempt to find the tangent to a curve or the velocity of an object.

## ■ The Tangent Problem

The word tangent is derived from the Latin word tangens, which means "touching." We can think of a tangent to a curve as a line that touches the curve and follows the same direction as the curve at the point of contact. How can this idea be made precise?

For a circle we could simply follow Euclid and say that a tangent is a line $\ell$ that intersects the circle once and only once, as in Figure 1(a). For more complicated curves this definition is inadequate. Figure 1(b) shows a line $\ell$ that appears to be a tangent to the curve $C$ at point $P$, but it intersects $C$ twice.

To be specific, let's look at the problem of trying to find a tangent line $\ell$ to the parabola $y=x^{2}$ in the following example.

EXAMPLE 1 Find an equation of the tangent line to the parabola $y=x^{2}$ at the point $P(1,1)$.

SOLUTION We will be able to find an equation of the tangent line $\ell$ as soon as we know its slope $m$. The difficulty is that we know only one point, $P$, on $\ell$, whereas we need two points to compute the slope. But observe that we can compute an approximation to $m$ by choosing a nearby point $Q\left(x, x^{2}\right)$ on the parabola (as in Figure 2) and computing the slope $m_{P Q}$ of the secant line $P Q$. (A secant line, from the Latin word secans, meaning cutting, is a line that cuts [intersects] a curve more than once.)

We choose $x \neq 1$ so that $Q \neq P$. Then

$$
m_{P Q}=\frac{x^{2}-1}{x-1}
$$

For instance, for the point $Q(1.5,2.25)$ we have

$$
m_{P Q}=\frac{2.25-1}{1.5-1}=\frac{1.25}{0.5}=2.5
$$

The tables in the margin show the values of $m_{P Q}$ for several values of $x$ close to 1 . The closer $Q$ is to $P$, the closer $x$ is to 1 and, it appears from the tables, the closer $m_{P Q}$ is to 2 . This suggests that the slope of the tangent line $\ell$ should be $m=2$.

We say that the slope of the tangent line is the limit of the slopes of the secant lines, and we express this symbolically by writing

$$
\lim _{Q \rightarrow P} m_{P Q}=m \quad \text { and } \quad \lim _{x \rightarrow 1} \frac{x^{2}-1}{x-1}=2
$$

Assuming that the slope of the tangent line is indeed 2, we use the point-slope form of the equation of a line $\left[y-y_{1}=m\left(x-x_{1}\right)\right.$, see Appendix B] to write the equation of the tangent line through $(1,1)$ as

$$
y-1=2(x-1) \quad \text { or } \quad y=2 x-1
$$ $\square$

Figure 3 illustrates the limiting process that occurs in Example 1. As $Q$ approaches $P$ along the parabola, the corresponding secant lines rotate about $P$ and approach the tangent line $\ell$.

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0114.jpg?height=832&width=488&top_left_y=387&top_left_x=250)
FIGURE 3

| $t$ | $Q$ |
| :--- | :--- |
| 0 | 10 |
| 0.02 | 8.187 |
| 0.04 | 6.703 |
| 0.06 | 5.488 |
| 0.08 | 4.493 |
| 0.1 | 3.676 |

Many functions that occur in the sciences are not described by explicit equations; they are defined by experimental data. The next example shows how to estimate the slope of the tangent line to the graph of such a function.

EXAMPLE 2 A pulse laser operates by storing charge on a capacitor and releasing it suddenly when the laser is fired. The data in the table describe the charge $Q$ remaining on the capacitor (measured in coulombs) at time $t$ (measured in seconds after the laser is fired). Use the data to draw the graph of this function and estimate the slope of the tangent line at the point where $t=0.04$. (Note: The slope of the tangent line represents the electric current flowing from the capacitor to the laser [measured in amperes].)

SOLUTION In Figure 4 we plot the given data and use these points to sketch a curve that approximates the graph of the function.

FIGURE 4
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0114.jpg?height=442&width=776&top_left_y=1897&top_left_x=1003)

| $R$ | $m_{P R}$ |
| :--- | :--- |
| $(0,10)$ | -82.425 |
| (0.02, 8.187) | -74.200 |
| (0.06, 5.488) | -60.750 |
| (0.08, 4.493) | -55.250 |
| (0.1, 3.676) | -50.450 |

Given the points $P(0.04,6.703)$ and $R(0,10)$ on the graph, we find that the slope of the secant line $P R$ is

$$
m_{P R}=\frac{10-6.703}{0-0.04}=-82.425
$$

The table at the left shows the results of similar calculations for the slopes of other secant lines. From this table we would expect the slope of the tangent line at $t=0.04$ to lie somewhere between -74.20 and -60.75. In fact, the average of the slopes of the two closest secant lines is

$$
\frac{1}{2}(-74.20-60.75)=-67.475
$$

So, by this method, we estimate the slope of the tangent line to be about -67.5.
Another method is to draw an approximation to the tangent line at $P$ and measure the sides of the triangle $A B C$, as in Figure 5.

FIGURE 5
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0115.jpg?height=440&width=836&top_left_y=908&top_left_x=849)

This gives an estimate of the slope of the tangent line as

$$
-\frac{|A B|}{|B C|} \approx-\frac{8.0-5.4}{0.06-0.02}=-65.0
$$ $\square$

## ■ The Velocity Problem

If you watch the speedometer of a car as you drive in city traffic, you see that the speed doesn't stay the same for very long; that is, the velocity of the car is not constant. We assume from watching the speedometer that the car has a definite velocity at each moment, but how is the "instantaneous" velocity defined?

Let's consider the velocity problem: Find the instantaneous velocity of an object moving along a straight path at a specific time if the position of the object at any time is known. In the next example, we investigate the velocity of a falling ball. Through experiments carried out four centuries ago, Galileo discovered that the distance fallen by any freely falling body is proportional to the square of the time it has been falling. (This model for free fall neglects air resistance.) If the distance fallen after $t$ seconds is denoted by $s(t)$ and measured in meters, then (at the earth's surface) Galileo's observation is expressed by the equation

$$
s(t)=4.9 t^{2}
$$

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0116.jpg?height=1983&width=535&top_left_y=218&top_left_x=217)
FIGURE 6

XAMPLE 3 Suppose that a ball is dropped from the upper observation deck of he CN Tower in Toronto, 450 m above the ground. Find the velocity of the ball after seconds.

OLUTION The difficulty in finding the instantaneous velocity at 5 seconds is that e are dealing with a single instant of time $(t=5)$, so no time interval is involved. owever, we can approximate the desired quantity by computing the average velocity ver the brief time interval of a tenth of a second from $t=5$ to $t=5.1$ :

$$
\begin{aligned}
\text { average velocity } & =\frac{\text { change in position }}{\text { time elapsed }} \\
& =\frac{s(5.1)-s(5)}{0.1} \\
& =\frac{4.9(5.1)^{2}-4.9(5)^{2}}{0.1}=49.49 \mathrm{~m} / \mathrm{s}
\end{aligned}
$$

he following table shows the results of similar calculations of the average velocity over successively smaller time periods.

| Time interval | Average velocity (m/s) |
| :--- | :--- |
| $5 \leqslant t \leqslant 5.1$ | 49.49 |
| $5 \leqslant t \leqslant 5.05$ | 49.245 |
| $5 \leqslant t \leqslant 5.01$ | 49.049 |
| $5 \leqslant t \leqslant 5.001$ | 49.0049 |

It appears that as we shorten the time period, the average velocity is becoming closer to $49 \mathrm{~m} / \mathrm{s}$. The instantaneous velocity when $t=5$ is defined to be the limiting value of these average velocities over shorter and shorter time periods that start at $t=5$. Thus it appears that the (instantaneous) velocity after 5 seconds is 49 m/s. $\square$

You may have the feeling that the calculations used in solving this problem are very similar to those used earlier in this section to find tangents. In fact, there is a close connection between the tangent problem and the velocity problem. If we draw the graph of the distance function of the ball (as in Figure 6) and we consider the points $P\left(5,4.9(5)^{2}\right.$ ) and $Q\left(5+h, 4.9(5+h)^{2}\right)$ on the graph, then the slope of the secant line $P Q$ is

$$
m_{P Q}=\frac{4.9(5+h)^{2}-4.9(5)^{2}}{(5+h)-5}
$$

which is the same as the average velocity over the time interval [5, 5+ h]. Therefore the velocity at time $t=5$ (the limit of these average velocities as $h$ approaches 0) must be equal to the slope of the tangent line at $P$ (the limit of the slopes of the secant lines).

Examples 1 and 3 show that in order to solve tangent and velocity problems we must be able to find limits. After studying methods for computing limits in the next five sections, we will return to the problems of finding tangents and velocities in Section 2.7.

### 2.1 Exercises

1. A tank holds 1000 liters of water, which drains from the bottom of the tank in half an hour. The values in the table show the volume $V$ of water remaining in the tank (in liters) after $t$ minutes.

| $t(\mathrm{~min})$ | 5 | 10 | 15 | 20 | 25 | 30 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $V(\mathrm{~L})$ | 694 | 444 | 250 | 111 | 28 | 0 |


    (a) If $P$ is the point $(15,250)$ on the graph of $V$, find the slopes of the secant lines $P Q$ when $Q$ is the point on the graph with $t=5,10,20,25$, and 30.
    (b) Estimate the slope of the tangent line at $P$ by averaging the slopes of two secant lines.
    (c) Use a graph of $V$ to estimate the slope of the tangent line at $P$. (This slope represents the rate at which the water is flowing from the tank after 15 minutes.)
2. A student bought a smartwatch that tracks the number of steps she walks throughout the day. The table shows the number of steps recorded $t$ minutes after 3:00 pm on the first day she wore the watch.

| $t(\mathrm{~min})$ | 0 | 10 | 20 | 30 | 40 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Steps | 3438 | 4559 | 5622 | 6536 | 7398 |


    (a) Find the slopes of the secant lines corresponding to the given intervals of $t$. What do these slopes represent?
(i) [0, 40]
(ii) [10, 20]
(iii) [20, 30]
    (b) Estimate the student's walking pace, in steps per minute, at 3:20 pm by averaging the slopes of two secant lines.
3. The point $P(2,-1)$ lies on the curve $y=1 /(1-x)$.
    (a) If $Q$ is the point $(x, 1 /(1-x))$, find the slope of the secant line $P Q$ (correct to six decimal places) for the following values of $x$ :
(i) 1.5
(ii) 1.9
(iii) 1.99
(iv) 1.999
(v) 2.5
(vi) 2.1
(vii) 2.01
(viii) 2.001
    (b) Using the results of part (a), guess the value of the slope of the tangent line to the curve at $P(2,-1)$.
    (c) Using the slope from part (b), find an equation of the tangent line to the curve at $P(2,-1)$.
4. The point $P(0.5,0)$ lies on the curve $y=\cos \pi x$.
    (a) If $Q$ is the point $(x, \cos \pi x)$, find the slope of the secant line $P Q$ (correct to six decimal places) for the following values of $x$ :
(i) 0
(ii) 0.4
(iii) 0.49
(iv) 0.499
(v) 1
(vi) 0.6
(vii) 0.51
(viii) 0.501
    (b) Using the results of part (a), guess the value of the slope of the tangent line to the curve at $P(0.5,0)$.

        (c) Using the slope from part (b), find an equation of the tangent line to the curve at $P(0.5,0)$.
        (d) Sketch the curve, two of the secant lines, and the tangent line.
5. The deck of a bridge is suspended 80 meters above a river. If a pebble falls off the side of the bridge, the height, in meters, of the pebble above the water surface after $t$ seconds is given by $y=80-4.9 t^{2}$.

        (a) Find the average velocity of the pebble for the time period beginning when $t=4$ and lasting
(i) 0.1 seconds
(ii) 0.05 seconds
(iii) 0.01 seconds
        (b) Estimate the instantaneous velocity of the pebble after 4 seconds.
6. If a rock is thrown upward on the planet Mars with a velocity of 10 m/s, its height in meters $t$ seconds later is given by $y=10 t-1.86 t^{2}$.

        (a) Find the average velocity over the given time intervals:
(i) [1, 2]
(ii) [1, 1.5]
(iii) [1, 1.1]
(iv) [1, 1.01]
(v) [1, 1.001]
        (b) Estimate the instantaneous velocity when $t=1$.
        7. The table shows the position of a motorcyclist after accelerating from rest.

| $t$ (seconds) | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $s$ (meters) | 0 | 1.5 | 6.3 | 14.2 | 24.1 | 38.0 | 53.9 |


            (a) Find the average velocity for each time period:
(i) [2, 4]
(ii) [3, 4]
(iii) [4, 5]
(iv) [4, 6]
            (b) Use the graph of $s$ as a function of $t$ to estimate the instantaneous velocity when $t=3$.
        8. The displacement (in centimeters) of a particle moving back and forth along a straight line is given by the equation of motion $s=2 \sin \pi t+3 \cos \pi t$, where $t$ is measured in seconds.
            (a) Find the average velocity during each time period:
(i) [1, 2]
(ii) [1, 1.1]
(iii) [1, 1.01]
(iv) [1, 1.001]
            (b) Estimate the instantaneous velocity of the particle when $t=1$.
        9. The point $P(1,0)$ lies on the curve $y=\sin (10 \pi / x)$.
            (a) If $Q$ is the point $(x, \sin (10 \pi / x))$, find the slope of the secant line $P Q$ (correct to four decimal places) for $x=2$, 1.5, 1.4, 1.3, 1.2, 1.1, 0.5, 0.6, 0.7, 0.8, and 0.9. Do the slopes appear to be approaching a limit?
            (b) Use a graph of the curve to explain why the slopes of the secant lines in part (a) are not close to the slope of the tangent line at $P$.
            (c) By choosing appropriate secant lines, estimate the slope of the tangent line at $P$.

### 2.2 The Limit of a Function

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0118.jpg?height=493&width=516&top_left_y=1018&top_left_x=241)
FIGURE 1

Having seen in the preceding section how limits arise when we want to find the tangent to a curve or the velocity of an object, we now turn our attention to limits in general and numerical and graphical methods for computing them.

## ■ Finding Limits Numerically and Graphically

Let's investigate the behavior of the function $f$ defined by $f(x)=(x-1) /\left(x^{2}-1\right)$ for values of $x$ near 1. The following table gives values of $f(x)$ for values of $x$ close to 1 but not equal to 1 .
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0118.jpg?height=466&width=738&top_left_y=717&top_left_x=1021)

From the table and the graph of $f$ shown in Figure 1 we see that the closer $x$ is to 1 (on either side of 1 ), the closer $f(x)$ is to 0.5 . In fact, it appears that we can make the values of $f(x)$ as close as we like to 0.5 by taking $x$ sufficiently close to 1 . We express this by saying "the limit of the function $f(x)=(x-1) /\left(x^{2}-1\right)$ as $x$ approaches 1 is equal to 0.5." The notation for this is

$$
\lim _{x \rightarrow 1} \frac{x-1}{x^{2}-1}=0.5
$$

In general, we use the following notation.

1 Intuitive Definition of a Limit Suppose $f(x)$ is defined when $x$ is near the number $a$. (This means that $f$ is defined on some open interval that contains $a$, except possibly at $a$ itself.) Then we write

$$
\lim _{x \rightarrow a} f(x)=L
$$

and say "the limit of $f(x)$, as $x$ approaches $a$, equals $L$ "
if we can make the values of $f(x)$ arbitrarily close to $L$ (as close to $L$ as we like) by restricting $x$ to be sufficiently close to $a$ (on either side of $a$ ) but not equal to $a$.

Roughly speaking, this says that the values of $f(x)$ approach $L$ as $x$ approaches $a$. In other words, the values of $f(x)$ tend to get closer and closer to the number $L$ as $x$ gets closer and closer to the number $a$ (from either side of $a$ ) but $x \neq a$. (A more precise definition will be given in Section 2.4.)

An alternative notation for

$$
\lim _{x \rightarrow a} f(x)=L
$$

is

$$
f(x) \rightarrow L \quad \text { as } \quad x \rightarrow a
$$

which is usually read " $f(x)$ approaches $L$ as $x$ approaches $a$."
Notice the phrase "but $x$ not equal to $a$ " in the definition of limit. This means that in finding the limit of $f(x)$ as $x$ approaches $a$, we never consider $x=a$. In fact, $f(x)$ need not even be defined when $x=a$. The only thing that matters is how $f$ is defined near $a$.

Figure 2 shows the graphs of three functions. Note that in part (b), $f(a)$ is not defined and in part (c), $f(a) \neq L$. But in each case, regardless of what happens at $a$, it is true that $\lim _{x \rightarrow a} f(x)=L$.

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0119.jpg?height=435&width=1731&top_left_y=724&top_left_x=161)
FIGURE $2 \lim _{x \rightarrow a} f(x)=L$ in all three cases

| $t$ | $\frac{\sqrt{t^{2}+9}-3}{t^{2}}$ |
| :--- | :--- |
| $\pm 0.001$ | 0.166667 |
| $\pm 0.0001$ | 0.166670 |
| $\pm 0.00001$ | 0.167000 |
| $\pm 0.000001$ | 0.000000 |

EXAMPLE 1 Estimate the value of $\lim _{t \rightarrow 0} \frac{\sqrt{t^{2}+9}-3}{t^{2}}$.
SOLUTION The table lists values of the function for several values of $t$ near 0 .

| $t$ | $\frac{\sqrt{t^{2}+9}-3}{t^{2}}$ |
| :--- | :--- |
| $\pm 1.0$ | 0.162277 ... |
| ±0.5 | $0.165525 \ldots$ |
| ±0.1 | 0.166620 ... |
| ±0.05 | 0.166655 ... |
| ±0.01 | $0.166666 \ldots$ |

As $t$ approaches 0, the values of the function seem to approach $0.1666666 \ldots$ and so we guess that

$$
\lim _{t \rightarrow 0} \frac{\sqrt{t^{2}+9}-3}{t^{2}}=\frac{1}{6}
$$ $\square$

In Example 1 what would have happened if we had taken even smaller values of $t$ ? The table in the margin shows the results from one calculator; you can see that something strange seems to be happening.

If you try these calculations on your own calculator you might get different values, but eventually you will get the value 0 if you make $t$ sufficiently small. Does this
mean that the answer is really 0 instead of $\frac{1}{6}$ ? No, the value of the limit is $\frac{1}{6}$, as we will show in the next section. The problem is that the calculator gave false values because $\sqrt{t^{2}+9}$ is very close to 3 when $t$ is small. (In fact, when $t$ is sufficiently small, a calculator's value for $\sqrt{t^{2}+9}$ is $3.000 \ldots$ to as many digits as the calculator is capable of carrying.)

Something similar happens when we try to graph the function

$$
f(t)=\frac{\sqrt{t^{2}+9}-3}{t^{2}}
$$

of Example 1 on a graphing calculator or computer. Parts (a) and (b) of Figure 3 show quite accurate graphs of $f$, and if we trace along the curve, we can estimate easily that the limit is about $\frac{1}{6}$. But if we zoom in too much, as in parts (c) and (d), then we get inaccurate graphs, again due to rounding errors within the calculations.

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0120.jpg?height=338&width=1771&top_left_y=899&top_left_x=244)
FIGURE 3

| $x$ | $\frac{\sin x}{x}$ |
| :--- | :--- |
| $\pm 1.0$ | 0.84147098 |
| ±0.5 | 0.95885108 |
| ±0.4 | 0.97354586 |
| ±0.3 | 0.98506736 |
| ±0.2 | 0.99334665 |
| ±0.1 | 0.99833417 |
| ±0.05 | 0.99958339 |
| ±0.01 | 0.99998333 |
| ±0.005 | 0.99999583 |
| ±0.001 | 0.99999983 |

FIGURE 4

EXAMPLE 2 Guess the value of $\lim _{x \rightarrow 0} \frac{\sin x}{x}$.
SOLUTION The function $f(x)=(\sin x) / x$ is not defined when $x=0$. Using a calculator (and remembering that, if $x \in \mathbb{R}, \sin x$ means the sine of the angle whose radian measure is $x$ ), we construct a table of values correct to eight decimal places. From the table at the left and the graph in Figure 4 we guess that

$$
\lim _{x \rightarrow 0} \frac{\sin x}{x}=1
$$

This guess is in fact correct, as will be proved in Chapter 3 using a geometric argument.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0120.jpg?height=278&width=497&top_left_y=1979&top_left_x=1144) $\square$

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0121.jpg?height=232&width=481&top_left_y=1147&top_left_x=120)
FIGURE 5
The Heaviside function

EXAMPLE 3 Find $\lim _{x \rightarrow 0}\left(x^{3}+\frac{\cos 5 x}{10,000}\right)$.
SOLUTION As before, we construct a table of values. From the first table it appears that the limit might be zero.

| $x$ | $x^{3}+\frac{\cos 5 x}{10,000}$ |
| :--- | :--- |
| 1 | 1.000028 |
| 0.5 | 0.124920 |
| 0.1 | 0.001088 |
| 0.05 | 0.000222 |
| 0.01 | 0.000101 |


| $x$ | $x^{3}+\frac{\cos 5 x}{10,000}$ |
| :--- | :--- |
| 0.005 | 0.00010009 |
| 0.001 | 0.00010000 |

But if we persevere with smaller values of $x$, the second table suggests that the limit is more likely to be 0.0001. In Section 2.5 we will be able to show that $\lim _{x \rightarrow 0} \cos 5 x=1$ and that it follows that

$$
\lim _{x \rightarrow 0}\left(x^{3}+\frac{\cos 5 x}{10,000}\right)=\frac{1}{10,000}=0.0001
$$ $\square$

## ■ One-Sided Limits

The Heaviside function $H$ is defined by

$$
H(t)= \begin{cases}0 & \text { if } t<0 \\ 1 & \text { if } t \geqslant 0\end{cases}
$$

(This function is named after the electrical engineer Oliver Heaviside [1850-1925] and can be used to describe an electric current that is switched on at time $t=0$.) Its graph is shown in Figure 5.

There is no single number that $H(t)$ approaches as $t$ approaches 0, so $\lim _{t \rightarrow 0} H(t)$ does not exist. However, as $t$ approaches 0 from the left, $H(t)$ approaches 0. As $t$ approaches 0 from the right, $H(t)$ approaches 1 . We indicate this situation symbolically by writing

$$
\lim _{t \rightarrow 0^{-}} H(t)=0 \quad \text { and } \quad \lim _{t \rightarrow 0^{+}} H(t)=1
$$

and we call these one-sided limits. The notation $t \rightarrow 0^{-}$indicates that we consider only values of $t$ that are less than 0 . Likewise, $t \rightarrow 0^{+}$indicates that we consider only values of $t$ that are greater than 0.

2 Intuitive Definition of One-Sided Limits We write

$$
\lim _{x \rightarrow a^{-}} f(x)=L
$$

and say that the left-hand limit of $f(x)$ as $x$ approaches $a$ [or the limit of $f(x)$ as $x$ approaches a from the left] is equal to $L$ if we can make the values of $f(x)$ arbitrarily close to $L$ by restricting $x$ to be sufficiently close to $a$ with $x$ less than $a$.

We write

$$
\lim _{x \rightarrow a^{+}} f(x)=L
$$

and say that the right-hand limit of $f(x)$ as $x$ approaches $a$ [or the limit of $f(x)$ as $x$ approaches a from the right] is equal to $L$ if we can make the values of $f(x)$ arbitrarily close to $L$ by restricting $x$ to be sufficiently close to $a$ with $x$ greater than $a$.

For instance, the notation $x \rightarrow 5^{-}$means that we consider only $x<5$, and $x \rightarrow 5^{+}$ means that we consider only $x>5$. Definition 2 is illustrated in Figure 6.

FIGURE 6
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0122.jpg?height=386&width=1131&top_left_y=341&top_left_x=825)

Notice that Definition 2 differs from Definition 1 only in that we require $x$ to be less than (or greater than) $a$. By comparing these definitions, we see that the following is true.

$3 \lim _{x \rightarrow a} f(x)=L \quad$ if and only if $\quad \lim _{x \rightarrow a^{-}} f(x)=L \quad$ and $\quad \lim _{x \rightarrow a^{+}} f(x)=L$

EXAMPLE 4 The graph of a function $g$ is shown in Figure 7.

FIGURE 7
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0122.jpg?height=355&width=497&top_left_y=1135&top_left_x=1142)

Use the graph to state the values (if they exist) of the following:
(a) $\lim _{x \rightarrow 2^{-}} g(x)$
(b) $\lim _{x \rightarrow 2^{+}} g(x)$
(c) $\lim _{x \rightarrow 2} g(x)$
(d) $\lim _{x \rightarrow 5^{-}} g(x)$
(e) $\lim _{x \rightarrow 5^{+}} g(x)$
(f) $\lim _{x \rightarrow 5} g(x)$

SOLUTION Looking at the graph we see that the values of $g(x)$ approach 3 as $x$ approaches 2 from the left, but they approach 1 as $x$ approaches 2 from the right. Therefore
(a) $\lim _{x \rightarrow 2^{-}} g(x)=3$ and
(b) $\lim _{x \rightarrow 2^{+}} g(x)=1$
(c) Since the left and right limits are different, we conclude from (3) that $\lim _{x \rightarrow 2} g(x)$ does not exist.

The graph also shows that
(d) $\lim _{x \rightarrow 5^{-}} g(x)=2$ and
(e) $\lim _{x \rightarrow 5^{+}} g(x)=2$
(f) This time the left and right limits are the same and so, by (3), we have

$$
\lim _{x \rightarrow 5} g(x)=2
$$

Despite this fact, notice that $g(5) \neq 2$. $\square$

## ■ How Can a Limit Fail to Exist?

We have seen that a limit fails to exist at a number $a$ if the left- and right-hand limits are not equal (as in Example 4). The next two examples illustrate additional ways that a limit can fail to exist.

EXAMPLE 5 Investigate $\lim _{x \rightarrow 0} \sin \frac{\pi}{x}$.
SOLUTION Notice that the function $f(x)=\sin (\pi / x)$ is undefined at 0 . Evaluating the function for some small values of $x$, we get

$$
\begin{array}{rlrl}
f(1) & =\sin \pi=0 & f\left(\frac{1}{2}\right) & =\sin 2 \pi=0 \\
f\left(\frac{1}{3}\right) & =\sin 3 \pi=0 & f\left(\frac{1}{4}\right) & =\sin 4 \pi=0 \\
f(0.1) & =\sin 10 \pi=0 & f(0.01) & =\sin 100 \pi=0
\end{array}
$$

Similarly, $f(0.001)=f(0.0001)=0$. On the basis of this information we might be tempted to guess that the limit is 0, but this time our guess is wrong. Note that although $f(1 / n)=\sin n \pi=0$ for any integer $n$, it is also true that $f(x)=1$ for infinitely many values of $x$ (such as $2 / 5$ or $2 / 101$ ) that approach 0 . You can see this from the graph of $f$ shown in Figure 8.

FIGURE 8
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0123.jpg?height=412&width=1110&top_left_y=1265&top_left_x=712)

The dashed lines near the $y$-axis indicate that the values of $\sin (\pi / x)$ oscillate between 1 and -1 infinitely often as $x$ approaches 0.

Since the values of $f(x)$ do not approach a fixed number as $x$ approaches 0,

$$
\lim _{x \rightarrow 0} \sin \frac{\pi}{x} \text { does not exist }
$$ $\square$

Examples 3 and 5 illustrate some of the pitfalls in guessing the value of a limit. It is easy to guess the wrong value if we use inappropriate values of $x$, but it is difficult to know when to stop calculating values. And, as the discussion after Example 1 shows, sometimes calculators and computers give the wrong values. In the next section, however, we will develop foolproof methods for calculating limits.

Another way a limit at a number $a$ can fail to exist is when the function values grow arbitrarily large (in absolute value) as $x$ approaches $a$.

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0124.jpg?height=341&width=496&top_left_y=1907&top_left_x=243)
FIGURE 10
$$
\lim _{x \rightarrow a} f(x)=\infty
$$

EXAMPLE 6 Find $\lim _{x \rightarrow 0} \frac{1}{x^{2}}$ if it exists.
SOLUTION As $x$ becomes close to $0, x^{2}$ also becomes close to 0 , and $1 / x^{2}$ becomes very large. (See the following table.) In fact, it appears from the graph of the function $f(x)=1 / x^{2}$ shown in Figure 9 that the values of $f(x)$ can be made arbitrarily large by taking $x$ close enough to 0 . Thus the values of $f(x)$ do not approach a number, so $\lim _{x \rightarrow 0}\left(1 / x^{2}\right)$ does not exist.

| $x$ | $\frac{1}{x^{2}}$ |
| :--- | :--- |
| $\pm 1$ | 1 |
| $\pm 0.5$ | 4 |
| ±0.2 | 25 |
| ±0.1 | 100 |
| ±0.05 | 400 |
| ±0.01 | 10,000 |
| ±0.001 | 1,000,000 |


![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0124.jpg?height=351&width=499&top_left_y=596&top_left_x=1411)
FIGURE 9

■ Infinite Limits; Vertical Asymptotes
To indicate the kind of behavior exhibited in Example 6, we use the notation

$$
\lim _{x \rightarrow 0} \frac{1}{x^{2}}=\infty
$$

This does not mean that we are regarding $\infty$ as a number. Nor does it mean that the limit exists. It simply expresses the particular way in which the limit does not exist: $1 / x^{2}$ can be made as large as we like by taking $x$ close enough to 0 .

In general, we write symbolically

$$
\lim _{x \rightarrow a} f(x)=\infty
$$

to indicate that the values of $f(x)$ tend to become larger and larger (or "increase without bound") as $x$ becomes closer and closer to $a$.

4 Intuitive Definition of an Infinite Limit Let $f$ be a function defined on both sides of $a$, except possibly at $a$ itself. Then

$$
\lim _{x \rightarrow a} f(x)=\infty
$$

means that the values of $f(x)$ can be made arbitrarily large (as large as we please) by taking $x$ sufficiently close to $a$, but not equal to $a$.

Another notation for $\lim _{x \rightarrow a} f(x)=\infty$ is

$$
f(x) \rightarrow \infty \quad \text { as } \quad x \rightarrow a
$$

Again, the symbol $\infty$ is not a number, but the expression $\lim _{x \rightarrow a} f(x)=\infty$ is often read as "the limit of $f(x)$, as $x$ approaches $a$, is infinity"
or " $f(x)$ becomes infinite as $x$ approaches $a$ "
or " $f(x)$ increases without bound as $x$ approaches $a$ "
This definition is illustrated graphically in Figure 10.

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0125.jpg?height=364&width=488&top_left_y=424&top_left_x=120)
FIGURE 11
$$
\lim _{x \rightarrow a} f(x)=-\infty
$$

A similar sort of limit, for functions that become large negative as $x$ gets close to $a$, is defined in Definition 5 and is illustrated in Figure 11.

5 Definition Let $f$ be a function defined on both sides of $a$, except possibly at $a$ itself. Then

$$
\lim _{x \rightarrow a} f(x)=-\infty
$$

means that the values of $f(x)$ can be made arbitrarily large negative by taking $x$ sufficiently close to $a$, but not equal to $a$.

The symbol $\lim _{x \rightarrow a} f(x)=-\infty$ can be read as "the limit of $f(x)$, as $x$ approaches $a$, is negative infinity" or " $f(x)$ decreases without bound as $x$ approaches $a$." As an example we have

$$
\lim _{x \rightarrow 0}\left(-\frac{1}{x^{2}}\right)=-\infty
$$

Similar definitions can be given for the one-sided infinite limits

$$
\begin{array}{lrl}
\lim _{x \rightarrow a^{-}} f(x) & =\infty & \lim _{x \rightarrow a^{+}} f(x) \\
\lim _{x \rightarrow a^{-}} f(x) & =-\infty \\
\lim _{x \rightarrow a^{+}} f(x) & =-\infty
\end{array}
$$

remembering that $x \rightarrow a^{-}$means that we consider only values of $x$ that are less than $a$, and similarly $x \rightarrow a^{+}$means that we consider only $x>a$. Illustrations of these four cases are given in Figure 12.

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0125.jpg?height=367&width=1776&top_left_y=1396&top_left_x=113)
FIGURE 12

6 Definition The vertical line $x=a$ is called a vertical asymptote of the curve $y=f(x)$ if at least one of the following statements is true:

$$
\begin{array}{lll}
\lim _{x \rightarrow a} f(x)=\infty & \lim _{x \rightarrow a^{-}} f(x)=\infty & \lim _{x \rightarrow a^{+}} f(x)=\infty \\
\lim _{x \rightarrow a} f(x)=-\infty & \lim _{x \rightarrow a^{-}} f(x)=-\infty & \lim _{x \rightarrow a^{+}} f(x)=-\infty
\end{array}
$$

For instance, the $y$-axis is a vertical asymptote of the curve $y=1 / x^{2}$ because $\lim _{x \rightarrow 0}\left(1 / x^{2}\right)=\infty$. In Figure 12 the line $x=a$ is a vertical asymptote in each of the four cases shown. In general, knowledge of vertical asymptotes is very useful in sketching graphs.

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0126.jpg?height=401&width=403&top_left_y=584&top_left_x=243)
FIGURE 13

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0126.jpg?height=402&width=505&top_left_y=1293&top_left_x=244)
FIGURE 14
$y=\tan x$

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0126.jpg?height=398&width=371&top_left_y=1843&top_left_x=244)
FIGURE 15
The $y$-axis is a vertical asymptote of the natural logarithmic function.

EXAMPLE 7 Does the curve $y=\frac{2 x}{x-3}$ have a vertical asymptote?
SOLUTION There is a potential vertical asymptote where the denominator is 0 , that is, at $x=3$, so we investigate the one-sided limits there.

If $x$ is close to 3 but larger than 3 , then the denominator $x-3$ is a small positive number and $2 x$ is close to 6. So the quotient $2 x /(x-3)$ is a large positive number. [For instance, if $x=3.01$ then $2 x /(x-3)=6.02 / 0.01=602$.] Thus, intuitively, we see that

$$
\lim _{x \rightarrow 3^{+}} \frac{2 x}{x-3}=\infty
$$

Likewise, if $x$ is close to 3 but smaller than 3 , then $x-3$ is a small negative number but $2 x$ is still a positive number (close to 6). So $2 x /(x-3)$ is a numerically large negative number. Thus

$$
\lim _{x \rightarrow 3^{-}} \frac{2 x}{x-3}=-\infty
$$

The graph of the curve $y=2 x /(x-3)$ is given in Figure 13. According to Definition 6, the line $x=3$ is a vertical asymptote. $\square$

NOTE Neither of the limits in Examples 6 and 7 exist, but in Example 6 we can write $\lim _{x \rightarrow 0}\left(1 / x^{2}\right)=\infty$ because $f(x) \rightarrow \infty$ as $x$ approaches 0 from either the left or the right. In Example 7, $f(x) \rightarrow \infty$ as $x$ approaches 3 from the right but $f(x) \rightarrow-\infty$ as $x$ approaches 3 from the left, so we simply say that $\lim _{x \rightarrow 3} f(x)$ does not exist.

EXAMPLE 8 Find the vertical asymptotes of $f(x)=\tan x$.
SOLUTION Because

$$
\tan x=\frac{\sin x}{\cos x}
$$

there are potential vertical asymptotes where $\cos x=0$. In fact, since $\cos x \rightarrow 0^{+}$as $x \rightarrow(\pi / 2)^{-}$and $\cos x \rightarrow 0^{-}$as $x \rightarrow(\pi / 2)^{+}$, whereas $\sin x$ is positive (near 1) when $x$ is near $\pi / 2$, we have

$$
\lim _{x \rightarrow(\pi / 2)^{-}} \tan x=\infty \quad \text { and } \quad \lim _{x \rightarrow(\pi / 2)^{+}} \tan x=-\infty
$$

This shows that the line $x=\pi / 2$ is a vertical asymptote. Similar reasoning shows that the lines $x=\pi / 2+n \pi$, where $n$ is an integer, are all vertical asymptotes of $f(x)=\tan x$. The graph in Figure 14 confirms this. $\square$

Another example of a function whose graph has a vertical asymptote is the natural logarithmic function $y=\ln x$. From Figure 15 we see that

$$
\lim _{x \rightarrow 0^{+}} \ln x=-\infty
$$

and so the line $x=0$ (the $y$-axis) is a vertical asymptote. In fact, the same is true for $y=\log _{b} x$ provided that $b>1$. (See Figures 1.5.11 and 1.5.12.)

## 2.2 | Exercises

1. Explain in your own words what is meant by the equation
$$
\lim _{x \rightarrow 2} f(x)=5
$$
Is it possible for this statement to be true and yet $f(2)=3$ ? Explain.
2. Explain what it means to say that
$$
\lim _{x \rightarrow 1^{-}} f(x)=3 \quad \text { and } \quad \lim _{x \rightarrow 1^{+}} f(x)=7
$$
In this situation is it possible that $\lim _{x \rightarrow 1} f(x)$ exists? Explain.
3. Explain the meaning of each of the following.
(a) $\lim _{x \rightarrow-3} f(x)=\infty$
(b) $\lim _{x \rightarrow 4^{+}} f(x)=-\infty$
4. Use the given graph of $f$ to state the value of each quantity, if it exists. If it does not exist, explain why.
(a) $\lim _{x \rightarrow 2^{-}} f(x)$
(b) $\lim _{x \rightarrow 2^{+}} f(x)$
(c) $\lim _{x \rightarrow 2} f(x)$
(d) $f(2)$
(e) $\lim _{x \rightarrow 4} f(x)$
(f) $f(4)$
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0127.jpg?height=299&width=344&top_left_y=1135&top_left_x=370)
5. For the function $f$ whose graph is given, state the value of each quantity, if it exists. If it does not exist, explain why.
(a) $\lim _{x \rightarrow 1} f(x)$
(b) $\lim _{x \rightarrow 3^{-}} f(x)$
(c) $\lim _{x \rightarrow 3^{+}} f(x)$
(d) $\lim _{x \rightarrow 3} f(x)$
(e) $f(3)$
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0127.jpg?height=298&width=343&top_left_y=1724&top_left_x=370)
6. For the function $h$ whose graph is given, state the value of each quantity, if it exists. If it does not exist, explain why.
(a) $\lim _{x \rightarrow-3^{-}} h(x)$
(b) $\lim _{x \rightarrow-3^{+}} h(x)$
(c) $\lim _{x \rightarrow-3} h(x)$
(d) $h(-3)$
(e) $\lim _{x \rightarrow 0^{-}} h(x)$
(f) $\lim _{x \rightarrow 0^{+}} h(x)$
(g) $\lim _{x \rightarrow 0} h(x)$
(h) $h(0)$
(i) $\lim _{x \rightarrow 2} h(x)$
(j) $h(2)$
(k) $\lim _{x \rightarrow 5^{+}} h(x)$
(1) $\lim _{x \rightarrow 5^{-}} h(x)$
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0127.jpg?height=341&width=593&top_left_y=423&top_left_x=1162)
7. For the function $g$ whose graph is shown, find a number $a$ that satisfies the given description.
    (a) $\lim _{x \rightarrow a} g(x)$ does not exist but $g(a)$ is defined.
    (b) $\lim _{x \rightarrow a} g(x)$ exists but $g(a)$ is not defined.
    (c) $\lim _{x \rightarrow a^{-}} g(x)$ and $\lim _{x \rightarrow a^{+}} g(x)$ both exist but $\lim _{x \rightarrow a} g(x)$ does not exist.
    (d) $\lim _{x \rightarrow a^{+}} g(x)=g(a)$ but $\lim _{x \rightarrow a^{-}} g(x) \neq g(a)$.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0127.jpg?height=257&width=342&top_left_y=1198&top_left_x=1282)
8. For the function $A$ whose graph is shown, state the following.
(a) $\lim _{x \rightarrow-3} A(x)$
(b) $\lim _{x \rightarrow 2^{-}} A(x)$
(c) $\lim _{x \rightarrow 2^{+}} A(x)$
(d) $\lim _{x \rightarrow-1} A(x)$
(e) The equations of the vertical asymptotes
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0127.jpg?height=365&width=629&top_left_y=1765&top_left_x=1144)
9. For the function $f$ whose graph is shown, state the following.
(a) $\lim _{x \rightarrow-7} f(x)$
(b) $\lim _{x \rightarrow-3} f(x)$
(c) $\lim _{x \rightarrow 0} f(x)$
(d) $\lim _{x \rightarrow 6^{-}} f(x)$
(e) $\lim _{x \rightarrow 6^{+}} f(x)$


(f) The equations of the vertical asymptotes
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0128.jpg?height=287&width=600&top_left_y=295&top_left_x=397)
10. A patient receives a 150-mg injection of a drug every 4 hours. The graph shows the amount $f(t)$ of the drug in the bloodstream after $t$ hours. Find
$$
\lim _{t \rightarrow 12^{-}} f(t) \quad \text { and } \quad \lim _{t \rightarrow 12^{+}} f(t)
$$
and explain the significance of these one-sided limits.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0128.jpg?height=378&width=390&top_left_y=896&top_left_x=505)
11-12 Sketch the graph of the function and use it to determine the values of $a$ for which $\lim _{x \rightarrow a} f(x)$ exists.
11. $f(x)= \begin{cases}e^{x} & \text { if } x \leqslant 0 \\ x-1 & \text { if } 0<x<1 \\ \ln x & \text { if } x \geqslant 1\end{cases}$
12. $f(x)= \begin{cases}\sqrt[3]{x} & \text { if } x \leqslant-1 \\ x & \text { if }-1<x \leqslant 2 \\ (x-1)^{2} & \text { if } x>2\end{cases}$
13-14 Use the graph of the function $f$ to state the value of each limit, if it exists. If it does not exist, explain why.
(a) $\lim _{x \rightarrow 0^{-}} f(x)$
(b) $\lim _{x \rightarrow 0^{+}} f(x)$
(c) $\lim _{x \rightarrow 0} f(x)$
13. $f(x)=x \sqrt{1+x^{-2}}$
14. $f(x)=\frac{e^{1 / x}-2}{e^{1 / x}+1}$
15-18 Sketch the graph of an example of a function $f$ that satisfies all of the given conditions.
15. $\lim _{x \rightarrow 1^{-}} f(x)=3, \quad \lim _{x \rightarrow 1^{+}} f(x)=0, \quad f(1)=2$
16. $\lim _{x \rightarrow 0} f(x)=4, \quad \lim _{x \rightarrow 8^{-}} f(x)=1, \quad \lim _{x \rightarrow 8^{+}} f(x)=-3$, $f(0)=6, \quad f(8)=-1$
17. $\lim _{x \rightarrow-1^{-}} f(x)=0, \quad \lim _{x \rightarrow-1^{+}} f(x)=1, \quad \lim _{x \rightarrow 2} f(x)=3$, $f(-1)=2, \quad f(2)=1$
18. $\lim _{x \rightarrow-3^{-}} f(x)=3, \quad \lim _{x \rightarrow-3^{+}} f(x)=2, \quad \lim _{x \rightarrow 3^{-}} f(x)=-1$, $\lim _{x \rightarrow 3^{+}} f(x)=2, \quad f(-3)=2, \quad f(3)=0$

19-22 Guess the value of the limit (if it exists) by evaluating the function at the given numbers (correct to six decimal places).

19. $$
\begin{aligned}
& \lim _{x \rightarrow 3} \frac{x^{2}-3 x}{x^{2}-9}, \\
& x=3.1,3.05,3.01,3.001,3.0001, \\
& 2.9,2.95,2.99,2.999,2.9999
\end{aligned}
$$
20. $$
\begin{aligned}
& \lim _{x \rightarrow-3} \frac{x^{2}-3 x}{x^{2}-9}, \\
& x=-2.5,-2.9,-2.95,-2.99,-2.999,-2.9999, \\
& -3.5,-3.1,-3.05,-3.01,-3.001,-3.0001
\end{aligned}
$$
21. $\lim _{t \rightarrow 0} \frac{e^{5 t}-1}{t}, \quad t= \pm 0.5, \pm 0.1, \pm 0.01, \pm 0.001, \pm 0.0001$
22. $$
\begin{aligned}
& \lim _{h \rightarrow 0} \frac{(2+h)^{5}-32}{h}, \\
& h= \pm 0.5, \pm 0.1, \pm 0.01, \pm 0.001, \pm 0.0001
\end{aligned}
$$

23-28 Use a table of values to estimate the value of the limit. If you have a graphing device, use it to confirm your result graphically.
23. $\lim _{x \rightarrow 4} \frac{\ln x-\ln 4}{x-4}$
24. $\lim _{p \rightarrow-1} \frac{1+p^{9}}{1+p^{15}}$
25. $\lim _{\theta \rightarrow 0} \frac{\sin 3 \theta}{\tan 2 \theta}$
26. $\lim _{t \rightarrow 0} \frac{5^{t}-1}{t}$
27. $\lim _{x \rightarrow 0^{+}} x^{x}$
28. $\lim _{x \rightarrow 0^{+}} x^{2} \ln x$

29-40 Determine the infinite limit.
29. $\lim _{x \rightarrow 5^{+}} \frac{x+1}{x-5}$
30. $\lim _{x \rightarrow 5^{-}} \frac{x+1}{x-5}$
31. $\lim _{x \rightarrow 2} \frac{x^{2}}{(x-2)^{2}}$
32. $\lim _{x \rightarrow 3^{-}} \frac{\sqrt{x}}{(x-3)^{5}}$
33. $\lim _{x \rightarrow 1^{+}} \ln (\sqrt{x}-1)$
34. $\lim _{x \rightarrow 0^{+}} \ln (\sin x)$
35. $\lim _{x \rightarrow(\pi / 2)^{+}} \frac{1}{x} \sec x$
36. $\lim _{x \rightarrow \pi^{-}} x \cot x$
37. $\lim _{x \rightarrow 1} \frac{x^{2}+2 x}{x^{2}-2 x+1}$
38. $\lim _{x \rightarrow 3^{-}} \frac{x^{2}+4 x}{x^{2}-2 x-3}$
39. $\lim _{x \rightarrow 0}\left(\ln x^{2}-x^{-2}\right)$
40. $\lim _{x \rightarrow 0^{+}}\left(\frac{1}{x}-\ln x\right)$

41. Find the vertical asymptote of the function
$$
f(x)=\frac{x-1}{2 x+4}
$$
42. (a) Find the vertical asymptotes of the function
$$
y=\frac{x^{2}+1}{3 x-2 x^{2}}
$$
(b) Confirm your answer to part (a) by graphing the function.
43. Determine $\lim _{x \rightarrow 1^{-}} \frac{1}{x^{3}-1}$ and $\lim _{x \rightarrow 1^{+}} \frac{1}{x^{3}-1}$
    (a) by evaluating $f(x)=1 /\left(x^{3}-1\right)$ for values of $x$ that approach 1 from the left and from the right,
    (b) by reasoning as in Example 7, and
    (c) from a graph of $f$.
44. (a) By graphing the function
$$
f(x)=\frac{\cos 2 x-\cos x}{x^{2}}
$$
and zooming in toward the point where the graph crosses the $y$-axis, estimate the value of $\lim _{x \rightarrow 0} f(x)$.
    (b) Check your answer in part (a) by evaluating $f(x)$ for values of $x$ that approach 0.
45. (a) Estimate the value of the limit $\lim _{x \rightarrow 0}(1+x)^{1 / x}$ to five decimal places. Does this number look familiar?
    (b) Illustrate part (a) by graphing the function $y=(1+x)^{1 / x}$.
46. (a) Graph the function $f(x)=e^{x}+\ln |x-4|$ for $0 \leqslant x \leqslant 5$. Do you think the graph is an accurate representation of $f$ ?
    (b) How would you get a graph that represents $f$ better?
47. (a) Evaluate the function $f(x)=x^{2}-\left(2^{x} / 1000\right)$ for $x=1,0.8,0.6,0.4,0.2,0.1$, and 0.05 , and guess the value of
$$
\lim _{x \rightarrow 0}\left(x^{2}-\frac{2^{x}}{1000}\right)
$$
    (b) Evaluate $f(x)$ for $x=0.04,0.02,0.01,0.005,0.003$, and 0.001. Guess again.
48. (a) Evaluate the function
$$
h(x)=\frac{\tan x-x}{x^{3}}
$$
for $x=1,0.5,0.1,0.05,0.01$, and 0.005.
    (b) Guess the value of $\lim _{x \rightarrow 0} \frac{\tan x-x}{x^{3}}$.
    (c) Evaluate $h(x)$ for successively smaller values of $x$ until you finally reach a value of 0 for $h(x)$. Are you still confident that your guess in part (b) is correct? Explain why you eventually obtained 0 values. (In Section 4.4 a method for evaluating this limit will be explained.)
(d) Graph the function $h$ in the viewing rectangle [-1, 1] by [0, 1]. Then zoom in toward the point where the graph crosses the $y$-axis to estimate the limit of $h(x)$ as $x$ approaches 0 . Continue to zoom in until you observe distortions in the graph of $h$. Compare with the results of part (c).
49. Use a graph to estimate the equations of all the vertical asymptotes of the curve
$$
y=\tan (2 \sin x) \quad-\pi \leqslant x \leqslant \pi
$$
Then find the exact equations of these asymptotes.
50. Consider the function $f(x)=\tan \frac{1}{x}$.
    (a) Show that $f(x)=0$ for $x=\frac{1}{\pi}, \frac{1}{2 \pi}, \frac{1}{3 \pi}, \ldots$
    (b) Show that $f(x)=1$ for $x=\frac{4}{\pi}, \frac{4}{5 \pi}, \frac{4}{9 \pi}, \ldots$
    (c) What can you conclude about $\lim _{x \rightarrow 0^{+}} \tan \frac{1}{x}$ ?
51. In the theory of relativity, the mass of a particle with velocity $v$ is
$$
m=\frac{m_{0}}{\sqrt{1-v^{2} / c^{2}}}
$$
where $m_{0}$ is the mass of the particle at rest and $c$ is the speed of light. What happens as $v \rightarrow c^{-}$?

### 2.3 Calculating Limits Using the Limit Laws

■ Properties of Limits
In Section 2.2 we used calculators and graphs to guess the values of limits, but we saw that such methods don't always lead to the correct answers. In this section we use the following properties of limits, called the Limit Laws, to calculate limits.

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0130.jpg?height=322&width=427&top_left_y=1645&top_left_x=245)
FIGURE 1

Limit Laws Suppose that $c$ is a constant and the limits

$$
\lim _{x \rightarrow a} f(x) \quad \text { and } \quad \lim _{x \rightarrow a} g(x)
$$

exist. Then

1. $\lim _{x \rightarrow a}[f(x)+g(x)]=\lim _{x \rightarrow a} f(x)+\lim _{x \rightarrow a} g(x)$
2. $\lim _{x \rightarrow a}[f(x)-g(x)]=\lim _{x \rightarrow a} f(x)-\lim _{x \rightarrow a} g(x)$
3. $\lim _{x \rightarrow a}[c f(x)]=c \lim _{x \rightarrow a} f(x)$
4. $\lim _{x \rightarrow a}[f(x) g(x)]=\lim _{x \rightarrow a} f(x) \cdot \lim _{x \rightarrow a} g(x)$
5. $\lim _{x \rightarrow a} \frac{f(x)}{g(x)}=\frac{\lim _{x \rightarrow a} f(x)}{\lim _{x \rightarrow a} g(x)} \quad$ if $\lim _{x \rightarrow a} g(x) \neq 0$

These five laws can be stated verbally as follows:

1. The limit of a sum is the sum of the limits.
2. The limit of a difference is the difference of the limits.
3. The limit of a constant times a function is the constant times the limit of the function.
4. The limit of a product is the product of the limits.
5. The limit of a quotient is the quotient of the limits (provided that the limit of the denominator is not 0).

It is easy to believe that these properties are true. For instance, if $f(x)$ is close to $L$ and $g(x)$ is close to $M$, it is reasonable to conclude that $f(x)+g(x)$ is close to $L+M$. This gives us an intuitive basis for believing that Law 1 is true. In Section 2.4 we give a precise definition of a limit and use it to prove this law. The proofs of the remaining laws are given in Appendix F.

EXAMPLE 1 Use the Limit Laws and the graphs of $f$ and $g$ in Figure 1 to evaluate the following limits, if they exist.
(a) $\lim _{x \rightarrow-2}[f(x)+5 g(x)]$
(b) $\lim _{x \rightarrow 1}[f(x) g(x)]$
(c) $\lim _{x \rightarrow 2} \frac{f(x)}{g(x)}$

SOLUTION

(a) From the graphs of $f$ and $g$ we see that
$$
\lim _{x \rightarrow-2} f(x)=1 \quad \text { and } \quad \lim _{x \rightarrow-2} g(x)=-1
$$

Therefore we have

$$
\begin{aligned}
\lim _{x \rightarrow-2}[f(x)+5 g(x)] & =\lim _{x \rightarrow-2} f(x)+\lim _{x \rightarrow-2}[5 g(x)] \quad \text { (by Limit Law 1) } \\
& =\lim _{x \rightarrow-2} f(x)+5 \lim _{x \rightarrow-2} g(x) \quad \text { (by Limit Law 3) } \\
& =1+5(-1)=-4
\end{aligned}
$$

(b) We see that $\lim _{x \rightarrow 1} f(x)=2$. But $\lim _{x \rightarrow 1} g(x)$ does not exist because the left and right limits are different:

$$
\lim _{x \rightarrow 1^{-}} g(x)=-2 \quad \lim _{x \rightarrow 1^{+}} g(x)=-1
$$

So we can't use Law 4 for the desired limit. But we can use Law 4 for the one-sided limits:

$$
\begin{gathered}
\lim _{x \rightarrow 1^{-}}[f(x) g(x)]=\lim _{x \rightarrow 1^{-}} f(x) \cdot \lim _{x \rightarrow 1^{-}} g(x)=2 \cdot(-2)=-4 \\
\lim _{x \rightarrow 1^{+}}[f(x) g(x)]=\lim _{x \rightarrow 1^{+}} f(x) \cdot \lim _{x \rightarrow 1^{+}} g(x)=2 \cdot(-1)=-2
\end{gathered}
$$

The left and right limits aren't equal, so $\lim _{x \rightarrow 1}[f(x) g(x)]$ does not exist.
(c) The graphs show that

$$
\lim _{x \rightarrow 2} f(x) \approx 1.4 \quad \text { and } \quad \lim _{x \rightarrow 2} g(x)=0
$$

Because the limit of the denominator is 0 , we can't use Law 5 . The given limit does not exist because the denominator approaches 0 while the numerator approaches a nonzero number. $\square$

If we use the Product Law repeatedly with $g(x)=f(x)$, we obtain the following law.

## Power Law 6. $\lim _{x \rightarrow a}[f(x)]^{n}=\left[\lim _{x \rightarrow a} f(x)\right]^{n} \quad$ where $n$ is a positive integer

A similar property, which you are asked to prove in Exercise 2.5.69, holds for roots:

## Root Law

7. $\lim _{x \rightarrow a} \sqrt[n]{f(x)}=\sqrt[n]{\lim _{x \rightarrow a} f(x)} \quad$ where $n$ is a positive integer [If $n$ is even, we assume that $\lim _{x \rightarrow a} f(x)>0$.]

In applying these seven limit laws, we need to use two special limits:
8. $\lim _{x \rightarrow a} c=c$
9. $\lim _{x \rightarrow a} x=a$

These limits are obvious from an intuitive point of view (state them in words or draw graphs of $y=c$ and $y=x$ ), but proofs based on the precise definition are requested in Exercises 2.4.23-24.

If we now put $f(x)=x$ in Law 6 and use Law 9, we get a useful special limit for power functions.

10. $\lim _{x \rightarrow a} x^{n}=a^{n} \quad$ where $n$ is a positive integer

## Newton and Limits

Isaac Newton was born on Christmas Day in 1642, the year of Galileo's death. When he entered Cambridge University in 1661 Newton didn't know much mathematics, but he learned quickly by reading Euclid and Descartes and by attending the lectures of Isaac Barrow. Cambridge was closed because of the plague from 1665 to 1666, and Newton returned home to refle t on what he had learned. Those two years were amazingly productive for at that time he made four of his major discoveries: (1) his representation of functions as sums of infini e series, including the binomial theorem; (2) his work on differential and integral calculus; (3) his laws of motion and law of universal gravitation; and (4) his prism experiments on the nature of light and color. Because of a fear of controversy and criticism, he was reluctant to publish his discoveries and it wasn't until 1687, at the urging of the astronomer Halley, that Newton published Principia Mathematica. In this work, the greatest scientific t eatise ever written, Newton set forth his version of calculus and used it to investigate mechanics, fluid dynamic , and wave motion, and to explain the motion of planets and comets.

The beginnings of calculus are found in the calculations of areas and volumes by ancient Greek scholars such as Eudoxus and Archimedes. Although aspects of the idea of a limit are implicit in their "method of exhaustion," Eudoxus and Archimedes never explicitly formulated the concept of a limit. Likewise, mathematicians such as Cavalieri, Fermat, and Barrow, the immediate precursors of Newton in the development of calculus, did not actually use limits. It was Isaac Newton who was the first o talk explicitly about limits. He explained that the main idea behind limits is that quantities "approach nearer than by any given difference." Newton stated that the limit was the basic concept in calculus, but it was left to later mathematicians like Cauchy to clarify his ideas about limits.

If we put $f(x)=x$ in Law 7 and use Law 9, we get a similar special limit for roots. (For square roots the proof is outlined in Exercise 2.4.37.)
11. $\lim _{x \rightarrow a} \sqrt[n]{x}=\sqrt[n]{a} \quad$ where $n$ is a positive integer
(If $n$ is even, we assume that $a>0$.)

EXAMPLE 2 Evaluate the following limits and justify each step.
(a) $\lim _{x \rightarrow 5}\left(2 x^{2}-3 x+4\right)$
(b) $\lim _{x \rightarrow-2} \frac{x^{3}+2 x^{2}-1}{5-3 x}$

## SOLUTION

(a)

$$
\begin{aligned}
\lim _{x \rightarrow 5}\left(2 x^{2}-3 x+4\right) & =\lim _{x \rightarrow 5}\left(2 x^{2}\right)-\lim _{x \rightarrow 5}(3 x)+\lim _{x \rightarrow 5} 4 & & \text { (by Laws 2 and 1) } \\
& =2 \lim _{x \rightarrow 5} x^{2}-3 \lim _{x \rightarrow 5} x+\lim _{x \rightarrow 5} 4 & & \text { (by 3) } \\
& =2\left(5^{2}\right)-3(5)+4 & & \text { (by 10, 9, and 8) } \\
& =39 & &
\end{aligned}
$$

(b) We start by using Law 5, but its use is fully justified only at the final stage when we see that the limits of the numerator and denominator exist and the limit of the denominator is not 0.

$$
\begin{array}{rlr}
\lim _{x \rightarrow-2} \frac{x^{3}+2 x^{2}-1}{5-3 x} & =\frac{\lim _{x \rightarrow-2}\left(x^{3}+2 x^{2}-1\right)}{\lim _{x \rightarrow-2}(5-3 x)} & \\
& =\frac{\lim _{x \rightarrow-2} x^{3}+2 \lim _{x \rightarrow-2} x^{2}-\lim _{x \rightarrow-2} 1}{\lim _{x \rightarrow-2} 5-3 \lim _{x \rightarrow-2} x} & \quad(\text { by } 1,2, \text { and } \text { 4 }) \\
& =\frac{(-2)^{3}+2(-2)^{2}-1}{5-3(-2)} & \quad(\text { by } 10,9, \text { and } 8) \\
& =-\frac{1}{11} &
\end{array}
$$ $\square$

## ■ Evaluating Limits by Direct Substitution

In Example 2(a) we determined that $\lim _{x \rightarrow 5} f(x)=39$, where $f(x)=2 x^{2}-3 x+4$. Notice that $f(5)=39$; in other words, we would have gotten the correct result simply by substituting 5 for $x$. Similarly, direct substitution provides the correct answer in part (b). The functions in Example 2 are a polynomial and a rational function, respectively, and similar use of the Limit Laws proves that direct substitution always works for such functions (see Exercises 59 and 60). We state this fact as follows.

Direct Substitution Property If $f$ is a polynomial or a rational function and $a$ is in the domain of $f$, then

$$
\lim _{x \rightarrow a} f(x)=f(a)
$$

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0133.jpg?height=661&width=396&top_left_y=1469&top_left_x=121)
FIGURE 2
The graphs of the functions $f$ (from Example 3) and $g$ (from Example 4)

Functions that have the Direct Substitution Property are called continuous at $a$ and will be studied in Section 2.5. However, not all limits can be evaluated initially by direct substitution, as the following examples show.

EXAMPLE 3 Find $\lim _{x \rightarrow 1} \frac{x^{2}-1}{x-1}$.
SOLUTION Let $f(x)=\left(x^{2}-1\right) /(x-1)$. We can't find the limit by substituting $x=1$ because $f(1)$ isn't defined. Nor can we apply the Quotient Law, because the limit of the denominator is 0 . Instead, we need to do some preliminary algebra. We factor the numerator as a difference of squares:

$$
\frac{x^{2}-1}{x-1}=\frac{(x-1)(x+1)}{x-1}
$$

The numerator and denominator have a common factor of $x-1$. When we take the limit as $x$ approaches 1 , we have $x \neq 1$ and so $x-1 \neq 0$. Therefore we can cancel the common factor, $x-1$, and then compute the limit by direct substitution as follows:

$$
\begin{aligned}
\lim _{x \rightarrow 1} \frac{x^{2}-1}{x-1} & =\lim _{x \rightarrow 1} \frac{(x-1)(x+1)}{x-1} \\
& =\lim _{x \rightarrow 1}(x+1)=1+1=2
\end{aligned}
$$

The limit in this example arose in Example 2.1.1 in finding the tangent to the parabola $y=x^{2}$ at the point $(1,1)$. $\square$

NOTE In Example 3 we were able to compute the limit by replacing the given function $f(x)=\left(x^{2}-1\right) /(x-1)$ by a simpler function, $g(x)=x+1$, that has the same limit. This is valid because $f(x)=g(x)$ except when $x=1$, and in computing a limit as $x$ approaches 1 we don't consider what happens when $x$ is actually equal to 1 . In general, we have the following useful fact.

If $f(x)=g(x)$ when $x \neq a$, then $\lim _{x \rightarrow a} f(x)=\lim _{x \rightarrow a} g(x)$, provided the limits exist.

EXAMPLE 4 Find $\lim _{x \rightarrow 1} g(x)$ where

$$
g(x)= \begin{cases}x+1 & \text { if } x \neq 1 \\ \pi & \text { if } x=1\end{cases}
$$

SOLUTION Here $g$ is defined at $x=1$ and $g(1)=\pi$, but the value of a limit as $x$ approaches 1 does not depend on the value of the function at 1. Since $g(x)=x+1$ for $x \neq 1$, we have

$$
\lim _{x \rightarrow 1} g(x)=\lim _{x \rightarrow 1}(x+1)=2
$$ $\square$

Note that the values of the functions in Examples 3 and 4 are identical except when $x=1$ (see Figure 2) and so they have the same limit as $x$ approaches 1.

EXAMPLE 5 Evaluate $\lim _{h \rightarrow 0} \frac{(3+h)^{2}-9}{h}$.
SOLUTION If we define

$$
F(h)=\frac{(3+h)^{2}-9}{h}
$$

then, as in Example 3, we can't compute $\lim _{h \rightarrow 0} F(h)$ by letting $h=0$ because $F(0)$ is undefined. But if we simplify $F(h)$ algebraically, we find that

$$
\begin{aligned}
F(h) & =\frac{\left(9+6 h+h^{2}\right)-9}{h}=\frac{6 h+h^{2}}{h} \\
& =\frac{h(6+h)}{h}=6+h
\end{aligned}
$$

(Recall that we consider only $h \neq 0$ when letting $h$ approach 0 .) Thus

$$
\lim _{h \rightarrow 0} \frac{(3+h)^{2}-9}{h}=\lim _{h \rightarrow 0}(6+h)=6
$$ $\square$

EXAMPLE 6 Find $\lim _{t \rightarrow 0} \frac{\sqrt{t^{2}+9}-3}{t^{2}}$.
SOLUTION We can't apply the Quotient Law immediately because the limit of the denominator is 0 . Here the preliminary algebra consists of rationalizing the numerator:

$$
\begin{aligned}
\lim _{t \rightarrow 0} \frac{\sqrt{t^{2}+9}-3}{t^{2}} & =\lim _{t \rightarrow 0} \frac{\sqrt{t^{2}+9}-3}{t^{2}} \cdot \frac{\sqrt{t^{2}+9}+3}{\sqrt{t^{2}+9}+3} \\
& =\lim _{t \rightarrow 0} \frac{\left(t^{2}+9\right)-9}{t^{2}\left(\sqrt{t^{2}+9}+3\right)} \\
& =\lim _{t \rightarrow 0} \frac{t^{2}}{t^{2}\left(\sqrt{t^{2}+9}+3\right)} \\
& =\lim _{t \rightarrow 0} \frac{1}{\sqrt{t^{2}+9}+3} \quad \begin{array}{l}
\text { (Here we use several properties } \\
\text { of limits: 5, 1, 7, 8, 10.) }
\end{array} \\
& =\frac{1}{\sqrt{\lim _{t \rightarrow 0}\left(t^{2}+9\right)}+3} \\
& =\frac{1}{3+3}=\frac{1}{6}
\end{aligned}
$$

This calculation confirms the guess that we made in Example 2.2.1. $\square$

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0135.jpg?height=275&width=461&top_left_y=1696&top_left_x=119)
FIGURE 4

## ■ Using One-Sided Limits

Some limits are best calculated by first finding the left- and right-hand limits. The following theorem is a reminder of what we discovered in Section 2.2. It says that a two-sided limit exists if and only if both of the one-sided limits exist and are equal.

1 Theorem $\lim _{x \rightarrow a} f(x)=L \quad$ if and only if $\quad \lim _{x \rightarrow a^{-}} f(x)=L=\lim _{x \rightarrow a^{+}} f(x)$

When computing one-sided limits, we use the fact that the Limit Laws also hold for one-sided limits.

EXAMPLE 7 Show that $\lim _{x \rightarrow 0}|x|=0$.
SOLUTION Recall that

$$
|x|= \begin{cases}x & \text { if } x \geqslant 0 \\ -x & \text { if } x<0\end{cases}
$$

Since $|x|=x$ for $x>0$, we have

$$
\lim _{x \rightarrow 0^{+}}|x|=\lim _{x \rightarrow 0^{+}} x=0
$$

For $x<0$ we have $|x|=-x$ and so

$$
\lim _{x \rightarrow 0^{-}}|x|=\lim _{x \rightarrow 0^{-}}(-x)=0
$$

Therefore, by Theorem 1,

$$
\lim _{x \rightarrow 0}|x|=0
$$ $\square$

EXAMPLE 8 Prove that $\lim _{x \rightarrow 0} \frac{|x|}{x}$ does not exist.
SOLUTION Using the facts that $|x|=x$ when $x>0$ and $|x|=-x$ when $x<0$, we have

$$
\begin{aligned}
& \lim _{x \rightarrow 0^{+}} \frac{|x|}{x}=\lim _{x \rightarrow 0^{+}} \frac{x}{x}=\lim _{x \rightarrow 0^{+}} 1=1 \\
& \lim _{x \rightarrow 0^{-}} \frac{|x|}{x}=\lim _{x \rightarrow 0^{-}} \frac{-x}{x}=\lim _{x \rightarrow 0^{-}}(-1)=-1
\end{aligned}
$$

Since the right- and left-hand limits are different, it follows from Theorem 1 that $\lim _{x \rightarrow 0}|x| / x$ does not exist. The graph of the function $f(x)=|x| / x$ is shown in Figure 4 and supports the one-sided limits that we found. $\square$

EXAMPLE 9 If

$$
f(x)= \begin{cases}\sqrt{x-4} & \text { if } x>4 \\ 8-2 x & \text { if } x<4\end{cases}
$$

determine whether $\lim _{x \rightarrow 4} f(x)$ exists.

It is shown in Example 2.4.4 that $\lim _{x \rightarrow 0^{+}} \sqrt{x}=0$.

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0136.jpg?height=254&width=486&top_left_y=376&top_left_x=244)
FIGURE 5

Other notations for $\llbracket x \rrbracket$ are $[x]$ and $\lfloor x\rfloor$. The greatest integer function is sometimes called the floor function.

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0136.jpg?height=436&width=461&top_left_y=905&top_left_x=244)
FIGURE 6
Greatest integer function

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0136.jpg?height=326&width=490&top_left_y=1901&top_left_x=242)
FIGURE 7

SOLUTION Since $f(x)=\sqrt{x-4}$ for $x>4$, we have

$$
\lim _{x \rightarrow 4^{+}} f(x)=\lim _{x \rightarrow 4^{+}} \sqrt{x-4}=\sqrt{4-4}=0
$$

Since $f(x)=8-2 x$ for $x<4$, we have

$$
\lim _{x \rightarrow 4^{-}} f(x)=\lim _{x \rightarrow 4^{-}}(8-2 x)=8-2 \cdot 4=0
$$

The right- and left-hand limits are equal. Thus the limit exists and

$$
\lim _{x \rightarrow 4} f(x)=0
$$

The graph of $f$ is shown in Figure 5. $\square$

EXAMPLE 10 The greatest integer function is defined by $\llbracket x \rrbracket=$ the largest integer that is less than or equal to $x$. (For instance, $\llbracket 4 \rrbracket=4, \llbracket 4.8 \rrbracket=4, \llbracket \pi \rrbracket=3, \llbracket \sqrt{2} \rrbracket=1$, $\llbracket-\frac{1}{2} \rrbracket=-1$.) Show that $\lim _{x \rightarrow 3} \llbracket x \rrbracket$ does not exist.

SOLUTION The graph of the greatest integer function is shown in Figure 6. Since $\llbracket x \rrbracket=3$ for $3 \leqslant x<4$, we have

$$
\lim _{x \rightarrow 3^{+}} \llbracket x \rrbracket=\lim _{x \rightarrow 3^{+}} 3=3
$$

Since $\llbracket x \rrbracket=2$ for $2 \leqslant x<3$, we have

$$
\lim _{x \rightarrow 3^{-}} \llbracket x \rrbracket=\lim _{x \rightarrow 3^{-}} 2=2
$$

Because these one-sided limits are not equal, $\lim _{x \rightarrow 3} \llbracket x \rrbracket$ does not exist by Theorem 1. ■

## ■ The Squeeze Theorem

The following two theorems describe how the limits of functions are related when the values of one function are greater than (or equal to) those of another. Their proofs can be found in Appendix F.

2 Theorem If $f(x) \leqslant g(x)$ when $x$ is near $a$ (except possibly at $a$ ) and the limits of $f$ and $g$ both exist as $x$ approaches $a$, then

$$
\lim _{x \rightarrow a} f(x) \leqslant \lim _{x \rightarrow a} g(x)
$$

3 The Squeeze Theorem If $f(x) \leqslant g(x) \leqslant h(x)$ when $x$ is near $a$ (except possibly at $a$ ) and
then

$$
\begin{gathered}
\lim _{x \rightarrow a} f(x)=\lim _{x \rightarrow a} h(x)=L \\
\lim _{x \rightarrow a} g(x)=L
\end{gathered}
$$

The Squeeze Theorem, which is sometimes called the Sandwich Theorem or the Pinching Theorem, is illustrated by Figure 7. It says that if $g(x)$ is squeezed between $f(x)$ and $h(x)$ near $a$, and if $f$ and $h$ have the same limit $L$ at $a$, then $g$ is forced to have the same limit $L$ at $a$.

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0137.jpg?height=349&width=499&top_left_y=896&top_left_x=119)
FIGURE 8
$y=x^{2} \sin (1 / x)$

EXAMPLE 11 Show that $\lim _{x \rightarrow 0} x^{2} \sin \frac{1}{x}=0$.
SOLUTION First note that we cannot rewrite the limit as the product of the limits $\lim _{x \rightarrow 0} x^{2}$ and $\lim _{x \rightarrow 0} \sin (1 / x)$ because $\lim _{x \rightarrow 0} \sin (1 / x)$ does not exist (see Example 2.2.5).

We can find the limit by using the Squeeze Theorem. To apply the Squeeze Theorem we need to find a function $f$ smaller than $g(x)=x^{2} \sin (1 / x)$ and a function $h$ bigger than $g$ such that both $f(x)$ and $h(x)$ approach 0 as $x \rightarrow 0$. To do this we use our knowledge of the sine function. Because the sine of any number lies between -1 and 1 , we can write

$$
-1 \leqslant \sin \frac{1}{x} \leqslant 1
$$

Any inequality remains true when multiplied by a positive number. We know that $x^{2} \geqslant 0$ for all $x$ and so, multiplying each side of the inequalities in (4) by $x^{2}$, we get

$$
-x^{2} \leqslant x^{2} \sin \frac{1}{x} \leqslant x^{2}
$$

as illustrated by Figure 8. We know that

$$
\lim _{x \rightarrow 0} x^{2}=0 \quad \text { and } \quad \lim _{x \rightarrow 0}\left(-x^{2}\right)=0
$$

Taking $f(x)=-x^{2}, g(x)=x^{2} \sin (1 / x)$, and $h(x)=x^{2}$ in the Squeeze Theorem, we obtain

$$
\lim _{x \rightarrow 0} x^{2} \sin \frac{1}{x}=0
$$ $\square$

### 2.3 Exercises

1. Given that
$$
\lim _{x \rightarrow 2} f(x)=4 \quad \lim _{x \rightarrow 2} g(x)=-2 \quad \lim _{x \rightarrow 2} h(x)=0
$$
find the limits that exist. If the limit does not exist, explain why.
(a) $\lim _{x \rightarrow 2}[f(x)+5 g(x)]$
(b) $\lim _{x \rightarrow 2}[g(x)]^{3}$
(c) $\lim _{x \rightarrow 2} \sqrt{f(x)}$
(d) $\lim _{x \rightarrow 2} \frac{3 f(x)}{g(x)}$
(e) $\lim _{x \rightarrow 2} \frac{g(x)}{h(x)}$
(f) $\lim _{x \rightarrow 2} \frac{g(x) h(x)}{f(x)}$
2. The graphs of $f$ and $g$ are given. Use them to evaluate each limit, if it exists. If the limit does not exist, explain why.
(a) $\lim _{x \rightarrow 2}[f(x)+g(x)]$
(b) $\lim _{x \rightarrow 0}[f(x)-g(x)]$
(c) $\lim _{x \rightarrow-1}[f(x) g(x)]$
(d) $\lim _{x \rightarrow 3} \frac{f(x)}{g(x)}$
(e) $\lim _{x \rightarrow 2}\left[x^{2} f(x)\right]$
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0137.jpg?height=251&width=260&top_left_y=1623&top_left_x=1159)
(f) $f(-1)+\lim _{x \rightarrow-1} g(x)$
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0137.jpg?height=249&width=258&top_left_y=1624&top_left_x=1499)
3-9 Evaluate the limit and justify each step by indicating the appropriate Limit Law(s).
3. $\lim _{x \rightarrow 5}\left(4 x^{2}-5 x\right)$
4. $\lim _{x \rightarrow-3}\left(2 x^{3}+6 x^{2}-9\right)$
5. $\lim _{v \rightarrow 2}\left(v^{2}+2 v\right)\left(2 v^{3}-5\right)$
6. $\lim _{t \rightarrow 7} \frac{3 t^{2}+1}{t^{2}-5 t+2}$
7. $\lim _{u \rightarrow-2} \sqrt{9-u^{3}+2 u^{2}}$
8. $\lim _{x \rightarrow 3} \sqrt[3]{x+5}\left(2 x^{2}-3 x\right)$
9. $\lim _{t \rightarrow-1}\left(\frac{2 t^{5}-t^{4}}{5 t^{2}+4}\right)^{3}$

10. (a) What is wrong with the following equation?
$$
\frac{x^{2}+x-6}{x-2}=x+3
$$
    (b) In view of part (a), explain why the equation
$$
\lim _{x \rightarrow 2} \frac{x^{2}+x-6}{x-2}=\lim _{x \rightarrow 2}(x+3)
$$
is correct.

11-34 Evaluate the limit, if it exists.
11. $\lim _{x \rightarrow-2}(3 x-7)$
12. $\lim _{x \rightarrow 6}\left(8-\frac{1}{2} x\right)$
13. $\lim _{t \rightarrow 4} \frac{t^{2}-2 t-8}{t-4}$
14. $\lim _{x \rightarrow-3} \frac{x^{2}+3 x}{x^{2}-x-12}$
15. $\lim _{x \rightarrow 2} \frac{x^{2}+5 x+4}{x-2}$
16. $\lim _{x \rightarrow 4} \frac{x^{2}+3 x}{x^{2}-x-12}$
17. $\lim _{x \rightarrow-2} \frac{x^{2}-x-6}{3 x^{2}+5 x-2}$
18. $\lim _{x \rightarrow-5} \frac{2 x^{2}+9 x-5}{x^{2}-25}$
19. $\lim _{t \rightarrow 3} \frac{t^{3}-27}{t^{2}-9}$
20. $\lim _{u \rightarrow-1} \frac{u+1}{u^{3}+1}$
21. $\lim _{h \rightarrow 0} \frac{(h-3)^{2}-9}{h}$
22. $\lim _{x \rightarrow 9} \frac{9-x}{3-\sqrt{x}}$
23. $\lim _{h \rightarrow 0} \frac{\sqrt{9+h}-3}{h}$
24. $\lim _{x \rightarrow 2} \frac{2-x}{\sqrt{x+2}-2}$
25. $\lim _{x \rightarrow 3} \frac{\frac{1}{x}-\frac{1}{3}}{x-3}$
26. $\lim _{h \rightarrow 0} \frac{(-2+h)^{-1}+2^{-1}}{h}$
27. $\lim _{t \rightarrow 0} \frac{\sqrt{1+t}-\sqrt{1-t}}{t}$
28. $\lim _{t \rightarrow 0}\left(\frac{1}{t}-\frac{1}{t^{2}+t}\right)$
29. $\lim _{x \rightarrow 16} \frac{4-\sqrt{x}}{16 x-x^{2}}$
30. $\lim _{x \rightarrow 2} \frac{x^{2}-4 x+4}{x^{4}-3 x^{2}-4}$
31. $\lim _{t \rightarrow 0}\left(\frac{1}{t \sqrt{1+t}}-\frac{1}{t}\right)$
32. $\lim _{x \rightarrow-4} \frac{\sqrt{x^{2}+9}-5}{x+4}$
33. $\lim _{h \rightarrow 0} \frac{(x+h)^{3}-x^{3}}{h}$
34. $\lim _{h \rightarrow 0} \frac{\frac{1}{(x+h)^{2}}-\frac{1}{x^{2}}}{h}$

35. (a) Estimate the value of
$$
\lim _{x \rightarrow 0} \frac{x}{\sqrt{1+3 x}-1}
$$
by graphing the function $f(x)=x /(\sqrt{1+3 x}-1)$.
    (b) Make a table of values of $f(x)$ for $x$ close to 0 and guess the value of the limit.
    (c) Use the Limit Laws to prove that your guess is correct.
36. (a) Use a graph of
$$
f(x)=\frac{\sqrt{3+x}-\sqrt{3}}{x}
$$
to estimate the value of $\lim _{x \rightarrow 0} f(x)$ to two decimal places.
    (b) Use a table of values of $f(x)$ to estimate the limit to four decimal places.
    (c) Use the Limit Laws to find the exact value of the limit.
37. Use the Squeeze Theorem to show that
$$
\lim _{x \rightarrow 0} x^{2} \cos 20 \pi x=0
$$
Illustrate by graphing the functions $f(x)=-x^{2}$, $g(x)=x^{2} \cos 20 \pi x$, and $h(x)=x^{2}$ on the same screen.
38. Use the Squeeze Theorem to show that
$$
\lim _{x \rightarrow 0} \sqrt{x^{3}+x^{2}} \sin \frac{\pi}{x}=0
$$
Illustrate by graphing the functions $f, g$, and $h$ (in the notation of the Squeeze Theorem) on the same screen.
39. If $4 x-9 \leqslant f(x) \leqslant x^{2}-4 x+7$ for $x \geqslant 0$, find $\lim _{x \rightarrow 4} f(x)$.
40. If $2 x \leqslant g(x) \leqslant x^{4}-x^{2}+2$ for all $x$, evaluate $\lim _{x \rightarrow 1} g(x)$.
41. Prove that $\lim _{x \rightarrow 0} x^{4} \cos \frac{2}{x}=0$.
42. Prove that $\lim _{x \rightarrow 0^{+}} \sqrt{x} e^{\sin (\pi / x)}=0$.

43-48 Find the limit, if it exists. If the limit does not exist, explain why.
43. $\lim _{x \rightarrow-4}(|x+4|-2 x)$
44. $\lim _{x \rightarrow-4} \frac{|x+4|}{2 x+8}$
45. $\lim _{x \rightarrow 0.5^{-}} \frac{2 x-1}{\left|2 x^{3}-x^{2}\right|}$
46. $\lim _{x \rightarrow-2} \frac{2-|x|}{2+x}$
47. $\lim _{x \rightarrow 0^{-}}\left(\frac{1}{x}-\frac{1}{|x|}\right)$
48. $\lim _{x \rightarrow 0^{+}}\left(\frac{1}{x}-\frac{1}{|x|}\right)$

49. The Signum Function The signum (or sign) function, denoted by sgn, is defined by
$$
\operatorname{sgn} x=\left\{\begin{aligned}
-1 & \text { if } x<0 \\
0 & \text { if } x=0 \\
1 & \text { if } x>0
\end{aligned}\right.
$$
    (a) Sketch the graph of this function.
    (b) Find each of the following limits or explain why it does not exist.
(i) $\lim _{x \rightarrow 0^{+}} \operatorname{sgn} x$
(ii) $\lim _{x \rightarrow 0^{-}} \operatorname{sgn} x$
(iii) $\lim _{x \rightarrow 0} \operatorname{sgn} x$
(iv) $\lim _{x \rightarrow 0}|\operatorname{sgn} x|$

50. Let $g(x)=\operatorname{sgn}(\sin x)$.
    (a) Find each of the following limits or explain why it does not exist.
(i) $\lim _{x \rightarrow 0^{+}} g(x)$
(ii) $\lim _{x \rightarrow 0^{-}} g(x)$
(iii) $\lim _{x \rightarrow 0} g(x)$
(iv) $\lim _{x \rightarrow \pi^{+}} g(x)$
(v) $\lim _{x \rightarrow \pi^{-}} g(x)$
(vi) $\lim _{x \rightarrow \pi} g(x)$
    (b) For which values of $a$ does $\lim _{x \rightarrow a} g(x)$ not exist?
    (c) Sketch a graph of $g$.
51. Let $g(x)=\frac{x^{2}+x-6}{|x-2|}$.
    (a) Find
(i) $\lim _{x \rightarrow 2^{+}} g(x)$
(ii) $\lim _{x \rightarrow 2^{-}} g(x)$
    (b) Does $\lim _{x \rightarrow 2} g(x)$ exist?
    (c) Sketch the graph of $g$.
52. Let
$$
f(x)= \begin{cases}x^{2}+1 & \text { if } x<1 \\ (x-2)^{2} & \text { if } x \geqslant 1\end{cases}
$$
    (a) Find $\lim _{x \rightarrow 1^{-}} f(x)$ and $\lim _{x \rightarrow 1^{+}} f(x)$.
    (b) Does $\lim _{x \rightarrow 1} f(x)$ exist?
    (c) Sketch the graph of $f$.
53. Let
$$
B(t)= \begin{cases}4-\frac{1}{2} t & \text { if } t<2 \\ \sqrt{t+\mathrm{c}} & \text { if } t \geqslant 2\end{cases}
$$
Find the value of $c$ so that $\lim _{t \rightarrow 2} B(t)$ exists.
54. Let
$$
g(x)= \begin{cases}x & \text { if } x<1 \\ 3 & \text { if } x=1 \\ 2-x^{2} & \text { if } 1<x \leqslant 2 \\ x-3 & \text { if } x>2\end{cases}
$$
    (a) Evaluate each of the following, if it exists.
(i) $\lim _{x \rightarrow 1^{-}} g(x)$
(ii) $\lim _{x \rightarrow 1} g(x)$
(iii) $g(1)$
(iv) $\lim _{x \rightarrow 2^{-}} g(x)$
(v) $\lim _{x \rightarrow 2^{+}} g(x)$
(vi) $\lim _{x \rightarrow 2} g(x)$
    (b) Sketch the graph of $g$.
55. (a) If the symbol $\llbracket \rrbracket$ denotes the greatest integer function defined in Example 10, evaluate
(i) $\lim _{x \rightarrow-2^{+}} \llbracket x \rrbracket$
(ii) $\lim _{x \rightarrow-2} \llbracket x \rrbracket$
(iii) $\lim _{x \rightarrow-2.4} \llbracket x \rrbracket$
    (b) If $n$ is an integer, evaluate
(i) $\lim _{x \rightarrow n^{-}} \llbracket x \rrbracket$
(ii) $\lim _{x \rightarrow n^{+}} \llbracket x \rrbracket$
    (c) For what values of $a$ does $\lim _{x \rightarrow a} \llbracket x \rrbracket$ exist?
56. Let $f(x)=\llbracket \cos x \rrbracket,-\pi \leqslant x \leqslant \pi$.
    (a) Sketch the graph of $f$.
    (b) Evaluate each limit, if it exists.
(i) $\lim _{x \rightarrow 0} f(x)$
(ii) $\lim _{x \rightarrow(\pi / 2)^{-}} f(x)$
(iii) $\lim _{x \rightarrow(\pi / 2)^{+}} f(x)$
(iv) $\lim _{x \rightarrow \pi / 2} f(x)$

    (c) For what values of $a$ does $\lim _{x \rightarrow a} f(x)$ exist?
57. If $f(x)=\llbracket x \rrbracket+\llbracket-x \rrbracket$, show that $\lim _{x \rightarrow 2} f(x)$ exists but is not equal to $f(2)$.
58. In the theory of relativity, the Lorentz contraction formula
$$
L=L_{0} \sqrt{1-v^{2} / c^{2}}
$$
expresses the length $L$ of an object as a function of its velocity $v$ with respect to an observer, where $L_{0}$ is the length of the object at rest and $c$ is the speed of light. Find $\lim _{v \rightarrow c^{-}} L$ and interpret the result. Why is a left-hand limit necessary?
59. If $p$ is a polynomial, show that $\lim _{x \rightarrow a} p(x)=p(a)$.
60. If $r$ is a rational function, use Exercise 59 to show that $\lim _{x \rightarrow a} r(x)=r(a)$ for every number $a$ in the domain of $r$.
61. If $\lim _{x \rightarrow 1} \frac{f(x)-8}{x-1}=10$, find $\lim _{x \rightarrow 1} f(x)$.
62. If $\lim _{x \rightarrow 0} \frac{f(x)}{x^{2}}=5$, find the following limits.
(a) $\lim _{x \rightarrow 0} f(x)$
(b) $\lim _{x \rightarrow 0} \frac{f(x)}{x}$
63. If
$$
f(x)= \begin{cases}x^{2} & \text { if } x \text { is rational } \\ 0 & \text { if } x \text { is irrational }\end{cases}
$$
prove that $\lim _{x \rightarrow 0} f(x)=0$.
64. Show by means of an example that $\lim _{x \rightarrow a}[f(x)+g(x)]$ may exist even though neither $\lim _{x \rightarrow a} f(x)$ nor $\lim _{x \rightarrow a} g(x)$ exists.
65. Show by means of an example that $\lim _{x \rightarrow a}[f(x) g(x)]$ may exist even though neither $\lim _{x \rightarrow a} f(x)$ nor $\lim _{x \rightarrow a} g(x)$ exists.
66. Evaluate $\lim _{x \rightarrow 2} \frac{\sqrt{6-x}-2}{\sqrt{3-x}-1}$.
67. Is there a number $a$ such that
$$
\lim _{x \rightarrow-2} \frac{3 x^{2}+a x+a+3}{x^{2}+x-2}
$$
exists? If so, find the value of $a$ and the value of the limit.
68. The figure shows a fixed circle $C_{1}$ with equation $(x-1)^{2}+y^{2}=1$ and a shrinking circle $C_{2}$ with radius $r$ and center the origin. $P$ is the point $(0, r), Q$ is the upper point of intersection of the two circles, and $R$ is the point of intersection of the line $P Q$ and the $x$-axis. What happens to $R$ as $C_{2}$ shrinks, that is, as $r \rightarrow 0^{+}$?
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0139.jpg?height=414&width=677&top_left_y=1953&top_left_x=1124)

### 2.4 The Precise Definition of a Limit

The intuitive definition of a limit given in Section 2.2 is inadequate for some purposes because such phrases as " $x$ is close to 2 " and " $f(x)$ gets closer and closer to $L$ " are vague. In order to be able to prove conclusively that

$$
\lim _{x \rightarrow 0}\left(x^{3}+\frac{\cos 5 x}{10,000}\right)=0.0001 \quad \text { or } \quad \lim _{x \rightarrow 0} \frac{\sin x}{x}=1
$$

we must make the definition of a limit precise.

## ■ The Precise Definition of a Limit

To motivate the precise definition of a limit, let's consider the function

$$
f(x)= \begin{cases}2 x-1 & \text { if } x \neq 3 \\ 6 & \text { if } x=3\end{cases}
$$

Intuitively, it is clear that when $x$ is close to 3 but $x \neq 3$, then $f(x)$ is close to 5 , and so $\lim _{x \rightarrow 3} f(x)=5$.

To obtain more detailed information about how $f(x)$ varies when $x$ is close to 3 , we ask the following question:
> How close to 3 does $x$ have to be so that $f(x)$ differs from 5 by less than 0.1?
The distance from $x$ to 3 is $|x-3|$ and the distance from $f(x)$ to 5 is $|f(x)-5|$, so our problem is to find a number $\delta$ (the Greek letter delta) such that

$$
|f(x)-5|<0.1 \quad \text { if } \quad|x-3|<\delta \quad \text { but } x \neq 3
$$

If $|x-3|>0$, then $x \neq 3$, so an equivalent formulation of our problem is to find a number $\delta$ such that

$$
|f(x)-5|<0.1 \quad \text { if } \quad 0<|x-3|<\delta
$$

Notice that if $0<|x-3|<(0.1) / 2=0.05$, then

$$
|f(x)-5|=|(2 x-1)-5|=|2 x-6|=2|x-3|<2(0.05)=0.1
$$

that is,

$$
|f(x)-5|<0.1 \quad \text { if } \quad 0<|x-3|<0.05
$$

Thus an answer to the problem is given by $\delta=0.05$; that is, if $x$ is within a distance of 0.05 from 3, then $f(x)$ will be within a distance of 0.1 from 5.

If we change the number 0.1 in our problem to the smaller number 0.01, then by using the same method we find that $f(x)$ will differ from 5 by less than 0.01 provided that $x$ differs from 3 by less than $(0.01) / 2=0.005$ :

$$
|f(x)-5|<0.01 \quad \text { if } \quad 0<|x-3|<0.005
$$

Similarly,

$$
|f(x)-5|<0.001 \quad \text { if } \quad 0<|x-3|<0.0005
$$

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0141.jpg?height=516&width=504&top_left_y=604&top_left_x=119)
FIGURE 1

It is traditional to use the Greek letters $\varepsilon$ and $\delta$ in the precise definition of a limit.

The numbers 0.1, 0.01, and 0.001 that we have considered are error tolerances that we might allow. For 5 to be the precise limit of $f(x)$ as $x$ approaches 3, we must not only be able to bring the difference between $f(x)$ and 5 below each of these three numbers; we must be able to bring it below any positive number. And, by the same reasoning, we can! If we write $\varepsilon$ (the Greek letter epsilon) for an arbitrary positive number, then we find as before that

1

$$
|f(x)-5|<\varepsilon \quad \text { if } \quad 0<|x-3|<\delta=\frac{\varepsilon}{2}
$$

This is a precise way of saying that $f(x)$ is close to 5 when $x$ is close to 3 because (1) says that we can make the values of $f(x)$ within an arbitrary distance $\varepsilon$ from 5 by restricting the values of $x$ to be within a distance $\varepsilon / 2$ from 3 (but $x \neq 3$ ).

Note that (1) can be rewritten as follows:

$$
\text { if } \quad 3-\delta<x<3+\delta \quad(x \neq 3) \quad \text { then } \quad 5-\varepsilon<f(x)<5+\varepsilon
$$

and this is illustrated in Figure 1. By taking the values of $x(\neq 3)$ to lie in the interval $(3-\delta, 3+\delta)$ we can make the values of $f(x)$ lie in the interval $(5-\varepsilon, 5+\varepsilon)$.

Using (1) as a model, we give a precise definition of a limit.

2 Precise Definition of a Limit Let $f$ be a function defined on some open interval that contains the number $a$, except possibly at $a$ itself. Then we say that the limit of $\boldsymbol{f}(\boldsymbol{x})$ as $\boldsymbol{x}$ approaches $\boldsymbol{a}$ is $\boldsymbol{L}$, and we write

$$
\lim _{x \rightarrow a} f(x)=L
$$

if for every number $\varepsilon>0$ there is a number $\delta>0$ such that

$$
\text { if } \quad 0<|x-a|<\delta \quad \text { then } \quad|f(x)-L|<\varepsilon
$$

Since $|x-a|$ is the distance from $x$ to $a$ and $|f(x)-L|$ is the distance from $f(x)$ to $L$, and since $\varepsilon$ can be arbitrarily small, the definition of a limit can be expressed in words as follows:
$\lim _{x \rightarrow a} f(x)=L$ means that the distance between $f(x)$ and $L$ can be made arbitrarily small by requiring that the distance from $x$ to $a$ be sufficiently small (but not 0 ).

Alternatively,
$\lim _{x \rightarrow a} f(x)=L$ means that the values of $f(x)$ can be made as close as we please to $L$ by requiring $x$ to be close enough to $a$ (but not equal to $a$ ).

We can also reformulate Definition 2 in terms of intervals by observing that the inequality $|x-a|<\delta$ is equivalent to $-\delta<x-a<\delta$, which in turn can be written as $a-\delta<x<a+\delta$. Also $0<|x-a|$ is true if and only if $x-a \neq 0$, that is, $x \neq a$. Similarly, the inequality $|f(x)-L|<\varepsilon$ is equivalent to the pair of inequalities $L-\varepsilon<f(x)<L+\varepsilon$. Therefore, in terms of intervals, Definition 2 can be stated as follows:
$\lim _{x \rightarrow a} f(x)=L$ means that for every $\varepsilon>0$ (no matter how small $\varepsilon$ is) we can find $\delta>0$ such that if $x$ lies in the open interval $(a-\delta, a+\delta)$ and $x \neq a$, then $f(x)$ lies in the open interval $(L-\varepsilon, L+\varepsilon)$.

We interpret this statement geometrically by representing a function by an arrow diagram as in Figure 2, where $f$ maps a subset of $\mathbb{R}$ onto another subset of $\mathbb{R}$.

FIGURE 2
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0142.jpg?height=176&width=1062&top_left_y=355&top_left_x=860)

The definition of limit says that if any small interval $(L-\varepsilon, L+\varepsilon)$ is given around $L$, then we can find an interval $(a-\delta, a+\delta)$ around $a$ such that $f$ maps all the points in $(a-\delta, a+\delta)$ (except possibly $a$ ) into the interval ( $L-\varepsilon, L+\varepsilon$ ). (See Figure 3.)

FIGURE 3
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0142.jpg?height=183&width=1064&top_left_y=790&top_left_x=859)

Another geometric interpretation of limits can be given in terms of the graph of a function. If $\varepsilon>0$ is given, then we draw the horizontal lines $y=L+\varepsilon$ and $y=L-\varepsilon$ and the graph of $f$. (See Figure 4.) If $\lim _{x \rightarrow a} f(x)=L$, then we can find a number $\delta>0$ such that if we restrict $x$ to lie in the interval $(a-\delta, a+\delta)$ and take $x \neq a$, then the curve $y=f(x)$ lies between the lines $y=L-\varepsilon$ and $y=L+\varepsilon$. (See Figure 5.) You can see that if such a $\delta$ has been found, then any smaller $\delta$ will also work.

It is important to realize that the process illustrated in Figures 4 and 5 must work for every positive number $\varepsilon$, no matter how small it is chosen. Figure 6 shows that if a smaller $\varepsilon$ is chosen, then a smaller $\delta$ may be required.

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0142.jpg?height=417&width=470&top_left_y=1481&top_left_x=244)
FIGURE 4

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0142.jpg?height=511&width=555&top_left_y=1500&top_left_x=838)
FIGURE 5

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0142.jpg?height=415&width=519&top_left_y=1502&top_left_x=1485)
FIGURE 6

EXAMPLE 1 Since $f(x)=x^{3}-5 x+6$ is a polynomial, we know from the Direct Substitution Property that $\lim _{x \rightarrow 1} f(x)=f(1)=1^{3}-5(1)+6=2$. Use a graph to find a number $\delta$ such that if $x$ is within $\delta$ of 1 , then $y$ is within 0.2 of 2 , that is,

$$
\text { if } \quad|x-1|<\delta \quad \text { then } \quad\left|\left(x^{3}-5 x+6\right)-2\right|<0.2
$$

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0143.jpg?height=326&width=458&top_left_y=292&top_left_x=120)
FIGURE 7

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0143.jpg?height=328&width=482&top_left_y=739&top_left_x=119)
FIGURE 8

In other words, find a number $\delta$ that corresponds to $\varepsilon=0.2$ in the definition of a limit for the function $f(x)=x^{3}-5 x+6$ with $a=1$ and $L=2$.

SOLUTION A graph of $f$ is shown in Figure 7; we are interested in the region near the point (1, 2). Notice that we can rewrite the inequality

$$
\left|\left(x^{3}-5 x+6\right)-2\right|<0.2
$$

as

$$
-0.2<\left(x^{3}-5 x+6\right)-2<0.2
$$

or equivalently

$$
1.8<x^{3}-5 x+6<2.2
$$

So we need to determine the values of $x$ for which the curve $y=x^{3}-5 x+6$ lies between the horizontal lines $y=1.8$ and $y=2.2$. Therefore we graph the curves $y=x^{3}-5 x+6, y=1.8$, and $y=2.2$ near the point $(1,2)$ in Figure 8. We estimate that the $x$-coordinate of the point of intersection of the line $y=2.2$ and the curve $y=x^{3}-5 x+6$ is about 0.911. Similarly, $y=x^{3}-5 x+6$ intersects the line $y=1.8$ when $x \approx 1.124$. So, rounding toward 1 to be safe, we can say that

$$
\text { if } \quad 0.92<x<1.12 \quad \text { then } \quad 1.8<x^{3}-5 x+6<2.2
$$

This interval (0.92, 1.12) is not symmetric about $x=1$. The distance from $x=1$ to the left endpoint is $1-0.92=0.08$ and the distance to the right endpoint is 0.12 . We can choose $\delta$ to be the smaller of these numbers, that is, $\delta=0.08$. Then we can rewrite our inequalities in terms of distances as follows:

$$
\text { if } \quad|x-1|<0.08 \quad \text { then } \quad\left|\left(x^{3}-5 x+6\right)-2\right|<0.2
$$

This just says that by keeping $x$ within 0.08 of 1, we are able to keep $f(x)$ within 0.2 of 2.

Although we chose $\delta=0.08$, any smaller positive value of $\delta$ would also have worked. $\square$

The graphical procedure used in Example 1 gives an illustration of the definition for $\varepsilon=0.2$, but it does not prove that the limit is equal to 2 . A proof has to provide a $\delta$ for every $\varepsilon$.

In proving limit statements it may be helpful to think of the definition of limit as a challenge. First it challenges you with a number $\boldsymbol{\varepsilon}$. Then you must be able to produce a suitable $\delta$. You have to be able to do this for every $\varepsilon>0$, not just a particular $\varepsilon$.

Imagine a contest between two people, A and B, and imagine yourself to be B. Person A stipulates that the fixed number $L$ should be approximated by the values of $f(x)$ to within a degree of accuracy $\varepsilon$ (say, 0.01 ). Person B then responds by finding a number $\delta$ such that if $0<|x-a|<\delta$, then $|f(x)-L|<\varepsilon$. Then A may become more exacting and challenge B with a smaller value of $\varepsilon$ (say, 0.0001). Again B has to respond by finding a corresponding $\delta$. Usually the smaller the value of $\varepsilon$, the smaller the corresponding value of $\delta$ must be. If B always wins, no matter how small A makes $\varepsilon$, then $\lim _{x \rightarrow a} f(x)=L$.

EXAMPLE 2 Prove that $\lim _{x \rightarrow 3}(4 x-5)=7$.
SOLUTION

1. Preliminary analysis of the problem (guessing a value for $\delta$ ). Let $\varepsilon$ be a given positive number. We want to find a number $\delta$ such that

$$
\text { if } \quad 0<|x-3|<\delta \quad \text { then } \quad|(4 x-5)-7|<\varepsilon
$$

## Cauchy and Limits

After the invention of calculus in the 17th century, there followed a period of free development of the subject in the 18th century. Mathematicians like the Bernoulli brothers and Euler were eager to exploit the power of calculus and boldly explored the consequences of this new and wonderful mathematical theory without worrying too much about whether their proofs were completely correct.

The 19th century, by contrast, was the Age of Rigor in mathematics. There was a movement to go back to the foundations of the subject-to provide careful definitions and igorous proofs. At the forefront of this movement was the French mathematician Augustin-Louis Cauchy (1789-1857), who started out as a military engineer before becoming a mathematics professor in Paris. Cauchy took Newton's idea of a limit, which was kept alive in the 18th century by the French mathematician Jean d'Alembert, and made it more precise. His definition of a limit eads as follows: "When the successive values attributed to a variable approach indefini ely a fi ed value so as to end by differing from it by as little as one wishes, this last is called the limit of all the others." But when Cauchy used this definition in xamples and proofs, he often employed delta-epsilon inequalities similar to the ones in this section. A typical Cauchy proof starts with: "Designate by $\delta$ and $\varepsilon$ two very small numbers; ..." He used $\varepsilon$ because of the correspondence between epsiIon and the French word erreur and $\delta$ because delta corresponds to différence. Later, the German mathematician Karl Weierstrass (1815-1897) stated the definition of a limit xactly as in our Definition 2

But $|(4 x-5)-7|=|4 x-12|=|4(x-3)|=4|x-3|$. Therefore we want $\delta$ such that

$$
\text { if } \quad 0<|x-3|<\delta \quad \text { then } \quad 4|x-3|<\varepsilon
$$

that is, if $\quad 0<|x-3|<\delta \quad$ then $\quad|x-3|<\frac{\varepsilon}{4}$
This suggests that we should choose $\delta=\varepsilon / 4$.
2. Proof (showing that this $\delta$ works). Given $\varepsilon>0$, choose $\delta=\varepsilon / 4$. If $0<|x-3|<\delta$, then

$$
|(4 x-5)-7|=|4 x-12|=4|x-3|<4 \delta=4\left(\frac{\varepsilon}{4}\right)=\varepsilon
$$

Thus if $0<|x-3|<\delta \quad$ then $\quad|(4 x-5)-7|<\varepsilon$

Therefore, by the definition of a limit,

$$
\lim _{x \rightarrow 3}(4 x-5)=7
$$

This example is illustrated by Figure 9.

FIGURE 9
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0144.jpg?height=509&width=465&top_left_y=1059&top_left_x=1148)

Note that in the solution of Example 2 there were two stages-guessing and proving. We made a preliminary analysis that enabled us to guess a value for $\delta$. But then in the second stage we had to go back and prove in a careful, logical fashion that we had made a correct guess. This procedure is typical of much of mathematics. Sometimes it is necessary to first make an intelligent guess about the answer to a problem and then prove that the guess is correct.

EXAMPLE 3 Prove that $\lim _{x \rightarrow 3} x^{2}=9$.
SOLUTION

1. Guessing a value for $\delta$. Let $\varepsilon>0$ be given. We have to find a number $\delta>0$ such that

$$
\text { if } \quad 0<|x-3|<\delta \quad \text { then } \quad\left|x^{2}-9\right|<\varepsilon
$$

To connect $\left|x^{2}-9\right|$ with $|x-3|$ we write $\left|x^{2}-9\right|=|(x+3)(x-3)|$. Then we want

$$
\text { if } \quad 0<|x-3|<\delta \quad \text { then } \quad|x+3||x-3|<\varepsilon
$$

Notice that if we can find a positive constant $C$ such that $|x+3|<C$, then

$$
|x+3||x-3|<C|x-3|
$$

and we can make $C|x-3|<\varepsilon$ by taking $|x-3|<\varepsilon / C$, so we could choose $\delta=\varepsilon / C$.

We can find such a number $C$ if we restrict $x$ to lie in some interval centered at 3 . In fact, since we are interested only in values of $x$ that are close to 3, it is reasonable to assume that $x$ is within a distance 1 from 3 , that is, $|x-3|<1$. Then $2<x<4$, so $5<x+3<7$. Thus we have $|x+3|<7$, and so $C=7$ is a suitable choice for the constant.

But now there are two restrictions on $|x-3|$, namely

$$
|x-3|<1 \quad \text { and } \quad|x-3|<\frac{\varepsilon}{C}=\frac{\varepsilon}{7}
$$

To make sure that both of these inequalities are satisfied, we take $\delta$ to be the smaller of the two numbers 1 and $\varepsilon / 7$. The notation for this is $\delta=\min \{1, \varepsilon / 7\}$.
2. Showing that this $\delta$ works. Given $\varepsilon>0$, let $\delta=\min \{1, \varepsilon / 7\}$. If $0<|x-3|<\delta$, then $|x-3|<1 \Rightarrow 2<x<4 \Rightarrow|x+3|<7$ (as in part 1). We also have $|x-3|<\varepsilon / 7$, so

$$
\left|x^{2}-9\right|=|x+3||x-3|<7 \cdot \frac{\varepsilon}{7}=\varepsilon
$$

This shows that $\lim _{x \rightarrow 3} x^{2}=9$. $\square$

## ■ One-Sided Limits

The intuitive definitions of one-sided limits that were given in Section 2.2 can be precisely reformulated as follows.

3 Precise Definition of Left-Hand Limit

$$
\lim _{x \rightarrow a^{-}} f(x)=L
$$

if for every number $\varepsilon>0$ there is a number $\delta>0$ such that

$$
\text { if } \quad a-\delta<x<a \quad \text { then } \quad|f(x)-L|<\varepsilon
$$

4 Precise Definition of Right-Hand Limit

$$
\lim _{x \rightarrow a^{+}} f(x)=L
$$

if for every number $\varepsilon>0$ there is a number $\delta>0$ such that

$$
\text { if } \quad a<x<a+\delta \quad \text { then } \quad|f(x)-L|<\varepsilon
$$

Notice that Definition 3 is the same as Definition 2 except that $x$ is restricted to lie in the left half $(a-\delta, a)$ of the interval $(a-\delta, a+\delta)$. In Definition 4, $x$ is restricted to lie in the right half $(a, a+\delta)$ of the interval $(a-\delta, a+\delta)$.

EXAMPLE 4 Use Definition 4 to prove that $\lim _{x \rightarrow 0^{+}} \sqrt{x}=0$.
SOLUTION

1. Guessing a value for $\delta$. Let $\varepsilon$ be a given positive number. Here $a=0$ and $L=0$, so we want to find a number $\delta$ such that
that is,

$$
\begin{array}{lll}
\text { if } & 0<x<\delta & \text { then } \\
\text { if } & |\sqrt{x}-0|<\varepsilon \\
& 0<x<\delta & \text { then } \\
& \sqrt{x}<\varepsilon
\end{array}
$$

or, squaring both sides of the inequality $\sqrt{x}<\varepsilon$, we get

$$
\text { if } \quad 0<x<\delta \quad \text { then } \quad x<\varepsilon^{2}
$$

This suggests that we should choose $\delta=\varepsilon^{2}$.
2. Showing that this $\delta$ works. Given $\varepsilon>0$, let $\delta=\varepsilon^{2}$. If $0<x<\delta$, then
so

$$
\begin{gathered}
\sqrt{x}<\sqrt{\delta}=\sqrt{\varepsilon^{2}}=\varepsilon \\
|\sqrt{x}-0|<\varepsilon
\end{gathered}
$$

According to Definition 4, this shows that $\lim _{x \rightarrow 0^{+}} \sqrt{x}=0$. $\square$

■ The Limit Laws
As the preceding examples show, it is not always easy to prove that limit statements are true using the $\varepsilon, \delta$ definition. In fact, if we had been given a more complicated function such as $f(x)=\left(6 x^{2}-8 x+9\right) /\left(2 x^{2}-1\right)$, a proof would require a great deal of ingenuity. Fortunately this is unnecessary because the Limit Laws stated in Section 2.3 can be proved using Definition 2, and then the limits of complicated functions can be found rigorously from the Limit Laws without resorting to the definition directly.

For instance, we prove the Sum Law: If $\lim _{x \rightarrow a} f(x)=L$ and $\lim _{x \rightarrow a} g(x)=M$ both exist, then

$$
\lim _{x \rightarrow a}[f(x)+g(x)]=L+M
$$

The remaining laws are proved in the exercises and in Appendix F.
PROOF OF THE SUM LAW Let $\varepsilon>0$ be given. We must find $\delta>0$ such that

$$
\text { if } \quad 0<|x-a|<\delta \quad \text { then } \quad|f(x)+g(x)-(L+M)|<\varepsilon
$$

Using the Triangle Inequality we can write
5

$$
\begin{aligned}
|f(x)+g(x)-(L+M)| & =|(f(x)-L)+(g(x)-M)| \\
& \leqslant|f(x)-L|+|g(x)-M|
\end{aligned}
$$

We make $|f(x)+g(x)-(L+M)|$ less than $\varepsilon$ by making each of the terms $|f(x)-L|$ and $|g(x)-M|$ less than $\varepsilon / 2$.

Since $\varepsilon / 2>0$ and $\lim _{x \rightarrow a} f(x)=L$, there exists a number $\delta_{1}>0$ such that

$$
\text { if } \quad 0<|x-a|<\delta_{1} \quad \text { then } \quad|f(x)-L|<\frac{\varepsilon}{2}
$$

Similarly, since $\lim _{x \rightarrow a} g(x)=M$, there exists a number $\delta_{2}>0$ such that

$$
\text { if } \quad 0<|x-a|<\delta_{2} \quad \text { then } \quad|g(x)-M|<\frac{\varepsilon}{2}
$$

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0147.jpg?height=400&width=463&top_left_y=1399&top_left_x=119)
FIGURE 10

Let $\delta=\min \left\{\delta_{1}, \delta_{2}\right\}$, the smaller of the numbers $\delta_{1}$ and $\delta_{2}$. Notice that if $\quad 0<|x-a|<\delta \quad$ then $\quad 0<|x-a|<\delta_{1} \quad$ and $\quad 0<|x-a|<\delta_{2}$ and so

$$
|f(x)-L|<\frac{\varepsilon}{2} \quad \text { and } \quad|g(x)-M|<\frac{\varepsilon}{2}
$$

Therefore, by (5),

$$
\begin{aligned}
|f(x)+g(x)-(L+M)| & \leqslant|f(x)-L|+|g(x)-M| \\
& <\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon
\end{aligned}
$$

To summarize,

$$
\text { if } \quad 0<|x-a|<\delta \quad \text { then } \quad|f(x)+g(x)-(L+M)|<\varepsilon
$$

Thus, by the definition of a limit,

$$
\lim _{x \rightarrow a}[f(x)+g(x)]=L+M
$$ $\square$

## ■ Infinite Limits

Infinite limits can also be defined in a precise way. The following is a precise version of Definition 2.2.4.

6 Precise Definition of an Infinite Limit Let $f$ be a function defined on some open interval that contains the number $a$, except possibly at $a$ itself. Then

$$
\lim _{x \rightarrow a} f(x)=\infty
$$

means that for every positive number $M$ there is a positive number $\delta$ such that

$$
\text { if } \quad 0<|x-a|<\delta \quad \text { then } \quad f(x)>M
$$

This says that the values of $f(x)$ can be made arbitrarily large (larger than any given number $M$ ) by requiring $x$ to be close enough to $a$ (within a distance $\delta$, where $\delta$ depends on $M$, but with $x \neq a$ ). A geometric illustration is shown in Figure 10.

Given any horizontal line $y=M$, we can find a number $\delta>0$ such that if we restrict $x$ to lie in the interval $(a-\delta, a+\delta)$ but $x \neq a$, then the curve $y=f(x)$ lies above the line $y=M$. You can see that if a larger $M$ is chosen, then a smaller $\delta$ may be required.

EXAMPLE 5 Use Definition 6 to prove that $\lim _{x \rightarrow 0} \frac{1}{x^{2}}=\infty$.
SOLUTION Let $M$ be a given positive number. We want to find a number $\delta$ such that

$$
\text { if } \quad 0<|x|<\delta \quad \text { then } \quad 1 / x^{2}>M
$$

But $\quad \frac{1}{x^{2}}>M \quad \Longleftrightarrow \quad x^{2}<\frac{1}{M} \quad \Longleftrightarrow \quad \sqrt{x^{2}}<\sqrt{\frac{1}{M}} \quad \Longleftrightarrow \quad|x|<\frac{1}{\sqrt{M}}$
So if we choose $\delta=1 / \sqrt{M}$ and $0<|x|<\delta=1 / \sqrt{M}$, then $1 / x^{2}>M$. This shows that $1 / x^{2} \rightarrow \infty$ as $x \rightarrow 0$. $\square$

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0148.jpg?height=357&width=462&top_left_y=223&top_left_x=243)
FIGURE 11

Similarly, the following is a precise version of Definition 2.2.5. It is illustrated by Figure 11.

7 Definition Let $f$ be a function defined on some open interval that contains the number $a$, except possibly at $a$ itself. Then

$$
\lim _{x \rightarrow a} f(x)=-\infty
$$

means that for every negative number $N$ there is a positive number $\delta$ such that

$$
\text { if } \quad 0<|x-a|<\delta \quad \text { then } \quad f(x)<N
$$

### 2.4 Exercises

1. Use the given graph of $f$ to find a number $\delta$ such that
if $\quad|x-1|<\delta \quad$ then $\quad|f(x)-1|<0.2$
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0148.jpg?height=343&width=419&top_left_y=985&top_left_x=458)
2. Use the given graph of $f$ to find a number $\delta$ such that
if $\quad 0<|x-3|<d \quad$ then $\quad|f(x)-2|<0.5$
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0148.jpg?height=357&width=512&top_left_y=1506&top_left_x=412)
3. Use the given graph of $f(x)=\sqrt{x}$ to find a number $\delta$ such that
if $\quad|x-4|<\delta \quad$ then $\quad|\sqrt{x}-2|<0.4$
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0148.jpg?height=280&width=512&top_left_y=2081&top_left_x=412)
4. Use the given graph of $f(x)=x^{2}$ to find a number $\delta$ such that
if $\quad|x-1|<\delta \quad$ then $\quad\left|x^{2}-1\right|<\frac{1}{2}$
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0148.jpg?height=345&width=510&top_left_y=999&top_left_x=1329)
5. Use a graph to find a number $\delta$ such that
if $\quad|x-2|<\delta \quad$ then $\quad\left|\sqrt{x^{2}+5}-3\right|<0.3$
6. Use a graph to find a number $\delta$ such that
if $\quad\left|x-\frac{\pi}{6}\right|<\delta \quad$ then $\quad\left|\cos ^{2} x-\frac{3}{4}\right|<0.1$
7. For the limit
$$
\lim _{x \rightarrow 2}\left(x^{3}-3 x+4\right)=6
$$
illustrate Definition 2 by finding values of $\delta$ that correspond to $\varepsilon=0.2$ and $\varepsilon=0.1$.
8. For the limit
$$
\lim _{x \rightarrow 0} \frac{e^{2 x}-1}{x}=2
$$
illustrate Definition 2 by finding values of $\delta$ that correspond to $\varepsilon=0.5$ and $\varepsilon=0.1$.
9. (a) Use a graph to find a number $\delta$ such that
    if $\quad 2<x<2+\delta \quad$ then $\quad \frac{1}{\ln (x-1)}>100$

    (b) What limit does part (a) suggest is true?

10. Given that $\lim _{x \rightarrow \pi} \csc ^{2} x=\infty$, illustrate Definition 6 by finding values of $\delta$ that correspond to (a) $M=500$ and (b) $M=1000$.
11. A machinist is required to manufacture a circular metal disk with area $1000 \mathrm{~cm}^{2}$.
    (a) What radius produces such a disk?
    (b) If the machinist is allowed an error tolerance of $\pm 5 \mathrm{~cm}^{2}$ in the area of the disk, how close to the ideal radius in part (a) must the machinist control the radius?
    (c) In terms of the $\varepsilon, \delta$ definition of $\lim _{x \rightarrow a} f(x)=L$, what is $x$ ? What is $f(x)$ ? What is $a$ ? What is $L$ ? What value of $\varepsilon$ is given? What is the corresponding value of $\delta$ ?
12. Crystal growth furnaces are used in research to determine how best to manufacture crystals used in electronic components. For proper growth of a crystal, the temperature must be controlled accurately by adjusting the input power. Suppose the relationship is given by
$$
T(w)=0.1 w^{2}+2.155 w+20
$$
where $T$ is the temperature in degrees Celsius and $w$ is the power input in watts.
    (a) How much power is needed to maintain the temperature at 200°C?
    (b) If the temperature is allowed to vary from 200°C by up to ±1°C, what range of wattage is allowed for the input power?
    (c) In terms of the $\varepsilon, \delta$ definition of $\lim _{x \rightarrow a} f(x)=L$, what is $x$ ? What is $f(x)$ ? What is $a$ ? What is $L$ ? What value of $\varepsilon$ is given? What is the corresponding value of $\delta$ ?
13. (a) Find a number $\delta$ such that if $|x-2|<\delta$, then $|4 x-8|<\varepsilon$, where $\varepsilon=0.1$.
    (b) Repeat part (a) with $\varepsilon=0.01$.
14. Given that $\lim _{x \rightarrow 2}(5 x-7)=3$, illustrate Definition 2 by finding values of $\delta$ that correspond to $\varepsilon=0.1, \varepsilon=0.05$, and $\varepsilon=0.01$.

15-18 Prove the statement using the $\varepsilon, \delta$ definition of a limit and illustrate with a diagram like Figure 9.
15. $\lim _{x \rightarrow 4}\left(\frac{1}{2} x-1\right)=1$
16. $\lim _{x \rightarrow 2}(2-3 x)=-4$
17. $\lim _{x \rightarrow-2}(-2 x+1)=5$
18. $\lim _{x \rightarrow 1}(2 x-5)=-3$

19-32 Prove the statement using the $\varepsilon, \delta$ definition of a limit.
19. $\lim _{x \rightarrow 9}\left(1-\frac{1}{3} x\right)=-2$
20. $\lim _{x \rightarrow 5}\left(\frac{3}{2} x-\frac{1}{2}\right)=7$
21. $\lim _{x \rightarrow 4} \frac{x^{2}-2 x-8}{x-4}=6$
22. $\lim _{x \rightarrow-1.5} \frac{9-4 x^{2}}{3+2 x}=6$
23. $\lim _{x \rightarrow a} x=a$
24. $\lim _{x \rightarrow a} c=c$
25. $\lim _{x \rightarrow 0} x^{2}=0$
26. $\lim _{x \rightarrow 0} x^{3}=0$
27. $\lim _{x \rightarrow 0}|x|=0$
28. $\lim _{x \rightarrow-6^{+}} \sqrt[8]{6+x}=0$
29. $\lim _{x \rightarrow 2}\left(x^{2}-4 x+5\right)=1$
30. $\lim _{x \rightarrow 2}\left(x^{2}+2 x-7\right)=1$
31. $\lim _{x \rightarrow-2}\left(x^{2}-1\right)=3$
32. $\lim _{x \rightarrow 2} x^{3}=8$

33. Verify that another possible choice of $\delta$ for showing that $\lim _{x \rightarrow 3} x^{2}=9$ in Example 3 is $\delta=\min \{2, \varepsilon / 8\}$.
34. Verify, by a geometric argument, that the largest possible choice of $\delta$ for showing that $\lim _{x \rightarrow 3} x^{2}=9$ is $\delta=\sqrt{9+\varepsilon}-3$.
T 35. (a) For the $\operatorname{limit~}_{\lim _{x \rightarrow 1}}\left(x^{3}+x+1\right)=3$, use a graph to find a value of $\delta$ that corresponds to $\varepsilon=0.4$.
    (b) By solving the cubic equation $x^{3}+x+1=3+\varepsilon$, find the largest possible value of $\delta$ that works for any given $\varepsilon>0$.
    (c) Put $\varepsilon=0.4$ in your answer to part (b) and compare with your answer to part (a).
36. Prove that $\lim _{x \rightarrow 2} \frac{1}{x}=\frac{1}{2}$.
37. Prove that $\lim _{x \rightarrow a} \sqrt{x}=\sqrt{a}$ if $a>0$.
$$
\left[\text { Hint: Use }|\sqrt{x}-\sqrt{a}|=\frac{|x-a|}{\sqrt{x}+\sqrt{a}} .\right]
$$
38. If $H$ is the Heaviside function defined in Section 2.2, prove, using Definition 2, that $\lim _{t \rightarrow 0} H(t)$ does not exist. [Hint: Use an indirect proof as follows. Suppose that the limit is $L$. Take $\varepsilon=\frac{1}{2}$ in the definition of a limit and try to arrive at a contradiction.]
39. If the function $f$ is defined by
$$
f(x)= \begin{cases}0 & \text { if } x \text { is rational } \\ 1 & \text { if } x \text { is irrational }\end{cases}
$$
prove that $\lim _{x \rightarrow 0} f(x)$ does not exist.
40. By comparing Definitions 2, 3, and 4, prove Theorem 2.3.1: $\lim _{x \rightarrow a} f(x)=L \quad$ if and only if $\quad \lim _{x \rightarrow a^{-}} f(x)=L=\lim _{x \rightarrow a^{+}} f(x)$
41. How close to -3 do we have to take $x$ so that
$$
\frac{1}{(x+3)^{4}}>10,000
$$
42. Prove, using Definition 6, that $\lim _{x \rightarrow-3} \frac{1}{(x+3)^{4}}=\infty$.
43. Prove that $\lim _{x \rightarrow 0^{+}} \ln x=-\infty$.
44. Suppose that $\lim _{x \rightarrow a} f(x)=\infty$ and $\lim _{x \rightarrow a} g(x)=c$, where $c$ is a real number. Prove each statement.
    (a) $\lim _{x \rightarrow a}[f(x)+g(x)]=\infty$
    (b) $\lim _{x \rightarrow a}[f(x) g(x)]=\infty$ if $c>0$
    (c) $\lim _{x \rightarrow a}[f(x) g(x)]=-\infty$ if $c<0$

### 2.5 Continuity

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0150.jpg?height=421&width=469&top_left_y=1115&top_left_x=244)
FIGURE 1

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0150.jpg?height=354&width=457&top_left_y=1741&top_left_x=242)
FIGURE 2

■ Continuity of a Function
We noticed in Section 2.3 that the limit of a function as $x$ approaches $a$ can often be found simply by calculating the value of the function at $a$. Functions having this property are called continuous at $a$. We will see that the mathematical definition of continuity corresponds closely with the meaning of the word continuity in everyday language. (A continuous process is one that takes place without interruption.)

1 Definition A function $f$ is continuous at a number $\boldsymbol{a}$ if

$$
\lim _{x \rightarrow a} f(x)=f(a)
$$

Notice that Definition 1 implicitly requires three things if $f$ is continuous at $a$ :

1. $f(a)$ is defined (that is, $a$ is in the domain of $f$ )
2. $\lim _{x \rightarrow a} f(x)$ exists
3. $\lim _{x \rightarrow a} f(x)=f(a)$

The definition says that $f$ is continuous at $a$ if $f(x)$ approaches $f(a)$ as $x$ approaches $a$. Thus a continuous function $f$ has the property that a small change in $x$ produces only a small change in $f(x)$. In fact, the change in $f(x)$ can be kept as small as we please by keeping the change in $x$ sufficiently small.

If $f$ is defined near $a$ (in other words, $f$ is defined on an open interval containing $a$, except perhaps at $a$ ), we say that $f$ is discontinuous at $\boldsymbol{a}$ (or $f$ has a discontinuity at $a$ ) if $f$ is not continuous at $a$.

Physical phenomena are usually continuous. For instance, the displacement or velocity of a moving vehicle varies continuously with time, as does a person's height. But discontinuities do occur in such situations as electric currents. [The Heaviside function, introduced in Section 2.2, is discontinuous at 0 because $\lim _{t \rightarrow 0} H(t)$ does not exist.]

Geometrically, you can think of a function that is continuous at every number in an interval as a function whose graph has no break in it: the graph can be drawn without removing your pen from the paper.

EXAMPLE 1 Figure 2 shows the graph of a function $f$. At which numbers is $f$ discontinuous? Why?

SOLUTION It looks as if there is a discontinuity when $a=1$ because the graph has a break there. The official reason that $f$ is discontinuous at 1 is that $f(1)$ is not defined.

The graph also has a break when $a=3$, but the reason for the discontinuity is different. Here, $f(3)$ is defined, but $\lim _{x \rightarrow 3} f(x)$ does not exist (because the left and right limits are different). So $f$ is discontinuous at 3 .

What about $a=5$ ? Here, $f(5)$ is defined and $\lim _{x \rightarrow 5} f(x)$ exists (because the left and right limits are the same). But

$$
\lim _{x \rightarrow 5} f(x) \neq f(5)
$$

So $f$ is discontinuous at 5 . $\square$

Now let's see how to detect discontinuities when a function is defined by a formula.

EXAMPLE 2 Where are each of the following functions discontinuous?
(a) $f(x)=\frac{x^{2}-x-2}{x-2}$
(b) $f(x)= \begin{cases}\frac{x^{2}-x-2}{x-2} & \text { if } x \neq 2 \\ 1 & \text { if } x=2\end{cases}$
(c) $f(x)=\left\{\begin{array}{cl}\frac{1}{x^{2}} & \text { if } x \neq 0 \\ 1 & \text { if } x=0\end{array}\right.$
(d) $f(x)=\llbracket x \rrbracket$

SOLUTION
(a) Notice that $f(2)$ is not defined, so $f$ is discontinuous at 2. Later we'll see why $f$ is continuous at all other numbers.
(b) Here $f(2)=1$ is defined and

$$
\lim _{x \rightarrow 2} f(x)=\lim _{x \rightarrow 2} \frac{x^{2}-x-2}{x-2}=\lim _{x \rightarrow 2} \frac{(x-2)(x+1)}{x-2}=\lim _{x \rightarrow 2}(x+1)=3
$$

exists. But

$$
\lim _{x \rightarrow 2} f(x) \neq f(2)
$$

so $f$ is not continuous at 2.
(c) Here $f(0)=1$ is defined but

$$
\lim _{x \rightarrow 0} f(x)=\lim _{x \rightarrow 0} \frac{1}{x^{2}}
$$

does not exist. (See Example 2.2.6.) So $f$ is discontinuous at 0 .
(d) The greatest integer function $f(x)=\llbracket x \rrbracket$ has discontinuities at all of the integers because $\lim _{x \rightarrow n} \llbracket x \rrbracket$ does not exist if $n$ is an integer. (See Example 2.3.10 and Exercise 2.3.55.) $\square$

Figure 3 shows the graphs of the functions in Example 2. In each case the graph can't be drawn without lifting the pen from the paper because a hole or break or jump occurs in the graph. The kind of discontinuity illustrated in parts (a) and (b) is called removable because we could remove the discontinuity by redefining $f$ at just the single number 2. [If we redefine $f$ to be 3 at $x=2$, then $f$ is equivalent to the function $g(x)=x+1$, which is continuous.] The discontinuity in part (c) is called an infinite discontinuity. The discontinuities in part (d) are called jump discontinuities because the function "jumps" from one value to another.

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0151.jpg?height=395&width=1779&top_left_y=1846&top_left_x=110)
FIGURE 3
Graphs of the functions in Example 2

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0152.jpg?height=295&width=449&top_left_y=1755&top_left_x=243)
FIGURE 4

2 Definition A function $f$ is continuous from the right at a number $\boldsymbol{a}$ if

$$
\lim _{x \rightarrow a^{+}} f(x)=f(a)
$$

and $f$ is continuous from the left at $\boldsymbol{a}$ if

$$
\lim _{x \rightarrow a^{-}} f(x)=f(a)
$$

EXAMPLE 3 At each integer $n$, the function $f(x)=\llbracket x \rrbracket$ [see Figure 3(d)] is continuous from the right but discontinuous from the left because

$$
\lim _{x \rightarrow n^{+}} f(x)=\lim _{x \rightarrow n^{+}} \llbracket x \rrbracket=n=f(n)
$$

but

$$
\lim _{x \rightarrow n^{-}} f(x)=\lim _{x \rightarrow n^{-}} \llbracket x \rrbracket=n-1 \neq f(n)
$$ $\square$

3 Definition A function $f$ is continuous on an interval if it is continuous at every number in the interval. (If $f$ is defined only on one side of an endpoint of the interval, we understand continuous at the endpoint to mean continuous from the right or continuous from the left.)

EXAMPLE 4 Show that the function $f(x)=1-\sqrt{1-x^{2}}$ is continuous on the interval [-1, 1].

SOLUTION If $-1<a<1$, then using the Limit Laws from Section 2.3, we have

$$
\begin{aligned}
\lim _{x \rightarrow a} f(x) & =\lim _{x \rightarrow a}\left(1-\sqrt{1-x^{2}}\right) & & \\
& =1-\lim _{x \rightarrow a} \sqrt{1-x^{2}} & & (\text { by Laws 2 and 8 }) \\
& =1-\sqrt{\lim _{x \rightarrow a}\left(1-x^{2}\right)} & & (\text { by 7 }) \\
& =1-\sqrt{1-a^{2}} & & (\text { by 2, 8, and 10) } \\
& =f(a) & &
\end{aligned}
$$

Thus, by Definition $1, f$ is continuous at $a$ if $-1<a<1$. Similar calculations show that

$$
\lim _{x \rightarrow-1^{+}} f(x)=1=f(-1) \quad \text { and } \quad \lim _{x \rightarrow 1^{-}} f(x)=1=f(1)
$$

so $f$ is continuous from the right at -1 and continuous from the left at 1. Therefore, according to Definition 3, $f$ is continuous on [-1, 1].

The graph of $f$ is sketched in Figure 4. It is the lower half of the circle

$$
x^{2}+(y-1)^{2}=1
$$ $\square$

## ■ Properties of Continuous Functions

Instead of always using Definitions 1, 2, and 3 to verify the continuity of a function as we did in Example 4, it is often convenient to use the next theorem, which shows how to build up complicated continuous functions from simple ones.

4 Theorem If $f$ and $g$ are continuous at $a$ and $c$ is a constant, then the following functions are also continuous at $a$ :

1. $f+g$
2. $f-g$
3. $c f$
4. $f g$
5. $\frac{f}{g}$ if $g(a) \neq 0$

PROOF Each of the five parts of this theorem follows from the corresponding Limit Law in Section 2.3. For instance, we give the proof of part 1. Since $f$ and $g$ are continuous at $a$, we have

$$
\lim _{x \rightarrow a} f(x)=f(a) \quad \text { and } \quad \lim _{x \rightarrow a} g(x)=g(a)
$$

Therefore

$$
\begin{aligned}
\lim _{x \rightarrow a}(f+g)(x) & =\lim _{x \rightarrow a}[f(x)+g(x)] \\
& =\lim _{x \rightarrow a} f(x)+\lim _{x \rightarrow a} g(x) \quad \text { (by Law 1) } \\
& =f(a)+g(a) \\
& =(f+g)(a)
\end{aligned}
$$

This shows that $f+g$ is continuous at $a$. $\square$

It follows from Theorem 4 and Definition 3 that if $f$ and $g$ are continuous on an interval, then so are the functions $f+g, f-g, c f, f g$, and (if $g$ is never 0 ) $f / g$. The following theorem was stated in Section 2.3 as the Direct Substitution Property.

5 Theorem

(a) Any polynomial is continuous everywhere; that is, it is continuous on $\mathbb{R}=(-\infty, \infty)$.
(b) Any rational function is continuous wherever it is defined; that is, it is continuous on its domain.

PROOF
(a) A polynomial is a function of the form

$$
P(x)=c_{n} x^{n}+c_{n-1} x^{n-1}+\cdots+c_{1} x+c_{0}
$$

where $c_{0}, c_{1}, \ldots, c_{n}$ are constants. We know that

$$
\lim _{x \rightarrow a} c_{0}=c_{0} \quad(\text { by Law } 8)
$$

and

$$
\lim _{x \rightarrow a} x^{m}=a^{m} \quad m=1,2, \ldots, n \quad \text { (by 10) }
$$

This equation is precisely the statement that the function $f(x)=x^{m}$ is a continuous function. Thus, by part 3 of Theorem 4, the function $g(x)=c x^{m}$ is continuous. Since $P$ is a sum of functions of this form and a constant function, it follows from part 1 of Theorem 4 that $P$ is continuous.

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0154.jpg?height=320&width=380&top_left_y=1430&top_left_x=243)
FIGURE 5

Another way to establish the limits in (6) is to use the Squeeze Theorem with the inequality $\sin \theta<\theta$ (for $\theta>0$ ), which is proved in Section 3.3.
(b) A rational function is a function of the form

$$
f(x)=\frac{P(x)}{Q(x)}
$$

where $P$ and $Q$ are polynomials. The domain of $f$ is $D=\{x \in \mathbb{R} \mid Q(x) \neq 0\}$. We know from part (a) that $P$ and $Q$ are continuous everywhere. Thus, by part 5 of Theorem 4, $f$ is continuous at every number in $D$. $\square$

As an illustration of Theorem 5, observe that the volume of a sphere varies continuously with its radius because the formula $V(r)=\frac{4}{3} \pi r^{3}$ shows that $V$ is a polynomial function of $r$. Likewise, if a ball is thrown vertically into the air with an initial velocity of 15 m/s, then the height of the ball in meters $t$ seconds later is given by the formula $h=15 t-4.9 t^{2}$. Again this is a polynomial function, so the height is a continuous function of the elapsed time, as we might expect.

Knowledge of which functions are continuous enables us to evaluate some limits very quickly, as the following example shows. Compare it with Example 2.3.2(b).

EXAMPLE 5 Find $\lim _{x \rightarrow-2} \frac{x^{3}+2 x^{2}-1}{5-3 x}$.
SOLUTION The function

$$
f(x)=\frac{x^{3}+2 x^{2}-1}{5-3 x}
$$

is rational, so by Theorem 5 it is continuous on its domain, which is $\left\{x \left\lvert\, x \neq \frac{5}{3}\right.\right\}$. Therefore

$$
\begin{aligned}
\lim _{x \rightarrow-2} \frac{x^{3}+2 x^{2}-1}{5-3 x} & =\lim _{x \rightarrow-2} f(x)=f(-2) \\
& =\frac{(-2)^{3}+2(-2)^{2}-1}{5-3(-2)}=-\frac{1}{11}
\end{aligned}
$$ $\square$

It turns out that most of the familiar functions are continuous at every number in their domains. For instance, Limit Law 11 in Section 2.3 is exactly the statement that root functions are continuous.

From the appearance of the graphs of the sine and cosine functions (Figure 1.2.19), we would certainly guess that they are continuous. We know from the definitions of $\sin \theta$ and $\cos \theta$ that the coordinates of the point $P$ in Figure 5 are $(\cos \theta, \sin \theta)$. As $\theta \rightarrow 0$, we see that $P$ approaches the point $(1,0)$ and so $\cos \theta \rightarrow 1$ and $\sin \theta \rightarrow 0$. Thus

6

$$
\lim _{\theta \rightarrow 0} \cos \theta=1 \quad \lim _{\theta \rightarrow 0} \sin \theta=0
$$

Since $\cos 0=1$ and $\sin 0=0$, the equations in (6) assert that the cosine and sine functions are continuous at 0. The addition formulas for cosine and sine can then be used to deduce that these functions are continuous everywhere (see Exercises 66 and 67).

It follows from part 5 of Theorem 4 that

$$
\tan x=\frac{\sin x}{\cos x}
$$

is continuous except where $\cos x=0$. This happens when $x$ is an odd integer multiple

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0155.jpg?height=401&width=504&top_left_y=180&top_left_x=119)
FIGURE 6
$y=\tan x$

The inverse trigonometric functions are reviewed in Section 1.5.
of $\pi / 2$, so $y=\tan x$ has infinite discontinuities when $x= \pm \pi / 2, \pm 3 \pi / 2, \pm 5 \pi / 2$, and so on (see Figure 6).

The inverse function of any continuous one-to-one function is also continuous. (This fact is proved in Appendix F, but our geometric intuition makes it seem plausible: the graph of $f^{-1}$ is obtained by reflecting the graph of $f$ about the line $y=x$. So if the graph of $f$ has no break in it, neither does the graph of $f^{-1}$.) Thus the inverse trigonometric functions are continuous.

In Section 1.4 we defined the exponential function $y=b^{x}$ so as to fill in the holes in the graph of $y=b^{x}$ where $x$ is rational. In other words, the very definition of $y=b^{x}$ makes it a continuous function on $\mathbb{R}$. Therefore its inverse function $y=\log _{b} x$ is continuous on $(0, \infty)$.

7 Theorem The following types of functions are continuous at every number in their domains:

- polynomials
- rational functions
- root functions
- trigonometric functions
- inverse trigonometric functions
- exponential functions
- logarithmic functions

EXAMPLE 6 Where is the function $f(x)=\frac{\ln x+\tan ^{-1} x}{x^{2}-1}$ continuous?
SOLUTION We know from Theorem 7 that the function $y=\ln x$ is continuous for $x>0$ and $y=\tan ^{-1} x$ is continuous on $\mathbb{R}$. Thus, by part 1 of Theorem $4, y=\ln x+\tan ^{-1} x$ is continuous on $(0, \infty)$. The denominator, $y=x^{2}-1$, is a polynomial, so it is continuous everywhere. Therefore, by part 5 of Theorem 4, $f$ is continuous at all positive numbers $x$ except where $x^{2}-1=0 \Leftrightarrow x= \pm 1$. So $f$ is continuous on the intervals $(0,1)$ and $(1, \infty)$. $\square$

EXAMPLE 7 Evaluate $\lim _{x \rightarrow \pi} \frac{\sin x}{2+\cos x}$.
SOLUTION Theorem 7 tells us that $y=\sin x$ is continuous. The function in the denominator, $y=2+\cos x$, is the sum of two continuous functions and is therefore continuous. Notice that this function is never 0 because $\cos x \geqslant-1$ for all $x$ and so $2+\cos x>0$ everywhere. Thus the ratio

$$
f(x)=\frac{\sin x}{2+\cos x}
$$

is continuous everywhere. Hence, by the definition of a continuous function,

$$
\lim _{x \rightarrow \pi} \frac{\sin x}{2+\cos x}=\lim _{x \rightarrow \pi} f(x)=f(\pi)=\frac{\sin \pi}{2+\cos \pi}=\frac{0}{2-1}=0
$$ $\square$

Another way of combining continuous functions $f$ and $g$ to get a new continuous function is to form the composite function $f \circ g$. This fact is a consequence of the following theorem.

8 Theorem If $f$ is continuous at $b$ and $\lim _{x \rightarrow a} g(x)=b$, then $\lim _{x \rightarrow a} f(g(x))=f(b)$. In other words,

$$
\lim _{x \rightarrow a} f(g(x))=f\left(\lim _{x \rightarrow a} g(x)\right)
$$

Intuitively, Theorem 8 is reasonable because if $x$ is close to $a$, then $g(x)$ is close to $b$, and since $f$ is continuous at $b$, if $g(x)$ is close to $b$, then $f(g(x))$ is close to $f(b)$. A proof of Theorem 8 is given in Appendix F.

EXAMPLE 8 Evaluate $\lim _{x \rightarrow 1} \arcsin \left(\frac{1-\sqrt{x}}{1-x}\right)$.
SOLUTION Because arcsin is a continuous function, we can apply Theorem 8:

$$
\begin{aligned}
\lim _{x \rightarrow 1} \arcsin \left(\frac{1-\sqrt{x}}{1-x}\right) & =\arcsin \left(\lim _{x \rightarrow 1} \frac{1-\sqrt{x}}{1-x}\right) \\
& =\arcsin \left(\lim _{x \rightarrow 1} \frac{1-\sqrt{x}}{(1-\sqrt{x})(1+\sqrt{x})}\right) \\
& =\arcsin \left(\lim _{x \rightarrow 1} \frac{1}{1+\sqrt{x}}\right) \\
& =\arcsin \frac{1}{2}=\frac{\pi}{6}
\end{aligned}
$$ $\square$

Let's now apply Theorem 8 in the special case where $f(x)=\sqrt[n]{x}$, with $n$ being a positive integer. Then
and

$$
\begin{aligned}
f(g(x)) & =\sqrt[n]{g(x)} \\
f\left(\lim _{x \rightarrow a} g(x)\right) & =\sqrt[n]{\lim _{x \rightarrow a} g(x)}
\end{aligned}
$$

If we put these expressions into Theorem 8, we get

$$
\lim _{x \rightarrow a} \sqrt[n]{g(x)}=\sqrt[n]{\lim _{x \rightarrow a} g(x)}
$$

and so Limit Law 7 has now been proved. (We assume that the roots exist.)

9 Theorem If $g$ is continuous at $a$ and $f$ is continuous at $g(a)$, then the composite function $f \circ g$ given by $(f \circ g)(x)=f(g(x))$ is continuous at $a$.

This theorem is often expressed informally by saying "a continuous function of a continuous function is a continuous function."

PROOF Since $g$ is continuous at $a$, we have

$$
\lim _{x \rightarrow a} g(x)=g(a)
$$

Since $f$ is continuous at $b=g(a)$, we can apply Theorem 8 to obtain

$$
\lim _{x \rightarrow a} f(g(x))=f(g(a))
$$

which is precisely the statement that the function $h(x)=f(g(x))$ is continuous at $a$; that is, $f \circ g$ is continuous at $a$. $\square$

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0157.jpg?height=313&width=472&top_left_y=1879&top_left_x=122)
FIGURE 9

EXAMPLE 9 Where are the following functions continuous?
(a) $h(x)=\sin \left(x^{2}\right)$
(b) $F(x)=\ln (1+\cos x)$

SOLUTION
(a) We have $h(x)=f(g(x))$, where

$$
g(x)=x^{2} \quad \text { and } \quad f(x)=\sin x
$$

We know that $g$ is continuous on $\mathbb{R}$ since it is a polynomial, and $f$ is also continuous everywhere. Thus $h=f \circ g$ is continuous on $\mathbb{R}$ by Theorem 9.
(b) We know from Theorem 7 that $f(x)=\ln x$ is continuous and $g(x)=1+\cos x$ is continuous (because both $y=1$ and $y=\cos x$ are continuous). Therefore, by Theorem 9, $F(x)=f(g(x))$ is continuous wherever it is defined. The expression $\ln (1+\cos x)$ is defined when $1+\cos x>0$, so it is undefined when $\cos x=-1$, and this happens when $x= \pm \pi, \pm 3 \pi, \ldots$. Thus $F$ has discontinuities when $x$ is an odd multiple of $\pi$ and is continuous on the intervals between these values (see Figure 7). $\square$

## ■ The Intermediate Value Theorem

An important property of continuous functions is expressed by the following theorem, whose proof is found in more advanced books on calculus.

10 The Intermediate Value Theorem Suppose that $f$ is continuous on the closed interval $[a, b]$ and let $N$ be any number between $f(a)$ and $f(b)$, where $f(a) \neq f(b)$. Then there exists a number $c$ in $(a, b)$ such that $f(c)=N$.

The Intermediate Value Theorem states that a continuous function takes on every intermediate value between the function values $f(a)$ and $f(b)$. It is illustrated by Figure 8. Note that the value $N$ can be taken on once [as in part (a)] or more than once [as in part (b)].

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0157.jpg?height=427&width=1118&top_left_y=1477&top_left_x=702)
FIGURE 8

If we think of a continuous function as a function whose graph has no hole or break, then it is easy to believe that the Intermediate Value Theorem is true. In geometric terms it says that if any horizontal line $y=N$ is given between $y=f(a)$ and $y=f(b)$ as in Figure 9, then the graph of $f$ can't jump over the line. It must intersect $y=N$ somewhere.

It is important that the function $f$ in Theorem 10 be continuous. The Intermediate Value Theorem is not true in general for discontinuous functions (see Exercise 52).

One use of the Intermediate Value Theorem is in locating solutions of equations as in the following example.

EXAMPLE 10 Show that there is a solution of the equation

$$
4 x^{3}-6 x^{2}+3 x-2=0
$$

between 1 and 2.
SOLUTION Let $f(x)=4 x^{3}-6 x^{2}+3 x-2$. We are looking for a solution of the given equation, that is, a number $c$ between 1 and 2 such that $f(c)=0$. Therefore we take $a=1, b=2$, and $N=0$ in Theorem 10. We have
and

$$
\begin{aligned}
& f(1)=4-6+3-2=-1<0 \\
& f(2)=32-24+6-2=12>0
\end{aligned}
$$

Thus $f(1)<0<f(2)$; that is, $N=0$ is a number between $f(1)$ and $f(2)$. The function $f$ is continuous since it is a polynomial, so the Intermediate Value Theorem says there is a number $c$ between 1 and 2 such that $f(c)=0$. In other words, the equation $4 x^{3}-6 x^{2}+3 x-2=0$ has at least one solution $c$ in the interval (1, 2).

In fact, we can locate a solution more precisely by using the Intermediate Value Theorem again. Since

$$
f(1.2)=-0.128<0 \quad \text { and } \quad f(1.3)=0.548>0
$$

a solution must lie between 1.2 and 1.3. A calculator gives, by trial and error,

$$
f(1.22)=-0.007008<0 \quad \text { and } \quad f(1.23)=0.056068>0
$$

so a solution lies in the interval (1.22, 1.23). $\square$

We can use a graphing calculator or computer to illustrate the use of the Intermediate Value Theorem in Example 10. Figure 10 shows the graph of $f$ in the viewing rectangle [-1, 3] by [-3, 3] and you can see that the graph crosses the $x$-axis between 1 and 2. Figure 11 shows the result of zooming in to the viewing rectangle [1.2, 1.3] by [-0.2, 0.2].

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0158.jpg?height=324&width=457&top_left_y=1610&top_left_x=775)
FIGURE 10

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0158.jpg?height=324&width=477&top_left_y=1611&top_left_x=1368)
FIGURE 11

In fact, the Intermediate Value Theorem plays a role in the very way these graphing devices work. A computer calculates a finite number of points on the graph and turns on the pixels that contain these calculated points. It assumes that the function is continuous and takes on all the intermediate values between two consecutive points. The computer therefore "connects the dots" by turning on the intermediate pixels.

### 2.5 Exercises

1. Write an equation that expresses the fact that a function $f$ is continuous at the number 4.
2. If $f$ is continuous on $(-\infty, \infty)$, what can you say about its graph?
3. (a) From the given graph of $f$, state the numbers at which $f$ is discontinuous and explain why.
    (b) For each of the numbers stated in part (a), determine whether $f$ is continuous from the right, or from the left, or neither.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0159.jpg?height=399&width=752&top_left_y=723&top_left_x=166)
4. From the given graph of $g$, state the numbers at which $g$ is discontinuous and explain why.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0159.jpg?height=345&width=605&top_left_y=1252&top_left_x=239)

5-6 The graph of a function $f$ is given.

(a) At what numbers $a$ does $\lim _{x \rightarrow a} f(x)$ not exist?
(b) At what numbers $a$ is $f$ not continuous?
(c) At what numbers $a$ does $\lim _{x \rightarrow a} f(x)$ exist but $f$ is not continuous at $a$ ?
5.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0159.jpg?height=260&width=344&top_left_y=1845&top_left_x=178)
6.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0159.jpg?height=259&width=344&top_left_y=1845&top_left_x=600)

7-10 Sketch the graph of a function $f$ that is defined on $\mathbb{R}$ and continuous except for the stated discontinuities.

7. Removable discontinuity at -2, infinite discontinuity at 2
8. Jump discontinuity at -3, removable discontinuity at 4
9. Discontinuities at 0 and 3 , but continuous from the right at 0 and from the left at 3
10. Continuous only from the left at -1, not continuous from the left or right at 3
11. The toll $T$ charged for driving on a certain stretch of a toll road is \$5 except during rush hours (between 7 am and 10 am and between 4 pm and 7 pm) when the toll is $\$ 7$.
    (a) Sketch a graph of $T$ as a function of the time $t$, measured in hours past midnight.
    (b) Discuss the discontinuities of this function and their significance to someone who uses the road.
12. Explain why each function is continuous or discontinuous.
    (a) The temperature at a specific location as a function of time
    (b) The temperature at a specific time as a function of the distance due west from New York City
    (c) The altitude above sea level as a function of the distance due west from New York City
    (d) The cost of a taxi ride as a function of the distance traveled
    (e) The current in the circuit for the lights in a room as a function of time

13-16 Use the definition of continuity and the properties of limits to show that the function is continuous at the given number $a$.

13. $f(x)=3 x^{2}+(x+2)^{5}, \quad a=-1$
14. $g(t)=\frac{t^{2}+5 t}{2 t+1}, \quad a=2$
15. $p(v)=2 \sqrt{3 v^{2}+1}, \quad a=1$
16. $f(r)=\sqrt[3]{4 r^{2}-2 r+7}, \quad a=-2$

17-18 Use the definition of continuity and the properties of limits to show that the function is continuous on the given interval.

17. $f(x)=x+\sqrt{x-4}, \quad[4, \infty)$
18. $g(x)=\frac{x-1}{3 x+6}, \quad(-\infty,-2)$

19-24 Explain why the function is discontinuous at the given number $a$. Sketch the graph of the function.
19. $f(x)=\frac{1}{x+2}$

$$
a=-2
$$

20. $f(x)= \begin{cases}\frac{1}{x+2} & \text { if } x \neq-2 \\ 1 & \text { if } x=-2\end{cases}$

$$
a=-2
$$

21. $f(x)= \begin{cases}x+3 & \text { if } x \leqslant-1 \\ 2^{x} & \text { if } x>-1\end{cases}$
$$
a=-1
$$
22. $f(x)= \begin{cases}\frac{x^{2}-x}{x^{2}-1} & \text { if } x \neq 1 \\ 1 & \text { if } x=1\end{cases}$
$$
a=1
$$
23. $f(x)= \begin{cases}\cos x & \text { if } x<0 \\ 0 & \text { if } x=0 \\ 1-x^{2} & \text { if } x>0\end{cases}$
$$
a=0
$$
24. $f(x)=\left\{\begin{array}{ll}\frac{2 x^{2}-5 x-3}{x-3} & \text { if } x \neq 3 \\ 6 & \text { if } x=3\end{array} \quad a=3\right.$

25-26

(a) Show that $f$ has a removable discontinuity at $x=3$.
(b) Redefine $f(3)$ so that $f$ is continuous at $x=3$ (and thus the discontinuity is "removed").
25. $f(x)=\frac{x-3}{x^{2}-9}$
26. $f(x)=\frac{x^{2}-7 x+12}{x-3}$

27-34 Explain, using Theorems 4, 5, 7, and 9, why the function is continuous at every number in its domain. State the domain.
27. $f(x)=\frac{x^{2}}{\sqrt{x^{4}+2}}$
28. $g(v)=\frac{3 v-1}{v^{2}+2 v-15}$
29. $h(t)=\frac{\cos \left(t^{2}\right)}{1-e^{t}}$
30. $B(u)=\sqrt{3 u-2}+\sqrt[3]{2 u-3}$
31. $L(v)=v \ln \left(1-v^{2}\right)$
32. $f(t)=e^{-t^{2}} \ln \left(1+t^{2}\right)$
33. $M(x)=\sqrt{1+\frac{1}{x}}$
34. $g(t)=\cos ^{-1}\left(e^{t}-1\right)$

35-38 Use continuity to evaluate the limit.
35. $\lim _{x \rightarrow 2} x \sqrt{20-x^{2}}$
36. $\lim _{\theta \rightarrow \pi / 2} \sin (\tan (\cos \theta))$
37. $\lim _{x \rightarrow 1} \ln \left(\frac{5-x^{2}}{1+x}\right)$
38. $\lim _{x \rightarrow 4} 3^{\sqrt{x^{2}-2 x-4}}$

39-40 Locate the discontinuities of the function and illustrate by graphing.
39. $f(x)=\frac{1}{\sqrt{1-\sin x}}$
40. $y=\arctan \frac{1}{x}$

41-42 Show that $f$ is continuous on $(-\infty, \infty)$.
41. $f(x)= \begin{cases}1-x^{2} & \text { if } x \leqslant 1 \\ \ln x & \text { if } x>1\end{cases}$
42. $f(x)= \begin{cases}\sin x & \text { if } x<\pi / 4 \\ \cos x & \text { if } x \geqslant \pi / 4\end{cases}$

43-45 Find the numbers at which $f$ is discontinuous. At which of these numbers is $f$ continuous from the right, from the left, or neither? Sketch the graph of $f$.
43. $f(x)= \begin{cases}x^{2} & \text { if } x<-1 \\ x & \text { if }-1 \leqslant x<1 \\ 1 / x & \text { if } x \geqslant 1\end{cases}$
44. $f(x)= \begin{cases}2^{x} & \text { if } x \leqslant 1 \\ 3-x & \text { if } 1<x \leqslant 4 \\ \sqrt{x} & \text { if } x>4\end{cases}$
45. $f(x)= \begin{cases}x+2 & \text { if } x<0 \\ e^{x} & \text { if } 0 \leqslant x \leqslant 1 \\ 2-x & \text { if } x>1\end{cases}$
46. The gravitational force exerted by the planet Earth on a unit mass at a distance $r$ from the center of the planet is

$$
F(r)=\left\{\begin{array}{cl}
\frac{G M r}{R^{3}} & \text { if } r<R \\
\frac{G M}{r^{2}} & \text { if } r \geqslant R
\end{array}\right.
$$

where $M$ is the mass of Earth, $R$ is its radius, and $G$ is the gravitational constant. Is $F$ a continuous function of $r$ ?
47. For what value of the constant $c$ is the function $f$ continuous on $(-\infty, \infty)$ ?

$$
f(x)= \begin{cases}c x^{2}+2 x & \text { if } x<2 \\ x^{3}-c x & \text { if } x \geqslant 2\end{cases}
$$

48. Find the values of $a$ and $b$ that make $f$ continuous everywhere.

$$
f(x)= \begin{cases}\frac{x^{2}-4}{x-2} & \text { if } x<2 \\ a x^{2}-b x+3 & \text { if } 2 \leqslant x<3 \\ 2 x-a+b & \text { if } x \geqslant 3\end{cases}
$$

49. Suppose $f$ and $g$ are continuous functions such that $g(2)=6$ and $\lim _{x \rightarrow 2}[3 f(x)+f(x) g(x)]=36$. Find $f(2)$.
50. Let $f(x)=1 / x$ and $g(x)=1 / x^{2}$.
(a) Find $(f \circ g)(x)$.
(b) Is $f \circ g$ continuous everywhere? Explain.

51. Which of the following functions $f$ has a removable discontinuity at $a$ ? If the discontinuity is removable, find a function $g$ that agrees with $f$ for $x \neq a$ and is continuous at $a$.
    (a) $f(x)=\frac{x^{4}-1}{x-1}, \quad a=1$
    (b) $f(x)=\frac{x^{3}-x^{2}-2 x}{x-2}, \quad a=2$
    (c) $f(x)=\llbracket \sin x \rrbracket, \quad a=\pi$
52. Suppose that a function $f$ is continuous on $[0,1]$ except at 0.25 and that $f(0)=1$ and $f(1)=3$. Let $N=2$. Sketch two possible graphs of $f$, one showing that $f$ might not satisfy the conclusion of the Intermediate Value Theorem and one showing that $f$ might still satisfy the conclusion of the Intermediate Value Theorem (even though it doesn't satisfy the hypothesis).
53. If $f(x)=x^{2}+10 \sin x$, show that there is a number $c$ such that $f(c)=1000$.
54. Suppose $f$ is continuous on [1,5] and the only solutions of the equation $f(x)=6$ are $x=1$ and $x=4$. If $f(2)=8$, explain why $f(3)>6$.

55-58 Use the Intermediate Value Theorem to show that there is a solution of the given equation in the specified interval.
55. $-x^{3}+4 x+1=0, \quad(-1,0)$
56. $\ln x=x-\sqrt{x}, \quad(2,3)$
57. $e^{x}=3-2 x, \quad(0,1)$
58. $\sin x=x^{2}-x, \quad(1,2)$

59-60

(a) Prove that the equation has at least one real solution.
(b) Use a calculator to find an interval of length 0.01 that contains a solution.
59. $\cos x=x^{3}$
60. $\ln x=3-2 x$

61-62

(a) Prove that the equation has at least one real solution.
(b) Find the solution correct to three decimal places, by graphing.
61. $100 e^{-x / 100}=0.01 x^{2}$
62. $\arctan x=1-x$

63-64 Prove, without graphing, that the graph of the function has at least two $x$-intercepts in the specified interval.
63. $y=\sin x^{3}, \quad(1,2)$
64. $y=x^{2}-3+1 / x, \quad(0,2)$

65. Prove that $f$ is continuous at $a$ if and only if
$$
\lim _{h \rightarrow 0} f(a+h)=f(a)
$$
66. To prove that sine is continuous, we need to show that $\lim _{x \rightarrow a} \sin x=\sin a$ for every real number $a$. By Exercise 65 an equivalent statement is that
$$
\lim _{h \rightarrow 0} \sin (a+h)=\sin a
$$
Use (6) to show that this is true.
67. Prove that cosine is a continuous function.
68. (a) Prove Theorem 4, part 3.
    (b) Prove Theorem 4, part 5.
69. Use Theorem 8 to prove Limit Laws 6 and 7 from Section 2.3.
70. Is there a number that is exactly 1 more than its cube?
71. For what values of $x$ is $f$ continuous?
$$
f(x)= \begin{cases}0 & \text { if } x \text { is rational } \\ 1 & \text { if } x \text { is irrational }\end{cases}
$$
72. For what values of $x$ is $g$ continuous?
$$
g(x)= \begin{cases}0 & \text { if } x \text { is rational } \\ x & \text { if } x \text { is irrational }\end{cases}
$$
73. Show that the function
$$
f(x)= \begin{cases}x^{4} \sin (1 / x) & \text { if } x \neq 0 \\ 0 & \text { if } x=0\end{cases}
$$
is continuous on $(-\infty, \infty)$.
74. If $a$ and $b$ are positive numbers, prove that the equation
$$
\frac{a}{x^{3}+2 x^{2}-1}+\frac{b}{x^{3}+x-2}=0
$$
has at least one solution in the interval (-1, 1).
75. A woman leaves her house at 7:00 am and takes her usual path to the top of a mountain, arriving at 7:00 pm. The following morning, she starts at 7:00 am at the top and takes the same path back, arriving at her home at 7:00 pm. Use the Intermediate Value Theorem to show that there is a point on the path that the woman will cross at exactly the same time of day on both days.
76. Absolute Value and Continuity
(a) Show that the absolute value function $F(x)=|x|$ is continuous everywhere.
(b) Prove that if $f$ is a continuous function on an interval, then so is $|f|$.
(c) Is the converse of the statement in part (b) also true? In other words, if $|f|$ is continuous, does it follow that $f$ is continuous? If so, prove it. If not, find a counterexample.

### 2.6 Limits at Infinity; Horizontal Asymptotes

| $x$ | $f(x)$ |
| :--- | :--- |
| 0 | -1 |
| $\pm 1$ | 0 |
| $\pm 2$ | 0.600000 |
| $\pm 3$ | 0.800000 |
| $\pm 4$ | 0.882353 |
| ±5 | 0.923077 |
| ±10 | 0.980198 |
| ±50 | 0.999200 |
| ±100 | 0.999800 |
| ±1000 | 0.999998 |

In Sections 2.2 and 2.4 we investigated infinite limits and vertical asymptotes of a curve $y=f(x)$. There we let $x$ approach a number and the result was that the values of $y$ became arbitrarily large (positive or negative). In this section we let $x$ become arbitrarily large (positive or negative) and see what happens to $y$.

■ Limits at Infinity and Horizontal Asymptotes
Let's begin by investigating the behavior of the function $f$ defined by

$$
f(x)=\frac{x^{2}-1}{x^{2}+1}
$$

as $x$ becomes large. The table at the left gives values of this function correct to six decimal places, and the graph of $f$ has been drawn by a computer in Figure 1.

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0162.jpg?height=281&width=1121&top_left_y=900&top_left_x=831)
FIGURE 1

You can see that as $x$ grows larger and larger, the values of $f(x)$ get closer and closer to 1. (The graph of $f$ approaches the horizontal line $y=1$ as we look to the right.) In fact, it seems that we can make the values of $f(x)$ as close as we like to 1 by taking $x$ sufficiently large. This situation is expressed symbolically by writing

$$
\lim _{x \rightarrow \infty} \frac{x^{2}-1}{x^{2}+1}=1
$$

In general, we use the notation

$$
\lim _{x \rightarrow \infty} f(x)=L
$$

to indicate that the values of $f(x)$ approach $L$ as $x$ becomes larger and larger.
[1] Intuitive Definition of a Limit at Infinity Let $f$ be a function defined on some interval $(a, \infty)$. Then

$$
\lim _{x \rightarrow \infty} f(x)=L
$$

means that the values of $f(x)$ can be made arbitrarily close to $L$ by requiring $x$ to be sufficiently large.

Another notation for $\lim _{x \rightarrow \infty} f(x)=L$ is

$$
f(x) \rightarrow L \quad \text { as } \quad x \rightarrow \infty
$$

The symbol $\infty$ does not represent a number. Nonetheless, the expression $\lim _{x \rightarrow \infty} f(x)=L$ is often read as
"the limit of $f(x)$, as $x$ approaches infinity, is $L$ "
or "the limit of $f(x)$, as $x$ becomes infinite, is $L$ "
or "the limit of $f(x)$, as $x$ increases without bound, is $L$ "
The meaning of such phrases is given by Definition 1. A more precise definition, similar to the $\varepsilon, \delta$ definition of Section 2.4, is given at the end of this section.

Geometric illustrations of Definition 1 are shown in Figure 2. Notice that there are many ways for the graph of $f$ to approach the line $y=L$ (which is called a horizontal asymptote) as we look to the far right of each graph.

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0163.jpg?height=334&width=1635&top_left_y=730&top_left_x=252)
FIGURE 2 Examples illustrating $\lim _{x \rightarrow \infty} f(x)=L$

Referring back to Figure 1, we see that for numerically large negative values of $x$, the values of $f(x)$ are close to 1. By letting $x$ decrease through negative values without bound, we can make $f(x)$ as close to 1 as we like. This is expressed by writing

$$
\lim _{x \rightarrow-\infty} \frac{x^{2}-1}{x^{2}+1}=1
$$

The general definition is as follows.

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0163.jpg?height=644&width=490&top_left_y=1566&top_left_x=118)
FIGURE 3
Examples illustrating $\lim _{x \rightarrow-\infty} f(x)=L$

2 Definition Let $f$ be a function defined on some interval $(-\infty, a)$. Then

$$
\lim _{x \rightarrow-\infty} f(x)=L
$$

means that the values of $f(x)$ can be made arbitrarily close to $L$ by requiring $x$ to be sufficiently large negative.

Again, the symbol $-\infty$ does not represent a number, but the expression $\lim _{x \rightarrow-\infty} f(x)=L$ is often read as
"the limit of $f(x)$, as $x$ approaches negative infinity, is $L$ "
Definition 2 is illustrated in Figure 3. Notice that the graph approaches the line $y=L$ as we look to the far left of each graph.

3 Definition The line $y=L$ is called a horizontal asymptote of the curve $y=f(x)$ if either

$$
\lim _{x \rightarrow \infty} f(x)=L \quad \text { or } \quad \lim _{x \rightarrow-\infty} f(x)=L
$$

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0164.jpg?height=364&width=464&top_left_y=223&top_left_x=244)
FIGURE 4
$y=\tan ^{-1} x$

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0164.jpg?height=408&width=489&top_left_y=830&top_left_x=247)
FIGURE 5

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0164.jpg?height=460&width=492&top_left_y=1737&top_left_x=243)
FIGURE 6
$\lim _{x \rightarrow \infty} \frac{1}{x}=0, \lim _{x \rightarrow-\infty} \frac{1}{x}=0$

For instance, the curve illustrated in Figure 1 has the line $y=1$ as a horizontal asymptote because

$$
\lim _{x \rightarrow \infty} \frac{x^{2}-1}{x^{2}+1}=1
$$

An example of a curve with two horizontal asymptotes is $y=\tan ^{-1} x$. (See Figure 4.) In fact,

4

$$
\lim _{x \rightarrow-\infty} \tan ^{-1} x=-\frac{\pi}{2} \quad \lim _{x \rightarrow \infty} \tan ^{-1} x=\frac{\pi}{2}
$$

so both of the lines $y=-\pi / 2$ and $y=\pi / 2$ are horizontal asymptotes. (This follows from the fact that the lines $x= \pm \pi / 2$ are vertical asymptotes of the graph of the tangent function.)

EXAMPLE 1 Find the infinite limits, limits at infinity, and asymptotes for the function $f$ whose graph is shown in Figure 5.

SOLUTION We see that the values of $f(x)$ become large as $x \rightarrow-1$ from both sides, so

$$
\lim _{x \rightarrow-1} f(x)=\infty
$$

Notice that $f(x)$ becomes large negative as $x$ approaches 2 from the left, but large positive as $x$ approaches 2 from the right. So

$$
\lim _{x \rightarrow 2^{-}} f(x)=-\infty \quad \text { and } \quad \lim _{x \rightarrow 2^{+}} f(x)=\infty
$$

Thus both of the lines $x=-1$ and $x=2$ are vertical asymptotes.
As $x$ becomes large, it appears that $f(x)$ approaches 4. But as $x$ decreases through negative values, $f(x)$ approaches 2. So

$$
\lim _{x \rightarrow \infty} f(x)=4 \quad \text { and } \quad \lim _{x \rightarrow-\infty} f(x)=2
$$

This means that both $y=4$ and $y=2$ are horizontal asymptotes. $\square$

EXAMPLE 2 Find $\lim _{x \rightarrow \infty} \frac{1}{x}$ and $\lim _{x \rightarrow-\infty} \frac{1}{x}$.
SOLUTION Observe that when $x$ is large, $1 / x$ is small. For instance,

$$
\frac{1}{100}=0.01 \quad \frac{1}{10,000}=0.0001 \quad \frac{1}{1,000,000}=0.000001
$$

In fact, by taking $x$ large enough, we can make $1 / x$ as close to 0 as we please. Therefore, according to Definition 1, we have

$$
\lim _{x \rightarrow \infty} \frac{1}{x}=0
$$

Similar reasoning shows that when $x$ is large negative, $1 / x$ is small negative, so we also have

$$
\lim _{x \rightarrow-\infty} \frac{1}{x}=0
$$

It follows that the line $y=0$ (the $x$-axis) is a horizontal asymptote of the curve $y=1 / x$. (This is a hyperbola; see Figure 6.) $\square$

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0165.jpg?height=467&width=453&top_left_y=1763&top_left_x=116)
FIGURE 7
$$
y=\frac{3 x^{2}-x-2}{5 x^{2}+4 x+1}
$$

## ■ Evaluating Limits at Infinity

Most of the Limit Laws that were given in Section 2.3 also hold for limits at infinity. It can be proved that the Limit Laws listed in Section 2.3 (with the exception of Laws 10 and 11) are also valid if " $x \rightarrow a$ " is replaced by " $x \rightarrow \infty$ " or " $x \rightarrow-\infty$." In particular, if we combine Laws 6 and 7 with the results of Example 2, we obtain the following important rule for calculating limits.

5 Theorem If $r>0$ is a rational number, then

$$
\lim _{x \rightarrow \infty} \frac{1}{x^{r}}=0
$$

If $r>0$ is a rational number such that $x^{r}$ is defined for all $x$, then

$$
\lim _{x \rightarrow-\infty} \frac{1}{x^{r}}=0
$$

EXAMPLE 3 Evaluate the following limit and indicate which properties of limits are used at each stage.

$$
\lim _{x \rightarrow \infty} \frac{3 x^{2}-x-2}{5 x^{2}+4 x+1}
$$

SOLUTION As $x$ becomes large, both numerator and denominator become large, so it isn't obvious what happens to their ratio. We need to do some preliminary algebra.

To evaluate the limit at infinity of any rational function, we first divide both the numerator and denominator by the highest power of $x$ that occurs in the denominator. (We may assume that $x \neq 0$, since we are interested only in large values of $x$.) In this case the highest power of $x$ in the denominator is $x^{2}$, so we have

$$
\begin{aligned}
\lim _{x \rightarrow \infty} \frac{3 x^{2}-x-2}{5 x^{2}+4 x+1} & =\lim _{x \rightarrow \infty} \frac{\frac{3 x^{2}-x-2}{x^{2}}}{\frac{5 x^{2}+4 x+1}{x^{2}}}=\lim _{x \rightarrow \infty} \frac{3-\frac{1}{x}-\frac{2}{x^{2}}}{5+\frac{4}{x}+\frac{1}{x^{2}}} \\
& =\frac{\lim _{x \rightarrow \infty}\left(3-\frac{1}{x}-\frac{2}{x^{2}}\right)}{\lim _{x \rightarrow \infty}\left(5+\frac{4}{x}+\frac{1}{x^{2}}\right)} \quad \text { (by Limit Law 5) } \\
& =\frac{\lim _{x \rightarrow \infty} 3-\lim _{x \rightarrow \infty} \frac{1}{x}-2 \lim _{x \rightarrow \infty} \frac{1}{x^{2}}}{\lim _{x \rightarrow \infty} 5+4 \lim _{x \rightarrow \infty} \frac{1}{x}+\lim _{x \rightarrow \infty} \frac{1}{x^{2}}} \quad \text { (by 1, 2, and 3) } \\
& =\frac{3-0-0}{5+0+0} \quad \text { (by 8 and Theorem 5) } \\
& =\frac{3}{5}
\end{aligned}
$$

A similar calculation shows that the limit as $x \rightarrow-\infty$ is also $\frac{3}{5}$. Figure 7 illustrates the

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0166.jpg?height=476&width=469&top_left_y=996&top_left_x=243)
FIGURE 8
$y=\frac{\sqrt{2 x^{2}+1}}{3 x-5}$

We can think of the given function as having a denominator of 1.

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0166.jpg?height=321&width=463&top_left_y=1981&top_left_x=243)
FIGURE 9

results of these calculations by showing how the graph of the given rational function approaches the horizontal asymptote $y=\frac{3}{5}=0.6$. $\square$

EXAMPLE 4 Find the horizontal asymptotes of the graph of the function

$$
f(x)=\frac{\sqrt{2 x^{2}+1}}{3 x-5}
$$

SOLUTION Dividing both numerator and denominator by $x$ (which is the highest power of $x$ in the denominator) and using the properties of limits, we have

$$
\begin{aligned}
\lim _{x \rightarrow \infty} \frac{\sqrt{2 x^{2}+1}}{3 x-5} & =\lim _{x \rightarrow \infty} \frac{\frac{\sqrt{2 x^{2}+1}}{x}}{\frac{3 x-5}{x}}=\lim _{x \rightarrow \infty} \frac{\sqrt{\frac{2 x^{2}+1}{x^{2}}}}{\frac{3 x-5}{x}} \quad\left(\text { since } \sqrt{x^{2}}=x \text { for } x>0\right) \\
& =\frac{\lim _{x \rightarrow \infty} \sqrt{2+\frac{1}{x^{2}}}}{\lim _{x \rightarrow \infty}\left(3-\frac{5}{x}\right)}=\frac{\sqrt{\lim _{x \rightarrow \infty} 2+\lim _{x \rightarrow \infty} \frac{1}{x^{2}}}}{\lim _{x \rightarrow \infty} 3-5 \lim _{x \rightarrow \infty} \frac{1}{x}}=\frac{\sqrt{2+0}}{3-5 \cdot 0}=\frac{\sqrt{2}}{3}
\end{aligned}
$$

Therefore the line $y=\sqrt{2} / 3$ is a horizontal asymptote of the graph of $f$.
In computing the limit as $x \rightarrow-\infty$, we must remember that for $x<0$, we have $\sqrt{x^{2}}=|x|=-x$. So when we divide the numerator by $x$, for $x<0$ we get

$$
\frac{\sqrt{2 x^{2}+1}}{x}=\frac{\sqrt{2 x^{2}+1}}{-\sqrt{x^{2}}}=-\sqrt{\frac{2 x^{2}+1}{x^{2}}}=-\sqrt{2+\frac{1}{x^{2}}}
$$

Therefore

$$
\lim _{x \rightarrow-\infty} \frac{\sqrt{2 x^{2}+1}}{3 x-5}=\lim _{x \rightarrow-\infty} \frac{-\sqrt{2+\frac{1}{x^{2}}}}{3-\frac{5}{x}}=\frac{-\sqrt{2+\lim _{x \rightarrow-\infty} \frac{1}{x^{2}}}}{3-5 \lim _{x \rightarrow-\infty} \frac{1}{x}}=-\frac{\sqrt{2}}{3}
$$

Thus the line $y=-\sqrt{2} / 3$ is also a horizontal asymptote. See Figure 8. $\square$

EXAMPLE 5 Compute $\lim _{x \rightarrow \infty}\left(\sqrt{x^{2}+1}-x\right)$.
SOLUTION Because both $\sqrt{x^{2}+1}$ and $x$ are large when $x$ is large, it's difficult to see what happens to their difference, so we use algebra to rewrite the function. We first multiply numerator and denominator by the conjugate radical:

$$
\begin{aligned}
\lim _{x \rightarrow \infty}\left(\sqrt{x^{2}+1}-x\right) & =\lim _{x \rightarrow \infty}\left(\sqrt{x^{2}+1}-x\right) \cdot \frac{\sqrt{x^{2}+1}+x}{\sqrt{x^{2}+1}+x} \\
& =\lim _{x \rightarrow \infty} \frac{\left(x^{2}+1\right)-x^{2}}{\sqrt{x^{2}+1}+x}=\lim _{x \rightarrow \infty} \frac{1}{\sqrt{x^{2}+1}+x}
\end{aligned}
$$

Notice that the denominator of this last expression $\left(\sqrt{x^{2}+1}+x\right)$ becomes large as $x \rightarrow \infty$ (it's bigger than $x$ ). So

$$
\lim _{x \rightarrow \infty}\left(\sqrt{x^{2}+1}-x\right)=\lim _{x \rightarrow \infty} \frac{1}{\sqrt{x^{2}+1}+x}=0
$$

Figure 9 illustrates this result. $\square$

EXAMPLE 6 Evaluate $\lim _{x \rightarrow 2^{+}} \arctan \left(\frac{1}{x-2}\right)$.
SOLUTION If we let $t=1 /(x-2)$, we know that $t \rightarrow \infty$ as $x \rightarrow 2^{+}$. Therefore, by the second equation in (4), we have

$$
\lim _{x \rightarrow 2^{+}} \arctan \left(\frac{1}{x-2}\right)=\lim _{t \rightarrow \infty} \arctan t=\frac{\pi}{2}
$$ $\square$

The graph of the natural exponential function $y=e^{x}$ has the line $y=0$ (the $x$-axis) as a horizontal asymptote. (The same is true of any exponential function with base $b>1$.) In fact, from the graph in Figure 10 and the corresponding table of values, we see that

6

$$
\lim _{x \rightarrow-\infty} e^{x}=0
$$

Notice that the values of $e^{x}$ approach 0 very rapidly.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0167.jpg?height=364&width=420&top_left_y=1012&top_left_x=785)

| $x$ | $e^{x}$ |
| :--- | :--- |
| 0 | 1.00000 |
| -1 | 0.36788 |
| -2 | 0.13534 |
| -3 | 0.04979 |
| -5 | 0.00674 |
| -8 | 0.00034 |
| -10 | 0.00005 |

EXAMPLE 7 Evaluate $\lim _{x \rightarrow 0^{-}} e^{1 / x}$.
SOLUTION If we let $t=1 / x$, we know that $t \rightarrow-\infty$ as $x \rightarrow 0^{-}$. Therefore, by (6),

$$
\lim _{x \rightarrow 0^{-}} e^{1 / x}=\lim _{t \rightarrow-\infty} e^{t}=0
$$

(See Exercise 81.) $\square$

EXAMPLE 8 Evaluate $\lim _{x \rightarrow \infty} \sin x$.
SOLUTION As $x$ increases, the values of $\sin x$ oscillate between 1 and -1 infinitely often and so they don't approach any definite number. Thus $\lim _{x \rightarrow \infty} \sin x$ does not exist. $\square$

## ■ Infinite Limits at Infinity

The notation

$$
\lim _{x \rightarrow \infty} f(x)=\infty
$$

is used to indicate that the values of $f(x)$ become large as $x$ becomes large. Similar meanings are attached to the following symbols:

$$
\lim _{x \rightarrow-\infty} f(x)=\infty \quad \lim _{x \rightarrow \infty} f(x)=-\infty \quad \lim _{x \rightarrow-\infty} f(x)=-\infty
$$

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0168.jpg?height=311&width=318&top_left_y=458&top_left_x=249)
FIGURE 11
$\lim _{x \rightarrow \infty} x^{3}=\infty, \lim _{x \rightarrow-\infty} x^{3}=-\infty$

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0168.jpg?height=450&width=433&top_left_y=979&top_left_x=245)
FIGURE 12
$e^{x}$ is much larger than $x^{3}$ when $x$ is large.

EXAMPLE 9 Find $\lim _{x \rightarrow \infty} x^{3}$ and $\lim _{x \rightarrow-\infty} x^{3}$.
SOLUTION When $x$ becomes large, $x^{3}$ also becomes large. For instance,

$$
10^{3}=1000 \quad 100^{3}=1,000,000 \quad 1000^{3}=1,000,000,000
$$

In fact, we can make $x^{3}$ as big as we like by requiring $x$ to be large enough. Therefore we can write

$$
\lim _{x \rightarrow \infty} x^{3}=\infty
$$

Similarly, when $x$ is large negative, so is $x^{3}$. Thus

$$
\lim _{x \rightarrow-\infty} x^{3}=-\infty
$$

These limit statements can also be seen from the graph of $y=x^{3}$ in Figure 11. $\square$

Looking at Figure 10 we see that

$$
\lim _{x \rightarrow \infty} e^{x}=\infty
$$

but, as Figure 12 demonstrates, $y=e^{x}$ becomes large as $x \rightarrow \infty$ at a much faster rate than $y=x^{3}$.

EXAMPLE 10 Find $\lim _{x \rightarrow \infty}\left(x^{2}-x\right)$.
SOLUTION Limit Law 2 says that the limit of a difference is the difference of the limits, provided that these limits exist. We cannot use Law 2 here because

$$
\lim _{x \rightarrow \infty} x^{2}=\infty \quad \text { and } \quad \lim _{x \rightarrow \infty} x=\infty
$$

In general, the Limit Laws can't be applied to infinite limits because $\infty$ is not a number $(\infty-\infty$ can't be defined). However, we can write

$$
\lim _{x \rightarrow \infty}\left(x^{2}-x\right)=\lim _{x \rightarrow \infty} x(x-1)=\infty
$$

because both $x$ and $x-1$ become arbitrarily large and so their product does too. $\square$

EXAMPLE 11 Find $\lim _{x \rightarrow \infty} \frac{x^{2}+x}{3-x}$.
SOLUTION As in Example 3, we divide the numerator and denominator by the highest power of $x$ in the denominator, which is simply $x$ :

$$
\lim _{x \rightarrow \infty} \frac{x^{2}+x}{3-x}=\lim _{x \rightarrow \infty} \frac{x+1}{\frac{3}{x}-1}=-\infty
$$

because $x+1 \rightarrow \infty$ and $3 / x-1 \rightarrow 0-1=-1$ as $x \rightarrow \infty$. $\square$

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0169.jpg?height=361&width=419&top_left_y=560&top_left_x=119)
FIGURE 13
$y=(x-2)^{4}(x+1)^{3}(x-1)$

The next example shows that by using infinite limits at infinity, together with intercepts, we can get a rough idea of the graph of a polynomial without having to plot a large number of points.

EXAMPLE 12 Sketch the graph of $y=(x-2)^{4}(x+1)^{3}(x-1)$ by finding its intercepts and its limits as $x \rightarrow \infty$ and as $x \rightarrow-\infty$.

SOLUTION The $y$-intercept is $f(0)=(-2)^{4}(1)^{3}(-1)=-16$ and the $x$-intercepts are found by setting $y=0: x=2,-1,1$. Notice that since $(x-2)^{4}$ is never negative, the function doesn't change sign at 2; thus the graph doesn't cross the $x$-axis at 2. The graph crosses the axis at -1 and 1.

When $x$ is large positive, all three factors are large, so

$$
\lim _{x \rightarrow \infty}(x-2)^{4}(x+1)^{3}(x-1)=\infty
$$

When $x$ is large negative, the first factor is large positive and the second and third factors are both large negative, so

$$
\lim _{x \rightarrow-\infty}(x-2)^{4}(x+1)^{3}(x-1)=\infty
$$

Combining this information, we give a rough sketch of the graph in Figure 13. $\square$

## ■ Precise Definitions

Definition 1 can be stated precisely as follows.

7 Precise Definition of a Limit at Infinity Let $f$ be a function defined onsome interval $(a, \infty)$. Then

$$
\lim _{x \rightarrow \infty} f(x)=L
$$

means that for every $\varepsilon>0$ there is a corresponding number $N$ such that

$$
\text { if } \quad x>N \quad \text { then } \quad|f(x)-L|<\varepsilon
$$

In words, this says that the values of $f(x)$ can be made arbitrarily close to $L$ (within a distance $\varepsilon$, where $\varepsilon$ is any positive number) by requiring $x$ to be sufficiently large (larger than $N$, where $N$ depends on $\varepsilon$ ). Graphically, it says that by keeping $x$ large enough (larger than some number $N$ ) we can make the graph of $f$ lie between the given horizontal lines $y=L-\varepsilon$ and $y=L+\varepsilon$ as in Figure 14. This must be true no matter how small we choose $\varepsilon$.

FIGURE 14
$\lim _{x \rightarrow \infty} f(x)=L$
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0169.jpg?height=372&width=1175&top_left_y=1912&top_left_x=678)

FIGURE 15
$\lim _{x \rightarrow \infty} f(x)=L$
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0170.jpg?height=360&width=1086&top_left_y=380&top_left_x=849)

Similarly, a precise version of Definition 2 is given by Definition 8, which is illustrated in Figure 16.

8 Definition Let $f$ be a function defined on some interval $(-\infty, a)$. Then

$$
\lim _{x \rightarrow-\infty} f(x)=L
$$

means that for every $\varepsilon>0$ there is a corresponding number $N$ such that

$$
\text { if } \quad x<N \quad \text { then } \quad|f(x)-L|<\varepsilon
$$

FIGURE 16
$\lim _{x \rightarrow-\infty} f(x)=L$
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0170.jpg?height=349&width=1099&top_left_y=1331&top_left_x=842)

In Example 3 we calculated that

$$
\lim _{x \rightarrow \infty} \frac{3 x^{2}-x-2}{5 x^{2}+4 x+1}=\frac{3}{5}
$$

In the next example we use a calculator (or computer) to relate this statement to Definition 7 with $L=\frac{3}{5}=0.6$ and $\varepsilon=0.1$.

EXAMPLE 13 Use a graph to find a number $N$ such that
if

$$
x>N \quad \text { then } \quad\left|\frac{3 x^{2}-x-2}{5 x^{2}+4 x+1}-0.6\right|<0.1
$$

Figure 15 shows that if a smaller value of $\varepsilon$ is chosen, then a larger value of $N$ may be required.

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0171.jpg?height=313&width=451&top_left_y=420&top_left_x=118)
FIGURE 17

SOLUTION We rewrite the given inequality as

$$
0.5<\frac{3 x^{2}-x-2}{5 x^{2}+4 x+1}<0.7
$$

We need to determine the values of $x$ for which the given curve lies between the horizontal lines $y=0.5$ and $y=0.7$. So we graph the curve and these lines in Figure 17. Then we use the graph to estimate that the curve crosses the line $y=0.5$ when $x \approx 6.7$. To the right of this number it seems that the curve stays between the lines $y=0.5$ and $y=0.7$. Rounding up to be safe, we can say that

$$
\text { if } x>7 \quad \text { then } \quad\left|\frac{3 x^{2}-x-2}{5 x^{2}+4 x+1}-0.6\right|<0.1
$$

In other words, for $\varepsilon=0.1$ we can choose $N=7$ (or any larger number) in Definition 7. $\square$

EXAMPLE 14 Use Definition 7 to prove that $\lim _{x \rightarrow \infty} \frac{1}{x}=0$.
SOLUTION Given $\varepsilon>0$, we want to find $N$ such that

$$
\text { if } \quad x>N \quad \text { then } \quad\left|\frac{1}{x}-0\right|<\varepsilon
$$

In computing the limit we may assume that $x>0$. Then $1 / x<\varepsilon \Longleftrightarrow x>1 / \varepsilon$. Let's choose $N=1 / \varepsilon$. So

$$
\text { if } \quad x>N=\frac{1}{\varepsilon} \quad \text { then } \quad\left|\frac{1}{x}-0\right|=\frac{1}{x}<\varepsilon
$$

Therefore, by Definition 7,

$$
\lim _{x \rightarrow \infty} \frac{1}{x}=0
$$

Figure 18 illustrates the proof by showing some values of $\varepsilon$ and the corresponding values of $N$.

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0171.jpg?height=447&width=442&top_left_y=1788&top_left_x=116)
FIGURE 18

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0172.jpg?height=310&width=488&top_left_y=223&top_left_x=245)
FIGURE 19
$$
\lim _{x \rightarrow \infty} f(x)=\infty
$$

Finally we note that an infinite limit at infinity can be defined as follows. The geometric illustration is given in Figure 19.

9 Precise Definition of an Infinite Limit at Infinity Let $f$ be a function defined on some interval $(a, \infty)$. Then

$$
\lim _{x \rightarrow \infty} f(x)=\infty
$$

means that for every positive number $M$ there is a corresponding positive number $N$ such that

$$
\text { if } \quad x>N \quad \text { then } \quad f(x)>M
$$

Similar definitions apply when the symbol $\infty$ is replaced by $-\infty$. (See Exercise 80.)

## 2.6 | Exercises

1. Explain in your own words the meaning of each of the following.
(a) $\lim _{x \rightarrow \infty} f(x)=5$
(b) $\lim _{x \rightarrow-\infty} f(x)=3$
2. (a) Can the graph of $y=f(x)$ intersect a vertical asymptote? Can it intersect a horizontal asymptote? Illustrate by sketching graphs.
    (b) How many horizontal asymptotes can the graph of $y=f(x)$ have? Sketch graphs to illustrate the possibilities.
3. For the function $f$ whose graph is given, state the following.
(a) $\lim _{x \rightarrow \infty} f(x)$
(b) $\lim _{x \rightarrow-\infty} f(x)$
(c) $\lim _{x \rightarrow 1} f(x)$
(d) $\lim _{x \rightarrow 3} f(x)$
    (e) The equations of the asymptotes
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0172.jpg?height=342&width=634&top_left_y=1724&top_left_x=348)
4. For the function $g$ whose graph is given, state the following.
(a) $\lim _{x \rightarrow \infty} g(x)$
(b) $\lim _{x \rightarrow-\infty} g(x)$
(c) $\lim _{x \rightarrow 0} g(x)$
(d) $\lim _{x \rightarrow 2^{-}} g(x)$
(e) $\lim _{x \rightarrow 2^{+}} g(x)$
(f) The equations of the asymptotes

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0172.jpg?height=342&width=634&top_left_y=1124&top_left_x=1264)

5-10 Sketch the graph of an example of a function $f$ that satisfies all of the given conditions.

5. $f(2)=4, \quad f(-2)=-4, \quad \lim _{x \rightarrow-\infty} f(x)=0, \quad \lim _{x \rightarrow \infty} f(x)=2$
6. $f(0)=0, \quad \lim _{x \rightarrow 1^{-}} f(x)=\infty, \quad \lim _{x \rightarrow 1^{+}} f(x)=-\infty$,
$$
\lim _{x \rightarrow-\infty} f(x)=-2, \quad \lim _{x \rightarrow \infty} f(x)=-2
$$
7. $\lim _{x \rightarrow 0} f(x)=\infty, \quad \lim _{x \rightarrow 3^{-}} f(x)=-\infty, \quad \lim _{x \rightarrow 3^{+}} f(x)=\infty$,
$$
\lim _{x \rightarrow-\infty} f(x)=1, \quad \lim _{x \rightarrow \infty} f(x)=-1
$$
8. $\lim _{x \rightarrow-\infty} f(x)=-\infty, \quad \lim _{x \rightarrow-2^{-}} f(x)=\infty, \quad \lim _{x \rightarrow-2^{+}} f(x)=-\infty$,
$$
\lim _{x \rightarrow 2} f(x)=\infty, \quad \lim _{x \rightarrow \infty} f(x)=\infty
$$
9. $f(0)=0, \quad \lim _{x \rightarrow 1} f(x)=-\infty, \quad \lim _{x \rightarrow \infty} f(x)=-\infty, \quad f$ is odd
10. $\lim _{x \rightarrow-\infty} f(x)=-1, \quad \lim _{x \rightarrow 0^{-}} f(x)=\infty, \quad \lim _{x \rightarrow 0^{+}} f(x)=-\infty$,
$$
\lim _{x \rightarrow 3^{-}} f(x)=1, \quad f(3)=4, \quad \lim _{x \rightarrow 3^{+}} f(x)=4, \quad \lim _{x \rightarrow \infty} f(x)=1
$$

11. Guess the value of the limit
$$
\lim _{x \rightarrow \infty} \frac{x^{2}}{2^{x}}
$$
by evaluating the function $f(x)=x^{2} / 2^{x}$ for $x=0,1,2,3$, 4, 5, 6, 7, 8, 9, 10, 20, 50, and 100. Then use a graph of $f$ to support your guess.
12. (a) Use a graph of
$$
f(x)=\left(1-\frac{2}{x}\right)^{x}
$$
to estimate the value of $\lim _{x \rightarrow \infty} f(x)$ correct to two decimal places.
    (b) Use a table of values of $f(x)$ to estimate the limit to four decimal places.

13-14 Evaluate the limit and justify each step by indicating the appropriate properties of limits.
13. $\lim _{x \rightarrow \infty} \frac{2 x^{2}-7}{5 x^{2}+x-3}$
14. $\lim _{x \rightarrow \infty} \sqrt{\frac{9 x^{3}+8 x-4}{3-5 x+x^{3}}}$
15-42 Find the limit or show that it does not exist.
15. $\lim _{x \rightarrow \infty} \frac{4 x+3}{5 x-1}$
16. $\lim _{x \rightarrow \infty} \frac{-2}{3 x+7}$
17. $\lim _{t \rightarrow-\infty} \frac{3 t^{2}+t}{t^{3}-4 t+1}$
18. $\lim _{t \rightarrow-\infty} \frac{6 t^{2}+t-5}{9-2 t^{2}}$
19. $\lim _{r \rightarrow \infty} \frac{r-r^{3}}{2-r^{2}+3 r^{3}}$
20. $\lim _{x \rightarrow \infty} \frac{3 x^{3}-8 x+2}{4 x^{3}-5 x^{2}-2}$
21. $\lim _{x \rightarrow \infty} \frac{4-\sqrt{x}}{2+\sqrt{x}}$
22. $\lim _{u \rightarrow-\infty} \frac{\left(u^{2}+1\right)\left(2 u^{2}-1\right)}{\left(u^{2}+2\right)^{2}}$
23. $\lim _{x \rightarrow \infty} \frac{\sqrt{x+3 x^{2}}}{4 x-1}$
24. $\lim _{t \rightarrow \infty} \frac{t+3}{\sqrt{2 t^{2}-1}}$
25. $\lim _{x \rightarrow \infty} \frac{\sqrt{1+4 x^{6}}}{2-x^{3}}$
26. $\lim _{x \rightarrow-\infty} \frac{\sqrt{1+4 x^{6}}}{2-x^{3}}$
27. $\lim _{x \rightarrow-\infty} \frac{2 x^{5}-x}{x^{4}+3}$
28. $\lim _{q \rightarrow \infty} \frac{q^{3}+6 q-4}{4 q^{2}-3 q+3}$
29. $\lim _{t \rightarrow \infty}\left(\sqrt{25 t^{2}+2}-5 t\right)$
30. $\lim _{x \rightarrow-\infty}\left(\sqrt{4 x^{2}+3 x}+2 x\right)$
31. $\lim _{x \rightarrow \infty}\left(\sqrt{x^{2}+a x}-\sqrt{x^{2}+b x}\right)$
32. $\lim _{x \rightarrow \infty}(x-\sqrt{x})$
33. $\lim _{x \rightarrow-\infty}\left(x^{2}+2 x^{7}\right)$
34. $\lim _{x \rightarrow \infty}\left(e^{-x}+2 \cos 3 x\right)$
35. $\lim _{x \rightarrow \infty}\left(e^{-2 x} \cos x\right)$
36. $\lim _{x \rightarrow \infty} \frac{\sin ^{2} x}{x^{2}+1}$
37. $\lim _{x \rightarrow \infty} \frac{1-e^{x}}{1+2 e^{x}}$
38. $\lim _{x \rightarrow \infty} \frac{e^{3 x}-e^{-3 x}}{e^{3 x}+e^{-3 x}}$
39. $\lim _{x \rightarrow(\pi / 2)^{+}} e^{\sec x}$
40. $\lim _{x \rightarrow 0^{+}} \tan ^{-1}(\ln x)$
41. $\lim _{x \rightarrow \infty}\left[\ln \left(1+x^{2}\right)-\ln (1+x)\right]$
42. $\lim _{x \rightarrow \infty}[\ln (2+x)-\ln (1+x)]$

43. (a) For $f(x)=\frac{x}{\ln x}$ find each of the following limits.
(i) $\lim _{x \rightarrow 0^{+}} f(x)$
(ii) $\lim _{x \rightarrow 1^{-}} f(x)$
(iii) $\lim _{x \rightarrow 1^{+}} f(x)$
    (b) Use a table of values to estimate $\lim _{x \rightarrow \infty} f(x)$.
    (c) Use the information from parts (a) and (b) to make a rough sketch of the graph of $f$.
44. (a) For $f(x)=\frac{2}{x}-\frac{1}{\ln x}$ find each of the following limits.
(i) $\lim _{x \rightarrow \infty} f(x)$
(ii) $\lim _{x \rightarrow 0^{+}} f(x)$
(iii) $\lim _{x \rightarrow 1^{-}} f(x)$
(iv) $\lim _{x \rightarrow 1^{+}} f(x)$
    (b) Use the information from part (a) to make a rough sketch of the graph of $f$.
45. (a) Estimate the value of
$$
\lim _{x \rightarrow-\infty}\left(\sqrt{x^{2}+x+1}+x\right)
$$
by graphing the function $f(x)=\sqrt{x^{2}+x+1}+x$.
    (b) Use a table of values of $f(x)$ to guess the value of the limit.
    (c) Prove that your guess is correct.
46. (a) Use a graph of
$$
f(x)=\sqrt{3 x^{2}+8 x+6}-\sqrt{3 x^{2}+3 x+1}
$$
to estimate the value of $\lim _{x \rightarrow \infty} f(x)$ to one decimal place.
    (b) Use a table of values of $f(x)$ to estimate the limit to four decimal places.
    (c) Find the exact value of the limit.

47-52 Find the horizontal and vertical asymptotes of each curve. You may want to use a graphing calculator (or computer) to check your work by graphing the curve and estimating the asymptotes.
47. $y=\frac{5+4 x}{x+3}$
48. $y=\frac{2 x^{2}+1}{3 x^{2}+2 x-1}$
49. $y=\frac{2 x^{2}+x-1}{x^{2}+x-2}$
50. $y=\frac{1+x^{4}}{x^{2}-x^{4}}$
51. $y=\frac{x^{3}-x}{x^{2}-6 x+5}$
52. $y=\frac{2 e^{x}}{e^{x}-5}$

53. Estimate the horizontal asymptote of the function
$$
f(x)=\frac{3 x^{3}+500 x^{2}}{x^{3}+500 x^{2}+100 x+2000}
$$
by graphing $f$ for $-10 \leqslant x \leqslant 10$. Then calculate the equation of the asymptote by evaluating the limit. How do you explain the discrepancy?
54. (a) Graph the function
$$
f(x)=\frac{\sqrt{2 x^{2}+1}}{3 x-5}
$$
How many horizontal and vertical asymptotes do you observe? Use the graph to estimate the values of the limits
$$
\lim _{x \rightarrow \infty} \frac{\sqrt{2 x^{2}+1}}{3 x-5} \quad \text { and } \quad \lim _{x \rightarrow-\infty} \frac{\sqrt{2 x^{2}+1}}{3 x-5}
$$
    (b) By calculating values of $f(x)$, give numerical estimates of the limits in part (a).
    (c) Calculate the exact values of the limits in part (a). Did you get the same value or different values for these two limits? [In view of your answer to part (a), you might have to check your calculation for the second limit.]
55. Let $P$ and $Q$ be polynomials. Find
$$
\lim _{x \rightarrow \infty} \frac{P(x)}{Q(x)}
$$
if the degree of $P$ is (a) less than the degree of $Q$ and (b) greater than the degree of $Q$.
56. Make a rough sketch of the curve $y=x^{n}$ ( $n$ an integer) for the following five cases:
(i) $n=0$
(ii) $n>0, n$ odd
(iii) $n>0, n$ even
(iv) $n<0, n$ odd
(v) $n<0, n$ even
Then use these sketches to find the following limits.
(a) $\lim _{x \rightarrow 0^{+}} x^{n}$
(b) $\lim _{x \rightarrow 0^{-}} x^{n}$
(c) $\lim _{x \rightarrow \infty} x^{n}$
(d) $\lim _{x \rightarrow-\infty} x^{n}$
57. Find a formula for a function $f$ that satisfies the following conditions:
$$
\begin{aligned}
& \lim _{x \rightarrow \pm \infty} f(x)=0, \quad \lim _{x \rightarrow 0} f(x)=-\infty, \quad f(2)=0, \\
& \lim _{x \rightarrow 3^{-}} f(x)=\infty, \quad \lim _{x \rightarrow 3^{+}} f(x)=-\infty
\end{aligned}
$$
58. Find a formula for a function that has vertical asymptotes $x=1$ and $x=3$ and horizontal asymptote $y=1$.
59. A function $f$ is a ratio of quadratic functions and has a vertical asymptote $x=4$ and just one $x$-intercept, $x=1$. It is known that $f$ has a removable discontinuity at $x=-1$ and $\lim _{x \rightarrow-1} f(x)=2$. Evaluate
(a) $f(0)$
(b) $\lim _{x \rightarrow \infty} f(x)$

60-64 Find the limits as $x \rightarrow \infty$ and as $x \rightarrow-\infty$. Use this information, together with intercepts, to give a rough sketch of the graph as in Example 12.
60. $y=2 x^{3}-x^{4}$
61. $y=x^{4}-x^{6}$
62. $y=x^{3}(x+2)^{2}(x-1)$
63. $y=(3-x)(1+x)^{2}(1-x)^{4}$
64. $y=x^{2}\left(x^{2}-1\right)^{2}(x+2)$

65. (a) Use the Squeeze Theorem to evaluate $\lim _{x \rightarrow \infty} \frac{\sin x}{x}$.
(b) Graph $f(x)=(\sin x) / x$. How many times does the graph cross the asymptote?
66. End Behavior of a Function By the end behavior of a function we mean the behavior of its values as $x \rightarrow \infty$ and as $x \rightarrow-\infty$.
    (a) Describe and compare the end behavior of the functions
$$
P(x)=3 x^{5}-5 x^{3}+2 x \quad Q(x)=3 x^{5}
$$
by graphing both functions in the viewing rectangles [-2, 2] by [-2, 2] and [-10, 10] by [-10,000, 10,000].
    (b) Two functions are said to have the same end behavior if their ratio approaches 1 as $x \rightarrow \infty$. Show that $P$ and $Q$ have the same end behavior.
67. Find $\lim _{x \rightarrow \infty} f(x)$ if, for all $x>1$,
$$
\frac{10 e^{x}-21}{2 e^{x}}<f(x)<\frac{5 \sqrt{x}}{\sqrt{x-1}}
$$
68. (a) A tank contains 5000 L of pure water. Brine that contains 30 g of salt per liter of water is pumped into the tank at a rate of 25 L/min. Show that the concentration of salt after $t$ minutes (in grams per liter) is
$$
C(t)=\frac{30 t}{200+t}
$$
    (b) What happens to the concentration as $t \rightarrow \infty$ ?
69. In Chapter 9 we will be able to show, under certain assumptions, that the velocity $v(t)$ of a falling raindrop at time $t$ is
$$
v(t)=v^{*}\left(1-e^{-g t / v^{*}}\right)
$$
where $g$ is the acceleration due to gravity and $v^{*}$ is the terminal velocity of the raindrop.
    (a) Find $\lim _{t \rightarrow \infty} v(t)$.
    (b) Graph $v(t)$ if $v^{*}=1 \mathrm{~m} / \mathrm{s}$ and $g=9.8 \mathrm{~m} / \mathrm{s}^{2}$. How long does it take for the velocity of the raindrop to reach 99\% of its terminal velocity?
70. (a) By graphing $y=e^{-x / 10}$ and $y=0.1$ on a common screen, discover how large you need to make $x$ so that $e^{-x / 10}<0.1$.
    (b) Can you solve part (a) without using a graph?

71. Use a graph to find a number $N$ such that
if
$$
x>N \quad \text { then } \quad\left|\frac{3 x^{2}+1}{2 x^{2}+x+1}-1.5\right|<0.05
$$
72. For the limit
$$
\lim _{x \rightarrow \infty} \frac{1-3 x}{\sqrt{x^{2}+1}}=-3
$$
illustrate Definition 7 by finding values of $N$ that correspond to $\varepsilon=0.1$ and $\varepsilon=0.05$.
73. For the limit
$$
\lim _{x \rightarrow-\infty} \frac{1-3 x}{\sqrt{x^{2}+1}}=3
$$
illustrate Definition 8 by finding values of $N$ that correspond to $\varepsilon=0.1$ and $\varepsilon=0.05$.
74. For the limit
$$
\lim _{x \rightarrow \infty} \sqrt{x \ln x}=\infty
$$
illustrate Definition 9 by finding a value of $N$ that corresponds to $M=100$.
75. (a) How large do we have to take $x$ so that $1 / x^{2}<0.0001$ ?
    (b) Taking $r=2$ in Theorem 5, we have the statement
$$
\lim _{x \rightarrow \infty} \frac{1}{x^{2}}=0
$$
Prove this directly using Definition 7.
76. (a) How large do we have to take $x$ so that $1 / \sqrt{x}<0.0001$ ?
    (b) Taking $r=\frac{1}{2}$ in Theorem 5, we have the statement
$$
\lim _{x \rightarrow \infty} \frac{1}{\sqrt{x}}=0
$$
Prove this directly using Definition 7.
77. Use Definition 8 to prove that $\lim _{x \rightarrow-\infty} \frac{1}{x}=0$.
78. Prove, using Definition 9, that $\lim _{x \rightarrow \infty} x^{3}=\infty$.
79. Use Definition 9 to prove that $\lim _{x \rightarrow \infty} e^{x}=\infty$.
80. Formulate a precise definition of
$$
\lim _{x \rightarrow-\infty} f(x)=-\infty
$$
Then use your definition to prove that
$$
\lim _{x \rightarrow-\infty}\left(1+x^{3}\right)=-\infty
$$
81. (a) Prove that
and
$$
\begin{aligned}
& \lim _{x \rightarrow \infty} f(x)=\lim _{t \rightarrow 0^{+}} f(1 / t) \\
& \lim _{x \rightarrow-\infty} f(x)=\lim _{t \rightarrow 0^{-}} f(1 / t)
\end{aligned}
$$
assuming that these limits exist.
    (b) Use part (a) and Exercise 65 to find
$$
\lim _{x \rightarrow 0^{+}} x \sin \frac{1}{x}
$$

### 2.7 Derivatives and Rates of Change

Now that we have defined limits and have learned techniques for computing them, we revisit the problems of finding tangent lines and velocities from Section 2.1. The special type of limit that occurs in both of these problems is called a derivative and we will see that it can be interpreted as a rate of change in any of the natural or social sciences or engineering.

■ Tangents
If a curve $C$ has equation $y=f(x)$ and we want to find the tangent line to $C$ at the point $P(a, f(a))$, then we consider (as we did in Section 2.1) a nearby point $Q(x, f(x))$, where $x \neq a$, and compute the slope of the secant line $P Q$ :

$$
m_{P Q}=\frac{f(x)-f(a)}{x-a}
$$

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0176.jpg?height=960&width=533&top_left_y=224&top_left_x=240)
FIGURE 1

Point-slope form for a line through the point $\left(x_{1}, y_{1}\right)$ with slope $m$ :

$$
y-y_{1}=m\left(x-x_{1}\right)
$$

Then we let $Q$ approach $P$ along the curve $C$ by letting $x$ approach $a$. If $m_{P Q}$ approaches a number $m$, then we define the tangent line $\ell$ to be the line through $P$ with slope $m$. (This amounts to saying that the tangent line is the limiting position of the secant line $P Q$ as $Q$ approaches $P$. See Figure 1.)

1 Definition The tangent line to the curve $y=f(x)$ at the point $P(a, f(a))$ is the line through $P$ with slope

$$
m=\lim _{x \rightarrow a} \frac{f(x)-f(a)}{x-a}
$$

provided that this limit exists.

In our first example we confirm the guess we made in Example 2.1.1.
EXAMPLE 1 Find an equation of the tangent line to the parabola $y=x^{2}$ at the point $P(1,1)$.

SOLUTION Here we have $a=1$ and $f(x)=x^{2}$, so the slope is

$$
\begin{aligned}
m & =\lim _{x \rightarrow 1} \frac{f(x)-f(1)}{x-1}=\lim _{x \rightarrow 1} \frac{x^{2}-1}{x-1} \\
& =\lim _{x \rightarrow 1} \frac{(x-1)(x+1)}{x-1} \\
& =\lim _{x \rightarrow 1}(x+1)=1+1=2
\end{aligned}
$$

Using the point-slope form of the equation of a line, we find that an equation of the tangent line at $(1,1)$ is

$$
y-1=2(x-1) \quad \text { or } \quad y=2 x-1
$$ $\square$

We sometimes refer to the slope of the tangent line to a curve at a point as the slope of the curve at the point. The idea is that if we zoom in far enough toward the point, the curve looks almost like a straight line. Figure 2 illustrates this procedure for the curve $y=x^{2}$ in Example 1. The more we zoom in, the more the parabola looks like a line. In other words, the curve becomes almost indistinguishable from its tangent line.

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0176.jpg?height=313&width=445&top_left_y=1877&top_left_x=317)
FIGURE 2
Zooming in toward the point $(1,1)$ on the parabola $y=x^{2}$

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0176.jpg?height=309&width=483&top_left_y=1881&top_left_x=909)
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0176.jpg?height=307&width=477&top_left_y=1883&top_left_x=1530)

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0177.jpg?height=348&width=497&top_left_y=222&top_left_x=121)
FIGURE 3

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0177.jpg?height=354&width=485&top_left_y=1415&top_left_x=118)
FIGURE 4

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0177.jpg?height=324&width=495&top_left_y=1893&top_left_x=121)
FIGURE 5

There is another expression for the slope of a tangent line that is sometimes easier to use. If $h=x-a$, then $x=a+h$ and so the slope of the secant line $P Q$ is

$$
m_{P Q}=\frac{f(a+h)-f(a)}{h}
$$

(See Figure 3 where the case $h>0$ is illustrated and $Q$ is located to the right of $P$. If it happened that $h<0$, however, $Q$ would be to the left of $P$.)

Notice that as $x$ approaches $a, h$ approaches 0 (because $h=x-a$ ) and so the expression for the slope of the tangent line in Definition 1 becomes

$$
m=\lim _{h \rightarrow 0} \frac{f(a+h)-f(a)}{h}
$$
2

EXAMPLE 2 Find an equation of the tangent line to the hyperbola $y=3 / x$ at the point (3, 1).

SOLUTION Let $f(x)=3 / x$. Then, by Equation 2, the slope of the tangent at (3, 1) is

$$
\begin{aligned}
m & =\lim _{h \rightarrow 0} \frac{f(3+h)-f(3)}{h} \\
& =\lim _{h \rightarrow 0} \frac{\frac{3}{3+h}-1}{h}=\lim _{h \rightarrow 0} \frac{\frac{3-(3+h)}{3+h}}{h} \\
& =\lim _{h \rightarrow 0} \frac{-h}{h(3+h)}=\lim _{h \rightarrow 0}-\frac{1}{3+h}=-\frac{1}{3}
\end{aligned}
$$

Therefore an equation of the tangent at the point $(3,1)$ is
which simplifies to

$$
\begin{gathered}
y-1=-\frac{1}{3}(x-3) \\
x+3 y-6=0
\end{gathered}
$$

The hyperbola and its tangent are shown in Figure 4. $\square$

## ■ Velocities

In Section 2.1 we investigated the motion of a ball dropped from the CN Tower and defined its velocity to be the limiting value of average velocities over shorter and shorter time periods.

In general, suppose an object moves along a straight line according to an equation of motion $s=f(t)$, where $s$ is the displacement (directed distance) of the object from the origin at time $t$. The function $f$ that describes the motion is called the position function of the object. In the time interval from $t=a$ to $t=a+h$, the change in position is $f(a+h)-f(a)$. (See Figure 5.)

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0178.jpg?height=351&width=449&top_left_y=227&top_left_x=242)
FIGURE 6

$$
\begin{aligned}
m_{P Q} & =\frac{f(a+h)-f(a)}{h} \\
& =\text { average velocity }
\end{aligned}
$$

The average velocity over this time interval is

$$
\text { average velocity }=\frac{\text { displacement }}{\text { time }}=\frac{f(a+h)-f(a)}{h}
$$

which is the same as the slope of the secant line $P Q$ in Figure 6.
Now suppose we compute the average velocities over shorter and shorter time intervals $[a, a+h]$. In other words, we let $h$ approach 0 . As in the example of the falling ball, we define the velocity (or instantaneous velocity) $v(a)$ at time $t=a$ to be the limit of these average velocities.

3 Definition The instantaneous velocity of an object with position function $f(t)$ at time $t=a$ is

$$
v(a)=\lim _{h \rightarrow 0} \frac{f(a+h)-f(a)}{h}
$$

provided that this limit exists.

This means that the velocity at time $t=a$ is equal to the slope of the tangent line at $P$ (compare Equation 2 and the expression in Definition 3).

Now that we know how to compute limits, let's reconsider the problem of the falling ball from Example 2.1.3.

EXAMPLE 3 Suppose that a ball is dropped from the upper observation deck of the CN Tower, 450 m above the ground.

(a) What is the velocity of the ball after 5 seconds?
(b) How fast is the ball traveling when it hits the ground?

SOLUTION Since two different velocities are requested, it's efficient to start by finding the velocity at a general time $t=a$. Using the equation of motion $s=f(t)=4.9 t^{2}$, we have

$$
\begin{aligned}
v(a) & =\lim _{h \rightarrow 0} \frac{f(a+h)-f(a)}{h}=\lim _{h \rightarrow 0} \frac{4.9(a+h)^{2}-4.9 a^{2}}{h} \\
& =\lim _{h \rightarrow 0} \frac{4.9\left(a^{2}+2 a h+h^{2}-a^{2}\right)}{h}=\lim _{h \rightarrow 0} \frac{4.9\left(2 a h+h^{2}\right)}{h} \\
& =\lim _{h \rightarrow 0} \frac{4.9 h(2 a+h)}{h}=\lim _{h \rightarrow 0} 4.9(2 a+h)=9.8 a
\end{aligned}
$$

(a) The velocity after 5 seconds is $v(5)=(9.8)(5)=49 \mathrm{~m} / \mathrm{s}$.
(b) Since the observation deck is 450 m above the ground, the ball will hit the ground at the time $t$ when $s(t)=450$, that is,
$$
4.9 t^{2}=450
$$
This gives
$$
t^{2}=\frac{450}{4.9} \quad \text { and } \quad t=\sqrt{\frac{450}{4.9}} \approx 9.6 \mathrm{~s}
$$

The velocity of the ball as it hits the ground is therefore

$$
v\left(\sqrt{\frac{450}{4.9}}\right)=9.8 \sqrt{\frac{450}{4.9}} \approx 94 \mathrm{~m} / \mathrm{s}
$$ $\square$

■ Derivatives
We have seen that the same type of limit arises in finding the slope of a tangent line (Equation 2) or the velocity of an object (Definition 3). In fact, limits of the form

$$
\lim _{h \rightarrow 0} \frac{f(a+h)-f(a)}{h}
$$

arise whenever we calculate a rate of change in any of the sciences or engineering, such as a rate of reaction in chemistry or a marginal cost in economics. Since this type of limit occurs so widely, it is given a special name and notation.

4 Definition The derivative of a function $\boldsymbol{f}$ at a number $\boldsymbol{a}$, denoted by $f^{\prime}(a)$, is

$$
f^{\prime}(a)=\lim _{h \rightarrow 0} \frac{f(a+h)-f(a)}{h}
$$

if this limit exists.

If we write $x=a+h$, then we have $h=x-a$ and $h$ approaches 0 if and only if $x$ approaches $a$. Therefore an equivalent way of stating the definition of the derivative, as we saw in finding tangent lines (see Definition 1), is

5

$$
f^{\prime}(a)=\lim _{x \rightarrow a} \frac{f(x)-f(a)}{x-a}
$$

EXAMPLE 4 Use Definition 4 to find the derivative of the function $f(x)=x^{2}-8 x+9$ at the numbers (a) 2 and (b) $a$.

SOLUTION
(a) From Definition 4 we have

$$
\begin{aligned}
f^{\prime}(2) & =\lim _{h \rightarrow 0} \frac{f(2+h)-f(2)}{h} \\
& =\lim _{h \rightarrow 0} \frac{(2+h)^{2}-8(2+h)+9-(-3)}{h} \\
& =\lim _{h \rightarrow 0} \frac{4+4 h+h^{2}-16-8 h+9+3}{h} \\
& =\lim _{h \rightarrow 0} \frac{h^{2}-4 h}{h}=\lim _{h \rightarrow 0} \frac{h(h-4)}{h}=\lim _{h \rightarrow 0}(h-4)=-4
\end{aligned}
$$

(b)

$$
\begin{aligned}
f^{\prime}(a) & =\lim _{h \rightarrow 0} \frac{f(a+h)-f(a)}{h} \\
& =\lim _{h \rightarrow 0} \frac{\left[(a+h)^{2}-8(a+h)+9\right]-\left[a^{2}-8 a+9\right]}{h} \\
& =\lim _{h \rightarrow 0} \frac{a^{2}+2 a h+h^{2}-8 a-8 h+9-a^{2}+8 a-9}{h} \\
& =\lim _{h \rightarrow 0} \frac{2 a h+h^{2}-8 h}{h}=\lim _{h \rightarrow 0}(2 a+h-8)=2 a-8
\end{aligned}
$$

As a check on our work in part (a), notice that if we let $a=2$, then $f^{\prime}(2)=2(2)-8=-4$. $\square$

EXAMPLE 5 Use Equation 5 to find the derivative of the function $f(x)=1 / \sqrt{x}$ at the number $a(a>0)$.

SOLUTION From Equation 5 we get

$$
\begin{aligned}
f^{\prime}(a) & =\lim _{x \rightarrow a} \frac{f(x)-f(a)}{x-a} \\
& =\lim _{x \rightarrow a} \frac{\frac{1}{\sqrt{x}}-\frac{1}{\sqrt{a}}}{x-a}=\lim _{x \rightarrow a} \frac{\frac{1}{\sqrt{x}}-\frac{1}{\sqrt{a}}}{x-a} \cdot \frac{\sqrt{x} \sqrt{a}}{\sqrt{x} \sqrt{a}} \\
& =\lim _{x \rightarrow a} \frac{\sqrt{a}-\sqrt{x}}{\sqrt{a x}(x-a)}=\lim _{x \rightarrow a} \frac{\sqrt{a}-\sqrt{x}}{\sqrt{a x}(x-a)} \cdot \frac{\sqrt{a}+\sqrt{x}}{\sqrt{a}+\sqrt{x}} \\
& =\lim _{x \rightarrow a} \frac{-(x-a)}{\sqrt{a x}(x-a)(\sqrt{a}+\sqrt{x})}=\lim _{x \rightarrow a} \frac{-1}{\sqrt{a x}(\sqrt{a}+\sqrt{x})} \\
& =\frac{-1}{\sqrt{a^{2}}(\sqrt{a}+\sqrt{a})}=\frac{-1}{a \cdot 2 \sqrt{a}}=-\frac{1}{2 a^{3 / 2}}
\end{aligned}
$$

You can verify that using Definition 4 gives the same result. $\square$

We defined the tangent line to the curve $y=f(x)$ at the point $P(a, f(a))$ to be the line that passes through $P$ and has slope $m$ given by Equation 1 or 2. Since, by Definition 4 (and Equation 5), this is the same as the derivative $f^{\prime}(a)$, we can now say the following.

The tangent line to $y=f(x)$ at $(a, f(a))$ is the line through $(a, f(a))$ whose slope is equal to $f^{\prime}(a)$, the derivative of $f$ at $a$.

If we use the point-slope form of the equation of a line, we can write an equation of the tangent line to the curve $y=f(x)$ at the point $(a, f(a))$ :

$$
y-f(a)=f^{\prime}(a)(x-a)
$$

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0181.jpg?height=391&width=446&top_left_y=229&top_left_x=121)
FIGURE 7

EXAMPLE 6 Find an equation of the tangent line to the parabola $y=x^{2}-8 x+9$ at the point (3, -6).

SOLUTION From Example 4(b) we know that the derivative of $f(x)=x^{2}-8 x+9$ at the number $a$ is $f^{\prime}(a)=2 a-8$. Therefore the slope of the tangent line at (3, -6) is $f^{\prime}(3)=2(3)-8=-2$. Thus an equation of the tangent line, shown in Figure 7, is

$$
y-(-6)=(-2)(x-3) \quad \text { or } \quad y=-2 x
$$ $\square$

## ■ Rates of Change

Suppose $y$ is a quantity that depends on another quantity $x$. Thus $y$ is a function of $x$ and we write $y=f(x)$. If $x$ changes from $x_{1}$ to $x_{2}$, then the change in $x$ (also called the increment of $x$ ) is

$$
\Delta x=x_{2}-x_{1}
$$

and the corresponding change in $y$ is

$$
\Delta y=f\left(x_{2}\right)-f\left(x_{1}\right)
$$

The difference quotient

$$
\frac{\Delta y}{\Delta x}=\frac{f\left(x_{2}\right)-f\left(x_{1}\right)}{x_{2}-x_{1}}
$$

is called the average rate of change of $\boldsymbol{y}$ with respect to $\boldsymbol{x}$ over the interval $\left[x_{1}, x_{2}\right]$ and can be interpreted as the slope of the secant line $P Q$ in Figure 8.

FIGURE 8
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0181.jpg?height=483&width=635&top_left_y=1180&top_left_x=941)

By analogy with velocity, we consider the average rate of change over smaller and smaller intervals by letting $x_{2}$ approach $x_{1}$ and therefore letting $\Delta x$ approach 0. The limit of these average rates of change is called the (instantaneous) rate of change of $\boldsymbol{y}$ with respect to $\boldsymbol{x}$ at $x=x_{1}$, which (as in the case of velocity) is interpreted as the slope of the tangent to the curve $y=f(x)$ at $P\left(x_{1}, f\left(x_{1}\right)\right)$ :

6 instantaneous rate of change $=\lim _{\Delta x \rightarrow 0} \frac{\Delta y}{\Delta x}=\lim _{x_{2} \rightarrow x_{1}} \frac{f\left(x_{2}\right)-f\left(x_{1}\right)}{x_{2}-x_{1}}$

We recognize this limit as being the derivative $f^{\prime}\left(x_{1}\right)$.
We know that one interpretation of the derivative $f^{\prime}(a)$ is as the slope of the tangent line to the curve $y=f(x)$ when $x=a$. We now have a second interpretation:

The derivative $f^{\prime}(a)$ is the instantaneous rate of change of $y=f(x)$ with respect to $x$ when $x=a$.

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0182.jpg?height=443&width=444&top_left_y=227&top_left_x=243)
FIGURE 9
The $y$-values are changing rapidly at $P$ and slowly at $Q$.

The connection with the first interpretation is that if we sketch the curve $y=f(x)$, then the instantaneous rate of change is the slope of the tangent to this curve at the point where $x=a$. This means that when the derivative is large (and therefore the curve is steep, as at the point $P$ in Figure 9), the $y$-values change rapidly. When the derivative is small, the curve is relatively flat (as at point $Q$ ) and the $y$-values change slowly.

In particular, if $s=f(t)$ is the position function of a particle that moves along a straight line, then $f^{\prime}(a)$ is the rate of change of the displacement $s$ with respect to the time $t$. In other words, $f^{\prime}(a)$ is the velocity of the particle at time $t=a$. The speed of the particle is the absolute value of the velocity, that is, $\left|f^{\prime}(a)\right|$.

In the next example we discuss the meaning of the derivative of a function that is defined verbally.

EXAMPLE 7 A manufacturer produces bolts of a fabric with a fixed width. The cost of producing $x$ meters of this fabric is $C=f(x)$ dollars.
(a) What is the meaning of the derivative $f^{\prime}(x)$ ? What are its units?
(b) In practical terms, what does it mean to say that $f^{\prime}(1000)=9$ ?
(c) Which do you think is greater, $f^{\prime}(50)$ or $f^{\prime}(500)$ ? What about $f^{\prime}(5000)$ ?

## SOLUTION

(a) The derivative $f^{\prime}(x)$ is the instantaneous rate of change of $C$ with respect to $x$; that is, $f^{\prime}(x)$ means the rate of change of the production cost with respect to the number of meters produced. (Economists call this rate of change the marginal cost. This idea is discussed in more detail in Sections 3.7 and 4.7.)

Because

$$
f^{\prime}(x)=\lim _{\Delta x \rightarrow 0} \frac{\Delta C}{\Delta x}
$$

the units for $f^{\prime}(x)$ are the same as the units for the difference quotient $\Delta C / \Delta x$. Since $\Delta C$ is measured in dollars and $\Delta x$ in meters, it follows that the units for $f^{\prime}(x)$ are dollars per meter.
(b) The statement that $f^{\prime}(1000)=9$ means that, after 1000 meters of fabric have been manufactured, the rate at which the production cost is increasing is $\$ 9 /$ meter . (When $x=1000, C$ is increasing 9 times as fast as $x$.)

Since $\Delta x=1$ is small compared with $x=1000$, we could use the approximation

$$
f^{\prime}(1000) \approx \frac{\Delta C}{\Delta x}=\frac{\Delta C}{1}=\Delta C
$$

and say that the cost of manufacturing the 1000th meter (or the 1001st) is about \$9.
(c) The rate at which the production cost is increasing (per meter) is probably lower when $x=500$ than when $x=50$ (the cost of making the 500th meter is less than the cost of the 50th meter) because of economies of scale. (The manufacturer makes more efficient use of the fixed costs of production.) So

$$
f^{\prime}(50)>f^{\prime}(500)
$$

But, as production expands, the resulting large-scale operation might become inefficient and there might be overtime costs. Thus it is possible that the rate of increase of costs will eventually start to rise. So it may happen that

$$
f^{\prime}(5000)>f^{\prime}(500)
$$ $\square$

In the following example we estimate the rate of change of the national debt with respect to time. Here the function is defined not by a formula but by a table of values.

| $t$ | $D(t)$ |
| :--- | :--- |
| 2000 | 5662.2 |
| 2004 | 7596.1 |
| 2008 | 10,699.8 |
| 2012 | 16,432.7 |
| 2016 | 19,976.8 |

Source: US Dept. of the Treasury

A Note On Units
The units for the average rate of change $\Delta D / \Delta t$ are the units for $\Delta D$ divided by the units for $\Delta t$, namely billions of dollars per year. The instantaneous rate of change is the limit of the average rates of change, so it is measured in the same units: billions of dollars per year.

EXAMPLE 8 Let $D(t)$ be the US national debt at time $t$. The table in the margin gives approximate values of this function by providing end of year estimates, in billions of dollars, from 2000 to 2016. Interpret and estimate the value of $D^{\prime}(2008)$.

SOLUTION The derivative $D^{\prime}(2008)$ means the rate of change of $D$ with respect to $t$ when $t=2008$, that is, the rate of increase of the national debt in 2008.

According to Equation 5,

$$
D^{\prime}(2008)=\lim _{t \rightarrow 2008} \frac{D(t)-D(2008)}{t-2008}
$$

One way we can estimate this value is to compare average rates of change over different time intervals by computing difference quotients, as compiled in the following table.

| $t$ | Time interval | Average rate of change $=\frac{D(t)-D(2008)}{t-2008}$ |
| :--- | :--- | :--- |
| 2000 | [2000, 2008] | 629.7 |
| 2004 | [2004, 2008] | 775.93 |
| 2012 | [2008, 2012] | 1433.23 |
| 2016 | [2008, 2016] | 1159.63 |

From this table we see that $D^{\prime}(2008)$ lies somewhere between 775.93 and 1433.23 billion dollars per year. [Here we are making the reasonable assumption that the debt didn't fluctuate wildly between 2004 and 2012.] A good estimate for the rate of increase of the US national debt in 2008 would be the average of these two numbers, namely

$$
D^{\prime}(2008) \approx 1105 \text { billion dollars per year }
$$

Another method would be to plot the debt function and estimate the slope of the tangent line when $t=2008$. $\square$

In Examples 3, 7, and 8 we saw three specific examples of rates of change: the velocity of an object is the rate of change of displacement with respect to time; marginal cost is the rate of change of production cost with respect to the number of items produced; the rate of change of the debt with respect to time is of interest in economics. Here is a small sample of other rates of change: In physics, the rate of change of work with respect to time is called power. Chemists who study a chemical reaction are interested in the rate of change in the concentration of a reactant with respect to time (called the rate of reaction). A biologist is interested in the rate of change of the population of a colony of bacteria with respect to time. In fact, the computation of rates of change is important in all of the natural sciences, in engineering, and even in the social sciences. Further examples will be given in Section 3.7.

All these rates of change are derivatives and can therefore be interpreted as slopes of tangents. This gives added significance to the solution of the tangent problem. Whenever we solve a problem involving tangent lines, we are not just solving a problem in geometry. We are also implicitly solving a great variety of problems involving rates of change in science and engineering.

### 2.7 Exercises

2. Graph the curve $y=e^{x}$ in the viewing rectangles [-1, 1] by [0, 2], [-0.5, 0.5] by [0.5, 1.5], and [-0.1, 0.1] by [0.9, 1.1]. What do you notice about the curve as you zoom in toward the point (0, 1)?
3. (a) Find the slope of the tangent line to the parabola $y=x^{2}+3 x$ at the point $(-1,-2)$
(i) using Definition 1
(ii) using Equation 2
    (b) Find an equation of the tangent line in part (a).
    (c) Graph the parabola and the tangent line. As a check on your work, zoom in toward the point (-1, -2) until the parabola and the tangent line are indistinguishable.
4. (a) Find the slope of the tangent line to the curve $y=x^{3}+1$ at the point $(1,2)$
(i) using Definition 1
(ii) using Equation 2
    (b) Find an equation of the tangent line in part (a).
    (c) Graph the curve and the tangent line in successively smaller viewing rectangles centered at $(1,2)$ until the curve and the line appear to coincide.
5-8 Find an equation of the tangent line to the curve at the given point.
5. $y=2 x^{2}-5 x+1, \quad(3,4)$
6. $y=x^{2}-2 x^{3}, \quad(1,-1)$
7. $y=\frac{x+2}{x-3}, \quad(2,-4)$
8. $y=\sqrt{1-3 x}, \quad(-1,2)$
9. (a) Find the slope of the tangent to the curve $y=3+4 x^{2}-2 x^{3}$ at the point where $x=a$.
    (b) Find equations of the tangent lines at the points $(1,5)$ and (2, 3).
    (c) Graph the curve and both tangents on a common screen.
10. (a) Find the slope of the tangent to the curve $y=2 \sqrt{x}$ at the point where $x=a$.
    (b) Find equations of the tangent lines at the points $(1,2)$ and (9, 6).
    (c) Graph the curve and both tangents on a common screen.
11. A cliff diver plunges from a height of 30 m above the water surface. The distance the diver falls in $t$ seconds is given by the function $d(t)=4.9 t^{2} \mathrm{~m}$.
    (a) After how many seconds will the diver hit the water?
    (b) With what velocity does the diver hit the water?
12. If a rock is thrown upward on the planet Mars with a velocity of 10 m/s, its height (in meters) after $t$ seconds is given by $H=10 t-1.86 t^{2}$.
    (a) Find the velocity of the rock after one second.
    (b) Find the velocity of the rock when $t=a$.
    (c) When will the rock hit the surface?
    (d) With what velocity will the rock hit the surface?
13. The displacement (in meters) of a particle moving in a straight line is given by the equation of motion $s=1 / t^{2}$, where $t$ is measured in seconds. Find the velocity of the particle at times $t=a, t=1, t=2$, and $t=3$.
14. The displacement (in meters) of a particle moving in a straight line is given by $s=\frac{1}{2} t^{2}-6 t+23$, where $t$ is measured in seconds.
    (a) Find the average velocity over each time interval:
(i) [4, 8]
(ii) [6, 8]
(iii) [8, 10]
(iv) [8, 12]
    (b) Find the instantaneous velocity when $t=8$.
    (c) Draw the graph of $s$ as a function of $t$ and draw the secant lines whose slopes are the average velocities in part (a). Then draw the tangent line whose slope is the instantaneous velocity in part (b).
15. (a) A particle starts by moving to the right along a horizontal line; the graph of its position function is shown in the figure. When is the particle moving to the right? Moving to the left? Standing still?
    (b) Draw a graph of the velocity function.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0184.jpg?height=249&width=520&top_left_y=1482&top_left_x=1333)
16. Shown are graphs of the position functions of two runners, A and B, who run a 100-meter race and finish in a tie.
    (a) Describe and compare how the runners run the race.
    (b) At what time is the distance between the runners the greatest?
    (c) At what time do they have the same velocity?

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0184.jpg?height=285&width=556&top_left_y=2060&top_left_x=1315)


1. A curve has equation $y=f(x)$.
(a) Write an expression for the slope of the secant line through the points $P(3, f(3))$ and $Q(x, f(x))$.
(b) Write an expression for the slope of the tangent line at $P$.

17. For the function $g$ whose graph is given, arrange the following numbers in increasing order and explain your reasoning:
$$
\begin{array}{cccc}
0 & g^{\prime}(-2) & g^{\prime}(0) & g^{\prime}(2) \\
& & y=g(x) \\
\hdashline-1 & & 1 \\
- & 2 & 3 & 4
\end{array}
$$
18. The graph of a function $f$ is shown.
    (a) Find the average rate of change of $f$ on the interval [20, 60].
    (b) Identify an interval on which the average rate of change of $f$ is 0.
    (c) Compute
$$
\frac{f(40)-f(10)}{40-10}
$$
What does this value represent geometrically?
    (d) Estimate the value of $f^{\prime}(50)$.
    (e) Is $f^{\prime}(10)>f^{\prime}(30)$ ?
    (f) Is $f^{\prime}(60)>\frac{f(80)-f(40)}{80-40} ?$ Explain.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0185.jpg?height=248&width=397&top_left_y=1243&top_left_x=340)
19-20 Use Definition 4 to find $f^{\prime}(a)$ at the given number $a$.
19. $f(x)=\sqrt{4 x+1}, \quad a=6$
20. $f(x)=5 x^{4}, \quad a=-1$
21-22 Use Equation 5 to find $f^{\prime}(a)$ at the given number $a$.
21. $f(x)=\frac{x^{2}}{x+6}, \quad a=3$
22. $f(x)=\frac{1}{\sqrt{2 x+2}}, \quad a=1$
23-26 Find $f^{\prime}(a)$.
23. $f(x)=2 x^{2}-5 x+3$
24. $f(t)=t^{3}-3 t$
25. $f(t)=\frac{1}{t^{2}+1}$
26. $f(x)=\frac{x}{1-4 x}$
27. Find an equation of the tangent line to the graph of $y=B(x)$ at $x=6$ if $B(6)=0$ and $B^{\prime}(6)=-\frac{1}{2}$.
28. Find an equation of the tangent line to the graph of $y=g(x)$ at $x=5$ if $g(5)=-3$ and $g^{\prime}(5)=4$.
29. If $f(x)=3 x^{2}-x^{3}$, find $f^{\prime}(1)$ and use it to find an equation of the tangent line to the curve $y=3 x^{2}-x^{3}$ at the point $(1,2)$.
30. If $g(x)=x^{4}-2$, find $g^{\prime}(1)$ and use it to find an equation of the tangent line to the curve $y=x^{4}-2$ at the point $(1,-1)$.
31. (a) If $F(x)=5 x /\left(1+x^{2}\right)$, find $F^{\prime}(2)$ and use it to find an equation of the tangent line to the curve $y=5 x /\left(1+x^{2}\right)$ at the point (2, 2).
(b) Illustrate part (a) by graphing the curve and the tangent line on the same screen.
32. (a) If $G(x)=4 x^{2}-x^{3}$, find $G^{\prime}(a)$ and use it to find equations of the tangent lines to the curve $y=4 x^{2}-x^{3}$ at the points $(2,8)$ and (3, 9).
(b) Illustrate part (a) by graphing the curve and the tangent lines on the same screen.
33. If an equation of the tangent line to the curve $y=f(x)$ at the point where $a=2$ is $y=4 x-5$, find $f(2)$ and $f^{\prime}(2)$.
34. If the tangent line to $y=f(x)$ at $(4,3)$ passes through the point $(0,2)$, find $f(4)$ and $f^{\prime}(4)$.

35-36 A particle moves along a straight line with equation of motion $s=f(t)$, where $s$ is measured in meters and $t$ in seconds. Find the velocity and the speed when $t=4$.
35. $f(t)=80 t-6 t^{2}$
36. $f(t)=10+\frac{45}{t+1}$

37. A warm can of soda is placed in a cold refrigerator. Sketch the graph of the temperature of the soda as a function of time. Is the initial rate of change of temperature greater or less than the rate of change after an hour?
38. A roast turkey is taken from an oven when its temperature has reached $85^{\circ} \mathrm{C}$ and is placed on a table in a room where the temperature is 24°C. The graph shows how the temperature of the turkey decreases and eventually approaches room temperature. By measuring the slope of the tangent, estimate the rate of change of the temperature after an hour.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0185.jpg?height=357&width=531&top_left_y=1858&top_left_x=1193)
39. Sketch the graph of a function $f$ for which $f(0)=0$, $f^{\prime}(0)=3, f^{\prime}(1)=0$, and $f^{\prime}(2)=-1$.

40. Sketch the graph of a function $g$ for which
$$
\begin{aligned}
& g(0)=g(2)=g(4)=0, g^{\prime}(1)=g^{\prime}(3)=0, \\
& g^{\prime}(0)=g^{\prime}(4)=1, g^{\prime}(2)=-1, \lim _{x \rightarrow \infty} g(x)=\infty, \text { and } \\
& \lim _{x \rightarrow-\infty} g(x)=-\infty .
\end{aligned}
$$
41. Sketch the graph of a function $g$ that is continuous on its domain $(-5,5)$ and where $g(0)=1, g^{\prime}(0)=1, g^{\prime}(-2)=0$, $\lim _{x \rightarrow-5^{+}} g(x)=\infty$, and $\lim _{x \rightarrow 5^{-}} g(x)=3$.
42. Sketch the graph of a function $f$ where the domain is (-2, 2), $f^{\prime}(0)=-2, \lim _{x \rightarrow 2^{-}} f(x)=\infty, f$ is continuous at all numbers in its domain except ±1, and $f$ is odd.
43-48 Each limit represents the derivative of some function $f$ at some number $a$. State such an $f$ and $a$ in each case.
43. $\lim _{h \rightarrow 0} \frac{\sqrt{9+h}-3}{h}$
44. $\lim _{h \rightarrow 0} \frac{e^{-2+h}-e^{-2}}{h}$
45. $\lim _{x \rightarrow 2} \frac{x^{6}-64}{x-2}$
46. $\lim _{x \rightarrow 1 / 4} \frac{\frac{1}{x}-4}{x-\frac{1}{4}}$
47. $\lim _{h \rightarrow 0} \frac{\tan \left(\frac{\pi}{4}+h\right)-1}{h}$
48. $\lim _{\theta \rightarrow \pi / 6} \frac{\sin \theta-\frac{1}{2}}{\theta-\frac{\pi}{6}}$
49. The cost (in dollars) of producing $x$ units of a certain commodity is $C(x)=5000+10 x+0.05 x^{2}$.
    (a) Find the average rate of change of $C$ with respect to $x$ when the production level is changed
        (i) from $x=100$ to $x=105$
        (ii) from $x=100$ to $x=101$
    (b) Find the instantaneous rate of change of $C$ with respect to $x$ when $x=100$. (This is called the marginal cost. Its significance will be explained in Section 3.7.)
50. Let $H(t)$ be the daily cost (in dollars) to heat an office building when the outside temperature is $t$ degrees Celsius.
    (a) What is the meaning of $H^{\prime}(14)$ ? What are its units?
    (b) Would you expect $H^{\prime}(14)$ to be positive or negative? Explain.
51. The cost of producing $x$ kilograms of gold from a new gold mine is $C=f(x)$ dollars.
    (a) What is the meaning of the derivative $f^{\prime}(x)$ ? What are its units?
    (b) What does the statement $f^{\prime}(22)=17$ mean?
    (c) Do you think the values of $f^{\prime}(x)$ will increase or decrease in the short term? What about the long term? Explain.
52. The quantity (in kilograms) of a gourmet ground coffee that is sold by a coffee company at a price of $p$ dollars per kilogram is $Q=f(p)$.
    (a) What is the meaning of the derivative $f^{\prime}(8)$ ? What are its units?
    (b) Is $f^{\prime}(8)$ positive or negative? Explain.
53. The quantity of oxygen that can dissolve in water depends on the temperature of the water. (So thermal pollution influences the oxygen content of water.) The graph shows how oxygen solubility $S$ varies as a function of the water temperature $T$.
    (a) What is the meaning of the derivative $S^{\prime}(T)$ ? What are its units?
    (b) Estimate the value of $S^{\prime}(16)$ and interpret it.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0186.jpg?height=381&width=463&top_left_y=526&top_left_x=1352)
Source: C. Kupchella et al., Environmental Science: Living Within the System of Nature, 2d ed. (Boston: Allyn and Bacon, 1989).
54. The graph shows the influence of the temperature $T$ on the maximum sustainable swimming speed $S$ of Coho salmon.
    (a) What is the meaning of the derivative $S^{\prime}(T)$ ? What are its units?
    (b) Estimate the values of $S^{\prime}(15)$ and $S^{\prime}(25)$ and interpret them.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0186.jpg?height=300&width=529&top_left_y=1286&top_left_x=1320)
55. Researchers measured the average blood alcohol concentration $C(t)$ of eight men starting one hour after consumption of 30 mL of ethanol (corresponding to two alcoholic drinks).

| $t$ (hours) | 1.0 | 1.5 | 2.0 | 2.5 | 3.0 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $C(t)(\mathrm{g} / \mathrm{dL})$ | 0.033 | 0.024 | 0.018 | 0.012 | 0.007 |


    (a) Find the average rate of change of $C$ with respect to $t$ over each time interval:
(i) [1.0, 2.0]
(ii) [1.5, 2.0]
(iii) [2.0, 2.5]
(iv) [2.0, 3.0]
In each case, include the units.
    (b) Estimate the instantaneous rate of change at $t=2$ and interpret your result. What are the units?
Source: Adapted from P. Wilkinson et al., "Pharmacokinetics of Ethanol after Oral Administration in the Fasting State," Journal of Pharmacokinetics and Biopharmaceutics 5 (1977): 207-24.

56. The number $N$ of locations of a popular coffeehouse chain is given in the table. (The numbers of locations as of October 1 are given.)

| Year | $N$ |
| :--- | :--- |
| 2008 | 16,680 |
| 2010 | 16,858 |
| 2012 | 18,066 |
| 2014 | 21,366 |
| 2016 | 25,085 |


    (a) Find the average rate of growth
        (i) from 2008 to 2010
        (ii) from 2010 to 2012
In each case, include the units. What can you conclude?
    (b) Estimate the instantaneous rate of growth in 2010 by taking the average of two average rates of change.
What are its units?
    (c) Estimate the instantaneous rate of growth in 2010 by measuring the slope of a tangent.
57-58 Determine whether $f^{\prime}(0)$ exists.
57. $f(x)= \begin{cases}x \sin \frac{1}{x} & \text { if } x \neq 0 \\ 0 & \text { if } x=0\end{cases}$
58. $f(x)= \begin{cases}x^{2} \sin \frac{1}{x} & \text { if } x \neq 0 \\ 0 & \text { if } x=0\end{cases}$
59. (a) Graph the function $f(x)=\sin x-\frac{1}{1000} \sin (1000 x)$ in the viewing rectangle $[-2 \pi, 2 \pi]$ by [-4,4]. What slope does the graph appear to have at the origin?
    (b) Zoom in to the viewing window [-0.4, 0.4] by $[-0.25,0.25]$ and estimate the value of $f^{\prime}(0)$. Does this agree with your answer from part (a)?
    (c) Now zoom in to the viewing window [-0.008, 0.008] by [-0.005, 0.005]. Do you wish to revise your estimate for $f^{\prime}(0)$ ?
60. Symmetric Difference Quotients In Example 8 we approximated an instantaneous rate of change by averaging two average rates of change. An alternative method is to use a single average rate of change over an interval centered at the desired value. We define the symmetric difference quotient of a function $f$ at $x=a$ on the interval $[a-d, a+d]$ as
$$
\frac{f(a+d)-f(a-d)}{(a+d)-(a-d)}=\frac{f(a+d)-f(a-d)}{2 d}
$$
    (a) Compute the symmetric difference quotient for the function $D$ in Example 8 on the interval [2004, 2012] and verify that your result agrees with the estimate for $D^{\prime}(2008)$ computed in the example.
    (b) Show that the symmetric difference quotient of a function $f$ at $x=a$ is equivalent to averaging the average rates of change of $f$ over the intervals $[a-d, a]$ and $[a, a+d]$.
    (c) Use a symmetric difference quotient to estimate $f^{\prime}(1)$ for $f(x)=x^{3}-2 x^{2}+2$ with $d=0.4$. Draw a graph of $f$ along with secant lines corresponding to average rates of change over the intervals [ $1-d$, 1 ], $[1,1+d]$, and $[1-d, 1+d]$. Which of these secant lines appears to have slope closest to that of the tangent line at $x=1$ ?

## WRITING PROJECT

## EARLY METHODS FOR FINDING TANGENTS

The first person to explicitly formulate the ideas of limits and derivatives was Sir Isaac Newton in the 1660s. But Newton acknowledged that "If I have seen further than other men, it is because I have stood on the shoulders of giants." Two of those giants were Pierre Fermat (1601-1665) and Newton's mentor at Cambridge, Isaac Barrow (1630-1677). Newton was familiar with the methods that these men used to find tangent lines, and their methods played a role in Newton's eventual formulation of calculus.

Learn about these methods by researching on the Internet or reading one of the references listed here. Write an essay comparing the methods of either Fermat or Barrow to modern methods. In particular, use the method of Section 2.7 to find an equation of the tangent line to the curve $y=x^{3}+2 x$ at the point $(1,3)$ and show how either Fermat or Barrow would have solved the same problem. Although you used derivatives and they did not, point out similarities between the methods.

1. C. H. Edwards, The Historical Development of the Calculus (New York: Springer-Verlag, 1979), pp. 124, 132.

2. Howard Eves, An Introduction to the History of Mathematics, 6th ed. (New York: Saunders, 1990), pp. 391, 395.
3. Morris Kline, Mathematical Thought from Ancient to Modern Times (New York: Oxford University Press, 1972), pp. 344, 346.
4. Uta Merzbach and Carl Boyer, A History of Mathematics, 3rd ed. (Hoboken, NJ: Wiley, 2011), pp. 323, 356.

### 2.8 The Derivative as a Function

■ The Derivative Function
In the preceding section we considered the derivative of a function $f$ at a fixed number $a$ :

1

$$
f^{\prime}(a)=\lim _{h \rightarrow 0} \frac{f(a+h)-f(a)}{h}
$$

Here we change our point of view and let the number $a$ vary. If we replace $a$ in Equation 1 by a variable $x$, we obtain

2

$$
f^{\prime}(x)=\lim _{h \rightarrow 0} \frac{f(x+h)-f(x)}{h}
$$

Given any number $x$ for which this limit exists, we assign to $x$ the number $f^{\prime}(x)$. So we can regard $f^{\prime}$ as a new function, called the derivative of $\boldsymbol{f}$ and defined by Equation 2. We know that the value of $f^{\prime}$ at $x, f^{\prime}(x)$, can be interpreted geometrically as the slope of the tangent line to the graph of $f$ at the point $(x, f(x))$.

The function $f^{\prime}$ is called the derivative of $f$ because it has been "derived" from $f$ by the limiting operation in Equation 2. The domain of $f^{\prime}$ is the set $\left\{x \mid f^{\prime}(x)\right.$ exists $\}$ and may be smaller than the domain of $f$.

EXAMPLE 1 The graph of a function $f$ is given in Figure 1. Use it to sketch the graph of the derivative $f^{\prime}$.

FIGURE 1
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0188.jpg?height=375&width=1132&top_left_y=1966&top_left_x=826)

SOLUTION We can estimate the value of the derivative at any value of $x$ by drawing the tangent at the point ( $x, f(x)$ ) and estimating its slope. For instance, for $x=3$ we draw a tangent at $P$ in Figure 2 and estimate its slope to be about $-\frac{2}{3}$. (We have drawn a triangle to help estimate the slope.) Thus $f^{\prime}(3) \approx-\frac{2}{3} \approx-0.67$ and this allows us to plot the point $P^{\prime}(3,-0.67)$ on the graph of $f^{\prime}$ directly beneath $P$. (The slope of the graph of $f$ becomes the $y$-value on the graph of $f^{\prime}$.)

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0189.jpg?height=883&width=1151&top_left_y=566&top_left_x=707)
FIGURE 2

The slope of the tangent drawn at $A$ appears to be about -1 , so we plot the point $A^{\prime}$ with a $y$-value of -1 on the graph of $f^{\prime}$ (directly beneath $A$ ). The tangents at $B$ and $D$ are horizontal, so the derivative is 0 there and the graph of $f^{\prime}$ crosses the $x$-axis (where $y=0$ ) at the points $B^{\prime}$ and $D^{\prime}$, directly beneath $B$ and $D$. Between $B$ and $D$, the graph of $f$ is steepest at $C$ and the tangent line there appears to have slope 1 , so the largest value of $f^{\prime}(x)$ between $B^{\prime}$ and $D^{\prime}$ is 1 (at $C^{\prime}$ ).

Notice that between $B$ and $D$ the tangents have positive slope, so $f^{\prime}(x)$ is positive there. (The graph of $f^{\prime}$ is above the $x$-axis.) But to the right of $D$ the tangents have negative slope, so $f^{\prime}(x)$ is negative there. (The graph of $f^{\prime}$ is below the $x$-axis.) $\square$

## EXAMPLE 2

(a) If $f(x)=x^{3}-x$, find a formula for $f^{\prime}(x)$.
(b) Illustrate this formula by comparing the graphs of $f$ and $f^{\prime}$.

## SOLUTION

(a) When using Equation 2 to compute a derivative, we must remember that the variable

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0190.jpg?height=673&width=465&top_left_y=221&top_left_x=243)
FIGURE 3

is $h$ and that $x$ is temporarily regarded as a constant during the calculation of the limit.

$$
\begin{aligned}
f^{\prime}(x) & =\lim _{h \rightarrow 0} \frac{f(x+h)-f(x)}{h}=\lim _{h \rightarrow 0} \frac{\left[(x+h)^{3}-(x+h)\right]-\left[x^{3}-x\right]}{h} \\
& =\lim _{h \rightarrow 0} \frac{x^{3}+3 x^{2} h+3 x h^{2}+h^{3}-x-h-x^{3}+x}{h} \\
& =\lim _{h \rightarrow 0} \frac{3 x^{2} h+3 x h^{2}+h^{3}-h}{h} \\
& =\lim _{h \rightarrow 0}\left(3 x^{2}+3 x h+h^{2}-1\right)=3 x^{2}-1
\end{aligned}
$$

(b) We use a calculator to graph $f$ and $f^{\prime}$ in Figure 3. Notice that $f^{\prime}(x)=0$ when $f$ has horizontal tangents and $f^{\prime}(x)$ is positive when the tangents have positive slope. So these graphs serve as a check on our work in part (a). $\square$

EXAMPLE 3 If $f(x)=\sqrt{x}$, find the derivative of $f$. State the domain of $f^{\prime}$.
SOLUTION

$$
\begin{aligned}
f^{\prime}(x) & =\lim _{h \rightarrow 0} \frac{f(x+h)-f(x)}{h}=\lim _{h \rightarrow 0} \frac{\sqrt{x+h}-\sqrt{x}}{h} \\
& =\lim _{h \rightarrow 0}\left(\frac{\sqrt{x+h}-\sqrt{x}}{h} \cdot \frac{\sqrt{x+h}+\sqrt{x}}{\sqrt{x+h}+\sqrt{x}}\right) \quad \text { (Rationalize the numerator.) } \\
& =\lim _{h \rightarrow 0} \frac{(x+h)-x}{h(\sqrt{x+h}+\sqrt{x})}=\lim _{h \rightarrow 0} \frac{h}{h(\sqrt{x+h}+\sqrt{x})} \\
& =\lim _{h \rightarrow 0} \frac{1}{\sqrt{x+h}+\sqrt{x}}=\frac{1}{\sqrt{x}+\sqrt{x}}=\frac{1}{2 \sqrt{x}}
\end{aligned}
$$

We see that $f^{\prime}(x)$ exists if $x>0$, so the domain of $f^{\prime}$ is $(0, \infty)$. This is slightly smaller than the domain of $f$, which is $[0, \infty)$. $\square$

Let's check to see that the result of Example 3 is reasonable by looking at the graphs of $f$ and $f^{\prime}$ in Figure 4. When $x$ is close to $0, \sqrt{x}$ is also close to 0 , so $f^{\prime}(x)=1 /(2 \sqrt{x})$ is very large and this corresponds to the steep tangent lines near $(0,0)$ in Figure 4(a) and the large values of $f^{\prime}(x)$ just to the right of 0 in Figure 4(b). When $x$ is large, $f^{\prime}(x)$ is very small and this corresponds to the flatter tangent lines at the far right of the graph of $f$ and the horizontal asymptote of the graph of $f^{\prime}$.

FIGURE 4
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0190.jpg?height=373&width=981&top_left_y=1889&top_left_x=900)

$$
\frac{\frac{a}{b}-\frac{c}{d}}{e}=\frac{a d-b c}{b d} \cdot \frac{1}{e}
$$

EXAMPLE 4 Find $f^{\prime}$ if $f(x)=\frac{1-x}{2+x}$.
SOLUTION

$$
\begin{aligned}
f^{\prime}(x) & =\lim _{h \rightarrow 0} \frac{f(x+h)-f(x)}{h} \\
& =\lim _{h \rightarrow 0} \frac{\frac{1-(x+h)}{2+(x+h)}-\frac{1-x}{2+x}}{h} \\
& =\lim _{h \rightarrow 0} \frac{(1-x-h)(2+x)-(1-x)(2+x+h)}{h(2+x+h)(2+x)} \\
& =\lim _{h \rightarrow 0} \frac{\left(2-x-2 h-x^{2}-x h\right)-\left(2-x+h-x^{2}-x h\right)}{h(2+x+h)(2+x)} \\
& =\lim _{h \rightarrow 0} \frac{-3 h}{h(2+x+h)(2+x)} \\
& =\lim _{h \rightarrow 0} \frac{-3}{(2+x+h)(2+x)}=-\frac{3}{(2+x)^{2}}
\end{aligned}
$$ $\square$

■ Other Notations
If we use the traditional notation $y=f(x)$ to indicate that the independent variable is $x$ and the dependent variable is $y$, then some common alternative notations for the derivative are as follows:

$$
f^{\prime}(x)=y^{\prime}=\frac{d y}{d x}=\frac{d f}{d x}=\frac{d}{d x} f(x)=D f(x)=D_{x} f(x)
$$

The symbols $D$ and $d / d x$ are called differentiation operators because they indicate the operation of differentiation, which is the process of calculating a derivative.

The symbol $d y / d x$, which was introduced by Leibniz, should not be regarded as a ratio (for the time being); it is simply a synonym for $f^{\prime}(x)$. Nonetheless, it is a very useful and suggestive notation, especially when used in conjunction with increment notation. Referring to Equation 2.7.6, we can rewrite the definition of derivative in Leibniz notation in the form

$$
\frac{d y}{d x}=\lim _{\Delta x \rightarrow 0} \frac{\Delta y}{\Delta x}
$$

If we want to indicate the value of a derivative $d y / d x$ in Leibniz notation at a specific number $a$, we use the notation

$$
\left.\left.\frac{d y}{d x}\right|_{x=a} \quad \text { or } \quad \frac{d y}{d x}\right]_{x=a}
$$

which is a synonym for $f^{\prime}(a)$. The vertical bar means "evaluate at."

3 Definition A function $f$ is differentiable at $\boldsymbol{a}$ if $f^{\prime}(a)$ exists. It is differentiable on an open interval $(a, b)$ [or $(a, \infty)$ or $(-\infty, a)$ or $(-\infty, \infty)$ ] if it is differentiable at every number in the interval.

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0192.jpg?height=762&width=461&top_left_y=1487&top_left_x=232)
FIGURE 5

EXAMPLE 5 Where is the function $f(x)=|x|$ differentiable?
SOLUTION If $x>0$, then $|x|=x$ and we can choose $h$ small enough that $x+h>0$ and hence $|x+h|=x+h$. Therefore, for $x>0$, we have

$$
\begin{aligned}
f^{\prime}(x) & =\lim _{h \rightarrow 0} \frac{|x+h|-|x|}{h}=\lim _{h \rightarrow 0} \frac{(x+h)-x}{h} \\
& =\lim _{h \rightarrow 0} \frac{h}{h}=\lim _{h \rightarrow 0} 1=1
\end{aligned}
$$

and so $f$ is differentiable for any $x>0$.
Similarly, for $x<0$ we have $|x|=-x$ and $h$ can be chosen small enough that $x+h<0$ and so $|x+h|=-(x+h)$. Therefore, for $x<0$,

$$
\begin{aligned}
f^{\prime}(x) & =\lim _{h \rightarrow 0} \frac{|x+h|-|x|}{h}=\lim _{h \rightarrow 0} \frac{-(x+h)-(-x)}{h} \\
& =\lim _{h \rightarrow 0} \frac{-h}{h}=\lim _{h \rightarrow 0}(-1)=-1
\end{aligned}
$$

and so $f$ is differentiable for any $x<0$.
For $x=0$ we have to investigate

$$
\begin{aligned}
f^{\prime}(0) & =\lim _{h \rightarrow 0} \frac{f(0+h)-f(0)}{h} \\
& =\lim _{h \rightarrow 0} \frac{|0+h|-|0|}{h}=\lim _{h \rightarrow 0} \frac{|h|}{h} \quad \text { (if it exists) }
\end{aligned}
$$

Let's compute the left and right limits separately:
and

$$
\begin{aligned}
& \lim _{h \rightarrow 0^{+}} \frac{|h|}{h}=\lim _{h \rightarrow 0^{+}} \frac{h}{h}=\lim _{h \rightarrow 0^{+}} 1=1 \\
& \lim _{h \rightarrow 0^{-}} \frac{|h|}{h}=\lim _{h \rightarrow 0^{-}} \frac{-h}{h}=\lim _{h \rightarrow 0^{-}}(-1)=-1
\end{aligned}
$$

Since these limits are different, $f^{\prime}(0)$ does not exist. Thus $f$ is differentiable at all $x$ except 0.

A formula for $f^{\prime}$ is given by

$$
f^{\prime}(x)= \begin{cases}1 & \text { if } x>0 \\ -1 & \text { if } x<0\end{cases}
$$

and its graph is shown in Figure 5(b). The fact that $f^{\prime}(0)$ does not exist is reflected geometrically in the fact that the curve $y=|x|$ does not have a tangent line at ( 0,0 ). [See Figure 5(a).] $\square$

Both continuity and differentiability are desirable properties for a function to have. The following theorem shows how these properties are related.

4 Theorem If $f$ is differentiable at $a$, then $f$ is continuous at $a$.

PROOF To prove that $f$ is continuous at $a$, we have to show that $\lim _{x \rightarrow a} f(x)=f(a)$. We will do this by showing that the difference $f(x)-f(a)$ approaches 0.

The given information is that $f$ is differentiable at $a$, that is,

$$
f^{\prime}(a)=\lim _{x \rightarrow a} \frac{f(x)-f(a)}{x-a}
$$

exists (see Equation 2.7.5). To connect the given and the unknown, we divide and multiply $f(x)-f(a)$ by $x-a$ (which we can do when $x \neq a$ ):

$$
f(x)-f(a)=\frac{f(x)-f(a)}{x-a}(x-a)
$$

Thus, using Limit Law 4, we can write

$$
\begin{aligned}
\lim _{x \rightarrow a}[f(x)-f(a)] & =\lim _{x \rightarrow a} \frac{f(x)-f(a)}{x-a}(x-a) \\
& =\lim _{x \rightarrow a} \frac{f(x)-f(a)}{x-a} \cdot \lim _{x \rightarrow a}(x-a) \\
& =f^{\prime}(a) \cdot 0=0
\end{aligned}
$$

To use what we have just proved, we start with $f(x)$ and add and subtract $f(a)$ :

$$
\begin{aligned}
\lim _{x \rightarrow a} f(x) & =\lim _{x \rightarrow a}[f(a)+(f(x)-f(a))] \\
& =\lim _{x \rightarrow a} f(a)+\lim _{x \rightarrow a}[f(x)-f(a)] \\
& =f(a)+0=f(a)
\end{aligned}
$$

Therefore $f$ is continuous at $a$. $\square$

NOTE The converse of Theorem 4 is false; that is, there are functions that are continuous but not differentiable. For instance, the function $f(x)=|x|$ is continuous at 0 because

$$
\lim _{x \rightarrow 0} f(x)=\lim _{x \rightarrow 0}|x|=0=f(0)
$$

(See Example 2.3.7.) But in Example 5 we showed that $f$ is not differentiable at 0 .

## ■ How Can a Function Fail To Be Differentiable?

We saw that the function $y=|x|$ in Example 5 is not differentiable at 0 and Figure 5(a) shows that its graph changes direction abruptly when $x=0$. In general, if the graph of a function $f$ has a "corner" or "kink" in it, then the graph of $f$ has no tangent at this point and $f$ is not differentiable there. [In trying to compute $f^{\prime}(a)$, we find that the left and right limits are different.]

Theorem 4 gives another way for a function not to have a derivative. It says that if $f$ is not continuous at $a$, then $f$ is not differentiable at $a$. So at any discontinuity (for instance, a jump discontinuity) $f$ fails to be differentiable.

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0194.jpg?height=371&width=473&top_left_y=224&top_left_x=244)
FIGURE 6

A third possibility is that the curve has a vertical tangent line when $x=a$; that is, $f$ is continuous at $a$ and

$$
\lim _{x \rightarrow a}\left|f^{\prime}(x)\right|=\infty
$$

This means that the tangent lines become steeper and steeper as $x \rightarrow a$. Figure 6 shows one way that this can happen; Figure 7(c) shows another. Figure 7 illustrates the three possibilities that we have discussed.

FIGURE 7
Three ways for $f$ not to be differentiable at $a$
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0194.jpg?height=390&width=1202&top_left_y=597&top_left_x=790)

A graphing calculator or computer provides another way of looking at differentiability. If $f$ is differentiable at $a$, then when we zoom in toward the point $(a, f(a))$ the graph straightens out and appears more and more like a line. (See Figure 8. We saw a specific example of this in Figure 2.7.2.) But no matter how much we zoom in toward a point like the ones in Figures 6 and 7(a), we can't eliminate the sharp point or corner (see Figure 9).

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0194.jpg?height=412&width=569&top_left_y=1288&top_left_x=775)
FIGURE 8
$f$ is differentiable at $a$.

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0194.jpg?height=408&width=547&top_left_y=1290&top_left_x=1426)
FIGURE 9
$f$ is not differentiable at $a$.

## ■ Higher Derivatives

If $f$ is a differentiable function, then its derivative $f^{\prime}$ is also a function, so $f^{\prime}$ may have a derivative of its own, denoted by $\left(f^{\prime}\right)^{\prime}=f^{\prime \prime}$. This new function $f^{\prime \prime}$ is called the second derivative of $f$ because it is the derivative of the derivative of $f$. Using Leibniz notation, we write the second derivative of $y=f(x)$ as

$$
\underbrace{\frac{d}{d x}}_{\substack{\text { derivative } \\ \text { of }}} \underbrace{\left(\frac{d y}{d x}\right)}_{\substack{\text { first } \\ \text { derivative }}}=\underbrace{\frac{d^{2} y}{d x^{2}}}_{\substack{\text { second } \\ \text { derivative }}}
$$

EXAMPLE 6 If $f(x)=x^{3}-x$, find and interpret $f^{\prime \prime}(x)$.
SOLUTION In Example 2 we found that the first derivative is $f^{\prime}(x)=3 x^{2}-1$. So the second derivative is

$$
\begin{aligned}
f^{\prime \prime}(x)=\left(f^{\prime}\right)^{\prime}(x) & =\lim _{h \rightarrow 0} \frac{f^{\prime}(x+h)-f^{\prime}(x)}{h} \\
& =\lim _{h \rightarrow 0} \frac{\left[3(x+h)^{2}-1\right]-\left[3 x^{2}-1\right]}{h} \\
& =\lim _{h \rightarrow 0} \frac{3 x^{2}+6 x h+3 h^{2}-1-3 x^{2}+1}{h} \\
& =\lim _{h \rightarrow 0}(6 x+3 h)=6 x
\end{aligned}
$$

The graphs of $f, f^{\prime}$, and $f^{\prime \prime}$ are shown in Figure 10.

FIGURE 10
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0195.jpg?height=326&width=493&top_left_y=841&top_left_x=1019)

We can interpret $f^{\prime \prime}(x)$ as the slope of the curve $y=f^{\prime}(x)$ at the point $\left(x, f^{\prime}(x)\right)$. In other words, it is the rate of change of the slope of the original curve $y=f(x)$.

Notice from Figure 10 that $f^{\prime \prime}(x)$ is negative when $y=f^{\prime}(x)$ has negative slope and positive when $y=f^{\prime}(x)$ has positive slope. So the graphs serve as a check on our calculations. $\square$

In general, we can interpret a second derivative as a rate of change of a rate of change. The most familiar example of this is acceleration, which we define as follows.

If $s=s(t)$ is the position function of an object that moves in a straight line, we know that its first derivative represents the velocity $v(t)$ of the object as a function of time:

$$
v(t)=s^{\prime}(t)=\frac{d s}{d t}
$$

The instantaneous rate of change of velocity with respect to time is called the acceleration $a(t)$ of the object. Thus the acceleration function is the derivative of the velocity function and is therefore the second derivative of the position function:

$$
a(t)=v^{\prime}(t)=s^{\prime \prime}(t)
$$

or, in Leibniz notation,

$$
a=\frac{d v}{d t}=\frac{d^{2} s}{d t^{2}}
$$

Acceleration is the change in velocity you feel when speeding up or slowing down in a car.
The third derivative $f^{\prime \prime \prime}$ is the derivative of the second derivative: $f^{\prime \prime \prime}=\left(f^{\prime \prime}\right)^{\prime}$. So $f^{\prime \prime \prime}(x)$ can be interpreted as the slope of the curve $y=f^{\prime \prime}(x)$ or as the rate of change of $f^{\prime \prime}(x)$. If $y=f(x)$, then alternative notations for the third derivative are

$$
y^{\prime \prime \prime}=f^{\prime \prime \prime}(x)=\frac{d}{d x}\left(\frac{d^{2} y}{d x^{2}}\right)=\frac{d^{3} y}{d x^{3}}
$$

We can also interpret the third derivative physically in the case where the function is the position function $s=s(t)$ of an object that moves along a straight line. Because $s^{\prime \prime \prime}=\left(s^{\prime \prime}\right)^{\prime}=a^{\prime}$, the third derivative of the position function is the derivative of the acceleration function and is called the jerk:

$$
j=\frac{d a}{d t}=\frac{d^{3} s}{d t^{3}}
$$

Thus the jerk $j$ is the rate of change of acceleration. It is aptly named because a large jerk means a sudden change in acceleration, which causes an abrupt movement.

The differentiation process can be continued. The fourth derivative $f^{\prime \prime \prime \prime}$ is usually denoted by $f^{(4)}$. In general, the $n$th derivative of $f$ is denoted by $f^{(n)}$ and is obtained from $f$ by differentiating $n$ times. If $y=f(x)$, we write

$$
y^{(n)}=f^{(n)}(x)=\frac{d^{n} y}{d x^{n}}
$$

EXAMPLE 7 If $f(x)=x^{3}-x$, find $f^{\prime \prime \prime}(x)$ and $f^{(4)}(x)$.
SOLUTION In Example 6 we found that $f^{\prime \prime}(x)=6 x$. The graph of the second derivative has equation $y=6 x$ and so it is a straight line with slope 6. Since the derivative $f^{\prime \prime \prime}(x)$ is the slope of $f^{\prime \prime}(x)$, we have

$$
f^{\prime \prime \prime}(x)=6
$$

for all values of $x$. So $f^{\prime \prime \prime}$ is a constant function and its graph is a horizontal line. Therefore, for all values of $x$,

$$
f^{(4)}(x)=0
$$ $\square$

We have seen that one application of second and third derivatives occurs in analyzing the motion of objects using acceleration and jerk. We will investigate another application of second derivatives in Section 4.3, where we show how knowledge of $f^{\prime \prime}$ gives us information about the shape of the graph of $f$. In Chapter 11 we will see how second and higher derivatives enable us to represent functions as sums of infinite series.

### 2.8 Exercises

1-2 Use the given graph to estimate the value of each derivative. Then sketch the graph of $f^{\prime}$.

1. (a) $f^{\prime}(0)$
(b) $f^{\prime}(1)$
(c) $f^{\prime}(2)$
(d) $f^{\prime}(3)$
(e) $f^{\prime}(4)$
(f) $f^{\prime}(5)$
(g) $f^{\prime}(6)$
(h) $f^{\prime}(7)$

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0196.jpg?height=259&width=385&top_left_y=2102&top_left_x=474)

2. (a) $f^{\prime}(-3)$
(b) $f^{\prime}(-2)$
(c) $f^{\prime}(-1)$
(d) $f^{\prime}(0)$
(e) $f^{\prime}(1)$
(f) $f^{\prime}(2)$
(g) $f^{\prime}(3)$

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0196.jpg?height=300&width=343&top_left_y=2014&top_left_x=1414)

3. Match the graph of each function in (a)-(d) with the graph of its derivative in I-IV. Give reasons for your choices.

(a)
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0197.jpg?height=239&width=271&top_left_y=324&top_left_x=230)

(b)
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0197.jpg?height=238&width=270&top_left_y=324&top_left_x=647)

(c)
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0197.jpg?height=213&width=269&top_left_y=618&top_left_x=231)

(d)
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0197.jpg?height=214&width=268&top_left_y=618&top_left_x=647)

I
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0197.jpg?height=245&width=268&top_left_y=897&top_left_x=231)

II
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0197.jpg?height=246&width=268&top_left_y=898&top_left_x=647)

III
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0197.jpg?height=243&width=267&top_left_y=1202&top_left_x=234)

IV
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0197.jpg?height=242&width=267&top_left_y=1202&top_left_x=650)

4-11 Trace or copy the graph of the given function $f$. (Assume that the axes have equal scales.) Then use the method of Example 1 to sketch the graph of $f^{\prime}$ below it.

4.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0197.jpg?height=252&width=332&top_left_y=1683&top_left_x=178)

5.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0197.jpg?height=254&width=331&top_left_y=1681&top_left_x=600)

6.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0197.jpg?height=254&width=332&top_left_y=2025&top_left_x=178)

7.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0197.jpg?height=252&width=333&top_left_y=2025&top_left_x=615)

8.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0197.jpg?height=252&width=333&top_left_y=241&top_left_x=1095)

9.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0197.jpg?height=251&width=334&top_left_y=230&top_left_x=1536)

10.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0197.jpg?height=251&width=333&top_left_y=564&top_left_x=1094)

11.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0197.jpg?height=253&width=333&top_left_y=570&top_left_x=1517)

12. Shown is the graph of the population function $P(t)$ for yeast cells in a laboratory culture. Use the method of Example 1 to graph the derivative $P^{\prime}(t)$. What does the graph of $P^{\prime}$ tell us about the yeast population?
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0197.jpg?height=284&width=525&top_left_y=1081&top_left_x=1196)
13. A rechargeable battery is plugged into a charger. The graph shows $C(t)$, the percentage of full capacity that the battery reaches as a function of time $t$ elapsed (in hours).
    (a) What is the meaning of the derivative $C^{\prime}(t)$ ?
    (b) Sketch the graph of $C^{\prime}(t)$. What does the graph tell you?

![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0197.jpg?height=363&width=714&top_left_y=1646&top_left_x=1099)

14. The graph (from the US Department of Energy) shows how driving speed affects gas mileage. Fuel economy $F$ is measured in liters per 100 km and speed $v$ is measured in kilometers per hour.
    (a) What is the meaning of the derivative $F^{\prime}(v)$ ?
    (b) Sketch the graph of $F^{\prime}(v)$.


(c) At what speed should you drive if you want to save on gas?
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0198.jpg?height=334&width=646&top_left_y=330&top_left_x=376)
15. The graph shows how the average surface water temperature $f$ of Lake Michigan varies over the course of a year (where $t$ is measured in months with $t=0$ corresponding to January 1). The average was calculated from data obtained over a 20-year period ending in 2011. Sketch the graph of the derivative function $f^{\prime}$. When is $f^{\prime}(t)$ largest?
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0198.jpg?height=337&width=614&top_left_y=966&top_left_x=391)
16-18 Make a careful sketch of the graph of $f$ and below it sketch the graph of $f^{\prime}$ in the same manner as in Exercises 4-11. Can you guess a formula for $f^{\prime}(x)$ from its graph?
16. $f(x)=\sin x$
17. $f(x)=e^{x}$
18. $f(x)=\ln x$
19. Let $f(x)=x^{2}$.
    (a) Estimate the values of $f^{\prime}(0), f^{\prime}\left(\frac{1}{2}\right), f^{\prime}(1)$, and $f^{\prime}(2)$ by zooming in on the graph of $f$.
    (b) Use symmetry to deduce the values of $f^{\prime}\left(-\frac{1}{2}\right), f^{\prime}(-1)$, and $f^{\prime}(-2)$.
    (c) Use the results from parts (a) and (b) to guess a formula for $f^{\prime}(x)$.
    (d) Use the definition of derivative to prove that your guess in part (c) is correct.
20. Let $f(x)=x^{3}$.
    (a) Estimate the values of $f^{\prime}(0), f^{\prime}\left(\frac{1}{2}\right), f^{\prime}(1), f^{\prime}(2)$, and $f^{\prime}(3)$ by zooming in on the graph of $f$.
    (b) Use symmetry to deduce the values of $f^{\prime}\left(-\frac{1}{2}\right), f^{\prime}(-1)$, $f^{\prime}(-2)$, and $f^{\prime}(-3)$.
    (c) Use the values from parts (a) and (b) to graph $f^{\prime}$.
    (d) Guess a formula for $f^{\prime}(x)$.
    (e) Use the definition of derivative to prove that your guess in part (d) is correct.
21-32 Find the derivative of the function using the definition of derivative. State the domain of the function and the domain of its derivative.
21. $f(x)=3 x-8$
22. $f(x)=m x+b$
23. $f(t)=2.5 t^{2}+6 t$
24. $f(x)=4+8 x-5 x^{2}$
25. $A(p)=4 p^{3}+3 p$
26. $F(t)=t^{3}-5 t+1$
27. $f(x)=\frac{1}{x^{2}-4}$
28. $F(v)=\frac{v}{v+2}$
29. $g(u)=\frac{u+1}{4 u-1}$
30. $f(x)=x^{4}$
31. $f(x)=\frac{1}{\sqrt{1+x}}$
32. $g(x)=\frac{1}{1+\sqrt{x}}$
33. (a) Sketch the graph of $f(x)=1+\sqrt{x+3}$ by starting with the graph of $y=\sqrt{x}$ and using the transformations of Section 1.3.
    (b) Use the graph from part (a) to sketch the graph of $f^{\prime}$.
    (c) Use the definition of a derivative to find $f^{\prime}(x)$. What are the domains of $f$ and $f^{\prime}$ ?
    (d) Graph $f^{\prime}$ and compare with your sketch in part (b).
34. (a) If $f(x)=x+1 / x$, find $f^{\prime}(x)$.
    (b) Check to see that your answer to part (a) is reasonable by comparing the graphs of $f$ and $f^{\prime}$.
35. (a) If $f(x)=x^{4}+2 x$, find $f^{\prime}(x)$.
    (b) Check to see that your answer to part (a) is reasonable by comparing the graphs of $f$ and $f^{\prime}$.
36. The table gives the number $N(t)$, measured in thousands, of minimally invasive cosmetic surgery procedures performed in the United States for various years $t$.

| $t$ | $N(t)$ (thousands) |
| :--- | :--- |
| 2000 | 5,500 |
| 2002 | 4,897 |
| 2004 | 7,470 |
| 2006 | 9,138 |
| 2008 | 10,897 |
| 2010 | 11,561 |
| 2012 | 13,035 |
| 2014 | 13,945 |

Source: American Society of Plastic Surgeons


    (a) What is the meaning of $N^{\prime}(t)$ ? What are its units?
    (b) Construct a table of estimated values for $N^{\prime}(t)$.
    (c) Graph $N$ and $N^{\prime}$.
    (d) How would it be possible to get more accurate values for $N^{\prime}(t)$ ?

37. The table gives the height as time passes of a typical pine tree grown for lumber at a managed site.

| Tree age (years) | 14 | 21 | 28 | 35 | 42 | 49 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Height (meters) | 12 | 16 | 19 | 22 | 24 | 25 |

Source: Arkansas Forestry Commission
If $H(t)$ is the height of the tree after $t$ years, construct a table of estimated values for $H^{\prime}$ and sketch its graph.
38. Water temperature affects the growth rate of brook trout. The table shows the amount of weight gained by brook trout after 24 days in various water temperatures.

| Temperature ( ${ }^{\circ} \mathrm{C}$ ) | 15.5 | 17.7 | 20.0 | 22.4 | 24.4 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Weight gained (g) | 37.2 | 31.0 | 19.8 | 9.7 | -9.8 |

If $W(x)$ is the weight gain at temperature $x$, construct a table of estimated values for $W^{\prime}$ and sketch its graph. What are the units for $W^{\prime}(x)$ ?
Source: Adapted from J. Chadwick Jr., "Temperature Effects on Growth and Stress Physiology of Brook Trout: Implications for Climate Change Impacts on an Iconic Cold-Water Fish." Masters Theses. Paper 897. 2012. scholarworks.umass.edu/theses/897.
39. Let $P$ represent the percentage of a city's electrical power that is produced by solar panels $t$ years after January 1, 2020.
    (a) What does $d P / d t$ represent in this context?
    (b) Interpret the statement
$$
\left.\frac{d P}{d t}\right|_{t=2}=3.5
$$
40. Suppose $N$ is the number of people in the United States who travel by car to another state for a vacation in a year when the average price of gasoline is $p$ dollars per liter. Do you expect $d N / d p$ to be positive or negative? Explain.

41-44 The graph of $f$ is given. State, with reasons, the numbers at which $f$ is not differentiable.
41.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0199.jpg?height=249&width=351&top_left_y=2086&top_left_x=176)
42.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0199.jpg?height=251&width=357&top_left_y=2086&top_left_x=598)

43. ![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0199.jpg?height=250&width=331&top_left_y=222&top_left_x=1096)
44. ![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0199.jpg?height=249&width=344&top_left_y=222&top_left_x=1516)
45. Graph the function $f(x)=x+\sqrt{|x|}$. Zoom in repeatedly, first toward the point $(-1,0)$ and then toward the origin. What is different about the behavior of $f$ in the vicinity of these two points? What do you conclude about the differentiability of $f$ ?
46. Zoom in toward the points $(1,0),(0,1)$, and (-1, 0) on the graph of the function $g(x)=\left(x^{2}-1\right)^{2 / 3}$. What do you notice? Account for what you see in terms of the differentiability of $g$.
47-48 The graphs of a function $f$ and its derivative $f^{\prime}$ are shown. Which is bigger, $f^{\prime}(-1)$ or $f^{\prime \prime}(1)$ ?
47. ![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0199.jpg?height=335&width=474&top_left_y=1032&top_left_x=1093)
48. ![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0199.jpg?height=362&width=488&top_left_y=1429&top_left_x=1093)
49. The figure shows the graphs of $f, f^{\prime}$, and $f^{\prime \prime}$. Identify each curve, and explain your choices.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0199.jpg?height=365&width=533&top_left_y=1972&top_left_x=1191)

50. The figure shows graphs of $f, f^{\prime}, f^{\prime \prime}$, and $f^{\prime \prime \prime}$. Identify each curve, and explain your choices.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0200.jpg?height=436&width=411&top_left_y=328&top_left_x=491)
51. The figure shows the graphs of three functions. One is the position function of a car, one is the velocity of the car, and one is its acceleration. Identify each curve, and explain your choices.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0200.jpg?height=368&width=528&top_left_y=999&top_left_x=422)
52. The figure shows the graphs of four functions. One is the position function of a car, one is the velocity of the car, one is its acceleration, and one is its jerk. Identify each curve, and explain your choices.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0200.jpg?height=335&width=555&top_left_y=1582&top_left_x=421)
53-54 Use the definition of a derivative to find $f^{\prime}(x)$ and $f^{\prime \prime}(x)$. Then graph $f, f^{\prime}$, and $f^{\prime \prime}$ on a common screen and check to see if your answers are reasonable.
53. $f(x)=3 x^{2}+2 x+1$
54. $f(x)=x^{3}-3 x$
55. If $f(x)=2 x^{2}-x^{3}$, find $f^{\prime}(x), f^{\prime \prime}(x), f^{\prime \prime \prime}(x)$, and $f^{(4)}(x)$. Graph $f, f^{\prime}, f^{\prime \prime}$, and $f^{\prime \prime \prime}$ on a common screen. Are the graphs consistent with the geometric interpretations of these derivatives?
56. (a) The graph of a position function of a car is shown, where $s$ is measured in meters and $t$ in seconds. Use it to graph the velocity and acceleration of the car. What is the acceleration at $t=10$ seconds?
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0200.jpg?height=346&width=521&top_left_y=416&top_left_x=1334)
    (b) Use the acceleration curve from part (a) to estimate the jerk at $t=10$ seconds. What are the units for jerk?
57. Let $f(x)=\sqrt[3]{x}$.
    (a) If $a \neq 0$, use Equation 2.7.5 to find $f^{\prime}(a)$.
    (b) Show that $f^{\prime}(0)$ does not exist.
    (c) Show that $y=\sqrt[3]{x}$ has a vertical tangent line at (0, 0). (Recall the shape of the graph of $f$. See Figure 1.2.13.)
58. (a) If $g(x)=x^{2 / 3}$, show that $g^{\prime}(0)$ does not exist.
    (b) If $a \neq 0$, find $g^{\prime}(a)$.
    (c) Show that $y=x^{2 / 3}$ has a vertical tangent line at (0, 0).
59. Show that the function $f(x)=|x-6|$ is not differentiable at 6. Find a formula for $f^{\prime}$ and sketch its graph.
60. Where is the greatest integer function $f(x)=\llbracket x \rrbracket$ not differentiable? Find a formula for $f^{\prime}$ and sketch its graph.
61. (a) Sketch the graph of the function $f(x)=x|x|$.
    (b) For what values of $x$ is $f$ differentiable?
    (c) Find a formula for $f^{\prime}$.
62. (a) Sketch the graph of the function $g(x)=x+|x|$.
    (b) For what values of $x$ is $y$ differentiable?
    (c) Find a formula for $g^{\prime}$.
63. Derivatives of Even and Odd Functions Recall that a function $f$ is called even if $f(-x)=f(x)$ for all $x$ in its domain and odd if $f(-x)=-f(x)$ for all such $x$. Prove each of the following.
    (a) The derivative of an even function is an odd function.
    (b) The derivative of an odd function is an even function.

64-65 Left- and Right-Hand Derivatives The left-hand and right-hand derivatives of $f$ at $a$ are defined by
and

$$
\begin{aligned}
f^{\prime}-(a) & =\lim _{h \rightarrow 0^{-}} \frac{f(a+h)-f(a)}{h} \\
f^{\prime}+(a) & =\lim _{h \rightarrow 0^{+}} \frac{f(a+h)-f(a)}{h}
\end{aligned}
$$

if these limits exist. Then $f^{\prime}(a)$ exists if and only if these one-sided derivatives exist and are equal.

64. Find $f^{\prime}-(0)$ and $f^{\prime}(0)$ for the given function $f$. Is $f$ differentiable at 0?
    (a) $$
f(x)= \begin{cases}0 & \text { if } x \leqslant 0 \\ x & \text { if } x>0\end{cases}
$$
    (b) $$
f(x)= \begin{cases}0 & \text { if } x \leqslant 0 \\ x^{2} & \text { if } x>0\end{cases}
$$
65. Let
$$
f(x)= \begin{cases}0 & \text { if } x \leqslant 0 \\ 5-x & \text { if } 0<x<4 \\ \frac{1}{5-x} & \text { if } x \geqslant 4\end{cases}
$$
    (a) Find $f_{-}^{\prime}(4)$ and $f_{+}^{\prime}(4)$.
    (b) Sketch the graph of $f$.
    (c) Where is $f$ discontinuous?
    (d) Where is $f$ not differentiable?
66. When you turn on a hot-water faucet, the temperature $T$ of the water depends on how long the water has been running. In Example 1.1.4 we sketched a possible graph of $T$ as a function of the time $t$ that has elapsed since the faucet was turned on.
    (a) Describe how the rate of change of $T$ with respect to $t$ varies as $t$ increases.
    (b) Sketch a graph of the derivative of $T$.
67. Nick starts jogging and runs faster and faster for 3 mintues, then he walks for 5 minutes. He stops at an intersection for 2 minutes, runs fairly quickly for 5 minutes, then walks for 4 minutes.
    (a) Sketch a possible graph of the distance $s$ Nick has covered after $t$ minutes.
    (b) Sketch a graph of $d s / d t$.
68. Let $\ell$ be the tangent line to the parabola $y=x^{2}$ at the point (1, 1). The angle of inclination of $\ell$ is the angle $\phi$ that $\ell$ makes with the positive direction of the $x$-axis. Calculate $\phi$ correct to the nearest degree.

## 2 REVIEW

CONCEPT CHECK Answers to the Concept Check are available at StewartCalculus.com.

1. Explain what each of the following means and illustrate with a sketch.
(a) $\lim _{x \rightarrow a} f(x)=L$
(b) $\lim _{x \rightarrow a^{+}} f(x)=L$
(c) $\lim _{x \rightarrow a^{-}} f(x)=L$
(d) $\lim _{x \rightarrow a} f(x)=\infty$
(e) $\lim _{x \rightarrow \infty} f(x)=L$
2. Describe several ways in which a limit can fail to exist. Illustrate with sketches.
3. State the following Limit Laws.
    (a) Sum Law
    (b) Difference Law
    (c) Constant Multiple Law
    (d) Product Law
    (e) Quotient Law
    (f) Power Law
    (g) Root Law
4. What does the Squeeze Theorem say?
5. (a) What does it mean to say that the line $x=a$ is a vertical asymptote of the curve $y=f(x)$ ? Draw curves to illustrate the various possibilities.
    (b) What does it mean to say that the line $y=L$ is a horizontal asymptote of the curve $y=f(x)$ ? Draw curves to illustrate the various possibilities.
6. Which of the following curves have vertical asymptotes? Which have horizontal asymptotes?
(a) $y=x^{4}$
(b) $y=\sin x$
(c) $y=\tan x$
(d) $y=\tan ^{-1} x$
(e) $y=e^{x}$
(f) $y=\ln x$
(g) $y=1 / x$
(h) $y=\sqrt{x}$
7. (a) What does it mean for $f$ to be continuous at $a$ ?
    (b) What does it mean for $f$ to be continuous on the interval $(-\infty, \infty)$ ? What can you say about the graph of such a function?
8. (a) Give examples of functions that are continuous on $[-1,1]$.
    (b) Give an example of a function that is not continuous on $[0,1]$.
9. What does the Intermediate Value Theorem say?
10. Write an expression for the slope of the tangent line to the curve $y=f(x)$ at the point $(a, f(a))$.
11. Suppose an object moves along a straight line with position $f(t)$ at time $t$. Write an expression for the instantaneous velocity of the object at time $t=a$. How can you interpret this velocity in terms of the graph of $f$ ?

12. If $y=f(x)$ and $x$ changes from $x_{1}$ to $x_{2}$, write expressions for the following.
    (a) The average rate of change of $y$ with respect to $x$ over the interval $\left[x_{1}, x_{2}\right]$
    (b) The instantaneous rate of change of $y$ with respect to $x$ at $x=x_{1}$
13. Define the derivative $f^{\prime}(a)$. Discuss two ways of interpreting this number.
14. Define the second derivative of $f$. If $f(t)$ is the position function of a particle, how can you interpret the second derivative?
15. (a) What does it mean for $f$ to be differentiable at $a$ ?
    (b) What is the relation between the differentiability and continuity of a function?
    (c) Sketch the graph of a function that is continuous but not differentiable at $a=2$.
16. Describe several ways in which a function can fail to be differentiable. Illustrate with sketches.

## TRUE-FALSE QUIZ

Determine whether the statement is true or false. If it is true, explain why. If it is false, explain why or give an example that disproves the statement.

1. $\lim _{x \rightarrow 4}\left(\frac{2 x}{x-4}-\frac{8}{x-4}\right)=\lim _{x \rightarrow 4} \frac{2 x}{x-4}-\lim _{x \rightarrow 4} \frac{8}{x-4}$
2. $\lim _{x \rightarrow 1} \frac{x^{2}+6 x-7}{x^{2}+5 x-6}=\frac{\lim _{x \rightarrow 1}\left(x^{2}+6 x-7\right)}{\lim _{x \rightarrow 1}\left(x^{2}+5 x-6\right)}$
3. $\lim _{x \rightarrow 1} \frac{x-3}{x^{2}+2 x-4}=\frac{\lim _{x \rightarrow 1}(x-3)}{\lim _{x \rightarrow 1}\left(x^{2}+2 x-4\right)}$
4. $\frac{x^{2}-9}{x-3}=x+3$
5. $\lim _{x \rightarrow 3} \frac{x^{2}-9}{x-3}=\lim _{x \rightarrow 3}(x+3)$
6. If $\lim _{x \rightarrow 5} f(x)=2$ and $\lim _{x \rightarrow 5} g(x)=0$, then $\lim _{x \rightarrow 5}[f(x) / g(x)]$ does not exist.
7. If $\lim _{x \rightarrow 5} f(x)=0$ and $\lim _{x \rightarrow 5} g(x)=0$, then $\lim _{x \rightarrow 5}[f(x) / g(x)]$ does not exist.
8. If neither $\lim _{x \rightarrow a} f(x)$ nor $\lim _{x \rightarrow a} g(x)$ exists, then $\lim _{x \rightarrow a}[f(x)+g(x)]$ does not exist.
9. If $\lim _{x \rightarrow a} f(x)$ exists but $\lim _{x \rightarrow a} g(x)$ does not exist, then $\lim _{x \rightarrow a}[f(x)+g(x)]$ does not exist.
10. If $p$ is a polynomial, then $\lim _{x \rightarrow b} p(x)=p(b)$.
11. If $\lim _{x \rightarrow 0} f(x)=\infty$ and $\lim _{x \rightarrow 0} g(x)=\infty$, then $\lim _{x \rightarrow 0}[f(x)-g(x)]=0$.
12. A function can have two different horizontal asymptotes.
13. If $f$ has domain $[0, \infty)$ and has no horizontal asymptote, then $\lim _{x \rightarrow \infty} f(x)=\infty$ or $\lim _{x \rightarrow \infty} f(x)=-\infty$.
14. If the line $x=1$ is a vertical asymptote of $y=f(x)$, then $f$ is not defined at 1.
15. If $f(1)>0$ and $f(3)<0$, then there exists a number $c$ between 1 and 3 such that $f(c)=0$.
16. If $f$ is continuous at 5 and $f(5)=2$ and $f(4)=3$, then $\lim _{x \rightarrow 2} f\left(4 x^{2}-11\right)=2$.
17. If $f$ is continuous on [-1, 1] and $f(-1)=4$ and $f(1)=3$, then there exists a number $r$ such that $|r|<1$ and $f(r)=\pi$.
18. Let $f$ be a function such that $\lim _{x \rightarrow 0} f(x)=6$. Then there exists a positive number $\delta$ such that if $0<|x|<\delta$, then $|f(x)-6|<1$.
19. If $f(x)>1$ for all $x$ and $\lim _{x \rightarrow 0} f(x)$ exists, then $\lim _{x \rightarrow 0} f(x)>1$.
20. If $f$ is continuous at $a$, then $f$ is differentiable at $a$.
21. If $f^{\prime}(r)$ exists, then $\lim _{x \rightarrow r} f(x)=f(r)$.
22. $\frac{d^{2} y}{d x^{2}}=\left(\frac{d y}{d x}\right)^{2}$
23. The equation $x^{10}-10 x^{2}+5=0$ has a solution in the interval (0, 2).
24. If $f$ is continuous at $a$, so is $|f|$.
25. If $|f|$ is continuous at $a$, so is $f$.
26. If $f$ is differentiable at $a$, so is $|f|$.

## EXERCISES

1. The graph of $f$ is given.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0203.jpg?height=352&width=541&top_left_y=379&top_left_x=272)
    (a) Find each limit, or explain why it does not exist.
(i) $\lim _{x \rightarrow 2^{+}} f(x)$
(ii) $\lim _{x \rightarrow-3^{+}} f(x)$
(iii) $\lim _{x \rightarrow-3} f(x)$
(iv) $\lim _{x \rightarrow 4} f(x)$
(v) $\lim _{x \rightarrow 0} f(x)$
(vi) $\lim _{x \rightarrow 2^{-}} f(x)$
(vii) $\lim _{x \rightarrow \infty} f(x)$
(viii) $\lim _{x \rightarrow-\infty} f(x)$
    (b) State the equations of the horizontal asymptotes.
    (c) State the equations of the vertical asymptotes.
    (d) At what numbers is $f$ discontinuous? Explain.
2. Sketch the graph of a function $f$ that satisfies all of the following conditions:
$$
\begin{aligned}
& \lim _{x \rightarrow-\infty} f(x)=-2, \quad \lim _{x \rightarrow \infty} f(x)=0, \quad \lim _{x \rightarrow-3} f(x)=\infty, \\
& \lim _{x \rightarrow 3^{-}} f(x)=-\infty, \quad \lim _{x \rightarrow 3^{+}} f(x)=2,
\end{aligned}
$$
$f$ is continuous from the right at 3
3-20 Find the limit.
3. $\lim _{x \rightarrow 0} \cos \left(x^{3}+3 x\right)$
4. $\lim _{x \rightarrow 3} \frac{x^{2}-9}{x^{2}+2 x-3}$
5. $\lim _{x \rightarrow-3} \frac{x^{2}-9}{x^{2}+2 x-3}$
6. $\lim _{x \rightarrow 1^{+}} \frac{x^{2}-9}{x^{2}+2 x-3}$
7. $\lim _{h \rightarrow 0} \frac{(h-1)^{3}+1}{h}$
8. $\lim _{t \rightarrow 2} \frac{t^{2}-4}{t^{3}-8}$
9. $\lim _{r \rightarrow 9} \frac{\sqrt{r}}{(r-9)^{4}}$
10. $\lim _{v \rightarrow 4^{+}} \frac{4-v}{|4-v|}$
11. $\lim _{r \rightarrow-1} \frac{r^{2}-3 r-4}{4 r^{2}+r-3}$
12. $\lim _{t \rightarrow 5} \frac{3-\sqrt{t+4}}{t-5}$
13. $\lim _{x \rightarrow \infty} \frac{\sqrt{x^{2}-9}}{2 x-6}$
14. $\lim _{x \rightarrow-\infty} \frac{\sqrt{x^{2}-9}}{2 x-6}$
15. $\lim _{x \rightarrow \pi^{-}} \ln (\sin x)$
16. $\lim _{x \rightarrow-\infty} \frac{1-2 x^{2}-x^{4}}{5+x-3 x^{4}}$
17. $\lim _{x \rightarrow \infty}\left(\sqrt{x^{2}+4 x+1}-x\right)$
18. $\lim _{x \rightarrow \infty} e^{x-x^{2}}$
19. $\lim _{x \rightarrow 0^{+}} \tan ^{-1}(1 / x)$
20. $\lim _{x \rightarrow 1}\left(\frac{1}{x-1}+\frac{1}{x^{2}-3 x+2}\right)$

21-22 Use graphs to discover the asymptotes of the curve. Then prove what you have discovered.
21. $y=\frac{\cos ^{2} x}{x^{2}}$
22. $y=\sqrt{x^{2}+x+1}-\sqrt{x^{2}-x}$
23. If $2 x-1 \leqslant f(x) \leqslant x^{2}$ for $0<x<3$, find $\lim _{x \rightarrow 1} f(x)$.
24. Prove that $\lim _{x \rightarrow 0} x^{2} \cos \left(1 / x^{2}\right)=0$.
25-28 Prove the statement using the precise definition of a limit.
25. $\lim _{x \rightarrow 2}(14-5 x)=4$
26. $\lim _{x \rightarrow 0} \sqrt[3]{x}=0$
27. $\lim _{x \rightarrow 2}\left(x^{2}-3 x\right)=-2$
28. $\lim _{x \rightarrow 4^{+}} \frac{2}{\sqrt{x-4}}=\infty$

29. Let
$$
f(x)= \begin{cases}\sqrt{-x} & \text { if } x<0 \\ 3-x & \text { if } 0 \leqslant x<3 \\ (x-3)^{2} & \text { if } x>3\end{cases}
$$
    (a) Evaluate each limit, if it exists.
(i) $\lim _{x \rightarrow 0^{+}} f(x)$
(ii) $\lim _{x \rightarrow 0^{-}} f(x)$
(iii) $\lim _{x \rightarrow 0} f(x)$
(iv) $\lim _{x \rightarrow 3^{-}} f(x)$
(v) $\lim _{x \rightarrow 3^{+}} f(x)$
(vi) $\lim _{x \rightarrow 3} f(x)$
    (b) Where is $f$ discontinuous?
    (c) Sketch the graph of $f$.
30. Let
$$
g(x)= \begin{cases}2 x-x^{2} & \text { if } 0 \leqslant x \leqslant 2 \\ 2-x & \text { if } 2<x \leqslant 3 \\ x-4 & \text { if } 3<x<4 \\ \pi & \text { if } x \geqslant 4\end{cases}
$$
    (a) For each of the numbers 2, 3, and 4, determine whether $g$ is continuous from the left, continuous from the right, or continuous at the number.
    (b) Sketch the graph of $g$.
31-32 Show that the function is continuous on its domain. State the domain.
31. $h(x)=x e^{\sin x}$
32. $g(x)=\frac{\sqrt{x^{2}-9}}{x^{2}-2}$

33-34 Use the Intermediate Value Theorem to show that there is a solution of the equation in the given interval.

33. $x^{5}-x^{3}+3 x-5=0, \quad(1,2)$
34. $\cos \sqrt{x}=e^{x}-2, \quad(0,1)$

35. (a) Find the slope of the tangent line to the curve $y=9-2 x^{2}$ at the point $(2,1)$.
    (b) Find an equation of this tangent line.
36. Find equations of the tangent lines to the curve
$$
y=\frac{2}{1-3 x}
$$
at the points with $x$-coordinates 0 and -1 .
37. The displacement (in meters) of an object moving in a straight line is given by $s=1+2 t+\frac{1}{4} t^{2}$, where $t$ is measured in seconds.
    (a) Find the average velocity over each time period.
(i) [1, 3]
(ii) [1, 2]
(iii) [1, 1.5]
(iv) [1, 1.1]
    (b) Find the instantaneous velocity when $t=1$.
38. According to Boyle's Law, if the temperature of a confined gas is held fixed, then the product of the pressure $P$ and the volume $V$ is a constant. Suppose that, for a certain gas, $P V=4000$, where $P$ is measured in pascals and $V$ is measured in liters.
    (a) Find the average rate of change of $P$ as $V$ increases from 3 L to 4 L .
    (b) Express $V$ as a function of $P$ and show that the instantaneous rate of change of $V$ with respect to $P$ is inversely proportional to the square of $P$.
39. (a) Use the definition of a derivative to find $f^{\prime}(2)$, where $f(x)=x^{3}-2 x$.
    (b) Find an equation of the tangent line to the curve $y=x^{3}-2 x$ at the point (2, 4).
    (c) Illustrate part (b) by graphing the curve and the tangent line on the same screen.
40. Find a function $f$ and a number $a$ such that
$$
\lim _{h \rightarrow 0} \frac{(2+h)^{6}-64}{h}=f^{\prime}(a)
$$
41. The total cost of repaying a student loan at an interest rate of $r \%$ per year is $C=f(r)$.
    (a) What is the meaning of the derivative $f^{\prime}(r)$ ? What are its units?
    (b) What does the statement $f^{\prime}(10)=1200$ mean?
    (c) Is $f^{\prime}(r)$ always positive or does it change sign?
42-44 Trace or copy the graph of the function. Then sketch a graph of its derivative directly beneath.
42.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0204.jpg?height=257&width=335&top_left_y=2100&top_left_x=344)
43.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0204.jpg?height=257&width=348&top_left_y=2099&top_left_x=765)
44. ![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0204.jpg?height=259&width=332&top_left_y=230&top_left_x=1240)

45-46 Find the derivative of $f$ using the definition of a derivative. What is the domain of $f^{\prime}$ ?
45. $f(x)=\frac{2}{x^{2}}$
46. $f(t)=\frac{1}{\sqrt{t+1}}$

47. (a) If $f(x)=\sqrt{3-5 x}$, use the definition of a derivative to find $f^{\prime}(x)$.
    (b) Find the domains of $f$ and $f^{\prime}$.
    (c) Graph $f$ and $f^{\prime}$ on a common screen. Compare the graphs to see whether your answer to part (a) is reasonable.
48. (a) Find the asymptotes of the graph of
$$
f(x)=\frac{4-x}{3+x}
$$
and use them to sketch the graph.
    (b) Use your graph from part (a) to sketch the graph of $f^{\prime}$.
    (c) Use the definition of a derivative to find $f^{\prime}(x)$.
    (d) Graph $f^{\prime}$ and compare with your sketch in part (b).
49. The graph of $f$ is shown. State, with reasons, the numbers at which $f$ is not differentiable.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0204.jpg?height=322&width=631&top_left_y=1514&top_left_x=1265)
50. The figure shows the graphs of $f, f^{\prime}$, and $f^{\prime \prime}$. Identify each curve, and explain your choices.
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0204.jpg?height=380&width=526&top_left_y=1976&top_left_x=1331)

51. Sketch the graph of a function $f$ that satisfies all of the following conditions:
The domain of $f$ is all real numbers except 0 ,
$$
\lim _{x \rightarrow 0^{-}} f(x)=1, \quad \lim _{x \rightarrow 0^{+}} f(x)=0,
$$
$f^{\prime}(x)>0$ for all $x$ in the domain of $f$,
$$
\lim _{x \rightarrow-\infty} f^{\prime}(x)=0, \quad \lim _{x \rightarrow \infty} f^{\prime}(x)=1
$$
52. Let $P(t)$ be the percentage of Americans under the age of 18 at time $t$. The table gives values of this function in census years from 1950 to 2010.

| $t$ | $P(t)$ | $t$ | $P(t)$ |
| :--- | :--- | :--- | :--- |
| 1950 | 31.1 | 1990 | 25.7 |
| 1960 | 35.7 | 2000 | 25.7 |
| 1970 | 34.0 | 2010 | 24.0 |
| 1980 | 28.0 |  |  |


    (a) What is the meaning of $P^{\prime}(t)$ ? What are its units?
    (b) Construct a table of estimated values for $P^{\prime}(t)$.
    (c) Graph $P$ and $P^{\prime}$.
    (d) How would it be possible to get more accurate values for $P^{\prime}(t)$ ?
53. Let $B(t)$ be the number of US $\$ 20$ bills in circulation at time $t$. The table gives values of this function from 1995 to 2015, as of December 31, in billions. Interpret and estimate the value of $B^{\prime}(2010)$.

| $t$ | 1995 | 2000 | 2005 | 2010 | 2015 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $B(t)$ | 4.21 | 4.93 | 5.77 | 6.53 | 8.57 |
54. The total fertility rate at time $t$, denoted by $F(t)$, is an estimate of the average number of children born to each woman (assuming that current birth rates remain constant). The graph of the total fertility rate in the United States shows the fluctuations from 1940 to 2010.
    (a) Estimate the values of $F^{\prime}(1950), F^{\prime}(1965)$, and $F^{\prime}(1987)$.
    (b) What are the meanings of these derivatives?
    (c) Can you suggest reasons for the values of these derivatives?
![](https://cdn.mathpix.com/cropped/d02e9c21-0c5f-4a16-8c2c-be3b3fbe3c43-0205.jpg?height=459&width=765&top_left_y=688&top_left_x=1076)
55. Suppose that $|f(x)| \leqslant g(x)$ for all $x$, where $\lim _{x \rightarrow a} g(x)=0$. Find $\lim _{x \rightarrow a} f(x)$.
56. Let $f(x)=\llbracket x \rrbracket+\llbracket-x \rrbracket$.
    (a) For what values of $a$ does $\lim _{x \rightarrow a} f(x)$ exist?
    (b) At what numbers is $f$ discontinuous?
