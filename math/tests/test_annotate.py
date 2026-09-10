# Tests for the callout/annotation primitive.
# TDD: expectations first, implement viz/primitives/annotate.py to satisfy.
import matplotlib
matplotlib.use("Agg", force=True)
import matplotlib.pyplot as plt


class TestAddCallout:
    def test_adds_annotation(self):
        from viz.primitives.annotate import add_callout

        fig, ax = plt.subplots()
        add_callout(ax, target=(1.0, 2.0), text="point", offset=(0.5, 0.5))
        assert len(ax.texts) == 1
        plt.close(fig)

    def test_annotation_has_arrow(self):
        from viz.primitives.annotate import add_callout

        fig, ax = plt.subplots()
        add_callout(ax, target=(1.0, 2.0), text="hi", offset=(0.5, 0.5))
        ann = ax.texts[0]
        # An annotation with an arrowpatch records it; inspect via get_arrow_patch
        assert ann.arrow_patch is not None
        plt.close(fig)

    def test_annotation_text(self):
        from viz.primitives.annotate import add_callout

        fig, ax = plt.subplots()
        add_callout(ax, target=(0.0, 0.0), text=r"$\frac{dy}{dx}=-3/4$", offset=(1, 1))
        assert ax.texts[0].get_text() == r"$\frac{dy}{dx}=-3/4$"
        plt.close(fig)

    def test_returns_annotation(self):
        from viz.primitives.annotate import add_callout

        fig, ax = plt.subplots()
        ann = add_callout(ax, target=(0, 0), text="t", offset=(1, 1))
        assert hasattr(ann, "set_text") or hasattr(ann, "get_text")
        plt.close(fig)