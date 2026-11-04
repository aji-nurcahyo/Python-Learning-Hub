"""Chapter 23 Example 03: Validated Properties with @property
Python Learning Hub - Professional Python Engineering
"""


class SignalTransmitter:
    """Perangkat pemancar dengan validasi daya transmisi via property setter."""

    def __init__(self, transmitter_id: str, power_dbm: float = 20.0) -> None:
        self.transmitter_id = transmitter_id
        self._power_dbm = 0.0
        self.power_dbm = power_dbm  # trigger property setter

    @property
    def power_dbm(self) -> float:
        return self._power_dbm

    @power_dbm.setter
    def power_dbm(self, value: float) -> None:
        if not (-30.0 <= value <= 50.0):
            raise ValueError(f"Daya {value} dBm di luar batas wajar (-30 hingga 50 dBm)")
        self._power_dbm = float(value)


def main() -> None:
    tx = SignalTransmitter("TX-BTS-01", 33.5)
    print(f"Transmitter : {tx.transmitter_id}")
    print(f"Daya Awal   : {tx.power_dbm} dBm")

    tx.power_dbm = 40.0
    print(f"Daya Baru   : {tx.power_dbm} dBm")

    try:
        tx.power_dbm = 99.0
    except ValueError as err:
        print(f"Ditolak     : {err}")


if __name__ == "__main__":
    main()
