# Merge Pdfs
this program is used to merge several pdfs into one pdf using the concept of file concatenation.
- We import the PdfMerger class from pypdf library, which is designed for merging PDF files.
- We create a list of paths of the PDF files that we want to merge.
- An object of PdfMerger class is created.
- We append all the pdfs to the merger object.
- `merger.write("result.pdf")` writes the merged content to a new file called `result.pdf`.
- merger.close() is called to clean up resources after the merge is complete.
