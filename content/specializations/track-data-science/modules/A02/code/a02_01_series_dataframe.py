import pandas as pd

df = pd.DataFrame(
    {
        "node": ["N-01", "N-02", "N-03", "N-04"],
        "region": ["Sumatera", "Jawa", "Sumatera", "Kalimantan"],
        "uptime_pct": [99.8, 99.2, 97.5, 98.9],
        "active_users": pd.Series([1240, 2980, 890, 1410], dtype="int64"),
    }
)

print("Dimensi DataFrame :", df.shape)
print("Daftar kolom      :", df.columns.tolist())
print("\nAkses iloc (2 baris pertama, 3 kolom pertama):")
print(df.iloc[:2, :3].to_string(index=False))

print("\nFilter loc (region Sumatera dengan uptime >= 98):")
filtered = df.loc[(df["region"] == "Sumatera") & (df["uptime_pct"] >= 98.0), ["node", "active_users"]]
print(filtered.to_string(index=False))

