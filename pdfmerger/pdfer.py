import PyPDF2
import sys

def pdfRotator():
    with open("twopage.pdf","rb") as file:
        reader = PyPDF2.PdfReader(file)
        page = reader.pages[0]
        page.rotate(90)
        writer = PyPDF2.PdfWriter()
        writer.add_page(page)
        with open("tilt.pdf","wb") as new_file:
            writer.write(new_file)


inputs = sys.argv[1:]

def pdfCombiner(pdf_list):
    merger = PyPDF2.PdfMerger()
    for f in pdf_list:
        merger.append(f)
    merger.write("super.pdf")
pdfCombiner(inputs)