"""Tests for the Region class"""
from life_expectancy.regions import Region


def test_countries(regions_expected):
    """Test the `countries` method to ensure it only returns actual countries."""
    countries = Region.countries()
    assert regions_expected == countries
