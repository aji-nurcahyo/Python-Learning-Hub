# Tugas Terstruktur B03: Segmentasi & Deteksi Anomali Tanpa Label

## Instruksi Implementasi (`tugas.py`)
1. `evaluate_kmeans_range(df: pd.DataFrame, feature_cols: list[str], k_values: list[int]) -> pd.DataFrame`: skalakan fitur dan evaluasi inertia serta Silhouette Score untuk setiap $K$.
2. `detect_density_anomalies(df: pd.DataFrame, feature_cols: list[str], eps: float = 0.9, min_samples: int = 3) -> list[str]`: jalankan DBSCAN di atas fitur terskala dan kembalikan daftar `user_id` berlabel `-1`.
3. `project_pca(df: pd.DataFrame, feature_cols: list[str], n_components: int = 2) -> tuple[np.ndarray, float]`: kembalikan koordinat hasil proyeksi PCA beserta total `explained_variance_ratio_`.

## Rubrik Penilaian (Total 100 Poin)
- Kebenaran Scaling & Pipeline Jarak (25%)
- Evaluasi Kualitas K-Means (Silhouette) (25%)
- Deteksi Noise DBSCAN & Reduksi PCA (30%)
- Unit Testing & Kebersihan Kode (20%)

