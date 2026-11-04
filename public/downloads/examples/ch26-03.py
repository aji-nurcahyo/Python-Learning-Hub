"""Chapter 26 Example 03: Exception Testing with assertRaises
Python Learning Hub - Professional Python Engineering
"""

import unittest


def parse_ip_address(ip_str: str) -> list[int]:
    """Mengurai alamat IPv4 menjadi 4 octet integer."""
    parts = ip_str.split(".")
    if len(parts) != 4:
        raise ValueError("Format IP tidak valid: harus memiliki tepat 4 oktet")

    octets: list[int] = []
    for p in parts:
        val = int(p)
        if not (0 <= val <= 255):
            raise ValueError(f"Oktet {val} di luar rentang valid 0-255")
        octets.append(val)
    return octets


class TestIpParsing(unittest.TestCase):
    def test_valid_ip(self) -> None:
        self.assertEqual(parse_ip_address("192.168.1.1"), [192, 168, 1, 1])

    def test_invalid_length_raises(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            parse_ip_address("192.168.1")
        self.assertIn("tepat 4 oktet", str(ctx.exception))

    def test_invalid_range_raises(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            parse_ip_address("192.168.1.300")
        self.assertIn("di luar rentang", str(ctx.exception))


def main() -> None:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestIpParsing)
    runner = unittest.TextTestRunner(verbosity=0)
    result = runner.run(suite)
    print(f"Uji Exception Selesai | Tests: {result.testsRun}, Sukses: {result.wasSuccessful()}")


if __name__ == "__main__":
    main()

