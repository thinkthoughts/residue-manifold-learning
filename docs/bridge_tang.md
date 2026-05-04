# Bridge: Tang-style Dequantization and Residue Manifold Learning

Tang's 2018 recommendation-system algorithm is useful here as a conceptual bridge: an apparent quantum advantage can disappear when classical algorithms receive structured sampling access.

Residue Manifold Learning starts from a different object: modular residue space. The mod30 baseline has eight coprime lanes:

```text
1, 7, 11, 13, 17, 19, 23, 29
```

The repo asks whether structure-aware sampling and simple recovery models reveal these lanes more cleanly than unconstrained or capacity-diluted baselines.

Working translation:

| Tang / dequantization | RML / mod30 baseline |
| --- | --- |
| norm sampling access | constraint-aligned residue sampling |
| low-rank structure | finite modular lane structure |
| quantum-inspired access model | geometric / CGCS access model |
| speedup gap collapses under matched access | brute-force gap shrinks when residue lanes are explicit |

Paper claim to test:

> Structured constraint sampling reveals latent modular geometry and reduces apparent complexity gaps between brute-force, classical, and quantum-inspired access models.
