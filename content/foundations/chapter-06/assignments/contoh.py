"""
Koleksi Contoh Kode Komputasi Terpadu - Chapter 06: Loops & Iteration
Python Learning Hub - Rekayasa Telekomunikasi
"""

def demonstrasi_range_dan_for():
    """Menampilkan ragam deret bilangan menggunakan range()."""
    print("=== 1. Deret Bilangan range() ===")
    print("range(5)         :", list(range(5)))
    print("range(1, 6)      :", list(range(1, 6)))
    print("range(10, 31, 5) :", list(range(10, 31, 5)))
    print("range(5, 0, -1)  :", list(range(5, 0, -1)))
    print()

def demonstrasi_akumulator_dan_statistik():
    """Menghitung total, rata-rata, min, dan max dari deret data sinyal."""
    print("=== 2. Pola Akumulator, Min & Max ===")
    sampel_daya = [25.0, 32.5, 40.0, 18.5, 50.0]

    total = 0.0
    cacah = 0
    nilai_min = sampel_daya[0]
    nilai_max = sampel_daya[0]

    for d in sampel_daya:
        total += d
        cacah += 1
        if d < nilai_min:
            nilai_min = d
        if d > nilai_max:
            nilai_max = d

    rata_rata = total / cacah if cacah > 0 else 0.0

    print(f"Data Daya Transmisi (mW) : {sampel_daya}")
    print(f"Jumlah Sampel Terbaca    : {cacah}")
    print(f"Total Akumulasi Daya     : {total:.1f} mW")
    print(f"Nilai Rata-Rata          : {rata_rata:.2f} mW")
    print(f"Daya Minimum             : {nilai_min:.1f} mW")
    print(f"Daya Maksimum            : {nilai_max:.1f} mW")
    print()

def demonstrasi_aliran_sensor_loop_control():
    """Simulasi pemrosesan telemetri sensor dengan break dan continue."""
    print("=== 3. Aliran Sensor dengan break dan continue ===")
    aliran_suhu = [28.5, 31.0, -999.0, 34.2, 85.0, 30.0]

    for detik, suhu in enumerate(aliran_suhu, start=1):
        if suhu == -999.0:
            print(f"Detik {detik}: Glitch sensor (-999.0 C) dilewati dengan continue.")
            continue
        if suhu >= 80.0:
            print(f"Detik {detik}: [ALARM KRITIS] Suhu {suhu} C melampaui batas aman! Hentikan dengan break.")
            break
        print(f"Detik {detik}: Suhu normal terukur = {suhu:.1f} C")
    print()

def demonstrasi_matriks_antena():
    """Pembangkitan kisi matriks antena MIMO dengan nested loop."""
    print("=== 4. Kisi Matriks Antena MIMO (Nested Loop) ===")
    for r in range(1, 4):
        for c in range(1, 5):
            print(f"[A{r}{c}]", end=" ")
        print()
    print()

if __name__ == "__main__":
    demonstrasi_range_dan_for()
    demonstrasi_akumulator_dan_statistik()
    demonstrasi_aliran_sensor_loop_control()
    demonstrasi_matriks_antena()
    print("Seluruh modul demonstrasi Chapter 06 berhasil dieksekusi.")
