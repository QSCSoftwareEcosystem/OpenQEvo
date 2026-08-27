# Trotterization Source Inventory

OpenQEvo keeps converted paper markdown in `raw_data/` so the local context is usable without QAppsWiki. Extracted concepts from those sources live in `key_points/`. Method metadata and selection rules live at `../../methods/` and `../../selection/`. Raw PDFs remain in `../../../QAppsWiki/raw/pdf/` from this file.

## Converted raw sources

| Topic | Raw PDF | Local markdown | Notes |
| :--- | :--- | :--- | :--- |
| Trotter ordering in electronic structure | `QAppsWiki/raw/pdf/openqevo-trotter-tranter-2019-1912.07555.pdf` | [`raw_data/openqevo-trotter-tranter-2019-1912.07555.md`](raw_data/openqevo-trotter-tranter-2019-1912.07555.md) | arXiv copy used because the publisher PDF endpoint was blocked; converted with `mid`/Marker using GPU. |
| Hamiltonian partitioning and Trotter error estimates | `QAppsWiki/raw/pdf/openqevo-trotter-mehendale-2025-2312.13282.pdf` | [`raw_data/openqevo-trotter-mehendale-2025-2312.13282.md`](raw_data/openqevo-trotter-mehendale-2025-2312.13282.md) | arXiv source; converted with `mid`/Marker using GPU. |
| Interaction-picture hybrid simulation | `QAppsWiki/raw/pdf/openqevo-trotter-rajput-2022-q-2022-08-17-780.pdf` | [`raw_data/openqevo-trotter-rajput-2022-q-2022-08-17-780.md`](raw_data/openqevo-trotter-rajput-2022-q-2022-08-17-780.md) | Quantum journal source; converted with `mid`/Marker using GPU. |
| Symmetry-based noise-robust Trotter decomposition | `QAppsWiki/raw/pdf/openqevo-trotter-yang-2025-2505.04552.pdf` | [`raw_data/openqevo-trotter-yang-2025-2505.04552.md`](raw_data/openqevo-trotter-yang-2025-2505.04552.md) | arXiv source; converted with `mid`/Marker using GPU. |
| Dissipative non-Gaussian many-body dynamics | `QAppsWiki/raw/pdf/openqevo-trotter-gonzalez-garcia-2025-2502.05658.pdf` | [`raw_data/openqevo-trotter-gonzalez-garcia-2025-2502.05658.md`](raw_data/openqevo-trotter-gonzalez-garcia-2025-2502.05658.md) | arXiv source; converted with `mid`/Marker using GPU. |
| Trotterized UCCSD chemical well-definedness | `QAppsWiki/raw/pdf/openqevo-trotter-grimsley-2020-1910.10329.pdf` | [`raw_data/openqevo-trotter-grimsley-2020-1910.10329.md`](raw_data/openqevo-trotter-grimsley-2020-1910.10329.md) | DOI/title in `trotter.md` corrected to match this paper; converted with `mid`/Marker using GPU. |
| VQE-UCCSD size consistency with FMO | `QAppsWiki/raw/pdf/openqevo-trotter-sugisaki-fmo-2024-2402.17993.pdf` | [`raw_data/openqevo-trotter-sugisaki-fmo-2024-2402.17993.md`](raw_data/openqevo-trotter-sugisaki-fmo-2024-2402.17993.md) | DOI in `trotter.md` corrected to `10.1002/jcc.27438`; converted with `mid`/Marker using GPU. |
| QPE full-CI size consistency with Trotter decomposition | `QAppsWiki/raw/pdf/openqevo-trotter-sugisaki-qpe-2024-2406.09830.pdf` | [`raw_data/openqevo-trotter-sugisaki-qpe-2024-2406.09830.md`](raw_data/openqevo-trotter-sugisaki-qpe-2024-2406.09830.md) | Converted with `mid`/Marker using GPU page-by-page after whole-document conversion exceeded GPU memory. |
| Suzuki generalized Trotter formula | `QAppsWiki/raw/pdf/openqevo-trotter-suzuki-1976-10.1007-BF01609348.pdf` | [`raw_data/openqevo-trotter-suzuki-1976-10.1007-BF01609348.md`](raw_data/openqevo-trotter-suzuki-1976-10.1007-BF01609348.md) | Springer source; converted with `mid`/Marker using GPU. |

## Not yet acquired

| Source | Reason |
| :--- | :--- |
| Suzuki 1991, DOI `10.1063/1.529425` | Publisher PDF endpoint returned HTTP 403. |
| Moler and Van Loan matrix exponential paper, DOI `10.1137/S00361445024180` | Publisher PDF endpoint returned HTTP 403. |
