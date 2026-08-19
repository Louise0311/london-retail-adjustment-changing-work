# Retail Adjustment and Changing Work in London

Code and documentation for an MSc Urban Spatial Science dissertation examining how post-pandemic changes in working and commuting patterns, together with office-market adjustment, are associated with retail change across London's office submarkets and commuting-linked residential areas.

## What this repository contains

This repository contains the reproducible analysis logic, documentation, a clean sequence of Jupyter notebooks, and a public-data package. The package includes the TfL station files used to construct the commuter-demand measure, the complete compressed ONS MSOA commuting-flow matrix used in the study, study boundary files, and OpenLocal-only analysis tables for retail and office outcomes. It does not distribute Green Street data, Green Street-derived data, figures, model outputs, or downloadable extracts based on safeguarded data.

The study has two objectives:

1. Relate weekday commuter-demand change at London stations to retail adjustment in workplace MSOAs and commuting-linked residential-origin MSOAs.
2. Examine office-market adjustment and retail-adjustment patterns within five Central London office submarkets.

## Data access

OpenLocal is openly licensed. The repository provides the study-scope OpenLocal analysis tables used for annual retail outcomes, office-market indicators, change measures and the public side of Objective 1. The full 627 MB property-level source is not duplicated because it is large; obtain it from the [official OpenLocal service](https://openlocal.uk/) when reproducing property-to-MSOA preparation, postcode reconciliation or record-level occupation audits. Green Street data are commercially safeguarded and are not included in this repository in any form. Researchers who wish to reproduce Green Street elements of the analysis should request authorised academic access through the Geographic Data Service (GeoDS). See [data/README.md](data/README.md), [data/external/README.md](data/external/README.md), and [docs/data_access.md](docs/data_access.md).

## Running the analysis

1. Create a Python environment and install the packages in `requirements.txt`.
2. Clone or download the repository locally. Public data are read from `data/public/`.
3. For record-level OpenLocal rebuilding, save the source as `data/external/openlocal/openlocal_property_level.parquet` or set `OPENLOCAL_PROPERTY_FILE`. Set `DISSERTATION_WORKSPACE` to the authorised Green Street workspace for safeguarded steps.
4. Read [docs/workflow.md](docs/workflow.md) and the [notebook-by-notebook reproduction matrix](docs/reproduction_matrix.md) before running the notebooks.
5. Run notebooks in the listed order. The public tables support inspection and partial reproduction; full end-to-end reproduction requires the matching OpenLocal property release and authorised Green Street data.

The notebooks are published with outputs cleared so that no restricted findings or intermediate files are distributed.

## Repository structure

```text
notebooks/  Cleaned analysis notebooks
config/     Example local-path configuration and file manifest
docs/       Workflow and data-access notes
data/       Public inputs, reproducible public-data derivatives, and access notes
```

## Citation

Please cite the dissertation and this repository using the metadata in `CITATION.cff` once the final dissertation URL is available.

## Licence

The code in this repository is released under the MIT License. Source datasets remain subject to their own licences, access conditions, and safeguarding requirements.
