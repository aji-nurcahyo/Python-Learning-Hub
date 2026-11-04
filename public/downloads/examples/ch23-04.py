"""Chapter 23 Example 04: Composition over Inheritance
Python Learning Hub - Professional Python Engineering
"""


class PowerSupply:
    """Komponen penyedia daya."""

    def __init__(self, voltage: float) -> None:
        self.voltage = voltage

    def is_healthy(self) -> bool:
        return self.voltage >= 11.5


class TelemetryLogger:
    """Komponen pencatat log telemetri."""

    def log(self, message: str) -> str:
        return f"[LOG-TELEMETRI] {message}"


class TelecomNode:
    """Node telekomunikasi yang dibangun melalui komposisi komponen."""

    def __init__(self, node_id: str, power: PowerSupply, logger: TelemetryLogger) -> None:
        self.node_id = node_id
        self.power = power
        self.logger = logger

    def operate(self) -> str:
        if not self.power.is_healthy():
            return self.logger.log(f"Node {self.node_id} gagal: Tegangan rendah ({self.power.voltage}V)")
        return self.logger.log(f"Node {self.node_id} beroperasi normal ({self.power.voltage}V)")


def main() -> None:
    ps = PowerSupply(12.4)
    logger = TelemetryLogger()
    node = TelecomNode("NODE-JKT-01", ps, logger)
    print(node.operate())


if __name__ == "__main__":
    main()
