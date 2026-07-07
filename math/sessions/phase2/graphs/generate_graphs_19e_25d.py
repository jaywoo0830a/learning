"""
Graphs for Sessions 19E and 25D — Vector/Matrix Calculus Bridges.

19E — Linear Systems and Phase Portraits:
  19e1: Harmonic oscillator state space (x, ẋ, t) — 3D helix
  19e2: Center phase portrait — ⬢3D ⬡2D ⬝1D three-panel
  19e3: Phase portrait zoo — 6 types grid
  19e4: Pendulum — ⬢3D energy surface ⬡2D portrait ⬝1D potential

25D — Conservative Fields and Potentials:
  25d1: Vortex field — ⬢3D ⬡2D circulation ⬝1D curl
  25d2: Gravity potential — ⬢3D equipotential ⬡2D gradient ⬝1D U(r)
  25d3: PES reaction path — ⬢3D surface ⬡2D contour ⬝1D energy profile
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Circle, FancyBboxPatch
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib import rcParams

rcParams['font.family'] = 'DejaVu Sans'
rcParams['axes.unicode_minus'] = True

OUT = '/home/rlawjddn/learning/math/sessions/phase2/graphs/'

# ============================================================
# Color palette
# ============================================================
C_BLUE = '#2166AC'
C_RED = '#B2182B'
C_GREEN = '#1B7837'
C_ORANGE = '#E08214'
C_PURPLE = '#762A83'
C_TEAL = '#008080'
C_GRAY = '#666666'
C_GOLD = '#D4A017'


# ================================================================
# 19E-1: Harmonic Oscillator State Space — 3D helix (x, ẋ, t)
# ================================================================
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

t = np.linspace(0, 4*np.pi, 500)
x = np.cos(t)
xdot = -np.sin(t)

# Draw the trajectory as a colored curve
for i in range(len(t)-1):
    ax.plot(x[i:i+2], xdot[i:i+2], t[i:i+2], color=plt.cm.plasma(i/len(t)),
            linewidth=2.5)

# Mark start and end
ax.scatter([1], [0], [0], c='green', s=100, zorder=10, label='Start (t=0)')
ax.scatter([1], [0], [4*np.pi], c='red', s=100, zorder=10, label='End (t=4π)')

# Projections
ax.plot(x, xdot, zs=0, zdir='z', color='gray', alpha=0.3, linewidth=1, linestyle='--')
ax.plot(x, np.zeros_like(x), t, color='gray', alpha=0.3, linewidth=1, linestyle='--')
ax.plot(np.ones_like(xdot)*1.5, xdot, t, color='gray', alpha=0.3, linewidth=1, linestyle='--')

# Shadow ellipse on floor
t_ellipse = np.linspace(0, 2*np.pi, 200)
ax.plot(np.cos(t_ellipse), -np.sin(t_ellipse), zs=0, zdir='z',
        color='blue', alpha=0.4, linewidth=2, label='Phase portrait (x, ẋ)')

ax.set_xlabel('x (position)', fontsize=12)
ax.set_ylabel('ẋ (velocity)', fontsize=12)
ax.set_zlabel('t (time)', fontsize=12)
ax.set_title('Graph 19E-1: Harmonic Oscillator in State Space (x, ẋ, t)',
             fontsize=14, fontweight='bold')
ax.legend(fontsize=10, loc='upper left')
ax.view_init(elev=20, azim=-60)

plt.tight_layout()
plt.savefig(OUT + '19e-harmonic-oscillator-state-space.png', dpi=180, bbox_inches='tight')
plt.close()
print("19E-1 done")


# ================================================================
# 19E-2: Center Phase Portrait — ⬢3D ⬡2D ⬝1D Three-Panel
# ================================================================
fig = plt.figure(figsize=(16, 5))

# --- Panel 1: ⬢ 3D view (x, ẋ, t) ---
ax1 = fig.add_subplot(131, projection='3d')
t = np.linspace(0, 6*np.pi, 600)
x_vals = np.cos(t)
xdot_vals = -np.sin(t)

for i in range(len(t)-1):
    ax1.plot(x_vals[i:i+2], xdot_vals[i:i+2], t[i:i+2],
             color=plt.cm.viridis(i/len(t)), linewidth=1.5)

ax1.plot(x_vals, xdot_vals, zs=0, zdir='z', color='blue', alpha=0.4, linewidth=1.5)
ax1.set_xlabel('x'); ax1.set_ylabel('ẋ'); ax1.set_zlabel('t')
ax1.set_title('3D State Space (x, xdot, t)', fontsize=11, fontweight='bold')
ax1.view_init(elev=18, azim=-55)

# --- Panel 2: ⬡ 2D Phase Portrait ---
ax2 = fig.add_subplot(132)
# Draw several trajectories (different amplitudes)
for amp in [0.5, 0.75, 1.0]:
    theta = np.linspace(0, 2*np.pi, 300)
    ax2.plot(amp*np.cos(theta), -amp*np.sin(theta), color=C_BLUE, linewidth=1.8, alpha=0.7)

# Direction arrows
for ang in [0, np.pi/2, np.pi, 3*np.pi/2]:
    r = 0.8
    xp, yp = r*np.cos(ang), -r*np.sin(ang)
    dx, dy = -0.15*np.sin(ang), -0.15*np.cos(ang)
    ax2.arrow(xp, yp, dx, dy, head_width=0.06, head_length=0.08, fc=C_RED, ec=C_RED, alpha=0.7)

ax2.axhline(0, color='gray', lw=0.5, alpha=0.5)
ax2.axvline(0, color='gray', lw=0.5, alpha=0.5)
ax2.set_xlabel('x'); ax2.set_ylabel('ẋ')
ax2.set_title('2D Phase Portrait (Center)', fontsize=11, fontweight='bold')
ax2.set_xlim(-1.3, 1.3); ax2.set_ylim(-1.3, 1.3)
ax2.set_aspect('equal')
ax2.grid(alpha=0.15)

# --- Panel 3: ⬝ 1D Time Trace ---
ax3 = fig.add_subplot(133)
t_trace = np.linspace(0, 4*np.pi, 500)
ax3.plot(t_trace, np.cos(t_trace), color=C_GREEN, linewidth=2)
ax3.axhline(0, color='gray', lw=0.5, alpha=0.5)
ax3.set_xlabel('t'); ax3.set_ylabel('x(t)')
ax3.set_title('1D Time Trace x(t)=cos(t)', fontsize=11, fontweight='bold')
ax3.grid(alpha=0.15)
ax3.set_xlim(0, 4*np.pi)

fig.suptitle('Graph 19E-2: Three Views of a Harmonic Oscillator (Center)',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '19e-center-phase-portrait.png', dpi=180, bbox_inches='tight')
plt.close()
print("19E-2 done")


# ================================================================
# 19E-3: Phase Portrait Zoo — 3D overview + 6 types grid
# ================================================================
import matplotlib.gridspec as gridspec

fig = plt.figure(figsize=(20, 12))
gs = gridspec.GridSpec(3, 3, figure=fig, height_ratios=[1.1, 1, 1],
                        hspace=0.35, wspace=0.3)

# --- Top: 3D overview spanning full width ---
ax3d = fig.add_subplot(gs[0, :], projection='3d')

t_vals = np.linspace(0, 5, 200)
# Draw 3 representative trajectory types in 3D
# Stable spiral
x_sp = np.exp(-0.3*t_vals) * np.cos(2*t_vals)
y_sp = np.exp(-0.3*t_vals) * np.sin(2*t_vals)
for i in range(len(t_vals)-1):
    ax3d.plot(x_sp[i:i+2], y_sp[i:i+2], t_vals[i:i+2],
              color=plt.cm.Blues(0.4 + 0.5*i/len(t_vals)), linewidth=1.5)
ax3d.plot(x_sp, y_sp, zs=0, zdir='z', color=C_BLUE, alpha=0.25, linewidth=1)

# Unstable spiral
x_us = 0.3 * np.exp(0.25*t_vals) * np.cos(1.5*t_vals)
y_us = 0.3 * np.exp(0.25*t_vals) * np.sin(1.5*t_vals)
for i in range(len(t_vals)-1):
    ax3d.plot(x_us[i:i+2], y_us[i:i+2], t_vals[i:i+2],
              color=plt.cm.Reds(0.4 + 0.5*i/len(t_vals)), linewidth=1.2, alpha=0.7)
ax3d.plot(x_us, y_us, zs=0, zdir='z', color=C_RED, alpha=0.2, linewidth=0.8)

# Saddle direction hints
for s in [-0.8, -0.4, 0.4, 0.8]:
    t_s = np.linspace(0, 3, 100)
    if s > 0:
        x_s = s * np.exp(0.8*t_s)
        y_s = np.zeros_like(t_s)
    else:
        x_s = np.zeros_like(t_s)
        y_s = s * np.exp(-1.5*t_s)
    if abs(s) > 0.1:
        ax3d.plot(x_s, y_s, t_s, color=C_PURPLE, linewidth=1.2, alpha=0.5)

ax3d.set_xlabel('x₁', fontsize=11); ax3d.set_ylabel('x₂', fontsize=11)
ax3d.set_zlabel('t', fontsize=11)
ax3d.set_title('3D View — Trajectories Through Time\n(Blue: stable spiral, Red: unstable spiral, Purple: saddle directions)',
               fontsize=12, fontweight='bold')
ax3d.view_init(elev=20, azim=-55)
ax3d.set_xlim(-1.5, 1.5); ax3d.set_ylim(-1.5, 1.5); ax3d.set_zlim(0, 5.5)

# --- Bottom: 6 phase portraits in 2x3 grid ---
portraits = [
    (np.array([[1, 2], [0, -2]]),  'Saddle\nλ₁>0, λ₂<0',         'saddle'),
    (np.array([[-1, 0], [0, -3]]), 'Stable Node\nλ₁,λ₂<0 (real)', 'stable_node'),
    (np.array([[1, 0], [0, 3]]),   'Unstable Node\nλ₁,λ₂>0',     'unstable_node'),
    (np.array([[-0.2, -2.5], [2.5, -0.2]]), 'Stable Spiral\nλ=α±iβ, α<0', 'spiral_in'),
    (np.array([[0.2, -2.5], [2.5, 0.2]]),   'Unstable Spiral\nλ=α±iβ, α>0', 'spiral_out'),
    (np.array([[0, -2], [2, 0]]),            'Center\nλ=±iβ (purely imag)',  'center'),
]

row_col = [(1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]

for (A, title, ptype), (r, c) in zip(portraits, row_col):
    ax = fig.add_subplot(gs[r, c])

    # --- Draw vector field (thin gray arrows) ---
    xg = np.linspace(-1.4, 1.4, 13)
    yg = np.linspace(-1.4, 1.4, 13)
    X, Y = np.meshgrid(xg, yg)
    U = A[0,0]*X + A[0,1]*Y
    V = A[1,0]*X + A[1,1]*Y
    mag = np.sqrt(U**2 + V**2)
    mag[mag < 0.001] = 1.0
    ax.quiver(X, Y, U/mag, V/mag, angles='xy', scale_units='xy',
              scale=22, color='#AAAAAA', alpha=0.45, width=0.004,
              headwidth=3, headlength=4, headaxislength=3.5)

    # --- Draw trajectories ---
    if ptype == 'saddle':
        # Eigenvectors: (1,0) with λ=1 (unstable, horizontal), (0,1) with λ=-2 (stable, vertical)
        # Unstable manifold (horizontal axis)
        for s in np.linspace(-1.3, 1.3, 13):
            if abs(s) > 0.02:
                t_traj = np.linspace(0, 2.8, 120) if abs(s) < 0.5 else np.linspace(0, 1.2, 120)
                pts_h = np.column_stack([s*np.exp(t_traj), np.zeros_like(t_traj)])
                ax.plot(pts_h[:,0], pts_h[:,1], color=C_RED, linewidth=1.5, alpha=0.65, zorder=3)
                pts_h2 = np.column_stack([s*np.exp(-t_traj), np.zeros_like(t_traj)])
                ax.plot(pts_h2[:,0], pts_h2[:,1], color=C_RED, linewidth=1.5, alpha=0.65, zorder=3,
                        linestyle=(0, (1, 1.5)))
        # Stable manifold (vertical axis)
        for s in np.linspace(-1.3, 1.3, 13):
            if abs(s) > 0.02:
                t_traj = np.linspace(0, 1.5, 120)
                pts_v = np.column_stack([np.zeros_like(t_traj), s*np.exp(-2*t_traj)])
                ax.plot(pts_v[:,0], pts_v[:,1], color=C_BLUE, linewidth=1.5, alpha=0.65, zorder=3)
        # Eigen-directions as thick reference lines
        ax.axhline(0, color=C_RED, lw=1.0, alpha=0.3, zorder=1)
        ax.axvline(0, color=C_BLUE, lw=1.0, alpha=0.3, zorder=1)

    elif ptype == 'stable_node':
        # Trajectories converge to origin, tangent to slow eigendirection (λ=-1, horizontal)
        for ang in np.linspace(0, 2*np.pi, 14, endpoint=False):
            r0 = 1.3
            start = np.array([r0*np.cos(ang), r0*np.sin(ang)])
            t_traj = np.linspace(0, 4.5, 180)
            pts = np.column_stack([start[0]*np.exp(-t_traj), start[1]*np.exp(-3*t_traj)])
            ax.plot(pts[:,0], pts[:,1], color=C_BLUE, linewidth=1.0, alpha=0.55, zorder=3)
        # Slow eigen-direction reference
        ax.axhline(0, color=C_BLUE, lw=1.0, alpha=0.25, zorder=1)

    elif ptype == 'unstable_node':
        # Trajectories diverge from origin, tangent to slow eigendirection (λ=1, horizontal)
        for ang in np.linspace(0, 2*np.pi, 14, endpoint=False):
            r0 = 0.08
            start = np.array([r0*np.cos(ang), r0*np.sin(ang)])
            t_traj = np.linspace(0, 2.5, 180)
            pts = np.column_stack([start[0]*np.exp(t_traj), start[1]*np.exp(3*t_traj)])
            ax.plot(pts[:,0], pts[:,1], color=C_RED, linewidth=1.0, alpha=0.55, zorder=3)
        ax.axhline(0, color=C_RED, lw=1.0, alpha=0.25, zorder=1)

    elif ptype == 'spiral_in':
        for r0 in [0.25, 0.55, 0.85, 1.15]:
            t_traj = np.linspace(0, 6, 300)
            x_tr = r0 * np.exp(-0.2*t_traj) * np.cos(2.5*t_traj)
            y_tr = r0 * np.exp(-0.2*t_traj) * np.sin(2.5*t_traj)
            ax.plot(x_tr, y_tr, color=C_BLUE, linewidth=1.2, alpha=0.6, zorder=3)

    elif ptype == 'spiral_out':
        for r0 in [0.04, 0.09, 0.16, 0.25]:
            t_traj = np.linspace(0, 4.5, 300)
            x_tr = r0 * np.exp(0.2*t_traj) * np.cos(2.5*t_traj)
            y_tr = r0 * np.exp(0.2*t_traj) * np.sin(2.5*t_traj)
            ax.plot(x_tr, y_tr, color=C_RED, linewidth=1.2, alpha=0.6, zorder=3)

    elif ptype == 'center':
        for r0 in [0.25, 0.5, 0.75, 1.0, 1.25]:
            theta_c = np.linspace(0, 2*np.pi, 300)
            ax.plot(r0*np.cos(theta_c), r0*np.sin(theta_c), color=C_BLUE,
                    linewidth=1.2, alpha=0.6, zorder=3)
        # Direction arrows on select orbits
        for r0 in [0.5, 1.0]:
            for ang in [0, np.pi/2, np.pi, 3*np.pi/2]:
                xc, yc = r0*np.cos(ang), r0*np.sin(ang)
                dx, dy = -0.18*np.sin(ang), 0.18*np.cos(ang)
                ax.arrow(xc, yc, dx, dy, head_width=0.06, head_length=0.08,
                        fc=C_RED, ec=C_RED, alpha=0.55, zorder=5)

    # Origin marker
    ax.plot(0, 0, 'o', color='black', markersize=5, zorder=10)

    ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.set_title(title, fontsize=10, fontweight='bold', pad=6)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_facecolor('#FCFCFC')
    for spine in ax.spines.values():
        spine.set_edgecolor('#CCCCCC')
        spine.set_linewidth(0.5)

fig.suptitle('Graph 19E-3: The Phase Portrait Zoo — All 6 Types of 2D Linear Systems',
             fontsize=16, fontweight='bold', y=1.01)
plt.savefig(OUT + '19e-phase-portrait-zoo.png', dpi=200, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.close()
print("19E-3 done")


# ================================================================
# 19E-4: Pendulum — ⬢3D Energy Surface ⬡2D Phase Portrait ⬝1D Potential
# ================================================================
fig = plt.figure(figsize=(16, 5))

g_L = 1.0  # g/L for simplicity

# --- Panel 1: ⬢ 3D Energy Surface E = ½θ̇² − cos(θ) ---
ax1 = fig.add_subplot(131, projection='3d')
theta = np.linspace(-2*np.pi, 2*np.pi, 120)
thetadot = np.linspace(-2.5, 2.5, 80)
Th, Td = np.meshgrid(theta, thetadot)
E = 0.5 * Td**2 - np.cos(Th)

ax1.plot_surface(Th, Td, E, cmap='RdYlBu_r', alpha=0.75, edgecolor='none')
# Mark equilibria
ax1.scatter([0], [0], [-1], c='green', s=80, zorder=10, label='Center (stable)')
ax1.scatter([-np.pi], [0], [1], c='red', s=80, zorder=10, label='Saddle (unstable)')
ax1.scatter([np.pi], [0], [1], c='red', s=80, zorder=10)
ax1.set_xlabel('θ'); ax1.set_ylabel('θ̇'); ax1.set_zlabel('E')
ax1.set_title('3D Energy Surface E(theta, thetadot)', fontsize=11, fontweight='bold')
ax1.legend(fontsize=8, loc='upper left')
ax1.view_init(elev=22, azim=-50)

# --- Panel 2: ⬡ 2D Phase Portrait ---
ax2 = fig.add_subplot(132)
theta_p = np.linspace(-2*np.pi, 2*np.pi, 30)
tdot_p = np.linspace(-2.5, 2.5, 22)
ThP, TdP = np.meshgrid(theta_p, tdot_p)
U_p = TdP
V_p = -g_L * np.sin(ThP)
mag_p = np.sqrt(U_p**2 + V_p**2)
mag_p[mag_p==0] = 1
ax2.quiver(ThP, TdP, U_p/mag_p, V_p/mag_p, angles='xy', scale_units='xy',
           scale=18, color='gray', alpha=0.4, width=0.003)

# Trajectories
for E0 in [-0.8, -0.5, -0.2, 0.5, 1.0, 1.5, 2.0, 2.5]:
    thetas = np.linspace(-2*np.pi, 2*np.pi, 800)
    # Only where E0 + cos(theta) >= 0
    kinetic = 2*(E0 + np.cos(thetas))
    valid = kinetic >= 0
    if np.sum(valid) > 1:
        # Positive branch
        tdot_pos = np.sqrt(np.maximum(kinetic, 0))
        ax2.plot(thetas[valid], tdot_pos[valid], color=C_BLUE, linewidth=0.8, alpha=0.5)
        ax2.plot(thetas[valid], -tdot_pos[valid], color=C_BLUE, linewidth=0.8, alpha=0.5)

# Separatrix (E=1)
thetas_sep = np.linspace(-np.pi, np.pi, 400)
tdot_sep = np.sqrt(2*(1 + np.cos(thetas_sep)))
ax2.plot(thetas_sep, tdot_sep, color=C_RED, linewidth=2.0, alpha=0.9, label='Separatrix (E=1)')
ax2.plot(thetas_sep, -tdot_sep, color=C_RED, linewidth=2.0, alpha=0.9)

# Equilibrium markers
for n in range(-2, 3):
    ax2.plot(2*n*np.pi, 0, 'o', color=C_GREEN, markersize=8, zorder=10)
    ax2.plot((2*n+1)*np.pi, 0, 'x', color=C_RED, markersize=10, mew=3, zorder=10)

ax2.set_xlabel('θ'); ax2.set_ylabel('θ̇')
ax2.set_title('2D Phase Portrait', fontsize=11, fontweight='bold')
ax2.set_xlim(-2*np.pi, 2*np.pi); ax2.set_ylim(-2.8, 2.8)
ax2.legend(fontsize=8, loc='upper right')
ax2.grid(alpha=0.1)

# --- Panel 3: ⬝ 1D Potential U(θ) = −cos(θ) ---
ax3 = fig.add_subplot(133)
theta_1d = np.linspace(-2*np.pi, 2*np.pi, 500)
U_1d = -np.cos(theta_1d)
ax3.plot(theta_1d, U_1d, color=C_PURPLE, linewidth=2.5)
ax3.fill_between(theta_1d, -1.5, U_1d, alpha=0.1, color=C_PURPLE)

# Equilibrium markers
for n in range(-2, 3):
    ax3.plot(2*n*np.pi, -1, 'o', color=C_GREEN, markersize=10, zorder=10)
    ax3.plot((2*n+1)*np.pi, 1, 'x', color=C_RED, markersize=12, mew=3, zorder=10)

# Energy levels
for E0, color, alpha in [(-0.5, C_BLUE, 0.4), (0.5, C_ORANGE, 0.4), (1.5, C_RED, 0.4)]:
    ax3.axhline(E0, color=color, linestyle='--', linewidth=1, alpha=alpha)

ax3.set_xlabel('θ'); ax3.set_ylabel('U(θ)')
ax3.set_title('1D Potential U(theta)=-cos(theta)', fontsize=11, fontweight='bold')
ax3.set_ylim(-1.5, 2.2)
ax3.grid(alpha=0.15)

fig.suptitle('Graph 19E-4: The Pendulum — Center × Saddle × Separatrix',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '19e-pendulum-phase-portrait.png', dpi=180, bbox_inches='tight')
plt.close()
print("19E-4 done")


# ================================================================
# 25D-1: Vortex Field — ⬢3D ⬡2D ⬝1D
# ================================================================
fig = plt.figure(figsize=(16, 5))

# --- Panel 1: ⬢ 3D quiver on the plane ---
ax1 = fig.add_subplot(131)
xg = np.linspace(-2, 2, 14)
yg = np.linspace(-2, 2, 14)
X, Y = np.meshgrid(xg, yg)
r2 = X**2 + Y**2 + 0.01  # avoid division by zero
U = -Y / r2
V = X / r2
mag = np.sqrt(U**2 + V**2)
ax1.quiver(X, Y, U/mag, V/mag, angles='xy', scale_units='xy', scale=18,
           color=C_TEAL, alpha=0.8, width=0.005)

# Circular streamlines
for r0 in [0.4, 0.8, 1.2, 1.6]:
    theta_c = np.linspace(0, 2*np.pi, 200)
    ax1.plot(r0*np.cos(theta_c), r0*np.sin(theta_c), color=C_TEAL,
             linewidth=1.5, alpha=0.5)

# Circulation loop
theta_loop = np.linspace(0, 2*np.pi, 200)
ax1.plot(np.cos(theta_loop), np.sin(theta_loop), color=C_RED,
         linewidth=2.5, alpha=0.8, label='Closed loop C')

# Origin marker
ax1.plot(0, 0, 'o', color=C_RED, markersize=12, zorder=10, label='Vortex core (hole)')

ax1.set_xlim(-2, 2); ax1.set_ylim(-2, 2)
ax1.set_aspect('equal')
ax1.set_xlabel('x'); ax1.set_ylabel('y')
ax1.set_title('3D Vortex Field on R^2 excluding (0,0)', fontsize=11, fontweight='bold')
ax1.legend(fontsize=8, loc='upper right')
ax1.grid(alpha=0.1)

# --- Panel 2: ⬡ 2D Circulation ---
ax2 = fig.add_subplot(132)
# Show vector field and loop more clearly
N = 10
theta_arr = np.linspace(0, 2*np.pi, N, endpoint=False)
for th in theta_arr:
    x0, y0 = np.cos(th), np.sin(th)
    # Tangent at this point (-y, x) but normalized
    dx, dy = -y0, x0
    norm = np.sqrt(dx**2+dy**2)
    ax2.arrow(x0, y0, 0.25*dx/norm, 0.25*dy/norm, head_width=0.08, head_length=0.1,
              fc=C_RED, ec=C_RED, alpha=0.8)

ax2.plot(np.cos(theta_loop), np.sin(theta_loop), color=C_RED, linewidth=2.5)
# Annotation
ax2.annotate(r'$\oint_C \vec{F}\cdot d\vec{r} = 2\pi \neq 0$',
             xy=(0, 0), fontsize=13, ha='center', va='center',
             color=C_RED, fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.9))

ax2.set_xlim(-1.8, 1.8); ax2.set_ylim(-1.8, 1.8)
ax2.set_aspect('equal')
ax2.set_xlabel('x'); ax2.set_ylabel('y')
ax2.set_title('2D Circulation Around the Hole', fontsize=11, fontweight='bold')
ax2.grid(alpha=0.1)

# --- Panel 3: ⬝ 1D Curl Density ---
ax3 = fig.add_subplot(133)
r_vals = np.linspace(0.05, 3, 300)
# The curl is zero for r>0, singular at r=0
curl_vals = np.zeros_like(r_vals)
ax3.plot(r_vals, curl_vals, color=C_GRAY, linewidth=2, label='∇×F = 0 for r>0')

# Delta function spike at origin
ax3.annotate('', xy=(0, 2*np.pi), xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', color=C_RED, lw=3))
ax3.plot(0, 2*np.pi, 'o', color=C_RED, markersize=10)

# Shade the area under the delta
ax3.fill_between([-0.02, 0.02], 0, [2*np.pi, 2*np.pi], alpha=0.3, color=C_RED)

ax3.set_xlim(-0.5, 3); ax3.set_ylim(-1, 8)
ax3.set_xlabel('r (distance from origin)'); ax3.set_ylabel('(∇×F)_z')
ax3.set_title('1D Curl Density = 2pi delta(r)', fontsize=11, fontweight='bold')
ax3.legend(fontsize=9, loc='upper right')
ax3.grid(alpha=0.1)

fig.suptitle('Graph 25D-1: The Vortex Field — Curl-Free but NOT Conservative',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '25d-vortex-field.png', dpi=180, bbox_inches='tight')
plt.close()
print("25D-1 done")


# ================================================================
# 25D-2: Gravity Potential — ⬢3D ⬡2D ⬝1D
# ================================================================
fig = plt.figure(figsize=(16, 5))

GMm = 1.0  # normalized

# --- Panel 1: ⬢ 3D Equipotential Spheres ---
ax1 = fig.add_subplot(131, projection='3d')

# Draw nested equipotential spheres (semi-transparent)
radii = [0.5, 0.75, 1.0, 1.3, 1.7]
colors_sphere = ['#8B0000', '#B22222', '#CD5C5C', '#DC143C', '#FF6347']
for r, c in zip(radii, colors_sphere):
    u = np.linspace(0, 2*np.pi, 40)
    v = np.linspace(0, np.pi, 25)
    x_s = r * np.outer(np.cos(u), np.sin(v))
    y_s = r * np.outer(np.sin(u), np.sin(v))
    z_s = r * np.outer(np.ones(np.size(u)), np.cos(v))
    ax1.plot_surface(x_s, y_s, z_s, color=c, alpha=0.12, edgecolor=c, linewidth=0.3)

# Gradient arrows (pointing inward — toward the mass at origin)
for th in np.linspace(0, 2*np.pi, 8, endpoint=False):
    for phi in [np.pi/4, np.pi/2, 3*np.pi/4]:
        r0 = 1.5
        x0 = r0 * np.sin(phi) * np.cos(th)
        y0 = r0 * np.sin(phi) * np.sin(th)
        z0 = r0 * np.cos(phi)
        # Gradient direction: -r̂ (inward)
        dr = -0.3 * x0 / r0
        dy = -0.3 * y0 / r0
        dz = -0.3 * z0 / r0
        ax1.quiver(x0, y0, z0, dr, dy, dz, color=C_RED, alpha=0.6,
                   linewidth=1.5, arrow_length_ratio=0.2)

# Mass at origin
ax1.scatter([0], [0], [0], c='black', s=150, zorder=10, label='Mass M')

ax1.set_xlabel('x'); ax1.set_ylabel('y'); ax1.set_zlabel('z')
ax1.set_title('3D Equipotential Spheres\nU(r) = -GMm/r', fontsize=11, fontweight='bold')
ax1.set_xlim(-1.8, 1.8); ax1.set_ylim(-1.8, 1.8); ax1.set_zlim(-1.8, 1.8)
ax1.legend(fontsize=8)

# --- Panel 2: ⬡ 2D Slice with gradient vectors ---
ax2 = fig.add_subplot(132)
# Contour lines (equipotential circles)
theta_c = np.linspace(0, 2*np.pi, 300)
for r in np.linspace(0.3, 1.8, 8):
    U_val = -GMm / r
    ax2.plot(r*np.cos(theta_c), r*np.sin(theta_c), color=C_BLUE,
             linewidth=1.2, alpha=0.7)

# Gradient arrows perpendicular to contours (pointing inward)
for th in np.linspace(0, 2*np.pi, 12, endpoint=False):
    r0 = 1.3
    x0 = r0 * np.cos(th)
    y0 = r0 * np.sin(th)
    # Gradient of -1/r is r̂/r², pointing outward. Force = -∇U = -r̂/r², pointing INWARD
    dx_in = -0.22 * np.cos(th)
    dy_in = -0.22 * np.sin(th)
    ax2.arrow(x0, y0, dx_in, dy_in, head_width=0.07, head_length=0.09,
              fc=C_RED, ec=C_RED, alpha=0.7)

ax2.plot(0, 0, 'ko', markersize=12)
ax2.set_xlim(-2, 2); ax2.set_ylim(-2, 2)
ax2.set_aspect('equal')
ax2.set_xlabel('x'); ax2.set_ylabel('y')
ax2.set_title('2D Slice — Gradient Perpendicular\nto Equipotential Circles', fontsize=11, fontweight='bold')
ax2.grid(alpha=0.1)

# --- Panel 3: ⬝ 1D U(r) = −GMm/r ---
ax3 = fig.add_subplot(133)
r_plot = np.linspace(0.3, 3, 400)
U_plot = -GMm / r_plot
ax3.plot(r_plot, U_plot, color=C_PURPLE, linewidth=2.5)

# Show -dU/dr = F (the slope gets gentler with distance)
r_tan = 1.0
U_tan = -GMm / r_tan
dU_dr = GMm / r_tan**2  # positive derivative
# Tangent line
r_tan_line = np.linspace(0.5, 1.8, 100)
U_tan_line = U_tan + dU_dr * (r_tan_line - r_tan)
ax3.plot(r_tan_line, U_tan_line, '--', color=C_RED, linewidth=1.5, alpha=0.7,
         label=f'Slope at r={r_tan}: F = −dU/dr = −{dU_dr:.2f}')

ax3.axhline(0, color='gray', lw=0.5, alpha=0.5)
ax3.set_xlabel('r (distance)'); ax3.set_ylabel('U(r)')
ax3.set_title('1D Potential U(r)=-GMm/r', fontsize=11, fontweight='bold')
ax3.set_ylim(-4, 1)
ax3.legend(fontsize=8, loc='lower right')
ax3.grid(alpha=0.15)

fig.suptitle('Graph 25D-2: Gravitational Potential — Force = −∇U',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '25d-gravity-potential.png', dpi=180, bbox_inches='tight')
plt.close()
print("25D-2 done")


# ================================================================
# 25D-3: PES Reaction Path — ⬢3D surface ⬡2D contour ⬝1D profile
# ================================================================
fig = plt.figure(figsize=(16, 5))

# Construct a model PES for A+BC→AB+C (collinear)
# LEPS-like surface: two valleys connected by a saddle
def model_pes(r1, r2):
    """r1 = A-B distance, r2 = B-C distance. Morse-like with coupling."""
    # Reactant valley: A + BC (r1 large, r2 ~ 1.0)
    # Product valley: AB + C (r1 ~ 1.0, r2 large)
    # Saddle at roughly r1=r2=1.2
    V_AB = 3.0 * (1 - np.exp(-1.5*(r1 - 1.0)))**2 - 0.5
    V_BC = 3.0 * (1 - np.exp(-1.5*(r2 - 1.0)))**2 - 0.5
    # Coupling term that creates the barrier
    coupling = 1.5 * np.exp(-1.5*(r1 - 1.2)**2 - 1.5*(r2 - 1.2)**2)
    return V_AB + V_BC + coupling

# --- Panel 1: ⬢ 3D PES ---
ax1 = fig.add_subplot(131, projection='3d')
r1 = np.linspace(0.7, 2.5, 70)
r2 = np.linspace(0.7, 2.5, 70)
R1, R2 = np.meshgrid(r1, r2)
V = model_pes(R1, R2)

ax1.plot_surface(R1, R2, V, cmap='terrain', alpha=0.8, edgecolor='none')

# Mark the reaction path points
# A simple path: from reactant (r1=2.2, r2=1.0) through saddle (~1.2,1.2) to product (r1=1.0, r2=2.2)
path_r1 = np.linspace(2.2, 1.0, 50)
path_r2 = np.linspace(1.0, 2.2, 50)
path_V = model_pes(path_r1, path_r2)
ax1.plot(path_r1, path_r2, path_V, color=C_RED, linewidth=3, zorder=10, label='Reaction path (IRC)')

# Mark saddle
ax1.scatter([1.2], [1.2], [model_pes(1.2, 1.2)], c=C_RED, s=100, zorder=10,
           marker='*', label='Transition State (‡)')
# Mark reactant and product
ax1.scatter([2.2], [1.0], [model_pes(2.2, 1.0)], c=C_GREEN, s=80, zorder=10, label='Reactants')
ax1.scatter([1.0], [2.2], [model_pes(1.0, 2.2)], c=C_BLUE, s=80, zorder=10, label='Products')

ax1.set_xlabel('r₁ (A−B)'); ax1.set_ylabel('r₂ (B−C)'); ax1.set_zlabel('Energy')
ax1.set_title('3D Potential Energy Surface\nA + BC -> AB + C', fontsize=11, fontweight='bold')
ax1.legend(fontsize=7, loc='upper left')
ax1.view_init(elev=25, azim=-55)

# --- Panel 2: ⬡ 2D Contour Map ---
ax2 = fig.add_subplot(132)
contour_levels = np.linspace(-1.5, 4, 25)
cs = ax2.contour(R1, R2, V, levels=contour_levels, cmap='terrain', linewidths=0.8)
ax2.clabel(cs, inline=True, fontsize=7, fmt='%.1f')

# Reaction path
ax2.plot(path_r1, path_r2, '--', color=C_RED, linewidth=2.5, label='IRC path')
ax2.plot(1.2, 1.2, '*', color=C_RED, markersize=15, zorder=10, label='TS (‡)')
ax2.plot(2.2, 1.0, 'o', color=C_GREEN, markersize=10, zorder=10, label='Reactants')
ax2.plot(1.0, 2.2, 'o', color=C_BLUE, markersize=10, zorder=10, label='Products')

# Gradient arrows (forces) along path
for i in range(0, 50, 8):
    r1p, r2p = path_r1[i], path_r2[i]
    # Gradient direction is steepest descent
    dr1, dr2 = path_r1[i+1]-r1p, path_r2[i+1]-r2p
    norm = np.sqrt(dr1**2+dr2**2)
    if norm > 0:
        ax2.arrow(r1p, r2p, 0.08*dr1/norm, 0.08*dr2/norm,
                 head_width=0.03, head_length=0.04, fc=C_RED, ec=C_RED, alpha=0.6)

ax2.set_xlabel('r₁ (A−B distance)'); ax2.set_ylabel('r₂ (B−C distance)')
ax2.set_title('2D Contour Map\n(Force = -grad U follows IRC)', fontsize=11, fontweight='bold')
ax2.legend(fontsize=7, loc='upper right')
ax2.set_aspect('equal')

# --- Panel 3: ⬝ 1D Energy Profile Along Reaction Coordinate ---
ax3 = fig.add_subplot(133)
s = np.linspace(0, 1, 50)  # normalized reaction coordinate
r1_s = 2.2 + (1.0 - 2.2)*s
r2_s = 1.0 + (2.2 - 1.0)*s
V_s = model_pes(r1_s, r2_s)

ax3.plot(s, V_s, color=C_PURPLE, linewidth=2.5)
# Barrier
s_saddle = (1.2 - 2.2) / (1.0 - 2.2)  # where r1=1.2
V_saddle = model_pes(1.2, 1.2)
V_reactants = model_pes(2.2, 1.0)
V_products = model_pes(1.0, 2.2)

# Barrier annotation
ax3.annotate('', xy=(s_saddle, V_saddle), xytext=(s_saddle, V_reactants),
            arrowprops=dict(arrowstyle='<->', color=C_RED, lw=2))
ax3.text(s_saddle+0.02, (V_saddle+V_reactants)/2, r'$E_a$ (activation energy)',
         fontsize=10, color=C_RED, va='center')

# ΔE annotation
ax3.annotate('', xy=(0.95, V_products), xytext=(0.95, V_reactants),
            arrowprops=dict(arrowstyle='<->', color=C_GREEN, lw=1.5))
ax3.text(0.96, (V_products+V_reactants)/2, r'$\Delta E$', fontsize=10, color=C_GREEN, va='center')

ax3.plot(s_saddle, V_saddle, '*', color=C_RED, markersize=15, zorder=10)
ax3.plot(0, V_reactants, 'o', color=C_GREEN, markersize=10)
ax3.plot(1, V_products, 'o', color=C_BLUE, markersize=10)

ax3.set_xlabel('Reaction coordinate s')
ax3.set_ylabel('Energy')
ax3.set_title('1D Energy Profile\nk = A exp(-Ea/RT)', fontsize=11, fontweight='bold')
ax3.grid(alpha=0.15)

fig.suptitle('Graph 25D-3: Potential Energy Surface — Reaction Follows −∇U',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '25d-pes-reaction-path.png', dpi=180, bbox_inches='tight')
plt.close()
print("25D-3 done")


print("\n=== All 19E & 25D graphs generated successfully! ===")
