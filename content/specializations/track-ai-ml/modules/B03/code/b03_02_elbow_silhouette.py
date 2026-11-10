from pathlib import Path
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

csv_path = Path(__file__).resolve().parent.parent / "datasets" / "user_usage_profiles.csv"
df = pd.read_csv(csv_path)
features = ["daily_gb", "video_ratio", "avg_latency_ms", "active_minutes"]

X_scaled = StandardScaler().fit_transform(df[features])

print("Evaluasi Jumlah Cluster K-Means:")
best_k = None
best_score = -1.0
for k in range(2, 6):
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    labels = km.fit_predict(X_scaled)
    sil = float(silhouette_score(X_scaled, labels))
    print(f"K={k} | Inertia={km.inertia_:6.2f} | Silhouette={sil:.4f}")
    if sil > best_score:
        best_score = sil
        best_k = k

print(f"\nRekomendasi K optimal (berdasarkan Silhouette tertinggi): K={best_k} (score={best_score:.4f})")

