# 🔄 ETL Pipeline — Fashion Studio Data

> **Final Project** — Dicoding "Belajar Fundamental Pemrosesan Data"  
> ⭐ **Rated 5 Stars (Advanced Level)**

---

## 📌 Project Overview

This project builds a **modular ETL (Extract, Transform, Load) Pipeline** that scrapes fashion product data from [Fashion Studio Dicoding](https://fashion-studio.dicoding.dev/), cleans and transforms the data, then loads it into three different data repositories simultaneously.

The pipeline collects **1,000 raw product records** across 50 pages, processes them into clean, analysis-ready data, and stores the results in CSV, Google Sheets, and PostgreSQL.

---

## 🏗️ Project Structure

```
submission-pemrosesan-data/
│
├── utils/
│   ├── extract.py          # Web scraping logic (Extract stage)
│   ├── transform.py        # Data cleaning & transformation (Transform stage)
│   └── load.py             # Data loading to 3 repositories (Load stage)
│
├── tests/
│   ├── test_extract.py     # Unit tests for Extract
│   ├── test_transform.py   # Unit tests for Transform
│   └── test_load.py        # Unit tests for Load
│
├── main.py                 # Pipeline orchestrator (run all stages)
├── requirements.txt        # Project dependencies
├── products.csv            # Output: cleaned data in CSV format
├── credentials.json        # Google Sheets API service account (not tracked in git)
└── README.md
```

---

## ⚙️ ETL Pipeline Stages

### 1. 📥 Extract (`utils/extract.py`)
- Scrapes **50 pages** from [fashion-studio.dicoding.dev](https://fashion-studio.dicoding.dev/)
- Collects **1,000 raw product records**
- Extracted fields:

| Field | Description |
|---|---|
| `Title` | Product name |
| `Price` | Price in USD |
| `Rating` | Customer rating |
| `Colors` | Number of available colors |
| `Size` | Available size |
| `Gender` | Target gender |
| `timestamp` | Extraction timestamp |

- Includes **error handling** per page (continues on failure, logs warning)

### 2. 🔧 Transform (`utils/transform.py`)
- Removes duplicates and null values
- Removes invalid data (e.g., `"Unknown Product"`, `"Invalid Rating"`)
- Converts `Price` from USD → **IDR (×Rp16,000)**
- Cleans `Rating` → `float` (e.g., `"4.8 / 5"` → `4.8`)
- Cleans `Colors` → `int` (e.g., `"3 Colors"` → `3`)
- Cleans `Size` → string without prefix (e.g., `"Size: M"` → `"M"`)
- Cleans `Gender` → string without prefix (e.g., `"Gender: Men"` → `"Men"`)

### 3. 📤 Load (`utils/load.py`)
Data is saved to **3 repositories simultaneously**:

| Repository | Function | Details |
|---|---|---|
| **CSV** | `save_to_csv()` | Saved as `products.csv` |
| **Google Sheets** | `save_to_google_sheets()` | Via Google Sheets API (service account) |
| **PostgreSQL** | `save_to_postgres()` | Via SQLAlchemy + Neon.tech |

---

## ✅ Unit Testing

All unit tests are in the `tests/` folder and cover all ETL stages.

| Test File | Coverage |
|---|---|
| `test_extract.py` | Tests successful scrape & error handling |
| `test_transform.py` | Tests data cleaning logic |
| `test_load.py` | Tests CSV, Google Sheets, and PostgreSQL save functions |

**Test Coverage: 80–100% (Advanced)**

---

## 📈 Key Results

- ✅ **All 3 criteria met at Advanced level**
- ⭐ **Score: 5/5 Stars**
- **Criteria 1 — Modular ETL Pipeline:** Advanced
- **Criteria 2 — Data Repositories:** Advanced (CSV + Google Sheets + PostgreSQL)
- **Criteria 3 — Unit Testing:** Advanced (80–100% coverage)

---

## 🛠️ Tech Stack

| Library | Usage |
|---|---|
| `requests` + `beautifulsoup4` | Web scraping |
| `pandas` | Data manipulation |
| `gspread` + `gspread_dataframe` | Google Sheets integration |
| `SQLAlchemy` + `psycopg2` | PostgreSQL connection |
| `google-auth` | Google API authentication |
| `pytest` + `pytest-cov` | Unit testing & coverage |

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/etl-pipeline-fashion-studio.git
cd etl-pipeline-fashion-studio
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up credentials
- Add your `credentials.json` (Google Sheets API service account) to the root directory
- Update the PostgreSQL `DB_URL` in `main.py` with your own connection string

### 4. Run the pipeline
```bash
python main.py
```

### 5. Run unit tests
```bash
# Run all tests
python -m pytest tests/

# Run with coverage report
python -m pytest --cov=utils tests/
```

---

## 📊 Output

- **CSV:** `products.csv` (locally)
- **Google Sheets:** [View Output Sheet](https://docs.google.com/spreadsheets/d/1XoDl_eJVDGjv1sXEgtE7T7yYFBwvXMtcoxfeZt7uMcs/edit?usp=sharing)
- **PostgreSQL:** Table `tabel_produk_etl` on Neon.tech

---

## 🔒 Security Note

`credentials.json` contains sensitive Google API credentials and is **excluded from this repository** via `.gitignore`. To use Google Sheets integration, provide your own service account credentials file.
