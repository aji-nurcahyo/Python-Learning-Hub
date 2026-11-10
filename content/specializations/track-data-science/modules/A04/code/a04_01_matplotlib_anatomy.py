import tempfile
from pathlib import Path
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

csv_path = Path(__file__).resolve().parent.parent / "datasets" / "telecom_qos_kpi.csv"
df = pd.read_csv(csv_path)
region_avg = df.groupby("region", as_index=False)["latency_ms"].mean().sort_values("latency_ms")

fig, ax = plt.subplots(figsize=(7.5, 4.2), dpi=150)
bars = ax.barh(region_avg["region"], region_avg["latency_ms"], color="#2563eb", edgecolor="#1e3a8a")
ax.set_title("Rata-rata Latensi Jaringan per Wilayah", fontsize=12, fontweight="bold", pad=10)
ax.set_xlabel("Latensi Rata-rata (ms)")
ax.grid(axis="x", linestyle="--", alpha=0.35)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

for bar in bars:
    w = bar.get_width()
    ax.text(w + 0.8, bar.get_y() + bar.get_height() / 2, f"{w:.1f} ms", va="center", fontsize=9)

out_file = Path(tempfile.gettempdir()) / "a04_region_latency.png"
fig.tight_layout()
fig.savefig(out_file, dpi=150)
plt.close(fig)

print("Figur berhasil dirender :", out_file.name)
print("Wilayah terurut latensi :", region_avg["region"].tolist())
print("Ukuran file PNG (> 0 B):", out_file.exists() and out_file.stat().st_size > 1000)

