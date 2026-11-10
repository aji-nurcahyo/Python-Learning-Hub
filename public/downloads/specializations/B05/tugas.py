"""Starter code Capstone B05: Predictive Maintenance & Inference System."""

from __future__ import annotations

from pathlib import Path
import pandas as pd


def add_domain_features(df: pd.DataFrame) -> pd.DataFrame:
    """Menghitung load_per_mhz dan loss_latency_index secara aman tanpa mutasi df input."""
    # TODO: Implementasikan fitur domain di atas df.copy()
    raise NotImplementedError("Implementasikan add_domain_features")


def train_and_select_model(train_df: pd.DataFrame):
    """Membandingkan kandidat model di atas CV dan mengembalikan model terbaik serta metrik holdout."""
    # TODO: Gunakan stratified split + StratifiedKFold + DummyClassifier baseline
    raise NotImplementedError("Implementasikan train_and_select_model")


def save_model_bundle(model, metrics: dict, out_dir: Path) -> Path:
    """Menyimpan Pipeline terlatih dengan joblib serta model_metadata.json."""
    # TODO: Gunakan joblib.dump dan json.dumps
    raise NotImplementedError("Implementasikan save_model_bundle")


def score_new_batch(bundle_dir: Path, batch_csv: Path) -> list[dict]:
    """Memuat model tersimpan dan memberi peringkat probabilitas kegagalan pada batch baru."""
    # TODO: Terapkan add_domain_features dan predict_proba pada batch_csv
    raise NotImplementedError("Implementasikan score_new_batch")


if __name__ == "__main__":
    ds_dir = Path(__file__).resolve().parent.parent / "datasets"
    print(f"Capstone B05 siap memproses dataset di: {ds_dir}")

