# Modul D05 (Capstone): Autonomous Data Ingestion & Reporting Bot

## 1. Orkestrasi Bot Pelaporan Otonom
Capstone Track D menyatukan keempat kemampuan otomasi yang telah Anda kuasai:
1. **Feed Collection (`d05_01_feed_collector.py`):** Menarik feed HTML harian melalui `httpx.Client` ber-retry selektif lalu mengurai tabel memakai `BeautifulSoup4` + normalisasi nominal IDR.
2. **Excel & PDF Publishing (`d05_02_excel_pdf_publisher.py`):** Menghasilkan workbook `.xlsx` ter-styling dengan formula aktif `=SUM(...)` serta laporan eksekutif `.pdf` melalui `fpdf2`.
3. **Rotating Archive, Idempotent Ledger & Webhook (`d05_03_idempotent_notifier.py`):** Mengompresi laporan ke arsip `.zip` berotasi (`keep=3`), mencatat selesainya batch tanggal hanya **sesudah** seluruh file sukses dibuat, lalu mengirim ringkasan JSON ke webhook.
4. **Bot Runner (`d05_04_reporting_bot_runner.py`):** Menjamin eksekusi pertama berjalan penuh dan eksekusi ulang di tanggal yang sama aman berstatus `SKIPPED_IDEMPOTENT`.

---

## 2. Prinsip Kritis Konsistensi Status
Jangan pernah menulis `"completed"` ke ledger di awal program sebelum pekerjaan selesai. Urutan transaksi aman adalah: **Collect -> Export Artifacts -> Archive -> Send Webhook -> Commit Ledger**.

