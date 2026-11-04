"""Wadah Generik Tipe Aman (Chapter 25)
Python Learning Hub - Professional Python Engineering
"""

from typing import Generic, TypeVar

T = TypeVar("T")


class EntityRepository(Generic[T]):
    """Repositori generik tipe aman yang mengelola koleksi elemen tipe T."""

    def __init__(self) -> None:
        self._storage: list[T] = []

    def save(self, item: T) -> None:
        self._storage.append(item)

    def get_all(self) -> list[T]:
        return list(self._storage)

    def count(self) -> int:
        return len(self._storage)

    def clear(self) -> None:
        self._storage.clear()

