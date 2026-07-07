#!/usr/bin/env python3
"""Generate all 8 graphs for Session 25E: Fourier Series and Transform."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.gridspec import GridSpec

plt.rcParams.update({'font.size': 10, 'figure.dpi': 150})
OUT = '/home/rlawjddn/learning/math/sessions/phase2/graphs'

# ============================================================
# Graph 25E-1: Fourier synthesis — building a square wave
# ============================================================
def square_wave_fourier(x, N):
    s = np.zeros_like(x)
    for n in range(1, N+1, 2):
        s += (4/(np.pi*n)) * np.sin(n * x)
    return s

fig = plt.figure(figsize=(18, 6))
# 3D
ax3 = fig.add_subplot(1, 3, 1, projection='3d')
N_vals = np.arange(1, 31, 2)
x_3d = np.linspace(-np.pi, np.pi, 200)
X3, N3 = np.meshgrid(x_3d, N_vals)
Z3 = np.zeros_like(X3)
for i, N in enumerate(N_vals):
    Z3[i, :] = square_wave_fourier(x_3d, N)
ax3.plot_surface(X3, N3, Z3, cmap='coolwarm', alpha=0.9, edgecolor='none')
ax3.set_xlabel('x'); ax3.set_ylabel('N (harmonics)'); ax3.set_zlabel('f(x)')
ax3.set_title('3D: Square wave builds from sines', fontweight='bold')

# 2D
ax2 = fig.add_subplot(1, 3, 2)
x_2d = np.linspace(-np.pi, np.pi, 400)
colors = ['#e74c3c', '#3498db', '#2ecc71']
for i, n in enumerate([1, 3, 5]):
    ax2.plot(x_2d, (4/(np.pi*n))*np.sin(n*x_2d), color=colors[i],
             label=f'n={n}, amp={4/(np.pi*n):.2f}', linewidth=1.5)
ax2.set_xlabel('x'); ax2.set_ylabel('amplitude')
ax2.set_title('2D: First 3 harmonic components', fontweight='bold')
ax2.legend(fontsize=8); ax2.grid(True, alpha=0.3)

# 1D
ax1 = fig.add_subplot(1, 3, 3)
target = np.where((x_2d % (2*np.pi)) < np.pi, 1.0, -1.0)
ax1.plot(x_2d, target, 'k--', linewidth=2, label='Target square wave')
for N, c, alpha in [(1, '#e74c3c', 0.7), (3, '#f39c12', 0.8), (5, '#3498db', 0.9), (15, '#2ecc71', 1.0)]:
    y = square_wave_fourier(x_2d, N)
    ax1.plot(x_2d, y, color=c, alpha=alpha, linewidth=1.3, label=f'N={N}')
ax1.set_xlabel('x'); ax1.set_ylabel('f(x)')
ax1.set_title('1D: Partial sums approaching square wave', fontweight='bold')
ax1.legend(fontsize=7); ax1.grid(True, alpha=0.3)
ax1.set_ylim(-1.5, 1.5)

plt.tight_layout()
plt.savefig(f'{OUT}/25e-fourier-synthesis.png', bbox_inches='tight', dpi=150)
plt.close()
print('✓ 25e-fourier-synthesis.png')

# ============================================================
# Graph 25E-2: Even vs Odd — triangle (cos) vs sawtooth (sin)
# ============================================================
fig = plt.figure(figsize=(18, 8))

# 3D
ax3 = fig.add_subplot(2, 3, 1, projection='3d')
n_vals = np.arange(1, 11)
x_3d = np.linspace(-1, 1, 150)
X3, N3 = np.meshgrid(x_3d, n_vals)
Z3_tri = np.zeros_like(X3)
for i, n in enumerate(n_vals):
    if n % 2 == 1:
        coef = -4/(n**2 * np.pi**2)
        Z3_tri[i, :] = coef * np.cos(n * np.pi * x_3d)
ax3.plot_surface(X3, N3, Z3_tri, cmap='viridis', alpha=0.85, edgecolor='none')
ax3.set_title('3D: Triangle (even) — cosine terms', fontweight='bold')
ax3.set_xlabel('x'); ax3.set_ylabel('n'); ax3.set_zlabel('amplitude')

ax3b = fig.add_subplot(2, 3, 2, projection='3d')
Z3_saw = np.zeros_like(X3)
for i, n in enumerate(n_vals):
    coef = 2*(-1)**(n+1)/(n*np.pi)
    Z3_saw[i, :] = coef * np.sin(n * np.pi * x_3d)
ax3b.plot_surface(X3, N3, Z3_saw, cmap='plasma', alpha=0.85, edgecolor='none')
ax3b.set_title('3D: Sawtooth (odd) — sine terms', fontweight='bold')
ax3b.set_xlabel('x'); ax3b.set_ylabel('n'); ax3b.set_zlabel('amplitude')

# 2D spectra
ax2a = fig.add_subplot(2, 3, 4)
n_rng = np.arange(1, 16)
tri_coef = np.array([4/(n**2*np.pi**2) if n%2==1 else 0 for n in n_rng])
ax2a.stem(n_rng, tri_coef, linefmt='#2ecc71', markerfmt='o', basefmt=' ')
ax2a.set_title('2D: Triangle spectrum ~1/n² (cos)', fontweight='bold')
ax2a.set_xlabel('n'); ax2a.set_ylabel('|coefficient|')
ax2a.grid(True, alpha=0.3)

ax2b = fig.add_subplot(2, 3, 5)
saw_coef = np.array([2/(n*np.pi) for n in n_rng])
ax2b.stem(n_rng, saw_coef, linefmt='#e74c3c', markerfmt='s', basefmt=' ')
ax2b.set_title('2D: Sawtooth spectrum ~1/n (sin)', fontweight='bold')
ax2b.set_xlabel('n'); ax2b.set_ylabel('|coefficient|')
ax2b.grid(True, alpha=0.3)

# 1D comparison
ax1 = fig.add_subplot(2, 3, 6)
n_list = np.arange(1, 21)
ax1.loglog(n_list, 1/n_list, 'r-o', label='~1/n (discontinuous)', markersize=4)
ax1.loglog(n_list, 1/n_list**2, 'g-s', label='~1/n² (continuous deriv)', markersize=4)
ax1.loglog(n_list, np.exp(-n_list/3), 'b-^', label='~e^{-n} (C^∞ smooth)', markersize=4)
ax1.set_xlabel('n'); ax1.set_ylabel('coefficient magnitude')
ax1.set_title('1D: Decay rate = smoothness', fontweight='bold')
ax1.legend(fontsize=8); ax1.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUT}/25e-even-odd-series.png', bbox_inches='tight', dpi=150)
plt.close()
print('✓ 25e-even-odd-series.png')

# ============================================================
# Graph 25E-3: Gibbs phenomenon
# ============================================================
fig = plt.figure(figsize=(18, 6))

# 3D — zoom near jump
ax3 = fig.add_subplot(1, 3, 1, projection='3d')
x_gibbs = np.linspace(-0.5, 0.5, 300)
N_gibbs = np.array([5, 11, 21, 51])
X3g, N3g = np.meshgrid(x_gibbs, N_gibbs)
Z3g = np.zeros_like(X3g)
for i, N in enumerate(N_gibbs):
    s = np.zeros_like(x_gibbs)
    for n in range(1, N+1, 2):
        s += (4/(np.pi*n)) * np.sin(n * (x_gibbs + np.pi/2))
    Z3g[i, :] = s
ax3.plot_surface(X3g, N3g, Z3g, cmap='coolwarm', alpha=0.85, edgecolor='none')
ax3.set_xlabel('x (near jump)'); ax3.set_ylabel('N')
ax3.set_title('3D: Overshoot narrows but never shrinks', fontweight='bold')

# 2D
ax2 = fig.add_subplot(1, 3, 2)
for N, c in [(5, '#e74c3c'), (15, '#f39c12'), (51, '#3498db')]:
    s = np.zeros_like(x_gibbs)
    for n in range(1, N+1, 2):
        s += (4/(np.pi*n)) * np.sin(n * (x_gibbs + np.pi/2))
    ax2.plot(x_gibbs, s, color=c, linewidth=1.2, label=f'N={N}')
ax2.axhline(y=1.08949, color='gray', linestyle=':', linewidth=1, label='~1.0895 (Gibbs constant)')
ax2.axhline(y=1.0, color='k', linestyle='--', linewidth=0.8)
ax2.set_xlim(-0.3, 0.3); ax2.set_ylim(0.7, 1.2)
ax2.set_xlabel('x'); ax2.set_ylabel('f(x)')
ax2.set_title('2D: Zoom on overshoot', fontweight='bold')
ax2.legend(fontsize=8); ax2.grid(True, alpha=0.3)

# 1D
ax1 = fig.add_subplot(1, 3, 3)
t = np.linspace(0.01, 5, 300)
integrand = np.sin(t)/t
gibbs_integral = np.array([np.trapz(integrand[:i], t[:i]) for i in range(1, len(t)+1)])
ax1.plot(t, gibbs_integral, 'b', linewidth=2)
ax1.axhline(y=np.pi/2, color='gray', linestyle='--', label='π/2')
overshoot_val = (1/np.pi)*np.trapz(integrand, t) - 0.5
ax1.axhline(y=np.pi/2, color='r', linestyle=':', linewidth=1.5,
            label=f'∫₀^∞ sin(t)/t dt = π/2\n→ overshoot = {overshoot_val:.4f}')
ax1.set_xlabel('t'); ax1.set_ylabel('∫₀^t sin(τ)/τ dτ')
ax1.set_title('1D: Gibbs constant integral', fontweight='bold')
ax1.legend(fontsize=8); ax1.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUT}/25e-gibbs-phenomenon.png', bbox_inches='tight', dpi=150)
plt.close()
print('✓ 25e-gibbs-phenomenon.png')

# ============================================================
# Graph 25E-4: Complex Fourier spectrum
# ============================================================
fig = plt.figure(figsize=(18, 6))

# 3D — c_n in complex plane
ax3 = fig.add_subplot(1, 3, 1, projection='3d')
n_vals = np.arange(-15, 16)
c_real = np.zeros(len(n_vals))
c_imag = np.zeros(len(n_vals))
for i, n in enumerate(n_vals):
    if n != 0 and n % 2 != 0:
        c_real[i] = 0
        c_imag[i] = -2/(n*np.pi) if n > 0 else 2/(abs(n)*np.pi)
    elif n == 0:
        c_real[i] = 0.5
        c_imag[i] = 0
n_nz = n_vals != 0
ax3.stem(n_vals[n_nz], c_imag[n_nz], c_real[n_nz], linefmt='#3498db', markerfmt='o', basefmt=' ')
ax3.scatter([0], [0], [0.5], color='#e74c3c', s=50, zorder=5)
ax3.set_xlabel('Re(c_n)'); ax3.set_ylabel('Im(c_n)'); ax3.set_zlabel('n (harmonic index)')
ax3.set_title('3D: c_n in complex plane', fontweight='bold')

# 2D — amplitude and phase
ax2a = fig.add_subplot(1, 3, 2)
n_pos = np.arange(0, 16)
amp = np.array([0.5 if n==0 else (2/(n*np.pi) if n%2==1 else 0) for n in n_pos])
ax2a.stem(n_pos, amp, linefmt='#e74c3c', markerfmt='o', basefmt=' ')
ax2a.set_xlabel('n'); ax2a.set_ylabel('|c_n|')
ax2a.set_title('2D: Amplitude spectrum', fontweight='bold')
ax2a.grid(True, alpha=0.3)

ax2b = fig.add_subplot(1, 3, 3)
power = amp**2
ax2b.stem(n_pos, power, linefmt='#2ecc71', markerfmt='s', basefmt=' ')
ax2b.set_xlabel('n'); ax2b.set_ylabel('|c_n|²')
ax2b.set_title('2D: Power spectrum ~1/n²', fontweight='bold')
ax2b.grid(True, alpha=0.3)
# annotation
cumulative = np.cumsum(power[1:])
total = np.sum(power[1:])
n90 = np.argmax(cumulative > 0.9*total) + 1
ax2b.annotate(f'90% energy\nin first {n90} harmonics', xy=(n90, power[n90]),
              xytext=(n90+2, power[1]*0.5), fontsize=8,
              arrowprops=dict(arrowstyle='->', color='gray'))

plt.tight_layout()
plt.savefig(f'{OUT}/25e-complex-spectrum.png', bbox_inches='tight', dpi=150)
plt.close()
print('✓ 25e-complex-spectrum.png')

# ============================================================
# Graph 25E-5: Rectangular pulse → sinc
# ============================================================
fig = plt.figure(figsize=(18, 8))

# 3D surface
ax3 = fig.add_subplot(2, 3, (1, 2), projection='3d')
omega = np.linspace(-20, 20, 200)
a_vals = np.array([0.3, 0.6, 1.0, 1.5, 2.0])
Om, Am = np.meshgrid(omega, a_vals)
Z_3d = np.abs(2 * np.sin(Om * Am) / (Om + 1e-10))
zero_idx = np.argmin(np.abs(omega))
Z_3d[:, zero_idx] = 2 * a_vals  # fix at omega=0
ax3.plot_surface(Om, Am, Z_3d, cmap='coolwarm', alpha=0.9, edgecolor='none')
ax3.set_xlabel('ω'); ax3.set_ylabel('a (pulse half-width)'); ax3.set_zlabel('|f̂(ω)|')
ax3.set_title('3D: |f̂(ω)| vs ω and pulse width a', fontweight='bold')

# 2D — three pulse widths
ax2t = fig.add_subplot(2, 3, 3)
t_pulse = np.linspace(-4, 4, 500)
for a, c in [(0.5, '#e74c3c'), (1.0, '#f39c12'), (2.0, '#3498db')]:
    pulse = np.where(np.abs(t_pulse) <= a, 1.0, 0.0)
    ax2t.plot(t_pulse, pulse, color=c, linewidth=2, label=f'a={a}')
ax2t.set_xlabel('t'); ax2t.set_ylabel('f(t)')
ax2t.set_title('2D: Rectangular pulses (time)', fontweight='bold')
ax2t.legend(); ax2t.grid(True, alpha=0.3)

ax2f = fig.add_subplot(2, 3, 6)
omega2 = np.linspace(-20, 20, 800)
for a, c in [(0.5, '#e74c3c'), (1.0, '#f39c12'), (2.0, '#3498db')]:
    spec = np.abs(2*np.sin(omega2*a)/(omega2 + 1e-10))
    spec[np.argmin(np.abs(omega2))] = 2*a
    ax2f.plot(omega2, spec, color=c, linewidth=1.5, label=f'a={a}')
ax2f.set_xlabel('ω'); ax2f.set_ylabel('|f̂(ω)|')
ax2f.set_title('2D: Sinc spectra (frequency)', fontweight='bold')
ax2f.legend(); ax2f.grid(True, alpha=0.3)
ax2f.set_xlim(-20, 20)

# 1D — sinc function
ax1 = fig.add_subplot(2, 3, (4, 5))
x_sinc = np.linspace(-10, 10, 500)
sinc = np.sin(np.pi*x_sinc)/(np.pi*x_sinc + 1e-15)
ax1.plot(x_sinc, sinc, '#2ecc71', linewidth=2)
ax1.fill_between(x_sinc, 0, sinc, where=(np.abs(x_sinc)>0), alpha=0.2, color='#2ecc71')
ax1.axhline(y=0, color='gray', linestyle='-', linewidth=0.5)
for k in range(1, 5):
    ax1.axvline(x=k, color='gray', linestyle=':', linewidth=0.5, alpha=0.5)
    ax1.axvline(x=-k, color='gray', linestyle=':', linewidth=0.5, alpha=0.5)
ax1.set_xlabel('x'); ax1.set_ylabel('sinc(x) = sin(πx)/(πx)')
ax1.set_title('1D: sinc function — zeros at integers, ~1/x envelope', fontweight='bold')
ax1.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUT}/25e-pulse-sinc.png', bbox_inches='tight', dpi=150)
plt.close()
print('✓ 25e-pulse-sinc.png')

# ============================================================
# Graph 25E-6: Gaussian → Gaussian
# ============================================================
fig = plt.figure(figsize=(18, 6))

# 3D
ax3 = fig.add_subplot(1, 3, 1, projection='3d')
t_gauss = np.linspace(-4, 4, 200)
sigma_vals = np.array([0.5, 0.75, 1.0, 1.5, 2.0])
Tg, Sg = np.meshgrid(t_gauss, sigma_vals)
Zg_t = np.exp(-Tg**2 / (2 * Sg**2))
ax3.plot_surface(Tg, Sg, Zg_t, cmap='Reds', alpha=0.7, edgecolor='none', label='Time')

omega_g = np.linspace(-4, 4, 200)
Og, Sg2 = np.meshgrid(omega_g, sigma_vals)
Zg_f = np.exp(-Sg2**2 * Og**2 / 2)
ax3.plot_surface(Og+5, Sg2, Zg_f, cmap='Blues', alpha=0.7, edgecolor='none')
ax3.set_xlabel('t (red) / ω (blue, shifted)'); ax3.set_ylabel('σ')
ax3.set_title('3D: Gaussian in time (red) and freq (blue)', fontweight='bold')

# 2D
ax2 = fig.add_subplot(1, 3, 2)
for sigma, c in [(0.5, '#e74c3c'), (1.0, '#f39c12'), (2.0, '#3498db')]:
    g = np.exp(-t_gauss**2/(2*sigma**2))
    ax2.plot(t_gauss, g, color=c, linewidth=2, label=f'σ={sigma}')
    g_hat = np.exp(-sigma**2 * omega_g**2 / 2)
    ax2.plot(omega_g, g_hat, '--', color=c, linewidth=1.5)
ax2.set_xlabel('t or ω'); ax2.set_ylabel('amplitude')
ax2.set_title('2D: Solid=time, Dashed=frequency', fontweight='bold')
ax2.legend(); ax2.grid(True, alpha=0.3)

# 1D — uncertainty product
ax1 = fig.add_subplot(1, 3, 3)
sigma_arr = np.linspace(0.3, 2.5, 100)
dt = sigma_arr / np.sqrt(2)
dw = 1/(sigma_arr * np.sqrt(2))
product = dt * dw
ax1.plot(sigma_arr, product, '#2ecc71', linewidth=2.5)
ax1.axhline(y=0.5, color='gray', linestyle='--', label='Theoretical minimum = 1/2')
ax1.fill_between(sigma_arr, product, 0.5, alpha=0.15, color='#2ecc71')
ax1.set_xlabel('σ'); ax1.set_ylabel('Δt · Δω')
ax1.set_title('1D: Uncertainty product (Gaussian = 1/2)', fontweight='bold')
ax1.legend(fontsize=8); ax1.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUT}/25e-gaussian-ft.png', bbox_inches='tight', dpi=150)
plt.close()
print('✓ 25e-gaussian-ft.png')

# ============================================================
# Graph 25E-7: Vibrating string normal modes
# ============================================================
fig = plt.figure(figsize=(18, 8))

# 3D — plucked string evolution
ax3 = fig.add_subplot(2, 3, (1, 2), projection='3d')
L = 1.0
x_str = np.linspace(0, L, 100)
t_str = np.linspace(0, 2, 100)
Xstr, Tstr = np.meshgrid(x_str, t_str)
c = 1.0
Ystr = np.zeros_like(Xstr)
# Sum first 20 odd modes for a center-plucked shape
for n in range(1, 40, 2):
    coef = (8/(n**2 * np.pi**2)) * np.sin(n*np.pi/2)
    Ystr += coef * np.sin(n*np.pi*Xstr/L) * np.cos(n*np.pi*c*Tstr/L)
ax3.plot_surface(Xstr, Tstr, Ystr, cmap='coolwarm', alpha=0.9, edgecolor='none')
ax3.set_xlabel('x'); ax3.set_ylabel('t'); ax3.set_zlabel('y(x,t)')
ax3.set_title('3D: Plucked string y(x,t)', fontweight='bold')

# 2D — first 4 normal modes
ax2 = fig.add_subplot(2, 3, 3)
for n, c in [(1, '#e74c3c'), (2, '#3498db'), (3, '#2ecc71'), (4, '#f39c12')]:
    mode = np.sin(n*np.pi*x_str/L)
    ax2.plot(x_str, mode + (n-1)*2.2, color=c, linewidth=2, label=f'n={n}, f={n*0.5:.1f} Hz')
ax2.set_xlabel('x'); ax2.set_yticks([])
ax2.set_title('2D: Normal modes (shifted)', fontweight='bold')
ax2.legend(fontsize=8); ax2.grid(True, alpha=0.3)

# 1D — Fourier coefficients (plucked vs struck)
ax1 = fig.add_subplot(2, 3, (4, 6))
n_plot = np.arange(1, 16)
plucked_coef = np.array([(8/(n**2*np.pi**2))*abs(np.sin(n*np.pi/2)) for n in n_plot])
struck_coef = np.array([0.8/n for n in n_plot])  # ~1/n for struck
ax1.stem(n_plot, plucked_coef, linefmt='#2ecc71', markerfmt='o', basefmt=' ',
         label='Plucked (center): only odd, ~1/n²')
ax1.stem(n_plot+0.15, struck_coef, linefmt='#e74c3c', markerfmt='s', basefmt=' ',
         label='Struck (piano): all n, ~1/n (brighter)')
ax1.set_xlabel('harmonic n'); ax1.set_ylabel('|coefficient|')
ax1.set_title('1D: Plucked (mellow) vs Struck (bright) spectrum', fontweight='bold')
ax1.legend(fontsize=8); ax1.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUT}/25e-string-modes.png', bbox_inches='tight', dpi=150)
plt.close()
print('✓ 25e-string-modes.png')

# ============================================================
# Graph 25E-8: NMR FID → spectrum
# ============================================================
fig = plt.figure(figsize=(18, 8))

# 3D — complex FID spiraling
ax3 = fig.add_subplot(2, 3, (1, 2), projection='3d')
t_fid = np.linspace(0, 1.5, 500)
f1, f2 = 300, 500
A1, T2_1 = 3, 0.5
A2, T2_2 = 1, 0.3
fid1 = A1 * np.exp(-t_fid/T2_1) * np.exp(1j * 2*np.pi * f1 * t_fid)
fid2 = A2 * np.exp(-t_fid/T2_2) * np.exp(1j * 2*np.pi * f2 * t_fid)
fid = fid1 + fid2
ax3.plot(t_fid[:300], fid.real[:300], fid.imag[:300], '#3498db', linewidth=1.2)
ax3.set_xlabel('t (s)'); ax3.set_ylabel('Re'); ax3.set_zlabel('Im')
ax3.set_title('3D: Complex FID spiraling in', fontweight='bold')

# 2D — FID (time) and spectrum (frequency)
ax2t = fig.add_subplot(2, 3, 3)
ax2t.plot(t_fid, fid.real, '#e74c3c', linewidth=0.8)
ax2t.set_xlabel('t (s)'); ax2t.set_ylabel('Re S(t)')
ax2t.set_title('2D: FID (time domain)', fontweight='bold')
ax2t.grid(True, alpha=0.3)

ax2f = fig.add_subplot(2, 3, 6)
freq = np.linspace(200, 600, 1000)
spectrum = np.zeros_like(freq, dtype=complex)
for A, T2, f0 in [(A1, T2_1, f1), (A2, T2_2, f2)]:
    spectrum += A * (1/T2) / (1/T2 + 1j*2*np.pi*(freq - f0))
ax2f.plot(freq, spectrum.real, '#3498db', linewidth=2)
ax2f.fill_between(freq, 0, spectrum.real, alpha=0.2, color='#3498db')
# annotate peaks
ax2f.annotate(f'{f1} Hz\nT₂={T2_1}s', xy=(f1, spectrum.real[np.argmin(np.abs(freq-f1))]),
              xytext=(f1+40, A1*0.7), fontsize=8, arrowprops=dict(arrowstyle='->'))
ax2f.annotate(f'{f2} Hz\nT₂={T2_2}s (broader)', xy=(f2, spectrum.real[np.argmin(np.abs(freq-f2))]),
              xytext=(f2-80, A2*1.2), fontsize=8, arrowprops=dict(arrowstyle='->'))
ax2f.set_xlabel('Frequency (Hz)'); ax2f.set_ylabel('Absorption')
ax2f.set_title('2D: FT → Lorentzian peaks', fontweight='bold')
ax2f.grid(True, alpha=0.3)

# 1D — ethanol schematic
ax1 = fig.add_subplot(2, 3, (4, 5))
chem_shifts = [1.2, 3.7, 5.3]
labels = ['CH₃\n(triplet)', 'CH₂\n(quartet)', 'OH\n(singlet)']
areas = [3, 2, 1]
x_chem = np.linspace(0, 7, 500)
y_chem = np.zeros_like(x_chem)
for cs, area in zip(chem_shifts, areas):
    y_chem += area * np.exp(-((x_chem-cs)/0.15)**2)  # gaussian approximation
ax1.plot(x_chem, y_chem, '#2c3e50', linewidth=2)
for cs, label, area in zip(chem_shifts, labels, areas):
    ax1.annotate(label, xy=(cs, area*1.05), fontsize=9, ha='center', fontweight='bold')
ax1.set_xlabel('Chemical shift δ (ppm)'); ax1.set_ylabel('Intensity')
ax1.set_title('1D: Ethanol ¹H NMR — three peak groups', fontweight='bold')
ax1.invert_xaxis()
ax1.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUT}/25e-nmr-fid-spectrum.png', bbox_inches='tight', dpi=150)
plt.close()
print('✓ 25e-nmr-fid-spectrum.png')

print('\n=== All 8 graphs for 25E generated! ===')
