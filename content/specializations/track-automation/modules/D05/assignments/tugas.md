# Tugas Capstone Track D: Autonomous Daily Ingestion & Reporting Bot

## Instruksi Implementasi (`tugas.py`)
1. `collect_daily_feed(client: httpx.Client, path: str = "/daily-feed") -> list[dict]`: unduh feed HTML dengan retry untuk `502/503/504`, lalu ekstrak baris tabel dengan BeautifulSoup dan konversi biaya ke `int`.
2. `publish_report_bundle(records: list[dict], out_dir: Path, batch_date: str) -> tuple[Path, Path]`: hasilkan workbook `.xlsx` berformula `=SUM()` serta dokumen `.pdf` via `fpdf2`.
3. `run_bot_once(batch_date: str, workspace: Path, feed_client: httpx.Client, webhook_client: httpx.Client) -> dict`: jalankan langkah koleksi -> publish -> backup ZIP berotasi -> kirim webhook -> simpan ledger idempotent.
4. Uji end-to-end dengan `pytest` (pastikan run kedua tanggal sama berstatus `SKIPPED_IDEMPOTENT` dan webhook tidak terpanggil dua kali).

## Rubrik Penilaian (Total 100 Poin)
- Ingestion Feed HTML & Ketahanan Retry (25%)
- Kualitas Ekspor Excel & PDF + Arsip ZIP (30%)
- Idempotency Ledger & Webhook Notifier (25%)
- Arsitektur Modular & Cakupan Pytest (20%)

