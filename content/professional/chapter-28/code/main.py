"""Chapter 28: Networking & API Integration
Main Application Entry Point: REST API Data Client System
"""

from mock_telecom_server import MockTelecomServer
from telecom_api_client import TelecomApiClient


def run_system() -> None:
    print("Memulai REST API Data Client System...")
    # Simulasi server yang mengalami transient error 1 kali sebelum pulih
    server = MockTelecomServer(transient_failures=1)
    client = TelecomApiClient(server_instance=server)

    print("\n[1] Menguji Ketahanan Client terhadap Transient Fault (Exponential Backoff):")
    res = client.request_with_retry("/api/v1/nodes?page=1&limit=2", max_retries=3)
    print(f" -> Status Code Akhir: {res.status_code} (Berhasil pulih dari error awal)")

    print("\n[2] Menjalankan Pengumpulan Data Terpaginasi:")
    nodes = client.fetch_all_pages("/api/v1/nodes", limit_per_page=3)
    print(f" -> Diperoleh {len(nodes)} records infrastruktur jaringan.")

    print("\nREST API Data Client System siap digunakan pada lingkungan produksi.")


if __name__ == "__main__":
    run_system()

