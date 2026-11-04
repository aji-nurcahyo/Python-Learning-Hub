"""Chapter 28 Example 04: HTTP POST Request with JSON Body
Python Learning Hub - Professional Python Engineering
"""

import json


class MockPostClient:
    """Mensimulasikan pengiriman HTTP POST dengan header Content-Type."""

    def post(self, url: str, json_data: dict, headers: dict) -> dict:
        # Memastikan header Content-Type dikirimkan
        if headers.get("Content-Type") != "application/json":
            return {"status_code": 415, "body": "Unsupported Media Type"}

        payload_bytes = json.dumps(json_data).encode("utf-8")
        return {
            "status_code": 201,
            "body": {
                "message": "Resource created successfully",
                "received_id": json_data.get("device_id"),
                "bytes_transferred": len(payload_bytes),
            },
        }


def main() -> None:
    client = MockPostClient()
    endpoint = "https://api.telecom.internal/v1/devices"
    payload = {
        "device_id": "SW-DIST-01",
        "vendor": "Cisco",
        "ports": 48,
        "is_poe": True,
    }
    req_headers = {
        "Content-Type": "application/json",
        "User-Agent": "TelecomController/2.0",
    }

    print(f"Mengirim HTTP POST ke {endpoint}...")
    resp = client.post(endpoint, json_data=payload, headers=req_headers)
    print(f"Status Code: {resp['status_code']}")
    print(f"Respons Body: {resp['body']}")


if __name__ == "__main__":
    main()

