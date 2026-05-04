"""Sampling utilities for residue manifolds."""

from __future__ import annotations

import numpy as np


def _rng(seed: int | None = None) -> np.random.Generator:
    return np.random.default_rng(seed)


def uniform_sample(values: np.ndarray, size: int, seed: int | None = None) -> np.ndarray:
    """Sample values uniformly with replacement."""
    if size <= 0:
        raise ValueError("size must be positive")
    values = np.asarray(values)
    return _rng(seed).choice(values, size=size, replace=True)


def constrained_sample(
    values: np.ndarray,
    modulus: int,
    valid_lanes: tuple[int, ...],
    size: int,
    seed: int | None = None,
) -> np.ndarray:
    """Sample only values whose residues land in ``valid_lanes``."""
    values = np.asarray(values)
    mask = np.isin(values % modulus, np.asarray(valid_lanes, dtype=int))
    constrained = values[mask]
    if constrained.size == 0:
        raise ValueError("no values satisfy the requested residue constraint")
    return uniform_sample(constrained, size=size, seed=seed)


def l2_weighted_sample(
    matrix: np.ndarray,
    size: int,
    axis: int = 0,
    seed: int | None = None,
) -> np.ndarray:
    """Return row/column indices sampled proportional to squared l2 norm.

    This is a classical analogue of norm-based access used in dequantization
    discussions. It returns indices rather than rows so callers can decide how
    to materialize examples.
    """
    if size <= 0:
        raise ValueError("size must be positive")
    matrix = np.asarray(matrix, dtype=float)
    if axis == 0:
        weights = np.sum(matrix * matrix, axis=1)
    elif axis == 1:
        weights = np.sum(matrix * matrix, axis=0)
    else:
        raise ValueError("axis must be 0 for rows or 1 for columns")
    total = weights.sum()
    if total <= 0:
        raise ValueError("cannot l2-sample from all-zero matrix")
    p = weights / total
    return _rng(seed).choice(np.arange(len(p)), size=size, replace=True, p=p)
