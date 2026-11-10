# Tugas Terstruktur A03: Diagnostik EDA Kualitas Jaringan

## Instruksi Implementasi (`tugas.py`)
1. `detect_iqr_outliers(series: pd.Series) -> tuple[pd.Series, dict[str, float]]`:
   - Hitung `q1`, `q3`, `iqr = q3 - q1`, `lower = q1 - 1.5 * iqr`, `upper = q3 + 1.5 * iqr`.
   - Kembalikan boolean `Series` mask dan dictionary batas statistik.
2. `summarize_skewness(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame`:
   - Mengembalikan DataFrame berisi kolom `column`, `mean`, `median`, `iqr`, `skew`.
3. `regional_crosstabs(df: pd.DataFrame) -> pd.DataFrame`:
   - Mengembalikan `pd.crosstab(df["region"], df["sla_status"], margins=True)`.

## Rubrik Penilaian (100 Poin)
- Akurasi Statistik Deskriptif & Skewness (25%)
- Logika Deteksi Outlier IQR & Z-Score (30%)
- Analisis Korelasi & Crosstab Segmen (25%)
- Testing & Kebersihan Kode (20%)

