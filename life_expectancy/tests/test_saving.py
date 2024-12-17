"""Tests for the savimh module"""
from unittest.mock import patch
import pandas as pd
from life_expectancy.saving import save_data
from life_expectancy.regions import Region

from . import OUTPUT_DIR


def test_save_data():
    """Test the save_data function."""
    with patch('pandas.DataFrame.to_csv') as mock_to_csv:
        df = pd.DataFrame({
            'col1': [1, 2, 3],
            'col2': [4, 5, 6]
        })
        save_data(df, country=Region.PT)        
        expected_filepath = str(OUTPUT_DIR / 'pt_life_expectancy.csv')
        mock_to_csv.assert_called_once_with(expected_filepath, index=False)
