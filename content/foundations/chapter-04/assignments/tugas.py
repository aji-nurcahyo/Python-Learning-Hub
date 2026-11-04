"""
Tugas Praktik 04: Generator Kartu Telemetri Node Jaringan
Mata Kuliah: Algoritma & Pemrograman / Python Learning Hub
Program Studi: Teknik Telekomunikasi - ITERA
Nama Mahasiswa: [Isi Nama Anda]
NIM           : [Isi NIM Anda]
"""

def generate_laporan_telemetri(daftar_node: list[dict]) -> None:
    """Mencetak kartu laporan telemetri stasiun pemancar terformat rapi."""
    lebar_total = 82
    garis_tebal = "=" * lebar_total
    garis_tipis = "-" * lebar_total

    print(garis_tebal)
    print(f"{'PUSAT OPERASI JARINGAN (NOC) — MONITORING TELEMETRI NODE':^{lebar_total}}")
    print(garis_tebal)
    print(
        f"{'ID NODE':<10} | "
        f"{'LOKASI STASIUN':<20} | "
        f"{'FREKUENSI':^14} | "
        f"{'DAYA TX':^10} | "
        f"{'PKT LOSS':>10} | "
        f"{'STATUS':>8}"
    )
    print(garis_tipis)

    total_daya = 0.0
    total_loss = 0.0

    for node in daftar_node:
        total_daya += node["daya"]
        total_loss += node["loss"]
        frek_str = f"{node['frekuensi']:.1f} MHz"
        daya_str = f"{node['daya']:.1f} W"
        loss_str = f"{node['loss']:.2%}"

        print(
            f"{node['id']:<10} | "
            f"{node['lokasi']:<20} | "
            f"{frek_str:^14} | "
            f"{daya_str:^10} | "
            f"{loss_str:>10} | "
            f"{node['status']:>8}"
        )

    print(garis_tipis)
    n = len(daftar_node)
    rata_daya = total_daya / n if n > 0 else 0.0
    rata_loss = total_loss / n if n > 0 else 0.0

    print(f"Total Stasiun Aktif : {n} Node")
    print(f"Rata-Rata Daya TX   : {rata_daya:.2f} Watt")
    print(f"Rata-Rata Pkt Loss  : {rata_loss:.2%}")
    print(garis_tebal)

if __name__ == "__main__":
    nodes_sample = [
        {"id": "NODE-01", "lokasi": "Gedung Kuliah A", "frekuensi": 900.0, "daya": 20.0, "loss": 0.0045, "status": "ONLINE"},
        {"id": "NODE-02", "lokasi": "Lab Telekomunikasi", "frekuensi": 1800.5, "daya": 40.0, "loss": 0.0120, "status": "ONLINE"},
        {"id": "NODE-03", "lokasi": "Gedung Rektorat", "frekuensi": 2100.0, "daya": 45.0, "loss": 0.0350, "status": "STANDBY"},
        {"id": "NODE-04", "lokasi": "Gerbang Utama", "frekuensi": 2600.0, "daya": 10.0, "loss": 0.0580, "status": "ALERT"},
    ]
    generate_laporan_telemetri(nodes_sample)
