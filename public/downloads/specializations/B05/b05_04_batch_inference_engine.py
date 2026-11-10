import json
import sys
import tempfile
from pathlib import Path

import joblib
import pandas as pd

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from b05_01_feature_engineering import FEATURE_COLS, engineer_domain_features
from b05_02_training_selection import select_best_model
from b05_03_model_persistence import save_and_verify_bundle


def run_capstone_predictive_workflow(train_csv: Path, batch_csv: Path, out_dir: Path) -> dict:
    train_df = pd.read_csv(train_csv)
    model, metrics, X_test = select_best_model(train_df)
    model_path = save_and_verify_bundle(model, metrics, X_test, out_dir)

    loaded_model = joblib.load(model_path)
    batch_df = engineer_domain_features(pd.read_csv(batch_csv))
    probs = loaded_model.predict_proba(batch_df[FEATURE_COLS])[:, 1]
    preds = (probs >= 0.5).astype(int)

    predictions = []
    for tower_id, prob, flag in zip(batch_df["tower_id"], probs, preds):
        predictions.append(
            {
                "tower_id": str(tower_id),
                "failure_probability": round(float(prob), 4),
                "priority_action": "INSPECT_URGENT" if int(flag) == 1 else "MONITOR",
            }
        )
    predictions.sort(key=lambda r: r["failure_probability"], reverse=True)

    report_path = out_dir / "batch_predictions.json"
    payload = {"model_metrics": metrics, "predictions": predictions}
    report_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return payload


if __name__ == "__main__":
    ds_dir = CODE_DIR.parent / "datasets"
    with tempfile.TemporaryDirectory() as tmp_dir:
        report = run_capstone_predictive_workflow(
            ds_dir / "telecom_maintenance_train.csv",
            ds_dir / "telecom_maintenance_batch.csv",
            Path(tmp_dir),
        )
        print("Model terpilih :", report["model_metrics"]["selected_model"])
        print("Holdout ROC-AUC:", report["model_metrics"]["holdout_roc_auc"])
        print("Prediksi Batch (diurutkan risiko tertinggi):")
        print(pd.DataFrame(report["predictions"]).to_string(index=False))

