# Analysis workflow

The public notebooks retain the logic used in the dissertation but have cleared outputs and configurable local paths. Run them only after acquiring authorised data and setting `config/paths.yml`.

1. `01_Data_Audit_Spatial_Framework.ipynb`: inventory data, establish geographic reference layers, and document spatial matching.
2. `02_GreenStreet_POI_Preparation.ipynb`: prepare safeguarded Green Street POI history within the authorised local environment.
3. `03_Source_Reconciliation_and_Indicator_Build.ipynb`: construct annual indicators and prepare comparable MSOA-level measures.
4. `04_Mapping_and_Spatial_Analysis.ipynb`: construct the core workplace and residential-origin spatial framework.
5. `05_MSOA_Origin_Exposure_Analysis.ipynb`: construct residential exposure and retail outcomes.
6. `06_Source_Reconciliation_and_Objective1_Refinement.ipynb`: reconcile Green Street and OpenLocal observation regimes and estimate Objective 1 diagnostics.
7. `07_Objective1_Destination_Robustness.ipynb`: estimate workplace-destination comparisons and robustness checks.
8. `08_GreenStreet_Historical_POI_Integration.ipynb`: integrate historical Green Street POI records into Objective 1 outcomes.
9. `09_Objective2_Office_Stock_Adjustment.ipynb`: construct office-market indicators and investigate Objective 2.
10. `10_Objective2_Retail_Adjustment_Pathways.ipynb`: identify retail-adjustment patterns and test office conditions across patterns.

The exact output locations, input filenames, and path configuration are intentionally local. Public users should adapt them to their authorised data environment without committing those changes.
