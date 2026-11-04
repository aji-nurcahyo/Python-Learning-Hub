"""Starter Template: Network Metric Search & Ranking Engine
Tugas Praktik Chapter 15: Searching & Sorting Algorithms — Python Learning Hub
Pengembang: Aji Pamungkas Tri Nurcahyo — Institut Teknologi Sumatera

Instruksi:
Lengkapi fungsi-fungsi pencarian dan pengurutan di bawah ini.
DILARANG menggunakan sorted() atau .sort() pada fungsi urut_bubble, urut_selection, dan urut_insertion.
Gunakan sorted() dengan parameter key lambda hanya pada fungsi peringkatkan_performa_bts.
"""

from typing import Any


# ==============================================================================
# BAGIAN 1: ALGORITMA PENCARIAN (SEARCHING)
# ==============================================================================

def cari_linier_node(daftar_node: list[str], target_id: str) -> int | None:
    """Mencari target_id pada daftar_node secara linier O(n)."""
    # TODO: Implementasikan Linear Search
    for idx, item in enumerate(daftar_node):
        if item == target_id:
            return idx
    return None


def cari_biner_frekuensi(daftar_terurut: list[int], target_khz: int) -> tuple[int | None, int]:
    """Mencari target_khz pada daftar_terurut secara biner O(log n)."""
    # TODO: Implementasikan Binary Search (kembalikan indeks dan hitungan perbandingan)
    kiri = 0
    kanan = len(daftar_terurut) - 1
    langkah = 0

    while kiri <= kanan:
        langkah += 1
        tengah = (kiri + kanan) // 2
        if daftar_terurut[tengah] == target_khz:
            return tengah, langkah
        elif daftar_terurut[tengah] < target_khz:
            kiri = tengah + 1
        else:
            kanan = tengah - 1

    return None, langkah


# ==============================================================================
# BAGIAN 2: ALGORITMA PENGURUTAN MANUAL (SORTING)
# ==============================================================================

def urut_bubble(data: list[float], reverse: bool = False) -> list[float]:
    """Mengurutkan data menggunakan Bubble Sort teroptimasi."""
    # TODO: Implementasikan Bubble Sort murni
    arr = list(data)
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            should_swap = (arr[j] < arr[j + 1]) if reverse else (arr[j] > arr[j + 1])
            if should_swap:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def urut_selection(data: list[float], reverse: bool = False) -> list[float]:
    """Mengurutkan data menggunakan Selection Sort."""
    # TODO: Implementasikan Selection Sort murni
    arr = list(data)
    n = len(arr)
    for i in range(n):
        target_idx = i
        for j in range(i + 1, n):
            is_better = (arr[j] > arr[target_idx]) if reverse else (arr[j] < arr[target_idx])
            if is_better:
                target_idx = j
        if target_idx != i:
            arr[i], arr[target_idx] = arr[target_idx], arr[i]
    return arr


def urut_insertion(data: list[float], reverse: bool = False) -> list[float]:
    """Mengurutkan data menggunakan Insertion Sort."""
    # TODO: Implementasikan Insertion Sort murni
    arr = list(data)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and ((arr[j] < key) if reverse else (arr[j] > key)):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# ==============================================================================
# BAGIAN 3: PEMERINGKATAN MULTI-KRITERIA (TIMSORT)
# ==============================================================================

def peringkatkan_performa_bts(daftar_bts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Memeringkatkan BTS: Utama latensi terendah (asc), Sekunder RSRP terkuat (desc)."""
    # TODO: Gunakan sorted() dengan key tuple lambda (latensi, -rsrp)
    return sorted(daftar_bts, key=lambda b: (float(b["latensi_ms"]), -float(b["rsrp_dbm"])))


def main() -> None:
    nodes = ["BTS-01", "BTS-02", "BTS-03", "BTS-04", "BTS-05"]
    print("1. Hasil Linear Search 'BTS-04':", cari_linier_node(nodes, "BTS-04"))

    freqs = [850, 900, 1800, 2100, 2300, 2600]
    idx, steps = cari_biner_frekuensi(freqs, 2100)
    print(f"2. Hasil Binary Search 2100 kHz: Indeks {idx} ({steps} langkah)")

    daya = [-85.0, -110.0, -72.5, -95.0, -60.0]
    print("\n3. Pengurutan Daya (Ascending):")
    print("   Bubble   :", urut_bubble(daya))
    print("   Selection:", urut_selection(daya))
    print("   Insertion:", urut_insertion(daya))

    bts_data = [
        {"id": "BTS-Utara",   "latensi_ms": 4.2,  "rsrp_dbm": -65.0},
        {"id": "BTS-Pusat",   "latensi_ms": 8.5,  "rsrp_dbm": -72.0},
        {"id": "BTS-Selatan", "latensi_ms": 14.0, "rsrp_dbm": -88.0},
        {"id": "BTS-Barat",   "latensi_ms": 4.2,  "rsrp_dbm": -60.0},
    ]
    print("\n4. Hasil Pemeringkatan Performa (Multi-Kriteria):")
    ranked = peringkatkan_performa_bts(bts_data)
    for r, b in enumerate(ranked, start=1):
        print(f"   Rank #{r}: {b['id']} | Latensi: {b['latensi_ms']} ms | RSRP: {b['rsrp_dbm']} dBm")


if __name__ == "__main__":
    main()

