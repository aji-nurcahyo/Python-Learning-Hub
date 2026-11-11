"""Contoh 17.7: Manajemen Path Modern dan Aman Menggunakan pathlib.Path
Python Learning Hub - Level 2: Intermediate
"""

from pathlib import Path

# Inisialisasi path relatif berbasis objek
folder_kerja = Path("data_proyek_telekomunikasi")
folder_arsip = folder_kerja / "arsip_log"
berkas_log = folder_arsip / "audit_november.log"

try:
    # 1. Membuat direktori bertingkat secara otomatis (parents=True)
    folder_arsip.mkdir(parents=True, exist_ok=True)

    # 2. Menulis dan membaca teks secara konsisten lintas OS (newline="\n")
    berkas_log.write_text("Sistem telekomunikasi siap diuji.\n", encoding="utf-8", newline="\n")

    # 3. Menginspeksi atribut berkas secara deklaratif
    print("Atribut Path:")
    print("  - Nama Berkas :", berkas_log.name)
    print("  - Ekstensi    :", berkas_log.suffix)
    print("  - Induk Folder:", berkas_log.parent.name)
    print("  - Berkas Ada? :", berkas_log.exists())
    print("  - Ukuran Byte :", berkas_log.stat().st_size)
    print("  - Isi Konten  :", berkas_log.read_text(encoding="utf-8").strip())
finally:
    # Pembersihan direktori sementara
    if berkas_log.exists():
        berkas_log.unlink()
    if folder_arsip.exists():
        folder_arsip.rmdir()
    if folder_kerja.exists():
        folder_kerja.rmdir()

