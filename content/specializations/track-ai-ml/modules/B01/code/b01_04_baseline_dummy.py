from pathlib import Path
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

csv_path = Path(__file__).resolve().parent.parent / "datasets" / "customer_churn_features.csv"
df = pd.read_csv(csv_path)

num_cols = ["tenure_months", "monthly_spend_k", "support_calls"]
cat_cols = ["contract_type", "region"]

X_train, X_test, y_train, y_test = train_test_split(
    df[num_cols + cat_cols], df["churned"], test_size=0.25, stratify=df["churned"], random_state=42
)

baseline = DummyClassifier(strategy="most_frequent")
baseline.fit(X_train, y_train)
base_acc = accuracy_score(y_test, baseline.predict(X_test))

prep = ColumnTransformer(
    [
        ("num", Pipeline([("imp", SimpleImputer(strategy="median")), ("sc", StandardScaler())]), num_cols),
        ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols),
    ]
)
clf_pipe = Pipeline([("prep", prep), ("clf", LogisticRegression(max_iter=500, random_state=42))])
clf_pipe.fit(X_train, y_train)
model_acc = accuracy_score(y_test, clf_pipe.predict(X_test))

print(f"Baseline (DummyClassifier) Accuracy : {base_acc:.4f}")
print(f"Pipeline (LogisticReg) Accuracy     : {model_acc:.4f}")
print(f"Kenaikan di atas Baseline           : +{model_acc - base_acc:.4f}")

