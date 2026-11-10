# Tugas Capstone Track E: End-to-End IoT Telemetry & RF Signal Analytics System

## Instruksi Implementasi (`tugas.py`)
1. `route_telemetry_via_mqtt(csv_path: Path, filter_topic: str) -> list[dict]`: baca CSV dan saring event memakai `mqtt.topic_matches_sub`.
2. `denoise_tower_vibration(fs: float = 600.0, cutoff_hz: float = 75.0) -> dict`: rancang filter Butterworth `output="sos"` + `sosfiltfilt`, hitung `snr_gain_db` dan frekuensi dominan `rfft`.
3. `evaluate_node_rf_health(csv_path: Path) -> list[dict]`: evaluasi kondisi setiap node untuk flag `COVERAGE_BLINDSPOT`, `HIGH_INTERFERENCE`, `THERMAL_ALERT`, dan `HIGH_PACKET_LOSS`.
4. `export_monitoring_bundle(csv_path: Path, out_dir: Path) -> dict[str, Path]`: hasilkan dashboard PNG, `node_health_report.json`, serta `ops_summary.md`, lalu verifikasi penuh lewat `pytest`.

## Rubrik Penilaian (Total 100 Poin)
- Akuisisi & Routing Telemetri MQTT (25%)
- DSP Spectral Check & Butterworth Filtering (25%)
- Diagnosa RF (RSRP/RSRQ/SINR) & Kesehatan Node (25%)
- Dashboard Artefak & Integration Test Pytest (25%)

