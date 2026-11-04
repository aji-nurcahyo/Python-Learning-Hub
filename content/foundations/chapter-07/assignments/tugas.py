"""
Tugas Praktik 07: Device Identifier & Sensor Message Processor
Mata Kuliah: Algoritma & Pemrograman / Python Learning Hub
Program Studi: Teknik Telekomunikasi - ITERA
Nama Mahasiswa: [Isi Nama Anda]
NIM           : [Isi NIM Anda]
"""

def validasi_format_device_id(device_id: str) -> tuple[bool, str]:
    """
    Kaidah ID Perangkat:
    1. Diawali dengan 'NODE-'
    2. Format 3 segmen: PREFIX-LOKASI-UNIT (Contoh: 'NODE-LPG-0123')
    3. Segmen 2 harus 3 huruf alfabet kapital
    4. Segmen 3 harus 4 digit angka numerik
    """
    id_bersih = device_id.strip()

    if not id_bersih.startswith("NODE-"):
        return False, "Harus diawali prefiks 'NODE-'"

    segmen = id_bersih.split("-")
    if len(segmen) != 3:
        return False, f"Harus terdiri dari 3 segmen dipisahkan tanda strip (ditemukan: {len(segmen)})"

    prefiks, lokasi, unit = segmen

    if len(lokasi) != 3 or not lokasi.isalpha() or not lokasi.isupper():
        return False, f"Segmen lokasi '{lokasi}' harus 3 huruf alfabet kapital"

    if len(unit) != 4 or not unit.isdigit():
        return False, f"Segmen unit '{unit}' harus tepat 4 digit angka"

    return True, f"Lokasi: {lokasi}, Unit: {unit}"

def parse_sensor_payload(payload_str: str) -> dict:
    """Mengurai string payload telemetri mentah menjadi dictionary terstruktur."""
    # 1. Bersihkan whitespace dan buang prefiks RAW_MSG: jika ada
    teks_bersih = payload_str.strip()
    if teks_bersih.startswith("RAW_MSG:"):
        teks_bersih = teks_bersih[len("RAW_MSG:"):]

    # 2. Pecah pasangan kunci=nilai berdasarkan delimiter titik-koma ';'
    field_list = teks_bersih.split(";")
    data_dict = {}

    for item in field_list:
        item_bersih = item.strip()
        if "=" in item_bersih:
            kunci, nilai = item_bersih.split("=", 1)
            data_dict[kunci.strip()] = nilai.strip()

    # 3. Normalisasi status operasional
    if "STAT" in data_dict:
        data_dict["STAT"] = data_dict["STAT"].upper()

    return data_dict

def tampilkan_laporan_lengkap(payload_mentah: str) -> None:
    """Menampilkan hasil validasi dan penguraian telemetri terpadu."""
    print("=" * 70)
    print("     GERBANG TELEMETRI IOT: PARSER PESAN & IDENTIFIER (ENGINE 07)")
    print("=" * 70)

    print("\n--- 1. UJI VALIDASI FORMAT IDENTIFIER PERANGKAT ---")
    daftar_uji_id = ["NODE-LPG-0123", "NODE-BDL-99", "GATEWAY-01", "NODE-sks-1234"]
    for id_uji in daftar_uji_id:
        is_valid, catatan = validasi_format_device_id(id_uji)
        status_str = "VALID  " if is_valid else "DITOLAK"
        print(f"Uji '{id_uji:<15}' -> {status_str} | {catatan}")

    print("\n--- 2. PENGURAIAN PAYLOAD TELEMETRI SENSOR ---")
    print(f"Payload Mentah       : '{payload_mentah}'")
    hasil = parse_sensor_payload(payload_mentah)

    dev_id = hasil.get("ID", "-")
    id_valid, id_info = validasi_format_device_id(dev_id)
    id_status = "VALID" if id_valid else "INVALID"

    print(f"Identitas Perangkat  : {dev_id} (Status ID: {id_status})")
    print(f"Suhu Sensor          : {hasil.get('TEMP', '-')}")
    print(f"Sisa Daya Baterai    : {hasil.get('BATT', '-')}")
    print(f"Kuat Sinyal RSRP     : {hasil.get('RSRP', '-')}")
    print(f"Status Operasional   : {hasil.get('STAT', '-')} (Ternormalisasi)")
    print("-" * 70)

    lokasi = dev_id.split("-")[1] if id_valid else "UNKNOWN"
    pesan_ringkas = f"Node {dev_id} [{lokasi}] beroperasi {hasil.get('STAT', '-')} dengan baterai {hasil.get('BATT', '-')}"
    print(f"Pesan Status Ringkas : \"{pesan_ringkas}\"")
    print("=" * 70)

if __name__ == "__main__":
    sampel_payload = "  RAW_MSG:ID=NODE-LPG-0123;TEMP=36.4C;BATT=94%;RSRP=-82.5dBm;STAT=ok  "
    tampilkan_laporan_lengkap(sampel_payload)

