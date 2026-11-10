# Latihan Mandiri A04 — Data Visualization

## Latihan 1: Figur Statistik 1x2
1. Gunakan `matplotlib.use("Agg")` bila menjalankan skrip di terminal tanpa layar GUI.
2. Buat dua subplot berdampingan (`fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))`).
3. Panel kiri: boxplot `latency_ms` berdasarkan `region`.
4. Panel kanan: heatmap korelasi Spearman memakai `sns.heatmap(..., annot=True, cmap="coolwarm", center=0)`.
5. Simpan grafik beresolusi `dpi=150` dan panggil `plt.close(fig)` sesudahnya.

