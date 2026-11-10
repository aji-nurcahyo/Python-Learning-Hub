import httpx
import pytest
from pydantic import BaseModel, Field, ValidationError


class Reading(BaseModel):
    device_id: str
    temp_c: float = Field(ge=-40.0, le=120.0)


def test_retry_succeeds_on_transient_503_and_stops_on_404() -> None:
    calls = {"n": 0}

    def handler(req: httpx.Request) -> httpx.Response:
        if req.url.path == "/not-found":
            return httpx.Response(404)
        calls["n"] += 1
        return httpx.Response(503) if calls["n"] < 2 else httpx.Response(200, json={"device_id": "D1", "temp_c": 29.4})

    with httpx.Client(base_url="https://mock.local", transport=httpx.MockTransport(handler), timeout=3.0) as client:
        for attempt in range(3):
            resp = client.get("/reading")
            if resp.status_code == 503 and attempt < 2:
                continue
            break
        assert resp.status_code == 200
        parsed = Reading.model_validate(resp.json())
        assert parsed.device_id == "D1"

        r404 = client.get("/not-found")
        assert r404.status_code == 404


def test_pydantic_rejects_out_of_range_temperature() -> None:
    with pytest.raises(ValidationError):
        Reading.model_validate({"device_id": "D2", "temp_c": 999.0})
