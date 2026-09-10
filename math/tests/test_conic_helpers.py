# Tests for conic-section helpers added for session 9B.
import matplotlib
matplotlib.use("Agg", force=True)
import matplotlib.pyplot as plt
import numpy as np

from viz.primitives.conic import (
    plot_parabola_v, plot_hyperbola_branches, plot_asymptotes,
)


class TestConicHelpers:
    def test_parabola_vertex(self):
        fig, ax = plt.subplots()
        xs = np.linspace(0, 4, 101)
        plot_parabola_v(ax, xs, 0.5, h=2, k=1)
        ys = ax.lines[0].get_ydata()
        # vertex is the minimum y, attained at x=h
        assert abs(min(ys) - 1.0) < 1e-6
        plt.close(fig)

    def test_hyperbola_four_branches(self):
        fig, ax = plt.subplots()
        lines = plot_hyperbola_branches(ax, 3, 2, xmax=8)
        assert len(lines) == 4
        plt.close(fig)

    def test_hyperbola_point_satisfies(self):
        # a point on the branch: y = b sqrt((x/a)^2 - 1) satisfies x^2/9-y^2/4=1
        fig, ax = plt.subplots()
        plot_hyperbola_branches(ax, 3, 2, xmax=8)
        xs = ax.lines[0].get_xdata()
        ys = ax.lines[0].get_ydata()
        lhs = xs**2 / 9 - ys**2 / 4
        assert np.allclose(lhs, 1, atol=1e-6)
        plt.close(fig)

    def test_two_asymptotes(self):
        fig, ax = plt.subplots()
        lines = plot_asymptotes(ax, 3, 2)
        assert len(lines) == 2
        plt.close(fig)