"""Chapter 26 Example 06: Test Branch Coverage Concepts
Python Learning Hub - Professional Python Engineering
"""

import unittest


def route_packet(priority: int, has_congestion: bool) -> str:
    """Fungsi dengan 3 jalur cabang eksekusi (branch)."""
    if priority >= 10:
        return "EXPRESS_QUEUE"
    elif has_congestion:
        return "BUFFER_QUEUE"
    else:
        return "NORMAL_QUEUE"


class TestBranchCoverage(unittest.TestCase):
    def test_express_branch(self) -> None:
        self.assertEqual(route_packet(10, False), "EXPRESS_QUEUE")

    def test_congestion_branch(self) -> None:
        self.assertEqual(route_packet(5, True), "BUFFER_QUEUE")

    def test_normal_branch(self) -> None:
        self.assertEqual(route_packet(3, False), "NORMAL_QUEUE")


def main() -> None:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestBranchCoverage)
    runner = unittest.TextTestRunner(verbosity=0)
    result = runner.run(suite)
    print(f"Uji 100% Branch Coverage Selesai | Tests: {result.testsRun}, Sukses: {result.wasSuccessful()}")


if __name__ == "__main__":
    main()

