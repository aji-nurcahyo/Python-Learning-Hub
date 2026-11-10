# Modul B03: Unsupervised Learning & Dimensionality Reduction

## 1. Belajar dari Data Tanpa Label (*Unsupervised Learning*)
Dalam segmentasi perilaku pengguna, deteksi pola trafik baru, atau kompresi fitur, kita sering belum memiliki kolom target (`y`). **Unsupervised Learning** menemukan struktur alami langsung dari distribusi ruang fitur `X`.

---

## 2. K-Means Clustering & Evaluasi Silhouette Score
**K-Means** mempartisi data menjadi $K$ kelompok (*clusters*) dengan meminimalkan jarak kuadrat tiap observasi ke pusat kelompoknya (*centroid*):
- **Prasyarat Wajib:** Lakukan `StandardScaler()` terlebih dahulu agar fitur berangka ratusan (`active_minutes`) tidak mengalahkan fitur desimal (`video_ratio`).
- **Metode Elbow:** Amati penurunan *inertia* (jumlah kuadrat jarak dalam cluster) saat $K$ bertambah.
- **Silhouette Score ($-1 \dots +1$):** Mengukur seberapa rapat titik di dalam clusternya sendiri dibandingkan jarak ke cluster tetangga terdekat. Makin dekat ke `+1.0`, separasi cluster makin baik.

---

## 3. Deteksi Anomali Berbasis Kepadatan dengan DBSCAN
Tidak seperti K-Means yang memaksa setiap titik masuk ke salah satu centroid, **DBSCAN** (*Density-Based Spatial Clustering of Applications with Noise*) mencari area padat titik bertetangga (`eps`, `min_samples`). Titik terpencil yang jauh dari kerumunan otomatis diberi label **`-1` (Noise / Anomali)** — sangat efektif mengisolasi pengguna ekstrem seperti `U16` atau `U17`.

---

## 4. Reduksi Dimensi dengan Principal Component Analysis (PCA)
**PCA** memproyeksikan $d$ fitur asli yang saling berkorelasi ke $k < d$ komponen ortogonal baru (*Principal Components*) yang menangkap varians informasi maksimal. Atribut `.explained_variance_ratio_` menunjukkan persentase informasi asli yang berhasil dipertahankan pada setiap komponen.

