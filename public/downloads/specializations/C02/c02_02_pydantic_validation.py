from fastapi import FastAPI, status
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field


class ItemCreate(BaseModel):
    name: str = Field(min_length=2, max_length=60)
    stock: int = Field(ge=0)
    price: float = Field(gt=0)


class ItemOut(ItemCreate):
    id: int


app = FastAPI()


@app.post("/items", response_model=ItemOut, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreate) -> ItemOut:
    return ItemOut(id=101, **payload.model_dump())


client = TestClient(app)
r_ok = client.post("/items", json={"name": "Antenna 5G", "stock": 12, "price": 850000.0})
r_bad = client.post("/items", json={"name": "X", "stock": -3, "price": 0})

print("POST valid status :", r_ok.status_code, "| body:", r_ok.json())
print("POST invalid status:", r_bad.status_code, "| jumlah error:", len(r_bad.json()["detail"]))
