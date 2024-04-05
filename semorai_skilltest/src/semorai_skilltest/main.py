"""Execute the the PDF crawling process."""

from pathlib import Path
from semorai_skilltest.pdf_crawler import DatasheetCrawler
from semorai_skilltest.excel_handler import ExcelHandler

PATH_TO_EXCEL = Path("C:\\Users\\ThinkCenter\\Desktop\\skilltest\\Test_data.xlsx")
crawler = DatasheetCrawler(PATH_TO_EXCEL.parent)
reader = ExcelHandler(PATH_TO_EXCEL)
