from tkinter import EXCEPTION
from openpyxl import Workbook

EXCEPTION_LIST = [' ', 'AEP-84 Volume II', 'Edition A Version 1']

def write_excel(filepath, text_from_pdf):
    wb = Workbook()
    ws = wb.active

    start_row = 1
    start_col = 1
    buffer = ''

    for page_number, text in enumerate(text_from_pdf):
        for line in text.split('\n'):
            print('line: ', line)
            strip_line = line.strip()
            if (not strip_line in EXCEPTION_LIST) and (not strip_line == ''):
                buffer = buffer + ' ' + strip_line
                ascii = ord(strip_line[0])                
                print('ascii: ', ascii)
                print('type ascii: ', type(ascii))
                if (ascii < 48) and (57 < ascii):
                    print('continue..')
                    continue
                else:
                    ws.cell(row=start_row, column=start_col, value=buffer)
                    start_row += 1
                    buffer = ''

    wb.save(filename=filepath)