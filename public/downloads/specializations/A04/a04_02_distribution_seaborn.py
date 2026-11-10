import tempfile
from pathlib import Path
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

csv_path = Path(__file__).resolve().parent.parent / "datasets" / "telecom_qos_kpi.csv"
df = pd.read_csv(csv_path)

sns.set_theme(style="whitegrid", palette="colorblind")
fig, axes = plt.subplots(1, 2, figsize=(11, 4.5), dpi=150)

sns.histplot(data=df, x="latency_ms", bins=8, kde=True, ax=axes[0], color="#0284c7")
median_val = float(df["latency_ms"].median())
axes[0].axvline(median_val, color="#dc2626", linestyle="--", label=f"Median: {median_val:.1f} ms")
axes[0].set_title("Distribusi Latensi Seluruh Menara")
axes[0].set_xlabel("Latensi (ms)")
axes[0].legend()

sns.boxplot(data=df, x="technology", y="latency_ms", ax=axes[1])
axes[1].set_title("Sebaran Latensi: 4G vs 5G")
axes[1].set_xlabel("Teknologi Radio")
axes[1].set_ylabel("Latensi (ms)")

out_file = Path(tempfile.gettempdir()) / "a04_dist_seaborn.png"
fig.tight_layout()
fig.savefig(out_file, dpi=150)
plt.close(fig)

print("Subplot panels dibuat  :", len(axes))
print("Median latensi referensi:", round(median_val, 2), "ms")
print("Statistik per teknologi :", df.groupby("technology")["latency_ms"].median().round(2).to_dict())
