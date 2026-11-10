from pathlib import Path
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
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

X_train_t = preprocessor.fit_transform(X_train)
X_test_t = preprocessor.transform(X_test)

print("Dimensi fitur sebelum transform :", X_train.shape[1])
print("Dimensi fitur sesudah OHE/Scale :", X_train_t.shape[1])
print("Missing value di X_test_t       :", int(pd.DataFrame(X_test_t.toarray() if hasattr(X_test_t, 'toarray') else X_test_t).isna().sum().sum()))
