from utils.extract import scrape_main
from utils.transform import clean_data
from utils.load import save_to_csv, save_to_google_sheets, save_to_postgres
import os

def run_pipeline():
    print("--- Memulai ETL Pipeline ---")
    
    print("Sedang mengambil data dari website (Extract)...")
    raw_data = scrape_main()
    
    if raw_data is not None and not raw_data.empty:
        print("Sedang membersihkan data (Transform)...")
        clean_df = clean_data(raw_data)
        
        if clean_df is not None:
            print("Sedang menyimpan data (Load)...")
            
            # save to CSV
            save_to_csv(clean_df, "products.csv")
            
            # save to Google Sheets
            save_to_google_sheets(clean_df, "products_data_etl")
            
            # save to PostgreSQL Neon.tech
            DB_URL = os.environ.get("DATABASE_URL", "")
            save_to_postgres(clean_df, DB_URL, "tabel_produk_etl")
            
            print("--- ETL Pipeline Selesai dengan Sukses! ---")
            print(f"Jumlah data akhir: {len(clean_df)} baris.")
        else:
            print("Gagal di tahap Transformasi.")
    else:
        print("Gagal di tahap Ekstraksi (Data kosong).")

if __name__ == "__main__":
    run_pipeline()
