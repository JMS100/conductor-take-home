import fitz  # PyMuPDF
import re
import os
from math import inf

class PDFNumberSearcher:
    """
    A utility class to extract and find the largest number in a PDF document.

    Numbers can include commas, decimals, and leading symbols (e.g., '$3,000.00').
    """
    def __init__(self, file_path):
        """
        Initializes the PDFNumberSearcher with a given PDF file.

        Parameters:
            file_path (str): The path to the PDF file.

        Raises:
            FileNotFoundError: If the provided file path does not exist.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        self.file_path = file_path
        self.doc = fitz.open(file_path)


    def get_max_on_page(self, page_number):
        """
        Returns the largest number found on a specific page of the PDF.

        Parameters:
            page_number (int): The zero-based index of the page to scan.

        Returns:
            float or None: The largest number found on the page, or None if no valid numbers are found.

        Raises:
            ValueError: If the page number is out of bounds.
        """
        # Throw error if page_number out of bounds
        if not (0 <= page_number < len(self.doc)):
            raise ValueError(f"Page number {page_number} out of range. Document has {len(self.doc)} pages.")
        
        # Get text of document and split it on white-space
        text = self.doc[page_number].get_text() 
        tokens = text.split() 

        # Match numbers with or without commas and decimals, optionally prefixed by currency or symbol
        number_pattern = re.compile(r'^[^A-Za-z\d]?\d{1,3}(?:,\d{3})*(?:\.\d+)?$|^[^A-Za-z\d]?\d+(?:\.\d+)?$')

        # Find max_num on page
        max_num = -inf
        for token in tokens:
            if number_pattern.match(token):
                cleaned = re.sub(r'[^0-9.]', '', token)  # Remove non-numeric except dot
                try:
                        num = float(cleaned.replace(',', ''))
                        max_num = max(max_num, num)
                except ValueError: # Handle case of multiple . (ex 12..32) or other edge cases
                        continue
        return max_num if max_num != -inf else None

    def get_max_in_doc(self):
        """
        Returns the largest number found across all pages in the PDF.

        Returns:
            float or None: The largest number found in the document, or None if no valid numbers are found.
        """
        max_val = -inf
        for page_number in range(self.doc.page_count):
            max_page = self.get_max_on_page(page_number)
            if max_page is not None:   
                max_val = max(max_page, max_val)
        return max_val if max_val != -inf else None # Returning None is not great, so check for that

if __name__ == "__main__":
    # Example usage: finds the largest number in "FY25.pdf"
    searcher = PDFNumberSearcher("FY25.pdf")
    print(f' Largest number in doc is: {searcher.get_max_in_doc()}')
