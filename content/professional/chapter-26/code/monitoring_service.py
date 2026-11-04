"""Layanan Monitoring Telekomunikasi & Klien Jaringan (Chapter 26)
Python Learning Hub - Professional Python Engineering
"""

import logging
from typing import Any

logger = logging.getLogger("telecom.service")


class ExternalApiClient:
    """Klien I/O eksternal yang melakukan panggilan jaringan nyata ke server remote."""

    def fetch_node_metrics(self, node_id: str) -> dict[str, Any]:
        # Dalam produksi nyata, method ini melakukan HTTP/socket request fisik
        raise RuntimeError("Koneksi jaringan fisik eksternal tidak aktif di lingkungan uji")


class TelecomMonitoringService:
    """Layanan bisnis yang memantau node dan mencatat status via structured logging."""

    def __init__(self, client: ExternalApiClient) -> None:
        self.client = client

    def check_node_health(self, node_id: str) -> dict[str, Any]:
        logger.info(f"Memulai pemeriksaan kesehatan untuk node: {node_id}")
        try:
            metrics = self.client.fetch_node_metrics(node_id)
        except Exception as err:
            logger.error(f"Gagal mengambil metrik node {node_id}: {err}")
            raise

        rsrp = float(metrics.get("rsrp_dbm", -120.0))
        if rsrp < -100.0:
            logger.warning(f"Sinyal lemah terdeteksi pada node {node_id}: {rsrp} dBm")
            status = "WARNING_POOR_SIGNAL"
        else:
            logger.info(f"Node {node_id} beroperasi dalam kondisi optimal: {rsrp} dBm")
            status = "HEALTHY"

        return {"node_id": node_id, "status": status, "metrics": metrics}
