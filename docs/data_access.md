# Data access and safeguarding

## Green Street

Green Street data used in this dissertation are commercially safeguarded. No raw records, processed extracts, intermediate files, derived aggregates, figures, or model outputs based on Green Street data are deposited here. Researchers seeking authorised academic access should apply through the Geographic Data Service (GeoDS), which manages safeguarded academic access on behalf of Green Street.

The repository retains code structure and field-level documentation so that authorised users can reproduce the workflow in a safeguarded environment. It does not provide a route to reconstruct or infer the underlying commercial data.

## OpenLocal and public sources

OpenLocal is openly licensed and intended for research use. TfL, ONS, and boundary data are public sources. This repository includes the TfL station files, the complete compressed ONS MSOA commuting-flow table, boundary files, and study-scope OpenLocal-only retail and office analysis tables. It does not duplicate the 627 MB property-level OpenLocal parquet. Obtain that source from the [official OpenLocal service](https://openlocal.uk/) only when rebuilding property assignment, postcode reconciliation, record-level occupation audits or alternative indicators from the original records. Save it at `data/external/openlocal/openlocal_property_level.parquet` or set `OPENLOCAL_PROPERTY_FILE`. Users remain responsible for checking current licences, documentation, and access terms before downloading or redistributing any source data.

## Public repository policy

OpenLocal, TfL, ONS, and boundary files may be obtained from their official public sources, subject to their current licence terms. Public analysis tables are included where they materially improve reproducibility without duplicating very large source files. Do not add Green Street records, processed Green Street extracts, derived aggregates, figures or model outputs based on Green Street data. Do not add local configuration files, source links carrying access tokens, or personal information.
