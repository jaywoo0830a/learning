# Tests for multi-panel / 3D canvas helpers.
import matplotlib
matplotlib.use("Agg", force=True)
import matplotlib.pyplot as plt


class TestCanvasMulti:
    def test_subplots_canvas_shape(self):
        from viz.canvas import subplots_canvas
        fig, axes = subplots_canvas(2, 3, size=(14, 9))
        assert axes.shape == (2, 3)
        assert len(fig.axes) == 6
        plt.close(fig)

    def test_subplots_canvas_flat(self):
        from viz.canvas import subplots_canvas
        fig, axes = subplots_canvas(1, 3, size=(12, 4))
        assert len(axes.flat) == 3
        plt.close(fig)

    def test_single_returns_axis_grid(self):
        from viz.canvas import subplots_canvas
        fig, ax = subplots_canvas(1, 1)
        assert hasattr(ax, "flat")  # still a (1,1) ndarray
        plt.close(fig)

    def test_3d_projection(self):
        from viz.canvas import new_axes3d
        fig = plt.figure()
        ax = new_axes3d(fig)
        assert ax.name == "3d"
        plt.close(fig)
