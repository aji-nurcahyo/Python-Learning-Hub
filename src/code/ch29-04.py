"""Chapter 29 Example 04: Configuration Management with Environment Variables
Python Learning Hub - Professional Python Engineering
"""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class AppConfig:
    """Konfigurasi aplikasi yang divalidasi dan diinjeksi dari environment variables."""

    app_name: str
    environment: str  # 'development' | 'staging' | 'production'
    port: int
    db_host: str
    enable_debug: bool

    @classmethod
    def from_env(cls) -> "AppConfig":
        env = os.environ.get("APP_ENV", "development").lower()
        port_raw = os.environ.get("APP_PORT", "8080")
        try:
            port = int(port_raw)
        except ValueError:
            port = 8080

        db_host = os.environ.get("DATABASE_HOST", "localhost")
        debug = os.environ.get("APP_DEBUG", "false").lower() in ("true", "1", "yes")

        return cls(
            app_name="TelecomDataHub",
            environment=env,
            port=port,
            db_host=db_host,
            enable_debug=debug,
        )


def main() -> None:
    print("Membaca Konfigurasi Aplikasi Berdasarkan Prinsip Twelve-Factor App:\n")

    # Simulasi environment variables
    os.environ["APP_ENV"] = "production"
    os.environ["APP_PORT"] = "9000"
    os.environ["DATABASE_HOST"] = "db.telecom.internal"
    os.environ["APP_DEBUG"] = "false"

    config = AppConfig.from_env()
    print("Konfigurasi Berhasil Diinisialisasi:")
    print(f" -> Aplikasi     : {config.app_name}")
    print(f" -> Lingkungan   : {config.environment}")
    print(f" -> Port Layanan : {config.port}")
    print(f" -> Basis Data   : {config.db_host}")
    print(f" -> Mode Debug   : {config.enable_debug}")


if __name__ == "__main__":
    main()

