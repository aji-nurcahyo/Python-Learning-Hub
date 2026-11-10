# Latihan Mandiri B05 (Capstone) — Predictive ML Application

## Latihan 1: Paritas Pipeline & Batch Scoring
1. Inspect `datasets/telecom_maintenance_train.csv` dan `datasets/telecom_maintenance_batch.csv`.
2. Periksa mengapa fitur `load_per_mhz` dan `loss_latency_index` perlu dihitung identik di training dan inferensi.
3. Simpan model ke folder temp memakai `joblib.dump` lalu verifikasi paritas `predict_proba` sebelum dan sesudah `joblib.load`.
4. Jalankan `pytest code/test_b05_capstone.py` dan pastikan semua assertion lolos.

