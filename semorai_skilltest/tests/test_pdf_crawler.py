"""Unittests for >Pdf Crawler."""

import unittest
from unittest.mock import Mock, patch
from pathlib import Path
import shutil
import pytest
from src.semorai_skilltest.pdf_crawler import PdfCrawler

OUTPUT_DIR = Path(__file__).parent / "output"


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
        Path.mkdir(OUTPUT_DIR, exist_ok=False)
        self.crawler = PdfCrawler()

    def tearDown(self: "TestCrawlPdf"):
        shutil.rmtree(OUTPUT_DIR)

    def test_crawl_pdf_no_url(self: "TestCrawlPdf"):
        """Test that method raises exception when a non URLish pattern is passed as URL."""
        with pytest.raises(ValueError):
            self.crawler.crawl_pdf(path=OUTPUT_DIR, product_id=32, product_url="-")

    def test_crawl_pdf_invalid_url(self: "TestCrawlPdf"):
        """Test that method raises exception when unaccessible or invalid URL is passed."""
        with pytest.raises(ValueError):
            self.crawler.crawl_pdf(
                path=OUTPUT_DIR,
                product_id=9999,  # just some random id
                product_url="https://ujbtgrvedcds.com/rfezunj.pdf",  # non existent url
            )
        # assert empty output dir
        assert not OUTPUT_DIR.iterdir()

    def test_crawl_pdf_valid_url_pdf_missing(self: "TestCrawlPdf"):
        """Test that method raises exception when PDF not found in URL."""

        with pytest.raises(
            FileNotFoundError, match="No PDFs or PDF links found on website."
        ):
            self.crawler.crawl_pdf(
                path=OUTPUT_DIR,
                product_id=9999,  # just some random id
                product_url="https://www.kyocera-avx.com/products/",  # manually made URL containing no PDF links
            )
        # assert empty output dir
        assert not list(OUTPUT_DIR.iterdir())

    def test_crawl_pdf_direct_valid_url(self: "TestCrawlPdf"):
        """Test that method downloads a new PDF into output folder.

        Filename should be generated like "<product-id-from-excel>-<Company-from-url>.pdf".
        """
        self.crawler.crawl_pdf(
            path=OUTPUT_DIR,
            product_id=2,
            product_url="https://www.vishay.com/docs/45199/vjcommercialseries.pdf",
        )
        # assert that downloaded pdf exists with correct name in output directory.
        assert OUTPUT_DIR / "2-vishay.pdf" in list(OUTPUT_DIR.iterdir())

    def test_crawl_pdf_indirect_valid_url(self: "TestCrawlPdf"):
        """Test that method downloads a PDF to folder with correct naming when link is accessible.

        Method should find PDF even though link leads not directly to PDF
        but to website containing final link to PDF.
        """
        self.crawler.crawl_pdf(
            path=OUTPUT_DIR,
            product_id=1229,
            product_url="https://www.kyocera-avx.com/products/ceramic-capacitors/surface-mount/x7r-dielectric/",
        )
        assert OUTPUT_DIR / "1229-kyocera-avx.pdf" in list(OUTPUT_DIR.iterdir())


class TestExecute(unittest.TestCase):
    """Test PdfCrawler.execute method."""

    @patch("PdfCrawler.crawl_pdf")
    @patch("ExcelReader.get_product_id")
    @patch("ExcelReader.get_product_url")
    def test_execute(
        self: "TestExecute",
        mock_prod_url: Mock,
        mock_prod_id: Mock,
        mock_crawl: Mock,
    ):
        """Test that execution method saves ALL datasheets and logs ALL failed ones into excel.

        Assert that it calls crawl_pdf method at least once.
        Assert that it calls save_failed_urls once.
        Assert that log excels exists for FAILED urls and one for NOT EXISTING urls."""
        mock_crawl.assert_any_call()
        mock_prod_id.assert_any_call()
        mock_prod_url.assert_any_call()
