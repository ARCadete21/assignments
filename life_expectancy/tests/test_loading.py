"""Tests for the loadind module"""
from unittest.mock import patch
from life_expectancy.loading import load_tsv_data, load_json_data


def test_load_tsv_data(eu_life_expectancy_raw):
    """Test the load data function for TSV files."""
    with patch('pandas.read_csv', return_value=eu_life_expectancy_raw):
        df = load_tsv_data('the_data_file_name')
        assert df.equals(eu_life_expectancy_raw)


def test_load_json_data(eurostat_life_expect):
    """Test the load data function for JSON files."""
    with patch('pandas.read_json', return_value=eurostat_life_expect):
        df = load_json_data('the_data_file_name')
        assert df.equals(eurostat_life_expect)
