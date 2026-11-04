"""Chapter 28: Networking & API Integration
Contoh Terpadu Klien REST API: GET, POST, Pagination, dan Log Sanitization
"""

import os
from mock_telecom_server import MockTelecomServer
from telecom_api_client import TelecomApiClient


def main() -> None:
    print("=== DEMO CHAPTER 28: NETWORKING & REST API INTEGRATION ===\n")

    # Inisialisasi mock server dan client
    server = MockTelecomServer()
    client = TelecomApiClient(server_instance=server)

    # 1. Menguji Safe Logging (Sanitasi Header)
    raw_headers = client._get_headers()
    masked = client.mask_headers_for_logging(raw_headers)
    print("[1] Log Header Aman (Credential Sanitization):")
    print(f" -> Authorization asli disamarkan menjadi: {masked['Authorization']}")
    print(f" -> User-Agent: {masked['User-Agent']}\n")

    # 2. Mengambil Seluruh Halaman dengan Pagination
    print("[2] Mengambil Data Paginasi BTS dari /api/v1/nodes:")
    nodes = client.fetch_all_pages("/api/v1/nodes", limit_per_page=2)
    for node in nodes:
        print(f" -> Simpul: {node['name']} ({node['id']}) | Band: {node['band']} | Status: {node['status']}")
    print(f"Total BTS berhasil diunduh: {len(nodes)} simpul.\n")

    # 3. Mengirimkan Data Telemetri dengan HTTP POST
    print("[3] Mengirimkan Payload Telemetri Baru via HTTP POST:")
    metric_payload = {
        "node_id": "ND-01",
        "metric_name": "RSRP_SIGNAL_STRENGTH",
        "value": -85.4,
    }
    response = client.post("/api/v1/metrics", json_body=metric_payload)
    print(f" -> Status Code: {response.status_code}")
    print(f" -> Respons Server: {response.json()}\n")

    print("Semua demonstrasi interaksi REST API selesai dengan sukses.")


if __name__ == "__main__":
    main()
