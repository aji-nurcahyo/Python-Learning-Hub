from pathlib import Path
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

csv_path = Path(__file__).resolve().parent.parent / "datasets" / "user_usage_profiles.csv"
df = pd.read_csv(csv_path)
features = ["daily_gb", "video_ratio", "avg_latency_ms", "active_minutes"]

pca_pipe = Pipeline(
    [
        ("scaler", StandardScaler()),
        ("pca", PCA(n_components=2, random_state=42)),
    ]
)
projected = pca_pipe.fit_transform(df[features])
pca_step: PCA = pca_pipe.named_steps["pca"]

print("Shape sebelum PCA :", df[features].shape)
print("Shape sesudah PCA :", projected.shape)
print("Explained variance ratio per komponen :", [round(float(v), 4) for v in pca_step.explained_variance_ratio_])
print("Total informasi dipertahankan (PC1+PC2):", round(float(sum(pca_step.explained_variance_ratio_)) * 100.0, 2), "%")

