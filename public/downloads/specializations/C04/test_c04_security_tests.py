import sys
from pathlib import Path
from fastapi.testclient import TestClient

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from c04_02_password_hash_hmac_token import create_signed_token, hash_password, verify_password, verify_signed_token
from c04_03_dependency_auth_guard import DEMO_API_TOKEN, build_secured_app


def test_password_hash_and_hmac_token_expiry() -> None:
    h = hash_password("Rahasia#99", salt="salt-unit-test")
    assert verify_password("Rahasia#99", h) is True
    assert verify_password("Salah", h) is False

    tok = create_signed_token("admin", exp_epoch=5000, secret="unit-test-hmac-secret-123")
    assert verify_signed_token(tok, "unit-test-hmac-secret-123", now_epoch=4000)["sub"] == "admin"
    assert verify_signed_token(tok + "tamper", "unit-test-hmac-secret-123", now_epoch=4000) is None
    assert verify_signed_token(tok, "unit-test-hmac-secret-123", now_epoch=6000) is None


def test_bearer_guard_rejects_missing_and_allows_valid() -> None:
    client = TestClient(build_secured_app())
    assert client.get("/admin/metrics").status_code == 401
    assert client.get("/admin/metrics", headers={"Authorization": "Bearer wrong"}).status_code == 401
    ok = client.get("/admin/metrics", headers={"Authorization": f"Bearer {DEMO_API_TOKEN}"})
    assert ok.status_code == 200
    assert ok.json()["authorized_as"] == "operator-itera"
