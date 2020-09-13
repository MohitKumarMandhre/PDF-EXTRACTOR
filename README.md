# PDF-EXTRACTOR

### Convert PDF To Text

- Did you ever wonder how to redact text in PDF documents? We have the solution for you. Simply convert your PDF document to text. With the help of Optical Character Recognition (OCR), you can extract any text from a PDF document into a simple text file.

- And it’s simple: just upload your PDF and let us do the rest. After you provided your file, PDF2Go will use OCR to get the text from your PDF and save it as a TXT file.

- ## main.py file contents

![alt text](https://github.com/MohitKumarMandhre/PDF-EXTRACTOR/blob/master/c-main.PNG)


- ## resume PDF Example

![alt text](https://github.com/MohitKumarMandhre/PDF-EXTRACTOR/blob/master/c-cv.PNG)


- ## txt.py file contents which gets extracted from PDF

![alt text](https://github.com/MohitKumarMandhre/PDF-EXTRACTOR/blob/master/c-txt.PNG)

# REQIREMENTS 

- ### pip install PyPDF2

## ABOUT 

- A Pure-Python library built as a PDF toolkit. It is capable of:

extracting document information (title, author, …)
splitting documents page by page
merging documents page by page
cropping pages
merging multiple pages into a single page
encrypting and decrypting PDF files
and more!
By being Pure-Python, it should run on any Python platform without any dependencies on external libraries. It can also work entirely on StringIO objects rather than file streams, allowing for PDF manipulation in memory. It is therefore a useful tool for websites that manage or manipulate PDFs.

- ### The PdfFileReader Class
class PyPDF2.PdfFileReader(stream, strict=True, warndest=None, overwriteWarnings=True)¶
Initializes a PdfFileReader object. This operation can take some time, as the PDF stream’s cross-reference tables are read into memory.

Parameters:	
stream – A File object or an object that supports the standard read and seek methods similar to a File object. Could also be a string representing a path to a PDF file.
strict (bool) – Determines whether user should be warned of all problems and also causes some correctable problems to be fatal. Defaults to True.
warndest – Destination for logging warnings (defaults to sys.stderr).
overwriteWarnings (bool) – Determines whether to override Python’s warnings.py module with a custom implementation (defaults to True).

- ### documentInfo()
- ### getNumPages()
- ### extractText()
