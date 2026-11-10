from pathlib import Path
import pandas as pd
from sklearn.compose import ColumnTransformer
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

preprocessor = ColumnTransformer(
    transformers=[
        ("num", Pipeline([("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())]), num_cols),
        ("cat", Pipeline([("imputer", SimpleImputer(strategy="most_frequent")), ("ohe", OneHotEncoder(handle_unknown="ignore"))]), cat_cols),
    ]
)

model_pipeline = Pipeline(
    steps=[
        ("prep", preprocessor),
        ("clf", LogisticRegression(max_iter=500, random_state=42)),
    ]
)

model_pipeline.fit(X_train, y_train)
preds = model_pipeline.predict(X_test)
print("Langkah Pipeline :", [name for name, _ in model_pipeline.steps])
print("Prediksi X_test  :", preds.tolist())
print("Aktual   y_test  :", y_test.tolist())
print("Akurasi Uji      :", round(float(accuracy_score(y_test, preds)), 4))
