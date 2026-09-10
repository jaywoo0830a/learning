# Tests for conic-section primitives (circle / ellipse / param curve).
import matplotlib
matplotlib.use("Agg", force=True)
import matplotlib.pyplot as plt
import numpy as np

from viz.primitives.conic import plot_ellipse_c, plot_circle_c, plot_param2d


class TestConic:
    def test_circle_adds_line(self):
        fig, ax = plt.subplots()
        plot_circle_c(ax, 3, -2, 4)
        assert len(ax.lines) == 1
        plt.close(fig)

    def test_circle_radius_points_on_circle(self):
        fig, ax = plt.subplots()
        plot_circle_c(ax, 0, 0, 5)
        xs = ax.lines[0].get_xdata()
        ys = ax.lines[0].get_ydata()
        assert np.allclose(xs**2 + ys**2, 25, atol=1e-6)
        plt.close(fig)

    def test_ellipse_fits_equation(self):
        fig, ax = plt.subplots()
        a, b, cx, cy = 2, 3, 1, 1
        plot_ellipse_c(ax, cx, cy, a, b)
        xs = ax.lines[0].get_xdata()
        ys = ax.lines[0].get_ydata()
        val = ((xs - cx) / a)**2 + ((ys - cy) / b)**2
        assert np.allclose(val, 1, atol=1e-6)
        plt.close(fig)

    def test_param2d(self):
        fig, ax = plt.subplots()
        t = np.linspace(0, 2 * np.pi, 200)
        plot_param2d(ax, t, np.cos(t), np.sin(t))
        assert len(ax.lines) == 1
        plt.close(fig)
