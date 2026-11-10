from pathlib import Path
import pandas as pd

csv_path = Path(__file__).resolve().parent.parent / "datasets" / "retail_transactions_raw.csv"
df = pd.read_csv(csv_path).drop_duplicates(subset=["order_id"]).copy()
df["city"] = df["city"].str.strip().str.title()
df["category"] = df["category"].str.strip().str.title()
df["quantity"] = df["quantity"].fillna(1.0)
df["unit_price"] = df["unit_price"].fillna(df.groupby("category")["unit_price"].transform("median"))
df["revenue"] = df["quantity"] * df["unit_price"]

# Named aggregation per kota
city_summary = (
    df.groupby("city", as_index=False)
    .agg(
        total_orders=("order_id", "count"),
        total_qty=("quantity", "sum"),
        total_revenue=("revenue", "sum"),
    )
    .sort_values("total_revenue", ascending=False)
)

# Pivot table kota vs kategori
pivot_rev = pd.pivot_table(
    df,
    values="revenue",
    index="city",
    columns="category",
    aggfunc="sum",
    fill_value=0.0,
)

print("Ringkasan Omzet per Kota:")
print(city_summary.to_string(index=False))
print("\nPivot Table Kota x Kategori:")
print(pivot_rev.to_string())

