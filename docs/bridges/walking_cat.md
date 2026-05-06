🧩 Bridge: Walking Cat Architecture ↔ Residue Manifold Learning

 (arXiv https://arxiv.org/abs/2604.19481)

Core claim (1–2 lines):
Walking-cat FTQC implements a dynamic constraint manifold (LDPC + decoding).
RML models a static constraint manifold (modular residues + CGCS).

Mapping
logical subspace ↔ admissible residues
LDPC constraints ↔ modular constraints
decoder projection ↔ constraint scoring (CGCS)
cat-state resources ↔ constraint enforcement
modular blocks ↔ local residue systems
Distributed extension

Single module → local constraint satisfaction
Multi-module → constraint consistency across links

mod30 → local residues
network → global consistency 📐

Next step (repo)
add notebook: distributed residue consistency
define CGCS as link-level consistency metric
add simple graph experiment (nodes + noisy edges)
