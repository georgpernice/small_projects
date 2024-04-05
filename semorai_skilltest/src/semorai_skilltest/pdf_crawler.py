from pathlib import Path
import requests
from bs4 import BeautifulSoup
import regex as re


class PdfCrawler:
    """Bundle methods used for downloading datasheet and saving them as well as handling download errors.

    execute saves all PDFs and saves failed URLs in new excel of toplevel folder.
    """

    def __init__(self: "PdfCrawler", output_dir: Path) -> None:
        """Initialize crawler passing a folder for possible error logs."""
        self.output_dir = output_dir

    def url_to_company_name(self, url: str):
        """Fishing out the company name from url with regex."""
        company_name = re.search(r"https?:\/\/(?:www\.)?([^.\/]+)", url)[1]
        return company_name

    def _crawl_pdfs_from_website(
        self, url: str, pdf_name: str, keyword_for_search: str = "datasheet"
    ):
        # Requests URL and get response object
        response = requests.get(url, timeout=10)

        # Parse text obtained
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all hyperlinks present on webpage
        links = soup.find_all("a")

        i = 0

        # From all links check for pdf link and
        # if present download file
        number_of_promising_pdfs = 0
        for link in links:
            if (
                ".pdf" in link.get("href", [])
                and keyword_for_search in link.string.lower()
            ):
                i += 1
                print("Downloading file: ", i)

                # Get response object for link
                response = requests.get(link.get("href"), timeout=10)
                # Write content in pdf file
                with open(
                    self.output_dir / (pdf_name + ("" if i == 1 else str(i)) + ".pdf"),
                    "wb",
                ) as pdf:
                    pdf.write(response.content)
                    number_of_promising_pdfs += 1
        if number_of_promising_pdfs == 0:
            raise FileNotFoundError(
                "No PDFs or PDF links found on website. As none where containing the keyword: "
                + keyword_for_search
            )

    def _download_pdf_from_direct_url(self, url: str, pdf_name: str):
        try:
            response = requests.get(url, timeout=10)
        except Exception as exc:
            raise exc
        # Write content in pdf file
        with open(
            self.output_dir / (pdf_name + ".pdf"),
            "wb",
        ) as pdf:
            pdf.write(response.content)

    def crawl_pdf(self: "PdfCrawler", path: Path, product_id: int, product_url: str):
        """Save the PDF from given url into a given path.

        For the saved file use as a filename <product_number>-<product_company>."""
        if "http" not in product_url:
            raise ValueError("This was no URL.")
        else:
            company = self.url_to_company_name(product_url)
            pdf_name = str(product_id) + "-" + str(company)
            if product_url[-4:] == ".pdf":
                try:
                    self._download_pdf_from_direct_url(product_url, pdf_name)
                except Exception as exc:
                    raise requests.exceptions.RequestException(
                        "Download failed. Maybe domain is unresolvable."
                    ) from exc
            else:
                self._crawl_pdfs_from_website(product_url, pdf_name)
