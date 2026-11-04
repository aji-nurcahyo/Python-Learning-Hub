"""
Koleksi Contoh Kode Komputasi Terpadu - Chapter 03: Operators & Expressions
Python Learning Hub - Rekayasa Telekomunikasi
"""

import math

def demonstrasi_operator_aritmatika():
    """Menampilkan perilaku operator aritmatika numerik."""
    print("=== 1. Demonstrasi Operator Aritmatika ===")
    a, b = 25, 4
    print(f"a = {a}, b = {b}")
    print(f"Penjumlahan (+)      : {a + b}")
    print(f"Pengurangan (-)      : {a - b}")
    print(f"Perkalian (*)        : {a * b}")
    print(f"Pembagian Riil (/)   : {a / b} (tipe: {type(a / b).__name__})")
    print(f"Pembagian Bulat (//) : {a // b} (tipe: {type(a // b).__name__})")
    print(f"Modulo Sisa Bagi (%) : {a % b}")
    print(f"Eksponensial (**)    : {a ** 2}")
    print()

def demonstrasi_perbandingan_dan_logika():
    """Menampilkan evaluasi relasional dan short-circuit boolean."""
    print("=== 2. Operator Relasional & Logika ===")
    rsrp = -88
    ambang = -90
    print(f"RSRP Terukur: {rsrp} dBm | Ambang Batas: {ambang} dBm")
    print(f"Kondisi Sinyal Memenuhi Syarat (rsrp >= ambang): {rsrp >= ambang}")
    
    daya_aktif = True
    suhu_normal = True
    gangguan = False
    siap_operasional = daya_aktif and suhu_normal and not gangguan
    print(f"Status Operasional Node (AND / NOT): {siap_operasional}")
    
    # Pembuktian short-circuit logic
    hasil_sc = False and (10 / 0 == 0)
    print(f"Uji Short-circuit AND (False and 10/0): {hasil_sc} (Aman dari ZeroDivisionError)")
    print()

def hitung_panjang_gelombang(frekuensi_hz: float, c: float = 3e8) -> float:
    """Menghitung panjang gelombang elektromagnetik: lambda = c / f."""
    return c / frekuensi_hz

def konversi_mw_ke_dbm(daya_mw: float) -> float:
    """Mengonversi daya dari miliwatt ke dBm: P_dBm = 10 * log10(P_mW)."""
    return 10 * math.log10(daya_mw)

def demonstrasi_studi_kasus_telekomunikasi():
    """Aplikasi formula fisika gelombang radio dan anggaran daya."""
    print("=== 3. Studi Kasus Telekomunikasi: Panjang Gelombang & Daya ===")
    f_hz = 1.8e9  # 1.8 GHz (LTE Band 3)
    p_mw = 40000.0  # 40 Watt pemancar

    panjang_gelombang_m = hitung_panjang_gelombang(f_hz)
    level_dbm = konversi_mw_ke_dbm(p_mw)

    print(f"Frekuensi Pembawa   : {f_hz / 1e6:.1f} MHz")
    print(f"Panjang Gelombang   : {panjang_gelombang_m * 100:.2f} cm")
    print(f"Daya Pemancar (mW)  : {p_mw} mW")
    print(f"Daya Pemancar (dBm) : {level_dbm:.2f} dBm")
    print()

if __name__ == "__main__":
    demonstrasi_operator_aritmatika()
    demonstrasi_perbandingan_dan_logika()
    demonstrasi_studi_kasus_telekomunikasi()
    print("Seluruh modul demonstrasi Chapter 03 berhasil dieksekusi.")

