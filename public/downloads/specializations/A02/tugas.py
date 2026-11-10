"""Starter code Tugas A02: Pipeline Pembersihan & Agregasi Laporan Penjualan."""

from __future__ import annotations

from pathlib import Path
import pandas as pd


def clean_transactions(df: pd.DataFrame) -> pd.DataFrame:
    """Membersihkan teks, duplikasi, tanggal, dan missing values transaksi."""
    # TODO: Implementasikan langkah cleaning tanpa memodifikasi df input secara langsung
    raise NotImplementedError("Implementasikan fungsi clean_transactions")


def summarize_by_city(df_clean: pd.DataFrame) -> pd.DataFrame:
    """Menghitung total_orders, total_qty, dan total_revenue per kota."""
    # TODO: Implementasikan groupby().agg() dan urutkan menurun berdasarkan total_revenue
    raise NotImplementedError("Implementasikan fungsi summarize_by_city")


if __name__ == "__main__":
    csv_path = Path(__file__).resolve().parent.parent / "datasets" / "retail_transactions_raw.csv"
    print(f"Dataset siap diproses dari: {csv_path}")
