#!/usr/bin/env python
"""Smoke test for residue-manifold-learning source utilities."""

from residue_manifold import (
    make_residue_dataset,
    mod30_prime_lanes,
    constrained_sample,
    residue_histogram,
    coverage_score,
    cosine_gate,
    cgcs_score,
)


def main() -> None:
    ds = make_residue_dataset(n=3000, modulus=30, valid_lanes=mod30_prime_lanes())
    sample = constrained_sample(ds.values, ds.modulus, ds.valid_lanes, size=500, seed=42)
    hist = residue_histogram(sample, modulus=30)
    coverage = coverage_score(sample % 30, ds.valid_lanes)
    cos, passed = cosine_gate(hist, residue_histogram(ds.values, modulus=30))
    score = cgcs_score(coverage=coverage, stability=max(cos, 0.0), signal_to_noise=coverage)
    print(f"valid_lanes={ds.valid_lanes}")
    print(f"coverage={coverage:.3f}")
    print(f"cosine={cos:.3f}, gate_passed={passed}")
    print(f"cgcs={score:.3f}")


if __name__ == "__main__":
    main()
