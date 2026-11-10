from pathlib import Path
import pandas as pd


def clean_retail_data(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path).copy()
    df["city"] = df["city"].astype(str).str.strip().str.title()
    df["category"] = df["category"].astype(str).str.strip().str.title()
    df = df.drop_duplicates(subset=["order_id"], keep="first").reset_index(drop=True)
    df["quantity"] = df["quantity"].fillna(1.0)
    df["unit_price"] = df["unit_price"].fillna(df.groupby("category")["unit_price"].transform("median"))
    df["revenue"] = df["quantity"] * df["unit_price"]
    return df


def test_clean_removes_duplicates_and_nulls() -> None:
    csv_path = Path(__file__).resolve().parent.parent / "datasets" / "retail_transactions_raw.csv"
    cleaned = clean_retail_data(csv_path)
    assert len(cleaned) == 11
    assert cleaned["order_id"].is_unique
    assert int(cleaned.isna().sum().sum()) == 0
    assert sorted(cleaned["category"].unique().tolist()) == ["Accessories", "Electronics", "Networking"]


def test_category_median_imputation_accuracy() -> None:
    csv_path = Path(__file__).resolve().parent.parent / "datasets" / "retail_transactions_raw.csv"
    cleaned = clean_retail_data(csv_path)
    trx003 = cleaned.loc[cleaned["order_id"] == "TRX003", "unit_price"].iloc[0]
    assert trx003 == 460000.0
