"""
Koleksi Contoh Kode Komputasi Terpadu - Chapter 07: Strings & Text Processing
Python Learning Hub - Rekayasa Telekomunikasi
"""

def demonstrasi_formatting_dan_slicing():
    """Pemformatan teks, pengindeksan, dan slicing."""
    print("=== 1. Pemformatan Teks & Slicing ===")
    teks = "BTS-Sukarame-BandarLampung"
    print(f"Teks Asli          : {teks}")
    print(f"Indeks Pertama [0] : {teks[0]}")
    print(f"Indeks Terakhir[-1]: {teks[-1]}")
    print(f"Slicing [0:3]      : {teks[0:3]}")
    print(f"Slicing [4:12]     : {teks[4:12]}")
    print(f"Pembalikan [::-1]  : {teks[::-1]}")
    print()

def demonstrasi_metode_string():
    """Ragam metode esensial: strip, title, replace, split, join."""
    print("=== 2. Metode Teks: strip, replace, split, join ===")
    pesan_mentah = "  [LOG]   Perangkat  Transceiver   ONLINE...   "
    bersih = pesan_mentah.replace("[LOG]", "").replace(".", "").strip()
    kata_kata = bersih.split()
    rapi = " ".join(kata_kata)

    print(f"Pesan Mentah: '{pesan_mentah}'")
    print(f"Setelah Pembersihan Spasi: '{rapi}'")
    print(f"Format Judul             : '{rapi.title()}'")
    print()

def validasi_id_node(device_id: str) -> tuple[bool, str]:
    """Validasi format identifier perangkat telekomunikasi."""
    id_s = device_id.strip()
    if not id_s.startswith("NODE-"):
        return False, "Prefix harus 'NODE-'"
    if len(id_s) != 10:
        return False, f"Panjang harus 10 karakter (saat ini: {len(id_s)})"
    if not id_s[5:].isalnum():
        return False, "Sufiks harus alfanumerik"
    return True, "Valid"

def demonstrasi_validasi_dan_parsing():
    """Validasi ID dan parsing payload telemetri berbasis delimiter."""
    print("=== 3. Validasi ID Perangkat & Parsing Payload ===")
    uji_id = ["NODE-A0123", "NODE-99", "HUB-12345"]
    for i in uji_id:
        val, catatan = validasi_id_node(i)
        print(f"Uji ID '{i:<10}' -> Valid: {str(val):<5} | Status: {catatan}")

    payload = "NODE=NODE-01;FREQ=1800.5;PWR=40.0;STAT=ACTIVE"
    print(f"\nParsing Payload: '{payload}'")
    tokens = payload.split(";")
    data = {}
    for t in tokens:
        k, v = t.split("=")
        data[k] = v
        print(f"  Field {k:<5} -> {v}")
    print()

if __name__ == "__main__":
    demonstrasi_formatting_dan_slicing()
    demonstrasi_metode_string()
    demonstrasi_validasi_dan_parsing()
    print("Seluruh modul demonstrasi Chapter 07 berhasil dieksekusi.")
