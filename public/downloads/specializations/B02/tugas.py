"""Starter code Tugas B02: Benchmark Regresi & Klasifikasi Supervised."""

from __future__ import annotations

from pathlib import Path
import pandas as pd


def evaluate_regressors(df: pd.DataFrame) -> pd.DataFrame:
    """Membandingkan DummyRegressor, LinearRegression, dan Ridge pada test set."""
    # TODO: Gunakan train_test_split(..., test_size=0.25, random_state=42) dan kembalikan DataFrame metrik
    raise NotImplementedError("Implementasikan evaluate_regressors")


def evaluate_classifiers(df: pd.DataFrame) -> pd.DataFrame:
    """Membandingkan DummyClassifier, LogisticRegression, dan RandomForestClassifier."""
    # TODO: Gunakan stratify=y dan hitung accuracy serta f1_score
    raise NotImplementedError("Implementasikan evaluate_classifiers")


def top_feature_importances(df: pd.DataFrame) -> list[tuple[str, float]]:
    """Mengekstrak peringkat fitur paling berpengaruh dari RandomForestClassifier."""
    # TODO: Latih RandomForestClassifier(n_estimators=60, random_state=42) dan urutkan importance
    raise NotImplementedError("Implementasikan top_feature_importances")


if __name__ == "__main__":
    csv_path = Path(__file__).resolve().parent.parent / "datasets" / "network_capacity_metrics.csv"
    print(f"Dataset B02 siap diuji dari: {csv_path}")

