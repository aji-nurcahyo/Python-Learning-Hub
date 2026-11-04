"""Modul Pemroses Data Fleksibel (data_processor.py)
Chapter 13: Advanced Functions — Python Learning Hub

Menyediakan fungsi tingkat tinggi untuk menyusun pipeline transformasi data,
menerapkan agregator bervariasi (*args, **kwargs), closure konfigurable,
serta pemfilteran predikat fungsional.
"""

from typing import Any, Callable


def make_scaler(factor: float, offset: float = 0.0) -> Callable[[float], float]:
    """Closure: Menghasilkan fungsi penskala nilai f(x) = x * factor + offset."""
    def scale(value: float) -> float:
        return round(value * factor + offset, 4)
    return scale


def make_threshold_filter(min_val: float | None = None, max_val: float | None = None) -> Callable[[float], bool]:
    """Closure: Menghasilkan fungsi predikat pemeriksa ambang batas nilai."""
    def is_within(value: float) -> bool:
        if min_val is not None and value < min_val:
            return False
        if max_val is not None and value > max_val:
            return False
        return True
    return is_within


def apply_pipeline(
    data: list[float],
    *transforms: Callable[[float], float],
    filter_func: Callable[[float], bool] | None = None
) -> list[float]:
    """Higher-Order Function: Menerapkan rangkaian transformasi dan filter pada koleksi data.

    Args:
        data: Koleksi data numerik awal.
        *transforms: Urutan fungsi transformasi (Callable) yang dieksekusi berantai.
        filter_func: Fungsi predikat penyaring opsional (keyword-only).

    Returns:
        list[float]: Koleksi data setelah transformasi dan pemfilteran.
    """
    results: list[float] = []
    for item in data:
        current = float(item)
        if filter_func is not None and not filter_func(current):
            continue
        for fn in transforms:
            current = fn(current)
        results.append(round(current, 4))
    return results


def summarize_dataset(
    data: list[float],
    *metrics: str,
    prefix: str = "Metrik",
    **custom_aggregators: Callable[[list[float]], float]
) -> dict[str, Any]:
    """Menghitung ringkasan statistik dataset menggunakan kombinasi metrik standar dan kustom.

    Args:
        data: Koleksi nilai numerik.
        *metrics: Nama-nama metrik bawaan ('sum', 'avg', 'min', 'max', 'count').
        prefix: Awalan label laporan.
        **custom_aggregators: Fungsi agregasi kustom eksternal berbasis keyword arguments.

    Returns:
        dict: Kamus hasil perhitungan metrik statistik.
    """
    summary: dict[str, Any] = {"total_samples": len(data)}
    if not data:
        return summary

    standard_ops = {
        "count": lambda d: len(d),
        "sum": lambda d: round(sum(d), 4),
        "avg": lambda d: round(sum(d) / len(d), 4),
        "min": lambda d: min(d),
        "max": lambda d: max(d),
    }

    selected_metrics = metrics if metrics else ("count", "avg", "min", "max")
    for m in selected_metrics:
        key_lower = m.lower()
        if key_lower in standard_ops:
            summary[f"{prefix}_{key_lower}"] = standard_ops[key_lower](data)

    for name, agg_func in custom_aggregators.items():
        try:
            summary[f"{prefix}_{name}"] = round(float(agg_func(data)), 4)
        except Exception as err:
            summary[f"{prefix}_{name}"] = f"ERR: {err}"

    return summary
