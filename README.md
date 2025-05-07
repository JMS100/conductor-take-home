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