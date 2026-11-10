"""Starter code Tugas B03: Mesin Segmentasi & Deteksi Anomali Unsupervised."""

from __future__ import annotations

from pathlib import Path
import numpy as np
import pandas as pd


def evaluate_kmeans_range(
    df: pd.DataFrame,
    feature_cols: list[str],
    k_values: list[int],
) -> pd.DataFrame:
    """Mengevaluasi inertia dan silhouette_score KMeans untuk rentang nilai K."""
    # TODO: Lakukan StandardScaler sebelum KMeans dan kembalikan DataFrame hasil
    raise NotImplementedError("Implementasikan evaluate_kmeans_range")


def detect_density_anomalies(
    df: pd.DataFrame,
    feature_cols: list[str],
    eps: float = 0.9,
    min_samples: int = 3,
) -> list[str]:
    """Mengembalikan daftar user_id yang diklasifikasikan DBSCAN sebagai noise (-1)."""
    # TODO: Terapkan StandardScaler + DBSCAN
    raise NotImplementedError("Implementasikan detect_density_anomalies")


def project_pca(
    df: pd.DataFrame,
    feature_cols: list[str],
    n_components: int = 2,
) -> tuple[np.ndarray, float]:
    """Mereduksi fitur ke n_components dan mengembalikan rasio varians kumulatif."""
    # TODO: Gunakan Pipeline([('scaler', StandardScaler()), ('pca', PCA(n_components=n_components))])
    raise NotImplementedError("Implementasikan project_pca")


if __name__ == "__main__":
    csv_path = Path(__file__).resolve().parent.parent / "datasets" / "user_usage_profiles.csv"
    print(f"Dataset B03 siap dimuat dari: {csv_path}")

