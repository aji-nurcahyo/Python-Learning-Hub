# Tugas Terstruktur A04: Generator Figur Publikasi Multi-Panel

## Instruksi Implementasi (`tugas.py`)
1. `plot_latency_distribution(df: pd.DataFrame, out_path: Path) -> Path`: buat `sns.histplot(..., kde=True)` dengan garis vertikal penanda median serta simpan beresolusi 150 DPI.
2. `plot_correlation_heatmap(df: pd.DataFrame, cols: list[str], out_path: Path) -> Path`: gambar correlation heatmap dengan mask segitiga atas dan `annot=True, fmt=".2f"`.
3. `build_qos_dashboard(df: pd.DataFrame, out_path: Path) -> Path`: rancang figur 2x2 ber-`suptitle` yang menampung distribusi latensi, boxplot teknologi, scatter trafik vs latensi, dan heatmap korelasi.

## Rubrik Penilaian (100 Poin)
- Kejelasan Object-Oriented API & Layout (30%)
- Kesesuaian Jenis Chart & Estetika (25%)
- Ekspor & Manajemen Memori Figure (25%)
- Unit Testing & Dokumentasi (20%)
