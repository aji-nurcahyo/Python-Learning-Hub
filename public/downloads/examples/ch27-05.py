"""Chapter 27 Example 05: Basic asyncio Coroutine & Event Loop
Python Learning Hub - Professional Python Engineering
"""

import asyncio


async def fetch_remote_banner(service_name: str) -> str:
    """Coroutine dasar: menggunakan await asyncio.sleep() untuk non-blocking I/O."""
    print(f"[ASYNC START] Menghubungi layanan {service_name}...")
    await asyncio.sleep(0.02)  # Menyerahkan kendali kembali ke event loop
    print(f"[ASYNC DONE] Respons diterima dari {service_name}")
    return f"BANNER_{service_name.upper()}_v1.0"


async def async_main() -> None:
    print("Memulai eksekusi coroutine tunggal di dalam event loop...")
    result = await fetch_remote_banner("telecom-gateway")
    print(f"Hasil Coroutine: {result}")


def main() -> None:
    # asyncio.run mengelola siklus hidup event loop secara otomatis
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

