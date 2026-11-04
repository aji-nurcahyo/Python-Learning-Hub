"""Contoh 19.2: Definisi Class, Constructor __init__, Parameter self & Instance Method
Python Learning Hub - Level 2: Intermediate Python
"""

class Rectangle:
    """Blueprint representasi bentuk geometri persegi panjang."""

    def __init__(self, panjang: float, lebar: float):
        # self merujuk secara eksplisit pada instance object yang sedang dibuat
        self.panjang = float(panjang)
        self.lebar = float(lebar)

    def luas(self) -> float:
        """Menghitung luas persegi panjang."""
        return self.panjang * self.lebar

    def keliling(self) -> float:
        """Menghitung keliling persegi panjang."""
        return 2 * (self.panjang + self.lebar)

    def info(self) -> str:
        return f"Persegi Panjang {self.panjang:.1f} x {self.lebar:.1f} -> Luas: {self.luas():.1f}, Keliling: {self.keliling():.1f}"

# Instansiasi dua object berbeda dari class Rectangle
r1 = Rectangle(10.0, 5.0)
r2 = Rectangle(7.5, 3.0)

print(r1.info())
print(r2.info())
