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


def test_pipeline_beats_dummy_and_handles_missing() -> None:
    csv_path = Path(__file__).resolve().parent.parent / "datasets" / "customer_churn_features.csv"
    df = pd.read_csv(csv_path)
    num_cols = ["tenure_months", "monthly_spend_k", "support_calls"]
    cat_cols = ["contract_type", "region"]
    X_train, X_test, y_train, y_test = train_test_split(
        df[num_cols + cat_cols], df["churned"], test_size=0.25, stratify=df["churned"], random_state=42
    )
    dummy = DummyClassifier(strategy="most_frequent").fit(X_train, y_train)
    prep = ColumnTransformer(
        [
            ("num", Pipeline([("imp", SimpleImputer(strategy="median")), ("sc", StandardScaler())]), num_cols),
            ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols),
        ]
    )
    pipe = Pipeline([("prep", prep), ("clf", LogisticRegression(max_iter=500, random_state=42))]).fit(X_train, y_train)
    assert accuracy_score(y_test, pipe.predict(X_test)) > accuracy_score(y_test, dummy.predict(X_test))
