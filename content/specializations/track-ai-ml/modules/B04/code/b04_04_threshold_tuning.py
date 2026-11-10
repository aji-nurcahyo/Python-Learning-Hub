from pathlib import Path
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

csv_path = Path(__file__).resolve().parent.parent / "datasets" / "fraud_alert_sample.csv"
df = pd.read_csv(csv_path)
features = ["amount_k", "night_tx", "velocity_1h", "distance_km"]

X_train, X_test, y_train, y_test = train_test_split(
    df[features], df["fraud_flag"], test_size=0.35, stratify=df["fraud_flag"], random_state=42
)

pipe = Pipeline([("sc", StandardScaler()), ("clf", LogisticRegression(random_state=42))]).fit(X_train, y_train)
probs = pipe.predict_proba(X_test)[:, 1]

print("Evaluasi Trade-Off Decision Threshold:")
for thr in [0.25, 0.50, 0.75]:
    preds = (probs >= thr).astype(int)
    p = precision_score(y_test, preds, zero_division=0)
    r = recall_score(y_test, preds, zero_division=0)
    f1 = f1_score(y_test, preds, zero_division=0)
    print(f"Threshold={thr:.2f} | Precision={p:.3f} | Recall={r:.3f} | F1={f1:.3f}")

