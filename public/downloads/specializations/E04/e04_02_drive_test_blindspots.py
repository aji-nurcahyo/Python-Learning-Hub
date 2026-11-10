from pathlib import Path
import pandas as pd


def diagnose_rf_issue(rsrp_dbm: float, sinr_db: float) -> str:
    if rsrp_dbm < -105.0 and sinr_db <= 3.0:
        return "CRITICAL_EDGE"
    if rsrp_dbm < -105.0:
        return "COVERAGE_BLINDSPOT"
    if rsrp_dbm >= -90.0 and sinr_db <= 3.0:
        return "HIGH_INTERFERENCE"
    return "HEALTHY"


if __name__ == "__main__":
    csv_path = Path(__file__).resolve().parent.parent / "datasets" / "drive_test_lte_measurements.csv"
    df = pd.read_csv(csv_path)
    df["diagnosis"] = [diagnose_rf_issue(r, s) for r, s in zip(df["rsrp_dbm"], df["sinr_db"])]

    print("Ringkasan Diagnosis Titik Drive Test:")
    print(df["diagnosis"].value_counts().to_string())

    print("\nTitik Bermasalah (Interferensi Kuat vs Coverage Blindspot):")
    issues = df.loc[df["diagnosis"] != "HEALTHY", ["point_id", "cell_id", "rsrp_dbm", "sinr_db", "handover_count", "diagnosis"]]
    print(issues.to_string(index=False))

