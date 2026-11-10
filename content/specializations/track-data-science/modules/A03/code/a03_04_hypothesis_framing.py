from pathlib import Path
import pandas as pd

csv_path = Path(__file__).resolve().parent.parent / "datasets" / "telecom_qos_kpi.csv"
df = pd.read_csv(csv_path)

# Komparasi metrik per teknologi (4G vs 5G) untuk menguji hipotesis performa
tech_summary = (
    df.groupby("technology", as_index=False)
    .agg(
        total_towers=("tower_id", "count"),
        median_traffic=("traffic_gbps", "median"),
        median_latency=("latency_ms", "median"),
        max_loss=("packet_loss_pct", "max"),
    )
)
print("Perbandingan Performa 4G vs 5G:")
print(tech_summary.to_string(index=False))

# Identifikasi segmen berisiko tinggi (latency > 50 ms)
high_risk = df.loc[df["latency_ms"] > 50.0, ["tower_id", "technology", "region", "latency_ms"]]
print("\nSegmen Risiko Tinggi (latency > 50 ms):")
print(high_risk.to_string(index=False))

