from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

csv_path = Path(__file__).resolve().parent.parent / "datasets" / "fraud_alert_sample.csv"
df = pd.read_csv(csv_path)
features = ["amount_k", "night_tx", "velocity_1h", "distance_km"]

X_train, _, y_train, _ = train_test_split(
    df[features], df["fraud_flag"], test_size=0.25, stratify=df["fraud_flag"], random_state=42
)

pipe = Pipeline([("sc", StandardScaler()), ("clf", LogisticRegression(random_state=42))])
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

f1_scores = cross_val_score(pipe, X_train, y_train, cv=cv, scoring="f1")
auc_scores = cross_val_score(pipe, X_train, y_train, cv=cv, scoring="roc_auc")

print("F1 per fold      :", np.round(f1_scores, 3).tolist())
print(f"CV F1 Mean +- Std: {f1_scores.mean():.4f} +- {f1_scores.std():.4f}")
print(f"CV ROC-AUC Mean  : {auc_scores.mean():.4f} +- {auc_scores.std():.4f}")

