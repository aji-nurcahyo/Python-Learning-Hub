from pathlib import Path
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import recall_score, roc_auc_score
from sklearn.model_selection import GridSearchCV, StratifiedKFold, cross_val_score, train_test_split
from sklearn.pipeline import Pipeline


def test_stratified_cv_and_gridsearch_tuning() -> None:
    csv_path = Path(__file__).resolve().parent.parent / "datasets" / "fraud_alert_sample.csv"
    df = pd.read_csv(csv_path)
    features = ["amount_k", "night_tx", "velocity_1h", "distance_km"]
    X_tr, X_te, y_tr, y_te = train_test_split(
        df[features], df["fraud_flag"], test_size=0.25, stratify=df["fraud_flag"], random_state=42
    )
    cv = StratifiedKFold(n_splits=4, shuffle=True, random_state=42)
    pipe = Pipeline([("rf", RandomForestClassifier(random_state=42))])
    auc_scores = cross_val_score(pipe, X_tr, y_tr, cv=cv, scoring="roc_auc")
    assert auc_scores.mean() > 0.85

    search = GridSearchCV(pipe, {"rf__max_depth": [2, 4], "rf__n_estimators": [20, 50]}, cv=cv, scoring="roc_auc")
    search.fit(X_tr, y_tr)
    probs = search.best_estimator_.predict_proba(X_te)[:, 1]
    assert roc_auc_score(y_te, probs) > 0.85


def test_lowering_threshold_preserves_or_improves_recall() -> None:
    y_true = pd.Series([0, 0, 1, 1, 0, 1])
    y_prob = pd.Series([0.1, 0.2, 0.35, 0.8, 0.4, 0.65])
    r_high = recall_score(y_true, (y_prob >= 0.7).astype(int))
    r_low = recall_score(y_true, (y_prob >= 0.3).astype(int))
    assert r_low >= r_high

