import sys
from pathlib import Path
from fastapi.testclient import TestClient

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from c03_04_fastapi_db_dependency import create_db_app


def test_sqlite_persistence_and_conflict(tmp_path: Path) -> None:
    app, engine = create_db_app(f"sqlite:///{tmp_path / 'test_assets.db'}")
    try:
        client = TestClient(app)
        res = client.post("/assets", json={"hostname": "RTR-SUM-01", "site": "Palembang"})
        assert res.status_code == 201
        assert res.json()["id"] == 1

        dup = client.post("/assets", json={"hostname": "RTR-SUM-01", "site": "Palembang"})
        assert dup.status_code == 409

        listing = client.get("/assets")
        assert listing.status_code == 200
        assert len(listing.json()) == 1
    finally:
        engine.dispose()

