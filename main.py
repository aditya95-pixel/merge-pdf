from pypdf import PdfMerger
pdfs = ['file1.pdf','file2.pdf','file3.pdf']
merger = PdfMerger()
for pdf in pdfs:
    merger.append(pdf)
merger.write("result.pdf")
merger.close()