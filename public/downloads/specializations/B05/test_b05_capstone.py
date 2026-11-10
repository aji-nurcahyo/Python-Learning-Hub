import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from b05_04_batch_inference_engine import run_capstone_predictive_workflow


def test_capstone_predictive_pipeline_and_batch_scoring(tmp_path: Path) -> None:
    ds_dir = CODE_DIR.parent / "datasets"
    payload = run_capstone_predictive_workflow(
        ds_dir / "telecom_maintenance_train.csv",
        ds_dir / "telecom_maintenance_batch.csv",
        tmp_path,
    )
    assert payload["model_metrics"]["holdout_roc_auc"] > 0.90
    assert (tmp_path / "maintenance_pipeline.joblib").exists()
    assert (tmp_path / "model_metadata.json").exists()
    assert (tmp_path / "batch_predictions.json").exists()

    by_id = {row["tower_id"]: row for row in payload["predictions"]}
    assert by_id["NEW-102"]["priority_action"] == "INSPECT_URGENT"
    assert by_id["NEW-101"]["priority_action"] == "MONITOR"

