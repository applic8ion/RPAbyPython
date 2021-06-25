from tkinter import *    # __all__

class ExcelToTor():
    def __init__(self, root, statusbar):
        self.text_from_pdf = ''

        # root frame
        self.root = Frame(root)        

        # create excel frame
        self.excel_frame = Frame(self.root)
        self.excel_frame.pack(fill="x", padx=5, pady=5)   # 간격 띄우기

        self.e_filepath_excel = Entry(self.excel_frame)
        self.e_filepath_excel.pack(side="left", fill="both", expand=True)
    
    def pack(self):
        self.root.pack()

    def pack_forget(self):
        self.root.pack_forget()