"""Create public notebook copies without outputs or local machine paths.

This utility is included for transparency. It copies the selected notebooks from
an authorised local workspace to a public code folder, removes outputs and
execution metadata, and replaces the original workspace path with the
DISSERTATION_WORKSPACE environment variable.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


SOURCE_NOTEBOOKS = {
    "01_Data_Audit_Spatial_Framework.ipynb": "01_data_audit_spatial_framework.ipynb",
    "03_GreenStreet_POI_Preparation.ipynb": "03_greenstreet_poi_preparation.ipynb",
    "04_Source_Reconciliation_and_Indicator_Build.ipynb": "04_source_reconciliation_and_indicator_build.ipynb",
    "06_Mapping_and_Spatial_Analysis.ipynb": "05_mapping_and_spatial_analysis.ipynb",
    "08_MSOA_Origin_Exposure_Analysis.ipynb": "06_msoa_origin_exposure_analysis.ipynb",
    "09_Source_Disagreement_and_H1_Model_Refinement.ipynb": "07_source_reconciliation_and_objective1_models.ipynb",
    "10_H1_Destination_Robustness.ipynb": "08_objective1_destination_robustness.ipynb",
    "11_GreenStreet_Historical_POI_Integration.ipynb": "09_greenstreet_historical_poi_integration.ipynb",
    "13_RQ2_Office_Stock_Adjustment_and_Retail_Change.ipynb": "10_objective2_office_stock_adjustment.ipynb",
    "14_RQ3_Retail_Adjustment_Pathways.ipynb": "11_objective2_retail_adjustment_pathways.ipynb",
}

PUBLIC_NOTE = [
    "# Public repository note\n",
    "\n",
    "This notebook is an output-cleared code copy. It requires locally authorised data and is not runnable from the public repository alone. Green Street raw data, intermediate files, derived aggregates and outputs are not distributed.\n",
]


def sanitise_notebook(source: Path, destination: Path) -> None:
    notebook = json.loads(source.read_text(encoding="utf-8"))
    notebook["cells"].insert(
        0,
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": PUBLIC_NOTE,
        },
    )

    for cell in notebook["cells"]:
        cell["execution_count"] = None
        cell["outputs"] = []
        cell.get("metadata", {}).pop("execution", None)
        source_text = "".join(cell.get("source", []))
        source_text = re.sub(
            r'BASE = Path\(r["\'].*?MSc_Dissertation_TfL["\']\)',
            'BASE = Path(os.environ.get("DISSERTATION_WORKSPACE", Path.cwd().resolve()))',
            source_text,
        )
        source_text = source_text.replace(
            "BASE = Path.cwd()",
            'BASE = Path(os.environ.get("DISSERTATION_WORKSPACE", Path.cwd().resolve()))',
        )
        if "from pathlib import Path" in source_text and "import os" not in source_text:
            source_text = source_text.replace("from pathlib import Path", "from pathlib import Path\nimport os")
        cell["source"] = source_text.splitlines(keepends=True)

    destination.write_text(json.dumps(notebook, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    source_root = project_root.parent
    notebook_dir = project_root / "notebooks"
    notebook_dir.mkdir(parents=True, exist_ok=True)

    for source_name, destination_name in SOURCE_NOTEBOOKS.items():
        sanitise_notebook(source_root / source_name, notebook_dir / destination_name)

if __name__ == "__main__":
    main()
