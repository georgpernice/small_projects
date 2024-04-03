from pathlib import Path
from pikepdf import Pdf
import unittest
import shutil
from src.pdfmerger.pdf_merger import PDFMerger # TODO actually this way we dont use the installed version which is bad, but works for now.

RESOURCES_PATH = Path(__file__).parent / "resources"
OUTPUT_PATH = Path(__file__).parent / "output"
class TestPDFMerger(unittest.TestCase):
    def test_merge_gives_enough_pages(self : "TestPDFMerger"):
        """This tests PDMMerger.merge() method by asserting that the merged PDF is three pages long when merging three onepage PDFs."""
        # prepare
        expected_numb_of_pages = 3
        Path.mkdir(OUTPUT_PATH, parents=True, exist_ok=True)
        destination = OUTPUT_PATH / "merged.pdf"
        output_was_empty_before = not [ i for i in OUTPUT_PATH.iterdir()] 
        merger = PDFMerger(destination)
        pdf_list = [RESOURCES_PATH / "".join(["unmerged", str(i+1), ".pdf"]) for i in range(3)]
        # tests and asserts
        merger.merge(pdf_list)
        assert pdf_list[0].name == "unmerged1.pdf"
        assert destination.exists()
        assert len(Pdf.open(destination).pages) == expected_numb_of_pages
        # cleanup
        if output_was_empty_before:
            shutil.rmtree(OUTPUT_PATH)