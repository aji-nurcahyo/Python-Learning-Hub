import httpx


def mock_api(request: httpx.Request) -> httpx.Response:
    if request.url.path == "/v1/health":
        return httpx.Response(
            200,
            json={"service": "telemetry-gateway", "status": "healthy", "version": "1.2.0"},
        )
    return httpx.Response(404, json={"detail": "Endpoint tidak ditemukan"})


transport = httpx.MockTransport(mock_api)
with httpx.Client(base_url="https://api.internal.local", transport=transport, timeout=5.0) as client:
    resp = client.get("/v1/health", headers={"Accept": "application/json"})
    resp.raise_for_status()
    data = resp.json()

print("Status Code :", resp.status_code)
print("Content-Type:", resp.headers.get("content-type"))
print("Payload JSON:", data)
