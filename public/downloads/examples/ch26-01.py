"""Chapter 26 Example 01: Test Fixtures with Setup & Teardown
Python Learning Hub - Professional Python Engineering
"""

import unittest


class DeviceDatabase:
    """Simulasi basis data memori lokal untuk unit test."""

    def __init__(self) -> None:
        self.devices: dict[str, str] = {}

    def insert(self, dev_id: str, model: str) -> None:
        self.devices[dev_id] = model

    def clear(self) -> None:
        self.devices.clear()


class TestDeviceDatabase(unittest.TestCase):
    def setUp(self) -> None:
        """Fixture setUp: Dijalankan sebelum setiap test case."""
        self.db = DeviceDatabase()
        self.db.insert("SW-01", "Cisco Catalyst")

    def tearDown(self) -> None:
        """Fixture tearDown: Dijalankan setelah setiap test case untuk pembersihan."""
        self.db.clear()

    def test_insert_and_retrieve(self) -> None:
        self.assertEqual(len(self.db.devices), 1)
        self.assertEqual(self.db.devices["SW-01"], "Cisco Catalyst")


def main() -> None:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestDeviceDatabase)
    runner = unittest.TextTestRunner(verbosity=0)
    result = runner.run(suite)
    print(f"Uji Fixture Selesai | Total Tests: {result.testsRun}, Errors: {len(result.errors)}, Failures: {len(result.failures)}")
    print("Status: SUKSES" if result.wasSuccessful() else "Status: GAGAL")


if __name__ == "__main__":
    main()
