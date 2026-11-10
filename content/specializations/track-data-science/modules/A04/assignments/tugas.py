"""Starter code Tugas A04: Generator Figur Publikasi Matplotlib & Seaborn."""

from __future__ import annotations

from pathlib import Path
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_latency_distribution(df: pd.DataFrame, out_path: Path) -> Path:
    """Merender histogram + KDE latensi beserta garis vertikal nilai median."""
    # TODO: Gunakan fig, ax = plt.subplots(...), sns.histplot, ax.axvline, fig.savefig, plt.close(fig)
    raise NotImplementedError("Implementasikan plot_latency_distribution")


def plot_correlation_heatmap(df: pd.DataFrame, cols: list[str], out_path: Path) -> Path:
    """Merender heatmap matriks korelasi Spearman dengan anotasi numerik."""
    # TODO: Gunakan np.triu mask agar tidak duplikat di atas diagonal
    raise NotImplementedError("Implementasikan plot_correlation_heatmap")


def build_qos_dashboard(df: pd.DataFrame, out_path: Path) -> Path:
    """Membangun dashboard ringkas 2x2 dan mengekspor PNG 150 DPI."""
    # TODO: Gunakan plt.subplots(2, 2, figsize=(12, 8)) dan fig.suptitle(...)
    raise NotImplementedError("Implementasikan build_qos_dashboard")


if __name__ == "__main__":
    csv_path = Path(__file__).resolve().parent.parent / "datasets" / "telecom_qos_kpi.csv"
    print(f"Siap merender visualisasi dari: {csv_path}")

