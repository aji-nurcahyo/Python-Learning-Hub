"""Starter Template: Algorithm Performance Comparator
Tugas Praktik Chapter 16: Algorithm Analysis & Problem Solving — Python Learning Hub
Pengembang: Aji Pamungkas Tri Nurcahyo — Institut Teknologi Sumatera

Instruksi:
Lengkapi bagian berlabel TODO dengan kalkulasi analitis dan pengukuran waktu empiris yang presisi.
Gunakan time.perf_counter() untuk mencatat durasi waktu eksekusi.
"""

import math
import time
from typing import Any, Callable


# ==============================================================================
# BAGIAN 1: ESTIMASI KOMPLEKSITAS TEORITIS BIG-O
# ==============================================================================

def estimasi_kompleksitas_teoritis(n: int) -> dict[str, int]:
    """Menghitung jumlah operasi teoritis untuk N data."""
    # TODO: Hitung operasi O(1), O(log n), O(n), O(n log n), O(n^2)
    return {
        "O(1)": 1,
        "O(log_n)": math.ceil(math.log2(n)) if n > 0 else 0,
        "O(n)": n,
        "O(n_log_n)": int(n * math.log2(n)) if n > 1 else 0,
        "O(n2)": n ** 2,
    }


# ==============================================================================
# BAGIAN 2: PENGUKURAN EMPIRIS RATARATA (BENCHMARKER)
# ==============================================================================

def ukur_latensi_rata_rata(
    fungsi: Callable[..., Any],
    *args: Any,
    repetisi: int = 5
) -> float:
    """Mengukur rata-rata durasi waktu eksekusi fungsi dalam milidetik (ms)."""
    # TODO: Gunakan loop repetisi dan time.perf_counter()
    if repetisi <= 0:
        repetisi = 1
    total_detik = 0.0
    for _ in range(repetisi):
        t0 = time.perf_counter()
        fungsi(*args)
        t1 = time.perf_counter()
        total_detik += (t1 - t0)
    return round((total_detik / repetisi) * 1000, 4)


# ==============================================================================
# BAGIAN 3: SPACE-TIME TRADEOFF (DUPLICATE DETECTION)
# ==============================================================================

def deteksi_duplikat_brute_force(arr: list[Any]) -> bool:
    """O(n^2) waktu, O(1) ruang memori."""
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return True
    return False


def deteksi_duplikat_hash_set(arr: list[Any]) -> bool:
    """O(n) waktu, O(n) ruang memori (Space-Time Tradeoff)."""
    diketahui = set()
    for x in arr:
        if x in diketahui:
            return True
        diketahui.add(x)
    return False


def main() -> None:
    print("1. Analisis Teoritis Big-O untuk N = 50,000:")
    teori = estimasi_kompleksitas_teoritis(50_000)
    for k, v in teori.items():
        print(f"   {k:<10}: {v:,} operasi")

    print("\n2. Pengujian Empiris Space-Time Tradeoff (N = 1,500 Elemen):")
    sampel_data = list(range(1500)) + [42]
    durasi_brute = ukur_latensi_rata_rata(deteksi_duplikat_brute_force, sampel_data, repetisi=3)
    durasi_hash = ukur_latensi_rata_rata(deteksi_duplikat_hash_set, sampel_data, repetisi=3)
    print(f"   Brute Force O(n^2): {durasi_brute:.4f} ms")
    print(f"   Hash Set O(n)     : {durasi_hash:.4f} ms")
    ratio = durasi_brute / durasi_hash if durasi_hash > 0 else 1.0
    print(f"   -> Hash Set {ratio:.1f}x lebih cepat!")

    print("\n3. Verifikasi Kasus Batas (Edge Cases):")
    kosong = []
    print("   Input list kosong:", deteksi_duplikat_hash_set(kosong))


if __name__ == "__main__":
    main()
