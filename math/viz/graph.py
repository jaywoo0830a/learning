"""Chainable, thin graph builder that collects figure + facts + checks together.

This is the middle path the repo settled on: not a fully-declarative
``FigureSpec`` (which gets abstruse for multi-panel graphs), but a small
collector whose drawing methods return ``self`` so a graph reads as a pipeline,
and which accumulates ``facts`` (exact sympy values) and ``checks`` (verifiable
claims) in one place — keeping verification next to the code that draws.

Single-panel use:

    g = G(size=(7, 6), title=r"$x^2+y^2=25$", equal_aspect=True)
    g.claim("slope at (3,4) == -3/4", lambda: m_at == sp.Rational(-3, 4))
    g.curve(xs, ys, label=r"$x^2+y^2=25$")
    g.tangent((3, 4), -0.75).point((3, 4)).callout((3, 4), r"$dy/dx=-3/4$", (-2.4, 0.9))
    fig, facts, checks = g.build()

Multi-panel graphs should use ``viz.canvas.subplots_canvas`` and the shared
primitives directly (and collect ``checks`` the same way).
"""


class G:
    """Chainable single-axes graph builder.

    Every drawing method returns ``self`` so calls compose.  ``facts`` and
    ``checks`` accumulate alongside the drawing; ``build()`` returns them so a
    registered builder can hand them back to the registry / test runner.
    """

    def __init__(self, *, size=(8.0, 5.0), title=None, equal_aspect=False,
                 xlim=None, ylim=None):
        from .canvas import new_canvas, simple_axes

        self.facts: dict = {}
        self.checks: dict = {}
        self.fig, self.ax = new_canvas(size=size)
        simple_axes(self.ax, equal_aspect=equal_aspect)
        if title:
            self.ax.set_title(title, fontweight="bold")
        if xlim:
            self.ax.set_xlim(*xlim)
        if ylim:
            self.ax.set_ylim(*ylim)

    # ── verification ────────────────────────────────────────────────
    def claim(self, name: str, fn) -> "G":
        """Attach a verifiable claim ``fn: () -> bool`` named ``name``."""
        self.checks[name] = fn
        return self

    def fact(self, name: str, value) -> "G":
        """Record an exact value the graph relies on into ``facts``."""
        self.facts[name] = value
        return self

    # ── drawing (thin wrappers, return self) ─────────────────────────
    def curve(self, x, y, **kw) -> "G":
        from .primitives.curve import plot_curve

        plot_curve(self.ax, x, y, **kw)
        return self

    def tangent(self, at, m, **kw) -> "G":
        from .primitives.curve import plot_tangent

        plot_tangent(self.ax, at[0], at[1], m, **kw)
        return self

    def point(self, xy, **kw) -> "G":
        from .primitives.curve import plot_point

        plot_point(self.ax, xy[0], xy[1], **kw)
        return self

    def region(self, x, y, **kw) -> "G":
        from .primitives.shapes import plot_region

        plot_region(self.ax, x, y, **kw)
        return self

    def callout(self, target, text, offset, **kw) -> "G":
        from .primitives.annotate import add_callout

        add_callout(self.ax, target, text, offset, **kw)
        return self

    def build(self):
        """Return ``(fig, facts, checks)`` for the registry / test runner."""
        return self.fig, dict(self.facts), dict(self.checks)