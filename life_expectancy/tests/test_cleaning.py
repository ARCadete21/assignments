"""Tests for the cleaning module"""
import pandas as pd
from life_expectancy.cleaning import clean_data


def test_clean_data(eu_life_expectancy_raw, eu_life_expectancy_expected):
    """Run the `clean_data` function and compare the output to the expected output"""
    df = clean_data(eu_life_expectancy_raw, country='PT')
    df.reset_index(drop=True, inplace=True)
    pd.testing.assert_frame_equal(df, eu_life_expectancy_expected)
