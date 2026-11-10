import tempfile
from pathlib import Path
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

csv_path = Path(__file__).resolve().parent.parent / "datasets" / "drive_test_lte_measurements.csv"
df = pd.read_csv(csv_path)

cell_summary = (
    df.groupby("cell_id", as_index=False)
    .agg(
        samples=("point_id", "count"),
        median_rsrp=("rsrp_dbm", "median"),
        median_sinr=("sinr_db", "median"),
        total_handovers=("handover_count", "sum"),
    )
    .sort_values("median_sinr")
)

fig, ax = plt.subplots(figsize=(7.2, 4.8), dpi=150)
sc = ax.scatter(df["lon"], df["lat"], c=df["rsrp_dbm"], cmap="RdYlGn", vmin=-115, vmax=-75, s=110, edgecolors="black")
cbar = fig.colorbar(sc, ax=ax)
cbar.set_label("RSRP (dBm)")
ax.set_title("Peta Sebar Drive-Test RSRP sepanjang Rute Pengukuran")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.grid(True, linestyle="--", alpha=0.3)

with tempfile.TemporaryDirectory() as td:
    out_png = Path(td) / "e04_coverage_map.png"
    fig.tight_layout()
    fig.savefig(out_png, dpi=150)
    plt.close(fig)
    print("Rekap Per Cell ID:")
    print(cell_summary.round(2).to_string(index=False))
    print("\nPeta cakupan RSRP tervalidasi:", out_png.exists() and out_png.stat().st_size > 2000)

