import argparse
from life_expectancy.cleaning import clean_data
from life_expectancy.loading_saving import load_data, save_data
from life_expectancy.regions import Region


def main() -> None:
    """Load, clean and save the DataFrame with country imputed."""
    parser = argparse.ArgumentParser(
        description="Clean data for a specified country."
    )
    parser.add_argument(
        '--country', 
        type=lambda x: Region[x],
        default=Region.PT,
        help='The country code for which to clean data (default is PT)'
    )
    args = parser.parse_args()

    data = load_data()
    data = clean_data(data, args.country)
    save_data(data, args.country)


if __name__ == "__main__":
    main()
