"""Execute the the PDF crawling process."""

from pathlib import Path
from src.semorai_skilltest.pdf_crawler import PdfCrawler
from src.semorai_skilltest.excel_handler import ExcelHandler

PATH_TO_EXCEL = Path("C:\\Users\\ThinkCenter\\Desktop\\skilltest\\Test_data.xlsx")
PATH_TO_LOG_FOLDER = PATH_TO_EXCEL.parent / "logs"
PATH_TO_OUTPUT_FOLDER = PATH_TO_EXCEL.parent / "output"
EXCEL_LENGTH = 2591  # sadly no time for a get function
crawler = PdfCrawler(PATH_TO_EXCEL.parent)
handler = ExcelHandler(PATH_TO_EXCEL, PATH_TO_LOG_FOLDER)


def execute():
    """Crawl all pdfs. Log errors to new excels."""
    for row in range(1, EXCEL_LENGTH + 1):
        prod_id = handler.get_product_id(row)
        url = handler.get_product_url(row)
        crawler.crawl_pdf(PATH_TO_OUTPUT_FOLDER, prod_id, url)
