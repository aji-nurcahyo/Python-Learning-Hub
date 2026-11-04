"""Unit Test Suite untuk Chapter 28: Networking & API Integration
Memvalidasi HTTP GET, POST, Pagination, Exponential Backoff, dan Sanitasi Header.
"""

import os
import sys
import unittest

# Menambahkan direktori code ke sys.path agar modul dapat diimpor
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CODE_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "code")
if CODE_DIR not in sys.path:
    sys.path.insert(0, CODE_DIR)

from mock_telecom_server import MockHttpResponse, MockTelecomServer
from telecom_api_client import TelecomApiClient


class TestNetworkingApiClient(unittest.TestCase):
    """Test case untuk memvalidasi fungsi klien REST API dan keamanannya."""

    def setUp(self) -> None:
        self.server = MockTelecomServer()
        self.client = TelecomApiClient(server_instance=self.server)

    def test_successful_get_request(self) -> None:
        """Memvalidasi HTTP GET request mengembalikan status 200 dan data yang valid."""
        response = self.client.get("/api/v1/nodes", params={"page": 1, "limit": 2})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["page"], 1)
        self.assertEqual(len(data["data"]), 2)
        self.assertTrue(data["has_next"])

    def test_post_request_with_json_payload(self) -> None:
        """Memvalidasi pengiriman payload telemetri dengan HTTP POST menghasilkan status 201 Created."""
        payload = {"node_id": "ND-02", "metric_name": "TEMPERATURE_C", "value": 31.8}
        response = self.client.post("/api/v1/metrics", json_body=payload)
        self.assertEqual(response.status_code, 201)
        res_data = response.json()
        self.assertEqual(res_data["message"], "Metric recorded")
        self.assertEqual(res_data["record"]["node_id"], "ND-02")

    def test_pagination_full_traversal(self) -> None:
        """Memvalidasi pengumpulan seluruh record melintasi beberapa halaman API secara otomatis."""
        records = self.client.fetch_all_pages("/api/v1/nodes", limit_per_page=2)
        # Database mock memiliki 5 records
        self.assertEqual(len(records), 5)
        node_ids = [r["id"] for r in records]
        self.assertEqual(node_ids, ["ND-01", "ND-02", "ND-03", "ND-04", "ND-05"])

    def test_retry_exponential_backoff_recovery(self) -> None:
        """Memvalidasi klien mampu bertahan dan pulih dari gangguan sementara (503) dengan retry."""
        faulty_server = MockTelecomServer(transient_failures=2)
        retry_client = TelecomApiClient(server_instance=faulty_server)

        # Retry max 3 kali harus berhasil karena failure disimulasikan 2 kali
        res = retry_client.request_with_retry("/api/v1/nodes", max_retries=3)
        self.assertEqual(res.status_code, 200)

    def test_unauthorized_token_error(self) -> None:
        """Memvalidasi bahwa token yang tidak valid menghasilkan HTTP 403 Forbidden."""
        self.client.token = "token_palsu_tidak_terdaftar"
        response = self.client.get("/api/v1/nodes")
        self.assertEqual(response.status_code, 403)

    def test_mask_headers_security(self) -> None:
        """Memvalidasi bahwa header Authorization disamarkan demi keamanan audit log."""
        raw_headers = {"Authorization": "Bearer super_secret_production_key_12345", "Accept": "application/json"}
        masked = TelecomApiClient.mask_headers_for_logging(raw_headers)
        self.assertNotIn("super_secret_production_key_12345", masked["Authorization"])
        self.assertTrue(masked["Authorization"].startswith("Bearer sup"))
        self.assertTrue(masked["Authorization"].endswith("2345"))


if __name__ == "__main__":
    unittest.main()

