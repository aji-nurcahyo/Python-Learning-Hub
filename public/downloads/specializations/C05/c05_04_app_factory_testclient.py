import sys
import tempfile
import time
from pathlib import Path
from typing import Generator

from fastapi import FastAPI, Request
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from c05_01_domain_schemas import ServiceConfig
from c05_02_repository_db import init_db_factory
from c05_03_service_auth_router import build_nodes_router, make_hmac_token


def create_app(config: ServiceConfig):
    engine, SessionLocal = init_db_factory(config.db_url)

    def get_db() -> Generator[Session, None, None]:
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    app = FastAPI(title=config.service_name, version="1.0.0")

    @app.middleware("http")
    async def timing_middleware(request: Request, call_next):
        t0 = time.perf_counter()
        response = await call_next(request)
        response.headers["X-Process-Time-Ms"] = f"{(time.perf_counter() - t0) * 1000:.2f}"
        return response

    @app.get("/health", tags=["Operations"])
    def health() -> dict[str, str]:
        return {"status": "healthy", "service": config.service_name}

    app.include_router(build_nodes_router(get_db, config.api_secret))
    return app, engine


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as td:
        cfg = ServiceConfig(
            service_name="Telemetry Nodes Microservice",
            db_url=f"sqlite:///{Path(td) / 'capstone.db'}",
            api_secret="demo-capstone-secret-key-2025",
        )
        app, engine = create_app(cfg)
        try:
            client = TestClient(app)
            token = make_hmac_token("ops-lead", cfg.api_secret)
            headers = {"Authorization": f"Bearer {token}"}

            r_health = client.get("/health")
            r_unauth = client.post("/api/v1/nodes", json={"code": "LPG-01", "region": "Sumatera"})
            r_create = client.post("/api/v1/nodes", json={"code": "LPG-01", "region": "Sumatera"}, headers=headers)
            r_update = client.put("/api/v1/nodes/1", json={"region": "Sumatera", "status": "maintenance"}, headers=headers)
            r_list = client.get("/api/v1/nodes")

            print("1. Health public        :", r_health.status_code, r_health.json())
            print("2. Unauth create (401)  :", r_unauth.status_code)
            print("3. Auth create (201)    :", r_create.status_code, r_create.json()["code"])
            print("4. Update status (200)  :", r_update.status_code, r_update.json()["status"])
            print("5. Public list + header :", r_list.status_code, "count=", len(r_list.json()), "| timing_hdr=", "X-Process-Time-Ms" in r_list.headers)
        finally:
            engine.dispose()
