"""Starter code Capstone A05: End-to-End Network Analytics Report Engine."""

from __future__ import annotations

from pathlib import Path
import pandas as pd


def validate_and_load(logs_path: Path, meta_path: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Memuat logs & metadata lalu memvalidasi kelengkapan kolom wajib."""
    # TODO: Periksa apakah seluruh kolom wajib tersedia; lempar ValueError bila hilang
    raise NotImplementedError("Implementasikan validate_and_load")


def clean_and_enrich(logs_df: pd.DataFrame, meta_df: pd.DataFrame) -> pd.DataFrame:
    """Deduplikasi, koreksi latensi negatif, left join metadata, dan imputasi."""
    # TODO: Lakukan cleaning serta tambahkan kolom sla_breach
    raise NotImplementedError("Implementasikan clean_and_enrich")


def compute_regional_kpis(enriched: pd.DataFrame) -> pd.DataFrame:
    """Menghitung KPI SLA per wilayah (compliance %, median & p95 latency)."""
    # TODO: Gunakan groupby('region') dan kembalikan DataFrame terurut
    raise NotImplementedError("Implementasikan compute_regional_kpis")


def generate_analytics_bundle(logs_path: Path, meta_path: Path, out_dir: Path) -> dict[str, Path]:
    """Menjalankan orkestrasi penuh: PNG dashboard, JSON summary, dan laporan Markdown."""
    # TODO: Panggil tiga fungsi di atas dan ekspor seluruh artefak ke out_dir
    raise NotImplementedError("Implementasikan generate_analytics_bundle")


if __name__ == "__main__":
    ds_dir = Path(__file__).resolve().parent.parent / "datasets"
    print(f"Capstone A05 siap memproses datasets pada: {ds_dir}")

