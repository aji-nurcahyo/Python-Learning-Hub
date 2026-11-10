# Latihan Mandiri E04 — Wireless Network & RF Analytics

## Latihan 1: Audit RSRP vs SINR pada Drive Test
1. Muat `datasets/drive_test_lte_measurements.csv` dengan Pandas.
2. Klasifikasikan kualitas tiap titik menurut `RSRP` dan `SINR`, lalu pisahkan zona `COVERAGE_BLINDSPOT` vs `HIGH_INTERFERENCE`.
3. Hitung penalti interferensi `snr_db - sinr_db` dan identifikasi sel dengan total `handover_count` terbanyak.
4. Uji formula Free-Space Path Loss serta jalankan `pytest code/test_e04_rf_analytics.py`.

