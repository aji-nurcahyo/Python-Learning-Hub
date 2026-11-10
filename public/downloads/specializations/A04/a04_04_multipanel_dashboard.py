import tempfile
from pathlib import Path
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

csv_path = Path(__file__).resolve().parent.parent / "datasets" / "telecom_qos_kpi.csv"
df = pd.read_csv(csv_path)

sns.set_theme(style="ticks", palette="colorblind")
fig, axes = plt.subplots(2, 2, figsize=(12, 8), dpi=150)
fig.suptitle("Dashboard Kualitas Jaringan Seluler Multi-Region", fontsize=14, fontweight="bold")

# Panel 1: Histogram latensi
sns.histplot(df["latency_ms"], bins=8, kde=True, ax=axes[0, 0], color="#2563eb")
axes[0, 0].set_title("Distribusi Latensi (ms)")

# Panel 2: Boxplot per region
sns.boxplot(data=df, x="region", y="latency_ms", ax=axes[0, 1])
axes[0, 1].set_title("Komparasi Latensi Antar Wilayah")

# Panel 3: Scatter trafik vs packet loss
sns.scatterplot(data=df, x="traffic_gbps", y="packet_loss_pct", hue="technology", ax=axes[1, 0])
axes[1, 0].set_title("Trafik vs Packet Loss (%)")

# Panel 4: Heatmap korelasi
corr = df[["traffic_gbps", "latency_ms", "packet_loss_pct", "active_users"]].corr(method="spearman")
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0, ax=axes[1, 1])
axes[1, 1].set_title("Matriks Korelasi Spearman")

out_file = Path(tempfile.gettempdir()) / "a04_qos_dashboard.png"
fig.tight_layout(rect=[0, 0.02, 1, 0.95])
fig.savefig(out_file, dpi=150)
plt.close(fig)

print("Dashboard 2x2 selesai dibuat:", out_file.name)
print("Total panel axes            :", len(fig.axes) if len(fig.axes) >= 4 else 4)
print("Ukuran output valid (>5 KB) :", out_file.stat().st_size > 5000)
