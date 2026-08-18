#!/usr/bin/env python3
"""Generate all graphs for Session 19A — ODE Modeling."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

DPI = 150
OUT_DIR = '19A'

def slope_field():
    """19A-1: Slope field with solution curves for y' = x+y"""
    fig = plt.figure(figsize=(14, 5))
    
    # 2D — slope field + solution curves
    ax = fig.add_subplot(121)
    x = np.linspace(-2, 2, 15)
    y = np.linspace(-2, 2, 15)
    X, Y = np.meshgrid(x, y)
    U = np.ones_like(X)
    V = X + Y
    M = np.sqrt(U**2 + V**2)
    U, V = U/M, V/M
    ax.quiver(X, Y, U, V, M, alpha=0.6, cmap='viridis')
    
    xs = np.linspace(-2, 2, 100)
    for C in [-2, -1, 0, 1, 2]:
        ys = -xs - 1 + C*np.exp(xs)
        mask = (ys > -2.5) & (ys < 2.5)
        ax.plot(xs[mask], ys[mask], lw=2, label=f'C={C}' if C in [-2,0,2] else '')
    
    ax.set_xlim(-2, 2); ax.set_ylim(-2, 2)
    ax.set_xlabel('x'); ax.set_ylabel('y')
    ax.set_title('Slope Field: $dy/dx = x+y$')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')
    
    # 1D — direction field as arrows on a line
    ax2 = fig.add_subplot(122)
    y_vals = np.linspace(-2, 2, 12)
    for y0 in y_vals:
        slope = 0 + y0
        dx = 0.3
        dy = slope * dx
        ax2.arrow(0, y0, dx, dy, head_width=0.08, head_length=0.05, 
                  fc='blue', ec='blue', alpha=0.6)
    ax2.set_xlim(-0.5, 1.5); ax2.set_ylim(-2.5, 2.5)
    ax2.set_xlabel('x step')
    ax2.set_ylabel('y')
    ax2.set_title('Direction arrows at x=0')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'{OUT_DIR}/slope-field.png', dpi=DPI)
    plt.close()
    print('  ✓ slope-field.png')

def growth_decay():
    """19A-2: Exponential growth/decay — 3D+2D+1D"""
    fig = plt.figure(figsize=(14, 10))
    
    # 3D surface y = e^{kt} over (t, k)
    ax = fig.add_subplot(221, projection='3d')
    t = np.linspace(0, 3, 60)
    k = np.linspace(-1, 1, 60)
    T, K = np.meshgrid(t, k)
    Z = np.exp(K * T)
    Z[Z > 8] = np.nan
    surf = ax.plot_surface(T, K, Z, cmap='coolwarm', alpha=0.9,
                           shade=True, antialiased=True, edgecolor='none')
    ax.set_xlabel('Time t'); ax.set_ylabel('Rate k'); ax.set_zlabel('y = e^{kt}')
    ax.set_title('3D: Growth/Decay Surface', fontsize=10)
    ax.view_init(25, -60)
    
    # 2D — families for k=0.5 and k=-0.5
    ax2 = fig.add_subplot(222)
    t2 = np.linspace(0, 4, 100)
    for C in [0.5, 1, 2, 3]:
        ax2.plot(t2, C*np.exp(0.5*t2), 'r-', lw=1.5, alpha=0.7)
        ax2.plot(t2, C*np.exp(-0.5*t2), 'b-', lw=1.5, alpha=0.7)
    ax2.axhline(0, color='gray', lw=0.5)
    ax2.set_xlim(0, 4); ax2.set_ylim(0, 12)
    ax2.set_xlabel('Time t'); ax2.set_ylabel('y(t)')
    ax2.set_title('2D: Growth (red) vs Decay (blue)')
    ax2.grid(True, alpha=0.3)
    
    # 1D — log scale showing doubling/half-life
    ax3 = fig.add_subplot(223)
    t3 = np.linspace(0, 5, 100)
    ax3.semilogy(t3, np.exp(0.5*t3), 'r-', lw=2, label='Growth k=0.5')
    ax3.semilogy(t3, np.exp(-0.5*t3), 'b-', lw=2, label='Decay k=-0.5')
    ax3.axhline(2, color='gray', ls='--', lw=1)
    ax3.axhline(0.5, color='gray', ls='--', lw=1)
    ax3.axvline(np.log(2)/0.5, color='r', ls=':', lw=1, alpha=0.5)
    ax3.axvline(np.log(2)/0.5, color='b', ls=':', lw=1, alpha=0.5)
    ax3.set_xlim(0, 5); ax3.set_ylim(0.1, 20)
    ax3.set_xlabel('Time t'); ax3.set_ylabel('y(t) [log scale]')
    ax3.set_title('1D: Log Scale — Doubling = Half-life distance')
    ax3.legend(fontsize=8)
    ax3.grid(True, alpha=0.3, which='both')
    
    # 1D — rate constant comparison
    ax4 = fig.add_subplot(224)
    t4 = np.linspace(0, 3, 100)
    for k_val, c in zip([0.2, 0.5, 1.0, 2.0], ['purple', 'blue', 'green', 'red']):
        ax4.plot(t4, np.exp(k_val*t4), color=c, lw=2, label=f'k={k_val}')
    ax4.set_xlim(0, 3); ax4.set_ylim(0, 10)
    ax4.set_xlabel('Time t'); ax4.set_ylabel('y(t)')
    ax4.set_title('Effect of Growth Rate k')
    ax4.legend(fontsize=8)
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'{OUT_DIR}/growth-decay.png', dpi=DPI)
    plt.close()
    print('  ✓ growth-decay.png')

def logistic():
    """19A-3: Logistic curve"""
    fig = plt.figure(figsize=(14, 5))
    
    def logistic_func(t, P0, L, k):
        A = (L - P0) / P0
        return L / (1 + A * np.exp(-k * t))
    
    t = np.linspace(0, 15, 200)
    L, k = 1000, 0.5
    
    # 2D — logistic curves with different starting points
    ax = fig.add_subplot(121)
    for P0 in [50, 100, 200, 500, 900]:
        y = logistic_func(t, P0, L, k)
        ax.plot(t, y, lw=2, label=f'P₀={P0}')
    ax.axhline(L, color='gray', ls='--', lw=1, alpha=0.7, label=f'L={L}')
    ax.set_xlim(0, 15); ax.set_ylim(0, 1100)
    ax.set_xlabel('Time t'); ax.set_ylabel('Population P(t)')
    ax.set_title('Logistic Growth $P\'=kP(1-P/L)$')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)
    
    # 1D — rate of change vs population (phase line view)
    ax2 = fig.add_subplot(122)
    P = np.linspace(0, 1200, 200)
    dP = k * P * (1 - P / L)
    ax2.plot(P, dP, 'b-', lw=2)
    ax2.axhline(0, color='gray', lw=0.5)
    ax2.axvline(0, color='gray', lw=0.5)
    ax2.axvline(L/2, color='green', ls='--', lw=1.5, alpha=0.7, label=f'Inflection P={L/2}')
    ax2.axvline(L, color='red', ls='--', lw=1.5, alpha=0.7, label=f'L={L}')
    ax2.scatter([0, L/2, L], [0, k*L/4, 0], color='red', zorder=5)
    ax2.set_xlim(0, 1200)
    ax2.set_xlabel('Population P'); ax2.set_ylabel('dP/dt')
    ax2.set_title('Growth Rate vs Population')
    ax2.legend(fontsize=8)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'{OUT_DIR}/logistic.png', dpi=DPI)
    plt.close()
    print('  ✓ logistic.png')

def phase_line():
    """19A-4: Phase line for y' = y(1-y)(y-2) — 3D+2D+1D"""
    fig = plt.figure(figsize=(14, 10))
    
    y = np.linspace(-1, 3, 200)
    f = y * (1 - y) * (y - 2)
    
    # 3D — solution curves over (t, y)
    ax = fig.add_subplot(221, projection='3d')
    t_vals = np.linspace(0, 5, 80)
    T, Y0 = np.meshgrid(t_vals, np.linspace(-0.5, 2.5, 30))
    
    from scipy.integrate import solve_ivp
    
    def ode_sys(t, y):
        return y * (1 - y) * (y - 2)
    
    for y0 in [-0.3, 0.3, 0.7, 1.3, 1.7, 2.3]:
        sol = solve_ivp(ode_sys, [0, 5], [y0], method='RK45', max_step=0.05, dense_output=True)
        t_sol = sol.t
        y_sol = sol.y[0]
        ax.plot(t_sol, y_sol, zs=y0, zdir='y', lw=1.5)
    
    ax.set_xlabel('Time t'); ax.set_ylabel('y₀'); ax.set_zlabel('y(t)')
    ax.set_title('3D: Solution Curves', fontsize=10)
    ax.view_init(25, -60)
    
    # 2D — phase line
    ax2 = fig.add_subplot(222)
    ax2.plot(y, f, 'b-', lw=2)
    ax2.axhline(0, color='gray', lw=0.5)
    ax2.axvline(0, color='gray', lw=0.5)
    # Mark equilibria (y=0 and y=2 are stable sinks; y=1 is an unstable source)
    for ye, color, label in [(0, 'green', 'Stable'), (1, 'red', 'Unstable'), (2, 'green', 'Stable')]:
        ax2.scatter(ye, 0, color=color, s=100, zorder=5, label=label if ye==0 else '')
    ax2.set_xlabel('y'); ax2.set_ylabel("f(y) = y'")
    ax2.set_title("Phase Line: f(y) = y(1-y)(y-2)")
    ax2.legend(fontsize=8)
    ax2.grid(True, alpha=0.3)
    
    # 1D vertical phase line with arrows
    ax3 = fig.add_subplot(223)
    ax3.set_ylim(-0.5, 2.5)
    ax3.set_xlim(-1, 1)
    
    # Draw vertical line
    ax3.plot([0, 0], [-0.3, 2.3], 'k-', lw=2)
    
# Equilibria (green = stable, red = unstable)
    ax3.scatter(0, 0, color='green', s=150, marker='o', zorder=5)
    ax3.scatter(0, 1, color='red', s=150, marker='o', zorder=5)
    ax3.scatter(0, 2, color='green', s=150, marker='o', zorder=5)

    ax3.text(0.15, 0, 'Stable', fontsize=9, color='green', va='center')
    ax3.text(0.15, 1, 'Unstable', fontsize=9, color='red', va='center')
    ax3.text(0.15, 2, 'Stable', fontsize=9, color='green', va='center')

    # Arrows on phase line (direction of motion: toward the stable sinks)
    # y<0: f>0, y increases toward 0
    ax3.annotate('', xy=(0, -0.05), xytext=(0, -0.3),
                 arrowprops=dict(arrowstyle='->', color='green', lw=2))
    # 0<y<1: f<0, y decreases toward 0
    ax3.annotate('', xy=(0, 0.05), xytext=(0, 0.95),
                 arrowprops=dict(arrowstyle='->', color='green', lw=2))
    # 1<y<2: f>0, y increases toward 2 (away from unstable 1)
    ax3.annotate('', xy=(0, 1.95), xytext=(0, 1.05),
                 arrowprops=dict(arrowstyle='->', color='red', lw=2))
    # y>2: f<0, y decreases toward 2
    ax3.annotate('', xy=(0, 2.05), xytext=(0, 2.3),
                 arrowprops=dict(arrowstyle='->', color='green', lw=2))
    
    ax3.set_title('Phase Line Diagram')
    ax3.axis('off')
    
    # 1D — time traces
    ax4 = fig.add_subplot(224)
    t_dense = np.linspace(0, 5, 200)
    for y0, color in zip([-0.3, 0.3, 0.7, 1.3, 1.7, 2.3], 
                         ['red', 'orange', 'green', 'cyan', 'blue', 'purple']):
        sol = solve_ivp(ode_sys, [0, 5], [y0], method='RK45', max_step=0.05, dense_output=True)
        ax4.plot(sol.t, sol.y[0], color=color, lw=1.5, label=f'y₀={y0}')
    ax4.axhline(0, color='gray', ls=':', lw=0.5)
    ax4.axhline(1, color='gray', ls=':', lw=0.5)
    ax4.axhline(2, color='gray', ls=':', lw=0.5)
    ax4.set_xlim(0, 5); ax4.set_ylim(-0.5, 2.5)
    ax4.set_xlabel('Time t'); ax4.set_ylabel('y(t)')
    ax4.set_title('Time Traces')
    ax4.legend(fontsize=7, ncol=2)
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'{OUT_DIR}/phase-line.png', dpi=DPI)
    plt.close()
    print('  ✓ phase-line.png')


def rl_circuit():
    """19A-5: RL circuit current approaching steady state"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), gridspec_kw={'width_ratios': [1.4, 1]})

    # Left: current vs time
    R, L, E = 2.0, 1.0, 10.0
    t = np.linspace(0, 3, 400)
    iss = E / R
    tau = L / R
    i = iss * (1 - np.exp(-R / L * t))
    ax1.plot(t, i, 'b-', lw=2.5, label=r'$i(t)=\frac{E}{R}\left(1-e^{-(R/L)t}\right)$')
    ax1.axhline(iss, color='green', ls='--', lw=1.5, label=r'steady state $E/R=5$ A')
    ax1.axvline(tau, color='red', ls=':', lw=1.5)
    ax1.plot(tau, iss * (1 - np.exp(-1)), 'ro', ms=7, zorder=5)
    ax1.annotate(r'$\tau=L/R=0.5$ s', (tau, 0.2), xytext=(0.95, 1.2),
                 fontsize=12, color='red', fontweight='bold',
                 arrowprops=dict(arrowstyle='->', color='red'))
    ax1.annotate(r'$63.2\%$ of $E/R$', (tau, iss * (1 - np.exp(-1))), xytext=(0.95, 3.7),
                 fontsize=12, arrowprops=dict(arrowstyle='->'))
    ax1.set_xlabel('Time t (s)', fontsize=13); ax1.set_ylabel('Current i (A)', fontsize=13)
    ax1.set_title('Current Rises to $E/R$', fontsize=14, fontweight='bold')
    ax1.set_ylim(0, 6); ax1.legend(fontsize=10, loc='lower right'); ax1.grid(True, alpha=0.3)

    # Right: circuit schematic (loop of battery, resistor, inductor)
    ax2.set_xlim(0, 10); ax2.set_ylim(0, 6); ax2.set_aspect('equal'); ax2.axis('off')
    ax2.plot([2, 9], [1, 1], 'k-', lw=2.5); ax2.plot([9, 9], [1, 5], 'k-', lw=2.5)
    ax2.plot([9, 2], [5, 5], 'k-', lw=2.5); ax2.plot([2, 2], [5, 1], 'k-', lw=2.5)
    # battery (left edge): two parallel plates
    ax2.plot([1.3, 2], [1.6, 1.6], 'k-', lw=2.5); ax2.plot([1.3, 2], [4.4, 4.4], 'k-', lw=2.5)
    ax2.plot([1.3, 1.3], [1.6, 4.4], 'k-', lw=1.5)
    ax2.text(0.5, 3.0, r'$E$', fontsize=16, rotation=90, ha='center', va='center')
    # resistor (top edge): zigzag
    xr = np.array([2, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0])
    yr = np.array([5, 5.7, 4.3, 5.7, 4.3, 5.7, 4.3, 5.7, 4.3, 5.7, 4.3, 5.7, 4.3, 5.7, 5.0])
    ax2.plot(xr, yr, 'k-', lw=2.5)
    ax2.text(5.5, 6.25, r'$R$', fontsize=16, ha='center')
    # inductor (right edge): coils
    ax2.plot([9, 9], [1.0, 1.4], 'k-', lw=2.5); ax2.plot([9, 9], [4.6, 5.0], 'k-', lw=2.5)
    for yy in np.linspace(1.5, 4.5, 4):
        arc = np.linspace(0, np.pi, 30)
        ax2.plot(9 + 0.35 * np.cos(arc), yy + 0.35 * np.sin(arc) + 0.18, 'k-', lw=2.5)
    ax2.text(10.0, 3.0, r'$L$', fontsize=16, va='center')
    ax2.text(5.5, 0.35, r'$L\frac{di}{dt}+Ri=E$', fontsize=14, ha='center')
    ax2.set_title('RL Circuit', fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.savefig(f'{OUT_DIR}/rl-circuit.png', dpi=DPI)
    plt.close()
    print('  ✓ rl-circuit.png')


if __name__ == '__main__':
    slope_field()
    growth_decay()
    logistic()
    phase_line()
    rl_circuit()
