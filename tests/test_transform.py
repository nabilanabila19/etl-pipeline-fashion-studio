import pandas as pd
from utils.transform import clean_data

def test_clean_data():
    raw_data = pd.DataFrame({
        "Title": ["Kaos Oblong", "Unknown Product"],
        "Price": ["$10.00", "$5.00"],
        "Rating": ["4.8 / 5", "Invalid Rating"],
        "Colors": ["3 Colors", "1 Color"],
        "Size": ["Size: M", "Size: L"],
        "Gender": ["Gender: Men", "Gender: Women"]
    })
    
    clean_df = clean_data(raw_data)
    
    assert "Unknown Product" not in clean_df['Title'].values
    assert clean_df['Price'].iloc[0] == 160000.0
    assert clean_df['Rating'].iloc[0] == 4.8
    assert clean_df['Size'].iloc[0] == "M"