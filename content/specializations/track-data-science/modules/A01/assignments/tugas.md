# Tugas Terstruktur A01: Pipeline Kalibrasi & Evaluasi Node Sensor

## Latar Belakang
Tim operasional infrastruktur membutuhkan modul kalibrasi numerik cepat untuk memproses matriks pengukuran dari 12 node sensor secara serentak tanpa bergantung pada loop Python yang lambat.

## Spesifikasi Teknis
Kerjakan starter code pada berkas `tugas.py` dan penuhi seluruh fungsi berikut:
1. `load_sensor_data(csv_path: str | Path) -> np.ndarray`: membaca dataset CSV menjadi array 2D `float64`.
2. `remove_bias(metrics: np.ndarray, bias_vector: np.ndarray) -> np.ndarray`: mengurangi setiap kolom dengan nilai bias memakai broadcasting.
3. `minmax_scale(metrics: np.ndarray) -> np.ndarray`: menormalkan setiap kolom ke rentang `[0.0, 1.0]` sambil menjaga kolom konstan tetap `0.0`.
4. `rank_nodes_by_stability(node_ids: np.ndarray, scaled_metrics: np.ndarray) -> list[tuple[int, float]]`: menghitung jarak Euclidean tiap baris terhadap vektor `[0.0, 0.0, 0.0, 0.0]` lalu mengurutkan dari jarak terkecil (paling stabil).

## Kriteria Penilaian (Total 100 Poin)
- Kebenaran Pembuatan & Inspeksi `ndarray` (25%)
- Penerapan Vectorization & Broadcasting (30%)
- Proteksi Kasus Batas & Testing (25%)
- Kualitas Kode & Dokumentasi (20%)

