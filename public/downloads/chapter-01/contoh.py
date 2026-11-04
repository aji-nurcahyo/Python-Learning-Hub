"""
Koleksi Contoh Kode Komputasi Terpadu - Chapter 01: Introduction to Python
Python Learning Hub - Rekayasa Telekomunikasi
"""

def demonstrasi_print_dan_argumen():
    """Menampilkan pesan pembuka dan operasi matematika dasar."""
    print("=== 1. Demonstrasi print() & Argumen ===")
    print("Selamat datang di Python Learning Hub!")
    print("Platform Pembelajaran Pemrograman Berorientasi Rekayasa.")
    print("Versi Interpreter:", 3, "| Status:", "Siap Digunakan")
    print("Hasil Operasi Aritmatika 100 + 200 =", 100 + 200)
    print()

def demonstrasi_case_sensitivity():
    """Menunjukkan sifat kepekaan huruf kapital pada variabel."""
    print("=== 2. Kepekaan Huruf (Case-Sensitivity) ===")
    frekuensi_mhz = 900
    Frekuensi_mhz = 1800
    FREKUENSI_MHZ = 2100

    print("Nilai frekuensi_mhz :", frekuensi_mhz)
    print("Nilai Frekuensi_mhz :", Frekuensi_mhz)
    print("Nilai FREKUENSI_MHZ :", FREKUENSI_MHZ)
    print("Ketiganya menempati alokasi referensi independen.")
    print()

def demonstrasi_indentasi_dan_blok():
    """Menunjukkan hierarki blok kontrol dengan indentasi 4 spasi."""
    print("=== 3. Struktur Indentasi Blok PEP 8 ===")
    daya_dbm = -75
    if daya_dbm >= -85:
        status = "Sinyal Bagus"
        print(f"Indikator Daya: {daya_dbm} dBm -> Kategori: {status}")
    else:
        status = "Sinyal Lemah"
        print(f"Indikator Daya: {daya_dbm} dBm -> Kategori: {status}")
    print()

def hitung_waktu_propagasi(jarak_meter: float, kecepatan_cahaya: float = 3e8) -> float:
    """Menghitung waktu tempuh sinyal gelombang radio dalam mikrodetik."""
    waktu_detik = jarak_meter / kecepatan_cahaya
    return waktu_detik * 1e6

def demonstrasi_studi_kasus():
    """Aplikasi perambatan gelombang radio nirkabel."""
    print("=== 4. Studi Kasus Propagasi Gelombang Radio ===")
    jarak = 1500.0  # meter
    t_mikro = hitung_waktu_propagasi(jarak)
    print(f"Jarak Stasiun BTS ke Penerima: {jarak} meter")
    print(f"Waktu Rambat Gelombang: {t_mikro:.4f} mikrodetik")
    print()

if __name__ == "__main__":
    demonstrasi_print_dan_argumen()
    demonstrasi_case_sensitivity()
    demonstrasi_indentasi_dan_blok()
    demonstrasi_studi_kasus()
    print("Seluruh modul demonstrasi Chapter 01 berhasil dieksekusi.")

