"""Starter code Tugas C04: Keamanan Token, Konfigurasi Env & Logging API."""

from __future__ import annotations

from dataclasses import dataclass
from fastapi import FastAPI


@dataclass(frozen=True)
class AppSettings:
    app_env: str
    api_secret: str
    token_ttl_seconds: int = 3600

    @classmethod
    def from_mapping(cls, env: dict[str, str]) -> "AppSettings":
        # TODO: Validasi panjang API_SECRET >= 16 dan kembalikan instance AppSettings
        raise NotImplementedError("Implementasikan AppSettings.from_mapping")


def hash_secret_value(raw: str) -> str:
    """Menghasilkan hash PBKDF2-HMAC-SHA256 bersalt acak."""
    # TODO: Gunakan secrets.token_hex(16) + hashlib.pbkdf2_hmac
    raise NotImplementedError("Implementasikan hash_secret_value")


def build_protected_app(settings: AppSettings) -> FastAPI:
    """Membangun FastAPI app dengan auth Bearer guard serta request logging middleware."""
    # TODO: Daftarkan middleware logging dan endpoint terproteksi /admin/status
    raise NotImplementedError("Implementasikan build_protected_app")


if __name__ == "__main__":
    print("Starter C04 siap diuji melalui TestClient dan pytest.")

