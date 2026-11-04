"""Chapter 27 Example 06: Concurrent Tasks with asyncio.gather
Python Learning Hub - Professional Python Engineering
"""

import asyncio


async def poll_sensor(sensor_id: str, delay: float) -> dict[str, str | float]:
    """Coroutine pemantau sensor yang berjalan konkuren secara non-blocking."""
    await asyncio.sleep(delay)
    return {"id": sensor_id, "reading": 25.4 + len(sensor_id)}


async def async_main() -> None:
    print("Memulai polling 3 sensor konkuren dengan asyncio.gather()...")
    # asyncio.gather menjalankan coroutine secara konkuren dan menjaga urutan kembalian
    results = await asyncio.gather(
        poll_sensor("SENS-A", 0.02),
        poll_sensor("SENS-B", 0.01),
        poll_sensor("SENS-C", 0.03),
    )

    print("Hasil Seluruh Sensor Berhasil Dikumpulkan:")
    for res in results:
        print(f" * Sensor {res['id']}: Nilai = {res['reading']}")


def main() -> None:
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

