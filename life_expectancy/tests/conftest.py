"""Pytest configuration file"""
import pandas as pd
import pytest

from . import FIXTURES_DIR


@pytest.fixture(scope="session")
def eu_life_expectancy_raw() -> pd.DataFrame:
    """Fixture to load the raw input"""
    return pd.read_csv(FIXTURES_DIR / "eu_life_expectancy_raw.tsv", sep="\t")


@pytest.fixture(scope="session")
def eu_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    return pd.read_csv(FIXTURES_DIR / "eu_life_expectancy_expected.csv")


@pytest.fixture(scope="session")
def regions_expected() -> pd.DataFrame:
    """Fixture to get list of expected regions (countries)"""
    return ['AL', 'AM', 'AT', 'AZ', 'BE', 'BG', 'BY', 'CH', 'CY', 'CZ', 'DE', 'DK',
            'EE', 'EL', 'ES', 'FI', 'FR', 'FX', 'GE', 'HR', 'HU', 'IE', 'IS', 'IT',
            'LI', 'LT', 'LU', 'LV', 'MD', 'ME', 'MK', 'MT', 'NL', 'NO', 'PL', 'PT',
            'RO', 'RS', 'RU', 'SE', 'SI', 'SK', 'SM', 'TR', 'UA', 'UK', 'XK']
