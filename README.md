# London Geospatial Representations

Code and selected results for the UCL GEOG0105 MSc dissertation:

> **Evaluating Multimodal Geospatial Representations for Spatially Generalisable Urban Prediction in London: Evidence from PTAL and EPC**

[View the project website](https://xinpeng00.github.io/london-geospatial-representations/) · [Browse the notebooks](notebooks/) · [Read the data notes](data/README.md)

## Overview

This project evaluates whether frozen pretrained geospatial representations provide useful and spatially transferable information for two urban prediction tasks in Greater London:

- **PTAL:** prediction of the 2023 Transport for London Public Transport Access Level Access Index for 6,597 sampled grid locations.
- **EPC:** prediction of postcode-mean current-energy-efficiency scores for 20,000 sampled postcodes.

Five representation families are compared: DINOv2 aerial imagery (768D), Street View CLIP (512D), SatCLIP location (256D), TESSERA Earth observation (128D), and AlphaEarth / Google Satellite Embedding (64D). The primary analysis uses Ridge regression with fold-local preprocessing and nested borough-held-out cross-validation.

## Main findings

- For PTAL, the spatial-control baseline achieved mean held-out R² = **0.401**. The strongest individual representations were AlphaEarth (**0.615**), Street View CLIP (**0.613**), and DINOv2 (**0.595**).
- Street View content plus availability metadata reached **0.661**; street-level and aerial fusion reached **0.673**; all representations plus Street View availability metadata reached **0.693**.
- PTAL performance declined under stricter continuous-region validation, while representation models retained more predictive value than spatial controls alone.
- For EPC, rich property controls were stronger than representation-only models. TESSERA provided a small positive increment beyond those controls, while broader fusion was largely redundant once construction-age and floor-area information were included. The compact-to-rich control improvement was driven primarily by construction-age information, with median floor area adding very little.
- Representation models reduced residual spatial autocorrelation but did not eliminate it.

All values above are mean outer-fold R² from the frozen final analysis. The study evaluates transfer within London; it does not claim external-city generalisation.

## Repository structure

```text
notebooks/
  upstream/                    Source and embedding preparation (00a–00d)
  01_...ipynb – 16_...ipynb   Final analysis and reporting sequence
src/config.py                  Shared path and analysis configuration
results/selected_tables/       Compact machine-readable summaries
data/README.md                 Data access and redistribution boundaries
docs/                          GitHub Pages project website
```

Notebook outputs are removed in this public repository to keep the code reviewable and avoid embedding derived or restricted assets. The private frozen analysis archive retains the executed versions and canonical outputs.

## Analysis sequence

| Step | Notebook | Purpose |
|---:|---|---|
| 01 | `01_data_audit_and_sample_construction.ipynb` | Audit source tables and construct corrected samples. |
| 02 | `02_alphaearth_missing_audit.ipynb` | Resolve boundary/sliver non-intersections. |
| 03 | `03_common_sample_and_representation_audit.ipynb` | Freeze the common 26,597-row sample. |
| 04 | `04_data_provenance_and_temporal_audit.ipynb` | Audit dates, support and modality provenance. |
| 05 | `05_unified_final_feature_table.ipynb` | Construct the canonical feature table and manifests. |
| 06 | `06_final_ridge_representation_benchmark.ipynb` | Run the primary nested spatial benchmark. |
| 07 | `07_controls_incremental_value_and_control_ablation.ipynb` | Estimate incremental value beyond matched controls. |
| 08 | `08_random_vs_spatial_cv_sensitivity.ipynb` | Compare random and borough-held-out validation. |
| 09 | `09_targeted_dinov2_satclip_combination.ipynb` | Test targeted aerial-location fusion. |
| 10 | `10_pca64_representation_dimension_sensitivity.ipynb` | Test fold-local PCA-to-64D sensitivity. |
| 11 | `11_geometric_spatial_blocks_and_residual_diagnostics.ipynb` | Test continuous regions and residual Moran's I. |
| 12 | `12_selected_xgboost_nonlinearity_robustness.ipynb` | Compare selected XGBoost and Ridge models. |
| 13 | `13_gatv2_neighbourhood_robustness.ipynb` | Compare GATv2 with matched MLP baselines. |
| 14 | `14_epc_reliability_and_record_timing_sensitivity.ipynb` | Test EPC reliability and record timing. |
| 15 | `15_success_failure_case_diagnostics.ipynb` | Diagnose held-out successes and failures. |
| 16 | `16_dissertation_figures_tables_FINAL.ipynb` | Generate final figures and tables from frozen outputs. |

The four upstream notebooks document source preparation and extraction of the frozen representation inputs.

## Reproduction

1. Create an environment using `requirements.txt`.
2. Reconstruct the private data layout described in [`data/README.md`](data/README.md).
3. Update the project root in `src/config.py` if the Drive directory differs.
4. Run the upstream notebooks only when representation inputs must be regenerated; otherwise begin with notebook 01.
5. Run notebooks 01–16 in order.

Exact reproduction requires authorised access to the licensed/private source assets. No credentials, API keys, raw imagery, full embeddings, or large model tables are included.

## Citation

See [`CITATION.cff`](CITATION.cff). Code is released under the MIT License; third-party data and pretrained models remain subject to their original terms, as described in [`NOTICE.md`](NOTICE.md).
