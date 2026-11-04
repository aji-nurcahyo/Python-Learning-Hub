"""Modul Exceptions: Hierarki custom exception untuk Inventory Management System.
Python Learning Hub - Chapter 22: Intermediate Capstone Project
"""

class InventoryException(Exception):
    """Base exception untuk seluruh domain sistem inventaris."""
    pass

class DeviceNotFoundError(InventoryException):
    """Dilempar ketika ID perangkat tidak ditemukan dalam repositori."""
    pass

class DuplicateDeviceError(InventoryException):
    """Dilempar saat registrasi ID perangkat yang sudah ada dalam repositori."""
    pass

class ValidationError(InventoryException):
    """Dilempar saat data input tidak memenuhi kriteria integritas."""
    pass

class StorageError(InventoryException):
    """Dilempar saat terjadi kegagalan I/O pada persistensi berkas data."""
    pass

