"""Starter code Capstone E05: IoT Telemetry & RF Signal Analytics System."""

from __future__ import annotations

from pathlib import Path


def route_telemetry_via_mqtt(csv_path: Path, filter_topic: str = "iot/#") -> list[dict]:
    """Memetakan baris CSV ke topik iot/{region}/{node_id}/telemetry dan menyaring via MQTT wildcard."""
    # TODO: Gunakan paho.mqtt.client.topic_matches_sub(filter_topic, topic)
    raise NotImplementedError("Implementasikan route_telemetry_via_mqtt")


def denoise_tower_vibration(fs: float = 600.0, cutoff_hz: float = 75.0) -> dict:
    """Melakukan filtering Butterworth SOS + rfft dan menghitung snr_gain_db."""
    # TODO: Implementasikan sintesis sinyal uji, butter(..., output='sos'), dan sosfiltfilt
    raise NotImplementedError("Implementasikan denoise_tower_vibration")


def evaluate_node_rf_health(csv_path: Path) -> list[dict]:
    """Mengaudit RSRP, SINR, suhu, dan packet loss per node dengan peringkat keparahan."""
    # TODO: Implementasikan deteksi flag dan pengurutan prioritas CRITICAL -> WARNING -> HEALTHY
    raise NotImplementedError("Implementasikan evaluate_node_rf_health")


def export_monitoring_bundle(csv_path: Path, out_dir: Path) -> dict[str, Path]:
    """Menghasilkan rf_monitoring_dashboard.png, node_health_report.json, dan ops_summary.md."""
    # TODO: Integrasikan ketiga tahapan di atas dan simpan artefak ke out_dir
    raise NotImplementedError("Implementasikan export_monitoring_bundle")


if __name__ == "__main__":
    csv_file = Path(__file__).resolve().parent.parent / "datasets" / "iot_node_telemetry_stream.csv"
    print(f"Starter Capstone E05 siap dijalankan dengan dataset: {csv_file}")

