import os
import argparse
import pandas as pd


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, 'data')


def load_data() -> pd.DataFrame:
    """Load the TSV Life Expectancy DataFrame."""
    input_data_path = os.path.join(DATA_PATH, 'eu_life_expectancy_raw.tsv')
    df = pd.read_csv(input_data_path, sep='\t')
    return df


def clean_data(df: pd.DataFrame, country: str) -> pd.DataFrame:
    """Clean the pandas DataFrame."""
    df = pd.melt(
        df, id_vars='unit,sex,age,geo\\time',
        value_vars=df.columns[1:], var_name='year'
        )

    var_cols = ['unit', 'sex', 'age', 'geo']
    df[var_cols] = df['unit,sex,age,geo\\time'].str.split(',', expand=True)

    df = df.drop(columns=['unit,sex,age,geo\\time'])

    df = df[var_cols + ['year', 'value']]

    df['year'] = df['year'].astype(int)

    colon_value_filter = df['value'] != ': '
    df = df[colon_value_filter].copy()
    df['value'] = df['value'].str.replace(r'[^0-9.]', '', regex=True)
    df['value'] = df['value'].astype(float)

    df = df.rename(columns={'geo': 'region'})
    return df[df['region'] == country].copy()


def save_data(df: pd.DataFrame, country: str) -> None:
    """Save the DataFrame from a given country in the data folder."""
    output_file_name = f'{country.lower()}_life_expectancy.csv'
    output_data_path = os.path.join(DATA_PATH, output_file_name)

    df.to_csv(output_data_path, index=False)


def main():
    """Load, clean and save the DataFrame with country imputed."""
    parser = argparse.ArgumentParser(
        description="Clean data for a specified country."
    )
    parser.add_argument(
        '--country', 
        type=str,
        default='PT',
        help='The country code for which to clean data (default is PT)'
    )
    args = parser.parse_args()

    df = load_data()
    df = clean_data(df, args.country)
    save_data(df, args.country)


if __name__ == "__main__":
    main()
