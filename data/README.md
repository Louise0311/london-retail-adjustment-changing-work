# Public data, access and schemas

This directory contains the directly usable public-data package for the dissertation. It distinguishes complete public source files, study-scope analysis-ready tables, reproducible derivatives, and sources that must be obtained separately. The file catalogue is available in [file_manifest.csv](file_manifest.csv); [file_manifest.example.csv](file_manifest.example.csv) lists the fields expected for the full local workflow.

## Included public data

| Folder | Contents | Use in this study |
|---|---|---|
| `public/tfl/` | Four annualised TfL station activity files for 2019 and 2023-2025 | Construction of the weekday commuter-demand shock score |
| `public/ons/` | Complete 2021 Census MSOA-to-MSOA commuting-flow table used in the study, compressed with gzip | Construction of residential-origin exposure |
| `public/boundaries/` | London office-market polygons and station point geometry | Study-area definition and spatial matching |
| `public/openlocal/` | OpenLocal-only study-scope retail and office analysis tables | Administrative-property outcomes used in Objectives 1 and 2 |
| `derived/` | Reproducible station shock tables, selected workplace stations/MSOAs, residential exposure and public Objective 1 workplace panels | Inputs to the workplace and residential-exposure workflow |

The OpenLocal tables are processed, openly licensed data products. They contain no Green Street fields, no Green Street-derived variables, and no tenant or address data. They are complete for the stated study scope and analytical stage, but they are not a copy of the full property-level OpenLocal database. Obtain the full source from the [official OpenLocal service](https://openlocal.uk/) when rebuilding spatial assignment, postcode reconciliation, record-level occupation checks or alternative indicators. Placement and environment-variable instructions are in [external/README.md](external/README.md).

## Sources not distributed here

Green Street data, including raw records, processed extracts, aggregates, figures and model outputs derived from those data, must not be added to this repository. The full OpenLocal property-level source is not duplicated because of its size, although the analysis-ready OpenLocal-only tables used by the dissertation are included.

| Source | Role in the analysis | Access |
|---|---|---|
| TfL annualised station entry/exit data | Constructs the weekday commuter-demand shock score | Public copies included in `public/tfl/` |
| ONS Census origin-destination data | Links workplace MSOAs to residential-origin MSOAs | Complete compressed study file included in `public/ons/` |
| Office-market and station boundaries | Spatial matching and five office-submarket framework | Public copies included in `public/boundaries/` |
| OpenLocal commercial property data | Administrative retail and office stock, floorspace, value and occupation measures | Openly licensed; study-scope analysis tables included, full property source obtained from the official service |
| Green Street retail data | Consumer-facing active stock, vacancy, long-term vacancy, turnover and net formation | Commercially safeguarded; request authorised academic access through GeoDS |

The derived TfL files are not independent source data: Notebook `01` rebuilds them from the four annualised TfL files and the station-point layer. The Objective 1 OpenLocal panels combine only public TfL, boundary and OpenLocal inputs. The expected local filenames and required fields for safeguarded and full property-level reproduction are listed in [file_manifest.example.csv](file_manifest.example.csv). These are schema notes, not substitutes for those source data.
