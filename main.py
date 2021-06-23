from tkinter import *   # __all__
from apis import file, pdf, excel

FILEPATH_PDF = 'C:/Users/user/Downloads/AEP-84 VOLII EDA V1 E.pdf'
FILEPATH_EXCEL = 'D:/04_genaral/02_Project/04_python_apps/RPAforSW/test.xlsx'
DEFAULT_PAGE_FROM = "40"
DEFAULT_PAGE_TO = "40"

def get_filepath(entry: Entry, title:str, filetypes:str):
    if entry == e_filepath_pdf:
        filepath = file.file_picker(title, filetypes)
    elif entry == e_filepath_excel:
        filepath = file.path_to_save_file(title, filetypes)

    if filepath != '':
        entry.delete(0, END)
        entry.insert(0, filepath)

def export_text_to_excel():
    global text_from_pdf
    text_from_pdf = pdf.get_text_from_pdf(e_filepath_pdf.get(), int(e_page_from.get()), int(e_page_to.get()))
    # excel.write_excel(e_filepath_excel.get(), data)

root = Tk()
root.title("RPA for SWPart")

# create excel frame
excel_frame = Frame(root)
excel_frame.pack(fill="x", padx=5, pady=5)   # 간격 띄우기

e_filepath_excel = Entry(excel_frame)
e_filepath_excel.pack(side="left")
e_filepath_excel.insert(0, FILEPATH_EXCEL)  # 기본 파일 경로 삽입

btn_filepicker_excel = Button(excel_frame, text="엑셀저장경로", command=lambda:get_filepath(e_filepath_excel, "Excel 저장 경로 선택", (("xlsx", "*.xlsx"), ("xls", "*.xls"), ("모든 파일", "*.*"))))
btn_filepicker_excel.pack(side="right")

# file picker frame
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)   # 간격 띄우기

e_filepath_pdf = Entry(file_frame)
e_filepath_pdf.pack(side="left")
e_filepath_pdf.insert(0, FILEPATH_PDF)  # 기본 파일 경로 삽입

btn_filepicker_pdf = Button(file_frame, text="PDF경로", command=lambda:get_filepath(e_filepath_pdf, "PDF 파일 선택", (("PDF", "*.pdf"), ("모든 파일", "*.*"))))
btn_filepicker_pdf.pack(side="right")

# pdf page label frame
page_range_label_frame = Frame(root)
page_range_label_frame.pack(fill="both", padx=5, pady=5)

label_page_from = Label(page_range_label_frame, text="시작 페이지")
label_page_from.pack(side="left")
label_page_to = Label(page_range_label_frame, text="종료 페이지")
label_page_to.pack(side="right")

# pdf page number frame
page_range_frame = Frame(root)
page_range_frame.pack(fill="both", padx=5, pady=5)

e_page_from = Entry(page_range_frame)
e_page_from.pack(side="left")
e_page_from.insert(0, DEFAULT_PAGE_FROM)

e_page_to = Entry(page_range_frame)
e_page_to.pack(side="right")
e_page_to.insert(0, DEFAULT_PAGE_TO)


# command frame
command_frame = Frame(root)
command_frame.pack(fill="both", padx=5, pady=5)
btn_export_text_to_excel = Button(command_frame, text="PDF 텍스트 추출", command=export_text_to_excel)
btn_export_text_to_excel.pack(fill="both")

btn_text_to_excel = Button(command_frame, text="엑셀에 텍스트 저장", command=lambda:excel.write_excel(e_filepath_excel.get(), text_from_pdf))
btn_text_to_excel.pack(fill="both")

root.resizable(False, False)
root.mainloop()