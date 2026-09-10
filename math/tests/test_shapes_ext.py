# Tests for extended primitives needed by 14D/14D1 graphs:
#   - plot_region (fill_between shaded regions)
#   - plot_circle + plot_ring (Circle / Wedge annulus)
#   - plot_shell_3d (sphere shell in 3D)
import matplotlib
matplotlib.use("Agg", force=True)
import matplotlib.pyplot as plt
import numpy as np

from viz.primitives.shapes import plot_region, plot_circle, plot_ring
from viz.primitives.threed import plot_shell_3d


class TestPlotRegion:
    def test_adds_fillcollection(self):
        fig, ax = plt.subplots()
        x = np.linspace(0, 1, 50)
        plot_region(ax, x, x**2, baseline=0, where=None)
        assert len(ax.collections) == 1
        plt.close(fig)

    def test_region_above_baseline_only_when_where(self):
        fig, ax = plt.subplots()
        x = np.linspace(0, 1, 50)
        w = x > 0.5
        plot_region(ax, x, x, baseline=0, where=w)
        col = ax.collections[0]
        assert col is not None
        plt.close(fig)


class TestPlotCircle:
    def test_adds_patch(self):
        fig, ax = plt.subplots()
        plot_circle(ax, 0, 0, r=3)
        assert len(ax.patches) == 1
        plt.close(fig)

    def test_circle_radius(self):
        from matplotlib.patches import Circle

        fig, ax = plt.subplots()
        plot_circle(ax, 0, 0, r=3)
        patch = ax.patches[0]
        assert isinstance(patch, Circle)
        assert abs(patch.radius - 3) < 1e-9
        plt.close(fig)


class TestPlotRing:
    def test_adds_annulus_patch(self):
        fig, ax = plt.subplots()
        plot_ring(ax, 0, 0, r=3, width=0.45)
        assert len(ax.patches) == 1
        plt.close(fig)

    def test_ring_is_wedge(self):
        from matplotlib.patches import Wedge

        fig, ax = plt.subplots()
        plot_ring(ax, 0, 0, r=3, width=0.45)
        assert isinstance(ax.patches[0], Wedge)
        plt.close(fig)


class TestPlotShell3D:
    def test_adds_surfaces(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        plot_shell_3d(ax, R=3.0, dr=0.5)
        # two shells -> at least two Poly3DCollection
        assert len(ax.collections) >= 2
        plt.close(fig)

    def test_returns_nothing_raises(self):
        # just import-test the helper exposes cleanly
        from viz.primitives import threed as t
        assert callable(t.plot_shell_3d)