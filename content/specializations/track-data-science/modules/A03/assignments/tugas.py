"""Starter code Tugas A03: Laporan Diagnostik EDA Kualitas Jaringan."""

from __future__ import annotations

from pathlib import Path
import pandas as pd


def detect_iqr_outliers(series: pd.Series) -> tuple[pd.Series, dict[str, float]]:
    """Mendeteksi outlier memakai aturan pagar Tukey 1.5 * IQR."""
    # TODO: Hitung q1, q3, iqr, lower, upper lalu kembalikan (mask, dict_batas)
    raise NotImplementedError("Implementasikan detect_iqr_outliers")


def summarize_skewness(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    """Menyusun ringkasan mean, median, IQR, dan skewness untuk daftar kolom."""
    # TODO: Kembalikan DataFrame ringkasan
    raise NotImplementedError("Implementasikan summarize_skewness")


def regional_crosstabs(df: pd.DataFrame) -> pd.DataFrame:
    """Membuat tabulasi silang region terhadap sla_status."""
    return pd.crosstab(df["region"], df["sla_status"], margins=True)


if __name__ == "__main__":
    csv_path = Path(__file__).resolve().parent.parent / "datasets" / "telecom_qos_kpi.csv"
    print(f"Dataset EDA siap dibaca dari: {csv_path}")

