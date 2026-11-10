import sys
from pathlib import Path
from fastapi.testclient import TestClient

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from c05_01_domain_schemas import ServiceConfig
from c05_03_service_auth_router import make_hmac_token
from c05_04_app_factory_testclient import create_app


def test_capstone_api_full_lifecycle_and_openapi(tmp_path: Path) -> None:
    cfg = ServiceConfig(
        service_name="Telemetry Capstone Test",
        db_url=f"sqlite:///{tmp_path / 'integration.db'}",
        api_secret="pytest-integration-secret-key",
    )
    app, engine = create_app(cfg)
    try:
        client = TestClient(app)
        auth = {"Authorization": f"Bearer {make_hmac_token('tester', cfg.api_secret)}"}

        assert client.get("/health").status_code == 200
        assert client.post("/api/v1/nodes", json={"code": "N01", "region": "Jawa"}).status_code == 401
        assert client.post("/api/v1/nodes", json={"code": "X", "region": "Jawa"}, headers=auth).status_code == 422

        r201 = client.post("/api/v1/nodes", json={"code": "N01", "region": "Jawa"}, headers=auth)
        assert r201.status_code == 201
        node_id = r201.json()["id"]

        assert client.post("/api/v1/nodes", json={"code": "N01", "region": "Jawa"}, headers=auth).status_code == 409
        assert client.put(f"/api/v1/nodes/{node_id}", json={"region": "Jawa", "status": "offline"}, headers=auth).status_code == 200
        assert client.delete(f"/api/v1/nodes/{node_id}", headers=auth).status_code == 204
        assert client.delete(f"/api/v1/nodes/{node_id}", headers=auth).status_code == 404
        assert "/api/v1/nodes" in app.openapi()["paths"]
    finally:
        engine.dispose()
