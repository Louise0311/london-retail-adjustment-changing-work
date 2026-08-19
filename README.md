# Retail Adjustment and Changing Work in London

Code and documentation for an MSc Urban Spatial Science dissertation examining how post-pandemic changes in working and commuting patterns, together with office-market adjustment, are associated with retail change across London's office submarkets and commuting-linked residential areas.

## What this repository contains

This repository contains the reproducible analysis logic, documentation, a clean sequence of Jupyter notebooks, and a small public-data package. The public-data package includes the TfL station files used to construct the commuter-demand measure, the resulting station-level shock and Top-100 tables, the study boundary files, and an OpenLocal-only MSOA-year retail-indicator table. It does not distribute Green Street data, Green Street-derived data, figures, model outputs, or downloadable extracts based on safeguarded data.

The study has two objectives:

1. Relate weekday commuter-demand change at London stations to retail adjustment in workplace MSOAs and commuting-linked residential-origin MSOAs.
2. Examine office-market adjustment and retail-adjustment patterns within five Central London office submarkets.

## Data access

OpenLocal is openly licensed. The repository provides an OpenLocal-only annual MSOA indicator table, while the full property-level source should be obtained from the official service. Green Street data are commercially safeguarded and are not included in this repository in any form. Researchers who wish to reproduce Green Street elements of the analysis should request authorised academic access through the Geographic Data Service (GeoDS). See [data/README.md](data/README.md) and [docs/data_access.md](docs/data_access.md).

## Running the analysis

1. Create a Python environment and install the packages in `requirements.txt`.
2. Copy `config/paths.example.yml` to `config/paths.yml` and set local paths to authorised source data.
3. Read [docs/workflow.md](docs/workflow.md) before running the notebooks.
4. Run notebooks in the listed order. Some notebooks require safeguarded Green Street access and will not run with public data alone.

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
