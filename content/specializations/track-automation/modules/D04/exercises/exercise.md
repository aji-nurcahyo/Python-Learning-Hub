# Latihan Mandiri D04 — Scheduling, Retry & Alerting

## Latihan 1: Backoff, Ledger Idempotency & Webhook
1. Buat fungsi retry memakai `sleep_fn` yang bisa diganti saat testing agar memverifikasi kelipatan jeda `[0.5, 1.0, 2.0]` dalam sekejap.
2. Buat kelas `IdempotentLedger` yang mencatat setiap `job_key` ke JSON di disk sehingga pemanggilan ganda di-skip otomatis.
3. Rakit payload JSON webhook alert dan uji pengirimannya ke endpoint tiruan dengan `httpx.MockTransport`.
4. Jalankan `pytest code/test_d04_orchestration.py`.

