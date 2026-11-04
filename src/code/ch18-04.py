"""Contoh 18.4: Alur Eksekusi Lengkap dengan Blok else dan finally
Python Learning Hub - Level 2: Intermediate
"""

def proses_transmisi_paket(kapasitas_total: int, ukuran_paket: int) -> int | None:
    """Mendemonstrasikan urutan eksekusi try-except-else-finally."""
    print(f"\n--- Memproses Transmisi ({kapasitas_total} KB / {ukuran_paket} KB) ---")
    hasil = None
    try:
        print("[1] Memulai alokasi buffer kanal...")
        hasil = kapasitas_total // ukuran_paket
    except ZeroDivisionError:
        print("[2] EXCEPT: Ukuran paket nol memicu ZeroDivisionError!")
    else:
        print(f"[3] ELSE: Kalkulasi sukses tanpa exception. Total paket: {hasil}")
    finally:
        print("[4] FINALLY: Membersihkan buffer dan merilis kanal transmisi.")
    return hasil

# Skenario 1: Berjalan sukses tanpa error (else dieksekusi)
proses_transmisi_paket(1024, 128)

# Skenario 2: Terjadi error division by zero (else dilewati, except & finally jalan)
proses_transmisi_paket(1024, 0)
