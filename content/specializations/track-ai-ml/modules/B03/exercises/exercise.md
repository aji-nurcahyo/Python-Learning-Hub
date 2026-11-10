# Latihan Mandiri B03 — Clustering & PCA

## Latihan 1: K-Means & Evaluasi Silhouette
1. Muat `datasets/user_usage_profiles.csv`.
2. Lakukan scaling seluruh fitur numerik dengan `StandardScaler()`.
3. Uji nilai $K \in \{2, 3, 4, 5\}$ menggunakan `KMeans(n_clusters=k, n_init=10, random_state=42)` dan catat inertia beserta Silhouette Score.

## Latihan 2: DBSCAN Anomaly & PCA 2D
1. Jalankan `DBSCAN(eps=0.9, min_samples=3)` pada `X_scaled` dan tampilkan `user_id` berlabel `-1`.
2. Terapkan `PCA(n_components=2)` untuk memampatkan 4 fitur menjadi 2 komponen utama serta hitung persentase varians informasi tersimpan.

