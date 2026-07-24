"""
Generate all figures for the Brain Efficiency Model README.
Output: PNG files in the graph/ directory.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

np.random.seed(42)

# ─── Common Style ───
plt.rcParams.update({
    "figure.dpi": 150,
    "font.size": 11,
    "axes.grid": True,
    "grid.alpha": 0.25,
    "axes.spines.top": False,
    "axes.spines.right": False,
})


# ═══════════════════════════════════════════════════════════════
# FIGURE 1: Core Model — Talented vs Ordinary Activation
# ═══════════════════════════════════════════════════════════════
def fig1_core_model():
    n = 20
    E_max = 10.0

    # Relevance: 4 high-relevance regions, rest low
    r = np.zeros(n)
    relevant = np.array([2, 7, 13, 17])
    r[relevant] = [0.95, 0.88, 0.92, 0.85]
    r[r == 0] = np.random.uniform(0, 0.15, n - 4)

    # Talented: activate top regions up to budget
    order = np.argsort(-r)
    a_talent = np.zeros(n)
    budget = E_max
    for idx in order:
        if budget <= 0:
            break
        a_talent[idx] = min(1.0, budget)
        budget -= a_talent[idx]

    # Ordinary: spread evenly
    a_ordinary = np.ones(n) * (E_max / n)

    # ── Plot ──
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))
    fig.suptitle("Figure 1: Core Model — Talented vs Ordinary Activation", fontsize=14, fontweight="bold")

    x = np.arange(n)
    w = 0.35

    # Panel A: Activation bars
    ax = axes[0]
    ax.bar(x - w/2, a_talent, w, label="Talented", color="steelblue", alpha=0.85)
    ax.bar(x + w/2, a_ordinary, w, label="Ordinary", color="coral", alpha=0.75)
    ax.set_xlabel("Brain region")
    ax.set_ylabel("Activation $a_i$")
    ax.set_title("Activation Patterns")
    ax.set_xticks(x)
    ax.legend(fontsize=9)

    # Panel B: Relevance vs Activation
    ax = axes[1]
    ax.scatter(r, a_talent, c="steelblue", s=60, label="Talented", zorder=3)
    ax.scatter(r, a_ordinary, c="coral", s=60, marker="s", label="Ordinary", zorder=3)
    ax.set_xlabel("Relevance $r_i$")
    ax.set_ylabel("Activation $a_i$")
    ax.set_title("Selectivity")
    ax.legend(fontsize=9)

    # Panel C: Efficiency metrics
    ax = axes[2]
    metrics = ["Active\nRegions", "Energy\n$E$", "Perf.\n$P$", "Efficiency\n$\\eta$"]
    talented_vals = [np.sum(a_talent > 0.01), np.sum(a_talent), np.dot(r, a_talent),
                     np.dot(r, a_talent) / np.sum(a_talent)]
    ordinary_vals = [np.sum(a_ordinary > 0.01), np.sum(a_ordinary), np.dot(r, a_ordinary),
                     np.dot(r, a_ordinary) / np.sum(a_ordinary)]

    xm = np.arange(len(metrics))
    ax.bar(xm - w/2, talented_vals, w, label="Talented", color="steelblue", alpha=0.85)
    ax.bar(xm + w/2, ordinary_vals, w, label="Ordinary", color="coral", alpha=0.75)
    ax.set_xticks(xm)
    ax.set_xticklabels(metrics, fontsize=9)
    ax.set_ylabel("Value")
    ax.set_title("Comparison")
    ax.legend(fontsize=9)

    plt.tight_layout()
    plt.savefig("graph/fig1_core_model.png", bbox_inches="tight")
    plt.close()
    print("  Saved: graph/fig1_core_model.png")


# ═══════════════════════════════════════════════════════════════
# FIGURE 2: Efficiency vs Sparsity
# ═══════════════════════════════════════════════════════════════
def fig2_efficiency_vs_sparsity():
    n = 30
    E_max = 10.0

    r = np.zeros(n)
    n_rel = 6
    rel_idx = np.random.choice(n, n_rel, replace=False)
    r[rel_idx] = np.random.uniform(0.8, 1.0, n_rel)
    r[r == 0] = np.random.uniform(0, 0.1, n - n_rel)

    order = np.argsort(-r)

    efficiencies = []
    entropies = []
    n_active_list = []

    for k in range(1, n + 1):
        a = np.zeros(n)
        for idx in order[:k]:
            a[idx] = min(1.0, E_max)
        a = a * min(1.0, E_max / np.sum(a))  # scale to budget
        if np.sum(a) > 0:
            eff = np.dot(r, a) / np.sum(a)
            p = a / np.sum(a)
            ent = -np.sum(p[p > 0] * np.log2(p[p > 0]))
            efficiencies.append(eff)
            entropies.append(ent)
            n_active_list.append(k)

    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))
    fig.suptitle("Figure 2: Efficiency vs Sparsity", fontsize=14, fontweight="bold")

    # Panel A: Efficiency vs active regions
    ax = axes[0]
    ax.plot(n_active_list, efficiencies, "o-", color="steelblue", markersize=5)
    ax.axvline(n_rel, color="red", ls="--", alpha=0.6, label=f"#relevant = {n_rel}")
    ax.set_xlabel("Number of active regions ($k$)")
    ax.set_ylabel("Efficiency $\\eta$")
    ax.set_title("More regions → lower efficiency")
    ax.legend(fontsize=9)

    # Panel B: Efficiency vs entropy
    ax = axes[1]
    ax.scatter(entropies, efficiencies, c=n_active_list, cmap="viridis_r", s=40, zorder=3)
    ax.set_xlabel("Entropy $H$ (bits)")
    ax.set_ylabel("Efficiency $\\eta$")
    ax.set_title("Low entropy = high efficiency")
    cbar = plt.colorbar(ax.collections[0], ax=ax, label="Active regions $k$")

    # Panel C: Energy distribution at k=4 vs k=20
    ax = axes[2]
    k_small, k_large = 4, 20
    a_small = np.zeros(n)
    a_large = np.zeros(n)
    for idx in order[:k_small]:
        a_small[idx] = min(1.0, E_max)
    for idx in order[:k_large]:
        a_large[idx] = min(1.0, E_max)
    a_small *= min(1.0, E_max / np.sum(a_small))
    a_large *= min(1.0, E_max / np.sum(a_large))

    xb = np.arange(n)
    ax.bar(xb - 0.2, a_small, 0.35, label=f"k={k_small}, η={np.dot(r,a_small)/np.sum(a_small):.3f}",
           color="steelblue", alpha=0.85)
    ax.bar(xb + 0.2, a_large, 0.35, label=f"k={k_large}, η={np.dot(r,a_large)/np.sum(a_large):.3f}",
           color="coral", alpha=0.75)
    ax.set_xlabel("Brain region")
    ax.set_ylabel("Activation")
    ax.set_title("Sparse vs Broad (same energy)")
    ax.legend(fontsize=8)

    plt.tight_layout()
    plt.savefig("graph/fig2_efficiency_vs_sparsity.png", bbox_inches="tight")
    plt.close()
    print("  Saved: graph/fig2_efficiency_vs_sparsity.png")


# ═══════════════════════════════════════════════════════════════
# FIGURE 3: WM Time-Course — Ordinary vs Prodigy
# ═══════════════════════════════════════════════════════════════
def fig3_wm_timecourse():
    T = 40
    n_regions = 4

    # Ordinary: all regions active simultaneously for long periods
    a_ord = np.zeros((n_regions, T))
    for i in range(n_regions):
        start = i * 3
        duration = 12
        a_ord[i, start:start + duration] = 0.8 + 0.2 * np.random.random()

    # Prodigy: staggered, brief activations
    a_pro = np.zeros((n_regions, T))
    for i in range(n_regions):
        start = i * 2
        duration = 5
        a_pro[i, start:start + duration] = 0.9 + 0.1 * np.random.random()

    # Compute cumulative energy
    cum_ord = np.cumsum(np.sum(a_ord, axis=0))
    cum_pro = np.cumsum(np.sum(a_pro, axis=0))

    fig, axes = plt.subplots(2, 2, figsize=(12, 7))
    fig.suptitle("Figure 3: Working Memory Time-Course", fontsize=14, fontweight="bold")

    # Panel A: Ordinary activation heat
    ax = axes[0, 0]
    im = ax.imshow(a_ord, aspect="auto", cmap="Reds", vmin=0, vmax=1, interpolation="nearest")
    ax.set_yticks(range(n_regions))
    ax.set_yticklabels([f"Region {i+1}" for i in range(n_regions)])
    ax.set_xlabel("Time step")
    ax.set_title("Ordinary: simultaneous, prolonged")
    plt.colorbar(im, ax=ax, label="Activation")

    # Panel B: Prodigy activation heat
    ax = axes[0, 1]
    im = ax.imshow(a_pro, aspect="auto", cmap="Blues", vmin=0, vmax=1, interpolation="nearest")
    ax.set_yticks(range(n_regions))
    ax.set_yticklabels([f"Region {i+1}" for i in range(n_regions)])
    ax.set_xlabel("Time step")
    ax.set_title("Prodigy: staggered, brief")
    plt.colorbar(im, ax=ax, label="Activation")

    # Panel C: Total instantaneous energy
    ax = axes[1, 0]
    ax.plot(range(T), np.sum(a_ord, axis=0), color="coral", linewidth=2, label="Ordinary")
    ax.plot(range(T), np.sum(a_pro, axis=0), color="steelblue", linewidth=2, label="Prodigy")
    ax.set_xlabel("Time step")
    ax.set_ylabel("Instantaneous energy")
    ax.set_title("Energy over time")
    ax.legend(fontsize=9)

    # Panel D: Cumulative energy
    ax = axes[1, 1]
    ax.plot(range(T), cum_ord, color="coral", linewidth=2, label=f"Ordinary (total: {cum_ord[-1]:.1f})")
    ax.plot(range(T), cum_pro, color="steelblue", linewidth=2, label=f"Prodigy (total: {cum_pro[-1]:.1f})")
    ax.fill_between(range(T), cum_pro, cum_ord, alpha=0.15, color="gray")
    ax.set_xlabel("Time step")
    ax.set_ylabel("Cumulative energy")
    ax.set_title("Cumulative energy (savings = shaded area)")
    ax.legend(fontsize=9)

    plt.tight_layout()
    plt.savefig("graph/fig3_wm_timecourse.png", bbox_inches="tight")
    plt.close()
    print("  Saved: graph/fig3_wm_timecourse.png")


# ═══════════════════════════════════════════════════════════════
# FIGURE 4: Abstraction Ladder
# ═══════════════════════════════════════════════════════════════
def fig4_abstraction_ladder():
    levels = [0, 1, 2, 3, 4]
    labels = ["Raw\nnumbers", "Vectors /\nMatrices", "Operators /\nTransforms",
              "Abstract\nStructures", "Entire\nProofs"]
    compression = [1, 5, 15, 35, 70]  # cumulative compression factors
    wm_cost = [100, 20, 6.7, 2.9, 1.4]  # relative WM cost = 100 / compression

    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))
    fig.suptitle("Figure 4: Abstraction Ladder — WM Cost vs Abstraction Level",
                 fontsize=13, fontweight="bold")

    # Panel A: WM cost
    ax = axes[0]
    colors = plt.cm.Blues(np.linspace(0.3, 0.9, len(levels)))
    bars = ax.bar(levels, wm_cost, color=colors, width=0.6, edgecolor="navy", linewidth=0.5)
    ax.set_xticks(levels)
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_xlabel("Abstraction Level $L$")
    ax.set_ylabel("Relative WM Energy Cost")
    ax.set_title("Higher abstraction → lower WM cost")
    for bar, val in zip(bars, wm_cost):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f"{val:.1f}×", ha="center", fontsize=8, fontweight="bold")

    # Panel B: Compression factor
    ax = axes[1]
    ax.plot(levels, compression, "o-", color="green", linewidth=2, markersize=8)
    ax.set_xticks(levels)
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_xlabel("Abstraction Level $L$")
    ax.set_ylabel("Information Compression Factor")
    ax.set_title("Exponential compression")
    for l, c in zip(levels, compression):
        ax.annotate(f"{c}×", (l, c), textcoords="offset points", xytext=(0, 10),
                    ha="center", fontsize=9, fontweight="bold", color="green")

    # Panel C: Who operates where
    ax = axes[2]
    y_pos = [1, 2, 3, 4]
    person_labels = ["Ordinary\nperson", "Good\nstudent", "Math\nprodigy", "von\nNeumann"]
    person_levels = [0.5, 1.5, 2.8, 4.0]
    colors_p = ["coral", "orange", "steelblue", "darkblue"]

    ax.barh(y_pos, person_levels, color=colors_p, height=0.5, alpha=0.8)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(person_labels, fontsize=9)
    ax.set_xlim(0, 5)
    ax.set_xlabel("Max Abstraction Level $L$")
    ax.set_title("Abstraction depth by expertise")
    ax.grid(axis="x", alpha=0.3)

    # Annotation
    for y, l, c in zip(y_pos, person_levels, colors_p):
        ax.text(l + 0.1, y, f"L={l:.1f}", va="center", fontsize=9, fontweight="bold", color=c)

    plt.tight_layout()
    plt.savefig("graph/fig4_abstraction_ladder.png", bbox_inches="tight")
    plt.close()
    print("  Saved: graph/fig4_abstraction_ladder.png")


# ═══════════════════════════════════════════════════════════════
# FIGURE 5: Von Neumann Efficiency Multiplier
# ═══════════════════════════════════════════════════════════════
def fig5_von_neumann_multiplier():
    factors = ["Abstraction\nCompression\n(10×)", "Compiled\nIntuition\n(5×)",
               "Rep.\nSwitching\n(3×)", "Combined\n(150×)"]
    values = [10, 5, 3, 150]

    # Time comparison
    tasks = ["Simple arithmetic\n(e.g., 37×29)",
             "Linear algebra\n(e.g., matrix inverse)",
             "Diff. equation\n(e.g., PDE solve)",
             "Abstract proof\n(e.g., functional analysis)"]
    time_ordinary = [60, 1800, 7200, 86400]   # seconds
    time_prodigy = [5, 120, 600, 3600]
    time_von = [2, 10, 60, 300]

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle("Figure 5: Von Neumann Efficiency Multiplier", fontsize=14, fontweight="bold")

    # Panel A: Factor breakdown
    ax = axes[0]
    colors = ["lightblue", "steelblue", "royalblue", "darkblue"]
    bars = ax.bar(factors, values, color=colors, width=0.5, edgecolor="navy", linewidth=0.5)
    ax.set_ylabel("Efficiency multiplier (×)")
    ax.set_title("Each mechanism compounds")
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 3,
                f"{val}×", ha="center", fontsize=11, fontweight="bold")

    # Panel B: Time to solve
    ax = axes[1]
    x = np.arange(len(tasks))
    w = 0.25
    ax.bar(x - w, time_ordinary, w, label="Ordinary", color="coral", alpha=0.8)
    ax.bar(x, time_prodigy, w, label="Prodigy", color="steelblue", alpha=0.8)
    ax.bar(x + w, time_von, w, label="von Neumann", color="darkblue", alpha=0.9)
    ax.set_xticks(x)
    ax.set_xticklabels(tasks, fontsize=8)
    ax.set_ylabel("Time (seconds, log scale)")
    ax.set_yscale("log")
    ax.set_title("Time to solve (log scale)")
    ax.legend(fontsize=9)

    plt.tight_layout()
    plt.savefig("graph/fig5_von_neumann_multiplier.png", bbox_inches="tight")
    plt.close()
    print("  Saved: graph/fig5_von_neumann_multiplier.png")


# ═══════════════════════════════════════════════════════════════
# FIGURE 6: Exploration-Exploitation Over Time
# ═══════════════════════════════════════════════════════════════
def fig6_exploration_exploitation():
    T = 100
    # sigmoid transition from exploration to exploitation
    t = np.linspace(0, T, T)
    entropy_over_time = 4.5 - 3.0 / (1 + np.exp(-0.1 * (t - 50)))
    efficiency_over_time = 0.15 + 0.35 / (1 + np.exp(-0.1 * (t - 50)))

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
    fig.suptitle("Figure 6: Exploration → Exploitation Over Time",
                 fontsize=14, fontweight="bold")

    # Panel A: Entropy & Efficiency
    ax = axes[0]
    ax.plot(t, entropy_over_time, color="coral", linewidth=2, label="Entropy $H$")
    ax.plot(t, efficiency_over_time, color="steelblue", linewidth=2, label="Efficiency $\\eta$")
    ax.axvline(30, color="gray", ls="--", alpha=0.5, label="Clues emerge")
    ax.axvline(65, color="gray", ls=":", alpha=0.5, label="Path clear")
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Adaptive strategy over time")
    ax.legend(fontsize=9)

    # Panel B: Phase diagram
    ax = axes[1]
    phases = ["Broad\nExploration", "Progressive\nFocusing", "Sparse\nExploitation"]
    phase_eff = [0.18, 0.35, 0.48]
    phase_ent = [4.3, 2.5, 1.6]
    phase_colors = ["coral", "gold", "steelblue"]
    for i, (ph, eff, ent, c) in enumerate(zip(phases, phase_eff, phase_ent, phase_colors)):
        ax.scatter(ent, eff, s=300, color=c, zorder=5, edgecolors="black")
        ax.annotate(ph, (ent, eff), textcoords="offset points",
                    xytext=(0, -20), ha="center", fontsize=9, fontweight="bold")

    # Add connecting arrow
    ax.annotate("", xy=(phase_ent[1], phase_eff[1]), xytext=(phase_ent[0], phase_eff[0]),
                arrowprops=dict(arrowstyle="->", color="gray", lw=1.5))
    ax.annotate("", xy=(phase_ent[2], phase_eff[2]), xytext=(phase_ent[1], phase_eff[1]),
                arrowprops=dict(arrowstyle="->", color="gray", lw=1.5))

    ax.set_xlabel("Entropy $H$ (bits)")
    ax.set_ylabel("Efficiency $\\eta$")
    ax.set_title("Phase transition in strategy space")
    ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig("graph/fig6_exploration_exploitation.png", bbox_inches="tight")
    plt.close()
    print("  Saved: graph/fig6_exploration_exploitation.png")


# ═══════════════════════════════════════════════════════════════
# Run all
# ═══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("Generating figures...")
    fig1_core_model()
    fig2_efficiency_vs_sparsity()
    fig3_wm_timecourse()
    fig4_abstraction_ladder()
    fig5_von_neumann_multiplier()
    fig6_exploration_exploitation()
    print("\nAll figures generated in graph/")
