# PDFNumberSearcher

This is a simple Python script that finds the largest number in a PDF file. It works by reading through the text on each page, pulling out anything that looks like a number (including commas and decimals), and comparing them.

It uses [PyMuPDF](https://pymupdf.readthedocs.io/) to extract the text.

Methods are provided to find the largest number in the entire document, or the largest number on a specific page.

The current script finds the largest numeric value in the provided PDF for the assignment.
## How to run (FY25.pdf)

1. Install dependencies:
   ```bash
    pip install -r requirements.txt

2. Run the script:
   ```bash
   python pdf_number_searcher.py
   ```

## Using Your Own PDF

To analyze a different PDF:

1. Replace `"FY25.pdf"` in the script with the name of your own PDF file.
   ```python
   searcher = PDFNumberSearcher("your_file_name.pdf")
   ```

2. (Optional) Add your own calls to the script.
   ```python
   # Example: Print largest value on first page (zero indexed)
   print(searcher = PDFNumberSearcher.get_max_on_page(0))
   ```

3. Run the script:
   ```bash
   python pdf_number_searcher.py
   ```

## Bugs and Issues

1. **No Numbers Found**  
   If no numbers are found in the PDF document, the program returns `None`. This behavior is fine for simple use cases, but would likely need to be changed if used in a larger application.

2. **Natural Language Context Not Accounted For**  
   The script does not interpret context like "in millions" or "thousands" that may accompany a number. For example, a value written as "Revenue (in millions): 32" will be interpreted as `32`, not `32,000,000`.

3. **Regex Limitations**  
   The current regular expression aims to catch most formats of numeric values (e.g., "$1,234.56", "1234.56", "1,000", etc.), but it hasn't been tested against every edge case. Numbers with unusual formatting or trailing units (e.g., "1234USD" or "($5,000)") may be missed or misinterpreted.

4. **No OCR or Scanned Text Handling**  
   This script only works with PDFs that contain extractable text. If your PDF is scanned or image-based, PyMuPDF will not extract numbers unless OCR (Optical Character Recognition) has been applied beforehand.

5. **Page Tokenization Is Naive**  
   Numbers are detected by splitting text on whitespace. If a number is broken across lines, columns, or formatting artifacts, it might not be recognized properly.

6. **Non-Numeric Symbols**  
   Symbols like `($1,000)` or `1,000.00*` are partially accounted for using the regex, but some edge cases may still throw off the parsing or conversion process.
