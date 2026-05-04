import numpy as np

from residue_manifold import (
    coprime_residues,
    make_residue_dataset,
    mod30_prime_lanes,
    coverage_score,
    cosine_gate,
    cgcs_score,
)


def test_mod30_prime_lanes_match_coprime_residues():
    assert mod30_prime_lanes() == coprime_residues(30)


def test_dataset_shape_and_labels():
    ds = make_residue_dataset(n=60, modulus=30, valid_lanes=mod30_prime_lanes())
    assert ds.one_hot.shape == (60, 30)
    assert set(ds.labels.tolist()) == {0, 1}


def test_coverage_score_full():
    lanes = mod30_prime_lanes()
    assert coverage_score(np.array(lanes), lanes) == 1.0


def test_cosine_gate_self_passes():
    cos, passed = cosine_gate(np.ones(5), np.ones(5))
    assert cos > 0.999
    assert passed


def test_cgcs_bounds():
    score = cgcs_score(1.0, 0.8, 0.9)
    assert 0 <= score <= 1
