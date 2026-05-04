# Residue Manifold Learning

**Residue Manifold Learning (RML)** studies constraint sampling and structure recovery on modular residue manifolds, starting from a mod30 baseline.

This repo prepares a paper-oriented experimental path connecting:

- modular residue structure,
- Tang-style dequantization intuition via structured sampling,
- NMF lane recovery,
- sparse-feature dilution baselines,
- CGCS-style coverage/stability scoring,
- 45° geometric constraint gates.

## Core frame

Structured constraint sampling can reveal latent modular geometry and reduce apparent complexity gaps between brute-force scans, classical sampling, and quantum-inspired access models.

## Repo layout

```text
residue-manifold-learning/
├── src/residue_manifold/      # reusable experiment utilities
├── scripts/                   # command-line prep scripts
├── tests/                     # smoke tests
├── notebooks/                 # paper-aligned notebooks, added next
├── data/                      # generated baseline CSVs
├── figures/                   # generated figures
├── docs/                      # bridge notes
└── paper/                     # paper.tex later
```

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
pip install -r requirements.txt
```

## Prep commands

```bash
python scripts/smoke_test.py
python scripts/build_baseline_data.py
python scripts/export_baseline_figures.py
pytest
```

## Initial notebook plan

1. `01_residue_space.ipynb` — construct mod30 residue manifold and lane baseline.
2. `02_constraint_sampling.ipynb` — compare uniform, constrained, and l2-weighted sampling.
3. `03_nmf_recovery.ipynb` — recover lane structure with NMF.
4. `04_sparse_dictionary_dilution.ipynb` — benchmark sparse coding / SAE-like fragmentation.
5. `05_coverage_phase_diagram.ipynb` — sweep capacity and sparsity.
6. `06_cgcs_metric.ipynb` — score coverage, stability, and signal/noise.
7. `07_geometry_phase_lock.ipynb` — analyze 45° cosine gate behavior.
8. `08_unified_experiment.ipynb` — compare brute-force, constrained sampling, NMF, and sparse baselines.
9. `09_figures_export.ipynb` — export paper-ready figures and data.

## Tang bridge

Ewin Tang's dequantization result showed that a quantum recommendation-system speedup can collapse when classical algorithms receive comparable norm-sampling access. RML uses mod30 residue structure as a controlled setting for testing a related principle: sampling aligned with structure can reveal the manifold directly.
