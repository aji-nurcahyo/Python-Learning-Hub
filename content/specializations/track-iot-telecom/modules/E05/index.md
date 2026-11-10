# Modul E05 (Capstone): IoT Monitoring & Signal Analytics System

## 1. Integrasi Lintas Lapisan Track E
Proyek Capstone Track E merangkai keempat kompetensi utama ke dalam satu sistem pemantauan stasiun pemancar dan node IoT terpadu:
1. **Lapisan Akuisisi & Routing MQTT (`e05_01_telemetry_decoder_mqtt.py`):** membaca log telemetri perangkat, memvalidasi paket, lalu mendistribusikannya melalui topik hierarkis `iot/{region}/{node_id}/telemetry` memakai pencocokan wildcard `paho-mqtt`.
2. **Lapisan Digital Signal Processing (`e05_02_signal_conditioning.py`):** memeriksa spektrum getaran motor pendingin menara melalui `rfft` dan membersihkan interferensi 150 Hz memakai filter *Butterworth* `output="sos"` + `sosfiltfilt`.
3. **Lapisan Diagnostik Radio & Kesehatan Node (`e05_03_rf_sla_diagnostics.py`):** memisahkan masalah `COVERAGE_BLINDSPOT`, `HIGH_INTERFERENCE` (`RSRP` baik tapi `SINR` jatuh di bawah SNR), `THERMAL_ALERT`, dan `HEALTHY`.
4. **Lapisan Monitoring & Pelaporan (`e05_04_monitoring_dashboard_runner.py`):** mengekspor dashboard PNG dua-panel, laporan kesehatan JSON terurut risiko tertinggi, serta ringkasan eksekutif Markdown.

---

## 2. Rekayasa Siap Produksi & Verifikasi Pytest
Setiap lapisan dipisahkan sebagai modul berparameter jelas dengan `TemporaryDirectory`/`tmp_path` pada suite `test_e05_capstone.py` agar pipeline berjalan konsisten baik secara lokal maupun di lingkungan pengujian otomatis.

