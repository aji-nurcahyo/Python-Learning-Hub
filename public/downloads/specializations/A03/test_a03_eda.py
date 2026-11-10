from pathlib import Path
import pandas as pd


def detect_iqr_outliers(series: pd.Series) -> tuple[pd.Series, dict[str, float]]:
    q1 = float(series.quantile(0.25))
    q3 = float(series.quantile(0.75))
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    mask = (series < lower) | (series > upper)
    return mask, {"q1": q1, "q3": q3, "iqr": iqr, "lower": lower, "upper": upper}


def test_iqr_identifies_high_latency_towers() -> None:
    csv_path = Path(__file__).resolve().parent.parent / "datasets" / "telecom_qos_kpi.csv"
    df = pd.read_csv(csv_path)
    mask, bounds = detect_iqr_outliers(df["latency_ms"])
    flagged = sorted(df.loc[mask, "tower_id"].tolist())
    assert bounds["upper"] > bounds["q3"]
    assert "TWR-09" in flagged
    assert "TWR-05" in flagged


def test_median_more_robust_than_mean_under_outlier() -> None:
    s = pd.Series([15.0, 16.0, 17.0, 18.0, 19.0, 250.0])
    assert abs(s.median() - 17.5) < 1e-9
    assert s.mean() > 50.0
