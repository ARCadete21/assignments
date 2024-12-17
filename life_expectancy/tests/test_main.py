"""Tests for the main"""
import argparse
from unittest.mock import Mock, patch
import pandas as pd
from life_expectancy.handler import DataHandler
from life_expectancy.regions import Region
from life_expectancy.main import get_arguments, main


@patch('argparse.ArgumentParser.parse_args')
def test_get_arguments(mock_parse_args):
    """Test the get arguments function by mocking parse arguments."""
    mock_parse_args.return_value = argparse.Namespace(
        file_path='test_file.tsv',
        country=Region.PT
    )
    file_path, country = get_arguments()
    assert file_path == 'test_file.tsv'
    assert country == Region.PT


@patch('life_expectancy.main.save_data')
def test_main(mock_save_data):
    # Create a mock DataHandler instance
    mock_data_handler = Mock(spec=DataHandler)

    # Mock the methods of DataHandler
    mock_data_handler.load_data.return_value = 'raw_data'

    # Create a mock DataFrame to represent cleaned data
    mock_cleaned_data = Mock(spec=pd.DataFrame)
    mock_data_handler.clean_data.return_value = mock_cleaned_data

    # Create a mock Region
    mock_country_code = Mock(spec=Region)
    mock_country_code.name = 'TestCountry'

    # Call the main function
    main(mock_data_handler, 'test_file.csv', mock_country_code)

    # Assertions
    mock_data_handler.load_data.assert_called_once_with('test_file.csv')
    mock_data_handler.clean_data.assert_called_once_with('raw_data', mock_country_code)
    mock_save_data.assert_called_once_with(mock_cleaned_data, mock_country_code)
