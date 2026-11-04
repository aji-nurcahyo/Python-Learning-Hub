"""Tugas Mini Project Chapter 28: REST API Data Client
Platform: Python Learning Hub
Institusi: Institut Teknologi Sumatera (ITERA)

Petunjuk:
Lengkapi implementasi ProductionApiClient di bawah ini.
Pastikan kode mematuhi kaidah penanganan request HTTP, Bearer token, pagination, dan retry backoff.
"""

import os
import time
from typing import Any, Optional


class MockApiServer:
    """Server simulasi offline untuk pengujian mandiri tugas."""

    def __init__(self, simulated_failures: int = 1) -> None:
        self.failures_remaining = simulated_failures
        self.valid_token = "itera_telecom_secret_token_2026"
        self.records = [
            {"id": "SITE-01", "name": "Tower ITERA Utama", "status": "ACTIVE"},
            {"id": "SITE-02", "name": "Tower Way Huwi", "status": "ACTIVE"},
            {"id": "SITE-03", "name": "Tower Jati Agung", "status": "MAINTENANCE"},
            {"id": "SITE-04", "name": "Tower Sukarame", "status": "ACTIVE"},
        ]

    def request(
        self,
        method: str,
        path: str,
        headers: dict[str, str],
        params: Optional[dict[str, Any]] = None,
        body: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        # Validasi Bearer Token
        auth = headers.get("Authorization", "")
        if not auth.startswith("Bearer ") or auth.split(" ")[1] != self.valid_token:
            return {"status": 401, "error": "Unauthorized"}

        # Simulasi Transient Error (503)
        if self.failures_remaining > 0:
            self.failures_remaining -= 1
            return {"status": 503, "error": "Transient Server Error"}

        if method == "GET" and path == "/api/v1/sites":
            params = params or {}
            page = int(params.get("page", 1))
            limit = int(params.get("limit", 2))
            start = (page - 1) * limit
            items = self.records[start : start + limit]
            has_next = (start + limit) < len(self.records)
            return {"status": 200, "page": page, "data": items, "has_next": has_next}

        if method == "POST" and path == "/api/v1/telemetry":
            if not body or "metric" not in body or "val" not in body:
                return {"status": 400, "error": "Bad Payload"}
            return {"status": 201, "message": "Saved", "data": body}

        return {"status": 404, "error": "Not Found"}


class ProductionApiClient:
    """Klien REST API tingkat produksi dengan fitur autentikasi aman, retry, dan paginasi."""

    def __init__(
        self,
        server: MockApiServer,
        token: Optional[str] = None,
        timeout_seconds: float = 3.0,
    ) -> None:
        self.server = server
        self.token = token or os.environ.get("API_TOKEN", "itera_telecom_secret_token_2026")
        self.timeout = timeout_seconds

    def get_headers(self) -> dict[str, str]:
        """Menyusun header HTTP lengkap termasuk Bearer token."""
        return {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "ProductionApiClient/1.0",
        }

    @staticmethod
    def mask_token(headers: dict[str, str]) -> dict[str, str]:
        """Menyamarkan isi header Authorization sebelum dicatat ke log audit."""
        safe = headers.copy()
        if "Authorization" in safe:
            val = safe["Authorization"]
            if len(val) > 16:
                safe["Authorization"] = f"{val[:11]}...{val[-4:]}"
        return safe

    def fetch_with_backoff(
        self,
        path: str,
        max_retries: int = 3,
        initial_delay: float = 0.05,
        backoff_mult: float = 2.0,
    ) -> dict[str, Any]:
        """Mengirim HTTP GET dengan algoritma exponential backoff saat menerima HTTP 503."""
        delay = initial_delay
        headers = self.get_headers()

        for attempt in range(1, max_retries + 1):
            res = self.server.request("GET", path, headers=headers)
            if res.get("status") == 200:
                return res

            if res.get("status") == 503 and attempt < max_retries:
                time.sleep(delay)
                delay *= backoff_mult
                continue

            return res

        return {"status": 500, "error": "Max retries reached"}

    def get_all_sites(self, path: str = "/api/v1/sites", page_size: int = 2) -> list[dict[str, Any]]:
        """Mengambil seluruh data tower dari endpoint paginasi hingga tuntas."""
        all_sites = []
        page = 1
        headers = self.get_headers()

        while True:
            res = self.server.request("GET", path, headers=headers, params={"page": page, "limit": page_size})
            if res.get("status") != 200:
                raise RuntimeError(f"Gagal mengambil halaman {page}: status {res.get('status')}")

            items = res.get("data", [])
            all_sites.extend(items)

            if not res.get("has_next", False):
                break
            page += 1

        return all_sites

    def submit_telemetry(self, path: str, metric_name: str, value: float) -> dict[str, Any]:
        """Mengirim data telemetri dengan HTTP POST."""
        headers = self.get_headers()
        body = {"metric": metric_name, "val": value, "timestamp": time.time()}
        return self.server.request("POST", path, headers=headers, body=body)


def main() -> None:
    print("=== PENGUJIAN MANDIRI: PRODUCTION REST API CLIENT ===")
    server = MockApiServer(simulated_failures=1)
    client = ProductionApiClient(server=server)

    # 1. Sanitasi Header
    masked = client.mask_token(client.get_headers())
    print("\n[1] Header Sanitasi:")
    print(f" -> Header Authorization Aman: {masked['Authorization']}")
    assert "..." in masked["Authorization"], "Token harus tersamar"

    # 2. Pengujian Retry Backoff
    print("\n[2] Menguji Exponential Backoff (Menghadapi 1 Transient Error 503):")
    res_retry = client.fetch_with_backoff("/api/v1/sites")
    print(f" -> Status Code Akhir: {res_retry.get('status')} (Berhasil pulih)")
    assert res_retry.get("status") == 200, "Harus pulih dan menghasilkan status 200"

    # 3. Pengujian Pagination Penuh
    print("\n[3] Menguji Traversal Paginasi:")
    sites = client.get_all_sites(page_size=2)
    for s in sites:
        print(f" -> Site: {s['name']} (ID: {s['id']})")
    assert len(sites) == 4, f"Ekspektasi 4 site, ditemukan {len(sites)}"

    # 4. Pengujian POST Telemetri
    print("\n[4] Menguji Pengiriman HTTP POST:")
    post_res = client.submit_telemetry("/api/v1/telemetry", "TEMPERATURE", 34.2)
    print(f" -> Respon POST: Status {post_res.get('status')} | {post_res.get('message')}")
    assert post_res.get("status") == 201, "Ekspektasi status 201 Created"

    print("\n[OK] SEMUA PENGUJIAN REST API CLIENT BERHASIL LULUS 100%!")


if __name__ == "__main__":
    main()
