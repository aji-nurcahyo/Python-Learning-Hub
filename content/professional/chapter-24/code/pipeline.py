"""Data Processing Pipeline Terpadu (Chapter 24)
Python Learning Hub - Professional Python Engineering
"""

from typing import Any
from decorators import time_tracker, validate_record_schema
from generators import (
    stream_telemetry_source,
    filter_degraded_signals,
    transform_telemetry_metrics,
)
from context_managers import execution_timer


@validate_record_schema(required_keys=["cell_id", "rsrp_dbm", "snr_db"])
@time_tracker
def process_single_record(record: dict[str, Any]) -> dict[str, Any]:
    """Memproses satu rekaman data telemetri dengan validasi schema dan tracking waktu."""
    return {
        "cell_id": record["cell_id"],
        "rsrp_dbm": float(record["rsrp_dbm"]),
        "snr_db": float(record["snr_db"]),
        "processed": True,
    }


def execute_pipeline(
    raw_data: list[dict[str, Any]],
    min_snr: float = 12.0,
) -> dict[str, Any]:
    """Mengeksekusi pipeline pemrosesan data berbasis generator di dalam context timer."""
    with execution_timer("TelemetryBatchProcessing") as timer_info:
        # Membangun rantai generator (lazy pipeline)
        source = stream_telemetry_source(raw_data)
        filtered = filter_degraded_signals(source, min_snr=min_snr)
        transformed = transform_telemetry_metrics(filtered, calibration_offset=2.0)

        results: list[dict[str, Any]] = []
        for item in transformed:
            validated = process_single_record(item)
            results.append(validated)

    return {
        "timer": timer_info,
        "processed_count": len(results),
        "results": results,
    }

