# Ensure the math packages are importable when running pytest from repo root.
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO not in sys.path:
    sys.path.insert(0, REPO)

# Headless rendering: force the non-interactive backend for all viz tests,
# regardless of what the host environment exposes.
import matplotlib  # noqa: E402

matplotlib.use("Agg", force=True)