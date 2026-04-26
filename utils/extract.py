import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def scrape_main():
    """
    Fungsi utama untuk mengambil data dari website Fashion Studio.
    Mengambil data dari halaman 1 sampai 50 (Total 1000 data sebelum dibersihkan).
    """
    all_products = []
    
    for page in range(1, 51):
        if page == 1:
            url = "https://fashion-studio.dicoding.dev/"
        else:
            url = f"https://fashion-studio.dicoding.dev/page/{page}/"
        
        try:
            response = requests.get(url, timeout=10)
            
            if response.status_code == 404:
                url = f"https://fashion-studio.dicoding.dev/page{page}/"
                response = requests.get(url, timeout=10)
            if response.status_code == 404:
                url = f"https://fashion-studio.dicoding.dev/?page={page}"
                response = requests.get(url, timeout=10)
                
            response.raise_for_status() 
            
            soup = BeautifulSoup(response.text, 'html.parser')
            items = soup.find_all('div', class_='product-details')
            
            for item in items:
                title = item.find('h3', class_='product-title').text.strip() if item.find('h3', class_='product-title') else "Unknown Product"
                
                price_tag = item.find('span', class_='price')
                price = price_tag.text.strip() if price_tag else "Price Unavailable"
                
                p_tags = item.find_all('p')
                rating = p_tags[0].text.strip() if len(p_tags) > 0 else "Invalid Rating"
                colors = p_tags[1].text.strip() if len(p_tags) > 1 else "0 Colors"
                size = p_tags[2].text.strip() if len(p_tags) > 2 else "Size: Unknown"
                gender = p_tags[3].text.strip() if len(p_tags) > 3 else "Gender: Unknown"
                
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                all_products.append({
                    "Title": title,
                    "Price": price,
                    "Rating": rating,
                    "Colors": colors,
                    "Size": size,
                    "Gender": gender,
                    "timestamp": timestamp
                })
                
        except Exception as e:
            print(f"Peringatan: Gagal mengakses halaman {page}. Error: {e}")
            continue 
            
    return pd.DataFrame(all_products)