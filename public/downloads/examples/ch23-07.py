"""Chapter 23 Example 07: Dependency Injection Basics
Python Learning Hub - Professional Python Engineering
"""

from abc import ABC, abstractmethod


class NotificationService(ABC):
    @abstractmethod
    def notify(self, message: str) -> None:
        pass


class ConsoleNotifier(NotificationService):
    def notify(self, message: str) -> None:
        print(f"[CONSOLE NOTIF] {message}")


class EmailNotifier(NotificationService):
    def notify(self, message: str) -> None:
        print(f"[EMAIL NOTIF] Mengirim surel: {message}")


class MonitoringAgent:
    """Kelas bisnis yang menerima dependensi notifier melalui constructor injection."""

    def __init__(self, notifier: NotificationService) -> None:
        self.notifier = notifier

    def alert_incident(self, severity: str, desc: str) -> None:
        payload = f"Severity: {severity.upper()} | {desc}"
        self.notifier.notify(payload)


def main() -> None:
    agent1 = MonitoringAgent(ConsoleNotifier())
    agent1.alert_incident("warning", "Suhu server mendekati 75 C")

    agent2 = MonitoringAgent(EmailNotifier())
    agent2.alert_incident("critical", "Koneksi gateway terputus")


if __name__ == "__main__":
    main()

