"""
tests/basis/test_persistent_constant.py

Basis audit of persist.pdf, Sections 1-2, 4, 6-8: the claimed
"persistent 24/25 constant" in r(L, Pk).

Source claim (verbatim, persist.pdf Section 1):
    r(L, Pk) = |S(Pk,L)| / (phi(Pk)/Pk * L/6) -> 24/25

This test computes r(L, Pk) directly, using the paper's own
Appendix A code unmodified, and separately checks Lemma 1's
refined heuristic against the same data.

Preserves the original claim as provenance. Does not rewrite the
source claim; only records what was independently computed.
"""
from math import gcd
from sympy import totient, primefactors


def residue_count(limit, primorial, residue):
    """Verbatim from persist.pdf Appendix A."""
    count_actual = 0
    for n in range(residue, limit, 6):
        if gcd(n, primorial) == 1:
            count_actual += 1
    density = totient(primorial) / primorial
    predicted = density * (limit / 6)
    return count_actual, predicted, count_actual / predicted


def refined_predicted(limit, primorial):
    """Lemma 1's refined heuristic: 1/6 * prod_{p|Pk, p>3} (1 - 1/p)."""
    dens = 1.0
    for p in primefactors(primorial):
        if p > 3:
            dens *= (1 - 1.0 / p)
    return dens * (limit / 6)


def run():
    Pk = 210  # 2*3*5*7, matches persist.pdf's table
    source_claim = {
        "statement": "r(L, Pk) -> 24/25",
        "location": "persist.pdf Section 1 / Section 8",
    }

    candidates = [10**5, 10**6, 10**7, 10**8]
    naive_results = []
    refined_results = []

    for L in candidates:
        actual, naive_predicted, naive_ratio = residue_count(L, Pk, 5)
        ref_predicted = refined_predicted(L, Pk)
        ref_ratio = actual / ref_predicted
        naive_results.append({
            "L": L, "actual": actual,
            "predicted": float(naive_predicted),
            "ratio": float(naive_ratio),
        })
        refined_results.append({
            "L": L, "actual": actual,
            "predicted": float(ref_predicted),
            "ratio": float(ref_ratio),
        })

    result = {
        "source_claim": source_claim,
        "tested_configuration": {
            "type": "L_sweep",
            "swept_parameter": "L",
            "candidates": candidates,
        },
        "naive_predictor_results": naive_results,
        "refined_predictor_results": refined_results,
        "summary": {
            "naive_ratio_limit_observed": round(naive_results[-1]["ratio"], 6),
            "refined_ratio_limit_observed": round(refined_results[-1]["ratio"], 6),
            "claimed_value": 24 / 25,
            "claim_status": "rejected",
            "note": (
                "r(L,Pk) converges to 3.000000 against the naive predictor "
                "used to define it in the paper, and to 1.000000 against "
                "Lemma 1's own refined heuristic. Neither is 24/25. The "
                "paper's Lemma 1 is correct and, if applied, already "
                "resolves Section 7's stated open problem."
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
