# Data access and schemas

No data files are bundled with this repository. OpenLocal is openly licensed, but the full source files are large and should be obtained directly from the official service. Green Street data, including derived or aggregated material, must not be added to this repository.

| Source | Role in the analysis | Access |
|---|---|---|
| TfL annualised station entry/exit data | Constructs the weekday commuter-demand shock score | Public TfL data |
| ONS Census origin-destination data | Links workplace MSOAs to residential-origin MSOAs | Public ONS data |
| Office-market and administrative boundaries | Spatial matching and five office-submarket framework | Public boundary sources |
| OpenLocal commercial property data | Administrative retail and office stock, floorspace, value and occupation measures | Openly licensed; obtain from the official OpenLocal service |
| Green Street retail data | Consumer-facing active stock, vacancy, long-term vacancy, turnover and net formation | Commercially safeguarded; request authorised academic access through GeoDS |

The expected local filenames and required fields are listed in [file_manifest.example.csv](file_manifest.example.csv). These are file-schema notes only, not data extracts.
