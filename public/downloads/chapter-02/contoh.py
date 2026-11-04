"""
Koleksi Contoh Kode Komputasi Terpadu - Chapter 02: Variables & Data Types
Python Learning Hub - Rekayasa Telekomunikasi
"""

def demonstrasi_variabel_dan_referensi():
    """Menunjukkan cara kerja penugasan variabel dan identitas memori."""
    print("=== 1. Demonstrasi Variabel & Referensi Memori ===")
    nama_stasiun = "BTS-Sukarame-01"
    id_node = 1042
    salinan_id = id_node

    print(f"Nama Stasiun: {nama_stasiun} (id: {id(nama_stasiun)})")
    print(f"ID Node: {id_node} (id: {id(id_node)})")
    print(f"Salinan ID: {salinan_id} (id: {id(salinan_id)})")
    print("Apakah merujuk objek identik?", salinan_id is id_node)
    print()

def demonstrasi_tipe_skalar():
    """Menampilkan inspeksi tipe data skalar int, float, str, bool."""
    print("=== 2. Tipe Data Skalar Primitif ===")
    jumlah_antena = 4
    frekuensi_ghz = 2.45
    nama_protokol = "IEEE 802.11ax"
    operasional = True

    data = [
        ("jumlah_antena", jumlah_antena),
        ("frekuensi_ghz", frekuensi_ghz),
        ("nama_protokol", nama_protokol),
        ("operasional", operasional),
    ]

    for label, val in data:
        print(f"Variabel: {label:<16} | Nilai: {str(val):<14} | Tipe: {type(val).__name__}")
    print()

def demonstrasi_type_casting():
    """Melakukan konversi eksplisit antar tipe data."""
    print("=== 3. Konversi Tipe Data Eksplisit (Type Casting) ===")
    teks_frek = "1800"
    f_int = int(teks_frek)
    f_float = float(teks_frek)

    print(f"String '{teks_frek}' -> int: {f_int} ({type(f_int).__name__})")
    print(f"String '{teks_frek}' -> float: {f_float} ({type(f_float).__name__})")
    print(f"Evaluasi Truthy/Falsy:")
    print(f"  bool(0)     : {bool(0)}")
    print(f"  bool(100)   : {bool(100)}")
    print(f"  bool('')    : {bool('')}")
    print(f"  bool('0')   : {bool('0')} (karena string tidak kosong)")
    print()

def validasi_parameter_bts(node_id: str, frekuensi: float, daya: int, status: bool) -> bool:
    """Memvalidasi tipe data parameter stasiun pemancar dengan isinstance()."""
    cek_id = isinstance(node_id, str)
    cek_frek = isinstance(frekuensi, (int, float))
    cek_daya = isinstance(daya, int)
    cek_status = isinstance(status, bool)
    return cek_id and cek_frek and cek_daya and cek_status

def demonstrasi_validasi_bts():
    """Uji coba fungsi validasi spesifikasi transceiver BTS."""
    print("=== 4. Validasi Parameter BTS dengan isinstance() ===")
    node = "BTS-BandarLampung-04"
    frek = 1800.0
    daya = 40
    aktif = True

    sukses = validasi_parameter_bts(node, frek, daya, aktif)
    print(f"Parameter Node: {node}")
    print(f"Frekuensi     : {frek} MHz")
    print(f"Daya Pancar   : {daya} W")
    print(f"Status Aktif  : {aktif}")
    print(f"Hasil Uji Validitas Tipe Data: {'VALID' if sukses else 'INVALID'}")
    print()

if __name__ == "__main__":
    demonstrasi_variabel_dan_referensi()
    demonstrasi_tipe_skalar()
    demonstrasi_type_casting()
    demonstrasi_validasi_bts()
    print("Seluruh modul demonstrasi Chapter 02 berhasil dieksekusi.")

