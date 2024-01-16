from pdf2docx import Converter
import tabula
import PyPDF2
from pdf2image import convert_from_path
import customtkinter
from tkinter import filedialog
import os

pdf_file="pdf-test.pdf"
word_file = "word_test.docx"


class FormatPDF:
    def __init__(self,path, export_file):
        self.path = path
        self.export_file = export_file
    def toDocx(self):
        dc = Converter(self.path)
        dc.convert(self.export_file, start=0, end=None)
        dc.close()


    def toTxt(self):
        pass

    def toJpg(self):
        pass



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


FORMAT_LIST = ("PDF", "DOCX", "TXT", "JPG")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.selected_file = customtkinter.StringVar()

        self.choose_button = customtkinter.CTkButton(self.master, text="Choose File", command=self.choose_file)
        self.choose_button.pack(pady=10)

        self.file_label = customtkinter.CTkLabel(self.master, textvariable=self.selected_file)
        self.file_label.pack(pady=10)


        self.title("Formats Converter")

        self.combofrom = customtkinter.CTkComboBox(self.master, values=FORMAT_LIST, state="readonly")
        self.combofrom.pack(pady=10)

        self.comboto = customtkinter.CTkComboBox(self.master, values=FORMAT_LIST, state="readonly")
        self.comboto.pack(pady=10)

        self.combofrom.bind("<<ComboboxSelected>>", self.on_select)
        self.comboto.bind("<<ComboboxSelected>>", self.on_select)

        self.button = customtkinter.CTkButton(self, text="Convert", command=self.button_callbck)
        self.button.pack(padx=20, pady=20)
    def button_callbck(self):
        print("button clicked")

    def choose_file(self):
        file_path = filedialog.askopenfilename(title="Choose a file", filetypes=[("All Files", "*.*")])
        if file_path:
            self.selected_file.set(file_path)
            file_extension = self.get_file_extension(file_path)
            file_extension = (file_extension.replace(".", "")).upper()
            self.combofrom.set(file_extension)

    def get_file_extension(self, file_path):
        _, file_extension = os.path.splitext(file_path)
        return file_extension

    def on_select(self, event):
        selected_value = self.combo_var.get()
        print(f"Selected: {selected_value}")

    def form_by_default(self):
        pass

    def convert_files(self):

app = App()
app.mainloop()