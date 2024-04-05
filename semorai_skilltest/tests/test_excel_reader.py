import unittest
from pathlib import Path
from semorai_skilltest.excel_reader import ExcelReader

EXCEL_PATH = Path(__file__).parent / "resources" / "Test_data.xlsx"


class TestExcelReader(unittest.TestCase):
    """Test reading methods of ExcelReader class."""

    def test_get_product_number(self: "TestExcelReader"):
        """Test that method reads the product link from excel."""
        # setup
        row_a2 = 1
        expected_content_a2 = 1
        reader = ExcelReader(EXCEL_PATH)
        # test
        col_a = reader.get_product_number()
        assert expected_content_a2 == col_a[row_a2]

    def test_get_product_url(self: "TestExcelReader"):
        """Test that method reads the product link from excel."""
        # setup
        row_b2 = 1
        expected_content_b2 = "https://www.murata.com/en-global/api/pdfdownloadapi?cate=luCeramicCapacitorsSMD&partno=GRM319R71H224KA01#"
        reader = ExcelReader(EXCEL_PATH)
        # test
        col_b = reader.get_product_url()
        assert expected_content_b2 == col_b[row_b2]
