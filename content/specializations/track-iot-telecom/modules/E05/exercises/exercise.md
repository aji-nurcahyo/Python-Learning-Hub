# Latihan Mandiri E05 (Capstone) — IoT & Signal Analytics System

## Latihan 1: Audit Integrasi Lintas Lapisan
1. Telusuri cara data `datasets/iot_node_telemetry_stream.csv` dirutekan ke topik MQTT `iot/{region}/{node_id}/telemetry`.
2. Periksa peningkatan SNR pada gelombang getaran 25 Hz setelah disaring memakai filter *Butterworth* `output="sos"`.
3. Periksa daftar node dengan status `CRITICAL`, terutama selisih `NODE-LPG-02` (`HIGH_INTERFERENCE`) melawan `NODE-JKT-02` (`COVERAGE_BLINDSPOT`).
4. Jalankan `pytest code/test_e05_capstone.py`.

