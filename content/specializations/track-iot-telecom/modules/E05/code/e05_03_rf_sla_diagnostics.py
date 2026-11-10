from pathlib import Path
import pandas as pd


def diagnose_node_health(row: dict) -> dict:
    flags: list[str] = []
    if row["rsrp_dbm"] < -105.0:
        flags.append("COVERAGE_BLINDSPOT")
    elif row["rsrp_dbm"] >= -90.0 and row["sinr_db"] <= 3.0:
        flags.append("HIGH_INTERFERENCE")
    if row["temp_c"] >= 38.0:
        flags.append("THERMAL_ALERT")
    if row["packet_loss_pct"] >= 1.5:
        flags.append("HIGH_PACKET_LOSS")

    status = "CRITICAL" if len(flags) >= 2 else ("WARNING" if len(flags) == 1 else "HEALTHY")
    return {
        "node_id": row["node_id"],
        "region": row["region"],
        "rsrp_dbm": row["rsrp_dbm"],
        "sinr_db": row["sinr_db"],
        "interference_penalty_db": round(row["snr_db"] - row["sinr_db"], 2),
        "status": status,
        "flags": flags,
    }


def evaluate_all_nodes(csv_path: Path) -> list[dict]:
    df = pd.read_csv(csv_path)
    results = [diagnose_node_health(r) for r in df.to_dict(orient="records")]
    priority_rank = {"CRITICAL": 0, "WARNING": 1, "HEALTHY": 2}
    return sorted(results, key=lambda item: (priority_rank[item["status"]], item["sinr_db"]))


if __name__ == "__main__":
    csv_file = Path(__file__).resolve().parent.parent / "datasets" / "iot_node_telemetry_stream.csv"
    audit = evaluate_all_nodes(csv_file)
    for item in audit:
        print(f"{item['node_id']:12s} | {item['status']:8s} | SINR={item['sinr_db']:5.1f} dB | flags={item['flags']}")

