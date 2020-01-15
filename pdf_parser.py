#!/usr/bin/env python

from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

file_name = str(sys.argv[1])
pattern =  str(sys.argv[2])
pdf = PdfFileReader(open(file_name, "rb"))
occurrences = 0
indexes = []

for pageNum in range(0, pdf.numPages):
    page = pdf.getPage(pageNum)
    text = page.extractText()
    count = text.count(pattern)

    if count > 0:
        occurrences += count
        indexes.append(pageNum)

print(occurrences, "ocurrencias del patrón en", pdf.numPages, "páginas")
print(indexes)
