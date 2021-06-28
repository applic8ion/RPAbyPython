from tkinter import *    # __all__
from tkinter import ttk
from ui.pdf_to_excel import PdfToExcel
from ui.excel_to_tor import ExcelToTor
from enum import Enum

class Mode(Enum):
    PDF_TO_EXCEL = 0
    EXCEL_TO_TOR = 1

MODE_LABEL_LIST = [
    "1. PDF to Excel",
    "2. Excel to TOR"
]

def check_tool():
    if var_tools.get() == Mode.PDF_TO_EXCEL.value:        
        pdf_to_excel.pack()
        excel_to_tor.pack_forget()
    elif var_tools.get() == Mode.EXCEL_TO_TOR.value:        
        excel_to_tor.pack()
        pdf_to_excel.pack_forget()

root = Tk()
root.title("RPA for SWPart")

menu = Menu(root)

# File menu
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

# Tools Menu
var_tools = IntVar()
var_tools.set(0)
menu_tools = Menu(menu, tearoff=0)
for i in range(len(MODE_LABEL_LIST)):    
    menu_tools.add_radiobutton(label=MODE_LABEL_LIST[i], value=i, variable=var_tools, command=check_tool)
menu.add_cascade(label="Tools", menu=menu_tools)

# Status bar
statusbar = Label(root, text="", bd=1, relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

# Progress bar
p_var = DoubleVar()    # 실수 반영을 위해 Double
progressbar = ttk.Progressbar(root, maximum=100, variable=p_var)
progressbar.pack(side=BOTTOM, fill=X)

pdf_to_excel = PdfToExcel(root, statusbar)
excel_to_tor = ExcelToTor(root, statusbar)
pdf_to_excel.pack()     # 기본 모드

root.resizable(False, False)
root.config(menu=menu)
root.mainloop()