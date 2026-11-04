"""Modul Dataset Transformation Toolkit (transform_toolkit.py)
Chapter 14: Comprehensions & Iterators — Python Learning Hub

Menyediakan utilitas transformasi, pemfilteran, perataan matriks, dan
agregasi memori efisien menggunakan list/dict/set comprehension serta generator.
"""

from typing import Any, Generator, Iterable


def filter_and_transform(
    records: list[dict[str, Any]],
    key: str,
    threshold: float,
    multiplier: float = 1.0
) -> list[dict[str, Any]]:
    """List comprehension: Memfilter rekaman dengan nilai atribut >= threshold dan menskala nilainya."""
    return [
        {**r, key: round(float(r[key]) * multiplier, 2)}
        for r in records
        if key in r and float(r[key]) >= threshold
    ]


def build_index_map(
    records: list[dict[str, Any]],
    id_key: str,
    val_key: str
) -> dict[Any, Any]:
    """Dictionary comprehension: Membangun peta indeks asosiatif id_key -> val_key."""
    return {r[id_key]: r[val_key] for r in records if id_key in r and val_key in r}


def extract_unique_categories(records: list[dict[str, Any]], key: str) -> set[str]:
    """Set comprehension: Mengekstrak nilai kategori unik yang dibersihkan dari spasi."""
    return {str(r[key]).strip().title() for r in records if key in r and str(r[key]).strip()}


def flatten_matrix(matrix: list[list[Any]]) -> list[Any]:
    """Nested list comprehension: Meratakan struktur matriks 2D menjadi list 1D."""
    return [item for row in matrix for item in row]


def stream_transformed_data(
    data: Iterable[float],
    threshold: float
) -> Generator[float, None, None]:
    """Generator expression: Streaming generator evaluasi lazy untuk nilai yang lolos filter."""
    return (round(x * 1.5, 2) for x in data if x >= threshold)

