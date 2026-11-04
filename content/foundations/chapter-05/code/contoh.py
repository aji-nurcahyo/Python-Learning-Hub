"""
Koleksi Contoh Kode Komputasi Terpadu - Chapter 05: Conditional Statements
Python Learning Hub - Rekayasa Telekomunikasi
"""

def demonstrasi_deteksi_tanda():
    """Deteksi bilangan positif, negatif, atau nol."""
    print("=== 1. Deteksi Bilangan Positif, Negatif, Nol ===")
    for bil in [15.5, -42.0, 0.0]:
        if bil > 0:
            status = "Positif"
        elif bil < 0:
            status = "Negatif"
        else:
            status = "Nol"
        print(f"Bilangan {bil:>5} -> {status}")
    print()

def demonstrasi_grade_akademik():
    """Klasifikasi nilai mutu mahasiswa."""
    print("=== 2. Klasifikasi Nilai Akademik ===")
    for skor in [85.5, 72.0, 64.0, 53.0, 41.5]:
        if skor >= 80.0:
            grade = "A"
        elif skor >= 70.0:
            grade = "B"
        elif skor >= 60.0:
            grade = "C"
        elif skor >= 50.0:
            grade = "D"
        else:
            grade = "E"
        print(f"Skor {skor:5.1f} -> Huruf Mutu: {grade}")
    print()

def demonstrasi_kabisat():
    """Pemeriksaan aturan tahun kabisat."""
    print("=== 3. Pemeriksaan Tahun Kabisat ===")
    for th in [2000, 2024, 2026, 1900]:
        kabisat = (th % 400 == 0) or (th % 4 == 0 and th % 100 != 0)
        print(f"Tahun {th}: {'Kabisat' if kabisat else 'Bukan Kabisat'}")
    print()

def demonstrasi_klasifikasi_sinyal_rsrp():
    """
    Klasifikasi kualitas sinyal RSRP seluler.
    Catatan Pedagogis: Ambang batas adalah asumsi instruksional pembelajaran.
    """
    print("=== 4. Klasifikasi Sinyal RSRP (Ilustrasi Pedagogis) ===")
    for rsrp in [-74.0, -84.5, -96.0, -112.0]:
        if rsrp >= -80.0:
            kat = "Sangat Baik (Excellent)"
        elif rsrp >= -90.0:
            kat = "Baik (Good)"
        elif rsrp >= -100.0:
            kat = "Cukup (Fair)"
        else:
            kat = "Buruk (Poor)"
        print(f"RSRP: {rsrp:6.1f} dBm -> Kategori: {kat}")
    print()

def demonstrasi_validasi_input():
    """Validasi masukan dengan kondisional dan penanganan batas."""
    print("=== 5. Validasi Masukan Alokasi Frekuensi ===")
    sampel = ["1800.5", "", "abc", "4500.0"]
    for teks in sampel:
        bersih = teks.strip()
        if not bersih:
            hasil = "Ditolak: Masukan teks kosong"
        else:
            try:
                val = float(bersih)
                if 700.0 <= val <= 3500.0:
                    hasil = f"Diterima: Frekuensi {val:.1f} MHz valid"
                else:
                    hasil = f"Ditolak: Frekuensi {val} MHz di luar batas (700-3500 MHz)"
            except ValueError:
                hasil = f"Ditolak: '{bersih}' bukan format numerik yang sah"
        print(f"Input: '{teks:<8}' -> Status: {hasil}")
    print()

if __name__ == "__main__":
    demonstrasi_deteksi_tanda()
    demonstrasi_grade_akademik()
    demonstrasi_kabisat()
    demonstrasi_klasifikasi_sinyal_rsrp()
    demonstrasi_validasi_input()
    print("Seluruh modul demonstrasi Chapter 05 berhasil dieksekusi.")
