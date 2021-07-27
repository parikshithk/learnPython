import PyPDF2 as pypdf

pdfFile = open('/Users/parikshithkulkarni/Downloads/meetingminutes1.pdf', 'rb')

reader = pypdf.PdfFileReader(pdfFile)

print(reader.getNumPages())
print(reader.getPage(0).extractText())

newPdf = open('new.pdf', 'wb')

writer = pypdf.PdfFileWriter()

writer.addPage(reader.getPage(0))
writer.write(newPdf)

pdfFile.close()
newPdf.close()
