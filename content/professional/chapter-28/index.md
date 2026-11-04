# Chapter 28: Networking & API Integration
## HTTP Clients, REST Architecture, Authentication & Resilient APIs

Selamat datang di **Chapter 28: Networking & API Integration** pada tingkat **Level 3: Professional Python Engineering** di **Python Learning Hub**.

Pada sistem perangkat lunak modern, aplikasi jarang berdiri sendiri sebagai pulau terisolasi. Aplikasi komersial, pipeline data telekomunikasi, dan layanan backend terdistribusi harus saling berkomunikasi melintasi batas jaringan melalui **Application Programming Interfaces (APIs)** berbasis protokol **Hypertext Transfer Protocol (HTTP)**.

Bab ini membahas prinsip rekayasa di balik integrasi jaringan dan konsumsi REST API. Anda akan mempelajari arsitektur klien-server, semantik metode HTTP, struktur payload JSON, autentikasi berbasis Bearer token, pertahanan terhadap gangguan jaringan dengan *exponential backoff retry*, penanganan dataset terpaginasi (*pagination*), serta praktik keamanan penting dalam menyamarkan kredensial pada pencatatan log sistem.

---

## 1. Arsitektur Client-Server & Protokol HTTP

Protokol HTTP adalah protokol lapisan aplikasi (*application layer*) yang beroperasi di atas transport TCP/IP. Pola komunikasinya berbasis permintaan-respons (*request-response model*):

- **Client:** Menginisiasi koneksi TCP, mengirim pesan HTTP request yang berisi metode, alamat URL, header metadata, dan opsional bodi data (*payload*).
- **Server:** Menerima koneksi, memproses logika bisnis atau kueri basis data, dan mengembalikan pesan HTTP response yang berisi status code, response headers, dan bodi konten.
- **Sifat Stateless:** Setiap pasangan request-response berdiri sendiri tanpa keterikatan status pada sesi sebelumnya di tingkat protokol.

---

## 2. Anatomi URL & Query Parameters

Uniform Resource Locator (URL) adalah alamat standar untuk mengidentifikasi resource di jaringan internet.

Struktur standar URL:
```
https://api.telekom.id:443/v1/sensors/search?status=ACTIVE&limit=10#overview
│       │                 │                │                       │
scheme  host:port         path             query parameters        fragment
```

### Mengelola Query Parameters
Karakter khusus seperti spasi, tanda tanya, atau karakter non-ASCII harus di-encode menggunakan mekanisme *percent-encoding*. Modul standar Python `urllib.parse` menyediakan fungsi `urlencode`:

```python
from urllib.parse import urlencode

params = {"city": "Bandar Lampung", "type": "4G", "limit": 20}
query_string = urlencode(params)
# Menghasilkan: 'city=Bandar+Lampung&type=4G&limit=20'
```

---

## 3. Semantik Metode HTTP & REST Architecture

**Representational State Transfer (REST)** adalah gaya arsitektur yang memanfaatkan metode standar HTTP untuk mengekspresikan tindakan terhadap suatu sumber daya (*resource*):

| Metode HTTP | Karakteristik Semantik | Idempoten? | Aman (Safe)? | Kasus Penggunaan Umum |
| :--- | :--- | :---: | :---: | :--- |
| **GET** | Mengambil representasi resource | Ya | Ya | Membaca data tanpa mengubah status sistem |
| **POST** | Membuat resource baru di server | Tidak | Tidak | Mengirim payload baru atau submit formulir |
| **PUT** | Mengganti resource yang ada secara utuh | Ya | Tidak | Memperbarui objek secara keseluruhan |
| **PATCH** | Memperbarui sebagian atribut resource | Bisa | Tidak | Mengubah status aktif atau nilai metrik tertentu |
| **DELETE** | Menghapus resource dari server | Ya | Tidak | Menghapus entri data dari sistem |

*Catatan:* **Idempoten** berarti pemanggilan operasi beberapa kali berturut-turut menghasilkan kondisi akhir sistem yang sama persis seperti pemanggilan sekali. **Aman (Safe)** berarti pemanggilan tidak mengubah representasi data sama sekali di server.

---

## 4. Format Data JSON & Deserialisasi Defensif

Dalam REST API modern, **JavaScript Object Notation (JSON)** adalah format pertukaran data standar karena ringkas, mudah dibaca manusia, dan didukung secara universal oleh hampir semua bahasa pemrograman.

### Parsing Defensif (*Defensive JSON Parsing*)
Jangan pernah mengasumsikan bahwa API pihak ketiga selalu mengembalikan semua kunci (*keys*) yang Anda harapkan. Mengakses kamus data secara langsung (`data["metrics"]["temp"]`) dapat memicu `KeyError` jika respons tidak lengkap.

Gunakan selalu metode `.get()` dengan nilai bawaan (*default value*):
```python
# Pendekatan defensif yang aman dari crash
voltage = payload.get("telemetry", {}).get("voltage", 0.0)
status = payload.get("status", "UNKNOWN")
```

---

## 5. Klasifikasi Kode Status HTTP (HTTP Status Codes)

Server mengembalikan kode status 3-digit untuk memberitahukan hasil pemrosesan kepada klien:

1. **2xx — Sukses:**
   - `200 OK`: Permintaan berhasil dan data disertakan dalam bodi.
   - `201 Created`: Resource baru berhasil dibuat (umum pada POST).
   - `204 No Content`: Permintaan sukses, namun tidak ada konten yang perlu dikembalikan (umum pada DELETE).
2. **4xx — Kesalahan Klien (Client Errors):**
   - `400 Bad Request`: Sintaks request atau payload salah.
   - `401 Unauthorized`: Kredensial autentikasi hilang atau token tidak valid.
   - `403 Forbidden`: Server memahami identitas klien, tetapi menolak akses izin (*permission denied*).
   - `404 Not Found`: Endpoint atau resource URL tidak ditemukan.
   - `429 Too Many Requests`: Klien melebihi kuota batas frekuensi (*rate limit*).
3. **5xx — Kesalahan Server (Server Errors):**
   - `500 Internal Server Error`: Terjadi kegagalan logika tak terduga pada server.
   - `502 Bad Gateway`: Server perantara/proxy menerima respons tidak valid dari upstream.
   - `503 Service Unavailable`: Server sedang sibuk sementara atau dalam masa perawatan (*maintenance*).

---

## 6. Pertahanan Jaringan: Timeouts & Exponential Backoff

### Wajib: Konfigurasi Timeout
Jika klien HTTP tidak menetapkan batas waktu tunggu (*timeout*), thread atau coroutine dapat menggantung selamanya ketika router atau server tujuan mengalami kegagalan transmisi tanpa memutus koneksi soket.

```python
# Pola penentuan timeout
response = client.get(url, timeout=5.0)  # Batas maksimal tunggu 5 detik
```

### Exponential Backoff Retry Strategy
Ketika berhadapan dengan kegagalan sementara (*transient errors*) seperti HTTP 503 atau 429, klien tidak boleh langsung mengirim request ulang secara beruntun (*spamming*). Hal tersebut dapat memicu fenomena *thundering herd* yang melumpuhkan server.

Gunakan algoritma **Exponential Backoff**:
- Setiap kegagalan, waktu tunggu digandakan: $delay = initial \times factor^{(attempt - 1)}$.
- Batasi jumlah maksimum percobaan (*max retries*).

---

## 7. Autentikasi Aman & Penyamaran Kredensial Log

Berdasarkan RFC 6750, standar autentikasi REST API modern menggunakan format **Bearer Token** pada header HTTP:
```
Authorization: Bearer <API_SECRET_TOKEN>
```

### Prinsip Keamanan Kredensial:
1. **Never Hardcode Secrets:** Jangan pernah menuliskan token atau password di dalam file `.py` yang disimpan di sistem kontrol versi (Git).
2. **Environment Variables:** Baca kredensial dari lingkungan sistem operasi menggunakan `os.environ.get("API_SECRET_KEY")`.
3. **Log Sanitization:** Saat mencatat permintaan HTTP ke berkas log audit produksi, samarkan isi token:
```python
def mask_token(token: str) -> str:
    if len(token) > 10:
        return f"{token[:4]}****{token[-4:]}"
    return "****"
```

---

## 8. Pola Paginasi REST API

Saat endpoint memiliki ribuan entri, server membagi data ke dalam halaman-halaman (*pagination*):
1. **Page-Based Pagination:** Menggunakan parameter `page` dan `limit` (misal `?page=2&limit=50`).
2. **Cursor-Based Pagination:** Menggunakan penunjuk posisi data terakhir (`?cursor=xyz`).

Klien yang andal mengimplementasikan loop traversal otomatis hingga flag penanda halaman berikutnya (`has_next`) bernilai `False`.

---

## 9. Ringkasan Materi & Referensi Lanjutan

- Gunakan metode HTTP sesuai semantik operasinya (GET untuk baca, POST untuk buat, PUT/PATCH untuk ubah, DELETE untuk hapus).
- Perlakukan seluruh respon jaringan secara defensif dengan validasi struktur data.
- Lindungi stabilitas sistem dengan timeout eksplisit dan strategi retry backoff.
- Jaga kerahasiaan token autentikasi dengan membaca dari environment variables dan menyamarkan log.
- **Referensi Resmi:**
  - [Python Docs: `urllib.request` & `urllib.parse`](https://docs.python.org/3/library/urllib.request.html)
  - [Requests: HTTP for Humans](https://requests.readthedocs.io/)
  - [HTTPX: Next Generation HTTP Client](https://www.python-httpx.org/)
  - [RFC 7231: Hypertext Transfer Protocol (HTTP/1.1) Semantics and Content](https://datatracker.ietf.org/doc/html/rfc7231)
