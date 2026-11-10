from pathlib import Path
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

csv_path = Path(__file__).resolve().parent.parent / "datasets" / "user_usage_profiles.csv"
df = pd.read_csv(csv_path)
features = ["daily_gb", "video_ratio", "avg_latency_ms", "active_minutes"]

pipe = Pipeline(
    [
        ("scaler", StandardScaler()),
        ("kmeans", KMeans(n_clusters=3, n_init=10, random_state=42)),
    ]
)
df["cluster"] = pipe.fit_predict(df[features])

summary = (
    df.groupby("cluster", as_index=False)
    .agg(users=("user_id", "count"), mean_gb=("daily_gb", "mean"), mean_minutes=("active_minutes", "mean"))
    .sort_values("mean_gb")
)
print("Profil 3 Cluster K-Means:")
print(summary.round(2).to_string(index=False))

