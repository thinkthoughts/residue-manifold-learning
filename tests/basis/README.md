# tests/basis/

Basis-audit suite: independently checks claims in `paper/persist.pdf`
that this repo's vocabulary and metrics were named after or may have
inherited justification from. This is RML auditing its own inherited
assumptions, using the same verification architecture (`specs/reading-point.yaml`,
`specs/correspondence.yaml`, `specs/experiment.yaml`) applied to any
external source.

## Ground rules for this directory

- The original source claim is always preserved verbatim, with its
  location in persist.pdf, as provenance. Never edit it into a
  corrected version in place.
- Results are computed independently and recorded alongside the
  source claim, not merged into it.
- A rejected source claim is never silently rewritten as supported.
  If a construction (a definition, a label, a name) remains useful
  after its original derivation is rejected, that is recorded
  separately from the derivation's status -- see each result's
  `vocabulary_note` where applicable.
- `physical_correspondence` follows the same firewall as every other
  experiment entry: nothing in this directory can set it to
  `supported`.
- Each test file is runnable standalone (`python3 tests/basis/test_*.py`)
  and prints its full JSON result; the corresponding `results/basis/*.yaml`
  is the human-readable, schema-conformant record of that same run.

## Current entries

| Test | Source claim | Status |
|---|---|---|
| `test_persistent_constant.py` | persist.pdf S1/S8: r(L,Pk) -> 24/25 | rejected; true limit is 3 (naive predictor) / 1 (Lemma 1's own refined predictor) |
| `test_9423_phase_lock.py` | persist.pdf S3: (9,4,2,3) construction corresponds to the 45-degree diagonal | rejected; arg(V) = 36.586776 degrees, no permutation reaches 45 degrees, no transformation specified |

## Open follow-ups

Both results flag an **unaudited downstream dependency**:

- `persistent_constant.yaml` -> whether the RML CGCS threshold
  (`>= 24/25` phase-locked) was derived from this claim or chosen
  independently and only coincidentally matches it.
- `9423_phase_lock.yaml` -> whether `notebooks/07_phase_lock_geometry.ipynb`'s
  ~45-degree cosine phase-lock derives from this construction or
  merely shares vocabulary with it.

Neither dependency has been checked yet. Do not assume either
direction until it has been.
