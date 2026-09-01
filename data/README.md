# Data availability

This public repository contains code and compact result summaries, not the full research data.

## Study inputs

- **PTAL:** Transport for London 2023 100 m grid Access Index data. PTAL measures public-transport access and is not a measure of destination accessibility or observed mobility.
- **EPC:** public Energy Performance Certificate records for England and Wales, reduced to the latest certificate per resolved property and aggregated by postcode. The target is the modelled `current_energy_efficiency` asset rating, not observed energy consumption.
- **Aerial imagery:** 25 cm Digimap imagery obtained through institutional access.
- **Street View:** a pre-existing Greater London archive used to extract CLIP representations and coverage metadata.
- **SatCLIP:** a frozen coordinate/location representation, not raw satellite imagery.
- **TESSERA:** a frozen 2024 Earth-observation representation.
- **AlphaEarth / Google Satellite Embedding:** supplied polygon-level mean embedding summaries.

## Publicly omitted assets

The following are excluded because of size, licensing, privacy, or reproducibility boundaries:

- the full EPC source export;
- Digimap aerial tiles and derived crops;
- the Street View image archive and thumbnails;
- full and intermediate embedding tables;
- the 26,597-row final model table and prediction parquet files;
- temporary crop, cache and fold-checkpoint files.

Authorised users can reconnect these inputs through `src/config.py`. The notebook sequence documents the expected filenames, schema checks and integrity gates.

## Scope of inference

The validation protocols test transfer within Greater London to held-out borough-level groups and continuous geographic regions. They do not constitute external-city validation.

