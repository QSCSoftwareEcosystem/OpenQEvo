# Trotterization Source Inventory

OpenQEvo keeps converted paper markdown in `raw_data/` so the local context is usable without QAppsWiki. Extracted concepts from those sources live in `key_points/`. Method metadata and selection rules live at `../methods/` and `../selection/`. Raw PDFs remain in `../../../QAppsWiki/raw/pdf/` from this file.

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

## Legacy conversions and source identities

These preserved paths were not previously inventoried. The preferred path is
an editorial retrieval alias based on matching title/identifier, not proof of
byte equality or matching publication version. Original acquisition date,
converter, and source PDF are unknown for these legacy files. Do not infer
provenance from a `DOI_` filename alone; the header or canonical inventory row
provides the identity. The canonical converted sources above remain preferred.

| Source ID | Preserved path | Classification / preferred local alias |
| --- | --- | --- |
| `sugisaki-fmo-2024` | [DOI_10.1002_jcc.27438.md](raw_data/DOI_10.1002_jcc.27438.md) | Legacy conversion; prefer [openqevo-trotter-sugisaki-fmo-2024-2402.17993.md](raw_data/openqevo-trotter-sugisaki-fmo-2024-2402.17993.md). |
| `grimsley-uccsd-2020` | [DOI_10.1021_acs.jctc.9b01083.md](raw_data/DOI_10.1021_acs.jctc.9b01083.md) | Legacy conversion; prefer [openqevo-trotter-grimsley-2020-1910.10329.md](raw_data/openqevo-trotter-grimsley-2020-1910.10329.md). |
| `sugisaki-qpe-2024` | [DOI_10.1063_5.0223661.md](raw_data/DOI_10.1063_5.0223661.md) | Legacy conversion; prefer [openqevo-trotter-sugisaki-qpe-2024-2406.09830.md](raw_data/openqevo-trotter-sugisaki-qpe-2024-2406.09830.md). |
| `gonzalez-garcia-dissipation-2025` | [DOI_10.1103_rd56-b8tc.md](raw_data/DOI_10.1103_rd56-b8tc.md) | Legacy conversion; prefer [openqevo-trotter-gonzalez-garcia-2025-2502.05658.md](raw_data/openqevo-trotter-gonzalez-garcia-2025-2502.05658.md). |
| `rajput-interaction-2022` | [DOI_10.22331.md](raw_data/DOI_10.22331.md) | Legacy conversion; prefer [openqevo-trotter-rajput-2022-q-2022-08-17-780.md](raw_data/openqevo-trotter-rajput-2022-q-2022-08-17-780.md). |
| `tranter-ordering-2019` | [DOI_10.3390.md](raw_data/DOI_10.3390.md) | Legacy conversion; prefer [openqevo-trotter-tranter-2019-1912.07555.md](raw_data/openqevo-trotter-tranter-2019-1912.07555.md). |
| `gonzalez-garcia-dissipation-2025` | [DOI_10.48550.md](raw_data/DOI_10.48550.md) | Legacy conversion; prefer [openqevo-trotter-gonzalez-garcia-2025-2502.05658.md](raw_data/openqevo-trotter-gonzalez-garcia-2025-2502.05658.md). |
| `yang-symmetry-2025` | [DOI_2505.04552.md](raw_data/DOI_2505.04552.md) | Legacy conversion; prefer [openqevo-trotter-yang-2025-2505.04552.md](raw_data/openqevo-trotter-yang-2025-2505.04552.md). |
| `grimsley-uccsd-2020` | [Grimsley2020.md](raw_data/Grimsley2020.md) | Legacy conversion; prefer [openqevo-trotter-grimsley-2020-1910.10329.md](raw_data/openqevo-trotter-grimsley-2020-1910.10329.md). |
| `gonzalez-garcia-dissipation-2025` | [gonzalez2025.md](raw_data/gonzalez2025.md) | Legacy conversion; prefer [openqevo-trotter-gonzalez-garcia-2025-2502.05658.md](raw_data/openqevo-trotter-gonzalez-garcia-2025-2502.05658.md). |

The same source IDs apply to the preferred aliases in this table; they identify
works, not a validated publication-version match. The additional
[`raw_data/tmp/gonzalez2025.md`](raw_data/tmp/gonzalez2025.md) is conversion
scratch for `gonzalez-garcia-dissipation-2025`; retain for recovery, exclude from
curated evidence selection. Image files are extraction companions, not papers.
