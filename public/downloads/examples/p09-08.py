def rata_rata(data):
    """Kembalikan rata-rata, atau None bila kosong."""
    if not data:
        return None
    return sum(data) / len(data)

print(rata_rata([-80, -100, -90]))  # -90.0
print(rata_rata([]))  # None
