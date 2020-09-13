import PyPDF2

a = PyPDF2.PdfFileReader('mohit_resSep12.pdf')

print(a.getDocumentInfo())
print(a.getNumPages())


str = ""
n = a.getNumPages()
for i in range(0, n):
    str += a.getPage(0).extractText()
print(str)

with open("text.txt", "w", encoding="utf-8") as f:
    f.write(str)