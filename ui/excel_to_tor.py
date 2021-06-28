from tkinter import *
from apis import file, pdf, excel

LABEL_FILEPATH_WORD = "WORD 저장 경로"
LABEL_FILEPATH_EXCEL = "EXCEL 파일 경로"
FILEPATH_WORD = ''
FILEPATH_EXCEL = ''

def get_filepath(entry: Entry, title:str, filetypes:str):
    filepath = ""
    if entry["text"] == LABEL_FILEPATH_WORD:
        filepath = file.file_picker(title, filetypes)
    elif entry["text"] == LABEL_FILEPATH_EXCEL:
        filepath = file.path_to_save_file(title, filetypes)

    if filepath != '':
        entry.delete(0, END)
        entry.insert(0, filepath)

class ExcelToTor():
    def __init__(self, root, statusbar):
        self.json_from_excel = {}

        # root frame
        self.root = Frame(root)        

        # save word file picker frame
        self.word_frame = Frame(self.root)
        self.word_frame.pack(fill="x", padx=5, pady=5)   # 간격 띄우기

        self.e_filepath_pdf = Entry(self.word_frame)
        self.e_filepath_pdf.pack(side="left", fill="both", expand=True)
        self.e_filepath_pdf.insert(0, FILEPATH_WORD)  # 기본 파일 경로 삽입

        self.btn_filepicker_pdf = Button(\
            self.word_frame, text=LABEL_FILEPATH_WORD, 
            width=6, 
            command=lambda:get_filepath(\
                self.btn_filepicker_pdf, 
                "{} 선택".format(LABEL_FILEPATH_WORD),
                (("WORD", "*.docx"), ("모든 파일", "*.*"))
            )
        )
        self.btn_filepicker_pdf.pack(side="right", fill="both", expand=True)

        # search excel frame
        self.excel_frame = Frame(self.root)
        self.excel_frame.pack(fill="x", padx=5, pady=5)   # 간격 띄우기

        self.e_FILEPATH_WORD = Entry(self.excel_frame)
        self.e_FILEPATH_WORD.pack(side="left", fill="both", expand=True)
        self.e_FILEPATH_WORD.insert(0, FILEPATH_WORD)  # 기본 파일 경로 삽입

        self.btn_filepicker_excel = Button(\
            self.excel_frame, text=LABEL_FILEPATH_EXCEL, 
            width=6, 
            command=lambda:get_filepath(
                self.btn_filepicker_excel,
                "{} 선택".format(LABEL_FILEPATH_EXCEL), 
                (("xlsx", "*.xlsx"), ("xls", "*.xls"), ("모든 파일", "*.*"))
            )
        )
        self.btn_filepicker_excel.pack(side="right", fill="both", expand=True)
    
    def pack(self):
        self.root.pack()

    def pack_forget(self):
        self.root.pack_forget()