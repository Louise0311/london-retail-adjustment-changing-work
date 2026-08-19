# ONS origin-destination commuting flows

This folder contains the complete 2021 Census MSOA-to-MSOA commuting-flow table used in the dissertation to construct residential-origin exposure. It is the study's local copy of `ODWP01EW_MSOA.csv`, compressed with gzip to reduce repository size. The smaller `ODWP01EW_LTLA.csv.gz` table is retained for legacy local-authority screening and mapping checks.

Pandas reads the file without manual extraction:

```python
flows = pandas.read_csv("data/public/ons/ODWP01EW_MSOA.csv.gz")
```

The contents remain subject to the conditions of the official ONS source release.
