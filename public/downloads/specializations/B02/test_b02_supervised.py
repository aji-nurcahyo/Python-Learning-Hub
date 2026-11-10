from pathlib import Path
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import Ridge
from sklearn.metrics import accuracy_score, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def test_ridge_regression_high_r2() -> None:
    csv_path = Path(__file__).resolve().parent.parent / "datasets" / "network_capacity_metrics.csv"
    df = pd.read_csv(csv_path)
    features = ["active_users", "bandwidth_mhz", "snr_db", "backhaul_util_pct"]
    X_tr, X_te, y_tr, y_te = train_test_split(df[features], df["throughput_mbps"], test_size=0.25, random_state=42)
    pipe = Pipeline([("sc", StandardScaler()), ("reg", Ridge(alpha=1.0))]).fit(X_tr, y_tr)
    assert r2_score(y_te, pipe.predict(X_te)) > 0.85


def test_random_forest_classifier_and_feature_importance() -> None:
    csv_path = Path(__file__).resolve().parent.parent / "datasets" / "network_capacity_metrics.csv"
    df = pd.read_csv(csv_path)
    features = ["active_users", "bandwidth_mhz", "snr_db", "backhaul_util_pct"]
    X_tr, X_te, y_tr, y_te = train_test_split(
        df[features], df["congestion_risk"], test_size=0.25, stratify=df["congestion_risk"], random_state=42
    )
    rf = RandomForestClassifier(n_estimators=60, random_state=42).fit(X_tr, y_tr)
    assert accuracy_score(y_te, rf.predict(X_te)) >= 0.80
    assert abs(sum(rf.feature_importances_) - 1.0) < 1e-6

