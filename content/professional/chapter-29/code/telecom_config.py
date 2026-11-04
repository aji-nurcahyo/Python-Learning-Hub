"""Chapter 29: Software Architecture & Deployment
Configuration Layer: Manajemen Konfigurasi Twelve-Factor Berbasis Environment Variables
"""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class AppConfig:
    """Konfigurasi aplikasi yang divalidasi dan diisolasi dari logika bisnis."""
    app_name: str
    environment: str
    service_port: int
    database_url: str
    log_level: str
    enable_metrics: bool

    @classmethod
    def load(cls) -> "AppConfig":
        env = os.environ.get("DEPLOY_ENV", "production").lower()
        port_raw = os.environ.get("SERVICE_PORT", "8000")
        try:
            port = int(port_raw)
        except ValueError:
            port = 8000

        db_url = os.environ.get("DATABASE_URL", "sqlite:///telecom_nodes.db")
        log_level = os.environ.get("LOG_LEVEL", "INFO").upper()
        metrics = os.environ.get("ENABLE_METRICS", "true").lower() in ("true", "1", "yes")

        return cls(
            app_name="TelecomDeploymentManager",
            environment=env,
            service_port=port,
            database_url=db_url,
            log_level=log_level,
            enable_metrics=metrics,
        )

