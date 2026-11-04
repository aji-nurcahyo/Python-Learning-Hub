"""Chapter 28 Example 09: Pagination Handling in REST APIs
Python Learning Hub - Professional Python Engineering
"""

from typing import Any


class MockPaginatedApi:
    """Simulasi endpoint REST API dengan mekanisme pagination berbasis halaman (page-based)."""

    DATABASE = [
        {"id": 101, "site": "BTS-Lampung-01", "band": "1800MHz", "status": "active"},
        {"id": 102, "site": "BTS-Lampung-02", "band": "2100MHz", "status": "active"},
        {"id": 103, "site": "BTS-Lampung-03", "band": "900MHz", "status": "maintenance"},
        {"id": 104, "site": "BTS-Lampung-04", "band": "1800MHz", "status": "active"},
        {"id": 105, "site": "BTS-Lampung-05", "band": "2300MHz", "status": "active"},
    ]

    @classmethod
    def get_sites(cls, page: int = 1, page_size: int = 2) -> dict[str, Any]:
        start = (page - 1) * page_size
        end = start + page_size
        items = cls.DATABASE[start:end]
        total = len(cls.DATABASE)
        total_pages = (total + page_size - 1) // page_size

        return {
            "page": page,
            "page_size": page_size,
            "total_records": total,
            "total_pages": total_pages,
            "has_next": page < total_pages,
            "data": items,
        }


def fetch_all_paginated_records(page_size: int = 2) -> list[dict[str, Any]]:
    """Mengonsumsi seluruh halaman API pagination secara sistematis hingga has_next bernilai False."""
    all_items = []
    current_page = 1

    while True:
        response = MockPaginatedApi.get_sites(page=current_page, page_size=page_size)
        items = response["data"]
        all_items.extend(items)
        print(
            f"Diunduh Halaman {response['page']} / {response['total_pages']} "
            f"({len(items)} record): {[item['site'] for item in items]}"
        )

        if not response["has_next"]:
            break
        current_page += 1

    return all_items


def main() -> None:
    print("Membaca data terpaginasi dari endpoint REST API:")
    results = fetch_all_paginated_records(page_size=2)
    print(f"\nTotal record berhasil dikumpulkan secara lengkap: {len(results)} entri.")


if __name__ == "__main__":
    main()
