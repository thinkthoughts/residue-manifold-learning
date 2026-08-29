"""
tests/basis/test_9423_phase_lock.py

Basis audit of persist.pdf, Section 3: the "9423 phase-lock
representation."

Source claim (verbatim, persist.pdf Section 3):
    Weighted tuple (9,4,2,3) at theta_k in {0,60,120,180} degrees.
    "The diagonal direction theta=45 degrees corresponds to (1,1)..."
    "We refer to this configuration as a 9423 phase-lock representation."

The paper states two facts in sequence (V's construction; (1,1) at
45 degrees) without specifying any map, normalization, or limiting
operation between them. This test computes V directly, checks
whether any assignment of the four weights to the four angles
reaches exactly 45 degrees, and records the correspondence as
unestablished per correspondence.yaml's firewall (no transformation
specified).
"""
import cmath
import math
from itertools import permutations


def V(weights, angles_deg):
    return sum(
        w * cmath.exp(1j * math.radians(a)) for w, a in zip(weights, angles_deg)
    )


def run():
    weights = [9, 4, 2, 3]
    angles_deg = [0, 60, 120, 180]

    source_claim = {
        "statement": "9423 weighted-vector construction corresponds to the 45-degree diagonal (1,1)",
        "location": "persist.pdf Section 3",
    }

    v_literal = V(weights, angles_deg)
    literal_angle = math.degrees(cmath.phase(v_literal))

    tested_configuration = {
        "type": "weight_to_angle_assignment_search",
        "swept_parameter": "permutation of weights over fixed angle set",
    }

    candidates = []
    for perm in permutations(weights):
        v = V(list(perm), angles_deg)
        candidates.append({
            "weights_order": list(perm),
            "angles_deg": angles_deg,
            "vector": [round(v.real, 6), round(v.imag, 6)],
            "arg_deg": round(math.degrees(cmath.phase(v)), 6),
        })

    exact_matches = [c for c in candidates if abs(c["arg_deg"] - 45.0) < 1e-6]

    selection = {
        "candidate_count": len(candidates),
        "candidates": candidates,
        "selected": {
            "weights_order": weights,
            "angles_deg": angles_deg,
            "vector": [round(v_literal.real, 6), round(v_literal.imag, 6)],
            "arg_deg": round(literal_angle, 6),
        },
        "canonical": True,
        "selection_basis": "unique",  # this is the literal order stated in the paper
    }

    target_object = complex(1, 1)
    target_reading = math.degrees(cmath.phase(target_object))

    result = {
        "source_claim": source_claim,
        "tested_configuration": tested_configuration,
        "selection": selection,
        "source_computed_reading_deg": round(literal_angle, 6),
        "target_computed_reading_deg": round(target_reading, 6),
        "permutation_search": {
            "permutations_checked": len(candidates),
            "exact_45_degree_matches": len(exact_matches),
        },
        "summary": {
            "shared_reading_status": "rejected",
            "structural_correspondence_status": "unestablished",
            "transformation_specified": False,
            "note": (
                "V, as literally constructed in the paper, has argument "
                "36.586776 degrees, not 45 degrees. No permutation of the "
                "weight-to-angle assignment (24 checked) reaches 45 "
                "degrees. The point (1,1) is at 45 degrees, but no map, "
                "normalization, projection, or limiting operation is "
                "specified in the source connecting V to (1,1). The two "
                "objects do not currently even share the claimed reading, "
                "let alone a specification."
            ),
        },
        "physical_correspondence": {
            "status": "unestablished",
            "evidence_type": None,
            "evidence": [],
        },
    }
    return result


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
