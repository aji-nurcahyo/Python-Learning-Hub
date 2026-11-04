"""Contoh 14.3: Dictionary Comprehensions (Pemetaan, Inversi, & Filter)
Python Learning Hub - Level 2: Intermediate
"""

# 1. Pembuatan indeks asosiatif dari koleksi rekaman
perangkat = [
    {"ip": "192.168.1.1", "host": "Gateway-Utama", "zona": "Inti"},
    {"ip": "192.168.1.2", "host": "Switch-Lt1", "zona": "Akses"},
    {"ip": "192.168.1.3", "host": "Switch-Lt2", "zona": "Akses"},
]

# Kamus lookup cepat: IP -> Nama Host
peta_ip_host = {p["ip"]: p["host"] for p in perangkat}
print("Peta IP ke Hostname:")
for ip, host in peta_ip_host.items():
    print(f"  {ip:<15} -> {host}")

# 2. Inversi kamus (Tukar Kunci dan Nilai)
kode_status = {200: "OK", 404: "NOT_FOUND", 500: "SERVER_ERROR"}
nama_ke_kode = {nilai: kunci for kunci, nilai in kode_status.items()}
print("\nInversi Kamus Status:", nama_ke_kode)

# 3. Filter kamus berdasarkan kriteria nilai
konsumsi_daya_w = {"BTS-01": 450, "BTS-02": 120, "BTS-03": 600, "BTS-04": 280}
bts_efisien = {k: v for k, v in konsumsi_daya_w.items() if v <= 300}
print("Stasiun Efisien (<= 300 W):", bts_efisien)
