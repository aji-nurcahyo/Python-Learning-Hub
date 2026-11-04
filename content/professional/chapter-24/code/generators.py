"""Pipeline Generator Pemrosesan Data Streaming (Chapter 24)
Python Learning Hub - Professional Python Engineering
"""

from collections.abc import Generator, Iterable
from typing import Any


def stream_telemetry_source(records: list[dict[str, Any]]) -> Generator[dict[str, Any], None, None]:
    """Tahap 1: Generator sumber yang mengalirkan record data satu per satu (lazy stream)."""
    for rec in records:
        yield rec.copy()


def filter_degraded_signals(
    stream: Iterable[dict[str, Any]],
    min_snr: float,
) -> Generator[dict[str, Any], None, None]:
    """Tahap 2: Generator filter yang hanya melewatkan sinyal dengan SNR di atas ambang batas."""
    for rec in stream:
        if float(rec.get("snr_db", 0.0)) >= min_snr:
            yield rec


def transform_telemetry_metrics(
    stream: Iterable[dict[str, Any]],
    calibration_offset: float = 1.5,
) -> Generator[dict[str, Any], None, None]:
    """Tahap 3: Generator transformasi yang mengkalibrasi nilai daya sinyal."""
    for rec in stream:
        raw_rsrp = float(rec.get("rsrp_dbm", -100.0))
        rec["calibrated_rsrp"] = round(raw_rsrp + calibration_offset, 2)
        rec["status"] = "OPTIMAL" if rec["calibrated_rsrp"] >= -85.0 else "SUBOPTIMAL"
        yield rec

