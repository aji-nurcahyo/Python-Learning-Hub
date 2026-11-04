"""Modul Algoritma Pencarian & Pengurutan (search_sort.py)
Chapter 15: Searching & Sorting Algorithms — Python Learning Hub

Menyediakan implementasi algoritma klasik: Linear Search, Binary Search,
Bubble Sort, Selection Sort, Insertion Sort, dan Pemeringkatan Rekaman.
"""

from typing import Any, Callable


def linear_search(items: list[Any], target: Any) -> int | None:
    """Pencarian linier O(n). Mengembalikan indeks kecocokan pertama atau None."""
    for idx, val in enumerate(items):
        if val == target:
            return idx
    return None


def binary_search(sorted_items: list[Any], target: Any) -> tuple[int | None, int]:
    """Pencarian biner O(log n) pada koleksi terurut.
    Mengembalikan (indeks, jumlah_perbandingan).
    """
    left = 0
    right = len(sorted_items) - 1
    steps = 0

    while left <= right:
        steps += 1
        mid = (left + right) // 2
        mid_val = sorted_items[mid]

        if mid_val == target:
            return mid, steps
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    return None, steps


def bubble_sort(items: list[Any], reverse: bool = False) -> list[Any]:
    """Pengurutan Bubble Sort teroptimasi dengan flag deteksi pertukaran."""
    arr = list(items)
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            should_swap = (arr[j] < arr[j + 1]) if reverse else (arr[j] > arr[j + 1])
            if should_swap:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def selection_sort(items: list[Any], reverse: bool = False) -> list[Any]:
    """Pengurutan Selection Sort dengan pencarian nilai ekstrem."""
    arr = list(items)
    n = len(arr)
    for i in range(n):
        target_idx = i
        for j in range(i + 1, n):
            is_better = (arr[j] > arr[target_idx]) if reverse else (arr[j] < arr[target_idx])
            if is_better:
                target_idx = j
        if target_idx != i:
            arr[i], arr[target_idx] = arr[target_idx], arr[i]
    return arr


def insertion_sort(items: list[Any], reverse: bool = False) -> list[Any]:
    """Pengurutan Insertion Sort dengan pergeseran prefix terurut."""
    arr = list(items)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and ((arr[j] < key) if reverse else (arr[j] > key)):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def rank_records(
    records: list[dict[str, Any]],
    sort_key: str,
    reverse: bool = True
) -> list[dict[str, Any]]:
    """Pemeringkatan rekaman data menggunakan Timsort bawaan Python."""
    return sorted(records, key=lambda r: r.get(sort_key, 0), reverse=reverse)
