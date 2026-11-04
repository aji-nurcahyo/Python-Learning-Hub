"""Starter Code - Tugas Praktik 18: Telecom Anomaly Detection & Robust Validator Suite
Python Learning Hub - Level 2: Intermediate
Nama Mahasiswa : ____________________
NIM            : ____________________
"""

import logging
from typing import Any

# TODO: Konfigurasikan logger bawaan Python


# TODO: Definisikan kelas dasar TelemetryValidationError dan kelas turunannya
class TelemetryValidationError(Exception):
    """Kelas dasar exception validasi telemetri."""
    pass


class MissingPropertyError(TelemetryValidationError):
    """Exception jika atribut wajib hilang."""
    pass


class ValueRangeError(TelemetryValidationError):
    """Exception jika nilai numerik melanggar batas ambang fisik."""
    pass


class RobustTelemetryValidator:
    """Mesin validasi data telemetri yang tangguh terhadap kesalahan runtime."""

    def __init__(self) -> None:
        self.valid_data: list[dict[str, Any]] = []
        self.rejected_data: list[dict[str, Any]] = []

    def validate_record(self, raw_record: dict[str, Any]) -> dict[str, Any]:
        """Memvalidasi satu record data telemetri.

        Raises:
            TelemetryValidationError: Jika data tidak valid.
        """
        # TODO: Implementasikan pemeriksaan field 'id', 'frekuensi_mhz', 'daya_dbm', 'latensi_ms'
        # Tangkap ValueError saat konversi float dan lemparkan ValueRangeError jika di luar batas
        pass

    def validate_batch(self, batch: list[dict[str, Any]]) -> dict[str, Any]:
        """Memproses batch data rekaman dan memisahkan data valid vs rejected."""
        # TODO: Implementasikan perulangan batch dengan blok try-except spesifik
        pass


if __name__ == "__main__":
    print("Inisialisasi Robust Telemetry Validator...")
    # Tulis pengujian demonstrasi kode Anda di sini

