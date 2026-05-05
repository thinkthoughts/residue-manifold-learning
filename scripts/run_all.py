import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
FIGS = ROOT / "figures" / "paper"

def ensure_dirs():
    DATA.mkdir(parents=True, exist_ok=True)
    FIGS.mkdir(parents=True, exist_ok=True)

def run():
    ensure_dirs()

    # Import your modules here
    # (adjust names to match your src/)
    from residue_manifold.residue import build_mod30_residues
    from residue_manifold.sampling import run_sampling_experiment
    from residue_manifold.nmf import run_nmf_recovery
    from residue_manifold.sae import run_sae_dilution
    from residue_manifold.phase import run_phase_diagram
    from residue_manifold.cgcs import compute_cgcs
    from residue_manifold.geometry import compute_phase_lock

    print("01: residue manifold")
    build_mod30_residues(out_dir=DATA)

    print("02: sampling")
    run_sampling_experiment(out_dir=DATA, fig_dir=FIGS)

    print("03: nmf")
    run_nmf_recovery(out_dir=DATA, fig_dir=FIGS)

    print("04: sae")
    run_sae_dilution(out_dir=DATA, fig_dir=FIGS)

    print("05: phase diagram")
    run_phase_diagram(out_dir=DATA, fig_dir=FIGS)

    print("06: cgcs")
    compute_cgcs(out_dir=DATA, fig_dir=FIGS)

    print("07: geometry")
    compute_phase_lock(out_dir=DATA, fig_dir=FIGS)

    print("\nDone. Figures in figures/paper/, data in data/")

if __name__ == "__main__":
    run()
