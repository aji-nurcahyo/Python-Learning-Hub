"""Modul Robust Data Validator untuk Integritas Data Jaringan
Python Learning Hub - Chapter 18: Exception Handling & Debugging
"""

import logging
from typing import Any

# Konfigurasi logger default
logger = logging.getLogger("DataValidator")
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(levelname)s: %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)


class ValidationError(Exception):
    """Kelas dasar exception untuk seluruh kegagalan validasi rekaman data."""
    pass


class MissingFieldError(ValidationError):
    """Exception yang dipicu jika atribut wajib tidak ditemukan pada payload."""
    def __init__(self, field_name: str) -> None:
        self.field_name = field_name
        super().__init__(f"Field wajib '{field_name}' tidak ditemukan pada rekaman.")


class InvalidRangeError(ValidationError):
    """Exception yang dipicu jika nilai numerik berada di luar rentang fisis yang diizinkan."""
    def __init__(self, field_name: str, value: float, min_val: float, max_val: float) -> None:
        self.field_name = field_name
        self.value = value
        self.min_val = min_val
        self.max_val = max_val
        super().__init__(
            f"Nilai '{field_name}'={value} di luar rentang valid [{min_val} s.d. {max_val}]."
        )


class TelecomRecordValidator:
    """Mesin validasi rekaman telemetri yang tangguh terhadap berbagai galat data."""

    REQUIRED_FIELDS = ["id", "lokasi", "frekuensi_mhz", "daya_dbm"]
    FREQ_RANGE = (100.0, 6000.0)      # 100 MHz s.d. 6 GHz
    POWER_RANGE = (-140.0, 60.0)       # -140 dBm s.d. 60 dBm

    def __init__(self) -> None:
        self.valid_records: list[dict[str, Any]] = []
        self.invalid_records: list[dict[str, Any]] = []

    def validate_single_record(self, record: dict[str, Any]) -> dict[str, Any]:
        """Memvalidasi satu rekaman data; memicu ValidationError spesifik jika cacat."""
        if not isinstance(record, dict):
            raise ValidationError(f"Tipe masukan harus berupa dictionary, bukan {type(record).__name__}.")

        # 1. Periksa keberadaan field wajib
        for field in self.REQUIRED_FIELDS:
            if field not in record or str(record[field]).strip() == "":
                raise MissingFieldError(field)

        # 2. Validasi numerik frekuensi
        try:
            freq = float(record["frekuensi_mhz"])
        except (ValueError, TypeError) as err:
            raise ValidationError(f"Konversi frekuensi gagal: {err}") from err

        min_f, max_f = self.FREQ_RANGE
        if not (min_f <= freq <= max_f):
            raise InvalidRangeError("frekuensi_mhz", freq, min_f, max_f)

        # 3. Validasi numerik daya
        try:
            daya = float(record["daya_dbm"])
        except (ValueError, TypeError) as err:
            raise ValidationError(f"Konversi daya transmisi gagal: {err}") from err

        min_p, max_p = self.POWER_RANGE
        if not (min_p <= daya <= max_p):
            raise InvalidRangeError("daya_dbm", daya, min_p, max_p)

        return {
            "id": str(record["id"]).strip(),
            "lokasi": str(record["lokasi"]).strip(),
            "frekuensi_mhz": freq,
            "daya_dbm": daya,
            "status": str(record.get("status", "ACTIVE")).strip()
        }

    def process_batch(self, batch_data: list[dict[str, Any]]) -> dict[str, Any]:
        """Memproses sekumpulan rekaman data dan memisahkan data valid vs invalid."""
        self.valid_records.clear()
        self.invalid_records.clear()

        for idx, item in enumerate(batch_data):
            try:
                cleaned = self.validate_single_record(item)
                self.valid_records.append(cleaned)
                logger.info(f"Rekaman #{idx + 1} [{cleaned['id']}] lolos validasi.")
            except ValidationError as err:
                logger.warning(f"Rekaman #{idx + 1} DITOLAK: {err}")
                self.invalid_records.append({"data": item, "alasan": str(err)})

        return self.get_summary()

    def get_summary(self) -> dict[str, Any]:
        """Mengembalikan statistik ringkasan proses validasi."""
        total = len(self.valid_records) + len(self.invalid_records)
        return {
            "total_diproses": total,
            "total_valid": len(self.valid_records),
            "total_invalid": len(self.invalid_records),
            "valid_ratio_pct": round((len(self.valid_records) / total * 100), 1) if total > 0 else 0.0
        }

