# TfL station activity

This folder contains the four public annualised station entry/exit files used in the analysis. The files are retained in their downloaded form for transparency around the commuter-demand shock calculation.

The 2019 file provides the pre-pandemic working-week reference. The 2023-2025 files provide the post-pandemic comparison period. Notebook `01` standardises the differing weekday group labels, calculates the commuter-demand shock score, ranks the Top-100 stations and writes the public derivatives in `data/derived/`.

`Top100_Master_Spatial_OD_Sheet_Clean.csv` is not a required input. It was an earlier project-development export that mixed the station ranking with an obsolete LAD-origin screening step.
