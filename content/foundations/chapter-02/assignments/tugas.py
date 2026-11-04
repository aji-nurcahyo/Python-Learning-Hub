"""
Tugas Praktik 02: Validasi Parameter Transceiver BTS
Mata Kuliah: Algoritma & Pemrograman / Python Learning Hub
Program Studi: Teknik Telekomunikasi - ITERA
Nama Mahasiswa: [Isi Nama Anda]
NIM           : [Isi NIM Anda]
"""

def proses_konfigurasi_bts(
    raw_name: str,
    raw_freq: str,
    raw_power: str,
    raw_status: str
) -> dict:
    """Mengonversi dan memvalidasi konfigurasi parameter stasiun BTS."""
    # 1. Bersihkan dan konversikan tipe data
    bts_name: str = raw_name.strip()
    frekuensi_mhz: float = float(raw_freq)
    daya_watt: int = int(raw_power)
    status_aktif: bool = bool(int(raw_status))
    
    # 2. Validasi kesesuaian tipe dan rentang nilai
    valid_name = isinstance(bts_name, str) and len(bts_name) > 5
    valid_freq = isinstance(frekuensi_mhz, (int, float)) and (700.0 <= frekuensi_mhz <= 3500.0)
    valid_power = isinstance(daya_watt, int) and (1 <= daya_watt <= 100)
    valid_status = isinstance(status_aktif, bool)
    
    semua_valid = valid_name and valid_freq and valid_power and valid_status
    
    return {
        "nama": bts_name,
        "frekuensi": frekuensi_mhz,
        "daya": daya_watt,
        "aktif": status_aktif,
        "valid": semua_valid
    }

def tampilkan_laporan(hasil: dict) -> None:
    """Mencetak kartu laporan validasi parameter ke konsol terminal."""
    print("=" * 50)
    print("        VALIDASI KONFIGURASI TRANSCEIVER BTS")
    print("=" * 50)
    print(f"Nama Stasiun      : {hasil['nama']} (str, {len(hasil['nama'])} karakter)")
    print(f"Frekuensi Operasi : {hasil['frekuensi']} MHz ({type(hasil['frekuensi']).__name__})")
    print(f"Daya Pancar       : {hasil['daya']} W ({type(hasil['daya']).__name__})")
    print(f"Status Aktif      : {hasil['aktif']} ({type(hasil['aktif']).__name__})")
    print("-" * 50)
    status_teks = "SEMUA PARAMETER VALID (SIAP TRANSMISI)" if hasil["valid"] else "PARAMETER TIDAK VALID!"
    print(f"Status Validasi   : {status_teks}")
    print("=" * 50)

if __name__ == "__main__":
    raw_bts_name = "  BTS-LampungSelatan-02  "
    raw_frequency_mhz = "2100.5"
    raw_tx_power_watt = "40"
    raw_is_operational = "1"
    
    hasil_uji = proses_konfigurasi_bts(raw_bts_name, raw_frequency_mhz, raw_tx_power_watt, raw_is_operational)
    tampilkan_laporan(hasil_uji)
