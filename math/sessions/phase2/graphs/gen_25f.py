#!/usr/bin/env python3
"""Generate all 6 graphs for Session 25F: PDE Separation of Variables."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.gridspec import GridSpec

plt.rcParams.update({'font.size': 10, 'figure.dpi': 150})
OUT = '/home/rlawjddn/learning/math/sessions/phase2/graphs'

# ============================================================
# Graph 25F-1: Heat bar evolution — single sine initial condition
# ============================================================
fig = plt.figure(figsize=(18, 8))
L = 1.0; alpha = 1.0; tau = L**2 / (alpha * np.pi**2)

# 3D surface
ax3 = fig.add_subplot(2, 3, (1, 2), projection='3d')
x = np.linspace(0, L, 80)
t = np.linspace(0, 3*tau, 80)
X, T = np.meshgrid(x, t)
U = np.sin(np.pi * X / L) * np.exp(-alpha * np.pi**2 * T / L**2)
ax3.plot_surface(X, T, U, cmap='hot', alpha=0.9, edgecolor='none')
ax3.set_xlabel('x'); ax3.set_ylabel('t'); ax3.set_zlabel('u(x,t)')
ax3.set_title('3D: u(x,t) = sin(πx/L) e^{-t/τ}', fontweight='bold')

# 2D snapshots
ax2 = fig.add_subplot(2, 3, 3)
t_snaps = [0, 0.5*tau, 1.0*tau, 2.0*tau]
colors = ['#e74c3c', '#f39c12', '#3498db', '#2ecc71']
for t_val, c in zip(t_snaps, colors):
    u_snap = np.sin(np.pi * x / L) * np.exp(-t_val / tau)
    ax2.plot(x, u_snap, color=c, linewidth=2, label=f't={t_val/tau:.1f}τ')
ax2.set_xlabel('x'); ax2.set_ylabel('u(x,t)')
ax2.set_title('2D: Temperature profiles at snapshots', fontweight='bold')
ax2.legend(fontsize=8); ax2.grid(True, alpha=0.3)

# 1D — midpoint temperature
ax1 = fig.add_subplot(2, 3, (4, 6))
t_dense = np.linspace(0, 4*tau, 300)
u_mid = np.exp(-t_dense / tau)
ax1.semilogy(t_dense/tau, u_mid, '#e74c3c', linewidth=2.5)
ax1.axhline(y=0.01, color='gray', linestyle=':', linewidth=1, label='1% of initial')
t_99 = -tau * np.log(0.01)
ax1.axvline(x=t_99/tau, color='gray', linestyle=':', linewidth=1,
            label=f'99% cooled at t={t_99/tau:.1f}τ')
ax1.set_xlabel('t / τ'); ax1.set_ylabel('u(L/2, t) [log scale]')
ax1.set_title('1D: Midpoint temp — pure exponential decay', fontweight='bold')
ax1.legend(fontsize=8); ax1.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUT}/25f-heat-bar-evolution.png', bbox_inches='tight', dpi=150)
plt.close()
print('✓ 25f-heat-bar-evolution.png')

# ============================================================
# Graph 25F-2: Heat eigenfunctions and decay rates
# ============================================================
fig = plt.figure(figsize=(18, 8))

# 3D — eigenfunctions
ax3 = fig.add_subplot(2, 3, (1, 2), projection='3d')
x_eig = np.linspace(0, L, 100)
n_vals = np.array([1, 2, 3, 4])
Xe, Ne = np.meshgrid(x_eig, n_vals)
Ze = np.sin(Ne * np.pi * Xe / L)
ax3.plot_surface(Xe, Ne, Ze, cmap='coolwarm', alpha=0.9, edgecolor='none')
ax3.set_xlabel('x'); ax3.set_ylabel('n'); ax3.set_zlabel('X_n(x)')
ax3.set_title('3D: Eigenfunctions sin(nπx/L)', fontweight='bold')

# 2D — decay rates
ax2 = fig.add_subplot(2, 3, 3)
t_decay = np.linspace(0, 3*tau, 200)
for n, c in [(1, '#e74c3c'), (2, '#3498db'), (3, '#2ecc71'), (4, '#f39c12')]:
    decay = np.exp(-alpha * n**2 * np.pi**2 * t_decay / L**2)
    ax2.plot(t_decay/tau, decay, color=c, linewidth=2, label=f'n={n}')
ax2.set_xlabel('t / τ'); ax2.set_ylabel('T_n(t)')
ax2.set_title('2D: Decay rates — n² in exponent', fontweight='bold')
ax2.legend(); ax2.grid(True, alpha=0.3)

# 1D — Fourier decomposition
ax1 = fig.add_subplot(2, 3, (4, 6))
x_fine = np.linspace(0, L, 300)
f_init = np.where(x_fine < L/2, 100.0, 0.0)
ax1.plot(x_fine, f_init, 'k-', linewidth=2.5, label='Initial f(x)')
partial_sums = [1, 3, 9, 39]
for Nmax, c, alpha_val in zip(partial_sums, ['#e74c3c', '#f39c12', '#3498db', '#2ecc71'], [0.4, 0.6, 0.8, 1.0]):
    s = np.zeros_like(x_fine)
    for n in range(1, Nmax+1, 2):
        bn = (200/(n*np.pi)) * (1 - np.cos(n*np.pi/2))
        s += bn * np.sin(n*np.pi*x_fine/L)
    ax1.plot(x_fine, s, color=c, linewidth=1.5, alpha=alpha_val,
             label=f'N={Nmax} terms')
ax1.set_xlabel('x'); ax1.set_ylabel('u(x,0)')
ax1.set_title('1D: Fourier sine series of half-heated bar', fontweight='bold')
ax1.legend(fontsize=8); ax1.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUT}/25f-heat-eigenfunctions.png', bbox_inches='tight', dpi=150)
plt.close()
print('✓ 25f-heat-eigenfunctions.png')

# ============================================================
# Graph 25F-3: Heat multi-mode solution
# ============================================================
fig = plt.figure(figsize=(18, 8))

# 3D
ax3 = fig.add_subplot(2, 3, (1, 2), projection='3d')
x_mode = np.linspace(0, L, 80)
t_mode = np.linspace(0, 3*tau, 80)
Xm, Tm = np.meshgrid(x_mode, t_mode)
Um = np.zeros_like(Xm)
for n in range(1, 30, 2):
    bn = (200/(n*np.pi)) * (1 - np.cos(n*np.pi/2))
    Um += bn * np.sin(n*np.pi*Xm/L) * np.exp(-alpha * n**2 * np.pi**2 * Tm / L**2)
ax3.plot_surface(Xm, Tm, Um, cmap='hot', alpha=0.9, edgecolor='none')
ax3.set_xlabel('x'); ax3.set_ylabel('t'); ax3.set_zlabel('u(x,t)')
ax3.set_title('3D: Half-heated bar cooling', fontweight='bold')

# 2D — contribution of modes at different times
ax2 = fig.add_subplot(2, 3, 3)
times_check = [0, 0.2*tau, 1.0*tau]
mode_colors = {1: '#e74c3c', 2: '#f39c12', 3: '#2ecc71', 4: '#3498db'}
for t_idx, t_val in enumerate(times_check):
    offset = t_idx * 110
    for n in [1, 2, 3, 4]:
        if n % 2 == 0:
            bn = 0
        else:
            bn = (200/(n*np.pi)) * (1 - np.cos(n*np.pi/2))
        mode_contrib = bn * np.sin(n*np.pi*x_mode/L) * np.exp(-alpha*n**2*np.pi**2*t_val/L**2)
        ax2.plot(x_mode, mode_contrib + offset, color=mode_colors[n], linewidth=1.2,
                 alpha=0.7, label=f'n={n}' if t_idx == 0 else '')
    ax2.text(0.02, offset+5, f't={t_val/tau:.1f}τ', fontsize=9, fontweight='bold')
ax2.set_xlabel('x'); ax2.set_yticks([])
ax2.set_title('2D: Mode-by-mode at different times', fontweight='bold')
ax2.legend(fontsize=7); ax2.grid(True, alpha=0.3)

# 1D — total heat content
ax1 = fig.add_subplot(2, 3, (4, 6))
t_heat = np.linspace(0, 5*tau, 300)
total_heat = np.zeros_like(t_heat)
for n in range(1, 40, 2):
    bn = (200/(n*np.pi)) * (1 - np.cos(n*np.pi/2))
    integral_factor = (2*L/(n*np.pi))  # ∫ sin(nπx/L) dx from 0 to L
    total_heat += bn * integral_factor * np.exp(-alpha * n**2 * np.pi**2 * t_heat / L**2)
ax1.plot(t_heat/tau, total_heat/total_heat[0], '#e74c3c', linewidth=2.5)
ax1.axhline(y=0.5, color='gray', linestyle='--', label='50% heat remaining')
ax1.set_xlabel('t / τ'); ax1.set_ylabel('Total heat / Initial heat')
ax1.set_title('1D: Heat content decay — dominated by n=1 mode', fontweight='bold')
ax1.legend(); ax1.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUT}/25f-heat-multimode.png', bbox_inches='tight', dpi=150)
plt.close()
print('✓ 25f-heat-multimode.png')

# ============================================================
# Graph 25F-4: Wave equation — string standing waves
# ============================================================
fig = plt.figure(figsize=(18, 8))
c_wave = 1.0; L_wave = 1.0
T_period = 2*L_wave/c_wave
omega1 = np.pi * c_wave / L_wave

# 3D
ax3 = fig.add_subplot(2, 3, (1, 2), projection='3d')
x_w = np.linspace(0, L_wave, 80)
t_w = np.linspace(0, T_period, 80)
Xw, Tw = np.meshgrid(x_w, t_w)
Yw = np.zeros_like(Xw)
for n in range(1, 30, 2):
    coef = (8/(n**2*np.pi**2)) * np.sin(n*np.pi/2)
    Yw += coef * np.sin(n*np.pi*Xw/L_wave) * np.cos(n*omega1*Tw)
ax3.plot_surface(Xw, Tw, Yw, cmap='coolwarm', alpha=0.9, edgecolor='none')
ax3.set_xlabel('x'); ax3.set_ylabel('t'); ax3.set_zlabel('y(x,t)')
ax3.set_title(f'3D: Plucked string — 1 period (T={T_period:.1f})', fontweight='bold')

# 2D snapshots
ax2 = fig.add_subplot(2, 3, 3)
snap_times = [0, T_period/8, T_period/4, 3*T_period/8, T_period/2]
colors_snap = ['#e74c3c', '#f39c12', '#3498db', '#2ecc71', '#9b59b6']
for t_s, c in zip(snap_times, colors_snap):
    y_snap = np.zeros_like(x_w)
    for n in range(1, 30, 2):
        coef = (8/(n**2*np.pi**2)) * np.sin(n*np.pi/2)
        y_snap += coef * np.sin(n*np.pi*x_w/L_wave) * np.cos(n*omega1*t_s)
    ax2.plot(x_w, y_snap, color=c, linewidth=2, label=f't=T/{int(T_period/t_s) if t_s>0 else 0}' if t_s>0 else 't=0')
ax2.set_xlabel('x'); ax2.set_ylabel('y(x,t)')
ax2.set_title('2D: String snapshots over half period', fontweight='bold')
ax2.legend(fontsize=7); ax2.grid(True, alpha=0.3)

# 1D — Fourier coefficients
ax1 = fig.add_subplot(2, 3, (4, 6))
n_spec = np.arange(1, 16)
plucked_bn = np.array([(8/(n**2*np.pi**2))*abs(np.sin(n*np.pi/2)) for n in n_spec])
struck_bn = np.array([1.2/n for n in n_spec])
ax1.stem(n_spec, plucked_bn, linefmt='#2ecc71', markerfmt='o', basefmt=' ',
         label='Plucked (center): odd only, ~1/n² (mellow)')
ax1.stem(n_spec+0.15, struck_bn, linefmt='#9b59b6', markerfmt='s', basefmt=' ',
         label='Struck (piano): all n, ~1/n (bright)')
wave_freq = c_wave/(2*L_wave)
# mark harmonics
for n in [1, 2, 3, 4]:
    ax1.annotate(f'f={n*wave_freq:.1f}', xy=(n, 0.1), fontsize=7, rotation=90, ha='center')
ax1.set_xlabel('Harmonic n'); ax1.set_ylabel('|A_n|')
ax1.set_title('1D: Harmonic spectrum — plucked vs struck', fontweight='bold')
ax1.legend(fontsize=8); ax1.grid(True, alpha=0.3)



plt.tight_layout()
plt.savefig(f'{OUT}/25f-wave-string-modes.png', bbox_inches='tight', dpi=150)
plt.close()
print('✓ 25f-wave-string-modes.png')

# ============================================================
# Graph 25F-5: Laplace on a rectangle
# ============================================================
fig = plt.figure(figsize=(18, 8))
a_rect = 1.0; b_rect = 1.0

# 3D surface
ax3 = fig.add_subplot(2, 3, (1, 2), projection='3d')
x_rect = np.linspace(0, a_rect, 60)
y_rect = np.linspace(0, b_rect, 60)
Xr, Yr = np.meshgrid(x_rect, y_rect)
Ur = np.zeros_like(Xr)
for n in range(1, 40, 2):
    cn = 4/(n*np.pi*np.sinh(n*np.pi))
    Ur += cn * np.sin(n*np.pi*Xr/a_rect) * np.sinh(n*np.pi*Yr/a_rect)
ax3.plot_surface(Xr, Yr, Ur, cmap='viridis', alpha=0.9, edgecolor='none')
ax3.set_xlabel('x'); ax3.set_ylabel('y'); ax3.set_zlabel('u(x,y)')
ax3.set_title('3D: Laplace solution on rectangle', fontweight='bold')

# 2D — equipotential curves
ax2 = fig.add_subplot(2, 3, 3)
levels = np.linspace(0.01, 0.99, 12)
contour = ax2.contour(Xr, Yr, Ur, levels=levels, cmap='viridis')
ax2.clabel(contour, inline=True, fontsize=7)
# color the edges
ax2.axhline(y=0, color='#3498db', linewidth=3, alpha=0.5, label='u=0')
ax2.axhline(y=b_rect, color='#e74c3c', linewidth=3, alpha=0.5, label='u=1 (top)')
ax2.axvline(x=0, color='#3498db', linewidth=3, alpha=0.5)
ax2.axvline(x=a_rect, color='#3498db', linewidth=3, alpha=0.5)
ax2.set_xlabel('x'); ax2.set_ylabel('y')
ax2.set_title('2D: Equipotential curves (∇²u=0)', fontweight='bold')
ax2.legend(fontsize=7)

# 1D — vertical slices
ax1 = fig.add_subplot(2, 3, (4, 6))
x_slice_positions = [a_rect/4, a_rect/2, 3*a_rect/4]
colors_slice = ['#e74c3c', '#f39c12', '#3498db']
for x_s, c, label in zip(x_slice_positions, colors_slice, ['x=a/4', 'x=a/2 (center)', 'x=3a/4']):
    u_slice = np.zeros_like(y_rect)
    for n in range(1, 40, 2):
        cn = 4/(n*np.pi*np.sinh(n*np.pi))
        u_slice += cn * np.sin(n*np.pi*x_s/a_rect) * np.sinh(n*np.pi*y_rect/a_rect)
    ax1.plot(y_rect, u_slice, color=c, linewidth=2, label=label)
ax1.set_xlabel('y'); ax1.set_ylabel('u(x₀, y)')
ax1.set_title('1D: Vertical slices — potential rising from 0', fontweight='bold')
ax1.legend(); ax1.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUT}/25f-laplace-rectangle.png', bbox_inches='tight', dpi=150)
plt.close()
print('✓ 25f-laplace-rectangle.png')

# ============================================================
# Graph 25F-6: Laplace on a disk — Poisson kernel
# ============================================================
fig = plt.figure(figsize=(18, 8))
R_disk = 1.0

# 3D — solution surface
ax3 = fig.add_subplot(2, 3, (1, 2), projection='3d')
r_vals = np.linspace(0, 0.98, 50)
theta_vals = np.linspace(0, 2*np.pi, 80)
Rgrid, Tgrid = np.meshgrid(r_vals, theta_vals)
X_disk = Rgrid * np.cos(Tgrid)
Y_disk = Rgrid * np.sin(Tgrid)
# f(theta) = 1 on [0,π], 0 on [π,2π]
U_disk = np.zeros_like(Rgrid)
for n in range(1, 30, 2):
    bn = 2/(n*np.pi)
    U_disk += bn * (Rgrid/R_disk)**n * np.sin(n*Tgrid)
U_disk += 0.5  # a0/2
ax3.plot_surface(X_disk, Y_disk, U_disk, cmap='viridis', alpha=0.9, edgecolor='none')
ax3.set_xlabel('x'); ax3.set_ylabel('y'); ax3.set_zlabel('u(r,θ)')
ax3.set_title('3D: Half-heated disk boundary', fontweight='bold')

# 2D — Poisson kernel
ax2 = fig.add_subplot(2, 3, 3)
phi = np.linspace(0, 2*np.pi, 400)
r_pk = [0.1, 0.5, 0.8, 0.95]
colors_pk = ['#e74c3c', '#f39c12', '#3498db', '#2ecc71']
theta_fixed = 0.0  # evaluate kernel at theta=0
for r_val, c in zip(r_pk, colors_pk):
    kernel = (R_disk**2 - r_val**2) / (R_disk**2 - 2*R_disk*r_val*np.cos(theta_fixed - phi) + r_val**2)
    ax2.plot(phi, kernel, color=c, linewidth=2, label=f'r={r_val}')
ax2.set_xlabel('φ'); ax2.set_ylabel('Poisson kernel P(r,θ; φ)')
ax2.set_title(f'2D: Poisson kernel at θ=0', fontweight='bold')
ax2.legend(fontsize=8); ax2.grid(True, alpha=0.3)

# 1D — radial profiles
ax1 = fig.add_subplot(2, 3, (4, 6))
theta_profiles = [0.0, np.pi/2, np.pi]
colors_prof = ['#e74c3c', '#f39c12', '#3498db']
labels_prof = ['θ=0 (hot center)', 'θ=π/2 (boundary)', 'θ=π (cold center)']
for th, c, lab in zip(theta_profiles, colors_prof, labels_prof):
    u_radial = np.zeros_like(r_vals)
    for n in range(1, 30, 2):
        bn = 2/(n*np.pi)
        u_radial += bn * (r_vals/R_disk)**n * np.sin(n*th)
    u_radial += 0.5
    ax1.plot(r_vals, u_radial, color=c, linewidth=2, label=lab)
ax1.axhline(y=0.5, color='gray', linestyle='--', linewidth=1, label='Mean = 0.5 (at r=0)')
ax1.set_xlabel('r'); ax1.set_ylabel('u(r, θ₀)')
ax1.set_title('1D: Radial profiles converge to mean at center', fontweight='bold')
ax1.legend(fontsize=8); ax1.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUT}/25f-laplace-disk.png', bbox_inches='tight', dpi=150)
plt.close()
print('✓ 25f-laplace-disk.png')

print('\n=== All 6 graphs for 25F generated! ===')
