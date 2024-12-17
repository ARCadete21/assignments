"""Tests for the cleaning module"""
import pandas as pd
from life_expectancy.cleaning import clean_tsv_data, clean_json_data
from life_expectancy.regions import Region


def test_tsv_cleaner_clean_data(eu_life_expectancy_raw, pt_life_expectancy_expected_tsv):
    """Test the clean data function for TSV files and compare the output to the expected output."""
    df = clean_tsv_data(eu_life_expectancy_raw, country=Region.PT)
    df.reset_index(drop=True, inplace=True)
    pd.testing.assert_frame_equal(df, pt_life_expectancy_expected_tsv)


def test_json_cleaner_clean_data(eurostat_life_expect, pt_life_expectancy_expected_json):
    """Test the clean data function for JSON files and compare the output to the expected output."""
    df = clean_json_data(eurostat_life_expect, country=Region.PT)
    df.reset_index(drop=True, inplace=True)
    pd.testing.assert_frame_equal(df, pt_life_expectancy_expected_json)
