from pathlib import Path
import pandas as pd

csv_path = Path(__file__).resolve().parent.parent / "datasets" / "retail_transactions_raw.csv"
orders = pd.read_csv(csv_path).drop_duplicates(subset=["order_id"]).copy()
orders["city"] = orders["city"].str.strip().str.title()
orders["category"] = orders["category"].str.strip().str.title()
orders["order_date"] = pd.to_datetime(orders["order_date"], format="%Y-%m-%d")
orders["quantity"] = orders["quantity"].fillna(1.0)
orders["unit_price"] = orders["unit_price"].fillna(orders.groupby("category")["unit_price"].transform("median"))
orders["revenue"] = orders["quantity"] * orders["unit_price"]

region_map = pd.DataFrame(
    {
        "city": ["Bandar Lampung", "Jakarta", "Palembang", "Bandung"],
        "region": ["Sumatera", "Jawa", "Sumatera", "Jawa"],
        "shipping_sla_days": [2, 1, 2, 1],
    }
)

enriched = pd.merge(orders, region_map, on="city", how="left")
enriched["order_day"] = enriched["order_date"].dt.day_name()

regional_kpi = (
    enriched.groupby("region", as_index=False)
    .agg(orders=("order_id", "count"), total_revenue=("revenue", "sum"), avg_sla=("shipping_sla_days", "mean"))
)
print("Ringkasan Regional Hasil Merge:")
print(regional_kpi.to_string(index=False))

