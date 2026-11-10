from pathlib import Path
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

csv_path = Path(__file__).resolve().parent.parent / "datasets" / "network_capacity_metrics.csv"
df = pd.read_csv(csv_path)

features = ["active_users", "bandwidth_mhz", "snr_db", "backhaul_util_pct"]
X_train, X_test, y_train, y_test = train_test_split(
    df[features], df["congestion_risk"], test_size=0.25, stratify=df["congestion_risk"], random_state=42
)

dt = DecisionTreeClassifier(max_depth=4, random_state=42).fit(X_train, y_train)
rf = RandomForestClassifier(n_estimators=60, random_state=42).fit(X_train, y_train)

print(f"DecisionTree Accuracy : {accuracy_score(y_test, dt.predict(X_test)):.4f}")
print(f"RandomForest Accuracy : {accuracy_score(y_test, rf.predict(X_test)):.4f}")

importances = pd.Series(rf.feature_importances_, index=features).sort_values(ascending=False)
print("\nFeature Importances (Random Forest):")
for feat, imp in importances.items():
    print(f" - {feat:20s}: {imp:.4f}")

