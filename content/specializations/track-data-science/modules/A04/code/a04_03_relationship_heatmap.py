import tempfile
from pathlib import Path
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

csv_path = Path(__file__).resolve().parent.parent / "datasets" / "telecom_qos_kpi.csv"
df = pd.read_csv(csv_path)
num_cols = ["traffic_gbps", "latency_ms", "packet_loss_pct", "active_users"]
corr = df[num_cols].corr(method="spearman")

fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.5), dpi=150)
sns.scatterplot(
    data=df,
    x="traffic_gbps",
    y="latency_ms",
    hue="technology",
    style="sla_status",
    s=90,
    ax=axes[0],
)
axes[0].set_title("Beban Trafik vs Latensi per Teknologi")
axes[0].set_xlabel("Trafik (Gbps)")
axes[0].set_ylabel("Latensi (ms)")

mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap="coolwarm", center=0, ax=axes[1])
axes[1].set_title("Heatmap Korelasi Spearman QoS")

out_file = Path(tempfile.gettempdir()) / "a04_rel_heatmap.png"
fig.tight_layout()
fig.savefig(out_file, dpi=150)
plt.close(fig)

print("Pasangan korelasi Spearman latency vs packet_loss:", round(float(corr.loc["latency_ms", "packet_loss_pct"]), 3))
print("Render PNG sukses:", out_file.exists() and out_file.stat().st_size > 1000)

