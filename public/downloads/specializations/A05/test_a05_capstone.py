import json
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from a05_04_report_generator import run_capstone_pipeline


def test_end_to_end_capstone_generates_all_artifacts(tmp_path: Path) -> None:
    ds_dir = CODE_DIR.parent / "datasets"
    artifacts = run_capstone_pipeline(
        ds_dir / "network_operations_logs.csv",
        ds_dir / "tower_metadata.csv",
        tmp_path,
    )
    assert artifacts["chart"].exists() and artifacts["chart"].stat().st_size > 3000
    assert artifacts["summary"].exists()
    assert artifacts["report"].exists()

    summary = json.loads(artifacts["summary"].read_text(encoding="utf-8"))
    regions = {item["region"] for item in summary}
    assert regions == {"Sumatera", "Jawa", "Kalimantan"}

