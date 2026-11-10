# Kurikulum Resmi Specialization Tracks — Python Learning Hub
**Total Kurikulum Platform:** 30 Core Chapters + **25 Specialization Modules** = **55 Modul Pembelajaran**

Setiap Specialization Track terdiri atas 5 modul berjenjang (`X01`–`X05`) dan diakhiri oleh proyek **Capstone Terapan (`X05`)**.

---

## Track A — Data Science & Visualization (`track-data-science`, `A01`–`A05`)
- **`A01` — Numerical Computing with NumPy** (Intermediate, 4 jam): `ndarray`, vectorization, broadcasting, `axis` aggregation, aljabar linier & boolean masking.
- **`A02` — Data Manipulation with Pandas** (Intermediate, 5 jam): `Series` & `DataFrame`, `.loc`/`.iloc`, pembersihan `missing values`/duplikat, `groupby().agg()`, `pivot_table`, serta `pd.merge`.
- **`A03` — Exploratory Data Analysis (EDA)** (Intermediate, 5 jam): mean vs median, skewness, deteksi `outlier` IQR & Z-score, korelasi Pearson vs Spearman, dan `pd.crosstab`.
- **`A04` — Data Visualization with Matplotlib & Seaborn** (Intermediate, 5 jam): Object-Oriented API (`fig, ax`), `histplot`, `boxplot`, `scatterplot`, correlation `heatmap`, dan dashboard multi-panel 2x2.
- **`A05` — Capstone: End-to-End Analytics Report** (Advanced, 8 jam): validasi skema multi-CSV, enrichment join, kalkulasi SLA compliance & P95 latency, serta ekspor dashboard PNG + JSON/Markdown.

---

## Track B — Artificial Intelligence & Machine Learning (`track-ai-ml`, `B01`–`B05`)
- **`B01` — ML Foundations & Scikit-Learn Pipelines** (Intermediate, 4 jam): stratified split (`random_state=42`), `ColumnTransformer`, pencegahan `data leakage`, dan baseline `DummyClassifier`.
- **`B02` — Supervised Learning: Regression & Classification** (Intermediate, 5 jam): `LinearRegression` vs `Ridge`, `LogisticRegression`, `DecisionTreeClassifier`, `RandomForestClassifier`, dan benchmark model.
- **`B03` — Unsupervised Learning & Dimensionality Reduction** (Intermediate, 5 jam): `StandardScaler`, `KMeans`, evaluasi Elbow & Silhouette Score, `DBSCAN` noise `-1`, serta `PCA`.
- **`B04` — Model Evaluation, Cross-Validation & Tuning** (Intermediate, 5 jam): Confusion Matrix, Precision/Recall/F1/ROC-AUC pada data imbalanced, `StratifiedKFold`, `GridSearchCV` di atas `Pipeline`, dan threshold tuning.
- **`B05` — Capstone: Predictive Analytics Application** (Advanced, 8 jam): feature engineering domain, seleksi model via CV + holdout, serialisasi atomik `joblib` + uji paritas, dan batch inference scoring.

---

## Track C — Web Development & APIs (`track-web-api`, `C01`–`C05`)
- **`C01` — HTTP Client Utility & JSON Contract** (Intermediate, 4 jam): `httpx.Client` dengan timeout, query pagination, retry selektif status `5xx` (tidak retry `4xx`), validasi Pydantic, dan `MockTransport`.
- **`C02` — Modern REST API with FastAPI & Pydantic** (Intermediate, 5 jam): routing path/query, model terpisah Input/Out, CRUD `200/201/204/404/422`, OpenAPI inspection, dan `TestClient`.
- **`C03` — Database Persistence with SQLAlchemy ORM** (Intermediate, 5 jam): SQLAlchemy 2.0 `DeclarativeBase`/`Mapped`, CRUD `Session`, relasi `ForeignKey`, `Depends(get_db)`, dan HTTP `409 Conflict`.
- **`C04` — API Security, Config, Logging & Testing** (Intermediate, 5 jam): environment config, hashing PBKDF2-HMAC + salt, `hmac.compare_digest`, token HMAC bertanda tangan, Bearer guard `401`, dan logging middleware.
- **`C05` — Capstone: Production-Ready REST API** (Advanced, 8 jam): arsitektur 4-lapis (`Schema -> NodeRepository -> APIRouter -> create_app factory`), integration test menyeluruh di `tmp_path`, serta kesiapan `/health`.

---

## Track D — Automation & Scripting (`track-automation`, `D01`–`D05`)
- **`D01` — File System Automation with pathlib & shutil** (Intermediate, 4 jam): audit `rglob`, mode aman `dry_run=True`, deteksi duplikat chunked SHA-256, dan rotasi arsip `.zip`.
- **`D02` — Spreadsheet & PDF Document Automation** (Intermediate, 5 jam): `openpyxl` styling/format ribuan, formula hidup `=SUM`/`=SUMIF` lintas sheet, dan generator PDF `fpdf2`.
- **`D03` — Web Data Collection & Ethical HTML Parsing** (Intermediate, 5 jam): CSS selector `BeautifulSoup4` tahan `None`, normalisasi nominal Rupiah, pengecekan `robots.txt` (`RobotFileParser`), dan offline HTML fixtures.
- **`D04` — Workflow Scheduling, Retry & Alerting** (Intermediate, 5 jam): exponential backoff (`sleep_fn` injectable), state ledger JSON idempoten, webhook alert POST, serta CLI cron runner ber-exit code.
- **`D05` — Capstone: Autonomous Data Ingestion & Reporting Bot** (Advanced, 8 jam): siklus otomatis Collect -> Excel/PDF -> ZIP berotasi -> Webhook -> Commit Ledger (verified run ke-1 `EXECUTED`, run ke-2 `SKIPPED_IDEMPOTENT`).

---

## Track E — IoT, Signal Processing & Telecommunications (`track-iot-telecom`, `E01`–`E05`)
- **`E01` — Sensor Telemetry, Serial Framing & Checksums** (Intermediate, 4 jam): parser frame `$TELEM,...*XX` + XOR checksum, binary packing `struct.Struct('<Hff')`, smoothing EMA, dan loopback serial `pyserial`.
- **`E02` — IoT Protocols & MQTT Publish-Subscribe** (Intermediate, 5 jam): desain topik hierarkis, wildcard `+`/`#` (`topic_matches_sub`), QoS 0/1/2, Retained Message, LWT disconnect, dan deduplikasi QoS 1.
- **`E03` — Digital Signal Processing with SciPy & FFT** (Intermediate, 5 jam): teorema Nyquist, spektrum `scipy.fft.rfft`/`rfftfreq`, filter digital *Butterworth* `output='sos'` + `sosfiltfilt`, serta perbaikan SNR (dB).
- **`E04` — Wireless Network & Cellular Signal Analytics** (Intermediate, 5 jam): pemisahan metrik RSSI, RSRP, RSRQ, dan perbedaan krusial SNR vs SINR, deteksi blindspot vs *high interference*, FSPL link budget, dan peta sebar lat/lon.
- **`E05` — Capstone: IoT Monitoring & Signal Analytics System** (Advanced, 8 jam): integrasi MQTT routing -> Butterworth vibration denoising -> diagnostik multi-flag RF/thermal -> PNG dashboard + JSON/Markdown report.

