"""Chapter 30 Example 03: Capstone Validation & Transformation Engine
Python Learning Hub - Professional Capstone Project
"""

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class NormalizedMetric:
    device_id: str
    signal_quality_rating: str  # 'EXCELLENT', 'FAIR', 'POOR'
    requires_maintenance: bool


class MetricTransformer:
    """Mesin transformasi dan validasi integritas telemetri jaringan."""

    @staticmethod
    def transform_and_evaluate(raw_record: dict[str, Any]) -> NormalizedMetric:
        rssi = float(raw_record.get("rssi_dbm", -120.0))
        loss = float(raw_record.get("packet_loss_pct", 100.0))

        if rssi >= -75.0 and loss < 1.0:
            rating = "EXCELLENT"
            maintenance = False
        elif rssi >= -95.0 and loss < 5.0:
            rating = "FAIR"
            maintenance = False
        else:
            rating = "POOR"
            maintenance = True

        return NormalizedMetric(
            device_id=str(raw_record.get("device_id", "UNKNOWN")),
            signal_quality_rating=rating,
            requires_maintenance=maintenance,
        )


def main() -> None:
    print("Mengeksekusi Transformasi & Evaluasi Metrik SLA (Capstone Layer 3):\n")
    samples = [
        {"device_id": "BTS-101", "rssi_dbm": -65.0, "packet_loss_pct": 0.05},
        {"device_id": "BTS-102", "rssi_dbm": -88.0, "packet_loss_pct": 2.10},
        {"device_id": "BTS-103", "rssi_dbm": -115.0, "packet_loss_pct": 14.50},
    ]

    for sample in samples:
        norm = MetricTransformer.transform_and_evaluate(sample)
        action = "PERLU TINDAKAN" if norm.requires_maintenance else "KONDISI NORMAL"
        print(f" -> {norm.device_id}: Rating={norm.signal_quality_rating} | Rekomendasi: {action}")


if __name__ == "__main__":
    main()
