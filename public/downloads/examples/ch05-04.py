# Validasi Multi-Kondisi Status Perangkat Jaringan
# File: ch05-04.py

def evaluasi_kesiapan_node(tegangan_volt: float, suhu_c: float, terhubung_jaringan: bool) -> tuple[bool, str]:
    """Mengevaluasi parameter operasional multi-kondisi."""
    tegangan_aman = 44.0 <= tegangan_volt <= 56.0  # Standar DC 48V telecom
    suhu_aman = 10.0 <= suhu_c <= 55.0

    if tegangan_aman and suhu_aman and terhubung_jaringan:
        return True, "Node Siap Beroperasi Penuh"
    elif not tegangan_aman:
        return False, "Alarm: Tegangan Suplai Di Luar Batas Toleransi"
    elif not suhu_aman:
        return False, "Alarm: Peringatan Suhu Kritis Ruang Rak"
    else:
        return False, "Peringatan: Tautan Jaringan Belum Terkoneksi"

uji_node = [
    (48.0, 32.5, True),
    (41.0, 30.0, True),
    (48.0, 68.0, True),
    (48.0, 28.0, False)
]

for v, t, conn in uji_node:
    siap, pesan = evaluasi_kesiapan_node(v, t, conn)
    print(f"V={v}V, T={t}C, Conn={conn} -> Siap: {siap} | Pesan: {pesan}")

