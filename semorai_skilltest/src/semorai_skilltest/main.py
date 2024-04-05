"""Execute the the PDF crawling process."""

from pathlib import Path
from src.semorai_skilltest.pdf_crawler import PdfCrawler
from src.semorai_skilltest.excel_handler import ExcelHandler
import requests

PATH_TO_EXCEL = Path("C:\\Users\\ThinkCenter\\Desktop\\skilltest\\Test_data.xlsx")
PATH_TO_LOG_FOLDER = PATH_TO_EXCEL.parent / "logs"
PATH_TO_OUTPUT_FOLDER = PATH_TO_EXCEL.parent / "output"
EXCEL_LENGTH = 22  # TODO replace with 2591  # sadly no time for a get function
crawler = PdfCrawler(PATH_TO_EXCEL.parent)
handler = ExcelHandler(PATH_TO_EXCEL, PATH_TO_LOG_FOLDER)


def execute():
    """Crawl all pdfs. Log errors to new excels."""
    not_url_ids = []
    failed_url_ids = []
    for row in range(1, EXCEL_LENGTH + 1):
        prod_id = row  # turns out the cells containing numbers are really not hardcoded
        # so just using the row as product_id is faster that resolving stuff like A44+1
        url = handler.get_product_url(row)
        print(f"prod_id: {prod_id}, row: {row}")
        try:
            crawler.crawl_pdf(PATH_TO_OUTPUT_FOLDER, prod_id, url)
        except ValueError:
            not_url_ids.append(prod_id)
        except FileNotFoundError:
            failed_url_ids.append(prod_id)
        except requests.exceptions.RequestException:
            failed_url_ids.append(prod_id)
    print(not_url_ids)
    print()
    print(failed_url_ids)
    handler.save_failed_url_product_ids(failed_url_ids, "title")
    handler.save_no_url_product_ids(failed_url_ids, "title")


if __name__ == "main":
    execute()
execute()
