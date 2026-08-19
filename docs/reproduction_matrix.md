# Reproduction matrix

This matrix distinguishes files included in the repository from sources that must be acquired separately. "Analysis-ready" means complete for the stated study scope and analytical stage; it does not mean that the full original provider database is redistributed.

| Notebook | Main inputs | Included? | What an external researcher must supply |
|---|---|---:|---|
| 01 Data audit and TfL shock | Four TfL annualised files; Underground station points | Yes | Nothing |
| 02 Green Street preparation | Green Street tenant-premises files; public boundaries | Boundaries only | Authorised GeoDS files with the documented fields |
| 03 Source reconciliation and indicators | Green Street vacancy files; full OpenLocal property source; public boundaries | Boundaries and OpenLocal analysis tables only | GeoDS files and the matching full OpenLocal release for record-level reconstruction |
| 04 Mapping and spatial framework | Outputs from 03; TfL shock; ONS flows; LAD/MSOA/office boundaries | ONS, TfL and boundaries included | Upstream Green Street/OpenLocal outputs where the figure or table uses them |
| 05 Residential-origin exposure | Complete ONS MSOA flows; selected workplaces; OpenLocal retail outcomes | ONS and analysis-ready OpenLocal retail tables included | Full OpenLocal source only when rebuilding property-to-MSOA assignment |
| 06 Reconciliation and Objective 1 refinement | Green Street and OpenLocal record-level data; Objective 1 panels | Public inputs only | GeoDS files and full OpenLocal property source |
| 07 Objective 1 destination robustness | Public station/submarket frame; OpenLocal property data; safeguarded upstream results | Public workplace OpenLocal panel included | Full OpenLocal source for raw reconstruction and GeoDS data for complete dissertation outcomes |
| 08 Historical Green Street integration | Green Street tenant-premises history | No | Authorised GeoDS files |
| 09 Objective 2 office adjustment | Full OpenLocal property source; Green Street retail panel | OpenLocal office analysis tables included | Full OpenLocal source for raw reconstruction and GeoDS data for complete Objective 2 analysis |
| 10 Objective 2 retail pathways | Outputs from 08 and 09 | Public OpenLocal office components only | Authorised upstream Green Street outputs generated locally |

## Included complete public sources

- TfL annualised station activity for 2019 and 2023-2025.
- The ONS 2021 Census MSOA-to-MSOA commuting matrix used in the dissertation, stored as `data/public/ons/ODWP01EW_MSOA.csv.gz`.
- The smaller ONS local-authority commuting table used by legacy mapping checks.
- Underground station, LAD, London MSOA and office-market geometry used by the notebooks.

## Included analysis-ready public tables

- OpenLocal retail MSOA-year indicators and baseline-relative change tables for the residential study scope.
- OpenLocal office MSOA-year indicators and office-adjustment components for the five office submarkets.
- Public Objective 1 workplace panels combining OpenLocal outcomes with the TfL shock and office-submarket assignment.

## Not redistributed

- The 627 MB full OpenLocal property-level parquet. It remains available from the [official OpenLocal service](https://openlocal.uk/) and is needed for property-level rebuilding, postcode reconciliation and alternative record-level indicators. Save it at `data/external/openlocal/openlocal_property_level.parquet` or set `OPENLOCAL_PROPERTY_FILE`.
- Any Green Street raw record, processed extract, aggregate, figure or model output. Authorised academic users must obtain the safeguarded files from GeoDS and process them locally.

The exact numerical results also depend on using the same source releases and field definitions as the dissertation. A newer provider release may legitimately produce different results.
