"""Curve primitives: parametric / x-y curves, tangent segments, and points.

Wrappers around matplotlib so every session uses the same conventions for
line style, tangent construction, and point markers — preventing the per-script
drift that caused misaligned labels and overlapping artists.
"""
from __future__ import annotations

from typing import Optional

import numpy as np

from ..theme import PALETTE


def plot_curve(
    ax,
    x,
    y,
    *,
    label: Optional[str] = None,
    color: str = "blue",
    lw: float = 2.5,
    ls: str = "-",
):
    """Plot an x-y curve and return the Line2D artist."""
    c = PALETTE.get(color, color)
    (line,) = ax.plot(x, y, color=c, lw=lw, ls=ls, label=label)
    if label:
        ax.legend()
    return line


def plot_tangent(ax, x0, y0, m, *, half: float = 1.0, color: str = "red", ls: str = "--", lw: float = 2.2, label: Optional[str] = None):
    """Draw a tangent segment centered on the point ``(x0, y0)`` with slope ``m``.

    The segment spans ``x in [x0 - half, x0 + half]`` along ``y = y0 + m(x - x0)``.
    Returns the Line2D artist.
    """
    xs = np.array([x0 - half, x0 + half])
    ys = y0 + m * (xs - x0)
    (line,) = ax.plot(xs, ys, color=PALETTE.get(color, color), lw=lw, ls=ls,
                      label=label)
    if label:
        ax.legend()
    return line


def plot_point(ax, x, y, *, color: str = "red", ms: float = 8, zorder: float = 6):
    """Place a single highlighted point at ``(x, y)`` via scatter.

    Returns the PathCollection so tests / callers can inspect offsets.
    """
    c = PALETTE.get(color, color)
    return ax.scatter([x], [y], color=c, s=ms**2, zorder=zorder)