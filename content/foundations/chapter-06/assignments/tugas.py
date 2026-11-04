"""
Tugas Praktik 06: Sensor Data Monitoring Simulator
Mata Kuliah: Algoritma & Pemrograman / Python Learning Hub
Program Studi: Teknik Telekomunikasi - ITERA
Nama Mahasiswa: [Isi Nama Anda]
NIM           : [Isi NIM Anda]
"""

def jalankan_simulator_sensor(aliran_suhu: list[float], ambang_waspada: float = 35.0, batas_kritis: float = 80.0) -> dict:
    """Memproses aliran telemetri sensor menggunakan perulangan dan kontrol alur."""
    print("=" * 70)
    print("       SIMULATOR PEMANTAUAN TELEMETRI SENSOR BTS (ENGINE 06)")
    print("=" * 70)

    total_valid = 0.0
    cacah_valid = 0
    cacah_waspada = 0
    nilai_min = None
    nilai_max = None
    dihentikan_paksa = False
    detik_terproses = 0

    for detik, suhu in enumerate(aliran_suhu, start=1):
        detik_terproses = detik

        # 1. Penyaringan glitch / noise dengan continue
        if suhu == -999.0:
            print(f"Detik {detik:02d}: [SENSOR NOISE] Nilai -999.0 C terdeteksi! Pembacaan dilewati.")
            continue

        # 2. Terminasi darurat jika suhu kritis dengan break
        if suhu >= batas_kritis:
            print(f"Detik {detik:02d}: [ALARM KRITIS] Suhu {suhu:.1f} C melampaui batas darurat ({batas_kritis:.1f} C)!")
            print("          Prosedur darurat aktif: Loop monitoring dihentikan segera.")
            dihentikan_paksa = True
            break

        # 3. Akumulasi data valid
        total_valid += suhu
        cacah_valid += 1

        if nilai_min is None or suhu < nilai_min:
            nilai_min = suhu
        if nilai_max is None or suhu > nilai_max:
            nilai_max = suhu

        # 4. Deteksi ambang waspada
        if suhu >= ambang_waspada:
            cacah_waspada += 1
            status = f"[PERINGATAN] Suhu Tinggi (>= {ambang_waspada} C)"
        else:
            status = "NORMAL"

        print(f"Detik {detik:02d}: Suhu = {suhu:4.1f} C | Status: {status}")

    rata_rata = total_valid / cacah_valid if cacah_valid > 0 else 0.0

    return {
        "detik_total": detik_terproses,
        "cacah_valid": cacah_valid,
        "cacah_waspada": cacah_waspada,
        "min": nilai_min if nilai_min is not None else 0.0,
        "max": nilai_max if nilai_max is not None else 0.0,
        "rata_rata": rata_rata,
        "alarm_aktif": dihentikan_paksa
    }

def cetak_ringkasan_statistik(ringkasan: dict) -> None:
    """Mencetak kartu ringkasan hasil pemantauan ke konsol terminal."""
    print("-" * 70)
    print("                   RINGKASAN STATISTIK TELEMETRI")
    print("-" * 70)
    print(f"Total Siklus Waktu      : {ringkasan['detik_total']} Detik")
    print(f"Total Sampel Valid      : {ringkasan['cacah_valid']} Sampel")
    print(f"Jumlah Peringatan (>=35): {ringkasan['cacah_waspada']} Kejadian")
    print(f"Suhu Minimum Terbaca    : {ringkasan['min']:.1f} C")
    print(f"Suhu Maksimum Terbaca   : {ringkasan['max']:.1f} C")
    print(f"Suhu Rata-Rata Valid    : {ringkasan['rata_rata']:.2f} C")
    status_akhir = "TERHENTI OLEH INTERUPSI ALARM KRITIS" if ringkasan["alarm_aktif"] else "SELESAI NORMAL TANPA INTERUPSI"
    print(f"Status Akhir Operasi    : {status_akhir}")
    print("=" * 70)

if __name__ == "__main__":
    sampel_data = [26.5, 28.0, 31.2, -999.0, 35.4, 38.0, 42.5, 85.0, 27.0]
    hasil = jalankan_simulator_sensor(sampel_data)
    cetak_ringkasan_statistik(hasil)
