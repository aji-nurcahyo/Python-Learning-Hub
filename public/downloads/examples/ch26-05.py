"""Chapter 26 Example 05: Temporary Directory Isolation
Python Learning Hub - Professional Python Engineering
"""

import os
import tempfile
import unittest


class ConfigFileManager:
    """Menulis dan membaca berkas konfigurasi node."""

    def __init__(self, directory: str) -> None:
        self.directory = directory

    def write_config(self, filename: str, content: str) -> str:
        filepath = os.path.join(self.directory, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return filepath


class TestConfigFileManager(unittest.TestCase):
    def test_isolated_temp_file(self) -> None:
        """Menggunakan tempfile.TemporaryDirectory agar tidak meninggalkan sisa berkas."""
        with tempfile.TemporaryDirectory() as temp_dir:
            mgr = ConfigFileManager(temp_dir)
            cfg_path = mgr.write_config("node.cfg", "PORT=9000\nDEBUG=TRUE")

            self.assertTrue(os.path.exists(cfg_path))
            with open(cfg_path, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertIn("PORT=9000", content)


def main() -> None:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestConfigFileManager)
    runner = unittest.TextTestRunner(verbosity=0)
    result = runner.run(suite)
    print(f"Uji Temp Directory Selesai | Tests: {result.testsRun}, Sukses: {result.wasSuccessful()}")


if __name__ == "__main__":
    main()
