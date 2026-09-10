"""Figure export helper (single point for filename/dpi/format decisions).

Kept minimal for now; will grow (name scheme, format selection bg) once the
naming convention section lands.
"""
from __future__ import annotations

import os

from .theme import DPI


def save_figure(fig, path: str, *, dpi: int = DPI, bbox_inches: str = "tight") -> str:
    """Render ``fig`` to ``path`` and return the absolute path written.

    Creates any parent directories. Uses the canonical DPI and tight bbox so
    every graph is exported the same way.
    """
    out = os.path.abspath(path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.savefig(out, dpi=dpi, bbox_inches=bbox_inches)
    return out