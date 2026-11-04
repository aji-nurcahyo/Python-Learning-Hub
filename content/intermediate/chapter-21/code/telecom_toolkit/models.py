"""Modul Models: Entitas domain stasiun pemancar telekomunikasi.
Python Learning Hub - Chapter 21: Packages, Environments & Testing
"""

class BaseStation:
    """Class representasi stasiun pemancar BTS."""

    def __init__(self, station_id: str, site_name: str, tx_power_dbm: float, antenna_gain_dbi: float):
        self.station_id = station_id
        self.site_name = site_name
        self.tx_power_dbm = tx_power_dbm
        self.antenna_gain_dbi = float(antenna_gain_dbi)

    @property
    def tx_power_dbm(self) -> float:
        return self._tx_power_dbm

    @tx_power_dbm.setter
    def tx_power_dbm(self, value: float) -> None:
        val = float(value)
        if not (-10.0 <= val <= 60.0):
            raise ValueError(f"Daya transmisi {val} dBm di luar batas operasional [-10 s/d 60 dBm]!")
        self._tx_power_dbm = val

    @property
    def eirp_dbm(self) -> float:
        """Effective Isotropic Radiated Power: EIRP (dBm) = Tx Power + Antenna Gain."""
        return self._tx_power_dbm + self.antenna_gain_dbi

    def __str__(self) -> str:
        return f"{self.station_id} ({self.site_name}) - EIRP: {self.eirp_dbm:.1f} dBm"

    def __repr__(self) -> str:
        return f"BaseStation('{self.station_id}', '{self.site_name}', {self._tx_power_dbm}, {self.antenna_gain_dbi})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BaseStation):
            return NotImplemented
        return self.station_id == other.station_id

