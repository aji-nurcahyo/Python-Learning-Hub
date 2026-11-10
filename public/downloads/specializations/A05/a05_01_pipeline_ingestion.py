from pathlib import Path
import pandas as pd

REQUIRED_LOG_COLS = {"log_id", "tower_id", "recorded_at", "throughput_mbps", "latency_ms", "packet_loss_pct"}
REQUIRED_META_COLS = {"tower_id", "region", "city", "technology", "sla_latency_ms"}


def load_and_validate(logs_path: Path, meta_path: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    logs_df = pd.read_csv(logs_path)
    meta_df = pd.read_csv(meta_path)

    missing_log = REQUIRED_LOG_COLS - set(logs_df.columns)
    missing_meta = REQUIRED_META_COLS - set(meta_df.columns)
    if missing_log:
        raise ValueError(f"Kolom wajib log hilang: {sorted(missing_log)}")
    if missing_meta:
        raise ValueError(f"Kolom wajib metadata hilang: {sorted(missing_meta)}")

    return logs_df, meta_df


if __name__ == "__main__":
    ds_dir = Path(__file__).resolve().parent.parent / "datasets"
    logs, meta = load_and_validate(ds_dir / "network_operations_logs.csv", ds_dir / "tower_metadata.csv")
    print("Validasi skema lolos.")
    print("Jumlah log mentah    :", len(logs))
    print("Jumlah menara master :", len(meta))

