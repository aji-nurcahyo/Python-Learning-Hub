from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI(title="Inventory Gateway API")

ITEMS = [
    {"id": 1, "name": "Router Core X1", "category": "networking"},
    {"id": 2, "name": "Sensor Suhu S2", "category": "iot"},
    {"id": 3, "name": "Switch Gigabit G8", "category": "networking"},
]


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/items")
def list_items(category: str | None = None) -> list[dict]:
    if category is None:
        return ITEMS
    return [item for item in ITEMS if item["category"] == category]


@app.get("/items/{item_id}")
def get_item(item_id: int) -> dict:
    return {"requested_id": item_id}


client = TestClient(app)
print("GET /health                  :", client.get("/health").json())
print("GET /items?category=iot      :", client.get("/items", params={"category": "iot"}).json())
print("GET /items/42                :", client.get("/items/42").json())
print("GET /items/bukan-angka (422) :", client.get("/items/bukan-angka").status_code)

