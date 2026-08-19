# Analysis workflow

The public notebooks retain the logic used in the dissertation but have cleared outputs. The repository now contains the complete ONS MSOA commuting-flow input and study-scope OpenLocal analysis tables. Full record-level reconstruction still requires the official OpenLocal property source and authorised Green Street data in a local research workspace.

1. `01_Data_Audit_Spatial_Framework.ipynb`: audit where every dataset enters the workflow; then harmonise the four public TfL annualised station files, construct the 2023-2025 commuter-demand shock, rank the Top-100 stations, attach station geometry, and write the public derived tables used downstream.
2. `02_GreenStreet_POI_Preparation.ipynb`: prepare safeguarded Green Street POI history within the authorised local environment.
3. `03_Source_Reconciliation_and_Indicator_Build.ipynb`: construct annual indicators and prepare comparable MSOA-level measures.
4. `04_Mapping_and_Spatial_Analysis.ipynb`: construct the core workplace and residential-origin spatial framework using the included TfL and ONS inputs.
5. `05_MSOA_Origin_Exposure_Analysis.ipynb`: construct residential exposure; either rebuild OpenLocal outcomes from the full property source or use the included analysis-ready tables.
6. `06_Source_Reconciliation_and_Objective1_Refinement.ipynb`: reconcile Green Street and OpenLocal observation regimes and estimate Objective 1 diagnostics.
7. `07_Objective1_Destination_Robustness.ipynb`: estimate workplace-destination comparisons and robustness checks.
8. `08_GreenStreet_Historical_POI_Integration.ipynb`: integrate historical Green Street POI records into Objective 1 outcomes.
9. `09_Objective2_Office_Stock_Adjustment.ipynb`: construct office-market indicators from the full OpenLocal property source; the resulting OpenLocal-only analysis tables are also included for transparent inspection and downstream use.
10. `10_Objective2_Retail_Adjustment_Pathways.ipynb`: identify retail-adjustment patterns and test office conditions across patterns.

## Reproduction levels

- **Public source reconstruction:** TfL shock and ONS residential-exposure inputs can be rebuilt from files included in the repository.
- **Public analysis-table reproduction:** the included OpenLocal-only tables support inspection and re-estimation of the public outcome components without distributing the 627 MB source parquet.
- **Full record-level reproduction:** obtain the matching OpenLocal property release from [OpenLocal](https://openlocal.uk/) and authorised Green Street files. Save OpenLocal at `data/external/openlocal/openlocal_property_level.parquet` or set `OPENLOCAL_PROPERTY_FILE`; set `DISSERTATION_WORKSPACE` for safeguarded Green Street inputs; preserve the fields listed in `data/file_manifest.example.csv`; then run the notebooks in sequence.

Local authorised paths must not be committed.
