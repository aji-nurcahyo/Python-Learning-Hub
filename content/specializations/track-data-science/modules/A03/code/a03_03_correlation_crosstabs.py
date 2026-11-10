from pathlib import Path
import pandas as pd

csv_path = Path(__file__).resolve().parent.parent / "datasets" / "telecom_qos_kpi.csv"
df = pd.read_csv(csv_path)

num_cols = ["traffic_gbps", "latency_ms", "packet_loss_pct", "active_users"]
pearson_corr = df[num_cols].corr(method="pearson").round(3)
spearman_corr = df[num_cols].corr(method="spearman").round(3)

print("Matriks Korelasi Pearson:")
print(pearson_corr.to_string())
print("\nMatriks Korelasi Spearman:")
print(spearman_corr.to_string())

ct = pd.crosstab(df["region"], df["sla_status"], margins=True)
print("\nCrosstab Region vs SLA Status:")
print(ct.to_string())

