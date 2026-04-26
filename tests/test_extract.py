import pytest
from unittest.mock import patch, MagicMock
from utils.extract import scrape_main
import pandas as pd

@patch('requests.get')
def test_scrape_main_success(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = '<html><div class="product-details"><h3 class="product-title">Baju</h3><span class="price">$10</span><p>4/5</p><p>1</p><p>M</p><p>Men</p></div></html>'
    mock_get.return_value = mock_response
    df = scrape_main()
    assert not df.empty
    assert df['Title'].iloc[0] == "Baju"

@patch('requests.get')
def test_scrape_main_error(mock_get):
    mock_get.side_effect = Exception("Website Down")
    
    df = scrape_main()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 0