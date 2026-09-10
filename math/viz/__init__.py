"""Shared rendering core for the math viz pipeline.

A single place that owns visual identity (colors, sizes, backend), canvas
creation with sane layout defaults, and export helpers — so that graphs produced
across sessions look consistent and avoid the per-script drift that caused
overlapping / broken elements.

Public API:
- theme: PALETTE, DPI, FONTS, apply_matplotlib_defaults()
- canvas: new_canvas(), simple_axes()
- export: save_figure()
"""
from .theme import PALETTE, DPI, FONTS, apply_matplotlib_defaults
from .canvas import new_canvas, simple_axes
from .export import save_figure

__all__ = [
    "PALETTE",
    "DPI",
    "FONTS",
    "apply_matplotlib_defaults",
    "new_canvas",
    "simple_axes",
    "save_figure",
]