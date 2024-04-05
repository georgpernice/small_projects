"""Define ExcelReader class."""

from pathlib import Path


class ExcelReader:
    """Bundle methods to wrap extraction of product ID and URL."""

    def __init__(self, path_to_excel: Path) -> None:
        """Initialize ExcelReader passing path to excel.

        The Excel file must contain product IDs in col A and product URLs in col B
        In the first row shall be located only the headings."""
        pass

    def get_product_id(self, row):
        """Wraps code for getting the product ID from the excel row."""

        pass

    def get_product_url(self, row):
        """Wraps code for getting the product URL from the excel row."""
        pass
