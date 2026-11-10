# Modul D04: Workflow Scheduling, Retry, Idempotency & Alerting

## 1. Realita Pekerjaan Terjadwal (*Cron* & *Task Scheduler*)
Skrip otomasi yang berjalan pukul 02.00 dini hari tanpa pengawasan manusia menghadapi tiga masalah utama:
1. Gangguan jaringan sesaat (*transient glitch*) ketika mengunduh data.
2. Risiko skrip tereksekusi ulang secara tak sengaja pada hari yang sama (**duplikasi**).
3. Kegagalan diam-diam tanpa pemberitahuan ke tim operasional (**silent failure**).

---

## 2. Exponential Backoff dengan Injectable `sleep_fn`
Alih-alih langsung menyerah pada kegagalan pertama atau mencoba ulang setiap 0 milidetik, **exponential backoff** menggandakan waktu jeda setiap gagal (`base_delay * (2 ** attempt)` -> `0.5s, 1.0s, 2.0s`). Dengan menyuntikkan parameter `sleep_fn=time.sleep`, unit test di `pytest` dapat menggantinya dengan fungsi pencatat `recorded_delays.append` sehingga pengujian selesai seketika tanpa menunggu detik asli.

---

## 3. Idempotency State Ledger
Operasi **idempoten** memastikan bahwa menjalankan tugas berkali-kali untuk kunci periode yang sama (`"report-2025-02-01"`) hanya memproduksi tepat satu eksekusi efek samping. Menyimpan himpunan `completed_keys` ke file ledger JSON sederhana mencegah pengiriman laporan atau tagihan ganda.

---

## 4. Webhook Alerting & CLI Exit Codes
Ketika percobaan retry habis, skrip harus:
- Mengirim ringkasan JSON (`severity`, `job_name`, `error`) via POST webhook (misalnya ke Slack, Discord, atau Telegram Bot Gateway).
- Keluar dengan **exit code `1`** (`0` untuk sukses/skip) sehingga sistem penjadwal (`cron`, GitHub Actions, Task Scheduler) langsung mencatat status kegagalan dengan benar.

