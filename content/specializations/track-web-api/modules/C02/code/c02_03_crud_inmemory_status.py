from fastapi import FastAPI, HTTPException, Response, status
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field


class ProductIn(BaseModel):
    name: str = Field(min_length=2)
    stock: int = Field(ge=0)


class ProductOut(ProductIn):
    id: int


def build_inventory_app() -> FastAPI:
    app = FastAPI(title="Modular Inventory API")
    store: dict[int, ProductOut] = {}
    seq = {"next": 1}

    @app.post("/products", response_model=ProductOut, status_code=status.HTTP_201_CREATED)
    def create_product(payload: ProductIn) -> ProductOut:
        pid = seq["next"]
        seq["next"] += 1
        item = ProductOut(id=pid, **payload.model_dump())
        store[pid] = item
        return item

    @app.get("/products/{pid}", response_model=ProductOut)
    def read_product(pid: int) -> ProductOut:
        if pid not in store:
            raise HTTPException(status_code=404, detail="Produk tidak ditemukan")
        return store[pid]

    @app.put("/products/{pid}", response_model=ProductOut)
    def update_product(pid: int, payload: ProductIn) -> ProductOut:
        if pid not in store:
            raise HTTPException(status_code=404, detail="Produk tidak ditemukan")
        updated = ProductOut(id=pid, **payload.model_dump())
        store[pid] = updated
        return updated

    @app.delete("/products/{pid}", status_code=status.HTTP_204_NO_CONTENT)
    def delete_product(pid: int) -> Response:
        if pid not in store:
            raise HTTPException(status_code=404, detail="Produk tidak ditemukan")
        del store[pid]
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return app


if __name__ == "__main__":
    client = TestClient(build_inventory_app())
    created = client.post("/products", json={"name": "Modem Fiber", "stock": 25})
    updated = client.put("/products/1", json={"name": "Modem Fiber Pro", "stock": 19})
    deleted = client.delete("/products/1")
    after_del = client.get("/products/1")

    print("1. Create (POST)  :", created.status_code, created.json())
    print("2. Update (PUT)   :", updated.status_code, updated.json())
    print("3. Delete (DELETE):", deleted.status_code)
    print("4. Get after del  :", after_del.status_code, after_del.json())
