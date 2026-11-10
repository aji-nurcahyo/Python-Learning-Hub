"""Starter code Tugas B01: Builder Pipeline Churn Prediction."""

from __future__ import annotations

from pathlib import Path
import pandas as pd
from sklearn.compose import ColumnTransformer


def split_features_target(
    df: pd.DataFrame,
    target_col: str,
    test_size: float = 0.25,
    random_state: int = 42,
):
    """Membagi fitur dan target secara stratified dengan random_state deterministik."""
    # TODO: Gunakan train_test_split(..., stratify=y, random_state=random_state)
    raise NotImplementedError("Implementasikan split_features_target")


def build_preprocessing_pipeline(
    numeric_cols: list[str],
    categorical_cols: list[str],
) -> ColumnTransformer:
    """Membangun ColumnTransformer bebas data leakage untuk fitur campuran."""
    # TODO: Susun SimpleImputer + StandardScaler untuk numerik, OneHotEncoder untuk kategorikal
    raise NotImplementedError("Implementasikan build_preprocessing_pipeline")


if __name__ == "__main__":
    csv_path = Path(__file__).resolve().parent.parent / "datasets" / "customer_churn_features.csv"
    print(f"Dataset B01 siap dimuat dari: {csv_path}")

