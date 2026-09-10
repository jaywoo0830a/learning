"""Generate + save the 7 migrated 14D / 14D1 graphs under the canonical naming.

Run inside the container:  python scripts/generate_14d_relations.py
Writes to math/graphs/<session>/<nn>-<slug>.png and prints verified facts.
"""
import matplotlib
matplotlib.use("Agg", force=True)
import matplotlib.pyplot as plt

from viz.export import save_figure
from scripts.graphs.spec_14d_relations import ALL_BUILDERS


def main():
    for name, fn in ALL_BUILDERS.items():
        fig, facts, path = fn()
        save_figure(fig, path)
        print(f"[{name}] saved -> {path}")
        print(f"      verified: {facts}")
        plt.close(fig)


if __name__ == "__main__":
    main()