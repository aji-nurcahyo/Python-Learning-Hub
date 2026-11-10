"""Starter code Tugas A01: Pipeline Kalibrasi & Evaluasi Node Sensor."""

from __future__ import annotations

from pathlib import Path
import numpy as np


def load_sensor_data(csv_path: str | Path) -> np.ndarray:
    """Memuat CSV sensor numerik (mengabaikan header) menjadi array float64 2D."""
    return np.genfromtxt(csv_path, delimiter=",", skip_header=1, dtype=np.float64)


def remove_bias(metrics: np.ndarray, bias_vector: np.ndarray) -> np.ndarray:
    """Mengkalibrasi metrik sensor dengan pengurangan bias menggunakan broadcasting."""
    # TODO: Ganti baris ini agar mengurangi metrics dengan bias_vector secara vektorisasi
    raise NotImplementedError("Implementasikan fungsi remove_bias")


def minmax_scale(metrics: np.ndarray) -> np.ndarray:
    """Menormalisasi setiap kolom ke [0.0, 1.0] dengan proteksi pembagian nol."""
    # TODO: Hitung min_col dan max_col memakai axis=0, keepdims=True
    raise NotImplementedError("Implementasikan fungsi minmax_scale")


def rank_nodes_by_stability(
    node_ids: np.ndarray,
    scaled_metrics: np.ndarray,
) -> list[tuple[int, float]]:
    """Mengurutkan node berdasarkan jarak Euclidean terkecil terhadap titik ideal nol."""
    # TODO: Gunakan np.linalg.norm(..., axis=1) lalu np.argsort untuk mengurutkan node
    raise NotImplementedError("Implementasikan fungsi rank_nodes_by_stability")


if __name__ == "__main__":
    sample_csv = Path(__file__).resolve().parent.parent / "datasets" / "sensor_matrix.csv"
    print(f"Siap menguji dataset pada: {sample_csv}")

