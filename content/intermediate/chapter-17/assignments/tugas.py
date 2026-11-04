"""Starter Code - Tugas Praktik 17: Telecom Gateway Data Pipeline & Serialization Suite
Python Learning Hub - Level 2: Intermediate
Nama Mahasiswa : ____________________
NIM            : ____________________
"""

import csv
import json
from pathlib import Path
from typing import Any


class TelecomDataPipeline:
    """Modul pipeline pemrosesan berkas CSV dan serialisasi JSON data telekomunikasi."""

    def __init__(self) -> None:
        self.records: list[dict[str, Any]] = []

    def load_csv(self, file_path: str | Path) -> tuple[int, int]:
        """Membaca rekaman dari berkas CSV dengan validasi kolom dan tipe data.

        Returns:
            tuple[int, int]: (jumlah_sukses, jumlah_gagal)
        """
        # TODO: Implementasikan pembacaan CSV menggunakan csv.DictReader
        # Pastikan menggunakan context manager with open(..., encoding="utf-8", newline="")
        # Tangani kemungkinan FileNotFoundError
        pass

    def add_or_update(self, node_id: str, lokasi: str, frekuensi_mhz: float, kapasitas_gbps: float, status: str = "ONLINE") -> str:
        """Menambahkan node baru atau memperbarui data node yang telah ada berdasarkan node_id."""
        # TODO: Implementasikan pembaruan in-place atau penambahan elemen baru
        pass

    def export_json(self, output_path: str | Path) -> bool:
        """Mengekspor seluruh data node ke file format JSON dengan indent=2."""
        # TODO: Implementasikan serialisasi data menggunakan json.dump
        pass

    def get_summary(self) -> dict[str, Any]:
        """Menghitung ringkasan statistik (total node, total kapasitas Gbps, jumlah online)."""
        # TODO: Kembalikan dictionary ringkasan metrik jaringan
        pass


if __name__ == "__main__":
    print("Inisialisasi Telecom Data Pipeline...")
    pipeline = TelecomDataPipeline()
    # Tulis pengujian demonstrasi kode Anda di sini

