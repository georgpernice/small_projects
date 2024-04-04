import unittest
from pathlib import Path
from semorai_skilltest.datasheet_crawler import DatasheetCrawler

EXCEL_PATH = Path(__file__).parent / "resources" / "Test_data.xlsx"


class TestDatasheetCrawler(unittest.TestCase):
    """Test reading methods of ExcelReader class."""

    def test_save_failed_urls(self : "TestDatasheetCrawler")
        """Test that method saves failed product urls to the new excel."""

    def test_save_datasheet(self: "TestDatasheetCrawler"):
        """Test that method crawls and saves a datasheet from product url to given folder.
        
        Ensure this is done using unified filename format.
        """
        
