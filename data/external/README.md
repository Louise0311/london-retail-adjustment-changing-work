# External inputs not stored in GitHub

This folder documents the files required for complete record-level reproduction but intentionally does not store them.

## OpenLocal property source

The full property-level OpenLocal parquet used in the dissertation is approximately 627 MB and is not duplicated in this repository. Obtain the matching release from the [official OpenLocal service](https://openlocal.uk/), then either:

1. save it as `data/external/openlocal/openlocal_property_level.parquet`; or
2. set the `OPENLOCAL_PROPERTY_FILE` environment variable to its absolute local path.

The repository already includes complete study-scope OpenLocal analysis tables in `data/public/openlocal/`. The full source is needed only to rebuild property-to-MSOA assignment, postcode reconciliation, record-level occupation checks, or alternative indicators.

## Green Street safeguarded source

No Green Street record, processed extract, aggregate, figure, or model output is distributed. Authorised academic researchers must request the safeguarded files through the Geographic Data Service (GeoDS) and keep them in their approved local environment. The expected fields are documented in `data/file_manifest.example.csv`.

These external files are ignored by Git and must never be committed.
