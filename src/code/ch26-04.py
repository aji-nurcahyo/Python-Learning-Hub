"""Chapter 26 Example 04: Mocking External Dependencies with patch
Python Learning Hub - Professional Python Engineering
"""

import unittest
from unittest.mock import MagicMock, patch


class ExternalGatewayClient:
    """Klien I/O eksternal yang berkomunikasi melalui jaringan."""

    def fetch_status(self, gateway_id: str) -> dict[str, str]:
        # Pada produksi, fungsi ini melakukan panggilan socket/HTTP nyata
        raise RuntimeError("Koneksi jaringan fisik tidak tersedia di unit test")


class GatewayService:
    def __init__(self, client: ExternalGatewayClient) -> None:
        self.client = client

    def is_gateway_healthy(self, gateway_id: str) -> bool:
        resp = self.client.fetch_status(gateway_id)
        return resp.get("status") == "UP"


class TestGatewayService(unittest.TestCase):
    def test_gateway_healthy_with_mock(self) -> None:
        mock_client = MagicMock(spec=ExternalGatewayClient)
        mock_client.fetch_status.return_value = {"status": "UP", "load": "25%"}

        service = GatewayService(mock_client)
        self.assertTrue(service.is_gateway_healthy("GW-01"))
        mock_client.fetch_status.assert_called_once_with("GW-01")


def main() -> None:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestGatewayService)
    runner = unittest.TextTestRunner(verbosity=0)
    result = runner.run(suite)
    print(f"Uji Mocking Selesai | Tests: {result.testsRun}, Sukses: {result.wasSuccessful()}")


if __name__ == "__main__":
    main()

