#!/usr/bin/env python3
"""Generate concept graphs for fields/ stage files (mechanics first).

Stage roadmap:
  stage 1  역학.md     -> f_m1..f_m5  (this file currently)
  stage 2  전자기학.md  -> f_e1..      (to be appended)
  stage 3  통합1.md     -> f_t1..      (to be appended)
  stage 4  통합2.md     -> f_t2..      (to be appended)
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

plt.rcParams.update({
    'figure.dpi': 200, 'font.size': 11, 'font.family': 'sans-serif',
    'axes.titlesize': 12, 'axes.labelsize': 11,
    'legend.fontsize': 8.5, 'xtick.labelsize': 8.5, 'ytick.labelsize': 8.5,
    'axes.grid': False, 'figure.facecolor': 'white', 'axes.facecolor': 'white',
})
BASE = os.path.join(os.path.dirname(__file__), 'graphs')
os.makedirs(BASE, exist_ok=True)

BLUE = '#1a73e8'
RED = '#d93025'
GREEN = '#188038'
AMBER = '#f9ab00'
GRAY = '#8a8a8a'
BLACK = '#202020'

def save(fig, name):
    fig.savefig(os.path.join(BASE, name), bbox_inches='tight')
    plt.close(fig)

def arrow(ax, x0, y0, x1, y1, color=RED, lw=2.2):
    ax.annotate('', xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw))

# ═══════════════════════ STAGE 1: 역학 ═══════════════════════

def f_m1_spring_energy():
    """Spring energy diagram: U=0.5kx^2, E-line, turning points, slope -> force."""
    k, m, E = 200.0, 1.0, 4.0
    A = np.sqrt(2*E/k)                     # 0.20 m
    fig, ax = plt.subplots(figsize=(7.4, 4.5))
    x = np.linspace(-0.26, 0.26, 600)
    U = 0.5*k*x**2
    ax.plot(x, U, color=BLUE, lw=2.6, label=r'$U(x)=\frac{1}{2}kx^2$  (Deposit)')
    xr = np.linspace(-A, A, 100)
    ax.plot(xr, np.full_like(xr, E), color=RED, ls='--', lw=2,
            label=r'total energy $E$ (Balance)')
    ax.fill_between(x, U, E, where=(U <= E), color=GREEN, alpha=0.20)

    # turning points
    for s in (-1, 1):
        ax.plot(s*A, E, 'o', color=RED, ms=8, zorder=5)
        ax.annotate(f'turning point\n$x={s*A:+.2f}$ m', xy=(s*A, E),
                    xytext=(s*0.095 - 0.05, 5.1), fontsize=8.5, ha='center',
                    arrowprops=dict(arrowstyle='->', color=GRAY, lw=0.9))

    # tangent at x0 -> slope = kx -> F = -kx
    x0 = 0.10
    U0 = 0.5*k*x0**2
    slope = k*x0                          # 20 N
    xt = np.linspace(0.005, 0.195, 12)
    ax.plot(xt, U0 + slope*(xt - x0), color=AMBER, lw=2.2, zorder=4,
            label=f'slope $=dU/dx={slope:.0f}$ N   $\\Rightarrow$   $F=-{slope:.0f}$ N')
    ax.annotate('$F$ (downhill)', xy=(0.095, U0+0.28), xytext=(0.155, U0+1.35),
                fontsize=9.5, color=RED,
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.4))
    arrow(ax, 0.105, U0+0.3, 0.065, U0+0.3, color=RED, lw=2.4)

    # equilibrium at bottom
    ax.plot(0, 0, 'o', color=BLACK, ms=7, zorder=5)
    ax.annotate('equilibrium:\nslope = 0  →  F = 0', xy=(0, 0), xytext=(0.10, 0.85),
                fontsize=8.5, arrowprops=dict(arrowstyle='->', color=GRAY, lw=0.9))

    # Cash gap annotation at x=0
    ax.annotate('', xy=(0.055, E-0.15), xytext=(0.055, 0.55),
                arrowprops=dict(arrowstyle='<->', color=GREEN, lw=1.8))
    ax.text(0.075, 2.05, 'Cash (KE)\n$=E-U(x)$', fontsize=9.5, color=GREEN)

    ax.set_xlabel('position $x$ (m)')
    ax.set_ylabel('energy (J)')
    ax.set_title('Energy diagram:  $F = -dU/dx$  (the slope, sign flipped)')
    ax.legend(loc='upper center', fontsize=8.5)
    ax.set_ylim(0, 6.4)
    save(fig, 'f_m1_spring_energy.png')
    print(f'[f_m1] k={k} E={E}  A={A:.4f} m  slope@0.10={slope:.1f} N  F={-slope:.1f} N')

def f_m2_gravity_linear():
    """U(h)=mgh: a straight line. slope = mg, E-line crossing = max height."""
    m, g = 2.0, 10.0
    E = 100.0
    h_max = E/(m*g)                        # 5 m
    fig, ax = plt.subplots(figsize=(7.4, 4.5))
    h = np.linspace(0, 6, 100)
    U = m*g*h
    ax.plot(h, U, color=BLUE, lw=2.6, label=r'$U(h)=mgh$  (Deposit)')
    ax.axhline(E, color=RED, ls='--', lw=2, label='total energy $E$ (Balance)')

    # turning point
    ax.plot(h_max, E, 'o', color=RED, ms=8, zorder=5)
    ax.annotate(f'turning point\n$h={h_max:.1f}$ m : Cash $=0$', xy=(h_max, E),
                xytext=(h_max-0.9, 108), fontsize=8.5,
                arrowprops=dict(arrowstyle='->', color=GRAY, lw=0.9))

    # slope triangle  h=2 -> h=5
    h1 = 2.0
    ax.plot([h1, h1], [U[0] if False else m*g*h1, E], color=RED, lw=1.5)
    ax.plot([h1, h_max], [E, E], color=RED, lw=1.5)
    ax.text(h1+0.08, 62, r'$\Delta U = 60$ J', fontsize=9, color=RED)
    ax.text(3.1, E+2.5, r'$\Delta h = 3$ m', fontsize=9, color=RED)
    ax.text(0.15, 88, f'slope = $\\Delta U/\\Delta h$ = $mg$ = {m*g:.0f} N', fontsize=10,
            color=AMBER)

    # downhill force arrow
    arrow(ax, 4.9, 112, 4.9, 92, color=RED, lw=2.4)
    ax.text(5.02, 102, r'$F=-mg=-20$ N', fontsize=9.5, color=RED)

    ax.set_xlabel('height $h$ (m)')
    ax.set_ylabel('energy (J)')
    ax.set_title(r'$U(h)=mgh$ is a STRAIGHT line: one slope everywhere  →  $F=-mg$ everywhere')
    ax.legend(loc='center right', fontsize=8.5)
    ax.set_xlim(0, 6); ax.set_ylim(0, 130)
    save(fig, 'f_m2_gravity_linear.png')
    print(f'[f_m2] mg={m*g:.1f} N  E={E}  h_max={h_max:.1f} m  slope triangle: 60/3 = {60/3:.1f} N')

def f_m3_gravity_well():
    """U(r) = -GMm/r well: bound vs escape, turning point, inset: mgh."""
    fig, ax = plt.subplots(figsize=(7.4, 4.8))
    r = np.linspace(0.42, 4.0, 600)
    U = -1.0/r                              # units of mgR
    ax.plot(r, U, color=BLUE, lw=2.6, label=r'$U(r)=-\frac{GMm}{r}$   (units of $mgR$)')

    # E = -0.75 : bound
    E1 = -0.75
    rc = -1.0/E1                            # 1.3333
    ax.axhline(E1, color=RED, ls='--', lw=2, label='$E_1=-0.75$ (bound)')
    ax.plot(rc, E1, 'o', color=RED, ms=8, zorder=5)
    ax.annotate(f'turning point\n$r={rc:.2f}R$', xy=(rc, E1), xytext=(1.85, -0.66),
                fontsize=8.5, arrowprops=dict(arrowstyle='->', color=GRAY, lw=0.9))
    # E = 0 : escape
    ax.axhline(0, color=GREEN, ls=':', lw=2, label='$E_2=0$ (escape: no crossing)')

    # surface
    ax.plot(1.0, -1.0, 'o', color=BLACK, ms=7, zorder=5)
    ax.annotate('surface\n$r=R$', xy=(1.0, -1.0), xytext=(1.30, -1.42), fontsize=8.5)

    # inset: near-surface linearization
    axin = ax.inset_axes([0.16, 0.13, 0.45, 0.36])
    hR = np.linspace(0, 0.16, 100)
    axin.plot(hR, -1/(1+hR), color=BLUE, lw=2.2)
    axin.plot(hR, -1 + hR, color=AMBER, ls='--', lw=1.8, label='tangent $-1+h/R$')
    axin.set_title('zoom: $U \\approx -mgR + mgh$\n(the straight tangent = $mgh$)', fontsize=7.6)
    axin.tick_params(labelsize=6.5)
    axin.legend(fontsize=6.5, loc='lower right')

    ax.set_xlabel('distance $r/R$')
    ax.set_ylabel('energy (units of $mgR$)')
    ax.set_title('Gravity well: bound ($E<0$) has a crossing, escape ($E\\geq0$) never does')
    ax.legend(loc='lower right', fontsize=8.5)
    ax.set_ylim(-1.95, 0.18)
    save(fig, 'f_m3_gravity_well.png')
    print(f'[f_m3] E1={E1}  r_cross={rc:.4f}R  inset tangent slope @0 = 1.0 (units 1/R)')

def f_m4_slope_zoom():
    """How to read dY/dX: tangent vs chord on U(x)=x^3-3x."""
    fig, ax = plt.subplots(figsize=(7.4, 4.8))
    x = np.linspace(-2.2, 2.2, 600)
    U = x**3 - 3*x
    ax.plot(x, U, color=BLUE, lw=2.6, label=r'$U(x)=x^3-3x$')

    # tangent at x=1.5
    x0 = 1.5
    U0 = x0**3 - 3*x0                     # -1.125
    slope = 3*x0**2 - 3                   # 3.75
    xt = np.linspace(1.05, 1.95, 20)
    ax.plot(xt, U0 + slope*(xt - x0), color=AMBER, lw=2.2, zorder=4,
            label=f'tangent slope $={slope:.2f}$ → $F={-slope:.2f}$ (instantaneous)')
    ax.plot(x0, U0, 'o', color=BLACK, ms=7, zorder=5)
    # slope triangle on tangent
    dx = 0.25
    ax.plot([x0, x0+dx], [U0, U0], color=GRAY, lw=1.4)
    ax.plot([x0+dx, x0+dx], [U0, U0+slope*dx], color=GRAY, lw=1.4)
    ax.text(x0+0.06, U0+0.5, 'rise', fontsize=8, color=GRAY)
    ax.text(x0+0.18, U0-0.55, 'run', fontsize=8, color=GRAY)

    # chord from 0.5 to 1.5
    xa, xb = 0.5, 1.5
    Ua, Ub = xa**3 - 3*xa, xb**3 - 3*xb    # -1.375, -1.125
    chord = (Ub - Ua)/(xb - xa)            # 0.25
    xc = np.linspace(xa, xb, 10)
    ax.plot(xc, Ua + chord*(xc - xa), color=GREEN, lw=2.0, ls='--', zorder=3,
            label=f'chord slope $={chord:.2f}$ → average $F={-chord:.2f}$')
    ax.plot([xa, xb], [Ua, Ub], 'o', color=GREEN, ms=6, zorder=5)

    # equilibria
    ax.plot(1, -2, 'o', color=RED, ms=9, zorder=5)
    ax.annotate('valley (stable)\nslope = 0', xy=(1, -2), xytext=(1.25, -3.6), fontsize=8.5,
                arrowprops=dict(arrowstyle='->', color=GRAY, lw=0.9))
    ax.plot(-1, 2, 'o', color=RED, ms=9, zorder=5)
    ax.annotate('hill (unstable)\nslope = 0', xy=(-1, 2), xytext=(-2.15, 3.2), fontsize=8.5,
                arrowprops=dict(arrowstyle='->', color=GRAY, lw=0.9))

    ax.set_xlabel('$x$')
    ax.set_ylabel('$U$')
    ax.set_title('Reading a slope: tangent = instantaneous $F$; chord = average $F$ over the interval')
    ax.legend(loc='upper left', fontsize=8.5)
    ax.set_ylim(-4.6, 5.0)
    save(fig, 'f_m4_slope_zoom.png')
    print(f'[f_m4] U0={U0:.3f} slope_tangent={slope:.2f}  chord(0.5→1.5)={chord:.2f}')

def f_m5_stability():
    """Valley vs hill: stable vs unstable equilibrium."""
    fig, axes = plt.subplots(1, 2, figsize=(9.8, 3.9))
    x = np.linspace(-2.4, 2.4, 300)
    for ax, sign, title, ball, ballcolor in (
        (axes[0], +1, 'VALLEY  $U=+x^2$   →   stable', 0.0, GREEN),
        (axes[1], -1, 'HILL  $U=-x^2$   →   unstable', 0.0, RED),
    ):
        U = sign * x**2
        ax.plot(x, U, color=BLUE, lw=2.6)
        ax.plot(ball, sign*ball**2, 'o', color=ballcolor, ms=13, zorder=5)
        ax.annotate('slope = 0\n$F=0$ (equilibrium)', xy=(0, 0), xytext=(0.42, 4.15),
                    fontsize=8.5, arrowprops=dict(arrowstyle='->', color=GRAY, lw=0.9))
        if sign > 0:
            arrow(ax, -1.6, 4.0, -0.75, 4.0, color=GREEN, lw=2.6)
            arrow(ax, 1.6, 4.0, 0.75, 4.0, color=GREEN, lw=2.6)
            ax.text(0, 4.75, 'nudge → pushed BACK (restoring)', fontsize=9.5,
                    color=GREEN, ha='center')
        else:
            arrow(ax, -0.75, 4.0, -1.6, 4.0, color=RED, lw=2.6)
            arrow(ax, 0.75, 4.0, 1.6, 4.0, color=RED, lw=2.6)
            ax.text(0, 4.75, 'nudge → pushed AWAY (runaway)', fontsize=9.5,
                    color=RED, ha='center')
        ax.set_xlabel('$x$')
        ax.set_ylabel('$U$')
        ax.set_title(title, fontsize=10.5)
        ax.set_ylim(-1.2, 6.6)
    save(fig, 'f_m5_stability.png')
    print('[f_m5] stability pair drawn')

if __name__ == '__main__':
    for f in (f_m1_spring_energy, f_m2_gravity_linear, f_m3_gravity_well,
              f_m4_slope_zoom, f_m5_stability):
        f()
    print('all stage-1 graphs saved')
