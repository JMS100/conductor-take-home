import fitz  # PyMuPDF
import re
import os
from math import inf

class PDFNumberSearcher:
    def __init__(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        self.file_path = file_path
        self.doc = fitz.open(file_path)

    def get_max_on_page(self, page_number):
        if not (0 <= page_number < len(self.doc)):
            raise ValueError(f"Page number {page_number} out of range")
        
        text = self.doc[page_number].get_text() # Get text of document
        tokens = text.split()

        # Match numbers with or without commas and decimals, optionally prefixed by currency or symbol
        number_pattern = re.compile(r'^[^A-Za-z\d]?\d{1,3}(?:,\d{3})*(?:\.\d+)?$|^[^A-Za-z\d]?\d+(?:\.\d+)?$')

        max_num = -inf
        for token in tokens:
            if number_pattern.match(token):
                            cleaned = re.sub(r'[^0-9.]', '', token)  # Remove non-numeric except dot
                            try:
                                 num = float(cleaned.replace(',', '')) 
                                 max_num = max(max_num, num)
                            except ValueError:
                                 continue
        return max_num if max_num != -inf else None

    def get_max_in_doc(self):
        max_val = -inf
        for page_number in range(self.doc.page_count):
            max_page = self.get_max_on_page(page_number)
            if max_page:   
                max_val = max(max_page, max_val)
        return max_val if max_val != -inf else None # 

if __name__ == "__main__":
    searcher = PDFNumberSearcher("FY25.pdf")
    print(searcher.get_max_in_doc())
