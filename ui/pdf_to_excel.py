from tkinter import *    # __all__
from apis import file, pdf, excel

# FILEPATH_PDF = ''
# FILEPATH_EXCEL = ''
FILEPATH_PDF = 'C:/Users/user/Downloads/AEP-84 VOLII EDA V1 E.pdf'
FILEPATH_EXCEL = 'D:/04_genaral/02_Project/04_python_apps/RPAforSW/test.xlsx'
# FILEPATH_PDF = 'C:/Users/TAEWON/Downloads/EN-SCI-271-03.pdf'
# FILEPATH_EXCEL = 'C:/Users/TAEWON/OneDrive/문서/01_projects/RPAbyPython/test.xlsx'
DEFAULT_PAGE_FROM = "40"
DEFAULT_PAGE_TO = "40"
LABEL_FILEPATH_PDF = "PDF 파일 경로"
LABEL_FILEPATH_EXCEL = "EXCEL 저장 경로"

def get_filepath(button:Button, entry: Entry, title:str, filetypes:str):
    filepath = ""
    if button["text"] == LABEL_FILEPATH_PDF:
        filepath = file.file_picker(title, filetypes)
    elif button["text"] == LABEL_FILEPATH_EXCEL:
        filepath = file.path_to_save_file(title, filetypes)

    if filepath != '':
        entry.delete(0, END)
        entry.insert(0, filepath)

def extract_text_from_pdf(filepath_pdf:str, filepath_excel:str, page_from:str, page_to:str, text_from_pdf:str, statusbar):
    if filepath_pdf == '':
        statusbar.config(text="[ERR]PDF 경로를 설정하십시오.")
        return
    elif page_from == '':
        statusbar.config(text="[ERR]시작 페이지를 설정하십시오.")
        return
    elif page_to == '':
        statusbar.config(text="[ERR]종료 페이지를 설정하십시오.")
        return    

    text_from_pdf = pdf.get_text_from_pdf(filepath_pdf, int(page_from), int(page_to))
    write_text_to_excel(filepath_excel, text_from_pdf, statusbar)
    # excel.write_excel(e_filepath_excel.get(), text_from_pdf.text_from_pdf)
    

def write_text_to_excel(filepath_excel, text_from_pdf, statusbar):
    if filepath_excel == '':
        statusbar.config(text="[ERR]EXCEL 저장 경로를 설정하십시오.")
        return
    elif text_from_pdf == '':
        statusbar.config(text="[ERR]PDF 텍스트 추출을 클릭하십시오.")
        return

    excel.write_excel(filepath_excel, text_from_pdf)
    statusbar.config(text="PDF to Excel 완료")

class PdfToExcel():
    def __init__(self, root, statusbar):
        self.text_from_pdf = ''

        # root frame
        self.root = Frame(root)        

        # create excel frame
        self.excel_frame = Frame(self.root)
        self.excel_frame.pack(fill="x", padx=5, pady=5)   # 간격 띄우기

        self.e_filepath_excel = Entry(self.excel_frame)
        self.e_filepath_excel.pack(side="left", fill="both", expand=True)
        self.e_filepath_excel.insert(0, FILEPATH_EXCEL)  # 기본 파일 경로 삽입

        self.btn_filepicker_excel = Button(\
            self.excel_frame, 
            text=LABEL_FILEPATH_EXCEL, 
            width=6, 
            command=lambda:get_filepath(\
                self.btn_filepicker_excel,
                self.e_filepath_excel, 
                "Excel 저장 경로 선택", 
                (("xlsx", "*.xlsx"), ("xls", "*.xls"), ("모든 파일", "*.*"))
            )
        )
        self.btn_filepicker_excel.pack(side="right", fill="both", expand=True)

        # file picker frame
        self.file_frame = Frame(self.root)
        self.file_frame.pack(fill="x", padx=5, pady=5)   # 간격 띄우기

        self.e_filepath_pdf = Entry(self.file_frame)
        self.e_filepath_pdf.pack(side="left", fill="both", expand=True)
        self.e_filepath_pdf.insert(0, FILEPATH_PDF)  # 기본 파일 경로 삽입

        self.btn_filepicker_pdf = Button(\
            self.file_frame, text=LABEL_FILEPATH_PDF, 
            width=6, 
            command=lambda:get_filepath(\
                self.btn_filepicker_pdf,
                self.e_filepath_pdf, 
                "PDF 파일 선택", 
                (("PDF", "*.pdf"), ("모든 파일", "*.*"))
            )
        )
        self.btn_filepicker_pdf.pack(side="right", fill="both", expand=True)

        # pdf page label frame
        self.page_range_label_frame = Frame(self.root)
        self.page_range_label_frame.pack(fill="both", padx=5, pady=5)

        self.label_page_from = Label(self.page_range_label_frame, text="시작 페이지")
        self.label_page_from.pack(side="left", fill="both", expand=True)
        self.label_page_to = Label(self.page_range_label_frame, text="종료 페이지")
        self.label_page_to.pack(side="right", fill="both", expand=True)

        # pdf page number frame
        self.page_range_frame = Frame(self.root)
        self.page_range_frame.pack(fill="both", padx=5, pady=5)
        
        self.e_page_from = Entry(self.page_range_frame)
        self.e_page_from.pack(side="left")
        self.e_page_from.insert(0, DEFAULT_PAGE_FROM)
        
        self.e_page_to = Entry(self.page_range_frame)
        self.e_page_to.pack(side="right")
        self.e_page_to.insert(0, DEFAULT_PAGE_TO)

        # command frame
        self.command_frame = Frame(self.root)
        self.command_frame.pack(fill="both", padx=5, pady=5)
        
        self.btn_export_text_to_excel = Button(\
            self.command_frame, text="Run PDF to Excel",\
            command=lambda:extract_text_from_pdf(
                self.e_filepath_pdf.get(),
                self.e_filepath_excel.get(),
                self.e_page_from.get(),
                self.e_page_to.get(),
                self.text_from_pdf, statusbar
            ))
        self.btn_export_text_to_excel.pack(fill="both")
    
    def pack(self):
        self.root.pack()

    def pack_forget(self):
        self.root.pack_forget()