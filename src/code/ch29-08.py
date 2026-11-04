"""Chapter 29 Example 08: Programmatic Automated Test Execution
Python Learning Hub - Professional Python Engineering
"""

import unittest


class SampleUnitTests(unittest.TestCase):
    def test_checksum_parity(self) -> None:
        self.assertEqual(len("TELECOM_HEADER"), 14)

    def test_port_validation(self) -> None:
        port = 8080
        self.assertTrue(1024 <= port <= 65535)

    def test_failure_handling(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            _ = 100 / 0


def run_programmatic_suite() -> dict[str, int | bool]:
    """Menjalankan test suite secara programatis di dalam pipeline CI."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(SampleUnitTests)

    # Gunakan TextTestRunner tanpa output verbose agar hasil deterministik
    import io
    stream = io.StringIO()
    runner = unittest.TextTestRunner(stream=stream, verbosity=0)
    result = runner.run(suite)

    return {
        "tests_run": result.testsRun,
        "failures": len(result.failures),
        "errors": len(result.errors),
        "is_successful": result.wasSuccessful(),
    }


def main() -> None:
    print("Mengeksekusi Automated Unit Test Suite secara Programatis:")
    summary = run_programmatic_suite()

    print(f" -> Total Pengujian Dijalankan : {summary['tests_run']}")
    print(f" -> Jumlah Kegagalan (Failures): {summary['failures']}")
    print(f" -> Jumlah Kesalahan (Errors)  : {summary['errors']}")
    print(f" -> Status Kelulusan Pipeline  : {'SUKSES (PASSED)' if summary['is_successful'] else 'GAGAL (FAILED)'}")


if __name__ == "__main__":
    main()

