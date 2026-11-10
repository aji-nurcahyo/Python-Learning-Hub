from pathlib import Path
import pandas as pd

csv_path = Path(__file__).resolve().parent.parent / "datasets" / "telecom_qos_kpi.csv"
df = pd.read_csv(csv_path)

latency = df["latency_ms"]
q1 = float(latency.quantile(0.25))
q3 = float(latency.quantile(0.75))
iqr = q3 - q1
upper_fence = q3 + 1.5 * iqr

iqr_mask = latency > upper_fence
outlier_towers = df.loc[iqr_mask, ["tower_id", "region", "latency_ms", "sla_status"]]

# Z-score sebagai pembanding
z_scores = (latency - latency.mean()) / latency.std(ddof=0)
z_mask = z_scores.abs() > 2.0

print(f"Q1={q1:.2f} ms, Q3={q3:.2f} ms, IQR={iqr:.2f} ms, Upper Fence={upper_fence:.2f} ms")
print("Outlier IQR terdeteksi:")
print(outlier_towers.to_string(index=False))
print(f"\nOutlier |Z| > 2.0      : {df.loc[z_mask, 'tower_id'].tolist()}")
print(f"Mean sebelum filter    : {latency.mean():.2f} ms | Median: {latency.median():.2f} ms")
print(f"Mean sesudah filter IQR: {latency[~iqr_mask].mean():.2f} ms | Median: {latency[~iqr_mask].median():.2f} ms")

