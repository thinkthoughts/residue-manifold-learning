# Residue Manifold Learning

**Residue Manifold Learning (RML)** studies structure, sampling, and representation in modular arithmetic using a mod30 residue manifold as a controlled experimental setting.

The project develops a paper-aligned pipeline showing how structured sampling and representation choices determine whether underlying modular structure is recovered or degraded.

---

## Core idea

Prime-support residues modulo 30 form an eight-lane discrete manifold embedded in ℤ/30ℤ.

RML investigates:

- how structure exists independently of representation,
- how sampling determines access to that structure,
- how representation determines whether structure is preserved.

A central result is:

> reconstruction quality alone does not imply structural fidelity.

---

## What this repo demonstrates

The notebooks build a minimal, reproducible chain:

1. **Structure** — mod30 residue lanes exist as a discrete manifold  
2. **Sampling** — constraint-aligned sampling concentrates signal  
3. **Recovery** — NMF recovers the manifold compactly  
4. **Failure modes** — sparse representations can fragment or dilute structure  
5. **Regimes** — behavior separates into recovered / partial / diluted / fragmented  
6. **Metric** — CGCS (Constraint-Guided Coherence Score) quantifies structure quality  
7. **Geometry** — structure quality corresponds to a cosine phase-lock constraint (~45°)

---

## Repo layout

residue-manifold-learning/
├── src/residue_manifold/      # reusable experiment utilities
├── scripts/                   # command-line prep scripts
├── tests/                     # smoke tests
├── notebooks/                 # paper-aligned experiments
├── data/                      # generated CSV outputs
├── figures/                   # SVG figures for paper
├── docs/                      # notes / bridges
└── paper/                     # paper.tex / paper.md

---

## Install

python -m venv .venv
source .venv/bin/activate
pip install -e .
pip install -r requirements.txt

---

## Prep commands

python scripts/smoke_test.py
python scripts/build_baseline_data.py
python scripts/export_baseline_figures.py
pytest

---

## Notebook pipeline

1. `01_residue_space.ipynb` — construct mod30 residue manifold  
2. `02_constraint_sampling.ipynb` — compare sampling strategies  
3. `03_nmf_recovery.ipynb` — recover structure with NMF  
4. `04_sae_dilution.ipynb` — show sparse feature fragmentation  
5. `05_coverage_phase_diagram.ipynb` — map regimes  
6. `06_cgcs_metric.ipynb` — define CGCS  
7. `07_phase_lock_geometry.ipynb` — geometric interpretation  

---

## CGCS

CGCS measures structural fidelity as a product of:

- coverage  
- alignment  
- redundancy penalty  
- dead-feature penalty  
- reconstruction penalty  

Threshold:

CGCS ≥ 24/25 → phase-locked  
CGCS < 24/25 → degraded

---

## Tang connection

Ewin Tang’s dequantization result showed that quantum speedups can disappear with structured classical sampling.

RML explores:

> when sampling aligns with structure, the manifold becomes directly recoverable.

and extends this:

> representation choice determines whether structure is preserved or diluted.

---

## Paper

paper/paper.tex  
paper/paper.md  

Figures:

figures/*.svg

---

## Summary

Residue Manifold Learning shows:

- structure exists,
- sampling reveals it,
- representation preserves or degrades it,
- CGCS measures it,
- geometry explains it.

---

## License

MIT
