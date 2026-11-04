"""Chapter 30: Professional Capstone Project
Configuration Layer: Konfigurasi Terpusat Twelve-Factor App
"""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class PlatformConfig:
    """Konfigurasi operasional platform yang dimuat dari environment variables."""
    app_name: str
    environment: str
    data_dir: str
    batch_size: int
    alert_loss_threshold: float
    alert_temp_threshold: float

    @classmethod
    def load(cls) -> "PlatformConfig":
        env = os.environ.get("APP_ENV", "production").lower()
        data_dir = os.environ.get("DATA_DIR", "./data")
        batch_raw = os.environ.get("BATCH_SIZE", "100")
        try:
            batch = int(batch_raw)
        except ValueError:
            batch = 100

        loss_raw = os.environ.get("ALERT_LOSS_THRESHOLD", "5.0")
        try:
            loss_thresh = float(loss_raw)
        except ValueError:
            loss_thresh = 5.0

        temp_raw = os.environ.get("ALERT_TEMP_THRESHOLD", "75.0")
        try:
            temp_thresh = float(temp_raw)
        except ValueError:
            temp_thresh = 75.0

        return cls(
            app_name="DataMonitoringPlatform",
            environment=env,
            data_dir=data_dir,
            batch_size=batch,
            alert_loss_threshold=loss_thresh,
            alert_temp_threshold=temp_thresh,
        )

