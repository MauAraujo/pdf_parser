#!/usr/bin/env python

from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

file_name = str(sys.argv[1])
pattern =  str(sys.argv[2])
pdf = PdfFileReader(open(file_name, "rb"))

for pageNum in range(0, pdf.numPages):
    page = pdf.getPage(pageNum)
    text = page.extractText()
    print(text.find(pattern))
    #print(page.extractText())
