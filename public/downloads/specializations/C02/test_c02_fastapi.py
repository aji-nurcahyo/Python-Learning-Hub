import sys
from pathlib import Path
from fastapi.testclient import TestClient

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from c02_03_crud_inmemory_status import build_inventory_app


def test_crud_lifecycle_and_validation() -> None:
    app = build_inventory_app()
    client = TestClient(app)

    bad = client.post("/products", json={"name": "A", "stock": -1})
    assert bad.status_code == 422

    created = client.post("/products", json={"name": "Switch L2", "stock": 10})
    assert created.status_code == 201
    pid = created.json()["id"]

    fetched = client.get(f"/products/{pid}")
    assert fetched.status_code == 200
    assert fetched.json()["stock"] == 10

    deleted = client.delete(f"/products/{pid}")
    assert deleted.status_code == 204
    assert client.get(f"/products/{pid}").status_code == 404
