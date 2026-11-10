from pathlib import Path
import numpy as np
import pandas as pd


def compute_regional_kpis(enriched: pd.DataFrame) -> pd.DataFrame:
    kpi = (
        enriched.groupby("region", as_index=False)
        .agg(
            total_logs=("log_id", "count"),
            breaches=("sla_breach", "sum"),
            median_latency_ms=("latency_ms", "median"),
            p95_latency_ms=("latency_ms", lambda s: float(np.percentile(s, 95))),
            avg_throughput_mbps=("throughput_mbps", "mean"),
        )
    )
    kpi["sla_compliance_pct"] = ((1.0 - (kpi["breaches"] / kpi["total_logs"])) * 100.0).round(2)
    return kpi.sort_values("sla_compliance_pct", ascending=True).reset_index(drop=True)


if __name__ == "__main__":
    ds_dir = Path(__file__).resolve().parent.parent / "datasets"
    logs = pd.read_csv(ds_dir / "network_operations_logs.csv").drop_duplicates(subset=["log_id"]).copy()
    meta = pd.read_csv(ds_dir / "tower_metadata.csv")
    logs.loc[logs["latency_ms"] < 0, "latency_ms"] = np.nan
    merged = pd.merge(logs, meta, on="tower_id", how="left")
    merged["throughput_mbps"] = merged["throughput_mbps"].fillna(merged.groupby("technology")["throughput_mbps"].transform("median"))
    merged["latency_ms"] = merged["latency_ms"].fillna(merged["latency_ms"].median())
    merged["sla_breach"] = merged["latency_ms"] > merged["sla_latency_ms"]
    print(compute_regional_kpis(merged).round(2).to_string(index=False))

