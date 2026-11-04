"""Contoh 13.2: Variable-Length Arguments (*args & **kwargs) dan Unpacking
Python Learning Hub - Level 2: Intermediate
"""

# 1. *args: Menerima argumen posisi tak hingga sebagai tuple
def hitung_total_bandwidth(*aliran_kbps: float) -> float:
    print(f"Argumen diterima (*args): {aliran_kbps} (Tipe: {type(aliran_kbps).__name__})")
    return sum(aliran_kbps)

print("Total 1:", hitung_total_bandwidth(128.5, 256.0, 512.0))
print("Total 2:", hitung_total_bandwidth())

# 2. **kwargs: Menerima argumen kata kunci tak hingga sebagai dict
def buat_profil_server(nama_host: str, **parameter: object) -> None:
    print(f"\nProfil Server '{nama_host}':")
    for kunci, nilai in parameter.items():
        print(f"  - {kunci}: {nilai}")

buat_profil_server("srv-core-01", ip="192.168.1.10", ram_gb=32, os="Linux", status="AKTIF")

# 3. Argument Unpacking (* pada sequence, ** pada dictionary)
paket_data = [64.0, 128.0, 256.0]
print("\nUnpacking List ke *args:", hitung_total_bandwidth(*paket_data))

opsi_tambahan = {"cpu_cores": 16, "lokasi": "Gedung Labtek 3"}
buat_profil_server("srv-backup-02", **opsi_tambahan)

