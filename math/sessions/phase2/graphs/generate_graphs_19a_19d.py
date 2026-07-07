"""
Graphs for Sessions 19A, 19B, 19C, 19D — ODE Modeling & Solutions.
Rich 3D→2D→1D visualizations for each major concept.

19A:
  19a-slope-field-family — 3D surface z=f(x,y), 2D slope field+curves, 1D solutions
  19a-growth-decay — 3D (t,y,k), 2D growth/decay, 1D doubling/half-life

19B:
  19b-integrating-factor — 3D surface mu*y, 2D slope field, 1D solution

19C:
  19c-exact-ode-potential — 3D phi(x,y), 2D level curves+vector field, 1D cross-section

19D:
  19d-damping-types — 3D state space, 2D phase portraits (3 types), 1D y(t) traces
  19d-euler-method — 3D comparison, 2D zoom, 1D error
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Circle, Rectangle
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rcParams
import matplotlib.gridspec as gridspec

rcParams['font.family'] = 'DejaVu Sans'
rcParams['axes.unicode_minus'] = True

OUT = '/home/rlawjddn/learning/math/sessions/phase2/graphs/'

C_BLUE = '#2166AC'
C_RED = '#B2182B'
C_GREEN = '#1B7837'
C_ORANGE = '#E08214'
C_PURPLE = '#762A83'
C_TEAL = '#008080'
C_GRAY = '#666666'

# ================================================================
# 19A-1: Slope Field Family — 3D Surface → 2D Field → 1D Solutions
# ================================================================
fig = plt.figure(figsize=(16, 5))
gs = gridspec.GridSpec(1, 3, figure=fig, wspace=0.35)

# Panel 1: 3D — The surface z = f(x,y) = x+y
ax1 = fig.add_subplot(gs[0, 0], projection='3d')
xg = np.linspace(-2.5, 2.5, 50)
yg = np.linspace(-2.5, 2.5, 50)
Xg, Yg = np.meshgrid(xg, yg)
Zg = Xg + Yg
ax1.plot_surface(Xg, Yg, Zg, cmap='coolwarm', alpha=0.6, edgecolor='none')
# Mark that dy/dx = x+y = height of this surface
ax1.set_xlabel('x'); ax1.set_ylabel('y'); ax1.set_zlabel("y' = x+y")
ax1.set_title('3D: Slope Field = Surface\nz = x+y', fontsize=10, fontweight='bold')
ax1.view_init(elev=25, azim=-45)

# Panel 2: 2D — Slope field with solution curves
ax2 = fig.add_subplot(gs[0, 1])
xv = np.linspace(-2.5, 2.5, 14)
yv = np.linspace(-2.5, 2.5, 14)
Xv, Yv = np.meshgrid(xv, yv)
U = np.ones_like(Xv)
V = Xv + Yv
mag = np.sqrt(1 + V**2)
ax2.quiver(Xv, Yv, U/mag, V/mag, angles='xy', scale_units='xy', scale=18,
           color='gray', alpha=0.5, width=0.004)
# Solution curves: y = Ce^x - x - 1
for C in [-2, -1, 0, 1, 2]:
    xc = np.linspace(-2.5, 2.5, 300)
    yc = C * np.exp(xc) - xc - 1
    mask = (yc > -3) & (yc < 3)
    ax2.plot(xc[mask], yc[mask], color=C_BLUE, linewidth=1.5, alpha=0.8)
ax2.set_xlim(-2.5, 2.5); ax2.set_ylim(-2.5, 2.5)
ax2.set_xlabel('x'); ax2.set_ylabel('y')
ax2.set_title('2D: Slope Field + Solutions\ny = Ceˣ − x − 1', fontsize=10, fontweight='bold')
ax2.set_aspect('equal')
ax2.grid(alpha=0.1)

# Panel 3: 1D — Individual solutions y(x)
ax3 = fig.add_subplot(gs[0, 2])
xc = np.linspace(-2.5, 2.5, 300)
for i, C in enumerate([-2, -1, 0, 1, 2]):
    yc = C * np.exp(xc) - xc - 1
    mask = (yc > -4) & (yc < 4)
    ax3.plot(xc[mask], yc[mask], color=plt.cm.viridis(i/5), linewidth=1.8,
             label=f'C={C}')
# y=-x-1 asymptote (C=0)
ax3.plot(xc, -xc-1, '--', color='gray', linewidth=1, alpha=0.6, label='y=-x-1 (C=0)')
ax3.set_xlim(-2.5, 2.5); ax3.set_ylim(-4, 4)
ax3.set_xlabel('x'); ax3.set_ylabel('y')
ax3.set_title('1D: Solution Family', fontsize=10, fontweight='bold')
ax3.legend(fontsize=7, loc='upper left')
ax3.grid(alpha=0.1)

fig.suptitle('Graph 19A-1: dy/dx = x+y — Three Views of a First-Order ODE',
             fontsize=13, fontweight='bold', y=1.02)
plt.savefig(OUT + '19a-slope-field-family.png', dpi=200, bbox_inches='tight',
            facecolor='white')
plt.close()
print("19A-1 done")


# ================================================================
# 19A-2: Growth & Decay — 3D (t, y, k) → 2D families → 1D doubling/half-life
# ================================================================
fig = plt.figure(figsize=(16, 5))
gs = gridspec.GridSpec(1, 3, figure=fig, wspace=0.35)

# Panel 1: 3D — y = Ce^{kt} as a surface over (t, k)
ax1 = fig.add_subplot(gs[0, 0], projection='3d')
t_vals = np.linspace(0, 4, 60)
k_vals = np.linspace(-0.8, 0.8, 50)
T, K = np.meshgrid(t_vals, k_vals)
Y = np.exp(K * T)  # C=1
ax1.plot_surface(T, K, Y, cmap='RdYlBu_r', alpha=0.7, edgecolor='none')
# Mark k=0 plane (y=1 constant)
ax1.plot(t_vals, np.zeros_like(t_vals), np.ones_like(t_vals),
         color='gray', linewidth=2, alpha=0.7, label='k=0 (constant)')
ax1.set_xlabel('t'); ax1.set_ylabel('k'); ax1.set_zlabel('y')
ax1.set_title('3D: y = e^{kt} over (t, k)\nGrowth (k>0) / Decay (k<0)', fontsize=10, fontweight='bold')
ax1.view_init(elev=22, azim=-50)
ax1.legend(fontsize=7)

# Panel 2: 2D — Growth (k>0) and Decay (k<0) families
ax2 = fig.add_subplot(gs[0, 1])
t_fine = np.linspace(0, 4, 300)
# Growth family
for C, alpha in [(0.5, 0.4), (0.75, 0.55), (1.0, 0.7), (1.5, 0.85), (2.0, 1.0)]:
    ax2.plot(t_fine, C * np.exp(0.5*t_fine), color=C_RED, linewidth=1.5, alpha=alpha)
# Decay family
for C, alpha in [(0.5, 0.4), (0.75, 0.55), (1.0, 0.7), (1.5, 0.85), (2.0, 1.0)]:
    ax2.plot(t_fine, C * np.exp(-0.5*t_fine), color=C_BLUE, linewidth=1.5, alpha=alpha)
ax2.axhline(1.0, color='gray', linestyle=':', linewidth=1, alpha=0.5)
ax2.set_xlabel('t'); ax2.set_ylabel('y')
ax2.set_title('2D: Growth (red, k=0.5)\nvs Decay (blue, k=−0.5)', fontsize=10, fontweight='bold')
ax2.set_ylim(0, 4.5)
ax2.grid(alpha=0.1)

# Panel 3: 1D — Doubling time & Half-life on log scale
ax3 = fig.add_subplot(gs[0, 2])
t_fine = np.linspace(0, 6, 400)
y_grow = np.exp(0.5 * t_fine)
y_decay = np.exp(-0.5 * t_fine)
ax3.semilogy(t_fine, y_grow, color=C_RED, linewidth=2, label='Growth: y=e^{0.5t}')
ax3.semilogy(t_fine, y_decay, color=C_BLUE, linewidth=2, label='Decay: y=e^{-0.5t}')

# Doubling time: y=1→2 at t=ln2/0.5≈1.386
t2 = np.log(2)/0.5
ax3.axvline(t2, color=C_RED, linestyle='--', alpha=0.5)
ax3.annotate('', xy=(t2, 2), xytext=(0, 2),
            arrowprops=dict(arrowstyle='<->', color=C_RED, lw=1.5))
ax3.text(t2/2, 2.2, r'$t_2=\frac{\ln 2}{k}=1.39$', fontsize=9,
         color=C_RED, ha='center')

# Half-life: y=1→0.5 at t=ln2/0.5≈1.386
th = np.log(2)/0.5
ax3.axhline(0.5, color=C_BLUE, linestyle=':', alpha=0.3)
ax3.annotate('', xy=(th, 0.5), xytext=(0, 0.5),
            arrowprops=dict(arrowstyle='<->', color=C_BLUE, lw=1.5))
ax3.text(th/2, 0.35, r'$t_{1/2}=\frac{\ln 2}{|k|}=1.39$', fontsize=9,
         color=C_BLUE, ha='center')

ax3.set_xlabel('t'); ax3.set_ylabel('y (log scale)')
ax3.set_title('1D: Log Scale — Doubling Time\n& Half-Life are the Same Length', fontsize=10, fontweight='bold')
ax3.legend(fontsize=8)
ax3.grid(alpha=0.1, which='both')

fig.suptitle('Graph 19A-2: y\' = ky — Exponential Growth and Decay',
             fontsize=13, fontweight='bold', y=1.02)
plt.savefig(OUT + '19a-growth-decay.png', dpi=200, bbox_inches='tight',
            facecolor='white')
plt.close()
print("19A-2 done")


# ================================================================
# 19B: Integrating Factor Visual — 3D μy surface → 2D field → 1D exact product rule
# ================================================================
fig = plt.figure(figsize=(16, 5))
gs = gridspec.GridSpec(1, 3, figure=fig, wspace=0.35)

# Panel 1: 3D — The surface z = mu*y for y'+2xy=x, mu=e^{x^2}
ax1 = fig.add_subplot(gs[0, 0], projection='3d')
x_vals = np.linspace(-1.5, 1.5, 60)
c_vals = np.linspace(-2, 3, 30)
Xm, Cm = np.meshgrid(x_vals, c_vals)
mu_vals = np.exp(Xm**2)
y_vals = 0.5 + Cm * np.exp(-Xm**2)
Z_vals = mu_vals * y_vals
ax1.plot_surface(Xm, Cm, Z_vals, cmap='viridis', alpha=0.7, edgecolor='none')
ax1.set_xlabel('x'); ax1.set_ylabel('C'); ax1.set_zlabel(r'$\mu y$')
ax1.set_title('3D: The Magic of μ\n(μy)\' = μQ becomes exact', fontsize=10, fontweight='bold')
ax1.view_init(elev=22, azim=-40)

# Panel 2: 2D — Slope field with μ
ax2 = fig.add_subplot(gs[0, 1])
xv = np.linspace(-2, 2, 14)
yv = np.linspace(-1, 4, 14)
Xv, Yv = np.meshgrid(xv, yv)
U = np.ones_like(Xv)
V = Xv - 2*Xv*Yv  # y' = x - 2xy
mag = np.sqrt(1 + V**2)
ax2.quiver(Xv, Yv, U/mag, V/mag, angles='xy', scale_units='xy', scale=18,
           color='gray', alpha=0.5, width=0.004)
# Solution curves
for C in [-1, -0.5, 0, 0.5, 1, 1.5, 2]:
    xc = np.linspace(-2, 2, 300)
    yc = 0.5 + C * np.exp(-xc**2)
    ax2.plot(xc, yc, color=C_BLUE, linewidth=1.5, alpha=0.7)
# Highlight particular solution C=0 (equilibrium)
ax2.plot(x_vals, 0.5*np.ones_like(x_vals), color=C_RED, linewidth=2.5,
         label='y=0.5 (equilibrium, C=0)')
ax2.set_xlim(-2, 2); ax2.set_ylim(-1, 4)
ax2.set_xlabel('x'); ax2.set_ylabel('y')
ax2.set_title("2D: y' + 2xy = x\nSolutions y=0.5+Ce^{-x²}", fontsize=10, fontweight='bold')
ax2.legend(fontsize=8)
ax2.grid(alpha=0.1)

# Panel 3: 1D — The product rule in action
ax3 = fig.add_subplot(gs[0, 2])
x_fine = np.linspace(-1.5, 1.5, 300)
mu_f = np.exp(x_fine**2)
# Show mu*y for C=1
y_f = 0.5 + 1.0 * np.exp(-x_fine**2)
muy = mu_f * y_f
# Show its derivative
dmuy = np.gradient(muy, x_fine)
ax3.plot(x_fine, muy, color=C_PURPLE, linewidth=2, label=r'$\mu y = e^{x^2}(0.5+e^{-x^2})$')
ax3.plot(x_fine, dmuy, color=C_ORANGE, linewidth=2, label=r"$(\mu y)' = \mu Q = x e^{x^2}$")
# Check: mu*Q = e^{x^2} * x
muQ = x_fine * np.exp(x_fine**2)
ax3.plot(x_fine, muQ, '--', color=C_RED, linewidth=1.5, alpha=0.7,
         label=r'$\mu Q = x e^{x^2}$ (should match)')
ax3.set_xlabel('x')
ax3.set_title('1D: (μy)\' = μQ — the Product Rule\nDerivative (orange) = μQ (red dashed)', fontsize=10, fontweight='bold')
ax3.legend(fontsize=7, loc='upper left')
ax3.grid(alpha=0.1)

fig.suptitle('Graph 19B: Integrating Factor — Making a Non-Exact ODE Exact',
             fontsize=13, fontweight='bold', y=1.02)
plt.savefig(OUT + '19b-integrating-factor.png', dpi=200, bbox_inches='tight',
            facecolor='white')
plt.close()
print("19B done")


# ================================================================
# 19C: Exact ODE = Level Curves of Potential — 3D φ → 2D field+contours → 1D slice
# ================================================================
fig = plt.figure(figsize=(16, 5))
gs = gridspec.GridSpec(1, 3, figure=fig, wspace=0.35)

# Example: (2x+y)dx + (x+2y)dy = 0, φ = x²+xy+y²

# Panel 1: 3D — The potential surface φ(x,y) = x² + xy + y²
ax1 = fig.add_subplot(gs[0, 0], projection='3d')
xg = np.linspace(-2, 2, 60)
yg = np.linspace(-2, 2, 60)
Xg, Yg = np.meshgrid(xg, yg)
Phig = Xg**2 + Xg*Yg + Yg**2
ax1.plot_surface(Xg, Yg, Phig, cmap='terrain', alpha=0.7, edgecolor='none')
# Mark some level curves on the surface
for c in [1, 2, 4, 7]:
    theta = np.linspace(0, 2*np.pi, 200)
    # Solve x²+xy+y² = c → ellipse
    a = np.sqrt(2*c/3)
    b = np.sqrt(2*c)
    xe = a*np.cos(theta) - b/np.sqrt(2)*np.sin(theta)
    ye = a*np.cos(theta) + b/np.sqrt(2)*np.sin(theta)
    ze = c * np.ones_like(theta)
    ax1.plot(xe, ye, ze, color=C_RED, linewidth=1.5, alpha=0.7)
ax1.set_xlabel('x'); ax1.set_ylabel('y'); ax1.set_zlabel(r'$\phi$')
ax1.set_title('3D: Potential Surface\nφ = x² + xy + y²', fontsize=10, fontweight='bold')
ax1.view_init(elev=28, azim=-50)

# Panel 2: 2D — Vector field ⟨2x+y, x+2y⟩ overlaid on level curves
ax2 = fig.add_subplot(gs[0, 1])
xv = np.linspace(-2, 2, 13)
yv = np.linspace(-2, 2, 13)
Xv, Yv = np.meshgrid(xv, yv)
U = 2*Xv + Yv
V = Xv + 2*Yv
mag = np.sqrt(U**2 + V**2)
mag[mag==0] = 1
ax2.quiver(Xv, Yv, U/mag, V/mag, angles='xy', scale_units='xy', scale=15,
           color=C_TEAL, alpha=0.6, width=0.005)
# Level curves (solutions)
for c in [0.5, 1, 2, 4, 7, 12]:
    theta = np.linspace(0, 2*np.pi, 300)
    a = np.sqrt(2*c/3); b = np.sqrt(2*c)
    xe = a*np.cos(theta) - b/np.sqrt(2)*np.sin(theta)
    ye = a*np.cos(theta) + b/np.sqrt(2)*np.sin(theta)
    ax2.plot(xe, ye, color=C_RED, linewidth=1.5, alpha=0.7)
ax2.set_xlim(-2, 2); ax2.set_ylim(-2, 2)
ax2.set_aspect('equal')
ax2.set_xlabel('x'); ax2.set_ylabel('y')
ax2.set_title('2D: ∇φ = ⟨2x+y, x+2y⟩ perp Level Curves\nSolutions φ(x,y) = C', fontsize=10, fontweight='bold')
ax2.grid(alpha=0.1)

# Panel 3: 1D — Slice through y = x
ax3 = fig.add_subplot(gs[0, 2])
s = np.linspace(-2, 2, 300)
phi_slice = s**2 + s*s + s**2  # 3s²
ax3.plot(s, phi_slice, color=C_PURPLE, linewidth=2.5, label=r'$\phi(s,s) = 3s^2$')
# Mark levels
for c in [1, 4, 9]:
    sc = np.sqrt(c/3)
    ax3.plot([-sc], [c], 'o', color=C_RED, markersize=8)
    ax3.plot([sc], [c], 'o', color=C_RED, markersize=8)
    ax3.axhline(c, color=C_RED, linestyle=':', linewidth=0.8, alpha=0.3)
ax3.set_xlabel('s (along y=x)'); ax3.set_ylabel(r'$\phi$')
ax3.set_title('1D: Slice Along y = x\nφ = 3s² (minimum at origin)', fontsize=10, fontweight='bold')
ax3.legend(fontsize=8)
ax3.grid(alpha=0.1)

fig.suptitle('Graph 19C: Exact ODE — Solutions Are Level Curves of a Potential',
             fontsize=13, fontweight='bold', y=1.02)
plt.savefig(OUT + '19c-exact-ode-potential.png', dpi=200, bbox_inches='tight',
            facecolor='white')
plt.close()
print("19C done")


# ================================================================
# 19D-1: Damping Types — 3D state space → 2D phase portraits → 1D y(t)
# ================================================================
fig = plt.figure(figsize=(18, 12))
gs = gridspec.GridSpec(3, 3, figure=fig, hspace=0.4, wspace=0.35,
                        height_ratios=[1.2, 1, 1])

# Top row: 3D state space overview
ax3d = fig.add_subplot(gs[0, :], projection='3d')
t_vals = np.linspace(0, 6, 300)

# Overdamped
y_od = np.exp(-0.5*t_vals) + 0.3*np.exp(-2*t_vals)
yd_od = -0.5*np.exp(-0.5*t_vals) - 0.6*np.exp(-2*t_vals)
for i in range(len(t_vals)-1):
    ax3d.plot(y_od[i:i+2], yd_od[i:i+2], t_vals[i:i+2],
              color=plt.cm.Reds(0.4+0.5*i/len(t_vals)), linewidth=1.5)
ax3d.plot(y_od, yd_od, zs=0, zdir='z', color=C_RED, alpha=0.25, linewidth=1)

# Underdamped
y_ud = np.exp(-0.3*t_vals) * np.cos(2*t_vals)
yd_ud = -0.3*np.exp(-0.3*t_vals)*np.cos(2*t_vals) - 2*np.exp(-0.3*t_vals)*np.sin(2*t_vals)
for i in range(len(t_vals)-1):
    ax3d.plot(y_ud[i:i+2], yd_ud[i:i+2], t_vals[i:i+2],
              color=plt.cm.Blues(0.4+0.5*i/len(t_vals)), linewidth=1.2)
ax3d.plot(y_ud, yd_ud, zs=0, zdir='z', color=C_BLUE, alpha=0.25, linewidth=1)

# Critically damped
y_cd = (1 + 0.8*t_vals) * np.exp(-t_vals)
yd_cd = (0.8 - 1 - 0.8*t_vals) * np.exp(-t_vals)
for i in range(len(t_vals)-1):
    ax3d.plot(y_cd[i:i+2], yd_cd[i:i+2], t_vals[i:i+2],
              color=plt.cm.Greens(0.4+0.5*i/len(t_vals)), linewidth=1.2)
ax3d.plot(y_cd, yd_cd, zs=0, zdir='z', color=C_GREEN, alpha=0.25, linewidth=1)

ax3d.set_xlabel('y'); ax3d.set_ylabel("y'"); ax3d.set_zlabel('t')
ax3d.set_title('3D: State Space Trajectories (y, y\', t)\nRed=Overdamped, Blue=Underdamped, Green=Critically Damped',
               fontsize=11, fontweight='bold')
ax3d.view_init(elev=18, azim=-55)

# Row 2: 2D Phase portraits
damping_types = [
    ('Overdamped\nReal distinct roots', C_RED,
     lambda t: np.exp(-0.5*t), lambda t: -0.5*np.exp(-0.5*t),
     lambda t: np.exp(-2*t), lambda t: -2*np.exp(-2*t)),
    ('Critically Damped\nRepeated root', C_GREEN,
     lambda t: np.exp(-t), lambda t: -np.exp(-t),
     None, None),
    ('Underdamped\nComplex roots', C_BLUE,
     None, None, None, None),
]

for idx, (title, color, f1, df1, f2, df2) in enumerate(damping_types):
    ax = fig.add_subplot(gs[1, idx])

    if idx == 0:  # Overdamped
        for s1 in np.linspace(-2, 2, 7):
            for s2 in np.linspace(-2, 2, 5):
                if abs(s1) > 0.05 or abs(s2) > 0.05:
                    t_traj = np.linspace(0, 5, 200)
                    y_tr = s1*np.exp(-0.5*t_traj) + s2*np.exp(-2*t_traj)
                    yd_tr = -0.5*s1*np.exp(-0.5*t_traj) - 2*s2*np.exp(-2*t_traj)
                    ax.plot(y_tr, yd_tr, color=color, linewidth=0.8, alpha=0.4)
        # Slow eigen-direction
        ax.axhline(0, color=color, lw=1.5, alpha=0.5)

    elif idx == 1:  # Critically damped
        for c1 in np.linspace(-2, 2, 7):
            for c2 in np.linspace(-2, 0, 4):
                if abs(c1) > 0.05 or abs(c2) > 0.05:
                    t_traj = np.linspace(0, 5, 200)
                    y_tr = (c1 + c2*t_traj) * np.exp(-t_traj)
                    yd_tr = (c2 - c1 - c2*t_traj) * np.exp(-t_traj)
                    ax.plot(y_tr, yd_tr, color=color, linewidth=0.8, alpha=0.4)
        ax.axhline(0, color=color, lw=1.5, alpha=0.5)

    elif idx == 2:  # Underdamped
        for r0 in [0.3, 0.7, 1.1, 1.5]:
            t_traj = np.linspace(0, 8, 400)
            x_tr = r0 * np.exp(-0.3*t_traj) * np.cos(2*t_traj)
            y_tr = -0.3*r0*np.exp(-0.3*t_traj)*np.cos(2*t_traj) - 2*r0*np.exp(-0.3*t_traj)*np.sin(2*t_traj)
            ax.plot(x_tr, y_tr, color=color, linewidth=1.2, alpha=0.6)

    ax.plot(0, 0, 'ko', markersize=4)
    ax.set_xlim(-2.2, 2.2); ax.set_ylim(-2.2, 2.2)
    ax.set_aspect('equal')
    ax.set_title(title, fontsize=9, fontweight='bold')
    ax.set_xticks([]); ax.set_yticks([])

# Row 3: 1D Time traces
for idx, (title, color, f1, df1, f2, df2) in enumerate(damping_types):
    ax = fig.add_subplot(gs[2, idx])
    t_fine = np.linspace(0, 8, 400)

    if idx == 0:  # Overdamped
        ax.plot(t_fine, np.exp(-0.5*t_fine), color=color, linewidth=2, label='Mode 1 (slow)')
        ax.plot(t_fine, np.exp(-2*t_fine), '--', color=color, linewidth=1.5, alpha=0.6, label='Mode 2 (fast)')
        ax.plot(t_fine, np.exp(-0.5*t_fine)+0.5*np.exp(-2*t_fine), '-', color='gray', linewidth=2.5, label='Sum')
        ax.legend(fontsize=7)
    elif idx == 1:
        t_f = np.linspace(0, 6, 400)
        ax.plot(t_f, np.exp(-t_f), color=color, linewidth=2, label=r'$e^{-t}$')
        ax.plot(t_f, 2*t_f*np.exp(-t_f), '--', color=color, linewidth=1.5, alpha=0.6, label=r'$2t e^{-t}$')
        ax.plot(t_f, (1+1.5*t_f)*np.exp(-t_f), '-', color='gray', linewidth=2.5, label='Sum')
        ax.legend(fontsize=7)
    else:
        ax.plot(t_fine, np.exp(-0.3*t_fine)*np.cos(2*t_fine), color=color, linewidth=2, label='y(t)')
        ax.plot(t_fine, np.exp(-0.3*t_fine), '--', color='gray', linewidth=1, alpha=0.5, label='Envelope')
        ax.plot(t_fine, -np.exp(-0.3*t_fine), '--', color='gray', linewidth=1, alpha=0.5)
        ax.legend(fontsize=7)

    ax.set_xlim(0, 8); ax.set_ylim(-2.2, 2.5)
    ax.set_xlabel('t')
    ax.grid(alpha=0.1)

# Col titles for rows
ax_r2_label = fig.add_subplot(gs[1, 1])
ax_r2_label.axis('off')
ax_r2_label.text(0.5, 1.05, '2D: Phase Portraits (y vs y\')', fontsize=11, fontweight='bold',
                 ha='center', transform=ax_r2_label.transAxes)

fig.suptitle('Graph 19D-1: Damped Harmonic Oscillator — Three Regimes',
             fontsize=14, fontweight='bold', y=1.01)
plt.savefig(OUT + '19d-damping-types.png', dpi=200, bbox_inches='tight',
            facecolor='white')
plt.close()
print("19D-1 done")


# ================================================================
# 19D-2: Euler Method — 3D comparison → 2D zoom → 1D error
# ================================================================
fig = plt.figure(figsize=(16, 5))
gs = gridspec.GridSpec(1, 3, figure=fig, wspace=0.35)

# y' = x + y, y(0) = 1, exact = -x-1+2e^x
def exact(x): return -x - 1 + 2*np.exp(x)

# Euler steps with h=0.3
h = 0.3
n_steps = 6
x_euler = [0.0]
y_euler = [1.0]
for i in range(n_steps):
    x_curr = x_euler[-1]
    y_curr = y_euler[-1]
    slope = x_curr + y_curr
    x_euler.append(x_curr + h)
    y_euler.append(y_curr + h * slope)
x_euler = np.array(x_euler)
y_euler = np.array(y_euler)

# Panel 1: 3D — Euler stairs vs exact surface
ax1 = fig.add_subplot(gs[0, 0], projection='3d')
x_fine = np.linspace(0, 1.8, 100)
y_exact = exact(x_fine)

# Plot exact solution as a curve in 3D
ax1.plot(x_fine, y_exact, np.zeros_like(x_fine), color=C_BLUE, linewidth=2.5,
         label='Exact solution')

# Plot Euler steps as vertical + horizontal line segments
for i in range(len(x_euler)-1):
    # Vertical segment (dt step)
    ax1.plot([x_euler[i], x_euler[i]], [y_euler[i], y_euler[i]],
             [0, h], color=C_RED, linewidth=2, alpha=0.7)
    # Horizontal jump
    ax1.plot([x_euler[i], x_euler[i+1]], [y_euler[i], y_euler[i+1]],
             [h, h], color=C_RED, linewidth=2, alpha=0.7)

# Floor projection of exact
ax1.plot(x_fine, y_exact, zs=0, zdir='z', color=C_BLUE, alpha=0.3, linewidth=1)

ax1.set_xlabel('x'); ax1.set_ylabel('y'); ax1.set_zlabel('step')
ax1.set_title('3D: Euler Staircase vs Exact\n(Each step = slope × h)', fontsize=10, fontweight='bold')
ax1.legend(fontsize=8)
ax1.view_init(elev=20, azim=-55)

# Panel 2: 2D — Euler vs Exact zoom
ax2 = fig.add_subplot(gs[0, 1])
# Slope field
xv = np.linspace(0, 1.8, 10)
yv = np.linspace(0.5, 4, 10)
Xv, Yv = np.meshgrid(xv, yv)
U = np.ones_like(Xv)
V = Xv + Yv
mag = np.sqrt(1 + V**2)
ax2.quiver(Xv, Yv, U/mag, V/mag, angles='xy', scale_units='xy', scale=15,
           color='gray', alpha=0.4, width=0.004)

ax2.plot(x_fine, y_exact, color=C_BLUE, linewidth=2.5, label='Exact: y=-x-1+2eˣ')
ax2.plot(x_euler, y_euler, 'o-', color=C_RED, linewidth=2, markersize=6,
         label=f'Euler (h={h})')
# Show slope segments
for i in range(len(x_euler)-1):
    ax2.plot([x_euler[i], x_euler[i+1]], [y_euler[i], y_euler[i]],
             color=C_RED, linewidth=1, alpha=0.3)

ax2.set_xlim(0, 1.9); ax2.set_ylim(0.5, 4.5)
ax2.set_xlabel('x'); ax2.set_ylabel('y')
ax2.set_title("2D: Euler vs Exact\ny' = x + y, y(0)=1", fontsize=10, fontweight='bold')
ax2.legend(fontsize=8)
ax2.grid(alpha=0.1)

# Panel 3: 1D — Error |y_euler - y_exact|
ax3 = fig.add_subplot(gs[0, 2])
exact_at_nodes = exact(x_euler)
errors = np.abs(y_euler - exact_at_nodes)
ax3.fill_between(x_euler, 0, errors, alpha=0.3, color=C_RED)
ax3.plot(x_euler, errors, 'o-', color=C_RED, linewidth=2, markersize=6)
for i, err in enumerate(errors):
    if i > 0:
        ax3.text(x_euler[i], err+0.02, f'{err:.3f}', fontsize=8, ha='center', color=C_RED)

# Theoretical: local error ~ O(h²), global ~ O(h)
# Fit line showing O(h) growth
ax3.plot(x_euler, 0.3*x_euler, '--', color='gray', linewidth=1, alpha=0.5,
         label=r'$\propto h$ (global error)')
ax3.set_xlabel('x'); ax3.set_ylabel('|Error|')
ax3.set_title('1D: Error Accumulation\nGlobal error ∝ h', fontsize=10, fontweight='bold')
ax3.legend(fontsize=8)
ax3.grid(alpha=0.1)

fig.suptitle('Graph 19D-2: Euler Method — Numerical Integration of ODEs',
             fontsize=13, fontweight='bold', y=1.02)
plt.savefig(OUT + '19d-euler-method.png', dpi=200, bbox_inches='tight',
            facecolor='white')
plt.close()
print("19D-2 done")


print("\n=== All 19A-D graphs generated successfully! ===")
