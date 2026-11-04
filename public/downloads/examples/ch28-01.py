"""Chapter 28 Example 01: HTTP GET Request Simulation & Status Codes
Python Learning Hub - Professional Python Engineering
"""

import json
from dataclasses import dataclass


@dataclass
class HttpResponse:
    status_code: int
    headers: dict[str, str]
    body: str

    def json(self) -> dict:
        return json.loads(self.body)


class MockHttpClient:
    """Klien HTTP deterministik lokal untuk demonstrasi tanpa dependensi jaringan eksternal."""

    def get(self, url: str) -> HttpResponse:
        if "/api/v1/telecom/status" in url:
            payload = json.dumps({"status": "ONLINE", "uptime_hours": 720, "region": "asia-southeast2"})
            return HttpResponse(status_code=200, headers={"Content-Type": "application/json"}, body=payload)
        return HttpResponse(status_code=404, headers={}, body=json.dumps({"error": "Not Found"}))


def main() -> None:
    client = MockHttpClient()
    url = "https://api.telecom.internal/api/v1/telecom/status"

    print(f"Mengirim HTTP GET ke: {url}")
    resp = client.get(url)

    print(f"Status Code  : {resp.status_code}")
    print(f"Content-Type : {resp.headers.get('Content-Type')}")
    data = resp.json()
    print(f"Response Body: Status={data['status']}, Uptime={data['uptime_hours']} jam, Region={data['region']}")


if __name__ == "__main__":
    main()
