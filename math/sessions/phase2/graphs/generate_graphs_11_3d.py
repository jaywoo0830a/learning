"""
Generate 3D/nD trig visualization graphs for Session 11B.

11k — 3D: Spherical coordinates (r, θ, φ) on the unit sphere
11l — nD: Hypersphere volume concept — trig generalizes to higher dimensions
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

rcParams['font.family'] = 'DejaVu Sans'
rcParams['axes.unicode_minus'] = True

OUT = '/home/rlawjddn/learning/math/sessions/phase2/graphs/'

# ================================================================
# 11k — 3D: Spherical Coordinates — Trig in Three Dimensions
# ================================================================
fig = plt.figure(figsize=(12, 11))
ax = fig.add_subplot(111, projection='3d')

# Draw unit sphere (wireframe, translucent)
u = np.linspace(0, 2*np.pi, 40)
v = np.linspace(0, np.pi, 30)
x_sphere = np.outer(np.cos(u), np.sin(v))
y_sphere = np.outer(np.sin(u), np.sin(v))
z_sphere = np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_wireframe(x_sphere, y_sphere, z_sphere, color='gray', linewidth=0.3, alpha=0.15)

# Mark a point at (r=1, θ=50°, φ=30°) in spherical coordinates
theta_deg = 50
phi_deg = 30
theta = np.deg2rad(theta_deg)
phi = np.deg2rad(phi_deg)

# Cartesian: x = r sinφ cosθ, y = r sinφ sinθ, z = r cosφ
r = 1.0
px = r * np.sin(phi) * np.cos(theta)
py = r * np.sin(phi) * np.sin(theta)
pz = r * np.cos(phi)

# Draw the point
ax.scatter([px], [py], [pz], s=120, c='red', zorder=5)
ax.text(px + 0.08, py + 0.08, pz + 0.08, r'$P(\theta,\phi)$', fontsize=13, color='red')

# Draw the radial line from origin
ax.plot([0, px], [0, py], [0, pz], 'r-', linewidth=2, alpha=0.7)

# Draw projection onto xy-plane
ax.plot([0, px], [0, py], [0, 0], 'b--', linewidth=1.5, alpha=0.5)
ax.plot([px, px], [py, py], [0, pz], 'g--', linewidth=1.5, alpha=0.5)

# Draw the θ arc in xy-plane (azimuthal angle)
arc_theta_vals = np.linspace(0, theta, 50)
arc_r = 0.35
ax.plot(arc_r * np.cos(arc_theta_vals), arc_r * np.sin(arc_theta_vals), 0,
        'b-', linewidth=2.5, label=r'$\theta$ (azimuth, 0 to $2\pi$)')

# Draw the φ arc from z-axis (polar angle)
arc_phi_vals = np.linspace(0, phi, 50)
# The phi arc lies in the vertical plane containing the point
arc_phi_x = 0.35 * np.sin(arc_phi_vals) * np.cos(theta)
arc_phi_y = 0.35 * np.sin(arc_phi_vals) * np.sin(theta)
arc_phi_z = 0.35 * np.cos(arc_phi_vals)
ax.plot(arc_phi_x, arc_phi_y, arc_phi_z, 'g-', linewidth=2.5,
        label=r'$\phi$ (polar, 0 to $\pi$)')

# Coordinate axes
ax.quiver(0, 0, 0, 1.3, 0, 0, color='black', linewidth=1, arrow_length_ratio=0.06)
ax.quiver(0, 0, 0, 0, 1.3, 0, color='black', linewidth=1, arrow_length_ratio=0.06)
ax.quiver(0, 0, 0, 0, 0, 1.3, color='black', linewidth=1, arrow_length_ratio=0.06)
ax.text(1.35, 0, 0, 'x', fontsize=13)
ax.text(0, 1.35, 0, 'y', fontsize=13)
ax.text(0, 0, 1.35, 'z', fontsize=13)

# Conversion formula box
ax.text2D(0.05, 0.95,
          r'Spherical → Cartesian:' + '\n'
          r'$x = r \sin\phi \cos\theta$' + '\n'
          r'$y = r \sin\phi \sin\theta$' + '\n'
          r'$z = r \cos\phi$' + '\n'
          r'$r \geq 0,\; 0 \leq \theta < 2\pi,\; 0 \leq \phi \leq \pi$',
          transform=ax.transAxes, fontsize=13, verticalalignment='top',
          bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.85))

ax.set_xlabel('X', fontsize=14)
ax.set_ylabel('Y', fontsize=14)
ax.set_zlabel('Z', fontsize=14)
ax.set_title('Graph 11k: Spherical Coordinates — Trigonometry in 3D', fontsize=16, fontweight='bold')
ax.legend(fontsize=12, loc='upper right')
ax.set_xlim([-1.3, 1.3])
ax.set_ylim([-1.3, 1.3])
ax.set_zlim([-1.3, 1.3])
ax.view_init(elev=25, azim=-55)
ax.tick_params(labelsize=11)
plt.tight_layout()
plt.savefig(OUT + '11k-spherical-coordinates-3d.png', dpi=180, bbox_inches='tight')
plt.close()
print("11k done — Spherical Coordinates (3D)")


# ================================================================
# 11l — nD: Hypersphere — Trig Generalizes to Higher Dimensions
# ================================================================
fig, ax = plt.subplots(figsize=(12, 8))

# Show volumes of n-spheres as a conceptual plot
dimensions = np.arange(1, 11)
# Volume of unit n-ball: V_n = π^{n/2} / Γ(n/2 + 1)
from math import gamma
volumes = np.array([np.pi**(d/2) / gamma(d/2 + 1) for d in dimensions])

# Bar chart of volumes
bars = ax.bar(dimensions, volumes, color='steelblue', alpha=0.7, edgecolor='navy', linewidth=1)

# Annotate bars with values
for dim, vol in zip(dimensions, volumes):
    ax.text(dim, vol + 0.03, f'{vol:.3f}', ha='center', fontsize=10, fontweight='bold')

# Highlight dimension 5 (peak volume)
ax.bar(5, volumes[4], color='darkorange', alpha=0.8, edgecolor='darkred', linewidth=2,
       label='Peak volume at n=5 (unit radius)')

ax.set_xlabel('Dimension n', fontsize=15)
ax.set_ylabel(r'Volume of unit $n$-ball  $V_n = \frac{\pi^{n/2}}{\Gamma(n/2 + 1)}$', fontsize=14)
ax.set_title('Graph 11l: The Volume of an $n$-Dimensional Sphere (Hypersphere)',
             fontsize=16, fontweight='bold')
ax.legend(fontsize=12, loc='upper right')
ax.grid(axis='y', alpha=0.3)
ax.set_xticks(dimensions)
ax.tick_params(labelsize=12)

# Insight box
ax.text(0.5, 0.88,
        r'Interesting fact: the volume of the unit $n$-sphere' + '\n'
        r'peaks at $n=5$, then shrinks toward zero as $n \to \infty$.' + '\n'
        r'The surface area is $S_{n-1} = n V_n$, involving $\sin^{n-2}\phi$' + '\n'
        r'in the angular integrals — trigonometry in every dimension.',
        transform=ax.transAxes, fontsize=12, ha='center',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8),
        verticalalignment='top')

# Add a conceptual annotation about spherical harmonics
ax.text(0.5, 0.55,
        r'In $n$ dimensions, the Laplacian eigenfunctions on the sphere' + '\n'
        r'are spherical harmonics — generalizations of $\sin(k\theta)$ and $\cos(k\theta)$.' + '\n'
        r'In 3D: $Y_\ell^m(\theta,\phi) \propto P_\ell^m(\cos\theta) e^{im\phi}$',
        transform=ax.transAxes, fontsize=11, ha='center', color='darkred',
        bbox=dict(boxstyle='round', facecolor='mistyrose', alpha=0.5),
        verticalalignment='top')

plt.tight_layout()
plt.savefig(OUT + '11l-hypersphere-volumes.png', dpi=180, bbox_inches='tight')
plt.close()
print("11l done — Hypersphere Volumes (nD concept)")


print("\n=== All 3D/nD trig graphs generated! ===")
