import os
from pathlib import Path

# Project root. Override GEOG0105_PROJECT_ROOT when the shared folder is mounted elsewhere.
BASE_DIR = Path(os.environ.get("GEOG0105_PROJECT_ROOT", "/content/drive/MyDrive/GEOG0105"))

RAW_DIR = BASE_DIR / "Raw Data"
CODE_DIR = BASE_DIR / "CODE"
OUTPUT_DIR = BASE_DIR / "Outputs"
TABLE_DIR = OUTPUT_DIR / "tables"
EMBED_DIR = OUTPUT_DIR / "embeddings"

FINAL_CODE_DIR = CODE_DIR / "FINAL_PIPELINE"
FINAL_OUTPUT_DIR = OUTPUT_DIR / "final_pipeline"
AUDIT_DIR = FINAL_OUTPUT_DIR / "audit"
FINAL_TABLE_DIR = FINAL_OUTPUT_DIR / "tables"
FINAL_EMBED_DIR = FINAL_OUTPUT_DIR / "embeddings"
FINAL_MODEL_DIR = FINAL_OUTPUT_DIR / "models"
FINAL_FIGURE_DIR = FINAL_OUTPUT_DIR / "figures"

for p in [
    FINAL_OUTPUT_DIR, AUDIT_DIR, FINAL_TABLE_DIR,
    FINAL_EMBED_DIR, FINAL_MODEL_DIR, FINAL_FIGURE_DIR
]:
    p.mkdir(parents=True, exist_ok=True)

# Core raw inputs
EPC_FILE = RAW_DIR / "EPC Data.csv"
PTAL_DIR = RAW_DIR / "PTAL"
POSTCODE_DIR = RAW_DIR / "Postcode_CSV"
BOUNDARY_DIR = RAW_DIR / "London_boundary"
ALPHA_GPKG_PATH = RAW_DIR / "AlphaEarth" / "extracted-lsoa-geopackage_2024_output.gpkg"

# Existing legacy outputs retained for comparison
LEGACY_EPC_CLEAN = TABLE_DIR / "epc_samples_clean.csv"
LEGACY_PTAL_CLEAN = TABLE_DIR / "ptal_samples_clean.csv"
LEGACY_MASTER_CLEAN = TABLE_DIR / "sample_master_clean.csv"
DINO_SAMPLE_PATH = TABLE_DIR / "dino_londonwide_sample.csv"
AERIAL_CROP_SOURCE_INDEX_PATH = TABLE_DIR / "aerial_crop_source_index_all.csv"

# Existing embeddings
ALPHA_EMB_PATH = EMBED_DIR / "alphaearth_2024_embeddings_dino_sample.parquet"
DINO2_EMB_PATH = EMBED_DIR / "dinov2_aerial_embeddings_dino_sample.parquet"
STREET_EMB_PATH = EMBED_DIR / "streetview_clip_dino_sample_embeddings.parquet"
TESSERA_EMB_PATH = EMBED_DIR / "tessera_embeddings_dino_sample.parquet"
SATCLIP_EMB_PATH = EMBED_DIR / "satclip_embeddings_full.parquet"

# Final-pipeline outputs created after audit.
EPC_20K_FINAL_CANDIDATE = FINAL_TABLE_DIR / "epc_20k_final_candidate.parquet"
ALPHA_FINAL_PATH = FINAL_EMBED_DIR / "alphaearth_2024_embeddings_dino_sample_final.parquet"

# Final common-sample / audit outputs.
COMMON_SAMPLE_FINAL_PATH = FINAL_TABLE_DIR / "common_sample_final.parquet"
REPRESENTATION_INVENTORY_PATH = AUDIT_DIR / "representation_inventory.csv"
SAMPLE_REPRESENTATIVENESS_PATH = AUDIT_DIR / "sample_representativeness_summary.csv"

# Canonical London borough codes/names (ONS E09 London borough geography).
LONDON_BOROUGH_CODE_TO_NAME = {
    "E09000001": "City of London",
    "E09000002": "Barking and Dagenham",
    "E09000003": "Barnet",
    "E09000004": "Bexley",
    "E09000005": "Brent",
    "E09000006": "Bromley",
    "E09000007": "Camden",
    "E09000008": "Croydon",
    "E09000009": "Ealing",
    "E09000010": "Enfield",
    "E09000011": "Greenwich",
    "E09000012": "Hackney",
    "E09000013": "Hammersmith and Fulham",
    "E09000014": "Haringey",
    "E09000015": "Harrow",
    "E09000016": "Havering",
    "E09000017": "Hillingdon",
    "E09000018": "Hounslow",
    "E09000019": "Islington",
    "E09000020": "Kensington and Chelsea",
    "E09000021": "Kingston upon Thames",
    "E09000022": "Lambeth",
    "E09000023": "Lewisham",
    "E09000024": "Merton",
    "E09000025": "Newham",
    "E09000026": "Redbridge",
    "E09000027": "Richmond upon Thames",
    "E09000028": "Southwark",
    "E09000029": "Sutton",
    "E09000030": "Tower Hamlets",
    "E09000031": "Waltham Forest",
    "E09000032": "Wandsworth",
    "E09000033": "Westminster",
}
LONDON_BOROUGH_NAME_TO_CODE = {
    name: code for code, name in LONDON_BOROUGH_CODE_TO_NAME.items()
}

COMMON_AUDIT_SUMMARY_PATH = AUDIT_DIR / "03_common_sample_audit_summary.json"
SAMPLE_DESIGN_EFFECT_PATH = AUDIT_DIR / "sample_design_effect_summary.csv"

# Provenance / temporal audit outputs.
PROVENANCE_TABLE_PATH = AUDIT_DIR / "modality_provenance_table.csv"
TEMPORAL_ALIGNMENT_SUMMARY_PATH = AUDIT_DIR / "temporal_alignment_summary.json"
AERIAL_METADATA_AUDIT_PATH = AUDIT_DIR / "aerial_25cm_metadata_audit.csv"
AERIAL_METADATA_SUMMARY_PATH = AUDIT_DIR / "aerial_25cm_metadata_summary.json"
AERIAL_SAMPLE_TEMPORAL_AUDIT_PATH = AUDIT_DIR / "aerial_sample_temporal_audit.csv"
AERIAL_SAMPLE_TEMPORAL_SUMMARY_PATH = AUDIT_DIR / "aerial_sample_temporal_summary.json"
STREETVIEW_TEMPORAL_AUDIT_PATH = AUDIT_DIR / "streetview_temporal_metadata_audit.json"
TESSERA_PROVENANCE_EVIDENCE_PATH = AUDIT_DIR / "tessera_provenance_evidence.txt"
PROVENANCE_AUDIT_SUMMARY_PATH = AUDIT_DIR / "04_provenance_audit_summary.json"

# Notebook 05: canonical feature-table and manifest outputs.
FINAL_MODEL_TABLE_PATH = FINAL_TABLE_DIR / "final_model_table.parquet"
FEATURE_MANIFEST_JSON_PATH = AUDIT_DIR / "feature_manifest.json"
FEATURE_MANIFEST_CSV_PATH = AUDIT_DIR / "feature_manifest.csv"
FINAL_MODEL_MISSINGNESS_PATH = AUDIT_DIR / "final_model_table_missingness.csv"
FINAL_MODEL_AUDIT_SUMMARY_PATH = AUDIT_DIR / "05_final_model_table_audit_summary.json"
DESIGN_REVIEW_PATH = AUDIT_DIR / "04_professor_design_review.md"
STREETVIEW_SEGMENT_AUDIT_PATH = AUDIT_DIR / "streetview_segment_length_audit.json"

# Fixed reference used only for interpretable coordinate controls.
# Approximately central London / Charing Cross in British National Grid.
LONDON_CENTRE_EASTING = 530000.0
LONDON_CENTRE_NORTHING = 180000.0

# Notebook 06: final Ridge linear-probe benchmark.
RIDGE_CORE_RESULTS_PATH = FINAL_MODEL_DIR / "06_ridge_core_fold_results.csv"
RIDGE_CORE_PREDICTIONS_PATH = FINAL_MODEL_DIR / "06_ridge_core_predictions.parquet"
RIDGE_CORE_SUMMARY_PATH = FINAL_MODEL_DIR / "06_ridge_core_summary.csv"
RIDGE_OUTER_FOLDS_PATH = AUDIT_DIR / "06_ridge_outer_fold_assignments.csv"
RIDGE_RUN_SPEC_PATH = AUDIT_DIR / "06_ridge_run_spec.json"
RIDGE_CORE_AUDIT_PATH = AUDIT_DIR / "06_ridge_core_audit_summary.json"
RIDGE_CHUNK_DIR = FINAL_MODEL_DIR / "06_ridge_chunks"
RIDGE_CHUNK_DIR.mkdir(parents=True, exist_ok=True)

# Notebook 07: incremental value beyond controls and EPC control ablation.
INCREMENTAL_RESULTS_PATH = FINAL_MODEL_DIR / "07_incremental_fold_results.csv"
INCREMENTAL_PREDICTIONS_PATH = FINAL_MODEL_DIR / "07_incremental_predictions.parquet"
INCREMENTAL_SUMMARY_PATH = FINAL_MODEL_DIR / "07_incremental_summary.csv"
INCREMENTAL_DELTAS_PATH = FINAL_MODEL_DIR / "07_paired_deltas_by_fold.csv"
INCREMENTAL_DELTA_SUMMARY_PATH = FINAL_MODEL_DIR / "07_paired_delta_summary.csv"
INCREMENTAL_ABLATION_SUMMARY_PATH = FINAL_MODEL_DIR / "07_epc_control_ablation_summary.csv"
INCREMENTAL_RUN_SPEC_PATH = AUDIT_DIR / "07_incremental_run_spec.json"
INCREMENTAL_AUDIT_PATH = AUDIT_DIR / "07_incremental_audit_summary.json"
INCREMENTAL_CHUNK_DIR = FINAL_MODEL_DIR / "07_incremental_chunks"
INCREMENTAL_CHUNK_DIR.mkdir(parents=True, exist_ok=True)

# Notebook 08: random-vs-borough spatial-CV sensitivity.
RANDOM_CV_RESULTS_PATH = FINAL_MODEL_DIR / "08_random_cv_fold_results.csv"
RANDOM_CV_PREDICTIONS_PATH = FINAL_MODEL_DIR / "08_random_cv_predictions.parquet"
RANDOM_VS_SPATIAL_SUMMARY_PATH = FINAL_MODEL_DIR / "08_random_vs_borough_summary.csv"
RANDOM_OUTER_FOLDS_PATH = AUDIT_DIR / "08_random_outer_fold_assignments.csv"
RANDOM_CV_RUN_SPEC_PATH = AUDIT_DIR / "08_random_cv_run_spec.json"
RANDOM_CV_AUDIT_PATH = AUDIT_DIR / "08_random_cv_audit_summary.json"
RANDOM_CV_CHUNK_DIR = FINAL_MODEL_DIR / "08_random_cv_chunks"
RANDOM_CV_CHUNK_DIR.mkdir(parents=True, exist_ok=True)

# Notebook 09: targeted DINOv2 + SatCLIP image-location combination.
IMAGE_LOCATION_RESULTS_PATH = FINAL_MODEL_DIR / "09_dinov2_satclip_fold_results.csv"
IMAGE_LOCATION_PREDICTIONS_PATH = FINAL_MODEL_DIR / "09_dinov2_satclip_predictions.parquet"
IMAGE_LOCATION_SUMMARY_PATH = FINAL_MODEL_DIR / "09_dinov2_satclip_summary.csv"
IMAGE_LOCATION_DELTAS_PATH = FINAL_MODEL_DIR / "09_dinov2_satclip_paired_comparisons_by_fold.csv"
IMAGE_LOCATION_COMPARISON_SUMMARY_PATH = FINAL_MODEL_DIR / "09_dinov2_satclip_comparison_summary.csv"
IMAGE_LOCATION_RUN_SPEC_PATH = AUDIT_DIR / "09_dinov2_satclip_run_spec.json"
IMAGE_LOCATION_AUDIT_PATH = AUDIT_DIR / "09_dinov2_satclip_audit_summary.json"
IMAGE_LOCATION_CHUNK_DIR = FINAL_MODEL_DIR / "09_dinov2_satclip_chunks"
IMAGE_LOCATION_CHUNK_DIR.mkdir(parents=True, exist_ok=True)

# Notebook 10: fold-local PCA-to-64D representation-dimension sensitivity.
PCA64_RESULTS_PATH = FINAL_MODEL_DIR / "10_pca64_fold_results.csv"
PCA64_PREDICTIONS_PATH = FINAL_MODEL_DIR / "10_pca64_predictions.parquet"
PCA64_SUMMARY_PATH = FINAL_MODEL_DIR / "10_pca64_summary.csv"
PCA64_DELTAS_PATH = FINAL_MODEL_DIR / "10_pca64_native_paired_deltas_by_fold.csv"
PCA64_COMPARISON_SUMMARY_PATH = FINAL_MODEL_DIR / "10_pca64_native_comparison_summary.csv"
PCA64_RANK_SUMMARY_PATH = FINAL_MODEL_DIR / "10_pca64_rank_stability.csv"
PCA64_RUN_SPEC_PATH = AUDIT_DIR / "10_pca64_run_spec.json"
PCA64_AUDIT_PATH = AUDIT_DIR / "10_pca64_audit_summary.json"
PCA64_CHUNK_DIR = FINAL_MODEL_DIR / "10_pca64_chunks"
PCA64_CHUNK_DIR.mkdir(parents=True, exist_ok=True)

# Notebook 11: target-independent geometric-block CV and OOF residual diagnostics.
GEOMETRIC_CV_RESULTS_PATH = FINAL_MODEL_DIR / "11_geometric_cv_fold_results.csv"
GEOMETRIC_CV_REFINED_RESULTS_PATH = FINAL_MODEL_DIR / "11_geometric_cv_fold_results_refined.csv"
GEOMETRIC_CV_PREDICTIONS_PATH = FINAL_MODEL_DIR / "11_geometric_cv_predictions.parquet"
GEOMETRIC_PROTOCOL_SUMMARY_PATH = FINAL_MODEL_DIR / "11_three_protocol_summary.csv"
GEOMETRIC_PROTOCOL_COMPARISON_PATH = FINAL_MODEL_DIR / "11_three_protocol_comparison.csv"
GEOMETRIC_RESIDUAL_MORAN_PATH = FINAL_MODEL_DIR / "11_residual_moran_summary.csv"
GEOMETRIC_RESIDUAL_FOLD_PATH = FINAL_MODEL_DIR / "11_residual_fold_summary.csv"
GEOMETRIC_OUTER_FOLDS_PATH = AUDIT_DIR / "11_geometric_outer_fold_assignments.csv"
GEOMETRIC_BLOCK_QA_PATH = AUDIT_DIR / "11_geometric_block_qa.csv"
GEOMETRIC_RUN_SPEC_PATH = AUDIT_DIR / "11_geometric_cv_run_spec.json"
GEOMETRIC_AUDIT_PATH = AUDIT_DIR / "11_geometric_cv_audit_summary.json"
GEOMETRIC_ALPHA_REFINEMENT_SPEC_PATH = AUDIT_DIR / "11_geometric_alpha_refinement_spec.json"
GEOMETRIC_ALPHA_REFINEMENT_RESULTS_PATH = FINAL_MODEL_DIR / "11_geometric_alpha_refinement_fold_results.csv"
GEOMETRIC_ALPHA_REFINEMENT_COMPARISON_PATH = FINAL_MODEL_DIR / "11_geometric_alpha_refinement_comparison.csv"
GEOMETRIC_CV_CHUNK_DIR = FINAL_MODEL_DIR / "11_geometric_cv_chunks"
GEOMETRIC_CV_CHUNK_DIR.mkdir(parents=True, exist_ok=True)

# Notebook 12: selected XGBoost non-linearity robustness check.
XGBOOST_RESULTS_PATH = FINAL_MODEL_DIR / "12_xgboost_fold_results.csv"
XGBOOST_PREDICTIONS_PATH = FINAL_MODEL_DIR / "12_xgboost_predictions.parquet"
XGBOOST_SUMMARY_PATH = FINAL_MODEL_DIR / "12_xgboost_summary.csv"
XGBOOST_VS_RIDGE_FOLD_PATH = FINAL_MODEL_DIR / "12_xgboost_vs_ridge_by_fold.csv"
XGBOOST_VS_RIDGE_SUMMARY_PATH = FINAL_MODEL_DIR / "12_xgboost_vs_ridge_summary.csv"
XGBOOST_INCREMENTAL_FOLD_PATH = FINAL_MODEL_DIR / "12_xgboost_incremental_by_fold.csv"
XGBOOST_INCREMENTAL_SUMMARY_PATH = FINAL_MODEL_DIR / "12_xgboost_incremental_summary.csv"
XGBOOST_RUN_SPEC_PATH = AUDIT_DIR / "12_xgboost_run_spec.json"
XGBOOST_AUDIT_PATH = AUDIT_DIR / "12_xgboost_audit_summary.json"
XGBOOST_CHUNK_DIR = FINAL_MODEL_DIR / "12_xgboost_chunks"
XGBOOST_CHUNK_DIR.mkdir(parents=True, exist_ok=True)

# Notebook 13: selected GATv2 neighbourhood robustness check.
# The first run remains preserved because its integrity gate passed, but its
# 250-epoch interpretation gate identified two repeated ceiling hits.
GATV2_V1_RESULTS_PATH = FINAL_MODEL_DIR / "13_gatv2_fold_results.csv"
GATV2_V1_AUDIT_PATH = AUDIT_DIR / "13_gatv2_audit_summary.json"

# The complete 500-epoch run also remains preserved. Its formal gate passed,
# but three PTAL-baseline MLP folds selected epochs 499/500/500, so the final
# run uses a near-boundary rule rather than checking exact equality only.
GATV2_V2_RESULTS_PATH = FINAL_MODEL_DIR / "13_gatv2_v2_fold_results.csv"
GATV2_V2_AUDIT_PATH = AUDIT_DIR / "13_gatv2_v2_audit_summary.json"

# Canonical final run: maximum epochs 1000; every other setting remains fixed.
GATV2_RESULTS_PATH = FINAL_MODEL_DIR / "13_gatv2_v3_fold_results.csv"
GATV2_PREDICTIONS_PATH = FINAL_MODEL_DIR / "13_gatv2_v3_predictions.parquet"
GATV2_SUMMARY_PATH = FINAL_MODEL_DIR / "13_gatv2_v3_summary.csv"
GATV2_VS_MLP_FOLD_PATH = FINAL_MODEL_DIR / "13_gatv2_v3_vs_mlp_by_fold.csv"
GATV2_VS_MLP_SUMMARY_PATH = FINAL_MODEL_DIR / "13_gatv2_v3_vs_mlp_summary.csv"
GATV2_INCREMENTAL_FOLD_PATH = FINAL_MODEL_DIR / "13_gatv2_v3_incremental_by_fold.csv"
GATV2_INCREMENTAL_SUMMARY_PATH = FINAL_MODEL_DIR / "13_gatv2_v3_incremental_summary.csv"
GATV2_REFERENCE_SUMMARY_PATH = FINAL_MODEL_DIR / "13_gatv2_v3_model_reference_summary.csv"
GATV2_RUN_SPEC_PATH = AUDIT_DIR / "13_gatv2_v3_run_spec.json"
GATV2_AUDIT_PATH = AUDIT_DIR / "13_gatv2_v3_audit_summary.json"
GATV2_CHUNK_DIR = FINAL_MODEL_DIR / "13_gatv2_v3_chunks"
GATV2_CHUNK_DIR.mkdir(parents=True, exist_ok=True)

# Notebook 14: EPC target reliability and record-timing sensitivity.
EPC_ROBUST_RESULTS_PATH = FINAL_MODEL_DIR / "14_epc_robustness_fold_results.csv"
EPC_ROBUST_PREDICTIONS_PATH = FINAL_MODEL_DIR / "14_epc_robustness_predictions.parquet"
EPC_ROBUST_SUMMARY_PATH = FINAL_MODEL_DIR / "14_epc_robustness_summary.csv"
EPC_ROBUST_INCREMENTAL_FOLD_PATH = FINAL_MODEL_DIR / "14_epc_robustness_incremental_by_fold.csv"
EPC_ROBUST_INCREMENTAL_SUMMARY_PATH = FINAL_MODEL_DIR / "14_epc_robustness_incremental_summary.csv"
EPC_TARGET_SENSITIVITY_PATH = FINAL_MODEL_DIR / "14_uprn_target_sensitivity.csv"
EPC_YEAR_SENSITIVITY_PATH = FINAL_MODEL_DIR / "14_record_year_model_sensitivity.csv"
EPC_TEMPORAL_RESIDUAL_PATH = FINAL_MODEL_DIR / "14_record_year_residual_diagnostic.csv"
EPC_TEMPORAL_BIN_PATH = FINAL_MODEL_DIR / "14_record_year_residual_bins.csv"
EPC_RELIABILITY_DESCRIPTIVE_PATH = FINAL_MODEL_DIR / "14_epc_reliability_descriptive.csv"
EPC_ROBUST_RUN_SPEC_PATH = AUDIT_DIR / "14_epc_robustness_run_spec.json"
EPC_ROBUST_AUDIT_PATH = AUDIT_DIR / "14_epc_robustness_audit_summary.json"
EPC_ROBUST_CHUNK_DIR = FINAL_MODEL_DIR / "14_epc_robustness_chunks"
EPC_ROBUST_CHUNK_DIR.mkdir(parents=True, exist_ok=True)

# Pre-specified nested-CV settings for the primary linear probe.
RIDGE_OUTER_SPLITS = 5
RIDGE_INNER_SPLITS = 3
RIDGE_ALPHA_GRID = [1e-3, 1e-2, 1e-1, 1.0, 10.0, 100.0, 1e3, 1e4, 1e5]

# Reproducibility
RANDOM_STATE = 42

# Current experimental settings. These are design choices and receive sensitivity checks later.
PTAL_SAMPLE_GRID_M = 500
PTAL_AERIAL_CROP_M = 300
EPC_AERIAL_CROP_M = 150

STREETVIEW_PTAL_K = 8
STREETVIEW_PTAL_RADIUS_M = 300
STREETVIEW_EPC_K = 4
STREETVIEW_EPC_RADIUS_M = 150
STREETVIEW_DISTANCE_OFFSET_M = 10

# Conservative AlphaEarth nearest-polygon fallback.
# The audit found the 12 current unmatched points are all within ~15 m.
ALPHA_NEAREST_MAX_DISTANCE_M = 50

