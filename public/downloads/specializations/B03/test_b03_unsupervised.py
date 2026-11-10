from pathlib import Path
import pandas as pd
from sklearn.cluster import DBSCAN, KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def test_kmeans_silhouette_above_half() -> None:
    csv_path = Path(__file__).resolve().parent.parent / "datasets" / "user_usage_profiles.csv"
    df = pd.read_csv(csv_path)
    features = ["daily_gb", "video_ratio", "avg_latency_ms", "active_minutes"]
    X_scaled = StandardScaler().fit_transform(df[features])
    labels = KMeans(n_clusters=3, n_init=10, random_state=42).fit_predict(X_scaled)
    assert silhouette_score(X_scaled, labels) > 0.50


def test_dbscan_flags_outliers_and_pca_retains_variance() -> None:
    csv_path = Path(__file__).resolve().parent.parent / "datasets" / "user_usage_profiles.csv"
    df = pd.read_csv(csv_path)
    features = ["daily_gb", "video_ratio", "avg_latency_ms", "active_minutes"]
    X_scaled = StandardScaler().fit_transform(df[features])
    db_labels = DBSCAN(eps=0.9, min_samples=3).fit_predict(X_scaled)
    assert -1 in set(db_labels)
    pca_pipe = Pipeline([("sc", StandardScaler()), ("pca", PCA(n_components=2))]).fit(df[features])
    assert sum(pca_pipe.named_steps["pca"].explained_variance_ratio_) > 0.85

