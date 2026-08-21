"""
Generate setup diagrams for the accounting-model worked examples.

Input : none (diagrams are drawn from the problem numbers)
Output: PNG files in physics/problems/mechanics/visual/graphs/

    work-1-lift.png      .. work-7-spring.png     (work/examples.md)
    energy-1-toss.png    .. energy-7-crate.png    (energy/examples.md)

Style : schematic physics setup diagrams, matplotlib mathtext (no LaTeX).
Run   : python3 generate_examples.py   (re-runnable, overwrites images)
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "graphs")
os.makedirs(OUT, exist_ok=True)

plt.rcParams.update({
    "figure.dpi": 150,
    "font.size": 11,
    "font.family": "DejaVu Sans",
})

C_BODY   = "#5b7db1"   # objects (blue-gray)
C_FORCE  = "#c0392b"   # force arrows (red)
C_MOTION = "#1e8449"   # velocity arrows (green)
C_LABEL  = "#2c3e50"   # annotation text (dark slate)
C_GROUND = "#8a6d3b"   # ground / Earth (brown)
C_WALL   = "#7f8c8d"   # wall / ceiling (gray)
C_RAMP   = "#e9dfc9"   # ramp fill


# ──────────────────────────────────────────────
# helpers
# ──────────────────────────────────────────────

def new_ax(w=4.6, h=4.2, title=None):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_aspect("equal")
    ax.axis("off")
    if title:
        ax.set_title(title, fontsize=12, fontweight="bold", pad=8)
    return fig, ax


def vec(ax, x, y, dx, dy, color, label=None, lx=0.10, ly=0.10, fs=10, lw=2.4):
    """Force / velocity arrow from (x, y) to (x+dx, y+dy), with optional label."""
    ax.annotate("", xy=(x + dx, y + dy), xytext=(x, y),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw))
    if label is not None:
        ax.text(x + dx * 0.55 + lx, y + dy * 0.55 + ly, label,
                color=color, fontsize=fs, ha="center", va="center")


def dim(ax, x1, y1, x2, y2, label, dx=0.0, dy=0.0, fs=10):
    """Double-arrowhead dimension line with centered label."""
    ax.plot([x1, x2], [y1, y2], color=C_LABEL, lw=1.0, ls="--")
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=C_LABEL, lw=1.0))
    ax.annotate("", xy=(x1, y1), xytext=(x2, y2),
                arrowprops=dict(arrowstyle="-|>", color=C_LABEL, lw=1.0))
    ax.text((x1 + x2) / 2 + dx, (y1 + y2) / 2 + dy, label,
            color=C_LABEL, fontsize=fs, ha="center", va="center")


def ground(ax, x0, x1, y=0.0, color=C_GROUND):
    """Ground line with hatch marks."""
    ax.plot([x0, x1], [y, y], color=color, lw=2.5)
    n = max(int((x1 - x0) / 0.45), 2)
    for i in range(n + 1):
        x = x0 + (x1 - x0) * i / n
        ax.plot([x, x - 0.16], [y, y - 0.14], color=color, lw=1.2)


def spring(ax, x1, x2, y0, coils=8, amp=0.16, color=C_LABEL, lw=2.0):
    """Horizontal zig-zag spring from x1 to x2 around y0."""
    tt = np.linspace(0, coils * np.pi, 2 * coils + 1)
    xx = np.linspace(x1, x2, len(tt))
    yy = y0 + amp * np.sin(tt)
    ax.plot(xx, yy, color=color, lw=lw)


def block(ax, cx, cy, w=1.3, h=0.9, angle=0.0, label=None, dashed=False, fs=10):
    """Rectangle block centered at (cx, cy), optionally rotated by angle (rad)."""
    corners = np.array([[-w / 2, -h / 2], [w / 2, -h / 2], [w / 2, h / 2], [-w / 2, h / 2]])
    if angle:
        Rm = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        corners = corners @ Rm.T
    pts = corners + np.array([cx, cy])
    ax.add_patch(Polygon(pts, closed=True,
                         facecolor="none" if dashed else C_BODY,
                         edgecolor=C_LABEL, lw=1.4, ls="--" if dashed else "-"))
    if label:
        ax.text(cx, cy, label, ha="center", va="center",
                fontsize=fs, color=C_LABEL if dashed else "white")


def save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("saved", path)


# ═══════════════════════════════════════════════
# WORK figures
# ═══════════════════════════════════════════════

def work1_lift():
    fig, ax = new_ax(4.6, 4.8, "Example 1 — The First Wire")
    ax.add_patch(Rectangle((-1.9, 4.05), 3.8, 0.32, facecolor=C_WALL, edgecolor="none"))
    ax.plot([0, 0], [2.65, 4.05], color=C_LABEL, lw=2.0)          # cable
    y0 = 1.55
    block(ax, 0, y0 + 0.45, w=1.3, h=0.9, label="5.0 kg")          # initial
    block(ax, 0, y0 + 0.45 + 1.5, w=1.3, h=0.9, dashed=True)       # final
    vec(ax, 0, y0 + 1.15, 0, 0.85, C_FORCE, r"$T$", lx=0.13)
    vec(ax, 0, y0 + 0.65, 0, -0.8, C_FORCE, r"$mg$", lx=0.13)
    ax.annotate("", xy=(1.7, y0 + 2.0), xytext=(1.7, y0 + 0.45),
                arrowprops=dict(arrowstyle="-|>", color=C_MOTION, lw=2.2))
    ax.text(2.05, y0 + 1.2, "constant\nspeed", color=C_MOTION, fontsize=9, ha="center")
    dim(ax, -1.35, y0 + 0.45, -1.35, y0 + 1.95, r"$d = 2.0$ m", dx=-0.32)
    ground(ax, -2.1, 2.1, y=-0.35)
    ax.text(0, -0.8, "Earth (inside the system)", color=C_GROUND, fontsize=10, ha="center")
    save(fig, "work-1-lift.png")


def work2_lift_accel():
    fig, ax = new_ax(4.6, 4.8, "Example 2 — The Accelerating Lift")
    ax.add_patch(Rectangle((-1.9, 4.05), 3.8, 0.32, facecolor=C_WALL, edgecolor="none"))
    ax.plot([0, 0], [2.65, 4.05], color=C_LABEL, lw=2.0)
    y0 = 1.55
    block(ax, 0, y0 + 0.45, w=1.3, h=0.9, label="5.0 kg")
    block(ax, 0, y0 + 0.45 + 1.5, w=1.3, h=0.9, dashed=True)
    vec(ax, 0, y0 + 1.25, 0, 0.9, C_FORCE, r"$T$", lx=0.13)
    vec(ax, 0, y0 + 0.6, 0, -0.8, C_FORCE, r"$mg$", lx=0.13)
    vec(ax, 0.85, y0 + 2.5, 0, 1.0, C_MOTION, r"$v_f = 3.0$ m/s", lx=0.0, ly=0.18, fs=9)
    ax.text(0.3, y0 + 0.45, "rest", fontsize=9, color=C_LABEL, ha="left", va="bottom")
    dim(ax, -1.35, y0 + 0.45, -1.35, y0 + 1.95, r"$d = 2.0$ m", dx=-0.32)
    ground(ax, -2.1, 2.1, y=-0.35)
    ax.text(0, -0.8, "Earth (inside the system)", color=C_GROUND, fontsize=10, ha="center")
    save(fig, "work-2-lift-accelerating.png")


def work3_fall():
    fig, ax = new_ax(4.2, 5.2, "Example 3 — The Falling Ball")
    x = 0.0
    top, bot = 4.7, 0.35
    ax.plot([x, x], [bot, top], color=C_LABEL, lw=1.1, ls="--")
    ax.add_patch(Circle((x, top), 0.2, facecolor=C_BODY, edgecolor=C_LABEL, lw=1.5))
    ax.add_patch(Circle((x, bot), 0.2, facecolor=C_BODY, edgecolor=C_LABEL, lw=1.5))
    ax.text(-1.05, top, "start: $v = 0$\nDeposit $= 200$ J", fontsize=9, va="center", ha="right")
    ax.text(-1.05, bot, "ground: Cash $= 200$ J\n$v = 20$ m/s", fontsize=9, va="center", ha="right")
    ax.annotate("", xy=(x + 0.45, bot + 0.6), xytext=(x + 0.45, top - 0.4),
                arrowprops=dict(arrowstyle="-|>", color=C_MOTION, lw=2.2))
    ax.text(x + 0.78, (top + bot) / 2, "falls", color=C_MOTION, fontsize=9, va="center", ha="left")
    dim(ax, 1.25, 0.0, 1.25, top, r"$h = 20$ m", dx=0.14)
    ground(ax, -1.35, 1.35, y=0.0)
    save(fig, "work-3-fall.png")


def _ramp(ax, x0, y0, th, L, label_deg, label_L, label_h, label_mu=None, mu_y=None):
    """Shared incline scaffold. Returns block-center helper info (dir, normal)."""
    x1, y1 = x0 + L * np.cos(th), y0 + L * np.sin(th)
    ax.add_patch(Polygon([(x0, y0), (x0 + L * np.cos(th), y0), (x1, y1)],
                         closed=True, facecolor=C_RAMP, edgecolor=C_LABEL, lw=1.5))
    ax.plot([x0, x1], [y0, y1], color=C_LABEL, lw=2.4)
    ground(ax, x0 - 0.5, x1 + 0.7, y=y0)
    ang = np.linspace(0, th, 20)
    r0 = 0.55
    ax.plot(x0 + r0 * np.cos(ang), y0 + r0 * np.sin(ang), color=C_LABEL, lw=1.2)
    ax.text(x0 + 0.82, y0 + 0.2, label_deg, fontsize=11, color=C_LABEL)
    ax.text((x0 + x1) / 2, y0 - 0.48, label_L, fontsize=10, color=C_LABEL, ha="center")
    dim(ax, x1 + 0.18, y0, x1 + 0.18, y1, label_h, dx=0.16)
    if label_mu is not None:
        ax.text(x0 + 0.15, y1 - 0.3, label_mu, fontsize=10, color=C_LABEL)
    return x1, y1


def work4_incline():
    fig, ax = new_ax(5.6, 3.6, "Example 4 — The Non-Refundable Fee")
    th = np.radians(30)
    L, s = 5.0, 2.5
    x0, y0 = -0.7, -0.25
    _ramp(ax, x0, y0, th, L, r"$30°$", r"$L = 5.0$ m", r"$h = 2.5$ m", r"$\mu_k = 0.30$")
    cx = x0 + s * np.cos(th)
    cy = y0 + s * np.sin(th)
    block(ax, cx, cy, w=0.75, h=0.75, angle=th, label="4.0 kg", fs=9)
    vec(ax, cx, cy, 0, -1.2, C_FORCE, r"$mg$", lx=0.15, ly=-0.06)
    nx, ny = -np.sin(th), np.cos(th)
    vec(ax, cx, cy, 1.1 * nx, 1.1 * ny, C_FORCE, r"$N$", lx=0.06, ly=0.12)
    vec(ax, cx, cy, 1.0 * np.cos(th), 1.0 * np.sin(th), C_FORCE, r"$f_k$", lx=0.08, ly=0.12)
    vec(ax, cx - 0.55 * np.cos(th), cy - 0.55 * np.sin(th), -0.75 * np.cos(th), -0.75 * np.sin(th),
        C_MOTION, r"$v$", lx=0.0, ly=0.16)
    save(fig, "work-4-incline.png")


def work5_sled():
    fig, ax = new_ax(5.6, 3.6, "Example 5 — The Towed Sled")
    th = np.radians(20)
    L, s = 4.0, 1.9
    x0, y0 = -0.7, -0.25
    x1, y1 = _ramp(ax, x0, y0, th, L, r"$20°$", r"$L = 4.0$ m", r"$h = 1.37$ m", r"$\mu_k = 0.25$")
    cx = x0 + s * np.cos(th)
    cy = y0 + s * np.sin(th)
    block(ax, cx, cy, w=1.35, h=0.5, angle=th, label="10 kg", fs=9)
    dx, dy = np.cos(th), np.sin(th)
    # rope from sled front edge, up-slope
    p0 = (cx + 0.68 * dx, cy + 0.68 * dy)
    p1 = (p0[0] + 1.55 * dx, p0[1] + 1.55 * dy)
    ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=C_LABEL, lw=2.0)
    vec(ax, p0[0] + 0.35 * dx, p0[1] + 0.35 * dy, 0.9 * dx, 0.9 * dy, C_FORCE, r"$T$", lx=0.0, ly=0.2)
    vec(ax, cx, cy, 0, -1.15, C_FORCE, r"$mg$", lx=0.15, ly=-0.06)
    nx, ny = -np.sin(th), np.cos(th)
    vec(ax, cx, cy, 1.05 * nx, 1.05 * ny, C_FORCE, r"$N$", lx=0.06, ly=0.12)
    vec(ax, cx, cy, -1.05 * dx, -1.05 * dy, C_FORCE, r"$f_k$", lx=0.02, ly=0.14)
    vec(ax, cx - 0.8 * dx, cy - 0.8 * dy, 0.6 * dx, 0.6 * dy, C_MOTION, r"$v$ const.", lx=0.0, ly=0.2, fs=9)
    save(fig, "work-5-sled.png")


def work6_jump():
    fig, ax = new_ax(6.0, 4.0, "Example 6 — The Jump")
    ground(ax, -2.7, 2.7, y=0.0)

    def person(x, head_y, hip_y, knee_x, knee_y, foot_x, foot_y, arm_up=False):
        ax.add_patch(Circle((x, head_y), 0.13, facecolor="white", edgecolor=C_LABEL, lw=1.6))
        ax.plot([x, x], [head_y - 0.14, hip_y], color=C_LABEL, lw=2.4)
        ax.plot([x, knee_x], [hip_y, knee_y], color=C_LABEL, lw=2.4)
        ax.plot([knee_x, foot_x], [knee_y, foot_y], color=C_LABEL, lw=2.4)
        if arm_up:
            ax.plot([x, x - 0.26], [head_y + 0.04, head_y + 0.4], color=C_LABEL, lw=2.4)
            ax.plot([x, x + 0.26], [head_y + 0.04, head_y + 0.4], color=C_LABEL, lw=2.4)
        else:
            ax.plot([x, x - 0.3], [head_y + 0.03, hip_y + 0.14], color=C_LABEL, lw=2.4)
            ax.plot([x, x + 0.2], [head_y + 0.03, hip_y + 0.12], color=C_LABEL, lw=2.4)

    x1, x2 = -1.35, 1.35
    person(x1, head_y=1.18, hip_y=0.62, knee_x=x1 + 0.32, knee_y=0.30, foot_x=x1 + 0.06, foot_y=0.02)
    person(x2, head_y=2.25, hip_y=1.38, knee_x=x2 + 0.06, knee_y=0.62, foot_x=x2 + 0.2, foot_y=0.02,
           arm_up=True)
    c1, c2 = 0.92, 1.32
    ax.plot([x1, x1 + 1.15], [c1, c1], color=C_LABEL, lw=0.9, ls="--")
    ax.plot([x2 - 1.15, x2], [c2, c2], color=C_LABEL, lw=0.9, ls="--")
    ax.plot(x1, c1, "o", color=C_LABEL, ms=7)
    ax.plot(x2, c2, "o", color=C_LABEL, ms=7)
    dim(ax, 2.05, c1, 2.05, c2, r"$\Delta y_{CM} = 0.40$ m", dx=0.2)
    vec(ax, x2, c2, 0, 0.75, C_MOTION, r"$v = 3.0$ m/s", lx=0.18)
    ax.text(x1, -0.5, "crouch (start)", fontsize=9, ha="center", color=C_LABEL)
    ax.text(x2, -0.5, "toe-off", fontsize=9, ha="center", color=C_LABEL)
    ax.text(0, -0.95, "the floor pushes up, but its point of contact never moves → zero work",
            fontsize=9, ha="center", color=C_GROUND)
    save(fig, "work-6-jump.png")


def work7_spring():
    fig, ax = new_ax(6.4, 3.0, "Example 7 — Filling the Spring Deposit")
    ax.add_patch(Rectangle((-3.5, -0.35), 0.4, 1.9, facecolor=C_WALL, edgecolor="none"))
    wall_x = -3.1
    xb = -1.5
    spring(ax, wall_x, xb, 0.6, coils=9, amp=0.17)
    block(ax, xb + 0.45, 0.6, w=0.9, h=0.9, label="2.0 kg", fs=9)
    vec(ax, xb + 1.9, 0.6, -0.65, 0, C_FORCE, r"$F_{hand}$", lx=0.0, ly=0.2)
    ax.plot([-3.5, 1.9], [-0.02, -0.02], color=C_LABEL, lw=2.0)
    ax.text(0.4, -0.55, "frictionless floor", fontsize=9, ha="center", color=C_LABEL)
    ax.plot([xb + 0.4, xb + 0.4], [-0.35, 1.15], color=C_LABEL, lw=1.0, ls="--")
    ax.text(xb + 0.4, 1.28, "natural\nlength", fontsize=8, ha="center", va="bottom", color=C_LABEL)
    dim(ax, xb, -0.85, xb + 0.4, -0.85, r"$x = 0.40$ m", dx=0.0, dy=0.0)
    ax.text((wall_x + xb) / 2, 1.15, r"$k = 500$ N/m", fontsize=9, ha="center", color=C_LABEL)
    ax.text(-3.3, 1.35, "wall:\ndoes no work", fontsize=8, ha="center", va="top", color=C_WALL)
    save(fig, "work-7-spring.png")


# ═══════════════════════════════════════════════
# ENERGY figures
# ═══════════════════════════════════════════════

def energy1_toss():
    fig, ax = new_ax(4.0, 5.6, "Example 1 — The Toss Ledger")
    x = 0.0
    top = 4.7
    ax.plot([x, x], [0.0, top], color=C_LABEL, lw=1.1, ls="--")
    ax.add_patch(Circle((x, 0.2), 0.17, facecolor=C_BODY, edgecolor=C_LABEL, lw=1.5))
    ax.add_patch(Circle((x, top), 0.17, facecolor=C_BODY, edgecolor=C_LABEL, lw=1.5))
    ax.add_patch(Circle((-0.13, 2.35), 0.14, facecolor="white", edgecolor=C_BODY, lw=1.2, ls="--"))
    ax.add_patch(Circle((0.13, 2.35), 0.14, facecolor="white", edgecolor=C_BODY, lw=1.2, ls="--"))
    ax.text(0.55, 0.2, "launch / catch\nCash $= 100$ J, $v = 20$ m/s", fontsize=9, va="center")
    ax.text(0.55, top, "top: $v = 0$\nDeposit $= 100$ J", fontsize=9, va="center")
    ax.text(-0.95, 2.35, "$h = 10$ m:\nCash 50 / Deposit 50", fontsize=9, va="center", ha="right")
    vec(ax, -0.13, 2.5, 0, 0.5, C_MOTION, r"14.1 m/s", lx=-0.42, ly=0.1, fs=8)
    vec(ax, 0.13, 2.2, 0, -0.5, C_MOTION, r"14.1 m/s", lx=0.42, ly=-0.12, fs=8)
    dim(ax, 1.15, 0.0, 1.15, top, r"$h_{top} = 20$ m", dx=0.16)
    ground(ax, -1.35, 1.35, y=0.0)
    save(fig, "energy-1-toss.png")


def energy2_pendulum():
    fig, ax = new_ax(4.8, 4.8, "Example 2 — The Pendulum")
    px, py = 0.0, 3.5
    L = 2.2
    th = np.radians(60)
    bx, by = px + L * np.sin(th), py - L * np.cos(th)
    ax.add_patch(Rectangle((-0.55, 3.66), 1.1, 0.26, facecolor=C_WALL, edgecolor="none"))
    ax.plot([px, px], [py - L - 0.3, py], color=C_LABEL, lw=1.0, ls="--")
    ax.plot([px, bx], [py, by], color=C_LABEL, lw=2.2)
    ax.add_patch(Circle((bx, by), 0.18, facecolor=C_BODY, edgecolor=C_LABEL, lw=1.5))
    ax.add_patch(Circle((px, py - L), 0.18, facecolor="white", edgecolor=C_BODY, lw=1.3, ls="--"))
    vec(ax, bx, by, -0.85 * np.sin(th), 0.85 * np.cos(th), C_FORCE, r"$T$", lx=0.12, ly=0.12)
    vec(ax, bx, by, 0, -0.85, C_FORCE, r"$mg$", lx=0.13, ly=-0.06)
    vec(ax, px + 0.55, py - L, 0.55, 0, C_MOTION, r"$v = \sqrt{20}$ m/s", lx=0.0, ly=0.2, fs=9)
    ang = np.linspace(-np.pi / 2, -np.pi / 2 + th, 30)
    r0 = 0.45
    ax.plot(px + r0 * np.cos(ang), py + r0 * np.sin(ang), color=C_LABEL, lw=1.2)
    ax.text(px + 0.68, py - 0.4, r"$60°$", fontsize=11, color=C_LABEL)
    ax.text((px + bx) / 2 + 0.14, (py + by) / 2, r"$L = 2.0$ m", fontsize=10, color=C_LABEL, ha="left")
    ax.plot([bx - 0.7, bx + 0.8], [by, by], color=C_LABEL, lw=0.9, ls="--")
    dim(ax, bx + 1.0, by, bx + 1.0, py - L, r"$h = 1.0$ m", dx=0.16)
    save(fig, "energy-2-pendulum.png")


def energy3_launcher():
    fig, ax = new_ax(4.4, 6.2, "Example 3 — The Spring Launcher")
    yb = 0.0
    ground(ax, -1.7, 1.7, y=yb)
    coils = 9
    tt = np.linspace(0, coils * np.pi, 2 * coils + 1)
    xx = 0.16 * np.sin(tt)
    yy = np.linspace(yb + 0.06, yb + 0.6, len(tt))
    ax.plot(xx, yy, color=C_LABEL, lw=2.0)
    ax.add_patch(Circle((0, yb + 0.78), 0.16, facecolor=C_BODY, edgecolor=C_LABEL, lw=1.5))
    y_nat = yb + 1.85
    ax.add_patch(Circle((0, y_nat), 0.16, facecolor="white", edgecolor=C_BODY, lw=1.3, ls="--"))
    y_top = yb + 5.1
    ax.add_patch(Circle((0, y_top), 0.16, facecolor="white", edgecolor=C_BODY, lw=1.3, ls="--"))
    vec(ax, 0.55, y_nat, 0, 0.55, C_MOTION, r"$v \approx 9.5$ m/s", lx=0.0, ly=0.16, fs=9)
    ax.text(0.6, y_top, "top: gravity Deposit\n$= 25$ J", fontsize=9, va="center")
    ax.text(0.6, yb + 0.35, "spring Deposit\n$= 25$ J", fontsize=9, va="center")
    dim(ax, 1.3, yb + 0.05, 1.3, y_nat, r"$0.50$ m", dx=0.16)
    dim(ax, 1.3, y_nat, 1.3, y_top, r"$4.5$ m", dx=0.16)
    ax.text(0.6, (yb + y_nat) / 2, "natural\nlength", fontsize=8, va="center", ha="left")
    save(fig, "energy-3-launcher.png")


def energy4_blocks():
    fig, ax = new_ax(6.6, 2.6, "Example 4 — Who Owns the Deposit?")
    ax.plot([-3.2, 3.2], [0.0, 0.0], color=C_LABEL, lw=2.2)
    ax.text(0, -0.5, "frictionless table", fontsize=9, ha="center", color=C_LABEL)
    xA, xB = -1.6, 0.7
    block(ax, xA + 0.45, 0.45, w=0.9, h=0.9, label="A\n2.0 kg", fs=9)
    block(ax, xB + 0.45, 0.45, w=0.9, h=0.9, label="B\n3.0 kg", fs=9)
    spring(ax, xA + 0.9, xB, 0.45, coils=7, amp=0.14)
    dim(ax, xA + 0.9, -0.8, xB, -0.8, r"$x = 0.50$ m", dx=0.0, dy=0.0)
    ax.text((xA + xB + 0.9) / 2, 1.28, r"$k = 600$ N/m", fontsize=9, ha="center", color=C_LABEL)
    vec(ax, xA + 0.2, 0.45, -0.85, 0, C_MOTION, r"$v_A$", lx=0.0, ly=0.2)
    vec(ax, xB + 0.7, 0.45, 0.85, 0, C_MOTION, r"$v_B$", lx=0.0, ly=0.2)
    save(fig, "energy-4-blocks.png")


def energy5_loop():
    fig, ax = new_ax(7.4, 4.4, "Example 5 — The Loop-the-Loop")
    R = 1.0
    cx, cy = -1.7, 1.0
    H = 2.5
    ground(ax, -6.9, 3.1, y=0.0)
    ax.plot([-6.3, -4.3], [H, 0.0], color=C_LABEL, lw=3.0)
    ax.plot([-4.3, cx - R], [0.0, 0.0], color=C_LABEL, lw=3.0)
    ax.add_patch(Circle((cx, cy), R, fill=False, ec=C_LABEL, lw=3.0))
    ax.plot([cx + R, 3.1], [0.0, 0.0], color=C_LABEL, lw=3.0)
    tx, ty = cx, cy + R
    ax.add_patch(Circle((tx, ty), 0.13, facecolor=C_BODY, edgecolor=C_LABEL, lw=1.4))
    vec(ax, tx + 0.12, ty, 0.55, 0, C_MOTION, r"$v$", lx=0.0, ly=0.2)
    vec(ax, tx - 0.42, ty, 0, -0.55, C_FORCE, r"$mg$", lx=0.13)
    ax.text(tx - 0.42, ty + 0.3, r"$N = 0$ (barely)", fontsize=9, color=C_LABEL, ha="left")
    dim(ax, -6.85, 0.0, -6.85, H, r"$H$", dx=0.15)
    dim(ax, cx + 0.4, cy, cx + 0.4, ty, r"$R = 5$ m", dx=0.15)
    ax.text(-6.3, H + 0.25, "cart starts\nfrom rest", fontsize=9, ha="center", color=C_LABEL)
    save(fig, "energy-5-loop.png")


def energy6_atwood():
    fig, ax = new_ax(4.6, 5.2, "Example 6 — The Atwood Machine")
    ax.add_patch(Rectangle((-1.2, 4.55), 2.4, 0.28, facecolor=C_WALL, edgecolor="none"))
    ax.plot([0, 0], [4.45, 4.55], color=C_LABEL, lw=2.0)
    ax.add_patch(Circle((0, 4.05), 0.4, facecolor="#b0b6b8", edgecolor=C_LABEL, lw=1.6))
    ax.text(1.05, 4.15, "massless,\nfrictionless pulley", fontsize=8, ha="left", va="center")
    ax.plot([-0.4, -0.4], [4.05, 1.25], color=C_LABEL, lw=1.8)
    ax.plot([0.4, 0.4], [4.05, 1.8], color=C_LABEL, lw=1.8)
    block(ax, -0.4, 0.85, w=0.9, h=0.8, label="3.0 kg", fs=9)
    block(ax, 0.4, 1.4, w=0.9, h=0.8, label="2.0 kg", fs=9)
    vec(ax, -0.4, 2.9, 0, 0.65, C_FORCE, r"$T$", lx=0.14)
    vec(ax, 0.4, 2.9, 0, 0.65, C_FORCE, r"$T$", lx=0.14)
    vec(ax, -0.4, 0.7, 0, -0.5, C_FORCE, r"$m_1g$", lx=0.15, ly=-0.04)
    vec(ax, 0.4, 1.25, 0, -0.5, C_FORCE, r"$m_2g$", lx=0.15, ly=-0.04)
    vec(ax, -1.3, 0.55, 0, -0.55, C_MOTION, r"$v$", lx=0.18)
    vec(ax, 1.2, 1.45, 0, 0.55, C_MOTION, r"$v$", lx=0.18)
    ax.text(0, -0.75, "released from rest; after $m_1$ falls $d = 1.0$ m", fontsize=9, ha="center", color=C_LABEL)
    save(fig, "energy-6-atwood.png")


def energy7_crate():
    fig, ax = new_ax(5.6, 3.6, "Example 7 — The Full Audit")
    th = np.radians(30)
    L, s = 5.0, 2.5
    x0, y0 = -0.7, -0.25
    _ramp(ax, x0, y0, th, L, r"$30°$", r"$L = 5.0$ m", r"$h = 2.5$ m", r"$\mu_k = 0.30$")
    cx = x0 + s * np.cos(th)
    cy = y0 + s * np.sin(th)
    block(ax, cx, cy, w=0.8, h=0.8, angle=th, label="4.0 kg", fs=9)
    dx, dy = np.cos(th), np.sin(th)
    vec(ax, cx, cy, 1.2 * dx, 1.2 * dy, C_FORCE, r"$F$", lx=0.02, ly=0.2)
    vec(ax, cx, cy, 0, -1.2, C_FORCE, r"$mg$", lx=0.15, ly=-0.06)
    nx, ny = -np.sin(th), np.cos(th)
    vec(ax, cx, cy, 1.05 * nx, 1.05 * ny, C_FORCE, r"$N$", lx=0.06, ly=0.12)
    vec(ax, cx, cy, -1.0 * dx, -1.0 * dy, C_FORCE, r"$f_k$", lx=0.02, ly=0.14)
    vec(ax, cx - 0.85 * dx, cy - 0.85 * dy, 0.6 * dx, 0.6 * dy, C_MOTION, r"$v$ const.", lx=0.0, ly=0.2, fs=9)
    save(fig, "energy-7-crate.png")


# ═══════════════════════════════════════════════

if __name__ == "__main__":
    work1_lift()
    work2_lift_accel()
    work3_fall()
    work4_incline()
    work5_sled()
    work6_jump()
    work7_spring()
    energy1_toss()
    energy2_pendulum()
    energy3_launcher()
    energy4_blocks()
    energy5_loop()
    energy6_atwood()
    energy7_crate()
    print("done")
