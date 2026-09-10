# Tests for the export path resolver (canonical naming/placement).
import os
import re

import pytest


class TestGraphPath:
    def test_resolves_under_graphs(self):
        from viz.export import graph_path

        p = graph_path("14d1", "04", "circle-ring")
        assert p.endswith(os.path.join("graphs", "14d1", "04-circle-ring.png"))
        assert os.path.abspath(p) == p

    def test_normalizes_session_id(self):
        from viz.export import graph_path

        p = graph_path("14D1", "04", "circle-ring")
        # session id lowered to a stable directory name
        assert os.path.basename(os.path.dirname(p)) == "14d1"

    def test_slug_sanitized(self):
        from viz.export import graph_path

        p = graph_path("14d", "01", "Derivative Units!!")
        assert os.path.basename(p) == "01-derivative-units.png"

    def test_base_contains_graphs_root(self):
        from viz.export import GRAPH_ROOT

        # GRAPH_ROOT points at a top-level graphs dir
        assert GRAPH_ROOT.endswith("graphs")