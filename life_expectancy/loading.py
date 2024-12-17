import os
import pandas as pd


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, 'data')


def load_tsv_data(file_name: str) -> pd.DataFrame:
    """Load data from TSV file."""
    return pd.read_csv(DATA_PATH + f'\\{file_name}.tsv', sep='\t')    


def load_json_data(file_name: str) -> pd.DataFrame:
    """Load data in zip folder from JSON file."""
    return pd.read_json(DATA_PATH + f'\\{file_name}.json')    
