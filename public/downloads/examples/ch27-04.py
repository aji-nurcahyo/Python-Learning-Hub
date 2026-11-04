"""Chapter 27 Example 04: ProcessPoolExecutor for CPU-bound Tasks
Python Learning Hub - Professional Python Engineering
"""

from concurrent.futures import ProcessPoolExecutor


def compute_crc_checksum(data_block: int) -> int:
    """Mensimulasikan kalkulasi CPU-bound intensif (checksum) yang bypass GIL."""
    acc = 0
    for i in range(1, 20000):
        acc = (acc + i * data_block) % 65535
    return acc


def main() -> None:
    data_blocks = [101, 102, 103, 104]
    print(f"Mengeksekusi kalkulasi CPU paralel untuk {len(data_blocks)} blok data...")

    # ProcessPoolExecutor membuat proses terpisah dengan memori dan GIL independen
    with ProcessPoolExecutor(max_workers=2) as executor:
        checksums = list(executor.map(compute_crc_checksum, data_blocks))

    for block, cs in zip(data_blocks, checksums):
        print(f" -> Blok {block}: Checksum CRC = 0x{cs:04X}")


# Guard if __name__ == '__main__': wajib untuk multiprocessing di Windows
if __name__ == "__main__":
    main()

