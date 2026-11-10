from pathlib import Path
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, roc_auc_score
from sklearn.model_selection import GridSearchCV, StratifiedKFold, train_test_split
from sklearn.pipeline import Pipeline

csv_path = Path(__file__).resolve().parent.parent / "datasets" / "fraud_alert_sample.csv"
df = pd.read_csv(csv_path)
features = ["amount_k", "night_tx", "velocity_1h", "distance_km"]

X_train, X_test, y_train, y_test = train_test_split(
    df[features], df["fraud_flag"], test_size=0.25, stratify=df["fraud_flag"], random_state=42
)

pipe = Pipeline([("rf", RandomForestClassifier(random_state=42))])
param_grid = {
    "rf__n_estimators": [20, 50],
    "rf__max_depth": [2, 4, None],
}
cv = StratifiedKFold(n_splits=4, shuffle=True, random_state=42)
search = GridSearchCV(pipe, param_grid=param_grid, cv=cv, scoring="roc_auc")
search.fit(X_train, y_train)

best_model = search.best_estimator_
test_probs = best_model.predict_proba(X_test)[:, 1]
test_preds = best_model.predict(X_test)

print("Best Hyperparameters :", search.best_params_)
print("Best Mean CV ROC-AUC :", round(float(search.best_score_), 4))
print("Holdout Test F1      :", round(float(f1_score(y_test, test_preds)), 4))
print("Holdout Test ROC-AUC :", round(float(roc_auc_score(y_test, test_probs)), 4))

