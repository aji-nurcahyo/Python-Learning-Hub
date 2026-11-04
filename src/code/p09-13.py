def konversi_suhu(celsius):
    """Konversi suhu dari Celsius ke Fahrenheit.

    Args:
        celsius (float): Suhu dalam Celsius.
    Returns:
        float: Suhu dalam Fahrenheit.
    """
    return celsius * 9 / 5 + 32

print(konversi_suhu.__doc__)
