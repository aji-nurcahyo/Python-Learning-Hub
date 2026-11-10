# Modul D03: Web Data Collection & Ethical HTML Parsing

## 1. Etika & Hirarki Pengumpulan Data Web
Sebelum menulis *web scraper*, ikuti prinsip tanggung jawab rekayasa perangkat lunak:
1. **Utamakan Official API / Open Dataset:** Jika situs menyediakan endpoint JSON atau file CSV terbuka, gunakan jalur tersebut.
2. **Patuhi `robots.txt`:** Periksa aturan izin jalur memakai `urllib.robotparser.RobotFileParser`.
3. **Sertakan `User-Agent` Transparan & Rate Limit:** Jangan membanjiri server target; hormati batas laju permintaan (*rate limiting*) dan jangan pernah mencoba mengakali autentikasi, paywall, atau tantangan anti-bot.

---

## 2. Selector CSS yang Tangguh di BeautifulSoup4
Gunakan parser bawaan Python **`"html.parser"`** bersama `.select()` / `.select_one()`:
- Gunakan atribut semantik (`table#device-catalog`, `tr.device-row`, `td.col-price`) daripada jalur rapuh seperti `div > div:nth-child(4) > span`.
- **Pertahanan terhadap `None`:** Elemen opsional (misal `<span class="badge-note">`) bisa ada di satu baris dan absen di baris lain. Bungkus akses dalam helper aman:

```python
def text_or_default(el, default: str = "") -> str:
    return el.get_text(" ", strip=True) if el is not None else default
```

---

## 3. Normalisasi Teks Kotor & Uji Coba Offline
Nilai di halaman web jarang langsung bersih: `"Rp 4.250.000"` perlu dibersihkan menjadi `int(4250000)` sebelum masuk ke analisis Pandas atau Excel. Untuk pengujian CI/pytest yang cepat serta ramah jaringan, gunakan snapshot HTML lokal bersama `httpx.MockTransport`.

