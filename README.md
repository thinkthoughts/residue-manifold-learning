# Residue Manifold Learning

**Residue Manifold Learning (RML)** studies structure, sampling, representation, and **distributed consistency** in modular arithmetic using a mod30 residue manifold as a controlled experimental setting.

The project develops a reproducible pipeline showing how structured sampling, representation, and **constraint consistency across noisy links** determine whether underlying modular structure is preserved, degraded, or recoverable. Alongside the notebook pipeline, the repo now includes a specification layer (`specs/`) for stating correspondence claims precisely and auditing them — including auditing this project's own originating paper.

> **Status:** Active experimental project. Core notebook results are being re-audited under the repository's new specification framework. Two claims inherited from the originating paper have been computationally rejected (see Basis audit, below), and the CGCS/phase-lock dependencies on those claims are under audit — not yet confirmed dependent, not yet confirmed independent.

---

## Reading Point

This repo's central result is already an instance of a general principle:

> reconstruction quality alone does not imply structural fidelity.

Reconstruction quality is a **reading** — a single number produced by one measurement procedure. Structural fidelity is a separate, independently specified property, checked by a different procedure. Two runs can share a reconstruction-quality reading while differing in structural fidelity; sharing the reading never identifies the two runs as structurally the same.

See [readingpoint.app](https://readingpoint.app) for the general statement of this principle across other domains, and `specs/reading-point.yaml` for how this repo formalizes it: every experiment records the reading it produced and the specification it was checked against as separate, explicit fields.

The phase-lock geometry in `notebooks/07_phase_lock_geometry.ipynb` connects to the same principle: a cosine similarity near 45° is one reading; whether that reading corresponds to the structure classified as phase-locked by CGCS is a separate, specified claim. (Whether that notebook's construction is itself derived from `paper/persist.pdf`'s phase-lock claim, addressed below, or only shares its vocabulary, is currently unaudited.)

---

## Core idea

The reduced residue classes modulo 30, {1, 7, 11, 13, 17, 19, 23, 29} — the canonical object (ℤ/30ℤ)ˣ — provide RML's eight-lane discrete state space. Every prime p > 5 falls into one of these eight classes. ("Manifold" here is project terminology for this discrete state space, not a manifold in the differential/topological sense.)

RML investigates:

- how structure exists independently of representation,
- how sampling determines access to that structure,
- how representation preserves or fragments structure,
- how **distributed systems degrade under noisy links**,
- how **projection restores constraint consistency**,
- how **stability becomes cost-dependent at scale**.

A central result is:
> reconstruction quality alone does not imply structural fidelity.

---

## What this repo demonstrates

The notebooks build a systems chain:

1. **Structure** — mod30 residue lanes form a discrete manifold
2. **Sampling** — constraint-aligned sampling concentrates signal
3. **Recovery** — NMF recovers compact structure
4. **Failure modes** — sparse representations fragment structure
5. **Metric** — CGCS quantifies structural fidelity
6. **Geometry** — notebook 07 tests a cosine phase-lock near 45°; its dependency on the originating 9423 construction is under audit
7. **Distributed systems** — noisy links degrade global consistency
8. **Projection** — constraint projection restores consistency
9. **Cost-aware stability** — recovery requires increasing effort under noise

---

## Specification layer (`specs/`)

Three specs govern how correspondence claims are made and bounded across this repo:

- **`reading-point.yaml`** — the core ontology: object → specification → interaction → observable → reading. States the invariant that a shared reading between two objects does not by itself imply a shared specification.
- **`correspondence.yaml`** — the vocabulary for correspondence claims (shared reading, cardinality match, statistical correspondence, group-theoretic tests, physical correspondence), their branching structure, and a firewall: no mathematical or statistical test can, on its own, establish `physical_correspondence`.
- **`experiment.yaml`** — the required schema for any test entry: which configuration was tested, what else was tested alongside it (`selection`), whether the reported choice was canonical, and the executable that produced the result. No entry may assert a result without a reproducible script behind it.

## Basis audit (`tests/basis/`, `results/basis/`)

The originating paper for this project, `paper/persist.pdf`, made two central claims. Both were formalized under `specs/experiment.yaml` and tested directly:

| Claim | Location | Result |
|---|---|---|
| A normalized residue-counting ratio r(L, Pk) converges to a persistent constant 24/25 | Section 1 / Section 8 | **Rejected.** The ratio converges to 3 against the paper's own naive predictor, and to 1 against the paper's own Lemma 1 (its refined heuristic is correct; it just isn't applied to the headline claim). |
| A weighted-vector construction (9,4,2,3) at four fixed angles corresponds to the 45° diagonal, called a "9423 phase-lock representation" | Section 3 | **Rejected.** The construction's actual angle is 36.586776°; an exhaustive search over all 24 weight-to-angle assignments finds none that reach 45°; no transformation between the construction and the diagonal point is specified anywhere in the source. |

Both results are recorded in `results/basis/`, with the original claims preserved verbatim as provenance rather than edited away. Neither result deletes the paper or retires its vocabulary — `paper/persist.pdf` is kept as a **historical / hypothesis-source** document rather than a verified computational basis. Definitions and labels that originated there (including "9423" and "CGCS") can remain useful as identifiers independent of whether their originating derivation held up; that distinction is tracked per-claim, not assumed either way.

Two dependency questions are flagged as **unaudited**, not resolved in either direction:

- Whether the CGCS `>= 24/25` phase-locked threshold was derived from the rejected persistent-constant claim, or chosen independently and only coincidentally shares the value.
- Whether `notebooks/07_phase_lock_geometry.ipynb`'s ~45° cosine phase-lock derives from the rejected §3 construction, or only shares its vocabulary.

See `tests/basis/README.md` for the audit's ground rules and current entries.

---

## Repo layout

```
residue-manifold-learning/
├── specs/                      # reading-point, correspondence, and experiment schemas
├── src/residue_manifold/       # reusable experiment utilities
├── scripts/                    # command-line prep scripts
├── tests/                      # smoke tests
│   └── basis/                  # audit of paper/persist.pdf's claims
├── notebooks/                  # experiments (paper-aligned)
├── figures/                    # canonical repo figures
├── results/                    # compact CSV/JSON outputs
│   └── basis/                  # basis-audit results
├── bridges/                    # external connections (e.g. FTQC)
├── paper/                      # paper.md (current draft), persist.pdf (historical basis)
├── README.md
├── pyproject.toml
├── requirements.txt
```

---

## Install

```
python -m venv .venv
source .venv/bin/activate
pip install -e .
pip install -r requirements.txt
```

## Prep commands

```
python scripts/smoke_test.py
python scripts/build_baseline_data.py
python scripts/export_baseline_figures.py
pytest
```

---

## Notebook pipeline

Core (paper v1):

1. `01_residue_space.ipynb`
2. `02_constraint_sampling.ipynb`
3. `03_nmf_recovery.ipynb`
4. `04_sae_dilution.ipynb`
5. `05_coverage_phase_diagram.ipynb`
6. `06_cgcs_metric.ipynb`
7. `07_phase_lock_geometry.ipynb`

Distributed extension:

8. `08_distributed_residue_consistency.ipynb`
9. `09_projection_threshold_boundary.ipynb` — there exists a critical link-noise threshold below which distributed constraint systems remain stable without correction, and above which required projection success follows a sublinear power-law scaling.

---

## CGCS

Constraint-Guided Coherence Score (CGCS):

```
CGCS = (coverage) × (alignment) × (redundancy penalty) × (dead feature penalty) × (reconstruction penalty)
```

Distributed extension:

```
CGCS = (local coverage) × (local validity) × (link consistency) × (global stability)
```

Configured threshold (provenance audit pending):

```
CGCS >= 24/25 → classified as phase-locked
CGCS <  24/25 → classified as degraded
```

The specific value 24/25 is shared with `paper/persist.pdf`'s rejected persistent-constant claim (see Basis audit, above). Whether that's the threshold's actual derivation or a coincidental match to a rejected claim is currently unaudited — treat the threshold as a configured decision boundary pending that check, not as a value derived from proven mathematics. ("Classified as," not "is": CGCS crossing this line changes the label a run is given, not a mathematical implication about the run.)

---

## Tang connection

Ewin Tang showed that quantum speedups can disappear with structured classical sampling.

RML shows:
> when sampling aligns with structure, the manifold becomes directly recoverable.

and extends this:
> distributed consistency depends on maintaining constraint alignment across noisy links.

---

## Paper

- `paper/paper.md` — current draft
- `paper/persist.pdf` — historical basis / hypothesis source (May 2026). Its two central claims are tested and rejected under `tests/basis/`; see Basis audit, above, before citing it as a verified result.

---

## Summary

Residue Manifold Learning shows:

- structure exists,
- sampling reveals it,
- representation preserves or fragments it,
- CGCS measures it,
- geometry explains it,
- distributed systems degrade under noise,
- projection restores consistency,
- stability requires increasing effort,
- and the project's own originating claims are subject to the same audit as any external source.

---

## License

MIT
