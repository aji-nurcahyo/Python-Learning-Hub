"""Chapter 30 Example 02: Capstone API Gateway Integration & Client Simulation
Python Learning Hub - Professional Capstone Project
"""

from typing import Any


class MockTelecomGateway:
    """Gateway API offline untuk demonstrasi pengambilan telemetri simpul jaringan."""

    def __init__(self) -> None:
        self.endpoints: dict[str, dict[str, Any]] = {
            "/api/v2/clusters/sumatera": {
                "cluster_name": "Sumatera Gateway Core",
                "active_nodes": 24,
                "overall_health_score": 98.4,
            },
            "/api/v2/clusters/jawa": {
                "cluster_name": "Jawa Backbone Core",
                "active_nodes": 48,
                "overall_health_score": 99.1,
            },
        }

    def fetch(self, path: str) -> dict[str, Any]:
        if path not in self.endpoints:
            return {"status_code": 404, "error": f"Path '{path}' not found"}
        return {"status_code": 200, "data": self.endpoints[path]}


def main() -> None:
    print("Mengambil Data Status Klaster Jaringan melalui API Gateway (Capstone Layer 2):\n")
    gateway = MockTelecomGateway()

    for path in ["/api/v2/clusters/sumatera", "/api/v2/clusters/jawa"]:
        res = gateway.fetch(path)
        payload = res["data"]
        print(f" -> Klaster: {payload['cluster_name']}")
        print(f"    Jumlah Simpul: {payload['active_nodes']} | Skor Kesehatan: {payload['overall_health_score']}%")


if __name__ == "__main__":
    main()

