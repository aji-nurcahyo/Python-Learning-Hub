"""
Koleksi Contoh Kode Komputasi Terpadu - Chapter 04: Input & Output
Python Learning Hub - Rekayasa Telekomunikasi
"""

def demonstrasi_print_kontrol():
    """Menampilkan parameter sep dan end pada fungsi print()."""
    print("=== 1. Kontrol Argumen print(sep, end) ===")
    print("Node-A", "Node-B", "Node-C", sep=" -> ")
    print("IP Address Gateway", "192.168.1.1", sep=": ")
    print("Inisialisasi koneksi", end="...")
    print(" [TERHUBUNG]\n")

def demonstrasi_fstrings_dan_specifiers():
    """Menampilkan fitur formatted string literals (f-strings) modern."""
    print("=== 2. Pemformatan Teks f-Strings & Specifiers ===")
    nama_bts = "BTS-Gedung-A"
    frekuensi_mhz = 1800.4567
    daya_watt = 43.528
    efisiensi = 0.9425
    id_antena = 9

    # Interpolasi variabel dan format specifier
    print(f"Nama Stasiun      : {nama_bts.upper()}")
    print(f"Frekuensi (2 des) : {frekuensi_mhz:.2f} MHz")
    print(f"Daya Pancar       : {daya_watt:.1f} W")
    print(f"Efisiensi Emisi   : {efisiensi:.1%}")
    print(f"ID Antena Padding : ANT-{id_antena:04d}")
    print(f"Total Bandwidth   : {20000000:,} Hz\n")

def demonstrasi_tabel_telemetri():
    """Menampilkan laporan tabel berformat dengan perataan kolom konsisten."""
    print("=== 3. Format Tabel Telemetri Node Jaringan ===")
    garis = "=" * 48
    print(garis)
    print(f"{'KODE BTS':<12} | {'FREKUENSI':^14} | {'DAYA':^8} | {'STATUS':>8}")
    print(garis)

    data_transceiver = [
        ("BTS-01", 900.0, 20.0, "ONLINE"),
        ("BTS-02", 1800.5, 40.0, "ONLINE"),
        ("BTS-03", 2100.0, 45.0, "STANDBY"),
        ("BTS-04", 2600.0, 10.0, "OFFLINE"),
    ]

    for kode, frek, daya, status in data_transceiver:
        print(f"{kode:<12} | {frek:^10.1f} MHz | {daya:^6.1f} W | {status:>8}")
    print(garis)
    print()

if __name__ == "__main__":
    demonstrasi_print_kontrol()
    demonstrasi_fstrings_dan_specifiers()
    demonstrasi_tabel_telemetri()
    print("Seluruh modul demonstrasi Chapter 04 berhasil dieksekusi.")

