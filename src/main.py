from pdf2docx import Converter
import tabula


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
    pass













