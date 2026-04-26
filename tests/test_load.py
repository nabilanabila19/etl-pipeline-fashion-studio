import pandas as pd
import os
import pytest
from unittest.mock import patch, MagicMock
from utils.load import save_to_csv, save_to_google_sheets, save_to_postgres

def test_save_to_csv_success():
    df = pd.DataFrame({"test": [1, 2, 3]})
    file_name = "test_output.csv"
    result = save_to_csv(df, file_name)
    assert result is True
    assert os.path.exists(file_name)
    os.remove(file_name)

def test_save_to_csv_error():
    result = save_to_csv(None, "error.csv")
    assert result is False

def test_save_to_google_sheets_fail():
    df = pd.DataFrame({"test": [1]})
    result = save_to_google_sheets(df, "Sheet Fail")
    assert result is False

@patch('utils.load.create_engine')
def test_save_to_postgres_success(mock_create_engine):
    mock_engine = MagicMock()
    mock_create_engine.return_value = mock_engine
    
    df = pd.DataFrame({"test": [1, 2, 3]})
    result = save_to_postgres(df, "postgresql://user:pass@localhost/db", "test_table")
    
    assert result is True
    mock_create_engine.assert_called_once()

@patch('utils.load.create_engine')
def test_save_to_postgres_fail(mock_create_engine):
    mock_create_engine.side_effect = Exception("Connection Failed")
    
    df = pd.DataFrame({"test": [1]})
    result = save_to_postgres(df, "wrong_link", "test_table")
    
    assert result is False