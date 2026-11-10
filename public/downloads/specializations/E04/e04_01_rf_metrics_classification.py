from pathlib import Path
import pandas as pd


def classify_rsrp(rsrp_dbm: float) -> str:
    if rsrp_dbm >= -80.0:
        return "Excellent"
    if rsrp_dbm >= -90.0:
        return "Good"
    if rsrp_dbm >= -105.0:
        return "Mid-Cell"
    return "Cell-Edge"


def classify_sinr(sinr_db: float) -> str:
    if sinr_db >= 20.0:
        return "Excellent"
    if sinr_db >= 13.0:
        return "Good"
    if sinr_db >= 0.0:
        return "Mid-Cell"
    return "Cell-Edge"


if __name__ == "__main__":
    csv_path = Path(__file__).resolve().parent.parent / "datasets" / "drive_test_lte_measurements.csv"
    df = pd.read_csv(csv_path)
    df["rsrp_grade"] = df["rsrp_dbm"].apply(classify_rsrp)
    df["sinr_grade"] = df["sinr_db"].apply(classify_sinr)
    df["interference_penalty_db"] = (df["snr_db"] - df["sinr_db"]).round(2)

    print("Distribusi Kelas RSRP :", df["rsrp_grade"].value_counts().to_dict())
    print("Distribusi Kelas SINR :", df["sinr_grade"].value_counts().to_dict())
    print("\nCuplikan Perbedaan SNR vs SINR (efek interferensi sel):")
    print(df[["point_id", "rsrp_dbm", "snr_db", "sinr_db", "interference_penalty_db"]].head(6).to_string(index=False))

