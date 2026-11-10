import httpx

CATALOG = [
    {"id": f"DEV-{i:02d}", "region": "Sumatera" if i % 2 == 1 else "Jawa"}
    for i in range(1, 8)
]


def paginated_handler(request: httpx.Request) -> httpx.Response:
    page = int(request.url.params.get("page", "1"))
    size = int(request.url.params.get("size", "3"))
    region = request.url.params.get("region")
    filtered = [d for d in CATALOG if (region is None or d["region"] == region)]
    start = (page - 1) * size
    chunk = filtered[start : start + size]
    return httpx.Response(200, json={"page": page, "items": chunk})


def fetch_all_devices(client: httpx.Client, region: str) -> list[dict]:
    collected: list[dict] = []
    page = 1
    while True:
        res = client.get("/v1/devices", params={"page": page, "size": 3, "region": region})
        res.raise_for_status()
        items = res.json()["items"]
        if not items:
            break
        collected.extend(items)
        page += 1
    return collected


with httpx.Client(base_url="https://api.internal.local", transport=httpx.MockTransport(paginated_handler), timeout=5.0) as client:
    sumatera_devs = fetch_all_devices(client, region="Sumatera")

print("Total perangkat Sumatera ditarik:", len(sumatera_devs))
print("Daftar ID perangkat             :", [d["id"] for d in sumatera_devs])

