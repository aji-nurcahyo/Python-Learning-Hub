"""Chapter 23 Example 02: Dataclass Configuration
Python Learning Hub - Professional Python Engineering
"""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class NetworkConfig:
    """Konfigurasi jaringan immutable menggunakan @dataclass."""

    host: str
    port: int = 8080
    timeout_sec: float = 5.0
    allowed_ips: list[str] = field(default_factory=lambda: ["127.0.0.1", "192.168.1.1"])

    def endpoint(self) -> str:
        return f"{self.host}:{self.port}"


def main() -> None:
    cfg = NetworkConfig(host="10.0.0.1", port=443)
    print(f"Host     : {cfg.host}")
    print(f"Port     : {cfg.port}")
    print(f"Endpoint : {cfg.endpoint()}")
    print(f"Allowed  : {cfg.allowed_ips}")


if __name__ == "__main__":
    main()
