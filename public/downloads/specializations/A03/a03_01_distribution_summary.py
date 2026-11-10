from pathlib import Path
import pandas as pd

csv_path = Path(__file__).resolve().parent.parent / "datasets" / "telecom_qos_kpi.csv"
df = pd.read_csv(csv_path)

for col in ["traffic_gbps", "latency_ms", "packet_loss_pct"]:
    s = df[col]
    q1 = float(s.quantile(0.25))
    q3 = float(s.quantile(0.75))
    print(
        f"{col:16s} | mean={s.mean():6.2f} | median={s.median():6.2f} "
        f"| IQR={q3 - q1:5.2f} | skew={s.skew():5.2f}"
    )
