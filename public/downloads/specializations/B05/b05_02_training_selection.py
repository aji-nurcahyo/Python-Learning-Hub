import sys
from pathlib import Path
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, roc_auc_score
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from b05_01_feature_engineering import FEATURE_COLS, engineer_domain_features


def select_best_model(df_raw: pd.DataFrame):
    df = engineer_domain_features(df_raw)
    X_train, X_test, y_train, y_test = train_test_split(
        df[FEATURE_COLS], df["failure_risk"], test_size=0.25, stratify=df["failure_risk"], random_state=42
    )

    candidates = {
        "Dummy": DummyClassifier(strategy="most_frequent"),
        "LogisticRegression": Pipeline(
            [("imp", SimpleImputer(strategy="median")), ("sc", StandardScaler()), ("clf", LogisticRegression(random_state=42))]
        ),
        "RandomForest": Pipeline(
            [("imp", SimpleImputer(strategy="median")), ("clf", RandomForestClassifier(n_estimators=50, max_depth=3, random_state=42))]
        ),
    }

    cv = StratifiedKFold(n_splits=4, shuffle=True, random_state=42)
    cv_summary = {}
    for name, pipe in candidates.items():
        scores = cross_val_score(pipe, X_train, y_train, cv=cv, scoring="roc_auc")
        cv_summary[name] = float(scores.mean())

    best_name = max([k for k in cv_summary if k != "Dummy"], key=lambda k: cv_summary[k])
    best_model = candidates[best_name].fit(X_train, y_train)
    probs = best_model.predict_proba(X_test)[:, 1]
    preds = best_model.predict(X_test)

    metrics = {
        "selected_model": best_name,
        "dummy_cv_auc": round(cv_summary["Dummy"], 4),
        "selected_cv_auc": round(cv_summary[best_name], 4),
        "holdout_f1": round(float(f1_score(y_test, preds)), 4),
        "holdout_roc_auc": round(float(roc_auc_score(y_test, probs)), 4),
    }
    return best_model, metrics, X_test


if __name__ == "__main__":
    csv_path = CODE_DIR.parent / "datasets" / "telecom_maintenance_train.csv"
    _, metrics, _ = select_best_model(pd.read_csv(csv_path))
    print("Hasil Seleksi & Evaluasi Holdout Model:")
    for k, v in metrics.items():
        print(f" - {k:16s}: {v}")

