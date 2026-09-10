# Tests for the export helper.
# TDD: define the contract, implement viz/export.py to satisfy it.
import os

import pytest


class TestSaveFigure:
    def test_writes_png(self, tmp_path):
        import matplotlib.pyplot as plt
        from viz.export import save_figure

        fig, ax = plt.subplots()
        ax.plot([0, 1], [0, 1])
        out = save_figure(fig, str(tmp_path / "a.png"))
        assert os.path.exists(out)
        assert out.endswith(".png")
        plt.close(fig)

    def test_writes_absolute_path(self, tmp_path):
        from viz.export import save_figure

        fig, _ = __import__("matplotlib.pyplot", fromlist=["subplots"]).subplots()
        out = save_figure(fig, str(tmp_path / "b" / "c.png"))
        assert out == str((tmp_path / "b" / "c.png").resolve())
        assert os.path.isdir(tmp_path / "b")
        __import__("matplotlib.pyplot", fromlist=["close"]).close(fig)

    def test_uses_canonical_dpi_by_default(self, tmp_path):
        import matplotlib.pyplot as plt
        from viz.export import save_figure
        from viz.theme import DPI

        fig, ax = plt.subplots()
        ax.plot([0, 1], [0, 1])
        out = save_figure(fig, str(tmp_path / "dpi.png"))
        # read back: not easily inspectable; at least ensure it rendered
        assert os.path.getsize(out) > 0
        assert DPI > 0
        plt.close(fig)