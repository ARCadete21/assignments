"""Tests for the loading/saving module"""
from unittest.mock import patch
import pandas as pd
from life_expectancy.loading_saving import load_data, save_data
from life_expectancy.regions import Region
from . import OUTPUT_DIR


def test_load_data(eu_life_expectancy_raw):
    """Test the load_data function"""
    with patch('pandas.read_csv', return_value=eu_life_expectancy_raw):
        df = load_data()
        assert df.equals(eu_life_expectancy_raw)


def test_save_data():
    """Test the save_data function"""
    with patch('pandas.DataFrame.to_csv') as mock_to_csv:
        df = pd.DataFrame({
            'col1': [1, 2, 3],
            'col2': [4, 5, 6]
        })
        save_data(df, country=Region.PT)        
        expected_filepath = str(OUTPUT_DIR / 'pt_life_expectancy.csv')
        mock_to_csv.assert_called_once_with(expected_filepath, index=False)
