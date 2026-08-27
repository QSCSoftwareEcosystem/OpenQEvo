# Software Source Inventory

Last updated: 2026-06-03

These sources document software behavior for OpenQEvo adapters and the
recommendation execution bridge. External AS/RAG orchestration can cite these
files when explaining why a method is executable, what inputs are required, or
why a planned adapter is non-executable.

| Topic | Source URL or local source | Local raw Markdown | Notes |
|---|---|---|---|
| Qiskit `PauliEvolutionGate` | https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.library.PauliEvolutionGate | [`raw_data/qiskit-pauli-evolution-gate.md`](raw_data/qiskit-pauli-evolution-gate.md) | Documents Pauli time-evolution gate, operator/time inputs, and synthesis behavior. Converted with MarkItDown without Marker. |
| Qiskit `SparsePauliOp` | https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.quantum_info.SparsePauliOp | [`raw_data/qiskit-sparse-pauli-op.md`](raw_data/qiskit-sparse-pauli-op.md) | Documents sparse Pauli operator representation used by Qiskit-backed Pauli decompositions. Converted with MarkItDown without Marker. |
| PennyLane `TrotterProduct` | https://docs.pennylane.ai/en/stable/code/api/pennylane.TrotterProduct.html | [`raw_data/pennylane-trotter-product.md`](raw_data/pennylane-trotter-product.md) | Documents Trotter-product parameters, decomposition, order, and repetition count. Converted with MarkItDown without Marker. |
| PennyLane `ApproxTimeEvolution` | https://docs.pennylane.ai/en/stable/code/api/pennylane.ApproxTimeEvolution.html | [`raw_data/pennylane-approx-time-evolution.md`](raw_data/pennylane-approx-time-evolution.md) | Documents the older approximate time-evolution operator and relation to Trotter behavior. Converted with MarkItDown without Marker. |
| Qrack simulator repository | https://github.com/unitaryfund/qrack | [`raw_data/qrack-readme.md`](raw_data/qrack-readme.md) | Documents Qrack project scope, simulator behavior, and accelerator/backend expectations. Stored from repository Markdown. |
| PyQrack Python package repository | https://github.com/unitaryfund/pyqrack | [`raw_data/pyqrack-readme.md`](raw_data/pyqrack-readme.md) | Documents Python package entry point for Qrack. Stored from repository Markdown. |
| Mitiq zero-noise extrapolation guide | https://mitiq.readthedocs.io/en/stable/guide/zne.html | [`raw_data/mitiq-zne-guide.md`](raw_data/mitiq-zne-guide.md) | Documents ZNE workflow concepts for Mitiq-backed mitigation. Converted with MarkItDown without Marker. |
| Mitiq API reference | https://mitiq.readthedocs.io/en/stable/apidoc.html | [`raw_data/mitiq-api-reference.md`](raw_data/mitiq-api-reference.md) | Documents `execute_with_zne`, factories, and noise-scaling helpers. Converted with MarkItDown without Marker. |
| OpenQEvo recommendation execution bridge | `src/openqevo/execution.py` | [`raw_data/openqevo-execute-recommendation.md`](raw_data/openqevo-execute-recommendation.md) | Documents local `openqevo.execute_recommendation(...)` behavior from project-owned source. |
