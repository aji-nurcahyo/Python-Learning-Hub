import json
import sys
import tempfile
from pathlib import Path

import joblib
import numpy as np
import pandas as pd

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from b05_01_feature_engineering import FEATURE_COLS
from b05_02_training_selection import select_best_model


def save_and_verify_bundle(model, metrics: dict, X_sample: pd.DataFrame, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    model_path = out_dir / "maintenance_pipeline.joblib"
    meta_path = out_dir / "model_metadata.json"

    joblib.dump(model, model_path)
    meta = {**metrics, "features": FEATURE_COLS}
    meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")

    reloaded = joblib.load(model_path)
    orig_prob = model.predict_proba(X_sample)[:, 1]
    reloaded_prob = reloaded.predict_proba(X_sample)[:, 1]
    if not np.allclose(orig_prob, reloaded_prob):
        raise AssertionError("Prediksi pasca joblib.load tidak identik!")
    return model_path


if __name__ == "__main__":
    csv_path = CODE_DIR.parent / "datasets" / "telecom_maintenance_train.csv"
    model, metrics, X_test = select_best_model(pd.read_csv(csv_path))
    with tempfile.TemporaryDirectory() as tmp_dir:
        bundle_path = save_and_verify_bundle(model, metrics, X_test, Path(tmp_dir))
        print("Serialisasi joblib & metadata berhasil:", bundle_path.name)
        print("Ukuran berkas model (.joblib)        :", bundle_path.stat().st_size, "bytes")
        print("Verifikasi paritas probabilitas      : IDENTIK (np.allclose=True)")

