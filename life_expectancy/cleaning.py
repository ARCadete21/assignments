import pandas as pd
from life_expectancy.regions import Region


def clean_tsv_data(df: pd.DataFrame, country: Region) -> pd.DataFrame:
    """Clean data from TSV file."""
    # Melt the DataFrame and separate columns by splitting based on commas
    df = pd.melt(
        df, id_vars='unit,sex,age,geo\\time',
        value_vars=df.columns[1:], var_name='year'
    )
    
    # Split the column into multiple columns directly na reorder them
    var_cols = ['unit', 'sex', 'age', 'geo']
    df[var_cols] = df['unit,sex,age,geo\\time'].str.split(',', expand=True)
    df = df.drop(columns=['unit,sex,age,geo\\time'])
    df = df[var_cols + ['year', 'value']]
    
    # Convert 'year' column to integer
    df['year'] = df['year'].astype(int)

    # Remove rows where value is ': ' and clean 'value' column
    df = df[df['value'] != ': '].copy()
    df['value'] = pd.to_numeric(
        df['value'].str.replace(r'[^0-9.]', '', regex=True), 
        errors='coerce'
    )

    # Rename 'geo' to 'region' and filter by the specified country
    df = df.rename(columns={'geo': 'region'})
    return df[df['region'] == country.name].copy()


def clean_json_data(df: pd.DataFrame, country: Region) -> pd.DataFrame:
    """Clean data from JSON file."""
    df = df.iloc[:,:-2].copy()
    df = df.rename(columns={
        'country': 'region',
        'life_expectancy': 'value',
    })
    return df[df['region'] == country.name].copy()
