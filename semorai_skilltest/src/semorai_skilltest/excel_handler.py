"""Define ExcelReader class."""

from pathlib import Path


class ExcelHandler:
    """Bundle methods to wrap extraction of product ID and URL."""

    def __init__(self, path_to_excel: Path, path_to_log_excels: Path) -> None:
        """Initialize ExcelReader passing path to excel.

        The Excel file must contain product IDs in col A and product URLs in col B
        In the first row shall be located only the headings."""
        self.excel_path = path_to_excel
        self.log_folder = path_to_log_excels

    def get_product_id(self, row):
        """Wraps code for getting the product ID from the excel row."""

        return -44

    def get_product_url(self, row):
        """Wraps code for getting the product URL from the excel row."""
        return "invalidurl"

    def save_failed_url_product_ids(self, urls: list[str], title: str):
        """Log all IDs whose URLs failed into a new excel file."""
        pass

    def save_no_url_product_ids(self, ids: list[int], title: str):
        """Log all IDs with missing URLs into a new excel file."""
        pass
