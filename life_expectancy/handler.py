from typing import Callable
import pandas as pd
from life_expectancy.loading import load_tsv_data, load_json_data
from life_expectancy.cleaning import clean_tsv_data, clean_json_data
from life_expectancy.regions import Region


class DataHandler:
    """Class to handle loading and cleaning of data using specified tools."""

    def __init__(
            self, 
            loader: Callable[[str], pd.DataFrame], 
            cleaner: Callable[[pd.DataFrame, Region], pd.DataFrame]
            ) -> None:
        self.loader = loader
        self.cleaner = cleaner

    def load_data(self, file_name: str) -> pd.DataFrame:
        """Load data function."""
        return self.loader(file_name)

    def clean_data(self, df: pd.DataFrame, country: Region) -> pd.DataFrame:
        """Clean data function."""
        return self.cleaner(df, country)


def get_data_handler(file_extension: str) -> DataHandler:
    """Get data loader and data cleaner from file extension."""
    handlers = {
        'tsv': DataHandler(loader=load_tsv_data, cleaner=clean_tsv_data),
        'json': DataHandler(loader=load_json_data, cleaner=clean_json_data),
    }
    try:
        return handlers[file_extension]
    except KeyError as exception:
        raise ValueError(
            f"Unsupported file extension: {file_extension}. "
            f"Supported extensions are: {list(handlers.keys())}."
            ) from exception
