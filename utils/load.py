import pandas as pd
import gspread
from sqlalchemy import create_engine
from gspread_dataframe import set_with_dataframe
from google.oauth2.service_account import Credentials

def save_to_csv(df, filename):
    try:
        df.to_csv(filename, index=False)
        print(f"Berhasil menyimpan data ke {filename}")
        return True 
    except Exception as e:
        print(f"Gagal menyimpan data ke CSV. Error: {e}")
        return False 

def save_to_google_sheets(df, spreadsheet_name, sheet_name="Sheet1"):
    try:
        scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
        credentials = Credentials.from_service_account_file("credentials.json", scopes=scopes)
        gc = gspread.authorize(credentials)
        sh = gc.open(spreadsheet_name)
        worksheet = sh.worksheet(sheet_name)
        worksheet.clear()
        set_with_dataframe(worksheet, df)
        print(f"Berhasil menyimpan data ke Google Sheets: '{spreadsheet_name}'")
        return True 
    except Exception as e:
        print(f"Gagal menyimpan data ke Google Sheets. Error: {e}")
        return False 

def save_to_postgres(df, db_url, table_name="products"):
    try:
        engine = create_engine(db_url)
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Berhasil menyimpan data ke PostgreSQL di tabel: '{table_name}'")
        return True 
    except Exception as e:
        print(f"Gagal menyimpan data ke PostgreSQL. Error: {e}")
        return False 