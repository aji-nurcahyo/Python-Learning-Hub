from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

csv_path = Path(__file__).resolve().parent.parent / "datasets" / "customer_churn_features.csv"
df = pd.read_csv(csv_path)

X = df.drop(columns=["customer_id", "churned"])
y = df["churned"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, stratify=y, random_state=42
)

print("Total sampel       :", len(df))
print("Train shape        :", X_train.shape, "| proporsi churn:", round(float(y_train.mean()), 2))
print("Test shape         :", X_test.shape, "| proporsi churn:", round(float(y_test.mean()), 2))
