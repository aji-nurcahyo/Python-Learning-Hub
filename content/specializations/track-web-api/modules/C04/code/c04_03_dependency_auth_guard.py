from fastapi import Depends, FastAPI, Header, HTTPException, status
from fastapi.testclient import TestClient

DEMO_API_TOKEN = "token-itera-lab-2025"


def require_bearer_token(authorization: str | None = Header(default=None)) -> str:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Header Authorization Bearer wajib disertakan",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = authorization.removeprefix("Bearer ").strip()
    if token != DEMO_API_TOKEN:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token tidak valid")
    return "operator-itera"


def build_secured_app() -> FastAPI:
    app = FastAPI()

    @app.get("/public/ping")
    def public_ping() -> dict[str, str]:
        return {"ping": "pong"}

    @app.get("/admin/metrics")
    def protected_metrics(actor: str = Depends(require_bearer_token)) -> dict[str, object]:
        return {"authorized_as": actor, "active_nodes": 48}

    return app


if __name__ == "__main__":
    client = TestClient(build_secured_app())
    print("Public /public/ping          :", client.get("/public/ping").status_code)
    print("Tanpa token /admin/metrics   :", client.get("/admin/metrics").status_code)
    print("Token valid /admin/metrics   :", client.get("/admin/metrics", headers={"Authorization": f"Bearer {DEMO_API_TOKEN}"}).json())

