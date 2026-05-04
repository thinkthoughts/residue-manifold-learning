"""Plot helpers for residue-manifold notebooks."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def savefig(path: str | Path, dpi: int = 200) -> None:
    """Save current matplotlib figure with consistent defaults."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(path, dpi=dpi, bbox_inches="tight")


def plot_residue_histogram(hist: np.ndarray, title: str = "Residue distribution"):
    """Create a simple residue histogram figure."""
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.bar(np.arange(len(hist)), hist)
    ax.set_xlabel("Residue class")
    ax.set_ylabel("Frequency")
    ax.set_title(title)
    return fig, ax


def plot_component_heatmap(components: np.ndarray, title: str = "Learned components"):
    """Create a heatmap for learned residue components."""
    fig, ax = plt.subplots(figsize=(10, 4))
    im = ax.imshow(np.asarray(components), aspect="auto")
    ax.set_xlabel("Residue class")
    ax.set_ylabel("Component")
    ax.set_title(title)
    fig.colorbar(im, ax=ax, label="Weight")
    return fig, ax
