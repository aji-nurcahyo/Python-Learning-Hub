"""Chapter 28 Example 08: Asynchronous HTTP Client Pattern
Python Learning Hub - Professional Python Engineering
"""

import asyncio
from typing import Any


class MockAsyncHttpClient:
    """Simulasi client HTTP asinkron untuk mengambil data dari multiple endpoint secara efisien."""

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    async def get(self, endpoint: str) -> dict[str, Any]:
        """Simulasi pengiriman HTTP GET secara non-blocking."""
        # Simulasi network delay mikro tanpa blocking event loop
        await asyncio.sleep(0.01)
        return {
            "endpoint": endpoint,
            "url": f"{self.base_url}{endpoint}",
            "status_code": 200,
            "data": f"Data telemetri dari {endpoint}",
        }


async def fetch_all_telecom_nodes(endpoints: list[str]) -> list[dict[str, Any]]:
    client = MockAsyncHttpClient("https://api.telekom.example.id/v1")
    # Mengirim multiple request konkuren menggunakan asyncio.gather
    tasks = [client.get(endpoint) for endpoint in endpoints]
    results = await asyncio.gather(*tasks)
    return list(results)


def main() -> None:
    endpoints = ["/nodes/JKT-01", "/nodes/BDG-02", "/nodes/SBY-03"]
    print("Mengirim 3 request HTTP secara konkuren menggunakan event loop asyncio:")

    responses = asyncio.run(fetch_all_telecom_nodes(endpoints))
    for res in sorted(responses, key=lambda x: x["endpoint"]):
        print(f" -> [{res['status_code']}] URL: {res['url']} | Payload: {res['data']}")

    print("\nSemua request asinkron selesai dikumpulkan tanpa memblokir thread.")


if __name__ == "__main__":
    main()

