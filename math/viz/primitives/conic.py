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