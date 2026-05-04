#!/usr/bin/env python
"""Build baseline residue dataset CSVs for notebooks."""

from pathlib import Path

import pandas as pd

from residue_manifold import make_residue_dataset, mod30_prime_lanes


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    data_dir = root / "data"
    data_dir.mkdir(exist_ok=True)
    ds = make_residue_dataset(n=30_000, modulus=30, valid_lanes=mod30_prime_lanes())
    df = pd.DataFrame({"value": ds.values, "residue_mod30": ds.residues, "valid_lane": ds.labels})
    out = data_dir / "mod30_baseline.csv"
    df.to_csv(out, index=False)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
