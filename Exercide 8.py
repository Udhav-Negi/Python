import pypdf
import os 
pdfList = os.listdir('./PDF')
pdfList.sort()

merger = pypdf.PdfWriter()

for pdf in pdfList:
    merger.append(f"./PDF/{pdf}")

merger.write("./PDF/merged-pdf.pdf")
merger.close()