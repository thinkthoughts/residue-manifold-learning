"""Residue-space construction utilities."""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd
from typing import Iterable

import numpy as np


MOD30_PRIME_LANES: tuple[int, ...] = (1, 7, 11, 13, 17, 19, 23, 29)


@dataclass(frozen=True)
class ResidueDataset:
    """Container for modular residue examples.

    Attributes
    ----------
    values:
        Integer values before residue projection.
    residues:
        Values reduced modulo ``modulus``.
    one_hot:
        One-hot residue representation with shape ``(n, modulus)``.
    modulus:
        Modulus used to construct the space.
    valid_lanes:
        Residue lanes treated as constrained/valid structure.
    labels:
        Binary indicator that a value belongs to ``valid_lanes``.
    """

    values: np.ndarray
    residues: np.ndarray
    one_hot: np.ndarray
    modulus: int
    valid_lanes: tuple[int, ...]
    labels: np.ndarray


def residue_classes(modulus: int) -> np.ndarray:
    """Return residue classes ``0, ..., modulus - 1``."""
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    return np.arange(modulus, dtype=int)


def coprime_residues(modulus: int) -> tuple[int, ...]:
    """Return residues coprime to ``modulus``."""
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    return tuple(r for r in range(modulus) if gcd(r, modulus) == 1)


def mod30_prime_lanes() -> tuple[int, ...]:
    """Return the eight mod-30 lanes that can contain primes greater than 5."""
    return MOD30_PRIME_LANES


def residue_histogram(values: Iterable[int], modulus: int = 30, normalize: bool = True) -> np.ndarray:
    """Compute histogram over residues modulo ``modulus``."""
    values_arr = np.asarray(list(values), dtype=int)
    residues = values_arr % modulus
    counts = np.bincount(residues, minlength=modulus).astype(float)
    if normalize and counts.sum() > 0:
        counts /= counts.sum()
    return counts


def make_residue_dataset(
    n: int = 10_000,
    modulus: int = 30,
    valid_lanes: tuple[int, ...] | None = None,
    start: int = 0,
) -> ResidueDataset:
    """Create a deterministic residue dataset over consecutive integers.

    This deliberately avoids primality testing. The baseline manifold is the
    modular lane structure itself, especially the lanes coprime to 30.
    """
    if n <= 0:
        raise ValueError("n must be positive")
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    lanes = tuple(valid_lanes if valid_lanes is not None else coprime_residues(modulus))
    values = np.arange(start, start + n, dtype=int)
    residues = values % modulus
    one_hot = np.eye(modulus, dtype=float)[residues]
    labels = np.isin(residues, np.asarray(lanes, dtype=int)).astype(int)
    return ResidueDataset(values=values, residues=residues, one_hot=one_hot, modulus=modulus, valid_lanes=lanes, labels=labels)
