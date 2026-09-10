"""Coordinate-graph helpers consolidated into the VIZ core.

Used by session graph builders so common 2D setups (origin axes + grid +
limits + aspect) and the save-to-canonical-path idiom live in one place.
"""
from __future__ import annotations

from .primitives import grid
from .export import save_figure, graph_path


def coords_ax(ax, *, xlo=-5, xhi=5, ylo=-5, yhi=5, aspect="equal", grid_alpha=0.3):
    """Configure a 2D coordinate axes: origin lines, light grid, limits, aspect."""
    grid.origin_axes(ax, grid_alpha=grid_alpha)
    grid.set_limits(ax, xlo, xhi, ylo, yhi)
    if aspect:
        ax.set_aspect(aspect)
    return ax


def build_and_save(fig, session, num, slug):
    """Save ``fig`` to the canonical graphs/<session>/<num>-<slug>.png and return (fig, path)."""
    path = graph_path(session, num, slug)
    save_figure(fig, path)
    return fig, path