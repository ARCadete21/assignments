import argparse
import logging
from typing import Tuple
from life_expectancy.regions import Region
from life_expectancy.handler import DataHandler, get_data_handler
from life_expectancy.saving import save_data


def get_arguments() -> Tuple[str, Region]:
    """Get country code through Argument Parser."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--file_path', 
        type=str,
        default='eu_life_expectancy_raw.tsv',
        help='The file relative path from the data to load (default is eu_life_expectancy_raw.tsv)'
    )
    parser.add_argument(
        '--country', 
        type=lambda x: Region[x],
        default=Region.PT,
        help='The country code for which to clean data (default is PT)'
    )
    args = parser.parse_args()
    return args.file_path, args.country


def main(data_handler: DataHandler, file_name: str, country_code: Region) -> None:
    """Load, clean and save the DataFrame with country code imputed."""
    logger = logging.getLogger(__name__)
    logger.info('Loading data from %s...', file_name)
    data = data_handler.load_data(file_name)
    logger.info('Data loaded!')
    logger.info('Cleaning data filtered by %s...', country_code.name)
    data = data_handler.clean_data(data, country_code)
    logger.info('Date cleaned!')
    logger.info('Saving data...')
    save_data(data, country_code)
    logger.info('Data saved!')


if __name__ == "__main__": # pragma: no cover
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(message)s'
    )
    file, country = get_arguments()
    file_title, file_extension = file.split('.')
    handler = get_data_handler(file_extension)
    main(handler, file_title, country)
