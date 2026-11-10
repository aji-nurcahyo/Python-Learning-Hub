# Modul C04: API Security, Config, Logging & Automated Testing

## 1. Memisahkan Konfigurasi dari Kode (Twelve-Factor Config)
Menaruh API key, password database, atau secret signing di dalam kode sumber (Git) merupakan celah keamanan kritis. Gunakan `os.environ` atau pemetaan dictionary environment injeksi yang dibungkus oleh model konfigurasi Pydantic/dataclass agar mudah diuji dan diubah per lingkungan (`dev`, `staging`, `prod`).

---

## 2. Password Hashing Kriptografis yang Benar
Jangan pernah menyimpan kata sandi sebagai plain-text atau `SHA-256` polos:
- **Gunakan Salt Unik:** hasilkan 16 byte acak memakai `secrets.token_hex(16)` per pengguna.
- **Gunakan Key Stretching:** gunakan `hashlib.pbkdf2_hmac("sha256", raw.encode(), salt.encode(), 100_000)` atau `scrypt` agar tebakan brute-force menjadi lambat dan mahal.
- **Verifikasi Anti Timing-Attack:** selalu bandingkan hash memakai `hmac.compare_digest(expected, actual)` bukan `==`.

---

## 3. Token Akses Bertanda Tangan & `Depends()` Guard
Untuk autentikasi stateless antar layanan:
1. Payload JSON (`{"sub": "engineer", "exp": timestamp}`) di-encode base64url.
2. Tanda tangan dibuat memakai `hmac.new(secret_bytes, payload_b64.encode(), hashlib.sha256)`.
3. Dependency FastAPI memeriksa header `Authorization: Bearer <token>`, memverifikasi signature dan waktu `exp`, lalu melempar `HTTPException(status_code=401)` bila tidak sah.

---

## 4. Structured Logging Middleware
Middleware HTTP di FastAPI (`@app.middleware("http")`) mencegat setiap request sebelum masuk ke route dan setelah respons terbentuk, memungkinkan pencatatan `method`, `path`, `status_code`, serta durasi eksekusi secara konsisten tanpa mengotori kode bisnis tiap endpoint.

