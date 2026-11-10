from pathlib import Path
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

csv_path = Path(__file__).resolve().parent.parent / "datasets" / "network_capacity_metrics.csv"
df = pd.read_csv(csv_path)

features = ["active_users", "bandwidth_mhz", "snr_db", "backhaul_util_pct"]
X_train, X_test, y_train, y_test = train_test_split(
    df[features], df["congestion_risk"], test_size=0.25, stratify=df["congestion_risk"], random_state=42
)

pipe = Pipeline([("scaler", StandardScaler()), ("clf", LogisticRegression(random_state=42))])
pipe.fit(X_train, y_train)

probs = pipe.predict_proba(X_test)[:, 1]
preds = pipe.predict(X_test)

result = X_test.copy()
result["actual"] = y_test.values
result["pred"] = preds
result["prob_risk"] = probs.round(3)

print("Akurasi Uji Logistic Regression:", round(float(accuracy_score(y_test, preds)), 4))
print(result[["active_users", "backhaul_util_pct", "actual", "pred", "prob_risk"]].to_string(index=False))

