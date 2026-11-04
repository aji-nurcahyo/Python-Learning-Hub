"""Contoh 22.5: Integrasi Pipeline Laporan Diagnostik & Analitik Capstone
Python Learning Hub - Level 2: Intermediate Capstone Project
"""

class InventoryAnalytics:
    @staticmethod
    def ringkas_portofolio(items: list[dict]) -> dict:
        total_aset = sum(item["price"] for item in items)
        kategori_count = {}
        for item in items:
            cat = item["category"]
            kategori_count[cat] = kategori_count.get(cat, 0) + 1
        return {
            "total_unit": len(items),
            "total_nilai_aset": total_aset,
            "rerata_harga": total_aset / len(items) if items else 0.0,
            "distribusi_kategori": kategori_count
        }

devices_sample = [
    {"id": "DEV-01", "name": "Core Router BGP", "category": "Network", "price": 18000000.0},
    {"id": "DEV-02", "name": "Access Switch 48P", "category": "Network", "price": 8500000.0},
    {"id": "DEV-03", "name": "Database Server Blade", "category": "Server", "price": 45000000.0},
    {"id": "DEV-04", "name": "Suhu & Kelembaban IoT", "category": "Sensor", "price": 750000.0},
]

analisis = InventoryAnalytics.ringkas_portofolio(devices_sample)

print("==================================================")
print("  LAPORAN AUDIT & ANALITIK PORTOFOLIO INVENTARIS  ")
print("==================================================")
print(f"Total Unit Perangkat : {analisis['total_unit']}")
print(f"Total Nilai Aset     : Rp {analisis['total_nilai_aset']:,.2f}")
print(f"Nilai Rata-rata/Unit : Rp {analisis['rerata_harga']:,.2f}")
print("Distribusi per Kategori:")
for cat, count in sorted(analisis["distribusi_kategori"].items()):
    print(f"  * {cat:<10}: {count} unit")
print("==================================================")
