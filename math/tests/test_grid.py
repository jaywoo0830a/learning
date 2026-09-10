# Tests for grid/origin-axes primitives.
import matplotlib
matplotlib.use("Agg", force=True)
import matplotlib.pyplot as plt


class TestOriginAxes:
    def test_draws_origin_lines(self):
        from viz.primitives.grid import origin_axes
        fig, ax = plt.subplots()
        origin_axes(ax)
        assert len(ax.lines) >= 2
        plt.close(fig)

    def test_set_limits(self):
        from viz.primitives.grid import set_limits
        fig, ax = plt.subplots()
        set_limits(ax, -3, 3, -5, 5)
        assert ax.get_xlim() == (-3, 3)
        assert ax.get_ylim() == (-5, 5)
        plt.close(fig)

    def test_axis_helpers(self):
        from viz.primitives.grid import xaxis, yaxis
        fig, ax = plt.subplots()
        n0 = len(ax.lines)
        xaxis(ax)
        yaxis(ax)
        assert len(ax.lines) == n0 + 2
        plt.close(fig)

    def test_light_grid(self):
        from viz.primitives.grid import light_grid
        fig, ax = plt.subplots()
        light_grid(ax)
        assert ax.xaxis.get_gridlines() is not None
        plt.close(fig)
