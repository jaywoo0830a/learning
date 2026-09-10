"""Conic-section primitives: circles, ellipses, and generic parametric curves.

Built on the shared palette. Each returns the Line2D artist and guarantees the
correct geometric sampling (points lie exactly on the conic).
"""
from __future__ import annotations

import numpy as np

from ..theme import PALETTE


def plot_circle_c(ax, cx: float, cy: float, r: float, *, color: str = "blue",
                  lw=2.5, n=300, label=None):
    """Draw a circle centered at ``(cx, cy)`` with radius ``r``."""
    theta = np.linspace(0, 2 * np.pi, n)
    xs = cx + r * np.cos(theta)
    ys = cy + r * np.sin(theta)
    c = PALETTE.get(color, color)
    (line,) = ax.plot(xs, ys, color=c, lw=lw, label=label)
    return line


def plot_ellipse_c(ax, cx: float, cy: float, a: float, b: float, *,
                   color: str = "blue", lw=2.5, n=300, label=None):
    """Draw an axis-aligned ellipse: ((x-cx)/a)^2 + ((y-cy)/b)^2 = 1."""
    theta = np.linspace(0, 2 * np.pi, n)
    xs = cx + a * np.cos(theta)
    ys = cy + b * np.sin(theta)
    c = PALETTE.get(color, color)
    (line,) = ax.plot(xs, ys, color=c, lw=lw, label=label)
    return line


def plot_param2d(ax, t, x, y, *, color: str = "blue", lw=2.5, label=None):
    """Plot a parametric curve (x(t), y(t)). Assumes ``t,x,y`` same length."""
    c = PALETTE.get(color, color)
    (line,) = ax.plot(x, y, color=c, lw=lw, label=label)
    return line


def plot_parabola_v(ax, xs, a, h=0.0, k=0.0, *, color="blue", lw=2.5, label=None):
    """Vertical parabola y = a(x-h)^2 + k."""
    c = PALETTE.get(color, color)
    (line,) = ax.plot(xs, a * (xs - h) ** 2 + k, color=c, lw=lw, label=label)
    return line


def plot_hyperbola_branches(ax, a, b, *, xmax=8, color="blue", lw=2.5, n=200):
    """Draw the two branches of x^2/a^2 - y^2/b^2 = 1."""
    c = PALETTE.get(color, color)
    xr = np.linspace(a, xmax, n)
    yr = b * np.sqrt((xr / a) ** 2 - 1)
    xl = np.linspace(-xmax, -a, n)
    yl = b * np.sqrt((xl / a) ** 2 - 1)
    lines = []
    for X, Y in ((xr, yr), (xr, -yr), (xl, yl), (xl, -yl)):
        (line,) = ax.plot(X, Y, color=c, lw=lw)
        lines.append(line)
    return lines


def plot_asymptotes(ax, a, b, *, xmax=8, color="orange", lw=1.5, n=100):
    """Draw the asymptotes y=+-(b/a)x for a hyperbola."""
    c = PALETTE.get(color, color)
    xa = np.linspace(-xmax, xmax, n)
    (l1,) = ax.plot(xa, b / a * xa, color=c, ls="--", lw=lw)
    (l2,) = ax.plot(xa, -b / a * xa, color=c, ls="--", lw=lw)
    return [l1, l2]