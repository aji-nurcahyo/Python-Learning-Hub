# Latihan Mandiri D05 (Capstone) — Autonomous Reporting Bot

## Latihan 1: Audit Siklus Lengkap & Idempotency
1. Telusuri interaksi antara `d05_01_feed_collector.py`, `d05_02_excel_pdf_publisher.py`, `d05_03_idempotent_notifier.py`, dan `d05_04_reporting_bot_runner.py`.
2. Jalankan bot dua kali pada `batch_date="2025-02-10"` di direktori `tmp_path` memakai `MockTransport`.
3. Periksa isi file Excel dengan `openpyxl`, verifikasi PDF dengan magic bytes `b"%PDF-"`, serta verifikasi webhook hanya dipanggil tepat 1 kali (`webhook_calls == 1`).
4. Jalankan `pytest code/test_d05_capstone.py`.

