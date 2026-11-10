from pathlib import Path
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

csv_path = Path(__file__).resolve().parent.parent / "datasets" / "user_usage_profiles.csv"
df = pd.read_csv(csv_path)
features = ["daily_gb", "video_ratio", "avg_latency_ms", "active_minutes"]

X_scaled = StandardScaler().fit_transform(df[features])
dbscan = DBSCAN(eps=0.9, min_samples=3)
df["dbscan_label"] = dbscan.fit_predict(X_scaled)

anomalies = df.loc[df["dbscan_label"] == -1, ["user_id", "daily_gb", "avg_latency_ms", "active_minutes"]]
print("Distribusi Label DBSCAN:", df["dbscan_label"].value_counts().sort_index().to_dict())
print("\nPengguna Terdeteksi Anomali (label == -1):")
print(anomalies.to_string(index=False))

