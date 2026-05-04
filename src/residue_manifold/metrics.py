"""Metrics for lane coverage, reconstruction, and CGCS-style stability."""

from __future__ import annotations

import numpy as np


def coverage_score(observed_residues: np.ndarray, valid_lanes: tuple[int, ...]) -> float:
    """Fraction of valid lanes observed at least once."""
    lanes = set(int(x) for x in valid_lanes)
    observed = set(int(x) for x in np.asarray(observed_residues).tolist())
    if not lanes:
        raise ValueError("valid_lanes must be non-empty")
    return len(lanes & observed) / len(lanes)


def reconstruction_error(original: np.ndarray, reconstructed: np.ndarray) -> float:
    """Relative Frobenius reconstruction error."""
    original = np.asarray(original, dtype=float)
    reconstructed = np.asarray(reconstructed, dtype=float)
    denom = np.linalg.norm(original)
    if denom == 0:
        return float(np.linalg.norm(reconstructed))
    return float(np.linalg.norm(original - reconstructed) / denom)


def cosine_gate(a: np.ndarray, b: np.ndarray, threshold: float = 1 / np.sqrt(2)) -> tuple[float, bool]:
    """Return cosine similarity and whether it passes the 45-degree gate."""
    a = np.asarray(a, dtype=float).ravel()
    b = np.asarray(b, dtype=float).ravel()
    denom = np.linalg.norm(a) * np.linalg.norm(b)
    if denom == 0:
        return 0.0, False
    cos = float(np.dot(a, b) / denom)
    return cos, bool(cos >= threshold)


def cgcs_score(
    coverage: float,
    stability: float,
    signal_to_noise: float,
    weights: tuple[float, float, float] = (0.4, 0.35, 0.25),
) -> float:
    """Constraint Gage Comprehension Score style aggregate.

    Inputs should already be normalized to ``[0, 1]``. The score is a pragmatic
    repo metric, not a universal theorem: it summarizes lane coverage,
    geometric stability, and signal/noise separation for experiments.
    """
    vals = np.asarray([coverage, stability, signal_to_noise], dtype=float)
    if np.any(vals < 0) or np.any(vals > 1):
        raise ValueError("coverage, stability, and signal_to_noise must be in [0, 1]")
    w = np.asarray(weights, dtype=float)
    w = w / w.sum()
    return float(np.dot(w, vals))
