"""Contoh 18.2: Validasi Tipe Data Numerik & Penanganan ValueError
Python Learning Hub - Level 2: Intermediate
"""

def parsing_frekuensi(teks_input: str) -> float | None:
    """Mengonversi teks masukan menjadi angka frekuensi (MHz) dengan validasi ketat."""
    try:
        nilai = float(teks_input.strip())
        if nilai <= 0:
            print(f"Validasi Gagal: Frekuensi harus positif ({teks_input.strip()})")
            return None
        return nilai
    except ValueError:
        print(f"Format Salah: Tidak dapat mengubah '{teks_input.strip()}' menjadi bilangan float.")
        return None

daftar_masukan = ["2412.0", "  5180.5 ", "sembilan ratus", "-100.0", "3.5GHz"]

print("Hasil Parsing Frekuensi Masukan:")
for teks in daftar_masukan:
    hasil = parsing_frekuensi(teks)
    if hasil is not None:
        print(f"  -> Frekuensi valid terdeteksi: {hasil:.1f} MHz")

