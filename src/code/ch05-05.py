# Klasifikasi Kualitas Sinyal Seluler (RSRP)
# File: ch05-05.py

# CATATAN PEDAGOGIS:
# Ambang batas RSRP berikut adalah asumsi pembelajaran untuk ilustrasi percabangan logika,
# bukan standar tunggal mutlak universal pada semua operator telekomunikasi.

def klasifikasi_sinyal_rsrp(rsrp_dbm: float) -> str:
    """Mengklasifikasikan kualitas sinyal berdasarkan ambang batas pedagogis."""
    if rsrp_dbm >= -80.0:
        return "Sangat Baik (Excellent)"
    elif rsrp_dbm >= -90.0:
        return "Baik (Good)"
    elif rsrp_dbm >= -100.0:
        return "Cukup (Fair)"
    else:
        return "Buruk (Poor)"

data_pengukuran = [-74.0, -84.5, -96.0, -112.0]

for sinyal in data_pengukuran:
    kategori = klasifikasi_sinyal_rsrp(sinyal)
    print(f"RSRP Terukur: {sinyal:6.1f} dBm -> Kategori: {kategori}")
