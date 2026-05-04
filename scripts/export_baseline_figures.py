#!/usr/bin/env python
"""Export baseline residue figures before notebook work begins."""

from pathlib import Path

from residue_manifold import make_residue_dataset, mod30_prime_lanes, residue_histogram
from residue_manifold.viz import plot_residue_histogram, savefig


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    fig_dir = root / "figures"
    ds = make_residue_dataset(n=30_000, modulus=30, valid_lanes=mod30_prime_lanes())
    hist_all = residue_histogram(ds.values, modulus=30)
    hist_lanes = residue_histogram(ds.values[ds.labels == 1], modulus=30)

    plot_residue_histogram(hist_all, "Uniform integers projected onto mod30")
    savefig(fig_dir / "baseline_mod30_all_residues.png")

    plot_residue_histogram(hist_lanes, "Constrained mod30 lanes: residues coprime to 30")
    savefig(fig_dir / "baseline_mod30_valid_lanes.png")
    print(f"wrote figures to {fig_dir}")


if __name__ == "__main__":
    main()
