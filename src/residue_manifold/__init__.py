"""Residue Manifold Learning utilities.

A small package for constructing modular residue manifolds, sampling under
constraints, measuring coverage, and benchmarking representation recovery.
"""

from .residues import (
    residue_classes,
    coprime_residues,
    mod30_prime_lanes,
    residue_histogram,
    make_residue_dataset,
)
from .sampling import uniform_sample, constrained_sample, l2_weighted_sample
from .metrics import coverage_score, reconstruction_error, cgcs_score, cosine_gate

__all__ = [
    "residue_classes",
    "coprime_residues",
    "mod30_prime_lanes",
    "residue_histogram",
    "make_residue_dataset",
    "uniform_sample",
    "constrained_sample",
    "l2_weighted_sample",
    "coverage_score",
    "reconstruction_error",
    "cgcs_score",
    "cosine_gate",
]
