# Tugas Terstruktur D04: Resilient Scheduled Automation & Alert Dispatcher

## Instruksi Implementasi (`tugas.py`)
1. `run_with_backoff(op, max_attempts=3, base_delay=0.5, sleep_fn=time.sleep)`: ulangi operasi saat error hingga `max_attempts`, hitung `base_delay * (2 ** attempt)`, lalu lempar exception terakhir jika tetap gagal.
2. Kelas `JobLedger(state_path: Path)`: sediakan `has_completed(job_key: str) -> bool` dan `mark_completed(job_key: str) -> None` persisten dalam JSON.
3. `dispatch_webhook_alert(client: httpx.Client, url: str, job_name: str, detail: str) -> int`: kirim POST JSON dengan status `raise_for_status()`.
4. Tambahkan entry point `argparse` yang mengembalikan integer exit code `0` atau `1`.

## Rubrik Penilaian (Total 100 Poin)
- Exponential Backoff & Injectable Sleep (25%)
- Desain Idempotent JobLedger Persisten (30%)
- Webhook Alert Formatter & HTTP Client (25%)
- CLI Design & Unit Testing Pytest (20%)

