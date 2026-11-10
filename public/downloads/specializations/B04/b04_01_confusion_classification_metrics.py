from pathlib import Path
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

csv_path = Path(__file__).resolve().parent.parent / "datasets" / "fraud_alert_sample.csv"
df = pd.read_csv(csv_path)
features = ["amount_k", "night_tx", "velocity_1h", "distance_km"]

X_train, X_test, y_train, y_test = train_test_split(
    df[features], df["fraud_flag"], test_size=0.30, stratify=df["fraud_flag"], random_state=42
)

pipe = Pipeline([("sc", StandardScaler()), ("clf", LogisticRegression(random_state=42))]).fit(X_train, y_train)
preds = pipe.predict(X_test)
probs = pipe.predict_proba(X_test)[:, 1]

cm = confusion_matrix(y_test, preds)
print("Confusion Matrix [[TN, FP], [FN, TP]]:\n", cm)
print(f"Precision : {precision_score(y_test, preds, zero_division=0):.4f}")
print(f"Recall    : {recall_score(y_test, preds, zero_division=0):.4f}")
print(f"F1-Score  : {f1_score(y_test, preds, zero_division=0):.4f}")
print(f"ROC-AUC   : {roc_auc_score(y_test, probs):.4f}")

