from pathlib import Path
import pandas as pd

csv_path = Path(__file__).resolve().parent.parent / "datasets" / "retail_transactions_raw.csv"
raw = pd.read_csv(csv_path)
print("Baris awal        :", len(raw))
print("Missing awal      :", raw.isna().sum().to_dict())

clean = raw.copy()
clean["city"] = clean["city"].astype(str).str.strip().str.title()
clean["category"] = clean["category"].astype(str).str.strip().str.title()
clean = clean.drop_duplicates(subset=["order_id"], keep="first").reset_index(drop=True)

# Imputasi missing quantity -> 1.0, unit_price -> median masing-masing category
clean["quantity"] = clean["quantity"].fillna(1.0)
cat_median_price = clean.groupby("category")["unit_price"].transform("median")
clean["unit_price"] = clean["unit_price"].fillna(cat_median_price)
clean["revenue"] = clean["quantity"] * clean["unit_price"]

print("Baris setelah dedup:", len(clean))
print("Missing akhir      :", int(clean.isna().sum().sum()))
print("\nTabel Transaksi Bersih (5 teratas):")
print(clean[["order_id", "city", "category", "quantity", "revenue"]].head(5).to_string(index=False))

