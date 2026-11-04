"""Chapter 26 Example 02: Parameterized Testing Patterns
Python Learning Hub - Professional Python Engineering
"""

import unittest


def classify_signal_quality(rsrp_dbm: float) -> str:
    """Mengklasifikasikan kualitas sinyal berdasarkan standar 4G/5G LTE."""
    if rsrp_dbm >= -80.0:
        return "EXCELLENT"
    if rsrp_dbm >= -95.0:
        return "GOOD"
    if rsrp_dbm >= -110.0:
        return "FAIR"
    return "POOR"


class TestSignalClassification(unittest.TestCase):
    def test_parameterized_quality(self) -> None:
        """Menguji sekumpulan kasus (parameterized subtests) menggunakan subTest()."""
        test_cases = [
            (-70.0, "EXCELLENT"),
            (-80.0, "EXCELLENT"),
            (-85.0, "GOOD"),
            (-100.0, "FAIR"),
            (-115.0, "POOR"),
        ]
        for rsrp, expected in test_cases:
            with self.subTest(rsrp=rsrp, expected=expected):
                actual = classify_signal_quality(rsrp)
                self.assertEqual(actual, expected)


def main() -> None:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestSignalClassification)
    runner = unittest.TextTestRunner(verbosity=0)
    result = runner.run(suite)
    print(f"Uji Parameterized Selesai | Tests: {result.testsRun}, Sukses: {result.wasSuccessful()}")


if __name__ == "__main__":
    main()
