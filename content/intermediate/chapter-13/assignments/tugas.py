"""Starter Template: Flexible Telemetry Pipeline Engine
Tugas Praktik Chapter 13: Advanced Functions — Python Learning Hub
Pengembang: Aji Pamungkas Tri Nurcahyo — Institut Teknologi Sumatera

Instruksi:
Lengkapi bagian berlabel TODO sesuai petunjuk pada berkas tugas.md.
Jalankan berkas ini untuk memverifikasi alur kerja pipeline fungsional Anda.
"""

from typing import Any, Callable


# ==============================================================================
# BAGIAN 1: CLOSURE FACTORY UNTUK AMBANG BATAS
# ==============================================================================

def buat_filter_rentang(
    min_val: float | None = None,
    max_val: float | None = None
) -> Callable[[float], bool]:
    """Closure: Menghasilkan fungsi predikat penyaring ambang batas nilai numerik."""
    # TODO: Implementasikan closure penyaring rentang [min_val, max_val]
    def predikat(nilai: float) -> bool:
        if min_val is not None and nilai < min_val:
            return False
        if max_val is not None and nilai > max_val:
            return False
        return True

    return predikat


# ==============================================================================
# BAGIAN 2: HIGHER-ORDER FUNCTION UNTUK EKSEKUSI PIPELINE
# ==============================================================================

def jalankan_pipeline(
    data: list[float],
    *transforms: Callable[[float], float],
    filter_kustom: Callable[[float], bool] | None = None
) -> list[float]:
    """Higher-Order Function: Menerapkan pemfilteran dan rantai transformasi nilai."""
    # TODO: Lakukan pemfilteran data dan eksekusi seluruh transforms berantai
    hasil: list[float] = []
    for item in data:
        if filter_kustom is not None and not filter_kustom(item):
            continue
        nilai = item
        for fn in transforms:
            nilai = fn(nilai)
        hasil.append(round(nilai, 4))
    return hasil


# ==============================================================================
# BAGIAN 3: AGREGATOR STATISTIK DENGAN *ARGS & **KWARGS
# ==============================================================================

def analisis_telemetri(
    data: list[float],
    /,
    unit: str = "mW",
    **kalkulator_kustom: Callable[[list[float]], float]
) -> dict[str, Any]:
    """Agregator telemetri dengan positional-only parameter dan **kwargs dinamis."""
    # TODO: Hitung ringkasan statistik bawaan (total, min, max, avg) dan kalkulator_kustom
    if not data:
        return {"total_sampel": 0, "status": "KOSONG"}

    laporan: dict[str, Any] = {
        "total_sampel": len(data),
        "unit": unit,
        "rata_rata": round(sum(data) / len(data), 2),
        "nilai_minimum": min(data),
        "nilai_maksimum": max(data),
    }

    for nama_metrik, fungsi_kalkulasi in kalkulator_kustom.items():
        try:
            laporan[nama_metrik] = round(float(fungsi_kalkulasi(data)), 2)
        except Exception as e:
            laporan[nama_metrik] = f"Error: {e}"

    return laporan


def main() -> None:
    sampel_data = [15.2, 48.0, 102.5, 7.8, 64.0, 95.2, 33.1]
    print(f"Dataset Mentah: {sampel_data}")

    # 1. Filter data dalam rentang normal 10.0 s.d. 100.0
    filter_normal = buat_filter_rentang(10.0, 100.0)

    # 2. Transformasi: Kalibrasi offset (+2.0) lalu penguatan Gain (*1.2)
    tambah_offset = lambda x: x + 2.0
    kalibrasi_gain = lambda x: x * 1.2

    hasil_pipeline = jalankan_pipeline(
        sampel_data,
        tambah_offset,
        kalibrasi_gain,
        filter_kustom=filter_normal
    )
    print(f"Hasil Pipeline: {hasil_pipeline}")

    # 3. Analisis statistik dengan metrik tambahan via **kwargs
    ringkasan = analisis_telemetri(
        hasil_pipeline,
        unit="mW",
        rentang_dinamis=lambda d: max(d) - min(d)
    )
    print(f"Ringkasan Analisis: {ringkasan}")


if __name__ == "__main__":
    main()

