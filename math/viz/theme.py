"""Central visual identity for all session graphs.

Keep every color / font / dpi decision here so a session never hard-codes its
own copy (previously duplicated in 16+ files).
"""
from __future__ import annotations

import matplotlib as mpl

# Single source of truth for the palette used across sessions.
PALETTE = {
    "blue": "#1a73e8",
    "red": "#d93025",
    "green": "#188038",
    "amber": "#f9ab00",
    "gray": "#666666",
    "purple": "#7b1fa2",
    "cyan": "#0097a7",
    "lightgray": "#999999",
}

# Render resolution used by the exporter.
DPI = 200

# Label fonts used by matplotlib rcParams.
FONTS = "sans-serif"


def apply_matplotlib_defaults() -> None:
    """Apply the canonical rcParams to the current matplotlib process.

    Idempotent; safe to call repeatedly (each script or spec may call it once).
    """
    mpl.rcParams.update(
        {
            "figure.dpi": DPI,
            "font.size": 11,
            "font.family": FONTS,
            "axes.titlesize": 12,
            "axes.labelsize": 11,
            "legend.fontsize": 9,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
            "axes.grid": False,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
        }
    )