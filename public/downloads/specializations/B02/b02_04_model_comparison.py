from pathlib import Path
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

csv_path = Path(__file__).resolve().parent.parent / "datasets" / "network_capacity_metrics.csv"
df = pd.read_csv(csv_path)
features = ["active_users", "bandwidth_mhz", "snr_db", "backhaul_util_pct"]

X_train, X_test, y_train, y_test = train_test_split(
    df[features], df["congestion_risk"], test_size=0.30, stratify=df["congestion_risk"], random_state=42
)

candidates = {
    "DummyBaseline": DummyClassifier(strategy="most_frequent"),
    "LogisticRegression": Pipeline([("sc", StandardScaler()), ("clf", LogisticRegression(random_state=42))]),
    "DecisionTree": DecisionTreeClassifier(max_depth=3, random_state=42),
    "RandomForest": RandomForestClassifier(n_estimators=60, random_state=42),
}

rows = []
for name, clf in candidates.items():
    clf.fit(X_train, y_train)
    pred = clf.predict(X_test)
    rows.append(
        {
            "model": name,
            "accuracy": round(float(accuracy_score(y_test, pred)), 4),
            "f1_score": round(float(f1_score(y_test, pred, zero_division=0)), 4),
        }
    )

print("Benchmark Model Klasifikasi Risiko Kongesti:")
print(pd.DataFrame(rows).sort_values(["f1_score", "accuracy"], ascending=False).to_string(index=False))

