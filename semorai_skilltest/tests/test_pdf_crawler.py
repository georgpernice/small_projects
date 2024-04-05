"""Unittests for DatasheetCrawler."""

import unittest
from pathlib import Path
from semorai_skilltest.pdf_crawler import PdfCrawler
import shutil

OUTPUT_PATH = Path(__file__).parent / "output"
LOG_PATH = Path(__file__).parent / "logs"


class TestCrawlPdf(unittest.TestCase):
    """Test method save_pdf.

    Ensure this is done using unified filename format.
    Ensure that all of the following cases are handled:
            * no URL given
            * invalid URL
            * valid URL
                * url ending with pdf ---------------------------> (SUCCESS)
                * url not ending with pdf
                * cannot find a link to pdf on website
                * on website found links to PDF
                    * valid -------------------------------------> (SUCCESS)
                    * invalid
    """

    def setUp(self: "TestCrawlPdf") -> None:
        Path.mkdir(OUTPUT_PATH, exist_ok=True)
        Path.mkdir(LOG_PATH, exist_ok=True)

    def tearDown(self: "TestCrawlPdf"):
        shutil.rmtree(OUTPUT_PATH)
        shutil.rmtree(LOG_PATH)

    def test_crawl_pdf_no_url(self: "TestCrawlPdf"):
        """Test that method raises exception when a non URLish pattern is passed as URL."""
        pass

    def test_crawl_pdf_invalid_url(self: "TestCrawlPdf"):
        """Test that method raises exception when unaccessible or invalid URL is passed."""
        pass

    def test_crawl_pdf_valid_url_pdf_missing(self: "TestCrawlPdf"):
        """Test that method raises exception when PDF not found in URL."""
        pass

    def test_crawl_pdf_direct_valid_url(self: "TestCrawlPdf"):
        """Test that method downloads a PDF to folder with correct naming when link is accessible.

        Method should find PDF even though link leads not directly to PDF
        but to website containing final link to PDF.
        """
        pass

    def test_crawl_pdf_indirect_valid_url(self: "TestCrawlPdf"):
        """Test that method downloads a PDF to folder with correct naming when link is accessible.

        Method should find PDF even though link leads not directly to PDF
        but to website containing final link to PDF.
        """
        pass

    def test_crawl_pdf_correct_filename(self: "TestCrawlPdf"):
        """Test that method saves under correct filename.

        Filename should be generated like "<product-id-from-excel>-<Company-from-url>.pdf".
        """
        pass


class TestExecute(unittest.TestCase):
    """Test PdfCrawler.execute method."""

    def test_execute(self: "TestExecute"):
        """Test that execution method saves ALL datasheets and logs ALL failed ones into excel.

        Assert that it calls crawl_pdf method at least once.
        Assert that it calls save_failed_urls once.
        Assert that log excels exists for FAILED urls and one for NOT EXISTING urls."""
