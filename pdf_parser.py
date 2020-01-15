#!/usr/bin/env python

from PyPDF2 import PdfFileWriter, PdfFileReader

pdf = PdfFileReader(open("test.pdf", "rb"))


for pageNum in range(0, pdf.numPages):
    page = pdf.getPage(pageNum)
    print(page.extractText())
