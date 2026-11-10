"""Starter code Tugas B04: Audit Cross-Validation & Hyperparameter Tuning."""

from __future__ import annotations

from pathlib import Path
import pandas as pd


def evaluate_with_cv(pipeline, X: pd.DataFrame, y: pd.Series, n_splits: int = 5) -> dict[str, float]:
    """Menjalankan StratifiedKFold CV dan mengembalikan mean serta std skor ROC-AUC."""
    # TODO: Gunakan StratifiedKFold dan cross_val_score(..., scoring='roc_auc')
    raise NotImplementedError("Implementasikan evaluate_with_cv")


def run_grid_search(X_train: pd.DataFrame, y_train: pd.Series):
    """Menjalankan GridSearchCV di atas Pipeline RandomForestClassifier secara deterministik."""
    # TODO: Gunakan prefix 'rf__' pada param_grid serta scoring='roc_auc'
    raise NotImplementedError("Implementasikan run_grid_search")


def threshold_tradeoff_table(
    y_true: pd.Series,
    y_prob: pd.Series,
    thresholds: list[float],
) -> pd.DataFrame:
    """Menyusun tabel Precision, Recall, dan F1 pada setiap nilai threshold."""
    # TODO: Hitung precision_score, recall_score, f1_score untuk (y_prob >= thr)
    raise NotImplementedError("Implementasikan threshold_tradeoff_table")


if __name__ == "__main__":
    csv_path = Path(__file__).resolve().parent.parent / "datasets" / "fraud_alert_sample.csv"
    print(f"Dataset B04 siap dimuat dari: {csv_path}")

