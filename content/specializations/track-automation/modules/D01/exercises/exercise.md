# Latihan Mandiri D01 — File System Automation

## Latihan 1: Safe Organizer & Deduplikasi
1. Gunakan `pathlib.Path` dan `rglob("*")` untuk menginventarisasi berkas di direktori sementara `tempfile.TemporaryDirectory`.
2. Terapkan `organize_directory(inbox, dry_run=True)` terlebih dahulu, lalu jalankan dengan `dry_run=False`.
3. Hitung hash SHA-256 setiap berkas dalam chunk 64 KB untuk menemukan salinan identik berbeda nama.
4. Uji rotasi arsip ZIP (`keep=2`) melalui `pytest`.

