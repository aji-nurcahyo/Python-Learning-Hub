"""Demonstrasi Deterministik: Flexible Data Processor
Chapter 13: Advanced Functions — Python Learning Hub
Pengembang: Aji Pamungkas Tri Nurcahyo — Institut Teknologi Sumatera
"""

from data_processor import apply_pipeline, make_scaler, make_threshold_filter, summarize_dataset

def main() -> None:
    print("==========================================================")
    print("DEMONSTRASI CHAPTER 13: ADVANCED FUNCTIONS")
    print("Python Learning Hub - Level 2: Intermediate")
    print("==========================================================")

    dataset = [10.0, 20.0, 30.0, 40.0, 50.0]
    print(f"\n1. Dataset Awal: {dataset}")

    # Uji 1: Pipeline Transformasi Berantai (Higher-Order Function)
    kali_dua = make_scaler(2.0)
    tambah_lima = make_scaler(1.0, 5.0)
    hasil_transform = apply_pipeline(dataset, kali_dua, tambah_lima)
    print(f"2. Hasil Transformasi (*2 lalu +5): {hasil_transform}")

    # Uji 2: Pipeline Pemfilteran Predikat (Closure)
    filter_rentang = make_threshold_filter(min_val=30.0, max_val=80.0)
    hasil_filter = apply_pipeline(hasil_transform, filter_func=filter_rentang)
    print(f"3. Hasil Filter Ambang [30, 80]: {hasil_filter}")

    # Uji 3: Ringkasan Dataset dengan *args dan **kwargs
    ringkasan = summarize_dataset(
        hasil_filter,
        "count", "avg", "min", "max", "sum",
        prefix="Metrik",
        rentang=lambda d: max(d) - min(d) if d else 0.0,
        median=lambda d: sorted(d)[len(d)//2] if d else 0.0
    )
    print("\n4. Ringkasan Statistik (*args standar & **kwargs kustom):")
    for k, v in ringkasan.items():
        print(f"   {k:<18}: {v}")

    print("\nSemua demonstrasi Advanced Functions berhasil dieksekusi.")


if __name__ == "__main__":
    main()

