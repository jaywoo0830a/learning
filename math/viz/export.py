"""Figure export helper (single point for filename/dpi/format decisions).

Owns the canonical naming/placement scheme:

    <GRAPH_ROOT>/<session_id>/<nn>-<slug>.png

so all session graphs land in one tree, sorted by session, with stable,
lower-cased ids and sanitized slugs (replacing the old date-stamped folders).
"""
from __future__ import annotations

import os
import re

from .theme import DPI

# Top-level graph root: <repo>/graphs
GRAPH_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "graphs"))


def _safe(part: str) -> str:
    """Lower-case and keep only [a-z0-9-] (collapse runs, strip edges)."""
    s = re.sub(r"[^a-zA-Z0-9]+", "-", part).strip("-").lower()
    # collapse consecutive dashes
    return re.sub(r"-{2,}", "-", s)


def graph_path(session_id: str, graph_id: str, slug: str) -> str:
    """Return the absolute path for a graph under the canonical schema.

    ``session_id`` -> directory (lower-cased), ``graph_id`` (e.g. '04') +
    ``slug`` (description) -> filename ``<id>-<slug>.png``.
    """
    sid = _safe(session_id)
    fname = f"{_safe(graph_id) or graph_id}-{_safe(slug) or 'graph'}.png"
    return os.path.join(GRAPH_ROOT, sid, fname)


def save_figure(
    fig,
    path: str,
    *,
    dpi: int = DPI,
    bbox_inches: str = "tight",
) -> str:
    """Render ``fig`` to ``path`` and return the absolute path written.

    Creates any parent directories. Uses the canonical DPI and tight bbox so
    every graph is exported the same way.
    """
    out = os.path.abspath(path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.savefig(out, dpi=dpi, bbox_inches=bbox_inches)
    return out