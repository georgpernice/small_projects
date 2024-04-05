from pathlib import Path
import requests
from bs4 import BeautifulSoup


class PdfCrawler:
    """Bundle methods used for downloading datasheet and saving them as well as handling download errors.

    execute saves all PDFs and saves failed URLs in new excel of toplevel folder.
    """

    def __init__(self: "PdfCrawler", path_to_logs_folder: Path) -> None:
        """Initialize crawler passing a folder for possible error logs."""
        pass

    def _crawl_pdfs_from_website(self, url: str):
        # Requests URL and get response object
        response = requests.get(url)

        # Parse text obtained
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all hyperlinks present on webpage
        links = soup.find_all("a")

        i = 0

        # From all links check for pdf link and
        # if present download file
        for link in links:
            if ".pdf" in link.get("href", []):
                i += 1
                print("Downloading file: ", i)

                # Get response object for link
                response = requests.get(link.get("href"))

                # Write content in pdf file
                pdf = open("pdf" + str(i) + ".pdf", "wb")
                pdf.write(response.content)
                pdf.close()
                print("File ", i, " downloaded")

    def _save_failed_urls(self, urls: list[str]):
        """Log all failed URLs into a new excel file."""
        pass

    def crawl_pdf(self: "PdfCrawler", path: Path, product_id: int, product_url: str):
        """Save the PDF from given url into a given path.

        For the saved file use as a filename <product_number>-<product_company>."""

        pass

    def execute(self):
        """Crawl all pdfs. Log errors to new excels."""
        pass
