"""Contoh 19.6: Konvensi Naming Public, Protected (_), dan Name Mangling (__)
Python Learning Hub - Level 2: Intermediate Python
"""

class ServerConfig:
    def __init__(self, host: str, port: int, secret_token: str):
        self.host = host                   # Public: bebas diakses publik
        self._port = port                  # Protected: konvensi internal modul / subclass
        self.__secret_token = secret_token # Private: Python menerapkan Name Mangling

    def verifikasi_token(self, input_token: str) -> bool:
        return self.__secret_token == input_token

config = ServerConfig("gateway.itera.ac.id", 8080, "TOKEN_SUPER_RAHASIA_99")

print(f"Public host    : {config.host}")
print(f"Protected port : {config._port} (dapat diakses, namun konvensi menyarankan tidak diubah langsung)")

# Mengakses atribut private secara langsung memicu AttributeError
try:
    print(config.__secret_token)
except AttributeError:
    print("Atribut '__secret_token' tidak ditemukan secara langsung (terproteksi name mangling)!")

# Membuktikan name mangling: _ClassName__attribute
print(f"Akses via name mangling: {config._ServerConfig__secret_token}")
print(f"Verifikasi via method : {config.verifikasi_token('TOKEN_SUPER_RAHASIA_99')}")
