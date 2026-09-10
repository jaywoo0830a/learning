# Tests for the reusable curve/tangent primitives.
# TDD: expectations defined first, then viz/primitives/curve.py implements them.
import matplotlib
matplotlib.use("Agg", force=True)
import matplotlib.pyplot as plt
import numpy as np

from viz.primitives.curve import plot_curve, plot_tangent, plot_point


class TestPlotCurve:
    def test_adds_a_line(self):
        fig, ax = plt.subplots()
        x = np.linspace(-1, 1, 50)
        plot_curve(ax, x, x**2)
        assert len(ax.lines) == 1
        plt.close(fig)

    def test_respects_label(self):
        fig, ax = plt.subplots()
        plot_curve(ax, np.linspace(0, 1, 5), np.linspace(0, 1, 5), label="y=x")
        assert ax.lines[0].get_label() == "y=x"
        plt.close(fig)

    def test_data_values(self):
        fig, ax = plt.subplots()
        x = np.array([0.0, 1.0, 2.0])
        y = np.array([0.0, 1.0, 4.0])
        plot_curve(ax, x, y)
        line = ax.lines[0]
        np.testing.assert_allclose(line.get_xdata(), x)
        np.testing.assert_allclose(line.get_ydata(), y)
        plt.close(fig)


class TestPlotTangent:
    def test_tangent_at_point_uses_slope(self):
        fig, ax = plt.subplots()
        x0, y0, m = 1.0, 1.0, 2.0
        half = 0.5
        plot_tangent(ax, x0, y0, m, half=half)
        line = ax.lines[0]
        xs = line.get_xdata()
        ys = line.get_ydata()
        # endpoints satisfy y = y0 + m*(x - x0)
        for x_, y_ in zip(xs, ys):
            assert abs(y_ - (y0 + m * (x_ - x0))) < 1e-9
        plt.close(fig)

    def test_tangent_centered_on_point(self):
        fig, ax = plt.subplots()
        x0 = 1.0
        half = 0.5
        plot_tangent(ax, x0, 1.0, 2.0, half=half)
        xs = ax.lines[0].get_xdata()
        assert abs((xs[0] + xs[1]) / 2 - x0) < 1e-9
        plt.close(fig)


class TestPlotPoint:
    def test_adds_a_marker(self):
        fig, ax = plt.subplots()
        plot_point(ax, 1.0, 2.0)
        # a 1-point scatter yields one collection with 1 offset
        assert len(ax.collections) == 1
        plt.close(fig)

    def test_point_position(self):
        fig, ax = plt.subplots()
        plot_point(ax, 3.0, 4.0)
        (path,) = ax.collections[0].get_offsets()
        assert path[0] == 3.0 and path[1] == 4.0
        plt.close(fig)