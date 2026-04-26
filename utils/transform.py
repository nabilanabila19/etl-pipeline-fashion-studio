import pandas as pd
import re

def clean_data(df):
    """
    Fungsi untuk membersihkan dan mentransformasi data hasil scraping.
    """
    try:
        df = df.drop_duplicates().reset_index(drop=True)

        def convert_price(price_str):
            if "Price Unavailable" in price_str or not price_str:
                return None
            numeric_price = re.sub(r'[^\d.]', '', price_str)
            if numeric_price:
                return float(numeric_price) * 16000
            return None

        df['Price'] = df['Price'].apply(convert_price)

        def clean_rating(rating_str):
            if "Invalid" in rating_str:
                return None
            match = re.search(r"(\d+\.\d+|\d+)", rating_str)
            return float(match.group(1)) if match else None

        df['Rating'] = df['Rating'].apply(clean_rating)
        df['Colors'] = df['Colors'].str.extract(r'(\d+)')
        df['Size'] = df['Size'].str.replace("Size: ", "", regex=False)
        df['Gender'] = df['Gender'].str.replace("Gender: ", "", regex=False)
        
        df = df[df['Title'] != "Unknown Product"]
        df = df.dropna().reset_index(drop=True)

        df['Rating'] = df['Rating'].astype(float)
        df['Price'] = df['Price'].astype(float)
        df['Colors'] = df['Colors'].astype(int)

        return df

    except Exception as e:
        print(f"Error saat melakukan transformasi: {e}")
        return None