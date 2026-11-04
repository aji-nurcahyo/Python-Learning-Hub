data = [
    {"id": "S01", "rsrp": -82},
    {"id": "S02", "rsrp": -107},
    {"id": "S03", "rsrp": -95},
]
terbaik = sorted(data, key=lambda x: x["rsrp"], reverse=True)
print([x["id"] for x in terbaik])
