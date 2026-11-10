import json
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from e05_04_monitoring_dashboard_runner import run_iot_monitoring_capstone


def test_capstone_iot_monitoring_produces_verified_artifacts(tmp_path: Path) -> None:
    csv_file = CODE_DIR.parent / "datasets" / "iot_node_telemetry_stream.csv"
    artifacts = run_iot_monitoring_capstone(csv_file, tmp_path)

    assert artifacts["chart"].exists() and artifacts["chart"].stat().st_size > 3000
    assert artifacts["json"].exists()
    assert artifacts["markdown"].exists()

    report = json.loads(artifacts["json"].read_text(encoding="utf-8"))
    assert report["mqtt_events_routed"] == 6
    assert report["dsp_snr_gain_db"] > 10.0
    assert report["dsp_dominant_hz"] == 25.0

    by_id = {n["node_id"]: n for n in report["node_diagnostics"]}
    assert "HIGH_INTERFERENCE" in by_id["NODE-LPG-02"]["flags"]
    assert "COVERAGE_BLINDSPOT" in by_id["NODE-JKT-02"]["flags"]
    assert by_id["NODE-LPG-01"]["status"] == "HEALTHY"

