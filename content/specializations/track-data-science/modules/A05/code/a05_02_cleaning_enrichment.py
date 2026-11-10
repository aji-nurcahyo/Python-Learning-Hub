from pathlib import Path
import numpy as np
import pandas as pd


def clean_and_enrich(logs_df: pd.DataFrame, meta_df: pd.DataFrame) -> pd.DataFrame:
    df = logs_df.drop_duplicates(subset=["log_id"], keep="first").copy()
    df["recorded_at"] = pd.to_datetime(df["recorded_at"], format="%Y-%m-%d")

    # Koreksi nilai latensi tidak fisik (negatif) menjadi NaN sebelum imputasi
    df.loc[df["latency_ms"] < 0, "latency_ms"] = np.nan

    enriched = pd.merge(df, meta_df, on="tower_id", how="left")
    enriched["throughput_mbps"] = enriched["throughput_mbps"].fillna(
        enriched.groupby("technology")["throughput_mbps"].transform("median")
    )
    enriched["latency_ms"] = enriched["latency_ms"].fillna(
        enriched.groupby("tower_id")["latency_ms"].transform("median")
    )
    enriched["latency_ms"] = enriched["latency_ms"].fillna(enriched["latency_ms"].median())
    enriched["sla_breach"] = enriched["latency_ms"] > enriched["sla_latency_ms"]
    return enriched


if __name__ == "__main__":
    ds_dir = Path(__file__).resolve().parent.parent / "datasets"
    raw_logs = pd.read_csv(ds_dir / "network_operations_logs.csv")
    meta = pd.read_csv(ds_dir / "tower_metadata.csv")
    result = clean_and_enrich(raw_logs, meta)
    print("Baris bersih hasil enrichment:", len(result))
    print("Total missing values tersisa :", int(result.isna().sum().sum()))
    print("Jumlah pelanggaran SLA       :", int(result["sla_breach"].sum()))

