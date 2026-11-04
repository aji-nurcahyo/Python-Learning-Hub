"""Chapter 29 Example 03: Dependency Injection in Python
Python Learning Hub - Professional Python Engineering
"""

from typing import Protocol


# Abstraksi Pengirim Notifikasi (Port)
class Notifier(Protocol):
    def send(self, recipient: str, message: str) -> bool:
        ...


# Implementasi Konkret 1: Email Notifier (Produksi)
class EmailNotifier:
    def send(self, recipient: str, message: str) -> bool:
        print(f" [EMAIL] Mengirim pesan ke {recipient}: '{message}' via SMTP")
        return True


# Implementasi Konkret 2: Mock Notifier (Pengujian / Lingkungan Lokal)
class MockNotifier:
    def __init__(self) -> None:
        self.sent_messages: list[tuple[str, str]] = []

    def send(self, recipient: str, message: str) -> bool:
        print(f" [MOCK] Mencatat pesan uji untuk {recipient}: '{message}'")
        self.sent_messages.append((recipient, message))
        return True


# Service yang bergantung pada abstraksi Notifier (Inversion of Control)
class AlertService:
    def __init__(self, notifier: Notifier) -> None:
        self.notifier = notifier

    def broadcast_incident(self, target: str, severity: str, details: str) -> bool:
        formatted = f"[{severity.upper()}] Insiden Jaringan: {details}"
        return self.notifier.send(target, formatted)


def main() -> None:
    print("Mendemonstrasikan Pola Dependency Injection (DI):\n")

    # 1. Menggunakan MockNotifier untuk Unit Testing
    print("Mode Pengujian Lokal:")
    mock_engine = MockNotifier()
    test_service = AlertService(notifier=mock_engine)
    test_service.broadcast_incident("admin-test@itera.ac.id", "warning", "Fiber optic link down")
    print(f"Total pesan terekam di mock: {len(mock_engine.sent_messages)}\n")

    # 2. Menggunakan EmailNotifier untuk Produksi
    print("Mode Produksi:")
    prod_engine = EmailNotifier()
    prod_service = AlertService(notifier=prod_engine)
    prod_service.broadcast_incident("noc@itera.ac.id", "critical", "Core router unreachable")


if __name__ == "__main__":
    main()

