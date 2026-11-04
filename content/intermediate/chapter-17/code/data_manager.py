"""Modul Data Manager CSV & JSON untuk Jaringan Telekomunikasi
Python Learning Hub - Chapter 17: File Handling & Data Serialization
"""

import csv
import json
from pathlib import Path
from typing import Any


class DataManagerError(Exception):
    """Base exception untuk kesalahan operasional DataManager."""
    pass


class RecordValidationError(DataManagerError):
    """Exception yang dipicu ketika suatu baris data tidak lolos validasi."""
    pass


class TelemetryDataManager:
    """Manajer pengolahan, validasi, dan serialisasi data telemetri telekomunikasi."""

    def __init__(self) -> None:
        self.records: list[dict[str, Any]] = []

    def load_from_csv(self, file_path: str | Path) -> int:
        """Membaca rekaman dari file CSV lokal dengan penanganan missing file yang aman."""
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Berkas CSV tidak ditemukan: {path.name}")

        loaded_count = 0
        with open(path, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    record = self._validate_and_parse(row)
                    self.records.append(record)
                    loaded_count += 1
                except RecordValidationError:
                    # Lewati baris cacat namun lanjutkan pemrosesan
                    continue
        return loaded_count

    def _validate_and_parse(self, row: dict[str, str]) -> dict[str, Any]:
        """Memvalidasi keberadaan field kunci dan mengonversi tipe data numerik."""
        required_fields = ["id", "lokasi", "frekuensi_mhz", "daya_dbm"]
        for field in required_fields:
            if field not in row or not row[field].strip():
                raise RecordValidationError(f"Field wajib '{field}' kosong atau hilang.")

        try:
            freq = float(row["frekuensi_mhz"])
            daya = float(row["daya_dbm"])
        except ValueError as err:
            raise RecordValidationError(f"Format angka tidak valid: {err}")

        if freq <= 0:
            raise RecordValidationError(f"Frekuensi harus bernilai positif: {freq}")

        return {
            "id": row["id"].strip(),
            "lokasi": row["lokasi"].strip(),
            "frekuensi_mhz": freq,
            "daya_dbm": daya,
            "status": row.get("status", "ACTIVE").strip() or "ACTIVE"
        }

    def add_or_update_record(self, record_data: dict[str, Any]) -> str:
        """Menambahkan rekaman baru atau memperbarui rekaman yang sudah ada berdasarkan ID."""
        r_id = str(record_data.get("id", "")).strip()
        if not r_id:
            raise RecordValidationError("ID rekaman tidak boleh kosong.")

        freq = float(record_data["frekuensi_mhz"])
        daya = float(record_data["daya_dbm"])
        status = str(record_data.get("status", "ACTIVE")).strip()

        cleaned_record = {
            "id": r_id,
            "lokasi": str(record_data["lokasi"]).strip(),
            "frekuensi_mhz": freq,
            "daya_dbm": daya,
            "status": status
        }

        for i, existing in enumerate(self.records):
            if existing["id"] == r_id:
                self.records[i] = cleaned_record
                return "UPDATED"

        self.records.append(cleaned_record)
        return "ADDED"

    def export_to_json(self, file_path: str | Path) -> int:
        """Mengekspor seluruh koleksi rekaman ke file JSON terstruktur."""
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.records, f, indent=2)
        return len(self.records)

    def calculate_summary(self) -> dict[str, Any]:
        """Menghitung ringkasan statistik dari kumpulan rekaman."""
        if not self.records:
            return {"total_records": 0, "avg_power_dbm": 0.0, "active_count": 0}

        total = len(self.records)
        sum_daya = sum(r["daya_dbm"] for r in self.records)
        active = sum(1 for r in self.records if r["status"].upper() == "ACTIVE")

        return {
            "total_records": total,
            "avg_power_dbm": round(sum_daya / total, 2),
            "active_count": active
        }
