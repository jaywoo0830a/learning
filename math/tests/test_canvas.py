# Tests for the render core (theme + canvas).
# TDD: define expected behavior first, implement viz/ to satisfy it.
# These tests run headless via the Agg backend (set in conftest/compose env).
import matplotlib
matplotlib.use("Agg", force=True)
import matplotlib.pyplot as plt
import numpy as np


class TestTheme:
    def test_palette_keys(self):
        from viz.theme import PALETTE

        for k in ("blue", "red", "green", "amber", "gray", "purple"):
            assert k in PALETTE

    def test_colors_are_hex(self):
        from viz.theme import PALETTE

        for c in PALETTE.values():
            assert c.startswith("#")
            assert len(c) == 7

    def test_dpi(self):
        from viz.theme import DPI

        assert DPI > 0


class TestCanvasNew:
    def test_returns_fig_ax(self):
        from viz.canvas import new_canvas

        fig, ax = new_canvas()
        assert fig is not None
        assert ax is not None
        plt.close(fig)

    def test_optional_size(self):
        from viz.canvas import new_canvas

        fig, ax = new_canvas(size=(4, 3))
        w, h = fig.get_size_inches()
        assert abs(w - 4) < 1e-6 and abs(h - 3) < 1e-6
        plt.close(fig)

    def test_canvas_is_clean(self):
        from viz.canvas import new_canvas

        fig, ax = new_canvas()
        # default axes on first creation: no data lines yet
        assert len(ax.lines) == 0
        plt.close(fig)


class TestCanvasShotguncallouts:
    """Callout/annotate helpers must not be required to exist yet; skip-free."""

    def test_theme_importable_alone(self):
        import viz.theme

        assert hasattr(viz.theme, "PALETTE")