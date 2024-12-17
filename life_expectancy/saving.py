import os
import pandas as pd
from life_expectancy.regions import Region


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, 'data')


def save_data(df: pd.DataFrame, country: Region) -> None:
    """Save the DataFrame from a given country in the data folder."""
    output_file_name = f'{country.name.lower()}_life_expectancy.csv'
    output_data_path = os.path.join(DATA_PATH, output_file_name)
    df.to_csv(output_data_path, index=False)
