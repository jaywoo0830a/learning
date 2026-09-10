"""Single source of truth for every graph in the repo.

Each builder is registered exactly once with ``@graph(...)``, which records its
graph-id, the (session, number, slug) naming triple, and a callable.  Everything
else that used to copy this mapping around — ``tools/build.py`` (id -> callable)
and ``tools/build_markdown.py`` (id -> session/number/slug tuples) — now derives
from this one registry, so adding a graph touches a single place.

Every registered builder returns ``(fig, facts, checks)`` where:
  - ``fig``   the matplotlib Figure (rendered only through viz.primitives),
  - ``facts`` exact (sympy) values the graph uses, as ``{name: value}``,
  - ``checks`` verifiable claims as ``{name: () -> bool}``.

The canonical output path is owned here via ``viz.export.graph_path``.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict, Tuple

from .export import graph_path


@dataclass(frozen=True)
class GraphSpec:
    """A registered graph: identity, builder callable, and canonical path."""

    graph_id: str
    fn: Callable
    session: str
    number: str
    slug: str

    @property
    def path(self) -> str:
        return graph_path(self.session, self.number, self.slug)

    def run(self) -> Tuple:
        """Call the builder and tag the result with the canonical output path.

        Returns ``(fig, facts, checks, path)`` for the exporter and tests.
        """
        fig, facts, checks = self.fn()
        return fig, facts, checks, self.path


_REGISTRY: Dict[str, GraphSpec] = {}


def graph(graph_id: str, *, session: str, number: str, slug: str):
    """Decorator registering a builder as a canonical graph.

    The decorated callable must return ``(fig, facts, checks)``.  It is left as
    the plain function so tests may still call it directly.

    Example:
        @graph("9b-01-line-forms", session="9b", number="01", slug="line-forms")
        def build_line_forms():
            ...
            return fig, facts, checks
    """

    def deco(fn):
        _REGISTRY[graph_id] = GraphSpec(graph_id, fn, session, number, slug)
        return fn

    return deco


def specs() -> Dict[str, GraphSpec]:
    """Return a copy of the registry: {graph_id: GraphSpec}."""
    return dict(_REGISTRY)


def spec(gid: str) -> GraphSpec:
    """Look up a single registered spec (raises KeyError if unknown)."""
    try:
        return _REGISTRY[gid]
    except KeyError:
        raise KeyError(
            f"unknown graph id: {gid!r}; register it with @graph(...) in a "
            f"module that is imported before the registry is used"
        )


def paths() -> Dict[str, str]:
    """Return {graph_id: canonical_output_path} for every registered graph."""
    return {gid: s.path for gid, s in _REGISTRY.items()}


def build_all() -> Dict[str, Tuple]:
    """Run every registered builder; return {gid: (fig, facts, checks, path)}."""
    return {gid: s.run() for gid, s in _REGISTRY.items()}