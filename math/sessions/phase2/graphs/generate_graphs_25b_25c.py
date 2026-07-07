"""
Graphs for 25B (Jacobian matrix) and 25C (Stokes → Faraday) enhancements.

25b-jacobian-matrix — 3D mapping (u,v)→(x,y), 2D parallelogram, 1D area scaling
25c-stokes-faraday — 3D surface+flux, 2D circulation loop, 1D EMF vs time
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Circle, Polygon, FancyBboxPatch
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib import rcParams
import matplotlib.gridspec as gridspec

rcParams['font.family'] = 'DejaVu Sans'
rcParams['axes.unicode_minus'] = True

OUT = '/home/rlawjddn/learning/math/sessions/phase2/graphs/'

C_BLUE  = '#2166AC'
C_RED   = '#B2182B'
C_GREEN = '#1B7837'
C_ORANGE= '#E08214'
C_PURPLE= '#762A83'
C_TEAL  = '#008080'
C_GRAY  = '#666666'
C_GOLD  = '#D4A017'


# ================================================================
# 25B: Jacobian Matrix — det(J) as the local area scaling factor
# ================================================================
fig = plt.figure(figsize=(16, 5))
gs = gridspec.GridSpec(1, 3, figure=fig, wspace=0.35)

# Mapping: (u,v) -> (x,y) = (u+v, u-v)  => J = [[1,1],[1,-1]], det(J) = -2, |det|=2

# Panel 1: 3D — mapping grid from (u,v) to (x,y) space
ax1 = fig.add_subplot(gs[0, 0], projection='3d')

# Draw (u,v) grid in the u-v plane (z=0)
u_vals = np.linspace(-1.5, 1.5, 7)
v_vals = np.linspace(-1.5, 1.5, 7)
for u in u_vals:
    v_line = np.linspace(-1.5, 1.5, 30)
    ax1.plot(np.full_like(v_line, u), v_line, np.zeros_like(v_line),
             color=C_GRAY, linewidth=0.6, alpha=0.5)
for v in v_vals:
    u_line = np.linspace(-1.5, 1.5, 30)
    ax1.plot(u_line, np.full_like(u_line, v), np.zeros_like(u_line),
             color=C_GRAY, linewidth=0.6, alpha=0.5)

# Draw (x,y) grid in transformed space (z=1.5)
x_vals = np.linspace(-3, 3, 7)
y_vals = np.linspace(-3, 3, 7)
for u in u_vals:
    v_line = np.linspace(-1.5, 1.5, 40)
    x_line = u + v_line
    y_line = u - v_line
    ax1.plot(x_line, y_line, 1.5*np.ones_like(v_line),
             color=C_BLUE, linewidth=0.8, alpha=0.6)
for v in v_vals:
    u_line = np.linspace(-1.5, 1.5, 40)
    x_line = u_line + v
    y_line = u_line - v
    ax1.plot(x_line, y_line, 1.5*np.ones_like(u_line),
             color=C_BLUE, linewidth=0.8, alpha=0.6)

# Highlight a small square in (u,v) and its image
u0, v0 = 0.5, 0.3
du, dv = 0.4, 0.3
# Unit square in (u,v)
sq_u = [u0, u0+du, u0+du, u0, u0]
sq_v = [v0, v0, v0+dv, v0+dv, v0]
ax1.plot(sq_u, sq_v, np.zeros(5), color=C_RED, linewidth=2.5, zorder=10)
sq_poly = Poly3DCollection([list(zip(sq_u[:-1], sq_v[:-1], [0]*4))], alpha=0.15, color=C_RED, zorder=9)
ax1.add_collection3d(sq_poly)

# Image parallelogram in (x,y)
sq_x = [u0+v0, u0+du+v0, u0+du+v0+dv, u0+v0+dv, u0+v0]
sq_y = [u0-v0, u0+du-v0, u0+du-v0-dv, u0-v0-dv, u0-v0]
ax1.plot(sq_x, sq_y, 1.5*np.ones(5), color=C_RED, linewidth=2.5, zorder=10)
sq_img = Poly3DCollection([list(zip(sq_x[:-1], sq_y[:-1], [1.5]*4))], alpha=0.15, color=C_RED, zorder=9)
ax1.add_collection3d(sq_img)

# Arrows showing mapping
for i in range(4):
    ax1.plot([sq_u[i], sq_x[i]], [sq_v[i], sq_y[i]], [0, 1.5],
             '--', color=C_RED, linewidth=0.8, alpha=0.4)

ax1.set_xlabel('u / x'); ax1.set_ylabel('v / y'); ax1.set_zlabel('')
ax1.set_title('3D: (u,v) Grid Maps to (x,y) Grid\nArea scales by |det J| = 2', fontsize=10, fontweight='bold')
ax1.view_init(elev=22, azim=-50)
ax1.set_zticks([0, 1.5])
ax1.set_zticklabels(['(u,v) plane', '(x,y) plane'])

# Panel 2: 2D — The unit square and its image as a parallelogram
ax2 = fig.add_subplot(gs[0, 1])

# Draw the matrix columns as vectors
J11, J12 = 1, 1   # column 1
J21, J22 = 1, -1  # column 2

# Draw column vectors of J
ax2.arrow(0, 0, J11, J21, head_width=0.1, head_length=0.12, fc=C_BLUE, ec=C_BLUE,
          linewidth=2.5, label=r'$J_{*,1} = (x_u, y_u)$')
ax2.arrow(0, 0, J12, J22, head_width=0.1, head_length=0.12, fc=C_TEAL, ec=C_TEAL,
          linewidth=2.5, label=r'$J_{*,2} = (x_v, y_v)$')

# The unit square image = parallelogram spanned by columns
paral_x = [0, J11, J11+J12, J12, 0]
paral_y = [0, J21, J21+J22, J22, 0]
ax2.fill(paral_x, paral_y, alpha=0.15, color=C_RED)
ax2.plot(paral_x, paral_y, color=C_RED, linewidth=2, label='Image of unit square')
ax2.text(J11/2, J21/2-0.15, r'$J_{*,1}$', fontsize=11, color=C_BLUE, ha='center')
ax2.text(J12+0.1, J22/2, r'$J_{*,2}$', fontsize=11, color=C_TEAL, va='center')

# Area annotation
ax2.text(0.5, 0.8, r'Area = |det J| = $|1\cdot(-1) - 1\cdot 1| = 2$',
         fontsize=11, color=C_RED, ha='center', fontweight='bold',
         transform=ax2.transAxes,
         bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.9))

ax2.set_xlim(-0.5, 2.5); ax2.set_ylim(-1.8, 1.8)
ax2.set_aspect('equal')
ax2.set_xlabel('x'); ax2.set_ylabel('y')
ax2.set_title('2D: J = [x_u x_v; y_u y_v] — Columns\nSpan a Parallelogram of Area |det J|', fontsize=10, fontweight='bold')
ax2.legend(fontsize=8, loc='lower right')
ax2.grid(alpha=0.1)

# Panel 3: 1D — det(J) along a polar ray
ax3 = fig.add_subplot(gs[0, 2])
r_vals = np.linspace(0.1, 3, 200)
detJ_vals = r_vals  # det(J) = r for polar
ax3.plot(r_vals, detJ_vals, color=C_PURPLE, linewidth=2.5, label=r'Polar: $\det J = r$')

# Mark the 2D example: |det J| = 2
ax3.axhline(2, color=C_RED, linestyle='--', linewidth=1.5, alpha=0.6,
            label='Example: |det(J)| = 2 (constant)')
ax3.annotate('Mapping (u,v)->(x,y)\n|det J| = 2 everywhere', xy=(2, 2),
             xytext=(2.1, 2.5), fontsize=9, color=C_RED,
             arrowprops=dict(arrowstyle='->', color=C_RED))

# Also show spherical Jacobian scaled
rho = np.linspace(0.1, 3, 200)
detJ_sph = rho**2 / 3  # scaled for comparison
ax3.plot(rho, detJ_sph, '--', color=C_GREEN, linewidth=1.5, alpha=0.6,
         label=r'Spherical: $\det J = \rho^2\sin\phi$ (at $\phi=\pi/3$)')

ax3.set_xlabel('r (distance from origin)'); ax3.set_ylabel('det(J) = area scale factor')
ax3.set_title('1D: det(J) as a Function of Position\nNon-constant for Curvilinear Coordinates', fontsize=10, fontweight='bold')
ax3.legend(fontsize=8)
ax3.grid(alpha=0.1)

fig.suptitle('Graph 25B-2: The Jacobian Matrix — det(J) as Local Area Scaling',
             fontsize=13, fontweight='bold', y=1.02)
plt.savefig(OUT + '25b-jacobian-matrix.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.close()
print("25B done")


# ================================================================
# 25C: Stokes → Faraday — Circulation = Rate of Change of Flux
# ================================================================
fig = plt.figure(figsize=(16, 5))
gs = gridspec.GridSpec(1, 3, figure=fig, wspace=0.35)

# Panel 1: 3D — Surface S with B-field and boundary C, E-field circulation
ax1 = fig.add_subplot(gs[0, 0], projection='3d')

# Draw a disk surface (the surface S)
phi_d = np.linspace(0, 2*np.pi, 50)
r_d = np.linspace(0, 1, 10)
R_d, Phi_d = np.meshgrid(r_d, phi_d)
X_d = R_d * np.cos(Phi_d)
Y_d = R_d * np.sin(Phi_d)
Z_d = np.zeros_like(X_d)
ax1.plot_surface(X_d, Y_d, Z_d, color=C_TEAL, alpha=0.3, edgecolor='none')

# Boundary curve C (unit circle)
theta_c = np.linspace(0, 2*np.pi, 100)
x_c = np.cos(theta_c)
y_c = np.sin(theta_c)
z_c = np.zeros_like(theta_c)
ax1.plot(x_c, y_c, z_c, color=C_RED, linewidth=3, label='Boundary C')

# B-field arrows through surface (uniform, upward)
bg_x = np.linspace(-0.8, 0.8, 5)
bg_y = np.linspace(-0.8, 0.8, 5)
Bg_x, Bg_y = np.meshgrid(bg_x, bg_y)
for i in range(len(bg_x)):
    for j in range(len(bg_y)):
        if bg_x[i]**2 + bg_y[j]**2 <= 0.85**2:
            ax1.quiver(bg_x[i], bg_y[j], 0, 0, 0, 0.5,
                       color=C_BLUE, alpha=0.6, linewidth=1.5, arrow_length_ratio=0.15)

# E-field arrows along boundary (tangent, CCW)
for th in np.linspace(0, 2*np.pi, 12, endpoint=False):
    xp, yp = np.cos(th), np.sin(th)
    dx, dy = -0.3*np.sin(th), 0.3*np.cos(th)
    ax1.quiver(xp, yp, 0, dx, dy, 0, color=C_RED, alpha=0.8,
               linewidth=2, arrow_length_ratio=0.15)

ax1.set_xlabel('x'); ax1.set_ylabel('y'); ax1.set_zlabel('z')
ax1.set_title("3D: Stokes' Theorem\nE-circulation (red) = B-flux change (blue)", fontsize=10, fontweight='bold')
ax1.legend(fontsize=8)
ax1.view_init(elev=30, azim=-45)

# Panel 2: 2D — Top-down view with circulation and flux
ax2 = fig.add_subplot(gs[0, 1])

# Disk region
disk = Circle((0, 0), 1, facecolor=C_TEAL, alpha=0.15, edgecolor=C_TEAL, linewidth=1.5)
ax2.add_patch(disk)

# B-field in background (uniform, upward = out of page = dots)
for bx in np.linspace(-0.8, 0.8, 6):
    for by in np.linspace(-0.8, 0.8, 6):
        if bx**2 + by**2 <= 0.9**2:
            ax2.plot(bx, by, 'o', color=C_BLUE, markersize=6, alpha=0.5)

# E-field around boundary
for th in np.linspace(0, 2*np.pi, 14, endpoint=False):
    xp, yp = np.cos(th), np.sin(th)
    dx, dy = -0.2*np.sin(th), 0.2*np.cos(th)
    ax2.arrow(xp, yp, dx, dy, head_width=0.07, head_length=0.09,
              fc=C_RED, ec=C_RED, alpha=0.8)

# Boundary
theta_b = np.linspace(0, 2*np.pi, 200)
ax2.plot(np.cos(theta_b), np.sin(theta_b), color=C_RED, linewidth=2.5)

# Annotations
ax2.annotate(r'$\oint_C \vec{E}\cdot d\vec{r}$', xy=(1.1, 0.2), fontsize=12,
             color=C_RED, fontweight='bold', ha='left')
ax2.annotate(r'$=-\frac{d}{dt}\iint_S \vec{B}\cdot d\vec{S}$', xy=(0, -0.2),
             fontsize=12, color=C_BLUE, fontweight='bold', ha='center',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.85))

ax2.set_xlim(-1.8, 1.8); ax2.set_ylim(-1.8, 1.8)
ax2.set_aspect('equal')
ax2.set_xlabel('x'); ax2.set_ylabel('y')
ax2.set_title("2D: Top View — Faraday's Law\nEMF = Circulation = -d(Flux)/dt", fontsize=10, fontweight='bold')
ax2.grid(alpha=0.1)

# Panel 3: 1D — EMF oscillates as flux changes
ax3 = fig.add_subplot(gs[0, 2])
t_vals = np.linspace(0, 4*np.pi, 400)
# Simulate B(t) = B0 cos(wt), Flux ~ cos(wt), EMF = -d(Flux)/dt ~ sin(wt)
flux = np.cos(t_vals)
emf = np.sin(t_vals)  # -d/dt(cos) = sin

ax3.plot(t_vals, flux, color=C_BLUE, linewidth=2, label=r'$\Phi_B(t) = \iint \vec{B}\cdot d\vec{S}$')
ax3.plot(t_vals, emf, color=C_RED, linewidth=2, label=r'$\mathcal{E} = -\frac{d\Phi_B}{dt}$')

# Mark zero crossings
for t0 in [0, np.pi, 2*np.pi, 3*np.pi, 4*np.pi]:
    ax3.axvline(t0, color='gray', linestyle=':', linewidth=0.6, alpha=0.4)

# Mark where EMF is maximum (flux changing fastest)
ax3.annotate('Flux changing\nfastest → EMF max', xy=(np.pi/2, 1),
             xytext=(np.pi/2+0.8, 0.7), fontsize=9, color=C_RED,
             arrowprops=dict(arrowstyle='->', color=C_RED))
ax3.annotate('Flux at extremum\n→ EMF = 0', xy=(np.pi, 0),
             xytext=(np.pi+0.8, 0.3), fontsize=9, color=C_BLUE,
             arrowprops=dict(arrowstyle='->', color=C_BLUE))

ax3.set_xlabel('t'); ax3.set_ylabel('')
ax3.set_title('1D: Flux & EMF vs Time\n(Faraday + Stokes = Maxwell)', fontsize=10, fontweight='bold')
ax3.legend(fontsize=8, loc='lower right')
ax3.grid(alpha=0.1)

fig.suptitle('Graph 25C-2: Stokes Theorem in Physics — Faraday\'s Law of Induction',
             fontsize=13, fontweight='bold', y=1.02)
plt.savefig(OUT + '25c-stokes-faraday.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.close()
print("25C done")


print("\n=== All 25B & 25C enhancement graphs generated! ===")
