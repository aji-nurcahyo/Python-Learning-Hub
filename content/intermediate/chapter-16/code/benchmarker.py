"""Modul Pembanding Kinerja Algoritma (benchmarker.py)
Chapter 16: Algorithm Analysis & Problem Solving — Python Learning Hub

Menyediakan perkakas komparasi empiris waktu komputasi (time.perf_counter),
evaluasi kompleksitas teoritis, analisis space-time tradeoff, serta verifikasi kebenaran.
"""

import time
from typing import Any, Callable


def benchmark_function(
    func: Callable[..., Any],
    *args: Any,
    repetitions: int = 5
) -> dict[str, Any]:
    """Mengukur durasi eksekusi empiris rata-rata dalam milidetik (ms)."""
    if repetitions <= 0:
        repetitions = 1
    total_time = 0.0
    result = None

    for _ in range(repetitions):
        t0 = time.perf_counter()
        result = func(*args)
        t1 = time.perf_counter()
        total_time += (t1 - t0)

    avg_ms = round((total_time / repetitions) * 1000, 4)
    return {
        "function_name": func.__name__,
        "average_duration_ms": avg_ms,
        "repetitions": repetitions,
        "sample_output": result,
    }


def compare_duplicate_detectors(data: list[Any]) -> dict[str, Any]:
    """Membandingkan pendekatan deteksi duplikat:
    1. Brute-force O(n²) waktu, O(1) ruang.
    2. Hash-set O(n) waktu, O(n) ruang.
    """
    def detector_brute_force(arr: list[Any]) -> bool:
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] == arr[j]:
                    return True
        return False

    def detector_hash_set(arr: list[Any]) -> bool:
        seen = set()
        for x in arr:
            if x in seen:
                return True
            seen.add(x)
        return False

    res_brute = benchmark_function(detector_brute_force, data, repetitions=3)
    res_hash = benchmark_function(detector_hash_set, data, repetitions=3)

    return {
        "dataset_size": len(data),
        "brute_force_ms": res_brute["average_duration_ms"],
        "hash_set_ms": res_hash["average_duration_ms"],
        "has_duplicates": res_hash["sample_output"],
    }


def analyze_theoretical_growth(n: int) -> dict[str, Any]:
    """Menghitung estimasi operasi teoritis Big-O untuk ukuran dataset n."""
    import math
    return {
        "N": n,
        "O(1)": 1,
        "O(log_n)": math.ceil(math.log2(n)) if n > 0 else 0,
        "O(n)": n,
        "O(n_log_n)": int(n * math.log2(n)) if n > 1 else 0,
        "O(n2)": n ** 2,
    }

