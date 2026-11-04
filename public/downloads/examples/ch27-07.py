"""Chapter 27 Example 07: asyncio Timeout & Task Cancellation
Python Learning Hub - Professional Python Engineering
"""

import asyncio


async def slow_network_handshake() -> str:
    """Coroutine yang membutuhkan waktu lama melebihi batas toleransi timeout."""
    try:
        await asyncio.sleep(0.5)
        return "HANDSHAKE_COMPLETED"
    except asyncio.CancelledError:
        print("[CANCELLED] Task dibatalkan sebelum selesai!")
        raise


async def async_main() -> None:
    print("Mencoba koneksi dengan batas timeout 0.05 detik...")
    try:
        # Menggunakan asyncio.wait_for untuk membatasi durasi eksekusi coroutine
        await asyncio.wait_for(slow_network_handshake(), timeout=0.05)
    except TimeoutError:
        print("[TIMEOUT] Batas waktu 0.05s terlampaui. Operasi aman dibatalkan.")


def main() -> None:
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

