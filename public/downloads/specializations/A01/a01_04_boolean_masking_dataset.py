from pathlib import Path
import numpy as np

csv_path = Path(__file__).resolve().parent.parent / "datasets" / "sensor_matrix.csv"
raw = np.genfromtxt(csv_path, delimiter=",", skip_header=1, dtype=np.float64)

node_ids = raw[:, 0].astype(np.int64)
metrics = raw[:, 1:]  # [temperature_c, humidity_pct, latency_ms, packet_loss_pct]

# Boolean masking: node dengan latensi > 25 ms atau packet loss > 0.5%
alert_mask = (metrics[:, 2] > 25.0) | (metrics[:, 3] > 0.5)
flagged_ids = node_ids[alert_mask]

# Pelabelan status node dengan np.where
status_labels = np.where(alert_mask, "PERLU_PERIKSA", "NORMAL")

print("Total observasi      :", len(node_ids))
print("Node berstatus alert :", flagged_ids.tolist())
print("Jumlah node NORMAL   :", int(np.sum(status_labels == "NORMAL")))
print("Rata-rata latensi (NORMAL) :", round(float(np.mean(metrics[~alert_mask, 2])), 2))
print("Rata-rata latensi (ALERT)  :", round(float(np.mean(metrics[alert_mask, 2])), 2))
