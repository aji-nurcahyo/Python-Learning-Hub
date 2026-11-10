import httpx

RETRYABLE_STATUS = {502, 503, 504}
attempts = {"count": 0}


def flaky_handler(request: httpx.Request) -> httpx.Response:
    if request.url.path == "/v1/missing":
        return httpx.Response(404, json={"error": "Resource tidak ditemukan"})
    attempts["count"] += 1
    if attempts["count"] < 3:
        return httpx.Response(503, json={"error": "Service unavailable"})
    return httpx.Response(200, json={"ok": True, "attempt": attempts["count"]})


def get_with_retry(client: httpx.Client, path: str, max_attempts: int = 3) -> dict:
    for attempt in range(1, max_attempts + 1):
        resp = client.get(path)
        if resp.status_code in RETRYABLE_STATUS and attempt < max_attempts:
            continue
        resp.raise_for_status()
        return resp.json()
    raise RuntimeError("Batas retry terlampaui")


with httpx.Client(base_url="https://api.internal.local", transport=httpx.MockTransport(flaky_handler), timeout=5.0) as client:
    ok_data = get_with_retry(client, "/v1/metrics")
    print("Sukses setelah retry :", ok_data)

    try:
        get_with_retry(client, "/v1/missing")
    except httpx.HTTPStatusError as exc:
        print("Error 404 langsung dihentikan:", exc.response.status_code, exc.response.json())

