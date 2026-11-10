# Latihan Mandiri A05 (Capstone) — End-to-End Analytics Pipeline

## Latihan 1: Audit Multi-Tahap
1. Buka `datasets/network_operations_logs.csv` dan periksa baris mana yang memiliki `log_id` ganda serta nilai `latency_ms` negatif.
2. Gabungkan dengan `datasets/tower_metadata.csv` memakai `pd.merge(..., how="left")`.
3. Hitung metrik `p95_latency_ms` dan `sla_compliance_pct` per wilayah.
4. Uji pipeline melalui `pytest code/test_a05_capstone.py` dari direktori modul A05.

