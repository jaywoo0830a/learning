"""Generate + save every registered graph under the canonical naming.

Run inside the container:  python scripts/generate_14d_relations.py
Writes to math/graphs/<session>/<nn>-<slug>.png and prints verified facts/checks.

The command-line entry point also runs examples: use ``--check`` to run only the
verifiable claims (no PNG output).
"""
import argparse
import matplotlib
matplotlib.use("Agg", force=True)
import matplotlib.pyplot as plt

from viz.export import save_figure
from viz.registry import specs
from verify.numeric import passive_validate

# Register every @graph builder (the registry is populated by import).
import scripts.graphs.spec_14d_relations  # noqa: F401
import scripts.graphs.spec_14d1a           # noqa: F401
import scripts.graphs.spec_9b              # noqa: F401


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="only run each builder's checks; do not save PNGs")
    args = parser.parse_args(argv)

    total_ok = True
    for gid, gspec in sorted(specs().items()):
        fig, facts, checks, path = gspec.run()
        ok, failures = passive_validate(checks)
        total_ok = total_ok and ok
        print(f"[{gid}] checks_ok={ok} failures={failures or None} facts={facts}")
        if not args.check:
            save_figure(fig, path)
            print(f"      saved -> {path}")
        plt.close(fig)
    print("ALL CHECKS PASS" if total_ok else "SOME CHECKS FAILED")


if __name__ == "__main__":
    main()