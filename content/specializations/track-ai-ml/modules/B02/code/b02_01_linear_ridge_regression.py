from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error, r2_score, root_mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

csv_path = Path(__file__).resolve().parent.parent / "datasets" / "network_capacity_metrics.csv"
df = pd.read_csv(csv_path)

features = ["active_users", "bandwidth_mhz", "snr_db", "backhaul_util_pct"]
X_train, X_test, y_train, y_test = train_test_split(df[features], df["throughput_mbps"], test_size=0.25, random_state=42)

models = {
    "DummyMedian": DummyRegressor(strategy="median"),
    "LinearRegression": Pipeline([("scaler", StandardScaler()), ("reg", LinearRegression())]),
    "Ridge(alpha=1.0)": Pipeline([("scaler", StandardScaler()), ("reg", Ridge(alpha=1.0))]),
}

for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    rmse = root_mean_squared_error(y_test, preds)
    r2 = r2_score(y_test, preds)
    print(f"{name:18s} | MAE={mae:6.2f} Mbps | RMSE={rmse:6.2f} Mbps | R2={r2:6.4f}")

