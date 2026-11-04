"""Chapter 26 Example 08: Testing Log Records with assertLogs
Python Learning Hub - Professional Python Engineering
"""

import logging
import unittest

logger = logging.getLogger("telecom.audit")


def perform_link_sync(link_id: str, is_active: bool) -> None:
    if is_active:
        logger.info(f"Link {link_id} berhasil disinkronisasi")
    else:
        logger.warning(f"Link {link_id} gagal sinkronisasi: status offline")


class TestLoggingOutput(unittest.TestCase):
    def test_sync_success_log(self) -> None:
        """Menguji apakah log level INFO tercatat saat sinkronisasi sukses."""
        with self.assertLogs("telecom.audit", level="INFO") as cm:
            perform_link_sync("LNK-99", is_active=True)

        self.assertEqual(len(cm.output), 1)
        self.assertIn("berhasil disinkronisasi", cm.output[0])

    def test_sync_failure_log(self) -> None:
        """Menguji apakah log level WARNING tercatat saat sinkronisasi gagal."""
        with self.assertLogs("telecom.audit", level="WARNING") as cm:
            perform_link_sync("LNK-99", is_active=False)

        self.assertEqual(len(cm.output), 1)
        self.assertIn("gagal sinkronisasi", cm.output[0])


def main() -> None:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestLoggingOutput)
    runner = unittest.TextTestRunner(verbosity=0)
    result = runner.run(suite)
    print(f"Uji AssertLogs Selesai | Tests: {result.testsRun}, Sukses: {result.wasSuccessful()}")


if __name__ == "__main__":
    main()

