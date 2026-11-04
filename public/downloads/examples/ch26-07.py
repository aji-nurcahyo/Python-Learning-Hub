"""Chapter 26 Example 07: Structured Logging Configuration
Python Learning Hub - Professional Python Engineering
"""

import io
import logging


def configure_demo_logger() -> tuple[logging.Logger, io.StringIO]:
    """Mengonfigurasi logger terstruktur yang mengalirkan log ke stream memori."""
    log_stream = io.StringIO()
    handler = logging.StreamHandler(log_stream)
    formatter = logging.Formatter("[%(levelname)s] [%(name)s] %(message)s")
    handler.setFormatter(formatter)

    logger = logging.getLogger("telecom.core")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    logger.addHandler(handler)
    logger.propagate = False

    return logger, log_stream


def main() -> None:
    logger, stream = configure_demo_logger()

    logger.debug("Pesan debug: tidak akan tercetak karena level INFO")
    logger.info("Inisialisasi subsistem RF selesai")
    logger.warning("Suhu transiver mencapai ambang batas 65 C")
    logger.error("Koneksi radio terputus pada sektor B")

    output_lines = stream.getvalue().strip().split("\n")
    print("Log Terstruktur yang Dihasilkan:")
    for line in output_lines:
        print(f" {line}")


if __name__ == "__main__":
    main()
