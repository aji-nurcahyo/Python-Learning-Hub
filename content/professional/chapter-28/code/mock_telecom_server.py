"""Chapter 28: Networking & API Integration
In-Memory Mock REST API Server untuk Pengujian & Simulasi Offline
"""

from typing import Any, Optional


class MockHttpResponse:
    """Representasi respons HTTP hasil panggilan client ke mock server."""

    def __init__(self, status_code: int, data: Any, headers: Optional[dict[str, str]] = None) -> None:
        self.status_code = status_code
        self._data = data
        self.headers = headers or {"Content-Type": "application/json"}

    def json(self) -> Any:
        return self._data

    @property
    def is_success(self) -> bool:
        return 200 <= self.status_code < 300


class MockTelecomServer:
    """Mock server simulasi gateway telemetri jaringan telekomunikasi."""

    VALID_TOKEN = "valid_telecom_token_prod_99"

    NODES_DB = [
        {"id": "ND-01", "name": "BTS-Lampung-Utara", "band": "1800MHz", "status": "ONLINE"},
        {"id": "ND-02", "name": "BTS-Bandar-Lampung", "band": "2100MHz", "status": "ONLINE"},
        {"id": "ND-03", "name": "BTS-Kalianda-01", "band": "900MHz", "status": "MAINTENANCE"},
        {"id": "ND-04", "name": "BTS-Metro-Center", "band": "1800MHz", "status": "ONLINE"},
        {"id": "ND-05", "name": "BTS-Pringsewu-02", "band": "2300MHz", "status": "ONLINE"},
    ]

    def __init__(self, transient_failures: int = 0) -> None:
        self.transient_failures = transient_failures
        self.attempt_count = 0
        self.created_metrics: list[dict[str, Any]] = []

    def handle_request(
        self,
        method: str,
        path: str,
        headers: Optional[dict[str, str]] = None,
        params: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
    ) -> MockHttpResponse:
        """Memproses request HTTP dan mengembalikan MockHttpResponse."""
        headers = headers or {}
        params = params or {}

        # 1. Verifikasi Autentikasi Bearer Token
        auth_header = headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return MockHttpResponse(401, {"error": "Unauthorized: Missing or invalid Bearer token"})

        token = auth_header.split("Bearer ", 1)[1].strip()
        if token != self.VALID_TOKEN:
            return MockHttpResponse(403, {"error": "Forbidden: Invalid credentials"})

        # 2. Simulasi Transient Error (misal 503 Service Unavailable)
        if self.transient_failures > 0 and self.attempt_count < self.transient_failures:
            self.attempt_count += 1
            return MockHttpResponse(503, {"error": "Service Temporarily Unavailable"})

        # 3. Routing Endpoint
        if method == "GET" and path == "/api/v1/nodes":
            page = int(params.get("page", 1))
            limit = int(params.get("limit", 2))
            start = (page - 1) * limit
            items = self.NODES_DB[start : start + limit]
            total = len(self.NODES_DB)
            total_pages = (total + limit - 1) // limit

            return MockHttpResponse(
                200,
                {
                    "page": page,
                    "limit": limit,
                    "total_records": total,
                    "total_pages": total_pages,
                    "has_next": page < total_pages,
                    "data": items,
                },
            )

        if method == "POST" and path == "/api/v1/metrics":
            if not json_body:
                return MockHttpResponse(400, {"error": "Bad Request: JSON body required"})
            required = ["node_id", "metric_name", "value"]
            if not all(k in json_body for k in required):
                return MockHttpResponse(422, {"error": f"Unprocessable Entity: Missing {required}"})

            new_entry = {**json_body, "id": len(self.created_metrics) + 1}
            self.created_metrics.append(new_entry)
            return MockHttpResponse(201, {"message": "Metric recorded", "record": new_entry})

        return MockHttpResponse(404, {"error": f"Endpoint not found: {method} {path}"})

