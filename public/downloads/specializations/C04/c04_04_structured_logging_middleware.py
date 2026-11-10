import logging
import time
from fastapi import FastAPI, Request
from fastapi.testclient import TestClient

audit_log: list[str] = []
logger = logging.getLogger("api.audit")
if not logger.handlers:
    logger.setLevel(logging.INFO)


def build_logged_app() -> FastAPI:
    app = FastAPI()

    @app.middleware("http")
    async def request_audit_middleware(request: Request, call_next):
        start = time.perf_counter()
        response = await call_next(request)
        elapsed_ms = round((time.perf_counter() - start) * 1000.0, 2)
        entry = f"method={request.method} path={request.url.path} status={response.status_code}"
        audit_log.append(entry)
        logger.info("%s elapsed_ms=%s", entry, elapsed_ms)
        response.headers["X-Process-Time-Ms"] = str(elapsed_ms)
        return response

    @app.get("/status")
    def get_status() -> dict[str, str]:
        return {"service": "ready"}

    return app


if __name__ == "__main__":
    audit_log.clear()
    client = TestClient(build_logged_app())
    res = client.get("/status")
    client.get("/not-exist")
    print("Header timing ada :", "X-Process-Time-Ms" in res.headers)
    print("Catatan audit log :", audit_log)
