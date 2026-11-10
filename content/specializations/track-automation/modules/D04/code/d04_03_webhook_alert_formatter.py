import httpx


def build_alert_payload(job_name: str, severity: str, detail: str) -> dict:
    return {
        "job": job_name,
        "severity": severity.upper(),
        "message": detail,
        "source": "automation-worker",
    }


def send_webhook_alert(client: httpx.Client, webhook_url: str, payload: dict) -> int:
    resp = client.post(webhook_url, json=payload)
    resp.raise_for_status()
    return resp.status_code


if __name__ == "__main__":
    captured: list[dict] = []

    def mock_webhook(request: httpx.Request) -> httpx.Response:
        import json

        captured.append(json.loads(request.content.decode("utf-8")))
        return httpx.Response(202, json={"accepted": True})

    payload = build_alert_payload("nightly-etl-sync", "critical", "Disk temp penuh 95%")
    with httpx.Client(transport=httpx.MockTransport(mock_webhook), timeout=5.0) as client:
        code = send_webhook_alert(client, "https://hooks.internal.local/ops-alerts", payload)

    print("HTTP Status Webhook :", code)
    print("Payload terkirim    :", captured[0])

