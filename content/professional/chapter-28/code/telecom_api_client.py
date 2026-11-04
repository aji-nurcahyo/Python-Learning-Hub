"""Chapter 28: Networking & API Integration
Klien REST API Tangguh (Headers, Timeout, Retry Backoff, Pagination, Safe Logging)
"""

import os
import time
from typing import Any, Optional

try:
    from mock_telecom_server import MockHttpResponse, MockTelecomServer
except ImportError:
    from .mock_telecom_server import MockHttpResponse, MockTelecomServer


class TelecomApiClient:
    """Client REST API untuk sistem telekomunikasi dengan fitur produksi lengkap."""

    def __init__(
        self,
        base_url: str = "https://telecom.itera.ac.id",
        server_instance: Optional[MockTelecomServer] = None,
        token_env_var: str = "TELECOM_API_TOKEN",
        timeout: float = 3.0,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.server = server_instance or MockTelecomServer()
        self.token = os.environ.get(token_env_var, "valid_telecom_token_prod_99")
        self.timeout = timeout

    def _get_headers(self) -> dict[str, str]:
        """Menyusun headers autentikasi Bearer dan spesifikasi konten."""
        return {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "TelecomClient/3.0 (Python Learning Hub)",
        }

    @staticmethod
    def mask_headers_for_logging(headers: dict[str, str]) -> dict[str, str]:
        """Menyamarkan token Authorization sebelum dicatat ke log sistem."""
        masked = headers.copy()
        if "Authorization" in masked:
            val = masked["Authorization"]
            if len(val) > 15:
                masked["Authorization"] = f"{val[:10]}...{val[-4:]}"
        return masked

    def get(self, endpoint: str, params: Optional[dict[str, Any]] = None) -> MockHttpResponse:
        """Mengirim HTTP GET request."""
        headers = self._get_headers()
        return self.server.handle_request("GET", endpoint, headers=headers, params=params)

    def post(self, endpoint: str, json_body: dict[str, Any]) -> MockHttpResponse:
        """Mengirim HTTP POST request dengan payload JSON."""
        headers = self._get_headers()
        return self.server.handle_request("POST", endpoint, headers=headers, json_body=json_body)

    def fetch_all_pages(self, endpoint: str, limit_per_page: int = 2) -> list[dict[str, Any]]:
        """Mengumpulkan seluruh data dari endpoint terpaginasi secara iteratif."""
        all_records: list[dict[str, Any]] = []
        page = 1

        while True:
            resp = self.get(endpoint, params={"page": page, "limit": limit_per_page})
            if not resp.is_success:
                raise RuntimeError(f"Gagal mengambil halaman {page}: {resp.status_code}")

            data = resp.json()
            items = data.get("data", [])
            all_records.extend(items)

            if not data.get("has_next", False):
                break
            page += 1

        return all_records

    def request_with_retry(
        self,
        endpoint: str,
        max_retries: int = 3,
        initial_backoff: float = 0.05,
        backoff_factor: float = 2.0,
    ) -> MockHttpResponse:
        """Mengirim request dengan exponential backoff jika menemui transient server error."""
        delay = initial_backoff
        for attempt in range(1, max_retries + 1):
            resp = self.get(endpoint)
            # Jika berhasil (200 OK), kembalikan langsung
            if resp.status_code == 200:
                return resp

            # Jika transient error (503 Service Unavailable atau 429 Too Many Requests)
            if resp.status_code in (429, 503) and attempt < max_retries:
                time.sleep(delay)
                delay *= backoff_factor
                continue

            return resp

        return resp

