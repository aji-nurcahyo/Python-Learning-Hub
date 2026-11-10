# Tugas Capstone A05: End-to-End Network Analytics Report Engine

## Instruksi Implementasi (`tugas.py`)
1. `validate_and_load(logs_path: Path, meta_path: Path) -> tuple[pd.DataFrame, pd.DataFrame]`: muat dua CSV dan validasi keberadaan semua kolom wajib.
2. `clean_and_enrich(logs_df: pd.DataFrame, meta_df: pd.DataFrame) -> pd.DataFrame`: hapus duplikat `log_id`, tandai latensi negatif sebagai `NaN`, gabungkan metadata menara via `left join`, dan isi missing values dengan median per kategori/teknologi.
3. `compute_regional_kpis(enriched: pd.DataFrame) -> pd.DataFrame`: hitung `total_logs`, `breaches`, `median_latency_ms`, `p95_latency_ms`, dan `sla_compliance_pct` per wilayah.
4. `generate_analytics_bundle(logs_path: Path, meta_path: Path, out_dir: Path) -> dict[str, Path]`: ekspor grafik `capstone_dashboard.png`, `kpi_summary.json`, dan `analytics_report.md` lengkap.

## Rubrik Penilaian (Total 100 Poin)
- Validasi Skema & Ketahanan Ingestion (20%)
- Data Cleaning, Enrichment & Rekayasa KPI (35%)
- Kualitas Artefak Laporan & Visualisasi (25%)
- Modularitas Kode & Cakupan Unit Test (20%)

