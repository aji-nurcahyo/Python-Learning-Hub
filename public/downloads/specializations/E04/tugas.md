# Tugas Terstruktur E04: Drive-Test RF Quality Auditor & Blindspot Locator

## Instruksi Implementasi (`tugas.py`)
1. `classify_rsrp(rsrp_dbm: float) -> str`: kategorikan menjadi `'Excellent'` (`>= -80`), `'Good'` (`>= -90`), `'Mid-Cell'` (`>= -105`), dan `'Cell-Edge'` (`< -105`).
2. `diagnose_rf_issue(rsrp_dbm: float, sinr_db: float) -> str`: kembalikan `'CRITICAL_EDGE'`, `'COVERAGE_BLINDSPOT'`, `'HIGH_INTERFERENCE'`, atau `'HEALTHY'`.
3. `compute_fspl_db(distance_km: float, freq_mhz: float) -> float`: validasi angka positif lalu hitung `32.44 + 20*log10(d) + 20*log10(f)`.
4. Buat fungsi rekap `summarize_cells(df: pd.DataFrame) -> pd.DataFrame` per `cell_id` dan uji memakai `pytest`.

## Rubrik Penilaian (Total 100 Poin)
- Akurasi Klasifikasi RSRP, RSRQ & Diagnosa SINR (35%)
- Kebenaran Formula FSPL Link Budget (25%)
- Agregasi Statistik per Cell ID & Peta Coverage (20%)
- Unit Testing RF Analytics (Pytest) (20%)

