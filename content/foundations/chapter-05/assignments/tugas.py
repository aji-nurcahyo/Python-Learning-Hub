"""
Tugas Praktik 05: Student Grade and Signal Quality Classifier
Mata Kuliah: Algoritma & Pemrograman / Python Learning Hub
Program Studi: Teknik Telekomunikasi - ITERA
Nama Mahasiswa: [Isi Nama Anda]
NIM           : [Isi NIM Anda]
"""

def klasifikasi_nilai_akademik(skor: float) -> tuple[bool, str, str]:
    """
    Memvalidasi dan mengklasifikasikan skor akademik mahasiswa.
    Returns: (is_valid, grade, keterangan)
    """
    if skor < 0.0 or skor > 100.0:
        return False, "-", f"Ditolak: Skor {skor} di luar rentang sah (0 - 100)"

    if skor >= 80.0:
        return True, "A", "Sangat Memuaskan (Kinerja Istimewa)"
    elif skor >= 70.0:
        return True, "B", "Memuaskan (Di atas standar rata-rata)"
    elif skor >= 60.0:
        return True, "C", "Cukup (Memenuhi kompetensi dasar minimum)"
    elif skor >= 50.0:
        return True, "D", "Kurang (Perlu perbaikan tugas tambahan)"
    else:
        return True, "E", "Gagal (Wajib mengulang mata kuliah)"

def klasifikasi_kualitas_rsrp(rsrp_dbm: float) -> tuple[bool, str, str]:
    """
    Memvalidasi dan mengklasifikasikan kekuatan sinyal seluler RSRP.
    Catatan Pedagogis: Ambang batas adalah asumsi instruksional pembelajaran.
    Returns: (is_valid, kategori, keterangan)
    """
    if rsrp_dbm < -140.0 or rsrp_dbm > -40.0:
        return False, "-", f"Ditolak: RSRP {rsrp_dbm} dBm di luar rentang fisik (-140 s.d. -40 dBm)"

    if rsrp_dbm >= -80.0:
        return True, "Sangat Baik", "Latensi minimal, modulasi tertinggi, throughput maksimal"
    elif rsrp_dbm >= -90.0:
        return True, "Baik", "Kualitas stabil untuk panggilan VoLTE dan transmisi video HD"
    elif rsrp_dbm >= -100.0:
        return True, "Cukup", "Batas minimum kenyamanan browsing, risiko degradasi kecepatan"
    else:
        return True, "Buruk", "Sinyal sangat lemah, risiko tinggi mengalami call drop"

def demonstrasi_pengujian():
    """Menjalankan kasus uji batas untuk kedua mesin klasifikasi."""
    print("=" * 70)
    print("       SISTEM KLASIFIKASI KONDISIONAL CERDAS (ENGINE 05)")
    print("=" * 70)

    print("\n--- PENGUJIAN 1: NILAI AKADEMIK MAHASISWA ---")
    uji_skor = [80.0, 79.9, 65.0, 50.0, 49.9, 105.0, -5.0]
    for s in uji_skor:
        valid, grade, ket = klasifikasi_nilai_akademik(s)
        if valid:
            print(f"Input Skor : {s:5.1f} -> Grade: {grade} | Keterangan: {ket}")
        else:
            print(f"Input Skor : {s:5.1f} -> {ket}")

    print("\n--- PENGUJIAN 2: KUALITAS SINYAL RSRP SELULER ---")
    uji_rsrp = [-78.5, -80.0, -89.9, -90.0, -100.0, -112.0, -150.0]
    for r in uji_rsrp:
        valid, kat, ket = klasifikasi_kualitas_rsrp(r)
        if valid:
            print(f"Input RSRP : {r:6.1f} dBm -> Kategori: {kat:<12} | {ket}")
        else:
            print(f"Input RSRP : {r:6.1f} dBm -> {ket}")

    print("=" * 70)

if __name__ == "__main__":
    demonstrasi_pengujian()

