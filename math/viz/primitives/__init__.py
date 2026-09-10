"""Reusable visual primitives that compose into session graphs.

Each primitive is a thin, consistent wrapper around matplotlib artists:
- curve: parametric / x-y curves, tangent segments, and points.
- annotate: called-out labels with arrows.
- shapes: shaded regions, filled circles, ring (annulus) patches.
- threed: 3D sphere shells.
(Schematics and vector-field primitives come next.)
"""
from .curve import plot_curve, plot_tangent, plot_point
from .annotate import add_callout
from .shapes import plot_region, plot_circle, plot_ring
from .threed import plot_shell_3d
from .grid import origin_axes, set_limits, xaxis, yaxis, light_grid, equal_aspect
from .conic import plot_circle_c, plot_ellipse_c, plot_param2d
from . import threed3 as d3

__all__ = [
    "plot_curve", "plot_tangent", "plot_point", "add_callout",
    "plot_region", "plot_circle", "plot_ring", "plot_shell_3d",
    "origin_axes", "set_limits", "xaxis", "yaxis", "light_grid", "equal_aspect",
    "plot_circle_c", "plot_ellipse_c", "plot_param2d", "d3",
]