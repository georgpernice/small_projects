"""Unittests for >Pdf Crawler."""

import unittest
from unittest.mock import Mock, patch
from pathlib import Path
import shutil
import pytest
import requests
from src.semorai_skilltest.pdf_crawler import PdfCrawler
from src.semorai_skilltest.excel_handler import ExcelHandler
from src.semorai_skilltest.main import execute

OUTPUT_DIR = Path(__file__).parent / "output"


class TestExecute(unittest.TestCase):
    """Test PdfCrawler.execute method."""

    def setUp(self: "TestExecute") -> None:
        self.crawler = PdfCrawler(OUTPUT_DIR)

    @patch("src.semorai_skilltest.main.PdfCrawler.crawl_pdf")
    @patch("src.semorai_skilltest.main.ExcelHandler.get_product_id")
    @patch("src.semorai_skilltest.main.ExcelHandler.get_product_url")
    def test_execute(
        self: "TestExecute", mock_prod_url: Mock, mock_prod_id: Mock, mock_crawl: Mock
    ):
        """Test that execution method saves ALL datasheets and logs ALL failed ones into excel.

        Assert that it calls crawl_pdf method at least once.
        Assert that it calls save_failed_urls once.
        Assert that log excels exists for FAILED urls and one for NOT EXISTING urls."""

        execute()
        mock_crawl.assert_called
        mock_prod_id.assert_called
        mock_prod_url.assert_called
