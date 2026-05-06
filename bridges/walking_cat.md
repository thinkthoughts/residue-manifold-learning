# Bridge: Walking Cat Architecture ↔ Residue Manifold Learning

**Bridge file:** `docs/bridges/bridge_walking_cat.md`  
**Primary reference:** *Fault-Tolerant Quantum Computing with Trapped Ions: The Walking Cat Architecture*  
**Paper:** https://arxiv.org/abs/2604.19481

## Core claim

Walking Cat architecture can be read as a **dynamic constraint manifold**:

- local logical states persist inside a code-defined subspace,
- errors are detected through repeated syndrome extraction,
- decoding projects observed behavior back toward valid logical structure,
- modular blocks become repeatable units of constrained computation.

Residue Manifold Learning (RML) models a simpler **static constraint manifold**:

- valid residue classes persist under modular exclusions,
- invalid states are filtered by constraint structure,
- CGCS-style scoring measures coverage, stability, and consistency.

The bridge is not “primes are quantum codes.”  
The bridge is:

> valid structure persists when invalid states are excluded, detected, or projected away.

## Structural mapping

| Walking Cat / FTQC | Residue Manifold Learning |
|---|---|
| logical subspace | admissible residue manifold |
| QLDPC constraints | modular residue constraints |
| syndrome extraction | constraint observation |
| streaming decoder | projection toward valid structure |
| cat-state resources | constraint-enforcement resources |
| modular memory blocks | local residue systems |
| interconnects between modules | consistency links across graph nodes |
| logical coherence | global constraint consistency |

## Local vs distributed scaling

A single Walking Cat module emphasizes local stability:

```text
local code constraints
→ local syndrome extraction
→ local decoding
→ stable logical subspace
```

A distributed architecture shifts emphasis toward links:

```text
many local modules
→ interconnect fidelity + latency
→ cross-node syndrome / state consistency
→ global logical coherence
```

RML gives a compact analogy:

```text
mod30 local residues
→ residue consistency across links
→ graph-level structure persistence
```

## Repo interpretation

This bridge suggests one new experiment direction:

> model several local residue manifolds as graph nodes, introduce noisy links between them, and measure whether global consistency survives.

That experiment does not simulate trapped-ion hardware directly.  
It provides a minimal constraint-system analogue for reasoning about:

- local validity,
- link reliability,
- global consistency,
- stability under noisy connections.

## Proposed notebook

`notebooks/05_distributed_residue_consistency.ipynb`

### Goal

Demonstrate how local constraint systems can remain individually valid while global consistency fails when inter-node links become noisy.

### Minimal experiment

1. Create several local mod30 residue systems.
2. Represent each system as a graph node.
3. Add links between nodes.
4. Corrupt some links with mismatch/noise.
5. Score:
   - local residue coverage,
   - link consistency,
   - global consistency,
   - CGCS-style combined score.

### Suggested figure

```text
local modules → noisy links → global consistency score
```

## Suggested CGCS bridge definition

For this bridge, CGCS can be interpreted as:

```text
CGCS = local coverage × link consistency × global stability
```

Where:

- **local coverage** measures whether each node preserves expected admissible residue structure,
- **link consistency** measures whether connected nodes agree on compatible residue relationships,
- **global stability** measures whether consistency survives across the full graph.

This keeps CGCS simple enough for a first repo bridge while leaving room for later mathematical refinement.

## Tweet-sized summary

Walking Cat = dynamic constraint manifold.  
RML = static residue constraint manifold.  

Local FTQC solves local stability.  
Distributed FTQC shifts focus to link consistency.

mod30 → local residues  
multi-node → global consistency 📐

## Future bridge files

Possible next bridge documents:

- `bridge_qldpc.md`
- `bridge_decoder_projection.md`
- `bridge_distributed_ftqc.md`
- `bridge_modular_quantum_networks.md`
- `bridge_constraint_graphs.md`
