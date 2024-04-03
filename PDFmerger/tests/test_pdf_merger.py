from pathlib import Path
import unittest
from src.pdfmerger.pdf_merger import PDFMerger # TODO actually this way we dont use the installed version which is bad, but works for now.

RESOURCES_PATH = Path(__file__) / "resources"

class TestPDFMerger(unittest.TestCase):
    def test_merge_gives_enough_pages(self : "TestPDFMerger"):
        """This tests PDMMerger.merge() method by asserting that the merged PDF is three pages long when merging three onepage PDFs.""" 
        expected_numb_of_pages = 3
        merger = PDFMerger()
        pdf_list = [RESOURCES_PATH / "".join(["unmerged", str(i), ".pdf"]) for i in range(3)]
        merged_document = merger.merge(pdf_list)
        assert merged_document.pages() == expected_numb_of_pages
