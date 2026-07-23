#!/usr/bin/env python3
"""Generate all graphs for Session 19E — Linear Systems & Phase Portraits."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

DPI = 150
OUT_DIR = '19E'

def harmonic_oscillator_state_space():
    """19E-1: Harmonic oscillator state space"""
    fig = plt.figure(figsize=(14, 4))
    
    t = np.linspace(0, 4*np.pi, 300)
    x = np.cos(t)
    x_dot = -np.sin(t)
    
    # 3D — (t, x, x')
    ax = fig.add_subplot(131, projection='3d')
    ax.plot(t, x, x_dot, 'b-', lw=2)
    ax.set_xlabel('Time t'); ax.set_ylabel('x'); ax.set_zlabel("x'")
    ax.set_title('3D: State Space (t, x, x\')', fontsize=10)
    ax.view_init(25, -70)
    
    # 2D — phase portrait (x, x') ellipse
    ax2 = fig.add_subplot(132)
    ax2.plot(x, x_dot, 'b-', lw=2)
    ax2.scatter([0], [0], color='black', s=50)
    # Arrows showing direction
    for theta in np.linspace(0, 2*np.pi-0.5, 8):
        xp = np.cos(theta)
        yp = -np.sin(theta)
        dx = -np.sin(theta) * 0.2
        dy = -np.cos(theta) * 0.2
        ax2.arrow(xp, yp, dx, dy, head_width=0.1, head_length=0.08, 
                  fc='blue', ec='blue', alpha=0.5)
    ax2.set_xlim(-1.5, 1.5); ax2.set_ylim(-1.5, 1.5)
    ax2.set_xlabel('x (position)'); ax2.set_ylabel("x' (velocity)")
    ax2.set_title('2D: Phase Portrait — Center')
    ax2.set_aspect('equal')
    ax2.grid(True, alpha=0.3)
    
    # 1D — time trace
    ax3 = fig.add_subplot(133)
    ax3.plot(t, x, 'b-', lw=2, label='x(t)')
    ax3.plot(t, x_dot, 'r--', lw=1.5, alpha=0.7, label="x'(t)")
    ax3.set_xlim(0, 4*np.pi)
    ax3.set_xlabel('Time t'); ax3.set_ylabel('Amplitude')
    ax3.set_title('1D: Time Traces')
    ax3.legend(fontsize=8)
    ax3.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'{OUT_DIR}/harmonic-oscillator-state-space.png', dpi=DPI)
    plt.close()
    print('  ✓ harmonic-oscillator-state-space.png')

def center_phase_portrait():
    """19E-2: Center — pure oscillation in phase space (same as harmonic but different view)"""
    fig = plt.figure(figsize=(14, 10))
    
    t = np.linspace(0, 8*np.pi, 400)
    x = np.cos(t)
    x_dot = -np.sin(t)
    
    # 3D — helical trajectory
    ax = fig.add_subplot(221, projection='3d')
    ax.plot(t, x, x_dot, 'b-', lw=1.5)
    # Projection on (x, x') plane
    ax.plot(np.zeros_like(t), x, x_dot, 'gray', lw=0.5, alpha=0.3)
    ax.set_xlabel('Time t'); ax.set_ylabel('x'); ax.set_zlabel("x'")
    ax.set_title('3D: Helix in State Space', fontsize=10)
    ax.view_init(20, -80)
    
    # 2D — multiple trajectories (different energies)
    ax2 = fig.add_subplot(222)
    for A in [0.5, 1, 1.5, 2]:
        theta = np.linspace(0, 2*np.pi, 200)
        ax2.plot(A*np.cos(theta), -A*np.sin(theta), lw=1.5, label=f'A={A}')
    ax2.set_xlim(-2.5, 2.5); ax2.set_ylim(-2.5, 2.5)
    ax2.set_xlabel('x'); ax2.set_ylabel("x'")
    ax2.set_title('2D: Concentric Ellipses (Conserved Energy)')
    ax2.set_aspect('equal')
    ax2.legend(fontsize=8)
    ax2.grid(True, alpha=0.3)
    
    # 1D — cosine with phase shifts
    ax3 = fig.add_subplot(223)
    for phi in [0, np.pi/4, np.pi/2, np.pi]:
        ax3.plot(t, np.cos(t + phi), lw=1.5, label=f'φ={phi:.2f}')
    ax3.set_xlim(0, 4*np.pi)
    ax3.set_xlabel('Time t'); ax3.set_ylabel('x(t)')
    ax3.set_title('1D: Phase-Shifted Oscillations')
    ax3.legend(fontsize=8)
    ax3.grid(True, alpha=0.3)
    
    # 1D — energy conservation
    ax4 = fig.add_subplot(224)
    E = 0.5*x**2 + 0.5*x_dot**2  # Total energy
    ax4.plot(t, E, 'g-', lw=2)
    ax4.set_xlim(0, 4*np.pi); ax4.set_ylim(0, 2)
    ax4.set_xlabel('Time t'); ax4.set_ylabel('Energy E')
    ax4.set_title('Energy Conservation')
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'{OUT_DIR}/center-phase-portrait.png', dpi=DPI)
    plt.close()
    print('  ✓ center-phase-portrait.png')

def phase_portrait_zoo():
    """19E-3: All six canonical phase portraits"""
    fig = plt.figure(figsize=(14, 10))
    
    systems = [
        ([[2, 0], [0, -1]], 'Saddle', 0),
        ([[-1, 0], [0, -3]], 'Stable Node', 1),
        ([[1, 0], [0, 3]], 'Unstable Node', 2),
        ([[-0.5, -2], [2, -0.5]], 'Stable Spiral', 3),
        ([[0.5, -2], [2, 0.5]], 'Unstable Spiral', 4),
        ([[0, -2], [2, 0]], 'Center', 5),
    ]
    
    def plot_system(ax, A, title):
        eigvals = np.linalg.eigvals(A)
        x = np.linspace(-2, 2, 12)
        y = np.linspace(-2, 2, 12)
        X, Y = np.meshgrid(x, y)
        U = A[0][0]*X + A[0][1]*Y
        V = A[1][0]*X + A[1][1]*Y
        M = np.sqrt(U**2 + V**2)
        ax.quiver(X, Y, U/M, V/M, M, alpha=0.5, cmap='viridis', width=0.005)
        
        # Sample trajectories
        from scipy.integrate import solve_ivp
        def lin_sys(t, z):
            return [A[0][0]*z[0]+A[0][1]*z[1], A[1][0]*z[0]+A[1][1]*z[1]]
        
        for start in [[1, 0], [0, 1], [-1, 0], [0, -1], [1.5, 1.5], [-1.5, -1.5]]:
            t_span = [0, 3] if all(np.linalg.eigvals(A).real <= 0) else [0, -3]
            try:
                sol = solve_ivp(lin_sys, t_span, start, method='RK45', max_step=0.05)
                ax.plot(sol.y[0], sol.y[1], 'b-', lw=1, alpha=0.6)
            except:
                pass
        
        ax.set_xlim(-2.5, 2.5); ax.set_ylim(-2.5, 2.5)
        ax.set_title(f'{title}\nλ={eigvals[0]:.2f}, {eigvals[1]:.2f}', fontsize=9)
        ax.set_aspect('equal')
        ax.axhline(0, color='gray', lw=0.5)
        ax.axvline(0, color='gray', lw=0.5)
    
    for idx, (A, name, pos) in enumerate(systems):
        ax = fig.add_subplot(2, 3, pos+1)
        plot_system(ax, A, name)
    
    plt.tight_layout()
    plt.savefig(f'{OUT_DIR}/phase-portrait-zoo.png', dpi=DPI)
    plt.close()
    print('  ✓ phase-portrait-zoo.png')

def pendulum_phase_portrait():
    """19E-4: Pendulum phase portrait — center and saddle"""
    fig = plt.figure(figsize=(14, 10))
    
    gL = 1.0  # g/L
    
    # 3D — energy surface
    ax = fig.add_subplot(221, projection='3d')
    theta = np.linspace(-np.pi, np.pi, 50)
    theta_dot = np.linspace(-3, 3, 50)
    TH, TD = np.meshgrid(theta, theta_dot)
    E = 0.5*TD**2 - gL*np.cos(TH)
    E[E > 5] = np.nan
    surf = ax.plot_surface(TH, TD, E, cmap='viridis', alpha=0.9,
                           shade=True, antialiased=True, edgecolor='none')
    ax.set_xlabel('θ'); ax.set_ylabel("θ'"); ax.set_zlabel('Energy E')
    ax.set_title('3D: Energy Surface E = ½θ\'² - cosθ', fontsize=10)
    ax.view_init(25, -60)
    
    # 2D — phase portrait
    ax2 = fig.add_subplot(222)
    Theta = np.linspace(-np.pi, np.pi, 15)
    Tdot = np.linspace(-3, 3, 15)
    Th, Td = np.meshgrid(Theta, Tdot)
    U = Td
    V = -gL * np.sin(Th)
    M = np.sqrt(U**2 + V**2)
    M[M == 0] = 1  # avoid division by zero
    ax2.quiver(Th, Td, U/M, V/M, M, alpha=0.5, cmap='viridis', width=0.005)
    
    from scipy.integrate import solve_ivp
    def pend_sys(t, z):
        return [z[1], -gL*np.sin(z[0])]
    
    # Sample trajectories
    for start in [[0.5, 0], [1.5, 0], [2.5, 0], [0, 1.5], [0, -1.5], [np.pi-0.3, 0]]:
        try:
            sol = solve_ivp(pend_sys, [0, 20], start, method='RK45', max_step=0.05)
            ax2.plot(sol.y[0], sol.y[1], 'b-', lw=1, alpha=0.6)
        except:
            pass
    
    ax2.scatter([0, 2*np.pi, -2*np.pi], [0, 0, 0], color='green', s=80, zorder=5)
    ax2.scatter([np.pi, -np.pi], [0, 0], color='red', s=80, zorder=5)
    ax2.set_xlim(-np.pi, np.pi); ax2.set_ylim(-3, 3)
    ax2.set_xlabel('θ'); ax2.set_ylabel("θ'")
    ax2.set_title('2D: Phase Portrait — Centers + Saddles')
    ax2.set_aspect('equal')
    ax2.grid(True, alpha=0.3)
    
    # 1D — potential energy
    ax3 = fig.add_subplot(223)
    th = np.linspace(-np.pi, np.pi, 200)
    U_pot = -gL*np.cos(th)
    ax3.plot(th, U_pot, 'b-', lw=2)
    ax3.scatter([0], [-1], color='green', s=80, zorder=5, label='Stable (minimum)')
    ax3.scatter([np.pi, -np.pi], [1, 1], color='red', s=80, zorder=5, label='Unstable (maximum)')
    ax3.set_xlim(-np.pi, np.pi)
    ax3.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
    ax3.set_xticklabels(['-π', '-π/2', '0', 'π/2', 'π'])
    ax3.set_xlabel('θ'); ax3.set_ylabel('U(θ) = -cosθ')
    ax3.set_title('1D: Potential Energy')
    ax3.legend(fontsize=8)
    ax3.grid(True, alpha=0.3)
    
    # 1D — time traces for small and large angles
    ax4 = fig.add_subplot(224)
    t_dense = np.linspace(0, 20, 200)
    for start, color, label in [([0.5, 0], 'green', 'Small θ₀=0.5'), 
                                 ([2.0, 0], 'blue', 'Large θ₀=2.0'),
                                 ([np.pi-0.1, 0], 'red', 'Near saddle')]:
        sol = solve_ivp(pend_sys, [0, 20], start, method='RK45', max_step=0.05, dense_output=True)
        ax4.plot(sol.t, sol.y[0], color=color, lw=1.5, label=label)
    
    ax4.set_xlim(0, 20)
    ax4.set_xlabel('Time t'); ax4.set_ylabel('θ(t)')
    ax4.set_title('1D: Pendulum Time Traces')
    ax4.legend(fontsize=8)
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'{OUT_DIR}/pendulum-phase-portrait.png', dpi=DPI)
    plt.close()
    print('  ✓ pendulum-phase-portrait.png')

if __name__ == '__main__':
    harmonic_oscillator_state_space()
    center_phase_portrait()
    phase_portrait_zoo()
    pendulum_phase_portrait()
