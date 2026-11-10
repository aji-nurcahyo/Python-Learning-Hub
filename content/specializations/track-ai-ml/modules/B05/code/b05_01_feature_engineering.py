from pathlib import Path
import pandas as pd

FEATURE_COLS = [
    "uptime_days",
    "temp_c",
    "latency_ms",
    "packet_loss_pct",
    "load_per_mhz",
    "loss_latency_index",
]


def engineer_domain_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    safe_bw = out["bandwidth_mhz"].clip(lower=1.0)
    out["load_per_mhz"] = (out["active_users"] / safe_bw).round(4)
    out["loss_latency_index"] = (out["packet_loss_pct"] * out["latency_ms"]).round(4)
    return out


if __name__ == "__main__":
    csv_path = Path(__file__).resolve().parent.parent / "datasets" / "telecom_maintenance_train.csv"
    df = pd.read_csv(csv_path)
    engineered = engineer_domain_features(df)
    print("Kolom fitur siap pakai:", FEATURE_COLS)
    print("Ringkasan fitur baru per failure_risk:")
    print(
        engineered.groupby("failure_risk")[["load_per_mhz", "loss_latency_index"]]
        .median()
        .round(3)
        .to_string()
    )

