import os
import pandas as pd


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, 'data')


def load_data() -> pd.DataFrame:
    """Load the TSV Life Expectancy DataFrame."""
    input_data_path = os.path.join(DATA_PATH, 'eu_life_expectancy_raw.tsv')
    df = pd.read_csv(input_data_path, sep='\t')
    return df


def save_data(df: pd.DataFrame, country: str) -> None:
    """Save the DataFrame from a given country in the data folder."""
    output_file_name = f'{country.lower()}_life_expectancy.csv'
    output_data_path = os.path.join(DATA_PATH, output_file_name)
    df.to_csv(output_data_path, index=False)
