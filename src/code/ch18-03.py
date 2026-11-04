"""Contoh 18.3: Penanganan Multi-Exception Spesifik (KeyError, IndexError, TypeError)
Python Learning Hub - Level 2: Intermediate
"""

def ambil_metrik_sinyal(daftar_node: list[dict], indeks: int, kunci: str) -> float | None:
    """Mengakses metrik node secara aman dari list of dictionaries."""
    try:
        node = daftar_node[indeks]
        nilai = node[kunci]
        nilai_numerik = float(nilai)
        return nilai_numerik
    except IndexError:
        print(f"IndexError: Indeks ke-{indeks} berada di luar rentang (Total: {len(daftar_node)}).")
        return None
    except KeyError:
        print(f"KeyError: Kunci '{kunci}' tidak ditemukan pada rekaman node.")
        return None
    except (TypeError, ValueError) as err:
        print(f"TypeError/ValueError: Gagal konversi nilai menjadi numerik ({err}).")
        return None

database_node = [
    {"id": "N-01", "rsrp": -85.5, "snr": 22.0},
    {"id": "N-02", "rsrp": "TIDAK_TERSEDIA", "snr": 18.4},
]

print("Pengujian Akses Multi-Exception:")
print("1. Sukses       :", ambil_metrik_sinyal(database_node, 0, "rsrp"))
print("2. Indeks Salah :", ambil_metrik_sinyal(database_node, 5, "rsrp"))
print("3. Kunci Hilang :", ambil_metrik_sinyal(database_node, 0, "suhu"))
print("4. Nilai Cacat  :", ambil_metrik_sinyal(database_node, 1, "rsrp"))
