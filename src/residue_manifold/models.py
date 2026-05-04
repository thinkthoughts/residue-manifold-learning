"""Lightweight model helpers used by notebooks and scripts."""

from __future__ import annotations

import numpy as np
from sklearn.decomposition import NMF, DictionaryLearning, MiniBatchDictionaryLearning


def fit_nmf(x: np.ndarray, n_components: int = 8, random_state: int = 0, max_iter: int = 1_000):
    """Fit nonnegative matrix factorization and return model, W, H."""
    model = NMF(n_components=n_components, init="nndsvda", random_state=random_state, max_iter=max_iter)
    w = model.fit_transform(np.asarray(x, dtype=float))
    h = model.components_
    return model, w, h


def fit_dictionary_learning(
    x: np.ndarray,
    n_components: int = 16,
    sparsity_alpha: float = 1.0,
    random_state: int = 0,
    max_iter: int = 1_000,
    batch: bool = True,
):
    """Fit a sparse dictionary model as a controlled SAE-like baseline.

    This is not a neural sparse autoencoder. It is a lightweight, reproducible
    sparse-coding baseline for notebooks before any heavier PyTorch SAE layer.
    """
    cls = MiniBatchDictionaryLearning if batch else DictionaryLearning
    kwargs = dict(
        n_components=n_components,
        alpha=sparsity_alpha,
        random_state=random_state,
        max_iter=max_iter,
        transform_algorithm="lasso_lars",
    )
    if batch:
        kwargs["batch_size"] = 256
    model = cls(**kwargs)
    codes = model.fit_transform(np.asarray(x, dtype=float))
    dictionary = model.components_
    return model, codes, dictionary
