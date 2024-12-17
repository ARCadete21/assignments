import unittest
from unittest.mock import MagicMock, patch
import pandas as pd
from life_expectancy.handler import DataHandler, get_data_handler


class TestDataHandler(unittest.TestCase):
    """Class with Data Handler class unit tests."""

    def setUp(self):
        # Mock data for testing
        self.mock_data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        
        # Mock loader and cleaner functions
        self.mock_loader = MagicMock(return_value=self.mock_data)
        self.mock_cleaner = MagicMock(return_value=self.mock_data)

        # Set data handler
        self.data_handler = DataHandler(loader=self.mock_loader, cleaner=self.mock_cleaner)

    def test_load_data(self):
        """Test load data function."""
        # Test the DataHandler's load_data method
        loaded_data = self.data_handler.load_data("mock_file")
        self.mock_loader.assert_called_once_with("mock_file")
        pd.testing.assert_frame_equal(loaded_data, self.mock_data)

    def test_clean_data(self):
        """Test clean data function."""
        # Test the DataHandler's clean_data method
        cleaned_data = self.data_handler.clean_data(self.mock_data, 'PT')
        self.mock_cleaner.assert_called_once_with(self.mock_data, 'PT')
        pd.testing.assert_frame_equal(cleaned_data, self.mock_data)


class TestGetDataHandler(unittest.TestCase):
    """Class with get data handler function unit tests."""

    @patch('life_expectancy.handler.load_tsv_data') 
    @patch('life_expectancy.handler.clean_tsv_data')
    def test_supported_extension(self, mock_clean_tsv, mock_load_tsv):
        """Test the function with supported file extension."""
        mock_load_tsv.return_value = "mocked loader"
        mock_clean_tsv.return_value = "mocked cleaner"
        handler = get_data_handler('tsv')
        self.assertEqual(handler.loader, mock_load_tsv)
        self.assertEqual(handler.cleaner, mock_clean_tsv)

    
    def test_unsupported_extension(self):
        """Test the function with an unsupported file extension."""
        with self.assertRaises(ValueError) as context:
            get_data_handler('csv')
        self.assertIn("Unsupported file extension: csv.", str(context.exception))
        self.assertIn("Supported extensions are: ['tsv', 'json'].", str(context.exception))
