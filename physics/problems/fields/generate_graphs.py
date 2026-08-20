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

# ═══════════════════════ STAGE 2: 전자기학 ═══════════════════════

def f_e1_uniform_field():
    """Parallel plates: equipotentials (left) + V(x) straight line with slope triangle (right)."""
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
    ax = axes[0]
    d = 0.02
    ax.plot([0, 0], [0.06, 0.94], color=RED, lw=7, solid_capstyle='butt')
    ax.plot([d, d], [0.06, 0.94], color=BLUE, lw=7, solid_capstyle='butt')
    for v in (0.25, 0.5, 0.75):
        ax.plot([0, d], [v, v], '--', color=GRAY, lw=1.1)
        ax.text(-0.0012, v, f'{int(v*200)} V', ha='right', va='center', fontsize=8)
    for yy in (0.12, 0.35, 0.62, 0.85):
        arrow(ax, 0.004, yy, 0.016, yy, color=GREEN, lw=2)
    ax.text(0.0, 1.06, '+ plate\n200 V', ha='center', fontsize=9, color=RED)
    ax.text(d, 1.06, '− plate\n0 V', ha='center', fontsize=9, color=BLUE)
    ax.text(0.01, -0.17, 'equipotential lines: equal V, evenly spaced → E uniform',
            ha='center', fontsize=8.5, color=GRAY)
    ax.set_xlim(-0.008, 0.028); ax.set_ylim(-0.24, 1.22)
    ax.axis('off')

    ax = axes[1]
    x = np.array([0.0, d])
    V = np.array([200.0, 0.0])
    ax.plot(x, V, color=BLUE, lw=2.4)
    x0, x1 = 0.004, 0.014          # points on the line: V=160, V=60
    ax.plot([x0, x0], [60, 160], color=RED, lw=1.6)
    ax.plot([x0, x1], [60, 60], color=RED, lw=1.6)
    ax.text(x0 + 0.0003, 102, r'$\Delta V = -100$ V', fontsize=9, color=RED)
    ax.text(0.008, 50, r'$\Delta d = 0.01$ m', fontsize=9, color=RED)
    ax.text(0.0098, 155, r'$E = -\dfrac{\Delta V}{\Delta d} = 10^4$ V/m', fontsize=11, color=GREEN)
    ax.set_xlim(-0.001, 0.023); ax.set_ylim(-10, 220)
    ax.set_xlabel('distance $x$ (m)'); ax.set_ylabel('potential $V$ (V)')
    ax.set_title('$V(x)$ in a uniform field: one straight slope → one constant $E$')
    save(fig, 'f_e1_uniform_field.png')
    print('[f_e1] E = -(-100 V)/(0.01 m) = 10000 V/m')

def f_e2_point_charge_V():
    """Point charge V(r): tangent slope = E, chord slope = average E; Q>0 and Q<0."""
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.3))
    kQ = 1.8e4                       # Q = 2 μC
    for ax, sign, label, adir in zip(axes, (1, -1), (r'$Q=+2\,\mu$C', r'$Q=-2\,\mu$C'), ('outward', 'inward')):
        r = np.linspace(0.6, 6.0, 400)
        V = sign * kQ / r
        ax.plot(r, V, color=BLUE, lw=2.4, label='$V(r)$')
        r0 = 2.0
        V0 = sign * kQ / r0
        dV = -sign * kQ / r0**2      # -4500 for Q>0
        rt = np.linspace(r0 - 0.8, r0 + 0.8, 12)
        ax.plot(rt, V0 + dV*(rt - r0), color=AMBER, lw=2.2,
                label=f'tangent slope $={dV:.0f}$ V/m  →  $E={-dV:.0f}$ N/C')
        r1, r2v = 2.0, 4.0
        V1, V2 = sign*kQ/r1, sign*kQ/r2v
        chord = (V2 - V1)/(r2v - r1)   # -2250 for Q>0
        rc = np.linspace(r1, r2v, 10)
        ax.plot(rc, V1 + chord*(rc - r1), color=GREEN, lw=2.0, ls='--',
                label=f'chord slope $={chord:.0f}$ V/m  →  average $E={-chord:.0f}$ N/C')
        for rr0 in (1.2, 2.5, 4.0):
            yy = sign * kQ / rr0
            arrow(ax, rr0 - sign*0.28, yy, rr0 + sign*0.28, yy, color=RED, lw=2.4)
        ax.axhline(0, color=GRAY, lw=0.9)
        ax.set_title(f'{label}:   $E = -dV/dr$, points {adir}')
        ax.set_xlabel('distance $r$ (m)'); ax.set_ylabel('potential $V$ (V)')
        ax.legend(loc='upper right', fontsize=7.6)
    save(fig, 'f_e2_point_charge_V.png')
    print('[f_e2] kQ=18000 V.m  tangent@2 = -4500 V/m (E=4500)  chord(2->4) = -2250 V/m (avg E=2250)')

def f_e3_dipole_equipotentials():
    """Dipole equipotential contours + E arrows perpendicular to contours, downhill."""
    x = np.linspace(-3.0, 3.0, 240)
    y = np.linspace(-2.4, 2.4, 200)
    X, Y = np.meshgrid(x, y)
    a = 1.0
    V = 1/np.sqrt((X - a)**2 + Y**2) - 1/np.sqrt((X + a)**2 + Y**2)
    Ey, Ex = np.gradient(V)
    Ex, Ey = -Ex, -Ey
    fig, ax = plt.subplots(figsize=(8.2, 5.8))
    lv = np.linspace(-1.4, 1.4, 29)
    cf = ax.contourf(X, Y, V, levels=lv, cmap='RdBu_r', alpha=0.9)
    ax.contour(X, Y, V, levels=lv, colors='k', linewidths=0.4, alpha=0.5)
    step = 18
    ax.quiver(X[::step, ::step], Y[::step, ::step],
              Ex[::step, ::step], Ey[::step, ::step], color=GREEN,
              scale=60, width=0.004, headwidth=3.4, angles='xy')
    ax.plot(a, 0, 'o', color=RED, ms=12)
    ax.plot(-a, 0, 'o', color=BLUE, ms=12)
    ax.text(a, 0.24, '$+$', color='k', ha='center', fontsize=14, fontweight='bold')
    ax.text(-a, 0.24, '$-$', color='w', ha='center', fontsize=14, fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.set_title('Equipotential lines (contours) + $\\vec{E}$ (arrows ⊥ contours, downhill)')
    ax.set_aspect('equal')
    fig.colorbar(cf, ax=ax, label='potential $V$')
    save(fig, 'f_e3_dipole_equipotentials.png')
    print('[f_e3] dipole map drawn')

def _plates_ax(ax):
    """Draw the shared plate + equipotential background used by f_e4/f_e5."""
    d = 0.02
    ax.plot([0, 0], [0.06, 0.94], color=RED, lw=8, solid_capstyle='butt', zorder=2)
    ax.plot([d, d], [0.06, 0.94], color=BLUE, lw=8, solid_capstyle='butt', zorder=2)
    for v in (0.25, 0.5, 0.75):
        ax.plot([0, d], [v, v], '--', color=GRAY, lw=1.2, zorder=1)
        ax.text(-0.0022, v, f'{int(v*120)} V', ha='right', va='center', fontsize=9, color=GRAY)
    ax.text(-0.0022, 1.05, '+ plate\n120 V', ha='right', va='bottom', fontsize=10, color=RED)
    ax.text(d + 0.0022, 1.05, '0 V\n− plate', ha='left', va='bottom', fontsize=10, color=BLUE)
    for yy in (0.12, 0.88):
        ax.annotate('', xy=(0.017, yy), xytext=(0.003, yy),
                    arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.6, alpha=0.7))
    ax.set_xlim(-0.012, 0.032)
    ax.set_ylim(-0.10, 1.28)
    ax.axis('off')

def f_e4_work_along():
    """Moving a charge ALONG an equipotential line: W = 0."""
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    _plates_ax(ax)
    ax.plot([0.004, 0.016], [0.5, 0.5], color=AMBER, lw=3.2, zorder=4)
    ax.annotate('', xy=(0.016, 0.5), xytext=(0.007, 0.5),
                arrowprops=dict(arrowstyle='->', color=AMBER, lw=2.8))
    ax.plot(0.005, 0.5, 'o', ms=15, color=AMBER, mec='k', mew=1.2, zorder=5)
    ax.text(0.005, 0.5, '+', color='white', ha='center', va='center',
            fontsize=13, fontweight='bold', zorder=6)
    ax.text(0.010, 0.27,
            'along an equipotential:\n' + r'$\Delta V = 0$  →  $W = q\,\Delta V = 0$' + '\n(same height — free ride)',
            fontsize=10, color=AMBER, ha='center', va='top',
            bbox=dict(boxstyle='round,pad=0.35', fc='white', ec=AMBER, alpha=0.92))
    ax.set_title('Moving ALONG an equipotential:  W = 0', fontsize=11.5)
    save(fig, 'f_e4_work_along.png')
    print('[f_e4] along equipotential: W = 0')

def f_e5_work_across():
    """Moving a charge ACROSS equipotential lines: W = qΔV."""
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    _plates_ax(ax)
    x0, y0, x1, y1 = 0.004, 0.82, 0.02, 0.12
    ax.plot([x0, x1], [y0, y1], color=GREEN, lw=3.2, zorder=4)
    ax.annotate('', xy=(0.0158, 0.303), xytext=(0.0075, 0.665),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=2.8))
    ax.plot(x0 + 0.0018, y0 - 0.0788, 'o', ms=15, color=GREEN, mec='k', mew=1.2, zorder=5)
    ax.text(x0 + 0.0018, y0 - 0.0788, '+', color='white', ha='center', va='center',
            fontsize=13, fontweight='bold', zorder=6)
    # crossing dots on the 90 / 60 / 30 V lines
    for vline, lab in ((0.75, '90'), (0.50, '60'), (0.25, '30')):
        xc = x0 + (x1 - x0) * (y0 - vline) / (y0 - y1)
        ax.plot(xc, vline, 'o', ms=7, color='w', mec='k', mew=1.2, zorder=6)
    ax.text(0.014, 1.02,
            'across equipotentials:\n' + r'$\Delta V = -120$ V  →  $W = q\cdot(-120$ V)' + '\n(field does the work — downhill)',
            fontsize=10, color=GREEN, ha='center', va='top',
            bbox=dict(boxstyle='round,pad=0.35', fc='white', ec=GREEN, alpha=0.92))
    ax.set_title('Crossing equipotentials:  W = qΔV', fontsize=11.5)
    save(fig, 'f_e5_work_across.png')
    print('[f_e5] across equipotentials: ΔV = -120 V')

# ═══════════════════════ STAGE 3: 통합1 ═══════════════════════

def f_t1a_force():
    """Outfit (a): force F = qE on a charge between plates."""
    fig, ax = plt.subplots(figsize=(6.2, 4.4))
    d = 0.02
    ax.plot([0, 0], [0.12, 0.88], color=RED, lw=6, solid_capstyle='butt')
    ax.plot([d, d], [0.12, 0.88], color=BLUE, lw=6, solid_capstyle='butt')
    ax.plot(0.01, 0.5, 'o', ms=17, color=AMBER, mec='k', mew=1.2)
    ax.text(0.01, 0.5, '+', color='white', ha='center', va='center',
            fontsize=13, fontweight='bold')
    ax.annotate('', xy=(0.018, 0.5), xytext=(0.012, 0.5),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=3))
    ax.text(0, 1.04, '$+$', ha='center', va='center', fontsize=14, color=RED, fontweight='bold')
    ax.text(d, 1.04, '$-$', ha='center', va='center', fontsize=14, color=BLUE, fontweight='bold')
    ax.text(0.01, 0.70, '$F=qE$', ha='center', fontsize=13)
    ax.set_xlim(-0.005, 0.025); ax.set_ylim(0, 1.18)
    ax.axis('off')
    ax.set_title('(a) Force outfit:  $F=qE$', fontsize=12)
    save(fig, 'f_t1a_force.png')
    print('[f_t1a] force outfit drawn')

def f_t1b_potential():
    """Outfit (b): potential V(x) straight line, slope = -E."""
    fig, ax = plt.subplots(figsize=(6.2, 4.4))
    d = 0.02
    ax.plot([0, d], [200, 0], color=BLUE, lw=2.6)
    ax.plot([0, d], [0, 0], color=GRAY, lw=0.8)
    ax.annotate('', xy=(0.0142, 0), xytext=(0.0142, 200),
                arrowprops=dict(arrowstyle='<->', color=RED, lw=1.6))
    ax.text(0.0154, 100, r'$\Delta V = 200$ V', rotation=90, va='center', fontsize=11, color=RED)
    ax.text(0.0040, 42, r'slope $= -E$  →  $E = \Delta V/d = 10^4$ V/m', fontsize=9.8, color=GREEN)
    ax.set_xlim(-0.001, 0.0225); ax.set_ylim(-15, 235)
    ax.set_xlabel('distance $x$ (m)'); ax.set_ylabel('potential $V$ (V)')
    ax.set_title('(b) Potential outfit:  $V=Ed$', fontsize=12)
    save(fig, 'f_t1b_potential.png')
    print('[f_t1b] potential outfit drawn')

def f_t1c_energy():
    """Outfit (c): energy bars U -> K between the plates."""
    fig, ax = plt.subplots(figsize=(6.2, 4.4))
    U0 = 4.0e-4
    ax.bar([0], [U0], width=0.38, color=BLUE, label='$U$ (Deposit)')
    ax.bar([0], [0], bottom=[U0], width=0.38, color=GREEN, label='$K$ (Cash)')
    ax.bar([1], [0], width=0.38, color=BLUE)
    ax.bar([1], [U0], bottom=[0], width=0.38, color=GREEN)
    ax.set_xticks([0, 1]); ax.set_xticklabels(['start', 'end'], fontsize=10)
    ax.set_ylabel('energy (J)')
    ax.set_ylim(0, 5.2e-4)
    ax.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))
    ax.legend(loc='upper right', fontsize=9)
    ax.set_title('(c) Energy outfit:  $U=qV$', fontsize=12)
    save(fig, 'f_t1c_energy.png')
    print('[f_t1c] energy outfit drawn')

def f_t1d_conservation():
    """Outfit (d): conservation — Balance line constant while K and U swap."""
    fig, ax = plt.subplots(figsize=(6.2, 4.4))
    U0 = 4.0e-4
    ax.bar([0], [U0], width=0.38, color=BLUE)
    ax.bar([0], [0], bottom=[U0], width=0.38, color=GREEN)
    ax.bar([1], [0], width=0.38, color=BLUE)
    ax.bar([1], [U0], bottom=[0], width=0.38, color=GREEN)
    ax.axhline(U0, color=RED, ls='--', lw=2, label='Balance $=K+U$ (constant)')
    ax.set_xticks([0, 1]); ax.set_xticklabels(['start', 'end'], fontsize=10)
    ax.set_ylabel('energy (J)')
    ax.set_ylim(0, 5.2e-4)
    ax.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))
    ax.legend(loc='upper right', fontsize=9)
    ax.set_title(r'(d) Conservation outfit:  $\Delta K = q\Delta V$', fontsize=12)
    save(fig, 'f_t1d_conservation.png')
    print('[f_t1d] conservation outfit drawn')

# ═══════════════════════ STAGE 4: 통합2 ═══════════════════════

def f_t2a_terrain_3d():
    """3D potential terrain with contour lines and gradient arrows on the floor."""
    x = np.linspace(-3.2, 3.2, 150)
    y = np.linspace(-3.2, 3.2, 150)
    X, Y = np.meshgrid(x, y)
    V = (0.16*X**2 + 0.26*Y**2
         + 2.2*np.exp(-((X-1.3)**2 + (Y-1.3)**2)/0.7)
         - 0.9*np.exp(-((X+1.6)**2 + (Y+1.1)**2)/1.1))
    Ey, Ex = np.gradient(V)
    Ex, Ey = -Ex, -Ey
    fig = plt.figure(figsize=(9.6, 7.0))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, V, cmap='terrain', alpha=0.96, linewidth=0, antialiased=True)
    zoff = V.min() - 1.5
    ax.contour(X, Y, V, zdir='z', offset=zoff, levels=9, colors='k', linewidths=0.7)
    step = 15
    Xs, Ys = X[::step, ::step], Y[::step, ::step]
    Exs, Eys = Ex[::step, ::step], Ey[::step, ::step]
    N = np.hypot(Exs, Eys)
    N[N == 0] = 1
    Zs = np.full_like(Xs, zoff)
    ax.quiver(Xs, Ys, Zs, Exs/N, Eys/N, np.zeros_like(Xs), color=RED,
              length=0.35, normalize=True, linewidth=1.1)
    ax.set_zlim(zoff, V.max() + 1.0)
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$'); ax.set_zlabel('potential $V$ ("height")')
    ax.set_title(r'3D: potential as a terrain — $\vec{E}=-\nabla V$: steepest downhill, ⊥ contours',
                 fontsize=11)
    ax.view_init(elev=30, azim=-62)
    save(fig, 'f_t2a_terrain_3d.png')
    print('[f_t2a] 3D terrain drawn')

def f_t2b_charge_map():
    """Single positive charge: concentric equipotentials + radial E arrows (length ∝ E)."""
    x = np.linspace(-3.2, 3.2, 260)
    y = np.linspace(-3.2, 3.2, 260)
    X, Y = np.meshgrid(x, y)
    r = np.hypot(X, Y)
    V = 1.0/r
    fig, ax = plt.subplots(figsize=(6.8, 6.2))
    levels = [0.25, 0.4, 0.6, 0.9, 1.3, 1.8, 2.6, 3.6]
    cf = ax.contourf(X, Y, V, levels=levels, cmap='YlOrRd', alpha=0.95)
    ax.contour(X, Y, V, levels=levels, colors='k', linewidths=0.5, alpha=0.6)
    for rr in np.linspace(0.7, 3.0, 6):
        for a in np.linspace(0, 2*np.pi, 13, endpoint=False):
            cx, cy = rr*np.cos(a), rr*np.sin(a)
            L = 0.06 + 0.25 * (0.49/rr**2)          # arrow length ∝ E = 1/r²
            ax.annotate('', xy=(cx + L*np.cos(a), cy + L*np.sin(a)), xytext=(cx, cy),
                        arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5, alpha=0.85))
    ax.plot(0, 0, 'o', color=RED, ms=13, zorder=6)
    ax.text(0, 0, '+', color='k', ha='center', va='center', fontsize=13, fontweight='bold', zorder=7)
    ax.set_xlim(-3.5, 3.5); ax.set_ylim(-3.5, 3.5)
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.set_title(r'Point charge: $V=kQ/r$ — contours crowd near the charge → E strongest', fontsize=11)
    ax.set_aspect('equal')
    fig.colorbar(cf, ax=ax, label='potential $V$')
    save(fig, 'f_t2b_charge_map.png')
    print('[f_t2b] charge contour map drawn')

# ═══════════════════════ STAGE 5: 필드갤러리 ═══════════════════════

def f_g1a_point_3d():
    """3D surfaces of V=kQ/r: spike for Q>0, funnel for Q<0."""
    fig = plt.figure(figsize=(10.8, 5.0))
    x = np.linspace(-2.6, 2.6, 130)
    y = np.linspace(-2.6, 2.6, 130)
    X, Y = np.meshgrid(x, y)
    r = np.hypot(X, Y)
    for i, sign, lab, cmap in ((1, 1, '$Q>0$: spike  $V=+kQ/r$', 'terrain'),
                               (2, -1, '$Q<0$ (or mass): funnel  $V=-kQ/r$', 'coolwarm')):
        ax = fig.add_subplot(1, 2, i, projection='3d')
        V = np.clip(sign*1.0/r, -2.6, 2.6)
        ax.plot_surface(X, Y, V, cmap=cmap, alpha=0.95, linewidth=0, antialiased=True)
        ax.set_zlim(-2.6, 2.6)
        ax.set_xlabel('$x$'); ax.set_ylabel('$y$'); ax.set_zlabel('$V$')
        ax.set_title(lab, fontsize=11)
        ax.view_init(elev=28, azim=-55)
    save(fig, 'f_g1a_point_3d.png')
    print('[f_g1a] 3D spike/funnel drawn')

def f_g1c_point_fieldlines():
    """Radial field lines of a point source with faint equipotential circles."""
    fig, ax = plt.subplots(figsize=(6.4, 6.0))
    for R in (0.6, 1.2, 1.8, 2.4):
        ax.add_patch(plt.Circle((0, 0), R, fill=False, color=GRAY, lw=1.0, ls='--'))
    for a in np.linspace(0, 2*np.pi, 13, endpoint=False):
        ax.annotate('', xy=(2.75*np.cos(a), 2.75*np.sin(a)), xytext=(0.45*np.cos(a), 0.45*np.sin(a)),
                    arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.7))
    ax.plot(0, 0, 'o', color=RED, ms=12, zorder=5)
    ax.text(0, 0, '+', color='k', ha='center', va='center', fontsize=13, fontweight='bold', zorder=6)
    ax.set_xlim(-3.0, 3.0); ax.set_ylim(-3.0, 3.0)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Field lines: streams from source — ⊥ the equipotential circles', fontsize=11)
    save(fig, 'f_g1c_point_fieldlines.png')
    print('[f_g1c] radial field lines drawn')

def f_g1d_point_cut():
    """1D cut V(r) with tangent (=E) and chord (=average E) — map-to-graph bridge."""
    fig, ax = plt.subplots(figsize=(6.8, 4.3))
    r = np.linspace(0.4, 4.0, 400)
    kQ = 9.0
    V = kQ/r
    ax.plot(r, V, color=BLUE, lw=2.4, label='$V(r)=kQ/r$')
    r0 = 1.5
    V0 = kQ/r0
    dV = -kQ/r0**2                      # -4
    rt = np.linspace(0.8, 2.2, 12)
    ax.plot(rt, V0 + dV*(rt-r0), color=AMBER, lw=2.2,
            label=f'tangent slope $={dV:.0f}$ V/m  →  $E={-dV:.0f}$ N/C')
    r1, r2v = 1.0, 2.0
    V1, V2 = kQ/r1, kQ/r2v
    chord = (V2-V1)/(r2v-r1)             # -4.5
    rc = np.linspace(r1, r2v, 10)
    ax.plot(rc, V1 + chord*(rc-r1), color=GREEN, lw=2.0, ls='--',
            label=f'chord slope $={chord:.1f}$ V/m  →  average $E={-chord:.1f}$ N/C')
    ax.set_xlabel('distance $r$ (m)'); ax.set_ylabel('$V$ (V)')
    ax.set_title('1D cut: slope = E  (map → graph bridge)', fontsize=11.5)
    ax.legend(fontsize=8)
    save(fig, 'f_g1d_point_cut.png')
    print(f'[f_g1d] tangent@1.5={dV:.1f} V/m  chord(1->2)={chord:.1f} V/m')

def f_g2_flux():
    """Why E ∝ 1/r²: the same field lines pierce spheres of radius r, 2r, 3r."""
    fig, ax = plt.subplots(figsize=(6.8, 6.2))
    for R in (1.0, 2.0, 3.0):
        ax.add_patch(plt.Circle((0, 0), R, fill=False, color=GRAY, lw=1.5))
        ax.text(R*0.75, R*0.75, f'{R:.0f}r', fontsize=9.5, color=BLACK)
    for a in np.linspace(0, 2*np.pi, 13, endpoint=False):
        ax.plot([0, 3.05*np.cos(a)], [0, 3.05*np.sin(a)], color=GREEN, lw=1.1, alpha=0.85)
    # highlighted wedge between two lines
    for a in (0.0, np.pi/6):
        ax.plot([0, 3.05*np.cos(a)], [0, 3.05*np.sin(a)], color=RED, lw=2.4)
    for R in (1.0, 2.0, 3.0):
        th = np.linspace(0, np.pi/6, 30)
        ax.plot(R*np.cos(th), R*np.sin(th), color=RED, lw=2.0)
        ax.text(0.55, R*0.16 + 0.14, f'arc ∝ {R:.0f}r', fontsize=8, color=RED)
    ax.plot(0, 0, 'o', color=BLACK, ms=10, zorder=5)
    ax.text(0.32, 0.32,
            'same 2 lines pierce\nevery sphere → line density\n∝ 1/r²  (3D: area 4πr²)',
            fontsize=9.5, color=RED, ha='left', va='bottom',
            bbox=dict(boxstyle='round,pad=0.35', fc='white', ec=RED, alpha=0.9))
    ax.set_xlim(-3.25, 3.25); ax.set_ylim(-3.25, 3.25)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(r'Why $E \propto 1/r^2$: field lines spread over a growing sphere', fontsize=11.5)
    save(fig, 'f_g2_flux.png')
    print('[f_g2] flux picture drawn')

def f_g3_earth_inside():
    """Earth field: g linear inside, 1/r² outside; U parabola inside + funnel outside."""
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
    ax = axes[0]
    r = np.linspace(0, 3, 400)
    g = np.piecewise(r, [r <= 1, r > 1], [lambda x: x, lambda x: 1/x**2])
    ax.plot(r, g, color=BLUE, lw=2.4)
    ax.axvline(1, color=GRAY, ls=':', lw=1.2)
    ax.text(0.35, 0.22, r'inside: $g \propto r$ (linear)', fontsize=9.5, color=GREEN)
    ax.text(1.45, 0.72, r'outside: $g \propto 1/r^2$', fontsize=9.5, color=GREEN)
    ax.set_xlabel('$r/R$'); ax.set_ylabel('$g/g_s$')
    ax.set_title('Field $g(r)$: linear inside, inverse-square outside')
    ax.set_xlim(0, 3); ax.set_ylim(0, 1.9)
    ax = axes[1]
    r = np.linspace(0.02, 3, 400)
    U = np.where(r <= 1, -1.5 + 0.5*r**2, -1.0/r)
    ax.plot(r, U, color=BLUE, lw=2.4)
    ax.axvline(1, color=GRAY, ls=':', lw=1.2)
    ax.plot(0, -1.5, 'o', color=RED, ms=6)
    ax.text(0.05, -1.38, r'center: $U=-1.5\,mgR$', fontsize=8.5, color=RED)
    ax.text(1.15, -1.12, 'surface: $-mgR$', fontsize=8.5, color=GRAY)
    ax.set_xlabel('$r/R$'); ax.set_ylabel('$U/(mgR)$')
    ax.set_title('Potential $U(r)$: parabola inside + funnel outside')
    ax.set_xlim(0, 3); ax.set_ylim(-1.75, 0.1)
    save(fig, 'f_g3_earth_inside.png')
    print('[f_g3] earth inside/outside drawn')

def f_g4_zoom():
    """Near the surface: parallel (uniform). Far away: radial (1/r²). Same field."""
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.6))
    ax = axes[0]
    ax.add_patch(plt.Circle((0, 0), 0.55, color='#d2a679', ec='k', lw=1.2))
    for a in np.linspace(0, 2*np.pi, 12, endpoint=False):
        ax.annotate('', xy=(2.7*np.cos(a), 2.7*np.sin(a)), xytext=(0.95*np.cos(a), 0.95*np.sin(a)),
                    arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.6))
    ax.set_xlim(-3.0, 3.0); ax.set_ylim(-3.0, 3.0)
    ax.set_aspect('equal'); ax.axis('off')
    ax.set_title(r'far view: radial, $g \propto 1/r^2$', fontsize=11.5)
    ax = axes[1]
    ax.add_patch(plt.Rectangle((-1.7, -1.3), 3.4, 2.6, fill=False, ec=GRAY, ls='--', lw=1.4))
    for yy in np.linspace(-1.0, 1.0, 7):
        ax.annotate('', xy=(1.35, yy), xytext=(-1.35, yy),
                    arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.8))
    ax.text(0, -1.55, 'surface', ha='center', fontsize=10)
    ax.set_xlim(-2.2, 2.2); ax.set_ylim(-1.9, 1.9)
    ax.axis('off')
    ax.set_title('near view: parallel (uniform $g$)', fontsize=11.5)
    save(fig, 'f_g4_zoom.png')
    print('[f_g4] zoom transition drawn')

def f_g5_sink_source():
    """Sink (mass / −Q) vs source (+Q): the fluid analogy."""
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.5))
    for ax, dirsign, title, color in ((axes[0], -1, 'SINK  (mass M or $-Q$)\nfield flows INWARD', BLUE),
                                      (axes[1], +1, 'SOURCE  ($+Q$)\nfield flows OUTWARD', RED)):
        for R in (0.6, 1.3, 2.0, 2.6):
            ax.add_patch(plt.Circle((0, 0), R, fill=False, color=GRAY, lw=1.0, ls='--'))
        for a in np.linspace(0, 2*np.pi, 9, endpoint=False):
            r0, r1 = 0.5, 2.75
            if dirsign < 0:
                ax.annotate('', xy=(r0*np.cos(a), r0*np.sin(a)), xytext=(r1*np.cos(a), r1*np.sin(a)),
                            arrowprops=dict(arrowstyle='->', color=color, lw=1.7))
            else:
                ax.annotate('', xy=(r1*np.cos(a), r1*np.sin(a)), xytext=(r0*np.cos(a), r0*np.sin(a)),
                            arrowprops=dict(arrowstyle='->', color=color, lw=1.7))
        ax.set_xlim(-2.9, 2.9); ax.set_ylim(-2.9, 2.9)
        ax.set_aspect('equal'); ax.axis('off')
        ax.set_title(title, fontsize=11)
    save(fig, 'f_g5_sink_source.png')
    print('[f_g5] sink/source drawn')

def f_g6_dipole_lines():
    """Dipole field lines via streamplot: from + (source) to − (sink)."""
    x = np.linspace(-3.0, 3.0, 200)
    y = np.linspace(-2.4, 2.4, 160)
    X, Y = np.meshgrid(x, y)
    a = 1.0
    rp = np.hypot(X - a, Y)
    rm = np.hypot(X + a, Y)
    Ex = (X - a)/rp**3 - (X + a)/rm**3
    Ey = Y/rp**3 - Y/rm**3
    fig, ax = plt.subplots(figsize=(8.6, 6.0))
    ax.streamplot(X, Y, Ex, Ey, color=np.hypot(Ex, Ey), cmap='viridis',
                  density=1.6, linewidth=0.9, arrowsize=0.8)
    ax.plot(a, 0, 'o', color=RED, ms=11, zorder=5)
    ax.plot(-a, 0, 'o', color=BLUE, ms=11, zorder=5)
    ax.text(a, 0.20, '$+$', color='k', ha='center', fontsize=14, fontweight='bold', zorder=6)
    ax.text(-a, 0.20, '$-$', color='w', ha='center', fontsize=14, fontweight='bold', zorder=6)
    ax.set_xlim(-3.0, 3.0); ax.set_ylim(-2.4, 2.4)
    ax.set_aspect('equal')
    ax.set_title('Field lines of a dipole: streams from + (source) to − (sink)', fontsize=11.5)
    save(fig, 'f_g6_dipole_lines.png')
    print('[f_g6] dipole streamlines drawn')

if __name__ == '__main__':
    for f in (f_m1_spring_energy, f_m2_gravity_linear, f_m3_gravity_well,
              f_m4_slope_zoom, f_m5_stability,
              f_e1_uniform_field, f_e2_point_charge_V,
              f_e3_dipole_equipotentials, f_e4_work_along, f_e5_work_across,
              f_t1a_force, f_t1b_potential, f_t1c_energy, f_t1d_conservation,
              f_t2a_terrain_3d, f_t2b_charge_map,
              f_g1a_point_3d, f_g1c_point_fieldlines, f_g1d_point_cut,
              f_g2_flux, f_g3_earth_inside, f_g4_zoom,
              f_g5_sink_source, f_g6_dipole_lines):
        f()
    print('all stage-1..5 graphs saved')
