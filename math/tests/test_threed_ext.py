# Tests for 3D primitives used by 9C (axes, plane, surface, quadric, point).
import matplotlib
matplotlib.use("Agg", force=True)
import matplotlib.pyplot as plt
import numpy as np

from viz.primitives import threed3 as d3


class TestThreeD:
    def test_axis3d_quiver(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        d3.plot_axis3d(ax, (0,0,0), np.array([1,0,0]), color="red")
        assert len(ax.collections) >= 1
        plt.close(fig)

    def test_point3d(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        d3.plot_point3d(ax, 3, 2, 4)
        plt.close(fig)

    def test_surface_render(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        x = np.linspace(-2, 2, 20); y = np.linspace(-2, 2, 20)
        X, Y = np.meshgrid(x, y)
        Z = X**2 + Y**2
        d3.plot_surface(ax, X, Y, Z, color="blue", alpha=0.5)
        assert len(ax.collections) >= 1
        plt.close(fig)

    def test_quadric_exists(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        d3.plot_quadric(ax, "ellipsoid", a=2, b=3, c=1)
        plt.close(fig)

    def test_contour_ring(self):
        x, y = d3.contour_circle(np.array([1.0, 2.0]), 1.5)
        assert len(x) == len(y) == 100
