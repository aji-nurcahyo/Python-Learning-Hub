"""
Tugas Praktik 01: Verifikasi Environment Node Telekomunikasi
Mata Kuliah: Algoritma & Pemrograman / Python Learning Hub
Program Studi: Teknik Telekomunikasi - ITERA
Nama Mahasiswa: [Isi Nama Anda]
NIM           : [Isi NIM Anda]
"""

import sys
import platform

def inspeksi_node() -> None:
    """Membaca parameter runtime interpreter dan mencetak status kesiapan node."""
    # 1. Dapatkan versi sistem operasi dan versi interpreter CPython
    nama_os = platform.system()
    versi_python = sys.version.split()[0]
    
    # 2. Parameter stasiun pemancar
    node_id = "NODE-TELKOM-ITERA-01"
    frekuensi_mhz = 1800.0
    
    # 3. Hitung waktu rambat propagasi untuk jarak 1000 meter (1 km)
    # Rumus: t = (jarak / kecepatan_cahaya) * 1e6 mikrodetik
    jarak_m = 1000.0
    c = 3e8
    waktu_mikrodetik = (jarak_m / c) * 1e6
    
    # 4. Tampilkan kartu laporan ke konsol terminal
    print("=" * 50)
    print("     SISTEM MONITORING NODE TELEKOMUNIKASI")
    print("=" * 50)
    print(f"Sistem Operasi      : {nama_os}")
    print(f"Versi CPython       : {versi_python}")
    print(f"ID Perangkat Node   : {node_id}")
    print(f"Frekuensi Dasar     : {frekuensi_mhz} MHz")
    print(f"Waktu Propagasi (1km): {waktu_mikrodetik:.2f} mikrodetik")
    print("Status Inisialisasi : OPERASIONAL / SIAP")
    print("=" * 50)

if __name__ == "__main__":
    inspeksi_node()
