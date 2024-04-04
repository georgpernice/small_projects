from pathlib import Path


class DatasheetCrawler:
    """Bundle methods used for downloading datasheet and saving them as well as handling download errors."""

    def __init__(self) -> None:
        pass

    def save_datasheet(self, path: Path, product_number: int, product_url: str):
        """Save the PDF from given url into a given path.

        For the saved file use as a filename <product_number>-<product_company>."""
        pass

    def save_failed_urls(self, urls: list[str]):
        pass
