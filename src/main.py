from pdf2docx import Converter
import tabula
import PyPDF2
from pdf2image import convert_from_path
pdf_file="pdf-test.pdf"
word_file = "word_test.docx"



#converter method
def pdf_to_word():
    dc = Converter(pdf_file)
    dc.convert(word_file, start=0, end=None)
    dc.close()

def pdf_to_csv():
    data=tabula.convert_into("table.pdf","table_new.csv", pages="all",output_format="csv")

def pdf_to_txt():
    # pdf to txt
    pdfFileObj = open("pdf-test.pdf", 'rb')

    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    pageObject = pdfReader.pages[0]
    text = pageObject.extract_text()
    pdfFileObj.close()
    with open("demo.txt", 'w') as file:
        file.write(text)


#popplers to path!
def pdf_to_images():
    images = convert_from_path(pdf_file)
    for i, image in enumerate(images):
        image.save(f"page_{i + 1}.jpg", "JPEG")

